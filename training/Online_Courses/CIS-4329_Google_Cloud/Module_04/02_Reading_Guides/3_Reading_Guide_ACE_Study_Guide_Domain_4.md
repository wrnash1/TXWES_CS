### 3. Reading Guide: ACE Study Guide Domain 4
**High-Yield Concepts:**
1. **Load Balancing Types:** 
   * *Global HTTP(S) Load Balancer:* Operates at Layer 7. Distributes traffic globally based on the user's geographic location. Requires your backend to be in a MIG.
   * *Network Load Balancer:* Operates at Layer 4 (TCP/UDP). Used for regional traffic that isn't HTTP/HTTPS.
2. **Uptime Checks:** Configured in Cloud Monitoring to constantly ping your web server from multiple locations around the world. If the site goes down, it triggers an alert policy.
3. **Log Sinks:** Cloud Logs are only retained for 30 days by default. To keep them longer for compliance, you must create a Log Sink to export them to a Cloud Storage bucket or BigQuery.

---
