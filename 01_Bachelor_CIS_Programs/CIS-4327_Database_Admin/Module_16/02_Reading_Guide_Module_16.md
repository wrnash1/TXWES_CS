# Reading Guide: Module 16 — Exam Preparation and Capstone

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4327 &BULL; DATABASE ADMINISTRATION & SQL OPTIMIZATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

This reading guide is your comprehensive study reference for the Google Cloud
Professional Database Engineer exam. It consolidates the most exam-critical concepts
from all 16 modules into organized tables, decision frameworks, and review checklists.

**Estimated reading time**: 75–90 minutes

Use this guide as your primary review document in the week before the exam.

---

## Section 1 — Service Selection Reference

### 1.1 Database Service Quick Reference

| Workload | Best Service | Key Reason |
|---|---|---|
| OLTP, SQL, regional HA, managed | Cloud SQL | Fully managed MySQL/PostgreSQL/SQL Server |
| OLTP, global scale, strong consistency | Cloud Spanner | Horizontal scale + external consistency |
| OLTP + analytics, PostgreSQL-compatible | AlloyDB | HTAP; columnar cache + Vertex AI |
| Wide-column NoSQL, time-series, IoT | Cloud Bigtable | Single-digit ms latency at petabyte scale |
| Document NoSQL, mobile/web | Firestore | Serverless; offline sync; real-time listeners |
| In-memory cache/session store | Memorystore | Redis or Valkey; sub-millisecond latency |
| Petabyte-scale analytics | BigQuery | Serverless OLAP; columnar; Dremel engine |

### 1.2 Cloud SQL Version Support

| Engine | Supported Versions |
|---|---|
| MySQL | 5.7, 8.0 |
| PostgreSQL | 9.6, 10, 11, 12, 13, 14, 15, 16 |
| SQL Server | 2017, 2019, 2022 (Enterprise/Standard/Web/Express) |

### 1.3 High Availability Summary

| Service | HA Mechanism | Failover Time |
|---|---|---|
| Cloud SQL | Synchronous standby in another zone | 30–120 seconds |
| AlloyDB | Automated failover to standby | ~60 seconds |
| Cloud Spanner (Regional) | 3-zone quorum writes | Automatic, transparent |
| Cloud Spanner (Multi-region) | Multi-region leader election | Automatic, transparent |
| BigQuery | Serverless; no HA configuration needed | N/A |

---

## Section 2 — Exam Domain Checklists

### 2.1 Section 1: Design (22%)

Key design decisions tested:

- Choosing between Cloud SQL, Spanner, AlloyDB, Bigtable, Firestore for a described workload
- Designing Spanner schemas to avoid hotspots (UUID keys, interleaved tables)
- Choosing availability type for Cloud SQL (REGIONAL vs. ZONAL)
- BigQuery table design: partition type, cluster columns, `require_partition_filter`
- CMEK configuration requirements and limitations (set at creation, not after)
- Cross-region read replica design for Cloud SQL
- AlloyDB read pool instance configuration

Common design question patterns:

- "A startup needs a relational database that scales globally with zero downtime. Which service?"
- "A table receives millions of timestamp-keyed writes per second. What Spanner key design prevents hotspots?"
- "Which Cloud SQL availability type provides automatic failover within a region?"

### 2.2 Section 2: Manage (20%)

Key management topics:

- Setting database flags with `gcloud sql instances patch --database-flags`
- Connection pooling: Cloud SQL Proxy + PgBouncer; built-in Cloud SQL connection pooler
- Point-in-time recovery: `gcloud sql instances clone --point-in-time`
- Maintenance windows and deny maintenance periods
- Cloud SQL Insights: enabling, interpreting query CPU time and wait events
- BigQuery DML: INSERT, UPDATE, DELETE, MERGE patterns and cost implications
- Managing BigQuery materialized view refresh (incremental vs. full)
- Spanner schema changes: `ALTER TABLE` is online and non-blocking

### 2.3 Section 3: Migrate (18%)

Migration tool selection:

