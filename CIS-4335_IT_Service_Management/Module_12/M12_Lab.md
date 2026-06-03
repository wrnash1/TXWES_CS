# Lab: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Lab Overview

**Title:** Planning and Reviewing a Production Release

**Duration:** 90–120 minutes

**Format:** Individual written deliverables with peer review component

**Submission:** Upload completed documents to the LMS by the module deadline.

In this lab you will work through the complete lifecycle of a fictional software release: drafting a release note, selecting and justifying a deployment strategy, running a simulated go/no-go checklist, and completing a post-implementation review after a simulated deployment event.

---

## Scenario

**Organization:** Lone Star Financial Services (LSFS)

**Application:** LSFS Mobile Banking App — iOS and Android

**Proposed Release:** Version 3.2.0

**What is changing:**

- New biometric login feature (Face ID and fingerprint) replacing PIN-only authentication.
- Bug fix for intermittent transaction timeout errors affecting approximately 8% of users.
- Updated privacy policy acceptance modal (regulatory requirement — must deploy by the 15th of the month).
- Performance improvement: reduced average app load time by 1.2 seconds.

**Environment facts:**

- Production user base: 142,000 active mobile users.
- Current uptime SLA: 99.5% (allows approximately 3.6 hours downtime per month).
- Deployment window: Saturday 2:00 AM – 6:00 AM Central Time.
- Previous release (3.1.5) caused a 45-minute outage three months ago due to a database migration error.
- The privacy policy modal is a regulatory requirement with a hard deadline.

---

## Part 1: Draft a Release Note (30 minutes)

Using the standard release note structure from the reading guide, draft a complete release note for LSFS Mobile Banking App v3.2.0.

Your release note must include all of the following sections:

### Required Sections

**1. Release Identifier**

Provide version number, release name (your choice), scheduled deployment date (use a realistic future date), and the deployment window.

**2. Change Request References**

Invent three plausible change request IDs (e.g., CHG-2024-0442) — one for each major change area: biometric login, the bug fix, and the privacy modal. You do not need real IDs — the exercise is about structure.

**3. Scope Summary**

Write 2–4 sentences summarizing what this release delivers in plain language suitable for business stakeholders.

**4. Components Affected**

List specific components: mobile app binary, authentication service API, database tables (if any), backend microservices affected.

**5. Pre-Deployment Prerequisites**

List at least five specific steps that must be completed before the deployment window opens.

**6. Validation Criteria**

List at least four specific pass/fail tests that confirm a successful deployment (e.g., "Biometric login succeeds on both iOS 17 and Android 14 test devices").

**7. Rollback Procedure**

Write a brief but realistic rollback procedure. Note: mobile app stores have delays for rolling back — address this constraint.

**8. Known Issues**

Document at least one known issue that will not be fixed in this release, with a target resolution version.

**9. Support Contacts**

List roles and fictional names: Deployment Lead, On-Call DBA, Mobile Platform Engineer, Help Desk Escalation Contact.

---

## Part 2: Select and Justify a Deployment Strategy (20 minutes)

Review the three primary deployment strategies from the reading guide: big bang, phased, and canary.

**Answer the following questions in 1–2 paragraphs each:**

**Question 2a:** Which deployment strategy would you recommend for LSFS v3.2.0, and why? Your answer must reference at least two specific characteristics of this release scenario (e.g., the hard regulatory deadline, the 142,000 user base, the previous outage history, the mobile app store constraints).

**Question 2b:** What strategy would you use if the regulatory deadline were removed and you had four additional weeks to deploy? Explain what changes in your risk calculus.

**Question 2c:** The biometric login feature involves a backend authentication service API change. What compatibility concern must be addressed during the deployment window if any users are still running version 3.1.5 after the deployment begins? What does this imply about your chosen strategy?

---

## Part 3: Go/No-Go Checklist Simulation (20 minutes)

It is 1:45 AM on Saturday — 15 minutes before the deployment window opens. You are the Release Manager conducting the go/no-go review.

