# Lab Activity: Module 11 — Incident Detection and Response Procedures

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Lab Overview

**Lab Title**: Conducting a Full Incident Response — The Apex Logistics Breach

**Estimated Time**: 90–120 minutes

**Format**: Individual assignment with written deliverables

**Submission**: Upload all deliverables as a single PDF or ZIP to the course LMS by the posted due date.

---

## Scenario Background

**Apex Logistics Solutions** is a mid-sized freight and supply chain company with 2,200 employees, 14 distribution centers, and operations across 8 US states. Apex maintains a customer portal used by 18,000 business clients to track shipments and manage invoices. The portal stores customer contact information, shipment data, and billing records including partial payment card information.

You are the Information Security Manager at Apex. It is a Tuesday morning when your SIEM fires an automated alert.

---

## The Incident Timeline

Use this timeline for all lab deliverables. Events are presented in the order your team discovered them. Do not assume you know future information when answering questions about an earlier point in time.

**07:14 AM — SIEM Alert**

SIEM fires a High-severity alert: "Unusual volume of outbound HTTPS connections from DB-PORTAL-02 to external IP 185.220.101.47." DB-PORTAL-02 is the primary database server for the customer portal. The IP address resolves to a known Tor exit node.

**07:31 AM — Initial Triage**

Your on-call analyst confirms the alert is genuine. The connection pattern began at approximately 11:48 PM the previous night. Total outbound data volume: approximately 2.1 GB over 7.5 hours. Connection is ongoing at time of discovery.

**08:02 AM — EDR Investigation**

Your EDR platform reveals that DB-PORTAL-02 has a web shell installed at `/var/www/html/admin/upload_handler.php`. The web shell was first written to disk on the previous Saturday at 3:17 PM — three days before detection. Process trees show the web shell has been used to execute database query commands.

**08:45 AM — Scope Expansion**

Log analysis reveals that the threat actor used the web shell to move laterally to APP-PORTAL-01 (the application server) and FILE-03 (an internal file server storing employee HR records). Both systems show signs of the same web shell technique.

**09:12 AM — Data Assessment**

Your database administrator confirms that DB-PORTAL-02 contains portal customer records for approximately 14,200 customers. The data includes names, email addresses, physical addresses, and the last four digits of payment cards. The lateral movement to FILE-03 potentially exposed HR records for 2,200 employees including Social Security numbers.

**10:30 AM — External Discovery Risk**

Your threat intelligence team finds a post on a dark web forum — timestamped approximately 6 hours ago — offering "Apex Logistics customer database" for sale, listing sample records that match your customer portal schema.

**02:00 PM — Containment Completed**

After completing initial evidence collection, your team has isolated all three affected systems from the network.

---

## Task 1 — Detection and Triage Analysis (20 points)

### Task 1 Instructions

Step 1: Analyze the 07:14 AM SIEM alert. Using the four triage questions from Module 11, complete a structured triage assessment as it would have existed at 07:31 AM — using only information available at that time. Do not use information discovered later.

Step 2: Identify the **specific Indicators of Compromise** present in this incident. List at least five distinct IoCs with their type (IP, hash, behavioral, etc.) and source.

Step 3: Assess the **detection timeline**. Calculate the dwell time for this incident. Explain what detection gaps or monitoring weaknesses allowed the attacker to operate undetected for this period. Propose two specific detection improvements that would have reduced dwell time.

### Task 1 Deliverable

A triage assessment table for the 07:31 AM decision point, an IoC table with five or more entries, and a dwell time analysis paragraph (four to six sentences) with two detection improvement recommendations.

---

## Task 2 — Containment Decision Analysis (25 points)

### Task 2 Instructions

Step 1: At 08:02 AM, your team has confirmed the web shell and active exfiltration. You must make the immediate containment decision. Using the containment strategy selection principles from Module 11, recommend a specific containment approach for DB-PORTAL-02 at this point in time. Your recommendation must:

- Specify whether you recommend immediate isolation or continued monitoring before isolation.

- Justify your choice by applying the evidence-versus-speed trade-off framework.

- Identify the volatile evidence that must be collected before isolation if you recommend isolation.

- Explain what business impact your containment action will have and how you will communicate this to the CFO and COO.

Step 2: At 08:45 AM, you discover lateral movement to APP-PORTAL-01 and FILE-03. How does this new information change your containment strategy? Explain specifically what new containment actions are required and in what order you prioritize them.

Step 3: Create a containment activity log for the period from 07:14 AM to 02:00 PM using the template below:

| Time | Action Taken | Authorized By | System/Asset Affected | Evidence Collected (Y/N) | Impact |
|---|---|---|---|---|---|
| (fill in) | | | | | |

Include a minimum of eight log entries covering the period.

### Task 2 Deliverable

Containment recommendation paragraph (Task 2 Step 1, minimum five sentences), strategy update paragraph (Task 2 Step 2, minimum four sentences), and completed containment activity log.

---

## Task 3 — Eradication Plan (20 points)

### Task 3 Instructions

At 02:00 PM, containment is complete. All three affected systems are isolated. You now plan eradication.

Step 1: Create a complete **Eradication Checklist** for this incident. Your checklist must cover all three affected systems and must include the following categories:

- Malware and web shell removal (with specific verification steps).

- Persistence mechanism identification and elimination.

