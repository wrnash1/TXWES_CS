# Quiz: Module 06 - Azure Storage Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A company needs to store machine-generated log files that grow continuously throughout the day. New log entries are added at the end of the file, and the existing content is never modified. Which Azure Blob type is most appropriate?

- A) Block blob
- B) Append blob
- C) Page blob
- D) Archive blob

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Append blobs are optimized for append-only write operations. Each write adds a new block at the end. This makes them ideal for log files, audit data, and streaming data where content is continuously added but existing entries are never modified.
- *Why A is incorrect:* Block blobs support general read and write operations but are not specifically optimized for append-only patterns. For log files where no modification of existing data is needed, append blobs provide better performance and cleaner semantics.
- *Why C is incorrect:* Page blobs are optimized for random read/write operations in fixed-size pages. They underpin Azure VM managed disks and are designed for workloads requiring frequent updates to arbitrary byte ranges — the opposite of sequential log appending.
- *Why D is incorrect:* "Archive blob" is not a blob type — Archive is an access tier that can be applied to block or append blobs. Archive tier data is offline and takes hours to retrieve, making it entirely unsuitable for actively written log files.

---

## Question 2

Which Azure Storage redundancy option protects against a complete Azure region failure by replicating data to a geographically separate region, while also providing zone-level redundancy within the primary region?

- A) Locally Redundant Storage (LRS)
- B) Zone-Redundant Storage (ZRS)
- C) Geo-Redundant Storage (GRS)
- D) Geo-Zone-Redundant Storage (GZRS)

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* GZRS combines ZRS (three copies across three Availability Zones in the primary region) with asynchronous geo-replication to a secondary region. It protects against both zone-level failures within the primary region AND complete regional failures — providing the highest level of protection.
- *Why A is incorrect:* LRS stores three copies within a single datacenter in one region. It protects against hardware failure within that datacenter but provides no zone or regional redundancy.
- *Why B is incorrect:* ZRS stores copies across three zones in one region, protecting against datacenter failures. However, it provides no protection against the entire region going offline — all three zones are within the same region and could be affected by a regional disaster.
- *Why C is incorrect:* GRS provides regional failure protection by replicating to a secondary region, but uses LRS (single datacenter) in the primary region. It does not provide zone-level redundancy within the primary region. GRS protects against regional failure but not against a single datacenter failure within the primary region.

---

## Question 3

An application needs to grant temporary read-only access to specific Azure Blob Storage files to external auditors for 48 hours. The auditors must not have ongoing access after the 48-hour period. Which access mechanism is most appropriate?

- A) Storage account key (key1 or key2)
- B) Shared Access Signature (SAS) token with 48-hour expiry and read-only permission
- C) Add the auditors as Storage Blob Data Owner role assignments
- D) Set the container public access to allow anonymous reads

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* SAS tokens are designed exactly for this use case — time-limited, permission-scoped access to specific storage resources. A SAS token can be configured to expire after 48 hours, restricted to read-only operations, and limited to specific blob paths. After expiry, the token provides no access.
- *Why A is incorrect:* Storage account keys grant full administrative access to everything in the account with no time limit. Sharing a key with auditors gives them permanent full access — they could read, write, and delete any data in the account, and the access does not automatically expire.
- *Why C is incorrect:* Azure RBAC role assignments (Storage Blob Data Owner) persist until manually removed. This does not automatically expire after 48 hours and grants the highest level of data access. Using RBAC for temporary external auditors creates an ongoing access management burden.
- *Why D is incorrect:* Setting container public access allows anonymous access to anyone on the internet — not just the specific auditors. This violates the principle of least privilege and exposes data to the public, which is inappropriate for audit data.

---

## Question 4

Which Azure Storage service should an organization use to replace on-premises network file shares that Windows and Linux VMs access using drive letter mappings?

- A) Azure Blob Storage
- B) Azure Table Storage
- C) Azure Files
- D) Azure Queue Storage

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Files provides fully managed cloud file shares accessible via SMB (for Windows) and NFS (for Linux). VMs can mount Azure File shares as network drives using standard OS protocols — Windows VMs map them as drive letters; Linux VMs mount them at a directory path. This is the direct replacement for on-premises file servers.
- *Why A is incorrect:* Azure Blob Storage is an object store accessed via HTTP REST API. It cannot be mounted as a drive letter or accessed with standard file system protocols like SMB or NFS. Applications require code changes to use the Blob Storage REST API.
- *Why B is incorrect:* Azure Table Storage is a NoSQL key-value store for structured data. It is not a file system and cannot be mounted or used as a file share replacement.
- *Why D is incorrect:* Azure Queue Storage is a message queuing service for asynchronous communication between application components. It is not a file storage service and cannot be used as a network drive.

