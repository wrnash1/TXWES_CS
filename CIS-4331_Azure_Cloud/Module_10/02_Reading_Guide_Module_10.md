# Reading Guide: Module 10 — Azure Databases

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

---

## Introduction

Azure's database portfolio spans managed relational engines, globally distributed NoSQL, open-source database services, and enterprise analytics. AZ-900 tests your ability to identify the correct database service for a scenario and understand the fundamental differences between relational and non-relational models. This guide provides detailed comparisons, decision frameworks, and exam tips for every database service on the exam.

---

## Section 1: Relational vs. Non-Relational Data Models

### 1.1 Relational Databases

Relational databases store data in tables (relations) with rows (records) and columns (attributes). The schema is defined before data is written. Tables are linked by primary and foreign keys.

Core properties:

| Property | Detail |
|---|---|
| Schema | Fixed; defined at table creation |
| Query language | SQL (Structured Query Language) |
| Transactions | ACID (Atomicity, Consistency, Isolation, Durability) |
| Scaling | Vertical (scale up) primary; horizontal sharding is complex |
| Best for | Structured data, transactional workloads, reporting |

Azure relational services: Azure SQL Database, Azure SQL Managed Instance, Azure Database for PostgreSQL, Azure Database for MySQL, Azure Database for MariaDB.

### 1.2 Non-Relational (NoSQL) Databases

Non-relational databases do not require a fixed schema. Data models vary by type:

| NoSQL Model | Storage Format | Azure Implementation |
|---|---|---|
| Document | JSON documents with flexible per-document schema | Cosmos DB Core SQL / MongoDB API |
| Key-Value | Simple key → value pairs | Cosmos DB Table API, Azure Table Storage |
| Wide-Column | Rows with variable column sets per row | Cosmos DB Cassandra API |
| Graph | Nodes (entities) + edges (relationships) | Cosmos DB Gremlin API |

Core properties:

| Property | Detail |
|---|---|
| Schema | Flexible; each record can have different fields |
| Query language | Varies by API |
| Consistency | Configurable (eventual to strong) |
| Scaling | Horizontal (built-in sharding) |
| Best for | Variable schema, global distribution, high velocity, flexible queries |

---

## Section 2: Azure SQL Database

### 2.1 Service Overview

Azure SQL Database is a fully managed PaaS relational database built on Microsoft SQL Server. It provides cloud-native SQL capabilities without OS or engine management.

Managed by Microsoft:

- Operating system
- SQL Server engine upgrades and patches
- Backup (point-in-time, up to 35-day retention in premium tiers)
- High availability and failover

Managed by customer:

- Database schema and stored procedures
- Application code and connection strings
- Performance tuning and index management
- Data and query security

### 2.2 Deployment Models

| Model | Description | Best For |
|---|---|---|
| Single Database | Isolated database with dedicated resources | New cloud applications |
| Elastic Pool | Multiple databases share a resource pool | SaaS apps with many variable-load databases |
| Hyperscale | Up to 100 TB; distributed architecture | Very large databases needing massive scale |

### 2.3 Compute Models

| Model | Configuration | Azure Hybrid Benefit | Best For |
|---|---|---|---|
| DTU | Pre-bundled compute + storage + I/O | No | Simple pricing, predictable workloads |
| vCore | Independent CPU, memory, storage selection | Yes (up to 55% savings) | Precise sizing, license portability |

### 2.4 SQL Deployment Option Comparison

| Factor | Azure SQL Database | Azure SQL Managed Instance | SQL Server on Azure VM |
|---|---|---|---|
| Service model | PaaS | PaaS | IaaS |
| OS access | No | No | Full |
| SQL Server Agent | Limited | Full | Full |
| Linked servers | Limited | Full | Full |
| Cross-database queries | Within same server | Full (same instance) | Full |
| CLR code | Limited | Full | Full |
| Service Broker | No | Yes | Yes |
| Database version | Latest stable | SQL Server 2017+ compatible | Any SQL Server version |
| Patching | Automatic | Automatic | Customer responsibility |
| Backup | Automatic | Automatic | Customer responsibility |
| Migration ease | Varies (feature check needed) | Near lift-and-shift | Full lift-and-shift |

### 2.5 High Availability Options

| Feature | Description |
|---|---|
| Zone-redundant configuration | Deploys replicas across Availability Zones in premium/business critical tiers |
| Active Geo-Replication | Up to 4 readable secondary replicas in secondary regions |
| Auto-Failover Groups | Single DNS endpoint; automatic regional failover with configurable grace period |
| Point-in-time restore | Restore to any point within the backup retention period |

---

## Section 3: Azure Cosmos DB

### 3.1 Overview

