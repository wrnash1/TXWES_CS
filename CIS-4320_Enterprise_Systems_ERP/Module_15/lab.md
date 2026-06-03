# Lab: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

**Title:** Implementation Planning and Change Management Design

**Estimated Time:** 90–120 minutes

**Format:** Individual work; written deliverables with planning documents

**Tools Required:** Word processor or Google Docs, spreadsheet tool (Excel or Google Sheets)

**Submission:** Upload completed lab report (PDF or DOCX) to the LMS by the module due date.

---

## Learning Objectives

By completing this lab you will be able to:

- Map a business scenario to the appropriate ASAP phase activities
- Design a simplified cutover plan for a Salesforce go-live
- Develop a change management stakeholder analysis
- Calculate a simplified five-year TCO model for a Salesforce implementation

---

## Lab Background

Crestwood Medical Group is a network of 12 urgent care clinics in the Dallas-Fort Worth area. They currently manage patient referrals, physician relationships, and marketing activities in a combination of spreadsheets and a 10-year-old contact management software that is no longer supported by its vendor.

Crestwood has decided to implement Salesforce Health Cloud for CRM and Salesforce Service Cloud for patient case management. The implementation involves approximately 85 users: 30 front desk staff, 20 medical schedulers, 15 clinic managers, 10 marketing staff, and 10 executives.

The project will go live in eight months. The implementation partner has assigned a project manager and two Salesforce consultants. Crestwood's internal IT team consists of one systems administrator.

---

## Part 1: ASAP Phase Mapping (25 points)

### Task 1.1: Phase Activity Assignment

The Crestwood project team has generated a list of activities that need to occur during the implementation. Your task is to assign each activity to the correct ASAP phase and provide a one-sentence justification for the assignment.

Note: While Crestwood is implementing Salesforce (not SAP), the ASAP phase structure provides a useful general framework for any ERP implementation.

**Activity List:**

1. Draft the project charter defining scope, budget, timeline, and executive sponsor

2. Conduct workshops with clinic managers to document current patient referral workflows and design the to-be Salesforce process

3. Configure the Salesforce Account, Contact, and Case objects based on the approved solution design document

4. Create 85 user accounts in Salesforce production with correct profiles and permission sets

5. Load 10 years of contact data from the old system into Salesforce using Data Loader

6. Conduct role-specific Salesforce training for front desk staff and schedulers

7. Decide which of the three Salesforce sandbox types will be used for UAT

8. Execute integration testing between Salesforce and the clinic's electronic health record (EHR) system

9. Hold the formal Go/No-Go meeting with Crestwood's VP of Operations

10. Establish the hypercare war room and triage process for the first two weeks after go-live

**Deliverable:** Complete the table below for each activity:

| Activity | ASAP Phase | Justification (one sentence) |
|----------|------------|------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |

---

### Task 1.2: Phase 2 Business Blueprint Question Design

You are facilitating the Business Blueprint workshop for Crestwood's patient referral process.

Write ten questions you would ask in the workshop to document the business requirements. Questions should be specific to Crestwood's scenario (clinic-based healthcare, referral management) and should address the types of information needed to configure Salesforce.

Format each question as:

- **Question:** [your question]
- **Why it matters:** [one sentence explaining what Salesforce configuration decision this question informs]

---

## Part 2: Cutover Planning (30 points)

### Task 2.1: Build a Cutover Plan

Crestwood will go live on a Saturday morning at 7:00 AM. The old contact management software will be shut down Friday at 5:00 PM, giving a 14-hour cutover window (5 PM Friday to 7 AM Saturday).

Build a cutover plan as a table. Include at least 15 tasks. For each task include:

- Task ID (sequential number)
- Task description
- Owner (use job titles: Project Manager, IT Admin, Salesforce Consultant, Data Migration Lead, etc.)
- Estimated Duration (in hours)
- Dependency (what task ID must be completed first)
- Status column (leave blank — this would be filled in during execution)

Ensure the plan covers: shutting down the old system, final data extraction, data transformation and load, user account activation, system validation testing, rollback decision point, stakeholder notification, go-live confirmation.

---

### Task 2.2: Define the Rollback Criteria

Write a rollback criteria statement for the Crestwood go-live. Your statement should:

1. Define the rollback decision point (what time and what conditions)

2. List three specific conditions that would trigger a rollback (e.g., "Data migration completion rate is below 95% by 3:00 AM")

3. Describe the rollback procedure in 5–7 steps

4. Explain why rollback becomes impractical after the 7:00 AM go-live announcement has been made

---

### Task 2.3: Hypercare Plan

Design a 14-day hypercare plan for Crestwood. Your plan should include:

1. **War room structure:** how will the support team be organized? What communication channel will be used?

2. **Issue severity levels:** define three severity levels (Critical, High, Low) with examples from the Crestwood scenario and target resolution times for each.

3. **Daily standup agenda:** list the five items that should be covered in the daily hypercare team meeting (maximum 30 minutes).

4. **Hypercare exit criteria:** what conditions must be true for the project to transition from hypercare to steady-state support? List at least four specific, measurable criteria.

