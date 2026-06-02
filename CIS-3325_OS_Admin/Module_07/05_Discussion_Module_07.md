# Discussion Forum: Module 07 - Shell Scripting Fundamentals

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content.

---

### Scenario A - Automating Server Health Checks

Your organization manages 12 Linux servers. Every morning the operations team manually logs into
each server to check disk usage, verify that three critical services are running, and confirm
that the system load is under a threshold. This takes 45 minutes each morning and is frequently
skipped when the team is busy. You have been asked to automate this process.

1. Describe the script structure you would use: what input it accepts (if any), what checks
   it performs, and what output it produces. Specify which bash constructs (loops, functions,
   conditionals) are appropriate for each part of the check.
2. The script needs to run on all 12 servers each morning without manual intervention.
   Explain how set -euo pipefail and a trap EXIT handler affect the behavior of an unattended
   script, and why these are more important for scripts run by cron than for scripts run
   interactively by an administrator.
3. Write the function signature and body for a single check_disk() function that accepts a
   mount point and a threshold percentage as arguments, logs a warning if usage exceeds the
   threshold, and returns 0 for OK and 1 for over-threshold. Include proper local variable
   declarations.

---

### Scenario B - Script Maintenance and Error Diagnosis

A junior administrator wrote a production backup script six months ago. You are reviewing it
after a backup failure incident. The script has no shebang line, no error handling, uses
unquoted variables throughout, and ends with rm -rf $BACKUP_DIR/old regardless of whether
the backup succeeded. The script has been overwriting good backups with empty archives when
disk space is low.

1. Explain specifically what happens when a script with no shebang line is executed with
   ./backup.sh on a system where the default shell is dash rather than bash. How does this
   create silent behavior differences from what the author intended?
2. The script contains: DEST=$BACKUP_BASE/$TODAY/archive.tar.gz. If TODAY is unset (perhaps
   because date failed), what path does DEST resolve to, and what would rm -rf $DEST
   potentially delete? Explain how set -u and quoted variable expansion both independently
   protect against this class of bug.
3. Write the corrected first five lines of the script (shebang through the first variable
   assignment) that incorporate proper error handling options and demonstrate safe variable
   quoting and parameter expansion with a default value.

---

### Scenario C - Script Portability and Reuse

Your team has a collection of bash scripts that work on Ubuntu servers but fail when run on
the RHEL servers that a partner team manages. Investigation reveals that some scripts use
bashisms (bash-specific syntax) while assuming /bin/sh compatibility, and others hardcode
paths like /bin/bash that do not exist on all systems.

1. Explain the difference between #!/bin/bash and #!/usr/bin/env bash as shebang lines.
   In what deployment scenario does #!/usr/bin/env bash provide better portability, and
   what security concern exists with using env in the shebang of a privileged script?
2. The scripts use [[ ]] syntax for all conditionals. Explain one capability [[ ]] provides
   that [ ] does not, and explain why this matters when the scripts are run with /bin/sh
   instead of /bin/bash. What practical step can you take to verify whether a script uses
   bashisms before deploying it to a system where only /bin/sh is available?
3. Functions in the scripts use local variables, but on one RHEL server the local keyword
   appears to be working differently. Explain the scope rules for variables in bash functions
   when local is used versus when it is omitted. Write a small test script (5-8 lines) that
   demonstrates the difference clearly.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 07 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

The difference between a script and a reliable script is error handling. A script that works
under normal conditions is easy to write. A script that logs what it did, stops safely when
something goes wrong, cleans up after itself, and gives you enough information to diagnose
failures — that takes deliberate design. set -euo pipefail and trap are not optional extras
for production scripts. They are the minimum standard. When a cron job runs at 3 AM and fails
silently, the question is never "did the script work?" but always "how will we know it failed?"
Build that answer into every script before you schedule it.
