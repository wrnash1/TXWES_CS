# Quiz — Module 03

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Compute Engine — VM Instances and Machine Types

### 10 Questions | 10 Points Each | Total: 100 Points

---

## Question 1

You are managing a fleet of Compute Engine instances. You need to capture the exact state of a data disk right before a major software upgrade so you can quickly roll back if the upgrade fails. What is the most efficient Google Cloud feature to use?

A. Create a custom image of the disk.

B. Create a snapshot of the disk.

C. Export the disk contents to a Cloud Storage bucket as a tar archive.

D. Use Database Migration Service to copy the disk contents to another project.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Custom images are designed to create reusable VM templates for provisioning new instances at scale, not for point-in-time backup and rollback of an existing running disk. While an image could technically preserve disk state, snapshots are the correct tool for pre-upgrade backup and rollback scenarios.
- Why C is incorrect: Exporting disk contents to Cloud Storage as an archive is a manual, time-consuming process not designed for quick pre-upgrade backup and rollback. It is used for long-term archiving or moving data out of GCP entirely.
- Why D is incorrect: Database Migration Service is designed for migrating database workloads between database systems, not for backing up or restoring raw Compute Engine persistent disks.

---

## Question 2

A developer stops a Compute Engine VM to resize it, then restarts it an hour later. Which statement about the VM's storage is correct?

A. All data on attached persistent disks is permanently lost when the VM stops.

B. Data on attached persistent disks is preserved; data on any local SSDs is permanently lost.

C. Data on both persistent disks and local SSDs is preserved across stop and start cycles.

D. The boot disk data is preserved, but all secondary persistent disks are automatically detached and lose their data.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Persistent disks are network-attached storage that exist independently of the VM instance lifecycle. Stopping or even deleting a VM does not delete its attached persistent disks unless you explicitly request deletion.
- Why C is incorrect: Local SSDs are physically attached to the host machine running the VM. Their data is ephemeral and is permanently lost whenever the VM stops, crashes, or is migrated to a different host machine.
- Why D is incorrect: Secondary persistent disks are not automatically detached or deleted when a VM stops. They remain attached and retain all data until explicitly detached or deleted by an administrator.

---

## Question 3

Your batch processing application processes video transcoding jobs that each take about 10 minutes. The application automatically retries any job that fails. You want to minimize compute costs while maintaining acceptable job completion rates. Which Compute Engine option is most appropriate?

A. N2 standard on-demand instances with 1-year committed use discounts.

B. Memory-optimized M2 instances for maximum RAM per transcoding job.

C. Spot VM instances.

D. Compute-optimized C2 instances billed by the second at full on-demand rates.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Committed use discounts offer up to 37% off for 1-year commitments, which is a significant savings. However, Spot VMs offer up to 91% off and are the minimum-cost option for fault-tolerant, retryable workloads. The scenario explicitly mentions automatic retry capability, making this a perfect Spot VM use case.
- Why B is incorrect: Memory-optimized M2 instances are designed for workloads requiring extremely large amounts of RAM, such as in-memory databases. Video transcoding is a CPU-bound workload; M2 instances would be far more expensive than necessary.
- Why D is incorrect: Compute-optimized C2 instances do provide high per-core CPU performance suitable for transcoding, but they are billed at full on-demand rates. Spot VMs provide the needed compute at a fraction of the cost for this fault-tolerant workload.

---

## Question 4

You need to deploy 50 identical web server VMs, each pre-configured with your company's custom Nginx setup, internal security hardening, and TLS certificates. What is the most operationally efficient approach?

A. Write a startup script that runs on every VM boot to download and install Nginx and apply configuration from a Git repository.

B. Create a custom image from a fully configured reference VM, then use that image as the boot disk for all 50 instances.

C. Take a snapshot of one configured VM's boot disk and manually restore it to each of the 50 VMs individually.

D. Use Cloud Marketplace to deploy a pre-configured Nginx template to all 50 VMs.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Startup scripts that download and install software on every boot introduce variability (package versions may change), depend on external repositories being available, slow down boot time, and add network dependency. Custom images are faster, more reliable, and more consistent for fleet deployment.
- Why C is incorrect: Snapshots are designed for backup and restore of existing disks, not for provisioning new instances at scale. Restoring a snapshot to each of 50 VMs individually is more complex and less efficient than using a custom image with an instance template or managed instance group.
- Why D is incorrect: Cloud Marketplace provides third-party pre-configured software stacks but cannot incorporate proprietary company-specific configuration, internal certificates, or custom security hardening scripts.

---

## Question 5

Which Compute Engine machine family is designed specifically for workloads that require a very large amount of RAM relative to vCPU count, such as SAP HANA deployments?

A. E2

B. C2

C. N2

D. M2

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: The E2 family is a cost-optimized general-purpose family suitable for development environments, small web servers, and cost-sensitive workloads. It provides standard RAM-to-vCPU ratios and is not designed for memory-intensive database workloads.
- Why B is incorrect: The C2 family is compute-optimized with the highest per-core CPU performance. It is designed for CPU-bound workloads like game servers, scientific computing, and high-performance computing — not for maximizing RAM capacity.
- Why C is incorrect: The N2 family is a general-purpose high-performance family suitable for production workloads requiring consistent CPU performance. While N2 offers more RAM than E2, it does not provide the extreme memory capacity of the M2 family.

---

## Question 6

