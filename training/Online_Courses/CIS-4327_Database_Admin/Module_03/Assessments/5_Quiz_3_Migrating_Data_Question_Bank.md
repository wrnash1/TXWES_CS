### 5. Quiz 3: Migrating Data (Question Bank)
**Question 1**
Your organization wishes to migrate a legacy on-premises Oracle database to Google Cloud SQL for PostgreSQL to reduce licensing costs. What type of migration is this, and what mandatory step must occur before data replication begins?
A) Homogeneous migration; you must export a `.bak` file.
B) Heterogeneous migration; you must convert the database schema and stored procedures.
C) Continuous migration; you must enable High Availability on the source database.
D) Lift-and-shift migration; you must configure an IPsec VPN.
*   **Correct Answer:** B) Heterogeneous migration; you must convert the database schema and stored procedures.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Moving from Oracle to PostgreSQL involves different database engines, making it heterogeneous, not homogeneous.
    *   *Why C is incorrect:* While it will likely be a continuous migration, enabling HA on the source is not a mandatory prerequisite for migration.
    *   *Why D is incorrect:* "Lift-and-shift" implies moving an application without changing its underlying architecture (e.g., migrating an Oracle DB on a physical server to an Oracle DB on a Compute Engine VM). Changing to PostgreSQL changes the architecture.

**Question 2**
You are using Google Cloud Database Migration Service (DMS) to perform a continuous migration from an on-premises MySQL database to Cloud SQL. The initial data load has finished, and Change Data Capture (CDC) is currently replicating live changes. What is the final step you must take to finalize the migration and make the Cloud SQL instance primary?
A) Delete the source database.
B) Stop the DMS job manually.
C) Promote the destination instance.
D) Change the DNS records to point to the DMS endpoint.
*   **Correct Answer:** C) Promote the destination instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting the source database before cutover will cause total data loss for any in-flight transactions.
    *   *Why B is incorrect:* Stopping the job manually will sever the replication link, leaving the destination database in a read-only or incomplete state.
    *   *Why D is incorrect:* You point your application to the new Cloud SQL instance's IP address, not the DMS tool's endpoint. Promoting the instance automatically handles severing the replication and making it writable.
