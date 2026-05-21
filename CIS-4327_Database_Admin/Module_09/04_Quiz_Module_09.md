# Quiz: Module 09 - Database Security – IAM, VPC, Encryption
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A new Cloud SQL for PostgreSQL instance is being set up for a production application running on Google Kubernetes Engine (GKE). Your security policy requires that no database traffic traverse the public internet and that connection credentials be managed through GCP IAM. Which configuration satisfies both requirements?
A) Configure the Cloud SQL instance with a Public IP address and use SSL certificates for encryption.
B) Configure the Cloud SQL instance with Private IP in the same VPC as the GKE cluster and use the Cloud SQL Auth Proxy sidecar for IAM-authenticated connections.
C) Configure the Cloud SQL instance with a Public IP address and add the GKE cluster's external IP to the authorized networks list.
D) Deploy the PostgreSQL database directly on a Compute Engine VM with Private IP and manage credentials manually.
*   **Correct Answer:** B) Configure the Cloud SQL instance with Private IP in the same VPC as the GKE cluster and use the Cloud SQL Auth Proxy sidecar for IAM-authenticated connections.
*   **Distractor Analysis:**
    *   *Why B is correct:* Private IP keeps all database traffic within Google's internal VPC network, satisfying the no-public-internet requirement. The Cloud SQL Auth Proxy sidecar container in the GKE pod authenticates connections using a Kubernetes service account mapped to a GCP service account with `roles/cloudsql.client`, satisfying the IAM credential management requirement.
    *   *Why A is incorrect:* A Public IP address exposes the database to the public internet, violating the first security requirement regardless of SSL encryption.
    *   *Why C is incorrect:* Adding the GKE cluster's external IP to authorized networks still requires a Public IP on the Cloud SQL instance and relies on IP allowlisting rather than IAM credential management.
    *   *Why D is incorrect:* A self-managed PostgreSQL on Compute Engine removes the benefits of Cloud SQL's managed service (automated backups, HA, patches) and does not integrate with IAM for connection authentication.

---

---

**Question 2**
A compliance audit requires that all Cloud SQL Data Access operations (SELECT, INSERT, UPDATE, DELETE) executed by application service accounts be logged in Cloud Audit Logs. An auditor reports that no Data Access log entries are appearing despite the application being actively used. What is the most likely cause?
A) Cloud SQL does not support Data Access audit logging; only Admin Activity logs are available.
B) Data Access audit logs are disabled by default and must be explicitly enabled in the Cloud IAM Audit Logs configuration.
C) The service account must be granted the `roles/logging.logWriter` role to write its own audit log entries.
D) Audit logs are only available for Cloud SQL Enterprise Plus tier instances.
*   **Correct Answer:** B) Data Access audit logs are disabled by default and must be explicitly enabled in the Cloud IAM Audit Logs configuration.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cloud Audit Logs has two categories: Admin Activity logs (always on, cannot be disabled, record instance creation/deletion/modification) and Data Access logs (disabled by default because they generate high data volume and storage cost, and must be explicitly enabled per service in the GCP project's IAM Audit Logs settings).
    *   *Why A is incorrect:* Cloud SQL does support Data Access audit logging; it records DATA_READ and DATA_WRITE operations. It is simply disabled by default.
    *   *Why C is incorrect:* Cloud Audit Logs entries are written by GCP infrastructure on behalf of the principal performing the action. The acting service account does not need `roles/logging.logWriter` to generate its own audit log entries.
    *   *Why D is incorrect:* Cloud Audit Logs availability is not restricted by Cloud SQL edition tier; Data Access logging can be enabled for any Cloud SQL instance.

---

---

**Question 3**
A Cloud SQL database administrator needs to **assign read-only access to a specific database schema for a newly created analyst user**. Which SQL command is most appropriate after connecting to the database?
A) GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO analyst_user;
B) CREATE INDEX idx_analyst ON reports(report_date);
C) EXPLAIN ANALYZE SELECT * FROM reports WHERE report_date > '2024-01-01';
D) ALTER USER analyst_user WITH SUPERUSER;
*   **Correct Answer:** A) GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO analyst_user;
*   **Distractor Analysis:**
    *   *Why A is correct:* `GRANT SELECT ON ALL TABLES IN SCHEMA` is the PostgreSQL DCL command that grants read-only query access on all tables within a named schema to the specified user. This follows the principle of least privilege by granting only SELECT, not INSERT/UPDATE/DELETE.
    *   *Why B is incorrect:* `CREATE INDEX` is a DDL command that creates a performance optimization structure on a table; it has no effect on user privileges or access control.
    *   *Why C is incorrect:* `EXPLAIN ANALYZE` executes a query and returns its execution plan for performance diagnostics; it does not modify user permissions.
    *   *Why D is incorrect:* `ALTER USER ... WITH SUPERUSER` grants full superuser privileges, which is the opposite of least-privilege access control and creates a major security risk.

