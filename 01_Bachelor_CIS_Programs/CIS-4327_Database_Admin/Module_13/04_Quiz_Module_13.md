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

---

### Question 11 (5 points)

A PostgreSQL DBA wants to restrict users in the `analyst_role` to only see rows in the `employees` table where `department = 'Finance'`. Which PostgreSQL feature enforces this transparently without requiring analysts to modify their queries?

A) Row-Level Security (RLS) with a policy `USING (department = 'Finance')` applied to `analyst_role`.
B) A view that filters `WHERE department = 'Finance'` with `GRANT SELECT` to `analyst_role`.
C) A `CHECK` constraint on the `department` column restricting values to `'Finance'`.
D) A `BEFORE SELECT` trigger that raises an exception for non-Finance rows.

**Correct Answer:** A

**Distractor Analysis:**

- B) A view requires analysts to query the view instead of the base table; if they have access to the table directly, they can bypass the view. RLS is enforced at the table level regardless of how the query reaches the table.
- C) A `CHECK` constraint validates values during INSERT/UPDATE; it does not restrict which rows are visible to specific roles during SELECT queries.
- D) PostgreSQL does not have `BEFORE SELECT` triggers; triggers fire on INSERT, UPDATE, DELETE, and TRUNCATE operations, not on SELECT statements.

---

### Question 12 (5 points)

A Cloud SQL for PostgreSQL instance uses the default `postgres` superuser account for all application connections. A security audit flags this as a violation of the principle of least privilege. What is the correct remediation?

A) Create a dedicated application database user with only the privileges required (e.g., SELECT, INSERT, UPDATE on specific tables) and update the application connection string.
B) Rename the `postgres` superuser to a less obvious name to reduce the attack surface.
C) Set a very long, complex password on the `postgres` account and rotate it monthly.
D) Disable remote connections for the `postgres` account in `pg_hba.conf`.

**Correct Answer:** A

**Distractor Analysis:**

- B) Renaming the superuser is security through obscurity; the account still has superuser privileges and a determined attacker using `pg_roles` can discover the new name.
- C) A strong password reduces brute-force risk but does not address the privilege problem; the application still has full superuser access when only SELECT/INSERT/UPDATE is needed.
- D) Disabling remote connections for `postgres` is a useful hardening step but does not create a least-privilege application account; the root issue is the use of superuser for application workloads.

---

### Question 13 (5 points)

A developer stores database credentials in a `.env` file committed to a Git repository. A security team discovers this in a code review. What is the correct remediation and prevention strategy?

A) Store credentials in Google Cloud Secret Manager, grant the application's service account `roles/secretmanager.secretAccessor`, and access secrets at runtime via the API — never commit secrets to version control.
B) Encrypt the `.env` file with AES-256 before committing it to the repository.
C) Use a private Git repository to restrict who can view the committed credentials.
D) Base64-encode the credentials in the `.env` file to obscure them from casual inspection.

**Correct Answer:** A

**Distractor Analysis:**

- B) Encrypting the `.env` file still puts a secret in version control; the encryption key itself becomes the secret that must be managed, and decrypting it at build time recreates the original problem.
- C) Private repositories do not prevent all employees, CI/CD pipelines, or attackers who gain repository access from reading the credentials; the secret is still in version history indefinitely.
- D) Base64 encoding is not encryption; it is trivially reversible with one command and provides no security protection.

---

### Question 14 (5 points)

Which Cloud SQL SSL mode setting enforces that all client connections must use TLS, rejecting any connection attempt without TLS?

A) `ALLOW_UNENCRYPTED_AND_ENCRYPTED`
B) `ENCRYPTED_ONLY`
C) `OPTIONAL_ENCRYPTED`
D) `SSL_REQUIRED_WITH_CERT_VERIFY`

**Correct Answer:** B

**Distractor Analysis:**

