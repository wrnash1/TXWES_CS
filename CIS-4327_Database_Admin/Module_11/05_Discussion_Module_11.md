# Discussion Forum: Module 11 — Database Performance Tuning and Query Optimization

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

Post your initial response by **Wednesday at 11:59 PM**. Reply to at least two peers by **Sunday at 11:59 PM**. Each scenario below is independent — your instructor will assign one scenario per section, or you may select the scenario that best matches your professional background.

---

### Scenario A — Diagnosing a Slow Query in Production

A team manages a Cloud SQL for PostgreSQL database supporting an e-commerce platform with 50 million order records. Users report that the order history page takes 45 seconds to load. The DBA runs `EXPLAIN ANALYZE` on the query driving the page and receives the following output:

```
Seq Scan on orders  (cost=0.00..980000.00 rows=18 width=40)
                    (actual time=0.028..44872.341 ms rows=18 loops=1)
  Filter: (customer_id = 'C004421')
  Rows Removed by Filter: 49999982
```

**Discussion Prompt**

Interpret this execution plan output in detail. Identify the scan type, explain what it means operationally, and calculate from the output how many rows the database read to return 18 results. Explain why this query is slow and what specific database change would fix it. After applying the fix, describe what the new execution plan output would look like — specifically, what scan type would replace the current one, what the approximate execution time would be, and why the improvement is so dramatic. Finally, explain what the DBA should check before creating the index to ensure the fix does not negatively impact write performance on this table.

**Response Requirements**

Write 175–225 words. Reference specific values from the execution plan output provided. Explain the mechanism of the fix, not just the command.

**Peer Response Guidance**

When responding to a classmate, evaluate whether their response correctly explains why index scans are faster than sequential scans in terms of algorithmic complexity (O(log n) versus O(n)). If a classmate's response does not address write-side overhead of creating the index, add that consideration and explain when a heavily written table might warrant careful evaluation before adding an index.

---

### Scenario B — Connection Pool Exhaustion at Scale

A SaaS company's application connects to Cloud SQL for PostgreSQL using direct connections from 12 application server instances, each with a thread pool of 100 threads. During peak hours, the application begins receiving `FATAL: sorry, too many clients already` errors. The current instance tier is `db-n1-standard-2`. The engineering team's proposed solution is to upgrade to `db-n1-standard-8` to increase the connection limit.

**Discussion Prompt**

Evaluate the team's proposed solution. Explain why upgrading the instance tier addresses the symptom but not the root cause of connection exhaustion. Describe the correct architectural solution — a connection pooler — and explain specifically how it resolves the problem. Include in your answer: what PgBouncer transaction pooling mode does with a database connection after each COMMIT or ROLLBACK, why this enables thousands of application threads to be served by a small pool of real database connections, and what application compatibility limitations exist in transaction pooling mode that the team must evaluate before deploying. If the team's application uses `SET session_replication_role` or advisory locks across transaction boundaries, what pooling mode should they use instead and why?

**Response Requirements**

Write 175–225 words. Use accurate terminology for connection pooling. Distinguish between application connections and real database connections explicitly.

**Peer Response Guidance**

When responding to a classmate, check whether their response correctly identifies transaction pooling mode as the recommended mode for OLTP applications. If a classmate recommends session pooling as "safer," add context explaining that session pooling provides compatibility at the cost of efficiency and is generally only necessary when the application uses session-level state that must persist across transactions.

---

### Scenario C — Spanner Hotspot and BigQuery Scan Optimization

A financial services team manages two GCP databases: a Cloud Spanner instance for transaction processing and a BigQuery data warehouse for analytics. The Spanner table uses a `BIGINT AUTOINCREMENT` primary key. Engineers observe that write throughput is saturated on a single Spanner node even though the instance has 10 nodes with low average utilization. Separately, a BigQuery analyst reports that queries filtering on `transaction_status = 'settled'` scan all 730 daily partitions on a table partitioned by `transaction_date`, despite the analyst only needing data from the past 7 days.

**Discussion Prompt**

Address both problems. For Spanner: explain the root cause of the single-node write saturation — specifically, why an auto-increment primary key creates a hotspot in Spanner's distributed architecture — and describe the correct primary key strategy to eliminate it. For BigQuery: explain why the `transaction_status` filter does not prevent the full partition scan and what the analyst must add to the query to enable partition pruning. Then describe the relationship between partitioning and clustering in BigQuery and explain what additional optimization the analyst could apply after fixing the partition pruning issue, and what query patterns that optimization would help.

**Response Requirements**

Write 175–225 words. Address both the Spanner and BigQuery problems. For BigQuery, include the specific clause the analyst must add to the query.

**Peer Response Guidance**

When responding to a classmate, evaluate their BigQuery response. If a classmate suggests clustering as the fix for the full partition scan, clarify that clustering improves block-level pruning within partitions but does not substitute for a partition column filter. The full partition scan continues unless the WHERE clause includes a filter on the partition column.

---

### Discussion Rubric — 10 Points Total

| Component | Points | Criteria |
|---|---|---|
| Initial post — technical accuracy | 3 | GCP terminology correct; plan interpretation accurate; no factual errors |
| Initial post — depth of analysis | 2 | Explains mechanisms and trade-offs, not just recommendations |
| Initial post — word count and clarity | 1 | 175–225 words; organized and readable |
| Peer response 1 | 2 | Adds technical content; addresses the specific guidance note for the scenario |
| Peer response 2 | 2 | Adds technical content; engages with a different aspect than Peer Response 1 |

**Note from Professor Nash:** The exam will show you an `EXPLAIN ANALYZE` output or a performance scenario and expect you to identify the root cause and the specific corrective action. Responses that demonstrate you can read an execution plan, identify the problem, explain the fix mechanistically, and address side effects will earn full marks. Responses that only name the correct tool or command without explaining the underlying mechanism will not.

---

Reference: cloud.google.com/learn
