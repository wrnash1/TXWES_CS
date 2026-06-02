# Reading Guide: Module 07 - Azure Database Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## Introduction

Azure provides a comprehensive set of managed database services covering relational SQL engines, globally distributed NoSQL, and open-source databases. Understanding which service matches which workload type is one of the most consistently tested competencies on AZ-900. This guide provides the depth required for both the exam and practical database architecture decisions.

---

## Section 1: Relational vs. Non-Relational Data Models

### 1.1 Relational Databases

Relational databases organize data into tables (relations) with rows (records) and columns (attributes). Relationships between tables are defined using primary keys and foreign keys. Queries use SQL (Structured Query Language).

Characteristics:

- Fixed schema — table structure defined before data is inserted
- ACID transactions (Atomicity, Consistency, Isolation, Durability)
- Strong data integrity through constraints and foreign key enforcement
- Vertical scaling (scale up) traditionally; horizontal sharding is complex
- Best for: structured data with predictable schema, transactional workloads, reporting

Examples of relational Azure services: Azure SQL Database, Azure Database for PostgreSQL, Azure Database for MySQL.

### 1.2 Non-Relational (NoSQL) Databases

Non-relational databases do not enforce a fixed schema and do not use the SQL relational model. Data is stored in flexible formats.

NoSQL data models:

| Model | Description | Azure Example |
|---|---|---|
| Document | JSON documents; flexible per-document schema | Cosmos DB Core SQL/MongoDB API |
| Key-Value | Simple key-to-value pairs; fastest lookups | Cosmos DB Table API, Azure Table Storage |
| Column-Family | Wide rows with variable columns per row | Cosmos DB Cassandra API |
| Graph | Nodes and edges representing entities and relationships | Cosmos DB Gremlin API |

Characteristics:

- Schema-flexible — different records can have different fields
- Designed for horizontal scaling (sharding across nodes)
- Often sacrifice some ACID guarantees for performance and availability
- Best for: variable schema, high-velocity data ingestion, global distribution, flexible querying

---

## Section 2: Azure SQL Database

### 2.1 Overview

Azure SQL Database is a fully managed PaaS relational database engine built on the latest stable version of Microsoft SQL Server. Microsoft handles patching, backups, high availability, and infrastructure management. The customer manages schemas, queries, application code, and data.

### 2.2 Deployment Options

| Option | Description | Use Case |
|---|---|---|
| Single Database | Isolated database with dedicated resources | New cloud applications, isolated workloads |
| Elastic Pool | Multiple databases share a resource pool | Many databases with variable utilization |
| Hyperscale | Massively scalable up to 100 TB | Very large databases, read-scale-out needed |

### 2.3 Compute Models

| Model | Description | Best For |
|---|---|---|
| DTU (Database Transaction Unit) | Pre-configured bundles of CPU, memory, I/O | Simple pricing, predictable workloads |
| vCore | Independently configure CPU and memory; Azure Hybrid Benefit eligible | Precise sizing, license portability |

Azure Hybrid Benefit: Organizations with existing SQL Server licenses with Software Assurance can apply those licenses to Azure SQL Database, significantly reducing cost.

### 2.4 High Availability and Backup

Azure SQL Database provides:

- Automatic point-in-time backup (up to 35-day retention in premium tiers)
- Automated patching — zero downtime for minor versions
- Zone-redundant configuration available in Business Critical and Premium tiers
- Active Geo-Replication: create readable secondary replicas in up to four secondary regions
- Auto-Failover Groups: automatic regional failover with a single DNS endpoint

### 2.5 Azure SQL Database vs. SQL Server on Azure VM

