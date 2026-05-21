# Quiz: Module 07 - DynamoDB – NoSQL at Scale
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A social media platform stores user activity events in DynamoDB. The table is being heavily throttled despite having sufficient total provisioned capacity. Investigation reveals that 80% of all requests target items associated with the top 5 most-followed celebrity accounts. What is the root cause and the recommended fix?
*   A) The table's total provisioned WCU is too low; increase provisioned capacity to 10x the current value.
*   B) The partition key is a low-cardinality attribute (e.g., celebrity account ID), creating hot partitions. Redesign the key using a higher-cardinality attribute or add a random suffix to distribute traffic.
*   C) DynamoDB does not support high write volumes; migrate to RDS Aurora for write-heavy workloads.
*   D) Enable DynamoDB Streams to fan out the writes across multiple tables and reduce per-table throughput.
*   **Correct Answer:** B) The hot partition problem occurs when a low-cardinality or skewed partition key concentrates traffic on a small number of physical partitions, exhausting their local throughput even when the total table capacity appears sufficient.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Increasing total provisioned capacity does not solve hot partition throttling. DynamoDB distributes capacity across partitions; if most traffic hits the same few partitions, adding global capacity to under-loaded partitions does not relieve the hot ones.
    *   *Why B is correct:* Hot partitions are the classic DynamoDB design flaw for the SAA-C03 exam. When a small number of partition key values receive disproportionate traffic, those partitions exhaust their local RCU/WCU allocation. Solutions include choosing a high-cardinality key, adding a random suffix (write sharding), or using a composite key that distributes requests across more partitions.
    *   *Why C is incorrect:* DynamoDB is designed for massive write throughput. The problem is the key design, not the service's capability. Migrating to Aurora would add SQL complexity and likely perform worse at this scale with these access patterns.
    *   *Why D is incorrect:* DynamoDB Streams capture a change log of table modifications for event-driven processing (e.g., triggering Lambda). Streams do not distribute write load across multiple tables or relieve hot partition throttling.

---

**Question 2**
Which of the following is the most accurate description of **DynamoDB Global Tables**?
*   A) A DynamoDB feature that creates read-only replicas in additional Regions, with all writes directed to a single primary Region.
*   B) A managed multi-Region, multi-active replication feature that makes a DynamoDB table writable in every configured Region, providing low-latency local reads and writes globally with automatic conflict resolution.
*   C) A cross-account DynamoDB backup feature that replicates table snapshots to a secondary AWS account for disaster recovery.
*   D) A feature that partitions a single DynamoDB table across multiple AZs within one Region to improve single-Region throughput.
*   **Correct Answer:** B) DynamoDB Global Tables provide multi-Region, multi-active (active-active) replication where every Region hosts a fully writable replica, enabling global low-latency access and built-in disaster recovery.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Global Tables are multi-active — all Region replicas accept writes simultaneously. There is no single "primary Region" concept. This description incorrectly describes a read-only replica pattern.
    *   *Why B is correct:* Global Tables is the SAA-C03 answer for "globally distributed application with low-latency reads AND writes, with automatic regional failover." The active-active model means any Region failure does not require a manual failover because all other Regions continue operating independently.
    *   *Why C is incorrect:* This describes a cross-account backup scenario, which is not what Global Tables does. Global Tables is live replication for active traffic, not backup/restore.
    *   *Why D is incorrect:* DynamoDB automatically spans storage across multiple AZs within a Region by default — this is a baseline durability feature, not Global Tables. Global Tables is specifically about extending the table to multiple Regions.

---

**Question 3**
A gaming application reads DynamoDB item data millions of times per second to serve real-time game state lookups. The current DynamoDB response latency of 5 milliseconds is too slow for the sub-millisecond requirement. Which solution reduces read latency to microseconds with the least code change?
*   A) Enable DynamoDB Read Replicas in the same Region for parallel read processing.
*   B) Migrate the game state data to Amazon ElastiCache for Redis and point the application to the Redis endpoint.
*   C) Deploy DynamoDB Accelerator (DAX) in front of the DynamoDB table; DAX is API-compatible with DynamoDB and requires minimal code changes.
*   D) Enable DynamoDB Streams and pre-compute game state in Lambda functions, storing results in S3.
*   **Correct Answer:** C) DAX is an in-memory, DynamoDB-API-compatible cache that reduces read latency from milliseconds to microseconds, with the application needing only to change the endpoint URL from DynamoDB to the DAX cluster.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DynamoDB does not have a concept of "Read Replicas" in the same way RDS does. Globally, DynamoDB achieves read scaling via Global Tables (multi-Region) or DAX (caching). There is no same-Region read replica to enable.
    *   *Why B is incorrect:* ElastiCache for Redis is a valid caching solution, but it requires building a separate cache population and invalidation layer — significant code change. DAX is API-compatible with DynamoDB and requires only changing the client endpoint, making it the "least code change" answer.
    *   *Why C is correct:* DAX is designed precisely for this scenario: existing DynamoDB workloads needing sub-millisecond latency. The DAX client uses the same API as the DynamoDB SDK. The application replaces the DynamoDB endpoint with the DAX cluster endpoint — typically a one-line configuration change.
    *   *Why D is incorrect:* Pre-computing results with Lambda and storing in S3 introduces significant architectural complexity, eventual consistency delays, and S3 latency (which is not sub-millisecond). This does not solve the real-time latency requirement.