A Cloud Architect is designing a data pipeline that runs overnight batch jobs processing large datasets. The jobs take approximately 3 hours and write results to Cloud Storage when complete. The pipeline restarts automatically if any individual step fails. The architect wants to minimize the nightly compute bill. Which pricing model is most appropriate?

A. On-demand E2 instances with sustained use discounts applied automatically.

B. Resource-based committed use discounts on N2 instances for a 3-year term.

C. Spot VMs for the pipeline worker nodes.

D. Per-second billing on custom machine types to minimize idle time.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: On-demand instances with sustained use discounts provide modest savings for workloads running continuously throughout the month. For a 3-hour nightly batch job that runs only a small fraction of each month, sustained use discounts provide minimal benefit. Spot VMs offer far greater savings for this fault-tolerant pattern.
- Why B is incorrect: A 3-year committed use commitment is inappropriate for a 3-hour nightly batch workload. CUDs are cost-effective for workloads that run continuously and would actually consume the committed capacity. Paying for committed capacity that runs only 3 hours per day would be wasteful.
- Why D is incorrect: Per-second billing is a billing increment, not a pricing model offering discount. It reduces waste at the end of jobs but does not provide the 91% cost reduction that Spot VMs offer for fault-tolerant batch workloads.

---

## Question 7

Your application running on a Compute Engine VM needs to store temporary files for fast processing. These files can be regenerated from the source data if lost. You need the highest I/O performance available in GCP. Which storage type should you use?

A. Standard persistent disk (pd-standard)

B. SSD persistent disk (pd-ssd)

C. Balanced persistent disk (pd-balanced)

D. Local SSD

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: Standard persistent disks use HDD technology and have the lowest I/O performance of all Compute Engine disk options. They are appropriate for sequential batch workloads but not for maximum I/O performance requirements.
- Why B is incorrect: SSD persistent disks provide high IOPS suitable for production databases, but they are still network-attached storage and cannot match the raw I/O performance of physically attached local SSDs.
- Why C is incorrect: Balanced persistent disks offer a good balance of performance and cost for general production workloads. Their performance is between standard and SSD persistent disks — still network-attached and lower performance than local SSDs.

---

## Question 8

A Managed Instance Group (MIG) is configured with a health check that tests whether port 80 is responding with HTTP 200. One VM in the group stops serving HTTP 200 responses after a configuration error. What does the MIG do?

A. Nothing — the MIG only manages scaling, not health monitoring.

B. The MIG logs a warning in Cloud Monitoring but takes no corrective action.

C. The MIG automatically deletes the unhealthy VM and creates a replacement VM using the instance template.

D. The MIG pauses autoscaling until the unhealthy VM recovers or is manually repaired.

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Managed Instance Groups support autohealing, which is specifically the feature that monitors VM health via health checks and replaces unhealthy VMs automatically. Autohealing is a core MIG capability alongside autoscaling, rolling updates, and multi-zone support.
- Why B is incorrect: While MIG health check failures do generate Cloud Monitoring metrics and alerts, the autohealing feature takes active corrective action — it does not merely log a warning. The unhealthy VM is automatically replaced.
- Why D is incorrect: MIG autohealing does not pause autoscaling when a VM becomes unhealthy. The MIG continues managing the group's target size and scaling behavior independently from the health check response for the affected VM.

---

## Question 9

A developer uses `gcloud compute instances create` to provision a new VM without specifying any service account. What service account is attached to the VM, and what is the security implication?

A. No service account is attached; the VM has no ability to call GCP APIs.

B. The Compute Engine default service account is attached, which has `roles/editor` on the project by default — granting broad write access to most project resources.

C. A new purpose-built service account is created automatically and attached with minimal permissions.

D. The current gcloud user's Google Account is used as the VM's identity for API calls.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: When a VM is created without specifying a service account, GCP automatically attaches the Compute Engine default service account rather than leaving the VM without any identity. The VM does have the ability to call GCP APIs.
- Why C is incorrect: GCP does not auto-create purpose-built service accounts on VM creation. The Compute Engine default service account already exists from when the Compute Engine API was enabled, and this pre-existing account is attached.
- Why D is incorrect: User accounts (human Google identities) are not attached to VMs as their runtime identity. VM instances authenticate as service accounts, not as the user who ran the `gcloud compute instances create` command.

---

## Question 10

You are reviewing your organization's Compute Engine environment and find that several production VMs use `e2-micro` machine types. The application teams report frequent CPU throttling and performance degradation under load. Which action addresses this most directly?

A. Move the VMs to Spot instances to access higher-performance hardware at a lower cost.

B. Upgrade the VMs to a higher machine type such as `e2-standard-4` or `n2-standard-4` that provides dedicated vCPUs and more memory.

C. Add more local SSDs to the VMs to increase I/O throughput and compensate for CPU bottlenecks.

D. Apply sustained use discounts to allow the VMs to access more CPU capacity automatically.

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Spot VMs can use any machine type, including e2-micro. Switching to Spot instances changes the pricing and availability model but does not change the underlying machine type or resolve the CPU throttling issue. Additionally, production services should not use Spot VMs due to preemption risk.
- Why C is incorrect: Local SSDs increase disk I/O performance, not CPU processing capacity. If the bottleneck is CPU throttling on an e2-micro (which uses shared-core CPU scheduling), additional storage does not address the root cause.
- Why D is incorrect: Sustained use discounts are a billing discount applied automatically to on-demand VMs that run for a significant portion of the month. They reduce cost but do not increase the VM's CPU allocation, memory capacity, or performance characteristics.

---

End of Quiz — Module 03

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
