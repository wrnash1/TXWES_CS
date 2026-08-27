# Lab Activity: Module 13 — Database Security

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Lab Overview

**Title**: Securing a Cloud SQL Instance — Encryption, IAM Auth, Audit Logging, and VPC Controls

**Estimated Time**: 90 minutes

**Difficulty**: Intermediate

In this lab you will harden a Cloud SQL for PostgreSQL instance using CMEK encryption,
configure IAM database authentication, enable and query audit logs, and verify SSL mode
enforcement. You will also create an authorized BigQuery view to demonstrate column-level
access control.

---

## Prerequisites

- Active GCP project with billing enabled
- Cloud SQL Admin API, Cloud KMS API, BigQuery API, and Secret Manager API enabled
- Owner or Cloud SQL Admin + BigQuery Admin roles
- Cloud Shell access

---

## Lab Objectives

By the end of this lab, you will be able to:

1. Create a Cloud KMS key and configure CMEK for a Cloud SQL instance
2. Enable IAM database authentication and connect using an IAM token
3. Configure and query Cloud Audit Logs for database connection events
4. Enforce SSL-only connections on Cloud SQL
5. Create a BigQuery authorized view to restrict column access

---

## Part 1 — CMEK Setup for Cloud SQL

### Step 1.1 — Create a Cloud KMS Key Ring and Key

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")

gcloud kms keyrings create lab13-keyring \
  --location=$REGION

gcloud kms keys create lab13-sql-key \
  --keyring=lab13-keyring \
  --location=$REGION \
  --purpose=encryption
```

### Step 1.2 — Grant Cloud SQL Service Account Access to the Key

```bash
gcloud kms keys add-iam-policy-binding lab13-sql-key \
  --keyring=lab13-keyring \
  --location=$REGION \
  --member="serviceAccount:service-${PROJECT_NUMBER}@gcp-sa-cloud-sql.iam.gserviceaccount.com" \
  --role="roles/cloudkms.cryptoKeyEncrypterDecrypter"
```

### Step 1.3 — Create a Cloud SQL Instance with CMEK

```bash
export KEY_NAME="projects/${PROJECT_ID}/locations/${REGION}/keyRings/lab13-keyring/cryptoKeys/lab13-sql-key"

gcloud sql instances create lab13-pg \
  --database-version=POSTGRES_15 \
  --region=$REGION \
  --tier=db-f1-micro \
  --disk-encryption-key=$KEY_NAME \
  --database-flags=cloudsql.iam_authentication=on
```

Wait for the instance to be created (approximately 3–5 minutes).

Verify the CMEK configuration:

```bash
gcloud sql instances describe lab13-pg \
  --format="value(diskEncryptionConfiguration.kmsKeyName)"
```

**Lab Question 1**: What would happen to the database data if you disabled the KMS
key version used for encryption? How would you re-enable access?

---

## Part 2 — IAM Database Authentication

### Step 2.1 — Create a Database and IAM User

Create the application database:

```bash
gcloud sql databases create lab13db --instance=lab13-pg
```

Create an IAM user mapped to your current Google identity:

```bash
# Get your current user email
export MY_EMAIL=$(gcloud config get-value account)

gcloud sql users create $MY_EMAIL \
  --instance=lab13-pg \
  --type=CLOUD_IAM_USER
```

### Step 2.2 — Install and Start the Cloud SQL Auth Proxy

```bash
# Download the Auth Proxy
curl -o cloud-sql-proxy \
  https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.6.0/cloud-sql-proxy.linux.amd64

chmod +x cloud-sql-proxy

# Start the proxy in the background
./cloud-sql-proxy --port=5432 ${PROJECT_ID}:${REGION}:lab13-pg &
export PROXY_PID=$!

echo "Proxy PID: $PROXY_PID"
```

### Step 2.3 — Connect Using an IAM Token

```bash
# Install PostgreSQL client if needed
sudo apt-get install -y postgresql-client 2>/dev/null

# Get a fresh IAM access token
export PGPASSWORD=$(gcloud auth print-access-token)

# Connect using your IAM identity
psql "host=127.0.0.1 port=5432 dbname=lab13db user=${MY_EMAIL} sslmode=disable"
```

Once connected, run these commands inside psql:

```sql
-- Verify your connected identity
SELECT current_user;

