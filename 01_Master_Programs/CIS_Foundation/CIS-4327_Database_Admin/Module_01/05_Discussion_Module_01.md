# Discussion Forum: Module 01 — Relational Database Fundamentals and SQL Review

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

---

### Overview

This discussion connects Module 01 concepts — relational design, ACID properties, SQL constraints, and GCP database service selection — to real-world engineering decisions. Read all three scenarios below, then post your initial response to the one that most closely relates to your professional background, academic focus, or personal interest. You must respond to at least two classmates from any scenario.

---

### Scenario A — Retail Order Management System

A regional retail company runs its order management system on an on-premises MySQL database with 8 million customer records and 40 million order rows. The development team reports frequent complaints about order status inconsistencies: occasionally a customer's account shows a charge but no corresponding order appears in the order history. The lead developer suspects the application bypasses foreign key constraints when performing bulk order imports via CSV.

For your initial post, address all of the following.

Identify which ACID property is being violated when a charge is recorded without a corresponding order record. Explain why this is a data integrity problem rather than just a display bug. Describe the specific SQL constraint or combination of constraints that should be enforced to prevent this scenario at the database level. If you were advising this company on a migration to Google Cloud, explain whether Cloud SQL for MySQL or another GCP service would be appropriate, and identify one operational risk of the migration.

Your initial post should be 175–225 words. Use correct technical terminology from the module.

---

### Scenario B — Global Financial Transaction Platform

A fintech startup is building a payment processing platform that must handle 50,000 transactions per second across users in North America, Europe, and Asia. Each transaction involves debiting one account and crediting another. The CTO wants to evaluate Google Cloud database options. A junior engineer recommends using Firestore because it is serverless and scales automatically.

For your initial post, address all of the following.

Explain why Firestore is not appropriate for this workload by referencing specific ACID properties it does not fully provide. Identify which GCP database service you would recommend and justify the choice using at least two technical criteria from the module. Describe what the terms Atomicity and Isolation mean in the context of a financial debit-credit transaction, and explain what failure modes occur if either property is absent. Reference the correct GCP service documentation domain from cloud.google.com/learn.

Your initial post should be 175–225 words. Use correct technical terminology from the module.

---

### Scenario C — University Enrollment Database

A university IT department maintains a student enrollment database in PostgreSQL on a local server. The schema includes tables for students, courses, enrollments, and grades. A recent audit found that the grades table contains rows referencing student_id values that no longer exist in the students table — students were deleted without cascading the deletion or first removing their grade records. Additionally, several enrollment records have a NULL value in the course_id column, which should not be allowed.

For your initial post, address all of the following.

Identify the two specific constraint types that are missing or misconfigured and explain what each constraint would have prevented. Write the SQL constraint definition (not a full CREATE TABLE, just the constraint clause) that would fix each problem. Explain the difference between ON DELETE RESTRICT and ON DELETE CASCADE in the context of the students-grades relationship, and state which behavior is more appropriate for an academic records system and why. Describe one situation where using ON DELETE CASCADE could result in permanent, unrecoverable data loss in this schema.

Your initial post should be 175–225 words. Use correct technical terminology from the module.

---

### Peer Response Guidelines

After your initial post is submitted, read your classmates' posts across all three scenarios and write constructive replies to at least two peers. Each reply must be at least 50 words. A reply that only says "great post" or "I agree" does not meet the requirement.

Useful approaches for peer replies include the following.

- Point out a constraint option or GCP service trade-off the original poster did not consider.
- Provide a counter-example that challenges or refines their recommendation.
- Connect their scenario to something you observed in your own lab work for this module.
- Ask a specific follow-up question that extends the technical discussion.

---

### Discussion Rubric — 10 Points Total

Initial post — 6 points.

- 5 to 6 points: Addresses all required prompt elements with technical accuracy, correct terminology, and clear reasoning. Meets the 175–225 word count. Demonstrates understanding of both the SQL constraint mechanics and the GCP service decision.
- 3 to 4 points: Addresses most prompt elements but lacks technical precision, omits a required element, or falls outside the word count range.
- 0 to 2 points: Initial post is missing, substantially incomplete, or demonstrates significant misunderstanding of the module concepts.

Peer responses — 4 points.

- 4 points: Responds constructively to at least two peers. Each reply adds technical value — a new consideration, a refined recommendation, a counter-example, or a substantive follow-up question. Minimum 50 words per reply.
- 2 points: Responds to only one peer, or both replies are superficial and do not contribute technical content.
- 0 points: No peer responses submitted by the due date.

---

### Due Dates

Initial post: Wednesday at 11:59 PM

Peer responses: Sunday at 11:59 PM

Professor Nash reads every post in this forum. Posts that demonstrate careful reading of the module material and genuine engagement with classmates' reasoning will be recognized in class.

---

Reference: cloud.google.com/learn
