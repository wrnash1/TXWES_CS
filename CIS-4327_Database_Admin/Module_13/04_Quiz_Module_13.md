# Quiz: Module 13 — Database Security

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A financial services company requires that database encryption keys be rotated quarterly and that the company — not Google — controls key access and rotation schedule. Which encryption option for Cloud SQL satisfies both requirements?

- A) Google-managed encryption keys (GMEK) with a quarterly rotation policy configured in the Cloud Console
- B) Customer-managed encryption keys (CMEK) using Cloud KMS, where the company manages the key ring, rotation schedule, and access policies
- C) Customer-supplied encryption keys (CSEK) passed with each API call to encrypt data in transit
- D) Transparent Data Encryption (TDE) configured at the PostgreSQL level through database flags

Correct Answer: B — CMEK uses Cloud KMS keys created and managed by the customer. The customer defines the key rotation schedule (quarterly in this case), controls IAM access to the key, and can revoke access by disabling or destroying the key. Google-managed keys rotate on Google's schedule and Google retains control over key access.

Distractor analysis: A is incorrect because GMEK is Google-managed — Google controls the rotation schedule and key access, not the customer. A customer cannot independently set a quarterly rotation policy for GMEK. C is incorrect because CSEK (customer-supplied encryption keys) is a Google Cloud Storage feature, not a Cloud SQL feature; Cloud SQL does not support CSEK. D is incorrect because Cloud SQL for PostgreSQL does not support TDE at the database level as a configuration option; encryption is implemented at the storage layer, not within PostgreSQL itself.

---

### Question 2

A Cloud SQL for PostgreSQL instance is configured with `ALLOW_UNENCRYPTED_AND_ENCRYPTED` SSL mode. A developer connects from a public network without specifying SSL. Which statement correctly describes what happens?

- A) The connection is blocked because Cloud SQL always enforces SSL regardless of the SSL mode setting
- B) The connection succeeds and data is transmitted in plaintext over the network
- C) The connection succeeds but query results are automatically encrypted before transmission by the server
- D) Cloud Audit Logs will flag this as a security policy violation and alert the security team

Correct Answer: B — `ALLOW_UNENCRYPTED_AND_ENCRYPTED` mode permits connections that do not use SSL/TLS. A developer connecting without SSL parameters successfully establishes an unencrypted connection, and all data — including query results, credentials, and PII — is transmitted in plaintext over the network. The correct security setting is `ENCRYPTED_ONLY` to enforce TLS for all connections.

Distractor analysis: A is incorrect because `ALLOW_UNENCRYPTED_AND_ENCRYPTED` explicitly allows unencrypted connections. Cloud SQL does not override the SSL mode setting. C is incorrect because Cloud SQL does not selectively encrypt query results before transmission when an unencrypted connection is established; the entire connection either uses TLS or does not. D is incorrect because Cloud Audit Logs record who connected and what they did, but they do not automatically alert on unencrypted connections or classify them as policy violations without a custom alerting policy.

---

### Question 3

An application running on Cloud Run needs to connect to a Cloud SQL instance. A security review requires that no static passwords, service account key files, or secrets are stored anywhere in the application environment. Which approach satisfies this requirement?

- A) Store the database password in a Secret Manager secret and grant the Cloud Run service account `roles/secretmanager.secretAccessor`
- B) Use Cloud SQL IAM database authentication with the Cloud Run service account identity — the service account token is short-lived and no key file is required
- C) Hard-code the password in an environment variable in the Cloud Run service definition
- D) Use the Cloud SQL Auth Proxy with a downloaded service account JSON key stored as a Cloud Run secret volume mount

Correct Answer: B — Cloud SQL IAM database authentication allows a GCP service account to authenticate to Cloud SQL using a short-lived OAuth 2.0 token derived from its identity. The Cloud Run service automatically provides its service account identity without requiring a key file, a password, or a stored secret. No static credential exists in the environment.

Distractor analysis: A is incorrect because while Secret Manager is more secure than hardcoding, it still stores a static password as a secret that can be read by the service account. The question requires no static passwords anywhere in the environment. B satisfies the requirement more completely because no static password exists at all. C is incorrect because hardcoding a password in an environment variable is a security anti-pattern and directly violates the requirement for no stored passwords. D is incorrect because using a downloaded service account JSON key stored as a volume mount is explicitly what the question prohibits — it is a stored key file in the application environment.

---

### Question 4

A team needs to audit which users queried a specific Cloud SQL for PostgreSQL table containing protected health information (PHI) over the past 30 days, including the exact SQL SELECT statements executed. Which combination of settings captures this data?

