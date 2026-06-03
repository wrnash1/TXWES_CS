# Quiz: Module 16 — Capstone Practice Exam

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This 20-question practice exam simulates the Google Cloud Professional Cloud Database Engineer certification exam. Take it under exam conditions: no notes, 40 minutes total (2 minutes per question). Each question is worth 5 points. Distractor analysis follows each question.

---

### Question 1

A global e-commerce company requires a relational database that serves transactions with strong consistency across North America, Europe, and Asia-Pacific simultaneously, with zero planned downtime. Which GCP database service is the correct choice?

- A) Cloud SQL for PostgreSQL with cross-region read replicas in each region
- B) AlloyDB with a read pool instance deployed in each region
- C) Cloud Spanner with a multi-region instance configuration
- D) BigQuery with regional dataset replication enabled

Correct Answer: C — Cloud Spanner multi-region instances use Paxos consensus replication across multiple regions, providing external strong consistency for globally distributed transactions with 99.999% availability. Cross-region operations are handled transparently by the Spanner architecture.

Distractor analysis: A is incorrect because Cloud SQL cross-region read replicas use asynchronous replication and require manual promotion; they cannot provide strong consistency for writes across multiple regions simultaneously. B is incorrect because AlloyDB is a single-region service — read pool instances are in the same region as the primary cluster and do not provide multi-region distribution. D is incorrect because BigQuery is an OLAP analytics service, not a transactional database; it does not support ACID transactions for operational workloads.

---

### Question 2

A Cloud Spanner table uses auto-incrementing integer primary keys. After launch, the team observes that all writes target a single Spanner split, creating a write hotspot. Which key design change eliminates the hotspot?

- A) Switch to UUID v4 primary keys to distribute writes randomly across all splits
- B) Add a secondary index on the auto-increment column to distribute index writes
- C) Increase the number of Spanner processing units to create more splits for the sequential range
- D) Enable Spanner's automatic key interleaving to spread hotspot writes across child tables

Correct Answer: A — Spanner splits data by key range. Sequential integer keys always insert at the top of the range, concentrating all writes on the split containing the highest values. UUID v4 keys are randomly distributed, spreading new inserts across all splits and eliminating the hotspot.

Distractor analysis: B is incorrect because a secondary index on the auto-increment column does not change the primary key distribution — all primary key writes still go to the same split. C is incorrect because adding nodes creates more splits, but all new rows with sequential keys still go to the split holding the highest key range, regardless of how many splits exist. D is incorrect because there is no "automatic key interleaving" feature in Spanner; interleaving is a schema design pattern for co-locating parent-child rows, not a hotspot remedy.

---

### Question 3

A team needs to migrate a PostgreSQL 14 database from AWS RDS to Cloud SQL for PostgreSQL with less than 60 seconds of application downtime. Which DMS configuration achieves this?

- A) A one-time DMS migration job with a 2-hour maintenance window for the full transfer
- B) A continuous DMS migration job with CDC replication running until replication lag drops below 5 seconds, then switching application connection strings during a brief write-stop
- C) `pg_dump` followed by `gcloud sql import` during an overnight maintenance window
- D) A Datastream CDC pipeline with no cutover — both databases remain active indefinitely

Correct Answer: B — Continuous DMS migration keeps the source and Cloud SQL target synchronized via CDC. When replication lag reaches near zero, the write-stop window is only as long as it takes the final lag to drain and connection strings to switch — well under 60 seconds for most workloads.

Distractor analysis: A is incorrect because a one-time migration requires the full dataset to be transferred during the maintenance window; for large databases this takes hours, far exceeding 60 seconds. C is incorrect because `pg_dump` requires the application to be stopped for the entire duration of the dump and restore, which for large databases takes hours. D is incorrect because Datastream is designed for ongoing CDC streaming to BigQuery or Cloud Storage for analytics, not for a database migration cutover.

---

### Question 4

A healthcare company's Cloud SQL instance stores PHI. The security team requires that if the encryption key is revoked, the data must become immediately inaccessible. Which encryption configuration achieves this?

