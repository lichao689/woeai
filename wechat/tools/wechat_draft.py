#!/usr/bin/env python3
"""Create or update WeChat Official Account drafts for WOEAI articles.

The CLI keeps secrets outside the repository, prints only safe status, and
defaults to dry-run behavior. Live draft creation/update is intentionally a
separate explicit subcommand.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import ipaddress
import json
import mimetypes
import os
import re
import secrets
import stat
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


WECHAT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = WECHAT_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from woeai.wechat.backlog import (  # noqa: E402,F401
    BacklogPaper,
    parse_backlog_papers,
    rank_against_target,
    read_backlog_item,
    read_backlog_publication_refs,
)
from woeai.wechat.options import (  # noqa: E402,F401
    AVAILABLE_MATH_RENDERERS,
    AVAILABLE_THEMES,
    DEFAULT_MATH_RENDERER,
    DEFAULT_THEME,
    validate_math_renderer,
    validate_theme,
)
from woeai.wechat.review import (  # noqa: E402,F401
    find_review_cover,
    parse_front_matter,
    parse_title as parse_title_text,
)

CONFIG_PATH = Path.home() / ".config/woeai/wechat_official_account.env"
RUNNER_CONFIG_PATH = Path.home() / ".config/woeai/wechat_runner.env"
TOKEN_CACHE_PATH = Path.home() / ".cache/woeai/wechat_access_token.json"
DEFAULT_REF = "ref-zhao2026-BS"
RTD_BASE_URL = "https://woeai.readthedocs.io/zh-cn/latest/"
EXPECTED_EGRESS_IPS_KEY = "WOEAI_WECHAT_EXPECTED_EGRESS_IPS"

TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token"
UPLOAD_BODY_IMAGE_URL = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
UPLOAD_PERMANENT_MATERIAL_URL = "https://api.weixin.qq.com/cgi-bin/material/add_material"
DRAFT_GET_URL = "https://api.weixin.qq.com/cgi-bin/draft/get"
DRAFT_ADD_URL = "https://api.weixin.qq.com/cgi-bin/draft/add"
DRAFT_UPDATE_URL = "https://api.weixin.qq.com/cgi-bin/draft/update"
PUBLIC_IP_ENDPOINTS = (
    ("https://api.ipify.org?format=json", "json_ip"),
    ("https://ifconfig.me/ip", "plain_text"),
    ("https://icanhazip.com", "plain_text"),
)


@dataclass(frozen=True)
class ImageRef:
    alt: str
    raw_src: str
    path: Path


@dataclass(frozen=True)
class ArticleContext:
    publication_ref: str
    article_path: Path
    review_path: Path
    backlog_path: Path
    title: str
    author: str
    digest: str
    content_source_url: str
    cover_path: Path
    body_images: list[ImageRef]
    action: str
    existing_media_id: str
    theme: str
    math_renderer: str


class WeChatError(RuntimeError):
    def __init__(self, stage: str, payload: dict[str, Any]):
        self.stage = stage
        self.payload = payload
        super().__init__(f"{stage}: {payload}")


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def load_renderer() -> Any:
    renderer_path = WECHAT_ROOT / "tools/render-copy-ready.py"
    spec = importlib.util.spec_from_file_location("woeai_wechat_render_copy_ready", renderer_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load renderer: {renderer_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_public_safety_checker() -> Any:
    checker_path = REPO_ROOT / "scripts/check-public-safe-content.py"
    spec = importlib.util.spec_from_file_location("woeai_check_public_safe_content", checker_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load public-safety checker: {checker_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "collect_findings"):
        raise RuntimeError(f"Public-safety checker has no collect_findings(): {checker_path}")
    return module


def parse_env_file(path: Path, *, required: bool) -> dict[str, str]:
    if not path.exists():
        if required:
            raise RuntimeError(f"Missing configuration file: {path}")
        return {}
    values: dict[str, str] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise RuntimeError(f"Configuration file {path} line {lineno} is missing '='")
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def load_env(path: Path = CONFIG_PATH) -> dict[str, str]:
    return parse_env_file(path, required=True)


def load_runner_config(path: Path = RUNNER_CONFIG_PATH) -> dict[str, str]:
    return parse_env_file(path, required=False)


def split_ip_list(raw_values: list[str]) -> list[str]:
    ips: list[str] = []
    for raw in raw_values:
        for value in re.split(r"[\s,;]+", raw.strip()):
            if not value:
                continue
            try:
                ips.append(str(ipaddress.ip_address(value)))
            except ValueError as exc:
                raise RuntimeError(f"Invalid expected egress IP: {value}") from exc
    return ips


def expected_egress_ips(args: argparse.Namespace | None = None) -> tuple[list[str], list[str]]:
    raw_values: list[str] = []
    sources: list[str] = []
    if args is not None:
        for value in getattr(args, "expected_ip", None) or []:
            raw_values.append(value)
            sources.append("argument")

    env_value = os.environ.get(EXPECTED_EGRESS_IPS_KEY, "")
    if env_value:
        raw_values.append(env_value)
        sources.append("environment")

    runner_config = load_runner_config()
    config_value = runner_config.get(EXPECTED_EGRESS_IPS_KEY, "")
    if config_value:
        raw_values.append(config_value)
        sources.append(str(RUNNER_CONFIG_PATH))

    ips = split_ip_list(raw_values)
    deduped_ips = list(dict.fromkeys(ips))
    return deduped_ips, sources


def extract_public_ip(body: str, mode: str) -> str:
    value = ""
    if mode == "json_ip":
        try:
            payload = json.loads(body)
            value = str(payload.get("ip", "")).strip()
        except json.JSONDecodeError:
            value = ""
    else:
        value = body.strip().splitlines()[0].strip() if body.strip() else ""
    if not value:
        return ""
    try:
        return str(ipaddress.ip_address(value))
    except ValueError:
        return ""


def fetch_public_ip() -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    for endpoint, mode in PUBLIC_IP_ENDPOINTS:
        try:
            req = Request(endpoint, headers={"User-Agent": "WOEAI-WeChat-Draft-Tool/0.1"})
            with urlopen(req, timeout=12) as resp:
                body = resp.read(256).decode("utf-8", errors="replace")
            public_ip = extract_public_ip(body, mode)
            attempts.append({"endpoint": endpoint, "ok": bool(public_ip), "ip": public_ip})
            if public_ip:
                return {
                    "ok": True,
                    "current_ip": public_ip,
                    "source": endpoint,
                    "checked_at": datetime.now().astimezone().isoformat(timespec="seconds"),
                    "attempts": attempts,
                }
        except Exception as exc:  # network diagnostics only; safe to summarize.
            attempts.append(
                {
                    "endpoint": endpoint,
                    "ok": False,
                    "error_type": type(exc).__name__,
                    "message": str(exc),
                }
            )
    return {
        "ok": False,
        "current_ip": "",
        "source": "",
        "checked_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "attempts": attempts,
    }


def egress_ip_summary(args: argparse.Namespace | None = None, *, require_expected_ip: bool) -> dict[str, Any]:
    expected_ips, expected_sources = expected_egress_ips(args)
    current = fetch_public_ip()
    current_ip = str(current.get("current_ip", ""))
    matched = bool(current_ip and current_ip in expected_ips)
    expected_configured = bool(expected_ips)
    ok = bool(current.get("ok")) and (matched if expected_configured else not require_expected_ip)
    if not current.get("ok"):
        message = "无法获取当前公网出口 IP；未读取微信凭据，也未联系微信 API。"
    elif not expected_configured:
        message = (
            f"当前公网出口 IP 是 {current_ip}，但还没有配置固定出口 IP。"
            if require_expected_ip
            else f"当前公网出口 IP 是 {current_ip}；未配置固定出口 IP，仅供查看。"
        )
    elif matched:
        message = f"当前公网出口 IP 是 {current_ip}，已匹配配置的固定 IP。"
    else:
        message = f"当前公网出口 IP 是 {current_ip}，不在配置的固定 IP 列表中。"
    return {
        "ok": ok,
        "stage": "egress_ip_check",
        "current_ip": current_ip,
        "ip_source": current.get("source", ""),
        "checked_at": current.get("checked_at", ""),
        "expected_ip_configured": expected_configured,
        "expected_ips": expected_ips,
        "expected_ip_sources": expected_sources,
        "matched_expected_ip": matched,
        "runner_config_path": str(RUNNER_CONFIG_PATH),
        "message": message,
        "will_read_credentials": False,
        "will_contact_wechat": False,
        "will_create_or_update_draft": False,
        "attempts": current.get("attempts", []),
    }


def credential_status(path: Path = CONFIG_PATH) -> dict[str, Any]:
    status: dict[str, Any] = {
        "file_exists": path.exists(),
        "mode_octal": None,
        "app_id_present": False,
        "app_id_starts_with_wx": False,
        "app_id_length": 0,
        "app_secret_present": False,
        "app_secret_length": 0,
        "unknown_keys": [],
        "format_errors": [],
    }
    if not path.exists():
        return status
    status["mode_octal"] = oct(stat.S_IMODE(path.stat().st_mode))
    values: dict[str, str] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            status["format_errors"].append(f"line {lineno}: missing =")
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        values[key] = value
        if key not in {"WECHAT_OFFICIAL_ACCOUNT_APP_ID", "WECHAT_OFFICIAL_ACCOUNT_APP_SECRET"}:
            status["unknown_keys"].append(key)
    appid = values.get("WECHAT_OFFICIAL_ACCOUNT_APP_ID", "")
    secret = values.get("WECHAT_OFFICIAL_ACCOUNT_APP_SECRET", "")
    status["app_id_present"] = bool(appid)
    status["app_id_starts_with_wx"] = appid.startswith("wx")
    status["app_id_length"] = len(appid)
    status["app_secret_present"] = bool(secret)
    status["app_secret_length"] = len(secret)
    return status


def api_get_json(url: str, params: dict[str, str]) -> dict[str, Any]:
    request_url = f"{url}?{urlencode(params)}"
    req = Request(request_url, headers={"User-Agent": "WOEAI-WeChat-Draft-Tool/0.1"})
    with urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
    return json.loads(body)


def api_post_json(url: str, token: str, payload: dict[str, Any]) -> dict[str, Any]:
    request_url = f"{url}?{urlencode({'access_token': token})}"
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = Request(
        request_url,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "WOEAI-WeChat-Draft-Tool/0.1",
        },
        method="POST",
    )
    with urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
    return json.loads(body)


def api_post_multipart(url: str, token: str, file_path: Path, extra_params: dict[str, str]) -> dict[str, Any]:
    request_url = f"{url}?{urlencode({'access_token': token, **extra_params})}"
    boundary = "----woeai-wechat-" + secrets.token_hex(12)
    mime = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    head = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{file_path.name}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode("utf-8")
    tail = f"\r\n--{boundary}--\r\n".encode("utf-8")
    data = head + file_path.read_bytes() + tail
    req = Request(
        request_url,
        data=data,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "WOEAI-WeChat-Draft-Tool/0.1",
        },
        method="POST",
    )
    with urlopen(req, timeout=90) as resp:
        body = resp.read().decode("utf-8")
    return json.loads(body)


def fetch_access_token(force_refresh: bool = False) -> dict[str, Any]:
    now = int(time.time())
    if not force_refresh and TOKEN_CACHE_PATH.exists():
        try:
            cached = json.loads(TOKEN_CACHE_PATH.read_text(encoding="utf-8"))
            if cached.get("access_token") and int(cached.get("expires_at", 0)) > now:
                return {**cached, "from_cache": True}
        except (json.JSONDecodeError, OSError, ValueError):
            pass

    values = load_env()
    appid = values.get("WECHAT_OFFICIAL_ACCOUNT_APP_ID", "")
    secret = values.get("WECHAT_OFFICIAL_ACCOUNT_APP_SECRET", "")
    if not appid or not secret:
        raise RuntimeError("Missing WECHAT_OFFICIAL_ACCOUNT_APP_ID or WECHAT_OFFICIAL_ACCOUNT_APP_SECRET")

    data = api_get_json(
        TOKEN_URL,
        {"grant_type": "client_credential", "appid": appid, "secret": secret},
    )
    if "access_token" not in data:
        raise WeChatError("fetch_access_token", data)

    expires_in = int(data.get("expires_in", 7200))
    record = {
        "access_token": data["access_token"],
        "expires_in": expires_in,
        "fetched_at": now,
        "fetched_at_iso": datetime.now(timezone.utc).isoformat(),
        "expires_at": now + max(0, expires_in - 300),
    }
    TOKEN_CACHE_PATH.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    tmp_path = TOKEN_CACHE_PATH.with_suffix(".tmp")
    tmp_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(tmp_path, 0o600)
    tmp_path.replace(TOKEN_CACHE_PATH)
    os.chmod(TOKEN_CACHE_PATH, 0o600)
    return {**record, "from_cache": False}


def parse_cover_path(review_path: Path) -> Path:
    # WeChat drafts require a cover; find_review_cover returns None when
    # absent, so surface that as an error here.
    cover = find_review_cover(review_path)
    if cover is None:
        raise RuntimeError(f"Cannot find cover image in {repo_relative(review_path)}")
    return cover


def parse_markdown_images(article_path: Path) -> list[ImageRef]:
    images: list[ImageRef] = []
    for raw in article_path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"!\[(.*?)\]\((.*?)\)", raw.strip())
        if not match:
            continue
        alt, src = match.groups()
        path = (article_path.parent / src).resolve()
        images.append(ImageRef(alt=alt, raw_src=src, path=path))
    return images


def parse_title(article_path: Path) -> str:
    # Path-based convenience wrapper over the pure parse_title_text.
    return parse_title_text(article_path.read_text(encoding="utf-8"))


def text_without_markup(markdown: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", markdown)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"</?u>", "", text)
    text = re.sub(r"[*_`#>$]", "", text)
    text = text.replace(r"\*", "*")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_first_paper_author(article_path: Path) -> str:
    for raw in article_path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*-\s+作者:\s*(.+)", raw)
        if not match:
            continue
        first = match.group(1).split(";", 1)[0].strip()
        first = re.sub(r"</?u>", "", first)
        first = re.sub(r"\*\*(.+?)\*\*", r"\1", first)
        first = first.replace(r"\*", "").replace("*", "")
        return re.sub(r"\s+", " ", first).strip()
    return ""


def parse_digest(article_path: Path, limit: int = 120) -> str:
    lines = article_path.read_text(encoding="utf-8").splitlines()
    paragraphs: list[str] = []
    current: list[str] = []
    for raw in lines[1:]:
        stripped = raw.strip()
        if not stripped:
            if current:
                paragraphs.append(text_without_markup(" ".join(current)))
                current = []
            continue
        if stripped.startswith("#") or stripped.startswith("!") or stripped.startswith("- "):
            if current:
                paragraphs.append(text_without_markup(" ".join(current)))
                current = []
            continue
        current.append(stripped)
        if paragraphs:
            break
    if current:
        paragraphs.append(text_without_markup(" ".join(current)))
    digest = next((p for p in paragraphs if p), "")
    return digest[:limit]


def image_dimensions(path: Path) -> tuple[int | None, int | None]:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data.startswith(b"\xff\xd8"):
        idx = 2
        while idx + 9 < len(data):
            if data[idx] != 0xFF:
                idx += 1
                continue
            marker = data[idx + 1]
            idx += 2
            if marker in {0xD8, 0xD9}:
                continue
            length = int.from_bytes(data[idx : idx + 2], "big")
            if 0xC0 <= marker <= 0xC3 and idx + 7 < len(data):
                height = int.from_bytes(data[idx + 3 : idx + 5], "big")
                width = int.from_bytes(data[idx + 5 : idx + 7], "big")
                return width, height
            idx += length
    return None, None


def rtd_paper_note_url(publication_ref: str) -> str:
    return f"{RTD_BASE_URL}paper-notes/{publication_ref}.html"


def resolve_content_source_url(publication_ref: str, front: dict[str, str]) -> str:
    if "wechat_content_source_url" in front:
        return front["wechat_content_source_url"].strip()
    return rtd_paper_note_url(publication_ref)


def article_title_for_ref(publication_ref: str, fallback: str = "") -> str:
    article_path = WECHAT_ROOT / f"articles/draft-public-safe/{publication_ref}.md"
    if article_path.exists():
        try:
            return parse_title(article_path)
        except RuntimeError:
            pass
    return fallback or publication_ref


def related_backlog_papers(
    publication_ref: str,
    *,
    require_wechat_url: bool = False,
    require_rtd_page: bool = False,
    limit: int = 3,
) -> list[BacklogPaper]:
    backlog_path = WECHAT_ROOT / "backlog/selected-papers.yml"
    papers = parse_backlog_papers(backlog_path)
    target = next((paper for paper in papers if paper.publication_ref == publication_ref), None)
    if target is None:
        return []

    candidates: list[BacklogPaper] = []
    for paper in papers:
        if paper.publication_ref == publication_ref:
            continue
        if paper.research_family != target.research_family:
            continue
        if require_wechat_url and not paper.latest_published_url:
            continue
        if require_rtd_page and not (REPO_ROOT / f"docs/source/paper-notes/{paper.publication_ref}.rst").exists():
            continue
        candidates.append(paper)
    return sorted(candidates, key=lambda p: rank_against_target(p, target))[:limit]


def related_wechat_links(publication_ref: str, *, limit: int = 3) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for paper in related_backlog_papers(publication_ref, require_wechat_url=True, limit=limit):
        links.append(
            {
                "publication_ref": paper.publication_ref,
                "title": article_title_for_ref(paper.publication_ref, paper.title),
                "url": paper.latest_published_url,
            }
        )
    return links


def escape_markdown_link_label(value: str) -> str:
    return value.replace("[", r"\[").replace("]", r"\]")


def append_wechat_related_navigation(markdown_text: str, links: list[dict[str, str]]) -> str:
    if not links or "## 相关论文导航" in markdown_text:
        return markdown_text
    lines = ["", "## 相关论文导航", ""]
    for link in links:
        lines.append(f"- [{escape_markdown_link_label(link['title'])}]({link['url']})")
    return markdown_text.rstrip() + "\n" + "\n".join(lines) + "\n"


def planned_content_source_items(publication_refs: list[str]) -> list[dict[str, Any]]:
    backlog_path = WECHAT_ROOT / "backlog/selected-papers.yml"
    items: list[dict[str, Any]] = []
    for publication_ref in publication_refs:
        review_path = WECHAT_ROOT / f"articles/review/{publication_ref}.review.md"
        article_path = WECHAT_ROOT / f"articles/draft-public-safe/{publication_ref}.md"
        front = parse_front_matter(review_path) if review_path.exists() else {}
        backlog_item = read_backlog_item(backlog_path, publication_ref)
        has_override = "wechat_content_source_url" in front
        expected_url = resolve_content_source_url(publication_ref, front)
        items.append(
            {
                "publication_ref": publication_ref,
                "title": article_title_for_ref(publication_ref, backlog_item.get("title", "")),
                "article_exists": article_path.exists(),
                "review_exists": review_path.exists(),
                "rtd_page_exists": (REPO_ROOT / f"docs/source/paper-notes/{publication_ref}.rst").exists(),
                "wechat_draft_media_id": backlog_item.get("wechat_draft_media_id", ""),
                "content_source_url_policy": "review_override" if has_override else "default_rtd_paper_note",
                "expected_content_source_url": expected_url,
                "default_rtd_paper_note_url": rtd_paper_note_url(publication_ref),
            }
        )
    return items


def update_backlog_after_success(backlog_path: Path, publication_ref: str, media_id: str, action: str) -> None:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = backlog_path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    in_item = False
    seen: set[str] = set()
    indent = "    "

    updates = {
        "wechat_status": "ready_to_publish",
        "wechat_draft_media_id": media_id,
        "wechat_draft_updated_at": now,
    }
    if action == "create":
        updates["wechat_draft_created_at"] = now

    for raw in lines:
        if re.match(r"\s*-\s+publication_ref:\s+" + re.escape(publication_ref) + r"\s*$", raw):
            in_item = True
            out.append(raw)
            continue
        if in_item and re.match(r"\s*-\s+publication_ref:\s+", raw):
            for key, value in updates.items():
                if key not in seen:
                    out.append(f"{indent}{key}: {value}")
            in_item = False
            seen.clear()
            out.append(raw)
            continue
        if in_item and ":" in raw:
            key = raw.split(":", 1)[0].strip()
            if key in updates:
                out.append(f"{indent}{key}: {updates[key]}")
                seen.add(key)
                continue
        out.append(raw)

    if in_item:
        for key, value in updates.items():
            if key not in seen:
                out.append(f"{indent}{key}: {value}")

    backlog_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def build_context(
    publication_ref: str,
    theme: str = DEFAULT_THEME,
    math_renderer: str = DEFAULT_MATH_RENDERER,
) -> ArticleContext:
    theme = validate_theme(theme)
    math_renderer = validate_math_renderer(math_renderer)
    article_path = WECHAT_ROOT / f"articles/draft-public-safe/{publication_ref}.md"
    review_path = WECHAT_ROOT / f"articles/review/{publication_ref}.review.md"
    backlog_path = WECHAT_ROOT / "backlog/selected-papers.yml"
    if not article_path.exists():
        raise RuntimeError(f"Missing article: {repo_relative(article_path)}")
    if not review_path.exists():
        raise RuntimeError(f"Missing review note: {repo_relative(review_path)}")
    front = parse_front_matter(review_path)
    if front.get("body_images_upload_approved", "").lower() != "true":
        raise RuntimeError("Review note has not approved body image upload")
    first_author = parse_first_paper_author(article_path)
    front_author = front.get("wechat_author", "")
    author = first_author if front_author == "WOEAI" and first_author else front_author or first_author or "WOEAI"
    content_source_url = resolve_content_source_url(publication_ref, front)
    cover_path = parse_cover_path(review_path)
    body_images = parse_markdown_images(article_path)
    backlog_item = read_backlog_item(backlog_path, publication_ref)
    existing_media_id = backlog_item.get("wechat_draft_media_id", "")
    return ArticleContext(
        publication_ref=publication_ref,
        article_path=article_path.resolve(),
        review_path=review_path.resolve(),
        backlog_path=backlog_path.resolve(),
        title=parse_title(article_path),
        author=author,
        digest=parse_digest(article_path),
        content_source_url=content_source_url,
        cover_path=cover_path,
        body_images=body_images,
        action="update" if existing_media_id else "create",
        existing_media_id=existing_media_id,
        theme=theme,
        math_renderer=math_renderer,
    )


def validate_context(ctx: ArticleContext) -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    for label, path in [("article", ctx.article_path), ("review", ctx.review_path), ("cover", ctx.cover_path)]:
        if not path.exists():
            problems.append({"kind": "missing_file", "label": label, "path": repo_relative(path)})
    for image in ctx.body_images:
        if not image.path.exists():
            problems.append({"kind": "missing_image", "alt": image.alt, "path": repo_relative(image.path)})
    try:
        checker = load_public_safety_checker()
        findings = checker.collect_findings([ctx.article_path, ctx.review_path])
        for finding in findings:
            problems.append({"kind": "public_safety", "message": finding})
    except Exception as exc:
        problems.append(
            {
                "kind": "public_safety_check_error",
                "error_type": type(exc).__name__,
                "message": str(exc),
            }
        )
    return problems


def file_summary(path: Path) -> dict[str, Any]:
    width, height = image_dimensions(path) if path.exists() else (None, None)
    return {
        "path": repo_relative(path),
        "exists": path.exists(),
        "bytes": path.stat().st_size if path.exists() else 0,
        "sha256_12": hashlib.sha256(path.read_bytes()).hexdigest()[:12] if path.exists() else "",
        "width": width,
        "height": height,
    }


def markdown_with_uploaded_urls(ctx: ArticleContext, image_url_map: dict[str, str]) -> Path:
    text = ctx.article_path.read_text(encoding="utf-8")
    for image in ctx.body_images:
        url = image_url_map[image.raw_src]
        text = text.replace(f"]({image.raw_src})", f"]({url})")
    text = append_wechat_related_navigation(text, related_wechat_links(ctx.publication_ref))
    tmp = tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        suffix=f".{ctx.publication_ref}.wechat-uploaded.md",
        delete=False,
    )
    with tmp:
        tmp.write(text)
    return Path(tmp.name)


def render_wechat_html(ctx: ArticleContext, image_url_map: dict[str, str]) -> str:
    renderer = load_renderer()
    if hasattr(renderer, "validate_theme"):
        renderer.validate_theme(ctx.theme)
    if hasattr(renderer, "validate_math_renderer"):
        renderer.validate_math_renderer(ctx.math_renderer)
    temp_md = markdown_with_uploaded_urls(ctx, image_url_map)
    try:
        return renderer.render_markdown(
            temp_md,
            embed_images=False,
            theme=ctx.theme,
            math_renderer=ctx.math_renderer,
        )
    finally:
        temp_md.unlink(missing_ok=True)


def build_article_payload(ctx: ArticleContext, thumb_media_id: str, content_html: str) -> dict[str, Any]:
    return {
        "title": ctx.title,
        "author": ctx.author,
        "digest": ctx.digest,
        "content": content_html,
        "content_source_url": ctx.content_source_url,
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 0,
        "only_fans_can_comment": 0,
    }


def command_config_check(_args: argparse.Namespace) -> int:
    print(json.dumps(credential_status(), ensure_ascii=False, indent=2))
    return 0


def command_token_check(args: argparse.Namespace) -> int:
    try:
        token = fetch_access_token(force_refresh=args.force_refresh)
    except WeChatError as exc:
        print(json.dumps({"ok": False, "stage": exc.stage, "response": exc.payload}, ensure_ascii=False, indent=2))
        return 1
    print(
        json.dumps(
            {
                "ok": True,
                "stage": "access_token_available",
                "from_cache": bool(token.get("from_cache")),
                "expires_at": token.get("expires_at"),
                "cache_path": str(TOKEN_CACHE_PATH),
                "cache_mode_octal": oct(stat.S_IMODE(TOKEN_CACHE_PATH.stat().st_mode)),
                "token_printed": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def dry_run_summary(ctx: ArticleContext) -> dict[str, Any]:
    return {
        "ok": True,
        "publication_ref": ctx.publication_ref,
        "action": ctx.action,
        "article": repo_relative(ctx.article_path),
        "review": repo_relative(ctx.review_path),
        "title": ctx.title,
        "author": ctx.author,
        "digest": ctx.digest,
        "content_source_url": ctx.content_source_url,
        "existing_media_id": ctx.existing_media_id,
        "wechat_related_links": related_wechat_links(ctx.publication_ref),
        "theme": ctx.theme,
        "math_renderer": ctx.math_renderer,
        "public_safety_check": repo_relative(REPO_ROOT / "scripts/check-public-safe-content.py"),
        "public_safety_scope": [repo_relative(ctx.article_path), repo_relative(ctx.review_path)],
        "cover": file_summary(ctx.cover_path),
        "body_images": [
            {"alt": image.alt, "markdown_src": image.raw_src, **file_summary(image.path)}
            for image in ctx.body_images
        ],
        "will_read_credentials": False,
        "will_contact_wechat": False,
        "will_create_or_update_draft": False,
    }


def command_dry_run(args: argparse.Namespace) -> int:
    ctx = build_context(args.publication_ref, args.theme, args.math_renderer)
    problems = validate_context(ctx)
    summary = dry_run_summary(ctx)
    summary["ok"] = not problems
    summary["problems"] = problems
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


def command_ip_check(args: argparse.Namespace) -> int:
    summary = egress_ip_summary(args, require_expected_ip=args.strict)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["ok"] else 1


def command_preflight(args: argparse.Namespace) -> int:
    ctx = build_context(args.publication_ref, args.theme, args.math_renderer)
    problems = validate_context(ctx)
    dry = dry_run_summary(ctx)
    dry["ok"] = not problems
    dry["problems"] = problems
    summary = {
        "ok": not problems,
        "stage": "preflight",
        "publication_ref": ctx.publication_ref,
        "theme": ctx.theme,
        "math_renderer": ctx.math_renderer,
        "draft_check": dry,
        "will_read_credentials": False,
        "will_contact_wechat": False,
        "will_create_or_update_draft": False,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["ok"] else 1


def command_content_source_plan(args: argparse.Namespace) -> int:
    refs = read_backlog_publication_refs(WECHAT_ROOT / "backlog/selected-papers.yml") if args.all else [args.publication_ref]
    items = planned_content_source_items(refs)
    summary = {
        "ok": True,
        "stage": "content_source_plan",
        "checked_count": len(items),
        "default_content_source_url_policy": "default_rtd_paper_note",
        "rtd_base_url": RTD_BASE_URL,
        "will_read_credentials": False,
        "will_contact_wechat": False,
        "will_create_or_update_draft": False,
        "items": items,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def fetch_remote_draft_article(token: str, media_id: str) -> dict[str, Any]:
    response = api_post_json(DRAFT_GET_URL, token, {"media_id": media_id})
    if "news_item" not in response:
        raise WeChatError("draft_get", response)
    news_items = response.get("news_item") or []
    if not news_items:
        raise WeChatError("draft_get", {"errcode": "empty_news_item", "errmsg": "Draft has no articles"})
    first = news_items[0]
    if not isinstance(first, dict):
        raise WeChatError("draft_get", {"errcode": "invalid_news_item", "errmsg": "Draft first article is not an object"})
    return first


def audit_remote_content_source(token: str, ctx: ArticleContext) -> dict[str, Any]:
    if not ctx.existing_media_id:
        return {
            "publication_ref": ctx.publication_ref,
            "ok": False,
            "stage": "missing_media_id",
            "expected_content_source_url": ctx.content_source_url,
            "remote_content_source_url": None,
            "matches_expected": False,
            "needs_update": True,
            "message": "backlog has no wechat_draft_media_id",
        }
    article = fetch_remote_draft_article(token, ctx.existing_media_id)
    remote_url = str(article.get("content_source_url", ""))
    matches = remote_url == ctx.content_source_url
    return {
        "publication_ref": ctx.publication_ref,
        "ok": True,
        "stage": "draft_checked",
        "wechat_draft_media_id": ctx.existing_media_id,
        "remote_title": str(article.get("title", "")),
        "expected_content_source_url": ctx.content_source_url,
        "remote_content_source_url": remote_url,
        "matches_expected": matches,
        "needs_update": not matches,
    }


def command_audit_content_source(args: argparse.Namespace) -> int:
    refs = read_backlog_publication_refs(WECHAT_ROOT / "backlog/selected-papers.yml") if args.all else [args.publication_ref]
    contexts = [build_context(ref, args.theme, args.math_renderer) for ref in refs]
    token_record = fetch_access_token(force_refresh=False)
    token = token_record["access_token"]
    items = [audit_remote_content_source(token, ctx) for ctx in contexts]
    needs_update = [item for item in items if item.get("needs_update")]
    summary = {
        "ok": not needs_update,
        "stage": "draft_content_source_audit",
        "checked_count": len(items),
        "needs_update_count": len(needs_update),
        "default_content_source_url_policy": "default_rtd_paper_note",
        "rtd_base_url": RTD_BASE_URL,
        "will_read_credentials": True,
        "will_contact_wechat": True,
        "will_create_or_update_draft": False,
        "token_printed": False,
        "items": items,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["ok"] else 1


def command_create_or_update(args: argparse.Namespace) -> int:
    ctx = build_context(args.publication_ref, args.theme, args.math_renderer)
    requested_action = "update" if args.update else "create"
    if requested_action == "update" and not ctx.existing_media_id:
        raise RuntimeError("Cannot update: backlog has no wechat_draft_media_id")
    if requested_action == "create" and ctx.existing_media_id and not args.new_copy:
        raise RuntimeError("Backlog already has wechat_draft_media_id; use update-draft or --new-copy")
    problems = validate_context(ctx)
    if problems:
        print(json.dumps({"ok": False, "stage": "validation", "problems": problems}, ensure_ascii=False, indent=2))
        return 1

    token_record = fetch_access_token(force_refresh=False)
    token = token_record["access_token"]

    cover_response = api_post_multipart(
        UPLOAD_PERMANENT_MATERIAL_URL,
        token,
        ctx.cover_path,
        {"type": "thumb"},
    )
    if "media_id" not in cover_response:
        raise WeChatError("upload_cover", cover_response)
    thumb_media_id = cover_response["media_id"]

    image_url_map: dict[str, str] = {}
    uploaded_images: list[dict[str, str]] = []
    for image in ctx.body_images:
        response = api_post_multipart(UPLOAD_BODY_IMAGE_URL, token, image.path, {})
        if "url" not in response:
            raise WeChatError("upload_body_image", response)
        image_url_map[image.raw_src] = response["url"]
        uploaded_images.append({"alt": image.alt, "src": image.raw_src, "url": response["url"]})

    content_html = render_wechat_html(ctx, image_url_map)
    article = build_article_payload(ctx, thumb_media_id, content_html)

    if requested_action == "create":
        response = api_post_json(DRAFT_ADD_URL, token, {"articles": [article]})
        if "media_id" not in response:
            raise WeChatError("draft_add", response)
        media_id = response["media_id"]
    else:
        media_id = ctx.existing_media_id
        response = api_post_json(
            DRAFT_UPDATE_URL,
            token,
            {"media_id": media_id, "index": 0, "articles": article},
        )
        if response.get("errcode") not in {0, "0", None}:
            raise WeChatError("draft_update", response)

    update_backlog_after_success(ctx.backlog_path, ctx.publication_ref, media_id, requested_action)
    print(
        json.dumps(
            {
                "ok": True,
                "stage": "draft_created" if requested_action == "create" else "draft_updated",
                "publication_ref": ctx.publication_ref,
                "wechat_draft_media_id": media_id,
                "uploaded_cover": repo_relative(ctx.cover_path),
                "uploaded_body_images": uploaded_images,
                "theme": ctx.theme,
                "math_renderer": ctx.math_renderer,
                "backlog_updated": repo_relative(ctx.backlog_path),
                "token_printed": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("config-check", help="Check local credential file shape without printing secrets")

    token = sub.add_parser("token-check", help="Fetch or reuse access_token without printing it")
    token.add_argument("--force-refresh", action="store_true")

    dry = sub.add_parser("dry-run", help="Validate first article and list what would be uploaded")
    dry.add_argument("--publication-ref", default=DEFAULT_REF)
    dry.add_argument("--theme", default=DEFAULT_THEME, choices=AVAILABLE_THEMES)
    dry.add_argument("--math-renderer", default=DEFAULT_MATH_RENDERER, choices=AVAILABLE_MATH_RENDERERS)

    ip = sub.add_parser("ip-check", help="Show the current public egress IP before any WeChat API call")
    ip.add_argument(
        "--expected-ip",
        action="append",
        default=[],
        help=f"Expected fixed egress IP. Can repeat or use commas. Also read from {EXPECTED_EGRESS_IPS_KEY}.",
    )
    ip.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero unless the current IP matches a configured expected IP",
    )

    preflight = sub.add_parser("preflight", help="Run article and asset validation without credentials")
    preflight.add_argument("--publication-ref", default=DEFAULT_REF)
    preflight.add_argument("--theme", default=DEFAULT_THEME, choices=AVAILABLE_THEMES)
    preflight.add_argument("--math-renderer", default=DEFAULT_MATH_RENDERER, choices=AVAILABLE_MATH_RENDERERS)

    plan = sub.add_parser("content-source-plan", help="Safe: list expected bottom 阅读原文 targets")
    plan.add_argument("--publication-ref", default=DEFAULT_REF)
    plan.add_argument("--all", action="store_true", help="List every publication_ref in the backlog")

    audit = sub.add_parser("audit-content-source", help="Live read-only: check WeChat draft content_source_url")
    audit.add_argument("--publication-ref", default=DEFAULT_REF)
    audit.add_argument("--all", action="store_true", help="Check every publication_ref in the backlog")
    audit.add_argument("--theme", default=DEFAULT_THEME, choices=AVAILABLE_THEMES)
    audit.add_argument("--math-renderer", default=DEFAULT_MATH_RENDERER, choices=AVAILABLE_MATH_RENDERERS)

    create = sub.add_parser("create-draft", help="Live: upload assets and create a WeChat draft")
    create.add_argument("--publication-ref", default=DEFAULT_REF)
    create.add_argument("--theme", default=DEFAULT_THEME, choices=AVAILABLE_THEMES)
    create.add_argument("--math-renderer", default=DEFAULT_MATH_RENDERER, choices=AVAILABLE_MATH_RENDERERS)
    create.add_argument("--new-copy", action="store_true", help="Create a new copy even if a draft media_id exists")
    create.set_defaults(update=False)

    update = sub.add_parser("update-draft", help="Live: upload assets and update the existing draft")
    update.add_argument("--publication-ref", default=DEFAULT_REF)
    update.add_argument("--theme", default=DEFAULT_THEME, choices=AVAILABLE_THEMES)
    update.add_argument("--math-renderer", default=DEFAULT_MATH_RENDERER, choices=AVAILABLE_MATH_RENDERERS)
    update.set_defaults(update=True, new_copy=False)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "config-check":
            return command_config_check(args)
        if args.command == "token-check":
            return command_token_check(args)
        if args.command == "dry-run":
            return command_dry_run(args)
        if args.command == "ip-check":
            return command_ip_check(args)
        if args.command == "preflight":
            return command_preflight(args)
        if args.command == "content-source-plan":
            return command_content_source_plan(args)
        if args.command == "audit-content-source":
            return command_audit_content_source(args)
        if args.command in {"create-draft", "update-draft"}:
            return command_create_or_update(args)
    except WeChatError as exc:
        print(json.dumps({"ok": False, "stage": exc.stage, "response": exc.payload}, ensure_ascii=False, indent=2))
        return 1
    except Exception as exc:
        print(
            json.dumps(
                {"ok": False, "stage": "local_error", "error_type": type(exc).__name__, "message": str(exc)},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1
    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
