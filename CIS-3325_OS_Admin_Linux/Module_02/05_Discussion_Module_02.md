# Discussion Prompt: Module 02 — Linux Installation and System Navigation

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Overview

Module 2 introduced two topic areas: the installation process (with its partitioning and filesystem decisions) and the core command-line navigation tools. This discussion connects those technical concepts to real-world administrative thinking. You will apply what you learned about partition layout to a practical scenario and reflect on your initial experience using the Linux command line.

---

## Discussion Prompt

This discussion has two required parts. Address both in a single, organized post.

### Part 1 — Partition Layout Decision

You have been hired as the junior Linux administrator for a small company. You are setting up a new Ubuntu Server that will serve as a web server. It will host the Apache web application, serve HTML/CSS/JavaScript files, write to a MySQL database, and store application logs. The server has a single 500 GB SSD.

Design a partition layout for this server. For each partition you create, specify:

- The mount point (e.g., `/`, `/var`, `/home`)
- The approximate size you would allocate
- The reason you chose that size and separated it from other partitions

You do not need to specify filesystem types unless you want to — focus on the mount point decisions and your reasoning. There is no single right answer, but your choices should reflect the server's workload described above.

Consider at minimum: root (`/`), swap, and at least two additional partitions that make sense for a web server with a database and log-generating application.

### Part 2 — Command-Line Reflection

You have now spent time in the Linux terminal using navigation and file management commands. Reflect on the following:

Describe one specific moment in this module's lab where a command behaved differently than you expected — or where you had to look up a flag or re-read the man page to understand what was happening. What was the command, what did you expect, and what actually happened? What did you learn from the difference?

If the lab went completely smoothly, describe one command from the module that you think is the most important for a Linux administrator to have in muscle memory and explain why, using a specific real-world scenario where that command would be critical.

---

## Response Requirements

- Initial post: minimum 275 words, due by Thursday at 11:59 PM.
- Reply to at least two classmates: minimum 75 words each, due by Sunday at 11:59 PM.
- For replies on Part 1: evaluate your classmate's partition layout. Would you make any different choices? Explain why.
- For replies on Part 2: share whether you had a similar experience with that command or a different one.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Partition layout with mount points, sizes, and reasoning for each | 40 |
| Part 2: Specific command reflection or scenario-based explanation | 30 |
| Two peer replies that engage with content | 20 (10 each) |
| Writing quality and minimum length | 10 |
| **Total** | **100** |

---

## Instructor Note

For Part 1, pay particular attention to `/var` — that is where MySQL databases, web server logs, and application data will live. If you put everything on `/`, a log file explosion can crash the web server. Partition layout is a real operational decision, not just an exam topic. I will comment on every post that proposes a layout, either affirming the choices or suggesting improvements.

For Part 2, "the lab went perfectly and I have nothing to report" is not an acceptable response. Even experienced administrators encounter unexpected command behavior. If the lab itself produced no surprises, use a man page to find a flag you did not know about and explain what it does.
