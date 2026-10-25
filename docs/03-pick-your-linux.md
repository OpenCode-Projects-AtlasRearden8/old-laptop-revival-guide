# Chapter 3 — Pick Your Linux

Here is the secret about installing Linux on an old laptop: the hard part ended years ago. Modern beginner distros install as smoothly as smartphones set up, they don't nag about licenses, and they feel like a calmer, faster Windows with a start menu. The only genuinely hard part is choosing, because the Internet offers 700 opinions and the laptop cannot explain itself.

This chapter offers a short, honest menu of four. Any of the four is a good answer; the differences are trim levels, not philosophies. First, the one question that filters everything: **how much RAM does the laptop have?** (Windows: ⊞ Win → "System Information" → Installed Physical RAM; Mac: About This Mac; or chapter 2's `lsblk` trick from a live USB.)

## The menu, simply explained

A "distro" (short for *distribution*) is a packaged version of Linux — the operating system plus a desktop look plus an installer. Two ingredients matter for old hardware: the base distro and the **desktop environment** (the visual layer — windows, menus, panels). The lighter the desktop, the more RAM is left over for models and documents.

| Option | Works on | Vibe in one line | One-line summary |
| --- | --- | --- | --- |
| **Linux Mint XFCE** | 2 GB, comfortable at 4 GB+ | Looks and reads like the Windows of memory | The default answer for a revived laptop |
| **Linux Mint Cinnamon** | 4 GB minimum, happy at 8 GB | The fanciest Mint, worth it if RAM allows | Same calm family, nicer wallpaper |
| **Lubuntu (LXQt)** | 1.5–2 GB | Frugal to a fault, friendly enough | The top choice for truly ancient laptops |
| **MX Linux XFCE** | 2 GB, comfortable at 4 GB+ | The road-trip edition with rescue tools baked in | Strong pick if it ever needs to rescue *other* machines |

All four are free forever, update politely without lockdown screens, and are entirely offline-capable once installed. All support **try-before-install**: they boot from USB as a live system so the laptop can be test-driven without touching the drive.

## The recommendation, without hedging

- **Have 4 GB or more:** Linux Mint XFCE, and stop reading this chapter. Mint is the friendliest beginner Linux, the XFCE desktop is very light, its forums are famously kind to newcomers, and its software manager installs everything this guide needs (Firefox is included; LibreOffice, Ollama, and the printer settings are one click each).
- **8 GB or more** and the machine will mainly be the spare-room *writing/chat* station, not a model runner: Mint Cinnamon's prettiest face costs a few hundred MB more RAM, which is nothing at 8 GB.
- **2 GB and not a byte more:** Lubuntu. It is Ubuntu with the LXQt desktop, meaning light frugality without feeling abandoned in a universe of terminal commands.
- **2–4 GB, and the laptop is begged to behave:** MX Linux XFCE. Similar lightness to Mint XFCE, built on Debian like the other three, with a well-loved Rescue Menu of boot tools — useful if this laptop is going to be the household's flashlight.

The honest reason not to sweat the choice further: distro-hopping later is a 40-minute exercise, not a life decision. Pick Mint XFCE unless one of the exceptions above clearly shouts.

## Where to download, and which file

From each project's own website — **linuxmint.com** (Mint), **lubuntu.me** (Lubuntu), **mxlinux.org** (MX) — downloads are free, large (each is an ISO disk image of roughly 2–3 GB, approximate), and come with a checksum file for verifying the download when being careful. Verification is one step worth doing: download the ISO and the checksum listed beside it, then compare them (Windows: `certutil -hashfile file.iso SHA256`; Linux or Mac: `shasum -a 256 file.iso`). If the two long strings match, the download is whole. Chapter 4 shows what to do with the ISO file once downloaded (short answer: flash it to a USB stick with a free flashing tool).

One compatibility note for *very* old hardware: machines from before roughly 2008 may have 32-bit CPUs that modern distros no longer support — the installer point above assumes a 64-bit CPU, which nearly everything after 2008 is. Chapter 9's FAQ has the words to search for those stragglers.

## If decisions are the enemy

Two absolute fallbacks so no one stalls here:

1. Linux Mint XFCE (the XFCE edition of Linux Mint, from linuxmint.com). That is the whole decision.
2. Choose the "Edition" dropdown only if a friend says your machine is straining; otherwise the default recommendation stands.

Then to chapter 4 for install day. Buy nothing, sign up for nothing, create no account.