- Credential rotation requirements (list all credential types that must be rotated and why).

- Vulnerability remediation (identify the probable attack vector and what must be closed before recovery).

Step 2: Explain how you will **validate** that eradication is complete before authorizing recovery to begin. Your validation plan must include at least three specific validation activities.

Step 3: Identify the **likely initial attack vector** for this incident based on the timeline. Explain your reasoning and describe the control that, if in place, would most likely have prevented initial access.

### Task 3 Deliverable

Completed eradication checklist (table format), validation plan paragraph (three to five sentences with three validation activities), and initial attack vector analysis paragraph (four to six sentences).

---

## Task 4 — Post-Incident Documentation and Lessons Learned (35 points)

### Task 4 Instructions

**Part A — Incident Timeline Document**: Construct a complete incident timeline from Saturday 3:17 PM (initial compromise) through 02:00 PM Tuesday (containment complete). Include all significant events with timestamps, what was known at each point, and who was notified. Format as a table.

**Part B — Notification Assessment**: Based on the data exposure described in the incident:

- Identify all external parties that Apex Logistics is legally or contractually obligated to notify.

- For each party, specify the applicable regulation or contract, the notification deadline, and whether Apex has already passed that deadline (assume today is the Tuesday of the incident).

- Identify any notification obligations that are at risk of being missed given the timeline.

**Part C — Lessons-Learned Report**: Write a structured lessons-learned report for this incident. Your report must contain:

- An executive summary of the incident (2–3 sentences for a non-technical audience).

- A list of three specific things the Apex security program did well.

- A list of four specific failures or gaps revealed by this incident.

- Root cause analysis for the primary failure (use the Five Whys method — ask "why" at least four times drilling down to a fundamental cause).

- Four specific, actionable recommendations with assigned owner titles and 90-day completion targets.

**Part D — IRP Update Recommendations**: Based on what this incident revealed, identify two specific changes that should be made to Apex's Incident Response Plan. For each change, explain what gap the current plan has and what the revised plan should say.

### Task 4 Deliverable

Incident timeline table (Part A), notification assessment table (Part B), lessons-learned report (Part C, written in complete sentences in paragraph and table format), and IRP update recommendations (Part D, two to three sentences each).

---

## Grading Rubric

| Deliverable | Points | Criteria |
|---|---|---|
| Task 1 — Detection and Triage | 20 | Triage assessment limited to information available at 07:31 AM; IoC table has five or more distinct entries; dwell time calculated correctly; detection improvement recommendations are specific and actionable |
| Task 2 — Containment | 25 | Containment recommendation applies evidence vs. speed framework correctly; lateral movement response is appropriately sequenced; activity log covers the full period with eight or more entries |
| Task 3 — Eradication | 20 | Eradication checklist covers all three systems and all required categories; validation activities are specific; attack vector analysis is reasoned and supported by timeline evidence |
| Task 4 — Post-Incident | 35 | Timeline document is complete and accurate; notification assessment correctly identifies all applicable obligations and deadline risks; lessons-learned report contains all required sections; Five Whys reaches a fundamental cause; IRP update recommendations are specific |
| **Total** | **100** | |

### Grading Notes

- Task 1 answers that use information available only after 08:00 AM in their 07:31 AM triage assessment will lose up to 10 points. Triage is a point-in-time process.

- Task 2 containment activity logs with fewer than eight entries lose 5 points.

- Task 4 Part B notification assessments that miss the GDPR implication (if any EU customers are included in portal data) or the SEC reporting question will lose up to 5 points.

- Task 4 Part C Five Whys analyses that stop at the first symptom rather than drilling to a root cause will lose up to 5 points.

---

## Submission Checklist

Before submitting, verify:

- [ ] Task 1 triage table covers all four triage questions.

- [ ] Task 1 IoC table lists five or more distinct indicators.

- [ ] Task 1 dwell time is correctly calculated and explained.

- [ ] Task 2 containment recommendation specifies isolation vs. monitoring with justification.

- [ ] Task 2 addresses lateral movement to both additional systems.

- [ ] Task 2 activity log has eight or more timestamped entries.

- [ ] Task 3 eradication checklist covers all three systems and all four categories.

- [ ] Task 3 includes three validation activities.

- [ ] Task 3 includes attack vector analysis paragraph.

- [ ] Task 4 Part A incident timeline covers Saturday through Tuesday.

- [ ] Task 4 Part B notification table identifies all applicable obligations with deadlines.

- [ ] Task 4 Part C lessons-learned report contains all required sections.

- [ ] Task 4 Part C Five Whys reaches a fundamental root cause.

- [ ] Task 4 Part D includes two specific IRP update recommendations.

- [ ] All deliverables compiled in a single PDF or ZIP file.

---

## Learning Connection

The Apex Logistics scenario compresses the full NIST SP 800-61 lifecycle — phases two, three, and four — into a single lab exercise. Working through it forces you to make the trade-off decisions that real incident responders make under time pressure.

The skills you apply here — structured triage, evidence-versus-speed judgment, eradication planning, and lessons-learned documentation — are among the most tested competencies in CISM Domain 4. More importantly, they are among the most consequential skills in professional security management. The decisions made in the first two hours of an incident determine much of the outcome.

Keep your completed deliverables. The incident timeline and lessons-learned report formats you produced are directly applicable to real-world incident response documentation.
