"""Registry-backed WeChat readers and no-submit/live writeback boundaries."""
from __future__ import annotations

import contextlib
from dataclasses import replace
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from woeai.wechat.backlog import parse_backlog_papers, read_backlog_item, read_backlog_publication_refs

ROOT = Path(__file__).resolve().parents[1]


def record(ref="ref-example", *, selected=True, order=0):
    return {
        "id": "KEY" + ref,
        "type": "article-journal",
        "title": "Authoritative title",
        "issued": {"date-parts": [[2026]]},
        "custom": {
            "publication_ref": ref,
            "research_family": "结构风工程",
            "subdirection": "数值风洞",
            "source": {"status": "missing"},
            "rtd": {"status": "unregistered", "path": f"docs/source/paper-notes/{ref}.rst", "issues": [], "evidence": {}},
            "wechat": {
                "path": f"wechat/articles/draft-public-safe/{ref}.md",
                "review_path": f"wechat/articles/review/{ref}.review.md",
                "selected": selected,
                "selection_order": order,
                "status": "drafting",
                "draft_updated_at": "",
                "latest_published_url": "https://mp.weixin.qq.com/s/current",
                "issues": [],
                "evidence": {},
                "legacy_backlog": {"repost_priority": "high", "wechat_status": "ready_to_publish", "latest_published_url": "obsolete"},
            },
        },
    }


class WeChatRegistryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.registry = self.root / "docs/data/publications.json"
        self.registry.parent.mkdir(parents=True)
        self.backlog = self.root / "wechat/backlog/selected-papers.yml"
        self.backlog.parent.mkdir(parents=True)
        self.backlog.write_text("items:\n  - publication_ref: ref-obsolete\n    title: Old view\n", encoding="utf-8")
        self.write_registry([record()])
        spec = importlib.util.spec_from_file_location("woeai_draft_registry_test", ROOT / "wechat/tools/wechat_draft.py")
        self.draft = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = self.draft
        spec.loader.exec_module(self.draft)
        for name, value in [("REPO_ROOT", self.root), ("WECHAT_ROOT", self.root / "wechat")]:
            patcher = mock.patch.object(self.draft, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.write_account_binding()

    def write_registry(self, records):
        self.registry.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def context(self, *, existing_media_id=""):
        article = self.root / "wechat/articles/draft-public-safe/ref-example.md"
        article.parent.mkdir(parents=True, exist_ok=True)
        article.write_text("# Example\n\nArticle body.\n", encoding="utf-8")
        review = self.root / "wechat/articles/review/ref-example.review.md"
        review.parent.mkdir(parents=True, exist_ok=True)
        review.write_text("Review evidence.\n", encoding="utf-8")
        cover = self.root / "wechat/assets/public-safe/ref-example/cover.png"
        cover.parent.mkdir(parents=True, exist_ok=True)
        cover.write_bytes(b"fake-image")
        return self.draft.ArticleContext("ref-example", article, review, self.backlog, "Example", "Author", "Digest", "https://example.org/paper", cover, [], "update" if existing_media_id else "create", existing_media_id, "academic-clean", "lightweight", article_index=0 if existing_media_id else None, draft_mapping_app_id="wx0000000000000000" if existing_media_id else "")

    def args(self, *, update=False):
        return SimpleNamespace(
            publication_ref="ref-example", theme="academic-clean",
            math_renderer="lightweight", update=update, new_copy=False,
        )

    @contextlib.contextmanager
    def live_stub(self, ctx, response):
        """Exercise the real state writeback without any network/credential I/O."""
        with (
            mock.patch.object(self.draft, "build_context", return_value=ctx),
            mock.patch.object(self.draft, "validate_context", return_value=[]),
            mock.patch.object(self.draft, "fetch_access_token", return_value={"access_token": "test-token"}),
            mock.patch.object(self.draft, "api_post_multipart", return_value={"media_id": "test-cover"}),
            mock.patch.object(self.draft, "render_wechat_html", return_value="<p>test</p>"),
            mock.patch.object(self.draft, "api_post_json", return_value=response) as post,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            yield post

    def test_registry_overrides_stale_view_and_legacy_fields(self):
        data = record()
        data["custom"]["wechat"]["draft_updated_at"] = "2026-10-01T12:00:00+00:00"
        self.write_registry([data])
        item = read_backlog_item(self.backlog, "ref-example")
        self.assertEqual(item["title"], "Authoritative title")
        self.assertEqual(item["wechat_status"], "drafting")
        self.assertEqual(item["original_year"], "2026")
        self.assertEqual(item["repost_priority"], "high")
        self.assertEqual(item["wechat_draft_updated_at"], "2026-10-01T12:00:00+00:00")
        self.assertEqual(item["latest_published_url"], "https://mp.weixin.qq.com/s/current")
        self.assertTrue(all(isinstance(value, str) for value in item.values()))
        self.assertEqual(read_backlog_item(self.backlog, "ref-obsolete"), {})

    def test_only_selected_items_in_selection_order_even_when_view_absent(self):
        self.write_registry([record("ref-later", order=5), record("ref-hidden", selected=False), record("ref-first", order=1)])
        self.backlog.unlink()
        self.assertEqual(read_backlog_publication_refs(self.backlog), ["ref-first", "ref-later"])
        papers = parse_backlog_papers(self.backlog)
        self.assertEqual([paper.publication_ref for paper in papers], ["ref-first", "ref-later"])
        self.assertEqual([paper.order for paper in papers], [0, 1])
        self.assertEqual(papers[0].wechat_status, "drafting")
        self.assertEqual(read_backlog_item(self.backlog, "ref-hidden"), {})

    def test_registry_reader_never_returns_private_media_identifiers(self):
        data = record()
        data["custom"]["wechat"]["legacy_backlog"]["wechat_draft_media_id"] = "must-stay-private"
        self.write_registry([data])
        self.assertNotIn("wechat_draft_media_id", read_backlog_item(self.backlog, "ref-example"))

    def test_invalid_registry_does_not_silently_fall_back_to_generated_view(self):
        self.registry.write_text("invalid json", encoding="utf-8")
        with self.assertRaises(ValueError):
            parse_backlog_papers(self.backlog)

    def test_legacy_fixture_without_registry_still_works(self):
        self.registry.unlink()
        self.assertEqual(read_backlog_publication_refs(self.backlog), ["ref-obsolete"])
        self.assertEqual(parse_backlog_papers(self.backlog)[0].title, "Old view")

    def test_no_submit_commands_do_not_mutate_files_or_read_credentials(self):
        ctx = self.context()
        before = self.snapshot()
        args = SimpleNamespace(publication_ref="ref-example", theme="academic-clean", math_renderer="lightweight")
        with mock.patch.object(self.draft, "build_context", return_value=ctx), mock.patch.object(self.draft, "validate_context", return_value=[]), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.draft.command_dry_run(args), 0)
            self.assertEqual(self.draft.command_preflight(args), 0)
        self.assertEqual(before, self.snapshot())

    def test_success_records_draft_created_and_private_identifier(self):
        from woeai.publications.registry import workflow_fingerprint
        ctx = self.context()
        before_record = json.loads(self.registry.read_text(encoding="utf-8"))[0]
        fingerprint = workflow_fingerprint(before_record, "wechat", self.root)
        with self.live_stub(ctx, {"media_id": "test-private-draft"}):
            self.assertEqual(self.draft.command_create_or_update(self.args()), 0)
        state = json.loads(self.registry.read_text(encoding="utf-8"))[0]["custom"]["wechat"]
        self.assertEqual(state["status"], "draft_created")
        self.assertTrue(state["draft_created_at"])
        self.assertTrue(state["draft_updated_at"])
        self.assertEqual(state["evidence"]["draft_created"]["fingerprint"], fingerprint)
        private_path = self.root / "wechat/.local/registry-drafts.json"
        self.assertEqual(json.loads(private_path.read_text())["ref-example"]["media_id"], "test-private-draft")
        self.assertEqual(private_path.stat().st_mode & 0o777, 0o600)
        self.assertNotIn("test-private-draft", self.registry.read_text())
        self.assertNotIn("test-private-draft", self.backlog.read_text())
        self.assertIn("draft_created", self.backlog.read_text())

    def test_failed_live_call_does_not_mutate_registry_or_private_state(self):
        ctx = self.context()
        before = self.snapshot()
        with self.live_stub(ctx, {"errcode": 40001}), self.assertRaises(self.draft.WeChatError):
            self.draft.command_create_or_update(self.args())
        self.assertEqual(before, self.snapshot())

    def test_build_context_finds_existing_id_only_in_private_storage(self):
        ctx = self.context()
        self.draft.save_private_draft(self.backlog, "ref-example", "test-existing", "old-time")
        before = self.snapshot()
        with (
            mock.patch.object(self.draft, "parse_front_matter", return_value={"body_images_upload_approved": "true"}),
            mock.patch.object(self.draft, "parse_cover_path", return_value=ctx.cover_path),
        ):
            loaded = self.draft.build_context("ref-example", math_renderer="lightweight")
        self.assertEqual(loaded.existing_media_id, "test-existing")
        self.assertEqual(loaded.action, "update")
        self.assertEqual(before, self.snapshot())
        self.assertNotIn("media_id", json.dumps(read_backlog_item(self.backlog, "ref-example")))

    def test_update_preserves_first_creation_timestamp_and_never_marks_ready(self):
        ctx = self.context(existing_media_id="test-existing")
        data = record()
        data["custom"]["wechat"]["draft_created_at"] = "2026-06-01T00:00:00+00:00"
        self.write_registry([data])
        with self.live_stub(ctx, {"errcode": 0}):
            self.assertEqual(self.draft.command_create_or_update(self.args(update=True)), 0)
        state = json.loads(self.registry.read_text())[0]["custom"]["wechat"]
        self.assertEqual(state["status"], "draft_created")
        self.assertEqual(state["draft_created_at"], "2026-06-01T00:00:00+00:00")
        self.assertEqual(state["evidence"]["draft_created"]["operation"], "update")
        self.assertEqual(self.draft.existing_draft_media_id(self.backlog, "ref-example"), "test-existing")

    def test_failed_or_unconfirmed_update_does_not_mutate_state(self):
        ctx = self.context(existing_media_id="test-existing")
        self.draft.save_private_draft(self.backlog, "ref-example", "test-existing", "old-time")
        before = self.snapshot()
        for response in ({"errcode": 40001}, {}, {"errcode": None}):
            with self.subTest(response=response):
                with self.live_stub(ctx, response), self.assertRaises(self.draft.WeChatError):
                    self.draft.command_create_or_update(self.args(update=True))
                self.assertEqual(before, self.snapshot())

    def test_edit_during_delivery_leaves_draft_evidence_stale(self):
        from woeai.publications.registry import workflow_fingerprint
        ctx = self.context()
        data = json.loads(self.registry.read_text())[0]
        before_fingerprint = workflow_fingerprint(data, "wechat", self.root)

        def successful_delivery(*_args):
            ctx.article_path.write_text("# Changed while API request was in flight\n")
            return {"media_id": "test-private-draft"}

        with self.live_stub(ctx, {}) as post:
            post.side_effect = successful_delivery
            self.assertEqual(self.draft.command_create_or_update(self.args()), 0)
        data = json.loads(self.registry.read_text())[0]
        evidence = data["custom"]["wechat"]["evidence"]["draft_created"]
        self.assertEqual(evidence["fingerprint"], before_fingerprint)
        self.assertNotEqual(evidence["fingerprint"], workflow_fingerprint(data, "wechat", self.root))

    def test_missing_registry_or_mismatched_path_blocks_before_credentials(self):
        ctx = self.context()
        data = record()
        data["custom"]["wechat"]["path"] = "wechat/articles/draft-public-safe/another.md"
        for registry_exists in (True, False):
            with self.subTest(registry_exists=registry_exists):
                if registry_exists:
                    self.write_registry([data])
                else:
                    self.registry.unlink()
                before = self.snapshot()
                with (
                    mock.patch.object(self.draft, "build_context", return_value=ctx),
                    mock.patch.object(self.draft, "validate_context", return_value=[]),
                    mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")),
                    self.assertRaises(RuntimeError),
                ):
                    self.draft.command_create_or_update(self.args())
                self.assertEqual(before, self.snapshot())

    def test_missing_private_historical_id_requires_explicit_new_copy(self):
        ctx = self.context()
        data = record()
        data["custom"]["wechat"]["status"] = "draft_created"
        self.write_registry([data])
        before = self.snapshot()
        with (
            mock.patch.object(self.draft, "build_context", return_value=ctx),
            mock.patch.object(self.draft, "validate_context", return_value=[]),
            mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")),
            self.assertRaisesRegex(RuntimeError, "restore the private draft mapping"),
        ):
            self.draft.command_create_or_update(self.args())
        self.assertEqual(before, self.snapshot())
        args = self.args()
        args.new_copy = True
        with self.live_stub(ctx, {"media_id": "explicit-new-copy"}):
            self.assertEqual(self.draft.command_create_or_update(args), 0)
        self.assertEqual(self.draft.existing_draft_media_id(self.backlog, "ref-example"), "explicit-new-copy")

    def test_invalid_private_map_does_not_silently_create_duplicate(self):
        private_path = self.root / "wechat/.local/registry-drafts.json"
        private_path.parent.mkdir(parents=True, exist_ok=True)
        private_path.write_text("[]")
        with self.assertRaises(ValueError):
            self.draft.existing_draft_media_id(self.backlog, "ref-example")

    def write_private_mapping(self, records):
        path = self.root / "wechat/.local/registry-drafts.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(records), encoding="utf-8")
        return path

    def write_account_binding(self, *, selected="wx0000000000000000"):
        path = self.root / "wechat/.local/account.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"app_id": selected, "credential_source": "legacy-file"}))

    def test_private_mapping_resolves_update_without_reading_credentials(self):
        ctx = self.context()
        self.draft.save_private_draft(self.backlog, "ref-example", "synthetic-draft", "old-time", article_index=2, app_id="wx0000000000000000")
        with mock.patch.object(self.draft, "parse_front_matter", return_value={"body_images_upload_approved": "true"}), mock.patch.object(self.draft, "parse_cover_path", return_value=ctx.cover_path), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")):
            loaded = self.draft.build_context("ref-example", math_renderer="lightweight")
        self.assertEqual((loaded.action, loaded.existing_media_id, loaded.article_index, loaded.draft_mapping_source), ("update", "synthetic-draft", 2, "private"))

    def test_private_mapping_without_index_never_assumes_zero(self):
        self.draft.save_private_draft(self.backlog, "ref-example", "synthetic-draft", "old-time")
        mapping = self.draft.resolve_draft_mapping(self.backlog, "ref-example")
        self.assertIsNone(mapping["article_index"])
        self.assertEqual(mapping["source"], "private")

    def test_existing_update_requires_private_binding_before_credentials(self):
        ctx = replace(self.context(existing_media_id="synthetic-draft"), draft_mapping_app_id="")
        with mock.patch.object(self.draft, "build_context", return_value=ctx), mock.patch.object(self.draft, "validate_context", return_value=[]), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")) as token, self.assertRaisesRegex(self.draft.ConfigurationError, "draft_account_unbound"):
            self.draft.command_create_or_update(self.args(update=True))
        token.assert_not_called()

    def test_private_update_preserves_selected_index_and_binding_in_writeback(self):
        ctx = replace(self.context(existing_media_id="synthetic-draft"), article_index=2)
        with self.live_stub(ctx, {"errcode": 0}) as post:
            self.assertEqual(self.draft.command_create_or_update(self.args(update=True)), 0)
        self.assertEqual(post.call_args.args[2]["index"], 2)
        mapping = self.draft.resolve_draft_mapping(self.backlog, "ref-example")
        self.assertEqual(mapping["source"], "private")
        self.assertEqual(mapping["article_index"], 2)
        self.assertEqual(mapping["app_id"], "wx0000000000000000")

    def test_content_source_audit_reads_selected_article_index(self):
        ctx = replace(self.context(existing_media_id="synthetic-draft"), article_index=1)
        with mock.patch.object(self.draft, "api_post_json", return_value={"news_item": [{"content_source_url": "https://example.org/wrong"}, {"content_source_url": ctx.content_source_url}]}):
            result = self.draft.audit_remote_content_source("fake-token", ctx)
        self.assertTrue(result["matches_expected"])

    def test_invalid_private_fields_and_duplicate_confirmed_targets_fail_closed(self):
        for item in [{"media_id": ""}, {"media_id": "synthetic-draft", "article_index": True}, {"media_id": "synthetic-draft", "article_index": -1}, {"media_id": "synthetic-draft", "access_token": "FAKE_ONLY"}, {"media_id": "synthetic-a", "wechat_draft_media_id": "synthetic-b"}]:
            with self.subTest(item=item):
                self.write_private_mapping({"ref-example": item})
                with self.assertRaises(ValueError):
                    self.draft.existing_draft_media_id(self.backlog, "ref-example")
        self.write_private_mapping({ref: {"media_id": "same-draft", "article_index": 2, "app_id": "wx0000000000000000"} for ref in ["ref-example", "ref-other"]})
        with self.assertRaises(ValueError):
            self.draft.existing_draft_media_id(self.backlog, "ref-example")

    def test_duplicate_private_keys_are_rejected_and_multi_article_draft_is_supported(self):
        path = self.write_private_mapping({})
        for contents in ['{"ref-example":{"media_id":"a","media_id":"b"}}', '{"ref-example":{"media_id":"a"},"ref-example":{"media_id":"b"}}']:
            path.write_text(contents)
            with self.assertRaises(ValueError):
                self.draft.read_private_drafts(self.backlog)
        records = {ref: {"media_id": "same-draft", "article_index": index, "app_id": "wx0000000000000000"} for index, ref in enumerate(["ref-example", "ref-other"])}
        self.write_private_mapping(records)
        self.assertEqual(self.draft.read_private_drafts(self.backlog), records)

    def test_stale_public_file_cannot_supply_or_replace_private_target(self):
        path = self.root / "wechat/data/draft-map.json"
        path.parent.mkdir(parents=True)
        path.write_text('[{"publication_ref":"ref-example","wechat_draft_media_id":"synthetic-public"}]')
        self.assertEqual(self.draft.existing_draft_media_id(self.backlog, "ref-example"), "")
        self.write_private_mapping({"ref-example": {"media_id": ""}})
        with self.assertRaises(ValueError):
            self.draft.existing_draft_media_id(self.backlog, "ref-example")

    def test_existing_private_mapping_blocks_duplicate_creation_before_credentials(self):
        ctx = self.context(existing_media_id="synthetic-draft")
        with mock.patch.object(self.draft, "build_context", return_value=ctx), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")) as token, self.assertRaises(RuntimeError):
            self.draft.command_create_or_update(self.args())
        token.assert_not_called()

    def test_private_account_mismatch_still_blocks_after_successful_writeback(self):
        ctx = replace(self.context(existing_media_id="synthetic-draft"), article_index=2)
        with self.live_stub(ctx, {"errcode": 0}):
            self.draft.command_create_or_update(self.args(update=True))
        self.write_account_binding(selected="wx1111111111111111")
        with mock.patch.object(self.draft, "build_context", return_value=ctx), mock.patch.object(self.draft, "validate_context", return_value=[]), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")) as token, self.assertRaisesRegex(self.draft.ConfigurationError, "account_mismatch"):
            self.draft.command_create_or_update(self.args(update=True))
        token.assert_not_called()

    def test_audit_requires_binding_before_network_or_credentials(self):
        ctx = replace(self.context(existing_media_id="synthetic-draft"), draft_mapping_app_id="")
        args = SimpleNamespace(all=False, publication_ref="ref-example", theme="academic-clean", math_renderer="lightweight")
        with mock.patch.object(self.draft, "build_context", return_value=ctx), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")) as token, self.assertRaises(self.draft.ConfigurationError):
            self.draft.command_audit_content_source(args)
        token.assert_not_called()

    def test_unknown_private_article_index_blocks_update_before_credentials(self):
        ctx = replace(self.context(existing_media_id="synthetic-draft"), article_index=None)
        with mock.patch.object(self.draft, "build_context", return_value=ctx), mock.patch.object(self.draft, "validate_context", return_value=[]), mock.patch.object(self.draft, "fetch_access_token", side_effect=AssertionError("credential read")) as token, self.assertRaisesRegex(self.draft.ConfigurationError, "draft_article_index_unverified"):
            self.draft.command_create_or_update(self.args(update=True))
        token.assert_not_called()


if __name__ == "__main__":
    unittest.main()
