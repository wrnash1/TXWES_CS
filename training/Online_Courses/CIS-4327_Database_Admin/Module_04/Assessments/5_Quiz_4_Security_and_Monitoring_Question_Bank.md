### 5. Quiz 4: Security and Monitoring (Question Bank)
**Question 1**
Your organization has strict compliance requirements that dictate all database backups and persistent disks must be encrypted using keys that your organization exclusively generates, manages, and rotates. Which Google Cloud feature must you implement to satisfy this requirement for Cloud SQL?
A) Google-managed encryption keys
B) Customer-Managed Encryption Keys (CMEK) using Cloud KMS
C) Transparent Data Encryption (TDE)
D) IPsec VPN tunnels
*   **Correct Answer:** B) Customer-Managed Encryption Keys (CMEK) using Cloud KMS
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Google-managed keys are the default, but they do not satisfy compliance requirements demanding that the *customer* generate and manage the key material.
    *   *Why C is incorrect:* TDE is a specific Microsoft SQL Server feature, not the Google Cloud native method for managing disk-level encryption keys across GCP services.
    *   *Why D is incorrect:* IPsec VPN encrypts data in *transit* across a network, not data at *rest* on persistent disks or backups.

**Question 2**
A developer complains that their application is running slowly. You suspect the database is the bottleneck, but the overall CPU utilization of the Cloud SQL instance is only at 40%. You need to identify if a specific, poorly optimized SQL `SELECT` statement is taking too long to execute. Which Google Cloud tool provides this specific visibility?
A) Cloud Audit Logs
B) Cloud SQL Proxy
C) Query Insights
D) Identity and Access Management (IAM)
*   **Correct Answer:** C) Query Insights
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Audit Logs track *who* performed an action (Data Access logs can show the query was run), but they do not provide performance metrics, execution plans, or database load analysis.
    *   *Why B is incorrect:* Cloud SQL Proxy is a tool used to establish a secure connection to the database, not a monitoring or performance tuning tool.
    *   *Why D is incorrect:* IAM manages access control and permissions, entirely unrelated to database query performance.
