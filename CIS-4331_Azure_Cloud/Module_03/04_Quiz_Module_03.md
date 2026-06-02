# Quiz: Module 03 - Azure Virtual Machines and Scale Sets

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A developer stops an Azure Virtual Machine from within the guest operating system using the `shutdown` command. What is the billing impact of this action?

- A) Compute, storage, and networking billing all stop immediately
- B) All billing stops because the VM is powered off
- C) Compute billing continues; storage billing continues; only networking egress billing stops
- D) Compute billing continues at the full rate; storage billing continues; compute billing only stops after deallocating the VM

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* Shutting down the OS (guest shutdown or `az vm stop`) puts the VM in a "Stopped" power state but does not release the compute allocation on the physical host. Azure continues billing for compute at the full hourly rate. Storage disk billing also continues. Only `az vm deallocate` (or the Portal "Stop" button which deallocates) stops compute billing.
- *Why A is incorrect:* Compute billing does not stop with a guest OS shutdown. Only deallocation stops compute billing.
- *Why B is incorrect:* Power-off without deallocation does not stop billing. The physical compute resources remain reserved for the VM.
- *Why C is incorrect:* The description is incomplete and misleading. Compute billing continues in full — it is not just networking that continues billing.

---

## Question 2

Which Azure VM size family is most appropriate for an in-memory analytics workload that requires 512 GB of RAM and moderate CPU?

- A) Compute Optimized (F-series)
- B) General Purpose (D-series)
- C) Memory Optimized (E or M series)
- D) Storage Optimized (L-series)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Memory Optimized VM families (E and M series) provide high memory-to-CPU ratios, making them ideal for memory-intensive workloads like in-memory databases, large caches, and analytics that hold large datasets in RAM. 512 GB RAM requirements are specifically served by the M-series.
- *Why A is incorrect:* Compute Optimized (F-series) provides high CPU-to-memory ratio — the opposite of what a high-RAM, moderate-CPU workload needs.
- *Why B is incorrect:* General Purpose (D-series) has a balanced CPU-to-memory ratio. It is not optimized for extreme memory requirements like 512 GB.
- *Why D is incorrect:* Storage Optimized (L-series) is designed for high disk throughput and IOPS — suitable for NoSQL databases or data warehousing, not in-memory analytics where the bottleneck is RAM, not disk.

---

## Question 3

What is the SLA for Azure Virtual Machines when two or more instances are deployed across separate Availability Zones?

- A) 99.9%
- B) 99.95%
- C) 99.99%
- D) 100%

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Deploying two or more VM instances across separate Availability Zones within the same region achieves a 99.99% compute SLA. This is the highest VM SLA available without cross-region deployment.
- *Why A is incorrect:* 99.9% is the SLA for a single VM with Premium SSD storage and no availability configuration. Zone distribution raises the SLA above this baseline.
- *Why B is incorrect:* 99.95% is the SLA for two or more VMs deployed in an Availability Set (fault domains within a single datacenter). This is less than the zone-distributed SLA.
- *Why D is incorrect:* No Azure service guarantees 100% uptime. SLAs are always expressed as percentages below 100%, and Azure credits customers when SLAs are missed.

---

## Question 4

A company uses Azure VM Scale Sets for a web application. During peak hours, CPU usage consistently exceeds 80%. After peak hours, CPU drops to 10%. The Scale Set is configured with minimum 2 instances, maximum 8 instances. Which autoscale behavior correctly describes what happens?

- A) Scale Sets cannot scale below 2 instances regardless of CPU
- B) The Scale Set scales to 8 instances permanently once the CPU threshold is reached
- C) The Scale Set scales out to handle peak demand and scales in during off-peak hours, respecting the minimum of 2 instances
- D) The Scale Set only scales out; it never removes instances once added

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* VM Scale Sets with autoscale rules scale out when demand exceeds the scale-out threshold and scale in when demand drops below the scale-in threshold. The minimum instance count (2) is a floor — the Scale Set will never scale below 2 regardless of low CPU. This is the correct elastic behavior.
- *Why A is incorrect:* While "A" contains a true statement (cannot scale below minimum), it does not describe the full behavior. Scale Sets do scale up during peak and down during off-peak — the minimum constraint only affects scale-in.
- *Why B is incorrect:* Scale Sets do not permanently maintain peak capacity. Once demand decreases, scale-in rules remove excess instances, returning to a count appropriate for the current load.
- *Why D is incorrect:* Scale Sets do scale in (remove instances) when demand decreases and scale-in rules are configured. Autoscale includes both scale-out and scale-in rules.

---

## Question 5

Data stored on the temporary disk of an Azure VM is lost under which condition?

- A) When the VM is restarted using the guest OS
- B) When the VM is resized to a different VM size
- C) When the VM is deallocated and then started again
- D) When a data disk is attached to the VM

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The temporary disk is local SSD storage on the physical host running the VM. When a VM is deallocated, the VM's placement on a physical host is released. When the VM starts again, it may be placed on a different physical host with a different local SSD. All data on the previous temporary disk is permanently lost.
- *Why A is incorrect:* A guest OS restart does not deallocate the VM — it remains on the same physical host. The temporary disk persists across normal reboots.
- *Why B is incorrect:* Resizing a VM may require moving it to a different physical host, which could cause temporary disk loss. However, deallocation is the primary and most clearly defined event causing loss. Resizing may preserve or lose temp data depending on whether reallocation is required — deallocation is the definitive trigger.
- *Why D is incorrect:* Attaching a data disk does not affect the temporary disk in any way. Data disks are independent managed disks with no interaction with the temp disk.

---

## Question 6

A university wants to provide each computer science student with an Azure VM for lab assignments throughout the semester. Students use VMs for 3-hour lab sessions but VMs sit idle between sessions. Which Azure VM type is most cost-appropriate for this use case?

