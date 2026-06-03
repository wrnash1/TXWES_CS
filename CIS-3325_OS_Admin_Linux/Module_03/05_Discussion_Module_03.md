# Discussion Prompt: Module 03 — Linux Filesystem Hierarchy Standard

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Overview

Module 3 covers the FHS and the tools for reading, finding, and processing file content. This discussion asks you to apply those concepts to a troubleshooting scenario and reflect on how the FHS knowledge affects your approach to practical Linux administration.

---

## Discussion Prompt

This discussion has two required parts. Address both in a single, organized post.

### Part 1 — Troubleshooting Scenario

You are the on-call Linux administrator for a company. At 2:00 AM you receive an alert that the web server is down. You SSH into the server. The web service is not responding.

Using only the command-line tools and filesystem knowledge from Modules 1 through 3, describe your initial investigation process step by step. Specifically address:

1. How would you check if the web server process is running? (Hint: you have learned commands that show system information — think about which directory holds runtime process data.)
2. Where would you look for the web server's log files? Name the specific directory path based on FHS conventions.
3. What command would you use to view the end of a log file to find the most recent error messages? What flag would you add if you wanted to watch it live?
4. If you found a configuration file that was recently modified, what `find` command would you use to identify files changed in the last 24 hours in `/etc`?

Write your response as a numbered list of actions, explaining why each action is appropriate based on what you know about the FHS and the commands from this module. You do not need to actually solve the problem — demonstrate the systematic investigation process.

### Part 2 — FHS Reflection

The Linux Filesystem Hierarchy Standard dictates that configuration files go in `/etc`, logs go in `/var/log`, binaries go in `/usr/bin`, and so on. This design philosophy of "a place for everything and everything in its place" is very different from how most Windows systems are organized, where applications often store configuration and data in their own installation directory under `C:\Program Files\`.

In your view, what are the practical advantages of the FHS approach for system administrators? Are there any disadvantages or situations where the FHS structure makes administration harder? Draw on specific examples from the lab or lecture to support your points.

This is an opinion question with no single right answer — I am looking for thoughtful reasoning backed by concrete examples, not a general statement that "FHS is good."

---

## Response Requirements

- Initial post: minimum 275 words, due by Thursday at 11:59 PM.
- Reply to at least two classmates: minimum 75 words each, due by Sunday at 11:59 PM.
- For replies: engage with your classmate's troubleshooting process in Part 1 — would you do anything differently at a specific step? For Part 2 replies, either build on their argument or respectfully offer a counterpoint.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Systematic troubleshooting steps with FHS-based reasoning | 45 |
| Part 2: FHS advantage/disadvantage analysis with specific examples | 30 |
| Two substantive peer replies | 15 (7.5 each) |
| Writing quality and minimum length | 10 |
| **Total** | **100** |

---

## Instructor Note

For Part 1, there are multiple valid approaches. I am not looking for one specific sequence — I am looking for reasoning that shows you understand why each directory holds what it holds. A student who says "I would check `/var/log/apache2/error.log` because web server logs go in `/var/log`" demonstrates that understanding. A student who says "I would check logs somewhere" does not.

For Part 2, consider the perspective of an administrator managing 50 servers instead of one. The FHS advantage becomes especially clear at scale — knowing that `/etc/nginx/nginx.conf` is the configuration file location on every RHEL and Ubuntu server without having to look it up is a significant time saver.
