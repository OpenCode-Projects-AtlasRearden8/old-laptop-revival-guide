# Chapter 9 — Troubleshooting FAQ

Every troubleshooting section is really a letter to overwhelm. These are the questions that actually come up, answered plainly before they can cause a middle-of-the-project crisis. Ordered by the moment they tend to appear.

## Setup-phase questions

**Q: How much RAM do I have, again?**
Windows before the wipe: ⊞ Win + R, type `msinfo32`, Enter, look for "Installed Physical Memory." That number, rounded down in your memory but trusted exactly as shown, decides the Linux chapter choice. After chapter 4 the same number comes from Settings → About.

**Q: The USB stick will not boot — the laptop never shows a menu.**
Almost always a costume drama: the boot-menu key gets pressed too late or not at all. Restart, then start tapping the moment the screen goes dark: F12 (Dell, Lenovo), F9 (HP), Esc (ASUS), F2 or Del (older machines, where a setup screen opens instead — find "Boot" there, enable USB and "Legacy"/UEFI as appropriate, save, retry). Also: some 2010–2014 machines only boot in a mode called *Legacy* rather than *UEFI*; if the USB appears in the menu but errors immediately, in Rufus choose "MBR" + "BIOS (or UEFI-CSM)" when re-flashing the stick (chapter 4's flashing step again, 15 minutes), and Etcher users get the same result by flashing with the stick formatted first.

**Q: I pressed the boot key and the menu came up, but the USB stick is not listed.**
Re-flash with the proper mode (above), or try the other USB port — old laptops treat their two ports like distant cousins. And confirm the charger is plugged in; the boot menu occasionally skips available options on a thirsty battery.

**Q: The installer says the disk "will be ERASED." That is supposed to be fine, right?**
Yes — that is the plan. Chapter 1's backup verified, chapter 2's decisions made; read the drive-size line against the laptop's known storage size and continue. The only wrong erase is an erase of the wrong *drive*, and the size line is what guards against that.

**Q: My keyboard layout went strange mid-install — the @ and " have swapped.**
The install-day layout picker chose the wrong country, and Linux lets the setting change without any re-installing: open keyboard settings (search "keyboard" in the start menu), choose the Layouts tab, pick the right country, done.

## Live-mode and try-before-install questions

**Q: In live mode, Wi-Fi lists no networks.**
Try the shield-icon menu (Mint: bottom-right network icon) once, then restart once — a 2013 Broadcom or similar chip often wakes up polite on the second boot. Failing that, connect one time by phone USB network-share (in phone settings) and install, then let Linux's post-install updates fetch the right **driver firmware package** — chapter 4's first-boot updates step picks that up automatically on Mint-family.

**Q: The touchpad is twitchy or reversed-scrolling.**
Mouse & Touchpad settings (type it into the menu search) has a natural-scrolling toggle and a sensitivity slider. Two minutes. No registry, no courage needed.

## Ollama-phase questions from chapter 5

**Q: `ollama: command not found`, right after install.**
Close the terminal and open a brand-new one — the terminal only refreshes its knowledge of programs when fresh. If it *still* misses, run `/usr/local/bin/ollama --version` directly; a full-path success is the sign of an environment quirk worth one `sudo reboot`.

**Q: The model download crawls or fails mid-way.**
Run `ollama rm <name>` to clear the partial download, then retry when the household Wi-Fi is quiet — 1–2 GB files occasionally need a second session. If a smaller model (`llama3.2:1b` instead of `3b`) also will not land after half an hour of honest tries, The Local AI Handbook's chapters 3 and 4 cover offline installation and model-mirroring on a second machine for exactly this case.

**Q: Replies come one word every few seconds. Is it broken?**
No — that is an old CPU's honest speed for the model chosen. The fixes, in order: a smaller model (see the table in chapter 5), a shorter prompt, and closing the other browser tabs. The Local AI Handbook's chapters 4 and 8 describe the speed trade-offs far more richly; the one-line version is that 1b-class models on 4 GB machines give roughly a word or two per second, and are lovely to read at that pace.

**Q: Can I fit a *bigger* model than the table suggests, by making what I have work harder?**
Every so often, yes, one notch: closing everything else and using a `Q4`-quantized variant (smaller file, same model — the Handbook's chapter 4 explains the letters) sometimes fits a model whose *unquantized* sibling would not. But no amount of cleverness puts a 7 GB model on a 4 GB machine. The half-RAM rule from chapter 5 stays the most honest guide.

## The spare-room and long-life chapter 6 questions

**Q: The laptop gets hot and sometimes warm-smelling while the model runs. Stop?**
Warm is expected; *alarm* smell or a fan that forgets to be quiet after 20 minutes is a stop-and-clean signal: power off, soft dry cloth on the vents, gentle vacuum at a distance if the vents are fluffy, and resume. A laptop running a model for the first time in a decade is doing the most strenuous work of its life — treat the heat like the honest toll it is.

**Q: Printers and their drivers — the scary Linux story. Is it still true?**
Mostly praise now: Mint detects and installs printers over USB/Wi-Fi in a minute or two. Rare but real cases: very old Wi-Fi-only printers want a proprietary Linux driver from the maker's site (Hewlett-Packard, Brother, and Epson all keep Linux pages), and CUPS' own browser page at `http://localhost:631` is a deeper cockpit. If the printer simply refuses, chapter 6's USB-cable approach settles the dispute permanently.

**Q: How do I let other people in the house use the local chat?**
The spare-room ideas scale in two directions: a household card (chapter 6's taped card with the command), or the friendlier window per The Local AI Handbook's chapter 6 (GPT4All or Open WebUI). The full model can also be reached from *another* machine on the house network by pointing that machine's chat app at the station's IP address — the Handbook's chapter 6 covers that connection and IP-nature questions.

## Privacy and safety questions

**Q: Is the local model really private? Give me the one-line version.**
Yes: with Ollama and a local model, prompts and answers exist only on the laptop — no account, no upload, no telemetry tied to a name. The long version (what remains *not* covered, network-adjacent caveats, and the moment when privacy claims are overstated) is The Local AI Handbook's chapter 7, whose one-line summary is "local is private in the ways that usually matter, and not a magical privacy vault."

**Q: Should the spare-room station's chat be health-advice adjacent?**
Treat any model answer, local or not, the way a good librarian might gracefully handle "should I take ibuprofen with my blood thinner": useful background, never a substitute for a professional. Health-education framing — not medical advice — is the standing boundary in all of Asdale Dynamics' guides.

## Chapter 9 in one breath

Boot-menu key by brand → re-flash mode MBR+CSM if the stick boot fails → RAM by `msinfo32` → right-layout keyboard settings fix it themselves → Wi-Fi restarts politely → `ollama` needs a *new* terminal → heat is honest, smells are not → printers mostly just work → privacy is chapter 7 of the Handbook, and one line here.
