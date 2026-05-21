# Reading Guide: Module 09 - Database Security – IAM, VPC, Encryption
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 09 - Database Security – IAM, VPC, Encryption**! This week focuses on securing GCP database services using the three foundational security layers: Identity and Access Management (IAM) for who can access the database, VPC networking for where connections are permitted, and encryption for protecting data at rest and in transit. Security is one of the highest-weighted domains on the GCP Professional Cloud Database Engineer exam.

Understanding how IAM roles, VPC Service Controls, Private IP, SSL/TLS, and Customer-Managed Encryption Keys (CMEK) apply to Cloud SQL, Spanner, Bigtable, Firestore, and AlloyDB is essential for both the exam and real-world database administration.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud IAM (Identity and Access Management)**: The GCP service that controls who (identity) can do what (role) on which resource. For database services, IAM governs who can create/delete instances, who can connect, and what data access operations are permitted. Predefined roles like `roles/cloudsql.client`, `roles/spanner.databaseReader`, and `roles/bigquery.dataViewer` follow the principle of least privilege.
*   **VPC Private IP**: Configuring a GCP database service with a Private IP address means all traffic to the database travels within Google's internal network and never traverses the public internet. This is the recommended configuration for production databases on Cloud SQL, AlloyDB, and Cloud Spanner, as it eliminates external network attack surface.
*   **Customer-Managed Encryption Keys (CMEK)**: GCP encrypts all data at rest by default using Google-managed keys. CMEK allows organizations to use their own encryption keys stored in Cloud Key Management Service (Cloud KMS). The customer controls key rotation, access, and can revoke access to all encrypted data by disabling or destroying the key. CMEK is required for many compliance frameworks (PCI-DSS, HIPAA).
*   **Cloud SQL Auth Proxy**: A client-side daemon that authenticates connections to Cloud SQL using IAM service account credentials and wraps all data in a mutual TLS (mTLS) tunnel. It is the recommended connection method for Cloud SQL because it eliminates the need to whitelist IP addresses and manages certificate rotation automatically.
*   **Audit Logging**: Cloud Audit Logs record two categories of database activity: Admin Activity logs (who created, modified, or deleted database instances — always enabled and cannot be disabled) and Data Access logs (who read, wrote, or queried data — disabled by default because they generate high volume and cost, and must be explicitly enabled for compliance).

---

### 2. Certification Exam Tips
*   **Principle of Least Privilege**: The exam consistently tests IAM role selection. Always choose the most restrictive predefined role that satisfies the use case. A reporting service should have `roles/bigquery.dataViewer`, not `roles/bigquery.admin`. A Cloud SQL application should authenticate with a service account that has `roles/cloudsql.client`, not `roles/cloudsql.instanceUser` or `roles/owner`.
*   **IAM vs. Database-Level Users**: Know the two-layer security model for Cloud SQL and AlloyDB. IAM controls who can connect at the GCP API level; database users (managed inside MySQL/PostgreSQL with `CREATE USER` and `GRANT`) control what schemas and tables the connected user can access. Both layers must be configured.
*   **Encryption in Transit vs. at Rest**: Encryption in transit (SSL/TLS, Cloud SQL Auth Proxy mTLS) protects data moving between the application and the database. Encryption at rest (Google-managed keys or CMEK) protects data stored on physical disks. The exam tests which type of encryption addresses which threat.
*   **VPC Service Controls**: A perimeter around GCP APIs that prevents data exfiltration. For example, a VPC Service Controls perimeter around BigQuery prevents an authorized user from copying a BigQuery table to an external project outside the perimeter, even if they have IAM permission to do so.
*   **Study Resource:** The official Google Cloud IAM and security documentation is the authoritative exam reference: [Cloud IAM Documentation – Google Cloud](https://cloud.google.com/iam/docs). The freeCodeCamp database course covers foundational security concepts: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to reinforce the SQL-level security concepts (GRANT, REVOKE, roles) that complement GCP IAM for database access control: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free comprehensive lecture covers database security fundamentals, including user management and encryption concepts relevant to GCP: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will configure a Cloud SQL instance with Private IP only, create a service account with the minimal required IAM role, connect using the Cloud SQL Auth Proxy, enable CMEK using Cloud KMS, and enable Data Access audit logs to verify query logging.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the security and user management chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the database security and access control segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the IAM, VPC, and CMEK configuration steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
