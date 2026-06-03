# Discussion: Module 09 — Shell Scripting Fundamentals

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This discussion asks you to reflect on shell scripting as a professional practice — not just a technical skill. Good scripts are readable, maintainable, and safe. Bad scripts can corrupt data, lock out users, or silently fail for months before anyone notices. This discussion explores what separates professional-grade scripts from fragile one-offs.

**Participation Requirements:**

- Post your initial response (minimum 200 words) by Thursday at 11:59 PM
- Reply to at least two classmates (minimum 75 words each) by Sunday at 11:59 PM
- Include at least one code snippet in your initial post

---

## Discussion Prompt

### Writing Scripts That Don't Fail Quietly

Consider this script written by a junior administrator:

```bash
#!/bin/bash
# daily_backup.sh — backs up /etc to a timestamped archive

BACKUP_DIR=/backups
DATE=`date +%Y%m%d`
cd $BACKUP_DIR
tar czf etc_backup_$DATE.tar.gz /etc
echo "Backup complete"
```

This script "works" in a happy-path scenario. But it has multiple problems that could cause silent failures or data loss in production.

**Part A — Code Review**

Identify at least four specific problems with `daily_backup.sh`. For each problem:

1. Describe what the problem is
2. Explain what could go wrong
3. Provide the corrected code

Write your corrected version of the complete script. It should use what you learned in this module: `set -euo pipefail`, proper quoting, error handling, `trap`, and logging.

**Part B — Automation and Risk**

Shell scripts are often run as root via cron jobs — unattended, on a schedule, with no human watching. This makes their correctness critically important.

Describe two practices (beyond what you fixed in Part A) that you would apply to any script that runs unattended as root:

- Why is each practice important?
- What specific failure mode does it prevent?

You may draw from the module content or from your own experience.

**Part C — Automation Ethics and Responsibility**

A fellow student says: "I write scripts fast and just test them in production — if they break something I fix it. It's faster than writing a bunch of error handling."

Respond to this approach. Consider:

- What categories of damage can a poorly-written root script cause?
- How does script quality connect to professional responsibility?
- What is the minimum standard of quality for a script that modifies system state (creates/deletes users, changes permissions, modifies configs)?

---

## Discussion Grading Rubric

| Criterion | Points |
|---|---|
| Part A: Correct identification of bugs (min 4) with fixed code | 35 |
| Part B: Two well-justified automation safety practices | 25 |
| Part C: Thoughtful response on professional responsibility | 20 |
| Two substantive peer replies with code feedback | 15 |
| Technical accuracy and code quality | 5 |
| **Total** | **100** |

---

## Hint — Problems in daily_backup.sh

Without giving away all the answers, here are prompts to help you find the issues:

- What happens if `/backups` does not exist?
- What is wrong with using backticks `` ` ` ``?
- What happens if the `cd` command fails?
- What does `$BACKUP_DIR` expand to if `BACKUP_DIR` is not set? (Hint: with `set -u` this would error; without it...)
- What happens to `$DATE` in `etc_backup_$DATE.tar.gz`?
- Does the script log anything useful for debugging?
- Who gets notified if this cron job fails at 2 AM?

---

## Peer Reply Guidelines

When reviewing classmates' corrected scripts:

- Does their script handle the case where `/backups` does not exist?
- Did they use `set -euo pipefail`?
- Is the `trap` correctly cleaning up temporary files?
- Would their script send any kind of alert if it fails?
- Is there any quoting issue that could cause problems with filenames containing spaces?

Good peer reviews read like a code review you would give a colleague — constructive, specific, and focused on making the code more reliable.
