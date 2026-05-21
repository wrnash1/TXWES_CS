# Reading Guide: Module 10 - Backup, Recovery, and High Availability
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 10 - Backup, Recovery, and High Availability**! This week focuses on protecting data and maintaining service continuity across GCP database services. Business continuity planning requires understanding Recovery Time Objective (RTO), Recovery Point Objective (RPO), backup strategies, high availability architectures, and disaster recovery procedures for Cloud SQL, Cloud Spanner, AlloyDB, and Bigtable.

These topics are heavily weighted on the GCP Professional Cloud Database Engineer exam because they represent the operational responsibilities of a database engineer in a production environment.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Recovery Time Objective (RTO)**: The maximum acceptable duration of downtime following a failure before the business sustains unacceptable losses. An RTO of 60 seconds means the database must be restored to a serving state within 60 seconds of a failure event. Choosing between Cloud SQL HA (RTO ~60–120s), AlloyDB (RTO ~30s), and Cloud Spanner (RTO ~0, always available) is directly driven by RTO requirements.
*   **Recovery Point Objective (RPO)**: The maximum acceptable amount of data loss measured in time. An RPO of 5 minutes means you can afford to lose up to 5 minutes of committed transactions. Cloud SQL HA uses synchronous replication (RPO ~0), while Cloud SQL read replicas use asynchronous replication (RPO = replication lag, potentially seconds to minutes).
*   **Point-in-Time Recovery (PITR)**: A backup capability that allows restoring a Cloud SQL database to any specific second within the retention window (up to 7 days). PITR uses a combination of automated daily backups and continuous binary log (MySQL) or write-ahead log (PostgreSQL) archiving. It is the primary protection against accidental data modification or deletion.
*   **Cloud SQL Automated Backups**: Fully managed daily snapshot backups stored in Cloud Storage (multi-regional by default for multi-region instances). Backups are retained for up to 365 days and are required for PITR. Automated backups can be taken on demand at any time using the Cloud SQL Admin API.
*   **Cross-Region Read Replicas**: Asynchronous read replicas created in a different GCP region from the primary instance. In the event of a complete regional outage, cross-region read replicas can be manually promoted to become a standalone writable primary. After promotion, the replica is no longer connected to the original primary and must be reconfigured. This is Cloud SQL's disaster recovery (DR) option for regional failures.

---

### 2. Certification Exam Tips
*   **HA vs. DR**: Know the difference. High Availability (HA) protects against zone-level failures using synchronous standby replicas within the same region — automatic failover, RTO ~60–120s. Disaster Recovery (DR) protects against region-level failures using cross-region read replicas — requires manual promotion, higher RTO. Spanner is always HA by design, eliminating the choice.
*   **Cloud Spanner HA**: Cloud Spanner provides 99.999% availability without any HA configuration by the user. Its multi-region configurations provide synchronous replication across regions, making it resilient to regional failures automatically. This is a key exam differentiator versus Cloud SQL.
*   **Backup Strategy Selection**: The exam presents RPO/RTO requirements and asks you to identify the backup and HA strategy. Map: RPO = 0, RTO = 0 → Cloud Spanner or AlloyDB; RPO ~0, RTO ~60s → Cloud SQL HA; RPO = last backup, RTO = restore time → Cloud SQL automated backups only (no HA).
*   **Promote vs. Failover**: Know the difference. HA failover is automatic and promotes the standby in the same region. Promoting a cross-region read replica is a manual operation that converts it to a standalone primary — the original replication link is severed and never reestablished automatically.
*   **Study Resource:** The official Cloud SQL documentation on backups and HA is the primary reference: [Cloud SQL Backup and Recovery – Google Cloud](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups). The freeCodeCamp course covers general backup and recovery concepts: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The database availability and recovery chapters in *Database Design* by Adrienne Watt provide the foundational concepts for backup and recovery strategies: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free comprehensive lecture covers database administration concepts including backup types and recovery procedures applicable to GCP services: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will enable automated backups and PITR on a Cloud SQL instance, take an on-demand backup, perform a PITR restore to a specific timestamp, create a cross-region read replica, and simulate a regional failover by promoting the replica to a standalone primary.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the backup, recovery, and availability chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the backup and recovery segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the PITR and replica promotion steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
