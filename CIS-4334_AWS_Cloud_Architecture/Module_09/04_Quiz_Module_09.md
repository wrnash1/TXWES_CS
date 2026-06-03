# Quiz: Module 09 — AWS Databases

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A company runs an RDS MySQL database with Multi-AZ enabled. Business analysts are running complex reporting queries that are causing performance degradation for the production application. The operations team suggests directing the reporting queries to the Multi-AZ standby instance to reduce primary load. What is WRONG with this suggestion?

A. The standby instance runs a different version of MySQL than the primary

B. The standby instance is not accessible for read traffic — it is a passive hot standby for failover only

C. Directing read traffic to the standby would cause the Multi-AZ replication to fail

D. The standby instance only stores the last 24 hours of data

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The standby runs the same MySQL version and stays in sync with the primary via synchronous replication.
- B is correct. The Multi-AZ standby is a passive instance maintained exclusively for automated failover. It does not accept any client connections for read or write traffic. To add read capacity, you must create one or more Read Replicas.
- C is incorrect. Multi-AZ replication is synchronous and operates independently of whether a client could theoretically connect to the standby. The suggestion is wrong because the standby is inaccessible, not because it would break replication.
- D is incorrect. The standby maintains a complete, fully synchronized copy of the database. It stores all data, not a rolling 24-hour window.

---

### Question 2

A startup needs a MySQL-compatible relational database. Requirements include: automatic storage growth from 10 GB to multiple terabytes, more than 5 read replicas, failover in under 60 seconds, and performance higher than standard community MySQL. Which AWS service meets ALL these requirements?

A. Amazon RDS for MySQL with Multi-AZ

B. Amazon Aurora MySQL

C. Amazon RDS for MySQL with Read Replicas

D. Amazon DynamoDB

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. RDS MySQL Multi-AZ provides failover but not within 60 seconds reliably, does not auto-grow storage, and supports only up to 5 read replicas. Multi-AZ failover typically takes 60–120 seconds.
- B is correct. Aurora MySQL is MySQL-compatible and provides: automatic storage growth (10 GB to 128 TB), up to 15 read replicas, failover in approximately 30 seconds (replica promotion with shared storage), and up to 5x better performance than community MySQL.
- C is incorrect. RDS MySQL with Read Replicas addresses read scaling but not the storage auto-growth, 15-replica, or sub-60-second failover requirements.
- D is incorrect. DynamoDB is a NoSQL key-value/document database, not a MySQL-compatible relational database. Applications requiring SQL and relational joins cannot use DynamoDB as a drop-in replacement.

---

### Question 3

A company's DynamoDB Orders table has a partition key of CustomerId and a sort key of OrderId. The e-commerce team now needs to query all orders for a specific ProductId across all customers. What is the MINIMUM change required to support this new access pattern?

A. Recreate the table with ProductId as the partition key

B. Create a Local Secondary Index with ProductId as the sort key

C. Create a Global Secondary Index with ProductId as the partition key

D. Enable DynamoDB Streams and process the stream with Lambda to build a separate lookup table

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Recreating the table changes the base access pattern. Queries by CustomerId would no longer be efficient, breaking the existing access patterns that the current design supports.
- B is incorrect. An LSI must share the same partition key as the base table (CustomerId). It can only provide an alternate sort key within a customer's partition. An LSI cannot support querying across all customers by ProductId. Additionally, LSIs cannot be added to existing tables.
- C is correct. A GSI can have any attribute as its partition key — ProductId in this case. The GSI replicates data with ProductId as the hash key, enabling efficient queries across all customers by product. GSIs can be added to existing tables at any time.
- D is incorrect. While technically possible, maintaining a separate lookup table via Streams is operationally complex, introduces replication lag, and requires custom code to build and maintain. A GSI accomplishes the same goal natively within DynamoDB.

---

### Question 4

An application makes identical DynamoDB GetItem calls for the same product catalog items thousands of times per second. Response times are in single-digit milliseconds but the team needs sub-millisecond response times for a new interactive feature. What is the SIMPLEST solution?

A. Switch DynamoDB from provisioned to on-demand capacity mode

