# Video Script: Module 10 — Azure Databases

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure Fundamentals (AZ-900)

---

## Opening (0:00–1:00)

Welcome to Module 10 of CIS-4331 Azure Cloud Computing. I'm Professor Nash. Today we are covering Azure Database Services — Microsoft's portfolio of managed database offerings.

Databases are the backbone of almost every application. Azure provides managed services for relational databases, globally distributed NoSQL databases, and open-source database engines — all with built-in high availability, automatic backups, and security. AZ-900 heavily tests your ability to match the right database service to a given scenario, and to understand the key differences between relational and non-relational data models. By the end of this module, you will have a clear decision framework for every database scenario you encounter.

---

## Section 1: Relational vs. Non-Relational Databases (1:00–4:00)

### The Foundational Distinction

Before we look at specific Azure services, we need to establish the most important distinction in database architecture: relational versus non-relational.

**Relational databases** store data in structured tables with rows and columns. Relationships between tables are defined by primary keys and foreign keys. All queries use SQL (Structured Query Language). The schema — the table structure — is defined before data is inserted. ACID properties (Atomicity, Consistency, Isolation, Durability) ensure data integrity and transactional reliability.

Example: A banking application stores customers in one table, accounts in another, and transactions in a third. A SQL query joins all three tables to show a customer's complete account history.

Azure relational database services: Azure SQL Database, Azure SQL Managed Instance, Azure Database for PostgreSQL, Azure Database for MySQL.

**Non-relational databases**, often called NoSQL, do not use fixed schemas or the SQL relational model. Data is stored in flexible formats: JSON documents, key-value pairs, wide-column tables, or graph structures. NoSQL databases trade some ACID guarantees for horizontal scalability and schema flexibility.

Example: An IoT platform ingests millions of sensor readings per minute. Each sensor type has a different set of fields. A document database accommodates this variable schema without requiring schema changes each time a new sensor type is added.

Azure non-relational database service: Azure Cosmos DB.

---

## Section 2: Azure SQL Database (4:00–8:30)

### What Is Azure SQL Database?

Azure SQL Database is a fully managed PaaS relational database built on the latest stable version of Microsoft SQL Server. Microsoft handles backups, patching, high availability, and infrastructure. You manage your schemas, queries, and application code.

This is the go-to service for cloud-native SQL workloads that need full T-SQL compatibility without infrastructure management.

### Deployment Options

Azure SQL Database has three deployment options.

**Single Database** — An isolated database with its own compute and storage resources. Best for new cloud applications that need a dedicated database.

**Elastic Pool** — Multiple databases share a pool of compute and storage resources. When one database is idle, its unused resources are available to busier databases. This is a cost optimization strategy for SaaS applications managing dozens or hundreds of small databases with variable utilization.

**Hyperscale** — Massively scalable architecture for databases up to 100 TB. Uses a distributed architecture with independent compute and storage scaling. For very large databases.

### Compute Models

Azure SQL Database offers two pricing models.

**DTU model** — Pre-configured bundles of CPU, memory, and I/O called Database Transaction Units. Simpler to understand and configure, but less flexible.

**vCore model** — Independently configure the number of virtual cores, memory tier, and storage. Supports Azure Hybrid Benefit — organizations with existing SQL Server licenses can apply those licenses to Azure SQL Database and save up to 55% in licensing costs.

[SHOW AZURE PORTAL] Navigate to Azure SQL Database > Create. Walk through the single database option. Show the server creation form. Show the DTU vs. vCore compute model selector. Point out the Backup storage redundancy option (LRS, ZRS, GRS).

### Azure SQL Database vs. SQL Server on Azure VM

This is one of the most commonly tested AZ-900 distinctions.

Azure SQL Database is PaaS — Microsoft manages the OS, the SQL Server engine, patching, and backups. You do not have access to the OS.

