# Reading Guide: Module 13 - Cron Jobs and Task Scheduling
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 13 – Cron Jobs and Task Scheduling**! This week covers Linux task automation — the traditional `cron` daemon, `crontab` syntax, system-wide cron directories, the `at` command for one-time jobs, and the modern `systemd` timer units. Task scheduling is tested on CompTIA Linux+ XK0-005 under Domain 1.0 (System Management) and Domain 4.0 (Scripting, Containers, and Automation).

As you work through this material you will learn how to create, edit, and troubleshoot cron jobs, interpret the five-field cron time expression, use `at` for one-time scheduling, and understand when systemd timers are the appropriate alternative to cron.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **`cron` and `crond`**: The cron daemon (`crond` or `cron`) runs continuously in the background and checks its schedule tables every minute, executing any jobs whose time expression matches the current time. Cron reads from user crontab files (`crontab -e`) and system-wide files in `/etc/cron.d/`, `/etc/cron.daily/`, `/etc/cron.weekly/`, and `/etc/cron.monthly/`. The main system crontab is at `/etc/crontab`.
*   **Crontab syntax (five-field format)**: Each cron job line uses the format: `minute hour day-of-month month day-of-week command`. Fields use: a specific number (`30`), `*` (any value), a range (`1-5`), a list (`1,3,5`), or a step (`*/15` = every 15 minutes). Example: `30 2 * * 0 /usr/bin/backup.sh` runs at 2:30 AM every Sunday. The `crontab -e` command opens the current user's crontab for editing; `crontab -l` lists it; `crontab -r` removes it.
*   **System cron directories**: `/etc/cron.daily/`, `/etc/cron.weekly/`, `/etc/cron.monthly/` contain scripts that `run-parts` executes on the corresponding schedule. Drop a script into the appropriate directory to schedule it without writing a crontab entry. Scripts must be executable and must not have a file extension (`.sh` suffix causes `run-parts` to skip them on some distributions). `/etc/cron.d/` holds crontab-format files with an extra username field before the command.
*   **`at` command**: Schedules a one-time job to run at a specified future time. `at 14:30` opens an interactive prompt where commands are entered and submitted with Ctrl+D. `at now + 2 hours` schedules a job relative to the current time. `atq` lists pending jobs; `atrm <jobid>` removes a queued job. The `at` daemon (`atd`) must be running. Unlike cron, `at` jobs execute once and are then removed.
*   **`/etc/cron.allow` and `/etc/cron.deny`**: Access control files that determine which users may use `crontab`. If `/etc/cron.allow` exists, only users listed in it may schedule cron jobs — all others are denied. If only `/etc/cron.deny` exists, all users except those listed may use cron. If neither file exists, the default behavior varies by distribution (often allows all users or only root).
*   **systemd timers**: A modern alternative to cron using two unit files: a `.service` unit (defines what to run) and a `.timer` unit (defines when to run it). `OnCalendar=daily` triggers daily; `OnBootSec=5min` triggers 5 minutes after boot. `systemctl list-timers --all` shows all timers and their next trigger times. Timers can catch up missed jobs if the system was off (via `Persistent=true`), which cron cannot do.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Task scheduling maps to Linux+ Domain 1.0 (System Management) and Domain 4.0 (Scripting, Containers, and Automation). Expect 4–6 questions on crontab syntax, field order, and the `at` command.
*   **Crontab field order trap:** The five fields are always: minute, hour, day-of-month, month, day-of-week. The exam frequently tests this order. A common wrong answer swaps hour and minute or places day-of-week before month. Memorize: **M H DOM MON DOW**.
*   **`*/5` vs `5` trap:** `*/5` in the minute field means "every 5 minutes" (0, 5, 10, 15...). `5` in the minute field means "at minute 5 of every hour" (one execution per hour). The exam presents scenarios asking for a job that runs every N minutes — the answer uses `*/N`.
*   **`cron.allow` vs `cron.deny` priority:** If `/etc/cron.allow` exists, it takes complete precedence — even if a user is not in `/etc/cron.deny`, they are denied if not in `cron.allow`. The exam may ask which file controls access when both exist — `cron.allow` wins.
*   **`at` vs cron use cases:** `at` is for one-time future execution; cron is for recurring scheduled jobs. The exam distinguishes between them with scenario questions like "run a maintenance script once at midnight tonight" (answer: `at`) vs "run a backup script every night at midnight" (answer: cron).
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) covers job scheduling concepts in its scripting and automation chapters. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of crontab editing, cron job troubleshooting, and the `at` command in a live environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the automation and scheduling chapters of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php), which cover cron job creation, crontab syntax, and scheduled task management on Linux.
*   **Required Video:** Watch the task scheduling videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates crontab editing, cron directory usage, and the `at` command with live examples.

---

### Lab & Command Integration
In this week's hands-on lab you will create a user crontab entry with `crontab -e` to run a script on a recurring schedule, verify the crontab with `crontab -l`, place a script in `/etc/cron.daily/`, and schedule a one-time job using `at`. You will also inspect `systemctl list-timers` to compare systemd timer behavior.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the scheduling chapters in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the task scheduling videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