B. Enable DynamoDB global tables for multi-region distribution

C. Add DynamoDB Accelerator (DAX) between the application and DynamoDB

D. Increase the provisioned read capacity units (RCUs) on the table

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. On-demand capacity mode changes how you pay for DynamoDB but does not reduce read latency. It does not add a cache layer.
- B is incorrect. Global Tables add multi-region replication for global active-active writes. They do not reduce read latency for a single-region application below what DynamoDB already provides.
- C is correct. DAX is an in-memory cache that is DynamoDB API-compatible. It caches frequently accessed items and serves them in microseconds — orders of magnitude faster than single-digit millisecond DynamoDB reads. For read-heavy workloads with repeated access to the same items, DAX is the direct solution.
- D is incorrect. Increasing RCUs increases throughput capacity and reduces throttling but does not reduce per-request read latency. DynamoDB already delivers single-digit milliseconds; more RCUs cannot push this to sub-millisecond.

---

### Question 5

A company needs to add a session management feature to their web application. Sessions must expire automatically after 30 minutes of inactivity. The session store must remain available if a single AZ fails. The application also needs to implement a real-time leaderboard for a gaming feature. Which AWS service and configuration BEST satisfies both requirements?

A. Amazon DynamoDB with TTL enabled

B. Amazon ElastiCache for Memcached in a multi-AZ configuration

C. Amazon ElastiCache for Redis with Multi-AZ enabled

D. Amazon RDS for PostgreSQL with Multi-AZ enabled

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. DynamoDB with TTL can handle session expiration and is highly available, but DynamoDB does not natively support sorted sets for leaderboards at microsecond latency, and TTL expiration is not guaranteed to the exact minute.
- B is incorrect. Memcached does not support Multi-AZ failover (no replication). If an AZ fails, Memcached data in that AZ is lost. Memcached also does not support sorted sets needed for leaderboards.
- C is correct. Redis supports TTL-based key expiration (for session management), Multi-AZ with automatic failover (for AZ resilience), and sorted sets (the native Redis data structure for real-time leaderboards with efficient rank queries). Redis satisfies all three requirements natively.
- D is incorrect. RDS is a relational database — using it for session management introduces unnecessary complexity and latency. RDS does not provide sub-millisecond session reads at high concurrency.

---

### Question 6

A company is building a fraud detection system that analyzes financial transactions. The system needs to identify patterns such as "accounts that sent money to an account that received money from a known fraud account within 24 hours." This requires traversing chains of financial relationships across millions of transactions. Which AWS database service is MOST appropriate?

A. Amazon RDS for PostgreSQL

B. Amazon DynamoDB

C. Amazon Redshift

D. Amazon Neptune

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect. While PostgreSQL can model relationships in a relational schema, multi-hop relationship traversals (A → B → C → D) using SQL JOINs become exponentially complex and slow as chain depth increases. Relational databases are not optimized for graph traversal.
- B is incorrect. DynamoDB is a key-value/document database. Multi-hop relationship traversal is not a supported query pattern. Each hop would require a separate query, making deep traversal extremely inefficient.
- C is incorrect. Redshift is optimized for historical analytical queries over large datasets (OLAP). It is not designed for real-time graph traversal across relationship chains.
- D is correct. Neptune is AWS's purpose-built graph database. Graph traversal queries (find all accounts within 2 hops of a fraud account) are natively supported by Neptune's Gremlin and SPARQL query languages. Neptune is specifically designed for relationship-centric analysis at scale.

---

### Question 7

A data analytics company needs to run complex SQL queries joining tables with billions of rows for business intelligence dashboards. Query results are displayed in a BI tool. The data is historical and updated daily via batch loads. Which database service is MOST appropriate?

A. Amazon Aurora MySQL

B. Amazon RDS for PostgreSQL

C. Amazon DynamoDB