- A) Google-managed encryption keys with quarterly automated rotation configured through Cloud Console
- B) SSL/TLS with `ENCRYPTED_ONLY` mode to ensure all data is encrypted in transit
- C) Customer-managed encryption keys (CMEK) via Cloud KMS — disabling the key version prevents Cloud SQL from decrypting the data files
- D) Customer-supplied encryption keys (CSEK) passed with each API call to encrypt at the request level

Correct Answer: C — CMEK uses Cloud KMS keys managed by the customer. Disabling or destroying the key version immediately prevents Cloud SQL from decrypting the database files — the data becomes cryptographically inaccessible. This is the standard mechanism for enforcing data destruction without physically deleting the data files.

Distractor analysis: A is incorrect because Google-managed keys are controlled by Google; the customer cannot revoke Google's access to GMEK keys. B is incorrect because SSL/TLS encrypts data in transit between the client and the server — it does not affect encryption of data at rest on disk. C is the correct mechanism. D is incorrect because CSEK is a Cloud Storage concept, not a Cloud SQL feature; Cloud SQL does not support customer-supplied encryption keys passed per API call.

---

### Question 5

A BigQuery table is partitioned by `order_date` and clustered by `region`. A query includes `WHERE region = 'Southwest'` but no `order_date` filter. What is BigQuery's behavior?

- A) BigQuery uses clustering to prune blocks within each partition but still opens and scans all partitions because there is no partition column filter
- B) BigQuery uses the `region` cluster column to skip all partitions that do not contain Southwest data
- C) BigQuery refuses to run the query because a partition filter is required by table configuration
- D) BigQuery automatically rewrites the query to infer a partition range from the cluster column value

Correct Answer: A — Partition pruning only operates on the partition column. Without a filter on `order_date`, BigQuery opens all partitions. Within each partition, clustering on `region` allows BigQuery to skip blocks that do not contain Southwest data. The result is reduced bytes scanned within partitions, but all partitions are still opened.

Distractor analysis: B is incorrect because clustering operates at the block level within partitions, not at the partition level. Clustering cannot eliminate entire partitions from the scan. C is incorrect because `require_partition_filter = true` is a table-level option that must be explicitly set; it is not enabled by default. D is incorrect because BigQuery does not infer partition ranges from clustering column values; partitioning and clustering are independent mechanisms.

---

### Question 6

An application service account needs to connect to Cloud SQL via the Auth Proxy and execute SELECT queries on a specific database. Which IAM configuration correctly applies the principle of least privilege?

- A) `roles/cloudsql.admin` on the project
- B) `roles/cloudsql.editor` on the Cloud SQL instance
- C) `roles/cloudsql.client` on the instance plus a SELECT grant in the database engine
- D) `roles/cloudsql.viewer` on the instance

Correct Answer: C — `roles/cloudsql.client` grants the minimum IAM permission required for the Auth Proxy to establish a connection. Database-level SELECT permissions are granted separately within the database engine (via `GRANT SELECT ON ... TO user`). This two-layer approach provides the minimum necessary access at each level.

Distractor analysis: A is incorrect because `roles/cloudsql.admin` grants full administrative rights to all Cloud SQL instances in the project — far exceeding what is needed for an application connection. B is incorrect because `roles/cloudsql.editor` allows modifying instance configuration and is not needed for a read-only application connection. D is incorrect because `roles/cloudsql.viewer` grants read-only access to instance metadata but does not include the permission to establish proxy connections.

---

### Question 7

A DMS continuous migration job shows `CDC IN PROGRESS` with replication lag steadily increasing over 4 hours. What is the most likely cause?

- A) DMS has a 4-hour job time limit and will terminate the migration automatically
- B) The source database's binary log is being purged before DMS can read it
- C) The Cloud SQL destination instance tier is too small to apply CDC events as fast as the source generates them
- D) Network bandwidth between the source and DMS is insufficient for the initial load phase

Correct Answer: C — Persistently and steadily increasing replication lag indicates the target cannot keep up with the source's write rate. The destination Cloud SQL instance's write throughput (IOPS and CPU for transaction application) is the bottleneck. Upgrading the destination tier resolves this.

