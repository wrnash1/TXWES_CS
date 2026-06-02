# Video Script — Module 03, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Compute Engine — VM Instances, Machine Types, and Disk Storage

### Estimated Duration: 13–15 minutes

---

## Introduction

Welcome to Module 03. I'm Professor Nash, and this module is all about Compute Engine — Google's Infrastructure as a Service offering. Compute Engine lets you create and manage virtual machines running in Google's data centers. It is the most foundational compute service in GCP and a major topic on the Associate Cloud Engineer exam.

By the end of this module you will be able to create a VM instance using the Console and the gcloud CLI, choose the right machine family for a given workload, select appropriate disk types, and understand the differences between persistent disks, local SSDs, and snapshots. You will also learn about startup scripts, preemptible and spot VMs, and managed instance groups.

---

## Section 1: Compute Engine Overview

**[SHOW SLIDE: Compute spectrum — Compute Engine (IaaS) on the left, moving toward GKE, App Engine, Cloud Run (Serverless) on the right]**

Compute Engine is Google's IaaS — Infrastructure as a Service — offering. When you use Compute Engine, you choose the hardware specifications, the operating system, the network configuration, and the storage. You are responsible for the OS and everything running on it, including patching, security configuration, and application management.

This is in contrast to PaaS services like App Engine or serverless offerings like Cloud Run, where Google manages more of the underlying infrastructure for you. Compute Engine gives you the most control but also the most responsibility.

Use Compute Engine when you need to lift-and-shift an existing application that requires a specific OS configuration, when you need control over kernel parameters or custom hardware, when you are running legacy software that was designed for VMs, or when no higher-level GCP service fits your workload.

---

## Section 2: Machine Families and Types

**[SHOW SLIDE: Machine family table with E2, N2, N2D, C2, M2 families and their use cases]**

When you create a VM, the most important choice is the machine type — this determines how much CPU and memory the VM has. GCP organizes machine types into machine families based on the workload they are optimized for.

### The E2 Family — General Purpose (Cost-Optimized)

E2 machines are Google's cost-optimized general-purpose family. They use a CPU scheduler that shares physical cores between VMs, which allows Google to offer them at lower prices. E2 VMs are suitable for development environments, small web servers, microservices, and any workload that does not require consistent high CPU performance.

Examples: `e2-micro` (2 vCPU, 1 GB), `e2-small` (2 vCPU, 2 GB), `e2-medium` (2 vCPU, 4 GB), `e2-standard-4` (4 vCPU, 16 GB).

The Free Tier includes one `e2-micro` VM per month in specific regions, which is what you use for course labs.

### The N2 Family — General Purpose (High Performance)

N2 and N2D machines provide higher sustained performance than E2. They use dedicated physical cores rather than a shared scheduler. N2 runs on Intel hardware; N2D runs on AMD EPYC processors. Use N2 or N2D for production web applications, mid-tier databases, and workloads that need consistent CPU performance.

### The C2 and C2D Families — Compute-Optimized

C2 and C2D machines are designed for compute-intensive workloads: high-performance computing, game servers, scientific simulations, and any application that is CPU-bound and benefits from the highest per-core performance. They are more expensive per vCPU but significantly faster than N2 for CPU-bound tasks.

### The M2 Family — Memory-Optimized

M2 machines provide the highest memory-to-vCPU ratio in GCP. They are designed for in-memory databases like SAP HANA, large-scale in-memory analytics, and workloads that require enormous amounts of RAM. An M2 machine can have up to 12 TB of memory — you will not need that for a web server, but for an enterprise in-memory database it is essential.

### Choosing the Right Machine Type

**[SHOW SLIDE: Decision tree — general purpose vs. memory-heavy vs. CPU-heavy vs. cost-sensitive]**

For the ACE exam, when a question describes a workload and asks which machine family to use:

- General purpose web server or app: E2 (cost-sensitive) or N2 (performance-sensitive)
- In-memory database (SAP HANA, Redis at massive scale): M2
- CPU-intensive scientific computing or game server: C2
- Fault-tolerant batch processing where cost matters most: Spot VMs (any family)

---

## Section 3: Disk Types

**[SHOW SLIDE: Disk types comparison table — Standard Persistent, Balanced Persistent, SSD Persistent, Extreme Persistent, Local SSD]**

Every VM needs storage. Compute Engine offers several disk types.

### Persistent Disks

Persistent disks are network-attached storage. They exist independently of the VM instance — if you stop or delete the VM, the persistent disk continues to exist and retains all data. You can attach a persistent disk to a new VM, detach it and re-attach it, or take snapshots of it.

Types of persistent disks:

- **Standard Persistent Disk (pd-standard)**: Uses hard disk drive (HDD) technology. Lowest cost. Good for sequential I/O — batch jobs, data warehousing — but slower for random I/O. Best for development, infrequent access workloads.
- **Balanced Persistent Disk (pd-balanced)**: Uses SSD technology. Good balance of performance and cost. The recommended default for most production workloads.
- **SSD Persistent Disk (pd-ssd)**: Higher IOPS than balanced. Use for databases and applications with high random I/O requirements.
- **Extreme Persistent Disk (pd-extreme)**: Highest IOPS. For workloads that need maximum I/O performance, like very high-transaction-rate databases.

### Local SSD

Local SSDs are physically attached NVMe drives that live on the same physical machine as the VM. They offer the highest I/O performance available in GCP — hundreds of thousands of IOPS and sub-millisecond latency. However, they are ephemeral: all data on a local SSD is permanently lost when the VM stops, crashes, live-migrates, or is deleted.

Use local SSDs only for scratch data, temporary caches, or data that you can reconstruct — for example, an in-memory database that populates itself from a persistent source at startup.

**[PAUSE — Professor on camera]**

This is an ACE exam classic. The question will say something like: "A VM stops and restarts. Which storage type loses its data?" The answer is always local SSD. Persistent disks survive VM stops and restarts. Always.

---

## Section 4: Snapshots and Custom Images

**[SHOW SLIDE: Diagram showing a persistent disk → snapshot → restore to new disk]**

### Snapshots

A snapshot is a point-in-time backup of a persistent disk. Snapshots are incremental — the first snapshot captures the full disk, and each subsequent snapshot captures only the blocks that changed since the last snapshot. This makes them storage-efficient and fast to create after the first one.

Use snapshots for:

- Pre-upgrade backups (capture disk state before a risky software upgrade)
- Disaster recovery (restore a disk to a previous known-good state)
- Migrating disk data to a new zone or region

Snapshots are stored in Cloud Storage and are available across regions.

### Custom Images

A custom image is a bootable disk image that you create from a running VM, a persistent disk, or a snapshot. You use custom images to create a "golden image" — a VM template that has your operating system pre-configured with all your software, security hardening, and configuration baked in.

Custom images are used for fleet deployment — creating tens or hundreds of identical VMs that all start with exactly the same configuration. This is far more reliable than startup scripts that install software on every boot, because the software is already installed in the image.

Key distinction: snapshots are for backup and restore of existing disks. Custom images are for creating new VMs from a reference configuration.

---

## Closing — Part 1

Let's summarize Part 1. Compute Engine is GCP's IaaS service giving you full control over VMs. Machine families include E2 (general purpose, cost-optimized), N2 (general purpose, high performance), C2 (compute-optimized), and M2 (memory-optimized). Disk types range from standard persistent disks (HDD, cheapest) to balanced and SSD persistent disks, to local SSDs (highest performance but ephemeral). Persistent disks survive VM stops. Local SSDs lose data on VM stop. Snapshots are for backup and restore. Custom images are for fleet deployment.

In Part 2 we will cover startup scripts, preemptible and spot VMs, managed instance groups, and the gcloud commands for creating and managing VMs.

---

End of Part 1 — Module 03

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
