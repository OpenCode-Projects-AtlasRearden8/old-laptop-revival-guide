# Chapter 10 — Glossary

Plain-English definitions for every word this guide uses with confidence and a little swagger. The Local AI Handbook carries a longer AI-flavored glossary; this one sticks to machine-and-Linux words, with a few borrowed phrases included for reader convenience.

## The people-friendly machinery list

**BIOS / UEFI** — the laptop's earliest software, the one that decides what the machine thinks about before the operating system wakes up. Its settings screen is reached at boot with a key like F2 or Del; its practical use in this project is making sure USB sticks are considered bootable.

**Boot menu** — the one-time menu (F12, F9, Esc by brand) that asks, just for this restart, what the laptop should pretend to be: USB stick, drive, or otherwise. The doorway for live mode.

**Bootable USB** — a USB stick holding an operating system in a way the laptop's boot menu will offer it. Chapter 4's Phase 1 makes one.

**Checksum** — a fingerprint for a downloaded file; if the fingerprint the site publishes matches the fingerprint your computer computes, the download arrived whole. One optional step in chapter 3.

**Cinnamon** — Linux Mint's default desktop: friendly, pretty, and the memory-hungriest of the friendly family. Choose at 8 GB RAM and up.

**CUPS** — the print system that has quietly run under Linux for decades; it also has its own web page at `http://localhost:631` for people who like to watch the plumbing.

**Desktop environment** — the visual coat of an operating system: windows, icons, menus, the taskbar. Different coats (Cinnamon, Xfce, LXQt) on the same bones, trading RAM for looks.

**Distillation** — occasionally, the practice of making a smaller model mimic a larger one's behavior; mentioned here because "distilled" turns up on model name labels and has nothing to do with the *distro* in the next entry.

**Distro (distribution)** — a packaged flavor of Linux: kernel plus desktop plus defaults plus installer. Mint, Lubuntu, and MX are the distros this guide is built around.

**Dual-boot** — Linux and Windows sharing one disk, with a menu at each boot. Chapter 4 names the trade: everything local is kept, but so is Windows' bulk and anxiety.

**Encryption (full-disk)** — scrambling the entire drive behind a password, so its contents only make sense when the password opens it. Chapter 2 uses it as the modern, honest wipe for SSDs; chapter 4 lets you turn it on during install.

**Firmware** — small, built-in software inside a piece of hardware (a Wi-Fi chip, a printer). Occasionally its absence explains a device that technically exists but will not behave; the word describes the fix, not a new tool to fear.

**Flashing (a USB stick)** — writing an ISO onto a USB stick in a way that turns it into a bootable USB. Etcher or Rufus is the tool; chapter 4 walks it.

**HDD** — a hard disk drive: spinning platters, a clicking sound, storage from the before-2012 era in this context. Wipes in the classic way (chapter 2's Path B, `dd` method is fine).

**ISO** — a single file that is a complete copy of a whole install DVD's worth of content, about 2–3 GB for the distros in chapter 3. What you download from linuxmint.com and friends.

**LTS (long-term support)** — a release version of a distro promised years of security updates (usually five for the choices in chapter 3). The calm choice for a spare-room machine.

**Li-ion** — the lithium-ion battery chemistry inside every laptop; its swollen form is the one safety-flavored item in this guide (chapter 7's rule: special drop-off, never mailing).

**Live mode / live USB** — running Linux entirely from the USB stick, with the laptop's drive unread-and-unwritten. The try-before-install trick from chapter 4's Phase 2.

**LXQt** — the thriftiest of the friendly desktops; Lubuntu's coat. The choice under 2 GB.

**Mint** — Linux Mint, the recommended beginner distro of this guide: Ubuntu-family bones, calm Windows-like coat (Cinnamon or Xfce), famously gentle community.

**Model (AI)** — the downloaded file that *is* the AI: billions of dials set by training, dressed sometimes as `llama3.2:1b`. Chapter 5's table lists the honest small ones for revived laptops.

**Ollama** — the free program that runs AI models on the laptop, started in chapter 5 with a single terminal command and no account.

**Partition** — a fence the installer draws within one drive, so Linux and (in dual-boot) Windows each have their own field. Chapter 4's Phase 3 mentions it once and asks you not to hand-fence manually.

**Q4 (quantization level)** — a size-reduction trick from The Local AI Handbook's chapter 4: storing the model's dials with slightly fewer decimal places so that the file is much smaller and the model is only a little dimmer. The `Q4` family is the sweet spot for small machines.

**RAM** — random-access memory: the workspace where the operating system and models live while running, distinct from storage (the drive) where they sleep. Its size is the single most honest predictor of what the laptop can do.

**ROTA** — a Linux column in `lsblk` output; `1` means the drive spins (HDD), `0` means it doesn't (SSD). The tech-iest entry in this glossary and proud of it.

**SSD** — solid-state drive: storage with no moving parts. Faster, silent, standard from about 2013. In wipes, it responds to the encrypt-then-erase trick rather than the overwrite ritual (chapter 2).

**Station** — the guide's favorite word for what a revived laptop becomes: an appliance with one job and a home, plugged in, quietly doing it.

**sudo** — the prefix that lets a Linux command act with the administrator's power, which asks for your user password once. Appears honestly twice in this guide: once to install Ollama, once to wipe a stubborn HDD.

**Terminal** — the black window with typed commands. The guide's rule: every terminal command in these chapters appears only when a plain-English sentence above it explains what it does and why.

**Ubuntu** — the widely-used Linux family beneath Mint, Lubuntu, and friends; its community answers make up the deep foundation of almost every search result for beginner Linux problems.

**Wipe** — erasing a drive's contents so files no longer exist in any recoverable sense. The guide gives it a whole calm chapter (2) precisely so it never has to be feared again.

**Xfce** — the lighter-coated Mint flavor: nearly as capable as Cinnamon, much thriftier with RAM. The default recommendation for 4 GB machines.