Distractor analysis: A is incorrect because DMS continuous migration jobs have no built-in time limit. B is incorrect because if the binary log were purged, DMS would report an error and the CDC job would fail, not continue with increasing lag. D is incorrect because network bandwidth affects the initial full load phase; during CDC, the data volume is incremental. Steady lag increase during CDC points to target write throughput, not network bandwidth.

---

### Question 8

A view in the `reporting` dataset needs to read from a table in the `raw_pii` dataset. Reporting analysts must not have direct access to `raw_pii`. Which BigQuery feature enables this cross-dataset access?

- A) A row access policy on the `raw_pii` table that filters rows visible to reporting analysts
- B) An authorized view — add the view to the `raw_pii` dataset's authorized views list, granting the view access without passing that access to its users
- C) A materialized view with cross-dataset refresh configured to cache `raw_pii` data in `reporting`
- D) BigQuery Omni federated query from the `reporting` dataset to `raw_pii`

Correct Answer: B — Authorized views grant a specific view the right to read from a source dataset. Users of the view do not inherit source dataset access — they can only see what the view exposes. This is configured in the source dataset's (raw_pii) access settings, not the view's dataset.

Distractor analysis: A is incorrect because row access policies restrict which rows a user can see within a single dataset; they do not grant cross-dataset read access to a view. C is incorrect because materialized views cache query results but the access control mechanism for cross-dataset reads is still the authorized view pattern. D is incorrect because BigQuery Omni is for querying data in other clouds (AWS S3, Azure Blob); it is not a mechanism for intra-BigQuery cross-dataset access control.

---

### Question 9

A production Cloud SQL for PostgreSQL instance has `availability_type = REGIONAL`. During a scheduled maintenance event, what is the expected user impact?

- A) The instance is unavailable for 2–5 minutes while the primary instance restarts and applies the patch
- B) The instance fails over to the standby with a brief reconnection event; applications with connection retry logic experience under 60 seconds of disruption
- C) Maintenance is deferred until the next scheduled maintenance window with no user impact
- D) The standby is patched first with no impact; then the primary is patched during a separate 10-minute window

Correct Answer: B — For HA (REGIONAL) instances, Cloud SQL performs maintenance by triggering a failover to the standby. The standby is patched, then becomes the new primary. Applications experience the same brief reconnection event as a regular failover — typically under 60 seconds. Applications with connection retry logic reconnect automatically.

Distractor analysis: A is incorrect because REGIONAL HA instances do not restart the primary in place for maintenance; they use a failover-based approach to minimize downtime. C is incorrect because maintenance is not deferred indefinitely — it occurs during the configured maintenance window. D is incorrect because the sequence is failover-based, not a sequential two-step patch; the standby is promoted and the old primary becomes the new standby.

---

### Question 10

A Terraform configuration must prevent a BigQuery table from being deleted when a team member runs `terraform destroy`. Which configuration achieves this?

- A) `lifecycle { ignore_changes = [schema] }` — prevents schema drift from triggering recreation
- B) `deletion_protection = true` on the `google_bigquery_table` resource
- C) `lifecycle { prevent_destroy = true }` in the resource block
- D) `force_destroy = false` on the `google_bigquery_dataset` resource

Correct Answer: C — The Terraform meta-argument `lifecycle { prevent_destroy = true }` causes Terraform to return an error when any plan would result in destroying the resource, whether from `terraform destroy` or `terraform apply` operations that would delete the resource.

Distractor analysis: A is incorrect because `ignore_changes = [schema]` prevents Terraform from detecting and applying schema changes but does not prevent the resource from being destroyed. B is incorrect because `deletion_protection` is a Cloud SQL resource attribute, not a BigQuery table attribute; `google_bigquery_table` does not have a `deletion_protection` field. D is incorrect because `force_destroy = false` on the dataset prevents the dataset from being deleted when it still contains tables, but it does not prevent the table itself from being destroyed by Terraform.

---

### Question 11

An application connects to Cloud SQL for MySQL using static passwords stored in Secret Manager. The security team wants to eliminate static passwords entirely. Which feature replaces them?

