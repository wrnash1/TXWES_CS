# Video Script: Module 06 - Azure Storage Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 06: Azure Storage Services"]**

Welcome to Module 06. I'm Professor Nash. Today we cover Azure Storage Services — the foundation for data persistence in the cloud. Every application we have discussed so far — VMs, containers, App Service — needs to store data somewhere. Azure Storage provides that somewhere in multiple forms, each optimized for different data types and access patterns.

AZ-900 expects you to recognize each storage service, understand its use case, and know how redundancy options affect durability and cost.

By the end of this module you will be able to:

- Describe the four Azure Storage service types: Blob, Files, Queue, and Table
- Select the appropriate storage service for a given scenario
- Explain Azure Storage redundancy options and their trade-offs
- Describe storage account tiers and access tiers
- Use Azure CLI to create storage accounts and work with blobs

---

## [01:30 - 05:30] Azure Storage Account Overview

**[SLIDE: "Azure Storage Account"]**

An Azure Storage Account is the container for all Azure Storage services. When you create a storage account, you are creating an endpoint that can host Blob Storage, File Shares, Queues, and Tables simultaneously. Each storage account gets a unique namespace: `https://[account-name].blob.core.windows.net`, `https://[account-name].file.core.windows.net`, and so on.

Storage account settings you configure at creation:

**Account kind:** General Purpose v2 (GPv2) is the standard, recommended for most scenarios. It supports all storage services. Blob Storage accounts are specialized for blobs only. Premium accounts use SSD-backed storage for low-latency workloads.

**Redundancy:** How many copies of your data Azure keeps and where. This is one of the most AZ-900-tested storage topics — we will cover it in depth shortly.

**Access tier:** Applies to Blob Storage. Hot tier for frequently accessed data, Cool tier for infrequently accessed data, Archive tier for rarely accessed data that can tolerate hours of retrieval latency.

**[SHOW PORTAL — Navigate to portal.azure.com, create storage account blade]**

When you create a storage account in the Portal, notice that the redundancy options appear prominently — this is because they significantly impact both cost and durability.

---

## [05:30 - 11:00] Azure Storage Service Types

**[SLIDE: "Blob Storage — Unstructured Data at Scale"]**

**Azure Blob Storage** is the most important and most-tested Azure Storage service. Blob stands for Binary Large Object. Blob Storage is designed for storing massive amounts of unstructured data — documents, images, videos, backups, log files, virtual machine disk images, and static website content.

Blob types:

**Block blobs** store text and binary data up to approximately 190 TB per blob. They are the most common type and ideal for most file storage scenarios.

**Append blobs** are optimized for append operations. Each append adds a new block at the end. Ideal for log files — you can append new log entries without rewriting existing data.

**Page blobs** are random-access files optimized for frequent read/write operations. Azure Managed Disks are built on page blobs behind the scenes.

**Blob access tiers:**

Hot: Highest storage cost, lowest access cost. For data accessed daily.

Cool: Lower storage cost, higher access cost, minimum 30-day retention. For data accessed occasionally.

Cold: Very low storage cost, higher access cost, minimum 90-day retention. Newer tier between Cool and Archive.

Archive: Lowest storage cost, highest retrieval cost, minimum 180-day retention. Data is offline — retrieval takes hours. For regulatory archives and rarely accessed backups.

**[SLIDE: "Azure Files — Managed File Shares"]**

**Azure Files** provides fully managed file shares in the cloud, accessible using the standard SMB (Server Message Block) or NFS (Network File System) protocols. This means you can mount an Azure File Share on Windows, Linux, and macOS — exactly like a network drive — without any special Azure client software.

Use cases:

- Lift-and-shift migration for applications that use network file shares
- Replacing on-premises file servers
- Shared configuration files for multiple VMs
- Diagnostic data that must be accessible from multiple locations

**[SLIDE: "Azure Queue Storage — Message Queuing"]**

**Azure Queue Storage** stores large numbers of messages that can be accessed from anywhere in the world via HTTP or HTTPS. A single queue can contain millions of messages, and each message can be up to 64 KB in size.

Queue Storage enables decoupled, asynchronous communication between application components. Instead of Service A directly calling Service B (tight coupling that fails if B is slow), Service A writes a message to the queue. Service B reads and processes messages from the queue at its own pace.

Use case example: An e-commerce order processing system. When a customer places an order, the web frontend writes an order message to a queue. The order processing backend reads from the queue and processes orders. If the backend is slow or temporarily down, orders queue up safely and are processed when the backend recovers — no orders are lost.

**[SLIDE: "Azure Table Storage — NoSQL Key-Value Data"]**

**Azure Table Storage** is a NoSQL key-attribute store for structured, non-relational data. It stores data in tables as collections of entities (rows), each identified by a partition key and row key. It is schema-less — different entities in the same table can have different properties.

Use cases:

- Web application user data
- Device telemetry data
- Metadata for other Azure services
- Any scenario requiring flexible, schema-free structured data at low cost

Note: Azure Cosmos DB for Table API is the premium, globally distributed successor to Table Storage. AZ-900 covers both — Table Storage as part of Azure Storage, Cosmos DB as a separate database service (Module 07).

---

## [11:00 - 16:00] Storage Redundancy Options

**[SLIDE: "Azure Storage Redundancy — Critical AZ-900 Topic"]**

