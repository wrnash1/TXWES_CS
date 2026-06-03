# Video Script: Module 03 — Compute Engine (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Introduction (1 minute)

Welcome to Module 03. This module covers Google Compute Engine — GCP's
Infrastructure as a Service offering and the foundation of most cloud
architectures.

Compute Engine is one of the most heavily tested services on the ACE exam.
You need to understand machine types, disk options, instance groups, autoscaling,
startup scripts, and the economics of preemptible and Spot VMs.

In Part 1 we cover the conceptual side: VM anatomy, machine families, disk
types, images, and instance lifecycle. In Part 2 we go hands-on with the
console and gcloud CLI.

---

## Segment 2 — Virtual Machine Fundamentals (3 minutes)

### What is a Compute Engine VM?

A Compute Engine virtual machine instance is a virtualized server running on
Google's physical infrastructure. Each VM is defined by:

- **Machine type** — vCPU count and memory
- **Boot disk** — The persistent disk containing the operating system
- **Zone** — Where the VM is deployed
- **Network interface** — VPC network and subnet
- **Service account** — The identity the VM uses to call GCP APIs

### Instance Lifecycle

A Compute Engine VM goes through these lifecycle states:

1. **PROVISIONING** — Resources are being allocated
2. **STAGING** — Resources are being prepared and the instance is being booted
3. **RUNNING** — The instance is fully operational
4. **STOPPING** — A stop command was issued; the instance is shutting down
5. **TERMINATED** — The instance is stopped; not deleted, not billed for compute
6. **SUSPENDED** — Instance memory is saved to disk; can be resumed quickly
7. **DELETED** — Instance and its non-persistent resources are destroyed

**Key distinction for the ACE exam:** A TERMINATED instance is NOT deleted.
It still exists and its persistent boot disk still exists (and is billed). You
can restart it at any time. Only after explicitly deleting the instance do the
non-persistent resources go away.

### Billing for VMs

- VMs are billed per second with a 1-minute minimum.
- Billing starts when the VM enters RUNNING state and stops when it enters
  TERMINATED state.
- Boot disk storage is billed regardless of whether the VM is running or stopped.
- Sustained use discounts apply automatically for VMs running more than 25% of
  a month.

---

## Segment 3 — Machine Families and Types (4 minutes)

GCP organizes VM configurations into machine families optimized for different
workload characteristics.

### General-Purpose Family (E2, N2, N2D, N1)

General-purpose machines offer a balance of compute, memory, and cost.

- **E2** — Cost-optimized; good for web servers, small databases, dev environments.
  Uses shared CPU. Most affordable option.
- **N1** — First-generation balanced machines; supports all add-on GPUs and TPUs.
- **N2** — Second-generation balanced; 20% better performance per dollar than N1.
  Based on Intel Cascade Lake.
- **N2D** — Same as N2 but using AMD EPYC processors; slightly lower cost.

### Compute-Optimized Family (C2, C2D, C3)

High-performance machines for compute-intensive workloads:

- Gaming servers, high-performance computing (HPC), scientific simulations
- C2: Intel Cascade Lake; highest single-thread performance in GCP
- C2D: AMD EPYC; better for highly parallel workloads

### Memory-Optimized Family (M1, M2, M3)

Extreme memory-to-vCPU ratios for in-memory databases:

- SAP HANA, large-scale analytics
- M3: Up to 30 TB of memory in a single VM (requires commitment)

### Accelerator-Optimized Family (A2, G2)

VMs with attached GPUs:

- A2: NVIDIA A100 GPUs for ML training and inference
- G2: NVIDIA L4 GPUs for graphics-intensive workloads

### Custom Machine Types

If no predefined machine type exactly fits your workload, you can create a
custom machine type with any combination of vCPU and memory within limits:

- Minimum: 1 vCPU, 0.9 GB memory per vCPU
- Maximum memory: 6.5 GB per vCPU (up to 8 GB per vCPU with extended memory)

