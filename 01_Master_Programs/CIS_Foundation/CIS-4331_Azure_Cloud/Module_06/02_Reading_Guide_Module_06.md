# Reading Guide: Module 06 - Azure Storage Services

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4331 &BULL; MICROSOFT AZURE CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## Introduction

Azure Storage is the foundational data persistence layer for cloud workloads. Every application deployed in Azure — from a simple web app to a large-scale analytics pipeline — relies on storage services. AZ-900 tests storage concepts thoroughly, particularly Blob Storage service types, redundancy options, and access tiers. This reading guide provides the depth required for both the exam and real-world storage architecture decisions.

---

## Section 1: Azure Storage Account

### 1.1 Storage Account as a Namespace

An Azure Storage Account is the top-level management resource for Azure Storage. Creating a storage account establishes a unique namespace under `[account-name].core.windows.net` that serves as the endpoint for all storage services within that account.

A single storage account can host:

- Blob containers (Blob Storage)
- File shares (Azure Files)
- Queues (Azure Queue Storage)
- Tables (Azure Table Storage)

### 1.2 Storage Account Types

| Account Type | Supported Services | Performance | Use Case |
|---|---|---|---|
| General Purpose v2 (GPv2) | Blobs, Files, Queues, Tables | Standard | Recommended for most scenarios |
| General Purpose v1 (GPv1) | Blobs, Files, Queues, Tables | Standard | Legacy — migrate to GPv2 |
| BlockBlobStorage | Block blobs and append blobs only | Premium (SSD) | High-transaction, low-latency blob workloads |
| FileStorage | File shares only | Premium (SSD) | High-performance file share workloads |
| BlobStorage | Blobs only (block and append) | Standard | Legacy blob-only accounts |

GPv2 is the recommended account type for new deployments. It supports all services and provides access to the latest features including all access tiers.

### 1.3 Storage Account Naming Rules

- 3-24 characters
- Lowercase letters and numbers only
- Must be globally unique across all Azure storage accounts worldwide
- No hyphens or special characters

---

## Section 2: Azure Blob Storage

### 2.1 What Is Blob Storage?

Azure Blob Storage is a massively scalable object storage service for unstructured data. It stores data as blobs (objects) within containers, accessible via HTTP/HTTPS using REST API.

Blobs are organized in containers (analogous to folders, but there is no true folder hierarchy — only flat namespace with `/` delimiter simulating paths).

### 2.2 Blob Types

| Blob Type | Max Size | Optimized For | Use Cases |
|---|---|---|---|
| Block blob | ~190.7 TB | Sequential read/write | Documents, images, video, backups |
| Append blob | ~195 GB | Append-only operations | Log files, audit data, streaming data |
| Page blob | 8 TB | Random read/write | Virtual machine disks (VHDs), database files |

### 2.3 Blob Access Tiers

Access tiers balance storage cost against data access cost. Choose based on how frequently your data is accessed.

| Tier | Storage Cost | Access Cost | Minimum Retention | Retrieval Time | Use Case |
|---|---|---|---|---|---|
| Hot | Highest | Lowest | None | Immediate | Actively accessed data |
| Cool | Lower | Higher | 30 days | Immediate | Monthly access, backups |
| Cold | Very Low | Higher | 90 days | Immediate | Quarterly access |
| Archive | Lowest | Highest | 180 days | 1-15 hours (rehydration) | Regulatory archives, long-term backups |

Early deletion penalty: If data in Cool, Cold, or Archive tier is deleted before the minimum retention period, a prorated early deletion fee applies.

Archive tier behavior: Blobs in Archive tier are stored offline. To read an archived blob, you must first rehydrate it — either move it to Hot or Cool tier, or copy it to a new blob in a higher tier. Standard rehydration priority takes up to 15 hours. High rehydration priority takes under 1 hour (higher cost).

### 2.4 Lifecycle Management Policies

Azure Blob Storage supports lifecycle management policies — rules that automatically transition blobs between tiers or delete them based on age:

Example policy rule: "Move blobs that have not been modified for 30 days from Hot to Cool. Move blobs that have not been modified for 90 days from Cool to Archive. Delete blobs that have not been modified for 365 days."

This automates cost optimization without requiring manual blob management.

### 2.5 Blob Storage Use Cases

- Static website hosting (HTML, CSS, JS files served directly from Blob Storage)
- Video and audio streaming
- Backup and disaster recovery data storage
- Log and telemetry data collection
- Data lake foundation (Azure Data Lake Storage Gen2 is built on Blob Storage)
- VM disk images and snapshots

