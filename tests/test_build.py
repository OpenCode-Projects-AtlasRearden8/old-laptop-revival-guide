import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build

LICENSE_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"
SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{16,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"(?i)\b(api[_-]?key|apikey|secret|token)\b\s*[:=]\s*['\"]?[A-Za-z0-9._-]{8,}",
    r"(?i)\bBearer\s+[A-Za-z0-9._-]{16,}",
]
ALLOWED_TOP_LEVEL = {
    ".git",
    ".gitignore",
    "LICENSE",
    "README.md",
    "STATUS.md",
    "docs",
    "scripts",
    "site",
    "tests",
}


class TagBalance(HTMLParser):
    VOID = {"meta", "link", "br", "hr", "img", "input"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.problems = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.problems.append("mismatch: %s (stack %s)" % (tag, self.stack[-3:]))
        else:
            self.stack.pop()


def balanced(html_text):
    parser = TagBalance()
    parser.feed(html_text)
    if parser.stack:
        parser.problems.append("unclosed: %s" % parser.stack)
    return parser.problems


class ConverterTests(unittest.TestCase):
    def test_heading_gets_slug_id(self):
        html = build.markdown_to_html("# Chapter 1 — Backup First")
        self.assertIn('<h1 id="chapter-1-backup-first">', html)

    def test_duplicate_heading_slugs_unique(self):
        html = build.markdown_to_html("## Slow\n## Slow")
        self.assertIn('id="slow"', html)
        self.assertIn('id="slow-1"', html)

    def test_inline_formatting(self):
        html = build.markdown_to_html("plain **bold** and *italic* and `code`")
        self.assertIn("<strong>bold</strong>", html)
        self.assertIn("<em>italic</em>", html)
        self.assertIn("<code>code</code>", html)

    def test_html_escaped(self):
        html = build.markdown_to_html("typing <script>alert('x')</script> here")
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)

    def test_code_fence_escaped(self):
        html = build.markdown_to_html("```bash\necho '<b>&</b>'\n```")
        self.assertIn("<pre><code", html)
        self.assertNotIn("<b>", html)

    def test_link_to_doc_maps_to_html(self):
        html = build.markdown_to_html("[see](07-retire-or-donate.md)", link_map={"07-retire-or-donate.md": "07-retire-or-donate.html"})
        self.assertIn('<a href="07-retire-or-donate.html">', html)

    def test_external_link_untouched(self):
        html = build.markdown_to_html("[ollama](https://ollama.com)")
        self.assertIn('href="https://ollama.com"', html)

    def test_anchor_link_untouched(self):
        html = build.markdown_to_html("[down](#chapter-2)")
        self.assertIn('<a href="#chapter-2">', html)

    def test_checkbox_lists(self):
        html = build.markdown_to_html("- [ ] unchecked\n- [x] done")
        self.assertIn('<li class="todo">☐ unchecked</li>', html)
        self.assertIn('<li class="done">☑ done</li>', html)
        self.assertIn('<ul class="checklist">', html)

    def test_numbered_list(self):
        html = build.markdown_to_html("1. first\n2. second")
        self.assertIn("<ol>", html)
        self.assertIn("<li>first</li>", html)

    def test_table(self):
        html = build.markdown_to_html("| A | B |\n| --- | --- |\n| 1 | 2 |")
        self.assertIn("<th>A</th>", html)
        self.assertIn("<td>1</td>", html)

    def test_blockquote(self):
        html = build.markdown_to_html("> **Wait a second:** hold the line")
        self.assertIn("<blockquote>", html)
        self.assertIn("<strong>Wait a second:</strong>", html)

    def test_horizontal_rule(self):
        html = build.markdown_to_html("above\n\n---\n\nbelow")
        self.assertIn("<hr>", html)

    def test_paragraph_joins_soft_lines(self):
        html = build.markdown_to_html("one line\ncontinues here")
        self.assertIn("<p>one line\ncontinues here</p>", html)

    def test_title_collected(self):
        collect = {}
        build.markdown_to_html("# My Title", collect=collect)
        self.assertEqual(collect["title"], "My Title")


