# Reading Guide: Module 14 - Multi-Cloud and Hybrid Database Strategies
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 14 - Multi-Cloud and Hybrid Database Strategies**! This week focuses on architectures where databases span multiple cloud providers or combine on-premises infrastructure with GCP. Multi-cloud and hybrid strategies are increasingly common in enterprises, and the GCP exam tests your ability to recommend the appropriate GCP tool (AlloyDB Omni, Spanner multi-region, Datastream, Pub/Sub) for each integration scenario.

You will learn the trade-offs between cloud-native-only, multi-cloud, and hybrid architectures, and understand which GCP database services support deployment outside of GCP-managed infrastructure.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Hybrid Database Architecture**: A database deployment model where some workloads run on-premises and others run in GCP, typically connected through Cloud Interconnect or VPN. Hybrid architectures are common during migration transitions or when regulatory requirements mandate that certain data remain on-premises while analytics are moved to GCP.
*   **AlloyDB Omni**: The self-managed, containerized version of AlloyDB for PostgreSQL that can run on any Linux machine — on-premises, another cloud provider (AWS, Azure), or bare metal. AlloyDB Omni enables organizations to use AlloyDB's PostgreSQL-compatible engine and performance optimizations outside of GCP managed infrastructure, supporting multi-cloud or on-premises-first strategies.
*   **Cross-Region Disaster Recovery (DR)**: A database architecture where a secondary copy of the database exists in a geographically separate region to protect against regional failures. For Cloud SQL, this is implemented using cross-region read replicas. For Cloud Spanner, multi-region configurations provide automatic synchronous replication across regions with no manual DR setup required.
*   **Datastream**: A serverless change data capture (CDC) and replication service that continuously streams database changes from Oracle, MySQL, PostgreSQL, or SQL Server sources into GCP destinations (BigQuery, Cloud Storage, Cloud Spanner). Datastream enables ongoing real-time data synchronization from on-premises or other-cloud databases to GCP, supporting hybrid analytics architectures.
*   **VPC Peering and Private Service Connect**: Network connectivity options that allow GCP VPCs (or on-premises networks via Interconnect) to access GCP managed database services (Cloud SQL, AlloyDB, Spanner) using Private IP addresses without traversing the public internet. Private Service Connect provides a more flexible, service-level connectivity model compared to traditional VPC peering.

---

### 2. Certification Exam Tips
*   **Multi-Cloud Scenarios**: The exam presents scenarios where an organization has databases on AWS or Azure and needs to integrate with GCP for analytics or migration. Key answers: use Datastream for real-time CDC into BigQuery; use AlloyDB Omni for running AlloyDB on non-GCP infrastructure; use Cloud Interconnect for private network connectivity between clouds.
*   **Regional vs. Multi-Regional Spanner**: Cloud Spanner regional configurations (single region) provide high availability within a region. Multi-region configurations provide cross-region synchronous replication and survive complete regional failures. The exam tests which configuration is required for a given availability SLA.
*   **DR Strategy Selection**: Know the RTO/RPO profile of each DR approach: Spanner multi-region (RPO=0, RTO~0), Cloud SQL HA (RPO~0, RTO~60s within region), Cloud SQL cross-region replica (RPO = replication lag, RTO = manual promotion time).
*   **Interconnect vs. VPN**: Cloud Dedicated Interconnect provides a physical private connection with guaranteed bandwidth SLAs, appropriate for high-volume production database replication. Cloud VPN uses IPsec tunnels over the public internet, appropriate for lower-volume or development workloads.
*   **Study Resource:** The official GCP documentation on hybrid connectivity and Datastream is the primary reference: [Datastream Documentation – Google Cloud](https://cloud.google.com/datastream/docs). The freeCodeCamp course covers SQL and database fundamentals applicable to hybrid scenarios: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to reinforce the database architecture concepts that multi-cloud strategies build on: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This comprehensive free lecture covers database architecture and replication concepts applicable to multi-cloud and hybrid strategies: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will configure a Datastream stream from a Cloud SQL for MySQL source to a BigQuery destination, verify real-time CDC replication, configure a Cloud SQL cross-region read replica for a simulated DR scenario, and review Cloud Spanner multi-region instance configurations.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the database architecture and replication chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the database architecture and replication segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the Datastream and cross-region replica configuration steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