- A) Cloud SQL SSL client certificates (mutual TLS) to authenticate the application without a password
- B) Cloud SQL IAM database authentication — the application authenticates using a short-lived IAM token derived from its service account identity
- C) A VPC Service Controls perimeter around the Cloud SQL instance that restricts which networks can connect
- D) Cloud Armor rules blocking connections from outside the corporate IP range

Correct Answer: B — Cloud SQL IAM database authentication allows applications to authenticate using a short-lived OAuth 2.0 token from the service account identity. No static password is needed. The token is obtained automatically from the metadata server in GCP compute environments and expires after a short period, eliminating the static credential.

Distractor analysis: A is incorrect because SSL client certificates authenticate the connection's transport-layer identity but still require a database user password for database-level authentication. C is incorrect because VPC Service Controls restricts which networks can call the Cloud SQL API but does not replace the database authentication mechanism. D is incorrect because Cloud Armor operates at the load balancer/HTTP layer and cannot filter database TCP connections.

---

### Question 12

A company needs to stream changes from an Oracle 19c on-premises database to BigQuery in near real-time for a live analytics dashboard. Which GCP service is designed for this use case?

- A) Database Migration Service with a continuous migration job targeting BigQuery
- B) Cloud Data Fusion with an Oracle-to-BigQuery pipeline template
- C) Datastream with Oracle as the source and BigQuery as the destination
- D) BigQuery Data Transfer Service with the Oracle connector

Correct Answer: C — Datastream is Google Cloud's serverless CDC replication service. It supports Oracle as a source, reads changes via Oracle LogMiner, and streams them directly to BigQuery in near real-time. It requires no server management and no custom code.

Distractor analysis: A is incorrect because DMS migrates data to Cloud SQL, AlloyDB, or AlloyDB for PostgreSQL targets — it does not support BigQuery as a migration destination. B is incorrect because Cloud Data Fusion is a batch/streaming ETL pipeline service that requires pipeline authoring; it is not purpose-built for CDC replication and requires more setup than Datastream. D is incorrect because BigQuery Data Transfer Service handles scheduled batch imports from SaaS applications; it does not provide near-real-time CDC from Oracle.

---

### Question 13

A BigQuery dataset must be stored exclusively within the European Union for GDPR compliance. At what point in the lifecycle must the EU data location be configured?

- A) It can be changed at any time using `ALTER SCHEMA SET OPTIONS (location = 'EU')`
- B) The location must be set at dataset creation; it cannot be changed after the dataset is created
- C) The location can be changed by Google support after submitting a GDPR compliance request
- D) The location is configured at the GCP project level and automatically applies to all datasets

Correct Answer: B — BigQuery dataset location is immutable after creation. The region or multi-region must be specified when the dataset is created. If the location needs to change, a new dataset must be created in the correct location and the data must be copied.

Distractor analysis: A is incorrect because `ALTER SCHEMA` in BigQuery can modify dataset-level options such as default table expiration, but location is not modifiable — it is set at creation only. C is incorrect because Google support does not provide a mechanism to change dataset location after creation; the data would need to be recreated. D is incorrect because GCP project location settings do not automatically configure BigQuery dataset locations; each dataset's location is set independently at creation.

---

### Question 14

A Cloud Monitoring alerting policy for Cloud SQL CPU utilization has a threshold of 80% and a duration condition of 5 minutes. CPU spikes to 90% for 3 minutes then drops to 50%. What happens?

- A) The alert fires because CPU exceeded the 80% threshold
- B) The alert does not fire because the condition was sustained for only 3 minutes, not the required 5 minutes
- C) The alert fires but is immediately resolved when CPU drops below 80%
- D) The alert fires on the first data point exceeding 80% regardless of the duration setting

Correct Answer: B — Cloud Monitoring alerting policies with a duration condition require the metric to continuously exceed the threshold for the full configured duration before the alert fires. A 3-minute spike that resolves before 5 minutes prevents the alert from firing. This design prevents alert storms from short-lived transient spikes.

