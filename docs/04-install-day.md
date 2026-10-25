# Chapter 4 — Install Day

The mood for today: unhurried, coffee-shop voice. Nothing about the next hour requires skill — only patience at the moments when the screen goes black and asks for trust. This chapter has three phases: make the installer stick, try before installing, install.

## Phase 1 — Make the installer stick

What is being built: a USB stick whose contents, when chosen at boot, run or install Linux. The ISO from chapter 3 is the recipe; a small free program writes it correctly.

1. On a working computer (Windows, Mac, or Linux), download a flashing tool. Trusted, free, long-standing options: **balenaEtcher** (works on Windows, Mac, and Linux; the simplest), **Rufus** (Windows only, slightly more options), or the `dd` command itself on Linux (chapter 2 already introduced that command). Approximate sizes: Etcher about 150 MB, Rufus about 30 MB.
2. Plug in the 8-GB-plus USB stick. Confirm nothing on it matters — it is about to be erased.
3. Open the tool, choose the ISO, choose the stick, press Flash/Start, and wait 10–20 minutes. Etcher walks all three steps with pictures; Rufus almost thinks for itself: one device dropdown, one "Select" button, START.
4. When the tool says *Verified* (Etcher) or returns control, eject the stick politely: right-click → Eject (Windows), ⌘E (Mac), the tray icon (Linux).

Windows note: on Windows, SmartScreen may pop a warning over Etcher's first run because it is unsigned freeware; "More info → Run anyway" is the standard path when the download came from balena.io itself.

## Phase 2 — Try before installing (live mode)

This phase is why no one panics later. Insert the stick into the tired laptop, then:

1. Restart and tap the **boot-menu key** every second or two as soon as the screen goes dark. Common keys by brand: F12 (Dell, Lenovo ThinkPad), F9 (HP), Esc (ASUS, newer HP), F2 (older machines show a BIOS instead — in that one, find "Boot" and enable USB first). The brand trivia chart gets a bigger version in chapter 9.
2. A menu appears listing devices. Choose the USB stick (often named "UEFI: SanDisk" or the brand word "SanDisk"/"Kingston" — or "Linux Mint" directly once the stick is readable). Wait through a minute of quiet scrolling text: arriving machinery, not an error.
3. A full Mint/Lubuntu/MX desktop appears, working, connected to Wi-Fi (click the network icon top-right, pick the network, type the password — like any phone). Play. Open Firefox. Check the touchpad feel.
4. When assurance is reached, either shut down (to revisit later) or double-click the **Install Linux** icon on the desktop (it ships right there) to continue immediately.

While in live mode, nothing written to the laptop's drive persists — rebooting wipes that session. It is a dressing room, not the house.

## Phase 3 — Install, carefully and slowly

Begin the installer and answer in order. Options below are Mint's wording; Lubuntu and MX differ in looks and agree in sense.

1. **Language, keyboard layout** — obvious. The keyboard layout screen has "detect" buttons that fix 90% of "my 3 key makes £" surprises.
2. **Wi-Fi connection** — connect here; several installers download updates *during* install and it speeds everything up.
3. **Installation type** — the important screen, and the one to read twice:
   - **"Erase disk and install"** — the chapter-2 Path A option: wipes the drive and installs. The revival default for this guide.
   - **"Install alongside Windows"** — dual-boot: no wipe, a menu offered at every boot between Windows and Linux. Honest choice, but on tired hardware Windows keeps its bulk and its update nagging; this guide's revival path prefers the calm of erase-and-install (chapter 1's backup covers the Windows side).
   - **"Something else"** — manual partitions. Every wrong-drive horror story begins here. Not needed for this project.
4. Confirm the erase target shows the right drive and roughly the right size, then press the affirmative button and put the kettle on: 10–40 minutes depending on drive speed.
5. **Time zone, name, user name, password.** Create a short user name (lowercase, no spaces — it appears in file paths forever). Choose a password you will type daily and *also* wrote down in chapter 1. "Log in automatically" is fine for a spare-room machine; the checkbox is honest either way.
6. Optional same screen or follow-up: **"encrypt the home folder"** / full-disk encryption. If this laptop is staying at home, convenience usually wins and no is a fine answer; if it might travel or be donated later, chapter 2's encrypt-then-erase trick says yes is worth it.
7. When it says done: **remove the USB stick when prompted**, then Enter to reboot into the new machine.

## First boot, in order

The new Linux will offer a tidy tour. For this project, four things matter, each ≤ 5 minutes:

1. **Updates.** A shield icon in the system tray (Mint) or the software updater will present a batch; apply them and let the fan do its one loud warm-up, then go quiet. Updates repeat automatically after this.
2. **Battery and closing-lid behavior.** Menus vary; on Mint: Power Settings → "when the lid is closed → do nothing" while plugged in, so the station can be closed and forgotten mid-chat.
3. **The shortcut that matters ahead of chapter 5:** open a terminal (Ctrl+Alt+T on Mint) and keep it in your pocket — that black rectangle is the doorway for Ollama in the next chapter.
4. Take a screenshot of the desktop for the file album of the mind. Projects that end with a photo taken are projects with morale.

## Chapter 4 in one breath

Flash the ISO with Etcher → boot from the stick with the brand's boot key → try it live, absolutely no commitment → install with "Erase disk and install" (or the dual-boot line if plans differ) → create the user and note the password → update once on first boot. Chapter 5 puts the AI on.
