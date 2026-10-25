import argparse
import html
import re
import shutil
import sys
from pathlib import Path

SITE_TITLE = "The Old Laptop Revival Guide"
SITE_TAGLINE = "A calm, plain-English manual for turning a tired laptop into a useful AI machine."
COMPANION_NOTE = (
    "This is the laptop half of the story. Its companion, The Local AI Handbook "
    "(free), covers the AI half: models, RAM, chat, and privacy."
)
FOOTER = "The Old Laptop Revival Guide — published free by Asdale Dynamics, LLC (MIT License)"

EMOJI_RE = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\u0400-\u04ff]")
CODE_FENCE_RE = re.compile(r"^```(\w*)\s*$")
HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$")
BULLET_RE = re.compile(r"^(\s*)[-*]\s+\[( |x|X)\]\s+(.*)$")
BULLET_PLAIN_RE = re.compile(r"^(\s*)[-*]\s+(.*)$")
NUMBERED_RE = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
QUOTE_RE = re.compile(r"^>\s?(.*)$")
TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
CODESPAN_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*\s][^*]*)\*(?!\*)")


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def strip_md(text):
    text = CODESPAN_RE.sub(r"\1", text)
    text = BOLD_RE.sub(r"\1", text)
    text = ITALIC_RE.sub(r"\1", text)
    text = LINK_RE.sub(r"\1", text)
    return text


class _InlineRenderer:
    def __init__(self, link_map, page_stem, anchors):
        self.link_map = link_map or {}
        self.page_stem = page_stem
        self.anchors = anchors if anchors is not None else set()

    def render(self, raw):
        codes = []

        def keep(m):
            codes.append(m.group(1))
            return "\x00{0}\x00".format(len(codes) - 1)

        text = CODESPAN_RE.sub(keep, raw)
        text = html.escape(text, quote=False)
        text = LINK_RE.sub(self._link, text)
        text = BOLD_RE.sub(r"<strong>\1</strong>", text)
        text = ITALIC_RE.sub(r"<em>\1</em>", text)
        for i, code in enumerate(codes):
            text = text.replace(
                "\x00{0}\x00".format(i),
                "<code>" + html.escape(code, quote=False) + "</code>",
            )
        return text

    def _link(self, m):
        label = m.group(1)
        url = m.group(2)
        href = self._resolve(url)
        return '<a href="{0}">{1}</a>'.format(html.escape(href, quote=False), label)

    def _resolve(self, url):
        if url.startswith("#") or url.startswith(("http://", "https://", "mailto:")):
            return url
        return self.link_map.get(url, url)


