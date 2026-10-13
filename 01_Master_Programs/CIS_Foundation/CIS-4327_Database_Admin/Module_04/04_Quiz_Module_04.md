# Quiz: Module 04 — Cloud Spanner: Globally Distributed Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A global retail company needs a database to manage inventory across warehouses in North America, Europe, and Asia. Every inventory update must be immediately consistent across all regions — a product sold in Dallas must never appear as available in London simultaneously. The system must scale to handle 50,000 writes per second. Which GCP database service is most appropriate?

- A) Cloud Spanner with a multi-region configuration
- B) Cloud SQL for PostgreSQL with cross-region read replicas
- C) Firestore in native mode with multi-region replication
- D) BigQuery with a replicated dataset across regions

Correct Answer: A — Cloud Spanner multi-region provides full ACID transactions with external consistency across regions and scales horizontally by adding processing units. It is the only GCP service that provides both global strong consistency and horizontal write scalability at this scale.

Distractor analysis: B is incorrect because Cloud SQL cross-region read replicas use asynchronous replication; a write in Dallas may not be immediately visible in London — this violates the strong consistency requirement. C is incorrect because Firestore provides eventual consistency at the document level; it does not provide strongly consistent transactions across documents in the same way Spanner does. D is incorrect because BigQuery is an analytical data warehouse and does not support transactional writes at 50,000 per second.

---

### Question 2

A Cloud Spanner table uses an auto-incrementing INT64 as its primary key. After several months in production, the engineering team reports that write throughput has not improved despite adding more Cloud Spanner nodes. What is the root cause?

- A) Sequential primary keys concentrate all writes on the tablet holding the highest key range, creating a hotspot that a single tablet serves regardless of node count.
- B) The INT64 data type does not support distributed storage in Cloud Spanner; STRING keys are required.
- C) The table needs secondary indexes before Cloud Spanner can distribute writes across nodes.
- D) Cloud Spanner does not support horizontal scaling for write operations; only reads scale horizontally.

Correct Answer: A — Sequential auto-incrementing keys cause a hotspot because all new inserts have the highest key value and go to the same tablet (the one responsible for the highest key range). Adding more nodes does not help because the insert workload cannot be distributed across tablets — it is always concentrated on one.

Distractor analysis: B is incorrect because INT64 is a valid Spanner type for primary keys; the problem is sequential values, not the data type itself. C is incorrect because secondary indexes do not affect how writes to the base table are distributed; they are for read access paths. D is incorrect because Cloud Spanner does scale writes horizontally — but only when the primary key design distributes rows across tablets.

---

### Question 3

You are designing a Cloud Spanner schema for a banking application. Each Account record has many Transaction records that are almost always queried through the Account. What Spanner design technique should you use?

- A) Define Transactions as an interleaved table in Account so Transaction rows are stored co-located with their parent Account row.
- B) Create a secondary index on Transactions.AccountId so joins between Account and Transactions are faster.
- C) Store Transactions as a STRUCT array column in the Account table to avoid a separate table.
- D) Use a Cloud SQL for PostgreSQL foreign key constraint to enforce the Account-Transaction relationship.

Correct Answer: A — Interleaving Transactions in Account physically co-locates Transaction rows with their parent Account row on the same Spanner server. Queries that read an account and all its transactions require no cross-server network hops. This is the recommended Spanner design for parent-child access patterns.

Distractor analysis: B is incorrect because a secondary index improves lookup by a non-primary-key column but does not provide physical co-location; the Transaction rows are still potentially on different servers from the Account. C is incorrect because storing repeated entities as STRUCT arrays within a column violates relational design principles and makes individual transactions unqueryable with standard SQL. D is incorrect because Cloud SQL foreign keys have no role in a Cloud Spanner schema design.

---

### Question 4

A financial reporting dashboard queries Cloud Spanner every 5 seconds to display account balance summaries. The query must return quickly and the dashboard can tolerate data that is up to 10 seconds old. Which read mode should be used?

- A) Bounded staleness read with a maximum staleness of 10 seconds
- B) Strong read to ensure the most current balance data
- C) Read-write transaction to lock the balance rows during the read
- D) Export to BigQuery and query from there instead

Correct Answer: A — Bounded staleness reads allow Spanner to serve the request from any replica (not just the Paxos leader), reducing latency significantly. Since the dashboard can tolerate 10-second-old data, a bounded staleness read of 10 seconds is appropriate and will reduce both latency and load on the leader replica.

