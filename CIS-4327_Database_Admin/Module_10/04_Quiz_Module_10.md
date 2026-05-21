# Quiz: Module 10 - Backup, Recovery, and High Availability
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A business requires its Cloud SQL for PostgreSQL database to have a Recovery Time Objective (RTO) of under 60 seconds and a Recovery Point Objective (RPO) of zero for zone-level failures. Which configuration satisfies both requirements?
A) Enable automated backups with a 7-day retention window and PITR.
B) Enable High Availability (HA) on the Cloud SQL instance, which uses synchronous replication to a standby in a different zone.
C) Create a cross-region read replica in a different GCP region and configure the application to fail over manually.
D) Schedule hourly on-demand backups using the Cloud SQL Admin API.
*   **Correct Answer:** B) Enable High Availability (HA) on the Cloud SQL instance, which uses synchronous replication to a standby in a different zone.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cloud SQL HA uses synchronous replication — every write is committed to both the primary and the standby before being acknowledged (RPO ~0). Automatic failover completes in approximately 60 seconds (satisfying RTO < 60s). The IP address does not change, so applications reconnect without configuration changes.
    *   *Why A is incorrect:* Automated backups and PITR protect against data modification errors (logical corruption) but do not provide automatic failover for zone failures. Restoring from a backup typically takes minutes to hours, far exceeding a 60-second RTO.
    *   *Why C is incorrect:* Cross-region replicas use asynchronous replication (non-zero RPO due to replication lag) and require manual promotion (manual failover violates the automatic RTO requirement).
    *   *Why D is incorrect:* Hourly backups mean up to 60 minutes of potential data loss (RPO = 60 minutes) and require a restore operation that takes far longer than 60 seconds.

---

---

**Question 2**
A Cloud SQL for MySQL instance has both High Availability and automated backups enabled. A developer accidentally deletes a critical table containing 6 months of transaction data at 2:15 PM today. The table did not contain a `deleted_at` soft-delete column. How do you recover the deleted data?
A) Fail over to the HA standby instance, which will have the table intact.
B) Perform a Point-in-Time Recovery (PITR) to restore the database to a state just before 2:15 PM today.
C) Restore from the most recent automated backup taken this morning and accept the data loss since then.
D) Check the Cloud SQL read replica for the table, since replicas cache deletes for 24 hours.
*   **Correct Answer:** B) Perform a Point-in-Time Recovery (PITR) to restore the database to a state just before 2:15 PM today.
*   **Distractor Analysis:**
    *   *Why B is correct:* PITR allows restoration to any point within the retention window with second-level granularity. Restoring to 2:14 PM recovers the table and all its data, losing only a single minute of transactions rather than the entire day.
    *   *Why A is incorrect:* HA uses synchronous replication — the DROP TABLE statement was replicated instantly to the standby. The standby contains the same deletion. HA protects against hardware and zone failures, not against logical data modifications.
    *   *Why C is incorrect:* Restoring from the morning's backup recovers the table but loses all data entered between the backup and 2:15 PM — potentially hours of transactions. PITR is strictly superior when it is available.
    *   *Why D is incorrect:* Cloud SQL read replicas use asynchronous replication but replicate all DML operations including DELETE and DROP TABLE. They do not cache or buffer deletions for any time period; the deletion appears on the replica with minimal lag.

---

---

**Question 3**
A database administrator needs to **create an index on the `order_date` column of the `orders` table to speed up queries that filter by date range on a Cloud SQL for PostgreSQL instance**. Which SQL command is most appropriate?
A) CREATE INDEX idx_order_date ON orders(order_date);
B) GRANT SELECT ON orders TO reporting_role;
C) EXPLAIN ANALYZE SELECT * FROM orders WHERE order_date > '2024-01-01';
D) ALTER TABLE orders ADD CONSTRAINT chk_date CHECK (order_date IS NOT NULL);
*   **Correct Answer:** A) CREATE INDEX idx_order_date ON orders(order_date);
*   **Distractor Analysis:**
    *   *Why A is correct:* `CREATE INDEX` creates a B-tree index on the `order_date` column, allowing the query planner to use an index range scan instead of a full sequential table scan for date filter queries.
    *   *Why B is incorrect:* `GRANT SELECT` assigns read privilege to a role; it has no effect on query performance or index creation.
    *   *Why C is incorrect:* `EXPLAIN ANALYZE` diagnoses whether an index is being used by the query planner; it does not create an index.
    *   *Why D is incorrect:* `ADD CONSTRAINT CHECK` adds a data validation rule that rejects NULL values; it does not create an index or improve query performance.

