### 4. Lab 3: Executing a Database Migration
**Objective:** Migrate a standalone MySQL database to Cloud SQL using DMS.
**Instructions:**
1. In Google Cloud Console, navigate to **Database Migration -> Migration jobs**.
2. Click **Create migration job**.
3. Under Source, select a pre-existing Compute Engine VM running MySQL (you will deploy this via a provided Deployment Manager script).
4. Under Destination, select Cloud SQL for MySQL.
5. Create a connection profile using the internal IP address of the source VM.
6. Start the migration job and monitor the 'Status' tab.
7. Once the status reads 'Running' and replication delay is near 0, click **Promote** to trigger the cutover.
**Deliverable:** Take a screenshot of the Migration Jobs dashboard showing your job with the status "Completed". Submit to Blackboard.

---
