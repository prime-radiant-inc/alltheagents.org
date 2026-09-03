"""Tests for scripts/entrybot. Run: python3 -m unittest scripts/tests/test_entry_bot.py -v"""
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
ROOT = SCRIPTS.parent
FIXTURES = HERE / "fixtures"
sys.path.insert(0, str(SCRIPTS))

from entrybot import forms  # noqa: E402

ADD_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "add-agent.yml"
FIX_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "update-agent.yml"


class FormsTest(unittest.TestCase):
    def test_parse_add_fixture(self):
        fields = forms.parse_add((FIXTURES / "add.md").read_text(), ADD_TEMPLATE)
        self.assertEqual(fields["name"], "Foo Agent")
        self.assertEqual(fields["url"], "https://foo.dev")
        self.assertIsNone(fields["license"])
        self.assertEqual(fields["category"], "agent")
        self.assertEqual(fields["platforms"], ["CLI", "Web"])
        self.assertEqual(fields["extensibility"], ["MCP", "Hooks"])
        self.assertEqual(fields["pricing"], "BYOK")
        self.assertIn("air-gapped", fields["narrative"])
        self.assertNotIn("confirm", fields)

    def test_parse_fix_fixture(self):
        parsed = forms.parse_fix((FIXTURES / "fix.md").read_text(), FIX_TEMPLATE)
        self.assertEqual(parsed["slug_hint"], "cline")
        self.assertEqual(
            parsed["changes"],
            [
                {"field": "license", "old": "Apache-2.0", "new": "MIT"},
                {"field": "maintained", "old": "active", "new": "dormant"},
            ],
        )
        self.assertEqual(parsed["unparsed"], ["this line is not a change"])
        self.assertIsNone(parsed["fields"]["category"])
        self.assertEqual(parsed["fields"]["source"], "https://github.com/cline/cline/blob/main/LICENSE")


if __name__ == "__main__":
    unittest.main()
