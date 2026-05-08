### 1. Video Script 2.1: Configuring High Availability (HA) in Cloud SQL
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 2. A database is the beating heart of an application. If the database goes down, the business stops. Therefore, configuring High Availability, or HA, is a paramount duty of a Cloud Database Engineer."
**Visual:** Diagram showing a primary Cloud SQL instance in 'us-central1-a' replicating data synchronously to a standby instance in 'us-central1-b'.
**[Alt-text: Two database cylinders. The left cylinder is marked 'Primary (Zone A)'. The right cylinder is marked 'Standby (Zone B)'. A solid arrow labeled 'Synchronous Replication' points from Primary to Standby.]**
**Audio:** "In Google Cloud SQL, HA is achieved through regional deployments. When you enable HA, Google automatically provisions a standby instance in a different zone within the same region. Data is synchronously replicated to a persistent disk accessible by both zones. If the primary zone fails, Cloud SQL automatically fails over to the standby instance in the secondary zone without changing the connection IP address. This ensures your application experiences minimal downtime."

---
