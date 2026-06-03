# Reading Guide: Module 13 — Database Security

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

This reading guide supports the Module 13 video lectures on database security. Security
is one of the highest-weighted domains on the Google Cloud Professional Database Engineer
exam. Mastering encryption, IAM, audit logging, network isolation, and data protection
patterns is essential for both the exam and production deployments.

**Estimated reading time**: 60–75 minutes

---

## Section 1 — Encryption

### 1.1 Encryption at Rest: Key Hierarchy

Google Cloud uses a hierarchical key system for data-at-rest encryption:

1. **Data Encryption Key (DEK)**: Encrypts the actual data. A unique DEK is generated
   for each data object (e.g., a Cloud SQL storage block).
2. **Key Encryption Key (KEK)**: Encrypts the DEK. This is the key stored in Cloud KMS
   when using CMEK.

This envelope encryption pattern means that changing or revoking the KEK immediately
invalidates all DEKs protected by that KEK, effectively making data inaccessible without
the need to re-encrypt all stored data.

**GMEK rotation**: Google automatically rotates the KEK at least once every year.
New DEKs are generated when data is written after rotation. Old data remains accessible
because Cloud KMS retains the old KEK version.

**CMEK rotation**: You can configure automatic key rotation on Cloud KMS keys. When
a key rotates, the old version is retained as a "previous version" and can still
decrypt data encrypted with it. New data is encrypted with the new primary version.
You can disable old key versions when confident all data has been re-encrypted.

### 1.2 CMEK Support by Service

Not all GCP services support CMEK equally. For the exam, know:

| Service | CMEK Support | Notes |
|---|---|---|
| Cloud SQL | Yes | Set at instance creation; cannot change after |
| BigQuery | Yes | Set at dataset or table creation |
| Cloud Spanner | Yes | Set at instance creation |
| Cloud Bigtable | Yes | Set at cluster creation |
| Cloud Storage | Yes | Set at bucket creation or object level |
| Memorystore (Redis/Valkey) | No | GMEK only |

### 1.3 Encryption in Transit Details

**TLS versions**: GCP services support TLS 1.2 and 1.3. TLS 1.0 and 1.1 are
deprecated and disabled on all Google services.

**Cloud SQL Auth Proxy**: The proxy manages TLS automatically, using certificates
from Google's certificate authority. The proxy also handles IAM authentication token
refresh, making it the recommended connection method for applications connecting to
Cloud SQL from GCP compute resources.

The proxy flow:

1. Application connects to localhost (proxy listening port).
2. Proxy authenticates to GCP using the application's service account.
3. Proxy establishes a TLS-encrypted tunnel to Cloud SQL.
4. All traffic is encrypted in transit through the tunnel.

---

## Section 2 — IAM Database Authentication

### 2.1 MySQL IAM Authentication

Cloud SQL for MySQL supports IAM authentication in MySQL 8.0. The setup differs
slightly from PostgreSQL:

- MySQL IAM users are created with `--type=CLOUD_IAM_USER` (same gcloud command).
- The MySQL user account name must match the IAM email exactly.
- The `cloudsql_iam_authentication` instance flag is required.
- For service accounts, use the service account email without the `.gserviceaccount.com`
  suffix as the MySQL username (e.g., `myapp@PROJECT` instead of `myapp@PROJECT.iam.gserviceaccount.com`).
  This is a common exam gotcha.

### 2.2 SQL Server IAM Authentication

Cloud SQL for SQL Server does NOT support IAM database authentication. SQL Server
instances on Cloud SQL use Windows-style SQL authentication only. For SQL Server,
use Secret Manager to store credentials and rely on SSL + Private IP for network security.

### 2.3 Service Account Best Practices

When an application connects to Cloud SQL via IAM authentication:

- Use a dedicated service account per application (not the default compute service account).
- Grant only `roles/cloudsql.instanceUser` — do not grant admin roles.
- Grant database-level permissions (SELECT, INSERT, etc.) within the database engine
  after creating the IAM user mapping.
