# Video Script: Module 09 — AWS Databases

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

### SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4334. I'm Professor Nash. Module 09 is all about databases — one of the richest topic areas on the SAA-C03 exam. AWS offers over a dozen database services, and the exam tests your ability to match workload characteristics to the right engine.

Today we cover six services: Amazon RDS with its Multi-AZ and Read Replica capabilities, Amazon Aurora and how it differs from standard RDS, Amazon DynamoDB with its key design patterns and accelerator, Amazon ElastiCache with Redis versus Memcached trade-offs, Amazon Redshift for data warehousing, and Amazon Neptune for graph workloads. We'll close with a unified decision framework for choosing the right database for any given scenario.

Let's start with the relational database workhorse — Amazon RDS.

---

### SEGMENT 2 — Amazon RDS: Multi-AZ and Read Replicas (1:30–6:00)

[SHOW DIAGRAM: RDS Multi-AZ architecture — Primary DB instance in AZ-A with synchronous replication arrow to Standby DB instance in AZ-B. A single DNS endpoint sits above both instances. A red X over the primary with a curved arrow showing automatic failover to standby.]

Amazon Relational Database Service — RDS — is a managed service for running relational databases on AWS. RDS manages the undifferentiated heavy lifting: hardware provisioning, database setup, patching, automated backups, and failover. You choose from six supported database engines: MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, and Amazon Aurora.

The two most tested RDS features are Multi-AZ and Read Replicas. They are fundamentally different, and confusing them is one of the most common SAA-C03 mistakes.

**RDS Multi-AZ** is a high availability feature. When you enable Multi-AZ, RDS provisions a synchronous standby replica in a different Availability Zone. Every write to the primary database is synchronously replicated to the standby before the write is confirmed to the application. If the primary instance fails — hardware failure, AZ outage, or even a maintenance window — RDS automatically updates the DNS endpoint to point to the standby and promotes it to primary. Failover typically takes 60–120 seconds.

The standby instance in Multi-AZ is not used for read traffic. It is purely a passive hot standby waiting to take over. The application uses a single DNS endpoint — the endpoint does not change during failover because it is DNS-based. This is a critical exam point: Multi-AZ is for availability, not read performance.

**RDS Read Replicas** are for read scaling. When you create a Read Replica, RDS uses asynchronous replication to maintain a copy of the database that can serve read queries. You can have up to 5 Read Replicas per RDS instance (15 for Aurora). Applications must be updated to direct read traffic to the replica endpoint.

Because replication is asynchronous, Read Replicas have some replication lag — they may return slightly stale data. For applications requiring strongly consistent reads, queries must go to the primary. For analytics, reporting, and read-heavy workloads where eventual consistency is acceptable, Read Replicas dramatically reduce load on the primary.

Read Replicas can be in the same region or in a different region — cross-region Read Replicas provide both read scaling and disaster recovery capability in a single feature. A cross-region Read Replica can be promoted to a full standalone database during a regional outage.

[SHOW DIAGRAM: Side-by-side comparison — Multi-AZ left column showing synchronous replication, 1 standby, same region only, no read scaling, automatic failover. Read Replicas right column showing asynchronous replication, up to 5 (15 Aurora), cross-region supported, read scaling yes, manual promotion.]

---

### SEGMENT 3 — Amazon Aurora (6:00–9:00)

[SHOW DIAGRAM: Aurora cluster architecture — primary instance and up to 15 read replicas all connected to a shared distributed storage layer spanning 3 AZs with 6 copies of data (2 per AZ). Writer endpoint and reader endpoint labeled above.]

Amazon Aurora is AWS's cloud-native relational database. Aurora is compatible with MySQL and PostgreSQL — you can migrate most MySQL or PostgreSQL applications to Aurora with minimal changes. Aurora is not just a hosted version of MySQL; it is a fundamentally different architecture.

Aurora separates compute from storage. All instances in an Aurora cluster — the primary and all read replicas — share the same distributed storage layer. That storage layer automatically replicates data across 3 Availability Zones with 6 copies total (2 per AZ). Aurora can survive the loss of 2 copies without affecting write availability and the loss of 3 copies without affecting read availability.

Aurora storage grows automatically from 10 GB to 128 TB in 10 GB increments as needed. There is no need to provision storage upfront and no storage volume to resize.

Aurora provides two endpoints: the **writer endpoint** always points to the current primary instance, and the **reader endpoint** load-balances read traffic across all read replicas automatically. Applications use these stable endpoints and never need to track individual instance endpoints.

Aurora failover is faster than RDS Multi-AZ. If the primary fails, Aurora promotes one of the read replicas to primary in approximately 30 seconds. This is because the new primary does not need to replay a transaction log — it already has access to the shared storage with all committed data.