- A) Admin Activity audit logs (always on) combined with Cloud SQL slow query log
- B) Data Access audit logs enabled for Cloud SQL combined with the pgaudit extension configured with `pgaudit.log = 'read'`
- C) System Event audit logs combined with Cloud SQL error log
- D) Policy Denied audit logs combined with Cloud SQL general query log

Correct Answer: B — Data Access audit logs for Cloud SQL capture connection events at the GCP API level (who accessed what resource). The pgaudit extension, when enabled on Cloud SQL for PostgreSQL and configured with `pgaudit.log = 'read'`, logs the exact SQL statements executed, including SELECT queries against specific tables. Together these provide both the identity of the user and the exact SQL they ran.

Distractor analysis: A is incorrect because Admin Activity logs capture DDL operations (CREATE TABLE, ALTER TABLE) and instance-level administrative actions, not DML SELECT queries against table data. The slow query log captures queries that exceed a time threshold but does not capture all SELECT queries. C is incorrect because System Event logs record infrastructure-level maintenance operations (instance restarts, failovers) and do not capture SQL queries. D is incorrect because Policy Denied logs record VPC Service Controls access denials, not successful SQL query executions.

---

### Question 5

A data analyst has `roles/bigquery.dataViewer` on a BigQuery dataset. The company requires that the analyst never see the `credit_card_number` column in the `transactions` table. Which BigQuery security feature enforces this restriction at query time?

- A) A row access policy with a filter condition `WHERE credit_card_number IS NULL` applied to the analyst's identity
- B) Removing the `credit_card_number` column from the table schema and storing card numbers in a separate restricted table
- C) A Policy Tag applied to the `credit_card_number` column in Data Catalog, where the analyst does not have the `roles/datacatalog.categoryFineGrainedReader` role for that tag taxonomy
- D) Setting the `credit_card_number` column as `NULLABLE` in the BigQuery table schema

Correct Answer: C — BigQuery column-level security uses Policy Tags from Data Catalog. A Policy Tag is applied to a column and restricts who can read that column's values. Users with `dataViewer` on the dataset can see the column exists (in the schema) but queries return NULL or an error for that column unless the user also has `roles/datacatalog.categoryFineGrainedReader` for the relevant tag taxonomy.

Distractor analysis: A is incorrect because a row access policy filters which rows a user can see, not which columns. A filter on `credit_card_number IS NULL` would hide rows where the value is not null — not the column itself across all rows. B is incorrect because removing the column and storing it separately requires schema changes and application refactoring; Policy Tags achieve column-level restriction without schema changes. D is incorrect because `NULLABLE` means the column can store NULL values but does not restrict access to the column's data.

---

### Question 6

An organization implements a VPC Service Controls perimeter around their BigQuery project. A data engineer with `roles/bigquery.admin` on the project attempts to copy a dataset to a different GCP project that is outside the perimeter. What happens?

- A) The copy succeeds because the engineer has BigQuery admin rights which override VPC Service Controls
- B) The copy is blocked by VPC Service Controls regardless of the engineer's IAM permissions
- C) The copy is allowed because VPC Service Controls only restricts external internet access, not inter-project copies within GCP
- D) The copy is logged as a warning in Cloud Audit Logs but proceeds normally

Correct Answer: B — VPC Service Controls operates at the API layer, independently of IAM. A perimeter restricts which identities and networks can call the protected APIs. Even a user with `roles/bigquery.admin` cannot copy data to a project outside the perimeter — the copy API call is blocked by the perimeter policy. IAM controls what you can do within the perimeter; VPC-SC controls whether you can access the service from outside or copy data outside.

Distractor analysis: A is incorrect because VPC Service Controls and IAM are complementary security layers — both must allow an operation for it to succeed. High IAM permissions do not override VPC-SC perimeter restrictions. C is incorrect because VPC Service Controls restricts all API calls that cross the perimeter boundary, including inter-project copies within GCP, not just internet egress. D is incorrect because VPC Service Controls blocks the API call — it does not allow it while logging a warning.

---

### Question 7

A user queries a BigQuery table and sees `XXXXXX@company.com` instead of the real email address in the `contact_email` column. The user has `roles/bigquery.dataViewer` on the table. Which BigQuery Data Catalog masking function most likely produced this output?

- A) SHA256 — a cryptographic hash that produces a fixed-length hex string
- B) DEFAULT — replaces values with the column's data type default (empty string for STRING)
- C) EMAIL_MASK — replaces the local part of an email address with placeholder characters while preserving the domain
- D) LAST_FOUR_CHARACTERS — returns only the last four characters of the string value

