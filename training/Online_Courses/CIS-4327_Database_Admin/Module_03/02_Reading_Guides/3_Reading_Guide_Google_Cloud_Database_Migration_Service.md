### 3. Reading Guide: Google Cloud Database Migration Service
**High-Yield Concepts:**
1. **Connectivity:** For DMS to work, it must be able to securely connect to your source database. This is typically achieved via IPsec VPN, Dedicated Interconnect, or an IP allowlist if the source is publicly accessible (not recommended).
2. **Cutover Strategy:** Understand the phases of continuous migration: Setup -> Initial load -> Change Data Capture (CDC) replication -> Cutover. 
3. **Supported Sources:** DMS natively supports migrating from MySQL, PostgreSQL, SQL Server, and Oracle (preview/heterogeneous).

---
