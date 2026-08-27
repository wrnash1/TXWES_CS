# Reading Guide: Module 03 — Compute Engine

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide covers Google Compute Engine (GCE) — GCP's IaaS offering.
Compute Engine questions appear on every ACE exam. You need to understand
machine types, disk options, instance groups, autoscaling, and the economics
of different VM pricing models.

**Estimated Reading Time:** 50–60 minutes

---

## Section 1 — Virtual Machine Anatomy

### 1.1 Core Components

Every Compute Engine instance is defined by:

- **Machine type** — vCPU and memory configuration
- **Boot disk** — Persistent disk with the operating system
- **Zone** — Isolated data center where the VM runs
- **VPC network and subnet** — Network connectivity
- **Service account** — GCP identity for API calls from within the VM
- **Firewall tags** — Used to apply firewall rules to the instance
- **Metadata** — Key-value pairs including startup scripts

### 1.2 Instance Lifecycle

| State | Description | Billed for Compute |
|---|---|---|
| PROVISIONING | Resources being allocated | No |
| STAGING | Booting | No |
| RUNNING | Fully operational | Yes |
| STOPPING | Shutting down | No |
| TERMINATED | Stopped; exists; not running | No |
| SUSPENDED | Memory saved to disk | No (storage yes) |
| DELETED | Permanently removed | No |

A TERMINATED instance still occupies its persistent disk (billed for storage)
and its static IP (billed if unused). Only a DELETED instance fully releases
all resources.

### 1.3 Live Migration

When Google needs to perform maintenance on the physical host, Compute Engine
can live-migrate your running VM to a different host with no downtime. This
happens transparently for most VM types.

Live migration is not available for:

- Preemptible and Spot VMs
- VMs with GPUs attached
- VMs with local SSD attached (maintenance causes VM to stop, not migrate)

---

## Section 2 — Machine Families

### 2.1 General-Purpose

| Series | Best For | Key Characteristic |
|---|---|---|
| E2 | Web serving, dev/test, small databases | Shared-core options; lowest cost |
| N1 | General workloads; GPU/TPU support | First-gen; supports all add-ons |
| N2 | Balanced compute | Intel Cascade Lake; 20% better than N1 |
| N2D | Balanced compute, parallel workloads | AMD EPYC; slightly cheaper than N2 |
| T2D | Scale-out workloads | AMD EPYC; high throughput |

### 2.2 Compute-Optimized

| Series | Best For |
|---|---|
| C2 | Single-thread HPC, gaming servers |
| C2D | Highly parallel HPC |
| C3 | Next-generation compute with DDR5 memory |

### 2.3 Memory-Optimized

| Series | Max Memory | Best For |
|---|---|---|
| M1 | 3.8 TB | Large in-memory databases |
| M2 | 12 TB | SAP HANA, large analytics |
| M3 | 30 TB | Largest in-memory workloads |

### 2.4 Accelerator-Optimized

| Series | GPU | Best For |
|---|---|---|
| A2 | NVIDIA A100 | ML training and inference |
| G2 | NVIDIA L4 | Graphics, video transcoding, ML inference |

### 2.5 Custom Machine Types

Custom machine types allow you to specify exact vCPU and memory values:

```bash
# Create a VM with custom machine type: 4 vCPUs, 16 GB RAM
gcloud compute instances create custom-vm \
  --zone=us-central1-a \
  --custom-cpu=4 \
  --custom-memory=16GB \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

Rules for custom machine types:

- Minimum: 1 vCPU
- Memory must be a multiple of 256 MB
- Default: 0.9 GB to 6.5 GB memory per vCPU
- Extended memory: up to 8 GB per vCPU with `--custom-extensions`

---

## Section 3 — Disk Types

### 3.1 Persistent Disk

Persistent Disk (PD) is network-attached block storage. It persists
independently of the VM lifecycle.

| Type | Backing | Use Case |
|---|---|---|
| pd-standard | HDD | Sequential I/O; archives; low-cost storage |
| pd-balanced | SSD | General purpose; boot disks |
| pd-ssd | SSD | Databases; low-latency applications |
| pd-extreme | SSD | Highest IOPS; demanding database workloads |

Persistent Disk properties:

- Can be resized online (increase only; cannot shrink)
- Can be attached to multiple VMs in read-only mode simultaneously
- Maximum size: 64 TB per disk
- Encrypted at rest by default; optionally customer-managed keys (CMEK)

### 3.2 Local SSD

Local SSD is NVMe-based storage physically attached to the host machine.

- 375 GB per partition; up to 24 partitions per VM (9 TB total)
- Very high IOPS and very low latency
- Data is NOT persistent across VM stops, restarts, or live migrations
- Use for: temporary data, caches, scratch space, shuffle storage for Spark

### 3.3 Snapshot Best Practices

Snapshots are incremental backups of persistent disks:

```bash
# Create a snapshot
gcloud compute disks snapshot DISK_NAME \
  --zone=ZONE \
  --snapshot-names=SNAPSHOT_NAME