---

**Question 4**
A Cloud SQL for MySQL instance is being reviewed for security hardening. The security team requires that all connections from application servers be encrypted in transit and that applications cannot connect using plaintext. Which configuration enforces this requirement?
A) Set the `ssl_mode` flag on the Cloud SQL instance to `TRUSTED_CLIENT_CERTIFICATE_REQUIRED` (or `REQUIRE_SSL` in MySQL), forcing all client connections to use SSL/TLS.
B) Enable CMEK for the Cloud SQL instance to encrypt all stored data with a customer-managed key.
C) Configure the Cloud SQL instance with Private IP only to ensure all traffic stays within the VPC.
D) Enable the `require_secure_transport` system variable in the Cloud SQL MySQL instance flags.
*   **Correct Answer:** D) Enable the `require_secure_transport` system variable in the Cloud SQL MySQL instance flags.
*   **Distractor Analysis:**
    *   *Why D is correct:* The MySQL `require_secure_transport` system variable, when set to `ON` via Cloud SQL database flags, forces all client connections to use SSL/TLS. Any connection attempt without SSL is rejected at the server level, ensuring all in-transit data is encrypted.
    *   *Why A is incorrect:* The description in option A conflates PostgreSQL SSL mode settings with MySQL; the MySQL-specific flag is `require_secure_transport`. Additionally, `ssl_mode` in the context described is a client-side setting, not a server-level enforcement.
    *   *Why B is incorrect:* CMEK protects data stored at rest on the physical disk; it does not affect whether client connections are encrypted in transit.
    *   *Why C is incorrect:* Private IP keeps connections within the VPC but does not enforce encryption at the transport layer; plaintext connections from within the VPC are still possible without SSL enforcement.

---

**Question 5**
When securing a Cloud SQL instance, you must mitigate the risk of **a compromised GCP project administrator using their IAM Owner role to extract all customer data from the database**. Which control best limits the blast radius of this threat?
A) Apply CMEK with Cloud KMS and place the Cloud KMS key in a separate, restricted GCP project. Revoke the administrator's IAM access to the KMS project.
B) Enable Cloud SQL Audit Logs to detect when the administrator runs data extraction queries.
C) Configure VPC Service Controls to block the administrator's account from calling the Cloud SQL API.
D) Rotate the Cloud SQL root password immediately when the administrator account is suspected of compromise.
*   **Correct Answer:** A) Apply CMEK with Cloud KMS and place the Cloud KMS key in a separate, restricted GCP project. Revoke the administrator's IAM access to the KMS project.
*   **Distractor Analysis:**
    *   *Why A is correct:* CMEK with a key stored in a separate, access-controlled KMS project creates an administrative boundary. Even if the GCP project admin has `roles/owner` on the database project, they cannot decrypt the data without access to the KMS key. This is the GCP recommended defense-in-depth pattern for separating data custody from key custody.
    *   *Why B is incorrect:* Audit logs detect and record the extraction after it has occurred; they do not prevent the administrator from accessing or extracting the data while their permissions are active.
    *   *Why C is incorrect:* VPC Service Controls restrict access by network perimeter, not by specific IAM identity. An administrator within the perimeter can still access the database; VPC Service Controls does not selectively block named users.
    *   *Why D is incorrect:* Rotating the root password prevents database-level credential access but does not prevent an IAM Owner from using the Cloud SQL Admin API to export a backup, create a new database user, or access data through other GCP control plane mechanisms.