Azure Cosmos DB is Microsoft's globally distributed, multi-model NoSQL database. It is the most capable and most premium database service in Azure's portfolio, and the most heavily differentiated on AZ-900.

Three key differentiators:

1. **Native global distribution** — Replicate to any Azure region with a configuration change
2. **Multi-model APIs** — Support multiple data models via different APIs
3. **Configurable consistency** — Five consistency levels from Strong to Eventual

### 3.2 Global Distribution Details

| Feature | Detail |
|---|---|
| Read regions | Add any Azure region as a read replica with one click |
| Multi-region writes | Enable write to the closest region; all regions converge |
| Read latency | Single-digit milliseconds from any global region |
| Transparent failover | Automatic failover to secondary regions; configurable priority |

### 3.3 API / Data Model Options

| API | Data Model | Protocol Compatibility | Typical Migration Source |
|---|---|---|---|
| Core SQL | JSON documents | SQL-like query language | New cloud apps |
| MongoDB API | BSON documents | MongoDB 3.2/3.6/4.0 clients | Existing MongoDB apps |
| Cassandra API | Wide-column | Apache Cassandra CQL | Existing Cassandra apps |
| Gremlin API | Graph (vertices + edges) | Apache TinkerPop Gremlin | Graph database apps |
| Table API | Key-value | Azure Table Storage SDK | Azure Table Storage migrations |

### 3.4 Five Consistency Levels

| Level | Description | Read Latency | Availability | Use Case |
|---|---|---|---|---|
| Strong | Always reads most recent write | Highest | Lower | Financial transactions, inventory |
| Bounded Staleness | Reads lag by configurable time/versions | High | Higher | Leaderboards, collaborative editing |
| Session | Consistent within a client session | Medium | High | Shopping carts, user sessions |
| Consistent Prefix | Reads see updates in commit order | Low | Higher | Log processing |
| Eventual | Weakest; replicas eventually converge | Lowest | Highest | IoT telemetry, social likes |

### 3.5 SLA Comparison

| Service | Single-Region SLA | Multi-Region SLA |
|---|---|---|
| Azure SQL Database | 99.99% | 99.99% (with failover groups) |
| Azure Cosmos DB | 99.99% | 99.999% (five nines) |
| Azure Database for PostgreSQL | 99.99% (Flexible Server + HA) | 99.99% (read replicas) |

### 3.6 Pricing Model

| Model | Billing Basis | Best For |
|---|---|---|
| Provisioned throughput | Configured RU/s (Request Units per second) | Predictable workloads |
| Autoscale | RU/s automatically scales between min and max | Variable, spiky workloads |
| Serverless | Pay per RU consumed, no minimum | Intermittent, dev/test |

---

## Section 4: Open-Source Managed Database Services

### 4.1 Azure Database for PostgreSQL

| Feature | Detail |
|---|---|
| Deployment model | Flexible Server (recommended) |
| Version support | PostgreSQL 11–16 |
| High availability | Zone-redundant with automatic failover |
| Extensions | PostGIS, pg_cron, pgBouncer, and 50+ others |
| AZ-900 signal | "PostgreSQL," "ANSI SQL compliance," "geospatial data," "open-source relational" |

### 4.2 Azure Database for MySQL

| Feature | Detail |
|---|---|
| Deployment model | Flexible Server |
| Version support | MySQL 5.7 and 8.0 |
| High availability | Zone-redundant with automatic failover |
| Read replicas | Up to 5 read replicas |
| AZ-900 signal | "MySQL," "LAMP stack," "WordPress," "PHP web application" |

### 4.3 Managed Open-Source Database Comparison

| Service | Engine | Version | AZ-900 Scenario Keywords |
|---|---|---|---|
| Azure SQL Database | SQL Server | Latest stable | SQL Server, T-SQL, enterprise, .NET |
| Azure Database for PostgreSQL | PostgreSQL | 11–16 | PostgreSQL, advanced SQL, GIS, open-source |
| Azure Database for MySQL | MySQL | 5.7, 8.0 | MySQL, LAMP, PHP, WordPress |
| Azure Database for MariaDB | MariaDB | 10.2, 10.3 | MariaDB (deprecated — migrating to MySQL) |

---

## Section 5: Azure Synapse Analytics

### 5.1 Overview

Azure Synapse Analytics is a unified analytics service for large-scale data warehousing and big data analytics.

Key components:

| Component | Description | Use Case |
|---|---|---|
| Dedicated SQL pool | Massively parallel processing (MPP) SQL | Petabyte-scale data warehouse queries |
| Serverless SQL pool | Query Azure Data Lake via T-SQL, pay-per-query | Ad-hoc analytics on lake data |
| Apache Spark pool | Distributed Spark compute | Data engineering, ML training |
| Synapse Link | Live integration with Cosmos DB, Dataverse | Analytical queries on operational data |
| Synapse Studio | Unified web UI for all Synapse services | Development and management |