SQL Server on Azure VM is IaaS — you get a full SQL Server installation on a VM you manage. Full OS access. Full SQL Server feature set including SQL Server Agent, linked servers, CLR, and Service Broker.

When does the scenario call for SQL Server on Azure VM instead of Azure SQL Database? When the application requires SQL Server Agent jobs, linked servers, cross-database transactions, CLR code, or specific SQL Server features not available in PaaS. Or when the organization needs OS-level access for configuration or compliance reasons.

### Azure SQL Managed Instance

Azure SQL Managed Instance sits between Azure SQL Database and SQL Server on Azure VM. It provides near-100% compatibility with on-premises SQL Server 2017+ while still being a fully managed PaaS service. It supports SQL Server Agent, linked servers, CLR, Service Broker, and cross-database queries within the same instance.

Use Managed Instance for migrating existing complex SQL Server applications to Azure without OS-level management and without code rewrites.

---

## Section 3: Azure Cosmos DB (8:30–13:00)

### What Makes Cosmos DB Different?

Azure Cosmos DB is Microsoft's flagship non-relational database. It is globally distributed, multi-model, and designed for applications that require global low-latency access and flexible data models.

Cosmos DB is unique among Azure database services in three critical ways: global distribution, multi-model APIs, and configurable consistency levels.

### Global Distribution

With a few clicks, you can replicate your Cosmos DB data to any Azure region worldwide. Users in Tokyo are served from a replica in Japan East. Users in Dallas are served from South Central US. Read latency is in single-digit milliseconds from any Azure region globally.

You can also enable multi-region writes — allowing applications to write to the nearest region, with replication happening automatically.

### Multi-Model APIs

Cosmos DB supports multiple data model APIs, allowing existing applications built on other platforms to migrate to Cosmos DB with minimal code changes.

**Core SQL API** — Stores JSON documents, queried using a SQL-like syntax. The most common API.

**MongoDB API** — Compatible with MongoDB drivers and tools. Existing MongoDB applications can connect to Cosmos DB using their MongoDB client.

**Cassandra API** — Compatible with Apache Cassandra. Wide-column data model.

**Gremlin API** — Graph data. Vertices and edges for relationship-heavy data.

**Table API** — Compatible with Azure Table Storage. Key-value pairs.

[SHOW AZURE PORTAL] Navigate to Azure Cosmos DB > Create. Show the API selection: Core SQL, MongoDB, Cassandra, Gremlin, Table. Show the Geo-Redundancy option and the multi-region write toggle.

### Five Consistency Levels

This is a key differentiator tested on AZ-900. Cosmos DB lets you choose the trade-off between consistency and latency.

**Strong** — Every read reflects the most recent committed write. Highest latency. Lowest availability. Use for: financial transactions, inventory management.

**Bounded Staleness** — Reads lag behind writes by a configurable time window or number of versions. Predictable staleness. Use for: collaborative apps, leaderboards.

**Session** — Consistent reads within a single client session. Default level. Use for: shopping carts, user profiles.

**Consistent Prefix** — Reads never see out-of-order writes. Read could be stale but never "jumbled." Use for: log aggregation.

**Eventual** — Lowest latency, weakest consistency. Replicas eventually converge. Use for: IoT telemetry, social media likes where absolute accuracy is not critical.

### Cosmos DB SLA

Cosmos DB provides a 99.999% SLA (five nines) for multi-region read and write availability. This is the highest SLA of any Azure database service — higher than Azure SQL Database's 99.99%.

---

## Section 4: Azure Database for PostgreSQL and MySQL (13:00–15:30)

### Open-Source Managed Databases

Azure provides fully managed versions of the three major open-source relational databases: PostgreSQL, MySQL, and MariaDB.

**Azure Database for PostgreSQL** — Fully managed PostgreSQL with automatic backups, scaling, and high availability. Flexible Server is the current recommended deployment model. PostgreSQL is known for its ANSI SQL compliance and extensive extension ecosystem (including PostGIS for geospatial data). Scenario signal: "PostgreSQL," "open-source relational," "advanced SQL compliance."

