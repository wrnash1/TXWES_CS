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

### Question 11 (5 points)

A solutions architect is designing a caching layer for an application that stores user shopping cart data. The cart must survive if a single cache node fails, the cache data must persist across restarts so carts are not lost, and the cache must support complex data structures like sorted sets. Which caching service and configuration is MOST appropriate?

A. Amazon ElastiCache for Memcached with Multi-AZ

B. Amazon ElastiCache for Redis with Multi-AZ and cluster mode enabled

C. Amazon ElastiCache for Memcached with a large number of nodes for redundancy

D. Amazon DynamoDB with DAX as the caching layer

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. ElastiCache for Memcached does not support replication between nodes, data persistence, or complex data structures like sorted sets. A single node failure results in permanent data loss for all keys on that node. Memcached is a pure in-memory cache with no persistence.
- B is correct. ElastiCache for Redis supports: (1) replication — Multi-AZ with automatic failover protects against node failure; (2) persistence — Redis can write snapshots (RDB) and append-only files (AOF) to disk for recovery; (3) sorted sets and other complex data structures natively. Cluster mode enables horizontal partitioning for large datasets.
- C is incorrect. Memcached with many nodes does not provide redundancy for individual keys — when any node fails, all keys on that node are lost permanently. Adding more nodes provides horizontal scaling but not fault tolerance.
- D is incorrect. DynamoDB with DAX is a caching solution for DynamoDB read workloads. It is not a general-purpose in-memory cache for application data like shopping carts, and it does not support Redis-style sorted sets.

---

### Question 12 (5 points)

A gaming leaderboard application needs to store player scores and instantly return the top 100 players sorted by score. The leaderboard is updated millions of times per day and must respond in under 1 millisecond. Which database service and data structure is MOST appropriate?

A. Amazon RDS for MySQL with an indexed score column and ORDER BY query

B. Amazon DynamoDB with a Global Secondary Index on the score attribute

C. Amazon ElastiCache for Redis using a sorted set (ZSET) data structure

D. Amazon Redshift with a materialized view sorted by score

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. RDS MySQL with an indexed score column can return sorted results, but relational database query execution at sub-millisecond latency for high-frequency updates to a globally sorted leaderboard is extremely challenging. MySQL would require locking mechanisms for concurrent updates and cannot easily achieve the sub-millisecond response requirement at millions of updates per day.
- B is incorrect. DynamoDB GSIs support efficient queries but do not natively provide a sorted ranking with rank number. Querying the top 100 scores across all players requires scanning the GSI and does not guarantee sub-millisecond response for leaderboard retrieval. DynamoDB latency is single-digit milliseconds, not sub-millisecond.
- C is correct. Redis sorted sets (ZSET) are specifically designed for this use case. Sorted sets maintain elements sorted by score with O(log N) insertion and O(log N + K) range retrieval. The ZREVRANGE command returns the top K elements by score in microseconds. Redis is the canonical answer for real-time leaderboards.
- D is incorrect. Amazon Redshift is a data warehouse designed for analytical queries over large datasets. It is not an OLTP system and has latency measured in seconds for query execution — completely incompatible with a sub-millisecond real-time leaderboard requirement.

---

### Question 13 (5 points)

A DynamoDB table uses a composite primary key with `UserID` as the partition key and `OrderDate` as the sort key. A query must retrieve all orders for a specific user placed in the year 2024. Which DynamoDB API operation is MOST efficient for this?

A. Scan the entire table with a filter expression `OrderDate BETWEEN '2024-01-01' AND '2024-12-31'`

B. Query with `KeyConditionExpression = 'UserID = :uid AND OrderDate BETWEEN :start AND :end'`

C. GetItem with UserID and the first OrderDate of 2024

