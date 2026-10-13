# Video Script: Module 03 — Compute Engine (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Recap and Agenda (1 minute)

Welcome back. In Part 1 we covered VM anatomy, machine families, disk types,
images, and startup scripts. In Part 2 we cover:

- Managed and unmanaged instance groups
- Autoscaling policies
- Preemptible and Spot VMs
- Console and gcloud CLI for Compute Engine
- ACE exam strategy for Compute Engine questions

---

## Segment 2 — Instance Groups (4 minutes)

### Why Instance Groups?

A single VM is a single point of failure. Instance groups let you manage
multiple VMs as a single unit, enabling high availability, load balancing, and
autoscaling.

### Managed Instance Groups (MIGs)

A Managed Instance Group (MIG) creates and manages identical VM instances based
on an instance template. Key capabilities:

- **Autoscaling** — Automatically add or remove VMs based on load
- **Autohealing** — Detects unhealthy VMs and automatically recreates them
- **Load balancing** — Integrates with GCP load balancers
- **Rolling updates** — Update the instance template and roll changes across
  the group with minimal downtime
- **Multi-zone deployment** — Spread instances across multiple zones for HA

Types of MIGs:

- **Zonal MIG** — All instances in one zone; single zone failure takes down the
  group
- **Regional MIG** — Instances spread across all zones in a region; survives
  individual zone failures; recommended for production

### Instance Templates

An instance template defines the configuration for all VMs in a MIG:

- Machine type
- Boot disk image and size
- Network and subnet
- Service account
- Metadata (including startup scripts)
- Labels and tags

Instance templates are immutable — you cannot edit them. To change the
configuration, create a new template and update the MIG to use it.

```bash
# Create an instance template
gcloud compute instance-templates create web-template \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=20GB \
  --metadata=startup-script='#!/bin/bash
apt-get update && apt-get install -y nginx
systemctl start nginx'

# Create a regional MIG using the template
gcloud compute instance-groups managed create web-mig \
  --template=web-template \
  --size=3 \
  --region=us-central1
```

### Unmanaged Instance Groups

An unmanaged instance group is a collection of heterogeneous VM instances that
you manage manually. They do not support autoscaling or autohealing. Use cases:

- Load balancing across VMs with different configurations
- Legacy workloads that cannot use identical instance templates

**ACE Exam Tip:** The ACE exam almost always prefers managed instance groups
over unmanaged for new architectures. Know the MIG capabilities (autoscaling,
autohealing, rolling updates) and when to use zonal vs. regional MIGs.

---

## Segment 3 — Autoscaling (3 minutes)

### Autoscaling Policies

A MIG autoscaler adds or removes VMs based on metrics. Supported scaling
signals include:

- **CPU utilization** — Scale when average CPU across the group exceeds a
  threshold (e.g., scale up when CPU > 70%)
- **HTTP load balancing serving capacity** — Scale based on requests per second
  or utilization
- **Cloud Monitoring metrics** — Use any custom metric for scaling
- **Cloud Pub/Sub queue depth** — Scale based on the number of unprocessed
  messages in a Pub/Sub subscription
- **Schedule-based scaling** — Set minimum instances for specific time windows

### Autoscaling Configuration

```bash
# Enable autoscaling on a MIG
gcloud compute instance-groups managed set-autoscaling web-mig \
  --region=us-central1 \
  --max-num-replicas=10 \
  --min-num-replicas=2 \
  --target-cpu-utilization=0.70 \
  --cool-down-period=90
```

Key parameters:

- `--min-num-replicas` — Never scale below this count (floor for availability)
- `--max-num-replicas` — Never scale above this count (ceiling for cost control)
- `--target-cpu-utilization` — Target average CPU as a decimal (0.70 = 70%)
- `--cool-down-period` — Seconds to wait after scaling before evaluating again

### Autohealing

Autohealing monitors VM health using a health check and recreates unhealthy
instances. Configure it on the MIG with a health check:

```bash
# Create a health check
gcloud compute health-checks create http web-health-check \
  --port=80 \
  --request-path=/health

# Set autohealing policy on the MIG
gcloud compute instance-groups managed update web-mig \
  --region=us-central1 \
  --health-check=web-health-check \
  --initial-delay=300
```

The `--initial-delay` gives newly started VMs time to complete startup before
health checks begin. Without it, newly started VMs may be recreated before
they finish booting.

---

## Segment 4 — Preemptible and Spot VMs (2 minutes)

