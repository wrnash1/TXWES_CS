# Quiz: Module 07 - Azure Database Services

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure database service is a globally distributed, multi-model database engine supporting SQL, MongoDB, and Cassandra APIs?

* A) Azure SQL Database
* B) Azure Database for PostgreSQL
* C) Azure Cosmos DB
* D) Azure SQL Managed Instance
* **Correct Answer:** C) Cosmos DB is Microsoft's NoSQL engine built for global distribution and multi-API access.
* **Distractor Analysis:**
  * *Why correct:* Cosmos DB is Microsoft's globally distributed NoSQL engine supporting multiple API compatibility layers including SQL Core, MongoDB, Cassandra, and others.
  * *Why A is incorrect:* Azure SQL Database is strictly relational using the SQL Server engine — it does not support MongoDB or Cassandra APIs.

---

**Question 2**
Which of the following most accurately describes **Azure Cosmos DB**?

* A) A globally distributed, multi-model NoSQL database service that replicates data across multiple Azure regions with millisecond latency and supports multiple API compatibility layers including SQL, MongoDB, and Cassandra.
* B) A fully managed relational database service based on the Microsoft SQL Server engine, supporting T-SQL queries and ACID transactions.
* C) A fully managed open-source PostgreSQL service where Microsoft handles OS patching, backups, and high availability automatically.
* D) A key-value cache service built on Redis that provides sub-millisecond response times for frequently accessed application data.
* **Correct Answer:** A) Cosmos DB is a globally distributed, multi-model NoSQL database that replicates across regions with millisecond latency and supports multiple API compatibility layers.
* **Distractor Analysis:**
  * *Why A is correct:* Cosmos DB's key AZ-900 characteristics are global distribution, multi-model API support, and millisecond read/write latency at any scale.
  * *Why B is incorrect:* That describes Azure SQL Database, which is relational and SQL Server-based.
  * *Why C is incorrect:* That describes Azure Database for PostgreSQL, which is an open-source managed service.
  * *Why D is incorrect:* That describes Azure Cache for Redis, a caching service — not a database.

---

**Question 3**
A company needs to migrate their existing on-premises MySQL application to Azure with minimal code changes and no OS management responsibility. Which Azure service is the best fit?

* A) SQL Server on Azure Virtual Machine (IaaS)
* B) Azure SQL Database
* C) Azure Database for MySQL
* D) Azure Cosmos DB with MongoDB API
* **Correct Answer:** C) Azure Database for MySQL is a fully managed PaaS service that runs the MySQL engine — existing MySQL applications connect without code changes, and Microsoft manages the OS and engine.
* **Distractor Analysis:**
  * *Why C is correct:* Azure Database for MySQL provides a fully managed MySQL-compatible environment, enabling lift-and-shift of MySQL workloads with no OS management.
  * *Why A is incorrect:* SQL Server on an Azure VM requires the customer to manage the OS — this does not meet the "no OS management" requirement.
  * *Why B is incorrect:* Azure SQL Database uses the SQL Server engine, not MySQL — the application would require migration to T-SQL syntax.
  * *Why D is incorrect:* Cosmos DB's MongoDB API is for document-style NoSQL workloads — MySQL applications use relational SQL and would require significant rewriting.

---

**Question 4**
A global e-commerce application needs a database that can serve reads and writes from Azure regions in North America, Europe, and Asia simultaneously, with the ability to tune consistency based on business requirements. Which Azure database service meets this need?

* A) Azure SQL Database with active geo-replication
* B) Azure Database for PostgreSQL with read replicas
* C) Azure Cosmos DB with multi-region writes enabled
* D) Azure SQL Managed Instance with Always On availability groups
* **Correct Answer:** C) Azure Cosmos DB supports multi-region writes across any number of Azure regions with tunable consistency levels, making it purpose-built for globally distributed applications.
* **Distractor Analysis:**
  * *Why C is correct:* Cosmos DB's native multi-region write capability and tunable consistency levels are specifically designed for globally distributed, low-latency scenarios.
  * *Why A is incorrect:* Azure SQL geo-replication provides read replicas in secondary regions but writes must go to the primary region — it does not support multi-region writes.
  * *Why B is incorrect:* PostgreSQL read replicas allow reads from secondary regions but all writes still go to the primary instance.
  * *Why D is incorrect:* SQL Managed Instance with Always On provides high availability within a region but does not support distributed global multi-region writes.

---

**Question 5**
What distinguishes Azure SQL Database (PaaS) from SQL Server on an Azure Virtual Machine (IaaS) in terms of customer responsibility?

* A) Azure SQL Database requires the customer to manage OS patching, while SQL Server on VM is fully managed by Microsoft.
* B) Azure SQL Database is fully managed by Microsoft including OS and engine patching; SQL Server on VM requires the customer to manage the OS, SQL Server version, and security patches.
* C) Azure SQL Database supports only read workloads; SQL Server on VM supports both read and write workloads.
* D) Azure SQL Database stores data only in memory; SQL Server on VM stores data on managed disks.
* **Correct Answer:** B) Azure SQL Database is PaaS — Microsoft manages OS and engine patching. SQL Server on VM is IaaS — the customer manages OS and SQL Server patching.
* **Distractor Analysis:**
  * *Why B is correct:* This is the shared responsibility distinction tested on AZ-900: PaaS databases remove OS/engine management from the customer; IaaS VMs do not.
  * *Why A is incorrect:* This reverses the responsibilities — it is Azure SQL Database (PaaS) that Microsoft manages, not the VM-based option.
  * *Why C is incorrect:* Both services support full read and write operations.
  * *Why D is incorrect:* Both services persist data to storage — neither is exclusively in-memory.
