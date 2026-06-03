# Video Script: Module 16 — Exam Preparation and Capstone (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Part 2 Introduction

Welcome back to Module 16. In Part 1 we reviewed exam Sections 1–3: database design,
multi-database management, and migration. In Part 2 we cover Sections 4 and 5:
cost-optimized deployment, security, automation, and monitoring. We finish with
exam strategy.

---

## SLIDE 2 — Section 4: Cost Optimization Review

Section 4 tests cost management across all GCP database services.

**Cloud SQL cost factors**:

- Instance tier (vCPU + RAM): The dominant cost. Right-size based on CPU and memory
  utilization. Use `db-g1-small` or `db-f1-micro` for development only.
- Storage: Charged per GB per month. Auto-storage increase prevents outages
  but can grow cost unexpectedly — set an alert on disk utilization.
- Backup storage: Automated backups are free up to the instance size; excess is charged.
- Network egress: Replicas in different regions incur cross-region egress charges.

**Cloud Spanner cost factors**:

- Processing units (PUs): Spanner's compute unit. 1,000 PUs = 1 node.
  Minimum is 100 PUs for development. Typical production starts at 1,000 PUs.
- Storage: $0.30/GB/month (approximate).
- Cost optimization: Right-size processing units based on CPU utilization.
  High-priority CPU should stay below 65%.

**BigQuery cost optimization** (covered extensively in Module 12):

- Use partitioning and clustering to reduce bytes scanned.
- Use `require_partition_filter = true` to prevent accidental full-table scans.
- Use materialized views for precomputed aggregations.
- Use flat-rate slot commitments for predictable high-volume workloads.
- Monitor `INFORMATION_SCHEMA.JOBS_BY_PROJECT` for expensive queries.

---

## SLIDE 3 — Section 4: Committed Use Discounts

Cloud SQL and Spanner offer committed use discounts (CUDs) for 1-year or 3-year
commitments. These are significant cost savings for steady-state production workloads.

**Cloud SQL CUDs**:

- 1-year commitment: approximately 25% discount on vCPU and memory
- 3-year commitment: approximately 52% discount
- Applicable to the instance tier; storage is not eligible

**Cloud Spanner CUDs**:

- 1-year commitment: approximately 20% discount on processing units
- 3-year commitment: approximately 40% discount

**For the exam**: CUDs make financial sense when resource utilization is consistently
high (> 60%). For variable workloads with predictable minimum utilization, commit
to the minimum level and pay on-demand for bursts.

---

## SLIDE 4 — Section 4: Cost Monitoring Tools

**Cloud Billing export to BigQuery**: All GCP billing data can be exported to BigQuery
in near real-time. This enables SQL-based cost analysis and alerting.

Example query — find the most expensive Cloud SQL instances over the past 30 days:

```sql
SELECT
  resource.labels.database_id,
  SUM(cost) AS total_cost,
  SUM(credits.amount) AS total_credits
FROM `PROJECT.billing_export.gcp_billing_export_v1_*`
WHERE service.description = 'Cloud SQL'
  AND usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
```

**Budget alerts**: Set budgets on projects or billing accounts that alert when
spending exceeds thresholds. Configure budget alerts at 50%, 75%, and 100% of
the monthly budget for each environment.

**Recommender API**: Google's Recommender service provides cost optimization
suggestions including idle Cloud SQL instances, right-sizing recommendations,
and BigQuery slot allocation adjustments. Check Recommender monthly.

---

## SLIDE 5 — Section 5: Security Review — Top Exam Topics

Security is tested in Sections 4 and 5. These are the highest-frequency security
exam topics:

**IAM least privilege**:

- Application service accounts: `roles/cloudsql.client` (not admin or editor)
- Read-only users: `roles/bigquery.dataViewer` + `roles/bigquery.jobUser`
- DBA team: `roles/cloudsql.editor` (no instance create/delete)

**Encryption**:

- CMEK: Set at resource creation, cannot change. Requires KMS key grant to service account.
- VPC-SC: Prevents API-level exfiltration. Works on top of IAM (both must pass).
- SSL mode: `ENCRYPTED_ONLY` for most production; `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`
  for highest assurance.

**Audit logging**:

- Admin Activity: always on, 400-day retention
- Data Access: must enable, 30-day retention, log data reads and writes
- pgaudit: SQL-level logging inside PostgreSQL engine

**Secret management**:

- Database passwords in Secret Manager, never in code or environment variables
- IAM database authentication: eliminates passwords entirely for Cloud SQL

**BigQuery security patterns**:

- Authorized views: restrict column access without exposing source tables
- Policy tags + masking: transform sensitive column values at query time
- Row access policies: restrict row visibility per identity
- VPC Service Controls: prevent cross-project data exfiltration

---

## SLIDE 6 — Section 5: Automation Review — Key Terraform Resources

The exam may ask which Terraform resource or attribute achieves a stated goal.

| Goal | Terraform Resource / Attribute |
|---|---|
| Create Cloud SQL instance | `google_sql_database_instance` |
| Create Cloud SQL database | `google_sql_database` |
| Create Cloud SQL user | `google_sql_user` |
| Enable HA on Cloud SQL | `settings.availability_type = "REGIONAL"` |
| Enable PITR | `settings.backup_configuration.point_in_time_recovery_enabled = true` |
| Set maintenance window | `settings.maintenance_window` block |
| Prevent deletion | `deletion_protection = true` and `lifecycle { prevent_destroy = true }` |
| Create BigQuery dataset | `google_bigquery_dataset` |
| Create BigQuery table | `google_bigquery_table` |
| Create Cloud Monitoring alert | `google_monitoring_alert_policy` |
| Create Cloud Monitoring dashboard | `google_monitoring_dashboard` |
| Store state remotely | `terraform { backend "gcs" {} }` |

