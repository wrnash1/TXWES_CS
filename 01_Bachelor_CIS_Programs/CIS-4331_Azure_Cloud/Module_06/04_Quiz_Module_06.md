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

---

### Question 11 (5 points)

A video streaming company stores 200 TB of video files that are accessed frequently during the first 30 days after upload, then accessed rarely after that. To minimize storage costs, which Azure Blob Storage feature should they implement?

- A) Move all videos to Archive tier on a fixed schedule using a script
- B) Configure a Blob Storage Lifecycle Management policy that transitions blobs to Cool tier after 30 days and to Archive tier after 90 days
- C) Create two separate storage accounts — one Hot and one Archive — and manually copy files between them
- D) Use ZRS redundancy to reduce per-GB storage costs

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Blob Storage Lifecycle Management policies automate tier transitions based on blob age (days since last modification or creation). A policy can be configured to move blobs from Hot to Cool after 30 days and to Archive after 90 days without any manual intervention. This is the purpose-built solution for cost optimization based on access patterns.
  - *Why A is incorrect:* Using a script to manually move blobs is operationally complex, error-prone, and requires ongoing maintenance. Lifecycle Management policies are declarative and fully managed by Azure — no custom scripts or scheduling are needed.
  - *Why C is incorrect:* Manually copying files between storage accounts is operationally expensive, requires custom scripts, and creates a period where data exists in both accounts (wasting money). Lifecycle Management handles this automatically within a single account.
  - *Why D is incorrect:* ZRS redundancy affects durability (data copies across zones) not the per-GB storage price tier. Changing redundancy does not reduce costs based on access frequency. Access tier (Hot/Cool/Archive) determines per-GB storage price.

---

### Question 12 (5 points)

A developer needs to allow a third-party application to upload files directly to a specific Azure Blob container without exposing the storage account key. The upload permission should be limited to a single container and expire in 24 hours. Which access mechanism satisfies all of these requirements?

- A) Account-level SAS token with write permission on all containers
- B) Service-level SAS token scoped to the specific container with write permission and a 24-hour expiry
- C) Grant the third-party application the Storage Blob Data Owner RBAC role
- D) Enable public write access on the container

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A service-level SAS token can be scoped to a single container with only write permission and a defined expiry time. This satisfies all three requirements: no storage key exposure, single-container scope, and automatic expiry after 24 hours.
  - *Why A is incorrect:* An account-level SAS with write on all containers grants broader access than required. The principle of least privilege requires limiting the scope to only the specific container needed.
  - *Why C is incorrect:* Storage Blob Data Owner is a permanent RBAC role assignment that does not expire automatically. It also grants read, write, and delete permissions across all containers in the account — far more than write access to a single container.
  - *Why D is incorrect:* Public write access is not a supported configuration in Azure Blob Storage. Azure only supports public anonymous read access for containers (anonymous reads, not writes). Enabling any form of public access also violates least privilege and would expose the container to the internet.

---

### Question 13 (5 points)

A storage administrator is choosing between LRS, ZRS, GRS, and GZRS for a production financial application that requires protection against both a single datacenter failure and a complete regional disaster, with the lowest possible RPO (Recovery Point Objective). Which redundancy option best meets these requirements?

- A) LRS — three copies in one datacenter, zero RPO within the datacenter
- B) ZRS — copies across three zones, protection against datacenter failures
- C) GRS — copies across two regions, uses LRS in the primary region
- D) GZRS — copies across three zones in the primary region and asynchronously replicated to the secondary region

- **Correct Answer:** D
- **Distractor Analysis:**
  - *Why D is correct:* GZRS provides both zone-level redundancy (ZRS in the primary region — three availability zones) and geo-redundancy (asynchronous replication to a secondary paired region). It protects against single datacenter failures via zone distribution AND against complete regional disasters via geo-replication. For a financial application needing the highest durability and broadest failure coverage, GZRS is the correct choice.
  - *Why A is incorrect:* LRS stores all three copies within a single datacenter in one region. A single datacenter fire, flood, or power failure could destroy all copies. It provides no protection against datacenter-level or regional failures.
  - *Why B is incorrect:* ZRS distributes copies across three zones in one region, protecting against individual datacenter failures. However, a scenario affecting the entire region (large-scale natural disaster, regional Azure outage) would affect all three zones simultaneously. ZRS provides no regional failover protection.
  - *Why C is incorrect:* GRS replicates to a secondary region but uses LRS within the primary region (single datacenter). A datacenter fire in the primary region would cause data loss equal to the replication lag (typically seconds to minutes) until failover. GRS does not provide the zone-level protection that GZRS does within the primary region.

---

### Question 14 (5 points)

