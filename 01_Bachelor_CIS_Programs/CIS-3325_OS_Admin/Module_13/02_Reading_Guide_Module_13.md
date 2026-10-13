# Reading Guide: Module 13 - Cron Jobs and Task Scheduling

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA / LearnLinuxTV &bull; CIS-3325 Module 13</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ (XK0-005) & LPI Linux Essentials Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ (XK0-005) & LPI Linux Essentials Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 4.0 - Automation and Scripting

---

### Glossary

**cron** - A daemon that wakes every minute and executes scheduled commands based on time specifications in crontab files and system cron directories.

**crontab** - A file containing cron job entries for a user or the system. Edited with `crontab -e` for user crontabs; `/etc/crontab` is the system-wide crontab with an added username field.

**run-parts** - A utility that executes all scripts in a directory that match naming rules. Used by cron to execute scripts in cron.hourly, cron.daily, cron.weekly, and cron.monthly.

**at** - A command for scheduling a one-time job to run at a future time. The `atd` daemon executes at jobs. Use when a task should not recur.

**atq** - Lists pending at jobs for the current user. Root sees all users' jobs.

**anacron** - A cron supplement that runs jobs that were missed while the system was powered off. Reads /etc/anacrontab and tracks last-run times in /var/spool/anacron/.

**systemd timer** - A systemd unit file with a .timer extension that activates a .service unit on a schedule. The modern alternative to cron, with full journald logging and dependency management.

**OnCalendar** - The systemd timer directive that specifies a calendar-based schedule (e.g., `daily`, `weekly`, `*-*-* 02:00:00`).

**Persistent=true** - A systemd timer option that triggers the timer immediately at boot if it was missed while the system was off. The systemd equivalent of anacron's catch-up behavior.

**cron.allow / cron.deny** - Files that control user access to cron. If cron.allow exists, only listed users may use cron. If only cron.deny exists, all users except listed ones may use cron.

---

### Crontab Field Reference

```
MIN   HOUR   DOM   MON   DOW   COMMAND
0-59  0-23   1-31  1-12  0-7
```

Day-of-week: 0 and 7 both represent Sunday.

| Field | Meaning | Example |
|-------|---------|---------|
| MIN | Minute (0-59) | `15` = at minute 15 |
| HOUR | Hour (0-23) | `3` = 3 AM |
| DOM | Day of month (1-31) | `1` = 1st of month |
| MON | Month (1-12) | `6` = June |
| DOW | Day of week (0-7) | `1-5` = Mon-Fri |

---

### Crontab Special Value Syntax

| Syntax | Meaning | Example |
|--------|---------|---------|
| `*` | Every value | `* * * * *` = every minute |
| `*/N` | Every N steps | `*/15` in MIN = every 15 min |
| `N,M` | List | `1,15` in HOUR = 1 AM and 3 PM |
| `N-M` | Range | `1-5` in DOW = Mon through Fri |
| `N-M/S` | Range with step | `0-59/10` in MIN = every 10 min |

---

### Common Crontab Examples

| Schedule | Crontab Entry |
|----------|---------------|
| 3:15 AM every day | `15 3 * * *` |
| Every 10 minutes | `*/10 * * * *` |
| Midnight every day | `0 0 * * *` |
| 6 AM Mon-Fri | `0 6 * * 1-5` |
| 1st of every month at midnight | `0 0 1 * *` |
| Every hour | `0 * * * *` |
| Every 30 minutes | `*/30 * * * *` |

---

### crontab Command Reference

| Command | Action |
|---------|--------|
| `crontab -e` | Edit current user's crontab |
| `crontab -l` | List current user's crontab |
| `crontab -r` | Remove current user's crontab (no confirmation) |
| `sudo crontab -u USER -e` | Edit another user's crontab |
| `sudo crontab -u USER -l` | List another user's crontab |

---

### Cron File Locations

| Location | Purpose | Username field? |
|----------|---------|-----------------|
| `/var/spool/cron/crontabs/USER` | Per-user crontab (edit with crontab -e) | No |
| `/etc/crontab` | System-wide crontab | Yes |
| `/etc/cron.d/` | Application-installed cron fragments | Yes |
| `/etc/cron.hourly/` | Scripts run every hour by run-parts | No |
| `/etc/cron.daily/` | Scripts run every day by run-parts | No |
| `/etc/cron.weekly/` | Scripts run every week by run-parts | No |
| `/etc/cron.monthly/` | Scripts run every month by run-parts | No |

---

### run-parts Naming Rules (Debian/Ubuntu)

Scripts in cron.hourly, cron.daily, cron.weekly, cron.monthly must:

* Contain only letters, digits, hyphens, and underscores
* Have NO file extension (no `.sh`, no `.py`, no `.rb`)
* Be executable (`chmod +x`)

A script named `backup.sh` is silently ignored. Rename it to `backup`.

---

### at Command Reference

| Command | Action |
|---------|--------|
| `at 23:45` | Schedule job at 11:45 PM today |
| `at 02:00 tomorrow` | Schedule job at 2 AM tomorrow |
| `at now + 2 hours` | Schedule job 2 hours from now |
| `echo "CMD" \| at 03:00` | Non-interactive at job |
| `atq` | List pending at jobs |
| `atrm N` | Remove at job number N |
| `at -c N` | Show full command for job N |

---

### anacron Configuration (/etc/anacrontab)

```
PERIOD   DELAY   JOB-ID       COMMAND
1        5       cron.daily   run-parts /etc/cron.daily
7        10      cron.weekly  run-parts /etc/cron.weekly
30       15      cron.monthly run-parts /etc/cron.monthly
```