# Create a disk from a snapshot
gcloud compute disks create NEW_DISK \
  --source-snapshot=SNAPSHOT_NAME \
  --zone=TARGET_ZONE

# List snapshots
gcloud compute snapshots list

# Delete a snapshot
gcloud compute snapshots delete SNAPSHOT_NAME
```

Snapshot storage is billed separately from disk storage.

---

## Section 4 — OS Images and Startup Scripts

### 4.1 Image Types

- **Public images**: Maintained by Google (Debian, Ubuntu, CentOS, RHEL, Windows,
  etc.) or Google Cloud Marketplace partners
- **Custom images**: Created from an existing disk, another image, or a snapshot;
  stored in your project
- **Machine images**: Capture the entire VM state including all disks,
  configuration, and metadata; used for VM cloning and migration

### 4.2 Image Families

Using an image family always references the latest non-deprecated version:

```bash
# Using an image family (recommended)
gcloud compute instances create my-vm \
  --image-family=debian-11 \
  --image-project=debian-cloud

# Using a specific image version (pinned)
gcloud compute instances create my-vm \
  --image=debian-11-bullseye-v20231010 \
  --image-project=debian-cloud
```

### 4.3 Startup Scripts

Startup scripts run automatically when a VM boots.

Delivery methods:

- Inline via `--metadata=startup-script='...'`
- File via `--metadata-from-file=startup-script=script.sh`
- Cloud Storage via `--metadata=startup-script-url=gs://bucket/script.sh`

```bash
# Create VM with startup script from a file
cat > startup.sh << 'EOF'
#!/bin/bash
apt-get update -y
apt-get install -y apache2
systemctl enable apache2
systemctl start apache2
echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html
EOF

gcloud compute instances create web-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --metadata-from-file=startup-script=startup.sh \
  --tags=http-server
```

---

## Section 5 — Instance Groups

### 5.1 Managed Instance Groups (MIGs)

MIGs are the foundation of scalable, highly available Compute Engine deployments.

MIG capabilities:

- **Autoscaling**: Add/remove VMs automatically based on signals
- **Autohealing**: Detect and recreate unhealthy VMs using health checks
- **Load balancing integration**: Native integration with GCP load balancers
- **Rolling updates**: Update the instance template across the group gradually
- **Canary deployments**: Test a new template on a subset of instances first
- **Stateful workloads**: Preserve instance name, disks, and metadata across
  updates (stateful MIGs)

### 5.2 Instance Templates

Instance templates are immutable configuration blueprints for MIG VMs:

```bash
# Create an instance template
gcloud compute instance-templates create web-template \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=20GB \
  --network=default \
  --tags=http-server \
  --metadata-from-file=startup-script=startup.sh

# List templates
gcloud compute instance-templates list

# Describe a template
gcloud compute instance-templates describe web-template
```

### 5.3 Creating and Managing MIGs

```bash
# Create a regional MIG
gcloud compute instance-groups managed create web-mig \
  --template=web-template \
  --size=3 \
  --region=us-central1

# List MIG instances
gcloud compute instance-groups managed list-instances web-mig \
  --region=us-central1

# Update MIG to use a new template (rolling update)
gcloud compute instance-groups managed rolling-action start-update web-mig \
  --version=template=web-template-v2 \
  --region=us-central1 \
  --max-unavailable=1

# Scale the MIG manually
gcloud compute instance-groups managed resize web-mig \
  --size=5 \
  --region=us-central1
```

### 5.4 Autoscaling

