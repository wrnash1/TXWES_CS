# Discussion Forum: Module 07 — MySQL and Cloud SQL

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Discussion Prompt

This module covered MySQL's architecture, InnoDB internals, user management, and Cloud SQL configuration including high availability and read replicas. The concepts in this module translate directly to real-world cloud architecture decisions.

Respond to **both parts** below.

---

## Part A — Architecture Design Scenario

You are a database engineer at a mid-sized e-commerce company. The development team is planning to migrate their MySQL 5.7 database from a self-managed VM to Cloud SQL for MySQL 8.0. The system has these characteristics:

- Peak traffic: 1,200 concurrent users during sales events
- Database size: 180 GB (mostly products, inventory, and orders tables)
- SLA requirement: 99.9% uptime, meaning less than 8.7 hours of downtime per year
- Reporting team runs large analytical queries during business hours that are causing query latency for the OLTP workload
- The application runs in GKE

Address all five points:

1. **Instance tier and HA:** Which instance tier would you select, and would you enable HA? Justify both choices using the SLA requirement.

2. **Read replica strategy:** How would you address the reporting query problem using read replicas? What connection string change is needed in the reporting application?

3. **innodb_buffer_pool_size:** The selected tier has 30 GB of RAM. What value would you set for `innodb_buffer_pool_size` in bytes? Show your calculation.

4. **Auth Proxy configuration:** Describe how you would configure the Auth Proxy for the GKE application. What IAM role does the GKE service account need?

5. **Authentication plugin concern:** The development team's MySQL client library is three years old. What potential issue should you flag before the migration, and what is the resolution?

---

## Part B — Storage Engine Reflection

One of the most consequential decisions in MySQL database design is the choice of storage engine. InnoDB is the clear production choice, but understanding why requires thinking about what would break if you used MyISAM.

1. Describe a real or hypothetical e-commerce operation — for example, placing an order, processing a payment, or updating inventory — that requires ACID transaction guarantees. Explain what could go wrong if that operation ran against a MyISAM table with no transaction support.

2. Why does Cloud SQL for MySQL only support InnoDB? What operational risk would Cloud SQL inherit if it supported MyISAM tables in a managed environment?

---

## Response Requirements

- Initial post: 350–450 words covering both parts.
- Reply to at least two classmates: 100–150 words each.
- Replies should add technical depth — challenge assumptions, point out edge cases, or extend the architecture with a feature your classmate did not consider.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part A — all five architecture points addressed with specific values | 45 |
| Part B — ACID scenario grounded in realistic consequence | 30 |
| Two peer replies with substantive technical content | 15 |
| Professional writing, correct MySQL and Cloud SQL terminology | 10 |
| **Total** | **100** |

---

## Instructor Notes

For Part A, look for students who correctly calculate `innodb_buffer_pool_size` in bytes rather than setting `30G` (which Cloud SQL does not accept as a flag value). Strong posts will also note that the reporting read replica should be in the same region to minimize replication lag for near-real-time reporting.

For Part B, the strongest responses will explain the specific failure mode — for example, that a MyISAM order insert that partially completes cannot be rolled back, leaving the database in an inconsistent state where payment was recorded but inventory was not decremented. Encourage students to think about the cascade of business consequences, not just the technical error.
