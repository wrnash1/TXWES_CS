# Quiz: Module 12 - Cloud Analytics – AWS Athena, Google BigQuery
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A company stores 5 TB of web server log files as compressed CSV files in Amazon S3. An analytics team wants to query these files using standard SQL without provisioning, configuring, or managing any database servers. Which AWS service best meets this requirement?
*   A) Amazon RDS — a managed relational database service that requires provisioning an instance size and storage volume before use.
*   B) Amazon Redshift — a provisioned columnar data warehouse cluster that requires selecting node types and cluster configuration before queries can run.
*   C) AWS Athena — a serverless interactive query service that runs SQL directly against files in S3 without any infrastructure to provision or manage.
*   D) Amazon DynamoDB — a serverless NoSQL key-value and document database optimized for high-speed single-item lookups.
*   **Correct Answer:** C) AWS Athena — a serverless interactive query service that runs SQL directly against files in S3 without any infrastructure to provision or manage.
*   **Distractor Analysis:**
    *   *Why correct:* Athena is serverless — it requires no cluster provisioning. Analysts define a schema on top of existing S3 files and immediately run SQL queries, paying only for the data scanned per query.
    *   A) RDS requires provisioning an instance type and storage before use — it is not serverless. B) Redshift requires selecting cluster node types and is a provisioned service, not serverless. D) DynamoDB is a NoSQL key-value store optimized for single-item lookups, not for SQL analytics over multi-terabyte log files.

---

**Question 2**
In cloud analytics, which of the following most accurately defines the **shared responsibility model**?
*   A) A billing arrangement in which cloud costs are divided proportionally between the provider and the customer based on the percentage of infrastructure each party manages.
*   B) A security framework in which the cloud provider is responsible for security of the cloud infrastructure (physical hardware, hypervisors, and the global network), while the customer is responsible for security in the cloud (data, access controls, encryption, and application configuration).
*   C) A high-availability design pattern in which workloads are distributed across multiple cloud regions so that one region's failure does not affect service availability.
*   D) A compliance requirement mandating that all personally identifiable information processed in the cloud be encrypted with customer-managed encryption keys.
*   **Correct Answer:** B) A security framework in which the cloud provider is responsible for security of the cloud infrastructure (physical hardware, hypervisors, and the global network), while the customer is responsible for security in the cloud (data, access controls, encryption, and application configuration).
*   **Distractor Analysis:**
    *   *Why B is correct:* The shared responsibility model defines the security boundary between provider and customer. The provider owns the physical layer; the customer owns everything they configure on top of it — including access policies, encryption settings, and data classification. Misconfigured permissions are always the customer's responsibility.
    *   *Why A is incorrect:* The shared responsibility model is about security accountability, not billing division. Cloud billing is typically pay-per-use and is not shared 50/50.
    *   *Why C is incorrect:* Distributing workloads across regions describes a multi-region high-availability architecture, not the shared responsibility model.
    *   *Why D is incorrect:* Mandating customer-managed encryption keys describes a specific compliance control, not the broader shared responsibility model that covers all aspects of cloud security.

---

**Question 3**
An analyst runs a query in Google BigQuery against a 2 TB table: `SELECT customer_id, SUM(revenue) FROM transactions GROUP BY customer_id`. The table has 40 columns. BigQuery uses columnar storage. Which statement best explains why this query performs efficiently despite the large table size?
*   A) BigQuery scans all 40 columns in parallel across multiple nodes, which is faster than a sequential single-node scan.
*   B) BigQuery reads only the two columns referenced in the query (customer_id and revenue), avoiding I/O on the other 38 columns thanks to columnar storage.
*   C) BigQuery caches the full 2 TB table in memory on the first query, so subsequent queries are fast.
*   D) BigQuery compresses each row individually, reducing the effective table size from 2 TB to a smaller in-memory footprint.
*   **Correct Answer:** B) BigQuery reads only the two columns referenced in the query (customer_id and revenue), avoiding I/O on the other 38 columns thanks to columnar storage.
*   **Distractor Analysis:**
    *   *Why B is correct:* Columnar storage organizes each column contiguously on disk. A query that references only 2 of 40 columns reads approximately 5% of the total data instead of the full table. This I/O reduction is the primary performance advantage of columnar formats for analytical queries.
    *   *Why A is incorrect:* Parallel processing across nodes is a feature of BigQuery's distributed architecture, but it applies regardless of storage format. The specific efficiency gain described in the scenario comes from columnar I/O reduction, not parallelism alone.
    *   *Why C is incorrect:* BigQuery does not cache full 2 TB tables in memory for all users. Its performance advantage for this query type comes from columnar storage reducing I/O, not from memory caching.
    *   *Why D is incorrect:* BigQuery does compress data, but compression is row-agnostic. The key efficiency described — reading only referenced columns — is a property of columnar layout, not row-level compression.

