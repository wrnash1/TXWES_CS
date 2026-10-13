# Quiz: Module 10 — Azure Databases

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. Total: 100 points.

---

### Question 1

A company is migrating an on-premises SQL Server 2019 application to Azure. The application uses SQL Server Agent for nightly backup jobs, linked servers to connect to a secondary SQL Server instance, and Service Broker for internal messaging. The team wants a fully managed PaaS database service and does not want to manage the operating system. Which Azure service best meets these requirements?

A. Azure SQL Database (Single Database)

B. Azure SQL Managed Instance

C. SQL Server on Azure Virtual Machine

D. Azure Database for PostgreSQL

**Correct Answer: B**

**Distractor Analysis:**

- **A (Azure SQL Database):** Azure SQL Database does not fully support SQL Server Agent, linked servers to external servers, or Service Broker. The migration would require significant application refactoring. Incorrect.
- **B (Azure SQL Managed Instance) — CORRECT:** Azure SQL Managed Instance provides near-100% compatibility with on-premises SQL Server 2017+, including full SQL Server Agent, linked servers, Service Broker, and cross-database queries. It is a fully managed PaaS service — no OS management required. This is the correct answer for "migrate complex SQL Server with advanced features to PaaS."
- **C (SQL Server on Azure VM):** SQL Server on Azure VM would also support all these features, but it is IaaS — the team would manage the OS, apply patches, and configure HA manually. The requirement is "fully managed PaaS." Incorrect.
- **D (Azure Database for PostgreSQL):** PostgreSQL is an entirely different database engine. It does not support T-SQL, SQL Server Agent, linked servers, or Service Broker. Incorrect.

---

### Question 2

An e-commerce application requires a database that can serve product catalog queries from users across Asia Pacific, Europe, and North America with sub-10 millisecond read latency for each region. The product catalog has a flexible schema — different product types have different attributes. Which Azure database service is the best fit?

A. Azure SQL Database with Active Geo-Replication to three regions

B. Azure Cosmos DB with multi-region distribution

C. Azure Database for MySQL with read replicas in each region

D. Azure Synapse Analytics Serverless SQL Pool

**Correct Answer: B**

**Distractor Analysis:**

- **A (Azure SQL Database with Geo-Replication):** SQL Database with geo-replication provides regional read replicas, but it uses a relational model with a fixed schema. A flexible schema across different product types would be difficult without complex table inheritance patterns. Also, latency is not guaranteed to be sub-10 ms globally. Incorrect.
- **B (Azure Cosmos DB) — CORRECT:** Cosmos DB is specifically designed for global distribution with single-digit millisecond read latency from any region. It natively supports flexible JSON document schemas with different attributes per document. Adding regions is a configuration change, not an architectural redesign.
- **C (Azure Database for MySQL with read replicas):** MySQL Flexible Server supports read replicas in secondary regions, but read latency across continents is not guaranteed to be sub-10 ms. Also, relational schema constraints make flexible product attributes more difficult to manage. Incorrect.
- **D (Azure Synapse Analytics):** Synapse is an analytics service for data warehousing and large-scale reporting queries. It is not designed for low-latency OLTP (online transaction processing) or operational reads for a live e-commerce application. Incorrect.

---

### Question 3

Which of the following Cosmos DB consistency levels guarantees that a client always reads its own writes within the same session, while providing reasonable read latency?

A. Strong

B. Bounded Staleness

C. Session

D. Eventual

**Correct Answer: C**

**Distractor Analysis:**

- **A (Strong):** Strong consistency guarantees every read reflects the most recent write globally, not just within a session. It provides the strongest guarantee but at the highest latency cost — it is not the best choice when session-level consistency is sufficient. Not the most specific answer. Incorrect.
- **B (Bounded Staleness):** Bounded Staleness guarantees reads lag behind writes by a configurable time or version count. It does not specifically provide session-level read-your-writes guarantees. Incorrect.
- **C (Session) — CORRECT:** Session consistency guarantees that within a single client session, all reads reflect the most recent writes made by that session. This is the default Cosmos DB consistency level and is ideal for user-centric applications like shopping carts and user profiles where a user should always see their own changes.
- **D (Eventual):** Eventual consistency provides no guarantees about read order or freshness. A client might not see its own writes immediately. This is the weakest consistency level. Incorrect.