| Factor | Azure SQL Database (PaaS) | SQL Server on Azure VM (IaaS) |
|---|---|---|
| OS access | No | Full |
| SQL Server Agent | Limited | Full |
| Linked servers | Limited | Full |
| CLR (Common Language Runtime) | Limited | Full |
| Cross-database queries | Within same server | Full |
| Service Broker | No | Yes |
| Patching | Automatic | Customer responsibility |
| Backup | Automatic | Customer responsibility |
| HA configuration | Automatic | Customer-configured |
| Migration complexity | Varies (feature compatibility) | Low (lift-and-shift) |

Decision rule for AZ-900: If a scenario mentions SQL Server Agent jobs, linked servers, or "full SQL Server compatibility," and PaaS is not acceptable, the answer is SQL Server on Azure VM. For new cloud-native SQL workloads, Azure SQL Database is preferred.

### 2.6 Azure SQL Managed Instance

SQL Managed Instance fills the gap between Azure SQL Database and SQL Server on VM:

- Near 100% compatibility with on-premises SQL Server 2017+
- Supports SQL Server Agent, linked servers, CLR, Service Broker, cross-database queries
- Fully managed PaaS (no OS access)
- Deployed into a Virtual Network for private network access
- Ideal for: migrating existing SQL Server applications that need PaaS management without code changes

---

## Section 3: Azure Cosmos DB

### 3.1 Overview

Azure Cosmos DB is Microsoft's globally distributed, multi-model NoSQL database. It is designed for applications requiring global low-latency access and flexible data models. Cosmos DB is the most premium and most capable Azure database service, and it is the most AZ-900-tested database differentiation topic.

### 3.2 Global Distribution

Cosmos DB can be configured to replicate data to any combination of Azure regions with a few clicks. Adding a region adds a read replica. Write regions can also be distributed for multi-region write scenarios.

Benefits:

- Read latency under 10 milliseconds from any Azure region globally
- Data served from the nearest replica to each user
- Multi-master writes: write to the closest region, replicate globally

### 3.3 APIs and Data Models

Cosmos DB presents different APIs that expose different data models:

| API | Data Model | Protocol Compatible With |
|---|---|---|
| Core (SQL) | Documents (JSON) | SQL-like query language |
| MongoDB API | Documents (BSON) | MongoDB drivers and tools |
| Cassandra API | Wide-column | Apache Cassandra clients |
| Gremlin API | Graph (vertices + edges) | Apache TinkerPop Gremlin |
| Table API | Key-value | Azure Table Storage |

The MongoDB, Cassandra, Gremlin, and Table APIs allow existing applications built for those platforms to migrate to Cosmos DB with minimal code changes.

### 3.4 Consistency Models

Cosmos DB provides five configurable consistency levels — a unique feature not offered by other Azure database services.

| Consistency Level | Description | Latency | Availability | Use Case |
|---|---|---|---|---|
| Strong | Every read reflects the most recent write | Highest | Lower | Financial transactions, inventory |
| Bounded Staleness | Reads lag by configurable time or version count | High | Higher | Collaborative apps, leaderboards |
| Session | Consistency within a client session | Medium | High | Shopping cart, user profile |
| Consistent Prefix | Never see out-of-order writes | Low | Higher | Log aggregation |
| Eventual | Lowest latency, weakest guarantee — replicas eventually converge | Lowest | Highest | IoT telemetry, social media likes |

### 3.5 SLA Commitments

| Metric | SLA |
|---|---|
| Single-region read availability | 99.99% |
| Single-region write availability | 99.99% |
| Multi-region read availability | 99.999% |
| Multi-region write availability | 99.999% |

Cosmos DB's 99.999% (five nines) multi-region SLA is the highest of any Azure database service.

### 3.6 Pricing Model

Cosmos DB bills based on Request Units (RUs) and storage:

- Request Unit (RU): normalized unit of CPU, memory, and I/O for a database operation
- Provisioned throughput: you reserve RU/s (RUs per second) in advance
- Autoscale: automatically scales between minimum and maximum RU/s based on demand
- Serverless: pay per actual RU consumed with no minimum (best for irregular workloads)

---

## Section 4: Open-Source Managed Database Services