def markdown_to_html(markdown_text, link_map=None, page_stem=None, collect=None):
    """Purposeful Markdown subset: headings, paragraphs, fences, quotes,
    lists (including checkboxes), tables, and rules."""
    link_map = link_map or {}
    anchors = set()
    renderer = _InlineRenderer(link_map, page_stem, anchors)
    lines = markdown_text.splitlines()
    out = []
    para = []

    def flush_para():
        if para:
            out.append("<p>%s</p>" % renderer.render("\n".join(para).strip()))
            para.clear()

    def flush_list(stack):
        while stack:
            out.append("</ul>" if stack.pop() == "ul" else "</ol>")

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        fence = CODE_FENCE_RE.match(line)
        if fence:
            flush_para()
            lang = fence.group(1) or ""
            body = []
            i += 1
            closed = False
            while i < n:
                if lines[i].startswith("```"):
                    closed = True
                    break
                body.append(lines[i])
                i += 1
            cls = ' class="language-{0}"'.format(lang) if lang else ""
            out.append("<pre><code%s>%s</code></pre>" % (cls, html.escape("\n".join(body))))
            i += 1
            continue

        heading = HEADING_RE.match(line)
        if heading:
            flush_para()
            level = len(heading.group(1))
            raw = heading.group(2).strip()
            anchor = slugify(strip_md(raw))
            while anchor in anchors:
                anchor += "-1"
            anchors.add(anchor)
            text = renderer.render(raw)
            out.append('<h{0} id="{1}">{2}</h{0}>'.format(level, anchor, text))
            if collect is not None and level == 1:
                collect["title"] = strip_md(raw)
            i += 1
            continue

        if re.match(r"^\s*(?:(\*|[-_])\s*){3,}$", line) and not para:
            flush_para()
            out.append("<hr>")
            i += 1
            continue

        if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
            flush_para()
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(render_table(rows, renderer))
            continue

        quote = QUOTE_RE.match(line)
        if quote:
            flush_para()
            body = []
            while i < n:
                q = QUOTE_RE.match(lines[i])
                if q and q.group(1).strip():
                    body.append(q.group(1))
                    i += 1
                elif not lines[i].strip():
                    i += 1
                    break
                else:
                    break
            inner = "<br>".join(renderer.render(b) for b in body)
            out.append("<blockquote><p>%s</p></blockquote>" % inner)
            continue

        bullet = BULLET_RE.match(line)
        plain = BULLET_PLAIN_RE.match(line)
        numbered = NUMBERED_RE.match(line)
        if bullet or plain or numbered:
            flush_para()
            items = []
            while i < n:
                cur = lines[i]
                b = BULLET_RE.match(cur)
                p = BULLET_PLAIN_RE.match(cur)
                m = NUMBERED_RE.match(cur)
                if b:
                    state = "input" if b.group(2) == " " else "done"
                    items.append(("ul", b.group(1), state, b.group(3)))
                    i += 1
                elif p:
                    items.append(("ul", p.group(1), None, p.group(2)))
                    i += 1
                elif m:
                    items.append(("ol", m.group(1), None, m.group(3)))
                    i += 1
                else:
                    blankish = not cur.strip()
                    if blankish and i + 1 < n and (
                        BULLET_PLAIN_RE.match(lines[i + 1]) or NUMBERED_RE.match(lines[i + 1])
                    ):
                        i += 1
                        continue
                    break
            out.append(render_list(items, renderer))
            continue

        if not line.strip():
            flush_para()
        else:
            para.append(line)
        i += 1

    flush_para()
    text = "\n".join(out)
    if collect is not None:
        collect.setdefault("title", SITE_TITLE)
    return text


def render_table(rows, renderer):
    def parse(row):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        return cells

    head = parse(rows[0])
    body_start = 1
    if len(rows) > 1 and TABLE_SEP_RE.match(rows[1]):
        body_start = 2
    pieces = ["<table><thead><tr>"]
    for cell in head:
        pieces.append("<th>%s</th>" % renderer.render(strip_md(cell)))
    pieces.append("</tr></thead>")
    if len(rows) > body_start:
        pieces.append("<tbody>")
        for row in rows[body_start:]:
            cells = parse(row)
            pieces.append("<tr>")
            for cell in cells:
                pieces.append("<td>%s</td>" % renderer.render(cell))
            pieces.append("</tr>")
        pieces.append("</tbody>")
    pieces.append("</table>")
    return "".join(pieces)


def render_list(items, renderer):
    parts = []
    current = None
    for kind, indent, checkbox, text in items:
        if kind != current:
            if current is not None:
                parts.append("</%s>" % current)
            current = kind
            parts.append('<ul class="checklist">' if kind == "ul" else "<ol>")
        if checkbox is None:
            parts.append("<li>%s</li>" % renderer.render(text))
        elif checkbox == "input":
            parts.append('<li class="todo">☐ %s</li>' % renderer.render(text))
        else:
            parts.append('<li class="done">☑ %s</li>' % renderer.render(text))
    if current is not None:
        parts.append("</%s>" % current)
    return "".join(parts)


