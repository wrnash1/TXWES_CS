# Reading Guide: Module 06 - Azure Storage Services

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 06 - Azure Storage Services**! This module covers Azure's core storage offerings as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Azure Storage is one of the most heavily tested topic areas in AZ-900 — you will need to know the storage types, blob access tiers, replication options, and appropriate use cases for each service.

You will learn how Blob Storage access tiers (Hot, Cool, Cold, Archive) balance cost against retrieval speed, how Azure Files provides SMB-compatible file shares, and how storage redundancy options protect against data loss at different geographic scales. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Blob Storage (Hot, Cool, Cold, Archive)**: Azure Blob Storage stores unstructured data as objects (blobs). Access tiers trade storage cost for retrieval cost and speed: Hot tier is optimized for frequently accessed data (highest storage cost, lowest retrieval cost); Cool tier is for infrequently accessed data stored at least 30 days; Cold tier is for data stored at least 90 days; Archive tier stores rarely accessed data for at least 180 days at the lowest storage cost but requires hours of rehydration before data can be read.

* **Azure Files**: A fully managed cloud file share service accessible via the SMB (Server Message Block) and NFS protocols, making it mountable by Windows, Linux, and macOS clients. Azure Files is used to replace or augment on-premises file servers, support lift-and-shift scenarios, and provide shared storage for applications running on multiple VMs.

* **Disk Storage**: Managed disk volumes for Azure Virtual Machines, available in four performance tiers: Ultra Disk (highest IOPS), Premium SSD, Standard SSD, and Standard HDD. Disk Storage is IaaS storage — it is attached to and managed with VMs. AZ-900 tests the difference between unmanaged and managed disks (managed disks are Microsoft-recommended).

* **Storage Replication Types**: Azure offers multiple redundancy levels — Locally Redundant Storage (LRS) stores 3 copies in a single datacenter; Zone-Redundant Storage (ZRS) stores copies across 3 Availability Zones in the same region; Geo-Redundant Storage (GRS) replicates to a secondary region; Geo-Zone-Redundant Storage (GZRS) combines ZRS in the primary region with geo-replication. AZ-900 tests which redundancy option protects against specific failure scenarios.

---

### 2. Certification Exam Tips

* **Blob Access Tier Trade-offs**: AZ-900 presents scenarios and asks which tier is appropriate. Key rule: the more frequently data is accessed, the hotter the tier should be. Archive tier data must be "rehydrated" (a process taking up to 15 hours) before it can be read — it is not suitable for data needing fast access.
* **Archive Rehydration Trap**: The exam may describe a scenario where data in Archive tier is needed urgently. Remember that retrieval from Archive is not instant — it requires rehydration. For data that may be needed quickly, Cool or Cold tier is more appropriate.
* **LRS vs. GRS**: LRS is cheapest but protects only against hardware failure within one datacenter — a datacenter fire destroys all copies. GRS protects against regional disasters. AZ-900 tests which redundancy protects against regional outages — the answer is GRS or GZRS.
* **Azure Files vs. Blob Storage**: Files = structured file-share accessed via SMB/NFS (mount as a drive). Blob = object storage accessed via HTTP/REST (for unstructured data like images, backups, and logs). AZ-900 may ask which service lets users map a network drive — the answer is Azure Files.
* **Study Resource**: The Microsoft Learn storage module covers all storage types, blob tiers, and redundancy with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure storage services including Blob tiers, Azure Files, and redundancy options. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free freeCodeCamp course covers Azure storage for AZ-900 — watch the storage section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Create an Azure Storage Account**: In the Azure portal, create a storage account, selecting a redundancy option (e.g., LRS) and observing how the region selection affects data residency.
* **Upload a blob to a container**: Create a blob container, upload a file, and set the blob's access level (private vs. public). Observe the blob URL structure and access behavior.
* **Modify blob access tier from Hot to Archive**: Change an uploaded blob's access tier from Hot to Archive in the portal. Observe the warning that the blob will not be immediately readable and that rehydration is required for retrieval.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure storage unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the storage section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for storage account creation, blob upload, and access tier modification.
* [ ] Proceed to the weekly hands-on lab activity.