---

### Question 4

A development team builds a SaaS application that provisions one Azure SQL Database per customer. They currently have 200 customers, with most databases being lightly used on evenings and weekends but very active during business hours. All databases are the same SKU size, resulting in significant wasted capacity. Which Azure SQL feature addresses this cost inefficiency?

A. SQL Server on Azure VM with multiple databases

B. Azure SQL Elastic Pools

C. Azure SQL Database Hyperscale tier

D. Azure SQL Managed Instance

**Correct Answer: B**

**Distractor Analysis:**

- **A (SQL Server on Azure VM):** Moving to IaaS would increase management overhead and would not directly solve the variable utilization cost problem unless the VM is significantly undersized, which would hurt performance. Incorrect.
- **B (Azure SQL Elastic Pools) — CORRECT:** Elastic Pools allow multiple databases to share a pool of DTU or vCore resources. When one database is idle (e.g., during off-hours), its unused resources are available to busier databases. This is precisely the cost optimization tool for SaaS scenarios with many databases having variable and unpredictable utilization.
- **C (Hyperscale):** Hyperscale is designed for very large individual databases (up to 100 TB) — not for managing many small databases with variable utilization. It would not solve the resource efficiency problem. Incorrect.
- **D (Azure SQL Managed Instance):** Managed Instance is an instance that hosts multiple databases, but it is primarily for migration of complex SQL Server applications. It does not provide the same elastic resource sharing model as Elastic Pools. Incorrect.

---

### Question 5

An organization's Azure Cosmos DB account has global distribution enabled across three regions. What is the multi-region write and read availability SLA provided by Cosmos DB with this configuration?

A. 99.9%

B. 99.99%

C. 99.999%

D. 100%

**Correct Answer: C**

**Distractor Analysis:**

- **A (99.9%):** 99.9% is the SLA for many basic Azure services. Cosmos DB's multi-region SLA is significantly higher. Incorrect.
- **B (99.99%):** 99.99% is the SLA for Azure SQL Database and single-region Cosmos DB read/write availability. Multi-region Cosmos DB provides a higher SLA. Incorrect.
- **C (99.999%) — CORRECT:** Azure Cosmos DB provides a 99.999% (five nines) SLA for both read and write availability when configured with multiple regions. This is the highest database availability SLA in Azure's portfolio.
- **D (100%):** No cloud service offers a 100% uptime SLA. 100% would mean zero downtime ever, which is not achievable or promised by any provider. Incorrect.

---

### Question 6

A data analytics team needs to run complex T-SQL queries across 10 years of sales transaction data totaling 50 TB. The queries involve large aggregations, multiple joins, and are run by business analysts for reporting purposes — not for operational transactions. Which Azure service is best suited for this workload?

A. Azure SQL Database (Hyperscale tier)

B. Azure Cosmos DB

C. Azure Synapse Analytics (Dedicated SQL Pool)

D. Azure Database for MySQL

**Correct Answer: C**

**Distractor Analysis:**

- **A (Azure SQL Database Hyperscale):** While Hyperscale supports databases up to 100 TB, it is designed for OLTP (online transactional processing) workloads — high-frequency, small transactions. Running large analytical aggregation queries across 50 TB is the definition of OLAP (online analytical processing) — the domain of data warehousing services. Incorrect.
- **B (Azure Cosmos DB):** Cosmos DB is optimized for globally distributed, low-latency operational reads and writes. It is not designed for large-scale analytical T-SQL queries across terabytes of data. Incorrect.
- **C (Azure Synapse Analytics Dedicated SQL Pool) — CORRECT:** Azure Synapse Analytics with Dedicated SQL Pool uses Massively Parallel Processing (MPP) to distribute large analytical queries across multiple compute nodes, providing excellent performance for petabyte-scale analytics and business intelligence workloads. This is precisely the scenario it was designed for.
- **D (Azure Database for MySQL):** MySQL is an OLTP relational database. While MySQL can run analytical queries, it is not designed for 50 TB analytical workloads and would perform poorly at this scale. Incorrect.