| Scenario | Tool |
|---|---|
| MySQL/PostgreSQL → Cloud SQL (continuous) | DMS |
| Oracle/SQL Server → Cloud SQL for PostgreSQL | DMS + schema conversion |
| Any relational → BigQuery (streaming CDC) | Datastream |
| Teradata/Redshift → BigQuery | BigQuery Data Transfer Service |
| Files → Cloud Storage → BigQuery | Storage Transfer + BigQuery load jobs |
| Complex ETL during migration | Dataflow |

DMS requirements checklist:

- MySQL source: `binlog_format=ROW`, `binlog_row_image=FULL`, migration user with REPLICATION privileges
- PostgreSQL source: `wal_level=logical`, replication slot, REPLICATION privilege
- SQL Server source: CDC enabled at database level, Agent service running

### 2.4 Section 4: Deploy Cost-Optimized (18%)

Cost optimization checklist by service:

**Cloud SQL**:

- Right-size tier based on CPU/memory utilization (< 60% CPU typical target)
- Use committed use discounts for steady-state workloads
- Enable auto-storage increase + disk utilization alert
- Delete idle read replicas

**BigQuery**:

- Partition + cluster tables to minimize bytes scanned
- Use `require_partition_filter = true` on large tables
- Materialized views for repeated aggregation queries
- Results cache: avoid non-deterministic functions in repeated queries
- Flat-rate slots for > ~$20K/month in on-demand query costs
- Monitor `INFORMATION_SCHEMA.JOBS_BY_PROJECT` for expensive queries

**Cloud Spanner**:

- Right-size processing units (high-priority CPU < 65%)
- Use committed use discounts
- Avoid cross-region replication unless global reads are required

### 2.5 Section 5: Automate and Monitor (22%)

Monitoring metric reference:

| Service | Metric | Alert Threshold |
|---|---|---|
| Cloud SQL | `database/cpu/utilization` | > 0.80 for 5 min |
| Cloud SQL | `database/memory/utilization` | > 0.90 |
| Cloud SQL | `database/postgresql/num_backends` | > 80% of max_connections |
| Cloud SQL | `database/disk/utilization` | > 0.85 |
| Cloud SQL Replica | `database/replication/replica_lag` | > 30 seconds |
| Spanner | `instance/cpu/utilization_by_priority` (high) | > 0.65 |
| BigQuery | `job/num_failed_jobs` | > 0 |

Terraform resource reference:

| Resource | Terraform Type |
|---|---|
| Cloud SQL instance | `google_sql_database_instance` |
| Cloud SQL database | `google_sql_database` |
| BigQuery dataset | `google_bigquery_dataset` |
| BigQuery table | `google_bigquery_table` |
| Cloud Monitoring alert | `google_monitoring_alert_policy` |
| Cloud Monitoring dashboard | `google_monitoring_dashboard` |

---

## Section 3 — Security Quick Reference

### 3.1 IAM Roles Summary

**Cloud SQL roles**:

- `roles/cloudsql.admin`: Full control
- `roles/cloudsql.editor`: Manage databases and users; no instance create/delete
- `roles/cloudsql.client`: Connect via proxy (minimum for application accounts)
- `roles/cloudsql.instanceUser`: IAM database authentication login

**BigQuery roles**:

- `roles/bigquery.admin`: Full control
- `roles/bigquery.dataEditor`: Read/write data
- `roles/bigquery.dataViewer`: Read-only data (requires jobUser to run queries)
- `roles/bigquery.jobUser`: Run query jobs

**Exam trap**: `roles/bigquery.dataViewer` alone cannot run queries.
Must combine with `roles/bigquery.jobUser`.

### 3.2 Encryption Decision Matrix

| Requirement | Solution |
|---|---|
| Default managed encryption | GMEK (no configuration needed) |
| Customer controls key rotation | CMEK with Cloud KMS |
| Customer controls key and HSM | Cloud External Key Manager (EKM) |
| Render data inaccessible immediately | Disable CMEK key version in KMS |

### 3.3 Security Architecture Patterns

