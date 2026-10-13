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

---

### Question 11 (5 points)

A company stores 10 TB of product images in Azure Blob Storage (Hot tier). Images are accessed heavily in the first week after upload but rarely afterward. The storage team wants to reduce costs automatically without manual intervention. Which Azure feature should they configure?

- A) Azure Storage replication failover to move old blobs to a secondary region
- B) A Blob Storage Lifecycle Management policy that transitions blobs to Cool tier after 7 days and Archive after 90 days
- C) Azure File Sync to cache frequently accessed blobs on local servers
- D) Change the entire storage account from GPv2 to Premium Block Blobs for lower per-GB cost

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Lifecycle Management policies automate tier transitions based on blob age metrics (days since creation, last modification, or last access). A policy moving blobs to Cool after 7 days and Archive after 90 days fully automates the cost optimization based on the described access pattern without any manual intervention.
  - *Why A is incorrect:* Storage replication failover is for disaster recovery — it switches data to the secondary region during a regional outage. It does not move blobs between access tiers or reduce storage costs for infrequently accessed data.
  - *Why C is incorrect:* Azure File Sync synchronizes Azure Files shares to on-premises Windows Servers — it has no relationship to Blob Storage access tiers or lifecycle management.
  - *Why D is incorrect:* Premium Block Blobs uses SSD storage optimized for low-latency, high-throughput workloads. It is significantly more expensive per GB than Standard Hot tier and does not support access tiers. For a cost reduction scenario based on access frequency, Premium Block Blobs is the wrong direction.

---

### Question 12 (5 points)

A developer uploads a file to Azure Blob Storage and then calls `az storage blob set-tier --tier Archive`. One hour later, another team member tries to download the file with `az storage blob download` and receives an error. What is the cause?

- A) The `set-tier` command failed silently and the blob was deleted
- B) Archive tier blobs are offline and must be rehydrated to Hot or Cool tier before they can be read; rehydration takes up to 15 hours at standard priority
- C) The blob is locked because `set-tier` acquires an exclusive lease that must be released first
- D) Archive tier requires RA-GRS redundancy; the account must be upgraded before the blob can be read

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Blobs in Archive tier are stored offline on a cost-optimized storage medium. They cannot be read directly. Before downloading, the blob must be rehydrated by changing its tier to Hot or Cool (or copying it to a new blob in a non-archive tier). Standard priority rehydration takes up to 15 hours; high priority takes under 1 hour for objects up to 10 GB.
  - *Why A is incorrect:* The `set-tier` command does not delete blobs. The blob still exists in the container — it is simply offline and inaccessible until rehydrated.
  - *Why C is incorrect:* The `set-tier` command does not acquire a lease on the blob. Azure Blob leases are a separate, explicit mechanism for exclusive write access. Tier changes do not affect blob lease state.
  - *Why D is incorrect:* Archive tier has no dependency on GRS or RA-GRS redundancy. Any storage redundancy option (LRS, ZRS, GRS, etc.) supports Archive tier. Redundancy is independent of access tier.

---

### Question 13 (5 points)

An organization needs to store structured NoSQL data where each record represents an IoT sensor reading with fields: `DeviceId` (used for grouping), `Timestamp` (used for ordering within a device), `Temperature`, and `Humidity`. The data will be queried by DeviceId and Timestamp range. Cost must be minimized. Which Azure storage option is most appropriate?