---

**Question 4**
A company's data engineering team uses AWS to run analytics. A developer accidentally configures an S3 bucket containing customer PII as publicly accessible on the internet. A third party downloads 50,000 customer records. Who bears primary responsibility for this breach under the AWS shared responsibility model?
*   A) AWS, because they provide the S3 service and should prevent misconfiguration by default.
*   B) The customer, because configuring access controls, bucket policies, and public access settings is the customer's responsibility under the shared responsibility model.
*   C) Both equally, because AWS owns the physical infrastructure but the customer pays for the service.
*   D) Neither party — publicly accessible cloud storage is a known risk and users accept this when agreeing to the terms of service.
*   **Correct Answer:** B) The customer, because configuring access controls, bucket policies, and public access settings is the customer's responsibility under the shared responsibility model.
*   **Distractor Analysis:**
    *   *Why B is correct:* Under the AWS shared responsibility model, AWS secures the physical infrastructure and the S3 service itself. The customer is responsible for configuring who can access their data — bucket policies, IAM permissions, and public access block settings. A misconfigured public bucket is a customer configuration error, not an AWS infrastructure failure.
    *   *Why A is incorrect:* AWS does provide tools to prevent public access (S3 Block Public Access settings), but the customer must enable them. AWS cannot unilaterally restrict customer bucket configurations without removing the customer's ability to use public hosting features they may legitimately need.
    *   *Why C is incorrect:* Responsibility is not split 50/50. The physical infrastructure is AWS's domain; data access configuration is entirely the customer's domain. This breach falls entirely within the customer's responsibility boundary.
    *   *Why D is incorrect:* Terms of service do not absolve the customer of regulatory liability (GDPR, HIPAA, CCPA) for exposing PII. The customer bears legal and operational responsibility for the breach.

---

**Question 5**
An organization currently runs analytics on an on-premises data warehouse with 20 TB of storage and 64 CPU cores. Every quarter-end, queries take 12+ hours because the fixed hardware cannot handle the peak reporting load. A cloud architect proposes migrating to a cloud analytics platform. Which cloud characteristic most directly solves the quarter-end performance problem?
*   A) Durability — cloud providers replicate data across multiple availability zones, preventing data loss during hardware failure.
*   B) Elasticity — cloud platforms can automatically scale compute resources up during peak demand (quarter-end) and scale down afterward, so the fixed hardware bottleneck no longer applies.
*   C) Serverless execution — cloud analytics services eliminate the need to write SQL and instead use graphical interfaces that run faster than SQL queries.
*   D) Shared tenancy — multiple customers share the same physical hardware, which reduces cost per query by distributing fixed infrastructure expenses.
*   **Correct Answer:** B) Elasticity — cloud platforms can automatically scale compute resources up during peak demand (quarter-end) and scale down afterward, so the fixed hardware bottleneck no longer applies.
*   **Distractor Analysis:**
    *   *Why B is correct:* The root cause of the problem is insufficient fixed compute capacity at peak load. Elasticity — the ability to provision additional compute on demand and release it when not needed — directly solves this. On-premises hardware must be sized for peak load and sits idle the rest of the time; cloud resources expand and contract with demand.
    *   *Why A is incorrect:* Durability addresses data availability and resilience against hardware failure. The scenario describes a performance problem under peak load, not a data loss or availability problem.
    *   *Why C is incorrect:* Serverless execution eliminates infrastructure management overhead, but it does not eliminate SQL. Athena and BigQuery both use standard SQL. Speed improvements come from distributed compute and columnar storage, not from removing SQL.
    *   *Why D is incorrect:* Shared tenancy describes the physical model of cloud infrastructure but is not a customer-facing capability. Customers do not directly benefit from or control shared tenancy; elasticity is the feature they provision and pay for.
