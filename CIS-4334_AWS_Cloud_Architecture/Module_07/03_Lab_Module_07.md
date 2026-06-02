# Lab: Module 07 - DynamoDB: NoSQL at Scale

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab builds hands-on DynamoDB skills through three exercises: designing a DynamoDB table schema for a given access pattern scenario, working with DynamoDB using the AWS CLI, and analyzing a DynamoDB architecture for performance and scalability issues.

---

## Prerequisites

- AWS account with DynamoDB permissions (AmazonDynamoDBFullAccess or a scoped read-write policy)
- AWS CLI v2 installed and configured
- Completed Module 07 video and reading guide

---

## Part 1: Table Design and Schema Modeling (40 points)

### Design Scenario

An e-learning platform stores student progress data. The following access patterns must be supported efficiently:

1. Get all course progress records for a specific student
2. Get the progress record for a specific student in a specific course
3. Get all students enrolled in a specific course (regardless of student)
4. Get all students who completed a course on a specific date

The data for each record includes: StudentId, CourseId, EnrollmentDate, CompletionDate, ProgressPercent, and Score.

### Task 1.1 — Primary Key Design

Design the primary key for a DynamoDB table that supports access patterns 1 and 2 as efficient single-table queries. Specify:

- The partition key attribute and type
- The sort key attribute and type (if used)
- How access pattern 1 maps to a DynamoDB query operation
- How access pattern 2 maps to a DynamoDB get-item or query operation

**Deliverable 1.1:** Primary key specification with explanation of how each access pattern maps to a DynamoDB operation using your key design.

### Task 1.2 — Secondary Index Design

Access patterns 3 and 4 cannot be served efficiently by the primary key from Task 1.1. Design a secondary index for each pattern. For each index, specify:

- Index type (GSI or LSI)
- Partition key and sort key for the index
- Why this index type (and not the other) is appropriate
- What attributes the index should project

**Deliverable 1.2:** Two secondary index specifications with justification for each index type choice.

### Task 1.3 — Create the Table with CLI

Create the DynamoDB table and one GSI using the AWS CLI. Write the complete create-table command with the attribute definitions, key schema, and GSI specification. Use on-demand billing mode. The table name should be `StudentProgress`.

**Deliverable 1.3:** Complete CLI create-table command. Paste the output if you run it, or explain what the output would show.

---

## Part 2: DynamoDB Operations with the CLI (35 points)

### Task 2.1 — Write Items

Write the AWS CLI commands to add the following two items to the StudentProgress table using the `put-item` operation.

Item 1 attributes:

- StudentId: STU001
- CourseId: AWS-201
- EnrollmentDate: 2024-09-01
- ProgressPercent: 85
- CompletionDate: 2024-11-15
- Score: 92

Item 2 attributes:

- StudentId: STU001
- CourseId: AWS-301
- EnrollmentDate: 2024-10-15
- ProgressPercent: 40

Note: Item 2 has no CompletionDate or Score — DynamoDB's schema-less design allows this.

**Deliverable 2.1:** Two complete `put-item` CLI commands with correct JSON attribute type syntax (S for string, N for number).

### Task 2.2 — Query by Partition Key

Write a CLI query command to retrieve all course progress records for student STU001. Use the `query` operation with a KeyConditionExpression.

**Deliverable 2.2:** Complete CLI query command. Explain what the output would contain and how it differs from using a `scan` operation.

### Task 2.3 — Conditional Write

Write a `put-item` command that adds a new progress record only if an item with the same StudentId and CourseId does not already exist. Use the `condition-expression` parameter.

**Deliverable 2.3:** Complete CLI command with condition expression. Explain what error DynamoDB returns if the condition fails and what this pattern prevents in a production application.

---

## Part 3: Architecture Analysis (25 points)

### Problematic Architecture Description

A gaming company uses DynamoDB to store game session leaderboard data. Their table has this design:

- Partition key: GameMode (values: SOLO, TEAM, TOURNAMENT)
- Sort key: Timestamp
- Capacity mode: Provisioned — 1,000 RCUs and 1,000 WCUs
- No secondary indexes
- DAX enabled

During weekend tournaments, they observe throttling errors despite provisioned capacity appearing underutilized on the CloudWatch dashboard. The team also receives complaints that leaderboard search by PlayerName (an attribute, not a key) is extremely slow.

### Task 3.1 — Identify Performance Issues

Identify and explain all performance and design issues in the architecture. For each issue, explain the root cause and the observed symptom.

**Deliverable 3.1:** List of all identified issues (minimum three) with root cause and symptom for each.

### Task 3.2 — Propose Fixes

For each issue identified in Task 3.1, propose a specific fix. Your fixes must address:

- The partition key throttling problem
- The leaderboard search by PlayerName problem
- Any other issues you identified

For each fix, specify the exact DynamoDB feature, configuration change, or redesign involved.

**Deliverable 3.2:** Specific fix for each identified issue with the exact DynamoDB feature or configuration involved.

### Task 3.3 — Streams Integration

The company wants to automatically update a separate "Top 100 Leaderboard" DynamoDB table whenever a player's score in the main table is updated. Describe the complete architecture using DynamoDB Streams and Lambda. Include:

- Which Stream view type should be enabled on the source table and why
- How the Lambda function is triggered
- What logic the Lambda function would implement
- How to handle failures in the Lambda processing

**Deliverable 3.3:** Architecture description covering all four points above.

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Include all CLI commands exactly as written and all written responses. Submit to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: Table Design | 40 | Primary key supports access patterns 1-2 correctly; index types correctly justified; create-table command syntactically correct |
| Part 2: CLI Operations | 35 | put-item commands use correct attribute type syntax; query uses KeyConditionExpression; condition expression correctly prevents duplicate writes |
| Part 3: Architecture Analysis | 25 | Hot partition key problem identified and correctly explained; PlayerName query solution is a GSI; Streams architecture includes correct view type, trigger mechanism, and failure handling |
| **Total** | **100** | |