- A) Azure Spot VM — lowest cost per hour
- B) Standard General Purpose VM — consistent performance for lab work
- C) Azure Burstable (B-series) VM — accumulates credits during idle time and uses them during active lab sessions
- D) Memory Optimized VM — handles student demand spikes

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* B-series burstable VMs are designed for workloads with variable CPU utilization. During the many hours the VM sits idle between lab sessions, it accumulates CPU credits. During the 3-hour lab session with active compilation, building, and testing, it spends those credits for full CPU performance. This gives students good performance during labs at a fraction of the cost of a dedicated-performance VM.
- *Why A is incorrect:* Spot VMs can be evicted with 30 seconds' notice when Azure needs the capacity. Lab VMs need to be reliably available during scheduled class times — eviction during a midterm lab would be unacceptable.
- *Why B is incorrect:* Standard General Purpose VMs provide consistent performance but charge the same rate whether CPU is 0% during idle or 100% during labs. B-series provides equivalent performance at lower cost for this usage pattern.
- *Why D is incorrect:* Memory Optimized VMs are sized for workloads requiring large amounts of RAM. Student lab VMs (compilation, coding, small application testing) do not require extreme RAM and do not benefit from this specialization.

---

## Question 7

Which attribute letter in an Azure VM size name indicates that the VM is eligible for Premium SSD storage?

- A) m
- B) s
- C) d
- D) a

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The lowercase `s` in an Azure VM size name (such as `Standard_D4s_v3`) indicates that the VM supports Premium SSD storage. VMs without the `s` designation can only use Standard HDD or Standard SSD managed disks.
- *Why A is incorrect:* The `m` attribute indicates a large memory configuration — a higher-than-standard memory option for that VM series.
- *Why C is incorrect:* The `d` attribute indicates that the VM has a local NVMe or SSD temporary disk. This relates to temporary disk type, not Premium SSD eligibility for managed data disks.
- *Why D is incorrect:* The `a` attribute indicates that the VM uses an AMD processor rather than Intel. This is a processor architecture designation, not a storage capability indicator.

---

## Question 8

An organization deploys two Azure VMs in the same region with no explicit availability configuration. Both VMs run the same web application behind a load balancer. What is the SLA for this deployment?

- A) 99.99% because two identical VMs are running
- B) 99.95% because two VMs are present
- C) 99.9% per VM — the load balancer does not improve the SLA beyond the single-VM baseline
- D) The composite SLA is calculated by multiplying the two individual VM SLAs together, resulting in a lower number

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Without an Availability Set or Availability Zone configuration, Azure does not guarantee that the two VMs are placed in different fault domains (separate racks) or update domains. They may be on the same physical rack. The 99.95% SLA (Availability Set) and 99.99% SLA (Availability Zones) require explicit configuration. Without configuration, each VM has a 99.9% individual SLA.
- *Why A is incorrect:* Simply running two VMs without zone configuration does not achieve 99.99%. The 99.99% SLA requires deployment across separate Availability Zones.
- *Why B is incorrect:* The 99.95% SLA requires deployment within a configured Availability Set. Without that explicit configuration, the SLA does not improve.
- *Why D is incorrect:* The composite SLA multiplication applies when services depend on each other serially (if A fails, the whole application fails). In a redundant load-balanced configuration, the application fails only if all instances fail — the availability logic is additive, not multiplicative.

---

## Question 9

A developer runs `az vm deallocate` on a VM that has a dynamically assigned public IP address. What happens to the public IP address?

- A) The IP address is permanently deleted and a new address must be manually assigned
- B) The IP address is retained and will be the same when the VM is started again
- C) The dynamic IP address is released back to Azure's pool and a different IP may be assigned when the VM starts
- D) The IP address is transferred to the resource group until the VM is restarted

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Dynamic public IP addresses are released when a VM is deallocated. When the VM starts again, Azure assigns a new dynamic IP address from its pool — this may be the same or a different address. To retain a consistent IP address across deallocation/start cycles, a static (Standard SKU) public IP address must be configured.
- *Why A is incorrect:* The IP address resource itself is not deleted — only the assignment is released. The public IP resource remains in the resource group and can be reassigned. A new IP does not need to be "manually assigned" from scratch — the existing resource is reassigned.
- *Why B is incorrect:* This describes static IP behavior. A dynamic IP address is not guaranteed to be the same after deallocation.
- *Why D is incorrect:* IP addresses are not "transferred to the resource group" — they are always resources within the resource group. The dynamic IP address lease is simply released to Azure's address pool.

---

## Question 10

Which Azure VM Scale Set feature prevents the autoscale engine from making repeated rapid scaling changes in response to short-duration metric fluctuations?

- A) Upgrade policy
- B) Instance termination notification
- C) Cool-down period
- D) Spot eviction policy

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The cool-down period is a configurable time window after a scaling event during which the autoscale engine ignores new scaling triggers. For example, a 5-minute cool-down after a scale-out event prevents the system from immediately scaling out again if CPU remains elevated due to the brief period before new instances become fully available and start handling requests.
- *Why A is incorrect:* Upgrade policy controls how OS and application updates are applied to Scale Set instances (Automatic, Rolling, or Manual). It has no relationship to autoscale frequency or oscillation prevention.
- *Why B is incorrect:* Instance termination notification is a feature that sends a notification to instances before they are terminated during scale-in, allowing applications to complete in-flight operations gracefully. It does not control when scaling events occur.
- *Why D is incorrect:* Spot eviction policy controls what happens to Scale Set Spot instances when Azure needs to reclaim capacity — either delete or deallocate them. It applies only to Spot VM Scale Sets and has no relationship to autoscale cool-down behavior.
