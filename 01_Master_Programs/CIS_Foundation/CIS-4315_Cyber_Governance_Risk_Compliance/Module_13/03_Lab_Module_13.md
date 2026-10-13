# Lab Activity: Module 13 — Business Continuity Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

---

## Lab Overview

In this lab you will apply the Business Continuity Planning methodology from Module 13 to a realistic scenario. You will conduct a structured Business Impact Analysis, establish RPO and RTO targets, select continuity strategies, and produce a BCP document outline. All deliverables are written artifacts — no special software is required beyond a word processor or text editor.

**Estimated Time:** 90–120 minutes

**Grading Weight:** See Canvas assignment for point value.

---

## Scenario: Meridian Regional Hospital

Meridian Regional Hospital is a 300-bed community hospital serving approximately 85,000 patients per year. The hospital operates an electronic health records (EHR) system, a patient billing platform, a laboratory information system (LIS), an emergency department triage system, and a pharmacy dispensing system. All systems run on-premises in a single data center located in the hospital's basement.

The hospital recently experienced a ransomware event that encrypted the EHR system and caused four hours of downtime before IT staff restored from backup. The incident revealed that the hospital had no formal BCP. Hospital leadership has engaged you — as the newly hired Information Security Manager — to build one.

---

## Part 1: Business Impact Analysis

### Task 1.1 — Identify and Classify Critical Processes

Review the five systems listed in the scenario. For each system, complete the following analysis in table format.

Create a table with these columns:

- **System / Process**

- **Primary Business Function**

- **Primary Users**

- **Data Sensitivity**

- **Critical (Yes/No)**

- **Justification for Criticality Decision**

Fill in all five rows: EHR System, Patient Billing Platform, Laboratory Information System, Emergency Department Triage System, and Pharmacy Dispensing System.

**Deliverable 1:** Completed five-row classification table. (15 points)

### Task 1.2 — Dependency Mapping

For each system you classified as Critical in Task 1.1, identify at least three dependencies. Use the following dependency categories:

- Technology (applications, databases, servers, network)

- Facilities (power, HVAC, physical access)

- Personnel (roles required for operation or recovery)

- External vendors (third parties providing services or support)

For each dependency, note whether it represents a single point of failure and explain your reasoning.

**Deliverable 2:** Dependency map for each critical system (narrative or table format). Minimum three dependencies per system. (20 points)

### Task 1.3 — Impact Timeline

Select the EHR system and the Emergency Department Triage System. For each, construct an impact timeline using the template below.

**Impact Timeline Template:**

| Time Elapsed | Financial Impact | Regulatory/Legal Impact | Safety Impact | Reputational Impact | Overall Severity (Low/Medium/High/Critical) |
|---|---|---|---|---|---|
| 1 hour | | | | | |
| 4 hours | | | | | |
| 12 hours | | | | | |
| 24 hours | | | | | |
| 72 hours | | | | | |

Complete the table for both selected systems. Use realistic estimates. For financial impact, estimate dollar loss per time period based on hospital revenue assumptions (you may research or reasonably estimate average community hospital revenue per hour).

**Deliverable 3:** Completed impact timeline tables for EHR and ED Triage systems. (20 points)

---

## Part 2: Recovery Objectives

### Task 2.1 — Establish RPO, RTO, and MTPD

Using the outputs from Part 1, establish RPO, RTO, and MTPD for each of the five systems. Present your results in a table with the following columns:

- **System**

- **RPO (with justification)**

- **RTO (with justification)**

- **MTPD (with justification)**

- **Recovery Safety Margin (MTPD minus RTO)**

Justifications must reference your BIA findings. Simply stating a number without justification will not receive full credit.

**Deliverable 4:** RPO/RTO/MTPD table with justifications. (20 points)

### Task 2.2 — Gap Analysis

The hospital currently performs nightly backups at 11:00 PM. The most recent ransomware incident occurred at 3:00 PM, meaning approximately sixteen hours of transactions were potentially affected.

Identify the gap between the current backup practice and the RPOs you established in Task 2.1 for each system. For systems where a gap exists, propose a specific technical control or architectural change to close the gap and explain how your proposed change meets the RPO target.

**Deliverable 5:** Gap analysis narrative, minimum 200 words. (10 points)

---

## Part 3: Continuity Strategy Selection

### Task 3.1 — Strategy Recommendation

For each of the five systems, recommend a continuity strategy from the following options:

- High Availability / Redundant Systems

- Hot Alternate Site

- Warm Alternate Site

- Cold Alternate Site

- Manual Workaround

- Cloud-Based Backup and Restore

- Cloud Warm Standby

Your recommendation must be consistent with the RTO you established in Task 2.1. A system with a two-hour RTO cannot be assigned a cold site strategy (which typically requires 24–72 hours to activate).

For each recommendation, provide a one-paragraph justification that addresses:

1. Why the recommended strategy meets the RTO.

2. Estimated relative cost tier (low / medium / high / very high).

3. Any significant limitations or risks of the strategy.

**Deliverable 6:** Strategy recommendation and justification for each system (five paragraphs). (25 points)

---

## Part 4: BCP Document Outline

### Task 4.1 — Produce a Structured BCP Outline

Using the eight-section BCP structure from the Module 13 Reading Guide, produce a structured outline for Meridian Regional Hospital's BCP. The outline does not need to contain full procedure text, but each section must include:

- The section title.

- A two- to four-sentence description of what that section will contain for this organization.

- For Section 2 (Roles and Responsibilities): name at least five specific hospital roles and their BCP responsibilities.

- For Section 3 (Activation Criteria): define at least two specific events that would trigger BCP activation for this organization.

