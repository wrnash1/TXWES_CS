# Reading Guide: Module 09 — Azure Storage

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

---

## Introduction

Azure Storage is a managed cloud storage service that provides scalable, durable, and highly available storage for any type of data. It is the foundational storage layer for Azure applications, Azure VMs, and many Azure services. AZ-900 tests your ability to identify the correct storage service type and redundancy option for a given scenario. This guide covers storage accounts, Blob Storage tiers, Azure Files, Queue Storage, Table Storage, redundancy options, and Azure Data Box.

---

## Section 1: Azure Storage Accounts

### 1.1 Storage Account Overview

A storage account is the top-level Azure resource that contains all Azure Storage services. It provides a unique namespace for storage — every object in your storage account has an address that includes the account name.

URL format: `https://<accountname>.blob.core.windows.net/<container>/<blob>`

### 1.2 Storage Account Types

| Account Type | Supported Services | Performance | Use Case |
|---|---|---|---|
| General-purpose v2 (GPv2) | Blob, Files, Queue, Table | Standard (HDD) | Recommended default for most workloads |
| General-purpose v1 (GPv1) | Blob, Files, Queue, Table | Standard (HDD) | Legacy; upgrade to GPv2 |
| Premium Block Blobs | Block blobs and append blobs only | Premium (SSD) | High-transaction, low-latency blob operations |
| Premium File Shares | Azure Files only | Premium (SSD) | High-IOPS file share workloads |
| Premium Page Blobs | Page blobs only | Premium (SSD) | Unmanaged VM disks |

### 1.3 Storage Account Security Defaults

Every Azure Storage account includes:

- **Encryption at rest:** 256-bit AES encryption, enabled by default, cannot be disabled
- **Encryption in transit:** HTTPS enforced by default (HTTP can be allowed but not recommended)
- **Azure Active Directory integration:** Azure RBAC for data plane access
- **Shared Access Signatures (SAS):** Time-limited, permission-limited access tokens
- **Storage firewalls:** Restrict access to specific IP ranges or VNets

---

## Section 2: Azure Blob Storage

### 2.1 Blob Storage Overview

Azure Blob Storage is object storage for unstructured data. Objects are stored as blobs inside containers (similar to folders).

Blob Storage hierarchy:

- Storage Account → Containers → Blobs

### 2.2 Blob Types

| Blob Type | Structure | Max Size | Best For |
|---|---|---|---|
| Block blob | 50,000 blocks of up to 4,000 MB each | ~190 TB | Files, images, video, documents |
| Append blob | Blocks added only to end | ~195 GB | Log files, streaming data |
| Page blob | 512-byte pages, random read/write | 8 TB | VM disks (VHD format) |

### 2.3 Blob Access Tiers

Access tiers optimize the cost-performance tradeoff based on how often data is accessed.

| Tier | Access Frequency | Storage Cost | Access Cost | Minimum Duration | Retrieval Time |
|---|---|---|---|---|---|
| Hot | Frequent | Highest | Lowest | None | Immediate |
| Cool | Infrequent (30-day minimum) | Medium | Medium | 30 days | Immediate |
| Archive | Rare (180-day minimum) | Lowest | Highest | 180 days | Hours (rehydration required) |

**Key rule for AZ-900:** Storage cost decreases from Hot → Cool → Archive. Access cost increases from Hot → Cool → Archive.

**Early deletion penalties:**

- Cool tier: If a blob is deleted or moved out of Cool before 30 days, a prorated early deletion fee applies
- Archive tier: If a blob is deleted or moved out of Archive before 180 days, a prorated early deletion fee applies

### 2.4 Archive Tier Rehydration

Data stored in the Archive tier is offline. Before it can be read, it must be rehydrated — moved to Hot or Cool tier. Two rehydration options:

| Option | Speed | Cost |
|---|---|---|
| Standard rehydration | Up to 15 hours | Lower |
| High-priority rehydration | Under 1 hour for objects under 10 GB | Higher |

### 2.5 Blob Lifecycle Management

Lifecycle Management policies automate tier transitions and deletion based on rules.

Example policy:

