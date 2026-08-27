# Quiz: Module 03 — Compute Engine

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers machine families, disk types, instance groups, autoscaling,
startup scripts, snapshots, and preemptible VMs.

---

## Question 1

A company needs to run SAP HANA, an in-memory database platform that requires
12 TB of RAM in a single node. Which GCP machine family is the correct choice?

- A) E2 — cost-optimized general purpose
- B) C2 — compute-optimized
- C) M2 — memory-optimized
- D) A2 — accelerator-optimized

**Correct Answer:** C

**Explanation:** The M2 memory-optimized machine family supports up to 12 TB of
memory and is specifically designed for SAP HANA and large in-memory database
workloads. E2 machines are for general-purpose and cost-sensitive workloads. C2
machines are compute-intensive but not memory-intensive. A2 machines are for
GPU-accelerated ML workloads.

---

## Question 2

A VM instance has been stopped (TERMINATED state). Which of the following
statements is correct?

- A) The VM and its boot disk are immediately deleted
- B) The VM continues to be billed at the full running rate
- C) The persistent boot disk still exists and is billed for storage
- D) The VM is automatically deleted after 7 days if not restarted

**Correct Answer:** C

**Explanation:** A TERMINATED VM still exists — it is not deleted. Its persistent
boot disk remains and incurs storage charges. Compute charges stop when the VM
is terminated, but storage charges for attached disks continue. The VM can be
restarted at any time and is not automatically deleted.

---

## Question 3

You are designing a web application that must remain available if a single
zone in us-central1 goes down. Which instance group configuration satisfies
this requirement at minimum cost?

- A) A zonal MIG in us-central1-a with 3 instances
- B) A regional MIG in us-central1 spanning all zones
- C) Three separate zonal MIGs, one in each zone
- D) A single VM with a static external IP

**Correct Answer:** B

**Explanation:** A regional MIG automatically distributes instances across all
zones in the region. If one zone fails, the instances in the other zones continue
serving traffic. A zonal MIG (option A) concentrates all instances in one zone
and would fail entirely on a zone outage. Three separate zonal MIGs (option C)
could work but adds unnecessary management complexity compared to a single
regional MIG.

---

## Question 4

An instance template has been used to create a managed instance group. You need
to change the machine type from e2-medium to e2-standard-4 for all instances
in the group. What is the correct procedure?

- A) Edit the existing instance template to change the machine type
- B) Create a new instance template with e2-standard-4 and perform a rolling
     update on the MIG to use the new template
- C) Stop all instances in the MIG and change their machine types individually
- D) Delete the MIG, delete the template, and recreate both from scratch

**Correct Answer:** B

**Explanation:** Instance templates are immutable — they cannot be edited after
creation. The correct process is to create a new instance template with the
desired configuration, then perform a rolling update on the MIG to gradually
replace instances with the new template. This achieves the change with minimal
downtime.

---

## Question 5

Which disk type offers the highest I/O performance but loses all data when the
VM is stopped or live-migrated?

- A) pd-extreme
- B) pd-ssd
- C) Local SSD
- D) Hyperdisk

**Correct Answer:** C

**Explanation:** Local SSD is physically attached to the host machine and offers
the highest IOPS and lowest latency of any GCP disk type. However, it is
ephemeral — data is not preserved if the VM stops, terminates, or is
live-migrated. pd-extreme (option A) is the highest-performance persistent disk
but survives VM stops. Persistent disks are always network-attached.

---

## Question 6

A data engineering team runs nightly batch jobs that process large datasets.
The jobs are designed to checkpoint progress every 10 minutes and retry failed
tasks automatically. The team wants to minimize compute costs. What VM type
should they use?

- A) N2 standard VMs with committed use discounts
- B) E2 VMs with sustained use discounts
- C) Spot VMs
- D) M2 memory-optimized VMs

**Correct Answer:** C

**Explanation:** Spot VMs offer up to 91% cost reduction compared to regular VMs.
Because the batch jobs are fault-tolerant (checkpoint every 10 minutes, retry
failed tasks), they can absorb the interruptions that Spot VMs may experience.
This is the textbook use case for Spot VMs. Committed use discounts (option A)
require a 1–3 year commitment and are better for always-on workloads.

---

## Question 7

You are configuring autohealing on a managed instance group that runs a web
application. The startup script takes about 4 minutes to complete. What should
the `--initial-delay` parameter be set to, at minimum?

- A) 0 seconds (health checks should start immediately)
- B) 30 seconds
- C) 240 seconds (4 minutes)
- D) 600 seconds (10 minutes)

**Correct Answer:** C

**Explanation:** The `--initial-delay` gives newly created instances time to
complete initialization before health checks begin. If the delay is shorter than
the startup time, the health check may mark the VM as unhealthy before it is
ready, triggering an unnecessary recreation. Setting the initial delay to at
least the startup script duration (240 seconds for a 4-minute startup) prevents
this.

---

## Question 8

Which autoscaling signal would be most appropriate for a MIG that processes
messages from a queue, where scaling should be based on backlog depth?

