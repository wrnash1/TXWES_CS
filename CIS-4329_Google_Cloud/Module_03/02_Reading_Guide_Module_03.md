# Reading Guide: Module 03 – Compute Engine: VM Instances and Machine Types
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 03 – Compute Engine: VM Instances and Machine Types**! Compute Engine is Google Cloud's Infrastructure-as-a-Service (IaaS) offering. This module covers creating and configuring virtual machine instances, selecting appropriate machine types, managing persistent disks, and using snapshots and custom images. The ACE exam tests your ability to select the right VM configuration for a given workload and cost requirement.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Machine Types**: Predefined VM configurations grouped by family. **General-purpose** (E2, N2, N1) balance price and performance for most workloads. **Compute-optimized** (C2) offer the highest per-core performance for CPU-bound tasks. **Memory-optimized** (M2) provide the most RAM per core for in-memory databases. Custom machine types let you specify exact vCPU and memory ratios.

*   **Preemptible VMs / Spot VMs**: Compute Engine VMs that run at a large discount (up to 91% off on-demand price) but can be stopped by Google at any time with only 30 seconds' notice. They are ideal for fault-tolerant batch processing workloads that can checkpoint and restart; they are unsuitable for stateful services like databases.

*   **Persistent Disk vs. Local SSD**: Persistent Disks are network-attached storage that persists independently of the VM lifecycle — data survives VM deletion. Local SSDs are physically attached to the host server, deliver very high IOPS, but are ephemeral: data is lost when the VM stops or is deleted.

*   **Snapshots**: Incremental backups of a Persistent Disk captured at a specific point in time. Snapshots are stored in Cloud Storage and are used for backup and disaster recovery. The first snapshot is a full copy; subsequent snapshots are incremental.

*   **Custom Images**: A reusable VM disk image created from an existing disk or snapshot. Custom images are used to pre-install software and configuration so that new VMs boot in a known, consistent state — ideal for stamping out identical fleet members at scale.

*   **GKE Autopilot vs. Standard**: In Standard GKE, you manage the underlying Compute Engine node pools and pay for the VMs regardless of pod utilization. In Autopilot GKE, Google manages nodes completely and you pay only for the CPU, memory, and storage that your running pods request.

---

### 2. Certification Exam Tips

*   **Spot/Preemptible = batch only**: The ACE exam heavily tests when to use Spot VMs. The key signal in the question is that the workload is *fault-tolerant* or can *retry automatically*. If the question mentions a database, API server, or anything stateful, Spot VMs are the wrong answer.

*   **Snapshot vs. Custom Image distinction**: Snapshots are for point-in-time backup of an existing disk (backup/DR). Custom Images are for creating a reusable golden template to provision new VMs. If the question says "roll back" or "backup before upgrade," the answer is snapshot. If the question says "deploy identical VMs" or "pre-install software," the answer is custom image.

*   **Persistent Disk survives VM deletion; Local SSD does not**: The exam tests whether you know that stopping or deleting a VM does not delete its attached Persistent Disk by default. Local SSD data is always lost on VM stop/delete.

*   **`gcloud compute` command family**: Know `gcloud compute instances create`, `gcloud compute instances list`, `gcloud compute instances stop`, `gcloud compute disks snapshot`, and `gcloud compute images create`. These commands are frequently shown in exam questions.

*   **Study Resource**: The freeCodeCamp ACE course covers Compute Engine machine types, disks, and images with practical examples: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). The official Compute Engine documentation is the authoritative reference for machine type families.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Compute Engine machine types documentation to understand the general-purpose, compute-optimized, and memory-optimized families: [Compute Engine Machine Types](https://cloud.google.com/compute/docs/machine-types).
*   **Required Reading**: Review persistent disk and snapshot concepts including how incremental snapshots work: [Persistent Disks and Snapshots](https://cloud.google.com/compute/docs/disks).
*   **Required Video**: Watch the Compute Engine segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Compute Engine chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create VM instances, take a disk snapshot, and create a custom image. Key commands to practice:

*   `gcloud compute instances create VM_NAME --machine-type=e2-medium --zone=us-central1-a` — creates a VM
*   `gcloud compute disks snapshot DISK_NAME --snapshot-names=SNAPSHOT_NAME` — takes a disk snapshot
*   `gcloud compute images create IMAGE_NAME --source-disk=DISK_NAME --source-disk-zone=ZONE` — creates a custom image
*   `gcloud compute instances list --filter="status=RUNNING"` — lists only running instances

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Compute Engine Machine Types](https://cloud.google.com/compute/docs/machine-types) documentation page.
- [ ] Read the [Persistent Disks and Snapshots](https://cloud.google.com/compute/docs/disks) documentation page.
- [ ] Watch the Compute Engine segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a VM, take a snapshot, create a custom image.
- [ ] Proceed to the weekly quiz.