---

**Question 4**
A serverless application has highly unpredictable DynamoDB traffic — sometimes zero requests for hours, then thousands of requests per second during promotional events. Which DynamoDB capacity mode is most cost-effective for this pattern?
*   A) Provisioned capacity with Auto Scaling configured to scale between 1 and 10,000 WCU.
*   B) DynamoDB On-Demand capacity mode, which automatically handles any request volume and bills per request with no minimum charge.
*   C) Provisioned capacity without Auto Scaling, set at the maximum expected peak load of 10,000 WCU.
*   D) Provisioned capacity with reserved capacity purchased for 3 years to minimize the per-WCU cost.
*   **Correct Answer:** B) On-Demand mode eliminates the cost of idle provisioned capacity, billing only per actual request — perfect for zero-to-peak unpredictable traffic.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Provisioned capacity with Auto Scaling has a minimum capacity charge even when the table is idle. Auto Scaling also has scale-up lag — it adjusts based on CloudWatch metrics over a period of time, which may not respond fast enough to sudden traffic spikes.
    *   *Why B is correct:* On-Demand mode is the SAA-C03 answer for unpredictable or spiky workloads. You pay per read/write request unit consumed, with no minimum or idle charges. The table handles any traffic volume instantly without capacity planning.
    *   *Why C is incorrect:* Provisioning at peak (10,000 WCU) and leaving it static means paying for all that capacity during the hours of zero activity — the highest possible cost for this traffic pattern.
    *   *Why D is incorrect:* Reserved capacity for 3 years offers the lowest per-unit cost but requires a minimum hourly commitment. For a workload with hours of zero traffic, reserved capacity means paying for unused capacity constantly — the worst cost outcome for this scenario.

---

**Question 5**
A user session management service stores session tokens in DynamoDB. Sessions should automatically expire and be deleted 24 hours after creation to prevent the table from growing indefinitely. Which DynamoDB feature handles this automatically at no additional cost?
*   A) DynamoDB Streams — configure a Lambda function triggered by stream events to delete items older than 24 hours.
*   B) DynamoDB TTL (Time to Live) — set a TTL attribute on each item with a Unix timestamp 24 hours in the future; DynamoDB automatically deletes expired items.
*   C) S3 Lifecycle policies — export DynamoDB data to S3 nightly and use S3 expiration rules to delete old sessions.
*   D) AWS Config rules — create a rule that identifies DynamoDB items older than 24 hours and triggers an auto-remediation Lambda to delete them.
*   **Correct Answer:** B) DynamoDB TTL is a native feature that automatically deletes items whose TTL attribute timestamp has passed, at no additional charge, making it the correct tool for session expiration.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using DynamoDB Streams with Lambda to delete old items is a valid pattern but adds operational complexity, Lambda invocation costs, and the need to manage the deletion logic. TTL achieves the same result natively with zero code and at no cost.
    *   *Why B is correct:* TTL is designed exactly for this use case. You set a numeric attribute (e.g., `expiresAt`) on each item containing the Unix epoch expiration timestamp. DynamoDB scans for and deletes expired items in the background within approximately 48 hours of expiration, at no charge. TTL is the canonical answer for session stores, temporary tokens, and auto-expiring records.
    *   *Why C is incorrect:* Exporting DynamoDB to S3 nightly adds significant operational complexity and latency — sessions are not deleted for up to 24 hours plus the export interval. S3 Lifecycle policies apply to S3 objects, not DynamoDB items.
    *   *Why D is incorrect:* AWS Config evaluates resource configuration compliance and can trigger remediations, but it is not designed for application-level data lifecycle management within DynamoDB tables. Config rules operate on AWS resource configurations (e.g., "is this S3 bucket public?"), not individual DynamoDB item attributes.