- A) CPU utilization target
- B) HTTP load balancing serving capacity
- C) Cloud Pub/Sub subscription backlog (undelivered message count)
- D) Cloud Monitoring custom memory metric

**Correct Answer:** C

**Explanation:** Pub/Sub subscription backlog depth is a supported autoscaling
signal for MIGs. When the number of undelivered messages increases, the
autoscaler adds VMs to process the backlog faster. When the backlog decreases,
VMs are removed. This is more accurate than CPU utilization for queue-based
workloads where VMs may be waiting for messages and thus show low CPU usage.

---

## Question 9

You need to create a VM with 6 vCPUs and 10 GB of RAM. No predefined machine
type matches these exact specifications. What should you do?

- A) Choose the nearest predefined machine type that exceeds these requirements
- B) Use a custom machine type to specify exactly 6 vCPUs and 10 GB
- C) Use two E2 machines and split the workload
- D) Custom machine types are not supported on Compute Engine

**Correct Answer:** B

**Explanation:** Compute Engine custom machine types allow you to specify any
vCPU count and memory combination within the allowed ranges. A custom machine
type with 6 vCPUs and 10 GB RAM avoids over-provisioning the memory that a
predefined n2-standard-8 (8 vCPUs, 32 GB) would provide. Custom machine types
cost slightly more per unit than predefined types but can save money overall
by avoiding unused capacity.

---

## Question 10

A snapshot is taken of a 500 GB persistent disk that has 200 GB of data
written to it. The snapshot is the first snapshot taken of this disk. How
large is the snapshot?

- A) 500 GB (full disk size)
- B) 200 GB (only data that has been written)
- C) 0 GB (snapshots are free)
- D) 50 GB (snapshots always compress to 25% of disk size)

**Correct Answer:** B

**Explanation:** The first snapshot of a disk captures only the bytes that have
actually been written (allocated), not the full provisioned disk size. For a
500 GB disk with 200 GB of data, the first snapshot is approximately 200 GB.
Subsequent snapshots are incremental — they capture only the changes since the
last snapshot.

---

End of Quiz — Module 03

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

You need to attach an additional persistent disk to a running Compute Engine VM
without stopping it. Which statement about this operation is correct?

- A) Additional disks can only be attached when the VM is in TERMINATED state
- B) Additional persistent disks can be attached to a running VM with no downtime
- C) Only Local SSD disks can be added to a running VM
- D) Adding a disk automatically resizes the boot disk to accommodate the new storage

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Stopping the VM is not required; GCP supports hot-attaching additional persistent disks to running instances.
  - C) Local SSD must be attached at VM creation time; it cannot be added to a running VM. Persistent disks are the type that supports hot-attach.
  - D) Attaching a new disk creates a separate block device; it has no effect on the size of the existing boot disk.

---

### Question 12 (5 points)

A VM instance is live-migrated by Google during a host maintenance event.
What is the user-visible impact during a successful live migration?

- A) The VM is rebooted and the startup script runs again
- B) The VM experiences a brief pause of a few seconds but remains in RUNNING
   state throughout; no restart occurs
- C) The VM is terminated and a new VM is created in a different zone
- D) The VM's external IP address changes after migration

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Live migration does not reboot the VM; the OS and processes continue running. The startup script does not re-execute.
  - C) Live migration moves the running VM to a new host without termination. Creating a new VM in a different zone describes a different operation entirely.
  - D) External IP addresses (static or ephemeral) are not affected by live migration; the VM retains its network configuration.

---

### Question 13 (5 points)

An instance template specifies `--image-family=debian-11`. Six months later,
Google releases a new Debian 11 patch image. What happens to VMs created
from this template after the new image is published?

- A) Existing VMs in the MIG are automatically updated to the new image
- B) New VMs created from the template use the latest Debian 11 image at
   creation time; existing VMs are unaffected
- C) The template becomes invalid and must be recreated with the new image
- D) The template pins to the exact image available at template creation time
   and never references newer images

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) MIG instances are not automatically re-imaged when a new image is published; a rolling update must be explicitly initiated.
  - C) Templates using image families remain valid indefinitely; they resolve to the latest non-deprecated image in the family at VM creation time.
  - D) Image families are dynamic pointers to the latest image, not pins to a specific image version. To pin, you must specify a full image name (e.g., `debian-11-bullseye-v20231010`) rather than the family name.

---

### Question 14 (5 points)

A managed instance group is configured with a maximum of 10 instances and a
target CPU utilization of 70%. Current CPU utilization drops to 15% and stays
there for the entire cool-down period. What does the autoscaler do?

- A) Immediately terminates all instances except the minimum
- B) Does nothing — the autoscaler only scales up, not down
- C) Gradually removes instances until CPU utilization returns to approximately
   70% or the minimum instance count is reached
- D) Converts remaining instances to preemptible VMs to reduce cost

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) The autoscaler scales down incrementally, not all at once. It also respects the configured minimum instance count and cool-down period.
  - B) The GCP autoscaler scales both up and down based on the configured signal; scale-down is a core feature.
  - D) The autoscaler only changes instance count; it never changes the instance type or provisioning model of existing VMs.

