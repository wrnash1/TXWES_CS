# Lab: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Lab Overview

**Title:** Asset Reconciliation, CMDB Design, and License Compliance Analysis

**Duration:** 90–120 minutes

**Format:** Individual written deliverables

**Submission:** Upload completed documents to the LMS by the module deadline.

In this lab you will perform three applied exercises: building an asset reconciliation analysis from raw discovery data, designing a partial CMDB record set with relationships, and conducting a software license compliance assessment.

---

## Scenario

**Organization:** Plainview County School District IT Department

**Environment:**

- 3 elementary schools, 2 middle schools, 1 high school
- Central IT office manages assets for all campuses
- Approximately 850 end-user devices (student and staff laptops, desktop workstations)
- 12 physical servers in a central data center
- 47 network switches and access points
- Active Directory + Microsoft 365 tenant (E3 licenses)
- Adobe Creative Cloud deployed in the high school's design lab (25 devices)
- Multiple legacy applications from a previous IT team with incomplete records

---

## Part 1: Asset Reconciliation (30 minutes)

The IT team ran a network-based discovery scan across all six campus networks. The following table shows the discovery results alongside the current asset register entries. Your job is to categorize each asset using the four reconciliation states and recommend a next action.

### Discovery vs. Asset Register Data

| Asset Tag | Serial Number | Type | Register Status | Discovery Result | Reconciliation Category | Recommended Action |
|---|---|---|---|---|---|---|
| PCSD-0042 | SRV-X4421 | Server | Active — Data Center | Found — IP 10.1.1.5 | | |
| PCSD-0091 | LAP-GH772 | Laptop | Active — HS Lab 3 | Not found | | |
| (none) | NET-SS881 | Switch | Not in register | Found — IP 10.3.2.1 | | |
| PCSD-0237 | LAP-TT390 | Laptop | Active — MS2 | Found — IP 10.5.1.44 | | |
| PCSD-0018 | SRV-Q2210 | Server | Disposed 14 months ago | Found — IP 10.1.1.9 | | |
| PCSD-0312 | LAP-BK004 | Laptop | Active — Elem1 | Found — IP 10.2.1.17 | | |
| PCSD-0099 | DES-WW331 | Desktop | Active — Central IT | Not found | | |
| (none) | TAB-ZZ009 | Tablet | Not in register | Found — IP 10.6.1.88 | | |

**Instructions:**

For each row, complete the Reconciliation Category column using one of: Known and Found, Known but Not Found, Found but Not Known, Known as Disposed.

Then complete the Recommended Action column with a specific, realistic action (not just "investigate" — say what to investigate, with whom, and by when).

**Written response (150–200 words):** Two of the entries above represent significant security or compliance risks that should be escalated beyond routine follow-up. Identify which two, explain the specific risk each poses, and recommend an escalation path (who should be notified, what immediate action should be taken).

---

## Part 2: CMDB Design Exercise (30 minutes)

You are designing CMDB records for the school district's student information system (SIS), which is critical for attendance, grades, and state reporting.

### System Components

- **Application server:** SIS-APP-01 (Windows Server 2022, 16 core, 64 GB RAM, IP 10.1.1.20)
- **Database server:** SIS-DB-01 (SQL Server 2022, Windows Server 2022, 16 core, 128 GB RAM, IP 10.1.1.21)
- **Web front end:** SIS-WEB-01 (IIS on Windows Server 2022, IP 10.1.1.22)
- **Application:** PowerSchool SIS v23.4
- **Service:** "Student Information System" — business service consumed by all 6 campuses, central admin, and the state reporting portal.

**Task 2a — CI Records:** Complete the CMDB CI table below for all five components. For each CI, define: CI Name, CI Type, Key Attributes (at least 3), Current Status, and Owner.

| CI Name | CI Type | Key Attributes | Status | Owner |
|---|---|---|---|---|
| SIS-APP-01 | | | | |
| SIS-DB-01 | | | | |
| SIS-WEB-01 | | | | |
| PowerSchool SIS v23.4 | | | | |
| Student Information System | | | | |

**Task 2b — Relationship Map:** Draw or describe (in text format if you cannot draw) the relationships between these five CIs. Use relationship types from the reading guide: Runs on, Depends on, Hosts, Part of, Connects to. Show at least six distinct relationships.

**Task 2c — Impact Scenario:** Using your relationship map, answer this question: SIS-DB-01 experiences a hardware failure at 8:00 AM on a school day. Based on your CMDB relationships, list every CI and every user group that is impacted. Which state reporting obligations could be affected? (2–3 sentences)

---

## Part 3: Software License Compliance Analysis (30 minutes)

The district's Microsoft 365 E3 contract includes 950 licensed seats for staff and teachers. The Adobe Creative Cloud contract covers 25 device licenses for the high school design lab.

### Microsoft 365 Discovery Data

A recent user activity report from the Microsoft 365 admin portal shows:

- 847 accounts have signed in within the last 30 days (active users).
- 103 accounts have not signed in within the last 90 days. Of these: 62 are retired or separated employees (per HR records); 41 are active employees who simply have not used M365 recently.
- 12 accounts are shared/service accounts (no associated named user).

### Adobe Creative Cloud Discovery Data

Agent-based discovery on the high school campus found Adobe Creative Cloud installed on:

- 25 designated design lab computers.
- 7 teacher laptops (Art department teachers installed it independently).
- 4 student laptops checked out from the laptop cart.

Total installations: 36 devices. Licensed: 25 devices.

**Task 3a — Microsoft 365 Compliance Position:**

Calculate the effective license utilization:

- How many licenses are actively used?
- How many licenses are potentially excess (could be reclaimed)?
- Is the district over-licensed, under-licensed, or approximately compliant?
- What actions would you recommend for the 62 separated employees and the 41 inactive-but-active employees?

**Task 3b — Adobe Creative Cloud Compliance Position:**

- Is the district currently in compliance or out of compliance with its Adobe agreement? By how many licenses?
- Who should be notified of this situation?
- What immediate steps should the IT team take?
- Write a brief email (3–5 sentences) to the High School Principal explaining the situation in non-technical terms and requesting cooperation with the remediation plan.

**Task 3c — SAM Improvement Recommendation:**

The off-boarding process for the school district does not currently include an IT step to disable M365 accounts and reclaim licenses when staff separate. Write a brief process improvement recommendation (5–7 bullet points) defining what the off-boarding IT checklist should include to prevent license waste and security exposure from active accounts belonging to separated employees.

---

## Submission Requirements

Submit one document (PDF or Word) containing:

- Part 1: Completed reconciliation table and written escalation response.
- Part 2: Completed CI table, relationship map/description, and impact scenario answer.
- Part 3: Compliance analysis for both products, principal email, and SAM improvement recommendation.

**Minimum length:** 800 words across written sections.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Part 1 reconciliation accuracy and escalation quality | 30 |
| Part 2 CMDB design completeness and relationship accuracy | 30 |
| Part 3 license compliance analysis and recommendations | 30 |
| Professional writing and formatting | 10 |
| **Total** | **100** |

---

*End of Module 13 Lab — approximately 160 lines*