- A) Azure SQL Database with a table indexed on DeviceId and Timestamp
- B) Azure Table Storage with DeviceId as the PartitionKey and Timestamp as the RowKey
- C) Azure Blob Storage with one JSON file per sensor reading
- D) Azure Queue Storage with one message per sensor reading

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Table Storage is a NoSQL key-value store optimized for exactly this pattern. The PartitionKey (DeviceId) determines the storage partition for efficient querying by device. The RowKey (Timestamp) orders rows within a partition for range queries. Table Storage charges per GB stored and per transaction, making it extremely cost-effective for high-volume IoT telemetry.
  - *Why A is incorrect:* Azure SQL Database is a relational database with higher cost per GB and complex schema management. While it would work, it is over-engineered and more expensive for simple key-based lookups of unstructured IoT data. Table Storage is more cost-effective for this volume.
  - *Why C is incorrect:* Storing one JSON file per sensor reading in Blob Storage creates millions of tiny blobs, making range queries by device and time extremely expensive in terms of both transactions and operational complexity. Blob Storage lacks native query capabilities for structured data.
  - *Why D is incorrect:* Queue Storage is for temporary message passing — messages are deleted after processing. Sensor data needs to be retained for historical analysis, not consumed and discarded like a work queue message.

---

### Question 14 (5 points)

A security team requires that all Azure Blob Storage data at rest be encrypted using keys managed by the organization (not Microsoft). The keys must be stored in Azure Key Vault and rotatable by the security team. Which Azure Storage encryption feature meets this requirement?

- A) Azure Storage Service Encryption (SSE) with Microsoft-managed keys (default)
- B) Customer-Managed Keys (CMK) with keys stored in Azure Key Vault
- C) Client-side encryption with keys stored on-premises outside Azure
- D) Azure Disk Encryption for storage accounts

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Customer-Managed Keys (CMK) allow organizations to use their own encryption keys stored in Azure Key Vault to encrypt Azure Storage data. The security team controls the key lifecycle — creation, rotation, and revocation. If the key is revoked, the storage account data becomes inaccessible. This satisfies the requirement for organization-controlled keys in Key Vault.
  - *Why A is incorrect:* Microsoft-managed keys (SSE default) are controlled by Microsoft, not the organization. While data is still encrypted at rest, the organization has no control over the key material. This does not meet the requirement for organization-managed keys.
  - *Why C is incorrect:* Client-side encryption (encrypting data before uploading it) uses keys managed entirely by the application. While this provides strong isolation, the keys must be managed entirely by the application code — not stored in Key Vault. It is also more complex to implement than CMK.
  - *Why D is incorrect:* Azure Disk Encryption is for VM managed disks (OS and data disks), not for Azure Storage accounts. Storage accounts use Storage Service Encryption (SSE), not disk encryption.

---

### Question 15 (5 points)

A company plans to migrate 500 TB of on-premises data to Azure using Azure Data Box. The Data Box device arrives, data is loaded onto it, and the device is shipped back to Microsoft. Once Microsoft receives the device, what happens to the data?

- A) Microsoft engineers manually copy the data to the customer's specified storage account and then notify the customer
- B) Microsoft uploads the data to the customer's specified Azure Storage account, then performs a secure wipe of the Data Box device
- C) The data is held in a Microsoft staging area until the customer activates the storage account
- D) Microsoft compresses and encrypts the data before uploading, which may alter the original file formats

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When Microsoft receives the returned Data Box device, they upload all data to the customer's specified Azure Storage account. After the data copy is verified, Microsoft performs a secure wipe of the Data Box device following NIST 800-88r1 guidelines (for Data Box) before the device is reused or retired. The customer receives a notification when the upload is complete.
  - *Why A is incorrect:* The process is automated, not performed by Microsoft engineers manually. The upload and wipe process is a standardized, automated procedure with tracking available through the Azure Portal.
  - *Why C is incorrect:* Data is not held in a staging area pending customer action. The upload to the customer's storage account happens automatically after the device is received and processed by Microsoft.
  - *Why D is incorrect:* Azure Data Box uploads data as-is without compressing or re-encoding it. Files arrive in Azure Storage in their original format. Azure Storage Service Encryption (SSE) encrypts the data at rest transparently, but this does not alter file formats or content.

---

### Question 16 (5 points)

A development team uses Azure Storage to hold build artifacts. Each build uploads new files, and the team wants to prevent any build artifact from being deleted or overwritten for at least 30 days for compliance. Which Azure Blob Storage feature enforces this immutability requirement?

