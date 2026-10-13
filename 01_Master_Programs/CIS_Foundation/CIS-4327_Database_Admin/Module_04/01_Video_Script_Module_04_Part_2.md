# Video Script: Module 04 — Cloud Spanner: Globally Distributed Databases (Part 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 11–13 minutes

---

### Opening

**[SHOW SLIDE: Module 04 Part 2 — DML, Secondary Indexes, Staleness, and Exam Tips]**

Welcome back. I am Professor Nash, and this is Part 2 of Module 04.

In Part 1 we covered Spanner's architecture, consistency model, DDL, and primary key design. Now we cover DML — how to query and mutate data in Spanner — secondary indexes, the concept of stale reads, and the exam scenarios that test when to choose Spanner.

---

### Section 1 — Spanner DML and Queries

**[SHOW CODE]**

```sql
-- Standard SQL SELECT
SELECT s.FullName, e.Grade, c.CourseName
FROM   Students  s
JOIN   Enrollments e ON s.StudentId = e.StudentId
JOIN   Courses     c ON e.CourseId  = c.CourseId
WHERE  s.EnrolledYear = 2024
ORDER  BY s.FullName;

-- INSERT
INSERT INTO Students (StudentId, FullName, Email, EnrolledYear)
VALUES (1001, 'Alice Johnson', 'alice@txwes.edu', 2024);

-- UPDATE
UPDATE Students
SET    FullName = 'Alice M. Johnson'
WHERE  StudentId = 1001;

-- DELETE
DELETE FROM Students
WHERE  StudentId = 1001;
```

**[END CODE]**

Spanner supports ANSI SQL for queries, INSERT, UPDATE, and DELETE. The syntax is very similar to standard SQL with a few differences.

Spanner also supports Mutations — an alternative to DML that performs batched read-modify-write operations. Mutations are lower-latency than DML for bulk operations because they bypass the query planner. However, they do not support conditional logic (WHERE clauses on reads before writes). DML is preferred for most application code; Mutations are used in high-throughput batch write scenarios.

---

### Section 2 — Secondary Indexes

**[SHOW CODE]**

```sql
-- Create a secondary index on Email for fast lookup
CREATE INDEX IdxStudentEmail
    ON Students (Email);

-- Create a secondary index with stored columns (covering index)
CREATE INDEX IdxEnrollmentsByCourse
    ON Enrollments (CourseId)
    STORING (Grade, EnrolledAt);
```

**[END CODE]**

Spanner secondary indexes work similarly to indexes in relational databases — they provide an alternate key path to find rows without a full table scan.

The STORING clause creates a covering index. The stored columns (Grade, EnrolledAt) are physically copied into the index, so a query that needs those columns can satisfy the entire request from the index without reading back to the base table. This eliminates the extra network hop to fetch non-indexed columns.

Without STORING, Spanner performs a back-join from the index to the base table to retrieve non-indexed columns. For large result sets, this adds latency.

---

### Section 3 — Stale Reads and Bounded Staleness

**[SHOW SLIDE: Strong reads vs. stale reads timeline]**

Spanner provides two read modes.

Strong reads return the most recent committed data as of the current transaction timestamp. All strong reads go through the Paxos leader, which adds latency because the leader must confirm that no newer transaction has committed since the read timestamp.

Stale reads allow the client to read data as of a timestamp slightly in the past. This is called bounded staleness. The client specifies either an exact timestamp or a maximum staleness duration (e.g., 15 seconds ago). Stale reads can be served by any replica, not just the leader, which dramatically reduces latency for read-heavy workloads.

**[SHOW SLIDE: Staleness trade-off — lower latency vs. potentially slightly outdated data]**

For the GCP exam, know this trade-off: if a scenario requires absolute current consistency (financial balance checks, inventory reservation), use strong reads. If a scenario describes a dashboard or reporting query where data that is a few seconds old is acceptable, bounded staleness reads provide lower latency and reduce load on the primary replica.

---

### Section 4 — Transactions in Cloud Spanner