```json
{
  "rules": [
    {
      "name": "hot-to-cool",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 90 },
            "delete": { "daysAfterModificationGreaterThan": 365 }
          }
        },
        "filters": {
          "blobTypes": ["blockBlob"]
        }
      }
    }
  ]
}
```

### 2.6 Blob Storage Access Levels

Containers have a public access level that controls anonymous read access:

| Access Level | Description |
|---|---|
| Private (no public access) | Only authenticated requests can access blobs |
| Blob (anonymous read for blobs) | Anyone with the blob URL can read the blob |
| Container (anonymous read for container and blobs) | Anyone can list the container and read all blobs |

---

## Section 3: Azure Files

### 3.1 Overview

Azure Files provides fully managed cloud file shares accessible via SMB (Server Message Block) 2.1/3.0 or NFS 4.1 protocols. Azure file shares can be mounted concurrently from Windows, Linux, and macOS clients.

### 3.2 Azure Files vs. Blob Storage

| Factor | Azure Files | Azure Blob Storage |
|---|---|---|
| Data model | File system (hierarchical) | Object store (flat namespace) |
| Protocol | SMB, NFS | HTTP/HTTPS REST API |
| Use case | Replace file server, shared config | Unstructured data, backups, static assets |
| Mount as drive | Yes (SMB) | No |
| Application compat | Drop-in for SMB file server | Requires code changes |

### 3.3 Azure File Sync

Azure File Sync synchronizes on-premises Windows Server directories with Azure Files. Enables hybrid deployment:

- On-premises servers retain frequently accessed files (cloud tiering)
- Full dataset always stored in Azure (cloud backup)
- Multi-site access: multiple offices sync the same Azure file share

---

## Section 4: Azure Queue Storage

### 4.1 Overview

Azure Queue Storage is a messaging service for storing large numbers of messages. Each message can be up to 64 KB. A single queue can store millions of messages.

### 4.2 Messaging Pattern

Queue Storage enables asynchronous, decoupled architectures:

1. **Producer** adds a message to the queue (e.g., "Process order #1234")
2. Queue stores message durably
3. **Consumer** polls the queue, reads the message, processes it
4. Consumer deletes the message upon successful processing
5. If consumer fails, the message becomes visible again after a visibility timeout

### 4.3 Queue Storage vs. Azure Service Bus

| Feature | Azure Queue Storage | Azure Service Bus |
|---|---|---|
| Message size | Up to 64 KB | Up to 256 KB (Standard) or 100 MB (Premium) |
| Message ordering | FIFO (not guaranteed) | Guaranteed FIFO (sessions) |
| Dead-letter queue | No | Yes |
| Topics/subscriptions | No | Yes |
| Cost | Lowest | Higher |
| Use case | Simple decoupling, basic queuing | Enterprise messaging, guaranteed delivery |

---

## Section 5: Azure Table Storage

### 5.1 Overview

Azure Table Storage is a NoSQL key-value store for semi-structured data. It stores entities (rows) with properties (columns). Unlike relational databases, entities in the same table can have different sets of properties.

### 5.2 Table Storage Structure

| Concept | Description |
|---|---|
| Table | A collection of entities |
| Entity | A row; has a PartitionKey, RowKey, and timestamp |
| PartitionKey | Groups entities for scalability and performance |
| RowKey | Unique identifier within a partition |
| Property | Name-value pair; up to 255 properties per entity |

### 5.3 Table Storage vs. Cosmos DB Table API

| Factor | Azure Table Storage | Cosmos DB Table API |
|---|---|---|
| Global distribution | No | Yes |
| SLA | 99.9% | 99.99% (multi-region 99.999%) |
| Consistency levels | Eventual only | Configurable (5 levels) |
| Throughput | Shared, unpredictable | Provisioned or serverless |
| Cost | Very low | Higher |
| Migration | Minimal code change | Drop-in compatible |

---

## Section 6: Storage Redundancy Options

### 6.1 Redundancy Overview

Azure Storage replicates data to protect against hardware failure, datacenter outage, and regional disaster. You choose the redundancy level when creating a storage account.

### 6.2 LRS — Locally Redundant Storage