- A) Azure Storage soft delete with a 30-day retention period
- B) A Shared Access Signature (SAS) token with read-only permissions
- C) Azure Blob Storage immutability policies (WORM — Write Once, Read Many) with a time-based retention of 30 days
- D) Azure Storage Lifecycle Management with a delete rule at 30 days

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Blob Storage immutability policies implement WORM (Write Once, Read Many) protection. A time-based retention policy locks blobs so they cannot be deleted or overwritten until the retention interval expires. This is a compliance-grade feature used in regulated industries. Once locked, even Azure subscription admins cannot delete the data during the retention period.
  - *Why A is incorrect:* Soft delete protects against accidental deletion by retaining deleted blobs for a configured period in a hidden state. However, it does not prevent deliberate deletion or overwrite by authorized users with sufficient permissions. It is a recovery mechanism, not an immutability control.
  - *Why B is incorrect:* A read-only SAS token prevents the holder of that token from writing or deleting. However, anyone with the storage account key or Owner/Contributor RBAC can still delete blobs. SAS tokens restrict specific access credentials but do not enforce system-wide immutability.
  - *Why D is incorrect:* A Lifecycle Management delete rule would automatically delete blobs after 30 days — the opposite of what is needed. The requirement is to prevent deletion for 30 days, not to delete after 30 days.

---

### Question 17 (5 points)

An organization runs Azure Files to host a shared department drive. Users mounting the share from home report that they cannot connect to the file share on port 445. What is the most likely cause, and what is the recommended workaround for remote users?

- A) Azure Files requires a Premium SKU for remote access; upgrade the storage account
- B) Port 445 (SMB) is commonly blocked by ISPs and home routers; the workaround is to use Azure VPN Gateway with Point-to-Site VPN to access the share over a secure tunnel
- C) Azure Files is only accessible from within Azure VNets and cannot be reached from on-premises
- D) The file share quota has been reached; increase the quota to allow new connections

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Many ISPs and home/corporate firewalls block outbound TCP port 445 (SMB) due to historical security concerns. Azure Files uses SMB over port 445. The recommended workaround for remote users who cannot use port 445 is to connect via Azure VPN Gateway (Point-to-Site VPN), which tunnels the SMB traffic over HTTPS (port 443). Alternatively, Azure Files REST API access works over HTTPS port 443.
  - *Why A is incorrect:* Azure Files is accessible remotely on both Standard and Premium SKUs. The SKU affects performance (HDD vs. SSD) and features, not whether remote access is possible. Port 445 blocking is an ISP/firewall issue unrelated to the storage SKU.
  - *Why C is incorrect:* Azure Files is accessible from outside Azure VNets — it has a public endpoint at `<account>.file.core.windows.net`. The connectivity issue is the ISP blocking port 445, not a VNet restriction.
  - *Why D is incorrect:* File share quota limits affect how much data can be stored, not how many connections can be made. A full quota would prevent uploads, not initial SMB connection establishment.

---

### Question 18 (5 points)

A storage administrator needs to generate a URL that gives a contractor read-only access to a single blob for exactly 48 hours, using the least privileged access mechanism. Which approach generates the most appropriate URL?

- A) Make the blob container public (anonymous access) and share the blob URL
- B) Share the storage account key and let the contractor use Azure Storage Explorer
- C) Generate a Service SAS token with read permission scoped to the specific blob and a 48-hour expiry, then append it to the blob URL
- D) Add the contractor's email address as a Storage Blob Data Owner on the storage account

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* A Service SAS token can be scoped to a single blob, limited to read permission, and set to expire after exactly 48 hours. The resulting URL (`https://account.blob.core.windows.net/container/blob?sv=...&se=...&sp=r&sig=...`) is self-contained — the contractor uses it directly with no other credentials. After 48 hours the URL is automatically invalid.
  - *Why A is incorrect:* Enabling public container access allows anonymous access to all blobs in the container by anyone with the URL — not just this contractor, and not just for 48 hours. This violates least privilege and the time-limited requirement.
  - *Why B is incorrect:* Storage account keys grant full administrative access to the entire storage account — all containers, all blobs, all services. They cannot be scoped to a single blob or limited to a time window. Sharing a key with a contractor is a major security risk.
  - *Why D is incorrect:* Storage Blob Data Owner is an RBAC role that persists until manually revoked. It does not expire automatically after 48 hours and grants read, write, and delete access to all blobs in the account — far exceeding least privilege for read-only access to a single blob.