### 4.1 Azure Database for PostgreSQL

Fully managed PostgreSQL database service. Microsoft manages the server infrastructure, OS, and database engine patches.

Key features:

- Flexible Server deployment model (current recommended option)
- PostgreSQL versions 11-16 supported
- Zone-redundant high availability
- Built-in connection pooling (pgBouncer) in Flexible Server
- Supports popular PostgreSQL extensions (PostGIS, pg_cron, etc.)

Use case signals: "PostgreSQL," "advanced SQL compliance," "open-source relational," "GIS/geospatial data."

### 4.2 Azure Database for MySQL

Fully managed MySQL database service.

Key features:

- Flexible Server deployment model
- MySQL 5.7 and 8.0 supported
- Zone-redundant HA with automatic failover
- Read replicas for scale-out of read workloads

Use case signals: "MySQL," "LAMP stack," "WordPress," "PHP web application."

### 4.3 Azure Database for MariaDB

Fully managed MariaDB (MySQL-compatible open-source fork).

Use case signals: "MariaDB," "open-source MySQL fork."

Note: Azure Database for MariaDB is scheduled for retirement — Microsoft encourages migration to Azure Database for MySQL Flexible Server. Be aware this may appear on AZ-900 but understand it is being deprecated.

### 4.4 Open-Source Database Comparison

| Service | Engine | Version Support | AZ-900 Use Case Trigger |
|---|---|---|---|
| Azure Database for PostgreSQL | PostgreSQL | 11-16 | "PostgreSQL," advanced SQL, geospatial |
| Azure Database for MySQL | MySQL | 5.7, 8.0 | "MySQL," LAMP, web apps |
| Azure Database for MariaDB | MariaDB | 10.2, 10.3 | "MariaDB" (deprecated path) |
| Azure SQL Database | SQL Server | Latest stable | "SQL Server," enterprise, T-SQL |

---

## Section 5: Database Service Selection Framework

### 5.1 Decision Tree

Use this framework for AZ-900 scenario questions:

**Step 1 — Is the data relational (structured, fixed schema) or non-relational (flexible, variable schema)?**

- Relational → proceed to Step 2
- Non-relational → Azure Cosmos DB

**Step 2 — What database engine is required?**

- SQL Server / T-SQL → proceed to Step 3
- PostgreSQL → Azure Database for PostgreSQL
- MySQL → Azure Database for MySQL
- MariaDB → Azure Database for MariaDB

**Step 3 — What level of SQL Server compatibility and management is needed?**

- Standard SQL operations, new application, PaaS preferred → Azure SQL Database
- Full SQL Server compatibility (SQL Agent, linked servers, CLR), PaaS preferred → Azure SQL Managed Instance
- Full OS access required, specific SQL Server version, or unsupported features → SQL Server on Azure VM

### 5.2 Summary Comparison Table

| Service | Model | Engine | Global Distribution | Best For |
|---|---|---|---|---|
| Azure SQL Database | PaaS | SQL Server | Limited (geo-replication) | New SQL applications |
| Azure SQL Managed Instance | PaaS | Full SQL Server | Limited | SQL Server migration, full features |
| SQL Server on Azure VM | IaaS | Full SQL Server | Manual setup | OS access needed, full compat |
| Azure Cosmos DB | PaaS (NoSQL) | Multi-model | Native, any region | Global, variable schema, NoSQL |
| Azure Database for PostgreSQL | PaaS | PostgreSQL | Read replicas | Open-source, PostgreSQL apps |
| Azure Database for MySQL | PaaS | MySQL | Read replicas | Open-source, web apps |

---

## Section 6: Azure CLI Commands for Databases

