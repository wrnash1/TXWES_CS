### 3. Reading Guide: Google Cloud Security and Monitoring
**High-Yield Concepts:**
1. **Encryption at Rest:** By default, Google Cloud encrypts all customer data at rest using Google-managed encryption keys. If your company requires absolute control over the keys due to compliance, you must configure Customer-Managed Encryption Keys (CMEK) via Cloud Key Management Service (KMS).
2. **Cloud SQL Proxy:** A secure way to connect to your Cloud SQL instance from your local machine or a GKE pod without having to explicitly whitelist your IP address in the database firewall. It automatically handles authentication via IAM.
3. **Audit Logs:** Cloud Audit Logs record "Admin Activity" (who created/deleted the database) and "Data Access" (who queried the database). Data Access logs are turned off by default to save money and must be explicitly enabled.

---
