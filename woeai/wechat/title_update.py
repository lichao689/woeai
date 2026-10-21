"""Change an existing draft title with strict, explained field comparisons."""
from copy import deepcopy
import hashlib
import json


class TitleUpdateError(RuntimeError):
    def __init__(self, code, *, write_attempted=False):
        self.code = code
        self.write_attempted = write_attempted
        super().__init__(code)


def field_differences(before, after, path=""):
    """Describe typed JSON differences without exposing their values."""
    if type(before) is type(after) and isinstance(before, dict):
        result = []
        for key in sorted(before.keys() | after.keys()):
            child = path + "/" + key.replace("~", "~0").replace("/", "~1")
            if key not in before or key not in after:
                result.append(_difference(before.get(key), after.get(key), child,
                                          "added" if key not in before else "removed"))
            else:
                result.extend(field_differences(before[key], after[key], child))
        return result
    if type(before) is type(after) and isinstance(before, list) and len(before) == len(after):
        return [change for i, (left, right) in enumerate(zip(before, after))
                for change in field_differences(left, right, path + "/" + str(i))]
    if type(before) is type(after) and before == after:
        return []
    return [_difference(before, after, path, "changed")]


def _difference(before, after, path, kind):
    root = path.split("/")[1] if path else ""
    category = {"content": "body_html", "thumb_media_id": "cover_material",
                "thumb_url": "cover_url", "cover_info": "cover_crop",
                "show_cover_pic": "cover_display", "url": "platform_preview_url",
                "title": "title"}.get(root, "metadata_or_unknown")
    def digest(value):
        return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return {"path": path, "kind": kind, "category": category,
            "before_type": type(before).__name__, "after_type": type(after).__name__,
            "before_sha256": digest(before), "after_sha256": digest(after)}


def comparison(before, after, *, title_change=False):
    changes = field_differences(before, after)
    for change in changes:
        # Keep the existing sole platform exception; never normalize body/cover.
        change["permitted"] = change["path"] == "/url" or (title_change and change["path"] == "/title")
    return {"differences": changes,
            "all_protected_equal": all(c["permitted"] for c in changes)}


def update_title(read_article, write_article, *, expected_title, desired_title, observe=None,
                 allow_platform_formatting=False, fetch_cover_image=None):
    """Read twice, snapshot before writing once, then explain the readback."""
    observe = observe or (lambda event, value: None)
    before = read_article()
    observe("before-article", before)
    if any(not isinstance(before.get(key), str) or not before[key] for key in ("title", "content", "thumb_media_id")):
        raise TitleUpdateError("incomplete_remote_article")
    previous_titles = (expected_title,) if isinstance(expected_title, str) else tuple(expected_title)
    if before.get("title") not in {*previous_titles, desired_title}:
        raise TitleUpdateError("remote_title_conflict")
    current = read_article()
    observe("prewrite-article", current)
    prewrite = comparison(before, current)
    observe("prewrite-differences", prewrite)
    if not prewrite["all_protected_equal"]:
        raise TitleUpdateError("remote_article_changed")
    if current["title"] == desired_title:
        return {"updated": False, "title_verified": True, "non_title_unchanged": True}
    payload = {key: deepcopy(value) for key, value in current.items()
               if key not in {"url", "thumb_url"}}
    payload["title"] = desired_title
    observe("article-request", payload)
    write_article(payload)
    after = read_article()
    observe("after-article", after)
    postwrite = comparison(current, after, title_change=True)
    if allow_platform_formatting:
        from woeai.wechat.title_equivalence import image_closing_equivalence, cover_url_equivalence
        proof = {"body": {"checked": False}, "cover": {"checked": False}}
        candidates = {"/content", "/thumb_url"}
        unknown = [c for c in postwrite["differences"] if not c["permitted"] and c["path"] not in candidates]
        if not unknown:
            for change in postwrite["differences"]:
                if change["path"] == "/content":
                    proof["body"] = {"checked": True, **image_closing_equivalence(current.get("content"), after.get("content"))}
                    change["permitted"] = proof["body"]["equivalent"]
                    change["equivalence_reason"] = proof["body"]["reason"]
            body_ok = not any(c["path"] == "/content" and not c["permitted"] for c in postwrite["differences"])
            for change in postwrite["differences"]:
                if body_ok and change["path"] == "/thumb_url" and fetch_cover_image is not None:
                    proof["cover"] = {"checked": True, **cover_url_equivalence(current.get("thumb_url"), after.get("thumb_url"), fetch_cover_image)}
                    change["permitted"] = proof["cover"]["equivalent"]
                    change["equivalence_reason"] = proof["cover"]["reason"]
        observe("platform-equivalence", proof)
        postwrite["all_protected_equal"] = all(c["permitted"] for c in postwrite["differences"])
    observe("postwrite-differences", postwrite)
    if after.get("title") != desired_title:
        raise TitleUpdateError("title_readback_failed", write_attempted=True)
    if not postwrite["all_protected_equal"]:
        raise TitleUpdateError("non_title_readback_changed", write_attempted=True)
    result = {"updated": True, "title_verified": True, "non_title_unchanged": True}
    if allow_platform_formatting:
        result["platform_equivalence_used"] = any(c.get("equivalence_reason") for c in postwrite["differences"])
    return result
