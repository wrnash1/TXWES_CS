# Quiz: Module 14 - Multi-Cloud and Hybrid Database Strategies
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A large retailer has an on-premises Oracle database that serves its OLTP workload. The data engineering team wants to stream real-time transaction changes into BigQuery for operational analytics without modifying the source Oracle database or impacting its performance. Which GCP service is most appropriate?
A) Database Migration Service (DMS) with a continuous migration job targeting BigQuery.
B) Google Cloud Datastream configured with Oracle as the source and BigQuery as the destination.
C) Cloud SQL for PostgreSQL with a read replica that replicates from Oracle using DMS.
D) AlloyDB Omni deployed on-premises with a Dataflow pipeline streaming changes to BigQuery.
*   **Correct Answer:** B) Google Cloud Datastream configured with Oracle as the source and BigQuery as the destination.
*   **Distractor Analysis:**
    *   *Why B is correct:* Datastream is specifically designed for ongoing CDC-based replication from source databases (including Oracle, MySQL, PostgreSQL, SQL Server) to GCP destinations (BigQuery, Cloud Storage, Spanner). It is serverless, reads Oracle's redo logs without adding significant load to the source, and delivers changes to BigQuery in near-real time.
    *   *Why A is incorrect:* DMS is a migration tool designed for one-time or transitional migrations to Cloud SQL, AlloyDB, or Spanner. It does not target BigQuery as a destination and is not designed for ongoing, production-grade CDC streaming.
    *   *Why C is incorrect:* DMS can migrate Oracle to Cloud SQL for PostgreSQL, but this creates a relational Cloud SQL instance — not a streaming pipeline to BigQuery. A read replica from a Cloud SQL instance also cannot replicate from Oracle.
    *   *Why D is incorrect:* AlloyDB Omni is a self-managed PostgreSQL-compatible database engine for non-GCP environments; it is not a CDC streaming tool and cannot read from Oracle.

---

---

**Question 2**
A global e-commerce company needs a database that can serve transactional read and write queries from users in North America, Europe, and Asia simultaneously with strong consistency guarantees and 99.999% availability. No single GCP region can satisfy the SLA. Which service and configuration is most appropriate?
A) Cloud SQL for PostgreSQL with HA enabled in `us-central1` and cross-region read replicas in `europe-west1` and `asia-east1`.
B) Cloud Spanner with a multi-region instance configuration spanning North America, Europe, and Asia.
C) Firestore in Native mode with multi-region configuration set to `nam5` (US) as the primary.
D) BigQuery with a multi-region dataset in `US` and federated queries from regional Cloud SQL instances.
*   **Correct Answer:** B) Cloud Spanner with a multi-region instance configuration spanning North America, Europe, and Asia.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cloud Spanner multi-region configurations synchronously replicate data across multiple GCP regions, providing automatic failover and 99.999% availability even if an entire region fails. It maintains external consistency (strong ACID) for all transactions regardless of which region a client connects to — exactly matching the requirements.
    *   *Why A is incorrect:* Cloud SQL cross-region read replicas use asynchronous replication (non-zero RPO) and cannot serve writes; only the primary region handles writes. This does not provide the strong consistency or the multi-region write capability described.
    *   *Why C is incorrect:* Firestore is a document database without SQL transactions; it does not support the relational OLTP transactional model implied by the scenario. The `nam5` multi-region configuration also does not span Europe and Asia simultaneously.
    *   *Why D is incorrect:* BigQuery is an analytics data warehouse, not an OLTP transactional database. It does not serve sub-second transactional reads and writes for e-commerce applications.

---

---

**Question 3**
A database administrator needs to **grant read-only access to a cross-region Cloud SQL read replica for a regional reporting service account**. Which approach is most appropriate?
A) Connect to the read replica and run `GRANT SELECT ON ALL TABLES IN SCHEMA public TO reporting_sa;` after authenticating with a superuser account.
B) Assign the `roles/cloudsql.viewer` IAM role to the service account on the Cloud SQL instance's parent project.
C) Connect to the read replica and run `REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC; GRANT SELECT ON ALL TABLES IN SCHEMA public TO reporting_sa;`.
D) Configure the Cloud SQL instance to use IAM database authentication and grant the service account the `cloudsql.instances.connect` permission.
*   **Correct Answer:** A) Connect to the read replica and run `GRANT SELECT ON ALL TABLES IN SCHEMA public TO reporting_sa;` after authenticating with a superuser account.
*   **Distractor Analysis:**
    *   *Why A is correct:* Database-level read access for a specific schema is granted using SQL DCL (`GRANT SELECT`). The IAM role controls the ability to connect at the GCP platform level; the SQL GRANT controls which data the connected identity can read. Both layers are needed for a complete least-privilege configuration.
    *   *Why B is incorrect:* `roles/cloudsql.viewer` is an IAM role that grants access to view Cloud SQL instance *metadata* (configuration, flags, metrics) in the Cloud Console. It does not grant the ability to connect to the database or read data from tables.
    *   *Why C is incorrect:* `REVOKE ALL ... FROM PUBLIC` is a valid hardening step but is separate from granting access to the specific service account. The combination described is incomplete; you need to also grant `CONNECT` on the database before granting schema permissions.
    *   *Why D is incorrect:* IAM database authentication with `cloudsql.instances.connect` permission grants the service account the ability to authenticate a database connection using IAM credentials, but does not grant any SQL object privileges (read access to tables). Without a subsequent `GRANT SELECT`, the connected user would have no data access.

