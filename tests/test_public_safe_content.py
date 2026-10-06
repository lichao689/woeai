from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check-public-safe-content.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("public_safe_content", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load public-safety checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PublicSafeContentTests(unittest.TestCase):
    def run_checker(self, root: Path, wechat_root: Path, *extra_roots: Path) -> tuple[int, str, str]:
        checker = load_checker()
        checker.ROOT = root
        checker.SCAN_ROOTS = [wechat_root, *extra_roots]
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = checker.main()
        return result, stdout.getvalue(), stderr.getvalue()

    def test_parent_private_directory_does_not_skip_wechat_scan(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "private" / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "draft.md").write_text(
                "appsecret = abcdefgh12345678\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("wechat/draft.md:1: possible secret pattern (appsecret)", stderr)

    def test_policy_text_without_secret_assignment_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "README.md").write_text(
                "Do not commit WeChat AppSecret, access tokens, or Zotero API keys.\n",
                encoding="utf-8",
            )

            result, stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 0)
            self.assertIn("Public-safety check passed", stdout)
            self.assertEqual(stderr, "")

    def test_failure_output_includes_line_and_pattern_label(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "draft.md").write_text(
                "title: draft\naccess_token = abcdefghijklmnop\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("Public-safety check failed:", stderr)
            self.assertIn("wechat/draft.md:2: possible secret pattern (access_token)", stderr)

    def test_scans_json_and_env_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "token.json").write_text(
                '{"refresh_token": "abcdefghijklmnop"}\n',
                encoding="utf-8",
            )
            (wechat_root / ".env").write_text(
                "ZOTERO_API_KEY=abcdefgh\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("wechat/token.json:1: possible secret pattern (refresh_token)", stderr)
            self.assertIn("wechat/.env:1: possible secret pattern (zotero_api_key)", stderr)

    def test_private_backend_values_are_rejected_without_echoing_values(self) -> None:
        cases = [
            ('media_id: "synthetic-media-123"', "media_id"),
            ('{"draft_id": "synthetic-draft-123"}', "draft_id"),
            ('publish_id=123456', "publish_id"),
            ('media_id: "optional"', "media_id"),
            ('media_id: "abcdefghijklmnopqrstuvwxyz"', "media_id"),
            ('DRAFT_ID = "synthetic-draft-123"', "draft_id"),
            ('- `wechat_draft_media_id`: `synthetic-media-123`', "wechat_draft_media_id"),
            ('- **thumb_media_id**：`synthetic-thumb-123`', "thumb_media_id"),
            ('草稿 media_id 为 `synthetic-media-123`。', "media_id"),
            ('The draft_id is `synthetic-draft-123`.', "draft_id"),
            ('media_id `synthetic-media-123`', "media_id"),
            ('media_id: >-\n  synthetic-media-123', "media_id"),
            ('media_id:\n  "synthetic-media-123"', "media_id"),
            ('backend_response: {"errcode": 0}', "backend_response"),
            ('"wechat_draft_response": {"errcode": 0}', "wechat_draft_response"),
            ('api_response: |\n  {"errcode": 0}', "api_response"),
            ('`backend_response`: `synthetic-response-123`', "backend_response"),
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            review_dir = wechat_root / "articles" / "review"
            review_dir.mkdir(parents=True)
            path = review_dir / "example.review.md"
            for snippet, field in cases:
                with self.subTest(field=field, snippet=snippet):
                    path.write_text("## 源文件获取记录\n## 关键事实证据定位记录\n" + snippet + "\n")
                    result, stdout, stderr = self.run_checker(root, wechat_root)
                    self.assertEqual(result, 1)
                    self.assertIn(f":3: private backend data ({field})", stderr)
                    self.assertNotIn("synthetic-", stdout + stderr)
                    self.assertNotIn("123456", stdout + stderr)

    def test_backend_checks_apply_to_all_public_scan_roots(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            roots = [root / "wechat", root / "docs/source/paper-notes", root / "docs/data"]
            for scan_root, suffix in zip(roots, (".yml", ".rst", ".json")):
                scan_root.mkdir(parents=True)
                (scan_root / ("example" + suffix)).write_text('"publish_id": "synthetic-publish-123"\n')
            result, _stdout, stderr = self.run_checker(root, *roots)
            self.assertEqual(result, 1)
            self.assertEqual(stderr.count("private backend data (publish_id)"), 3)

    def test_backend_policy_names_and_citation_keys_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            wechat_root.mkdir()
            (wechat_root / "README.md").write_text(
                "Keep media_id, draft_id, publish_id and backend_response private.\n"
                "Use `wechat_draft_media_id` to update a draft.\n"
                "- `wechat_draft_media_id`: optional existing draft `media_id` returned by the API.\n"
                "Zotero key: SYNTH123\nzotero_item_key: SYNTH456\n"
                'media_id: ""\ndraft_id: null\npublish_id: <private>\n'
                "media_id: [REDACTED]\nbackend_response: {}\n"
                "A `media_id` is returned by the API.\n"
            )
            result, _stdout, stderr = self.run_checker(root, wechat_root)
            self.assertEqual(result, 0, stderr)

    def test_backend_data_in_ignored_private_storage_is_not_scanned(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            private = wechat_root / ".local"
            private.mkdir(parents=True)
            (private / "draft.json").write_text('{"media_id": "synthetic-media-123"}')
            result, _stdout, stderr = self.run_checker(root, wechat_root)
            self.assertEqual(result, 0, stderr)

    def test_private_source_locators_are_rejected_without_echo(self) -> None:
        cases = [
            ("PDF attachment key: `SYNTH123`", "attachment_identifier"),
            ("ATTACH_KEY=SYNTH123", "attachment_identifier"),
            ("PDF attachment keys: `SYNTH123`, `SYNTH456`", "attachment_identifier"),
            ("PDF attachment: Zotero child `SYNTH123`", "attachment_identifier"),
            ("Zotero child IDs: SYNTH123", "attachment_identifier"),
            ("Zotero Local API children: passed (`SYNTH123`, application/pdf)", "attachment_identifier"),
            ("PDF associated with attachment `SYNTH123`", "attachment_identifier"),
            ('{"zotero_attachment_key": "SYNTH123"}', "attachment_identifier"),
            ('attachment_keys: ["SYNTH123", "SYNTH456"]', "attachment_identifier"),
            ("PDF: `/Users/synthetic/Documents/source.pdf`", "local_source_path"),
            ("Source: /home/synthetic/papers/source.pdf", "local_source_path"),
            ("Source: `/workspace/shared/private/source.txt`", "local_source_path"),
            ("PDF: file:///tmp/synthetic/source.pdf", "local_source_path"),
            (r"PDF: C:\Users\synthetic\source.pdf", "local_source_path"),
            ("Local PDF: ~/papers/synthetic.pdf", "local_source_path"),
            ('library_file_id: "file-synthetic123"', "library_operational_identifier"),
            ('Library folder ID: "synthetic-folder-123"', "library_operational_identifier"),
            ("Library ID: `synthetic-library-123`", "library_operational_identifier"),
            ("Download: sediment://file_synthetic123", "library_operational_identifier"),
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            research_root = root / "project/research"
            wechat_root.mkdir()
            research_root.mkdir(parents=True)
            for scan_root, name in [(wechat_root, "audit.md"), (research_root, "audit.md")]:
                path = scan_root / name
                for snippet, label in cases:
                    with self.subTest(root=scan_root.name, snippet=snippet):
                        path.write_text("Audit\n" + snippet + "\n", encoding="utf-8")
                        result, stdout, stderr = self.run_checker(root, wechat_root, research_root)
                        self.assertEqual(result, 1)
                        self.assertIn(f":2: private source locator ({label})", stderr)
                        self.assertNotIn("SYNTH123", stdout + stderr)
                        self.assertNotIn("synthetic", stdout + stderr)
                path.unlink()

    def test_public_bibliographic_keys_and_generic_provenance_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            wechat_root.mkdir()
            (wechat_root / "audit.md").write_text(
                'Zotero item key: SYNTH123\nZotero key: SYNTH456\n'
                '{"zotero_item_key": "SYNTH123", "key": "SYNTH456"}\n'
                'PDF attachment keys remain in private storage.\n'
                'ATTACH_KEY=PRIVATE_ATTACHMENT_KEY\n'
                'Zotero attachment records verified; original Library copy used.\n'
                'PDF associated with attachment metadata in private storage.\n'
                'PDF file page 3; Fig. 2.\n'
                'https://example.org/papers/source.pdf\n'
                'Approved asset: ../assets/public-safe/figure.png\n', encoding="utf-8")
            result, _stdout, stderr = self.run_checker(root, wechat_root)
            self.assertEqual(result, 0, stderr)

    def test_research_audits_are_in_default_scan_scope(self) -> None:
        checker = load_checker()
        self.assertIn(ROOT / "project/research", checker.SCAN_ROOTS)
        self.assertIn(ROOT / "project/plans", checker.SCAN_ROOTS)

    def test_attachment_inventory_table_preserves_public_item_key_column(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            plans_root = root / "project/plans"
            wechat_root.mkdir()
            plans_root.mkdir(parents=True)
            path = plans_root / "inventory.md"
            table = ("| Zotero item key | PDF attachment key | Notes |\n"
                     "| --- | --- | --- |\n"
                     "| SYNTH456 | {attachment} | PDF and HTML attachment records exist |\n")
            path.write_text(table.format(attachment="`SYNTH123`"), encoding="utf-8")
            result, _stdout, stderr = self.run_checker(root, wechat_root, plans_root)
            self.assertEqual(result, 1)
            self.assertIn("project/plans/inventory.md:3: private source locator (attachment_identifier)", stderr)
            self.assertNotIn("SYNTH123", stderr)
            path.write_text(table.format(attachment="private storage"), encoding="utf-8")
            result, _stdout, stderr = self.run_checker(root, wechat_root, plans_root)
            self.assertEqual(result, 0, stderr)

    def test_reviews_reject_internal_metadata_and_preview_history(self) -> None:
        cases = [
            ("zotero_key: SYNTH123", "review_zotero_identifier"),
            ('"zotero_item_key": "SYNTH123"', "review_zotero_identifier"),
            ("Zotero item key: `SYNTH123`", "review_zotero_identifier"),
            ("Zotero item `SYNTH123`", "review_zotero_identifier"),
            ("Zotero citation ID: SYNTH123", "review_zotero_identifier"),
            ("zotero://select/library/items/SYNTH123", "review_zotero_identifier"),
            ("wechat_draft_created_at: '2026-01-01T01:00:00Z'", "review_draft_history"),
            ("wechat_draft_updated_at: '2026-01-02T01:00:00Z'", "review_draft_history"),
            ("preview_html: preview.html", "review_preview_field"),
            ("preview_html_path: temporary/preview.html", "review_preview_field"),
            ("offline_html_path: temporary/offline.html", "review_preview_field"),
            ("local_preview_path: temporary/preview.html", "review_preview_field"),
            ("Local preview: `wechat/.local/synthetic/preview.html`", "review_private_path"),
            ("Local preview: `/tmp/synthetic/preview.html`", "review_private_path"),
            ("Crops: `wechat-preview-html/synthetic/crop.png`", "review_private_path"),
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            review_dir = wechat_root / "articles/review"
            review_dir.mkdir(parents=True)
            path = review_dir / "example.review.md"
            for snippet, label in cases:
                with self.subTest(label=label, snippet=snippet):
                    path.write_text("## 源文件获取记录\n## 关键事实证据定位记录\n" + snippet + "\n", encoding="utf-8")
                    result, stdout, stderr = self.run_checker(root, wechat_root)
                    self.assertEqual(result, 1)
                    self.assertIn(f":3: review contains private or obsolete workflow content ({label})", stderr)
                    self.assertNotIn("SYNTH123", stdout + stderr)
                    self.assertNotIn("synthetic", stdout + stderr)
                    self.assertNotIn("2026-01-01", stdout + stderr)

    def test_review_ready_status_requires_all_current_preview_flags(self) -> None:
        checker = load_checker()
        flags = checker.REVIEW_READY_FLAGS
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            review_dir = wechat_root / "articles/review"
            review_dir.mkdir(parents=True)
            path = review_dir / "example.review.md"
            for missing in [None, *flags]:
                for value in ["false", "missing", '"true"']:
                    with self.subTest(flag=missing, value=value):
                        lines = ["---", "wechat_status: ready_to_publish"]
                        for flag in flags:
                            if flag == missing and value == "missing":
                                continue
                            lines.append(f"{flag}: {value if flag == missing else 'true'}")
                        lines += ["---", "## 源文件获取记录", "## 关键事实证据定位记录"]
                        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
                        result, _stdout, stderr = self.run_checker(root, wechat_root)
                        self.assertEqual(result, 0 if missing is None else 1, stderr)
                        if missing:
                            self.assertIn(":2: review readiness lacks current preview approvals (review_stale_ready)", stderr)

    def test_review_readiness_ignores_prose_mentions_and_body_flags(self) -> None:
        checker = load_checker()
        self.assertEqual(checker.stale_review_ready_lines(
            "---\nwechat_status: awaiting_review\n---\n"
            "The ready_to_publish state follows preview approval.\n"
            "wechat_status: ready_to_publish\n"), [])
        self.assertEqual(checker.stale_review_ready_lines(
            "---\nwechat_status: ready_to_publish\n---\n" +
            "\n".join(f"{flag}: true" for flag in checker.REVIEW_READY_FLAGS)), [2])
        self.assertEqual(checker.stale_review_ready_lines(
            "---\nwechat_status: 'ready_to_publish'\n" +
            "\n".join(f"{flag}: true # confirmed" for flag in checker.REVIEW_READY_FLAGS) + "\n---\n"), [])

    def test_minimal_reviews_preserve_current_scientific_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            review_dir = wechat_root / "articles/review"
            review_dir.mkdir(parents=True)
            (review_dir / "example.review.md").write_text(
                "---\npublication_ref: ref-example\ndoi: 10.0000/example\n"
                "wechat_status: awaiting_review\nformula_preview_checked: false\n"
                "wechat_backend_preview_checked: false\n"
                "cover_image: wechat/assets/public-safe/ref-example/cover.png\n"
                "rtd_cover_image: wechat/assets/public-safe/ref-example/cover-rtd.png\n---\n"
                "## 源文件获取记录\nPrivate authorized Library source; Zotero metadata checked.\n"
                "Source SHA-256: " + "a" * 64 + "\n"
                "## 关键事实证据定位记录\nPDF file page 4, Fig. 2; equation (3).\n"
                "Body: wechat/articles/draft-public-safe/ref-example.md\n"
                "![Figure](../../assets/public-safe/ref-example/figure.png)\n", encoding="utf-8")
            result, _stdout, stderr = self.run_checker(root, wechat_root)
            self.assertEqual(result, 0, stderr)

    def test_review_rules_do_not_reject_registry_or_sync_identifiers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wechat_root = root / "wechat"
            data_root = root / "docs/data"
            wechat_root.mkdir()
            data_root.mkdir(parents=True)
            (data_root / "publications.json").write_text(
                '{"zotero_key": "SYNTH123", "id": "SYNTH456"}', encoding="utf-8")
            (wechat_root / "README.md").write_text(
                "Zotero item key: SYNTH123\nwechat_status: ready_to_publish\n", encoding="utf-8")
            result, _stdout, stderr = self.run_checker(root, wechat_root, data_root)
            self.assertEqual(result, 0, stderr)

    def test_reader_facing_draft_rejects_editor_only_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            draft_dir = wechat_root / "articles" / "draft-public-safe"
            draft_dir.mkdir(parents=True)
            (draft_dir / "ref-example.md").write_text(
                "---\n"
                "status: draft-public-safe\n"
                "---\n\n"
                "# Title\n\n"
                "【待上传原文图 Fig. 1】\n\n"
                "### 计划配图\n\n"
                "## 发布前人工复核项\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("reader draft contains editor-only content (yaml_front_matter)", stderr)
            self.assertIn("reader draft contains editor-only content (pending_placeholder)", stderr)
            self.assertIn("reader draft contains editor-only content (figure_plan)", stderr)
            self.assertIn("reader draft contains editor-only content (pre_publish_checklist)", stderr)

    def test_rtd_paper_deep_dive_rejects_english_abstract_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            paper_notes_root = root / "docs" / "source" / "paper-notes"
            wechat_root.mkdir(parents=True)
            paper_notes_root.mkdir(parents=True)
            (paper_notes_root / "ref-example.rst").write_text(
                "示例标题\n"
                "========\n\n"
                "摘要\n"
                "--\n\n"
                "**英文摘要**\n\n"
                "Example abstract.\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root, paper_notes_root)

            self.assertEqual(result, 1)
            self.assertIn("docs/source/paper-notes/ref-example.rst:7: RTD paper deep-dive contains editor-only content (english_abstract)", stderr)

    def test_rtd_paper_deep_dive_rejects_latex_tag(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            paper_notes_root = root / "docs" / "source" / "paper-notes"
            wechat_root.mkdir(parents=True)
            paper_notes_root.mkdir(parents=True)
            (paper_notes_root / "ref-example.rst").write_text(
                "示例标题\n"
                "========\n\n"
                ".. math::\n\n"
                "   a+b=c\\tag{1}\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root, paper_notes_root)

            self.assertEqual(result, 1)
            self.assertIn("latex_tag_in_math", stderr)

    def test_rtd_paper_deep_dive_requires_wechat_cover_after_short_article_line(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            paper_notes_root = root / "docs" / "source" / "paper-notes"
            wechat_root.mkdir(parents=True)
            paper_notes_root.mkdir(parents=True)
            (paper_notes_root / "ref-example.rst").write_text(
                "示例论文精解\n"
                "============\n\n"
                "精简版微信公众号文章：待发布\n\n"
                ".. contents:: 本页目录\n\n"
                "1 结论\n"
                "------\n\n"
                "Conclusion.\n\n"
                "参考文献\n"
                "--------\n\n"
                "- Reference.\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root, paper_notes_root)

            self.assertEqual(result, 1)
            self.assertIn("top_wechat_cover", stderr)

    def test_rtd_paper_deep_dive_allows_appendix_between_conclusion_and_references(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            paper_notes_root = root / "docs" / "source" / "paper-notes"
            wechat_root.mkdir(parents=True)
            paper_notes_root.mkdir(parents=True)
            (paper_notes_root / "ref-example.rst").write_text(
                "示例论文精解\n"
                "============\n\n"
                "精简版微信公众号文章：待发布\n\n"
                ".. image:: ../../../wechat/assets/public-safe/ref-example/cover-wechat.png\n\n"
                "1 结论\n"
                "------\n\n"
                "Conclusion.\n\n"
                "附录 A 方法细节\n"
                "---------------\n\n"
                "Appendix.\n\n"
                "参考文献\n"
                "--------\n\n"
                "- Reference.\n",
                encoding="utf-8",
            )

            result, stdout, stderr = self.run_checker(root, wechat_root, paper_notes_root)

            self.assertEqual(result, 0)
            self.assertIn("Public-safety check passed", stdout)
            self.assertEqual(stderr, "")

    def test_rtd_paper_deep_dive_rejects_disallowed_section_between_conclusion_and_references(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            paper_notes_root = root / "docs" / "source" / "paper-notes"
            wechat_root.mkdir(parents=True)
            paper_notes_root.mkdir(parents=True)
            (paper_notes_root / "ref-example.rst").write_text(
                "示例论文精解\n"
                "============\n\n"
                "精简版微信公众号文章：待发布\n\n"
                ".. image:: ../../../wechat/assets/public-safe/ref-example/cover-wechat.png\n\n"
                "1 结论\n"
                "------\n\n"
                "Conclusion.\n\n"
                "CRediT 作者贡献声明\n"
                "-------------------\n\n"
                "Contribution.\n\n"
                "参考文献\n"
                "--------\n\n"
                "- Reference.\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root, paper_notes_root)

            self.assertEqual(result, 1)
            self.assertIn("post_conclusion_section: CRediT 作者贡献声明", stderr)

    def test_review_template_may_contain_editor_workflow_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            review_dir = wechat_root / "articles" / "review"
            review_dir.mkdir(parents=True)
            (review_dir / "ref-example.review.md").write_text(
                "---\n"
                "formula_preview_checked: false\n"
                "---\n\n"
                "## 源文件获取记录\n\n"
                "- Zotero key: EXAMPLE\n\n"
                "## 关键事实证据定位记录\n\n"
                "- 摘要: pending PDF page audit\n\n"
                "## 发布前任务\n\n"
                "- 图片状态: pending original high-resolution figure\n",
                encoding="utf-8",
            )

            result, stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 0)
            self.assertIn("Public-safety check passed", stdout)
            self.assertEqual(stderr, "")

    def test_review_note_requires_source_and_evidence_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            review_dir = wechat_root / "articles" / "review"
            review_dir.mkdir(parents=True)
            (review_dir / "ref-example.review.md").write_text(
                "---\n"
                "formula_preview_checked: false\n"
                "---\n\n"
                "## 发布前任务\n\n"
                "- 图片状态: pending original high-resolution figure\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("review note missing required section (源文件获取记录)", stderr)
            self.assertIn("review note missing required section (关键事实证据定位记录)", stderr)


if __name__ == "__main__":
    unittest.main()
