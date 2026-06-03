# Lab Activity: Module 09 — Incident Response: Containment and Recovery

## Course: CIS-4332 Cyber Analyst | Texas Wesleyan University

## Instructor: Professor Nash

## CySA+ CS0-003 Domain: Domain 1 - Security Operations (33%)

---

## Lab Overview

In this lab you will serve as the lead incident responder for a confirmed multi-system malware incident at Meridian Financial Services, continuing the scenario introduced in the Module 08 lab. You will make containment decisions, build a complete eradication plan, document a recovery validation procedure, and write a post-incident summary. All scenario data is provided within this document. No external software or environments are required.

Total Points: 100

Estimated Completion Time: 75-90 minutes

Submission: Upload your completed Lab Report to the Canvas Module 09 Lab assignment.

---

## Learning Objectives

By completing this lab you will be able to:

- Select appropriate short-term and long-term containment actions for a multi-system incident
- Build a complete eradication checklist addressing all artifact types and persistence mechanisms
- Develop a recovery validation plan that confirms the attack vector is closed
- Conduct a backup integrity assessment for a ransomware-adjacent scenario
- Write a post-incident summary suitable for management reporting

---

## Scenario Context

It is Tuesday morning. You are the on-call IR lead at Meridian Financial Services. The Module 08 lab escalation has been fully triaged and confirmed by Tier 2. The incident involves a commodity RAT dropped via a malicious Excel macro attachment. The complete scope from Module 08 IOC pivoting is:

WS-FINANCE-08: Primary patient zero. Confirmed malware execution. C2 active. Persistence via registry run key and scheduled task confirmed.

WS-HR-04: C2 domain queried three times in the past 24 hours. No hash match confirmed. No EDR behavioral alert.

WS-EXEC-01: C2 IP contact confirmed in proxy logs. EDR reports process injection into explorer.exe by svcupd.exe (same hash as WS-FINANCE-08).

WS-DEV-11: C2 domain queried once, 18 hours ago. No other IOC match. No behavioral alert.

The malware established the following persistence on WS-FINANCE-08 and WS-EXEC-01 (confirmed):