**[SHOW CODE]**

```sql
-- Read-write transaction example (application code concept)
BEGIN TRANSACTION;

UPDATE Accounts
SET    Balance = Balance - 500
WHERE  AccountId = 'ACC-001';

UPDATE Accounts
SET    Balance = Balance + 500
WHERE  AccountId = 'ACC-002';

COMMIT;
```

**[END CODE]**

Spanner's read-write transactions use a two-phase commit protocol internally. When a transaction spans multiple Spanner servers (because the rows it reads and writes are on different tablets), Spanner's TrueTime-based protocol ensures that all servers agree on the commit order without a central coordinator.

The client application should implement retry logic for transactions that are aborted due to lock conflicts. Spanner aborts conflicting transactions and the client must retry. This is standard behavior for any database that provides serializable or stronger isolation.

---

### Section 5 — Spanner Managed Backup and PITR

**[SHOW CODE]**

```bash
# Create a Spanner database backup
gcloud spanner backups create my-backup \
    --instance=txwes-spanner \
    --database=university_db \
    --expiration-date=2025-12-31

# List available backups
gcloud spanner backups list \
    --instance=txwes-spanner

# Restore from a backup
gcloud spanner databases restore \
    --destination-instance=txwes-spanner \
    --destination-database=university_db_restored \
    --source-instance=txwes-spanner \
    --source-backup=my-backup
```

**[END CODE]**

Cloud Spanner supports managed backups with configurable expiration dates. Spanner also supports point-in-time recovery to any second within the version retention period, which can be set from 1 hour to 7 days. No additional configuration is required — Spanner retains old versions of data automatically within the retention window.

---

### Section 6 — Exam Tips for Module 04

**[SHOW SLIDE: Cloud Spanner exam tips]**

Tip one: the exam will present a scenario with a requirement for global consistency and horizontal scalability. The answer is Cloud Spanner. No other GCP service provides both properties simultaneously.

Tip two: Cloud Spanner's SLA is 99.999% (five nines) for multi-region configurations. This is the highest availability SLA of any GCP database service. Scenarios with contractual five-nines availability requirements point to Spanner.

Tip three: sequential auto-increment primary keys are a hotspot anti-pattern in Spanner. When an exam question describes write performance degrading on a Spanner table, suspect a sequential primary key. The fix is UUID or bit-reversed keys.

Tip four: INTERLEAVE IN PARENT is not a relationship or constraint — it is a physical storage optimization. It co-locates child rows with parent rows to eliminate cross-server reads. Know what it does and when to use it (parent-child access patterns).

Tip five: stale reads reduce latency by allowing any replica to serve the read. Strong reads require the Paxos leader. When a scenario asks how to reduce Spanner read latency for a dashboard that can tolerate slightly old data, bounded staleness is the answer.

Tip six: Spanner uses processing units, not machine types. 1000 PUs = 1 node. The minimum for production is typically 1 node (1000 PUs). 100 PUs is only for very light development workloads.

Tip seven: Spanner does not have a concept of "read replicas" in the Cloud SQL sense. In multi-region configurations, all replicas are part of the same Paxos consensus group and can serve reads. Adding regions adds both read capacity and write latency.

Tip eight: Cloud Spanner is significantly more expensive than Cloud SQL. Any exam question comparing the two must weigh cost against the global consistency and availability requirements. If the workload is regional and cost-sensitive, Cloud SQL is typically the right answer.

---

### Closing — Module 04 Wrap-Up

**[SHOW SLIDE: Module 04 complete]**

That completes Module 04. You now understand Cloud Spanner's architecture, schema design principles, DML, secondary indexes, read modes, and how to position it against Cloud SQL.

Your lab walks you through creating a Spanner instance, designing a schema with interleaved tables, running queries, and creating a backup.

In Module 05 we move to Bigtable — Google's wide-column NoSQL store for massive-scale time-series and analytics workloads. It is a completely different data model from anything we have covered so far.

See you in Module 05.

---

Reference: cloud.google.com/learn