**The following status report has just arrived:**

- All unit and integration tests passed earlier today.
- The regression test suite completed at 11:00 PM — 2 test cases are marked "skipped" due to a test environment configuration issue; they were last run successfully 8 days ago.
- The Help Desk briefing was scheduled for 1:00 PM Friday but the lead engineer had a family emergency; the Help Desk received the release notes by email at 6:00 PM but no live briefing occurred.
- Production database backup completed at 12:30 AM — verified.
- The on-call DBA is confirmed available.
- Network change to update the API gateway timeout setting was supposed to be completed by 11:00 PM but the networking team has not confirmed completion. The deployment lead has sent two Slack messages with no response.

**Your task:** Complete the go/no-go checklist below. For each item, mark GO or NO-GO and provide a one-sentence rationale. Then make a final recommendation: proceed, hold, or proceed with conditions?

| Criterion | Status | Rationale |
|---|---|---|
| Regression tests fully passed | | |
| Help Desk briefed and prepared | | |
| Production backup verified | | |
| On-call DBA available | | |
| Infrastructure changes confirmed complete | | |
| Release notes distributed | | |

**Final recommendation and written justification (3–5 sentences):** State your decision and the reasoning behind it. If you recommend "proceed with conditions," specify exactly what conditions must be met and by whom within what timeframe.

---

## Part 4: Post-Implementation Review (30 minutes)

The deployment has been completed. It is now Monday morning, 48 hours after go-live. You have gathered the following data:

**Deployment outcomes:**

- Deployment completed at 4:47 AM — 47 minutes past the end of the scheduled window (ended at 6:00 AM).
- The API gateway timeout setting was completed by the networking team at 2:23 AM (23 minutes into the deployment window) — confirmed before proceeding.
- Biometric login is functional on iOS. Android Face ID is failing on Samsung Galaxy devices running Android 13 — affecting approximately 11,000 users. Those users fall back to PIN login successfully.
- The transaction timeout bug fix is confirmed resolved.
- Privacy policy modal is live and users are accepting at the expected rate.
- Three Priority 3 help desk tickets were raised about the Android Face ID issue.
- The Help Desk handled the tickets adequately but the lead engineer noted they would have preferred a live briefing.

**Complete a structured PIR report addressing each of the following:**

**4a. Schedule Adherence:** Was the deployment on time? What caused the overrun? Was this acceptable given the maintenance window constraints?

**4b. Acceptance Criteria Assessment:** Which criteria were met? Which were not met? What is the status of the Android Face ID defect?

**4c. Incident Impact:** Describe the scope and severity of the Android Face ID issue. Was this a release failure or an acceptable known limitation?

**4d. Communication Assessment:** Evaluate the Help Desk preparation process. What should change for the next release?

**4e. Lessons Learned:** List three specific, actionable lessons from this deployment. For each lesson, specify: what happened, what should change, and who owns the change.

**4f. Continual Improvement Actions:** Based on your PIR findings, write two improvement items for the Continual Improvement register. Format each as: **Issue | Current State | Target State | Owner | Due Date.**

---

## Submission Requirements

Submit one document (PDF or Word) containing:

- Part 1: Complete release note (formatted clearly).
- Part 2: Three written responses.
- Part 3: Completed checklist table and final recommendation.
- Part 4: Structured PIR report with all six sections.

**Minimum length:** 1,200 words across all parts.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Release note completeness and realism | 25 |
| Deployment strategy justification (quality of reasoning) | 20 |
| Go/no-go checklist accuracy and final recommendation | 20 |
| PIR depth and quality of lessons learned | 25 |
| Professional writing and formatting | 10 |
| **Total** | **100** |

---

## Peer Review Component (optional +5 bonus)

Exchange your go/no-go recommendation (Part 3) with a classmate. Write a 100-word response to their recommendation: do you agree? Would you have made a different call? What factors did they weigh that you did not? Submit the peer review alongside your main lab document.

---

*End of Module 12 Lab — approximately 175 lines*