D. BatchGetItem with all UserIDs and OrderDates for 2024

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. A Scan reads every item in the table and applies the filter after reading, consuming read capacity units for every item regardless of the filter result. For a large table, this is extremely expensive and slow. The filter expression reduces the items returned but not the read capacity consumed.
- B is correct. A Query with a KeyConditionExpression uses the primary key to directly locate all items with the matching partition key (UserID) and applies the sort key range condition (BETWEEN on OrderDate) to further narrow results within that partition. This reads only the items needed, consuming minimal RCUs and returning results in milliseconds.
- C is incorrect. GetItem retrieves a single item by its exact primary key. You would need to know the exact OrderDate to use GetItem, and it only returns one item. This is not suitable for retrieving all 2024 orders for a user.
- D is incorrect. BatchGetItem retrieves individual items by exact primary keys in batches. It is designed for point lookups on specific known keys, not for range queries across a partition. You would need to know every specific OrderDate, which defeats the purpose.

---

### Question 14 (5 points)

An application reads the same DynamoDB table items repeatedly as part of a product catalog page. The catalog items change infrequently, but the read traffic causes high RCU consumption. The team wants to add a caching layer in front of DynamoDB to reduce RCU costs. Which service is purpose-built for this use case?

A. Amazon ElastiCache for Redis with a read-through cache pattern

B. Amazon DAX (DynamoDB Accelerator)

C. Amazon CloudFront with Lambda@Edge to cache DynamoDB responses

D. Amazon RDS Read Replica in the same Region as DynamoDB

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. ElastiCache for Redis can cache DynamoDB query results, but it requires application-level cache management: the application must check Redis before calling DynamoDB, handle cache misses, and invalidate stale cache entries. DAX is purpose-built for DynamoDB and handles this transparently.
- B is correct. DAX is an in-memory cache purpose-built for DynamoDB. It is API-compatible with DynamoDB — no application code changes are needed beyond updating the endpoint from the DynamoDB endpoint to the DAX endpoint. DAX handles cache miss/hit logic transparently and reduces DynamoDB read latency from single-digit milliseconds to microseconds, directly reducing RCU consumption for frequently read items.
- C is incorrect. CloudFront with Lambda@Edge could cache static HTTP responses, but this is a complex custom solution requiring Lambda@Edge functions to translate HTTP requests to DynamoDB API calls. This is not a purpose-built database caching solution.
- D is incorrect. RDS Read Replicas are for relational databases (RDS/Aurora). DynamoDB is a NoSQL service and does not have RDS Read Replicas. These are completely different service categories.

---

### Question 15 (5 points)

An e-commerce company uses Amazon Redshift for its data warehouse. Sales analysts are running complex analytical queries that take 15-30 minutes to complete, and the queries are scheduled to run at 6 AM daily. The warehouse is idle for the rest of the day. Which Redshift feature minimizes cost for this workload pattern?

A. Redshift Multi-AZ with automatic failover to ensure high availability during the daily query window

B. Redshift Serverless, which automatically scales and bills only for compute used during query execution

C. Redshift Spectrum to query S3 directly without a persistent Redshift cluster

D. Redshift Reserved Node pricing for all three AZs

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Redshift Multi-AZ provides high availability for the data warehouse, but it doubles the cluster cost. The question focuses on minimizing cost for a workload that is only active 1-2 hours per day — Multi-AZ addresses availability, not cost efficiency for intermittent use.
- B is correct. Redshift Serverless automatically scales compute resources during query execution and charges only for the compute used (measured in Redshift Processing Units per second). During the 22+ hours per day when the warehouse is idle, there is no cluster cost. For a workload running only once daily, Serverless eliminates the idle cluster cost.
- C is incorrect. Redshift Spectrum enables running SQL queries directly against data in S3 using Redshift query infrastructure, but it still requires a running Redshift cluster as the query coordinator. It extends Redshift's reach to S3 data but does not eliminate cluster costs.
- D is incorrect. Redshift Reserved Nodes reduce the hourly rate for running nodes by up to 75%, but a running cluster still incurs charges even when idle. Reserved Nodes are cost-effective for clusters running continuously, not for once-daily workloads.

---

### Question 16 (5 points)

A company needs a fully managed graph database to store and query a social network where the primary access pattern is traversing relationships — "find all friends of friends who have purchased product X." Which AWS database service is MOST appropriate?

