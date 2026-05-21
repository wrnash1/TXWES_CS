# Reading Guide: Module 15 – Migration to GCP: Transfer Service and Migrate for Compute Engine
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 15 – Migration to GCP: Transfer Service and Migrate for Compute Engine**! Moving workloads and data to GCP requires selecting the right migration tool for the source environment and data type. This module covers Storage Transfer Service and Transfer Appliance for data migration, Migrate for Compute Engine (formerly Velostrata) for VM lift-and-shift migrations, and Database Migration Service for moving relational databases to Cloud SQL or AlloyDB. The ACE exam tests your ability to select the correct migration tool for a given scenario and understand the key tradeoffs between tools.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Storage Transfer Service**: A fully managed GCP service that transfers data from Amazon S3, Azure Blob Storage, HTTP/HTTPS sources, or on-premises file systems to Cloud Storage. Supports one-time and recurring scheduled transfers. For on-premises sources, the Transfer Service for On Premises Data agent runs on your local network to read and upload data. Best for data sets that can be transferred over the network in a reasonable timeframe.

*   **Transfer Appliance**: A physical hardware device shipped by Google that you fill with data (up to 1 PB per appliance) and ship back to Google for ingestion into Cloud Storage. Use Transfer Appliance when the data volume is so large that transferring over the internet would take weeks or months (as a rule of thumb, when network transfer would take more than one week). Transfer Appliance is offline — your data is loaded onto the device without a network transfer.

*   **Migrate for Compute Engine**: A GCP service that replicates on-premises or other-cloud VMs to GCP using continuous block-level replication. Migrations can be tested in GCP before cutover, and the cutover itself causes only minutes of downtime. After migration, VMs run as Compute Engine instances. Supports sources including VMware vSphere, AWS EC2, and Azure VMs.

*   **Database Migration Service (DMS)**: A fully managed service for migrating relational databases to Cloud SQL (MySQL, PostgreSQL, SQL Server) or AlloyDB with minimal downtime. DMS uses continuous change data capture (CDC) replication to keep the destination database in sync with the source until cutover. The source database can remain online and serving traffic during migration.

*   **Lift-and-Shift vs. Re-platform vs. Re-architect**: Three migration strategies. Lift-and-shift moves workloads to GCP with no code changes (use Migrate for Compute Engine). Re-platform adapts the workload to use managed services (e.g., moving from self-managed MySQL on a VM to Cloud SQL). Re-architect refactors the application to be cloud-native (e.g., decomposing a monolith into Cloud Run microservices). The ACE exam tests choosing the right strategy for a given scenario.

*   **Cloud Storage Transfer Service vs. `gsutil`**: For large-scale data migration, Storage Transfer Service is preferred over `gsutil rsync` because it runs fully managed without requiring a local machine to stay connected, supports scheduling, and provides transfer job monitoring. `gsutil` is appropriate for ad hoc small uploads and scripted operations but requires a persistent client connection.

---

### 2. Certification Exam Tips

*   **Bandwidth determines Transfer Appliance vs. online transfer**: The exam uses bandwidth and data size to test which tool is appropriate. If moving 500 TB over a 1 Gbps link would take more than a week, Transfer Appliance is the answer. If the data is tens of GB or a few TB and the network is fast enough to complete transfer in days, Storage Transfer Service is correct.

*   **DMS requires network connectivity to the source**: Database Migration Service connects to the source database over the network. For on-premises sources, this typically requires Cloud VPN or Cloud Interconnect. The exam may test that DMS cannot migrate a database that has no network path to GCP.

*   **Migrate for Compute Engine preserves VM configurations**: Unlike manually re-creating VMs in GCP, Migrate for Compute Engine replicates the exact disk contents, including OS, applications, and data. The migrated VM runs identically on Compute Engine. No application changes are required.

*   **One-time vs. recurring transfers**: Storage Transfer Service supports both. One-time transfers for a bulk data migration, and recurring transfers for ongoing synchronization (e.g., keeping a GCS bucket in sync with an S3 bucket as a data sharing arrangement). The ACE exam tests whether you know to use a scheduled recurring transfer for ongoing sync versus a one-time job for a migration.

*   **Study Resource**: The freeCodeCamp ACE course covers Storage Transfer Service, Migrate for Compute Engine, and Database Migration Service with architecture overviews: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Migration chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Storage Transfer Service overview including supported sources, transfer job configuration, and the on-premises agent for local network transfers: [Storage Transfer Service Overview](https://cloud.google.com/storage-transfer/docs/overview). The source types and scheduling options are directly exam-relevant.
*   **Required Reading**: Review the Migrate for Compute Engine overview to understand the replication-based migration workflow, test clone capabilities, and supported source environments: [Migrate for Compute Engine Overview](https://cloud.google.com/migrate/compute-engine/docs/5.0/concepts/migrate-for-compute-engine-overview).
*   **Required Video**: Watch the Migration segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the GCP Migration chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a Storage Transfer Service job to move data from an S3 bucket to Cloud Storage and review the migration architecture for Migrate for Compute Engine. Key commands to practice:

*   `gcloud transfer jobs create gs://destination-bucket --source-agent-pool=projects/PROJECT/agentPools/default` — creates a transfer job from an on-premises source using the agent pool
*   `gcloud transfer jobs list` — lists all Storage Transfer Service jobs in the project
*   `gcloud transfer jobs describe JOB_NAME` — shows the status and configuration of a transfer job
*   `gcloud database-migration migration-jobs create my-migration --region=us-central1 --type=CONTINUOUS --source=source-connection --destination=dest-connection` — creates a continuous DMS migration job

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Storage Transfer Service Overview](https://cloud.google.com/storage-transfer/docs/overview) documentation page.
- [ ] Read the [Migrate for Compute Engine Overview](https://cloud.google.com/migrate/compute-engine/docs/5.0/concepts/migrate-for-compute-engine-overview) documentation page.
- [ ] Watch the Migration segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a Storage Transfer Service job and review the Migrate for Compute Engine workflow.
- [ ] Proceed to the weekly quiz.
