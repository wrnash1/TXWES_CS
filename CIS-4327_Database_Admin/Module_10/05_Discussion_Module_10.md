# Discussion Forum: Module 10 — Database Performance Tuning

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Discussion Prompt

Performance tuning requires combining diagnostic tools, knowledge of index types, and an understanding of query patterns to systematically reduce latency. In this discussion, you will analyze a real query problem and design an indexing strategy.

Respond to **both parts** below.

---

## Part A — EXPLAIN ANALYZE Interpretation

The following is an EXPLAIN ANALYZE output from a production PostgreSQL database. Read it carefully and answer the questions below.

```text
Gather  (cost=1000.00..89234.12 rows=4821 width=72)
        (actual time=1203.44..8920.11 rows=3987 loops=1)
  Workers Planned: 2
  Workers Launched: 2
  ->  Parallel Seq Scan on orders  (cost=0.00..87751.02 rows=2008 width=72)
                                   (actual time=1189.33..8840.05 rows=1329 loops=3)
        Filter: ((status = 'completed') AND (total_amount > 10000.00)
                  AND (order_date >= '2024-01-01'::date))
        Rows Removed by Filter: 1498671
        Buffers: shared read=21450
```

Answer all four questions in your post:

1. **Plan interpretation:** What is this query doing at a high level? What does the `Gather` node indicate? What does `Parallel Seq Scan` mean?

2. **The filter problem:** `Rows Removed by Filter: 1,498,671` while only 3,987 rows were returned. What does this ratio tell you about the efficiency of the current plan?

3. **Buffers analysis:** `Buffers: shared read=21,450` means all 21,450 pages were read from disk (none from cache). What does this tell you about the working set relative to the server's `shared_buffers`, and what are two possible remedies?

4. **Index recommendation:** Recommend one or two specific indexes that would improve this query. Include the full `CREATE INDEX` statement for each, specifying the index type, columns, and any partial index condition. Explain why each choice would improve the plan.

---

## Part B — Index Design Trade-off

A startup is building an event analytics platform. The main table is:

```sql
CREATE TABLE events (
    event_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    properties JSONB,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- 500 million rows, growing 50 million rows per month
-- Rows are always inserted in occurred_at order
```

The application runs these three query patterns regularly:

- Pattern 1: `WHERE user_id = $1 ORDER BY occurred_at DESC LIMIT 50` — user activity feed
- Pattern 2: `WHERE properties @> '{"campaign": "summer2024"}'` — campaign analytics
- Pattern 3: `WHERE occurred_at >= $1 AND occurred_at < $2` — time-range scans for reports

Answer these questions:

1. For each of the three patterns, identify the most appropriate index type (B-tree, BRIN, GIN, partial, covering, etc.) and explain why.

2. The team proposes adding a B-tree index on `occurred_at` for Pattern 3. You propose a BRIN index instead. Write a 3–4 sentence justification for your BRIN recommendation using specific properties of the table.

3. The team is concerned that the GIN index for Pattern 2 will significantly slow down inserts (50 million per month). Is this concern valid? What mitigation strategies exist for GIN index maintenance overhead on high-write tables?

---

## Response Requirements

- Initial post: 400–500 words covering both parts.
- Reply to at least two classmates: 100–150 words each.
- Replies should either challenge an index choice with a counter-argument (for example, pointing out a pattern the chosen index does not cover) or extend the answer with an additional optimization.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part A — all four questions answered with specific CREATE INDEX statements | 40 |
| Part B — all three query patterns addressed with correct index types | 35 |
| Two substantive peer replies | 20 |
| Clear technical writing, correct SQL syntax | 5 |
| **Total** | **100** |

---

## Instructor Notes

Part A is intentionally based on a realistic production query plan. The key insights students should reach are: (1) the Parallel Seq Scan with 1.5 million filtered rows is very inefficient; (2) a partial index on `(order_date, total_amount) WHERE status = 'completed'` would dramatically reduce the scan; (3) `shared read=21450` means the working set for this query is 21,450 × 8 KB = 171 MB, which may exceed `shared_buffers` if it is set to the default 128 MB.

For Part B, the BRIN justification should mention: rows inserted in timestamp order, 500 million rows makes B-tree expensive to maintain, BRIN size is tiny (one entry per 128 pages) vs B-tree which would be hundreds of MB. GIN maintenance concern is valid — GIN uses a pending list that is merged in the background, and at 50M inserts/month, `gin_pending_list_limit` and autovacuum settings matter.