### Preemptible VMs

Preemptible VMs are short-lived VM instances available at up to 91% discount.
GCP can terminate (preempt) them at any time with a 30-second warning when it
needs the capacity back.

Constraints:

- Maximum runtime of 24 hours (then automatically terminated)
- Cannot be live-migrated
- Cannot be set to automatically restart on maintenance

Use cases:

- Batch processing jobs
- Data pipelines
- Scientific simulations
- Fault-tolerant distributed workloads

### Spot VMs

Spot VMs replaced preemptible VMs as the recommended short-lived VM type.
Key difference: Spot VMs have no maximum 24-hour runtime limit. Otherwise
similar pricing and constraints.

```bash
# Create a preemptible VM
gcloud compute instances create batch-vm \
  --zone=us-central1-a \
  --machine-type=n2-standard-4 \
  --preemptible

# Create a Spot VM (preferred)
gcloud compute instances create batch-vm-spot \
  --zone=us-central1-a \
  --machine-type=n2-standard-4 \
  --provisioning-model=SPOT
```

**ACE Exam Tip:** If a question describes a batch or fault-tolerant workload
where interruptions are acceptable and cost is a priority, the answer involves
preemptible or Spot VMs. If the workload must run continuously without
interruption, preemptible VMs are not appropriate.

---

## Segment 5 — Console and gcloud CLI Walkthrough (4 minutes)

### Creating a VM in the Console

1. Navigate to **Compute Engine > VM Instances**.
2. Click **Create Instance**.
3. Configure:
   - **Name**: `lab03-web-vm`
   - **Region/Zone**: `us-central1 / us-central1-a`
   - **Machine configuration**: E2, e2-medium
   - **Boot disk**: Debian 11, 10 GB pd-balanced
   - **Firewall**: Allow HTTP and HTTPS traffic
4. Click **Create**.

### Key gcloud Compute Commands

```bash
# Create a VM
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --boot-disk-size=20GB \
  --tags=http-server

# List instances
gcloud compute instances list

# Describe an instance
gcloud compute instances describe my-vm --zone=us-central1-a

# SSH into an instance
gcloud compute ssh my-vm --zone=us-central1-a

# Stop and start
gcloud compute instances stop my-vm --zone=us-central1-a
gcloud compute instances start my-vm --zone=us-central1-a

# Delete
gcloud compute instances delete my-vm --zone=us-central1-a

# Create a snapshot
gcloud compute disks snapshot my-vm \
  --zone=us-central1-a \
  --snapshot-names=my-vm-snapshot-$(date +%Y%m%d)

# Create a disk from a snapshot
gcloud compute disks create restored-disk \
  --source-snapshot=my-vm-snapshot-20260101 \
  --zone=us-central1-a
```

### Checking Startup Script Logs

```bash
# SSH in and view startup script output
gcloud compute ssh my-vm --zone=us-central1-a
# Then inside the VM:
sudo journalctl -u google-startup-scripts.service
# Or:
sudo cat /var/log/syslog | grep startup-script
```

---

## Segment 6 — ACE Exam Strategy for Compute Engine (1 minute)

Top ACE exam patterns for Module 03:

- **Machine family selection**: Match the described workload characteristics
  to the right family. Memory-heavy → M2. GPU/ML → A2. Cost-sensitive → E2.
- **Managed vs. unmanaged instance groups**: New architectures always use MIGs.
- **Zonal vs. regional MIG**: Regional MIGs are recommended for production HA.
- **Preemptible/Spot VM use cases**: Batch, fault-tolerant, cost-sensitive.
  Never use for continuous/critical workloads.
- **Autohealing initial delay**: Know why it matters.
- **Instance templates are immutable**: To change config, create a new template.
- **Terminated vs. deleted**: Terminated VMs still exist; you are still billed
  for their persistent disks.

---

## Summary — Module 03

Across both parts we covered:

- VM anatomy, lifecycle states, and billing
- Machine families and custom machine types
- Disk types: standard, balanced, SSD, extreme, local SSD
- Snapshots for backup and migration
- OS images, custom images, and startup scripts
- Managed instance groups: templates, autoscaling, autohealing, rolling updates
- Zonal vs. regional MIGs
- Preemptible and Spot VMs: economics and use cases
- Console and gcloud CLI for all of the above

The lab will have you create VMs, configure a managed instance group with
autoscaling, and test startup scripts.

---

End of Part 2 — Module 03

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/compute/docs
