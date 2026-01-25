# CIS-4327: Database Fundamentals Labs

## Lab 1: Relational Data Modeling & SQL
**Objective**: Build a robust database schema and enforce data integrity.

1.  **Normalization**: Explain the requirements for 1st, 2nd, and 3rd Normal Form (3NF).
2.  **DDL**: Create a `Courses` table with a `CourseID` (PK), `CourseName`, and `Credits`.
3.  **Foreign Keys**: Create an `Enrollment` table that links `Students` and `Courses` using Foreign Keys.
4.  **Data Integrity**: Add a CHECK constraint to the `GPA` column in the `Students` table to ensure it is between 0.0 and 4.0.

## Lab 2: Advanced SQL & Data Analysis
**Objective**: Extract insights from relational data.

1.  **Subqueries**: Find all students who are enrolled in more than 3 courses.
2.  **Views**: Create a VIEW called `DeanList` that shows only students with a GPA > 3.8.
3.  **Indexes**: Create an index on the `LastName` column and explain how B-Trees improve query performance.

## Lab 3: Database Security & Optimization
**Objective**: Protect and tune the database for production.

1.  **RBAC**: Create a role `LabAssistant` and grant it only INSERT/UPDATE permissions on the `Students` table.
2.  **Execution Plans**: Use the `EXPLAIN` command on a query and identify the "Cost".
3.  **Log Shipping**: Explain the concept of Transaction Logs and why they are critical for Point-in-Time Recovery (PITR).

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
