# Reading Guide: Module 07 - DynamoDB: NoSQL at Scale

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

Amazon DynamoDB is a cornerstone service for serverless and high-scale application architectures on AWS. The SAA-C03 exam tests DynamoDB across multiple dimensions: data modeling (key design, indexes), capacity planning (provisioned vs. on-demand), event-driven integrations (Streams, Lambda), and multi-region architecture (Global Tables). This reading guide provides the reference tables, design patterns, and exam decision frameworks needed to answer DynamoDB scenario questions accurately.

---

## Section 1: DynamoDB Data Model

### 1.1 Core Concepts

| Concept | DynamoDB Term | Relational Equivalent |
|---|---|---|
| Collection of items | Table | Table |
| Single record | Item | Row |
| Named field in an item | Attribute | Column |
| Unique identifier (partition key only) | Simple primary key | Primary key |
| Unique identifier (partition + sort) | Composite primary key | Composite primary key |

DynamoDB is schema-less for non-key attributes. Two items in the same table can have completely different attribute sets, as long as each item has the required primary key attributes.

### 1.2 Primary Key Design Patterns

| Pattern | When to Use | Example |
|---|---|---|
| Partition key only | Each item accessed by a single, unique ID | UserId → User profile |
| Partition + Sort key | Items grouped by a parent entity with sorting | CustomerId + OrderDate → Order history |
| Hierarchical data | Partition = entity type, Sort = sub-entity | EntityType + EntityId → polymorphic table |

Good partition key design distributes writes evenly across partitions. A bad partition key (low cardinality, hot key) concentrates I/O on a single partition, causing throttling even if total provisioned capacity is sufficient.

### 1.3 Partition Key Best Practices

