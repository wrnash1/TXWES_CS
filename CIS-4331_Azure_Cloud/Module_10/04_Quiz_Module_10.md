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
