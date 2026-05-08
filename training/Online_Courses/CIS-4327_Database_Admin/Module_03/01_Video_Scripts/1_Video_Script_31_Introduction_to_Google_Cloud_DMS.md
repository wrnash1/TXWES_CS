### 1. Video Script 3.1: Introduction to Google Cloud DMS
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 3. Once you design the perfect cloud database, you have to get your data into it. Migrating massive databases with zero downtime is one of the most challenging tasks in IT. To solve this, Google provides the Database Migration Service, or DMS."
**Visual:** A flowchart showing an on-premises database connecting to a Cloud SQL instance via DMS.
**[Alt-text: Flowchart. On-premises Database -> IPsec VPN / Interconnect -> Google Cloud Database Migration Service -> Destination Cloud SQL Instance. Text indicates 'Continuous Replication'.]**
**Audio:** "DMS automates the migration process. Instead of taking your on-premises database offline, exporting a massive SQL dump file, and importing it over hours of downtime, DMS uses continuous replication. It takes an initial snapshot and then listens for any new changes. Your local database stays online while data replicates to the cloud in the background. When the cloud database is fully synchronized, you perform a 'cutover', routing your application to the cloud with mere seconds of downtime."

---
