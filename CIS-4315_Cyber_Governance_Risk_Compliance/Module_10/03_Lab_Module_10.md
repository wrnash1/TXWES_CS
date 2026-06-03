# Lab Activity: Module 10 — Incident Management Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Lab Overview

**Lab Title**: Developing the Incident Response Plan for Crestview Regional Medical Center

**Estimated Time**: 90–120 minutes

**Format**: Individual assignment with written deliverables

**Submission**: Upload all deliverables as a single PDF or ZIP to the course LMS by the posted due date.

---

## Scenario Background

You have been engaged as a cybersecurity consultant for **Crestview Regional Medical Center**, a 340-bed nonprofit hospital serving a rural community in the southeastern United States. Crestview employs 1,400 staff, operates an electronic health record (EHR) system, processes approximately 85,000 patient records annually, and recently expanded with a telehealth platform serving an additional 22,000 patients.

Crestview's IT infrastructure includes:

- On-premises EHR system (Epic) hosted in an on-site data center.

- Microsoft 365 for email and collaboration.

- Two remote clinics connected via VPN.

- A vendor-managed telehealth platform (SaaS).

- Medical device network (IoT) isolated on a separate VLAN.

Crestview has **no existing Incident Response Plan**. The organization experienced two security incidents in the past 18 months: a phishing attack that compromised four email accounts (no patient data confirmed accessed) and a ransomware alert on a single administrative workstation (isolated by IT before spread). Neither incident was formally documented.

The Chief Medical Officer (CMO) and the Board of Trustees have authorized development of a formal IRP following a recent HIPAA risk assessment that cited the absence of an IR plan as a significant finding. You have been given 90 days to deliver a complete IRP framework.

---

## Task 1 — Incident Classification Framework (20 points)

Design a four-level severity classification framework tailored to Crestview Regional Medical Center's risk environment.

### Task 1 Instructions

Step 1: Define four severity levels (Critical, High, Medium, Low or Severity 1 through Severity 4).

Step 2: For each level, specify:

- A clear definition with at least three qualifying criteria specific to Crestview's environment.

- Maximum response initiation time (time from detection to response activation).

- Minimum escalation requirements (who must be notified).

- Examples of incident types that would fall in this category.

Step 3: Write a brief policy statement (3–4 sentences) explaining how the classification framework will be used operationally and who has the authority to upgrade or downgrade an incident's severity classification after initial assignment.

### Task 1 Deliverable

A severity classification table with all required columns completed, followed by the policy statement paragraph.

---

## Task 2 — Incident Response Team Design (25 points)

Design the Incident Response Team structure for Crestview Regional Medical Center.

### Task 2 Instructions

Step 1: Define a minimum of seven IRT roles appropriate for a 1,400-employee regional hospital. For each role, specify:

- Role title.

- Primary responsibilities during an incident (three to five bullet points).

- Reporting authority during an active incident (who does this role report to in incident command?).

- Qualification requirements (what knowledge, skills, or credentials should this person have?).

Step 2: Create a RACI matrix for the following six incident response activities. Assign R (Responsible), A (Accountable), C (Consulted), or I (Informed) for each role across each activity:

- Incident severity classification and declaration.

- System isolation decision for a production clinical system.

- Patient data breach determination.

- HIPAA breach notification preparation.

- Media and public statement approval.

- Post-incident root cause analysis.

Step 3: Identify which two IRT roles at Crestview present the greatest coverage risk (positions most likely to be unavailable during an incident) and describe how you would mitigate that risk.

### Task 2 Deliverable

IRT role definition table, completed RACI matrix, and a paragraph (four to six sentences) addressing coverage risk.

---

## Task 3 — Communication Plan Development (30 points)

Develop the communication plan component of Crestview's IRP, covering both internal and external communication obligations.

### Task 3 Instructions

**Part A — Internal Notification Chain**: Create a notification chain table for each severity level. For each level, specify who must be notified, by what method, and within what timeframe. Include a minimum of four notification targets per severity level for Critical and High incidents.

**Part B — External Notification Obligations**: Crestview is a HIPAA covered entity operating in a US state with a 45-day breach notification law. Identify all external parties that Crestview must or should notify following a confirmed patient data breach. For each external party, specify:

- Party name and type (regulator, customer, partner, law enforcement).

- Legal basis for notification (regulation or contract).

- Notification deadline.

- Required notification method or form.

**Part C — Pre-Drafted Templates**: Write two pre-drafted communication templates that Crestview should have ready before an incident occurs:

Template 1: A media holding statement for use in the first 24 hours after a breach becomes public. This statement should acknowledge the situation, commit to patient care, and avoid admitting liability.