---

### Question 7

A company is currently running a web application that uses a MySQL database on premises. They want to migrate to Azure with minimal application code changes, managed infrastructure, and automatic patching. Which Azure service should they use?

A. SQL Server on Azure Virtual Machine running MySQL

B. Azure SQL Database

C. Azure Database for MySQL Flexible Server

D. Azure Cosmos DB with Table API

**Correct Answer: C**

**Distractor Analysis:**

- **A (SQL Server on Azure VM running MySQL):** You can install MySQL on an Azure VM (IaaS), but this requires managing the OS, applying MySQL updates, configuring HA, and managing backups manually. It also does not minimize operational overhead. Incorrect.
- **B (Azure SQL Database):** Azure SQL Database uses SQL Server (T-SQL). It is not MySQL — migrating to SQL Server would require application code changes and query compatibility testing. Incorrect.
- **C (Azure Database for MySQL Flexible Server) — CORRECT:** Azure Database for MySQL Flexible Server is a fully managed MySQL service. It supports the same MySQL protocol and SQL dialect as on-premises MySQL, so application code changes are minimal or none. Microsoft manages patching, backups, and HA automatically.
- **D (Azure Cosmos DB with Table API):** Cosmos DB Table API is a key-value NoSQL store compatible with Azure Table Storage — it is not a MySQL replacement and would require complete application redesign. Incorrect.

---

### Question 8

Which of the following correctly describes the difference between Azure SQL Database and Azure SQL Managed Instance?

A. SQL Managed Instance supports the IaaS model; SQL Database is PaaS

B. SQL Managed Instance provides near-full SQL Server compatibility including SQL Agent and linked servers; SQL Database is a subset with limited feature support

C. SQL Database can be deployed in any Azure region; SQL Managed Instance can only be deployed in US regions

D. SQL Managed Instance is less expensive than SQL Database for all workload sizes

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. Both Azure SQL Database and Azure SQL Managed Instance are PaaS services — neither requires OS management by the customer. SQL Server on Azure VM is IaaS.
- **B — CORRECT:** Azure SQL Managed Instance provides near-100% compatibility with on-premises SQL Server, including SQL Server Agent, linked servers, CLR code, Service Broker, and cross-database queries. Azure SQL Database is a cloud-native subset of SQL Server features — advanced features like SQL Agent and linked servers have limited or no support.
- **C:** Incorrect. Both SQL Database and SQL Managed Instance are available in all Azure regions that support Azure SQL services. Regional availability is not a differentiator between the two.
- **D:** Incorrect. Azure SQL Managed Instance generally costs more than an equivalently sized SQL Database deployment because it provides more compute resources and features. It is not less expensive for all workload sizes.

---

### Question 9

A startup wants to run an existing Apache Cassandra application on a managed Azure service without rewriting the application code. Which Azure Cosmos DB API would enable this migration?

A. Core SQL API

B. MongoDB API

C. Gremlin API

D. Cassandra API

**Correct Answer: D**

**Distractor Analysis:**

- **A (Core SQL API):** The Core SQL API uses a JSON document model queried with SQL-like syntax — it is not compatible with Apache Cassandra CQL drivers. An existing Cassandra app would need to be completely rewritten. Incorrect.
- **B (MongoDB API):** The MongoDB API provides compatibility with MongoDB drivers and tools. It does not provide Apache Cassandra compatibility. Incorrect.
- **C (Gremlin API):** The Gremlin API is for graph data using the Apache TinkerPop Gremlin language. It has no relationship to Cassandra. Incorrect.
- **D (Cassandra API) — CORRECT:** Azure Cosmos DB's Cassandra API provides compatibility with the Apache Cassandra CQL (Cassandra Query Language) protocol. Existing Cassandra applications can connect to Cosmos DB using their existing Cassandra drivers with minimal or no code changes, while gaining Cosmos DB's global distribution and managed infrastructure.

---

### Question 10

