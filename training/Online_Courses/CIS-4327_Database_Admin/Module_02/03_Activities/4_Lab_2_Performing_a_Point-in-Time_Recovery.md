### 4. Lab 2: Performing a Point-in-Time Recovery
**Objective:** Enable PITR, simulate a data loss event, and recover the database.
**Instructions:**
1. In the Google Cloud Console, navigate to your `txwes-pg-db` Cloud SQL instance.
2. Go to **Backups** and ensure "Enable point-in-time recovery" is checked.
3. Connect to the database via Cloud Shell: `gcloud sql connect txwes-pg-db --user=postgres`
4. Create a table and insert a record: `CREATE TABLE test (id INT); INSERT INTO test VALUES (1);`
5. Note the exact current time (UTC). Wait 2 minutes.
6. Simulate a disaster: `DROP TABLE test;`
7. In the GCP Console, go to **Backups**, click **Clone**, and select **Point-in-time recovery**. Enter the time you noted in step 5.
**Deliverable:** Take a screenshot showing the successful creation of the cloned (recovered) database instance in the GCP console.

---
