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
