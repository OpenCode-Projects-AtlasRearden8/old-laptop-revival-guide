# The Old Laptop Revival Guide — Read This First

There is a laptop in a drawer, or behind the couch, or in that closet that closes badly. Its battery holds maybe an hour, Windows feels like wading through mud, and every time it is opened, something updates for forty minutes.

This guide is for that laptop. Windows itself is about to stop supporting machines like it — support windows close on old versions of Windows much the way they closed for Windows 10 in late 2025 — and the easy next move is the recycling bin.

The bin is half right. Running even a modest AI model used to mean a high-end desktop; today a tired laptop can handle it, if you dress the machine in lightweight Linux and give it one job. This guide walks the transformation: back up what matters, wipe the disk calmly, choose a Linux that fits the hardware, install it, add Ollama and a couple of small models, and turn the thing into a spare-room station that writes, prints, and chats locally. The last chapters cover the honest alternative: when revival is not worth it, and how to retire or donate the laptop without any data surviving on it.

This guide is the *machine half* of the story. Its companion, **The Local AI Handbook** (free, at dylanasdale.github.io), covers the *AI half* — how models work, what RAM means in model terms, chat commands, desktop chat apps, and the privacy trade-offs. Where the subjects overlap, the Handbook gets the depth and this guide gives a short, honest map plus a pointer.

## Who this guide is for

- You are not a Linux expert. Maybe you have never installed an operating system, and the phrase "boot menu" made you slightly nervous a minute ago.
- You would like photos, letters, and passwords rescued *before* anything gets erased — and you would like the rescuing part explained slowly, because that is where real damage happens.
- You want the machine to do one job well: writing, printing, or chatting with a small local AI model. Not everything. One job.
- You have a normal evening or two. This is a weekend-shaped project, not a career change.

## What you will need

- The laptop, charger included. Battery health does not have to be great.
- A second computer, phone, or tablet for looking things up mid-project. Using the same laptop as the patient and the surgeon is avoidable and worth avoiding.
- An external USB drive big enough to hold the old files — any brand, roughly $10–20 for the smallest useful sizes at any office-supply or big-box store, prices approximate.
- One USB stick, 8 GB or larger. It will be erased during the process, so it should hold nothing precious.
- Optionally, a printed copy of the hardware checklist in chapter 8. Paper is its own backup plan.

## How to read this guide

Chapters 1 through 10 are meant to be read in order, then acted on one at a time. If a chapter is not relevant (the laptop is already wiped, or Linux is already on it), skip it without guilt. Nothing here requires paying for software, and nothing requires knowing the command line *before* starting — every terminal command appears with a plain-English sentence above it.

Conventions used throughout:

- **Bold** marks words that will appear on screen, or a step worth slowing down for.
- `code` in a gray box marks something to type or a menu item, copied exactly as written.
- Bigger quoted notes mark the places where a friend would grab your shoulder: *wait a second before the next step.*
- Wherever a number (model size, download size, hardware requirement) might drift over time, it is labeled approximate. October 2026 is the accuracy horizon for specifics in this view of the guide.

## A five-minute taste

Not every visit needs to be a commitment. If the laptop still boots:

1. Just curious how this ends? Skim chapter 3 (which Linux) and chapter 6 (the spare-room station) for the fun bits.
2. Lined up a laptop from a relative or friend, already wiped? Start at chapter 1, then breathe; the wipe in chapter 2 will be shorter for you.
3. Want the AI part and nothing else? Chapter 5 is the shortest honest route to Ollama, and The Local AI Handbook is the long one.

The rest of the guide exists because the boring middle — backups, wipes, installers — is where projects quietly die or quietly get hurt. It is meant to be read once, unhurried, with a cup of something warm.

## The map

| Going to... | Chapter |
| --- | --- |
| Rescue the data and back it up safely | 1 — Backup First |
| Erase the drive without fear or regret | 2 — The Calm Wipe |
| Choose a lightweight Linux that fits | 3 — Pick Your Linux |
| Get it installed without drama | 4 — Install Day |
| Put modest local models on it | 5 — Ollama on a Tired Laptop |
| Give it one job and a home | 6 — The Spare-Room Station |
| Let it go gracefully | 7 — Retire or Donate |
| Print a pre-flight list | 8 — Hardware Checklist |
| Fix what goes sideways | 9 — Troubleshooting FAQ |
| Decipher the vocabulary | 10 — Glossary |

See you in chapter 1.
