# Discussion Forum: Module 13 - Cron Jobs and Task Scheduling

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

### Scenario A - Automating Server Maintenance Tasks

You are a Linux administrator responsible for a production Ubuntu 22.04 web server. You need to
automate three recurring maintenance tasks: a database dump script at 2:00 AM daily, a log
cleanup script at 11:45 PM every Sunday, and a certificate renewal check every 12 hours.

1. Write the three complete crontab entries for these jobs. For the database dump, use the full
   path `/usr/local/bin/db-dump.sh` and redirect both stdout and stderr to
   `/var/log/db-dump.log`. Explain why using absolute paths and explicit output redirection is
   essential in cron jobs and what happens to output if you do not redirect it.
2. A junior administrator asks whether to put these jobs in their personal crontab or in
   `/etc/cron.d/`. Explain the trade-offs: which is more appropriate for production automation,
   what the username field in `/etc/cron.d/` entries does, and how the system cron differs from
   a user crontab in terms of persistence and visibility.
3. Six months later, the certificate renewal check is generating noise in the log because it runs
   even when no certificates are near expiration. The administrator wants to suppress successful
   output but preserve error output. Rewrite the crontab entry to achieve this, and explain the
   difference between `> /dev/null`, `2>&1`, and `> /dev/null 2>&1` in the context of cron.

---

### Scenario B - Scheduling with at and Handling Missed Jobs

Your organization runs a batch reporting system on a server that has weekly maintenance windows
every Sunday from 2:00 AM to 4:00 AM. The system uses both cron and at for scheduling, and the
server is sometimes also powered off for hardware maintenance.

1. A one-time data migration script must run at exactly 11:00 PM tonight. Write the complete
   `at` command to schedule it. Then explain what `atq` and `atrm` do, and describe a scenario
   where you would use `atrm` before the job runs. Also explain the access control rules for `at`
   using `/etc/at.allow` and `/etc/at.deny`.
2. A nightly summary report job is scheduled with cron at 3:00 AM. During the Sunday maintenance
   window, the server is offline and the job is missed. Explain specifically what cron does (or
   does not do) about the missed job when the server comes back online. Then explain how anacron
   would handle the same situation differently, referencing its PERIOD, DELAY, and JOB-ID fields.
3. The team decides to migrate the nightly report from cron to a systemd timer to get better
   logging. Write the complete `.service` and `.timer` unit files for a job that runs
   `/usr/local/bin/nightly-report.sh` at 3:00 AM daily and catches up on any missed runs. Include
   the `Persistent=true` directive and explain its equivalence to anacron's catch-up behavior.

---

### Scenario C - Cron Troubleshooting and Access Control

A developer named `carlos` reports that their cron job has not run in three days despite being
correctly entered in their crontab. Investigation reveals several potential issues on the RHEL 9
server they use.

1. List four distinct reasons a cron job might silently fail to execute even when the crontab
   entry appears syntactically correct. For each reason, write the specific diagnostic command
   or check you would perform and the exact fix. Include at least one reason specific to scripts
   placed in `/etc/cron.daily/` on RHEL systems.
2. Investigation reveals that `/etc/cron.allow` exists on the server and does not contain
   `carlos`. Explain step by step why this prevents `carlos` from using cron, what the precedence
   rules are between `cron.allow` and `cron.deny`, and what the administrator must do to restore
   `carlos`'s access. Also explain what would happen if `/etc/cron.allow` were deleted entirely
   and only `/etc/cron.deny` remained (with `carlos` not listed in it).
3. After fixing the access issue, `carlos` wants to verify their cron job will fire at the
   correct time without waiting for the next scheduled run. Write the commands `carlos` should
   use to list their crontab, check the cron daemon logs for recent job executions, and manually
   test the script in a minimal environment that simulates the PATH constraints cron uses.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 13 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Automation is where Linux administration becomes leverage. A task you automate once runs correctly
forever — at 3 AM, on weekends, while you are on vacation. A task you do manually runs correctly
only when you remember it. The tools in this module (cron, at, anacron, systemd timers) are
straightforward, but the discipline around them matters: use absolute paths, redirect output to
logs you actually check, document what each job does in a comment above the entry, and test in a
minimal shell environment before trusting cron to run it. The most expensive cron mistakes are the
silent ones — jobs that appear to be running, generate no errors, but do nothing because a command
was not found in cron's restricted PATH. Verify your jobs actually produce their intended output,
not just that they appear in `crontab -l`.
