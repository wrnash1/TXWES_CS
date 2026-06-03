# Quiz: Module 09 — Azure Storage

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. Total: 100 points.

---

### Question 1

A company stores regulatory compliance documents that must be retained for 7 years. These documents are accessed once a year during an audit and the access involves reading thousands of files over a two-day period. Which Blob Storage access tier provides the lowest overall cost for this scenario?

A. Hot tier — minimizes access latency during audits

B. Cool tier — balances storage and access costs for monthly access patterns

C. Archive tier — lowest storage cost for rarely accessed data

D. Premium tier — fastest retrieval for audit workloads

**Correct Answer: C**

**Distractor Analysis:**

- **A (Hot tier):** Hot tier has the highest storage cost. For data accessed once per year, the continuous high storage cost far exceeds the minimal access savings. Not cost-optimal. Incorrect.
- **B (Cool tier):** Cool tier is designed for data accessed infrequently but still more regularly than once per year. The storage cost is lower than Hot but higher than Archive. For annual-only access over 7 years, Archive is significantly cheaper. Incorrect.
- **C (Archive tier) — CORRECT:** Archive tier has the lowest storage cost of the three tiers and is designed for data accessed rarely — ideally less than once per year. With a 7-year retention and annual access, Archive provides the lowest total cost despite higher rehydration costs during the two-day audit.
- **D (Premium tier):** Premium tier is for high-performance block blobs requiring low latency and high transaction rates. It does not apply to compliance archiving scenarios and would be the most expensive option. Incorrect.

---

### Question 2

An Azure Blob Storage account uses Geo-Redundant Storage (GRS). A developer wants to read data from the secondary region endpoint to offload read traffic from the primary region. Which GRS variant supports reading from the secondary region?

A. Standard GRS

B. RA-GRS (Read-Access GRS)

C. ZRS

D. LRS with blob snapshots

**Correct Answer: B**

**Distractor Analysis:**

- **A (Standard GRS):** Standard GRS replicates to a secondary region but does NOT provide read access to the secondary endpoint. The secondary is only used by Microsoft during failover. Incorrect.
- **B (RA-GRS) — CORRECT:** RA-GRS (Read-Access Geo-Redundant Storage) provides a secondary read endpoint at `https://<account>-secondary.blob.core.windows.net`. Applications can route read traffic to this endpoint to distribute load or serve regional reads.
- **C (ZRS):** ZRS replicates across three Availability Zones in the primary region only. It provides no secondary region at all. Incorrect.
- **D (LRS with blob snapshots):** LRS replicates within a single datacenter. Snapshots are point-in-time copies within the same account — they provide versioning, not geo-redundancy or a secondary read endpoint. Incorrect.

---

### Question 3

A company needs to migrate 800 TB of legacy data from its on-premises data center to Azure Blob Storage. Their internet connection is 200 Mbps shared with production traffic. Which Azure solution is most appropriate for this migration?

A. Azure Import/Export with self-shipped hard drives

B. AzCopy command-line tool over the existing internet connection

C. Azure Data Box Heavy

D. Azure ExpressRoute with bandwidth boost

**Correct Answer: C**

**Distractor Analysis:**

- **A (Azure Import/Export):** Azure Import/Export is a legacy service where customers ship their own drives to an Azure datacenter. It works but requires sourcing, preparing, and shipping drives manually. For 800 TB, Data Box Heavy is the purpose-built, supported solution. Not the best answer.
- **B (AzCopy over 200 Mbps):** At 200 Mbps theoretical maximum (shared), transferring 800 TB would take approximately 370 days. This is completely impractical for a data migration project. Incorrect.
- **C (Azure Data Box Heavy) — CORRECT:** Data Box Heavy supports up to 1 PB usable capacity in a single device. For 800 TB, it is the appropriate purpose-built Microsoft solution. Microsoft ships the device, the customer loads data, ships it back, and Microsoft uploads it to Azure Storage securely.
- **D (ExpressRoute):** ExpressRoute provides high-bandwidth private connectivity but does not accelerate one-time data migration cost-effectively. A 10 Gbps ExpressRoute circuit would still take approximately 178 hours (7+ days) for 800 TB, plus ongoing circuit costs. Not optimal for one-time migration. Incorrect.