Template 2: An internal all-staff communication to be sent by the CMO once a patient data breach is confirmed and regulatory notification has been submitted. This communication should inform staff of the situation without providing details that could create additional legal exposure.

Each template should be 75–125 words in length.

**Part D — Out-of-Band Communication Plan**: Crestview's 2019 ransomware incident encrypted several file servers. Describe a realistic out-of-band communication plan for the IR team in the event that Microsoft 365 email and internal VoIP are compromised. Your plan should be specific to Crestview's environment and size.

### Task 3 Deliverable

Internal notification chain table, external notification obligations table, two pre-drafted templates, and a paragraph (four to six sentences) describing the out-of-band communication plan.

---

## Task 4 — Escalation Procedures (25 points)

Design criteria-based escalation procedures for Crestview Regional Medical Center.

### Task 4 Instructions

Step 1: Design a minimum of **ten specific escalation criteria** for Crestview. Each criterion must:

- State the specific, observable condition that triggers escalation.

- Identify who is notified when the condition is met.

- Specify the notification method and timeframe.

Use the following categories to ensure coverage: data-related triggers (at least three criteria), time-based triggers (at least two criteria), threat-based triggers (at least two criteria), regulatory triggers (at least two criteria), and operational triggers (at least one criterion).

Step 2: Create an escalation decision flowchart in text format (you do not need to create a graphic — describe the decision logic in a structured outline with indented conditions and outcomes).

Step 3: Write a brief policy statement (three to five sentences) explaining why escalation procedures must be criteria-based rather than left to the judgment of the on-call security analyst. Reference the CISM principle of management authorization and the human factors involved in high-stress incident response.

### Task 4 Deliverable

Escalation criteria table with all columns completed, text-format escalation flowchart, and the policy statement paragraph.

---

## Grading Rubric

| Deliverable | Points | Criteria |
|---|---|---|
| Task 1 — Classification Framework | 20 | Four levels with specific criteria; response times and escalation defined; examples relevant to a hospital environment; policy statement present |
| Task 2 — IRT Design | 25 | Seven or more roles defined with responsibilities; RACI matrix complete and logically consistent; coverage risk paragraph demonstrates practical reasoning |
| Task 3 — Communication Plan | 30 | Notification chain covers all severity levels; external obligations accurate for HIPAA-covered entity; templates are professional and legally appropriate; out-of-band plan is specific and realistic |
| Task 4 — Escalation Procedures | 25 | Ten or more criteria with specific triggers and notifications; flowchart logic is clear; policy statement references management authorization and human factors |
| **Total** | **100** | |

### Grading Notes

- Templates in Task 3 that admit liability, make unverified factual claims, or violate HIPAA minimum necessary standard will lose up to 10 points.

- RACI matrices with multiple Accountable (A) assignments for a single activity are logically incorrect and will lose 5 points per error. Each activity has exactly one A.

- Escalation criteria that use vague language such as "if the situation seems serious" rather than specific observable conditions will lose 2 points each.

---

## Submission Checklist

Before submitting, verify:

- [ ] Task 1 severity classification table has all four levels with criteria, response times, escalation requirements, and examples.

- [ ] Task 1 includes the operational policy statement paragraph.

- [ ] Task 2 IRT role table includes seven or more roles with all required fields.

- [ ] Task 2 RACI matrix covers all six activities across all IRT roles.

- [ ] Task 2 includes the coverage risk paragraph.

- [ ] Task 3 Part A internal notification chain covers all severity levels.

- [ ] Task 3 Part B external notification table is complete for all applicable parties.

- [ ] Task 3 Part C includes both pre-drafted templates at appropriate length.

- [ ] Task 3 Part D out-of-band communication plan paragraph is present.

- [ ] Task 4 includes ten or more escalation criteria with specific triggers and notifications.

- [ ] Task 4 includes the text-format escalation flowchart.

- [ ] Task 4 includes the policy statement paragraph.

- [ ] All deliverables compiled in a single PDF or ZIP file.

---

## Learning Connection

The IRP components you develop in this lab represent exactly what a CISM-certified professional is expected to be able to produce in a professional engagement. The severity classification framework, RACI matrix, and escalation criteria you design here are the same artifacts that security consultants deliver to healthcare organizations following HIPAA risk assessments.

When you sit for the CISM exam, questions in Domain 4 will present scenarios similar to Crestview's situation and ask you to identify the most appropriate action. Having built these artifacts from scratch in this lab, you will recognize the correct answer not through memorization but through genuine understanding of why each component exists and what would happen without it.

Keep your completed deliverables. With minor customization, they can serve as professional portfolio samples demonstrating competency in incident response planning.