An organization stores files in Azure Blob Storage and uses a Shared Access Signature (SAS) to grant read access to a partner. Security auditors discover the SAS token was embedded in a mobile application's source code and exposed in a public GitHub repository. What is the most immediate action to revoke the compromised token?

- A) Delete and recreate the storage account
- B) Rotate the storage account access key that was used to sign the SAS token
- C) Change the storage account name to invalidate the existing SAS URI
- D) Enable Azure Defender for Storage to block the token

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A SAS token is cryptographically signed using either a storage account key or a User Delegation Key. If the SAS was signed with account key1, rotating (regenerating) key1 immediately invalidates all SAS tokens signed with that key — even ones that have not yet reached their expiry time. This is the fastest way to revoke a compromised SAS token.
  - *Why A is incorrect:* Deleting and recreating the storage account is a destructive action that would delete all stored data. This is completely disproportionate to the incident and would cause a major service outage.
  - *Why C is incorrect:* Storage account names cannot be changed after creation. An Azure Storage account name is permanent and tied to the DNS namespace (`[name].blob.core.windows.net`).
  - *Why D is incorrect:* Microsoft Defender for Storage provides threat detection and alerting — it monitors for suspicious activity. It does not have the ability to retroactively block or revoke an existing SAS token that was already issued.

---

### Question 15 (5 points)

Which Azure Storage service stores data as key-attribute pairs (NoSQL), is highly scalable for workloads requiring rapid lookups of structured data by a partition key and row key, and does not support SQL joins or stored procedures?

- A) Azure SQL Database
- B) Azure Table Storage
- C) Azure Queue Storage
- D) Azure Blob Storage

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Table Storage is a NoSQL key-value store that organizes data into tables with partition key and row key as the composite primary key. It is optimized for rapid lookups by these keys, stores structured data without a fixed schema, scales to billions of entities, and does not support SQL joins, foreign keys, or stored procedures.
  - *Why A is incorrect:* Azure SQL Database is a fully relational database service that fully supports SQL joins, stored procedures, and ACID transactions. It is not a key-value store and does not use partition/row key concepts.
  - *Why C is incorrect:* Azure Queue Storage is a message queuing service for asynchronous communication. It stores messages (not structured data entities) and is designed for temporary message passing, not data lookup by key.
  - *Why D is incorrect:* Azure Blob Storage is an object store for unstructured data — files, images, video, backups. It does not have a key-attribute entity model or support structured data queries.

---

### Question 16 (5 points)

A company needs to mount a file share on both Windows Server VMs (which use SMB protocol) and Linux VMs (which use NFS protocol). Which Azure storage service supports both protocols?

- A) Azure Blob Storage with hierarchical namespace enabled
- B) Azure Files
- C) Azure Table Storage
- D) Azure Queue Storage

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Files supports both SMB (Server Message Block) for Windows clients and NFS (Network File System) for Linux clients. Windows VMs can map Azure File shares as drive letters using SMB; Linux VMs mount them via NFS. This makes Azure Files the direct cloud replacement for on-premises network file servers that serve mixed OS environments.
  - *Why A is incorrect:* Azure Blob Storage with hierarchical namespace (Azure Data Lake Storage Gen2) provides a filesystem-like hierarchy for analytics workloads but does not support SMB or NFS mounting for general-purpose file share access. It is accessed via HDFS-compatible API, not as a network drive.
  - *Why C is incorrect:* Azure Table Storage is a NoSQL key-value store. It has no file system semantics and cannot be mounted via SMB or NFS.
  - *Why D is incorrect:* Azure Queue Storage is a message queue service. It has no file system semantics and is not mountable as a network drive.

---

### Question 17 (5 points)

A developer creates a new Azure Storage account and uploads a blob to a private container. Later, they want to verify that the blob cannot be accessed without authentication. Which URL format would return an HTTP 404 or 403 error if the container is private?

- A) `https://[account].blob.core.windows.net/[container]/[blob]` with no SAS token or auth header
- B) `https://[account].blob.core.windows.net/[container]/[blob]?sp=r&sig=[key]` with a valid SAS
- C) `az storage blob download --account-name [account] --container-name [container] --name [blob]` with authenticated CLI
- D) A URL with a valid Authorization header from Entra ID RBAC

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Accessing a blob URL in a private container without any authentication (no SAS token, no Authorization header) returns HTTP 403 (ResourceNotFound or AuthorizationFailure) — the request is rejected. This is the expected behavior for a private container and confirms that anonymous access is blocked.
  - *Why B is incorrect:* A URL with a valid SAS token (`?sp=r&sig=...`) provides read authorization and would successfully return the blob content — HTTP 200. This does not test anonymous access denial.
  - *Why C is incorrect:* `az storage blob download` with an authenticated Azure CLI session uses the user's Entra ID credentials for authorization. An authenticated download would succeed — it does not test anonymous access.
  - *Why D is incorrect:* A valid Authorization header from Entra ID RBAC (with appropriate Storage Blob Data Reader role) would successfully authorize the request and return the blob. This is authenticated access, not anonymous access testing.

