# Discussion Forum: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

---

### Overview

This discussion connects Cloud SQL operational decisions to real-world production engineering scenarios. Read all three scenarios and post your initial response to the one that best matches your professional background or academic focus. You must reply to at least two classmates from any scenario.

---

### Scenario A — Startup Migration from Heroku to Cloud SQL

A fast-growing SaaS startup currently runs a PostgreSQL database on Heroku. The database is 120 GB, serves 50,000 active users, and is experiencing latency spikes during peak hours because analytics queries from the reporting team run during business hours on the same database instance. The engineering team has decided to migrate to Google Cloud SQL for PostgreSQL within 90 days.

For your initial post, address all of the following.

Identify the specific Cloud SQL features you would use to resolve the analytics query latency problem and explain how each feature addresses it. Describe what connection method you would configure for the application and why, referencing the specific security concern that method addresses. State whether you would choose Cloud SQL Enterprise or Enterprise Plus for this workload and justify your choice based on at least two technical criteria from Module 03. Identify one risk specific to the 90-day migration timeline and describe a mitigation strategy. Your post should be 175–225 words using correct Cloud SQL terminology.

---

### Scenario B — Financial Services Production Outage Response

A financial services company runs a Cloud SQL for MySQL instance as the primary database for a trading platform. The instance is configured as a single-zone (zonal) instance with automated backups enabled but PITR disabled. At 9:47 AM on a trading day, a developer runs a migration script that accidentally drops a critical reference table containing 180,000 rows of pricing data. The table contained no foreign key references from other tables. Trading operations are halted.

For your initial post, address all of the following.

Explain why PITR was not available to recover the dropped table in this scenario, citing the specific configuration gap. Describe the recovery options that are available given the current configuration, and identify the most likely data loss exposure (how much data could be permanently lost). Identify two configuration changes that should have been made before go-live to prevent or minimize this type of incident. Explain what the term "zonal instance" means and describe the additional risk it represents beyond the data loss scenario. Your post should be 175–225 words using correct Cloud SQL terminology.

---

### Scenario C — Multi-Tenant SaaS Connection Management

A multi-tenant SaaS platform runs on Google Kubernetes Engine and uses Cloud SQL for PostgreSQL as its database. The platform has 300 tenant customers, and each API request opens a new database connection. The engineering team reports that they frequently hit the Cloud SQL maximum connection limit, causing connection timeouts during peak usage even though CPU and RAM utilization on the database instance is only at 40%.

For your initial post, address all of the following.

Explain why the application can exhaust Cloud SQL's connection limit even when CPU and RAM are not the bottleneck, and what resource is actually being consumed. Identify the specific solution recommended in Module 03 for this problem and describe how it works at an architectural level. Describe what transaction pooling mode means in the context of that solution and why it is recommended over session pooling for a Kubernetes microservice architecture. Identify one trade-off or limitation of the recommended solution that the engineering team should be aware of before deploying it to production. Your post should be 175–225 words using correct terminology from Module 03.

---

### Peer Response Guidelines

Reply to at least two classmates across any scenario. Each reply must be at least 50 words and add technical value — a configuration detail they missed, a trade-off to consider, a counter-scenario, or a substantive follow-up question. Superficial agreement does not qualify.

---

### Discussion Rubric — 10 Points Total

Initial post — 6 points.

- 5 to 6 points: Addresses all required elements with technical accuracy, correct Cloud SQL terminology, and clear reasoning. Meets the 175–225 word count.
- 3 to 4 points: Addresses most elements but omits one required item or lacks technical precision.
- 0 to 2 points: Initial post is missing, substantially incomplete, or contains significant errors about Cloud SQL behavior.

Peer responses — 4 points.

- 4 points: Two substantive replies of at least 50 words each that contribute technical content.
- 2 points: Only one qualifying reply, or both replies are superficial.
- 0 points: No peer responses by the deadline.

---

### Due Dates

Initial post: Wednesday at 11:59 PM

Peer responses: Sunday at 11:59 PM

Professor Nash reads every post. Responses that demonstrate hands-on understanding from the lab will be recognized in class.

---

Reference: cloud.google.com/learn