---

### Question 4

Which Azure Storage service should be used to store application logs that are continuously appended to as the application runs, with data written only at the end of the file and never modified?

A. Azure Table Storage with PartitionKey based on timestamp

B. Block blobs in Azure Blob Storage

C. Append blobs in Azure Blob Storage

D. Azure Queue Storage with FIFO ordering

**Correct Answer: C**

**Distractor Analysis:**

- **A (Table Storage):** Table Storage is a NoSQL key-value store for semi-structured entities. While it can store log records, it is not designed for streaming append operations and does not natively provide the append-only blob semantics. Incorrect.
- **B (Block blobs):** Block blobs are for general-purpose files. To append to a block blob, you must overwrite or re-upload entire blocks — this is not efficient for continuous log streaming. Incorrect.
- **C (Append blobs) — CORRECT:** Append blobs are specifically optimized for append operations. New data is added as blocks to the end of the blob without modifying existing content. This is the ideal type for log files, audit trails, and streaming data that grows continuously.
- **D (Queue Storage):** Queue Storage is a messaging service for producer-consumer communication, not for persistent log file storage. Messages are deleted after consumption. Incorrect.

---

### Question 5

A company wants maximum storage resiliency for critical business data. The data must survive both an individual zone failure within the primary region AND a complete regional outage. Which redundancy option meets both requirements?

A. ZRS (Zone-Redundant Storage)

B. GRS (Geo-Redundant Storage)

C. LRS (Locally Redundant Storage)

D. GZRS (Geo-Zone-Redundant Storage)

**Correct Answer: D**

**Distractor Analysis:**

- **A (ZRS):** ZRS protects against zone failure within the primary region but does NOT protect against a complete regional outage. If the entire region goes down, ZRS data is unavailable. Incorrect.
- **B (GRS):** GRS protects against regional outage (geo-replication to secondary region) but uses LRS within the primary region — it does NOT protect against a zone failure within the primary region (because the three primary copies are all in the same datacenter). Incorrect.
- **C (LRS):** LRS only protects against disk/server failure within a single datacenter. It provides neither zone nor regional protection. Incorrect.
- **D (GZRS) — CORRECT:** GZRS combines ZRS (three copies across three availability zones in the primary region) with geo-replication to a secondary region. It is the only option that protects against BOTH zone-level failures in the primary region AND complete regional outages.

---

### Question 6

An application team wants to mount an Azure storage resource as a network drive on their Windows development VMs using standard Windows file sharing protocol. Which Azure Storage service supports this scenario?

A. Azure Blob Storage with anonymous access enabled

B. Azure Table Storage

C. Azure Files with SMB protocol

D. Azure Queue Storage

**Correct Answer: C**

**Distractor Analysis:**

- **A (Blob Storage):** Azure Blob Storage is accessed via HTTP/HTTPS REST API. It cannot be mounted as a Windows network drive using standard file sharing protocols without third-party software. Incorrect.
- **B (Table Storage):** Azure Table Storage is a NoSQL data store accessed via REST API. It cannot be mounted as a file system drive. Incorrect.
- **C (Azure Files with SMB) — CORRECT:** Azure Files provides fully managed file shares accessible via SMB 2.1 and SMB 3.0 protocols — the native Windows file sharing standard. Azure file shares can be mapped as network drives on Windows (and mounted on Linux/macOS as well) with no code changes required.
- **D (Queue Storage):** Queue Storage is a messaging service for asynchronous communication. It has no file system interface and cannot be mounted as a drive. Incorrect.

---

### Question 7

What is the minimum storage duration for a blob in the Cool access tier before Azure applies an early deletion penalty?

A. 7 days

B. 14 days

C. 30 days

D. 90 days

**Correct Answer: C**

**Distractor Analysis:**

- **A (7 days):** Incorrect. The Cool tier minimum is 30 days, not 7.
- **B (14 days):** Incorrect. The Cool tier minimum is 30 days.
- **C (30 days) — CORRECT:** Blobs in the Cool tier must remain for a minimum of 30 days. If a blob is deleted, moved to Hot tier, or moved to Archive before 30 days have elapsed, a prorated early deletion charge applies for the remaining days.
- **D (90 days):** Incorrect. 90 days is a common internal practice recommendation, not the Azure-enforced minimum. The Archive tier has a 180-day minimum, not 90 days.