- Enable Workload Identity Federation if the application runs on GKE, allowing
  Kubernetes service accounts to impersonate GCP service accounts without key files.

---

## Section 3 — Audit Logging Deep Dive

### 3.1 Log Storage and Retention

By default, Cloud Audit Logs are stored in Cloud Logging with these retention periods:

- Admin Activity logs: 400 days
- Data Access logs: 30 days
- System Event logs: 400 days

For compliance requirements exceeding these periods, export logs to Cloud Storage
(long-term archival) or BigQuery (analytical querying). Log sinks route log entries
to destinations as they are generated.

Creating a log sink to BigQuery:

```bash
gcloud logging sinks create audit-to-bq \
  bigquery.googleapis.com/projects/PROJECT_ID/datasets/audit_logs \
  --log-filter='logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"'
```

### 3.2 Key Log Fields for Database Security

When investigating a security incident, these are the most important fields in a
Cloud Audit Log entry for database operations:

- `protoPayload.authenticationInfo.principalEmail`: The identity that performed the action
- `protoPayload.methodName`: The API method called (e.g., `cloudsql.instances.connect`)
- `protoPayload.resourceName`: The resource affected
- `protoPayload.requestMetadata.callerIp`: The originating IP address
- `timestamp`: When the event occurred
- `protoPayload.status.code`: 0 = success, non-zero = failure

### 3.3 BigQuery Query Log Fields

For BigQuery, the most useful audit log fields are in `protoPayload.serviceData.jobCompletedEvent.job`:

- `jobConfiguration.query.query`: The full SQL text
- `jobStatistics.totalBilledBytes`: Bytes billed for the query
- `jobStatistics.createTime` / `endTime`: Query timing
- `jobConfiguration.query.destinationTable`: Where results were written

These fields allow you to audit who ran what queries, when, at what cost, and to which
destination tables.

---

## Section 4 — VPC Service Controls

### 4.1 Dry Run Mode

When first implementing VPC Service Controls, use **dry run mode** to evaluate what
would be blocked without actually blocking anything. In dry run mode, violations are
logged but not enforced.

```bash
gcloud access-context-manager perimeters dry-run create analytics-perimeter \
  --policy=POLICY_ID \
  --perimeter-title="Analytics Data Perimeter" \
  --perimeter-type=regular \
  --perimeter-resources=projects/PROJECT_NUMBER \
  --perimeter-restricted-services=bigquery.googleapis.com
```

After reviewing dry-run violation logs, convert to enforced mode:

```bash
gcloud access-context-manager perimeters dry-run enforce analytics-perimeter \
  --policy=POLICY_ID
```

### 4.2 Ingress and Egress Rules

VPC Service Controls allow fine-grained control over traffic crossing the perimeter:

**Ingress rules**: Allow specific sources (projects, identities, access levels) to call
specific API methods on resources inside the perimeter.

**Egress rules**: Allow specific identities inside the perimeter to call API methods
on specific external resources.

Example use case: Allow your Dataflow pipeline (running in a separate project) to
write to a BigQuery dataset inside the perimeter, without making the entire Dataflow
project part of the perimeter.

### 4.3 VPC Service Controls Limitations

VPC-SC does not protect against:

- Actions taken by Google infrastructure (e.g., Google's internal data processing)
- Services not explicitly listed in the restricted services configuration
- Data accessed via resource-level public sharing (e.g., a BigQuery dataset shared
  as "public" — disable public access before enabling VPC-SC)

---

## Section 5 — BigQuery Column-Level Security

### 5.1 Policy Tag Inheritance

Policy tags support a hierarchical taxonomy. If a child policy tag is applied to a
column, and a user has access to a parent policy tag, that user can also see columns
tagged with child tags.

Example taxonomy:

```
PII Classification
├── PII-High (SSN, credit card, biometrics)
│   └── PII-High-Financial (credit card only)
└── PII-Low (name, email, phone)
```

A user with fine-grained reader access on `PII-Low` can see columns tagged with
`PII-Low` but NOT columns tagged with `PII-High` or `PII-High-Financial`.

### 5.2 Row-Level Security

BigQuery also supports **row-level security** through **row access policies**. A row
access policy filters which rows a user can see when they query a table.

```sql
CREATE ROW ACCESS POLICY region_filter
ON txwes-analytics.sales_data.orders
GRANT TO ("user:southwest-analyst@company.com")
FILTER USING (region = 'Southwest');
```

Users with this policy applied can only see rows where `region = 'Southwest'`.
Row access policies and column-level security can be combined for comprehensive
data access control.

---

## Section 6 — Key Terms

**CMEK (Customer-Managed Encryption Key)**: An encryption key stored in Cloud KMS that the customer controls, including rotation and revocation.

**Envelope encryption**: A pattern where data is encrypted with a DEK, and the DEK is encrypted with a KEK. Changing the KEK invalidates access to all protected data.

**Cloud SQL Auth Proxy**: A binary that creates an encrypted tunnel between an application and a Cloud SQL instance, handling SSL and IAM authentication automatically.

**VPC Service Controls**: A GCP feature that creates API-level perimeters around projects and services to prevent data exfiltration.

**Policy Tag**: A Data Catalog classification applied to a BigQuery column that triggers column-level security and masking rules.

**pgaudit**: A PostgreSQL extension for query-level audit logging, available on Cloud SQL for PostgreSQL.

**Row access policy**: A BigQuery feature that restricts which rows a user can see in a table based on a filter expression.

**Secret Manager**: GCP service for securely storing and accessing secrets such as database passwords and API keys.

---

## Section 7 — Review Questions

1. What is the difference between GMEK, CMEK, and CSEK? In what scenario would a healthcare company use CMEK?

2. A Cloud SQL instance is configured with `ALLOW_UNENCRYPTED_AND_ENCRYPTED` SSL mode. What risk does this create, and how would you remediate it?

3. Explain how IAM database authentication eliminates the password rotation problem for Cloud SQL. What happens when an IAM token expires?

4. What are the four types of Cloud Audit Logs? Which are enabled by default, and which must be explicitly enabled?

5. Why would you use VPC Service Controls in addition to Private IP? What specific attack does VPC-SC prevent that Private IP does not?

6. A BigQuery table contains a `ssn` column tagged with a `PII-High` policy tag. A user has `roles/bigquery.dataViewer` on the dataset but not the fine-grained reader role. What do they see when they query the `ssn` column?

7. What is the difference between an authorized view and row-level security in BigQuery? When would you use each?

8. A developer wants to store a Cloud SQL password in the application's Docker image environment variables. What do you recommend instead, and why?

9. Describe the envelope encryption pattern. Why is it used instead of encrypting data directly with the KEK?

10. What IAM role does an application service account need to run BigQuery queries? What two roles are typically required together?

---

## Section 8 — Certification Exam Alignment

Database security appears across multiple exam domains:

- **Section 1 (Design)**: Choosing encryption strategy, IAM role design, Private IP vs. public IP
- **Section 2 (Ingest and manage)**: IAM authentication, SSL configuration, secret management
- **Section 4 (Secure)**: All security features — exam dedicates a full domain to this
- **Section 5 (Monitor)**: Audit log setup, security monitoring, alert policies for auth failures

Expect 6–8 security-focused questions on the exam. Many will involve scenario-based
tradeoffs (e.g., "Which configuration meets both compliance and operational requirements?").

---

## Recommended Resources

- Cloud SQL security overview: cloud.google.com/sql/docs/postgres/security
- BigQuery column-level security: cloud.google.com/bigquery/docs/column-level-security
- VPC Service Controls overview: cloud.google.com/vpc-service-controls/docs/overview
- Cloud KMS overview: cloud.google.com/kms/docs/overview
- Cloud Audit Logs: cloud.google.com/logging/docs/audit

---

Module 13 Reading Guide — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