```bash
# Create an Azure SQL Server (logical server)
az sql server create \
  --name "lab07sqlserver[initials]" \
  --resource-group "lab07-rg" \
  --location "eastus" \
  --admin-user "sqladmin" \
  --admin-password "SecurePass123!"

# Create an Azure SQL Database
az sql db create \
  --resource-group "lab07-rg" \
  --server "lab07sqlserver[initials]" \
  --name "lab07db" \
  --service-objective "S0"

# Show SQL Database details
az sql db show \
  --resource-group "lab07-rg" \
  --server "lab07sqlserver[initials]" \
  --name "lab07db"

# Configure SQL Server firewall to allow Azure services
az sql server firewall-rule create \
  --resource-group "lab07-rg" \
  --server "lab07sqlserver[initials]" \
  --name "AllowAzureServices" \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0

# Create a Cosmos DB account
az cosmosdb create \
  --name "lab07cosmos[initials]" \
  --resource-group "lab07-rg" \
  --default-consistency-level Session

# Create a Cosmos DB database
az cosmosdb sql database create \
  --account-name "lab07cosmos[initials]" \
  --resource-group "lab07-rg" \
  --name "lab07db"
```

Reference: learn.microsoft.com/en-us/cli/azure/sql

---

## Section 7: AZ-900 Exam Tips

1. **PaaS vs. IaaS for SQL:** Azure SQL Database and Azure Database for PostgreSQL/MySQL are PaaS — Microsoft manages the OS and engine. SQL Server on Azure VM is IaaS — you manage the OS. If a scenario mentions "manage the OS" or "full SQL Server features," IaaS is the answer.

2. **Cosmos DB global distribution:** When a scenario uses words like "global," "low latency for users worldwide," "multiple regions simultaneously," or "millisecond response globally," Cosmos DB is likely the answer. No other Azure database service provides native global distribution.

3. **Cosmos DB consistency levels:** Cosmos DB is the only Azure database service with configurable consistency levels (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual). If the exam asks about consistency models for a database service, the answer involves Cosmos DB.

4. **Cosmos DB SLA:** The 99.999% multi-region SLA is the highest of any Azure database service. If a scenario requires five-nines availability for a database, Cosmos DB is the answer.

5. **SQL Managed Instance vs. SQL Database:** SQL Managed Instance supports SQL Server Agent, linked servers, CLR, and Service Broker. Azure SQL Database has limited support for these. If a scenario mentions migrating a complex on-premises SQL Server application that uses these features, SQL Managed Instance is the answer (not a basic SQL Database).

6. **Open-source signals:** "LAMP stack," "WordPress," "PHP application" → MySQL. "Advanced SQL compliance," "geospatial data," "PostgreSQL extension" → PostgreSQL. "MariaDB" → Azure Database for MariaDB.

7. **Cosmos DB multi-model:** Cosmos DB supports multiple APIs (SQL, MongoDB, Cassandra, Gremlin, Table). An existing MongoDB application can migrate to Cosmos DB using the MongoDB API with minimal code changes. This is tested as a migration scenario.

8. **Elastic Pool use case:** Multiple databases with variable and unpredictable utilization patterns benefit from Elastic Pools — they share a resource pool, so an active database can use the compute of idle databases. This is a cost optimization tool.

---

## Section 8: Required Resources

- Azure SQL Database overview: learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview
- Azure Cosmos DB introduction: learn.microsoft.com/en-us/azure/cosmos-db/introduction
- Azure Database for PostgreSQL: learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview
- Azure Database for MySQL: learn.microsoft.com/en-us/azure/mysql/flexible-server/overview
- Microsoft Learn AZ-900 database module: learn.microsoft.com/en-us/training/modules/azure-database-fundamentals/

---

## Section 9: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the database service summary comparison table (Section 5.2)
- [ ] Work through the decision tree in Section 5.1 using your own scenarios
- [ ] Memorize the Cosmos DB consistency models table (Section 3.4)
- [ ] Complete the Microsoft Learn "Explore Azure database and analytics services" module
- [ ] Complete Lab Activity Module 07
- [ ] Take Quiz Module 07
- [ ] Post Discussion Module 07 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM
