# Discussion Forum: Module 06 — PostgreSQL Administration

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Discussion Prompt

This week we covered PostgreSQL administration in depth — configuration, authentication, roles, VACUUM, monitoring, and connection pooling. These are the skills that separate a developer who can query a database from a DBA who can keep one running reliably under production load.

For this discussion, respond to **both parts** below.

---

## Part A — Configuration Decision

You are the database engineer for a SaaS company that is migrating a self-managed PostgreSQL 14 instance to Cloud SQL for PostgreSQL. The application currently uses 350 persistent connections from an application server pool. The Cloud SQL instance will be an `n2-standard-8` (8 vCPUs, 32 GB RAM).

Address all four points in your post:

1. **shared_buffers and work_mem:** What values would you recommend for `shared_buffers` and `work_mem` on a 32 GB instance? Justify your choices using the sizing rules from the lecture.

2. **max_connections vs PgBouncer:** The engineering team proposes setting `max_connections = 400` to accommodate growth. Do you agree or disagree? If you recommend a different approach, explain it with specific PgBouncer configuration values (`max_client_conn`, `default_pool_size`, `pool_mode`).

3. **wal_level for replication:** The company wants a read replica for reporting queries. What `wal_level` is needed, and how would you set this flag on Cloud SQL?

4. **pg_hba.conf equivalent on Cloud SQL:** Cloud SQL does not expose pg_hba.conf directly. How do you control which clients can connect, and which authentication method does Cloud SQL enforce for SSL connections?

---

## Part B — Real-World Reflection

Think about a database or application you have worked with (a class project, personal project, internship, or job experience). If you have not worked with a database directly, use a publicly documented system (e.g., a well-known open-source project on GitHub).

Answer these questions:

1. Did that system show any signs of the problems discussed in this module — connection exhaustion, bloated tables, slow queries from stale statistics, or lock contention? Describe what you observed or found in the documentation.

2. Based on what you learned in Module 06, what one change would have the biggest positive impact on that system, and why?

3. Would PgBouncer transaction pooling be safe to use with that application, or would session-level features require session pooling instead? Explain your reasoning.

---

## Response Requirements

- Initial post: 300–400 words covering both parts.
- Reply to at least two classmates: 100–150 words each.
- Your replies should either challenge an assumption in your classmate's recommendation with a specific counter-argument, or extend their idea with an additional configuration they did not mention.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part A — all four configuration points addressed with justification | 40 |
| Part B — reflection grounded in specific observable detail | 30 |
| Two peer replies that are substantive and technically accurate | 20 |
| Professional writing, correct PostgreSQL terminology | 10 |
| **Total** | **100** |

---

## Instructor Notes

Look for students who correctly identify that `work_mem` must be sized conservatively because a single query can allocate it multiple times across parallel sort nodes. A common error is assuming `work_mem = 500 MB` is safe on a 32 GB box when `max_connections = 400` — the math shows potential worst-case RAM usage of 200 GB. Strong posts will catch this.

For Part B, the goal is to build metacognitive awareness — connecting textbook parameters to real performance problems. Encourage students who say "I haven't worked with a database" to explore a GitHub project's issue tracker for performance-related issues; almost every large open-source project has them.