Three synchronous copies within a single physical datacenter in the primary region.

| Property | Detail |
|---|---|
| Copies | 3 |
| Location | Single datacenter, single region |
| Protects against | Disk failure, server failure |
| Does NOT protect against | Datacenter failure, regional disaster |
| Durability | 99.999999999% (11 nines) |
| Cost | Lowest |
| Best for | Dev/test, non-critical data, data that can be recreated |

### 6.3 ZRS — Zone-Redundant Storage

Three synchronous copies, one in each of three Availability Zones in the primary region.

| Property | Detail |
|---|---|
| Copies | 3 |
| Location | Three Availability Zones, single region |
| Protects against | Datacenter failure, zone-level failure |
| Does NOT protect against | Regional disaster |
| Durability | 99.9999999999% (12 nines) |
| Cost | Medium |
| Best for | Production data with high availability within a region |

### 6.4 GRS — Geo-Redundant Storage

Six copies total: 3 in primary region (LRS-style) + 3 in secondary region (asynchronous replication).

| Property | Detail |
|---|---|
| Copies | 6 (3 primary + 3 secondary) |
| Location | Primary region + paired secondary region |
| Protects against | Datacenter failure + regional disaster |
| Secondary readable | No (unless RA-GRS) |
| Durability | 99.99999999999999% (16 nines) |
| Cost | Higher |
| Best for | Data requiring geo-redundancy and disaster recovery |

**RA-GRS (Read-Access GRS):** Secondary region is available for read-only access. Provides a secondary endpoint: `https://<account>-secondary.blob.core.windows.net`.

### 6.5 GZRS — Geo-Zone-Redundant Storage

Combines ZRS in the primary region with asynchronous geo-replication to a secondary region.

| Property | Detail |
|---|---|
| Copies | 6 (3 across zones in primary + 3 in secondary) |
| Location | Three zones in primary + secondary region |
| Protects against | Zone failure AND regional disaster |
| Secondary readable | No (unless RA-GZRS) |
| Durability | 99.99999999999999% (16 nines) |
| Cost | Highest |
| Best for | Mission-critical data requiring maximum resiliency |

### 6.6 Redundancy Summary Table

| Option | Copies | Zone Failure | Region Failure | Relative Cost | AZ-900 Signal |
|---|---|---|---|---|---|
| LRS | 3 | No | No | $ | Dev/test, non-critical |
| ZRS | 3 | Yes | No | $$ | Production, zone-tolerant |
| GRS | 6 | No | Yes | $$$ | Geo-redundancy, DR |
| GZRS | 6 | Yes | Yes | $$$$ | Maximum resiliency |

---

## Section 7: Azure Data Box

### 7.1 When to Use Data Box

Data transfer over the internet becomes impractical at large scales. Data Box provides physical data transfer for offline migration.

Rule of thumb: if transferring data over a 100 Mbps connection would take more than 7 days, consider Data Box.

At 100 Mbps: 1 TB takes approximately 22 hours. 100 TB takes approximately 90 days.

### 7.2 Data Box Product Family

| Product | Capacity | Form Factor | Use Case |
|---|---|---|---|
| Data Box Disk | Up to 40 TB (5 disks × 8 TB) | Portable SSD | Small-to-medium migrations |
| Data Box | Up to 100 TB usable | Ruggedized appliance (50 lbs) | Standard large migrations |
| Data Box Heavy | Up to 1 PB usable | Wheeled ruggedized enclosure | Massive dataset migrations |

All Data Box devices use AES-256-bit encryption. The device is wiped after Microsoft receives it and uploads the data.

### 7.3 AZ-900 Signal for Data Box

Scenario keywords that indicate Data Box:

- "Terabytes or petabytes of data to migrate"
- "Limited bandwidth"
- "Too slow to upload over the internet"
- "Offline data transfer"
- "Physical device"

---

## Section 8: Azure CLI Reference