---

## Question 5

A blob in Azure Archive tier needs to be read immediately. What must happen before the blob can be accessed?

- A) The blob can be read immediately — Archive tier has the same access latency as Hot tier
- B) The blob must be rehydrated to Hot or Cool tier first, which takes up to 15 hours at standard priority
- C) The storage account must be upgraded from LRS to GRS to enable Archive access
- D) A SAS token must be generated to unlock Archive tier blobs for reading

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Blobs in Archive tier are stored offline and cannot be read directly. To access the data, the blob must first be rehydrated — either by changing its tier to Hot or Cool, or by copying it to a new blob in a non-archive tier. Standard priority rehydration takes up to 15 hours. High priority rehydration (higher cost) can complete in under 1 hour.
- *Why A is incorrect:* Archive tier has dramatically different access latency compared to Hot or Cool tier. Archive data is offline, and direct access is not possible — the hours-long rehydration process is mandatory.
- *Why C is incorrect:* Storage account redundancy (LRS vs. GRS) has no relationship to the Archive access tier or rehydration process. Rehydration is a tier-level operation independent of redundancy configuration.
- *Why D is incorrect:* SAS tokens control access authorization — who can access what. They do not affect the physical state of archived data. A SAS token cannot make an offline archived blob immediately readable.

---

## Question 6

An e-commerce application has two components: a web frontend that accepts orders and an order processing backend. Orders must not be lost even if the backend is temporarily unavailable for maintenance. The components should be decoupled so the frontend is not blocked waiting for the backend to process. Which Azure Storage service supports this architecture?

- A) Azure Blob Storage — store each order as a blob for the backend to process
- B) Azure Table Storage — store orders as table entities for the backend to read
- C) Azure Queue Storage — the frontend writes order messages to a queue; the backend reads and processes at its own pace
- D) Azure Files — store order files in a shared folder the backend monitors

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Queue Storage is designed for exactly this decoupled, asynchronous messaging pattern. The frontend writes order messages to the queue and returns immediately — it is not blocked waiting for processing. The backend reads messages from the queue at whatever pace it can handle. If the backend is down for maintenance, messages accumulate in the queue safely and are processed when the backend recovers.
- *Why A is incorrect:* Blob Storage has no built-in queuing or message visibility mechanism. The backend would need to poll for new blobs, handle race conditions between multiple workers, and manage the "in-progress" state manually. This is operationally complex compared to Queue Storage's built-in message locking.
- *Why B is incorrect:* Table Storage is a data store, not a messaging system. Like Blob Storage, it lacks message visibility timeouts, automatic message locking for exclusive processing, and other queue-specific behaviors.
- *Why D is incorrect:* File-based polling patterns (watch a folder for new files) are fragile, have race conditions with multiple workers, and lack the retry-on-failure semantics of a proper queue. Azure Files is designed for file sharing, not workflow orchestration.

---

## Question 7

What is the minimum storage retention period for blobs in the Archive access tier before early deletion fees apply?

- A) 7 days
- B) 30 days
- C) 90 days
- D) 180 days

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* The Archive tier has a minimum storage duration of 180 days. If a blob in Archive tier is deleted, overwritten, or moved to a different tier before 180 days have elapsed, a prorated early deletion fee is charged for the remaining days. This reflects the cost structure of Archive tier, which is optimized for long-term storage.
- *Why A is incorrect:* 7 days does not correspond to any storage tier minimum retention period in Azure. This may be confused with some backup retention policies.
- *Why B is incorrect:* 30 days is the minimum retention period for the Cool access tier, not Archive. Deleting Cool tier blobs before 30 days incurs early deletion fees at the Cool tier rate.
- *Why C is incorrect:* 90 days is the minimum retention period for the Cold access tier (a tier between Cool and Archive). This is sometimes confused with Archive because of similar naming.

---

## Question 8