* PERIOD: days between runs
* DELAY: minutes to wait after system boot (prevents boot spike)
* JOB-ID: unique name; last-run date stored in `/var/spool/anacron/JOB-ID`

---

### systemd Timer Unit Structure

Two files are required.

`/etc/systemd/system/example.service`:

```ini
[Unit]
Description=Example Job

[Service]
Type=oneshot
ExecStart=/usr/local/bin/example.sh
```

`/etc/systemd/system/example.timer`:

```ini
[Unit]
Description=Example Timer

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

---

### systemd Timer OnCalendar Examples

| Value | Schedule |
|-------|---------|
| `daily` | Every day at midnight |
| `weekly` | Every Monday at midnight |
| `monthly` | First day of every month |
| `*-*-* 02:00:00` | Every day at 2 AM |
| `Mon..Fri *-*-* 06:00:00` | Weekdays at 6 AM |
| `*-*-* */4:00:00` | Every 4 hours |
| `*:0/15` | Every 15 minutes |

---

### systemd Timer Commands

| Command | Action |
|---------|--------|
| `systemctl list-timers` | Show all active timers |
| `systemctl enable --now NAME.timer` | Enable and start a timer |
| `systemctl status NAME.timer` | Check timer status and next trigger |
| `journalctl -u NAME.service` | View output from the timer's service |
| `systemd-analyze calendar "SPEC"` | Test/validate an OnCalendar expression |

---

### cron.allow / cron.deny Precedence

| State | Who can use cron |
|-------|-----------------|
| cron.allow exists | Only users listed in cron.allow |
| cron.deny exists, cron.allow does not | All users except those in cron.deny |
| Neither file exists | All users (implementation-dependent) |

The same rules apply to `at` via `/etc/at.allow` and `/etc/at.deny`.

---

### Cron Troubleshooting Checklist

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Job never runs | Wrong field order | Verify: MIN HOUR DOM MON DOW |
| Job never runs | Script not executable | `chmod +x /path/script.sh` |
| Job in cron.daily never runs | Filename has extension | Rename: remove `.sh` |
| Command not found in cron | PATH too short | Use full paths or set PATH= |
| No output visible | Not redirected | Add `>> /log/file.log 2>&1` |
| Cron daemon not running | Service stopped | `systemctl start cron` |

---

### Exam Tips

1. Crontab field order is MIN HOUR DOM MON DOW. The most common exam mistake is reversing minute and hour. `15 3 * * *` = 3:15 AM. `3 15 * * *` = 3:03 PM.

2. `*/N` in the minute field means "every N minutes." `*/15` = runs at :00, :15, :30, :45 every hour. This is step syntax, not a range.

3. cron.allow precedence: if `/etc/cron.allow` exists, it is the only file that matters. cron.deny is completely ignored when cron.allow exists.

4. run-parts on Debian/Ubuntu: scripts must have no extension. `backup.sh` is silently skipped. This is a directly testable exam scenario.

5. `at` is for one-time jobs. Cron is for recurring jobs. If the exam says "run once tonight," the answer is `at`, not a crontab entry with `* * *`.

6. anacron catches missed jobs on systems that are not always running. `Persistent=true` in a systemd timer does the same thing. Both are alternatives to standard cron for laptops or machines with unpredictable uptime.

7. Cron runs with a minimal PATH. Always use absolute paths in crontab entries. This is the most common reason a cron job works interactively but fails when run by cron.

8. systemd timers require both a `.timer` unit and a `.service` unit. The timer activates the service. Enable with `systemctl enable --now NAME.timer`, not the service unit directly.

---

## 9. Supplemental Resources

**1. [crontab(5) — Linux manual pages](https://man7.org/linux/man-pages/man5/crontab.5.html)**
https://man7.org/linux/man-pages/man5/crontab.5.html
The authoritative man page for crontab file format, covering field ranges, special characters (*/N, N-M, N,M), the username field in /etc/crontab, and environment variable handling in cron jobs.

**2. [systemd.timer — freedesktop.org](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)**
https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html
Official reference for all systemd timer unit directives including OnCalendar, Persistent, AccuracySec, OnBootSec, and OnUnitActiveSec with calendar expression examples.

**3. [anacron(8) — Linux manual pages](https://man7.org/linux/man-pages/man8/anacron.8.html)**
https://man7.org/linux/man-pages/man8/anacron.8.html
Complete reference for anacron configuration and behavior, covering the /etc/anacrontab format, PERIOD/DELAY/JOB-ID fields, and how anacron determines whether a missed job needs to run using /var/spool/anacron timestamps.

---

#
---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 13 - Cron Jobs and Task Scheduling** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 13 - Cron Jobs and Task Scheduling**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 13 - Cron Jobs and Task Scheduling**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 13 - Cron Jobs and Task Scheduling**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

* Write a crontab entry for any given time specification without reversing minute and hour
* Explain the meaning of `*/15`, `1,15`, and `1-5` in crontab fields
* Use `crontab -e`, `crontab -l`, and `crontab -r` correctly
* Explain why scripts in /etc/cron.daily/ must not have a .sh extension on Ubuntu
* Schedule a one-time job with `at` and list or remove pending jobs with `atq`/`atrm`
* Explain what anacron does that cron cannot
* Create a systemd timer unit pair (.service + .timer) for a scheduled job
* Use `systemctl list-timers` to view active timer schedules
* Explain the difference between cron.allow and cron.deny and their precedence
* Troubleshoot a cron job that silently fails (PATH, permissions, filename extension)