---

## Section 3: Azure Files

### 3.1 What Is Azure Files?

Azure Files provides fully managed cloud file shares accessible using the industry-standard Server Message Block (SMB) 2.1, 3.0, and 3.1.1 protocols and the NFS 4.1 protocol. Windows, Linux, and macOS clients can mount Azure file shares without any special Azure client software — the share appears as a standard network drive.

### 3.2 Azure Files vs. Blob Storage

| Characteristic | Azure Files | Blob Storage |
|---|---|---|
| Protocol | SMB, NFS | HTTP/HTTPS (REST) |
| Access model | File system (directory/file hierarchy) | Object store (flat namespace) |
| Mount as drive | Yes (like a network drive) | No |
| POSIX compliance | Partial (NFS shares) | No |
| Max file size | 4 TB per file | ~190 TB per block blob |
| Use case | File server replacement, shared app config | Unstructured data at massive scale |

### 3.3 Azure Files Tiers

| Tier | Storage Type | IOPS | Use Case |
|---|---|---|---|
| Premium | SSD | High | Latency-sensitive applications, databases |
| Transaction optimized | HDD | Moderate | High-transaction but latency-tolerant |
| Hot | HDD | Moderate | General-purpose shares accessed frequently |
| Cool | HDD | Lower | Archives, backups with occasional access |

---

## Section 4: Azure Queue Storage

### 4.1 What Is Queue Storage?

Azure Queue Storage is a service for storing large numbers of messages that can be accessed from anywhere via HTTP or HTTPS. A queue can contain millions of messages. Each message can be up to 64 KB. Messages have a configurable visibility timeout — after a consumer retrieves a message, it becomes invisible to other consumers for the timeout period, allowing time to process and delete it.

### 4.2 Queue Storage Use Cases

Queue Storage enables decoupled, asynchronous application architectures:

- **Order processing:** Web frontend writes orders to queue; backend order processor reads queue independently
- **Email notification pipeline:** Application writes notification requests; email service reads and sends
- **Image thumbnail generation:** Upload service writes new image paths; thumbnail generator reads queue and processes
- **Rate limiting:** Control the pace at which messages are consumed regardless of producer speed

### 4.3 Queue Storage vs. Azure Service Bus

| Feature | Queue Storage | Azure Service Bus |
|---|---|---|
| Message size | 64 KB | 256 KB (Standard), 100 MB (Premium) |
| Message ordering | Approximate (not guaranteed) | Guaranteed (FIFO queues) |
| Duplicate detection | No | Yes |
| Dead-letter queue | No | Yes |
| Topics/subscriptions | No | Yes (pub/sub) |
| Cost | Very low | Moderate |
| Best for | Simple decoupling at scale | Enterprise messaging, complex routing |

---

## Section 5: Azure Table Storage

### 5.1 What Is Table Storage?

Azure Table Storage is a NoSQL key-value store for structured, non-relational data. Data is stored as entities (rows) in tables, with each entity identified by a composite key: PartitionKey + RowKey. There is no enforced schema — different entities in the same table can have different sets of properties.

### 5.2 Table Storage Characteristics

- Highly scalable: stores hundreds of terabytes
- Very low cost per GB
- Fast read/write for key-based lookups
- No support for complex queries, joins, or transactions across partitions
- No built-in relationships

### 5.3 When to Use Table Storage vs. Cosmos DB

| Factor | Table Storage | Azure Cosmos DB (Table API) |
|---|---|---|
| Global distribution | No | Yes |
| SLA | 99.9% | 99.99% read, 99.999% write |
| Performance guarantee | Best effort | Guaranteed throughput (RU/s) |
| Cost | Very low | Higher |
| Consistency models | Eventual | 5 consistency models |
| Best for | Simple, low-cost key-value storage | Global, mission-critical NoSQL |

---

## Section 6: Storage Redundancy Options

### 6.1 Redundancy Overview

Azure Storage always keeps multiple copies of your data to protect against hardware failures, datacenter outages, and regional disasters. The redundancy option you select determines how many copies are kept, where they are stored, and the durability guarantee.

### 6.2 Locally Redundant Storage (LRS)

LRS stores three synchronous copies of data within a single physical datacenter in a single Azure region.

- Protects against: single disk failure, server failure, rack failure
- Does not protect against: datacenter-level failure (fire, flood, power grid)
- Durability: 99.999999999% (11 nines) per year
- Cost: Lowest
- Use case: Non-critical data, dev/test, reproducible data, data with regional compliance requirements