---

### Question 18 (5 points)

A company's compliance policy requires that all data written to Azure Storage be encrypted at rest. A security officer asks whether Azure Storage automatically encrypts data. What is the correct response?

- A) Azure Storage encryption at rest is optional and must be enabled per storage account
- B) Azure Storage automatically encrypts all data at rest using 256-bit AES encryption by default, and this cannot be disabled
- C) Azure Storage encrypts only Premium tier storage; Standard tier requires manual encryption configuration
- D) Azure Storage encryption at rest requires the customer to provide their own encryption keys stored on-premises

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Storage Service Encryption (SSE) is enabled by default on all storage accounts — new and existing — and cannot be disabled. All data written to Azure Storage (Blob, Files, Queue, Table) is automatically encrypted at rest using 256-bit AES before being persisted to disk. Decryption is automatic and transparent on reads. No configuration is required.
  - *Why A is incorrect:* SSE is not optional — it is always on. There is no setting to disable at-rest encryption in Azure Storage.
  - *Why C is incorrect:* SSE applies to all Azure Storage tiers — both Standard and Premium. The distinction between Standard and Premium is performance (HDD vs. SSD), not encryption capability.
  - *Why D is incorrect:* By default, Azure manages the encryption keys (Microsoft-managed keys). Customers have the option to provide their own keys using Customer-Managed Keys (CMK) stored in Azure Key Vault, but this is not a requirement. The default (Microsoft-managed) configuration is fully compliant for most regulatory frameworks.

---

### Question 19 (5 points)

An organization uses Azure Files to host a shared departmental drive. Users report that file operations are slow when accessing the share from VMs in a different Azure region. Which Azure Files feature can reduce latency for users in multiple regions without requiring each user to have a direct connection to the primary file share?

- A) Azure Files Sync — synchronize the share to on-premises Windows Server file servers near the users
- B) Azure Files geo-redundancy — use GZRS to automatically serve reads from the nearest region
- C) Azure File Share snapshots — take regular snapshots to create read-only copies in each region
- D) Azure CDN — cache file share content at CDN edge nodes globally

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Azure File Sync synchronizes an Azure file share to one or more Windows Server instances. Servers in different regions (or on-premises locations) can cache the share content locally. Users access the local cache on the Windows Server with LAN-speed latency, while the Azure cloud share remains the authoritative master copy. This is the purpose-built solution for multi-site file share access latency.
  - *Why B is incorrect:* GZRS geo-redundancy replicates data to the secondary region for disaster recovery, but the secondary endpoint is read-only and not directly mountable as a file share by users. GZRS is a durability feature, not a performance/latency feature.
  - *Why C is incorrect:* Azure File Share snapshots are point-in-time backups of a file share. They create read-only snapshots within the same storage account and do not create copies in other regions. Snapshots are a backup and recovery feature, not a latency optimization.
  - *Why D is incorrect:* Azure CDN is designed for HTTP-accessible content (web assets, blobs with public access). Azure Files uses SMB/NFS protocols, which are not compatible with CDN caching. CDN cannot cache or serve SMB file share content.

---

### Question 20 (5 points)

A developer creates an Azure Storage account using the Azure CLI command below. What is missing that would cause blob operations on the account to fail when using object replication or versioning features?

```bash
az storage account create \
  --name "mystoragev2" \
  --resource-group "lab-rg" \
  --location "eastus" \
  --sku "Standard_LRS" \
  --kind "BlobStorage"
```

- A) The `--sku` should be `Standard_GRS` to support versioning
- B) The `--kind` should be `StorageV2` (General Purpose v2) instead of `BlobStorage` to support all blob features
- C) The `--location` must be `westus` for versioning to be supported
- D) A `--enable-versioning true` flag must be added at account creation time

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The `BlobStorage` account kind is a legacy account type (Blob-only storage, also called v1 Blob). Many modern features — including object replication, versioning, lifecycle management, and hierarchical namespace — require a `StorageV2` (General Purpose v2) account. Microsoft recommends creating `StorageV2` accounts for all new workloads.
  - *Why A is incorrect:* The `--sku` (redundancy) setting does not affect whether versioning or object replication is supported. LRS is a valid SKU for accounts that use these features.
  - *Why C is incorrect:* Azure Blob versioning and object replication are available in all Azure regions including `eastus`. Region selection does not affect feature support for these capabilities.
  - *Why D is incorrect:* Blob versioning is not enabled at account creation time with a creation flag — it is configured separately after the account is created (`az storage account blob-service-properties update --enable-versioning true`). The account kind (`StorageV2`) is the prerequisite, not a creation-time flag.
