# STATUS

Project: The Old Laptop Revival Guide
Owner: Asdale Dynamics, LLC
State: complete and verified (October 2026)

## What was built

A beginner-facing, step-by-step manual for turning a tired old laptop into a useful local-AI machine — backup, wipe, lightweight Linux, Ollama with modest models, spare-room station setup, and honest retirement/donation — plus the tooling to turn it into a static website. It complements The Local AI Handbook (the sibling repo): the Handbook covers the AI half (models, RAM math, chat, privacy); this guide covers the *machine* half and defers overlapping depth to the Handbook rather than repeating it.

- **docs/** (11 Markdown files: front matter + 10 numbered chapters):
  - `00-read-this-first.md` — front matter: audience, needs list, conventions, five-minute taste, trip map.
  1. Backup First (rescue categories, external-drive copy, unplug-and-replug verification, passwords of the future, laptop-won't-boot paths)
  2. The Calm Wipe (HDD vs SSD, the encrypt-then-erase trick, Path A for revival via the installer, Path B for donation via reset tools or a live-USB wipe, account unlinking)
  3. Pick Your Linux (RAM-first decision, Mint Cinnamon/Xfce, Lubuntu, MX compared in one table, live-USB trick, official download + checksum)
  4. Install Day (ISO flashing with Etcher/Rufus, boot keys by brand, try-before-install, "Erase disk and install" vs dual-boot, first-boot checklist)
  5. Ollama on a Tired Laptop (one-command install, half-the-RAM model rule, starter-model table, three maintenance commands, pointer to The Local AI Handbook for depth)
  6. The Spare-Room Station (three jobs: writing table, printer wrangler, local-chat terminal; appliance habits; monthly rescue-copy ritual)
  7. Retire or Donate (honest math for reviving, part-out retirement, wipe-before-leaving, donation channels, swollen-battery safety)
  8. Hardware Checklist (printable, in project order: pre-flight, rescue-drive record, wipe day, install day, AI record, station record, retirement record, RAM-upgrade note)
  9. Troubleshooting FAQ (boot-key and USB-mode fixes, RAM and keyboard answers, live-mode Wi-Fi, `ollama: command not found`, download stalls, speed honesty, heat, printers, privacy one-liner)
  10. Glossary (plain-English machine/Linux/AI terms)
- **scripts/build.py**: standard-library-only static site builder. Zero dependencies, zero network. Produces a landing page, one polished page per chapter with sidebar navigation and prev/next pagers, a single-page "whole book" for printing/Ctrl+F, and a stylesheet (light/dark aware, print styles). `00-` stems are treated as front matter, so on-page kickers read "Front matter" and "Chapter N of 10", matching the book's internal numbering.
- **scripts/style.css**: the site stylesheet, copied into `site/` at build time.
- **CLI flags**: `--docs/--out` for custom paths, `--from-md FILE` to convert one chapter to HTML on stdout, `--check` to lint the docs (chapter numbering, headings, link targets, local anchors, closed code fences, non-Latin characters).
- **tests/test_build.py**: 37 tests covering the Markdown converter (headings, slugs, inline formatting, escaping, checkboxes, tables, fences, quotes, rules), the builder (numbering, file manifest, tag balance, no `<script>`, sidebar/book contents, reproducible builds), the CLI (all flags, exit codes), and repo hygiene (exact MIT line, README credit, secret-pattern scan, allowed top-level files, companion mentions).
- **README.md, LICENSE** (MIT, "Copyright (c) 2026 Asdale Dynamics, LLC"), **.gitignore**.

## How to run it

```bash
python3 scripts/build.py            # build site/ from docs/
python3 scripts/build.py --check    # lint docs (links, anchors, numbering)
python3 scripts/build.py --from-md docs/09-faq.md   # one chapter to stdout
python3 -m unittest discover -s tests   # run the test suite (37 tests)
```

Then open `site/index.html` in a browser — no server needed; the site makes no external requests, so it works offline and from file://. `site/book.html` is the whole book on one printable page.

## Verification results (run in this folder)

- `python3 --version` → Python 3.13.5
- `python3 scripts/build.py --check` → "Checked 11 markdown files: clean"
- `python3 scripts/build.py` → "Built 14 files into site" (13 HTML pages + style.css)
- HTML structural check (html.parser tag balance over all 14 generated pages) → 0 problems
- `python3 -m unittest discover -s tests` → 37 tests, OK (0 failures, 0 errors)
- Checkbox rendering verified on the built pages (`class="todo"` items with ☐ glyphs appear for every unchecked line in chapter 8)
- Reproducible-build test passes (two consecutive builds byte-identical)
- Secret-pattern scan across docs/scripts/tests/README/LICENSE → 0 matches
- Non-Latin character lint over docs → clean (only intentional dashes, arrows, ☐/☑, ⌘/⊞ key symbols)
- Git initialized with the existing configured identity (Dylan Asdale); repo committed, nothing pushed, no remote, no Co-authored-by trailers

## Fix-ups applied during this pass

- Several chapters accumulated garbled tokens or incomplete sentences while drafting (e.g. stray non-English characters, a truncated installer-question in the FAQ, a mangled GPT4All/Open WebUI setup block in chapter 6, and duplicated/Garbled logic in the first cut of chapter 3). Each was rewritten to be clean, honest, and consistent with the guide's one-voice style; the docs lint (non-Latin character check) now guards the character-level version of that mistake permanently.
- To avoid guessing at commands that change quickly (Open WebUI's install line, in particular), chapter 6 defers those steps to The Local AI Handbook's chapter 6 instead of quoting commands that could drift; the guide stays tested-local-first rather than pseudo-accurate.
- The converter's first cut mislabeled unchecked checkboxes as plain list items; fixed and covered by a test.
- The horizontal-rule regex required a standalone `---` line; fixed and covered by a test.
- Sidebar/TOC labels deduplicated ("Chapter 1 of 10 — Chapter 1 — Backup First" became "Chapter 1 of 10 — Backup First").

## Known gaps

- `site/` is a generated artifact and is gitignored; run `python3 scripts/build.py` after any docs change.
- No full-text search page; use `site/book.html` with browser Ctrl+F (deliberate: no JavaScript, no tracking).
- The Markdown converter is a purposeful subset (no images, footnotes, or definition lists; lists are flat, with checkbox support). Convention violations are caught by `--check` and the tests rather than silently rendered.
- HW/distro/model specifics (ISO sizes, model file sizes, requirements) are labeled approximate in-text and accurate as of October 2026; Ollama's model list drifts, so chapter 5 teaches the half-RAM rule rather than fixed favorites alone.
- Installer/download flows (Etcher, Rufus, Mint, Ollama) were not executed in this environment (none are needed to build or test the repo); steps follow the vendors' documented, widely-current flows.
- Donation programs and take-back schemes named in chapter 7 are examples, not endorsements; the chapter teaches the search pattern rather than a fixed list.