---

**Question 4**
An organization is designing a disaster recovery architecture for its Cloud Spanner database. The current Spanner instance is configured as a single-region instance in `us-central1`. The DR requirement is RPO = 0 and RTO < 30 seconds for a regional failure. Which change satisfies this requirement?
A) Add a Cloud Spanner multi-region instance configuration (e.g., `nam6`) that synchronously replicates to `us-east1` and `us-west1` in addition to `us-central1`.
B) Create a Cloud SQL cross-region read replica in `us-east1` as a DR target for the Spanner database.
C) Enable automated backups on the Spanner instance with a cross-region export to Cloud Storage in `us-east1`.
D) Increase the Spanner instance's node count to 5 to improve failover performance within `us-central1`.
*   **Correct Answer:** A) Add a Cloud Spanner multi-region instance configuration (e.g., `nam6`) that synchronously replicates to `us-east1` and `us-west1` in addition to `us-central1`.
*   **Distractor Analysis:**
    *   *Why A is correct:* Cloud Spanner multi-region configurations use synchronous Paxos replication across multiple regions. If `us-central1` fails completely, Spanner automatically re-elects a leader in another replica region within seconds, providing RPO = 0 (no data loss because replication is synchronous) and RTO < 30 seconds (automatic failover). No manual intervention is required.
    *   *Why B is incorrect:* Cloud SQL read replicas are not applicable to a Cloud Spanner database. Cloud SQL and Cloud Spanner are entirely separate services with different replication mechanisms.
    *   *Why C is incorrect:* Automated backups exported to Cloud Storage represent the state at backup time. Restoring from a backup does not achieve RPO = 0 (data written after the last backup is lost) or RTO < 30 seconds (restore operations take significantly longer).
    *   *Why D is incorrect:* Adding nodes to a single-region Spanner instance increases throughput within that region but does not provide any protection against a regional failure; all nodes in a single-region configuration are in the same region.

---

**Question 5**
When designing a hybrid architecture where an on-premises PostgreSQL database replicates changes to Cloud SQL for PostgreSQL via a VPN tunnel, you must mitigate the risk of **the VPN tunnel going down and the on-premises database falling significantly out of sync with the Cloud SQL replica before the tunnel is restored**. Which control best addresses this risk?
A) Configure Cloud Monitoring to alert when the Cloud SQL replication lag metric (`cloudsql.googleapis.com/database/replication/replica_lag`) exceeds a threshold, and establish an operational runbook for re-syncing the replica when the VPN is restored.
B) Enable HA on the Cloud SQL replica instance to ensure the standby takes over replication if the primary VPN connection fails.
C) Increase the VPN tunnel bandwidth to reduce the risk of replication delays during high write periods.
D) Configure the on-premises PostgreSQL to use synchronous replication commit mode to block writes if the VPN tunnel is unavailable.
*   **Correct Answer:** A) Configure Cloud Monitoring to alert when the Cloud SQL replication lag metric exceeds a threshold, and establish an operational runbook for re-syncing the replica when the VPN is restored.
*   **Distractor Analysis:**
    *   *Why A is correct:* Monitoring replication lag and alerting when it exceeds an acceptable threshold ensures the operations team is immediately notified when the VPN goes down or degrades. An operational runbook for re-syncing the replica (using `pg_basebackup` or a DMS re-sync job) when connectivity is restored limits the maximum out-of-sync window to the alert response time.
    *   *Why B is incorrect:* Cloud SQL HA provides a standby in a different zone within GCP for Cloud SQL instance zone failures; it has no mechanism to keep a replica in sync with an on-premises source when the VPN tunnel is unavailable. HA is for GCP-side failures, not for external connectivity failures.
    *   *Why C is incorrect:* Higher VPN bandwidth reduces replication lag under normal conditions but does not prevent the replication stream from stopping when the tunnel goes down entirely. Bandwidth is not the failure mode being addressed.
    *   *Why D is incorrect:* Configuring synchronous commit mode on the on-premises PostgreSQL would cause all writes to block indefinitely when the VPN is unavailable, which creates a denial-of-service condition on the primary production database — an unacceptable trade-off for a production system.