---

## SLIDE 7 — Section 5: Automation — Cloud Build and Cloud Scheduler

Automating database operations beyond Terraform:

**Cloud Build for database CI/CD**:

- Run `terraform plan` on every PR to databases infrastructure
- Run schema migration scripts (Flyway, Liquibase) as Cloud Build steps
- Run failover tests monthly on a Cloud Build trigger triggered by Cloud Scheduler

**Cloud Scheduler for recurring tasks**:

- Schedule weekly report exports from BigQuery to Cloud Storage
- Trigger monthly failover tests
- Run nightly database health check scripts

**Dataflow for database ETL**:

- Transform and load data between Cloud SQL and BigQuery
- Implement deduplication, type conversion, or enrichment during migration
- Use pre-built Dataflow templates for common patterns (Cloud SQL to BigQuery)

**Cloud Functions for event-driven automation**:

- Trigger on Pub/Sub messages from Datastream CDC events
- Send Slack alerts when specific database conditions are detected via log sinks
- Automate snapshot creation before a schema migration job

---

## SLIDE 8 — Full-Course Concept Map

Here is how all the modules connect for the exam:

**Database Design** (Modules 1–6):

- Cloud SQL (MySQL, PostgreSQL, SQL Server): OLTP, regional HA, managed
- Cloud Spanner: global OLTP, strong consistency, interleaved tables
- AlloyDB: HTAP, Vertex AI integration, PostgreSQL-compatible
- Bigtable: wide-column NoSQL, time-series, IoT scale
- Firestore: document NoSQL, mobile/web backend
- Memorystore: key-value cache, session storage

**Operations and Analytics** (Modules 7–12):

- High availability and disaster recovery: HA, cross-region replicas, PITR
- Performance optimization: indexes, query plans, Cloud SQL Insights, read replicas
- BigQuery: columnar storage, Dremel, partitioning, clustering, DML/DDL, materialized views

**Security** (Module 13):

- Encryption (GMEK, CMEK), IAM auth, SSL modes, audit logging, VPC-SC, column-level security

**Migration** (Module 14):

- DMS (homogeneous, heterogeneous, CDC), Datastream, BigQuery DTS, validation, cutover

**Automation and Monitoring** (Module 15):

- Cloud Monitoring metrics and alerts, Cloud SQL Insights, Terraform, failover testing

---

## SLIDE 9 — Exam Strategy

With the technical content reviewed, let's talk about how to approach the exam itself.

**Read the full question**: Exam questions often have critical details near the end.
"With minimal downtime" or "without changing the schema" or "using only managed
services" radically change the correct answer.

**Eliminate clearly wrong answers first**: Most questions have one or two obviously
incorrect options. Eliminating them narrows your choice and improves your odds
on uncertain questions.

**Watch for absolute language**: Answers containing "always," "never," or "all"
are often incorrect. GCP services have nuances and exceptions.

**Identify the constraint**: Most questions have a stated constraint
(minimal downtime, zero data loss, cheapest solution, minimum configuration). The
correct answer satisfies the constraint; other answers may be technically valid but
do not meet the specific requirement.

**Time management**: With 2 hours for 50–60 questions, you have approximately
2 minutes per question. Flag difficult questions and move on. Return to flagged
questions after completing the rest.

**Practice questions**: The 20-question quiz in this module simulates exam format.
Take it under exam conditions (no notes, timed) to identify weak areas.

---

## SLIDE 10 — Certification Path and Next Steps

After earning the Professional Database Engineer certification:

**Complementary certifications**:

- **Professional Cloud Architect**: Broader GCP design skills. Database Engineer
  knowledge is a strong foundation.
- **Professional Data Engineer**: Focuses on data pipelines (Dataflow, Pub/Sub,
  BigQuery). Complements Database Engineer with stream processing skills.
- **Professional Cloud Developer**: Application-focused. Useful for full-stack
  engineers who manage their own databases.

**Staying current**: GCP releases new database features regularly. Follow:

- Google Cloud Blog (cloud.google.com/blog) for release announcements
- Google Cloud release notes (cloud.google.com/release-notes)
- Google Cloud Next conference sessions (available on YouTube)

**Exam recertification**: Professional certifications expire after 2 years.
Recertification is available 1 year after passing.

---

## SLIDE 11 — Final Words

This has been a demanding course, and you have covered substantial ground —
from Cloud SQL provisioning in Module 1 through BigQuery optimization,
database security, migration strategies, and infrastructure automation.

The Google Cloud Professional Database Engineer certification validates that you
can design, operate, secure, and troubleshoot production database systems on GCP.
That is a valuable and in-demand skill.

Take the practice quiz under exam conditions. Review the reading guide's concept
tables. Complete the capstone lab — designing a complete multi-tier database
architecture challenges you to integrate everything from the course.

Thank you for your work throughout CIS-4327. Good luck on the certification exam,
and I look forward to seeing your capstone architecture designs.

---

*End of Part 2 Script*
