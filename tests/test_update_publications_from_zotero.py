from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/update-publications-from-zotero.py"


def load_publication_script():
    spec = importlib.util.spec_from_file_location("update_publications_from_zotero", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load publication updater")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_item(extra: str | None, creators: list[dict[str, str]], bib: str) -> dict[str, object]:
    return {
        "key": "TEST1234",
        "data": {
            "extra": extra,
            "creators": creators,
            "publicationTitle": "Journal of Tests",
        },
        "bib": bib,
    }


class UpdatePublicationsFromZoteroTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.updater = load_publication_script()

    def test_corresponding_author_tag_marks_group_leader(self) -> None:
        item = make_item(
            "🏷️ _通讯作者、Wind engineering",
            [
                {"firstName": "Lingwei", "lastName": "Chen", "creatorType": "author"},
                {"firstName": "Chao", "lastName": "Li", "creatorType": "author"},
            ],
            "Chen Lingwei; Li Chao, Example[J]. Journal of Tests, 2024.",
        )

        rendered = self.updater.rendered_entry(item, 1)

        self.assertIn(":student-first-author:`Chen Lingwei`; **Li Chao**\\*, Example[J]. **Journal of Tests**", rendered)
        self.assertEqual(self.updater.corresponding_author_display_names(item), ["Li Chao"])

    def test_explicit_corresponding_author_marks_named_author(self) -> None:
        item = make_item(
            "通讯作者: Gang Hu",
            [
                {"firstName": "Lingwei", "lastName": "Chen", "creatorType": "author"},
                {"firstName": "Chao", "lastName": "Li", "creatorType": "author"},
                {"firstName": "Gang", "lastName": "Hu", "creatorType": "author"},
            ],
            "Chen Lingwei; Li Chao; Hu Gang, Example[J]. Journal of Tests, 2024.",
        )

        rendered = self.updater.rendered_entry(item, 1)

        self.assertIn(":student-first-author:`Chen Lingwei`; **Li Chao**; Hu Gang\\*, Example[J]", rendered)
        self.assertEqual(self.updater.corresponding_author_display_names(item), ["Hu Gang"])

    def test_existing_star_is_not_duplicated(self) -> None:
        item = make_item(
            "🏷️ _通讯作者",
            [{"firstName": "Chao", "lastName": "Li", "creatorType": "author"}],
            "Li Chao*, Example[J]. Journal of Tests, 2024.",
        )

        rendered = self.updater.rendered_entry(item, 1)

        self.assertIn("**Li Chao**\\*, Example[J]", rendered)
        self.assertNotIn("\\*\\*", rendered)


if __name__ == "__main__":
    unittest.main()