A company needs to migrate its large on-premises SQL Server database to Azure SQL Database. They want to identify any T-SQL features used in the application that are not supported in Azure SQL Database before beginning the migration. Which Microsoft tool should they use?

A. Azure Database Migration Service (DMS)

B. Azure Migrate

C. Data Migration Assistant (DMA)

D. Azure Advisor

**Correct Answer: C**

**Distractor Analysis:**

- **A (Azure Database Migration Service):** DMS is used to perform the actual database migration — moving data from the source to the target. It does not perform pre-migration compatibility assessment of T-SQL features. Incorrect.
- **B (Azure Migrate):** Azure Migrate is used to discover, assess, and migrate VMs, servers, databases, and web apps. For database-specific compatibility assessment and feature gap analysis, DMA provides more detailed database-level analysis. Incorrect.
- **C (Data Migration Assistant) — CORRECT:** Data Migration Assistant (DMA) specifically analyzes SQL Server databases for feature compatibility with Azure SQL Database and Azure SQL Managed Instance. It identifies breaking changes, deprecated features, and unsupported T-SQL syntax, and provides remediation recommendations before migration begins.
- **D (Azure Advisor):** Azure Advisor provides cost, security, reliability, and performance recommendations for existing Azure resources. It does not assess on-premises SQL Server compatibility for migration. Incorrect.

---

*Quiz 10 — Module 10: Azure Databases | CIS-4331 | Texas Wesleyan University*

---

### Question 11 (5 points)

A company runs an Azure SQL Database and wants to ensure that it automatically scales compute capacity up during peak business hours and down overnight to minimize cost. Which Azure SQL Database feature enables this automatic scaling?

- A) Azure SQL Elastic Pools with autoscale rules based on CPU percentage
- B) Azure SQL Database Serverless tier with auto-pause and auto-resume
- C) Azure SQL Database Active Geo-Replication with a read-only secondary
- D) Azure SQL Managed Instance with automatic failover groups

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure SQL Database Serverless is a compute tier that automatically scales vCores up and down based on workload demand within a configured min/max range. It also supports auto-pause — when the database is idle for a configurable period, compute billing stops completely. When a new connection arrives, the database auto-resumes (with a brief delay). This is ideal for workloads with variable or unpredictable demand.
  - *Why A is incorrect:* Elastic Pools share resources across multiple databases but do not autoscale the pool's total capacity based on CPU metrics automatically. The pool's DTU or vCore maximum is a fixed configuration that requires manual changes to scale.
  - *Why C is incorrect:* Active Geo-Replication creates a readable secondary replica in another region for disaster recovery and read scale-out. It does not scale compute capacity based on demand and does not eliminate costs during idle periods.
  - *Why D is incorrect:* Azure SQL Managed Instance does not have a serverless tier. Automatic failover groups are for high availability and disaster recovery, not compute autoscaling.

---

### Question 12 (5 points)

An application stores user session data in Azure Cosmos DB. The team configures the consistency level to "Eventual." A user updates their shopping cart and then immediately navigates to the cart summary page. What is a potential behavior the user might experience with Eventual consistency?

- A) The cart update operation fails with a consistency violation error
- B) The cart summary page may show the previous state of the cart before the update, because replication has not yet propagated
- C) The cart update is queued and not committed until the user's session ends
- D) The user cannot read from any replica until the write is confirmed by all replicas globally

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Eventual consistency provides the weakest consistency guarantee — reads may return stale data because replicas may not have yet received the latest write. In a multi-region Cosmos DB setup, a read from a different region (or even a different replica in the same region) may return the pre-update state of the cart. The data will eventually converge to the correct state, but not immediately.
  - *Why A is incorrect:* Eventual consistency does not cause operation failures. The write succeeds immediately and is propagated asynchronously. There are no "consistency violation errors" thrown to the application.
  - *Why C is incorrect:* Cosmos DB does not queue writes until session end under any consistency level. Writes are committed to the local replica immediately. Eventual consistency affects how quickly reads on other replicas reflect those writes.
  - *Why D is incorrect:* This describes the behavior of Strong consistency, where reads wait for writes to be confirmed by all replicas before returning. Eventual consistency is the opposite — it returns immediately from the nearest replica without waiting.

