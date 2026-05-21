# Reading Guide: Module 07 - Azure Database Services

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 07 - Azure Database Services**! This module covers Azure's managed database offerings as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Azure provides a broad portfolio of fully managed database services, eliminating the need to manage underlying OS, database engine patching, and hardware.

You will learn the key characteristics of Azure SQL Database (relational), Azure Cosmos DB (globally distributed NoSQL), and Azure Database for MySQL/PostgreSQL (open-source engines). AZ-900 tests whether you can match a workload description to the correct Azure database service. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure SQL Database**: A fully managed PaaS relational database built on the Microsoft SQL Server engine. Azure handles OS patching, backups, high availability, and scaling automatically. It supports T-SQL queries and integrates with existing SQL Server workloads. Azure SQL Database is the primary choice for relational/structured data workloads on AZ-900.

* **Azure Cosmos DB (multi-model, global distribution)**: A globally distributed, multi-model NoSQL database service supporting multiple APIs including SQL (Core), MongoDB, Cassandra, Gremlin (graph), and Azure Table. Cosmos DB replicates data across any number of Azure regions with millisecond read/write latency. It is the correct AZ-900 answer when a scenario requires global distribution, multi-region writes, or flexible schema.

* **Azure Database for MySQL / PostgreSQL**: Fully managed PaaS versions of the open-source MySQL and PostgreSQL database engines. Microsoft handles patching, backups, and high availability. These services are ideal for migrating existing open-source database workloads to Azure without rewriting application code (lift-and-shift with managed infrastructure).

---

### 2. Certification Exam Tips

* **SQL vs. Cosmos DB**: AZ-900 tests this distinction frequently. Azure SQL = structured, relational, T-SQL. Cosmos DB = unstructured or semi-structured, globally distributed, multiple API options, flexible schema. If a scenario mentions "global distribution," "multiple regions," or "NoSQL," Cosmos DB is the answer.
* **PaaS vs. IaaS databases**: All three database services in this module are PaaS — Microsoft manages the OS and database engine. If a scenario requires full control over the database engine (custom engine versions, OS-level access), the answer would be SQL Server on an Azure VM (IaaS).
* **Cosmos DB Consistency Levels**: Cosmos DB offers five consistency levels (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual). AZ-900 does not require deep knowledge of all levels but does expect you to know that Cosmos DB supports tunable consistency for global distribution scenarios.
* **Azure SQL Purchasing Models**: Azure SQL Database offers two purchasing models — DTU (Database Transaction Unit, a bundled compute/storage/IO metric) and vCore (explicit CPU/memory selection). AZ-900 may ask which model gives more granular control — vCore does.
* **Study Resource**: The Microsoft Learn path for AZ-900 covers Azure database services with knowledge checks. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure database services including SQL Database, Cosmos DB, and open-source managed databases. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free freeCodeCamp course covers Azure database services for AZ-900 — watch the database section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Deploy an Azure SQL database instance**: Create an Azure SQL Database using the portal, selecting a service tier (e.g., General Purpose, 2 vCores) and observing the automatic backup and geo-restore options configured by default.
* **Examine connection strings**: Review the ADO.NET and JDBC connection strings generated for the SQL Database. Observe that connection strings use the server FQDN and do not expose the underlying server OS.
* **Configure Cosmos DB global replica sites**: In a Cosmos DB account, add a secondary read region. Observe how global distribution is enabled with a few clicks and how the chosen consistency level affects replication behavior.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure database services unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the database section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for Azure SQL Database deployment and Cosmos DB replication configuration.
* [ ] Proceed to the weekly hands-on lab activity.