A. Amazon DynamoDB with a complex GSI structure for relationship modeling

B. Amazon Neptune

C. Amazon RDS for PostgreSQL with recursive Common Table Expressions

D. Amazon Redshift with a star schema

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. DynamoDB can model relationships using adjacency list patterns, but deep relationship traversal (friends of friends, n-hop graph queries) requires complex, multi-step queries. DynamoDB is not optimized for graph traversal and does not support native graph query languages.
- B is correct. Amazon Neptune is a fully managed graph database service that supports Property Graph (Gremlin, openCypher) and RDF (SPARQL) query languages. Graph traversal queries like "friends of friends who purchased X" are first-class operations in Neptune with optimized graph storage. Neptune is the SAA-C03 trigger answer for any scenario involving social networks, recommendation engines, fraud detection, or knowledge graphs.
- C is incorrect. PostgreSQL with recursive CTEs can model graph relationships in a relational schema, but this requires complex SQL, does not leverage graph-optimized storage, and performance degrades for deep traversals (many hops). PostgreSQL is not purpose-built for graph workloads at scale.
- D is incorrect. Redshift with a star schema is a data warehouse architecture for analytical reporting, not for real-time graph traversal. Star schemas are optimized for fact/dimension joins, not recursive relationship traversals.

---

### Question 17 (5 points)

A company needs to query archived financial data stored in Amazon S3 in Parquet format without loading it into a database or data warehouse. The queries are ad hoc and run infrequently. Which AWS service enables SQL queries directly against S3 data at the lowest cost?

A. AWS Glue ETL to load S3 data into RDS before querying

B. Amazon Athena, a serverless query engine that executes SQL on S3 data and charges per TB scanned

C. Amazon EMR with a Spark cluster running on Reserved Instances

D. Amazon Redshift with S3 Spectrum enabled and a persistent cluster

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Loading data into RDS before each query adds data transfer costs, storage costs, and requires ETL processing time. For infrequent ad hoc queries, loading into RDS is operationally complex and expensive compared to querying S3 directly.
- B is correct. Amazon Athena is a serverless, interactive query service that executes standard SQL against data stored in S3. There is no infrastructure to provision or manage — you pay only for the data scanned per query (approximately $5 per TB). Parquet is a columnar format that significantly reduces the data scanned per query, lowering cost further. Athena is the canonical answer for ad hoc S3 queries on the SAA-C03 exam.
- C is incorrect. EMR with a Spark cluster provides powerful distributed computing for large-scale ETL and analytics, but it requires cluster management, launch time, and ongoing compute costs. For infrequent ad hoc queries, the overhead is disproportionate compared to serverless Athena.
- D is incorrect. Redshift with Spectrum still requires a running Redshift cluster, which incurs costs even when not querying. For infrequent ad hoc queries, Athena's pay-per-query serverless model is significantly cheaper than maintaining a persistent Redshift cluster.

---

### Question 18 (5 points)

A Lambda function connects to an Amazon RDS for PostgreSQL database to process incoming events. During peak hours, Lambda scales to 500 concurrent invocations, each opening a new database connection. The RDS instance has a max_connections limit of 400, causing connection failures. The team cannot increase the RDS instance size. Which solution resolves this with MINIMAL code changes?

A. Increase Lambda concurrency limit to 200 and add a CloudWatch Alarm to alert when concurrency approaches the limit

B. Add Amazon RDS Proxy between Lambda and RDS; Lambda connects to the Proxy endpoint instead of directly to RDS

C. Switch from RDS to DynamoDB to eliminate connection limits