- **Defense in depth**: Network (Private IP, VPC-SC) → Identity (IAM, IAM auth) →
  Data (CMEK, SSL) → Audit (Admin Activity, Data Access logs)
- **Authorized views**: Cross-dataset data access without exposing source tables
- **Column-level security**: Policy tags + masking rules in BigQuery
- **Row-level security**: Row access policies in BigQuery

---

## Section 4 — Common Exam Traps Summary

| Trap | Correct Understanding |
|---|---|
| BigQuery dataViewer can run queries | False — also needs jobUser |
| DMS migrates stored procedures | False — data only; objects migrated separately |
| DMS promotion can be reversed | False — promotion is one-way |
| CMEK can be added to an existing Cloud SQL instance | False — set at creation only |
| BigQuery automatically blocks table scans without partition filter | False — only when `require_partition_filter = true` is set |
| Cloud SQL SSL is enforced by default | False — default is ALLOW_UNENCRYPTED_AND_ENCRYPTED |
| Spanner needs HA configuration like Cloud SQL | False — HA is built in; no configuration needed |
| Admin Activity audit logs must be explicitly enabled | False — always on |
| Data Access audit logs are always on | False — must be explicitly enabled |
| Terraform state is local by default and automatically backed up | False — local by default, not backed up; use GCS backend |

---

## Section 5 — 20-Question Practice Exam Reference Topics

The Module 16 quiz covers 20 questions across all exam domains. Before taking it,
verify you can confidently explain:

**Design**:

- Spanner hotspot prevention strategies
- Cloud SQL HA vs. non-HA failover behavior
- AlloyDB vs. Cloud SQL selection criteria
- BigQuery partition type selection

**Manage**:

- Cloud SQL PITR vs. automated backup differences
- IAM database authentication configuration steps
- Cloud SQL Insights setup and interpretation
- Database flag configuration syntax

**Migrate**:

- DMS MySQL source prerequisites
- DMS vs. Datastream use case distinction
- Schema conversion scope (what DMS converts vs. what requires manual work)
- Migration validation levels (1, 2, 3)

**Cost**:

- BigQuery on-demand vs. flat-rate decision threshold
- Cloud SQL committed use discount savings percentages
- BigQuery partition pruning mechanism

**Security and Automate**:

- Authorized view configuration steps
- VPC Service Controls vs. Private IP distinction
- Terraform `prevent_destroy` vs. `deletion_protection`
- Cloud Monitoring alert duration semantics
- Forced failover command and measurement

---

## Section 6 — Exam-Day Checklist

- Register at webassessor.com or through Google Cloud's certification portal
- Valid government-issued photo ID required
- Remote proctoring: quiet room, clear desk, webcam and microphone
- No notes, no additional browser tabs
- 2 hours, 50–60 questions
- Results: pass/fail shown immediately; detailed score report sent within a few days

---

---

## 9. Supplemental Resources

The following free, open-access resources support Module 16 capstone topics:

**1. [Google Cloud — Professional Cloud Database Engineer Exam Guide](https://cloud.google.com/learn/certification/guides/database-engineer)**
The official exam guide listing all exam domains, weightings, and topic areas. Use this to verify coverage before sitting the exam.

**2. [Google Cloud — Database Services Overview](https://cloud.google.com/products/databases)**
High-level summary of all GCP database services (Cloud SQL, Spanner, AlloyDB, Bigtable, Firestore, BigQuery) with links to documentation, helping with service selection decisions tested across all exam domains.

**3. [Google Cloud — Architecture Center: Database Solutions](https://cloud.google.com/architecture/databases)**
Reference architectures for common database patterns including HA, migration, analytics, and security configurations — all topics covered on the Professional Cloud Database Engineer exam.

**4. [Google Cloud Skills Boost — Professional Cloud Database Engineer Learning Path](https://www.cloudskillsboost.google/paths/22)**
Free hands-on labs, courses, and quests aligned to the Professional Cloud Database Engineer exam domains, including interactive Qwiklabs for Cloud SQL, BigQuery, Spanner, and Datastream.

---

Module 16 Reading Guide — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
