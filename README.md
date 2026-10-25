# The Old Laptop Revival Guide

A calm, plain-English manual for turning a tired laptop into a useful AI machine — backing it up safely, wiping it without panic, picking a lightweight Linux that fits it, installing Ollama for modest models, and setting it up as a spare-room writing, printing, and local-chat station. Written the way a friend would explain it: step by step, honest trade-offs, never condescending.

Published as a free resource by [Asdale Dynamics, LLC](https://dylanasdale.github.io), the beginner-friendly AI education project of author Dylan Asdale.

## The one-sentence version

**Back it up, wipe it gently, dress it in lightweight Linux, give it one job, and it will serve for years — or thank it and let it go.**

This guide is the *laptop half* of the story. For the deep dive on running and chatting with local AI models, read the companion book, **The Local AI Handbook** (also free, also by Asdale Dynamics). This guide covers what has to happen to the machine itself, and points to the Handbook whenever the subjects overlap.

## Who this is for

- You have an old laptop doing nothing — frustratingly slow, out of updates, retired before its time.
- You are not a Linux expert. You might never have installed an operating system.
- You want your photos, letters, and browser data safely backed up *before* anything is erased.
- You want a machine for one real job: writing, printing, or talking to a small local AI model with no subscription and no cloud.

## What is inside

- **docs/** — the guide itself, one Markdown file per chapter. `00-read-this-first.md` is front matter; the numbered chapters run 1–10:
  1. Backup First (what to copy, how to verify it, why to be slow here)
  2. The Calm Wipe (secure erasure explained without fear, HDD vs SSD)
  3. Pick Your Linux (lightweight distros for old hardware, simply compared)
  4. Install Day (USB installer, try-before-install, partition patience)
  5. Ollama on a Tired Laptop (the short honest version, plus pointer to the Handbook)
  6. The Spare-Room Station (writing, printing, local chat — one machine, one job)
  7. Retire or Donate (when revival is not worth it, and how to let it go safely)
  8. Hardware Checklist (a printable pre-flight list)
  9. Troubleshooting FAQ (the questions that actually come up)
  10. Glossary (plain-English definitions)
- **scripts/build.py** — a standard-library-only static site builder. Converts the chapters into a polished, offline-friendly HTML site: a landing page, one page per chapter with sidebar navigation and prev/next links, and a single "whole book" page for printing or Ctrl+F. Requires nothing but Python 3.9+, needs no network, and makes zero external requests.
- **tests/test_build.py** — tests for the converter, the builder, the CLI, docs linting, and repo hygiene.
- **site/** — the generated site (built locally; gitignored, not committed).

## Quick start

Read it as plain text:

```bash
less docs/00-read-this-first.md
```

Build the static site (Python 3.9+, nothing else):

```bash
python3 scripts/build.py
```

Then open `site/index.html` in any browser — no server needed, no JavaScript, no network. Prefer the whole book on one page?

```bash
xdg-open site/book.html      # Linux (or: open site/book.html on macOS)
```

Lint the documentation (links, anchors, chapter structure):

```bash
python3 scripts/build.py --check
```

Convert one chapter to HTML on stdout:

```bash
python3 scripts/build.py --from-md docs/09-faq.md
```

Run the tests:

```bash
python3 -m unittest discover -s tests
```

## How this complements The Local AI Handbook

The two books share a voice but not a job:

| Question | Where to go |
| --- | --- |
| Should I use local AI at all? | The Local AI Handbook, ch. 1 & 8 |
| What do models, RAM, and quantization mean? | The Local AI Handbook, ch. 2 & 4 |
| Chat commands, UIs, privacy details | The Local AI Handbook, ch. 5–7 |
| What do I do with the *laptop* first? | This guide, ch. 1–4 |
| What one job should it do afterward? | This guide, ch. 6–9 |

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.
