# Quiz: Module 06 - Azure Storage Services

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which storage tier has the lowest storage cost but the highest data retrieval latency?

* A) Hot Tier
* B) Cool Tier
* C) Cold Tier
* D) Archive Tier
* **Correct Answer:** D) Archive storage offers the cheapest capacity rates but requires hours to rehydrate/retrieve data.
* **Distractor Analysis:**
  * *Why correct:* Archive storage offers the cheapest capacity rates but requires hours to rehydrate data before it can be read.
  * *Why A/B/C are incorrect:* Hot, Cool, and Cold tiers keep data online for immediate or near-immediate access at progressively higher storage costs.

---

**Question 2**
Which of the following most accurately describes the **Azure Blob Storage Archive tier**?

* A) The lowest-cost blob storage tier designed for data that is rarely accessed, stored for at least 180 days, and requires a rehydration process that can take up to 15 hours before data becomes readable.
* B) A premium storage tier for frequently accessed data with sub-millisecond latency, optimized for high-throughput workloads such as video streaming.
* C) A storage tier that automatically migrates blobs between Hot and Cool based on last-access timestamp, with no manual intervention required.
* D) A storage tier that encrypts blobs at rest using customer-managed keys stored in Azure Key Vault, providing the highest level of data protection.
* **Correct Answer:** A) The Archive tier is the lowest-cost blob storage option for rarely accessed data stored at least 180 days, requiring rehydration before the data can be read.
* **Distractor Analysis:**
  * *Why A is correct:* Archive tier's defining characteristics on AZ-900 are its minimum storage duration, rehydration requirement, lowest storage cost, and highest retrieval cost.
  * *Why B is incorrect:* That describes the Hot tier combined with Premium storage — not the Archive tier.
  * *Why C is incorrect:* Azure Blob Storage lifecycle management policies can automate tier transitions, but that is a feature of the service, not the definition of the Archive tier.
  * *Why D is incorrect:* Encryption at rest with customer-managed keys is an Azure Storage security feature available on all tiers — not a characteristic specific to Archive.

---

**Question 3**
A company needs to provide a shared file system that Windows and Linux VMs in Azure can mount as a network drive using the SMB protocol. Which Azure storage service is the correct choice?

* A) Azure Blob Storage
* B) Azure Queue Storage
* C) Azure Files
* D) Azure Table Storage
* **Correct Answer:** C) Azure Files provides fully managed cloud file shares accessible via SMB and NFS protocols, mountable by Windows and Linux clients as a network drive.
* **Distractor Analysis:**
  * *Why C is correct:* Azure Files is the only Azure storage service that supports SMB/NFS protocol mounting as a network drive.
  * *Why A is incorrect:* Blob Storage is accessed via HTTP REST APIs — it cannot be mounted as a network drive.
  * *Why B is incorrect:* Queue Storage is a message queuing service for decoupled application communication — not a file system.
  * *Why D is incorrect:* Table Storage is a NoSQL key-value store for structured data — not a mountable file system.

---

**Question 4**
A business stores compliance records in Azure Blob Storage. Regulations require that data be protected even if an entire Azure region is destroyed. Which redundancy option meets this requirement?

* A) Locally Redundant Storage (LRS)
* B) Zone-Redundant Storage (ZRS)
* C) Geo-Redundant Storage (GRS)
* D) Premium SSD Managed Disk
* **Correct Answer:** C) GRS replicates data to a secondary Azure region hundreds of miles away, protecting against regional disasters including complete regional outages.
* **Distractor Analysis:**
  * *Why C is correct:* GRS (and GZRS) provide cross-region redundancy, protecting against the complete loss of an Azure region.
  * *Why A is incorrect:* LRS keeps three copies within a single datacenter — a datacenter or regional disaster destroys all copies.
  * *Why B is incorrect:* ZRS spreads copies across three Availability Zones within one region — a full regional outage would affect all zones.
  * *Why D is incorrect:* Premium SSD Managed Disk is VM disk storage — it has its own redundancy but is not a blob storage configuration.

---

**Question 5**
An organization wants to reduce storage costs for log files that are generated daily but accessed only once a month for audits, with occasional retrieval within minutes. Which blob access tier is most cost-effective while meeting the retrieval speed requirement?

* A) Hot tier — optimized for frequent access, lowest retrieval cost
* B) Cool tier — lower storage cost than Hot, data accessible within milliseconds, minimum 30-day storage
* C) Archive tier — lowest storage cost, data rehydration required before access
* D) Cold tier — lower storage cost than Cool, data accessible within milliseconds, minimum 90-day storage
* **Correct Answer:** B) Cool tier provides lower storage costs than Hot tier while keeping data online for millisecond retrieval, suitable for monthly audit access patterns.
* **Distractor Analysis:**
  * *Why B is correct:* Monthly access with minute-level retrieval speed rules out Archive (hours to rehydrate). Cool tier balances lower storage cost with immediate data availability.
  * *Why A is incorrect:* Hot tier is optimized for frequent access — it costs more than Cool for data accessed only monthly.
  * *Why C is incorrect:* Archive tier requires hours of rehydration before data can be read, which exceeds the "within minutes" retrieval requirement.
  * *Why D is incorrect:* Cold tier requires a minimum 90-day storage commitment — monthly-generated logs may not meet this threshold without early deletion penalties.