---

## Part 3: Change Management Plan (25 points)

### Task 3.1: Stakeholder Analysis

Conduct a stakeholder analysis for the Crestwood implementation. Analyze each stakeholder group using the two-by-two impact/support matrix.

For each stakeholder group, assess:

- Level of impact (High / Medium / Low)
- Current level of support for the implementation (Supportive / Neutral / Resistant)
- Recommended engagement strategy (1–2 sentences)

**Stakeholder groups:**

1. Front desk staff (30 users) — daily users of the current system, worried about learning a new tool
2. Medical schedulers (20 users) — rely heavily on the referral tracking features of the old system
3. Clinic managers (15 users) — want better visibility into referral metrics but concerned about disruption
4. Marketing staff (10 users) — excited about Salesforce Marketing Cloud potential
5. Executives and VP of Operations — financially committed but largely hands-off since project kick-off
6. IT system administrator — the only internal technical resource; responsible for ongoing system support

---

### Task 3.2: Apply the ADKAR Model

The Crestwood IT Administrator recently overheard a group of front desk staff saying: "We went to the training. The new system looks really different, and honestly we're not sure we can use it during a busy check-in rush."

Using the ADKAR model, diagnose this situation:

1. Which ADKAR stage is most clearly the barrier based on this statement?

2. What evidence from the statement supports your diagnosis?

3. What three specific interventions would you implement before go-live to address this barrier?

4. If the front desk staff's concern is not addressed before go-live, what outcome would you predict for the first week of operations?

---

### Task 3.3: Communication Plan Excerpt

Design a communication plan for the two weeks immediately before go-live. Create a table with:

- Communication #: sequential number
- Target audience: who receives this communication
- Message content: what is being communicated (2–3 sentences)
- Sender: who sends it (job title and why this person has credibility with the audience)
- Channel: email, town hall, team meeting, poster, etc.
- Timing: days before go-live

Include at least six communications covering all stakeholder groups.

---

## Part 4: Total Cost of Ownership Model (20 points)

### Task 4.1: Build the TCO Model

Build a simplified five-year TCO model for the Crestwood Salesforce implementation. Use the following cost inputs:

**Year 1 Costs:**

- Salesforce Health Cloud licenses: $175/user/month × 85 users × 12 months
- Salesforce Service Cloud licenses: $150/user/month × 30 users × 12 months (front desk and schedulers only)
- Implementation consulting fees: $280,000 (fixed)
- Internal IT staff time (implementation): 40% of one year of IT Administrator salary at $85,000/year
- Training materials and delivery: $12,000

**Years 2–5 Annual Costs (per year):**

- Salesforce Health Cloud licenses (same as Year 1)
- Salesforce Service Cloud licenses (same as Year 1)
- Internal IT Admin (ongoing support): 25% of IT Administrator salary
- Annual enhancement consulting: $40,000 per year

Build a table showing:

| Cost Category | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
|---------------|--------|--------|--------|--------|--------|--------------|
| Health Cloud Licenses | | | | | | |
| Service Cloud Licenses | | | | | | |
| Implementation Consulting | | | | | | |
| Internal IT Staff | | | | | | |
| Training | | | | | | |
| Annual Enhancements | | | | | | |
| **Annual Total** | | | | | | |
| **Cumulative Total** | | | | | | |

**Analysis questions:**

1. What is the five-year TCO?

2. What percentage of the five-year TCO is ongoing annual cost (Year 2–5) versus Year 1 implementation cost?

3. If the current system costs $8,000/year in licensing and $20,000/year in IT support (no further development), what is the net five-year cost difference of implementing Salesforce?

4. Name two costs that are NOT included in your model but that a real TCO analysis should address.

---

## Submission Checklist

Before submitting, verify:

- Part 1: Phase mapping table completed; ten Blueprint questions written with explanations
- Part 2: Cutover plan table with 15+ tasks; rollback criteria defined; hypercare plan documented
- Part 3: Stakeholder analysis for all six groups; ADKAR diagnosis and interventions; communication plan with six entries
- Part 4: TCO spreadsheet with all cells calculated; four analysis questions answered
- Document has your name, student ID, and date on the cover page

---

## Grading Rubric

| Section | Points | Criteria |
|---------|--------|----------|
| Part 1 — Phase mapping | 15 | Correct phase assignments with logical justifications |
| Part 1 — Blueprint questions | 10 | Questions are scenario-specific, not generic; "why it matters" demonstrates configuration awareness |
| Part 2 — Cutover plan | 20 | 15+ tasks with all required fields; logical sequencing; rollback point identified |
| Part 2 — Rollback criteria and hypercare | 10 | Criteria are specific and measurable; hypercare exit criteria include measurable thresholds |
| Part 3 — Stakeholder analysis | 15 | All six groups analyzed; engagement strategies are concrete and appropriate |
| Part 3 — ADKAR and communications | 10 | Correct ADKAR barrier identified with evidence; interventions are actionable; communication plan covers all groups |
| Part 4 — TCO model | 20 | Calculations are correct; analysis questions answered with specific figures |
| **Total** | **100** | |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
