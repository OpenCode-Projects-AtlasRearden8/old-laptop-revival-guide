# Chapter 1 — Backup First

Everything in this guide is reversible *except* erasing the old files. Wipes can be redone from a fresh installer. Linux can be swapped for a different flavor over coffee. A deleted family photo cannot be un-deleted — not by this guide, not by a paid service, not by anyone with total confidence.

So this chapter comes first and moves slowly on purpose. Nothing in it is technical. It is a checklist with instructions attached, and if it is followed, the rest of the project becomes genuinely hard to do lasting damage with. Take as long as it takes.

## What actually needs saving

Before copying anything, spend five minutes deciding what is worth copying. On most unloved laptops the answer is small; whole-disk backups of a machine this tired are unnecessary and mostly save a decade of old installers.

Go through this list with the dots-jump trick in the back of your mind — walk the categories in order rather than hunting around randomly:

- **Photos and videos** in the laptop's Pictures folders, including anything inside "Camera Roll" or "WhatsApp Media" style folders.
- **Personal documents** — Desktop, Documents, and Downloads. Downloads especially: bank statements, ticket PDFs, scanned forms.
- **Bookmarks and passwords** in the browser. For Chrome-style browsers: Settings → "You and Google" → sync and export options; for Firefox: Settings → Library → Bookmarks → "Show All Bookmarks" → "Import and Backup". Export bookmarks to an HTML file.
- **Email** if the laptop runs a desktop mail client with years of mail in it. If it only has a webmail tab open in the browser, there is no local mail to lose.
- **Music, podcasts, audiobooks** — anywhere a media library has lived locally.
- **Tax, work, or family paperwork** — anything whose loss would cause an afternoon of groaning.
- **License keys and serial numbers** recorded in old text files or sticky-note apps: Windows and Office product keys, printer software keys, anything resembling an activation code.
- **Game saves** if the laptop has any (look for folders like `Documents\My Games`, the hidden `AppData` folders on Windows, or islands inside `~/.config` on Linux — and if it is not obvious, skip this one; a lost old game save is survivable).

What *not* to worry about: programs themselves (they will be reinstalled fresh, not copied), Windows itself, browser caches, and any file marked "TEMP". All of that is attic insulation, not family jewels.

## Where to put the backup

The simple, local-first choice: an external USB drive. It works with no account, no subscription, no upload time, and no further decision about which cloud company sees the family photos.

- Plug the drive into the laptop directly — **not** through a cheap multi-port hub, which is the most common cause of a flaky, half-finished copy.
- If the drive is brand new, it may need a one-time format. On Windows, right-click the drive in File Explorer → Format → NTFS, then Format. On a Mac, use Disk Utility → Erase → "Mac OS Extended" or APFS. (Formatting wipes the *external* drive, which should be empty anyway.)
- Two copies beat one. If there is a second USB stick or a cloud folder already in use (Google Drive, iCloud, OneDrive, Dropbox you already pay for or already use), also copy the Documents folder there. Chapter 2 will hand-wave "a copy exists elsewhere," and it is nice when that is simply true.

## The copy, done patiently

The recommended method — no software to install, works on every operating system:

1. Create a folder on the external drive named something unambiguous: `LAPTOP_RESCUE_2026-10`.
2. Inside it, make subfolders matching the categories above: `Photos`, `Documents`, `Bookmarks_and_Passwords`, `Email`, `Media`, `Keys`.
3. Copy each category from the laptop into its matching subfolder. On Windows: select folders, copy, paste into the matching subfolder. On a Mac: the same, with ⌘C and ⌘V. Do one category at a time.
4. For the browser: run the bookmark export from the list above and save the HTML file into `Bookmarks_and_Passwords`. For saved passwords, export through the browser's own password manager (Chrome: Settings → Passwords → ⋮ → Export passwords; Firefox: Settings → Passwords → ⋮ → Export Passwords). The export file is a **plain, readable CSV of every saved password** — treat it like a house key. Copy it to the rescue folder, then never leave it lying on a shared machine.
5. Wait for each copy to finish before starting the next. Untidy jabbing at "copy" mid-transfer is where corrupted rescues come from.

Notes on patience:

- Old spinning hard drives (HDDs) read slowly, especially when ill. A 50 GB haul can take an hour or more. That is normal. Put on music.
- If Windows offers to "compress" or "encrypt" the backup folder on the way out, decline — plain folders are the most portable, most recoverable form.

## Verify before trusting anything else

This is the shoulder-grab moment. **Do not proceed to chapter 2 until the backup is verified.** Verification here means a human spot-check, not software incantations:

1. Unplug the external drive, count to five, plug it back in. (This rules out a copy that only worked over a dead USB connection.)
2. Open the rescue folder and open a few files inside it: one photo from each year it matters, a PDF from Downloads, the bookmarks HTML file.
3. Look at the numbers: right-click → Properties (Windows) or Get Info (Mac) on the drive's rescue folder, and compare the size against roughly what the laptop held in those categories. Closeness is fine; zero in a category you know was stuffed is not.
4. Spot-check the password CSV (first name only) and then close it.

If any of that fails, re-copy the missing category before moving on. Time spent here is the cheapest insurance in the entire project.

## A quiet word about passwords

One more item belongs to this chapter, and it is about the *future*, not the past. Once Linux is installed (chapter 4), there will be no recovery key, no Windows reset tool, no Apple ID wiggle-out. Write down, on paper or in a password manager you already trust:

- The **Linux user password** created during install, and the username that goes with it.
- The laptop's **disk-encryption password**, if chapter 4's partition screen offers "encrypt the disk" and yes is chosen. Losing this one makes the drive fully unreadable, by design.
- Any Wi-Fi password worth knowing twice.

The test: imagine spilling coffee on the laptop tomorrow and needing to log in from a fresh machine. If anything on paper would be missed, it belongs on paper.

## If the laptop will not boot

Backup advice that assumes a working laptop is useless when the patient has already stalled. Three humane options, in order of ease:

1. **Try booting anyway**, twice or three times with the charger plugged in and a full 30 seconds of patience at each black screen. Tired laptops boot into repair/recovery modes more often than people expect.
2. **Use a live USB** — the same installer stick from chapter 4 will double as a rescue stick. It runs Linux straight from the USB without touching the drive, and from there the folders can be copied to an external drive like any other day. Chapter 4 shows how to make the stick; a friend with a working computer is needed for that one step, and it takes fifteen minutes.
3. **Pull the drive.** On many older laptops the drive is a small metal rectangle behind one or two screws, easier to remove than people fear. It can be connected to a working computer with a cheap USB drive adapter (roughly $10–15, prices approximate) and read like a USB stick. Chapter 7 covers this in donation terms.

If the data is *irreplaceable* and there is a budget for professional data recovery, stop here rather than improvising — recovery companies exist precisely for this moment. For memories and paperwork, options 1–3 handle nearly every case.

## Chapter 1 in one breath

Sort what matters → copy it to an external drive with into named folders → unplug and plug back in, spot-check it → write down the passwords of the future. Now, and only now, to chapter 2.