Custom machine types cost slightly more than equivalent predefined types, but
can save money by avoiding over-provisioning.

**ACE Exam Tip:** Know which machine family to recommend for a given scenario.
Memory-heavy workloads like SAP HANA → M2. GPU/ML workloads → A2. Cost-sensitive
web apps → E2. High single-thread performance → C2.

---

## Segment 4 — Disk Types and Storage (3 minutes)

### Persistent Disk

Persistent Disk (PD) is the default block storage for Compute Engine VMs. It
persists independently of the VM — if you delete the VM, the disk still exists
unless you checked the "Delete boot disk with instance" option.

Persistent Disk types:

- **pd-standard** — HDD-backed; cheapest; sequential read/write workloads
- **pd-balanced** — SSD-backed; good balance of performance and cost; default
  for most new VMs
- **pd-ssd** — High-performance SSD; for databases and latency-sensitive apps
- **pd-extreme** — Highest IOPS; for very demanding database workloads; must
  be explicitly requested

### Local SSD

Local SSD is physically attached to the host machine. It offers the highest
performance of any GCP disk type — very high IOPS and very low latency.

Critical limitation: Local SSD data is NOT persistent. If the VM stops, restarts,
or is live-migrated, local SSD data is lost. Use only for temporary data,
caches, or scratch space.

### Hyperdisk

Hyperdisk is a newer generation of network-attached block storage that
decouples capacity, throughput, and IOPS into independently configurable
parameters. Currently available in select machine families.

### Boot Disk vs. Additional Disks

- **Boot disk**: Contains the OS image; required; usually pd-balanced by default
- **Additional disks**: Can be attached to a VM for data; can be attached to
  multiple VMs in read-only mode; can be detached and moved between VMs

### Snapshots

A snapshot is a point-in-time backup of a persistent disk. Snapshots are:

- Stored in Cloud Storage (not in a disk)
- Incremental after the first full snapshot
- Used to create new persistent disks or restore data
- Usable for cross-region disk migration

---

## Segment 5 — Images and Startup Scripts (2 minutes)

### OS Images

An image is the template used to create a boot disk. GCP provides:

- **Public images** — Maintained by Google or third parties; include Debian,
  Ubuntu, CentOS, Windows Server, RHEL, SLES
- **Custom images** — Created from your own disk or imported from on-premises
- **Marketplace images** — Pre-configured solutions (LAMP stack, etc.)

### Image Families

An image family points to the latest non-deprecated version of an image. Using
an image family (e.g., `debian-11`) rather than a specific image version
(e.g., `debian-11-bullseye-v20231010`) ensures you always use the most recent
patched version.

### Startup Scripts

A startup script is a script (bash, PowerShell) that runs when a VM boots.
It is passed via the `--metadata=startup-script` flag or via a URL in
`startup-script-url`.

Use cases:

- Install software packages
- Configure the OS
- Register the instance with a configuration management system
- Download application code from Cloud Storage

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --metadata=startup-script='#! /bin/bash
apt-get update
apt-get install -y nginx
systemctl start nginx'
```

**ACE Exam Tip:** Startup scripts run as root on Linux. They run every time the
VM boots, not just on first creation. For one-time initialization, check a flag
file and exit early if already configured.

---

## Summary — Part 1

In Part 1 we covered:

- VM anatomy: machine type, disk, zone, network, service account
- Instance lifecycle states and billing implications
- Machine families: E2, N2, N2D, C2, M2, A2 and when to use each
- Custom machine types
- Disk types: pd-standard, pd-balanced, pd-ssd, pd-extreme, local SSD
- Snapshots for backup and migration
- OS images, image families, and startup scripts

In Part 2 we cover instance groups, autoscaling, preemptible VMs, and the
gcloud CLI for Compute Engine.

See you in Part 2.

---

End of Part 1 — Module 03

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/compute/docs