Distractor analysis: B is incorrect because strong reads are higher latency and route to the Paxos leader unnecessarily when slightly stale data is acceptable. C is incorrect because a read-write transaction acquires locks, increases latency, and is only appropriate when the read is part of a conditional write operation. D is incorrect because exporting to BigQuery adds significant latency and operational complexity for a 5-second dashboard refresh cycle.

---

### Question 5

Which Cloud Spanner SLA level is provided for a multi-region instance configuration?

- A) 99.999% (five nines)
- B) 99.99% (four nines)
- C) 99.95% (three and a half nines)
- D) 99.9% (three nines)

Correct Answer: A — Cloud Spanner multi-region configurations provide a 99.999% (five nines) SLA. This is the highest availability guarantee of any GCP database service. Regional Spanner configurations also provide 99.999% availability across three zones within one region.

Distractor analysis: B is incorrect because 99.99% is the SLA for Cloud SQL Enterprise Plus HA instances; it is not the Spanner multi-region SLA. C is incorrect because 99.95% is the SLA for Cloud SQL Enterprise HA instances. D is incorrect because 99.9% is lower than what Spanner provides; it corresponds to typical single-zone services without HA.

---

### Question 6

A developer creates the following Cloud Spanner DDL. What will happen when a Warehouse row is deleted?

```sql
CREATE TABLE Products (
    WarehouseId STRING(36)  NOT NULL,
    ProductId   STRING(36)  NOT NULL,
    ProductName STRING(200) NOT NULL
) PRIMARY KEY (WarehouseId, ProductId),
  INTERLEAVE IN PARENT Warehouses ON DELETE CASCADE;
```

- A) All Products rows with that WarehouseId will be automatically deleted.
- B) The delete will fail because Products rows exist for that Warehouse.
- C) The Products rows will have their WarehouseId set to NULL.
- D) Interleaved tables do not support ON DELETE CASCADE; the DDL will fail to compile.

Correct Answer: A — ON DELETE CASCADE in an INTERLEAVE IN PARENT definition causes all interleaved child rows to be automatically deleted when the parent row is deleted. This is the same semantic as ON DELETE CASCADE in a standard foreign key constraint, applied to the physical co-location structure.

Distractor analysis: B is incorrect because ON DELETE CASCADE explicitly allows the parent deletion and automatically removes children; it does not block the delete. C is incorrect because cascade behavior deletes the child rows entirely; it does not set a column to NULL (that would be ON DELETE SET NULL, which is not supported in Spanner interleaving). D is incorrect because ON DELETE CASCADE is valid syntax for interleaved tables in Cloud Spanner.

---

### Question 7

You are creating a secondary index on a Cloud Spanner table and want to avoid back-joins to the base table for queries that retrieve ProductName and StockQuantity filtered by Category. Which DDL correctly implements this?

- A) `CREATE INDEX IdxCategory ON Products (Category) STORING (ProductName, StockQuantity);`
- B) `CREATE INDEX IdxCategory ON Products (Category, ProductName, StockQuantity);`
- C) `CREATE UNIQUE INDEX IdxCategory ON Products (Category);`
- D) `CREATE INDEX IdxCategory ON Products STORING (Category, ProductName, StockQuantity);`

Correct Answer: A — The STORING clause in a Cloud Spanner secondary index copies the specified columns into the index structure. When a query filters by Category and projects ProductName and StockQuantity, the entire result can be served from the index without reading back to the base table (a back-join).

Distractor analysis: B is incorrect because including non-selective columns (ProductName, StockQuantity) in the index key columns (not STORING) inflates the index size and changes the index key structure unnecessarily; STORING is the correct mechanism for read-only projection columns. C is incorrect because a UNIQUE index on Category would fail if any two products share the same category, which is the expected case; it also does not store the additional columns. D is incorrect because STORING must list columns that are not part of the index key; Category is already the index key column and should not be in the STORING list.

---

### Question 8

What does TrueTime provide that enables Cloud Spanner's external consistency guarantee?

- A) Globally synchronized timestamps accurate to within a few milliseconds, allowing Spanner to order transactions across distributed data centers without a central coordinator.
- B) A unique transaction ID assigned by a central global coordinator that all Spanner nodes contact before committing.
- C) A vector clock implementation that tracks causality between transactions within a single Spanner region.
- D) A distributed lock manager that holds write locks globally while transactions are in progress.

