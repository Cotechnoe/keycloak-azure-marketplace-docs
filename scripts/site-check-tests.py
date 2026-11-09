#!/usr/bin/env python3
"""Regression tests against an isolated copy of the real Jekyll build."""

import contextlib
import importlib.util
import io
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("site_check", ROOT / "scripts/site-check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class SiteCheckTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="jekyll-validation-")
        self.addCleanup(self.directory.cleanup)
        CHECK.ROOT = Path(self.directory.name).resolve()
        CHECK.SITE = CHECK.ROOT / "_site"
        shutil.copytree(ROOT / "_site", CHECK.SITE)
        shutil.copytree(ROOT / "docs", CHECK.ROOT / "docs")
        for source in ROOT.glob("*.md"):
            shutil.copy2(source, CHECK.ROOT / source.name)
        shutil.copy2(ROOT / "_config.yml", CHECK.ROOT / "_config.yml")

    def validate(self):
        with contextlib.redirect_stdout(io.StringIO()):
            CHECK.validate()

    def change(self, relative, old, new):
        path = CHECK.SITE / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_valid_site(self):
        self.validate()

    def test_missing_translation(self):
        (CHECK.SITE / "QUICKSTART-fr.html").unlink()
        with self.assertRaisesRegex(ValueError, "HTML pages"):
            self.validate()

    def test_broken_content_link(self):
        self.change("index.html", 'href="/keycloak-azure-marketplace-docs/fr/"',
                    'href="/keycloak-azure-marketplace-docs/missing/"')
        with self.assertRaisesRegex(ValueError, "rendered link destinations"):
            self.validate()

    def test_wrong_navigation_language(self):
        self.change("fr/index.html", 'href="/keycloak-azure-marketplace-docs/QUICKSTART-fr.html"',
                    'href="/keycloak-azure-marketplace-docs/QUICKSTART.html"')
        with self.assertRaisesRegex(ValueError, "main navigation language"):
            self.validate()

    def test_internal_file_leak(self):
        (CHECK.SITE / "internal.txt").write_text("internal note", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Unexpected files"):
            self.validate()

    def test_missing_skip_target(self):
        self.change("index.html", 'id="main"', 'id="absent"')
        with self.assertRaisesRegex(ValueError, "Missing fragment"):
            self.validate()


if __name__ == "__main__":
    unittest.main()
