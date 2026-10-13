# Discussion Forum: Module 12 — BigQuery for Analytics

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

This discussion asks you to connect BigQuery's design principles to real organizational
decision-making. Analytics infrastructure decisions have significant cost, performance,
and governance implications. Good database administrators must reason about tradeoffs,
not just technical mechanics.

**Due date**: See course schedule in Canvas.

**Grading**: See rubric at the bottom of this prompt.

---

## Primary Post Prompt

BigQuery's architecture makes several deliberate design choices that differ from
traditional relational databases: no traditional indexes, a billing model based on
bytes scanned rather than compute time, and a separation between storage and compute
that allows both to scale independently.

Choose **one** of the following scenarios and write a substantive primary post
(minimum 250 words) addressing the questions provided.

---

### Scenario A — The Cost Surprise

A mid-size retail company recently migrated their data warehouse to BigQuery. Three
months later, the finance team escalates a concern: the monthly BigQuery bill is
$40,000 — nearly triple the projected $14,000. The data team investigates and
discovers that five analysts are running large `SELECT *` queries against a 20 TB
customer behavior table without any date filters, multiple times per day.

Address the following in your post:

1. Explain technically why `SELECT *` queries without partition filters are so
   expensive in BigQuery. Use the columnar storage and Dremel concepts from the
   module in your explanation.

2. Propose at least three specific technical controls you would implement to
   prevent this from happening again. For each control, explain what it does
   and what its limitations are.

3. The analysts argue that their queries are necessary for exploratory data
   analysis and that adding restrictions will slow their work. How would you
   balance the need for cost governance with analyst productivity? What
   organizational or tooling changes would support both goals?

---

### Scenario B — The Architecture Decision

Your company is building a new customer analytics platform. The data engineering
lead proposes using a single, massive denormalized BigQuery table for all analytics —
one table with 200 columns, including nested ARRAY fields for events. A senior
database architect argues for a normalized star schema with a fact table and 15
dimension tables, similar to what they used with the company's previous on-premises
Redshift warehouse.

Address the following in your post:

1. Evaluate both approaches (denormalized wide table vs. normalized star schema)
   in the context of BigQuery's columnar architecture. Which approach aligns
   better with how BigQuery physically stores and accesses data?

2. The company expects the table to grow to 500 billion rows over 5 years.
   Describe how you would design partitioning and clustering for the primary
   fact table, and explain your choices.

3. What are the operational tradeoffs of the two approaches for the data
   engineering team (schema evolution, ETL complexity, query maintenance)?
   Is there a hybrid approach that captures benefits of both?

---

### Scenario C — The Migration Decision

A government agency currently runs a Teradata data warehouse on-premises, processing
approximately 300 TB of historical data with 50 analysts running complex multi-table
queries. The CTO wants to evaluate migrating to BigQuery. The compliance team flags
a concern: the agency handles data subject to FedRAMP High authorization requirements,
and data must not leave US-based infrastructure.

Address the following in your post:

1. Is BigQuery a viable platform for FedRAMP High workloads? What specific
   BigQuery configuration options address data residency and compliance requirements?

2. Teradata uses a row-based architecture with primary index distributions for
   query optimization. How would you re-architect the key tables for BigQuery,
   and what optimization strategy replaces the Teradata primary index?

3. The agency has 300 TB of historical data and cannot afford more than 4 hours of
   downtime. Outline a high-level migration approach that meets this constraint,
   including what tools you would use and what risks you would need to mitigate.

---

## Response Posts

After submitting your primary post, reply to **two classmates** who chose different
scenarios than you. Each reply must be at least 100 words and do one of the following:

- Add a technical consideration or alternative the original poster did not address
- Respectfully challenge an assumption or recommendation with a specific counter-argument
- Connect the scenario to a related concept from Modules 10–12 (Cloud SQL, Spanner,
  or BigQuery)

Responses that simply agree or say "great post" without substantive content will
receive no credit.

---

## Grading Rubric

| Criteria | Points |
|---|---|
| Primary post meets 250-word minimum | 10 |
| Correct and specific use of BigQuery technical concepts | 30 |
| Addresses all three sub-questions for chosen scenario | 30 |
| Critical thinking — tradeoffs acknowledged, not just positives | 15 |
| Two substantive peer responses (100+ words each) | 15 |
| **Total** | **100** |

---

## Technical Vocabulary Checklist

Strong posts will naturally incorporate relevant terms. Do not force them, but use
them correctly when applicable:

- Dremel / multi-level serving tree
- Columnar storage / Capacitor
- Partition pruning / clustering
- Bytes scanned / on-demand vs. flat-rate
- Materialized view / query rewriting
- Authorized view
- Slot reservation
- INFORMATION_SCHEMA.JOBS_BY_PROJECT
- require_partition_filter
- Time travel / table clone / snapshot

---

Module 12 Discussion — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