### 5.2 When to Use Synapse vs. Other Services

| Scenario | Recommended Service |
|---|---|
| OLTP — transactional web app database | Azure SQL Database |
| Global low-latency NoSQL | Azure Cosmos DB |
| Data warehouse — large analytics queries | Azure Synapse Analytics (Dedicated SQL Pool) |
| Ad-hoc queries on data lake files | Azure Synapse Analytics (Serverless SQL Pool) |
| Real-time analytics on IoT streams | Azure Stream Analytics + Synapse |

---

## Section 6: Database Migration

### 6.1 Azure Database Migration Service (DMS)

Azure Database Migration Service is a fully managed migration tool for moving databases to Azure.

| Migration Path | DMS Support |
|---|---|
| SQL Server → Azure SQL Database | Yes |
| SQL Server → Azure SQL Managed Instance | Yes |
| MySQL → Azure Database for MySQL | Yes |
| PostgreSQL → Azure Database for PostgreSQL | Yes |
| Oracle → Azure SQL Database | Yes (with Schema Conversion Tool) |
| MongoDB → Azure Cosmos DB | Yes |

Migration modes:

- **Online migration:** Continuous sync; minimal downtime; cutover during a brief maintenance window
- **Offline migration:** One-time backup/restore; requires planned downtime window

### 6.2 Database Assessment Tools

| Tool | Purpose |
|---|---|
| Data Migration Assistant (DMA) | Assess SQL Server compatibility with Azure SQL Database; identify blocking issues |
| Azure Migrate | Discover, assess, and migrate servers, databases, and web apps |
| Database Experimentation Assistant (DEA) | Compare query performance on source vs. target |

---

## Section 7: Database Service Selection Framework

### 7.1 Decision Framework for AZ-900

**Step 1 — Relational or non-relational?**

- Fixed schema, SQL queries, ACID transactions → Relational (go to Step 2)
- Flexible schema, global distribution, variable data models → Azure Cosmos DB

**Step 2 — Which SQL engine?**

- SQL Server / T-SQL → Step 3
- PostgreSQL → Azure Database for PostgreSQL
- MySQL → Azure Database for MySQL

**Step 3 — Which SQL Server deployment?**

- New cloud app, PaaS, standard SQL features → Azure SQL Database
- Migrating complex SQL Server app, needs SQL Agent/linked servers, PaaS preferred → Azure SQL Managed Instance
- Full SQL Server, OS access required, any version → SQL Server on Azure VM

**Step 4 — Is the workload analytical?**

- Large-scale analytics, data warehouse, BI → Azure Synapse Analytics

### 7.2 Full Service Summary Table

| Service | Model | Engine | Global Distribution | Best For |
|---|---|---|---|---|
| Azure SQL Database | PaaS | SQL Server | Geo-replication | Cloud-native SQL apps |
| Azure SQL Managed Instance | PaaS | Full SQL Server | Limited | Migrating complex SQL Server apps |
| SQL Server on Azure VM | IaaS | Full SQL Server | Manual | OS access, full compat, any version |
| Azure Cosmos DB | PaaS (NoSQL) | Multi-model | Native (any region) | Global, flexible schema, NoSQL |
| Azure Database for PostgreSQL | PaaS | PostgreSQL | Read replicas | Open-source PostgreSQL apps |
| Azure Database for MySQL | PaaS | MySQL | Read replicas | Open-source MySQL, web apps |
| Azure Synapse Analytics | PaaS | T-SQL / Spark | Regional | Data warehousing, big data analytics |

---

## Section 8: Azure CLI Reference

```bash
# Create a SQL Server (logical server)
az sql server create \
  --name lab10sqlserver \
  --resource-group lab10-rg \
  --location eastus \
  --admin-user sqladmin \
  --admin-password "SecureP@ss123!"

# Create an Azure SQL Database
az sql db create \
  --resource-group lab10-rg \
  --server lab10sqlserver \
  --name lab10db \
  --service-objective S0

# Allow Azure services to access the SQL Server
az sql server firewall-rule create \
  --resource-group lab10-rg \
  --server lab10sqlserver \
  --name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0

# Allow your client IP (replace with actual IP)
az sql server firewall-rule create \
  --resource-group lab10-rg \
  --server lab10sqlserver \
  --name AllowClientIP \
  --start-ip-address <YOUR_IP> \
  --end-ip-address <YOUR_IP>

# Show database details
az sql db show \
  --resource-group lab10-rg \
  --server lab10sqlserver \
  --name lab10db \
  --query "{name:name, status:status, serviceObjective:currentServiceObjectiveName}" \
  --output table

# Create a Cosmos DB account (Core SQL API)
az cosmosdb create \
  --name lab10cosmos \
  --resource-group lab10-rg \
  --default-consistency-level Session \
  --locations regionName=eastus failoverPriority=0

# Create a Cosmos DB database and container
az cosmosdb sql database create \
  --account-name lab10cosmos \
  --resource-group lab10-rg \
  --name lab10cosmosdb

az cosmosdb sql container create \
  --account-name lab10cosmos \
  --resource-group lab10-rg \
  --database-name lab10cosmosdb \
  --name products \
  --partition-key-path "/categoryId" \
  --throughput 400
```