Distractor analysis: A is incorrect because the duration condition (5 minutes) overrides immediate threshold-crossing behavior; the alert does not fire until the sustained condition is met. C is incorrect because the alert never fires in this scenario — the 5-minute sustained condition was not met, so there is no alert to resolve. D is incorrect because the duration parameter explicitly defines a sustained-condition requirement; it is not ignored.

---

### Question 15

An organization is migrating from Teradata (12 TB) to BigQuery. The team wants a fully managed, no-code solution. Which service is most appropriate?

- A) Database Migration Service — migrates relational databases to Cloud SQL and AlloyDB
- B) Datastream — streams CDC changes from databases to BigQuery
- C) Cloud Dataflow with a Teradata JDBC connector template requiring custom pipeline code
- D) BigQuery Data Transfer Service with the Teradata connector — managed migration with no custom code

Correct Answer: D — BigQuery Data Transfer Service provides a managed Teradata connector that handles schema mapping, data extraction, and loading into BigQuery. It requires no custom code and is designed for warehouse-to-warehouse migrations at this scale.

Distractor analysis: A is incorrect because DMS migrates to Cloud SQL, AlloyDB, or AlloyDB for PostgreSQL — it does not target BigQuery. B is incorrect because Datastream is for ongoing CDC replication, not one-time warehouse migrations; it also does not support Teradata as a source. C is incorrect because Dataflow with a JDBC connector requires writing and maintaining custom pipeline code, which violates the no-code requirement.

---

### Question 16

A Cloud SQL for PostgreSQL instance stores sensitive customer data. The compliance team requires that all executed SQL queries — including SELECT statements — be logged with the user identity and full query text. Which configuration achieves this?

- A) Enable Cloud SQL Data Access audit logs for DATA_READ events in Cloud Logging
- B) Enable the `pgaudit` extension with `pgaudit.log = 'read,write,ddl'` to log all SQL statements at the engine level
- C) Enable the `log_min_duration_statement = 0` database flag to log all queries above 0 milliseconds
- D) Enable Cloud SQL Insights with full query string capture to record all query text

Correct Answer: B — The `pgaudit` extension provides SQL-level audit logging for PostgreSQL. With `pgaudit.log = 'read,write,ddl'`, all SELECT, INSERT, UPDATE, DELETE, and DDL statements are logged with the executing user's identity and the full query text. These logs appear in Cloud Logging.

Distractor analysis: A is incorrect because Cloud SQL Data Access audit logs record API-level access events (which user called which Cloud SQL API) but do not capture the full SQL query text or individual DML/SELECT statements within a session. C is incorrect because `log_min_duration_statement = 0` logs all queries that take longer than 0 milliseconds to the PostgreSQL server log, but this does not include the user identity in a structured format and does not use pgaudit's structured audit log format required for compliance tooling. D is incorrect because Cloud SQL Insights captures performance metrics (CPU, latency) and normalized query patterns for performance analysis; it is not a security audit log and does not replace pgaudit for compliance logging.

---

### Question 17

A security team wants to prevent any Cloud SQL instance in their organization from being created with a public IP address. Which GCP mechanism enforces this requirement across all projects?

- A) A Cloud Monitoring alerting policy that detects public-IP Cloud SQL instances and notifies the security team
- B) An Organization Policy constraint (`constraints/sql.restrictPublicIp`) applied at the organization level
- C) A Terraform module that always sets `ipv4_enabled = false` — all teams are required to use the approved module
- D) A VPC firewall rule blocking inbound traffic on ports 5432 and 3306 from `0.0.0.0/0`

Correct Answer: B — Organization Policy constraints allow administrators to enforce configuration requirements across all projects in the organization. The `constraints/sql.restrictPublicIp` constraint prevents Cloud SQL instances from being created or modified to have a public IP address, regardless of who creates them.

Distractor analysis: A is incorrect because an alerting policy detects and reports violations after the fact; it does not prevent the public-IP instance from being created. B is the proactive enforcement mechanism. C is incorrect because requiring teams to use a Terraform module is a process control, not a technical enforcement. A team could create an instance manually via Console or gcloud without using the module. D is incorrect because a firewall rule blocks network traffic to the instance but does not prevent the instance from being created with a public IP. The IP is still assigned; traffic is just blocked at the network layer.