Correct Answer: A — TrueTime uses atomic clocks and GPS receivers in every Google data center to provide a globally synchronized clock with bounded uncertainty (typically a few milliseconds). By knowing the precise global time, Spanner can assign commit timestamps that are guaranteed to be after the timestamps of all previously committed transactions, eliminating the need for a central coordinator.

Distractor analysis: B is incorrect because TrueTime specifically eliminates the need for a central coordinator; requiring nodes to contact a central coordinator would create a bottleneck and a single point of failure. C is incorrect because TrueTime is a physical clock mechanism, not a vector clock (logical causality tracker); it provides real-time ordering, not just causal ordering. D is incorrect because TrueTime is a timekeeping infrastructure, not a lock manager; Spanner does use locking internally, but TrueTime's role is timestamp assignment, not lock coordination.

---

### Question 9

Which statement correctly describes the difference between Cloud Spanner Mutations and Cloud Spanner DML?

- A) Mutations are batched write operations without conditional logic; DML supports conditional WHERE clauses and is preferred for most application code.
- B) DML is faster than Mutations for all write operations; Mutations are only used for schema changes.
- C) Mutations provide ACID guarantees while DML does not; use Mutations for all transactional writes.
- D) Mutations and DML are interchangeable; they produce identical performance and behavior.

Correct Answer: A — Mutations are a set of buffered Insert/Update/Delete operations applied atomically at commit time. They bypass the query planner and are faster for bulk writes but cannot evaluate conditional logic (no WHERE clause reads before writes). DML (INSERT, UPDATE, DELETE with WHERE clauses) supports conditional write logic and is easier to work with for most application use cases.

Distractor analysis: B is incorrect because Mutations are often faster than DML for bulk writes precisely because they bypass the query planner; the claim that DML is faster for all operations is wrong. C is incorrect because both Mutations and DML provide full ACID guarantees within a Spanner transaction; the distinction is expressiveness and performance, not consistency. D is incorrect because Mutations and DML have meaningful differences in capabilities and performance characteristics.

---

### Question 10

A Cloud Spanner instance currently handles its peak load at 80% CPU utilization with 2000 processing units. The team expects a 3x traffic increase in the next quarter. What is the correct scaling action?

- A) Increase the processing units to approximately 6000 to proportionally handle 3x traffic while maintaining headroom.
- B) Create read replicas and distribute traffic across them.
- C) Increase the machine tier from Standard to High-Memory.
- D) Migrate the workload to Cloud SQL for PostgreSQL, which supports higher connection counts.

Correct Answer: A — Cloud Spanner scales horizontally by adding processing units. At 80% CPU with 2000 PUs handling current load, a 3x traffic increase would require approximately 3x the processing units. Increasing to 6000 PUs provides the proportional capacity and maintains some headroom above 80% utilization.

Distractor analysis: B is incorrect because Cloud Spanner does not have separate read replicas in the Cloud SQL sense; in multi-region configurations all replicas serve reads as part of the consensus group, and capacity is scaled by adding processing units to the instance, not by creating separate replica instances. C is incorrect because Cloud Spanner does not have machine tiers the way Cloud SQL does; capacity is expressed in processing units, not memory-optimized machine types. D is incorrect because migrating to Cloud SQL would remove global consistency and horizontal scaling capabilities, regressing the architecture.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

A Cloud Spanner table is defined with a UUID (STRING(36)) primary key generated using `GENERATE_UUID()`. A developer proposes switching to a SHA-256 hash of a business key instead. What is the primary reason UUID or hash-based keys are preferred over sequential integers in Cloud Spanner?

- A) They produce random key values that distribute rows evenly across tablets, preventing write hotspots.
- B) UUID keys are smaller in storage than INT64, reducing tablet storage consumption.
- C) Cloud Spanner's query optimizer requires string keys to build efficient execution plans.
- D) Sequential integer keys violate the Cloud Spanner DDL syntax rules for primary key definitions.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A UUID stored as STRING(36) is larger than an INT64; storage size is not the motivation for using UUIDs in Spanner.
  - C) The query optimizer works with both INT64 and STRING primary keys; key type does not determine optimizer behavior.
  - D) Cloud Spanner fully supports INT64 as a primary key data type; the issue is the sequential pattern of values, not the type itself.

---

### Question 12 (5 points)

A Cloud Spanner read-write transaction reads a row, performs a computation, and then updates that row. The transaction spans 45 seconds of application processing time. What risk does this create?