D. Implement connection pooling in the Lambda function code using a persistent connection reused across invocations

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Reducing Lambda concurrency limits the throughput of the system, which may not meet processing requirements. It does not solve the fundamental problem — it just reduces the concurrency that causes it. This is a performance sacrifice, not a solution.
- B is correct. RDS Proxy maintains a pool of established database connections and multiplexes many Lambda connections to a much smaller number of actual database connections. Lambda connects to the Proxy endpoint (one code change), and the Proxy handles connection pooling transparently. The Proxy can support thousands of Lambda invocations while maintaining far fewer actual RDS connections.
- C is incorrect. Switching from RDS to DynamoDB is a major architectural refactoring requiring rewriting all SQL queries as DynamoDB operations and migrating the data. This is not "minimal code changes."
- D is incorrect. Lambda execution environments are ephemeral and connections established in one execution environment may not persist across invocations. While connection reuse within a warm Lambda execution environment is a good practice, it does not solve the fundamental problem: 500 concurrent Lambda invocations in different execution environments each hold a separate connection, still exceeding the 400-connection limit.

---

### Question 19 (5 points)

A company uses DynamoDB with on-demand capacity mode for a new application. After launch, the application consistently processes 10,000 read requests per second and 2,000 write requests per second. The access pattern is stable and predictable. What change minimizes DynamoDB costs?

A. Keep on-demand mode — it automatically scales and is always cheaper than provisioned mode

B. Switch to provisioned capacity mode with RCUs and WCUs matching the steady traffic pattern, and optionally add Auto Scaling

C. Enable DynamoDB Accelerator (DAX) to reduce the number of read requests hitting DynamoDB

D. Enable DynamoDB global tables to distribute the read load across multiple Regions

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. On-demand mode charges per request (read and write) at a higher per-unit rate than provisioned mode. For predictable, consistent traffic, on-demand mode is more expensive than provisioned capacity. On-demand is optimal for unpredictable workloads where traffic spikes without warning.
- B is correct. Provisioned capacity mode with the traffic's actual RCU/WCU requirements charges at a lower per-unit rate than on-demand. With stable, predictable traffic, provisioned capacity with DynamoDB Auto Scaling (to adjust capacity if needed) is significantly cheaper than on-demand. The Auto Scaling buffer handles minor fluctuations without over-provisioning.
- C is incorrect. DAX reduces DynamoDB read latency and RCU consumption by caching frequently read items, which can reduce costs. However, DAX has its own cluster costs (per-node hourly fee). For simple cost optimization of predictable workloads, switching to provisioned capacity is more straightforward.
- D is incorrect. DynamoDB global tables replicate data to multiple Regions for multi-region active-active use cases. They do not reduce RCU consumption in the primary Region and add replication costs. They are a global availability feature, not a cost optimization for stable single-region workloads.

---

### Question 20 (5 points)

An architect is designing the database tier for an application with these requirements: (1) ACID transactions across multiple tables, (2) SQL query interface, (3) automatic scaling from 0 to 128 vCPUs without connection interruption, (4) MySQL compatibility, and (5) minimum operational overhead. Which database service satisfies ALL five requirements?

A. Amazon RDS for MySQL with Multi-AZ and Auto Scaling on the instance class

B. Amazon Aurora MySQL Serverless v2

C. Amazon DynamoDB with transactions enabled

D. Amazon Aurora MySQL provisioned with read replicas

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. RDS for MySQL supports ACID transactions and SQL, but "scaling from 0 to 128 vCPUs without connection interruption" is not a feature of RDS. Changing the RDS instance class requires a reboot (brief downtime). RDS does not scale automatically from zero.
- B is correct. Aurora MySQL Serverless v2: (1) supports full ACID transactions; (2) SQL interface with MySQL compatibility; (3) scales from 0 to maximum ACUs in fine-grained increments without dropping connections; (4) fully MySQL-compatible; (5) fully managed by AWS. This is the only option that satisfies all five requirements simultaneously.
- C is incorrect. DynamoDB with transactions supports ACID transactions (DynamoDB Transactions API), but it does not support a SQL query interface. DynamoDB uses its own API (PutItem, GetItem, Query, etc.) with a non-relational data model. MySQL compatibility is not applicable.
- D is incorrect. Aurora MySQL provisioned with read replicas supports requirements 1, 2, and 4. However, scaling compute capacity requires selecting a new instance class and waiting for the change to apply — it does not scale automatically or from zero without connection interruption. The operational overhead of managing a provisioned cluster is also higher than Serverless v2.

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