class BuilderTests(unittest.TestCase):
    DOCS = {
        "00-read-this-first.md": "# Read This First\n\nWelcome to the trip.\n",
        "01-backup.md": "# Chapter 1 — Backup\n\nSave things. [go](02-more.md)\n",
        "02-more.md": "# Chapter 2 — More\n\n[up](#chapter-1-more)\n## chapter 1 more\n",
    }

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.docs = self.base / "docs"
        self.docs.mkdir()
        for name, text in self.DOCS.items():
            (self.docs / name).write_text(text, encoding="utf-8")
        self.out = self.base / "site"

    def tearDown(self):
        self.tmp.cleanup()

    def build(self):
        entries, link_map = build.gather_docs(self.docs)
        made = build.build(entries, link_map, self.out)
        return made, entries, link_map

    def test_gather_docs_front_matter_numbering(self):
        _, entries, _ = self.build()
        numbers = [e["number"] for e in entries]
        self.assertEqual(numbers, [None, 1, 2])

    def test_made_files(self):
        made, _, _ = self.build()
        self.assertIn("index.html", made)
        self.assertIn("book.html", made)
        self.assertIn("style.css", made)
        self.assertEqual(len(made), 6)

    def test_pages_are_well_formed_and_script_free(self):
        self.build()
        for page in self.out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertEqual(balanced(text), [], page.name)
            self.assertNotIn("<script", text, page.name)

    def test_sidebar_links_chapters(self):
        self.build()
        page = (self.out / "02-more.html").read_text(encoding="utf-8")
        for stem in ("00-read-this-first", "01-backup", "02-more"):
            self.assertIn(stem + ".html", page)

    def test_book_contains_all_chapters(self):
        self.build()
        book = (self.out / "book.html").read_text(encoding="utf-8")
        self.assertIn("Read This First", book)
        self.assertIn("Chapter 1 of 10", book)
        self.assertIn("Chapter 2 of 10", book)

    def test_build_is_reproducible(self):
        self.build()
        first = {p.name: p.read_bytes() for p in sorted(self.out.iterdir())}
        shutil.rmtree(self.out)
        self.build()
        second = {p.name: p.read_bytes() for p in sorted(self.out.iterdir())}
        self.assertEqual(list(first), list(second))
        self.assertEqual(first, second)

    def test_style_sheet_contains_no_external_urls(self):
        self.build()
        css = (self.out / "style.css").read_text(encoding="utf-8")
        self.assertNotIn("http://", css)
        self.assertNotIn("https://", css)

    def test_check_detects_broken_anchor(self):
        (self.docs / "02-more.md").write_text("# Chapter 2 — More\n\n[bad](#no-such-anchor)\n", encoding="utf-8")
        problems, count = build.check_docs(self.docs)
        self.assertTrue(any("no-such-anchor" in p for p in problems))
        self.assertEqual(count, 3)

    def test_check_detects_missing_target(self):
        (self.docs / "02-more.md").write_text("# Chapter 2 — More\n\n[bad](99-nowhere.md)\n", encoding="utf-8")
        problems, _ = build.check_docs(self.docs)
        self.assertTrue(any("99-nowhere.md" in p for p in problems))

    def test_check_passes_on_real_docs(self):
        problems, count = build.check_docs(ROOT / "docs")
        self.assertEqual(problems, [])
        self.assertEqual(count, 11)


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build.py"), *args],
            capture_output=True,
            text=True,
        )

    def test_check_real_docs_clean(self):
        proc = self.run_cli("--check")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("clean", proc.stdout)

    def test_from_md_prints_fragment(self):
        proc = self.run_cli("--from-md", str(ROOT / "docs" / "09-faq.md"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("<h1", proc.stdout)
        self.assertNotIn("<!DOCTYPE", proc.stdout)

    def test_from_md_missing_file_errors(self):
        proc = self.run_cli("--from-md", "/nonexistent/nope.md")
        self.assertNotEqual(proc.returncode, 0)

    def test_build_to_temp_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "site"
            proc = self.run_cli("--out", str(out))
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertTrue((out / "index.html").exists())
            self.assertTrue((out / "book.html").exists())
            self.assertTrue((out / "style.css").exists())
            manifest = "\n".join(sorted(p.name for p in out.iterdir()))
            self.assertIn("00-read-this-first.html", manifest)

    def test_check_exit_code_on_broken_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            docs.mkdir()
            (docs / "01-x.md").write_text("# X\n\n[broken](01-x.md#missing)\n", encoding="utf-8")
            proc = self.run_cli("--check", "--docs", str(docs))
            self.assertEqual(proc.returncode, 1)
            self.assertIn("problem", proc.stderr)


class HygieneTests(unittest.TestCase):
    def text_files(self):
        paths = []
        for folder in ("docs", "scripts", "tests"):
            paths.extend((ROOT / folder).glob("**/*"))
        for name in ("README.md", "LICENSE"):
            paths.append(ROOT / name)
        return [p for p in paths if p.is_file() and p.suffix in (".md", ".py", ".css", "") or p.name == "LICENSE"]

    def test_license_line_exact(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn(LICENSE_LINE, text)
        self.assertTrue((ROOT / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"))

    def test_readme_credits_company(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)
        self.assertIn("Dylan Asdale", readme)

    def test_no_secrets(self):
        offenders = []
        for path in self.text_files():
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                if re.search(pattern, text):
                    offenders.append((path.name, pattern))
        self.assertEqual(offenders, [])

    def test_top_level_files_expected(self):
        present = {p.name for p in ROOT.iterdir()}
        unexpected = present - ALLOWED_TOP_LEVEL
        self.assertEqual(unexpected, set())

    def test_gitignore_exists(self):
        self.assertTrue((ROOT / ".gitignore").exists())
        self.assertIn("site/", (ROOT / ".gitignore").read_text(encoding="utf-8"))

    def test_documentation_mentions_companion(self):
        docs_text = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "docs").glob("*.md"))
        self.assertIn("The Local AI Handbook", docs_text)

    def test_site_builds_clean_from_current_docs(self):
        problems, _ = build.check_docs(ROOT / "docs")
        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