- For Section 4 (Communication Procedures): identify at least three stakeholder groups and the communication method for each.

**Deliverable 7:** Eight-section BCP outline. (20 points)

---

## Part 5: Testing Plan

### Task 5.1 — Recommend a Testing Schedule

Design a twelve-month BCP testing schedule for Meridian Regional Hospital. Include at least one tabletop exercise, one simulation exercise, and describe the conditions under which a full-interruption test would be appropriate and when the hospital should consider conducting one.

For each scheduled exercise, specify:

- Exercise type (tabletop / simulation / full interruption).

- Target month.

- Scope (which systems and/or processes are included).

- Estimated duration.

- Key participants.

- Primary objective.

**Deliverable 8:** Twelve-month testing schedule table and full-interruption test recommendation narrative. (15 points)

---

## Submission Requirements

1. Compile all eight deliverables into a single document.

2. Include your name, course number, and module number in the document header.

3. Label each deliverable clearly (Deliverable 1, Deliverable 2, etc.).

4. Minimum total length: 1,200 words of analytical content (tables and headers do not count toward word count).

5. Submit as PDF or DOCX through the Canvas assignment portal.

---

## Grading Rubric Summary

| Deliverable | Points | Key Criteria |
|---|---|---|
| 1 — Classification Table | 15 | Completeness, reasoning quality |
| 2 — Dependency Map | 20 | Accuracy, SPOF identification |
| 3 — Impact Timeline | 20 | Realistic estimates, severity logic |
| 4 — RPO/RTO/MTPD Table | 20 | BIA-grounded justifications |
| 5 — Gap Analysis | 10 | Identifies gap, proposes specific fix |
| 6 — Strategy Recommendations | 25 | RTO consistency, cost awareness, risk |
| 7 — BCP Document Outline | 20 | Completeness, specificity to scenario |
| 8 — Testing Schedule | 15 | All three types, realistic schedule |
| **Total** | **145** | |

---

## Troubleshooting and Common Errors

**Common error — RPO/RTO confusion:** RPO looks backward (data age); RTO looks forward (recovery time). If you are assigning an RPO to describe recovery time, re-read Section 3 of the Reading Guide before proceeding.

**Common error — MTPD less than RTO:** MTPD must always be greater than or equal to RTO. If your table shows an MTPD shorter than the RTO, the logic is inverted. Revisit your impact timeline to recalibrate.

**Common error — Strategy misalignment:** If you assign a cold site to a system with a two-hour RTO, the strategy cannot achieve the objective. Verify that every strategy recommendation is technically capable of meeting its associated RTO.

---

## Part 9 — Challenge Exercise

### Challenge 1: BIA Sensitivity Analysis — What If the RTO Changes?

The hospital's executive team is reviewing your BIA deliverables and proposes cutting the IT budget by 25%, which would require relaxing the EHR system's RTO from two hours to eight hours and eliminating the planned hot standby architecture in favor of a warm site.

1. Recalculate the financial impact of an eight-hour EHR outage using the revenue and regulatory penalty data from your original BIA (Part 1). Build a comparison table showing total impact at two hours, four hours, six hours, and eight hours of downtime. Include direct revenue loss, estimated regulatory penalty exposure, and an estimated reputational impact category (Low / Moderate / High / Severe).
2. Evaluate whether a warm site architecture is technically capable of achieving an eight-hour RTO for the EHR system. Reference specific warm site characteristics — activation time, data currency, staffing requirements — and identify at least two assumptions the organization must validate before finalizing this strategy change.
3. Draft a one-page executive briefing (150–200 words) addressed to the CFO explaining the risk trade-off of relaxing the EHR RTO from two hours to eight hours. Use business language — do not cite technical specifications. Conclude with a clear recommendation.
4. Identify one compensating control the organization could implement to reduce financial exposure during the extended eight-hour recovery window (for example: manual paper-based workflows, pre-negotiated mutual aid with a neighboring hospital, or temporary contracted EHR support). Describe the control, its limitations, and its cost relative to the hot standby alternative.

### Challenge 2: BCP Maintenance Trigger Analysis

Six months after the BCP is finalized and approved, the following five changes occur at Meridian Regional Hospital. For each change, determine whether it constitutes an immediate BCP review trigger, a scheduled review item, or no review action required.

1. The hospital signs a contract with a new cloud-based telehealth platform that will host patient visit records for approximately 12,000 patients per year. The platform operates under a shared-responsibility model for data availability.
2. The IT Director named as the BCP Recovery Coordinator accepts a position at another hospital and gives two weeks' notice.
3. The hospital replaces its aging network switches with new hardware from a different vendor, upgrading from 1 Gbps to 10 Gbps backbone capacity.
4. A regional tornado causes the hospital to activate its emergency management plan for the first time, but the data center (in the basement) sustains no damage and systems remain online throughout.
5. The federal government issues a new HIPAA Security Rule amendment requiring that covered entities document recovery time objectives for all electronic PHI systems and test those objectives annually.

For each of the five items: state your trigger classification, provide a one-paragraph justification, and describe the specific BCP section or sections that would require review or update.

### Reflection Questions

1. A security manager argues that the BIA is a one-time exercise that should be conducted when the BCP is first created, and that subsequent updates are unnecessary unless a major incident occurs. Using specific BIA methodology concepts from this module, explain why this position is incorrect and describe two organizational changes that would require BIA reassessment even without a triggering incident.
2. An organization's RTO for its payment processing system is four hours, but the most cost-effective recovery architecture available achieves a six-hour recovery. Management asks the security manager to simply revise the RTO to six hours to match available resources. Explain why revising the RTO to match technical capability rather than business impact is a governance failure, and describe the correct process for making an informed risk acceptance decision in this situation.
