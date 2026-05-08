### 4. Lab 1: Provisioning a Cloud SQL Instance
**Objective:** Deploy a PostgreSQL instance using Google Cloud Console and connect via Cloud Shell.
**Instructions:**
1. Log into your Google Cloud Student Account. Ensure your project is selected.
2. Navigate to **SQL** in the navigation menu. Click **Create Instance**.
3. Choose **PostgreSQL**.
4. Set the Instance ID to `txwes-pg-db` and generate a secure root password. Save this password.
5. Under Configuration, select **Development** (to save credits) and choose the `us-central1` region. Click Create.
6. Once created, click the **Open Cloud Shell** icon at the top right.
7. Run the command: `gcloud sql connect txwes-pg-db --user=postgres --quiet` and enter your password.
**Deliverable:** Take a screenshot of your Cloud Shell showing the `postgres=>` prompt, proving successful connection.

---
