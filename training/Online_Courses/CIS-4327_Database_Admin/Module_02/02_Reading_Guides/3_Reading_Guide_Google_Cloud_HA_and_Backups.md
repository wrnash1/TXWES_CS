### 3. Reading Guide: Google Cloud HA and Backups
**High-Yield Concepts:**
1. **Synchronous vs Asynchronous Replication:** HA in Cloud SQL uses *synchronous* replication (data must be written to both zones before returning success). Read Replicas use *asynchronous* replication.
2. **Failover Process:** During a failover, the primary instance is stopped, the persistent disk is attached to the standby instance, and the standby becomes the new primary. Connections are briefly dropped and must be re-established by the client application.
3. **Point-in-Time Recovery (PITR):** PITR requires automated backups to be enabled. It allows restoration to any point within the retention period (usually up to 7 days).

---