D. Amazon Redshift

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect. Aurora is optimized for OLTP (frequent small transactional reads and writes). Complex analytical queries joining billions of rows would be slow and expensive on Aurora, which uses row-based storage rather than columnar storage.
- B is incorrect. Same reasoning as A — RDS PostgreSQL uses row-based storage optimized for transactional workloads, not analytical aggregations across billions of rows.
- C is incorrect. DynamoDB is a NoSQL database that does not support SQL JOIN operations or complex aggregations across the entire dataset. It is optimized for single-item reads and simple range queries.
- D is correct. Redshift is a columnar, massively parallel processing (MPP) data warehouse designed specifically for OLAP workloads. It executes complex analytical SQL queries across petabytes of historical data efficiently. Daily batch loads are the standard Redshift ingestion pattern.

---

### Question 8

An RDS PostgreSQL database in us-east-1 has Multi-AZ enabled. A solutions architect wants to add disaster recovery capability that allows failing over to a different AWS Region during a regional outage. What is the correct approach?

A. Enable a second Multi-AZ standby in us-west-2

B. Create a cross-region Read Replica in us-west-2

C. Enable automated backups and restore to us-west-2 during a disaster

D. Enable RDS Global Database

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Multi-AZ is a single-region feature. You cannot configure a Multi-AZ standby in a different region. Multi-AZ only protects against AZ-level failures within a region.
- B is correct. Cross-region Read Replicas replicate data from the primary in us-east-1 to a Read Replica in us-west-2. During a regional disaster, the cross-region Read Replica can be promoted to a standalone primary database. This provides regional DR capability for RDS (non-Aurora) databases.
- C is incorrect. Restoring from automated backups involves downloading backup files from S3 and provisioning a new RDS instance, which takes significant time (potentially hours). This provides a high RTO that may not be acceptable for disaster recovery.
- D is incorrect. RDS Global Database is an Aurora-specific feature, not available for standard RDS PostgreSQL. For Aurora, Global Database is the correct DR approach, but for standard RDS, cross-region Read Replicas is the answer.

---

### Question 9

A company's DynamoDB table uses `UserId` as the partition key and `Timestamp` as the sort key. A new requirement needs to query the table for all items where `Category = 'Electronics'` regardless of which user created them. Which solution BEST addresses this WITHOUT recreating the table?

A. Enable DynamoDB Streams and build a secondary table sorted by Category

B. Add a Local Secondary Index using Category as the sort key

C. Add a Global Secondary Index using Category as the partition key

D. Run a DynamoDB Scan with a FilterExpression on Category

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Building a secondary table via Streams is operationally complex, introduces replication lag, and requires custom code. It is the wrong solution when a native GSI can accomplish the same thing.
- B is incorrect. LSIs cannot be added after a table is created — they must be defined at table creation time. Additionally, an LSI shares the same partition key (UserId), which means it cannot support cross-user queries on Category.
- C is correct. A GSI with Category as the partition key enables efficient queries across all users by category. GSIs can be added to existing tables at any time and have their own partition key independent of the base table.
- D is incorrect. A Scan reads every item in the table and applies a filter after reading. For a large table, this is expensive (consumes RCUs proportional to table size) and slow. It is functionally correct but architecturally wrong for a recurring query pattern.

---

### Question 10

A company has an Amazon Aurora MySQL cluster with one primary instance and three read replicas. The primary instance fails. What happens next?

A. The cluster is unavailable until a new primary is manually provisioned

B. One of the read replicas is automatically promoted to primary in approximately 30 seconds

C. The Multi-AZ standby takes over as the primary in 60–120 seconds

D. Aurora performs a point-in-time restore from the most recent automated backup

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Aurora does not require manual intervention for primary instance failover when read replicas are present. Automatic promotion is a core Aurora feature.
- B is correct. Aurora's shared distributed storage architecture means that when the primary fails, any read replica already has access to all committed data. Aurora automatically promotes one of the read replicas to primary in approximately 30 seconds, minimizing downtime without replaying transaction logs.
- C is incorrect. There is no separate "Multi-AZ standby" in Aurora. Aurora achieves high availability through its shared storage layer and read replica promotion, not through the same standby mechanism as standard RDS Multi-AZ.
- D is incorrect. Point-in-time restore from backup is a manual data recovery operation used when data corruption occurs, not for instance failover. It would take significantly longer than automatic promotion and would result in data loss up to the last backup point.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
