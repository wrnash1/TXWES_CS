# Reading Guide: Module 07 - DynamoDB – NoSQL at Scale
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 07 - DynamoDB – NoSQL at Scale**! Amazon DynamoDB is AWS's fully managed NoSQL database service, designed for applications requiring single-digit millisecond performance at any scale — from a few requests per second to millions. This module covers DynamoDB's data model (partition keys, sort keys, items), its capacity mode options, Global Tables for multi-Region deployments, and DynamoDB Accelerator (DAX) for microsecond caching. DynamoDB is a key differentiator on the SAA-C03 exam for scenarios requiring extreme scale, flexible schemas, and serverless architecture.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **DynamoDB Partition Key (Primary Key)**: The mandatory attribute that uniquely identifies each item in a DynamoDB table and determines the physical partition where the item is stored. Choosing a high-cardinality partition key (one with many distinct values, such as a user ID or order ID) distributes data and throughput evenly across partitions. A poorly chosen partition key that results in many requests targeting the same value creates a "hot partition" bottleneck — a common exam anti-pattern.

*   **DynamoDB Sort Key (Composite Key)**: An optional second attribute that, combined with the partition key, forms a composite primary key. Multiple items can share the same partition key if they have different sort keys, enabling efficient range queries (e.g., "all orders for user X placed after date Y"). Sort key queries use conditions like `begins_with`, `between`, `=`, `<`, and `>`.

*   **DynamoDB Capacity Modes**: On-Demand mode automatically scales read and write capacity to match traffic with no capacity planning required — billed per request. Provisioned mode requires specifying Read Capacity Units (RCUs) and Write Capacity Units (WCUs) in advance, with optional Auto Scaling; it is more cost-effective for predictable, steady-state workloads. One RCU supports one strongly consistent read (or two eventually consistent reads) of up to 4 KB per second. One WCU supports one write of up to 1 KB per second.

*   **DynamoDB Global Tables**: A multi-Region, multi-active replication feature that automatically replicates a DynamoDB table across selected AWS Regions. All replicas are writable (active-active), providing low-latency local access for globally distributed applications and built-in disaster recovery with sub-second RPO. Conflict resolution uses "last writer wins" based on timestamps.

*   **DynamoDB Accelerator (DAX)**: A fully managed, in-memory cache for DynamoDB that delivers microsecond read latency (compared to DynamoDB's single-digit millisecond baseline). DAX is a write-through cache — writes go to DynamoDB first, then to the cache. It is designed for read-heavy DynamoDB workloads that can tolerate eventually consistent data. DAX does not cache writes or strongly consistent reads.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** DynamoDB appears in Design High-Performing Architectures (24%) and Design Resilient Architectures (26%). Expect scenario-based questions on when to use DynamoDB vs. RDS, and on key design choices.

*   **DynamoDB vs. RDS Selection Trap:** DynamoDB is the correct answer for: massive scale (millions of requests/second), unpredictable or highly variable traffic (use On-Demand mode), flexible schema (different items can have different attributes), key-value or document access patterns, and serverless architectures. RDS is correct for: complex SQL queries, JOIN operations, ACID transactions across multiple tables, and structured relational data.

*   **Hot Partition Anti-Pattern:** The exam will present a table with severe throughput throttling despite sufficient total capacity. The root cause is a poorly designed partition key (e.g., using a Boolean "isActive" field as the key, concentrating all traffic on two values). The solution is always to choose a higher-cardinality partition key or add a random suffix to distribute load.

*   **DAX vs. ElastiCache:** DAX is purpose-built for DynamoDB and integrates natively. ElastiCache (Redis or Memcached) is a general-purpose caching layer that can cache DynamoDB responses alongside any other data source. The exam will specify "DynamoDB caching" → DAX. "Application-level caching across multiple backends" → ElastiCache.

*   **TTL (Time to Live):** DynamoDB TTL allows you to set an expiration timestamp attribute on items. DynamoDB deletes expired items automatically at no cost (within 48 hours of expiration). TTL is the right answer for session stores, temporary tokens, and audit logs that should auto-expire.

*   **Study Resource:** The DynamoDB Developer Guide provides comprehensive coverage of the data model and best practices: [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/). The "Best practices for designing and using partition keys effectively" section is exam-critical.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the DynamoDB chapter in the AWS Solutions Architect study materials. Review the [Amazon DynamoDB FAQs page](https://aws.amazon.com/dynamodb/faqs/) for concise coverage of capacity modes and Global Tables. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Amazon DynamoDB — Under the Hood" whitepaper for deep architectural context.

*   **Required Video:** Watch the DynamoDB module in the official course playlist, focusing on partition key design, capacity modes comparison, and the DAX caching architecture: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create a DynamoDB table and insert items with composite keys:** Use the AWS Console or CLI to create a table with a partition key (e.g., `userId`) and sort key (e.g., `orderDate`). Insert multiple items with the same partition key but different sort keys. Use the Query operation to retrieve all orders for a specific user.

*   **Compare On-Demand vs. Provisioned capacity modes:** Create one table in On-Demand mode and one in Provisioned mode with Auto Scaling. Use the AWS CLI to write 1,000 items to each and compare the CloudWatch consumed capacity metrics.

*   **Enable DynamoDB TTL and observe expiration:** Add a TTL attribute (Unix timestamp 5 minutes in the future) to several items using `aws dynamodb update-time-to-live`. Observe item deletion in the console after expiration.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Understand partition key design best practices at [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html).
- [ ] Compare DynamoDB capacity modes at [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html).
- [ ] Watch the DynamoDB video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab creating tables, querying with composite keys, and testing TTL.
- [ ] Proceed to the weekly quiz.