Correct Answer: C — `EMAIL_MASK` is a BigQuery Data Catalog masking rule that replaces the local part (before the `@`) of an email address with `XXXXXX` while preserving the domain portion. The output `XXXXXX@company.com` is the signature output of `EMAIL_MASK`.

Distractor analysis: A is incorrect because SHA256 produces a 64-character hexadecimal hash string, not the `XXXXXX@domain.com` pattern. B is incorrect because the `DEFAULT` masking function replaces the value with the data type's default — an empty string `''` for STRING columns, not the `XXXXXX@domain.com` pattern. D is incorrect because `LAST_FOUR_CHARACTERS` returns the final four characters of the column value, which would produce `m.com` for a long email address, not `XXXXXX@company.com`.

---

### Question 8

Which Cloud SQL IAM role grants a service account the minimum permissions needed to connect to a Cloud SQL instance using the Cloud SQL Auth Proxy?

- A) `roles/cloudsql.admin` — full administrative access to all Cloud SQL resources
- B) `roles/cloudsql.editor` — ability to modify instance configuration and connect
- C) `roles/cloudsql.client` — permission to connect to Cloud SQL instances via the proxy without granting any data access rights
- D) `roles/cloudsql.viewer` — read-only access to instance metadata and connection capability

Correct Answer: C — `roles/cloudsql.client` is the minimum IAM role required for the Cloud SQL Auth Proxy to establish a connection to a Cloud SQL instance. It grants the ability to connect to instances but does not grant any database-level permissions (those are controlled by the database user account). This follows the principle of least privilege.

Distractor analysis: A is incorrect because `roles/cloudsql.admin` grants full administrative access including the ability to create, modify, and delete instances — far more than required for an application proxy connection. B is incorrect because `roles/cloudsql.editor` allows modifying instance configuration, which is unnecessary for a connection-only service account. D is incorrect because `roles/cloudsql.viewer` grants read-only access to instance metadata but does not include the permission to establish proxy connections to the instance.

---

### Question 9

A multi-tenant BigQuery analytics platform stores all tenants' data in a single shared table with a `tenant_id` column partitioning the data logically. Users from Tenant A must only see rows where `tenant_id = 'A'`. Which BigQuery feature most efficiently enforces this row-level restriction at query time without requiring changes to user queries?

- A) Authorized views — create one view per tenant filtered by `tenant_id` and grant each tenant access to their view
- B) Row access policies — define one policy per tenant that filters the table to rows where `tenant_id` matches the current user's assigned tenant
- C) Dataset-level IAM — grant each tenant read access to a separate dataset containing only their data
- D) Materialized views — create one materialized view per tenant with the `tenant_id` filter built into the view definition

Correct Answer: B — Row access policies in BigQuery allow you to define a filter condition per identity group. A policy such as `FILTER USING (tenant_id = SESSION_USER())` or a policy tied to a group automatically restricts visible rows without requiring users to modify their queries. The filter is applied transparently at query execution time.

Distractor analysis: A is incorrect because authorized views work for cross-dataset access control but require creating and maintaining one view per tenant. For hundreds of tenants, this is operationally unscalable. Row access policies centralize the tenant isolation logic. C is incorrect because separate datasets require copying or moving data per tenant, duplicating storage costs and creating synchronization complexity. D is incorrect because materialized views cache query results and refresh on a schedule; they are not designed for row-level access control and would require one view per tenant, similar to the authorized view approach.

---

### Question 10

A security auditor requests evidence that all administrative changes to Cloud SQL instances — creates, deletes, and configuration changes — over the past year have been captured in an audit log. Where would you find this data?

- A) Cloud SQL slow query logs in Cloud Logging — captures all queries including DDL changes
- B) Admin Activity audit logs in Cloud Logging — always enabled by default and retained for 400 days
- C) Data Access audit logs — provide the most detailed record of all activity but must be manually enabled for each service
- D) System Event logs — record all infrastructure-level operations including instance creates and deletes

Correct Answer: B — Admin Activity audit logs are always enabled for all GCP services and cannot be disabled. They record all administrative operations (instance creation, deletion, configuration changes, user management). They are retained for 400 days in Cloud Logging by default, covering the past year requested by the auditor.

Distractor analysis: A is incorrect because Cloud SQL slow query logs capture SQL queries that exceed a time threshold (for performance tuning purposes), not administrative API operations like instance creates or deletes. C is incorrect because Data Access audit logs must be manually enabled per resource type and service; they capture data access events (reads, writes) but are not the source for administrative configuration changes. Admin Activity logs cover the auditor's requirement. D is incorrect because System Event logs record Google-initiated infrastructure maintenance operations (live migrations, automated restarts) rather than customer-initiated administrative actions like instance creation or configuration changes.

---

Reference: cloud.google.com/learn