-- Create a test table
CREATE TABLE lab_data (
  id      SERIAL PRIMARY KEY,
  value   TEXT,
  created TIMESTAMP DEFAULT NOW()
);

-- Insert test data
INSERT INTO lab_data (value) VALUES ('test-row-1'), ('test-row-2'), ('test-row-3');

-- Verify
SELECT * FROM lab_data;

\q
```

**Lab Question 2**: What is the advantage of using an IAM token as the password rather
than a static password stored in a configuration file?

---

## Part 3 — SSL Enforcement

### Step 3.1 — Check Current SSL Mode

```bash
gcloud sql instances describe lab13-pg \
  --format="value(settings.ipConfiguration.sslMode)"
```

### Step 3.2 — Enforce SSL-Only Connections

```bash
gcloud sql instances patch lab13-pg \
  --ssl-mode=ENCRYPTED_ONLY
```

### Step 3.3 — Verify SSL Enforcement

Attempt a connection without SSL (should fail):

```bash
PGPASSWORD=$(gcloud auth print-access-token) \
psql "host=127.0.0.1 port=5432 dbname=lab13db user=${MY_EMAIL} sslmode=disable"
```

Note: Connections through the Auth Proxy are always encrypted regardless of the
instance SSL mode. To truly test SSL enforcement, you would connect directly to the
instance's public IP without the proxy.

**Lab Question 3**: What is the difference between `ENCRYPTED_ONLY` and
`TRUSTED_CLIENT_CERTIFICATE_REQUIRED`? When would you use each?

---

## Part 4 — Audit Logging

### Step 4.1 — Enable Data Access Audit Logs

Navigate to the GCP Console: IAM and Admin → Audit Logs.

Find **Cloud SQL** in the list and enable:

- DATA_READ
- DATA_WRITE

Click Save.

Alternatively, using gcloud:

```bash
gcloud projects get-iam-policy $PROJECT_ID > /tmp/policy.yaml
```

Open `/tmp/policy.yaml` in Cloud Shell editor and add the following section before
the `bindings:` line:

```yaml
auditConfigs:
- auditLogConfigs:
  - logType: DATA_READ
  - logType: DATA_WRITE
  service: cloudsql.googleapis.com
```

Then apply:

```bash
gcloud projects set-iam-policy $PROJECT_ID /tmp/policy.yaml
```

### Step 4.2 — Generate Connection Events

Reconnect to the database a few times to generate log entries:

```bash
for i in 1 2 3; do
  PGPASSWORD=$(gcloud auth print-access-token) \
  psql "host=127.0.0.1 port=5432 dbname=lab13db user=${MY_EMAIL} sslmode=disable" \
  -c "SELECT NOW();"
done
```

### Step 4.3 — Query Audit Logs in Cloud Logging

In the GCP Console, navigate to Logging → Log Explorer. Use this filter:

```text
resource.type="cloudsql_database"
logName=~"cloudaudit.googleapis.com"
resource.labels.database_id="${PROJECT_ID}:lab13-pg"
```

**Lab Question 4**: Find a connection event in the logs. What fields are present
in `protoPayload.authenticationInfo`? What IP address did the connection come from?

---

## Part 5 — BigQuery Authorized View

### Step 5.1 — Create Source Dataset and Table with PII

In the BigQuery console, run:

```sql
CREATE SCHEMA IF NOT EXISTS `lab13_source`;

CREATE OR REPLACE TABLE `lab13_source.customers` (
  customer_id  INT64,
  name         STRING,
  email        STRING,
  ssn          STRING,
  region       STRING,
  revenue      NUMERIC
);

INSERT INTO `lab13_source.customers` VALUES
  (1, 'Alice Smith', 'alice@example.com', '123-45-6789', 'Southwest', 5000.00),
  (2, 'Bob Jones',   'bob@example.com',   '987-65-4321', 'Midwest',   3200.00),
  (3, 'Carol Wu',    'carol@example.com', '555-12-3456', 'Northeast', 7800.00);
```

### Step 5.2 — Create the Analytics Dataset and Authorized View

```sql
CREATE SCHEMA IF NOT EXISTS `lab13_analytics`;

CREATE OR REPLACE VIEW `lab13_analytics.customers_safe` AS
SELECT
  customer_id,
  name,
  region,
  revenue