- High cardinality: many distinct values (UserId, OrderId) are better than low cardinality (Status: active/inactive)
- Avoid hot keys: if all reads hit the same partition key (e.g., Today's date), the partition becomes a bottleneck
- For time-series data: use a composite key where partition key is a high-cardinality entity ID and sort key is a timestamp

---

## Section 2: Secondary Indexes

### 2.1 LSI vs. GSI Comparison

| Feature | Local Secondary Index (LSI) | Global Secondary Index (GSI) |
|---|---|---|
| Partition key | Same as base table | Any attribute |
| Sort key | Different from base table | Any attribute (optional) |
| Creation timing | At table creation only | At table creation or any time after |
| Capacity sharing | Shares table's RCUs/WCUs | Separate RCUs/WCUs (provisioned) or on-demand |
| Consistency | Strongly consistent reads possible | Eventually consistent only |
| Maximum per table | 5 | 20 |
| Item collection size limit | 10 GB per partition key | No limit |
| Cross-partition queries | No (same partition as base) | Yes (global across all partitions) |

### 2.2 Index Design Examples

Base table: Orders

| Attribute | Type | Key Role |
|---|---|---|
| CustomerId | String | Partition key |
| OrderId | String | Sort key |
| OrderDate | String | Attribute |
| TotalAmount | Number | Attribute |
| ProductCategory | String | Attribute |

LSI — sort orders by TotalAmount within a customer's partition:

- Partition key: CustomerId (same)
- Sort key: TotalAmount (different sort key)
- Query: all orders for customer C001 with amount > 100

GSI — query orders by ProductCategory globally:

- Partition key: ProductCategory
- Sort key: OrderDate
- Query: all orders for category "Electronics" in the last 30 days, across all customers

---

## Section 3: Capacity Modes

### 3.1 Capacity Unit Reference

| Operation | Strongly Consistent | Eventually Consistent |
|---|---|---|
| Read (up to 4 KB) | 1 RCU | 0.5 RCU |
| Transactional Read | 2 RCUs | N/A |
| Write (up to 1 KB) | 1 WCU | N/A |
| Transactional Write | 2 WCUs | N/A |

For items larger than the base size, the cost scales proportionally. A strongly consistent read of a 12 KB item costs 3 RCUs (12/4 = 3).

### 3.2 Choosing Between Provisioned and On-Demand

| Scenario | Recommended Mode |
|---|---|
| Steady, predictable traffic patterns | Provisioned with Auto Scaling |
| New table with unknown traffic | On-demand |
| Highly variable or spiky traffic | On-demand or Provisioned + Aggressively-configured Auto Scaling |
| Cost-sensitive with predictable load | Provisioned (lower per-unit cost at scale) |
| Development and testing | On-demand (no idle capacity charges) |
| Infrequently accessed tables | On-demand |

### 3.3 Auto Scaling for Provisioned Mode

Auto Scaling adjusts RCUs and WCUs to maintain a target utilization percentage:

- Default target utilization: 70%
- Scaling responds to changes in consumed capacity metrics
- Scale-out is faster than scale-in to avoid throttling during sudden spikes
- Works with both read and write capacity independently
- Does not instantly handle sudden, large spikes — there is a short lag before new capacity is active

For workloads with known sudden spikes, consider: on-demand mode, or pre-scaling before the expected event using scheduled DynamoDB capacity updates via AWS Application Auto Scaling.

---

## Section 4: DynamoDB Streams

### 4.1 Stream View Types

| View Type | Contents |
|---|---|
| KEYS_ONLY | Only the key attributes of the modified item |
| NEW_IMAGE | The entire item as it appears after the modification |
| OLD_IMAGE | The entire item as it appeared before the modification |
| NEW_AND_OLD_IMAGES | Both the new and old images of the item |

For audit logging, use NEW_AND_OLD_IMAGES to capture before and after state. For downstream processing of new records, NEW_IMAGE is sufficient.

### 4.2 Stream Processing Architecture

```text
DynamoDB Table
    |
    | (item changes via Streams)
    v
DynamoDB Stream (24-hour retention)
    |
    | (event source mapping)
    v
AWS Lambda Function
    |
    | (process records)
    v
Target: Elasticsearch / SNS / S3 / Another DynamoDB table
```

Lambda processes stream records in batches. The Lambda function receives a batch of stream records, processes them, and acknowledges. If processing fails, the batch is retried. Failed batches can be sent to an SQS dead-letter queue for investigation.

---

## Section 5: DynamoDB Accelerator (DAX)

### 5.1 DAX Architecture

DAX is a cluster of nodes deployed within your VPC. Your application code replaces the DynamoDB SDK client with the DAX client (same API). Read requests are served from DAX's item cache or query cache. Writes go directly to DynamoDB and the DAX cache is invalidated.

| Feature | DynamoDB Direct | DynamoDB + DAX |
|---|---|---|
| Read latency | Single-digit milliseconds | Microseconds |
| Cost | RCU charges per read | DAX cluster hourly + reduced RCU charges |
| Consistency | Strongly or eventually consistent | Eventually consistent only |
| Write performance | Unchanged | Unchanged (writes go to DynamoDB) |

### 5.2 When to Use DAX vs. ElastiCache

| Factor | DAX | ElastiCache (Redis/Memcached) |
|---|---|---|
| API compatibility | DynamoDB-native | Generic cache (requires application logic) |
| Data source | DynamoDB only | Any data source |
| Cache invalidation | Automatic on write | Manual or TTL-based |
| Use case | Accelerate DynamoDB reads | General application caching, session storage |
| Best for | Read-heavy DynamoDB tables with repeated item access | Application session state, computed results, multi-source caching |

---

## Section 6: Global Tables

### 6.1 Global Tables Architecture

DynamoDB Global Tables create a multi-region active-active database. All replica tables share the same table name and schema. Writes to any replica are replicated to all other replicas using DynamoDB Streams internally.

Conflict resolution: last-writer-wins based on timestamp. For applications where concurrent writes to the same item from different Regions could occur, implement application-level conflict resolution if business rules require it.

Requirements for Global Tables:

- DynamoDB Streams must be enabled on the table
- On-demand capacity mode or provisioned mode with Auto Scaling enabled
- All replica tables must have the same table structure

### 6.2 Global Tables vs. Cross-Region Read Replicas (RDS)

| Feature | DynamoDB Global Tables | RDS Cross-Region Read Replica |
|---|---|---|
| Write capability | Active-active (all Regions accept writes) | Active-passive (only primary accepts writes) |
| Replication | DynamoDB Streams (sub-second) | Asynchronous binary log replication |
| Failover | Application changes endpoint | Manual promotion required |
| Data model | Key-value/document (DynamoDB) | Relational (SQL) |

---

## Section 7: DynamoDB vs. RDS Decision Framework

| Requirement | DynamoDB | RDS / Aurora |
|---|---|---|
| Millions of requests per second | Yes | Difficult at this scale |
| Single-digit millisecond latency at scale | Yes | Challenging without caching |
| Multi-table JOIN queries | No | Yes |
| Complex ACID transactions across tables | Limited (single-table) | Yes (full SQL transactions) |
| Schema flexibility (varied attributes) | Yes | No (fixed schema) |
| SQL query language | No | Yes |
| Known, simple access patterns | Yes | Works but over-engineered |
| Ad-hoc analytical queries | Not well-suited | Better (with read replicas for reporting) |
| Serverless/pay-per-request model | Yes | No (Aurora Serverless approximates this) |

---

## Section 8: SAA-C03 Exam Tips for Module 07

**Exam Tip 1 — GSI for non-key attribute queries:**
If a scenario requires querying a DynamoDB table by an attribute that is not the partition key, the answer is always a Global Secondary Index. LSIs can only be created at table creation, so if the table already exists and needs a new query pattern, it must be a GSI.

**Exam Tip 2 — DynamoDB Streams for Lambda triggers:**
When a scenario asks how to automatically process DynamoDB writes (trigger processing when an item is created or updated), the answer involves DynamoDB Streams as the event source for a Lambda function.

**Exam Tip 3 — On-demand for unknown traffic:**
For new tables or unpredictable workloads, on-demand capacity mode eliminates the risk of throttling from under-provisioning. Provisioned is more cost-efficient when traffic patterns are well understood.

**Exam Tip 4 — DAX only helps with reads:**
DAX accelerates DynamoDB reads. It does not improve write performance. If a scenario mentions write-heavy workloads, DAX is not the answer.

**Exam Tip 5 — Global Tables for multi-region active-active:**
If a scenario requires writing data in multiple Regions simultaneously with automatic replication (not just reading), DynamoDB Global Tables is the answer. RDS cross-region Read Replicas are active-passive (only one Region accepts writes).

**Exam Tip 6 — Hot partition key design:**
A partition key with low cardinality (Status: active/inactive) concentrates I/O on one or two partitions. At scale, this causes throttling even with sufficient total capacity. Design partition keys with high cardinality.

**Exam Tip 7 — Strongly consistent reads cost more:**
A strongly consistent read costs twice as many RCUs as an eventually consistent read for the same item size. Use eventually consistent reads when slight staleness is acceptable to reduce read costs.

**Exam Tip 8 — TTL for automatic item expiration:**
DynamoDB Time to Live (TTL) automatically deletes items after a specified timestamp attribute value. This is used for session data, temporary records, and expiring cache entries without requiring application-side deletion logic. TTL deletions are not counted against WCU capacity.

---

## Section 9: Key CLI Commands for Module 07

Describe a DynamoDB table:

```bash
aws dynamodb describe-table \
  --table-name MyTable \
  --query "Table.{Name:TableName,Status:TableStatus,Keys:KeySchema,Capacity:ProvisionedThroughput}"
```

List all DynamoDB tables:

```bash
aws dynamodb list-tables --output table
```

Get an item by primary key:

```bash
aws dynamodb get-item \
  --table-name Users \
  --key '{"UserId": {"S": "user001"}}'
```

Query items with a partition key:

```bash
aws dynamodb query \
  --table-name Orders \
  --key-condition-expression "CustomerId = :cid" \
  --expression-attribute-values '{":cid": {"S": "C001"}}'
```

---

## Section 10: Study Checklist

- [ ] Explain the difference between a simple primary key and a composite primary key with an example of each
- [ ] Describe when to use an LSI vs. a GSI — include the creation timing difference
- [ ] Explain why a low-cardinality partition key causes performance problems at scale
- [ ] Compare provisioned and on-demand capacity modes on cost model and use case
- [ ] Describe DynamoDB Streams view types and give a use case for NEW_AND_OLD_IMAGES
- [ ] Explain when to use DAX and what type of reads it cannot accelerate
- [ ] Describe how DynamoDB Global Tables resolve write conflicts
- [ ] Identify three scenarios where DynamoDB is the better choice over RDS and three where RDS is better
- [ ] Run the CLI commands in Section 9 and record the output
- [ ] Complete the Module 07 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 07 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: aws.amazon.com/certification
