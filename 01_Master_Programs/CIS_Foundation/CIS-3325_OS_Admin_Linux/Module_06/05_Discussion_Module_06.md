# Discussion: Module 06 — Storage and Disk Management

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

Storage is where failures become permanent. Unlike a misconfigured process or a broken script, a storage failure can mean irretrievable data loss. The decisions made in storage management — partition table, filesystem type, LVM vs. fixed partitions, RAID level — have long-lasting consequences.

Reflect on the following questions and address **at least two** in your initial post:

1. **The fstab danger zone** — A bad `/etc/fstab` entry for the root filesystem can prevent a server from booting. Some cloud providers (AWS, Azure, GCP) specifically warn about this in their documentation. How would you safely test an fstab change before rebooting a production server? Describe the steps you would take to verify the entry is correct, including what commands you would run and what outcome you would look for. What is the `nofail` option, and when should you use it versus not use it?

2. **LVM vs. fixed partitions** — Most enterprise Linux installations use LVM rather than fixed partitions. What concrete problems does LVM solve that you cannot easily solve with fixed partitions? Are there situations where LVM adds complexity without proportionate benefit — for example, on a small single-disk VM or an embedded device? Where is the right place to use LVM and where would you skip it?

3. **RAID level selection** — Imagine you are setting up storage for two different scenarios:
   - A database server running a payment processing application (high write I/O, zero tolerance for data loss)
   - A media server storing video archives (sequential read, infrequent writes, cost-sensitive)

   Which RAID level would you choose for each, and why? Justify your selection in terms of the redundancy, performance, and cost trade-offs we covered.

4. **Disk health and the monitoring gap** — SMART monitoring can give early warning of a failing disk, but many organizations do not monitor SMART data proactively. By the time a disk shows obvious failure symptoms — slowness, read errors in logs — significant damage may have already occurred. Design a basic disk health monitoring strategy for a 10-server environment: what would you check, how often, and how would you be alerted?

---

## Response Guidelines

Strong initial posts will:

- Address two or more prompts with specific technical detail
- Name commands, tools, or configuration options from the module
- Describe trade-offs rather than presenting a single "right answer"
- Connect the technical content to a realistic failure mode or production scenario

Strong response posts will:

- Challenge or extend a specific claim your classmate made
- Offer a scenario or counter-example they did not consider
- Share related experience from work, home labs, or other coursework

---

## Grading Rubric

| Criterion | Excellent (A) | Satisfactory (B/C) | Needs Work (D/F) |
|---|---|---|---|
| Depth of analysis | Addresses 2+ prompts with original insight; references specific commands | Addresses 1–2 prompts; mostly restates module content | Vague generalities; no specific technical references |
| Technical accuracy | All claims, commands, and reasoning are correct | Minor inaccuracies that do not undermine the argument | Significant factual errors |
| Professional relevance | Connects to a realistic production scenario with concrete details | Scenario mentioned but underdeveloped | No professional connection |
| Peer engagement | Substantively extends or challenges a classmate's specific argument | Acknowledges classmate but adds little new content | Generic or absent response |
| Writing quality | Clear, organized, college-level prose; meets word count | Understandable but informal or slightly short | Difficult to follow or significantly under length |

---

## Instructor Notes

Prompt 1 (fstab safety) has a definitive answer: `sudo mount -a` after editing fstab (but before rebooting) will attempt to mount all entries and show errors. Students should also know about `nofail` — it prevents a failed non-critical mount from halting the boot process. This is essential knowledge for cloud VMs where external volumes may not always be attached.

Prompt 3 (RAID selection) reinforces that there is no universally correct RAID level. The payment processor answer (RAID 10 for performance + redundancy) and the media server answer (RAID 5 or 6 for capacity efficiency) are both defensible if the reasoning matches the requirements. Look for students who identify the write penalty of RAID 5 as the reason to avoid it for high-write workloads.

Prompt 4 (monitoring strategy) is open-ended by design. Accept answers that include `smartd` (the smartmontools daemon), scheduled `smartctl -H` via cron, or integration with monitoring platforms. The goal is systems thinking about proactive vs. reactive monitoring.

---

*End of Module 06 Discussion*