- A) `ALLOW_UNENCRYPTED_AND_ENCRYPTED` is the permissive default that accepts both encrypted and unencrypted connections; it does not enforce TLS.
- C) `OPTIONAL_ENCRYPTED` is not a valid Cloud SQL SSL mode name; the valid options are `ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `ENCRYPTED_ONLY`.
- D) `SSL_REQUIRED_WITH_CERT_VERIFY` is not a valid Cloud SQL SSL mode; certificate verification for mutual TLS is a separate configuration (requiring client certificates) layered on top of `ENCRYPTED_ONLY`.

---

### Question 15 (5 points)

A company uses pgaudit on Cloud SQL for PostgreSQL to log all DDL operations. After reviewing logs, they find that `pgaudit.log = 'ddl'` is capturing CREATE and DROP statements but not GRANT and REVOKE statements. What change is needed?

A) Add `'role'` to the `pgaudit.log` setting: `pgaudit.log = 'ddl, role'` — GRANT and REVOKE are role-related events logged under the `role` category.
B) Set `pgaudit.log = 'all'` to capture every possible event type.
C) Enable Data Access audit logs in the Cloud Console to supplement pgaudit DDL logs.
D) Run `GRANT` and `REVOKE` statements as superuser to ensure they appear in the DDL log.

**Correct Answer:** A

**Distractor Analysis:**

- B) Setting `pgaudit.log = 'all'` would capture everything including every SELECT and DML statement, generating enormous log volume and cost; targeted logging categories are the correct approach.
- C) Data Access audit logs capture GCP API-level access events, not PostgreSQL-internal privilege changes (GRANT/REVOKE); pgaudit is the correct tool for SQL-level privilege auditing.
- D) Running GRANT/REVOKE as superuser does not change their pgaudit category; GRANT and REVOKE are categorized as `role` events regardless of which user executes them.

---

### Question 16 (5 points)

A BigQuery dataset contains sensitive PII. An analyst's service account has `roles/bigquery.dataViewer` on the dataset. The security team wants to mask the `ssn` column so the analyst sees `***-**-XXXX` instead of the real value. Which BigQuery feature provides this?

A) Policy Tag on the `ssn` column with a Data Catalog masking rule assigning `LAST_FOUR_CHARACTERS` masking to the analyst's principal.
B) A row access policy on the `ssn` column filtering rows where `ssn IS NULL`.
C) An authorized view that replaces `ssn` with a static string `'***-**-XXXX'` for all rows.
D) Removing `roles/bigquery.dataViewer` and replacing it with a custom role that excludes the `ssn` column.

**Correct Answer:** A

**Distractor Analysis:**

- B) Row access policies control which rows are visible, not column value masking; filtering on `ssn IS NULL` would hide rows without a null SSN, not mask the column value.
- C) An authorized view can mask columns but requires the analyst to query the view directly; Policy Tags with masking rules apply transparently to the base table without requiring users to change their query target.
- D) Custom IAM roles control resource-level access but cannot enforce column-level value masking within BigQuery; Policy Tags are the purpose-built mechanism for this requirement.

---

### Question 17 (5 points)

An organization needs to ensure that Cloud SQL backups cannot be accessed or deleted by anyone — including project owners — unless two authorized security officers approve the request. Which Google Cloud feature enforces this four-eyes principle for backup deletion?

A) VPC Service Controls perimeter around the Cloud SQL project.
B) Cloud KMS key destruction with a 24-hour scheduled deletion window.
C) Access Approval — requires explicit approval from designated approvers before Google or privileged users can access or modify protected resources.
D) Binary Authorization requiring signed attestations before any Cloud SQL operation.

**Correct Answer:** C

**Distractor Analysis:**

- A) VPC Service Controls restricts which networks and identities can call APIs; it does not implement a multi-person approval workflow for specific operations.
- B) Cloud KMS scheduled key destruction is a protection for encryption keys, not a general-purpose approval workflow for Cloud SQL backup operations.
- D) Binary Authorization controls which container images can be deployed to GKE based on attestations; it is not applicable to Cloud SQL backup operations.

---

### Question 18 (5 points)

A DBA needs to grant a reporting service account read-only access to a specific BigQuery table without granting access to the entire dataset. Which IAM binding achieves this at the minimum required scope?

A) Grant `roles/bigquery.dataViewer` on the specific table resource, not the dataset.
B) Grant `roles/bigquery.dataViewer` on the dataset and use a row access policy to restrict to specific rows.
C) Grant `roles/bigquery.admin` at the project level and rely on the application to only read the allowed table.
D) Grant `roles/bigquery.dataViewer` at the project level to ensure the service account can access all tables.

**Correct Answer:** A

**Distractor Analysis:**

- B) Granting `dataViewer` at the dataset level provides access to all tables in the dataset, not just the specific one; row access policies control row visibility, not table access.
- C) Granting `bigquery.admin` at the project level violates the principle of least privilege and provides far more access than needed, including the ability to delete tables and modify schemas.
- D) Project-level `dataViewer` grants access to all datasets and tables in the project; table-level grants are the correct minimum scope for single-table access.

---

### Question 19 (5 points)

A security team enables Cloud Audit Logs Data Access logging for BigQuery at the organization level. After one week, they discover the logs are costing more than expected. Which Data Access log type is most likely generating the highest volume and cost?

A) Admin Activity logs — capturing all DDL changes.
B) DATA_READ logs — capturing every BigQuery SELECT query including all analyst exploratory queries.
C) POLICY_DENIED logs — capturing all IAM permission denials.
D) DATA_WRITE logs — capturing all INSERT, UPDATE, and DELETE operations.

**Correct Answer:** B

**Distractor Analysis:**

- A) Admin Activity logs are always on but only capture administrative operations (dataset creation, IAM changes, etc.); in an analytics organization, DDL changes are infrequent and generate low log volume.
- C) POLICY_DENIED logs are a separate log type for VPC Service Controls access denials; they generate entries only when access is blocked, not on every query.
- D) DATA_WRITE logs capture DML writes; in a read-heavy analytics organization, write volume is far lower than read volume from analyst SELECT queries.

---

### Question 20 (5 points)

Which PostgreSQL mechanism allows a superuser to define a security barrier that prevents a user-defined function in a `WHERE` clause from seeing row values before the security policy filter is applied?

A) `CREATE VIEW ... WITH (security_barrier = true)` — prevents the view's WHERE clause from leaking row values to functions called in the outer query.
B) `CREATE FUNCTION ... SECURITY DEFINER` — runs the function as its owner rather than the caller.
C) `SET row_security = on` — enables row security globally for all tables.
D) `GRANT EXECUTE ON FUNCTION ... TO PUBLIC` — restricts function execution to specific roles.

**Correct Answer:** A

**Distractor Analysis:**

- B) `SECURITY DEFINER` changes which user's privileges the function runs under; it does not prevent the function from seeing rows that should be filtered by a security policy.
- C) `SET row_security = on` enables row-level security enforcement for the session, but it does not specifically address the security barrier issue of functions in WHERE clauses seeing pre-filter row values.
- D) `GRANT EXECUTE` controls who can call the function; revoking public execute access limits who runs the function but does not prevent it from seeing pre-filter values when executed by an authorized user.