```bash
# Create a storage account
az storage account create \
  --name labstorage09 \
  --resource-group lab09-rg \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2 \
  --access-tier Hot

# Create a blob container
az storage container create \
  --name labcontainer \
  --account-name labstorage09 \
  --public-access off

# Upload a blob
az storage blob upload \
  --account-name labstorage09 \
  --container-name labcontainer \
  --name sample.txt \
  --file ./sample.txt

# List blobs in a container
az storage blob list \
  --account-name labstorage09 \
  --container-name labcontainer \
  --output table

# Set blob access tier
az storage blob set-tier \
  --account-name labstorage09 \
  --container-name labcontainer \
  --name sample.txt \
  --tier Cool

# Show storage account details
az storage account show \
  --name labstorage09 \
  --resource-group lab09-rg

# Create an Azure file share
az storage share create \
  --name labfileshare \
  --account-name labstorage09 \
  --quota 5
```

---

## Section 9: AZ-900 Exam Tips

1. **Blob access tier decision:** Hot = frequently accessed, lowest access cost. Cool = infrequently accessed (30-day minimum). Archive = rarely accessed (180-day minimum), must rehydrate before reading. The key pattern: lower storage cost = higher access cost.

2. **Archive rehydration:** Data in the Archive tier cannot be read immediately — it must be rehydrated to Hot or Cool tier first. Standard rehydration takes up to 15 hours. High-priority takes under 1 hour for small objects.

3. **Redundancy scope:** LRS stays in one datacenter. ZRS spans three datacenters in one region. GRS and GZRS span two regions. If the exam says "protect against regional disaster," the answer must be GRS or GZRS.

4. **GRS secondary is read-only by default:** With GRS, the secondary region copy is not readable unless you choose RA-GRS. If a scenario mentions read access from a secondary region, RA-GRS is the answer.

5. **Data Box for large offline migrations:** If a scenario describes terabytes of data and limited internet bandwidth, Azure Data Box is the answer. Do not confuse with Azure Import/Export (legacy job-based service).

6. **Azure Files for SMB:** If a scenario says "mount as a network drive" or "replace a Windows file server," the answer is Azure Files. Blob Storage cannot be mounted as a drive natively.

7. **Queue Storage for decoupling:** If a scenario describes async message passing between application components (producer/consumer), the answer is Azure Queue Storage.

8. **Table Storage is NoSQL:** Azure Table Storage is a NoSQL key-value store. Do not confuse with relational databases. If a scenario needs flexible schema and simple key-value access without global distribution, Table Storage is a cost-effective option.

---

## Section 10: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the blob access tier table (Section 2.3)
- [ ] Memorize the redundancy summary table (Section 6.6)
- [ ] Understand Archive tier rehydration (Section 2.4)
- [ ] Know the Data Box product family (Section 7.2)
- [ ] Complete the Microsoft Learn "Describe Azure storage services" module
- [ ] Complete Lab Module 09
- [ ] Take Quiz Module 09
- [ ] Post Discussion Module 09 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure Blob Storage access tiers**
https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview
Deep dive into Hot, Cool, Cold, and Archive tier pricing models, rehydration options (standard vs. high priority), early deletion fees, and lifecycle management policy configuration — the most-tested storage topic on AZ-900.

**2. Microsoft Learn — Blob Storage lifecycle management**
https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview
Covers the policy JSON schema, rule conditions (daysAfterCreationGreaterThan, daysAfterLastAccessTimeGreaterThan), tier transition and delete actions, and access time tracking configuration required for access-based policies.

**3. Microsoft Learn — Azure Data Box documentation**
https://learn.microsoft.com/en-us/azure/databox/data-box-overview
Overview of the Data Box product family (Data Box Disk, Data Box, Data Box Heavy), capacity options, the end-to-end import workflow, security (NIST 800-88 wipe), and guidance for choosing between Data Box and online transfer methods.

---

## Required Reading Resources

- Azure Storage overview: learn.microsoft.com/en-us/azure/storage/common/storage-introduction
- Blob Storage overview: learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
- Azure Storage redundancy: learn.microsoft.com/en-us/azure/storage/common/storage-redundancy
- Azure Files overview: learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction
- Azure Data Box: learn.microsoft.com/en-us/azure/databox/data-box-overview
- Microsoft Learn AZ-900 storage module: learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/
