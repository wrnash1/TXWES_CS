# Video Script: Module 11 — Cloud Spanner and Distributed Databases (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back. This is Part 2 of Module 11: Cloud Spanner and Distributed Databases.

In Part 1 we covered the theory — TrueTime, Paxos, hotspot prevention, and interleaved tables. In Part 2 we get practical: Spanner DDL, transactions, reads, the decision matrix for choosing Spanner vs Cloud SQL, and exam scenarios.

---

## Section 1 — Spanner DDL and Instance Setup

### Creating a Spanner Instance

```bash
# Create a regional Spanner instance
gcloud spanner instances create my-spanner-instance \
  --config=regional-us-central1 \
  --description="Lab Spanner Instance" \
  --processing-units=100 \
  --project=my-project

# Create a multi-region instance
gcloud spanner instances create my-global-instance \
  --config=nam6 \
  --description="Multi-region US instance" \
  --processing-units=1000 \
  --project=my-project
```

**Processing units (PUs):** Spanner compute is measured in processing units. 1,000 PUs = 1 Spanner node. You can provision as few as 100 PUs (0.1 node) for small workloads. One node handles approximately 2,000 QPS of reads or 1,000 QPS of writes at typical query complexity.

### Creating a Database

```bash
gcloud spanner databases create mydb \
  --instance=my-spanner-instance \
  --project=my-project
```

### Applying DDL

```bash
gcloud spanner databases ddl update mydb \
  --instance=my-spanner-instance \
  --ddl='CREATE TABLE customers (
    customer_id STRING(36) NOT NULL,
    full_name STRING(200),
    email STRING(150),
    region STRING(20),
    created_at TIMESTAMP OPTIONS (allow_commit_timestamp=true)
  ) PRIMARY KEY (customer_id)' \
  --project=my-project
```

`OPTIONS (allow_commit_timestamp=true)` is a Spanner-specific feature. When you write `spanner.commit_timestamp()` as the value, Spanner automatically fills in the exact commit timestamp. This is useful for audit logs and event ordering.

---

## Section 2 — Reading and Writing Data

### DML Transactions

Spanner supports standard SQL DML inside ACID transactions.

```sql
-- Insert with generated UUID
INSERT INTO customers (customer_id, full_name, email, region)
VALUES (GENERATE_UUID(), 'Alice Johnson', 'alice@example.com', 'West');

-- Update
UPDATE orders SET status = 'completed', updated_at = CURRENT_TIMESTAMP
WHERE order_id = '550e8400-e29b-41d4-a716-446655440000';

-- Delete
DELETE FROM orders WHERE status = 'cancelled' AND order_date < '2023-01-01';
```

### Transaction Types in Spanner

Spanner has three transaction types. This is a heavily tested exam topic.

**Read-write transactions** — full ACID transactions that can read and write. All reads within the transaction are consistent at a single timestamp. Writes are batched and applied atomically at commit time.

```bash
gcloud spanner databases execute-sql mydb \
  --instance=my-spanner-instance \
  --sql="SELECT customer_id, full_name FROM customers WHERE region = 'West' LIMIT 10" \
  --project=my-project
```

**Read-only transactions** — provide a consistent snapshot read at a specific timestamp. No locking. Two types:

- **Strong reads** — read the most recent version of data (uses Spanner's global consensus)
- **Stale reads** — read data at a specified timestamp or staleness bound in the past (for example, 15 seconds ago)

Stale reads are significantly cheaper and faster than strong reads because they can be served from any replica without consulting the Paxos leader.

```bash
# Strong read (default)
gcloud spanner databases execute-sql mydb \
  --instance=my-spanner-instance \
  --sql="SELECT COUNT(*) FROM orders WHERE status = 'active'" \
  --project=my-project

# Stale read with 10-second bounded staleness
gcloud spanner databases execute-sql mydb \
  --instance=my-spanner-instance \
  --sql="SELECT COUNT(*) FROM orders WHERE status = 'active'" \
  --read-timestamp=$(date -u -d '10 seconds ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-10S +%Y-%m-%dT%H:%M:%SZ) \
  --project=my-project
```

**Partitioned DML** — a special transaction type for large-scale data manipulation (bulk updates, deletes) that may span many splits. Partitioned DML executes in parallel across splits and does not hold locks on the entire operation.

```sql
-- Update millions of rows without holding a global lock
PDML: UPDATE orders SET archived = true WHERE order_date < '2020-01-01';
```

Partitioned DML has restrictions: it cannot be used with transactions that also include reads (the DML must be standalone), and it is not serializable across the full operation.

---

## Section 3 — Spanner Indexes

Spanner supports secondary indexes, which are implemented as interleaved tables internally.

```sql
-- Standard secondary index
CREATE INDEX idx_customers_email ON customers (email);

-- Storing additional columns in the index (avoids back-join to base table)
CREATE INDEX idx_orders_status ON orders (customer_id, status)
STORING (total_amount, order_date);

-- Query that uses the STORING index (no back-join needed)
SELECT order_id, total_amount, order_date
FROM orders@{FORCE_INDEX=idx_orders_status}
WHERE customer_id = '550e8400-...' AND status = 'active';
```

`STORING` in Spanner is equivalent to `INCLUDE` in PostgreSQL — it stores additional columns in the index to enable index-only lookups.

The `@{FORCE_INDEX=index_name}` hint forces Spanner to use a specific index when the optimizer would not otherwise choose it.

### Interleaved Indexes

Indexes can also be interleaved in parent tables for co-location:

```sql
CREATE INDEX idx_orders_date ON orders (customer_id, order_date DESC),
  INTERLEAVE IN customers;
```

This stores the index entries adjacent to the parent customer rows, making customer-specific queries extremely fast.

---

## Section 4 — Spanner SQL Dialect

Spanner uses **GoogleSQL** (formerly called Cloud Spanner dialect SQL), which is ANSI SQL with some extensions. Key differences from PostgreSQL/MySQL:

- No `AUTO_INCREMENT` or `SERIAL` — use `GENERATE_UUID()` or `GET_NEXT_SEQUENCE_VALUE()`
- `INT64` not `INTEGER` or `BIGINT`
- `STRING(n)` not `VARCHAR(n)`
- `FLOAT64` not `DOUBLE PRECISION`
- Array literals: `ARRAY[1, 2, 3]` or `[1, 2, 3]`
- `TIMESTAMP` is always UTC; no timezone-aware type needed separately
- No stored procedures (as of 2024, user-defined functions are limited)
- Subqueries must use table aliases

### Useful Spanner-Specific Functions

```sql
-- Generate a UUID for a primary key
SELECT GENERATE_UUID();

-- Current timestamp
SELECT CURRENT_TIMESTAMP;

-- Commit timestamp (in a write statement)
INSERT INTO audit_log (id, event, logged_at)
VALUES (GENERATE_UUID(), 'login', PENDING_COMMIT_TIMESTAMP());

-- Array operations
SELECT user_id, roles FROM users
WHERE 'admin' IN UNNEST(roles);
```

---

## Section 5 — Cloud Spanner vs Cloud SQL Decision Matrix

This is the highest-priority topic for the certification exam from Module 11. You must be able to select the right service for a given scenario without hesitation.

| Criterion | Cloud SQL | Cloud Spanner |
|---|---|---|
| Scale | Up to ~30 TB, vertical scaling | Petabyte-scale, horizontal |
| Global distribution | No (single region) | Yes (multi-region, global) |
| Consistency | Strong (single instance) | External consistency (global) |
| Availability SLA | 99.95% (HA) | 99.999% (5 nines) |
| ACID transactions | Yes | Yes |
| SQL dialect | PostgreSQL / MySQL | GoogleSQL |
| Schema migration | Online DDL with some caveats | Online DDL, non-blocking |
| Cost at low scale | Low ($~10/month dev) | Higher (min 100 PUs = ~$65/month) |
| Full-text search | PostgreSQL: tsearch | Limited (use BigQuery or external) |
| Stored procedures | Yes | Limited |
| PRIMARY KEY | Auto-increment supported | UUID recommended; no auto-increment |

### When to Choose Cloud SQL

- Single-region application with moderate data volume (< 10 TB)
- Existing PostgreSQL or MySQL codebase that should not be rewritten
- Budget-sensitive development and small production workloads
- Full stored procedure support required
- Full-text search via PostgreSQL tsearch

### When to Choose Cloud Spanner

- Global application requiring strongly consistent reads/writes across regions
- Five-nines availability requirement
- Write throughput > what a single Cloud SQL instance can handle
- Schema that naturally fits distributed key design (no auto-increment reliance)
- Financial, inventory, or gaming systems requiring global consistency

### The Classic Exam Scenario

The exam will often describe: "A global fintech company needs a database that serves users in the US, Europe, and Asia-Pacific simultaneously with zero data loss and strongly consistent transactions." The answer is Cloud Spanner.

Alternatively: "A startup building a content management system needs a PostgreSQL database with standard SQL features and a monthly budget under $100." The answer is Cloud SQL for PostgreSQL.

---

## Section 6 — Monitoring and Observability

### Cloud Spanner Metrics

```bash
# Check instance utilization
gcloud spanner instances describe my-spanner-instance \
  --project=my-project \
  --format="value(currentDiskBytes,instanceType)"
```

Key metrics available in Cloud Monitoring:

- `spanner.googleapis.com/instance/cpu/utilization` — CPU utilization per node. Sustained > 65% means you need to add processing units.
- `spanner.googleapis.com/instance/storage/utilized_bytes` — storage used.
- `spanner.googleapis.com/api/request_latencies` — 99th percentile latency for reads and writes.

### Query Execution Plans in Spanner

```bash
# Get execution plan for a query
gcloud spanner databases execute-sql mydb \
  --instance=my-spanner-instance \
  --sql="SELECT c.full_name, COUNT(o.order_id) FROM customers c JOIN orders o ON o.customer_id = c.customer_id GROUP BY c.full_name" \
  --query-mode=PLAN \
  --project=my-project
```

Spanner's execution plans show distributed operators like `Distributed Union`, `Distributed Cross Apply`, and `Scan` operations.

---

## Section 7 — Exam Tips for Module 11

**Most-tested scenarios:**

- TrueTime: what it is, why it exists, what problem it solves (don't say "it prevents network latency" — it handles clock uncertainty for transaction ordering)
- Hotspot prevention: monotonically increasing keys = bad; UUID = good; BRIN-style range is not applicable to Spanner
- Interleaved tables: when to use them (parent-child relationships with frequent joins); what the syntax looks like
- Read-only transaction types: strong read vs bounded stale read — stale is cheaper and served from any replica
- Partitioned DML: for bulk operations that would otherwise time out
- Spanner vs Cloud SQL: 5-nines availability, global consistency, petabyte scale → Spanner; standard SQL, low cost, single region → Cloud SQL

**Common traps:**

- The exam may say "the application uses AUTO_INCREMENT primary keys and migrating to Spanner." The correct answer is to redesign primary keys to use UUIDs before migration — Spanner does not support AUTO_INCREMENT.
- "Strong read" in Spanner does NOT mean the query reads from all replicas simultaneously. It means the read is consistent with the most recent committed data, served by (or coordinated through) the Paxos leader.
- Spanner's 99.999% SLA applies to multi-region configurations. A regional Spanner instance has a lower SLA.

---

## Closing

That is Module 11 and the end of our core technical modules. You now have a complete understanding of Cloud Spanner's architecture — from TrueTime and Paxos through DDL, transactions, and the decision matrix.

Complete the Module 11 lab and reading guide. The quiz tests both theoretical concepts and practical SQL syntax.

You have now covered all the major services in the Google Cloud Professional Database Engineer exam: PostgreSQL administration, MySQL and Cloud SQL, backup and recovery, high availability and replication, performance tuning, and Cloud Spanner. Excellent work — see you in the next module.