A developer deploys an Azure Storage Account with the `Standard_GRS` SKU. By default, can the developer read data from the secondary region endpoint?

- A) Yes — GRS allows reading from both the primary and secondary region by default
- B) No — with GRS, the secondary region is only used for failover; RA-GRS is required to read from the secondary
- C) Yes — but only during an active regional failover event
- D) No — GRS does not replicate data to a secondary region; GZRS is required for geo-replication

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Standard GRS replicates data to the secondary (paired) region asynchronously, but the secondary region endpoint is read-only and only accessible after a regional failover is initiated. To have constant read access to the secondary region without waiting for failover, Read-Access Geo-Redundant Storage (RA-GRS, SKU `Standard_RAGRS`) must be selected. RA-GRS gives a secondary endpoint like `[account-name]-secondary.blob.core.windows.net`.
- *Why A is incorrect:* This describes RA-GRS behavior, not GRS. Standard GRS replicates to the secondary region but does not expose that data for reading until failover occurs.
- *Why C is incorrect:* While the secondary data becomes accessible during failover (when GRS failover is initiated), "only during failover" does not fully describe when secondary access is available — after failover completes, the secondary becomes the primary. The question asks about normal (non-failover) read access, which GRS does not provide.
- *Why D is incorrect:* GRS does replicate to a secondary region. This is the core definition of GRS. GZRS adds zone-level redundancy in the primary region in addition to geo-replication, but both GRS and GZRS provide geo-replication.

---

## Question 9

An organization currently stores all storage data with Geo-Redundant Storage (GRS). They want to reduce storage costs for a large dataset of 50 TB of historical archived data that has no regional recovery requirement but must remain durable within a single region. Which storage configuration change would reduce cost while maintaining appropriate durability?

- A) Change the entire storage account to LRS
- B) Keep the storage account as GRS but move the archived blobs to Archive access tier with LRS-equivalent redundancy on a separate storage account
- C) Move the archived data to a separate storage account with LRS redundancy and Archive access tier
- D) Delete the secondary region copies manually to reduce the GRS overhead

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Creating a separate storage account with LRS (no regional redundancy needed per the scenario) and Archive tier (lowest cost for rarely accessed data) achieves the lowest storage cost for this historical dataset. LRS provides sufficient intra-datacenter durability, and Archive provides the lowest per-GB storage rate. Changing the account type to LRS removes the geo-replication cost.
- *Why A is incorrect:* Changing the entire storage account to LRS would affect all data in that account, including data that does need GRS redundancy. The better approach is isolating the historical archive data in a separate account.
- *Why B is incorrect:* Azure Storage accounts have a single redundancy SKU that applies to all data in the account. You cannot have GRS for some blobs and LRS for others within the same account. The redundancy level is set at the account level, not the blob or container level.
- *Why D is incorrect:* You cannot manually delete secondary region copies in GRS. The replication is fully managed by Azure. The only way to stop geo-replication charges is to change the account SKU to LRS or ZRS.

---

## Question 10

Azure Blob Storage supports static website hosting, allowing HTML, CSS, and JavaScript files to be served directly from a storage account as a website. Which access configuration is required for the files to be publicly accessible to website visitors?

- A) The storage account must use RA-GRS redundancy
- B) The blob container serving website content must have public access enabled, or the static website feature must be enabled through the storage account's "Static website" setting
- C) A SAS token must be embedded in every HTML file link
- D) The storage account must be created in the Premium performance tier

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Storage static website hosting creates a special `$web` container, and content in that container is served publicly through the static website endpoint (`[account-name].z13.web.core.windows.net`). The static website feature must be enabled in the storage account settings. Alternatively, enabling public access on a container allows direct public blob URL access.
- *Why A is incorrect:* Storage redundancy (RA-GRS vs. LRS etc.) has no relationship to website hosting or public accessibility of blobs. Redundancy determines where copies are stored, not whether they are publicly accessible.
- *Why C is incorrect:* SAS tokens are used for authenticated access, not for public anonymous access. Embedding SAS tokens in HTML links is also a security anti-pattern — the tokens would be visible in browser source code and could be shared inappropriately.
- *Why D is incorrect:* Premium performance tier uses SSD-backed storage optimized for high-IOPS workloads. Static website hosting does not require Premium tier and is fully functional on the Standard tier. Using Premium for static website files would be unnecessarily expensive.
