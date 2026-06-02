# Video Script: Module 07 - Azure Database Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 07: Azure Database Services"]**

Welcome to Module 07. I'm Professor Nash. Today we cover Azure Database Services — the managed database offerings that let you run SQL Server, PostgreSQL, MySQL, MariaDB, and globally distributed NoSQL databases without managing database engine software yourself.

Azure's database services are a critical section of AZ-900. The exam tests your ability to match database scenarios to the correct Azure service and to understand the fundamental differences between relational and non-relational databases.

By the end of this module you will be able to:

- Describe Azure SQL Database and its relationship to SQL Server
- Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VM
- Describe Azure Cosmos DB and explain its globally distributed architecture
- Identify Azure Database for PostgreSQL, MySQL, and MariaDB as open-source managed offerings
- Choose the appropriate database service for a given scenario
- Explain the difference between relational and non-relational data models

---

## [01:30 - 05:00] Relational vs. Non-Relational Databases

**[SLIDE: "Two Data Models for AZ-900"]**

Before we look at specific Azure services, let's establish the foundational distinction between relational and non-relational databases — because this distinction determines which Azure database service you recommend in any scenario.

**Relational databases** store data in structured tables with rows and columns. Relationships between tables are defined by foreign keys. The schema (table structure) is defined before data is inserted. Relational databases use SQL (Structured Query Language) for queries. ACID properties — Atomicity, Consistency, Isolation, Durability — ensure data integrity.

Example: A banking system stores customers in one table, accounts in another, and transactions in a third. A transaction query joins all three tables to show a customer's full account history.

Azure relational database services: Azure SQL Database, Azure SQL Managed Instance, Azure Database for PostgreSQL, Azure Database for MySQL.

**Non-relational databases** (often called NoSQL) do not use fixed schemas or table-and-column structures. They store data in flexible formats: documents (JSON), key-value pairs, column families, or graphs. They trade ACID guarantees for flexibility and horizontal scalability.

Example: An IoT platform stores millions of sensor readings per minute. Each reading has a slightly different set of fields depending on the sensor type. A document database accommodates this variable schema without requiring table schema changes.

Azure non-relational database service: Azure Cosmos DB.

---

## [05:00 - 11:00] Azure SQL Database

**[SLIDE: "Azure SQL Database"]**

Azure SQL Database is a fully managed PaaS relational database built on the latest stable version of Microsoft SQL Server. It handles backup, patching, high availability, and scaling automatically — you manage your schemas and queries, not the database engine infrastructure.

Key characteristics:

**Fully managed PaaS:** No OS, no SQL Server installation, no patching. Microsoft manages the entire stack below your database.

**Built on SQL Server:** Uses the same T-SQL dialect, same compatibility levels, same tools (SQL Server Management Studio, Azure Data Studio). Migrating an existing SQL Server database is often straightforward.

**Deployment options:**

Single Database — an isolated database with its own resources and its own DTU or vCore allocation. Best for new cloud applications.

Elastic Pool — multiple databases share a pool of compute and storage resources. Best when multiple databases have variable and unpredictable utilization patterns — they share the pool rather than each sitting idle.

**Compute models:**

DTU (Database Transaction Unit) model: pre-packaged bundles of compute, storage, and I/O. Simple pricing, less flexible.

vCore model: independently configure CPU, memory, and storage. Enables Azure Hybrid Benefit (use existing SQL Server licenses). Preferred for new deployments.

**High availability:** Built-in zone-redundant configuration available in premium tiers. Automatic failover with no data loss.

**[SHOW PORTAL — Navigate to Azure SQL Database creation blade]**

Here in the Portal, creating a SQL Database requires specifying a server (logical container for one or more databases), the compute tier, and backup settings. Notice the comparison between DTU and vCore models — for most scenarios, vCore gives more flexibility.

**[SLIDE: "Azure SQL Database vs. SQL Server on Azure VM"]**

A common exam question: when do you use Azure SQL Database versus SQL Server on an Azure VM?

Azure SQL Database (PaaS) characteristics:

- No OS management
- Automatic patching, backup, HA
- Supports most SQL Server features
- Cannot access OS or SQL Server agent jobs natively

SQL Server on Azure VM (IaaS) characteristics:

- Full SQL Server instance with all features
- Full OS access
- Can run SQL Server Agent, linked servers, CLR, etc.
- You manage OS patching, backups, and HA configuration
- Required for: applications needing SQL Server Agent, cross-database transactions, features not supported in Azure SQL Database

If the scenario mentions needing a specific SQL Server feature not available in PaaS, or needing OS-level access, the answer is SQL Server on Azure VM.

**[SLIDE: "Azure SQL Managed Instance"]**

Azure SQL Managed Instance is the middle tier between SQL Database and SQL Server on VM. It provides near-100% compatibility with on-premises SQL Server while still being a fully managed PaaS service. Managed Instance supports:

- SQL Server Agent jobs
- Linked servers
- Cross-database queries within the same instance
- CLR (Common Language Runtime)
- Service Broker

Use Managed Instance for: migrating existing SQL Server applications with advanced features that Azure SQL Database does not support, when full IaaS management is not desired.

---

## [11:00 - 16:00] Azure Cosmos DB

**[SLIDE: "Azure Cosmos DB — Globally Distributed NoSQL"]**