**Aurora Serverless v2** automatically scales the database's compute capacity (measured in Aurora Capacity Units — ACUs) up or down in increments as fine as 0.5 ACUs based on actual demand. This is ideal for workloads with highly variable or unpredictable query volumes. You are billed per ACU-second, similar to Lambda's pay-per-invocation model.

On the exam: if a scenario mentions "MySQL or PostgreSQL compatible," "automatic storage scaling," "15 read replicas," "faster failover than RDS," or "variable workload serverless database," Aurora is the answer.

---

### SEGMENT 4 — Amazon DynamoDB (9:00–12:30)

[SHOW DIAGRAM: DynamoDB table with partition key and sort key illustrated. Arrows show partition key → partition hash → storage partition. GSI shown as a separate projected table with a different partition key.]

DynamoDB is AWS's fully managed serverless NoSQL key-value and document database. It delivers single-digit millisecond performance at any scale — millions of requests per second — with automatic sharding, replication across 3 AZs, and no infrastructure to manage.

DynamoDB data model: data is stored as **items** (equivalent to rows) in **tables**. Items are identified by a **primary key** — either a simple partition key or a composite partition key plus sort key. The partition key determines which physical partition stores the item. Items with the same partition key and different sort keys are stored together and can be queried as a range.

**Global Secondary Indexes (GSI)** allow you to query DynamoDB by any attribute, not just the primary key. A GSI has its own partition key and optional sort key — completely different from the base table. You can add GSIs to an existing table at any time. Maximum 20 GSIs per table.

**Local Secondary Indexes (LSI)** share the same partition key as the base table but use a different sort key. LSIs must be created when the table is created and cannot be added later. Maximum 5 LSIs per table. LSIs allow range queries within a partition on an alternate sort key.

On the exam: if you need a new query pattern on an existing table, the answer is GSI (cannot add LSI after creation). If the question involves querying by a non-key attribute at all, think GSI first.

**DynamoDB Accelerator (DAX)** is a fully managed in-memory read cache for DynamoDB. DAX is DynamoDB-compatible — your application uses the same API calls, but DAX intercepts reads and serves cached results in microseconds. DAX is only beneficial for read-heavy workloads with repeated access to the same items. DAX does not improve write performance. DAX provides only eventually consistent reads — if your application requires strongly consistent reads, DAX cannot serve those (they go directly to DynamoDB).

**DynamoDB Global Tables** provide multi-region active-active replication. All replica tables accept reads and writes. Conflict resolution uses last-writer-wins. Global Tables require DynamoDB Streams to be enabled. This is the answer when any scenario asks for multi-region write capability with automatic replication.

---

### SEGMENT 5 — Amazon ElastiCache (12:30–15:00)

[SHOW DIAGRAM: Application tier → ElastiCache cluster (Redis or Memcached) → Database. Cache hit path shown going directly from ElastiCache back to application. Cache miss path shown going through to the database, then back through ElastiCache to application.]

ElastiCache is a fully managed in-memory caching service. It reduces database load by caching frequently accessed data in memory, delivering sub-millisecond response times. ElastiCache supports two engines: Redis and Memcached.

**Redis** is the feature-rich option. Redis supports complex data structures — strings, hashes, lists, sets, sorted sets — making it suitable not just for caching but also for leaderboards, session stores, geospatial indexes, and pub/sub messaging. Redis supports persistence (saving data to disk), replication, Multi-AZ with automatic failover, and Redis Cluster mode for horizontal sharding. Redis is the right choice when you need high availability, data persistence, or complex data structures beyond simple key-value storage.

**Memcached** is simpler and designed purely for high-performance distributed caching. It supports only string key-value pairs, no persistence, and no replication. Memcached uses multi-threading, which can be more efficient than Redis for pure caching at very high throughput. Memcached is the right choice when you need the simplest, fastest pure cache with no other requirements.

[SHOW DIAGRAM: Redis vs. Memcached feature matrix with checkmarks — Data structures, Persistence, Replication, Multi-AZ, Pub/Sub: all checked for Redis, all unchecked for Memcached except checkmarks for Simplicity and Multi-threading]

On the exam: if a scenario mentions "leaderboard," "session store," "high availability cache," "pub/sub," or "cache with persistence" → Redis. If it says "simple cache, highest throughput, no special features needed" → Memcached.

The Lazy Loading caching pattern loads data into the cache only when a cache miss occurs. The Write-Through caching pattern updates the cache every time a write occurs. For SAA-C03, understand these patterns conceptually but the exam typically tests engine selection rather than caching strategy implementation.

