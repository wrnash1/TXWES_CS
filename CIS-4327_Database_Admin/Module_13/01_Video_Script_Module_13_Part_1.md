# Video Script: Module 13 — Database Security (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Welcome and Module Overview

Welcome to Module 13 of CIS-4327. I'm Professor Nash, and in this module we cover
database security on Google Cloud Platform. Security is consistently one of the most
heavily tested topics on the Google Cloud Professional Database Engineer exam.

In Part 1 we cover:

- Encryption at rest and in transit for GCP databases
- Cloud SQL IAM database authentication
- Database audit logging with Cloud Logging

In Part 2 we cover:

- VPC Service Controls for databases
- Data masking and column-level security in BigQuery
- Security architecture and the principle of defense in depth

Let's get started.

---

## SLIDE 2 — Security Fundamentals: The Defense-in-Depth Model

Before diving into specific features, it's important to understand the layered security
model that GCP databases use. Defense in depth means applying security controls at
multiple layers so that a failure at one layer does not expose data.

The layers for GCP databases are:

1. **Network layer**: VPC isolation, Private IP, firewall rules, VPC Service Controls
2. **Identity layer**: IAM roles, Cloud SQL IAM authentication, service accounts
3. **Data layer**: Encryption at rest, encryption in transit, CMEK
4. **Application layer**: Column-level security, data masking, authorized views
5. **Audit layer**: Cloud Audit Logs, Data Access logs, query logs

For the exam, be able to identify which layer a specific security feature belongs to
and what threat it mitigates.

---

## SLIDE 3 — Encryption at Rest

All GCP databases encrypt data at rest by default. This means data stored on disk —
including backups, temporary files, and transaction logs — is encrypted before being
written to storage.

**Default encryption**: Google-managed encryption keys (GMEK). Google rotates keys
automatically. You have no management overhead, but Google controls the keys.

**Customer-managed encryption keys (CMEK)**: You provide a key stored in Cloud Key
Management Service (Cloud KMS). GCP uses your key to encrypt database data. You
control key rotation, and you can revoke access to the key at any time, effectively
making all encrypted data inaccessible.

**Customer-supplied encryption keys (CSEK)**: For Cloud Storage and some Compute
Engine use cases (not standard for Cloud SQL or BigQuery), you supply the raw key
bytes with each API call. GCP never stores your key.

For the exam, know that CMEK provides the strongest organizational control for
regulated industries (finance, healthcare, government), and that revoking a CMEK
key in Cloud KMS immediately prevents GCP services from decrypting the data.

---

## SLIDE 4 — Configuring CMEK for Cloud SQL

To enable CMEK on a Cloud SQL instance:

Step 1 — Create a key ring and key in Cloud KMS:

```bash
gcloud kms keyrings create sql-keyring \
  --location=us-central1

gcloud kms keys create sql-key \
  --keyring=sql-keyring \
  --location=us-central1 \
  --purpose=encryption
```

Step 2 — Grant the Cloud SQL service account access to use the key:

```bash
gcloud kms keys add-iam-policy-binding sql-key \
  --keyring=sql-keyring \
  --location=us-central1 \
  --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloud-sql.iam.gserviceaccount.com" \
  --role="roles/cloudkms.cryptoKeyEncrypterDecrypter"
```

Step 3 — Create the Cloud SQL instance referencing the key:

```bash
gcloud sql instances create my-instance \
  --database-version=POSTGRES_15 \
  --region=us-central1 \
  --disk-encryption-key=projects/PROJECT_ID/locations/us-central1/keyRings/sql-keyring/cryptoKeys/sql-key
```

Important: Once a Cloud SQL instance is created with CMEK, you cannot switch it to
GMEK or to a different key. Plan your key hierarchy before creating production instances.

---

## SLIDE 5 — Encryption in Transit

Encryption in transit protects data moving between clients and GCP database services.

**Cloud SQL**:

- SSL/TLS is supported on all Cloud SQL instances (MySQL, PostgreSQL, SQL Server).
- You can configure SSL mode at the instance level:
  - `ALLOW_UNENCRYPTED_AND_ENCRYPTED`: Both SSL and non-SSL connections accepted.
  - `ENCRYPTED_ONLY`: Only SSL connections accepted.
  - `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`: Client certificate verification required
    (mutual TLS / mTLS).
- The Cloud SQL Auth Proxy automatically handles SSL certificate management,
  so applications using the proxy do not need to manage certificates manually.

**BigQuery**:

- All connections to BigQuery are over HTTPS (TLS 1.2 or 1.3). This is enforced
  automatically and cannot be disabled.

**Cloud Spanner**:

- All API calls use TLS. Spanner does not support direct TCP connections.

**Bigtable**:

- Client library connections use TLS. Enforced by default.

For the exam: know the Cloud SQL SSL modes and when each is appropriate. The
`TRUSTED_CLIENT_CERTIFICATE_REQUIRED` mode is the strongest and is required for
compliance scenarios where you need to verify that only specific clients can connect.

---

## SLIDE 6 — Cloud SQL IAM Database Authentication

Traditional database authentication uses a username and password stored in the
database engine. Cloud SQL IAM database authentication replaces passwords with
Google Cloud IAM identity tokens, eliminating the need to manage database-level
passwords.

How it works:

1. A GCP identity (user or service account) is granted the
   `roles/cloudsql.instanceUser` IAM role on the Cloud SQL instance.
2. The identity is also mapped to a database user inside Cloud SQL with the
   `cloudsql_iam_authentication` flag enabled (PostgreSQL) or equivalent (MySQL).
3. When connecting, the client uses a short-lived IAM access token as the password.
   The token is obtained from the metadata server or gcloud CLI automatically.
