# Video Script: Module 07 - DynamoDB: NoSQL at Scale

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 07: DynamoDB — NoSQL at Scale.

Amazon DynamoDB is AWS's fully managed, serverless, key-value and document NoSQL database. It is one of the most frequently tested services on the SAA-C03 exam because it has unique performance characteristics, capacity modes, and access patterns that require deliberate design decisions.

By the end of this module you will be able to:

- Explain DynamoDB's data model including partition keys, sort keys, and the concept of items and attributes
- Choose between provisioned and on-demand capacity modes
- Configure Global Secondary Indexes and Local Secondary Indexes for query flexibility
- Explain DynamoDB Streams and their use in event-driven architectures
- Describe DynamoDB Global Tables for multi-region active-active replication
- Apply DynamoDB Accelerator for read caching
- Identify when DynamoDB is the right choice versus a relational database

---

## [01:30 - 06:30] DynamoDB Data Model

[SHOW DIAGRAM]

DynamoDB stores data as items (analogous to rows) in tables. Each item consists of attributes (analogous to columns), but unlike relational databases, DynamoDB items in the same table do not need to have the same attributes — it is schema-less except for the primary key.

The primary key can be one of two forms:

- **Partition key only (simple primary key):** Each item is uniquely identified by its partition key value. DynamoDB uses the partition key to distribute items across storage partitions. All reads and writes for a specific partition key go to the same partition. Example: a Users table where UserId is the partition key.

- **Partition key + Sort key (composite primary key):** Items are uniquely identified by the combination of partition key and sort key. All items with the same partition key are stored together (in the same partition) and sorted by the sort key. This enables powerful range queries on the sort key within a partition. Example: an Orders table where CustomerId is the partition key and OrderDate is the sort key — you can query all orders for a customer and optionally filter by date range.

[SHOW DIAGRAM]

DynamoDB attribute types:

- Scalar types: String (S), Number (N), Binary (B), Boolean (BOOL), Null
- Document types: Map (M — a JSON object), List (L — an ordered list)
- Set types: String Set (SS), Number Set (NS), Binary Set (BS)

Items are retrieved by partition key (full table scan without a key is inefficient). The key design principle: design your access patterns first, then design your table schema to support those access patterns directly. This is the opposite of relational database design where you normalize first.

---

## [06:30 - 11:00] Capacity Modes and Throughput

[SHOW DIAGRAM]

DynamoDB has two capacity modes that control how you provision and pay for throughput.

**Provisioned Capacity Mode** — you specify the number of Read Capacity Units (RCUs) and Write Capacity Units (WCUs) per second. One RCU provides one strongly consistent read per second (or two eventually consistent reads) for items up to 4 KB. One WCU provides one write per second for items up to 1 KB. Charges are based on the provisioned capacity, not actual usage. Use provisioned mode for predictable, steady-state traffic. Combine with Auto Scaling to automatically adjust capacity based on traffic patterns.

**On-Demand Capacity Mode** — DynamoDB automatically scales to handle any level of traffic. You pay per request (per million read request units and per million write request units). No capacity planning required. Use on-demand mode for unpredictable traffic, new tables where usage is unknown, or infrequently accessed tables.

Capacity mode comparison:

| Feature | Provisioned | On-Demand |
|---|---|---|
| Capacity management | You set RCUs/WCUs | Automatic |
| Cost model | Pay for provisioned capacity | Pay per request |
| Cost efficiency | More efficient at steady load | More efficient at low or unpredictable load |
| Scaling | Manual or Auto Scaling | Instantaneous |
| Throttling | Possible if traffic exceeds provisioned | No throttling (up to account limits) |

**DynamoDB Auto Scaling** works with provisioned mode to automatically adjust RCUs and WCUs based on a target utilization. You set a minimum and maximum capacity and a target utilization (default 70%). When utilization exceeds the target, DynamoDB adds capacity; when it drops, capacity is reduced.

**Read Consistency:** DynamoDB supports two read consistency models:

- Eventually consistent reads: may return stale data up to seconds old; costs 0.5 RCUs per 4 KB
- Strongly consistent reads: always returns the most recent data; costs 1 RCU per 4 KB

For most application reads (product catalog, user profile), eventual consistency is acceptable. For reads that must reflect a recent write (payment confirmation, inventory check), use strongly consistent reads.

---

## [11:00 - 15:30] Secondary Indexes

[SHOW DIAGRAM]

DynamoDB tables can only be queried efficiently using the primary key. Secondary indexes allow you to query on non-key attributes. There are two types.

**Local Secondary Index (LSI):**

- Shares the same partition key as the base table but has a different sort key
- Must be created at table creation time — cannot be added later
- Gives an alternate sort key for querying within a partition
- Shares RCU/WCU capacity with the base table
- Up to 5 LSIs per table