```bash
# Set autoscaling policy
gcloud compute instance-groups managed set-autoscaling web-mig \
  --region=us-central1 \
  --max-num-replicas=10 \
  --min-num-replicas=2 \
  --target-cpu-utilization=0.70 \
  --cool-down-period=90

# Remove autoscaling
gcloud compute instance-groups managed stop-autoscaling web-mig \
  --region=us-central1
```

### 5.5 Autohealing

```bash
# Create a health check
gcloud compute health-checks create http web-health-check \
  --port=80 \
  --request-path=/health \
  --check-interval=10 \
  --timeout=5 \
  --healthy-threshold=2 \
  --unhealthy-threshold=3

# Attach health check to MIG
gcloud compute instance-groups managed update web-mig \
  --region=us-central1 \
  --health-check=web-health-check \
  --initial-delay=300
```

---

## Section 6 — Preemptible and Spot VMs

### 6.1 Comparison

| Feature | Regular VM | Preemptible VM | Spot VM |
|---|---|---|---|
| Price | Full price | Up to 91% off | Up to 91% off |
| Can be interrupted | No | Yes (30-sec warning) | Yes (30-sec warning) |
| Max runtime | None | 24 hours | None |
| Live migration | Yes | No | No |
| Auto-restart | Yes | No | No |

### 6.2 Handling Preemption

When GCP preempts a VM, the VM receives a 30-second shutdown signal
(ACPI G2 Soft Off). Best practices:

- Handle the SIGTERM signal and checkpoint work before shutdown
- Design jobs to be resumable from the last checkpoint
- Use a managed instance group to automatically replace preempted VMs

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Machine type | vCPU and memory specification for a VM |
| Machine family | Category of machine types optimized for a workload type |
| Custom machine type | VM with user-specified vCPU and memory values |
| Persistent Disk | Network-attached block storage that persists across VM lifecycle |
| Local SSD | High-performance ephemeral storage physically on the host |
| Snapshot | Incremental point-in-time backup of a persistent disk |
| Image | Bootable disk template used to create a VM boot disk |
| Image family | Pointer to the latest version of an image series |
| Startup script | Script that runs automatically when a VM boots |
| MIG | Managed Instance Group — fleet of identical VMs managed as a unit |
| Instance template | Immutable configuration blueprint for VMs in a MIG |
| Autoscaling | Automatic adjustment of MIG size based on defined signals |
| Autohealing | Automatic VM recreation when a health check detects an unhealthy VM |
| Preemptible VM | Short-lived, low-cost VM that can be interrupted by Google |
| Spot VM | Successor to preemptible VM; same interruption model, no 24-hour limit |

---

## ACE Exam Focus Areas — Module 03

- Recommend the correct machine family for a described workload.
- Explain the difference between a TERMINATED and DELETED instance.
- Identify appropriate disk type for workload I/O requirements.
- Describe when to use local SSD vs. persistent disk.
- Explain why instance templates are immutable and how to update a MIG.
- Choose regional vs. zonal MIG for given availability requirements.
- Identify valid autoscaling signals (CPU, HTTP, Pub/Sub, custom metrics).
- Describe preemptible and Spot VM use cases and limitations.
- Explain the purpose of the autohealing initial delay.

---

## Further Reading

- Compute Engine overview: cloud.google.com/compute/docs
- Machine families: cloud.google.com/compute/docs/machine-resource
- Disk types: cloud.google.com/compute/docs/disks
- Instance groups: cloud.google.com/compute/docs/instance-groups
- Preemptible VMs: cloud.google.com/compute/docs/instances/preemptible
- Spot VMs: cloud.google.com/compute/docs/instances/spot

## 9. Supplemental Resources

**1. Google Cloud Documentation — Compute Engine Machine Families**
<https://cloud.google.com/compute/docs/machine-resource>
Complete reference for all machine families (E2, N2, C2, M2, A2, etc.),
including vCPU/memory ranges, supported features, and guidance on choosing
the right family for your workload type.

**2. Google Cloud Skills Boost — Creating Virtual Machines**
<https://www.cloudskillsboost.google/focuses/3563>
Hands-on lab covering VM creation with various machine types, disk
configurations, and startup scripts. Includes tasks on instance groups and
autoscaling directly relevant to the ACE exam.

**3. Google Cloud Documentation — Managed Instance Groups**
<https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances>
Official guide covering MIG creation, rolling updates, autohealing, and
autoscaling configuration with detailed examples for both zonal and regional
MIG deployments.
