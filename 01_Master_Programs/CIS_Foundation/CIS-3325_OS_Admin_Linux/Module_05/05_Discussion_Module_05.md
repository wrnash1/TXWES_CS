# Discussion: Module 05 — Process Management and System Monitoring

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

## Discussion Overview

**Due:** See course calendar

**Initial post:** Minimum 200 words, due by Thursday 11:59 PM

**Responses:** Reply to at least two classmates, minimum 100 words each, due by Sunday 11:59 PM

**Grading:** See rubric below

---

## Prompt

Process management and system monitoring are the skills that determine whether a sysadmin can respond to a crisis or is flying blind. Reflect on the following questions and address **at least two** in your initial post:

1. **The SIGKILL last resort** — The module established a best practice: always try SIGTERM first, wait, then escalate to SIGKILL. Why does this matter? Think about what a process might be doing when it receives SIGTERM — what kind of cleanup might it perform? Describe a real scenario where killing a database or web server with SIGKILL instead of SIGTERM could cause actual data loss or service degradation.

2. **Monitoring philosophy** — Some organizations run dedicated monitoring platforms (Nagios, Zabbix, Datadog, Prometheus) while others rely on built-in commands like those in this module. When is `vmstat` or `free` sufficient, and when does the overhead of a monitoring platform pay off? Consider factors like team size, number of servers, and alerting requirements.

3. **The load average debate** — Load average has been criticized as a misleading metric because it includes processes in D state (uninterruptible sleep), which could be caused by I/O wait rather than CPU saturation. If a server shows a load average of 8 on a 4-core system but `vmstat` shows `wa` (I/O wait) near 0 and `id` (idle) near 60%, what is likely happening and what tool would you use to investigate further?

4. **Cron at scale** — As a sysadmin managing 50 servers, you realize that each server has its own crontab with slightly different versions of the same maintenance scripts. This "crontab drift" makes updates risky — changing one server misses others. How would you solve this problem? Think about configuration management tools, centralized scheduling, or architectural approaches that eliminate per-server crontabs.

---

## Response Guidelines

Strong initial posts will:

- Reference specific commands and outputs from the module
- Connect the question to a real or plausible professional scenario
- Demonstrate understanding of trade-offs (not just "X is better than Y")
- Show that you have thought about failure modes, not just happy paths

Strong response posts will:

- Engage with a specific claim or scenario your classmate described
- Add a counter-example, edge case, or additional tool they did not mention
- Share related professional experience or a scenario from another course or job

---

## Grading Rubric

| Criterion | Excellent (A) | Satisfactory (B/C) | Needs Work (D/F) |
|---|---|---|---|
| Depth of analysis | Addresses 2+ prompts with original insight; references specific commands | Addresses 1–2 prompts; mostly restates module content | Vague generalities; no specific technical references |
| Technical accuracy | All claims and command references are correct | Minor inaccuracies that do not undermine the argument | Significant factual errors |
| Professional relevance | Connects to a realistic job scenario with concrete details | Scenario mentioned but underdeveloped | No professional connection |
| Peer engagement | Substantively extends or challenges a classmate's specific argument | Acknowledges classmate but adds little new content | Generic or absent response |
| Writing quality | Clear, organized, college-level prose; meets word count | Understandable but informal or slightly short | Difficult to follow or significantly under length |

---

## Instructor Notes

Prompt 1 (SIGKILL) is accessible to all students — everyone has forcefully closed an application and lost data. Push students to think about database transaction logs, in-memory write buffers, and open network connections.

Prompt 3 (load average) targets students who read more deeply. The correct answer involves the D state contribution to load average. `vmstat` showing `wa≈0` with high load but significant idle CPU is a classic sign of a single-threaded application bottlenecked on one core, or an I/O subsystem issue that only affects specific processes. `iostat -x` and `lsof` would be the next investigative steps.

Prompt 4 (cron at scale) is intentionally open-ended. Accept answers ranging from "use Ansible to deploy crontabs" to "migrate to Kubernetes CronJobs" to "use a job scheduler like Jenkins or Rundeck." The goal is systems thinking, not a specific right answer.

---

*End of Module 05 Discussion*