Example: an Orders table with partition key CustomerId and sort key OrderDate. An LSI with sort key TotalAmount lets you query all orders for a customer sorted by amount. You still provide the partition key — the LSI just changes the sort dimension.

**Global Secondary Index (GSI):**

- Can have any attribute as partition key and/or sort key — different from the base table primary key
- Can be added to an existing table (unlike LSI)
- Has its own provisioned RCU/WCU (or shares on-demand mode)
- Replicates a subset or all attributes from the base table
- Up to 20 GSIs per table

Example: the same Orders table. A GSI with partition key ProductId and sort key OrderDate lets you query all orders containing a specific product regardless of which customer placed them — a query pattern impossible with the base table key.

For the SAA-C03 exam: if a scenario requires querying a DynamoDB table by an attribute that is not the primary key, the answer is a GSI. If the scenario specifically mentions querying within a partition by a different sort key, it is an LSI. If the scenario involves adding a new query capability to an existing table, it must be a GSI (LSIs cannot be added to existing tables).

---

## [15:30 - 19:30] DynamoDB Streams, DAX, and Global Tables

**DynamoDB Streams** capture a time-ordered sequence of item-level modifications (inserts, updates, deletes) in a DynamoDB table. Each record in the stream contains the before and/or after image of the modified item. Stream records are available for 24 hours.

[SHOW DIAGRAM]

Stream use cases:

- Trigger a Lambda function when an item is written (event-driven architecture)
- Replicate changes to another DynamoDB table, Elasticsearch, or analytics store
- Implement audit logging of all data changes
- Build a cross-region replication pipeline (or use Global Tables which do this automatically)

For the SAA-C03 exam: if a scenario asks how to trigger a Lambda function when a DynamoDB item is created or updated, the answer is DynamoDB Streams with a Lambda trigger.

**DynamoDB Accelerator (DAX)** is a fully managed in-memory cache for DynamoDB. DAX is DynamoDB-compatible — your application uses the same API calls, but DAX intercepts read requests and serves them from cache if the item is cached. Read latency drops from single-digit milliseconds to microseconds.

DAX use cases: read-heavy applications where the same items are read frequently (product details, configuration data, leaderboards). DAX does not help with write-heavy workloads or infrequently accessed items.

DAX is not appropriate when: strongly consistent reads are required (DAX provides eventually consistent reads only), or for write-heavy workloads.

**DynamoDB Global Tables** provide multi-region, active-active replication. You designate multiple Regions as replica Regions. DynamoDB automatically replicates all writes to all replica tables using DynamoDB Streams. Each Region can accept read and write traffic. Conflict resolution uses last-writer-wins based on timestamp.

Global Tables use cases:

- Globally distributed applications where users in different Regions write data (user profile updates, session data)
- Multi-region active-active disaster recovery
- Low-latency access for a global user base

---

## [19:30 - 22:00] When to Use DynamoDB vs. RDS

This is a critical exam decision. DynamoDB and RDS solve different problems.

[SHOW DIAGRAM]

Use DynamoDB when:

- Access patterns are simple and known (key-value or simple range queries)
- Scale is massive (millions of requests per second, petabytes of data)
- Low predictable latency is required at scale (single-digit milliseconds)
- Data model is flexible or document-oriented
- Serverless, pay-per-request pricing fits the workload
- You need multi-region active-active without complex replication management

Use RDS or Aurora when:

- Complex queries with JOIN operations across multiple tables are required
- Strong ACID transactions across multiple tables are needed
- The data has complex relational structure with referential integrity
- The team has deep SQL expertise and the workload is query-heavy
- Ad-hoc analytical queries are needed

The exam trap: if a scenario mentions "complex multi-table JOIN queries," "referential integrity," or "ACID transactions across multiple tables," the answer is relational (RDS/Aurora), not DynamoDB. If the scenario mentions "single-digit millisecond latency at millions of requests per second," DynamoDB is the answer.

---

## [22:00 - 24:00] Module Summary

DynamoDB is a fully managed, serverless NoSQL database. Primary key design — partition key or partition key plus sort key — determines access patterns. Secondary indexes (LSI for alternate sort key within partition; GSI for any attribute) enable additional query patterns.

Capacity modes: provisioned for predictable load with Auto Scaling; on-demand for unpredictable or low-volume load. Strongly consistent reads cost twice as many RCUs as eventually consistent.

DynamoDB Streams enable event-driven Lambda triggers. DAX provides microsecond read caching. Global Tables provide multi-region active-active replication.

Choose DynamoDB for: high-scale key-value access, low-latency requirements, serverless architectures. Choose RDS/Aurora for: complex SQL, joins, ACID across tables, relational integrity.

For your certification study: aws.amazon.com/certification.

---

End of Module 07 Video Script
