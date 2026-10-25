# Chapter 6 — The Spare-Room Station

This is the chapter the whole project has been walking toward, and it is also the shortest-feeling one, because a revived Linux laptop makes this part genuinely easy. The idea: stop thinking of the machine as "an old laptop" and start thinking of it as a **station** — a small appliance that lives in a spare room, on a shelf, or on a corner table, plugged in, lid mostly closed, and given one job at a time.

The station's three jobs are described in this chapter with setup steps. It can do all three; most people lean on one.

## Job 1 — the writing table

The typing machine. LibreOffice Writer (already on Mint and Lubuntu via the menus) opens and saves `.docx` like breathing. For distraction-free pages, the Software Center offers **FocusWriter** (full-screen, typewriter feel, one-click) for free, or **Apostrophe** for more minimal markdown-adjacent flows. Either installs without a command line: Software Manager → type the name → Install.

Small set-up notes for a station that lives in the spare room:

- Set the laptop to stay awake while plugged in: Power settings → "when plugged in → never sleep" for screen blanking comfort; lid-close action "do nothing" if using it closed.
- Connect a mouse and keyboard only if the desk is permanent. A station often ends up undocked anyway.
- Turn off notifications once, if the desktop offers it, and let the visitor go be a stenographer of your thoughts.

One honest suggestion about the AI role here: this station's model (chapter 5) is a *beginning-draft partner and warm critic*, not a ghostwriter. The machine that handles "break my outline into 12 beats" locally and privately is exactly the machine that will not blink at a half-finished personal essay.

## Job 2 — the printer wrangler

Mint speaks Printer fluently. Steps, in order of likelihood of success:

1. Plug the printer into the laptop with its USB cable, or join it to the same Wi-Fi network as the station.
2. Open Settings → (Screens/Devices) Printers. In Mint: (they vary slightly; typing "printer" in the menu search finds it) → "Add" — Linux usually discovers it in seconds and installs a driver itself.
3. Print a test page.
4. To make the printer available to **other** machines in the house, in the printer's properties tick "Share this printer." The underlying plumbing is CUPS — the print system that has run quietly inside Linux for two decades — and it has its own barely-visible web page at `http://localhost:631` for anyone who enjoys going a level deeper. Chapter 9's FAQ has the fixes for the fussy-printer cases.

The quiet delight here: an old laptop is *excellent* at being a print server and does not mind being the house's printer brain 24/7/365. Debt repaid for a decade of service.

## Job 3 — the local chat terminal

Two levels, from the terminal upward:

**Level A — the terminal it already is.** Chapter 5 gave that to you: open a terminal, type `ollama run llama3.2:1b`, and chat. For a station whose role is "sit down, ask the private model, sit back," that is genuinely enough. If typing the model name each visit feels like work, chapter 8's checklist suggests printing a small card with the one-liner commands and taping it to the shelf.

**Level B — a chat window that feels like an app.** Two free paths, both local-only:

1. **The double-click experience: GPT4All.** Download the Linux installer from the GPT4All website (nomic.ai/gpt4all), run it, and choose "Ollama" or a local model as the backend on first run — it offers to grab its own small models too. This is the "chat window strangers can use" experience: icons, chat bubbles, no terminal. It is the Handbook's chapter 6 author pick for exactly this reason.
2. **The browser-tab experience: Open WebUI.** A friendlier multi-user chat page that runs on the laptop itself; the Handbook's chapter 6 has the current, tested install commands for it (they have changed more than once, which is precisely why they are not copied here — this guide refuses to quote commands it cannot stand behind today).

Which to choose? If the sentence "I would rather type less and point more" resonates, add the window. If the station will be shared around the household (kids, partner, someone who fears the terminal), the window earns its install in a day.

## Taming the machine room

Regardless of which jobs the station holds, five small habits turn a laptop into a genuinely pleasant appliance:

- **Power:** plug it in and leave it plugged in; laptops raised on mains power age far more gently than ones cycling their batteries nightly.
- **Ventilation:** spare rooms get dusty. A soft dry-cloth wipe of the vents every couple of months keeps the old fan honest.
- **Updates leave you alone** with Mint's defaults — monthly notices, click approve. That is the entire worst case.
- **Storage etiquette:** the station is not a second dump for stray files. Its Documents folder stays small, like a drawer, not a landfill.
- **A card on the shelf** with the password and the two magic commands (`ollama run llama3.2:1b` and the Wi-Fi name) makes the station neighbor-friendly while remaining privacy-safe.

One boundary note from chapter 1's spirit that matters even more now: this station handles family paperwork and local AI, but it is *not* the cloud backup of anything important. Keep the rescue-drive habit from chapter 1 alive by having the station *receive* a copy of the family's important folders monthly — from the main computer to an external drive to the station. A spare room full of trust is a spare room worth having.

## Chapter 6 in one breath

Give the machine one job — writing table, print wrangler, or local-chat terminal; set up with three clicks each; add habits (mains power, vent wipes, small Documents); and if a friendlier chat window is wanted, the Handbook's chapter 6 finishes that sentence.