---

### SEGMENT 6 — Amazon Redshift and Neptune (15:00–18:00)

[SHOW DIAGRAM: Redshift cluster architecture — Leader Node receiving SQL queries from BI tools, with arrows to 2–128 Compute Nodes processing data in parallel. S3 icon labeled COPY showing data loading from S3.]

**Amazon Redshift** is a fully managed petabyte-scale data warehouse optimized for OLAP (Online Analytical Processing) queries over large historical datasets. Redshift uses columnar storage, data compression, and massively parallel processing (MPP) to execute complex analytical queries across billions of rows efficiently.

Redshift is the right choice when you need to run complex analytical SQL queries against large historical datasets for business intelligence. It is not a replacement for OLTP databases — it is optimized for queries that aggregate, join, and filter massive tables, not for frequent small read/write operations.

Key features: **Redshift Spectrum** allows you to run SQL queries directly against data stored in S3 without loading it into Redshift first. **Redshift Serverless** automatically provisions and scales query capacity without cluster management. **Redshift RA3 nodes** separate compute from storage, allowing you to scale each independently.

On the exam: if a scenario mentions "business intelligence," "data warehouse," "OLAP," "petabyte-scale analytics," or "historical reporting" → Redshift.

**Amazon Neptune** is a fully managed graph database service. It supports two graph data models: Property Graph (queried with Gremlin) and RDF (queried with SPARQL). Neptune is designed for use cases where relationships between data are as important as the data itself.

Graph database use cases: social networks (who follows whom, mutual connections), fraud detection (transactional relationship analysis), knowledge graphs, recommendation engines (users who bought X also bought Y), and network topology management.

On the exam: if a scenario mentions "graph," "relationships between entities," "social network," or "fraud detection based on transaction relationships" → Neptune.

---

### SEGMENT 7 — Choosing the Right Database (18:00–20:30)

[SHOW DIAGRAM: Database selection decision tree — Relational/SQL required? → RDS or Aurora. Need 15 read replicas or serverless scaling? → Aurora. NoSQL, millions of req/sec, single-digit ms? → DynamoDB. Reduce DB load with caching? → ElastiCache. Petabyte analytics/BI? → Redshift. Graph relationships? → Neptune.]

Choosing the right database is the ultimate exam skill for this module. Let me give you the complete decision framework.

Choose **RDS** when: you need a managed relational database with SQL, you have existing MySQL, PostgreSQL, Oracle, SQL Server, or MariaDB applications, and you need Multi-AZ high availability with standard read replica scaling.

Choose **Aurora** over RDS when: you need MySQL or PostgreSQL compatibility with higher performance (Aurora is up to 5x faster than MySQL and 3x faster than PostgreSQL), you need more than 5 read replicas, you need faster failover, you need automatic storage scaling, or your workload is variable and Aurora Serverless v2 would reduce costs.

Choose **DynamoDB** when: your workload requires single-digit millisecond latency at any scale, access patterns are defined (key-value or range queries), you need a serverless pay-per-request model, the data model is flexible (document or key-value), or you need multi-region active-active replication.

Choose **ElastiCache** when: you need to reduce database read load by caching hot data. Redis when you need high availability, persistence, complex data structures, or pub/sub. Memcached when you need a simple, fast, multi-threaded pure cache.

Choose **Redshift** when: you are building a data warehouse or analytics platform and need to run complex SQL queries over large historical datasets for business intelligence.

Choose **Neptune** when: your application's primary challenge is traversing and querying relationships between entities — social graphs, fraud detection, knowledge bases.

---

### SEGMENT 8 — Summary and Exam Tips (20:30–22:00)

Module 09 in 60 seconds: RDS Multi-AZ is availability, Read Replicas are read scaling. Aurora is MySQL/PostgreSQL compatible with shared storage, 15 read replicas, and faster failover. DynamoDB for high-scale NoSQL with single-digit ms latency — GSI for non-key queries, DAX for read caching, Global Tables for multi-region active-active. ElastiCache Redis for feature-rich cache with HA and persistence, Memcached for simple high-throughput caching. Redshift for petabyte OLAP analytics. Neptune for graph relationships.

The exam will give you a scenario and ask which database to use. Use these triggers: "millions of requests per second" → DynamoDB. "Business intelligence, data warehouse" → Redshift. "Social network, fraud detection, graph" → Neptune. "Reduce database read load" → ElastiCache. "MySQL compatible, more than 5 replicas" → Aurora. "Oracle or SQL Server" → RDS.

Module 10 covers VPC networking — one of the most architecture-intensive topics on the exam. I'll see you there.

---

*End of Module 09 Video Script*

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
