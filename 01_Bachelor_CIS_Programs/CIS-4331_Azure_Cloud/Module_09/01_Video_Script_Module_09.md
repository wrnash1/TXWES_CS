# Video Script: Module 09 — Azure Storage

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure Fundamentals (AZ-900)

---

## Opening (0:00–1:00)

Welcome to Module 09 of CIS-4331 Azure Cloud Computing. I'm Professor Nash. Today we are covering Azure Storage — Microsoft's cloud storage platform that underpins almost every Azure service and application.

Storage is one of the most thoroughly tested areas on the AZ-900 exam. You will need to understand the different storage service types, the access tiers for Blob storage, storage account redundancy options, and the specialized data transfer tool Azure Data Box. By the end of this module, you will be able to select the right storage service and redundancy configuration for any scenario.

Let's get started.

---

## Section 1: Azure Storage Accounts (1:00–3:30)

### What Is a Storage Account?

An Azure Storage Account is the top-level container for all Azure Storage services. Every Azure Storage resource — blobs, files, queues, and tables — lives inside a storage account. The storage account defines:

- The storage performance tier (Standard or Premium)
- The redundancy option (LRS, ZRS, GRS, or GZRS)
- The geographic region
- The network access settings

All data in a storage account is encrypted at rest using 256-bit AES encryption. This is automatic and cannot be disabled.

### Storage Account Types

Azure offers three storage account types.

**General-purpose v2 (GPv2)** — The most common and recommended type. Supports all storage services (Blob, Files, Queue, Table) and all access tiers (Hot, Cool, Archive). Use this for most new deployments.

**Premium Block Blobs** — For block blob workloads requiring low latency and high transaction rates. Backed by SSD storage. Does not support GPv2's tiering features.

**Premium File Shares** — For Azure Files workloads requiring high IOPS. Backed by SSD storage.

[SHOW AZURE PORTAL] Navigate to Storage Accounts > Create. Walk through the Basics tab. Show the Redundancy dropdown. Show the Advanced tab options — hierarchical namespace (enables Azure Data Lake Storage Gen2).

---

## Section 2: Azure Blob Storage (3:30–9:00)

### What Is Blob Storage?

Azure Blob Storage is Microsoft's object storage solution. It is designed for storing unstructured data — data that does not fit into a relational model. Common examples include:

- Images, videos, and audio files
- Log files and diagnostic data
- Backup and archive files
- Static website assets (HTML, CSS, JavaScript)
- Data files for analytics pipelines

Blob stands for Binary Large Object. Data is stored as blobs inside containers, and containers are inside storage accounts.

### Blob Types

There are three blob types.

**Block blobs** — Made of blocks. Used for text and binary files like images, video, and documents. The most common type. Supports up to approximately 190 TB.

**Append blobs** — Optimized for append operations. Used for log files where data is continuously written to the end of the file but never modified in the middle.

**Page blobs** — Optimized for random read/write operations. Used as the backing storage for Azure VM disks (VHD files).

### Blob Access Tiers

This is one of the most heavily tested AZ-900 topics. Blob Storage has three access tiers that trade cost against access frequency.

**Hot tier** — For data accessed frequently. Lowest access cost, highest storage cost. Examples: active website images, recently uploaded documents, files accessed daily.

**Cool tier** — For data accessed infrequently, stored for at least 30 days. Lower storage cost than Hot, higher access cost. Examples: short-term backups, monthly reports, data accessed occasionally.

**Archive tier** — For data rarely accessed, stored for at least 180 days. Lowest storage cost of all three tiers. Very high access cost. Data in Archive is offline and must be "rehydrated" before it can be read — this can take hours.

The key rule for the exam: as you move from Hot to Cool to Archive, storage cost decreases and access cost increases.

[SHOW AZURE PORTAL] Navigate to a storage account > Containers > Show a blob's Properties tab. Show the Access Tier field. Show how to change a blob's tier manually. Navigate to Lifecycle Management to show automated tier transitions.

### Lifecycle Management Policies

You can automate tier transitions and deletion using Lifecycle Management policies. For example, a policy might say:

- Move blobs not accessed in 30 days from Hot to Cool
- Move blobs not accessed in 90 days from Cool to Archive
- Delete blobs after 365 days

This allows cost optimization without manual management.

---

## Section 3: Azure Files (9:00–11:30)

### What Is Azure Files?

Azure Files provides fully managed cloud file shares that you can mount using the Server Message Block (SMB) protocol or Network File System (NFS) protocol. This is the cloud equivalent of a traditional file server.

Key use cases for Azure Files:

- Lift-and-shift applications that use a file share for shared configuration or data
- Replacing on-premises file servers
- Developer tools and settings that need to be shared across multiple VMs
- Diagnostic data, crash dumps, and log files shared across a cluster

The big advantage of Azure Files over Blob Storage for file-sharing scenarios is the protocol support. SMB is the native Windows file sharing protocol. Applications that already use SMB network drives require zero code changes to use Azure Files.

[SHOW AZURE PORTAL] Navigate to Storage Account > File Shares > Create a new share. Show the quota setting. Show the Connect button that provides the PowerShell and Linux mount commands.

### Azure File Sync