**Azure Database for MySQL** — Fully managed MySQL. Flexible Server deployment. Supports MySQL 5.7 and 8.0. MySQL is the dominant open-source database for web applications and the "M" in the LAMP stack (Linux, Apache, MySQL, PHP). Scenario signal: "MySQL," "LAMP stack," "WordPress," "PHP web application."

**Azure Database for MariaDB** — Fully managed MariaDB, a community fork of MySQL. Note: Azure Database for MariaDB is being retired — Microsoft recommends migrating to Azure Database for MySQL Flexible Server. It may appear on older AZ-900 exam versions.

All three services provide automatic backups, built-in high availability, automatic patching, and Azure Active Directory (Entra ID) authentication.

---

## Section 5: Azure Synapse Analytics (15:30–17:30)

### What Is Azure Synapse?

Azure Synapse Analytics is a cloud analytics service that brings together data warehousing and big data analytics into a single unified service. It is designed for analytical workloads — running complex queries across massive datasets for business intelligence and reporting.

Key Synapse capabilities:

**Dedicated SQL pools** — Previously known as Azure SQL Data Warehouse. Massively parallel processing (MPP) for petabyte-scale analytics.

**Serverless SQL pool** — Query data in Azure Data Lake storage using T-SQL without provisioning compute. Pay-per-query.

**Apache Spark pools** — Run Spark-based data engineering and machine learning workloads.

**Data integration** — Built-in data integration pipelines similar to Azure Data Factory.

Synapse is the answer when a scenario describes large-scale analytics, business intelligence reporting across massive datasets, or data warehousing.

[SHOW AZURE PORTAL] Navigate to Azure Synapse Analytics > Create. Show the Synapse workspace creation. Show the overview of the different pool types.

---

## Section 6: Database Migration and Choosing the Right Service (17:30–20:30)

### Azure Database Migration Service

Azure Database Migration Service is a fully managed tool for migrating databases to Azure. It supports migrations from:

- SQL Server (on-premises or on VM) to Azure SQL Database / Azure SQL Managed Instance
- MySQL to Azure Database for MySQL
- PostgreSQL to Azure Database for PostgreSQL
- Oracle to Azure SQL Database (with Schema Conversion Tool)

The migration tool provides an online migration option (minimal downtime using continuous sync) and an offline migration option (one-time full backup restore, requires planned downtime).

### Choosing the Right Database Service

Let me give you the AZ-900 decision framework.

**Does the data have a fixed schema and use SQL?** → Relational database.

**Does the data need flexible schema, global distribution, or variable data models?** → Azure Cosmos DB.

**For relational databases — what engine?**

- SQL Server / T-SQL, new cloud-native app → Azure SQL Database
- SQL Server with full feature set (SQL Agent, linked servers), PaaS preferred → Azure SQL Managed Instance
- SQL Server, OS access required → SQL Server on Azure VM
- PostgreSQL → Azure Database for PostgreSQL
- MySQL → Azure Database for MySQL

**Is the workload analytical (reporting, BI, data warehouse)?** → Azure Synapse Analytics.

**Is global distribution with single-digit millisecond latency required?** → Azure Cosmos DB.

---

## Closing (20:30–21:30)

Today we covered Azure's full database portfolio. You now understand the relational vs. non-relational distinction, the three SQL Server deployment options (SQL Database, Managed Instance, SQL Server on VM), Cosmos DB's global distribution and five consistency levels, the open-source managed databases for PostgreSQL and MySQL, and Azure Synapse Analytics for analytical workloads.

In your lab this week, you will create an Azure SQL Database, connect to it using the Azure Portal Query Editor, create a table, and insert records. This gives you hands-on experience with the foundational PaaS database model.

In Module 11, we cover Azure Identity, Security, and Governance — Azure Active Directory, MFA, RBAC, and Azure Policy. See you there.

---

*End of Script — Module 10*
