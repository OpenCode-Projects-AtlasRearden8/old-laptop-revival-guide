# Chapter 2 — The Calm Wipe

Most of the dread in this project lives in this chapter, so it gets shorter and kinder than feared. Wiping a laptop is a routine act with one rule: **the backup is verified first** (chapter 1). After that, wiping is not scary. It is the moment the laptop stops being a museum of old software and becomes a clean slate.

There are two wiped-and-done scenarios — the drive being reused on the same laptop (the normal revival path), and the drive going with the laptop to someone else (the donation path in chapter 7). Both are covered here. Pick the section that matches the plan.

## First, know what is in there

Two different technologies live inside old laptops, and the wipe method differs:

- **HDD** — a hard disk drive: spinning metal platters, a little clicking when it wakes up, usually thick and heavy, from before roughly 2012. Slower, and erasure is a genuine, satisfying erasing experience: writing over every sector.
- **SSD** — a solid-state drive with no moving parts: silent, much faster, standard from about 2013 onward. Erasure works differently — see the note below.

To check on Windows: press ⊞ Win, type `System Information`, open it, and expand Components → Storage → Disks. To check on a Mac:  → About This Mac → System Report → Storage. On Linux (or a live USB): in a terminal run `lsblk -d -o NAME,ROTA,MODEL,SIZE`. `ROTA 1` means spinning (HDD); `ROTA 0` means SSD. When in doubt, the era of the laptop is a good enough guess.

## The SSD shortcut that is not a cheat

There is a trick that is *better* than the paranoid stereotype. Modern SSDs do not let software truly scrub their innards — the drive's own controller shuffles data around invisibly, so "overwrite everything 7 times" tools are theater on SSDs. The honest, strong method is shorter:

1. **Turn on full-disk encryption** (chapter 4's installer offers this on Linux: "encrypt the disk"; on Windows, BitLocker; on a Mac, FileVault).
2. **Then erase the disk** in any ordinary way.

Because encryption is scrambled *at rest*, deleting the encryption key turns every remaining byte into permanent gibberish. The result is exactly as good as the old thrice-overwrite ritual, minus the hours. This trick — encrypt, then wipe — is the method this guide recommends for every SSD in both the revival and donation paths.

## Path A — wiping for revival (Linux takes the drive)

The nice thing about this path: the installer you build in chapter 4 *is* the wipe tool. Linux installers can erase the entire disk as their first act. So this path is a preview of Install Day:

1. One quiet disclaimer before the list: after chapter 1's verification, there is genuinely nothing left to protect here.
2. Boot the installer USB (chapter 4 shows how; briefly: insert the stick, restart, and tap the boot-menu key — F12 on many Dell/Lenovo/HP machines, Esc on others — then pick the USB stick).
3. In the installer's *Installation type* screen, choose the option worded roughly **"Erase disk and install"** (Mint's installer literally says "Erase disk and install Linux Mint"). Do not choose "Something else" or manual partitioning — those are expert wading pools, and every person who accidentally wipes the wrong drive chose "Something else."
4. Confirm that the only drive listed in the erase screen is the right one and its size matches the laptop's storage (115 GB, 240 GB, 500 GB — it will say). Then let it run.

That single step — erase and install — handles the wipe and the new operating system in one pass. If the plan is dual-boot (keeping Windows), no wipe happens at all and chapter 4's dual-boot path applies instead.

> **Wait a second:** if an SSD full-disk-encryption wipe was planned for this drive but Linux itself will run encrypted afterward, there is nothing extra to do — installing Linux with "encrypt the disk" already scrambles at rest, and the old Windows data was overwritten as part of the install.

## Path B — wiping for donation or sale (laptop goes away)

Here the laptop leaves with someone else attached, and *verifiably clean* matters. Two free, boring, honest methods; either is plenty for a secondhand laptop's dignity.

**Method 1 — the operating system's own reset.** The tools built into Windows and macOS are genuinely good in their recent versions:

- Windows 10/11: Settings → System → Recovery → **Reset this PC** → remove everything → and *local reinstall* if asked to choose cloud vs. local. If asked whether to "clean the drive," yes — that choice runs a deeper pass on the way out. Let it run an hour or two.
- macOS: macOS Ventura or newer has *Erase All Content and Settings* in System Settings → General → Transfer or Reset, which is essentially instant and includes the SSD-trick logic natively. Older macOS: boot into Recovery (⌘R at startup), use Disk Utility → Erase, then reinstall macOS from that same screen.

**Method 2 — the Linux live USB, for stubborn machines.** If Windows will not boot for the reset (not rare on tired laptops), boot the chapter-4 installer USB, choose "Try Linux Mint" instead of install, open a terminal, and run, one at a time:

```bash
lsblk -d -o NAME,MODEL,SIZE
sudo dd if=/dev/sda of=/dev/zero bs=1M status=progress
```

The first command lists the drives so the name and size of the laptop's internal drive can be written down; the second writes zeros across the whole drive. **The `of=/dev/...` must be the laptop's internal drive** (`/dev/sda` on most, `/dev/nvme0n1` on newer SSDs — match the size from the list) and **must not** be the USB stick itself; checking the name and size twice before pressing Enter is the honest sanity check.

Two notes on depth: for an HDD, once is genuinely enough when the goal is a clean secondhand laptop, no matter what the seven-pass folklore says. For an SSD, the `dd` pass is honest but not the strongest trick — the encrypt-then-erase method from above is stronger on SSDs, so if this drive is an SSD *and* the wipe must be airtight (for a stranger), put the laptop through the Linux installer once with "encrypt the disk" turned on, then boot the installer again and erase everything, which tosses the encryption key. Boring, but every step is free.

## The wipe, as a kindness ritual

One practical detail people skip and later miss: **unplug everything** — external drives, phones, printers, and especially the chapter-1 rescue drive. Attach nothing that could contain a copy of the data. Additionally:

- Sign out of and remove the laptop from any account lists while the old system still boots: Microsoft account "remove device," Apple ID, any Dropbox/OneDrive "unlink this device" — searchable under each service's settings page by the phrase "remove device."
- Deauthorize things that count authorizations: music services, Adobe-style license seats.
- Keep the rescue drive outside the room until the wipe is confirmed finished. It cannot be too safely ignored.

## Chapter 2 in one breath

Verify the backup → know HDD vs SSD → revival path: the installer wipes it for you; donation path: reset with the built-in tools, or Linux live USB for stubborn machines → unplug everything that could carry copies → next chapter, choose the Linux.