---

### Question 8

A developer needs to build a system where a web front end can add tasks to a backlog and a background worker can pick up and process tasks independently, without the front end waiting for the worker to complete. Which Azure Storage service is designed for this asynchronous decoupling pattern?

A. Azure Table Storage

B. Azure Blob Storage

C. Azure Queue Storage

D. Azure File Storage

**Correct Answer: C**

**Distractor Analysis:**

- **A (Table Storage):** Table Storage stores structured data entities but has no built-in messaging or task visibility timeout mechanism. Applications would need to implement complex polling and locking logic. Not designed for this pattern. Incorrect.
- **B (Blob Storage):** Blob Storage stores files and objects. While a trigger-based system could be built around blob uploads, it does not natively provide the producer-consumer messaging pattern with visibility timeouts. Incorrect.
- **C (Queue Storage) — CORRECT:** Azure Queue Storage is specifically designed for the producer-consumer messaging pattern. The front end adds messages; the worker reads and processes them. Visibility timeouts ensure messages are re-processed if the worker fails. Messages persist until explicitly deleted after successful processing.
- **D (File Storage):** Azure Files provides SMB file shares. While files could be used as a crude task handoff mechanism, it lacks built-in message delivery guarantees and visibility timeouts. Incorrect.

---

### Question 9

Which Azure Storage account type is recommended for new deployments that need to support Blob, Files, Queue, and Table services with all access tiers available?

A. General-purpose v1 (GPv1)

B. Premium Block Blobs

C. General-purpose v2 (GPv2)

D. BlobStorage

**Correct Answer: C**

**Distractor Analysis:**

- **A (GPv1):** GPv1 is the legacy storage account type. It supports the same services as GPv2 but has higher per-transaction costs and does not support access tiers (Hot/Cool/Archive) for Blob. Microsoft recommends upgrading GPv1 accounts to GPv2. Incorrect.
- **B (Premium Block Blobs):** Premium Block Blobs uses SSD-backed storage for high-performance blob operations. It supports only block blobs and append blobs — not Azure Files, Queue, or Table services. It also does not support access tiers. Incorrect.
- **C (GPv2) — CORRECT:** General-purpose v2 is the recommended storage account type. It supports all four services (Blob, Files, Queue, Table), supports all three access tiers (Hot, Cool, Archive) for Blob, and provides the latest storage features. This is the go-to choice for new deployments.
- **D (BlobStorage):** BlobStorage accounts are a legacy type that supported only blob storage. This account type was effectively superseded by GPv2 and is no longer recommended for new deployments. Incorrect.

---

### Question 10

An organization is evaluating Azure Blob Storage Lifecycle Management. They want blobs that have not been accessed in 60 days to automatically move to the Archive tier. What type of policy rule condition should they use?

A. daysAfterCreationGreaterThan: 60

B. daysAfterModificationGreaterThan: 60

C. daysAfterLastAccessTimeGreaterThan: 60

D. daysAfterExpiryGreaterThan: 60

**Correct Answer: C**

**Distractor Analysis:**

- **A (daysAfterCreationGreaterThan):** This condition is based on the blob's creation date, not its last access date. A blob created 60 days ago but accessed yesterday would incorrectly be moved to Archive. Not the right condition for "not accessed in 60 days." Incorrect.
- **B (daysAfterModificationGreaterThan):** This is the most common condition and is based on the blob's last modification date. However, for data that is read-only (not modified after upload), this behaves the same as daysAfterCreationGreaterThan. The question asks specifically about access, not modification. Incorrect.
- **C (daysAfterLastAccessTimeGreaterThan) — CORRECT:** This condition transitions blobs based on the last access time — when the blob was last read or written. It requires enabling access time tracking on the storage account. This is the correct condition when the intent is to archive data that hasn't been accessed (read) in 60 days.
- **D (daysAfterExpiryGreaterThan):** This condition is used for blob version expiry, not access time. It applies to versioned blob policies, not general access-based tiering. Incorrect.

---

*Quiz 09 — Module 09: Azure Storage | CIS-4331 | Texas Wesleyan University*