### 6.3 Zone-Redundant Storage (ZRS)

ZRS stores three synchronous copies of data, one in each of three Availability Zones within a single region. Each zone has independent power, cooling, and networking.

- Protects against: datacenter failure (zone-level)
- Does not protect against: entire region going offline
- Durability: 99.9999999999% (12 nines) per year
- Cost: Slightly higher than LRS
- Use case: High-availability applications that must remain online during zone failure, regulated workloads requiring regional data residency

### 6.4 Geo-Redundant Storage (GRS)

GRS stores three LRS copies in the primary region plus asynchronously replicates to a secondary (paired) region where three additional LRS copies are stored. Total: six copies.

Secondary region is not readable by default (failover only). With RA-GRS (Read-Access GRS), the secondary region is readable at all times.

- Protects against: regional failure
- Data replication to secondary is asynchronous — small amount of data may be lost during failover (RPO)
- Durability: 99.99999999999999% (16 nines)
- Cost: Higher than ZRS
- Use case: Disaster recovery, business continuity, data that must survive regional failures

### 6.5 Geo-Zone-Redundant Storage (GZRS)

GZRS combines ZRS in the primary region with async replication to a secondary region. It provides both zone-level and regional failure protection.

- Protects against: zone failure AND regional failure
- Durability: Highest available (16 nines)
- Cost: Highest
- RA-GZRS adds read access to secondary region
- Use case: Maximum durability and availability for mission-critical data

### 6.6 Redundancy Comparison Table

| Option | Copies | Primary Region | Secondary Region | Readable Secondary | Durability |
|---|---|---|---|---|---|
| LRS | 3 | 1 datacenter | None | N/A | 11 nines |
| ZRS | 3 | 3 zones | None | N/A | 12 nines |
| GRS | 6 | 1 datacenter (LRS) | 1 datacenter (LRS) | No (RA-GRS: Yes) | 16 nines |
| GZRS | 6 | 3 zones (ZRS) | 1 datacenter (LRS) | No (RA-GZRS: Yes) | 16 nines |

---

## Section 7: Storage Access Control

### 7.1 Storage Account Keys

Two primary access keys (key1 and key2) provide full administrative access to all data in a storage account. Keys should be treated like passwords:

- Store in Azure Key Vault, not in code or configuration files
- Rotate regularly (Azure supports rotating one key while the other remains active)
- Never share with end users — use SAS tokens for delegated access

### 7.2 Shared Access Signatures (SAS)

A Shared Access Signature is a URI that grants restricted access to a storage resource for a defined period. SAS tokens specify:

- Which resources can be accessed (account, service, container, or individual blob)
- What operations are permitted (read, write, delete, list)
- Start and expiry time
- Allowed IP addresses
- Required protocol (HTTPS only recommended)

SAS types:

| Type | Scope | Best For |
|---|---|---|
| Account SAS | Entire storage account | Administrative delegation |
| Service SAS | Single service (blob, file, queue, table) | Service-level access |
| User delegation SAS | Blob or data lake storage, signed with Entra ID credential | Most secure — no account key needed |

### 7.3 Azure AD Authorization (Recommended)

Using Entra ID (Azure AD) for storage access is the recommended approach. Entra ID-based access assigns storage data roles to users, groups, or managed identities:

- Storage Blob Data Reader: Read blobs
- Storage Blob Data Contributor: Read, write, delete blobs
- Storage Blob Data Owner: Full access including POSIX permissions

Managed identities (system-assigned or user-assigned) allow Azure services (VMs, Functions, App Service) to access storage without storing credentials in code.

---

## Section 8: Azure CLI Commands for Storage

```bash
# Create a storage account
az storage account create \
  --name "lab06sa[initials]" \
  --resource-group "lab06-rg" \
  --location "eastus" \
  --sku "Standard_LRS" \
  --kind "StorageV2"

# Show storage account details
az storage account show \
  --name "lab06sa[initials]" \
  --resource-group "lab06-rg"

# Get storage account connection string
az storage account show-connection-string \
  --name "lab06sa[initials]" \
  --resource-group "lab06-rg" \
  --output tsv

# Create a blob container
az storage container create \
  --name "mycontainer" \
  --account-name "lab06sa[initials]" \
  --public-access off

# Upload a blob
az storage blob upload \
  --container-name "mycontainer" \
  --name "example.txt" \
  --file "./example.txt" \
  --account-name "lab06sa[initials]"

# List blobs in a container
az storage blob list \
  --container-name "mycontainer" \
  --account-name "lab06sa[initials]" \
  --output table

# Download a blob
az storage blob download \
  --container-name "mycontainer" \
  --name "example.txt" \
  --file "./downloaded.txt" \
  --account-name "lab06sa[initials]"

# Set blob access tier
az storage blob set-tier \
  --container-name "mycontainer" \
  --name "example.txt" \
  --tier Cool \
  --account-name "lab06sa[initials]"

# Delete a blob
az storage blob delete \
  --container-name "mycontainer" \
  --name "example.txt" \
  --account-name "lab06sa[initials]"
```