---

### Question 13 (5 points)

A company plans to run a complex OLAP (Online Analytical Processing) workload over 20 TB of sales data in Azure Synapse Analytics. They want to pause compute when the analytics team is not working (nights and weekends) to reduce costs, while keeping the data available. Which Synapse Analytics pool type supports this pause/resume capability?

- A) Synapse Serverless SQL Pool
- B) Synapse Dedicated SQL Pool
- C) Synapse Spark Pool
- D) Azure SQL Database Hyperscale

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Synapse Analytics Dedicated SQL Pool supports a pause/resume feature. When paused, compute billing stops while the data remains stored in Azure Data Lake Storage Gen2. When resumed, the compute cluster restarts and queries can execute again. This is specifically designed for workloads with predictable on/off usage patterns where storage costs are acceptable but compute costs during idle periods should be eliminated.
  - *Why A is incorrect:* Synapse Serverless SQL Pool does not have a pause/resume concept — it is serverless and bills per TB of data scanned per query. It is already cost-optimized for ad-hoc queries, but it cannot run the same performance-optimized MPP queries as the Dedicated pool for 20 TB workloads.
  - *Why C is incorrect:* Synapse Spark Pool is for distributed data processing using Apache Spark, not T-SQL analytical queries. Spark pools do auto-pause when not used, but Spark is not the right tool for T-SQL OLAP workloads.
  - *Why D is incorrect:* Azure SQL Database Hyperscale is a single-database OLTP/large database service, not a data warehouse. It does not have a pause/resume feature and is not designed for MPP analytical queries over 20 TB datasets.

---

### Question 14 (5 points)

A development team migrates a MongoDB application to Azure Cosmos DB using the MongoDB API. After migration, they notice that certain complex aggregation pipeline queries run significantly slower on Cosmos DB than on their original MongoDB cluster. What is the most likely architectural reason for this performance difference?

- A) Azure Cosmos DB does not support MongoDB aggregation pipelines
- B) The Cosmos DB partition key was chosen poorly, causing many queries to require cross-partition scans instead of targeting a single partition
- C) Cosmos DB MongoDB API has a hard limit of 400 RU/s that cannot be increased
- D) The MongoDB API is only available in the East US region, adding network latency

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In Cosmos DB, data is physically distributed across partitions based on the partition key. Queries that include the partition key value in their filter can target a single partition (highly efficient). Queries that do not include the partition key (or use a key with poor cardinality) must scan all partitions — this is called a cross-partition query and can be orders of magnitude slower, especially for aggregation pipelines that process many documents.
  - *Why A is incorrect:* Azure Cosmos DB MongoDB API does support aggregation pipelines, including common stages like `$group`, `$match`, `$project`, and `$sort`. Some advanced pipeline operators may have limitations, but basic aggregation pipelines are supported.
  - *Why C is incorrect:* Cosmos DB throughput (RU/s) is not limited to 400 — that is just the minimum for a single container. Throughput can be provisioned in the tens of thousands of RU/s, or unlimited in Autoscale mode. The hard limit is not the cause of slow aggregation.
  - *Why D is incorrect:* The Cosmos DB MongoDB API is available in all Azure regions that support Cosmos DB globally — not just East US. Region availability is not the cause of the performance issue.

---

### Question 15 (5 points)

A company needs its Azure SQL Database to automatically fail over to a secondary region in the event of a regional outage, with read/write capability restored within minutes and no manual intervention required. Which Azure SQL Database feature provides this automated geo-failover capability?