---

**Question 4**
A Cloud SQL for PostgreSQL instance serving a regional application has just experienced a complete regional outage. The operations team has a cross-region read replica in a secondary region. What is the correct sequence of actions to restore write service?
A) Promote the cross-region read replica to a standalone primary instance, then update the application connection string to point to the new primary.
B) Wait for Google to restore the primary region; cross-region replicas automatically reconnect and sync when the primary comes back online.
C) Enable HA on the cross-region read replica to create a new standby before promoting it.
D) Restore the most recent backup from Cloud Storage to a new Cloud SQL instance in the secondary region.
*   **Correct Answer:** A) Promote the cross-region read replica to a standalone primary instance, then update the application connection string to point to the new primary.
*   **Distractor Analysis:**
    *   *Why A is correct:* Promoting the cross-region read replica converts it from a read-only replica into a writable standalone primary. This is the correct Cloud SQL disaster recovery procedure for regional failures. After promotion, you must update the application connection string because the replica's IP address or hostname is different from the original primary.
    *   *Why B is incorrect:* Regional outages can last hours or longer. The replica does not automatically become writable and the application cannot write to a read replica. Waiting for the primary region is not an acceptable DR response.
    *   *Why C is incorrect:* You cannot enable HA on a read replica before promoting it; HA is configured on a primary instance. Attempting to do this in sequence would delay the recovery unnecessarily.
    *   *Why D is incorrect:* Restoring from backup is a slower alternative that also loses any data replicated to the read replica after the last backup. Promoting the existing replica is faster and preserves more recent data.

---

**Question 5**
When designing the backup strategy for a Cloud SQL instance storing financial transaction records, you must mitigate the risk of **ransomware encrypting the database and all its backups stored within the same GCP project**. Which control best addresses this threat?
A) Enable automated backups with cross-region storage and restrict backup deletion permissions using an IAM policy that denies `cloudsql.backupRuns.delete` to all except a dedicated backup admin service account in a separate project.
B) Enable CMEK for Cloud SQL storage so that ransomware cannot read the encrypted backup files.
C) Schedule daily on-demand exports of Cloud SQL data to a Cloud Storage bucket in the same project for easy accessibility.
D) Enable HA on the Cloud SQL instance so that the standby always has a clean copy of the data.
*   **Correct Answer:** A) Enable automated backups with cross-region storage and restrict backup deletion permissions using an IAM policy that denies `cloudsql.backupRuns.delete` to all except a dedicated backup admin service account in a separate project.
*   **Distractor Analysis:**
    *   *Why A is correct:* Ransomware that compromises the GCP project would attempt to delete backups before demanding payment. Restricting the `cloudsql.backupRuns.delete` permission at the project level — and placing the authoritative IAM control in a separate project the ransomware cannot reach — prevents backup deletion even if the primary project is fully compromised. Cross-region storage adds geographic redundancy.
    *   *Why B is incorrect:* CMEK protects data from being read by unauthorized parties, but ransomware that has compromised the project already has access to the decryption key (via the project's IAM bindings to KMS). Encryption at rest does not prevent a privileged attacker from deleting backups.
    *   *Why C is incorrect:* Exporting to a Cloud Storage bucket in the same project means ransomware that compromises the project can also delete the Cloud Storage objects. Same-project backups are not protected from a project-level compromise.
    *   *Why D is incorrect:* HA synchronously replicates all operations to the standby — including any destructive operations performed by ransomware. The standby is not an isolated backup copy.