- A) The transaction's read locks will expire after the default 10-second idle timeout, causing the transaction to abort with a DEADLINE_EXCEEDED error.
- B) Another transaction that reads the same row will be blocked for 45 seconds, degrading overall throughput.
- C) The Paxos consensus vote will time out if the transaction does not commit within 30 seconds.
- D) Cloud Spanner will automatically commit the transaction after 30 seconds to prevent lock accumulation.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Spanner uses optimistic concurrency for reads in read-write transactions; read locks in a snapshot read do not block concurrent readers; the contention risk is at commit time, not during the read phase.
  - C) The Paxos consensus vote occurs at commit time, not during the transaction's open window; a 45-second transaction does not directly cause a Paxos timeout unless the commit itself is delayed.
  - D) Cloud Spanner does not auto-commit open transactions; it aborts them when they exceed the maximum transaction duration limit.

---

### Question 13 (5 points)

Which Cloud Spanner feature allows an application to run a read-only workload and explicitly specify that it should observe a consistent snapshot of the database as of 30 seconds ago?

- A) Timestamp-bound read using `read_timestamp` or `exact_staleness` set to 30 seconds.
- B) Read-write transaction with a `SET TRANSACTION READ ONLY` statement.
- C) Blind write Mutation with a timestamp set to 30 seconds in the past.
- D) A secondary index with a STORING clause covering all queried columns.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `SET TRANSACTION READ ONLY` is a SQL SQL Server/Oracle concept; Cloud Spanner read-only transactions use timestamp bound parameters in the client library API, not SQL syntax.
  - C) A blind write Mutation is a write operation; setting a past timestamp on a Mutation does not create a read snapshot.
  - D) A STORING secondary index optimizes read performance by eliminating back-joins; it does not control the staleness or snapshot time of a read.

---

### Question 14 (5 points)

You are migrating a workload to Cloud Spanner. The source schema has a `products` table and a `product_images` table joined by `product_id`. In production, images are always fetched together with their product. Which Spanner schema design is recommended?

- A) Interleave `product_images` in parent `products` so image rows are physically co-located with product rows.
- B) Create a secondary index on `product_images.product_id` with STORING for all image columns.
- C) Merge both tables into a single `products` table with image data stored as a BYTES column.
- D) Keep the tables separate with standard foreign keys and rely on Spanner's join optimizer.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A secondary index with STORING still requires a back-join to the base table for columns not in STORING, and does not provide physical co-location of parent and child rows on the same server.
  - C) Storing binary image data as a BYTES column in the parent table creates very large rows, complicates querying individual images, and is not the recommended relational approach.
  - D) Cloud Spanner does not support foreign key constraints with the same semantics as traditional RDBMS; interleaving is the recommended design for parent-child access patterns, not separate tables with implicit joins.

---

### Question 15 (5 points)

An engineering team wants to perform a schema change on a production Cloud Spanner table that has millions of rows — specifically adding a new NOT NULL column with a default value. What is true about schema changes in Cloud Spanner?

- A) Cloud Spanner schema changes are fully online and non-blocking; the new column is added without locking the table or requiring a maintenance window.
- B) Adding a NOT NULL column requires taking the table offline to backfill all existing rows with the default value before the change completes.
- C) Cloud Spanner does not support NOT NULL constraints; all columns are implicitly nullable.
- D) Schema changes in Cloud Spanner require exporting all data, dropping the table, recreating it with the new schema, and reimporting the data.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Spanner performs schema changes online using a long-running schema change operation; it does not lock the table; backfill of NOT NULL columns with defaults happens in the background.
  - C) Cloud Spanner does support NOT NULL constraints on columns; this is a valid DDL constraint.
  - D) The export-drop-recreate-reimport approach is required in some traditional databases but not in Cloud Spanner, where DDL changes are applied online as background operations.

---

### Question 16 (5 points)

What is the purpose of the `NULLS_FIRST` ordering behavior for Cloud Spanner's ASC sort order on secondary index keys?

- A) NULL values sort before non-NULL values in ascending order, which means NULLable indexed columns place rows with NULL key values at the start of the index.
- B) NULL values are excluded from the secondary index entirely, reducing index size.
- C) NULLable columns cannot be used as secondary index keys in Cloud Spanner.
- D) NULL values always sort after non-NULL values regardless of ASC or DESC ordering in Spanner.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) NULL values are included in Cloud Spanner secondary indexes; they are not excluded; understanding their sort position is important for query correctness.
  - C) NULLable columns can be used as secondary index keys in Cloud Spanner; the index handles NULL values with defined ordering semantics.
  - D) Cloud Spanner's behavior is NULL FIRST for ASC and NULL LAST for DESC, which is the opposite of some other SQL databases; this is specifically tested behavior.

