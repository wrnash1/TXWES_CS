# Quiz: Module 03 – Compute Engine: VM Instances and Machine Types
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
You are managing a fleet of Compute Engine instances. You need to capture the exact state of a data disk right before a major software upgrade so you can quickly roll back if the upgrade fails. What is the most efficient Google Cloud feature to use?

A) Create a Custom Image of the disk.
B) Create a Snapshot of the disk.
C) Export the disk to a Cloud Storage bucket.
D) Use Database Migration Service to copy the disk contents.

*   **Correct Answer:** B) Create a Snapshot of the disk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Custom Images are designed to create reusable VM templates for provisioning new instances, not for point-in-time backup and rollback of an existing disk.
    *   *Why C is incorrect:* Exporting a disk takes significantly longer than snapshotting and is used for moving disks out of GCP or deep archiving — not for quick pre-upgrade backups.
    *   *Why D is incorrect:* Database Migration Service is for migrating databases between systems, not for backing up or restoring raw Compute Engine persistent disks.

---

**Question 2**
When deploying a Kubernetes application on Google Cloud, you want to avoid managing the underlying Compute Engine nodes (VMs) entirely. You only want to focus on your containers and pay only for the CPU and memory your pods request. Which service should you choose?

A) GKE Standard Cluster
B) GKE Autopilot Cluster
C) Compute Engine Managed Instance Group (MIG)
D) App Engine Flexible Environment

*   **Correct Answer:** B) GKE Autopilot Cluster
*   **Distractor Analysis:**
    *   *Why A is incorrect:* In a GKE Standard cluster you are responsible for managing node pools and you pay for the underlying VMs regardless of whether your pods use all their capacity.
    *   *Why C is incorrect:* Managed Instance Groups manage raw Compute Engine VMs, not Kubernetes pods or containers; they have no awareness of Kubernetes constructs.
    *   *Why D is incorrect:* App Engine Flexible runs containers, but it is a PaaS environment with no Kubernetes API; GKE Autopilot is specifically the Kubernetes offering that abstracts node management.

---

**Question 3**
Your batch processing application processes thousands of video transcoding jobs. Each job takes about 10 minutes and the application automatically retries any job that fails. You want to minimize compute costs. Which Compute Engine option is most appropriate?

A) N2 standard on-demand instances with committed use discounts.
B) Memory-optimized M2 instances for maximum RAM per job.
C) Spot (Preemptible) VM instances.
D) Compute-optimized C2 instances billed by the second.

*   **Correct Answer:** C) Spot (Preemptible) VM instances.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Committed use discounts offer up to 57% off for 1- or 3-year commitments, but Spot VMs offer up to 91% off and are the lowest-cost option for fault-tolerant, retryable workloads.
    *   *Why B is incorrect:* Memory-optimized instances cost significantly more and are intended for in-memory databases and analytics — not video transcoding, which is CPU-bound.
    *   *Why D is incorrect:* Compute-optimized C2 instances provide the highest per-core performance but at full on-demand pricing; they are appropriate for CPU-intensive workloads that cannot tolerate preemption.

---

**Question 4**
A developer stops a Compute Engine VM to resize it, then restarts it an hour later. Which of the following statements about the VM's storage is correct?

A) All data on attached Persistent Disks is lost when the VM is stopped.
B) Data on attached Persistent Disks is preserved; data on Local SSDs is lost.
C) Data on both Persistent Disks and Local SSDs is preserved across stop/start cycles.
D) The boot disk is preserved, but all secondary Persistent Disks are deleted automatically.

*   **Correct Answer:** B) Data on attached Persistent Disks is preserved; data on Local SSDs is lost.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Persistent Disks are network-attached storage that exist independently of the VM instance lifecycle — stopping or even deleting a VM does not delete its Persistent Disks unless explicitly requested.
    *   *Why C is incorrect:* Local SSDs are physically attached to the host machine and their data is ephemeral; it is permanently lost whenever the VM stops, crashes, or is migrated.
    *   *Why D is incorrect:* Secondary Persistent Disks are not automatically deleted when a VM stops; they remain attached and retain all data until explicitly deleted by an administrator.

---

**Question 5**
You need to deploy 50 identical web server VMs, each pre-configured with your company's custom Nginx setup, security hardening scripts, and internal TLS certificates. What is the most operationally efficient way to ensure all 50 VMs start in exactly the same state?

A) Write a startup script that runs on every VM boot to install and configure Nginx from scratch.
B) Create a Custom Image from a fully configured reference VM, then use that image as the boot disk source for all 50 instances.
C) Take a snapshot of one VM's boot disk and restore it to each of the 50 VMs individually.
D) Use Cloud Marketplace to deploy a pre-configured Nginx template to all 50 VMs simultaneously.

*   **Correct Answer:** B) Create a Custom Image from a fully configured reference VM, then use that image as the boot disk source for all 50 instances.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Startup scripts that install software on every boot are slower to launch, depend on external package repositories being available, and introduce variability if package versions change between deployments.
    *   *Why C is incorrect:* Snapshots are point-in-time disk backups designed for backup and restore of existing disks, not for provisioning new instances at scale; Custom Images are the correct mechanism for fleet deployment.
    *   *Why D is incorrect:* Cloud Marketplace provides third-party pre-configured stacks but cannot incorporate your company's proprietary configuration, internal certificates, or custom security hardening.