Reference: learn.microsoft.com/en-us/cli/azure/storage

---

## Section 9: Storage Services Comparison

| Service | Data Type | Protocol | Max Object Size | Use Case |
|---|---|---|---|---|
| Blob Storage | Unstructured (files, media, backups) | HTTP/HTTPS REST | ~190 TB | Object storage, data lake, CDN origin |
| Azure Files | Structured file system | SMB, NFS | 4 TB per file | File server replacement, shared config |
| Queue Storage | Messages | HTTP/HTTPS | 64 KB per message | Decoupled async messaging |
| Table Storage | Structured NoSQL | HTTP/HTTPS REST | 1 MB per entity | Key-value NoSQL, device telemetry |

---

## Section 10: AZ-900 Exam Tips

1. **Blob type selection:** Block blobs for general file storage (most common). Append blobs for log files (append-only). Page blobs for VM disk images (random I/O). These are three separate things — do not confuse them.

2. **Archive tier retrieval time:** Archive tier data takes 1-15 hours to retrieve (rehydrate). The exam may give a scenario requiring immediate data access and ask which tier is inappropriate — Archive is the answer when immediate access is needed.

3. **GRS vs. ZRS:** GRS replicates to a second region (regional failure protection). ZRS replicates across zones within one region (datacenter failure protection within a region). The geographic scope is the key differentiator.

4. **Azure Files vs. Blob Storage:** Azure Files mounts as a network drive using SMB or NFS. Blob Storage is accessed via HTTP REST API. If a scenario describes "mounting a drive" or "SMB file access," the answer is Azure Files.

5. **SAS token security:** SAS tokens should be time-limited and use HTTPS only. Do not store account keys in application code — use managed identities or Key Vault instead.

6. **Redundancy and cost:** LRS is cheapest but offers no regional protection. GZRS is most expensive but provides the highest durability. For the exam, match the redundancy to the scenario's stated requirement (regional failure protection = GRS or GZRS; zone protection only = ZRS).

7. **Queue Storage for decoupling:** When a scenario describes two application components that need to communicate asynchronously without tight coupling, and one component may be slower than the other, the answer is Queue Storage (or Azure Service Bus for more advanced scenarios).

8. **Cool/Archive early deletion fees:** If data is deleted from Cool tier before 30 days, or Archive tier before 180 days, early deletion fees apply. The exam may test awareness of this cost consideration.

---

## Section 11: Required Resources

- Azure Storage introduction: learn.microsoft.com/en-us/azure/storage/common/storage-introduction
- Blob Storage overview: learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
- Storage redundancy: learn.microsoft.com/en-us/azure/storage/common/storage-redundancy
- Azure Files: learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction
- Microsoft Learn AZ-900 storage module: learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/

---

## Section 12: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the blob access tier table (Section 2.3)
- [ ] Memorize the redundancy comparison table (Section 6.6)
- [ ] Know the four storage service types and one use case for each
- [ ] Understand all CLI commands in Section 8
- [ ] Complete Lab Activity Module 06
- [ ] Take Quiz Module 06
- [ ] Post Discussion Module 06 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure Blob Storage documentation**
https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
Complete reference for Blob Storage including blob types (Block, Append, Page), access tiers (Hot/Cool/Cold/Archive), lifecycle management policies, versioning, and object replication.

**2. Microsoft Learn — Azure Storage redundancy**
https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy
Detailed explanation of all redundancy options (LRS, ZRS, GRS, RA-GRS, GZRS, RA-GZRS) with durability percentages, replication mechanics, and guidance for choosing the right redundancy for each workload.

**3. Microsoft Learn — Grant limited access to Azure Storage resources using SAS**
https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview
Covers the three types of SAS tokens (Account SAS, Service SAS, User Delegation SAS), SAS signing keys, permissions scope, expiry configuration, and security best practices for temporary delegated access.