- Registry run key: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\WindowsUpdate` pointing to `C:\Users\Public\svcupd.exe`
- Scheduled task: `WindowsUpdate` executing `C:\Users\Public\svcupd.exe` on user logon

The initial access vector was a phishing email containing a macro-enabled Excel attachment. The macro exploited an unpatched vulnerability in Microsoft Office (CVE-2024-38200). The vulnerability has a patch available from Microsoft.

The following accounts were active during the incident period and may have been exposed:

- `jsmith` — finance analyst account on WS-FINANCE-08
- `mwilliams` — executive account on WS-EXEC-01
- `finance_svc` — service account with read access to the finance database

IT has confirmed that Meridian Financial Services maintains daily incremental backups to an on-premises backup server (backup server was on the same VLAN as WS-FINANCE-08) and weekly full backups to an immutable cloud storage bucket (last full backup: Sunday at 2:00 AM, 72 hours before the incident was detected).

---

## Exercise 1: Containment Actions (25 points)

### Task 1A — Immediate Containment Plan (15 points)

For each of the four systems in scope, specify the exact short-term containment action you would take and the reason for your choice. Then describe one short-term containment action that applies to the entire environment.

Your answer must address:

1. The specific containment action for each system (EDR isolation, account disable, network block, or a justified alternative)
2. The reason the action is appropriate for that system's confirmed evidence level
3. Whether any system should NOT be isolated immediately and why
4. The one environment-wide containment action and what attacker capability it removes

Scoring: 3 points per system (1 for correct action, 2 for accurate justification) plus 3 points for the environment-wide action.

### Task 1B — Long-Term Containment Decisions (10 points)

Now that short-term containment is in place, describe the long-term containment strategy for this incident. In 4-5 sentences, address:

1. What long-term containment measures are appropriate given this incident's scope
2. How the finance_svc service account should be handled during the long-term containment period (it cannot be fully disabled without impacting finance operations)
3. What compensating control you would implement for the unpatched Microsoft Office vulnerability while patching is in progress across all endpoints

---

## Exercise 2: Eradication Plan (30 points)

### Task 2A — Full Eradication Checklist (20 points)

Build a complete eradication checklist for this incident. Your checklist must be organized by the five eradication steps from the Reading Guide and must address each step specifically for this incident's IOCs and scope.

Your checklist must include:

For Step 1 (Remove malware artifacts): the specific file path and hash of the artifact to remove on each confirmed compromised system.

For Step 2 (Remove persistence mechanisms): the specific registry key path and value name, and the specific scheduled task name to remove. Address both WS-FINANCE-08 and WS-EXEC-01 specifically.

For Step 3 (Reset compromised credentials): which accounts must be reset, and why each is included in the reset scope. Address all three accounts listed in the scenario context.

For Step 4 (Patch exploited vulnerability): the CVE ID and the scope of systems that must be patched.

For Step 5 (Verify eradication): describe the specific EDR hunt query you would run and what you would look for in the results to confirm eradication is complete across all four in-scope systems.

Scoring: 4 points per step (2 for correct identification of what to address, 2 for specificity and completeness).

### Task 2B — Eradication Scope for Potentially Compromised Systems (10 points)

WS-HR-04 and WS-DEV-11 had C2 domain queries but no confirmed malware execution. In 4-5 sentences, address:

1. Should these systems go through the full eradication checklist or a reduced scope? Justify your answer using the scope classification framework from the Reading Guide.
2. What specific eradication steps are most critical for a system classified as "potentially compromised" versus "confirmed compromised"?
3. What finding during the eradication process would cause you to reclassify WS-HR-04 from potentially compromised to confirmed compromised?

---

## Exercise 3: Recovery Planning (25 points)

### Task 3A — Recovery Approach Selection (10 points)

For each of the four in-scope systems, select a recovery approach (restore from backup, reimage from clean baseline, or in-place remediation) and justify your selection in 1-2 sentences per system.

Your justification must address:

1. Why the selected approach is most appropriate given the system's confirmed compromise level
2. For any system you recommend restoring from backup, address the backup integrity question specifically using the scenario's backup details

### Task 3B — Backup Integrity Assessment (8 points)

Based on the scenario context, assess the backup options available for WS-FINANCE-08. In 4-5 sentences, address:

1. Which backup option (daily incremental to on-premises server, or weekly full to immutable cloud storage) provides a clean recovery point and why
2. Why the on-premises backup server's backup may not be trusted and what the specific risk is
3. What the maximum data loss would be if the immutable cloud backup is used
4. What you would verify about the cloud backup before beginning the restore

### Task 3C — Recovery Validation Plan (7 points)

Write a complete recovery validation plan for WS-FINANCE-08 after recovery. Your plan must address all five items from the recovery validation checklist in the Reading Guide, applied specifically to this incident's IOCs and initial access vector.

---

## Exercise 4: Post-Incident Summary (20 points)

### Task 4A — Management Summary (12 points)

Write a post-incident summary suitable for distribution to the CISO and department heads at Meridian Financial Services. Your summary must include the following labeled sections:

Incident Overview: One paragraph describing what happened, when it was detected, and what systems were affected.

Confirmed Impact: What data or systems were accessed or compromised during the attacker's dwell time.

Response Actions Taken: A brief ordered list of the containment, eradication, and recovery actions completed.

Root Cause: The initial access vector and vulnerability exploited.

Remediation Status: Confirmation that eradication is complete and systems have been returned to production, or current status if recovery is ongoing.

Regulatory Considerations: Does this incident trigger any notification obligations? State your reasoning.

### Task 4B — Lessons Learned (8 points)

In 5-6 sentences, identify at least three specific improvements that should result from this incident. For each improvement, address:

1. The specific gap the incident revealed (detection, response process, or security control)
2. The concrete change you recommend (new SIEM rule, playbook update, security control deployment, or training)
3. Which phase of the NIST lifecycle the gap affected

---

## Grading Rubric

| Exercise | Points | Grading Criteria |
|---|---|---|
| Exercise 1A — Immediate Containment Plan | 15 | Correct action per system with accurate justification; environment-wide action identified |
| Exercise 1B — Long-Term Containment | 10 | Appropriate long-term measures; service account handling; compensating control for unpatched CVE |
| Exercise 2A — Eradication Checklist | 20 | All five steps addressed with incident-specific detail; persistence mechanisms named specifically |
| Exercise 2B — Potentially Compromised Scope | 10 | Correct scope classification applied; appropriate eradication scope for partially confirmed systems |
| Exercise 3A — Recovery Approach Selection | 10 | Appropriate approach per system; backup integrity addressed for backup-restore selections |
| Exercise 3B — Backup Integrity Assessment | 8 | Both backup options assessed; on-premises risk identified; cloud backup data loss calculated |
| Exercise 3C — Recovery Validation Plan | 7 | All five validation items addressed with incident-specific detail |
| Exercise 4A — Management Summary | 12 | All six sections present; accurate impact statement; regulatory analysis included |
| Exercise 4B — Lessons Learned | 8 | Three specific improvements identified with gap, recommendation, and NIST phase |
| Total | 100 | |

---

## Submission Instructions

1. Use the Lab Report Template from Canvas or a clearly labeled document matching this lab's section structure.
2. Include your full name, student ID, course section, and submission date.
3. Present eradication checklists as formatted numbered lists with sub-items.
4. Submit to the Canvas Module 09 Lab assignment by the posted deadline.

---

## Academic Integrity Notice

All scenario data in this lab is fabricated for educational purposes. CVE-2024-38200 is referenced here for educational context only. All work must be your own. Reference professormesser.com and comptia.org for additional study context.