Azure File Sync is a service that synchronizes on-premises Windows Server file shares with Azure Files, enabling hybrid access. You can have a local cached copy on-premises and a full copy in Azure. This is particularly useful for offices that want low-latency local access and cloud backup.

---

## Section 4: Queue Storage and Table Storage (11:30–14:00)

### Azure Queue Storage

Azure Queue Storage provides reliable, asynchronous message-based communication between application components. A queue stores messages up to 64 KB in size. Messages remain in the queue until a consumer reads and processes them.

Queue Storage enables decoupled architectures: a producer adds a message when a task needs to be done, and a consumer picks up the message when it is ready to process it. This prevents data loss if the consumer is temporarily unavailable.

Example: An e-commerce web front end adds an order message to a queue. A background worker reads the queue and processes payment and fulfillment. The web front end does not wait for the worker — it responds immediately to the customer.

### Azure Table Storage

Azure Table Storage is a NoSQL key-value store for semi-structured data. It stores data as entities (rows) with properties (columns). Each entity can have different properties — there is no fixed schema.

Table Storage is a cost-effective option for large volumes of semi-structured data that does not require relational joins or complex queries. For example: log data, user profile data, device inventory.

Note for AZ-900: Azure Cosmos DB's Table API is compatible with Azure Table Storage. If you need global distribution or SLA guarantees beyond Table Storage, migrating to Cosmos DB Table API requires minimal code changes.

---

## Section 5: Storage Redundancy Options (14:00–18:00)

### Why Redundancy Matters

Azure replicates your data to protect against hardware failure, datacenter outages, and regional disasters. The level of redundancy you choose determines your cost, your recovery capabilities, and your SLA.

There are four redundancy options. This is extremely heavily tested on AZ-900.

### LRS — Locally Redundant Storage

LRS makes 3 copies of your data within a single datacenter in a single region. This protects against disk failure and server failure within the datacenter, but if the entire datacenter goes down, data could be lost.

SLA: 99.999999999% (11 nines) object durability.

Cost: Lowest. Use for: dev/test, non-critical data, data that can be easily recreated.

### ZRS — Zone-Redundant Storage

ZRS makes 3 copies of your data, one in each Availability Zone in a region. This protects against datacenter failure. If one zone goes down, your data is still accessible from the other zones.

SLA: 99.9999999999% (12 nines) object durability.

Cost: Slightly higher than LRS. Use for: production data requiring high availability within a region.

### GRS — Geo-Redundant Storage

GRS makes 3 copies in the primary region (using LRS) and asynchronously replicates to a secondary region hundreds of miles away. The secondary region data is NOT readable by default — it is only available if Microsoft initiates a regional failover.

SLA: 99.99999999999999% (16 nines) object durability.

Cost: Higher. Use for: data that needs geo-redundancy and recovery from regional disasters.

**RA-GRS (Read-Access GRS):** A variant of GRS where the secondary region IS readable for read workloads.

### GZRS — Geo-Zone-Redundant Storage

GZRS combines ZRS in the primary region (3 zones) with geo-replication to a secondary region. This provides protection against both zone-level failures in the primary region and complete regional outages.

SLA: 99.99999999999999% (16 nines) object durability.

Cost: Highest. Use for: mission-critical data requiring maximum resiliency.

**RA-GZRS:** Read-access GZRS where the secondary is also readable.

[SHOW AZURE PORTAL] Navigate to Storage Account > Configuration. Show the Redundancy dropdown with all four options. Show the primary and secondary region display for GRS/GZRS.

---

## Section 6: Azure Data Box (18:00–20:00)

### The Data Transfer Challenge

What if you need to migrate 50 terabytes of data to Azure? Uploading 50 TB over the internet at 100 Mbps would take approximately 46 days. That is not practical.

Azure Data Box is Microsoft's solution for physically transferring large datasets to or from Azure when network transfer is not practical due to time, bandwidth, or cost constraints.

Azure Data Box is a rugged, secure hardware device that Microsoft ships to you. You copy your data onto the device, ship it back to Microsoft, and they upload it to your Azure Storage account. The entire device is encrypted.

Data Box product family:

**Data Box Disk** — Up to 8 TB per disk (up to 5 disks = 40 TB). Portable SSD.

**Data Box** — Up to 100 TB. The standard device for most large migrations.

**Data Box Heavy** — Up to 1 PB. For massive dataset migrations — multiple hard drive bays in a ruggedized enclosure.

The exam rule: if a scenario mentions terabytes or petabytes of data and "limited bandwidth" or "too slow to transfer over the internet," Azure Data Box is the answer.

---

## Closing (20:00–21:00)

Today we covered the full Azure Storage portfolio. We walked through storage account types, Blob Storage with Hot/Cool/Archive tiers and lifecycle management, Azure Files for SMB file shares, Queue Storage for decoupled messaging, and Table Storage for NoSQL key-value data. We covered the four redundancy options — LRS, ZRS, GRS, and GZRS — and their SLA and cost tradeoffs. And we introduced Azure Data Box for physical large-scale data transfer.

In your lab this week, you will create a storage account, upload blobs to different tiers, and configure lifecycle management. These are tasks you will perform repeatedly in real Azure environments.

In Module 10, we move to Azure Databases. See you there.

---

*End of Script — Module 09*