---

## Section 9: AZ-900 Exam Tips

1. **PaaS vs. IaaS for SQL:** Azure SQL Database and Azure Database for PostgreSQL/MySQL are PaaS — Microsoft manages the OS and engine. SQL Server on Azure VM is IaaS — you manage the OS. Exam signals for IaaS: "OS access needed," "SQL Server Agent required," "linked servers," "specific SQL Server version."

2. **Cosmos DB global distribution signal:** If the exam scenario uses the words "global," "low latency for users worldwide," "multiple regions," or "millisecond response from any region," Azure Cosmos DB is the answer. No other Azure database service provides native global distribution.

3. **Cosmos DB consistency levels:** Cosmos DB is the only Azure database service with five configurable consistency levels. If the exam asks about consistency trade-offs for a database service, Cosmos DB is involved. Remember: Strong = highest latency, Eventual = lowest latency.

4. **Cosmos DB SLA = 99.999%:** The five-nines SLA for multi-region Cosmos DB is the highest of any Azure database service. If a scenario requires "maximum database availability" or "five-nines SLA," Cosmos DB is the answer.

5. **Elastic Pools for SaaS:** Multiple databases with variable, unpredictable utilization benefit from Elastic Pools — idle database compute is shared with active ones. Signal: "SaaS application with many customers, each with their own database."

6. **SQL Managed Instance for migration:** If the scenario mentions migrating an on-premises SQL Server application that uses SQL Agent, linked servers, CLR, or Service Broker, and the team wants PaaS, the answer is Azure SQL Managed Instance — not Azure SQL Database.

7. **Cosmos DB MongoDB API:** An existing MongoDB application can migrate to Cosmos DB using the MongoDB API with minimal code changes. Signal: "existing MongoDB application," "need managed NoSQL," "migrate from MongoDB."

8. **Synapse for analytics:** Azure Synapse Analytics is the answer for data warehousing, large-scale analytics, and business intelligence. Signal: "petabytes of data," "analytical queries," "data warehouse," "BI reporting."

---

## Section 10: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the SQL deployment option comparison table (Section 2.4)
- [ ] Memorize the Cosmos DB five consistency levels table (Section 3.4)
- [ ] Memorize the full service summary table (Section 7.2)
- [ ] Work through the decision framework in Section 7.1
- [ ] Complete the Microsoft Learn "Explore Azure database and analytics services" module
- [ ] Complete Lab Module 10
- [ ] Take Quiz Module 10
- [ ] Post Discussion Module 10 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure Cosmos DB consistency levels**
https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels
Detailed explanation of all five consistency levels (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual) with latency and throughput trade-offs, the consistency spectrum diagram, and guidance for choosing the right level for common application patterns.

**2. Microsoft Learn — Azure SQL Database and SQL Managed Instance feature comparison**
https://learn.microsoft.com/en-us/azure/azure-sql/database/features-comparison
Side-by-side comparison of features supported in Azure SQL Database vs. SQL Managed Instance — including SQL Agent, linked servers, CLR, Service Broker, cross-database queries, and other SQL Server features critical for migration planning.

**3. Microsoft Learn — Azure Synapse Analytics overview**
https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is
Covers the unified analytics workspace architecture including Dedicated SQL Pool (MPP data warehouse), Serverless SQL Pool (pay-per-query), Spark Pools, Synapse Pipelines, and Synapse Link for Cosmos DB — the reference for understanding Azure's end-to-end analytics platform.

---

## Required Reading Resources

- Azure SQL Database overview: learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview
- Azure SQL Managed Instance: learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview
- Azure Cosmos DB introduction: learn.microsoft.com/en-us/azure/cosmos-db/introduction
- Azure Database for PostgreSQL: learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview
- Azure Database for MySQL: learn.microsoft.com/en-us/azure/mysql/flexible-server/overview
- Azure Synapse Analytics: learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is
- Microsoft Learn AZ-900 database module: learn.microsoft.com/en-us/training/modules/azure-database-fundamentals/