def gather_docs(docs_dir):
    docs = sorted(
        (p for p in docs_dir.glob("*.md") if p.name[0] not in (".", "_")),
        key=lambda p: p.name,
    )
    entries = []
    for path in docs:
        stem = path.stem
        collect = {"title": None}
        html_body = markdown_to_html(path.read_text(encoding="utf-8"), collect=collect)
        number = None
        m = re.match(r"^(\d\d)-", stem)
        if m:
            number = int(m.group(1)) or None
        label = strip_md(collect["title"] or stem)
        entries.append(
            {
                "stem": stem,
                "title": collect["title"] or stem,
                "label": label,
                "number": number,
                "body": html_body,
                "path": path,
            }
        )
    link_map = {e["stem"] + ".md": e["stem"] + ".html" for e in entries}
    return entries, link_map


def page_shell(title, body_html, sidebar="", base=""):
    return PAGE_TEMPLATE.format(title=title, sidebar=sidebar, body=body_html, base=base, footer=html.escape(FOOTER))


def short_label(entry):
    if entry["number"] is None:
        return "Read this first"
    return re.sub(r"^Chapter \d+\s*[—-]\s*", "", entry["label"])


def sidebar_html(entries, active_stem):
    rows = []
    for e in entries:
        href = e["stem"] + ".html"
        display = short_label(e)
        class_attr = ' class="active"' if e["stem"] == active_stem else ""
        rows.append('<li%s><a href="%s">%s</a></li>' % (class_attr, href, html.escape(display)))
    return '<nav class="sidebar"><h2 class="sidebar-title"><a href="index.html">%s</a></h2><ul>%s</ul></nav>' % (
        html.escape(SITE_TITLE),
        "\n".join(rows),
    )


def build(entries, link_map, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for e in entries:
        sidebar = sidebar_html(entries, e["stem"])
        idx = [i for i, x in enumerate(entries) if x["stem"] == e["stem"]][0]
        prev = entries[idx - 1] if idx > 0 else None
        nxt = entries[idx + 1] if idx + 1 < len(entries) else None
        nav = []
        if prev:
            nav.append('<a class="prev" href="%s.html">← %s</a>' % (prev["stem"], html.escape(prev["label"])))
        if nxt:
            nav.append('<a class="next" href="%s.html">%s →</a>' % (nxt["stem"], html.escape(nxt["label"])))
        pager = '<div class="pager">%s</div>' % "\n".join(nav)
        number_label = "Front matter" if e["number"] is None else "Chapter %d of 10" % e["number"]
        body = '<main class="content"><p class="kicker">%s</p>%s%s</main>' % (
            html.escape(number_label),
            e["body"],
            pager,
        )
        title = e["title"]
        page = page_shell(title + " · " + SITE_TITLE, body, sidebar)
        (out_dir / (e["stem"] + ".html")).write_text(page, encoding="utf-8")
        made.append(e["stem"] + ".html")

    toc = []
    for e in entries:
        number_label = "Read this first" if e["number"] is None else "Chapter %d of 10" % e["number"]
        if e["number"] is None:
            toc.append('<li><a href="%s.html"><strong>Read this first</strong></a></li>' % e["stem"])
        else:
            toc.append(
                '<li><a href="%s.html"><strong>%s</strong> — %s</a></li>'
                % (e["stem"], html.escape(number_label), html.escape(short_label(e)))
            )
    landing_body = """<div class="hero">
<h1>%s</h1>
<p class="tagline">%s</p>
<p class="companion">%s</p>
<ul class="cta">
<li><a class="big" href="00-read-this-first.html">Start with Read This First</a></li>
<li><a class="big ghost" href="book.html">Open the whole book (one page, printable)</a></li>
</ul>
</div>
<h2>The trip, chapter by chapter</h2>
<ol class="toc">
%s
</ol>
<p class="fine">No JavaScript, no tracking, no network requests: this site works offline, straight from a browser.</p>""" % (
        html.escape(SITE_TITLE),
        html.escape(SITE_TAGLINE),
        html.escape(COMPANION_NOTE),
        "\n".join(toc),
    )
    page = page_shell(SITE_TITLE, landing_body, "")
    (out_dir / "index.html").write_text(page, encoding="utf-8")
    made.append("index.html")

    book_parts = []
    for e in entries:
        number_label = "Front matter" if e["number"] is None else "Chapter %d of 10" % e["number"]
        book_parts.append('<section class="chapter"><p class="kicker">%s</p>%s</section>' % (html.escape(number_label), e["body"]))
    book_body = '<main class="content book"><h1 class="book-title">%s</h1><p class="tagline">%s</p>%s</main>' % (
        html.escape(SITE_TITLE),
        html.escape(SITE_TAGLINE),
        "\n".join(book_parts),
    )
    page = page_shell(SITE_TITLE + " — the whole book", book_body, "")
    (out_dir / "book.html").write_text(page, encoding="utf-8")
    made.append("book.html")

    css_path = Path(__file__).parent / "style.css"
    (out_dir / "style.css").write_text(css_path.read_text(encoding="utf-8"), encoding="utf-8")
    made.append("style.css")
    return sorted(made)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{base}style.css">
</head>
<body>
{sidebar}
{body}
<footer>{footer}</footer>
</body>
</html>
"""


def check_docs(docs_dir):
    entries, _ = gather_docs(docs_dir)
    problems = []
    stems = {e["stem"] + ".md" for e in entries}
    expected = [None] + list(range(1, 11))
    seen = [e["number"] for e in entries]
    if seen != expected:
        problems.append("chapter numbering is off; found files with numbers: %s" % seen)
    for e in entries:
        text = e["path"].read_text(encoding="utf-8")
        if not text.startswith("# "):
            problems.append("%s: does not start with a # heading" % e["path"].name)
        if EMOJI_RE.search(text):
            problems.append("%s: contains non-Latin characters" % e["path"].name)
        lines = text.splitlines()
        depth = 0
        for ln, line in enumerate(lines, start=1):
            if CODE_FENCE_RE.match(line):
                depth = 1 - depth
            elif EMOJI_RE.search(line):
                problems.append("%s:%d: unexpected characters" % (e["path"].name, ln))
        if depth:
            problems.append("%s: unclosed code fence" % e["path"].name)
        anchors = set()
        for m in HEADING_RE.finditer(text):
            anchors.add(slugify(strip_md(m.group(2).strip())))
        for m in LINK_RE.finditer(text):
            label, url = m.group(1), m.group(2)
            if url.startswith("#"):
                if url[1:] not in anchors:
                    problems.append("%s: broken local anchor %s" % (e["path"].name, url))
            elif not url.startswith(("http://", "https://", "mailto:")):
                if url not in stems:
                    problems.append("%s: link target not in docs: %s" % (e["path"].name, url))
    if problems:
        return problems, len(entries)
    return [], len(entries)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the static site from docs/ Markdown.")
    parser.add_argument("--docs", default="docs", help="markdown source directory")
    parser.add_argument("--out", default="site", help="output directory")
    parser.add_argument("--check", action="store_true", help="lint the docs and exit")
    parser.add_argument("--from-md", dest="from_md", metavar="FILE", help="convert one markdown file to HTML on stdout")
    args = parser.parse_args(argv)

    if args.from_md:
        path = Path(args.from_md)
        if not path.exists():
            parser.error("file not found: %s" % args.from_md)
        text = path.read_text(encoding="utf-8")
        collect = {"title": None}
        body = markdown_to_html(text, collect=collect)
        print(body)
        return 0

    docs_dir = Path(args.docs)
    if not docs_dir.exists():
        print("docs directory not found: %s" % docs_dir, file=sys.stderr)
        return 2

    if args.check:
        problems, count = check_docs(docs_dir)
        if problems:
            for p in problems:
                print("problem: %s" % p, file=sys.stderr)
            print("Checked %d markdown files: %d problem(s)" % (count, len(problems)), file=sys.stderr)
            return 1
        print("Checked %d markdown files: clean" % count)
        return 0

    entries, link_map = gather_docs(docs_dir)
    out_dir = Path(args.out)
    made = build(entries, link_map, out_dir)
    print("Built %d files into %s" % (len(made), out_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
