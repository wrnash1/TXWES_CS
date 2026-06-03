# Lab Activity: Module 12 — Release and Deployment Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Scenario: Crestview Financial Services

Crestview Financial Services (CFS) is a regional bank with 340 branch locations and approximately 4,200 internal staff. The IT department is preparing to release version 3.1 of the Crestview Online Banking Platform — a customer-facing web application used by 180,000 active customers. The release includes three components:

- A redesigned account dashboard (new feature — high visibility)
- A security patch addressing a session-management vulnerability (critical)
- A database schema change adding two new audit-logging columns to the transactions table

The release is scheduled for a Saturday night maintenance window. The IT Director has asked you — acting as Release Manager — to complete the following four exercises before the deployment proceeds.

---

## Exercise 1: Deployment Approach Selection (25 points)

CFS leadership is debating which deployment approach to use for the 3.1 release. Three options are on the table.

**Option A:** Deploy the full release to all 180,000 customers simultaneously Saturday night.

**Option B:** Deploy to 2% of customers first, monitor for 48 hours, then expand to 25%, then 100%.

**Option C:** Build a parallel production environment with the 3.1 release, route all traffic to it via load balancer switch, maintain the 3.0 environment on standby for instant rollback.

### Task 1a: Identify each option

For each option, write the ITIL 4 deployment approach name and a one-sentence definition.

- Option A: _______________ — _______________
- Option B: _______________ — _______________
- Option C: _______________ — _______________

### Task 1b: Recommend and justify

Given the following constraints — a customer-facing banking application, a database schema change that is difficult to reverse, and a critical security patch that cannot be delayed — write a 150–200 word recommendation identifying which approach you would select. Address:

- Why your chosen approach fits the risk profile of this release
- What the primary risk of your chosen approach is and how you would mitigate it
- Why you rejected the other two approaches

---

## Exercise 2: Release Notes Draft (25 points)

Draft release notes for the Crestview Online Banking Platform version 3.1 release. Your release notes must be complete enough to serve all three audiences: end users (customers), operations staff, and the change record.

Use the structure below. Each section must be substantively completed — not left blank or described only in abstract terms.

### CFS Online Banking Platform — Release Notes v3.1

**Release version:** 3.1
**Release date:** _______________
**Deployment window:** Saturday 10:00 PM — Sunday 2:00 AM CT

**Summary of changes:**

- (List each of the three components with a one-sentence description suitable for the end-user audience)

**Known issues and limitations:**

- (Describe at least one realistic limitation for this type of release)

**Dependencies and prerequisites:**

- (List at least two realistic prerequisites that operations staff must verify before deployment begins)

**Post-deployment verification steps:**

- (List at least four steps operations staff should take to confirm the deployment succeeded)

**Rollback instructions:**

- (Write the rollback procedure for your chosen deployment approach from Exercise 1)

**Support contact during deployment window:**

- (Provide a realistic escalation path)

---

## Exercise 3: Database Schema Rollback Analysis (25 points)

The transactions table schema change — adding two audit-logging columns — is the most complex rollback scenario in this release.

### Task 3a: Rollback scenario

The deployment completed at 11:45 PM Saturday. At 12:30 AM Sunday, the monitoring system reports that 3.4% of transaction submissions are returning a 500 error. The on-call engineer suspects the schema change may have introduced a conflict with the existing transaction processing stored procedure.

Describe the rollback steps for the database schema change. Your description must address:

1. What information the on-call engineer needs to confirm the schema change is the cause (not application code or another factor)
2. Why adding columns is generally safer to roll back than deleting columns
3. The specific data-integrity risk if transactions were written to the new audit columns during the 45-minute window and the columns are now dropped

**Response (150–200 words):**

### Task 3b: Forward-only migration alternative

Some organizations use a "forward-only migration" philosophy for database changes — they design schema changes so they never need to be reversed. Describe one technique that allows the application to be rolled back to v3.0 even if the database schema change is not reversed.

**Response (75–100 words):**

---

## Exercise 4: Post-Implementation Review (25 points)

Two weeks after the 3.1 release, you are conducting the post-implementation review. The following events occurred during and after the deployment:

- The deployment itself completed on schedule and within the maintenance window
- Three customers reported being unable to log in for approximately 18 minutes after the traffic switch; this was caused by a session-cache warm-up delay that was not in the deployment plan
- The release notes did not include the session-cache warm-up step, so the on-call engineer took 11 minutes to diagnose it
- No other incidents were reported
- Customer satisfaction scores for the new dashboard are significantly above baseline

Complete the PIR template below.

### PIR Template: CFS Online Banking Platform v3.1

**Release:** CFS Online Banking Platform v3.1
**Deployment date:** _______________
**PIR date:** _______________
**PIR facilitator:** _______________

**Did the release achieve its intended outcomes?**

(Assess each of the three components against its stated goal)

**Incidents caused by or associated with the release:**

| Incident | Description | Duration | Root Cause |
|---|---|---|---|
| INC-001 | | | |

**Deployment plan accuracy:**

(Was the deployment plan complete and accurate? What was missing?)

**Release notes quality:**

(Were the release notes complete and useful for the audience that needed them?)

**Rollback plan viability:**

(Was the rollback plan tested before deployment? Was it viable?)

**Lessons learned (at least three):**

1. Lesson: _______________
2. Lesson: _______________
3. Lesson: _______________

**Recommended improvements for future releases:**

(Write at least two specific, actionable recommendations that will be added to the Continual Improvement Register)

---

## Submission

Submit your completed lab document to the Canvas assignment portal by the due date shown in the course schedule. Your document should include all four exercises with substantive responses — not template placeholders. Screenshots or supplemental diagrams may be included but are not required.

**Grading:** Each exercise is worth 25 points. Within each exercise, points are allocated based on completeness, accuracy of ITIL 4 terminology, and quality of reasoning.