- A) Azure SQL Database backup and restore to a secondary region
- B) Azure SQL Database Auto-failover groups
- C) Azure SQL Database zone-redundant configuration
- D) Azure SQL Managed Instance with manual failover

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure SQL Database Auto-failover groups enable automatic, coordinated failover of one or more databases to a secondary region. In the event of a regional failure, the failover group automatically promotes the secondary to primary, providing a read/write endpoint that the application reconnects to. No manual intervention is required. The failover group provides a geo-readable listener endpoint that always points to the current primary.
  - *Why A is incorrect:* Backup and restore to a secondary region requires manually initiating a restore operation after a disaster, which takes hours. This is not automatic and does not meet the "minutes, no manual intervention" requirement.
  - *Why C is incorrect:* Zone-redundant configuration distributes Azure SQL Database replicas across Availability Zones within a single region, protecting against datacenter failures. It does not provide cross-region protection or automated geo-failover.
  - *Why D is incorrect:* Azure SQL Managed Instance does support auto-failover groups, but this option says "manual failover" — which explicitly contradicts the requirement for automatic failover without manual intervention.

---

### Question 16 (5 points)

A graph database is needed to store and query relationships between users in a social network — modeling connections like "User A follows User B" and queries like "Find all users within 3 hops of User X." Which Azure Cosmos DB API is designed for this graph traversal use case?

- A) Core SQL API (document model)
- B) MongoDB API (document model)
- C) Gremlin API (graph model using Apache TinkerPop)
- D) Cassandra API (wide-column model)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The Gremlin API in Azure Cosmos DB implements the Apache TinkerPop graph traversal framework. Graph databases model data as vertices (entities like users) and edges (relationships like "follows"). Graph traversal queries like "find all users within N hops" are natively efficient in graph databases, whereas the same query in a relational or document model would require complex recursive joins or application-side traversal logic.
  - *Why A is incorrect:* The Core SQL API stores data as JSON documents. Representing social graph traversals in a document model requires complex nested structures or multiple round trips — it is not optimized for multi-hop relationship queries.
  - *Why B is incorrect:* The MongoDB API uses a document model similar to Core SQL. MongoDB does support limited graph-like queries, but it is not a native graph database and does not support efficient multi-hop Gremlin-style traversals.
  - *Why D is incorrect:* The Cassandra API uses a wide-column data model optimized for high-throughput key-based reads and writes. It is not designed for graph traversal or relationship queries.

---

### Question 17 (5 points)

An organization uses Azure SQL Database and wants to understand the Query Performance Insight feature. Which statement correctly describes what this feature provides?

- A) Query Performance Insight automatically optimizes and rewrites slow queries to improve performance
- B) Query Performance Insight shows the top resource-consuming queries (by CPU, duration, and IO) and identifies opportunities for index improvements
- C) Query Performance Insight monitors replication lag between the primary and geo-secondary databases
- D) Query Performance Insight automatically scales the database DTUs when query performance drops below a threshold

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure SQL Database Query Performance Insight is a portal feature that visualizes the top queries consuming the most CPU, I/O, or execution duration. It integrates with the Intelligent Performance recommendations to suggest missing indexes or query parameter issues. It helps DBAs identify performance bottlenecks without needing to query DMVs (Dynamic Management Views) directly.
  - *Why A is incorrect:* Query Performance Insight does not automatically rewrite queries. It provides visibility and recommendations, but query optimization requires a developer or DBA to make code changes.
  - *Why C is incorrect:* Replication lag monitoring is available through geo-replication health views and Azure Monitor metrics. Query Performance Insight focuses on query-level performance analysis, not replication health.
  - *Why D is incorrect:* Automatic DTU/vCore scaling based on query performance is a separate feature (the Serverless tier's autoscale, or manual scaling). Query Performance Insight is a diagnostic and visualization tool, not an autoscaling mechanism.

---

### Question 18 (5 points)

A company stores product inventory in Azure Cosmos DB with a partition key of `/productCategory`. The inventory has 5 categories (Electronics, Clothing, Food, Books, Sports) but 10 million total items. What potential performance problem does this partition key create?

- A) The partition key has too many distinct values, causing excessive partition splits
- B) The partition key has too few distinct values (low cardinality), causing uneven data distribution and "hot partitions" that limit throughput
- C) Cosmos DB does not support string partition keys — only numeric keys are valid
- D) A partition key with 5 distinct values limits the maximum throughput to 5,000 RU/s total

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Cosmos DB distributes data and throughput across logical partitions based on the partition key value. With only 5 categories for 10 million items, most items will be in very few logical partitions. If one category (e.g., Electronics) holds 70% of the items, that partition receives 70% of the read/write traffic — a "hot partition." Cosmos DB limits per-partition throughput to 10,000 RU/s, so a hot partition can become a bottleneck. A good partition key should have high cardinality (thousands or millions of distinct values).
  - *Why A is incorrect:* Low cardinality (too few distinct values) is the problem here, not high cardinality. High cardinality (many distinct values) is actually desirable in Cosmos DB to distribute data evenly.
  - *Why C is incorrect:* Cosmos DB supports string, numeric, and other data types as partition keys. String partition keys are fully supported and very common.
  - *Why D is incorrect:* The number of distinct partition key values does not impose a hard ceiling on total account throughput. Total throughput can be provisioned independently. The problem with 5 partition values is uneven distribution causing hot partitions, not an absolute throughput limit.