Storage redundancy is how Azure protects your data from hardware failure, datacenter outage, or regional disaster. Azure makes multiple copies of your data — how many and where depends on the redundancy option you choose.

**[SLIDE: "Locally Redundant Storage (LRS)"]**

**LRS** stores three copies of your data within a single datacenter in a single region. If the datacenter loses power or the physical storage hardware fails, LRS protects you. If the entire datacenter burns down, LRS data may be lost.

Cost: Lowest. Durability: 99.999999999% (11 nines) per year.

Best for: Non-critical data, reproducible data, data that can tolerate regional loss.

**[SLIDE: "Zone-Redundant Storage (ZRS)"]**

**ZRS** stores three copies of your data across three Availability Zones within a single region. If one datacenter (zone) fails completely, ZRS data remains accessible from the other two zones.

Cost: Slightly higher than LRS. Durability: 99.9999999999% (12 nines).

Best for: High availability requirements within a region, regulated workloads that must remain in the same region.

**[SLIDE: "Geo-Redundant Storage (GRS)"]**

**GRS** combines LRS in the primary region with asynchronous replication to a secondary region (the paired region). Six total copies: three in the primary region, three in the secondary region.

By default, the secondary region copy is not readable — it is only for failover. If you need to read from the secondary region, use Read-Access Geo-Redundant Storage (RA-GRS).

Cost: Higher. Durability: 99.99999999999999% (16 nines).

Best for: Business continuity, disaster recovery, data that must survive a regional failure.

**[SLIDE: "Geo-Zone-Redundant Storage (GZRS)"]**

**GZRS** combines ZRS in the primary region with async replication to a secondary region. This provides the highest combination of availability (zone redundancy locally) and durability (geo-replication for regional failure).

Cost: Highest.

Best for: Maximum durability and availability requirements.

**[SLIDE: "Redundancy Comparison Table"]**

| Option | Copies | Protection Against | Readable Secondary | Cost |
|---|---|---|---|---|
| LRS | 3 (1 datacenter) | Hardware failure | N/A | Lowest |
| ZRS | 3 (3 zones, 1 region) | Datacenter failure | N/A | Low-Medium |
| GRS | 6 (3+3 across regions) | Regional failure | No (RA-GRS adds reads) | Medium-High |
| GZRS | 6 (zone+geo) | Zone + Regional failure | No (RA-GZRS adds reads) | Highest |

---

## [16:00 - 19:00] Storage Access and Security

**[SLIDE: "Storage Access Methods"]**

Azure Storage provides multiple ways to control access:

**Storage Account Key:** Two primary access keys that grant full access to all data in the account. Like a root password — should never be shared with end users. Rotate periodically.

**Shared Access Signature (SAS):** A URL that grants limited, time-bounded access to specific storage resources. You can restrict the operations allowed (read only, write only), the IP addresses that can use the token, and the expiration time. SAS tokens are used when you need to grant temporary access to external users or systems.

**Azure AD (Entra ID) Integration:** Role-based access using Entra ID credentials. Grants access through RBAC roles (Storage Blob Data Reader, Storage Blob Data Contributor, etc.). This is the recommended approach for Azure services accessing storage — no keys in code.

**[SHOW CODE — Azure CLI storage commands]**

```bash
# Create a storage account
az storage account create \
  --name "lab06sa[your-initials]" \
  --resource-group "lab06-rg" \
  --location "eastus" \
  --sku "Standard_LRS"

# Create a blob container
az storage container create \
  --name "mycontainer" \
  --account-name "lab06sa[your-initials]"

# Upload a file to blob storage
az storage blob upload \
  --container-name "mycontainer" \
  --name "myfile.txt" \
  --file "./myfile.txt" \
  --account-name "lab06sa[your-initials]"

# List blobs in container
az storage blob list \
  --container-name "mycontainer" \
  --account-name "lab06sa[your-initials]" \
  --output table
```

---

## [19:00 - 22:30] Lab Preview and Exam Alignment

**[SLIDE: "Module 06 Lab"]**

In today's lab you will create a storage account, create blob containers, upload files, and work with different access tiers. You will also use the Azure Portal's Storage Browser to verify your work visually. This hands-on experience with blob storage is directly applicable to every cloud workload — from VM backup to application file storage to static website hosting.

**[SLIDE: "AZ-900 Exam Alignment"]**

The highest-frequency storage exam topics:

- Blob Storage: the most versatile, most common, must know the three blob types and four access tiers
- Redundancy options: know the acronyms (LRS, ZRS, GRS, GZRS) and what geographic scope each provides
- The difference between Azure Files (network file share, SMB/NFS) and Blob Storage (object storage, HTTP access)
- Queue Storage as the decoupled messaging mechanism
- SAS tokens as time-limited, permission-scoped access credentials

---

## [22:30 - 24:00] Closing

**[INSTRUCTOR ON CAMERA]**

You now understand Azure Storage Services — the four service types, redundancy options, access tiers, and access control mechanisms. Storage is the foundation beneath every Azure workload.

In Module 07, we cover Azure Database Services — Azure SQL, Cosmos DB, Azure Database for PostgreSQL and MySQL, and the difference between relational and non-relational database options in Azure. I will see you there.

---

**References:**

- learn.microsoft.com/en-us/azure/storage/common/storage-introduction
- learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction
- learn.microsoft.com/en-us/azure/storage/common/storage-redundancy