---

### Question 17 (5 points)

A Cloud Spanner database uses a multi-region configuration spanning `nam6` (North America). A regional outage takes down one of the read-write regions. What is the expected behavior?

- A) Spanner continues serving reads and writes from the remaining regions without data loss; the Paxos quorum can still be achieved with the surviving replicas.
- B) All write transactions are blocked until the failed region recovers to maintain strict consistency.
- C) Spanner automatically promotes a read-only replica to a read-write replica and redirects all traffic.
- D) The database enters read-only mode until the failed region is restored to prevent split-brain writes.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The Paxos consensus protocol in Spanner is designed to tolerate the loss of minority replicas; a quorum of surviving replicas can continue committing transactions without blocking.
  - C) Spanner's multi-region configuration does not have a separate "promotion" step; the consensus group automatically re-forms around surviving replicas.
  - D) Entering read-only mode would violate the 99.999% SLA guarantee; Spanner's design specifically prevents this by using a quorum that can function without a single region.

---

### Question 18 (5 points)

Which statement correctly describes Cloud Spanner's PITR (point-in-time recovery) capability compared to Cloud SQL PITR?

- A) Cloud Spanner has built-in version retention for PITR with no additional configuration; Cloud SQL requires WAL archiving to be explicitly enabled before PITR is possible.
- B) Cloud SQL PITR supports any point within the last 30 days; Cloud Spanner PITR is limited to the last 1 hour.
- C) Both services require manual snapshot exports to Cloud Storage before PITR is possible.
- D) Cloud Spanner PITR requires Enterprise Plus edition while Cloud SQL PITR is available on all editions.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Spanner's version retention window is configurable up to 7 days; Cloud SQL PITR retention is also configurable but not 30 days by default; the key distinction is that Spanner requires no setup while Cloud SQL requires enabling WAL archiving.
  - C) Cloud SQL PITR does not require manual snapshot exports; it uses WAL logs; Cloud Spanner PITR uses built-in versioning; neither requires manual exports.
  - D) Cloud Spanner does not have edition tiers that control PITR; all Spanner instances support version retention.

---

### Question 19 (5 points)

A development team wants to query Cloud Spanner from within a Python application. Which client library approach does Google recommend for new applications?

- A) Use the `google-cloud-spanner` Python client library with the Spanner client and transaction API.
- B) Connect using a standard PostgreSQL JDBC driver pointed at the Spanner instance's IP address.
- C) Use the REST API directly with `urllib` and manually construct JSON mutation payloads.
- D) Use the `psycopg2` PostgreSQL adapter since Cloud Spanner supports a PostgreSQL dialect.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Spanner does not expose a standard PostgreSQL TCP port; it uses gRPC-based connections through the Cloud Spanner API, not a standard database TCP socket.
  - C) Using raw REST API calls is functionally possible but is significantly more complex and error-prone than using the client library; Google explicitly recommends the client library for all new applications.
  - D) While Cloud Spanner does support a PostgreSQL-compatible dialect through the PGAdapter proxy, `psycopg2` connecting directly without PGAdapter does not work; the client library is the recommended approach.

---

### Question 20 (5 points)

An application inserts 10,000 rows into Cloud Spanner in a single operation. Which approach provides the best throughput?

- A) Use Mutations buffered in a single read-write transaction committed atomically, leveraging Spanner's batch write capability.
- B) Issue 10,000 individual DML INSERT statements in separate transactions.
- C) Use a single DML INSERT ... SELECT statement reading from a subquery.
- D) Export the rows to Cloud Storage as CSV and use Spanner's built-in data import to load them.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Issuing 10,000 separate transactions adds network round-trip overhead for each commit; batching mutations in one transaction is dramatically faster.
  - C) INSERT ... SELECT in DML reads from a subquery within the same database; it does not apply to loading externally generated rows and goes through the query planner, which is slower than batched mutations.
  - D) Cloud Spanner does not have a built-in CSV import feature equivalent to Cloud SQL's import; data loading is done through client libraries using mutations or the Dataflow template for large datasets.