---

### Question 19 (5 points)

A company's data engineering team needs to ingest streaming data from IoT devices, transform it with Apache Spark, join it with historical data in a data lake, and expose it to business analysts via SQL queries — all within a single integrated workspace. Which Azure service provides this unified analytics platform?

- A) Azure Databricks (standalone)
- B) Azure SQL Database with Elastic Jobs
- C) Azure Synapse Analytics
- D) Azure Cosmos DB with Synapse Link

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Synapse Analytics is a unified analytics platform that integrates data ingestion (Synapse Pipelines), Apache Spark processing (Synapse Spark Pools), SQL analytics over a data lake (Synapse Serverless SQL), and traditional data warehousing (Synapse Dedicated SQL Pool) — all in a single workspace. It is specifically designed for the end-to-end analytics workflow described.
  - *Why A is incorrect:* Azure Databricks is a powerful Spark-based analytics platform, but it is not a fully unified workspace with native SQL analyst access, data ingestion pipelines, and data lake integration under one portal. It typically requires additional services (Azure Data Factory, Azure Data Lake) to achieve equivalent capability.
  - *Why B is incorrect:* Azure SQL Database with Elastic Jobs is for managing scheduled jobs across multiple SQL databases. It has no Spark processing capability, IoT data ingestion, or data lake integration.
  - *Why D is incorrect:* Azure Cosmos DB with Synapse Link enables analytical queries over Cosmos DB operational data using Synapse Analytics — it is a feature that connects Cosmos DB to Synapse. However, Cosmos DB with Synapse Link alone is not the full unified platform described. The answer is Azure Synapse Analytics, which can include Synapse Link as one of its data sources.

---

### Question 20 (5 points)

A company is evaluating whether to migrate its on-premises MySQL workload to Azure Database for MySQL Flexible Server or to SQL Server on an Azure VM running MySQL. The key requirements are: automated backups, automatic minor version patching, built-in high availability without manual configuration, and no OS management. Which option meets all four requirements?

- A) SQL Server on Azure VM running MySQL — because VMs provide full control over patching schedules
- B) Azure Database for MySQL Flexible Server — because it is a fully managed PaaS service that handles backups, patching, and HA automatically
- C) Both options meet all four requirements equally well
- D) Neither option meets all four requirements — Azure does not provide managed MySQL

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Database for MySQL Flexible Server is a fully managed PaaS database service. It provides: automated backups (point-in-time restore up to 35 days), automatic minor version patching, built-in zone-redundant HA (standby replica in a different zone with automatic failover), and no OS management — Microsoft manages the underlying infrastructure. All four requirements are met natively.
  - *Why A is incorrect:* SQL Server on an Azure VM is an IaaS deployment. The customer manages the OS — including installing MySQL, applying OS and MySQL patches, configuring backup jobs, and setting up replication for HA. None of the four requirements (automated backups, auto-patching, built-in HA, no OS management) are met automatically; all require manual configuration.
  - *Why C is incorrect:* The two options are fundamentally different (PaaS vs. IaaS). The VM option requires manual management of all four items. Only Flexible Server meets all four requirements natively.
  - *Why D is incorrect:* Azure Database for MySQL Flexible Server is a generally available, production-ready managed MySQL service. Azure provides fully managed MySQL — this option is factually incorrect.
