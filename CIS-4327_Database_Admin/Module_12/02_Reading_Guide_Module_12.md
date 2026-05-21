# Reading Guide: Module 12 - Database Migration – DMS and Migrate for Compute Engine
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 12 - Database Migration – DMS and Migrate for Compute Engine**! This week focuses on migrating existing databases to Google Cloud using the Database Migration Service (DMS) and related GCP tools. Database migration is a core responsibility of a Cloud Database Engineer and is a significant exam domain.

You will learn the difference between homogeneous and heterogeneous migrations, understand the continuous migration lifecycle (Initial Load → CDC → Cutover), and know when to use DMS versus manual export/import versus Datastream for different migration scenarios.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Database Migration Service (DMS)**: Google Cloud's fully managed service for migrating databases to Cloud SQL, AlloyDB, and Cloud Spanner. DMS supports continuous migration using Change Data Capture (CDC) to replicate ongoing changes while the source database remains live, minimizing application downtime during cutover.
*   **Homogeneous Migration**: A database migration where the source and destination use the same database engine (e.g., MySQL to Cloud SQL for MySQL, PostgreSQL to Cloud SQL for PostgreSQL). Homogeneous migrations are simpler because the schema, data types, and stored procedures are compatible without conversion.
*   **Heterogeneous Migration**: A database migration where the source and destination use different database engines (e.g., Oracle to Cloud SQL for PostgreSQL, SQL Server to Cloud SQL for MySQL). Heterogeneous migrations require schema and query conversion before data transfer begins. Google's migration guides and the Schema Conversion Tool assist with this conversion.
*   **Change Data Capture (CDC)**: A migration technique that continuously reads the source database's transaction log (binary log for MySQL, WAL for PostgreSQL) and replays every INSERT, UPDATE, and DELETE on the destination in real time. CDC allows the destination to stay synchronized with the source during the migration period, enabling a low-downtime cutover.
*   **Datastream**: A GCP serverless change data capture and replication service that streams database changes from Oracle, MySQL, PostgreSQL, and SQL Server into BigQuery, Cloud Storage, or Spanner in real time. Unlike DMS (which targets Cloud SQL and AlloyDB for live migration), Datastream is used for ongoing data replication pipelines to analytics systems.

---

### 2. Certification Exam Tips
*   **DMS Migration Lifecycle**: Know the four phases of a DMS continuous migration: (1) Create and configure the migration job, (2) Initial Load — full dump of existing data, (3) CDC replication — ongoing changes replicated in near-real-time, (4) Cutover — stop writes to source, allow CDC to drain, promote destination. The exam tests which phase a described scenario is in and what action is needed next.
*   **Homogeneous vs. Heterogeneous**: The exam asks you to classify a migration and identify the additional steps required. Heterogeneous always requires schema conversion before the initial load. Homogeneous is a near-direct transfer. Remember: Oracle → PostgreSQL is heterogeneous even though both are RDBMS; different SQL dialects mean incompatible DDL and stored procedure syntax.
*   **Promoting the Destination**: After CDC synchronization, the final cutover step is "promoting" the DMS destination instance. This severs the replication link and makes the destination writable as a standalone primary. You must update application connection strings to point to the new instance — DMS does not redirect traffic automatically.
*   **Connectivity Requirements**: DMS requires network connectivity to the source database. Options: VPN tunnel, Dedicated Interconnect, or IP allowlisting (not recommended for production). Know which connectivity method is appropriate for on-premises versus cloud-hosted source databases.
*   **Study Resource:** The official Google Cloud Database Migration Service documentation is the primary exam reference: [Database Migration Service – Google Cloud](https://cloud.google.com/database-migration/docs). The freeCodeCamp course covers SQL fundamentals applicable to migration scenarios: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to reinforce the relational schema concepts that are central to migration planning and schema conversion: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free lecture covers SQL fundamentals and schema design principles that apply to both homogeneous and heterogeneous migration planning: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will create a DMS migration job from a MySQL source to Cloud SQL for MySQL, observe the initial load and CDC phases, verify replication lag metrics, and perform a cutover by promoting the destination instance. You will also update the application's connection string to point to the new Cloud SQL instance.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the schema design and SQL chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the database administration and migration concepts in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the DMS migration job configuration steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