FROM `lab13_source.customers`;
```

In the BigQuery Console, navigate to `lab13_source` dataset → Sharing → Authorize Views.

Add `lab13_analytics.customers_safe` as an authorized view.

### Step 5.3 — Verify Access Isolation

Query the authorized view:

```sql
SELECT * FROM `lab13_analytics.customers_safe`;
```

Attempt to query the source table directly:

```sql
SELECT ssn FROM `lab13_source.customers`;
```

**Lab Question 5**: If a user has `roles/bigquery.dataViewer` on `lab13_analytics`
only, can they see the `ssn` column? Explain why or why not.

---

## Cleanup

```bash
# Stop the proxy
kill $PROXY_PID 2>/dev/null

# Delete Cloud SQL instance
gcloud sql instances delete lab13-pg --quiet

# Delete KMS key (disable it first)
gcloud kms keys versions disable 1 \
  --key=lab13-sql-key \
  --keyring=lab13-keyring \
  --location=$REGION
```

In BigQuery console, delete datasets `lab13_source` and `lab13_analytics`.

---

## Lab Deliverables

Submit a document containing:

1. Screenshot showing the CMEK key name on the Cloud SQL instance
2. Screenshot of a successful IAM-authenticated psql connection with `SELECT current_user` output
3. Answers to Lab Questions 1 through 5
4. Screenshot of at least one connection audit log entry showing `authenticationInfo`

---

## Grading Rubric

| Component | Points |
|---|---|
| CMEK instance created with KMS key verified | 20 |
| IAM auth connection successful and current_user correct | 20 |
| SSL enforcement demonstrated | 10 |
| Audit log entry captured and analyzed | 25 |
| Authorized view created and access isolation verified | 25 |
| **Total** | **100** |

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Row-Level Security Policy

1. On your Cloud SQL for PostgreSQL instance, enable row-level security on the `employees` table and create a policy that restricts each user to rows in their own department:

   ```sql
   ALTER TABLE employees ENABLE ROW LEVEL SECURITY;

   CREATE POLICY dept_isolation ON employees
     USING (department = current_setting('app.current_department'));
   ```

2. Create two test roles and grant them table access:

   ```sql
   CREATE ROLE analyst_finance;
   CREATE ROLE analyst_hr;
   GRANT SELECT ON employees TO analyst_finance, analyst_hr;
   ```

3. Test the policy by setting the session variable and querying as each role:

   ```sql
   SET ROLE analyst_finance;
   SET app.current_department = 'Finance';
   SELECT * FROM employees;
   -- Should return only Finance rows

   SET app.current_department = 'HR';
   SELECT * FROM employees;
   -- Should return only HR rows
   ```

4. Verify that a superuser bypasses RLS by default, then force the policy to apply to superusers using `ALTER TABLE employees FORCE ROW LEVEL SECURITY;` and re-test.

### Challenge 2: Least-Privilege Application Account Audit

1. List all database users and their privileges on the `orders` and `customers` tables:

   ```sql
   SELECT grantee, table_name, privilege_type
   FROM information_schema.role_table_grants
   WHERE table_name IN ('orders', 'customers')
   ORDER BY grantee, table_name, privilege_type;
   ```

2. Create a least-privilege application role that has only INSERT and SELECT on `orders` and SELECT-only on `customers`:

   ```sql
   CREATE ROLE app_readonly;
   GRANT SELECT ON customers TO app_readonly;
   GRANT SELECT, INSERT ON orders TO app_readonly;
   ```

3. Attempt operations that exceed this role's privileges (UPDATE, DELETE, DROP) and confirm each is rejected with a permission denied error.

4. Write a query against `pg_roles` and `pg_auth_members` that lists all roles that are members of the `app_readonly` role, to audit which accounts could use these privileges.

### Reflection Questions

1. In Challenge 1, you used `current_setting('app.current_department')` as the RLS policy filter. What is the security risk of this approach if an attacker controls the client session, and what is a more secure alternative using authenticated identity rather than a session variable?
2. In Challenge 2, you audited an application role's privileges. In a real DBA environment, how would you audit privilege creep — where accounts accumulate permissions over time — and what automated process would you put in place to detect when a role's privileges have changed since the last review?

---

Module 13 Lab — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
