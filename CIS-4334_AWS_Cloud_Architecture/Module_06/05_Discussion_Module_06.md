# Discussion Forum: Module 06 - RDS and Aurora: Managed Relational Databases

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Instructions

Read all three scenarios below and select one to address in your initial post. Your initial post must be 175-225 words, technically precise, and reference specific RDS or Aurora features from this module. Respond to at least two classmates who chose different scenarios from yours.

Initial post due: Wednesday at 11:59 PM
Peer responses due: Sunday at 11:59 PM

---

## Scenario A - Read Performance vs. High Availability Confusion

A startup's CTO asks the engineering team to "add a Multi-AZ standby to handle the reporting team's heavy SQL queries — they're killing production performance." The lead engineer agrees and enables Multi-AZ on the production database. After the change, the reporting queries are still running on the primary instance and the performance problem persists. Diagnose the architectural misunderstanding, explain specifically why Multi-AZ did not solve the problem, and propose the correct architecture. In your response, identify the specific RDS feature that should have been used, how the reporting team must change their connection string or database endpoint, and why the chosen solution works when Multi-AZ does not.

---

## Scenario B - Database Migration Decision

A company is migrating three databases from on-premises to AWS: (1) a MySQL 8.0 transactional database for their e-commerce platform processing 10,000 orders per day, (2) a PostgreSQL analytics database running complex queries on 2 TB of historical data, and (3) a small development MySQL database used by the engineering team for testing and available only during business hours. For each database, recommend whether to use RDS for MySQL, RDS for PostgreSQL, Aurora MySQL, Aurora PostgreSQL, or Aurora Serverless v2, and justify each recommendation. Your response should address performance requirements, cost, and availability for each database individually.

---

## Scenario C - Disaster Recovery Architecture

A financial services company currently runs Aurora MySQL in us-east-1. Their current DR plan is to restore from automated backups if the primary Region fails — estimated recovery time is 45-60 minutes. The compliance team has set a new RTO requirement of 5 minutes for any database-related failure, including full regional outages. The company also wants users in Europe and Asia Pacific to experience lower database read latency. Evaluate the current DR plan against the new RTO requirement, explain why it fails, and propose a replacement architecture that satisfies both the 5-minute RTO and the global read latency requirements. Identify the specific Aurora feature involved and explain how it addresses both goals simultaneously.

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — technical accuracy | 3 | Correctly identifies RDS/Aurora features, replication types, and endpoint behavior; no factual errors |
| Initial post — depth and completeness | 2 | Addresses all parts of the chosen scenario; 175-225 words; uses specific AWS service and feature names |
| Initial post — clarity | 1 | Well-organized, professional tone, correct AWS database terminology |
| Peer response 1 — substantive engagement | 2 | Adds an alternative approach, identifies a missed consideration, or extends the scenario; minimum 50 words |
| Peer response 2 — substantive engagement | 2 | Adds an alternative approach, identifies a missed consideration, or extends the scenario; minimum 50 words |
| **Total** | **10** | |

---

## Professor Nash Note

Scenario A requires you to understand the specific behavior of the Multi-AZ standby — not just that it is "for availability." Scenario B requires you to make cost-justified recommendations, not just recommend Aurora for everything. Scenario C requires you to know the RTO limitations of restore-from-backup and the specific Aurora feature that addresses sub-5-minute RTO with cross-region capability. Peer responses should engage with the design tradeoffs, not just validate the initial post.
