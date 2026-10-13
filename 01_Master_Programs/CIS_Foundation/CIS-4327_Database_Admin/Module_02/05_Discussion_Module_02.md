# Discussion Forum: Module 02 — Database Design: Normalization and ERDs

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

---

### Overview

This discussion connects normalization theory and ERD design to real-world schema decisions. Read all three scenarios, then post your initial response to the one that most closely matches your professional background or academic focus. You must reply to at least two classmates from any scenario.

---

### Scenario A — Healthcare Records Flat Table Migration

A regional hospital is migrating a legacy Microsoft Access database to Cloud SQL for PostgreSQL. The Access database stores all patient data in a single flat table with 47 columns, including patient demographics, insurance details, physician information, and visit records all in one row. The DBA estimates there are roughly 800,000 rows and 23 distinct transitive dependencies.

For your initial post, address all of the following.

Explain why a flat-table design with 23 transitive dependencies creates specific risks during a cloud migration — not just in the target Cloud SQL schema, but during the migration process itself. Identify the type of normalization violation that accounts for most of these dependencies (1NF, 2NF, or 3NF) and explain your reasoning. Describe the first two tables you would extract from the flat table during normalization, including what functional dependency drives each extraction. Identify one data quality check you would run before the migration to assess the severity of existing update anomalies. Your post should be 175–225 words using precise normalization terminology.

---

### Scenario B — E-Commerce Analytics vs. Transactional Schema

A growing e-commerce company currently runs all operations on a normalized Cloud SQL for MySQL database. The data warehouse team wants to copy the same schema directly into BigQuery to run analytics queries. A junior data engineer argues that because the schema is already "good" (normalized to 3NF), it should work well in BigQuery without modification. The senior engineer disagrees and recommends denormalizing the data before loading it into BigQuery.

For your initial post, address all of the following.

Explain why a 3NF normalized schema that performs well in Cloud SQL may perform poorly in BigQuery for analytical queries. Reference at least one specific characteristic of BigQuery's storage architecture that makes denormalization advantageous. Describe what a denormalized version of a typical order analytics table might look like compared to the normalized 3NF version — you do not need to write SQL, but describe the structural difference. Identify one trade-off of denormalization in BigQuery that could create data consistency problems and explain how it is typically managed. Your post should be 175–225 words using correct terminology from Module 02.

---

### Scenario C — University Course Registration System Redesign

A university IT department is redesigning its course registration system from scratch. The current system stores all registration data in three tables: one master table with student, course, instructor, and room details all combined, one grades table, and one billing table. Students frequently complain that their registered courses disappear from their profile when a course is cancelled — apparently because deletion of a course record also deletes the student's enrollment record.

For your initial post, address all of the following.

Identify the specific deletion anomaly described in the scenario and trace it to the design flaw that causes it. Explain what foreign key ON DELETE behavior was most likely configured (or absent) that allowed this to happen. Design a minimal four-table normalized schema that eliminates this problem — list the tables by name, their primary keys, and the foreign key relationships. Explain what ON DELETE behavior you would specify for each foreign key in your schema and why. Your post should be 175–225 words using correct terminology from Module 02.

---

### Peer Response Guidelines

Reply to at least two classmates across any scenario. Each reply must be at least 50 words and add technical value — a refinement to their schema, a counter-example, a trade-off they did not consider, or a specific follow-up question. Replies that restate agreement without adding substance do not meet the requirement.

---

### Discussion Rubric — 10 Points Total

Initial post — 6 points.

- 5 to 6 points: Addresses all required prompt elements with technical accuracy, correct normalization terminology, and clear reasoning. Meets the 175–225 word count.
- 3 to 4 points: Addresses most elements but omits one required item or lacks technical precision.
- 0 to 2 points: Initial post is missing, substantially incomplete, or contains significant conceptual errors.

Peer responses — 4 points.

- 4 points: Two substantive replies of at least 50 words each that add technical content to the discussion.
- 2 points: Only one qualifying reply, or both replies are superficial.
- 0 points: No peer responses submitted by the deadline.

---

### Due Dates

Initial post: Wednesday at 11:59 PM

Peer responses: Sunday at 11:59 PM

Professor Nash reads every post. Posts that demonstrate careful application of the normalization rules from the reading guide will be recognized in class.

---

Reference: cloud.google.com/learn
