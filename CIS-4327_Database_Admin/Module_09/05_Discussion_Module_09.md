# Discussion Forum: Module 09 — High Availability and Replication

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Discussion Prompt

High availability and replication architecture decisions have direct business consequences. A wrong configuration choice can mean the difference between five minutes of downtime and five hours, or between zero data loss and the loss of an hour of transactions.

Respond to **both parts** below.

---

## Part A — Architecture Decision Scenario

A legal technology firm runs a PostgreSQL 15 database containing case evidence records, billing records, and client communications on Google Cloud Compute Engine VMs (not Cloud SQL). The system requirements are:

- RPO = 0 — no data loss is acceptable under any circumstance
- RTO = 5 minutes — the system must be operational within 5 minutes of failure detection
- Read load: 40% of all queries are read-only analytics run by the billing team
- The infrastructure team has 2 engineers and limited capacity to manage complex systems
- The database is 300 GB and receives approximately 500 write transactions per minute

Address all four points:

1. **Replication type:** Should this system use synchronous or asynchronous replication? Justify your choice using the RPO requirement. Identify the specific PostgreSQL parameter that must be set and what value it needs.

2. **Standby read access:** Can the billing team's analytics queries run against the standby? What PostgreSQL parameter controls this? What is the RPO implication if they do?

3. **Automatic failover:** The infrastructure team cannot run a 24/7 on-call rotation. What tool would you recommend for automatic failover, and what additional infrastructure (consensus store) does it require?

4. **Cloud SQL alternative:** Given the infrastructure team's limited capacity, would you recommend migrating to Cloud SQL HA instead? What does the team gain and what do they lose compared to self-managed with Patroni?

---

## Part B — The Synchronous Replication Tradeoff

Synchronous replication guarantees RPO = 0 by requiring the standby to acknowledge WAL before the primary commits. But it introduces a dangerous failure mode: if all named synchronous standbys disconnect, the primary stalls indefinitely — no new commits can complete until a standby reconnects.

1. Describe a real scenario (data center network partition, standby disk failure, or standby server crash) that would cause the primary to stall under synchronous replication. What would users experience?

2. PostgreSQL offers `synchronous_commit = remote_write` as an intermediate setting. How does it differ from full `synchronous_commit = on`? What RPO guarantee does it actually provide?

3. Is it ever appropriate to accept some data loss (RPO > 0) even for financial or legal systems? Describe one scenario where a well-reasoned argument could be made for asynchronous replication despite the data loss risk.

---

## Response Requirements

- Initial post: 400–500 words covering both parts.
- Reply to at least two classmates: 100–150 words each.
- Replies should specifically engage with a configuration choice your classmate made — either agreeing with specific technical reasoning, or identifying a risk they did not consider.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part A — all four points with specific parameter names and values | 40 |
| Part B — nuanced analysis of synchronous replication tradeoffs | 35 |
| Two substantive peer replies | 20 |
| Clear technical writing | 5 |
| **Total** | **100** |

---

## Instructor Notes

Part A is designed to surface a common student error: assuming Cloud SQL HA automatically provides read scalability from the standby. It does not — the Cloud SQL HA standby cannot serve queries. Strong responses to point 4 will note that Cloud SQL HA provides simpler operations and built-in failover but removes the read-capable hot standby that a self-managed Patroni cluster would have. The firm might need both Cloud SQL HA and a Cloud SQL read replica for their requirements.

For Part B, the goal is for students to develop nuanced thinking. The stall scenario is a real operational risk — `synchronous_standby_names = 'standby1'` with a single standby means any standby outage halts the primary. Using `FIRST 1 (standby1, standby2)` with two standbys reduces this risk significantly. Strong posts will arrive at this insight independently.