---

### Question 18

An AlloyDB cluster is experiencing read query latency that exceeds SLA during peak hours with 500 concurrent read queries. The primary instance handles writes. Which AlloyDB feature addresses read latency without modifying the primary instance configuration?

- A) Increase the primary instance machine type to a larger tier with more CPU and RAM
- B) Add read pool instances to the AlloyDB cluster and route read queries to the pool
- C) Enable the AlloyDB columnar cache on the primary instance for analytical read queries
- D) Create a cross-region replica in a region geographically closer to the read clients

Correct Answer: B — AlloyDB read pool instances are purpose-built for read scaling. Adding read pool instances distributes read query load horizontally. The primary instance's write workload is unaffected. Read queries are routed to the pool via the AlloyDB read endpoint.

Distractor analysis: A is incorrect because increasing the primary instance tier helps with write throughput and concurrent connection limits, but the question specifies not modifying the primary instance. B is the correct horizontal scaling approach. C is incorrect because the columnar cache accelerates analytical queries that benefit from columnar access on the primary instance, but it does not add read capacity for OLTP read queries and would be modifying the primary instance. D is incorrect because AlloyDB is a single-region service; cross-region replicas are not an AlloyDB feature (they are a Cloud SQL feature).

---

### Question 19

Terraform state for a production database infrastructure is stored locally on a developer's laptop. The developer leaves the company and the laptop is returned without the state file. What is the immediate operational risk?

- A) All GCP resources managed by the Terraform configuration are deleted because Terraform state controls resource lifecycle
- B) Other team members cannot run `terraform plan` or `terraform apply` because Terraform cannot determine the current infrastructure state without the state file
- C) Terraform automatically regenerates the state file from current GCP resource APIs without requiring the missing state
- D) The state file is backed up automatically in Google Cloud and can be retrieved from the Cloud Console

Correct Answer: B — Terraform state maps resource definitions to real GCP resource IDs. Without the state file, Terraform treats existing resources as unknown and would attempt to create new resources rather than managing the existing ones. `terraform plan` and `apply` produce incorrect results. State recovery requires using `terraform import` for each resource.

Distractor analysis: A is incorrect because Terraform does not delete GCP resources when the state file is missing; GCP resources continue running independently. Terraform only affects infrastructure when an explicit apply is run. C is incorrect because Terraform does not automatically reconstruct state from GCP APIs; `terraform refresh` updates values in an existing state file but cannot create a state file from scratch. D is incorrect because Terraform local state files are not backed up to GCP; this is a key reason why remote state backends (Cloud Storage bucket with versioning) are required for production team workflows.

---

### Question 20

A data analyst runs a BigQuery query and receives `Access Denied: User does not have bigquery.jobs.create permission`. The analyst has `roles/bigquery.dataViewer` on the target dataset. Which additional role resolves this error?

- A) `roles/bigquery.dataEditor` — adds INSERT, UPDATE, DELETE permissions to the dataset
- B) `roles/bigquery.admin` — grants full administrative access across all BigQuery resources
- C) `roles/bigquery.jobUser` — grants permission to create BigQuery query jobs at the project level
- D) `roles/bigquery.dataOwner` — full control over dataset contents and metadata

Correct Answer: C — `roles/bigquery.jobUser` grants `bigquery.jobs.create` at the project level, which is required to run queries in BigQuery. `roles/bigquery.dataViewer` controls which datasets and tables the user can read, but does not grant the ability to submit query jobs. Both roles are needed to run queries.

Distractor analysis: A is incorrect because `roles/bigquery.dataEditor` grants INSERT, UPDATE, DELETE rights on dataset contents but does not grant `bigquery.jobs.create`. B is incorrect because `roles/bigquery.admin` would resolve the error but violates the principle of least privilege — `jobUser` is the correct minimum role. D is incorrect because `roles/bigquery.dataOwner` grants full control over a dataset (including deleting it) but like `dataEditor` does not include `bigquery.jobs.create` at the project level.

---

Reference: cloud.google.com/learn
