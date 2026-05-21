# Reading Guide: Module 03 - Cloud SQL – MySQL and PostgreSQL on GCP
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 03 - Cloud SQL – MySQL and PostgreSQL on GCP**! This week you will study Google Cloud's fully managed relational database service in depth. Cloud SQL is one of the most heavily tested services on the Google Cloud Professional Cloud Database Engineer exam because it covers the broadest range of real-world database administration tasks: provisioning, high availability, backups, replication, security, and monitoring.

You will learn how Cloud SQL abstracts the operational burden of managing a database server while still requiring administrators to make important configuration choices that directly affect availability, cost, and performance.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud SQL**: Google Cloud's fully managed relational database service supporting MySQL, PostgreSQL, and SQL Server. It handles OS patching, storage auto-scaling, automated backups, and failover. Cloud SQL is best suited for regional applications that need ACID-compliant SQL with minimal migration effort from on-premises or other cloud providers.
*   **High Availability (HA) Configuration**: When HA is enabled, Cloud SQL creates a standby instance in a different zone within the same region. Data is written synchronously to both the primary and the standby before a transaction is confirmed. If the primary zone fails, Cloud SQL automatically promotes the standby with no IP address change, minimizing downtime.
*   **Read Replica**: An asynchronous copy of the primary instance used to offload read queries. Unlike the HA standby, a read replica can serve SELECT queries. Because replication is asynchronous, it has a small replication lag and does not provide automatic failover. Cross-region read replicas can be manually promoted if the primary region is lost.
*   **Point-in-Time Recovery (PITR)**: A backup strategy that allows restoration of a database to any second within the configured retention window (up to 7 days by default). PITR requires automated backups to be enabled and uses binary log (MySQL) or write-ahead log (PostgreSQL) to replay transactions after restoring the most recent full backup.
*   **Cloud SQL Auth Proxy**: A local daemon that authenticates connections to Cloud SQL using IAM credentials and wraps them in a secure TLS tunnel. It eliminates the need to manage IP allowlists and SSL certificates manually, and is the recommended connection method for GKE pods and applications running outside the VPC.

---

### 2. Certification Exam Tips
*   **HA vs. Read Replica**: This is a classic exam trap. HA provides automated failover but the standby cannot serve reads. Read replicas serve reads but do not provide automatic failover. Many exam scenarios combine both: use HA for availability SLAs and add read replicas for read scaling.
*   **Synchronous vs. Asynchronous Replication**: HA uses synchronous replication (data written to both zones before commit, so no data loss). Read replicas and cross-region replicas use asynchronous replication (slight lag possible). The exam tests whether you know which type applies in each scenario.
*   **PITR Requirements**: PITR only works if automated backups are enabled. Know that enabling PITR alone is not sufficient — you must also enable binary logging (MySQL) or confirm WAL archiving (PostgreSQL) is active. Disabling automated backups also disables PITR.
*   **Connection Security**: Know the three connection methods: Private IP (recommended for production — keeps traffic on the Google network), Public IP with SSL (for external access with certificate verification), and Cloud SQL Auth Proxy (recommended for apps running on Google Cloud services like GKE, Cloud Run, or App Engine).
*   **Study Resource:** The official Google Cloud documentation on Cloud SQL is the authoritative study source for this module: [Cloud SQL Documentation – Google Cloud](https://cloud.google.com/sql/docs). The freeCodeCamp SQL course is a useful supplement for SQL syntax review: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The open textbook *Database Design* by Adrienne Watt covers relational fundamentals that apply directly to Cloud SQL administration; read it alongside the official Cloud SQL documentation for a complete picture: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free comprehensive lecture covers SQL concepts, backup strategies, and connection management that map to Cloud SQL exam objectives: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will provision a Cloud SQL for PostgreSQL instance with HA enabled, configure automated backups with PITR, create a read replica, connect using both the Cloud SQL Auth Proxy and a Private IP configuration, and simulate a failover.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the relational fundamentals chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the SQL and backup concepts segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the Cloud SQL configuration steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