---

### Question 15 (5 points)

What is the maximum size of a single persistent disk that can be attached to
a Compute Engine VM?

- A) 10 TB
- B) 32 TB
- C) 64 TB
- D) 100 TB

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) 10 TB is well below the actual limit; this figure is not a documented GCE limit.
  - B) 32 TB is incorrect; the maximum for a single persistent disk is 64 TB.
  - D) 100 TB exceeds the single-disk limit; to achieve this total capacity you would need to attach multiple disks or use a distributed storage solution.

---

### Question 16 (5 points)

A VM is running a stateful application. The team wants to take a daily
snapshot for backup purposes. Which approach minimizes the snapshot size
on day 2 and beyond?

- A) Delete the previous snapshot before creating each new one to save space
- B) GCP snapshots are incremental by default — each snapshot after the first
   captures only the blocks that changed since the last snapshot
- C) Use full snapshots each day to ensure data integrity; incremental snapshots
   are not supported on pd-ssd
- D) Compress the disk before snapshotting to reduce the stored size

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Deleting the previous snapshot before creating a new one would make each new snapshot a full snapshot, increasing both snapshot time and storage cost.
  - C) GCP snapshots are always incremental after the first; full snapshots are not a separate option, and incremental snapshots are fully supported on all persistent disk types including pd-ssd.
  - D) There is no pre-snapshot disk compression step; GCP's snapshot system handles data efficiency automatically at the storage layer.

---

### Question 17 (5 points)

A developer creates a VM with `--no-address` flag to omit the external IP.
The VM needs to download packages from the internet using `apt-get`. What
must be configured to allow this outbound internet access?

- A) The VM automatically receives internet access through the internal VPC
   network regardless of external IP assignment
- B) Cloud NAT must be configured on the subnet's region to provide outbound
   internet access for VMs without external IPs
- C) A VPN tunnel must be established to route internet traffic
- D) The VM must be assigned a static internal IP to access the internet

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) VMs without external IPs cannot initiate outbound connections to the internet unless Cloud NAT or a proxy is configured; the internal VPC network provides only private connectivity.
  - C) A VPN tunnel connects to on-premises or other cloud networks, not to the general internet; Cloud NAT is the correct solution for outbound internet from private VMs.
  - D) Internal IP addresses are private RFC 1918 addresses and are not routable on the public internet; having a static internal IP does not grant internet access.

---

### Question 18 (5 points)

Which of the following correctly describes the difference between a
machine image and a snapshot in Compute Engine?

- A) A snapshot captures the full VM state including CPU registers; a machine
   image captures only disk data
- B) A machine image captures the complete VM configuration including all
   attached disks, metadata, and network settings; a snapshot captures only
   one persistent disk
- C) Snapshots can be used to create new VMs directly; machine images cannot
- D) Machine images and snapshots are interchangeable terms for the same
   feature

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Neither snapshots nor machine images capture live CPU register state; live migration handles in-flight process state, not backup tools.
  - C) Both snapshots and machine images can be used to create new VMs; a snapshot is used as a source disk, while a machine image creates a complete VM replica including all disks.
  - D) They are distinct features: machine images are for full VM cloning/migration scenarios while snapshots are for disk-level backup and disk creation.

---

### Question 19 (5 points)

A production web application runs in a regional MIG across `us-central1-a`,
`us-central1-b`, and `us-central1-c`. Zone `us-central1-b` goes down. What
happens to the instances that were running in that zone?

- A) All instances in the MIG are immediately terminated for safety
- B) The MIG detects the zone outage and recreates the affected instances in
   the remaining healthy zones to maintain the target instance count
- C) Traffic is automatically rerouted but no new instances are created until
   the zone recovers
- D) The MIG enters a degraded state and requires manual intervention to
   redistribute instances

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The MIG does not terminate healthy instances in other zones during a single-zone outage; only the affected zone's instances are impacted.
  - C) A regional MIG actively works to maintain the target instance count; it creates replacement instances in available zones rather than waiting passively.
  - D) Regional MIGs handle zone failures automatically without manual intervention; this self-healing behavior is a primary reason to use regional over zonal MIGs.

---

### Question 20 (5 points)

You create a Spot VM for a batch workload. The VM is preempted after 2 hours.
What is billed for those 2 hours?

- A) Full on-demand pricing for 2 hours — preemption discounts only apply if
   the VM runs for at least 1 hour
- B) Spot VM pricing for 2 hours, subject to a 1-minute minimum billing
- C) Nothing — preempted VMs are not billed for any usage
- D) A preemption penalty fee in addition to the Spot VM usage charges

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Spot VM pricing applies for the entire duration the VM ran; there is no minimum runtime threshold before discounts apply.
  - C) Spot VMs are billed for the time they run at the Spot price; you pay for the 2 hours of compute usage even though the VM was preempted.
  - D) There is no preemption penalty fee; GCP does not charge extra when it reclaims a Spot VM.
