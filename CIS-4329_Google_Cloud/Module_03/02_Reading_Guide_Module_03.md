# Reading Guide — Module 03

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Compute Engine — VM Instances and Machine Types

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

Compute Engine is GCP's Infrastructure as a Service offering and a major ACE exam domain. This reading guide covers machine families, disk types, pricing models, managed instance groups, and the gcloud commands for VM lifecycle management. Study every section — the ACE exam tests both conceptual knowledge (which machine type for which workload) and CLI knowledge (correct flags and command syntax).

---

## 1. Machine Families

### General-Purpose Families

| Family | Processor | Best For | Notes |
|---|---|---|---|
| E2 | Variable (shared core) | Dev, low-traffic web, cost-sensitive | Lowest cost; shared CPU scheduling |
| N1 | Intel Skylake/Broadwell | Legacy general workloads | Older generation; still widely used |
| N2 | Intel Cascade Lake | Production web apps, mid-tier databases | Higher sustained performance than E2 |
| N2D | AMD EPYC Rome/Milan | Same as N2, AMD hardware | Often slightly cheaper than N2 |
| T2D | AMD EPYC Milan | Scale-out, web serving | Good price-performance for horizontal scale |

### Compute-Optimized Families

| Family | Best For | Key Characteristic |
|---|---|---|
| C2 | HPC, game servers, scientific simulation | Highest per-core performance (Intel) |
| C2D | Same as C2, AMD hardware | AMD EPYC, high frequency |

### Memory-Optimized Families

| Family | RAM Range | Best For |
|---|---|---|
| M2 | Up to 12 TB | SAP HANA, large in-memory databases |
| M3 | Up to 3.8 TB | In-memory analytics, large caches |

### Accelerator-Optimized Family

The A2 family includes NVIDIA GPUs. Used for machine learning training, inference, and GPU compute. Not covered in depth on the standard ACE exam but worth knowing exists.

### Custom Machine Types

You can create a custom machine type with any combination of vCPU count and memory, within certain limits. This allows you to fit a VM precisely to workload requirements without paying for excess capacity. Custom types are available in most N-series families.

```bash
gcloud compute instances create custom-vm \
  --zone=us-central1-a \
  --custom-cpu=6 \
  --custom-memory=12GB
```

---

## 2. Disk Storage Types

### Persistent Disk Types

| Type | Identifier | Technology | Best For | IOPS |
|---|---|---|---|---|
| Standard | pd-standard | HDD | Batch, sequential I/O | Low |
| Balanced | pd-balanced | SSD | General production workloads | Medium |
| SSD | pd-ssd | SSD | High-transaction databases | High |
| Extreme | pd-extreme | SSD | Maximum I/O, very high-TPS databases | Highest |

All persistent disk types share these properties:

- Network-attached (not physically on the VM's host machine)
- Data survives VM stop, restart, and deletion (unless deleted explicitly)
- Can be resized online (increase only — no decrease)
- Can be attached to multiple VMs in read-only mode
- Encrypted at rest by default with Google-managed keys

### Local SSD

| Property | Value |
|---|---|
| Interface | NVMe (fast) |
| Performance | Highest IOPS available in GCP |
| Persistence | Ephemeral — data lost on VM stop/crash/migration |
| Attachment | Fixed at VM creation time |
| Size | 375 GB per disk; up to 24 disks per VM |
| Best For | Scratch data, temp caches, data reconstructable from persistent storage |

Local SSDs cannot be detached and re-attached to another VM. They are tied to the VM's physical host.

### Disk Persistence Summary

| Storage Type | VM Stop | VM Delete | VM Live Migration |
|---|---|---|---|
| Persistent Disk | Data preserved | Data preserved (disk not deleted unless requested) | No impact |
| Local SSD | Data LOST | Data LOST | Data LOST |

---

## 3. Snapshots and Custom Images

### Snapshots

| Property | Value |
|---|---|
| Purpose | Point-in-time backup of a persistent disk |
| Storage location | Cloud Storage (managed by GCP) |
| Incremental | Yes — first snapshot is full; subsequent are incremental |
| Cross-region | Yes — can restore to a different zone or region |
| Consistent | Best taken from a stopped disk; application-consistent snapshots require quiescing writes |
| gcloud command | `gcloud compute disks snapshot DISK --snapshot-names=NAME` |

### Custom Images

| Property | Value |
|---|---|
| Purpose | Bootable disk image template for fleet deployment |
| Source | Existing disk, snapshot, another image, or RAW file in Cloud Storage |
| Scope | Available across the project (or organization with shared image families) |
| Families | Images can be grouped into families; the latest image in a family is returned by `--image-family` |
| gcloud command | `gcloud compute images create NAME --source-disk=DISK` |

### Snapshot vs. Custom Image Decision

| Scenario | Correct Tool |
|---|---|
| Backup disk before a risky software upgrade | Snapshot |
| Disaster recovery restore point | Snapshot |
| Deploy 100 identical pre-configured VMs | Custom Image |
| Share a golden OS configuration with another team | Custom Image |
| Restore a disk to a previous state | Snapshot |

---

## 4. Pricing Models

### On-Demand Pricing

Pay per second (minimum 1 minute) for the machine type at the standard rate. No commitment, fully flexible.

### Committed Use Discounts

| Commitment | Discount vs. On-Demand | Notes |
|---|---|---|
| 1 year | ~37% | Billed monthly regardless of usage |
| 3 year | ~57% | Billed monthly regardless of usage |

Commitment types:

- Resource-based: commit to vCPU/memory in a region; any matching VM gets the discount
- Spend-based: commit to a minimum spend per hour; applies to certain services

### Spot VMs

| Property | Value |
|---|---|
| Discount | Up to 91% vs. on-demand |
| Risk | Can be preempted by Google at any time |
| Notice | 30-second shutdown notice before preemption |
| Max runtime | 24 hours per session |
| Best for | Fault-tolerant batch jobs, ML training, video processing, data pipelines |
| Avoid for | Databases, web servers, any stateful service requiring continuous availability |

### Sustained Use Discounts

Automatically applied to on-demand N1, N2, N2D, and E2 VMs. No commitment needed. If a VM runs for more than 25% of the month, a discount is automatically applied. Runs at full month: discount up to 30%. These do NOT apply to committed use instances or Spot VMs.

---

## 5. Managed Instance Groups (MIGs)

### MIG Architecture

```text
Instance Template (defines VM spec)
        |
Managed Instance Group (manages fleet)
        |
  +-----------+-----------+
  |           |           |
 VM-1        VM-2        VM-3
  (us-central1-a) (us-central1-b) (us-central1-c)
```

### MIG Capabilities

| Feature | Description |
|---|---|
| Autoscaling | Adds/removes VMs based on CPU, LB capacity, or custom metrics |
| Autohealing | Replaces unhealthy VMs automatically based on health check results |
| Rolling updates | Deploys new instance templates one batch at a time without downtime |
| Blue-green deployment | Create two MIGs, shift traffic with load balancer, then delete old MIG |
| Stateful MIGs | Preserve per-instance disks and network IPs across updates (for stateful workloads) |
| Regional MIGs | Span multiple zones in a region for zone-failure resilience |

### Instance Templates

An instance template is a reusable definition for VM properties:

- Machine type
- Boot disk image and type
- Network and subnet
- Network tags
- Service account
- Startup script metadata

Instance templates are immutable after creation. To update a MIG's configuration, create a new template and apply it via rolling update.

---

## 6. gcloud compute Command Reference

### Instance Lifecycle

| Command | Description |
|---|---|
| `gcloud compute instances create NAME --zone=Z --machine-type=TYPE` | Create a VM |
| `gcloud compute instances list` | List all VMs in the project |
| `gcloud compute instances describe NAME --zone=Z` | Show VM details |
| `gcloud compute instances start NAME --zone=Z` | Start a stopped VM |
| `gcloud compute instances stop NAME --zone=Z` | Stop a running VM |
| `gcloud compute instances delete NAME --zone=Z` | Delete a VM |
| `gcloud compute ssh NAME --zone=Z` | SSH into a VM |
| `gcloud compute instances add-metadata NAME --metadata=KEY=VALUE` | Add or update metadata |

### Disk Operations

| Command | Description |
|---|---|
| `gcloud compute disks list` | List all disks in the project |
| `gcloud compute disks snapshot DISK --snapshot-names=NAME` | Create a snapshot |
| `gcloud compute disks create NAME --source-snapshot=SNAP --zone=Z` | Create disk from snapshot |
| `gcloud compute disks resize NAME --size=SIZE_GB --zone=Z` | Increase disk size |

### Image Operations

| Command | Description |
|---|---|
| `gcloud compute images list --filter="family:debian"` | List Debian public images |
| `gcloud compute images create NAME --source-disk=DISK --source-disk-zone=Z` | Create custom image from disk |
| `gcloud compute images deprecate NAME --state=DEPRECATED` | Mark image as deprecated |

### Instance Template and MIG

| Command | Description |
|---|---|
| `gcloud compute instance-templates create TEMPLATE --machine-type=TYPE --image-family=IMG --image-project=PRJ` | Create instance template |
| `gcloud compute instance-groups managed create MIG --template=TEMPLATE --size=N --zone=Z` | Create zonal MIG |
| `gcloud compute instance-groups managed set-autoscaling MIG --max-num-replicas=10 --target-cpu-utilization=0.6` | Configure autoscaling |

---

## 7. Startup Script Reference

### Passing a Script Inline

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --metadata=startup-script='#!/bin/bash
  apt-get update && apt-get install -y nginx'
```

### Passing a Script from Cloud Storage

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --metadata=startup-script-url=gs://my-bucket/setup.sh
```

### Viewing Startup Script Output

```bash
gcloud compute instances get-serial-port-output my-vm --zone=us-central1-a
```

The serial port output captures all boot-time console messages including startup script output. Useful for debugging failed startups.

---

## 8. ACE Exam Tips

1. Spot VMs are for fault-tolerant batch workloads only. Signal words in ACE questions: "fault-tolerant," "retryable," "batch," "can restart." Disqualifying words: "database," "web server," "must remain available," "stateful."

2. Persistent disk data survives VM deletion unless you check "Delete boot disk when instance is deleted." Local SSD data is always lost on VM stop or deletion.

3. Custom images are for fleet deployment; snapshots are for backup and restore. If the scenario says "roll back," choose snapshot. If it says "deploy identical VMs," choose custom image.

4. The default Compute Engine service account has `roles/editor`. Creating a VM without specifying a service account will use this default — a security concern in production.

5. Committed use discounts (CUDs) require no machine-type lock-in for resource-based CUDs. You commit to vCPU and memory in a region and any matching VM gets the discount automatically.

6. Regional MIGs span multiple zones and survive zone failures. Zonal MIGs are in a single zone and do not survive zone failures.

7. The `--image-family` flag with `gcloud compute instances create` automatically selects the latest image in the family. Use this instead of hardcoding specific image versions to ensure you always get security patches.

8. MIG autohealing requires a health check. Without a configured health check, autohealing does not know when a VM is unhealthy and cannot replace it.

---

## 9. Study Checklist

- [ ] Name the four main machine families and their use cases without notes
- [ ] Explain the difference between pd-standard, pd-balanced, pd-ssd, and local SSD
- [ ] State what happens to persistent disk data and local SSD data when a VM is stopped
- [ ] Explain the difference between a snapshot and a custom image with a real scenario for each
- [ ] Describe when to use Spot VMs and when not to
- [ ] Explain the three types of compute pricing models: on-demand, committed use, spot
- [ ] Describe the four capabilities MIGs provide: autoscaling, autohealing, rolling updates, multi-zone
- [ ] Run `gcloud compute instances create` with machine type and zone flags
- [ ] Run `gcloud compute disks snapshot` on a VM's disk
- [ ] Run `gcloud compute images create` from a disk
- [ ] Complete the Module 03 lab
- [ ] Take the Module 03 quiz
- [ ] Post your Module 03 discussion response

---

End of Reading Guide — Module 03

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn
