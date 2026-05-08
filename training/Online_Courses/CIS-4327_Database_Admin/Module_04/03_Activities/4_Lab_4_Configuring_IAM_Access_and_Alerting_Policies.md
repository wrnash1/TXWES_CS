### 4. Lab 4: Configuring IAM Access and Alerting Policies
**Objective:** Apply least privilege IAM roles and create a proactive monitoring alert.
**Instructions:**
1. Log into your Google Cloud project.
2. Navigate to **IAM & Admin -> IAM**.
3. Click **Grant Access**. Enter the email address of a classmate or a secondary Google account you own.
4. Assign them the role of **Cloud SQL Viewer** (This allows them to see the instance in the console, but not connect or change data).
5. Navigate to **Monitoring -> Alerting**.
6. Click **Create Policy**.
7. Select the metric: `Cloud SQL Database -> CPU utilization`.
8. Set the condition to trigger if the value is `Above 80%` for `3 minutes`.
9. Set the notification channel to your email address. Name the policy "High CPU Alert".
**Deliverable:** Take a screenshot of your Alerting dashboard showing the enabled "High CPU Alert" policy. Submit to Blackboard.

---