---

### Question 19 (5 points)

A company's application uses Azure Queue Storage messages with a default visibility timeout of 30 seconds. A background worker dequeues a message and begins processing. The processing takes 45 seconds to complete. What happens after 30 seconds if the worker has not yet completed processing?

- A) The message is permanently deleted from the queue after the timeout expires
- B) The message becomes visible again in the queue and can be dequeued by another worker, potentially causing duplicate processing
- C) The queue locks all other workers until the original worker finishes processing
- D) The message is moved to a dead-letter queue for manual inspection

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Queue Storage visibility timeout makes a message invisible to other consumers for the duration of the timeout after it is dequeued. If the consumer does not delete the message (confirming successful processing) before the timeout expires, the message becomes visible again and can be picked up by any other worker. This protects against message loss if a worker fails — but it means applications must handle idempotency (processing the same message twice must be safe).
  - *Why A is incorrect:* Messages are not automatically deleted when the visibility timeout expires. Only explicit calls to `DeleteMessage` (after successful processing) remove a message. Expiring timeout simply makes the message visible again.
  - *Why C is incorrect:* Queue Storage does not lock other workers when one worker is processing a message. The visibility timeout mechanism is per-message — other messages in the queue remain accessible to other workers. Only the specific message being processed is invisible during its timeout window.
  - *Why D is incorrect:* Azure Queue Storage does not have a built-in dead-letter queue. Messages that are dequeued and returned to the queue repeatedly (exceeding the dequeue count threshold) can be detected by the application, but there is no automatic dead-lettering. Azure Service Bus (a different messaging service) provides dead-letter queues.

---

### Question 20 (5 points)

A company evaluates whether to use Azure Storage Account keys or Azure AD (Entra ID) authentication for an application that reads blobs. The security team recommends Entra ID. Which statement correctly describes a security advantage of Entra ID authentication over storage account keys for this scenario?

- A) Entra ID authentication is faster than key-based authentication because it skips the HMAC signature computation
- B) Entra ID authentication uses short-lived tokens and integrates with Conditional Access and MFA policies; storage account keys are long-lived shared secrets that cannot be scoped to a specific service or user
- C) Storage account keys support key rotation; Entra ID tokens cannot be revoked once issued
- D) Entra ID authentication requires Premium storage accounts; standard accounts must use storage account keys

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Entra ID (Azure AD) authentication for Azure Storage uses OAuth 2.0 bearer tokens. These tokens are short-lived (typically 1 hour), scoped to specific roles via RBAC, and subject to Conditional Access policies (including MFA, location restrictions, and device compliance). Storage account keys are full-access shared secrets with no expiry by default, no scope restriction, and no integration with identity governance policies.
  - *Why A is incorrect:* Authentication mechanism performance (speed) is not the primary security distinction. Both methods involve cryptographic operations. HMAC and token validation are both fast. Performance is not a security argument for choosing Entra ID over keys.
  - *Why C is incorrect:* This reverses the truth. Storage account key rotation is possible (via key regeneration) but requires updating all applications using the key. Entra ID tokens can be effectively revoked by changing RBAC role assignments or by Conditional Access policy enforcement. Token revocation in Entra ID is faster than coordinating key rotation across all consumers.
  - *Why D is incorrect:* Entra ID (Azure AD) authentication for Azure Storage is available on all storage account SKUs — Standard and Premium. There is no SKU restriction for using Entra ID authentication.