4. Cloud SQL validates the token against IAM and grants or denies the connection.

Benefits:

- **No password rotation**: Tokens are short-lived (1 hour). No password database to
  maintain or leak.
- **Centralized access control**: Adding or revoking database access is done via IAM,
  the same system used for all other GCP resources.
- **Audit trail**: All logins are recorded in Cloud Audit Logs with the IAM identity
  of the connecting user.

---

## SLIDE 7 — Configuring IAM Authentication on Cloud SQL (PostgreSQL)

Enabling IAM authentication at the instance level:

```bash
gcloud sql instances patch my-pg-instance \
  --database-flags=cloudsql.iam_authentication=on
```

Creating a database user linked to an IAM identity:

```bash
# For a human user:
gcloud sql users create user@company.com \
  --instance=my-pg-instance \
  --type=CLOUD_IAM_USER

# For a service account:
gcloud sql users create myapp@project.iam.gserviceaccount.com \
  --instance=my-pg-instance \
  --type=CLOUD_IAM_SERVICE_ACCOUNT
```

Inside PostgreSQL, grant the user access to a database:

```sql
GRANT CONNECT ON DATABASE mydb TO "user@company.com";
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA public TO "user@company.com";
```

Connecting using the Cloud SQL Auth Proxy with IAM authentication:

```bash
cloud-sql-proxy --port=5432 PROJECT:REGION:INSTANCE &
PGPASSWORD=$(gcloud auth print-access-token) psql \
  -h 127.0.0.1 -U user@company.com -d mydb
```

The proxy handles SSL automatically. The access token acts as the password.

---

## SLIDE 8 — Cloud Audit Logs for Databases

Cloud Audit Logs records who did what, where, and when across all GCP services.
For databases, audit logging is critical for compliance (SOC 2, HIPAA, PCI DSS,
GDPR) and for incident investigation.

GCP provides four audit log types:

1. **Admin Activity logs** (always on, free): Records administrative operations —
   creating/deleting instances, modifying configurations, changing IAM policies.

2. **Data Access logs** (off by default, chargeable): Records data reads (who read
   which data) and data writes at the API level. For Cloud SQL, this includes
   `cloudsql.instances.connect` events.

3. **System Event logs** (always on, free): Records GCP-initiated maintenance events
   such as automatic failover or instance restarts.

4. **Policy Denied logs** (always on, free): Records when IAM policies deny access.

---

## SLIDE 9 — Enabling Data Access Audit Logs

Data Access logs must be explicitly enabled because they can generate large volumes
of log data and incur Cloud Logging ingestion charges.

To enable Data Access logs for Cloud SQL via the GCP console:

1. Navigate to IAM and Admin → Audit Logs.
2. Find `Cloud SQL` in the service list.
3. Check `DATA_READ`, `DATA_WRITE`, and `ADMIN_READ` as needed.
4. Click Save.

Using gcloud (via Organization Policy or IAM policy):

```bash
gcloud projects get-iam-policy PROJECT_ID > policy.yaml
# Edit policy.yaml to add auditConfigs section:
# auditConfigs:
# - auditLogConfigs:
#   - logType: DATA_READ
#   - logType: DATA_WRITE
#   service: cloudsql.googleapis.com
gcloud projects set-iam-policy PROJECT_ID policy.yaml
```

Querying audit logs in Cloud Logging:

```
resource.type="cloudsql_database"
logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"
protoPayload.methodName="cloudsql.instances.connect"
```

---

## SLIDE 10 — Database Query Logging

Beyond API-level audit logs, you can enable query-level logging within the database
engine itself.

**Cloud SQL for PostgreSQL** — `pgaudit` extension:

```sql
-- Enable pgaudit
CREATE EXTENSION pgaudit;

-- Set audit logging in postgresql.conf via instance flags:
-- pgaudit.log = 'read,write,ddl'
-- pgaudit.log_catalog = off
-- pgaudit.log_level = log
```

With `pgaudit` enabled, every SELECT, INSERT, UPDATE, DELETE, and DDL statement is
logged to Cloud Logging. These logs capture the full SQL text, the executing user,
and the affected database and table.

**Cloud SQL for MySQL** — General query log:

```bash
gcloud sql instances patch my-mysql-instance \
  --database-flags=general_log=on
```

**BigQuery** — All queries are automatically logged to:

- `INFORMATION_SCHEMA.JOBS_BY_PROJECT` (queryable with SQL)
- Cloud Audit Logs (Data Access logs, if enabled)

BigQuery audit logs include the full query text, the user's email, bytes processed,
and job duration — everything you need for a cost and compliance audit.

---

## SLIDE 11 — Key Exam Points for Part 1

Let's summarize the key exam topics from Part 1:

- **Encryption at rest**: GMEK (default), CMEK (KMS-managed), CSEK (user-supplied). CMEK
  allows key revocation to render data inaccessible.
- **Cloud SQL SSL modes**: ALLOW_UNENCRYPTED_AND_ENCRYPTED, ENCRYPTED_ONLY,
  TRUSTED_CLIENT_CERTIFICATE_REQUIRED. The proxy handles SSL automatically.
- **IAM database auth**: Replaces passwords with short-lived IAM tokens.
  Managed via `roles/cloudsql.instanceUser` + database user mapping.
- **Audit logs**: Admin Activity (always on), Data Access (must enable), System Event,
  Policy Denied. Data Access logs record who read/wrote what.
- **pgaudit**: Query-level logging extension for PostgreSQL on Cloud SQL.

In Part 2 we cover VPC Service Controls for database isolation, data masking, and
column-level security in BigQuery.

---

*End of Part 1 Script*