Azure Cosmos DB is Microsoft's globally distributed, multi-model NoSQL database service. It is the most premium and most powerful database service in Azure's portfolio — and one of the most AZ-900-tested.

Key characteristics that distinguish Cosmos DB from every other Azure database service:

**Global distribution:** With a few clicks or CLI commands, you can replicate your data to any Azure region worldwide. Users in Tokyo get data from a replica in Japan East. Users in Dallas get data from a replica in South Central US. Latency for reads is in single-digit milliseconds globally.

**Multi-model:** Cosmos DB natively supports multiple data models through different APIs:

- Core SQL API (documents, JSON — the most common)
- MongoDB API (compatible with MongoDB applications)
- Cassandra API (compatible with Apache Cassandra applications)
- Gremlin API (graph data)
- Table API (compatible with Azure Table Storage)

**Five consistency models:** This is a key AZ-900 differentiator. Cosmos DB lets you choose the consistency-vs-latency trade-off:

- Strong: Read returns the most recently committed write. Highest latency.
- Bounded Staleness: Reads lag behind writes by a configurable time or version count.
- Session: Consistent reads within a client session.
- Consistent Prefix: Reads never see out-of-order writes.
- Eventual: Lowest latency, weakest consistency. Replicas eventually converge.

**SLA commitments:** Cosmos DB provides 99.999% SLA (five nines) for multi-region read and write availability. This is the highest SLA of any Azure database service.

**[SLIDE: "When to Use Cosmos DB"]**

Use Cosmos DB for:

- Applications requiring global low-latency reads and writes
- Applications with variable or unpredictable schema (documents, JSON)
- IoT platforms with massive ingestion rates
- Gaming applications requiring single-digit millisecond response times
- Multi-model data (your app uses both document and graph queries)
- Applications already built on MongoDB, Cassandra, or Gremlin that need managed infrastructure

Do not use Cosmos DB for:

- Standard relational/SQL workloads (use Azure SQL Database)
- Budget-sensitive applications with predictable structured data (Cosmos DB is expensive)

---

## [16:00 - 19:00] Open-Source Database Services

**[SLIDE: "Azure Database for PostgreSQL, MySQL, and MariaDB"]**

Azure provides fully managed versions of the three major open-source relational databases:

**Azure Database for PostgreSQL:** Fully managed PostgreSQL with automatic backups, scaling, and high availability. Supports PostgreSQL extensions. Available in Flexible Server configuration (more control) and previously as Single Server (now retired for new deployments). PostgreSQL is popular for its ANSI SQL compliance and advanced features.

**Azure Database for MySQL:** Fully managed MySQL. Flexible Server configuration. Supports MySQL 5.7 and 8.0. Popular for web applications — the "M" in LAMP and MEAN stacks.

**Azure Database for MariaDB:** Fully managed MariaDB, a community-developed MySQL fork. Available as a fully managed service. MariaDB is popular in the open-source community for its GPL license.

All three services provide: automatic backups, built-in high availability, automatic patching, vertical and horizontal scaling, and Azure Active Directory authentication.

**[SLIDE: "Open-Source Database Comparison"]**

| Service | Engine | AZ-900 Use Case Signal |
|---|---|---|
| Azure SQL Database | SQL Server (T-SQL) | Microsoft stack, existing SQL Server, enterprise |
| Azure Database for PostgreSQL | PostgreSQL | Open-source, advanced SQL compliance |
| Azure Database for MySQL | MySQL | LAMP stack, web applications |
| Azure Database for MariaDB | MariaDB | Open-source MySQL fork |
| Azure Cosmos DB | NoSQL multi-model | Global distribution, variable schema, NoSQL |

---

## [19:00 - 22:30] Lab Preview and Exam Alignment

**[SLIDE: "Module 07 Lab"]**

In today's lab, you will create an Azure SQL Database using the Azure Portal and connect to it using the built-in Query Editor. You will create a table, insert sample data, and run basic queries. This hands-on experience demonstrates the PaaS database model — you interact with a fully functional SQL database without ever touching a server OS.

**[SLIDE: "AZ-900 Exam Alignment"]**

The highest-frequency database exam topics:

- Azure SQL Database is PaaS — no OS management. SQL Server on VM is IaaS — full OS access.
- Cosmos DB's global distribution with single-digit millisecond latency is its primary differentiator. If a scenario mentions "global" and "low latency" together, Cosmos DB is likely the answer.
- Cosmos DB supports five consistency levels — this is unique among Azure database services.
- Azure Database for PostgreSQL/MySQL/MariaDB are fully managed open-source database engines.

---

## [22:30 - 24:00] Closing

**[INSTRUCTOR ON CAMERA]**

You now understand Azure's database landscape — from SQL Server to open-source relational databases to globally distributed NoSQL with Cosmos DB. The relational vs. non-relational distinction is fundamental, and the PaaS vs. IaaS distinction (SQL Database vs. SQL Server on VM) appears on every AZ-900 exam I have seen reviewed.

In Module 08, we start the security and identity section of the course with Microsoft Entra ID — the identity backbone of Azure and Microsoft 365. I will see you there.

---

**References:**

- learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview
- learn.microsoft.com/en-us/azure/cosmos-db/introduction
- learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview
