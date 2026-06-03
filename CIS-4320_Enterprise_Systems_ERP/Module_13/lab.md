# Lab: Module 13 — ERP Security and Access Control

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

**Title:** Salesforce Security Configuration and SoD Analysis

**Estimated Time:** 90–120 minutes

**Format:** Individual work with written deliverables

**Tools Required:** Salesforce Developer Edition org (free at developer.salesforce.com), web browser, word processor

**Submission:** Upload completed lab report (PDF or DOCX) to the LMS by the module due date.

---

## Learning Objectives

By completing this lab you will be able to:

- Configure Salesforce profiles and permission sets for a given access control scenario
- Identify and apply organization-wide default settings
- Analyze a set of user access assignments for SoD conflicts
- Document an audit trail review and explain what it reveals

---

## Lab Background

Pinnacle Financial Services is a regional investment advisory firm using Salesforce Financial Services Cloud. They are preparing for an annual SOX compliance audit. The compliance team has asked you — as the Salesforce Administrator — to review and remediate the access control configuration and document the findings.

Pinnacle has the following roles (Salesforce role hierarchy):

- VP Operations (top)
  - Regional Director — East
    - Account Manager — East A
    - Account Manager — East B
  - Regional Director — West
    - Account Manager — West A
    - Account Manager — West B

All Account Managers work with Opportunity, Account, and Contact records. Regional Directors review their team's pipeline. VPs need read-only access to all records.

---

## Part 1: Profile and Permission Set Design (35 points)

### Task 1.1: Define the Access Requirements

Review the business requirements below and complete the access matrix table. For each role, fill in the appropriate CRUD permissions (C = Create, R = Read, U = Update, D = Delete, blank = no access) for each object.

**Business Requirements:**

- Account Managers should be able to create and manage their own Opportunities, Accounts, and Contacts. They should NOT be able to delete Contacts.
- Regional Directors should be able to view all team records and edit Opportunities but not create new Accounts.
- VPs should have read-only access to all objects; they should not create, edit, or delete any records.
- Only the System Administrator should have full CRUD on all objects.

**Access Matrix — Complete this table:**

| Role | Opportunity | Account | Contact | Task | Event |
|------|-------------|---------|---------|------|-------|
| System Admin | CRUD | CRUD | CRUD | CRUD | CRUD |
| VP Operations | | | | | |
| Regional Director | | | | | |
| Account Manager | | | | | |

For each cell, write the applicable permission letters (e.g., "CRU" or "R" or "CRUD").

---

### Task 1.2: Profile Configuration in Salesforce

Log in to your Salesforce Developer Edition org.

Navigate to Setup > Profiles. You will create a new custom profile for Account Managers.

1. Click "New Profile." Base it on the "Standard User" profile. Name it "Account Manager — Pinnacle."

2. After creation, locate the Object Settings for Opportunity. Adjust the permissions to match your matrix from Task 1.1 for the Account Manager role. Screenshot the Opportunity object permissions page showing your settings.

3. Locate the Object Settings for Contact. Remove the Delete permission. Screenshot the Contact object permissions page.

4. Save the profile.

**Documentation required:** Two screenshots (or written descriptions) of the permission settings plus a brief explanation of why you made each change.

---

### Task 1.3: Create a Permission Set for Deal Desk Access

Pinnacle has a small "Deal Desk" team of two Account Managers who are authorized to approve discounts over 15%. This capability should be additive on top of the standard Account Manager profile.

1. Navigate to Setup > Permission Sets. Click "New."

2. Create a permission set with:
   - Label: `Deal_Desk_Approver`
   - API Name: (auto-populated)
   - License: Salesforce

3. In the permission set, navigate to System Permissions. Enable "Run Flows" (this represents the ability to trigger an approval flow process).

4. Do NOT add any object-level permissions — those are already handled by the profile.

5. Screenshot the completed permission set showing the enabled system permission.

**Reflection question (3–5 sentences):** Why is it better to implement Deal Desk access as a permission set rather than creating a separate profile? What happens to the two Deal Desk users' access if the base profile is updated?

---

## Part 2: Organization-Wide Defaults and Sharing (30 points)

### Task 2.1: Set Appropriate OWD Settings

Navigate to Setup > Sharing Settings. Review the default Organization-Wide Default settings.

For each object, determine the correct OWD setting based on the Pinnacle requirements and explain your reasoning:

| Object | Required OWD Setting | Reasoning (1–2 sentences) |
|--------|---------------------|--------------------------|
| Opportunity | | |
| Account | | |
| Contact | | |
| Lead | | |
| Case | | |

Note: You do not need to change the settings in your Developer Edition org (that could affect other lab exercises). Simply document your recommendations.

---

### Task 2.2: Design a Sharing Rule

Pinnacle's compliance team (a Salesforce public group) needs to be able to view all Opportunity records across all regional teams for audit purposes. Account Managers own their own Opportunities; OWD for Opportunity is set to Private.

Design a sharing rule to solve this requirement:

1. What type of sharing rule would you use — owner-based or criteria-based?

2. Write out the sharing rule definition:
   - Rule Name: (your choice)
   - Share with whom: (specify the group or role)
   - Access Level: (Read Only or Read/Write — justify your choice)
   - Scope: (which records should be shared)

3. Why can this requirement NOT be solved by the role hierarchy alone?

---

### Task 2.3: OWD Impact Analysis

A new administrator suggests setting all objects to "Public Read/Write" to eliminate sharing complexity.

Write a 150–200 word analysis explaining:

- What security risk this creates for Pinnacle, a financial services firm
- How it affects the principle of least privilege
- What regulatory implications it might have
- What the correct approach is

---

## Part 3: SoD Conflict Analysis (20 points)

### Task 3.1: Identify the SoD Conflicts

Review the access assignments for five Pinnacle users below. Identify any SoD conflicts and explain why each is problematic.

**User Access Assignments:**

| User | Profile | Permission Sets Assigned |
|------|---------|--------------------------|
| Sarah Chen | Account Manager — Pinnacle | Deal_Desk_Approver, Contract_Creator, Contract_Approver |
| Marcus Webb | Account Manager — Pinnacle | Deal_Desk_Approver |
| Diana Torres | Account Manager — Pinnacle | Contract_Creator |
| James Park | Regional Director (custom profile) | Override_Discount, Deal_Desk_Approver |
| Priya Nair | System Administrator | (none) |

**SoD Conflict Definitions for Pinnacle:**

- A user with both `Contract_Creator` and `Contract_Approver` can create and approve their own contracts — this is a high-risk SoD conflict.
- A user with both `Override_Discount` and `Deal_Desk_Approver` can both override a discount and approve it — this is a high-risk SoD conflict.
- A System Administrator having any operational permission sets is a medium-risk concern.

For each user, fill in:

| User | SoD Conflict? (Yes/No) | Conflict Description | Risk Level | Recommended Remediation |
|------|----------------------|---------------------|------------|--------------------------|
| Sarah Chen | | | | |
| Marcus Webb | | | | |
| Diana Torres | | | | |
| James Park | | | | |
| Priya Nair | | | | |

---

### Task 3.2: Design a Compensating Control

For the conflict identified for Sarah Chen, a business stakeholder says she legitimately needs both Contract_Creator and Contract_Approver because she is the only person who handles contracts for a key client during a colleague's leave.

Design a compensating control:

1. Describe the compensating control in 3–5 sentences.

2. What audit evidence would the compliance team require to accept this compensating control?

3. Is this a permanent or temporary solution? What process should be followed when the colleague returns?

---

## Part 4: Audit Trail Review (15 points)

### Task 4.1: Review the Setup Audit Trail

In your Salesforce Developer Edition org, navigate to Setup > Security > View Setup Audit Trail.

1. How many entries are visible? What is the date range shown?

2. Identify three types of configuration changes shown in the audit trail. For each, note:
   - What was changed
   - Who made the change
   - When the change occurred

3. What field in the audit trail would help you confirm that a specific administrator — and not someone using their credentials — made a sensitive configuration change?

---

### Task 4.2: Enable Field History Tracking

Navigate to the Opportunity object in Setup > Object Manager > Opportunity > Fields & Relationships. Locate the "Set History Tracking" button.

Enable field history tracking for the following fields:

- Stage
- Amount
- Close Date
- Probability

Screenshot the Field History Tracking configuration showing these four fields enabled.

Answer these questions:

1. Where can a user see the field history for a specific Opportunity record? What is the component called?

2. How long does Salesforce retain field history data by default?

3. A Pinnacle compliance officer asks whether field history data can serve as legal evidence that a specific user changed an Opportunity Stage. What are the limitations of relying on field history for this purpose?

---

## Submission Checklist

Before submitting, verify:

- Part 1: Access matrix completed; profile screenshots or descriptions included; permission set created and documented; reflection question answered
- Part 2: OWD recommendations with reasoning; sharing rule designed; OWD impact analysis written
- Part 3: SoD conflict table completed; compensating control designed
- Part 4: Audit trail observations documented; field history tracking enabled and screenshotted
- Document has your name, student ID, and date on the cover page

---

## Grading Rubric

| Section | Points | Criteria |
|---------|--------|----------|
| Part 1 — Access matrix and profile configuration | 20 | Matrix is logically correct; profile changes match requirements; screenshots included |
| Part 1 — Permission set design and reflection | 15 | Permission set correctly created; reflection demonstrates understanding of profile vs. permission set design |
| Part 2 — OWD recommendations and analysis | 30 | OWD settings are appropriate for a financial services firm; sharing rule is correctly designed; impact analysis addresses all four required points |
| Part 3 — SoD conflict identification and remediation | 20 | All conflicts correctly identified; risk levels appropriate; compensating control is realistic and includes audit evidence requirement |
| Part 4 — Audit trail and field history | 15 | Observations are accurate; field history enabled correctly; limitations question answered with specificity |
| **Total** | **100** | |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
