# Chapter 5 — Ollama on a Tired Laptop

Here is the chapter where the revived machine gets its one job. The honest news up front: this is the shortest chapter in the guide. Installing Ollama on Linux is one command, and downloading a small model is another. The *deep* material about models — what the sizes mean, how quantization makes them fit, how to chat well, what preserves privacy — lives in **The Local AI Handbook**, chapters 2 through 7, and it is worth the evening. This chapter is the working minimum, plus the choices that matter specifically on a tired old machine.

## What Ollama is, in one paragraph

Ollama is a free, small program that downloads and runs AI models on the laptop itself. Nothing is sent anywhere: no account, no subscription, no cloud. The laptop becomes a small, private AI server, and the "chat" happens in a terminal window (or later, in a chat window — chapter 6 sets that up). Running it costs nothing but the laptop's electricity, which on a wound-down spare-room machine is about the cost of a nightlight.

## Step 1 — Install Ollama

Open a terminal (Ctrl+Alt+T on Mint) and copy this line in, then Enter:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Reading it in plain English: download the official installer script from ollama.com and run it. It will ask for the user password once (that is the Linux `sudo` prompt, the laptop's own way of saying "you may"), and everything else is automatic — it installs the program and sets it up to start whenever the laptop boots.

Check that it worked:

```bash
ollama --version
```

A version number, something like `ollama version 0.x.y`, should print. (The exact numbers change often, so read that "x.y" as "a number I will see" — approximate by nature, accurate as of October 2026.)

## Step 2 — pick a model that fits an old machine

The one rule that matters before choosing: **the model file should be no bigger than half the laptop's RAM.** A 4 GB laptop → look in the 1.5–2 GB range. An 8 GB laptop → 3–4 GB models run comfortably. Bigger files than that either fail outright or crawl. (The full RAM-to-model-size table is The Local AI Handbook's chapter 2.)

For most revived laptops entering service, these are the honest starting picks — names and approximate download sizes, October 2026:

| Model name to type | Approx. size | Good at | Pair with RAM |
| --- | --- | --- | --- |
| `qwen2.5:1.5b` | ~1 GB | Quick questions, everyday writing prompts | 4 GB |
| `llama3.2:1b` | ~1.3 GB | The gentlest first model; fast even on old CPUs | 4 GB |
| `llama3.2:3b` | ~2 GB | Noticeably better writing and summaries | 6–8 GB |
| `gemma2:2b` | ~1.6 GB | Balanced chats, pleasant tone | 4–6 GB |
| `phi3:mini` | ~2.2 GB | Punches above its weight on reasoning prompts | 6 GB |

The `b` suffix means "billion parameters" — roughly, the number of dials in the model, which is the honest proxy for how smart the model is and how much RAM it drinks. Smaller is faster and shallower; the Handbook's chapter 4 explains the trade-offs far better, and its framing is worth stealing: *the model you can actually run is the best model.*

## Step 3 — download and meet it

One command does both: it downloads the model the first time, then opens a chat.

```bash
ollama run llama3.2:1b
```

The download shows a progress bar (the 1.3 GB takes a few minutes on home internet; it happens once, and it is stored locally forever). Then a prompt appears, and the laptop talks back. Type a sentence — "Explain what a paragraph is, like I am holding a pen" — and watch it respond. A tired machine drinking its first electricity in service does something to people. Let it happen.

Three commands worth knowing, then the escape hatches of `/bye` (leaves the chat), `/clear` (empties the current conversation), and Ctrl+C (interrupts a reply that is going long):

1. `ollama list` — shows what is downloaded and the disk space each takes.
2. `ollama rm <model-name>` — frees the disk space of a model that did not earn its keep.
3. `ollama ps` — shows what is loaded in memory right now.

## Step 4 — retire *old* hardware wisely

Two small, tired-laptop-specific notes that the Handbook can skip and this guide cannot:

- **Close the lid, not the door to it.** Until chapter 6 sets up the nicer arrangement, the model keeps running in that terminal. If the reply is taking ages on old hardware, Ctrl+C is always available and re-asking is free.
- **Heat and speed on old laptops are one topic.** If batteries are original and nearly dead, the machine may run more slowly while plugged in and hot; "stuck" often means "thinking as fast as a 2011 CPU can." The Handbook's speed expectations chapter (8) is the honest reference.

## If it did not work

Chapter 9's FAQ handles the usual suspects: `command not found` after install, the download stalling, "connection refused" errors, and what to do with 2 GB machines that want something even smaller (the `1b` family has smaller cousins, and the Handbook's chapter 4 has the full zoo).

## Chapter 5 in one breath

One command installs Ollama → pick a model file smaller than half the RAM → `ollama run` and meet it → three maintenance commands → the Handbook turns this taste into a meal.
