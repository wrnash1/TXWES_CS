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

---

### Question 11 (5 points)

A company needs to deploy a virtual machine that will run a SQL Server workload requiring 1 TB of RAM. Which Azure VM series is specifically designed for this memory requirement?

- A) D-series (General Purpose)
- B) F-series (Compute Optimized)
- C) M-series (Memory Optimized)
- D) L-series (Storage Optimized)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The M-series provides the highest memory-to-CPU ratios in Azure, with configurations supporting up to 4 TB of RAM. It is specifically designed for workloads like SAP HANA and large SQL Server in-memory configurations that require extreme amounts of RAM.
  - *Why A is incorrect:* The D-series provides a balanced CPU-to-memory ratio designed for general workloads. It does not offer configurations with 1 TB or more of RAM.
  - *Why B is incorrect:* The F-series is compute optimized — it has a high CPU-to-memory ratio, meaning relatively less RAM per core. It is the opposite of what a memory-intensive SQL Server workload requires.
  - *Why D is incorrect:* The L-series is storage optimized for high disk throughput and IOPS, designed for NoSQL and data warehousing scenarios that need fast local disk. It does not provide extreme RAM configurations.

---

### Question 12 (5 points)

A VM is running with a dynamically assigned public IP address. The VM is deallocated overnight to reduce costs and restarted the next morning. What is the expected behavior of the public IP address?

- A) The IP address is permanently deleted when the VM is deallocated and a new one must be manually created
- B) The same dynamic IP address is always preserved across deallocation cycles for the lifetime of the VM
- C) The dynamic IP address is released when the VM is deallocated; a new IP address (potentially different) is assigned when the VM starts again
- D) The IP address is converted to a static IP automatically after the first deallocation

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Dynamic public IP addresses are released back to Azure's address pool when a VM is deallocated. When the VM is started again, Azure assigns a new dynamic IP from the pool — it may or may not be the same address as before. To guarantee a consistent IP across start/stop cycles, a static public IP must be explicitly configured.
  - *Why A is incorrect:* The public IP address resource itself persists in the resource group — it is not deleted. Only the IP lease is released. The IP resource can be reused when the VM restarts.
  - *Why B is incorrect:* Dynamic IP behavior does not guarantee the same address is preserved. That is the definition of static IP behavior. If the same address happens to be re-assigned, it is coincidental, not guaranteed.
  - *Why D is incorrect:* Azure does not automatically convert dynamic IPs to static IPs during deallocation. Static IP assignment is an explicit configuration choice made by the administrator, not an automatic transition.

---

### Question 13 (5 points)

An organization wants to deploy 100 identical web server VMs and distribute traffic evenly among them. The number of VMs should automatically increase when CPU exceeds 70% and decrease when CPU drops below 30%. Which Azure feature handles both the identical VM deployment and the autoscaling in a single resource?

- A) Azure Availability Set with autoscale rules
- B) Azure Virtual Machine Scale Set
- C) Azure Load Balancer with backend pool
- D) Azure App Service with scale-out rules

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Virtual Machine Scale Sets allow deployment of multiple identical VM instances and include built-in autoscale rules based on metrics like CPU utilization. Scale Sets can scale out (add instances) when CPU is high and scale in (remove instances) when CPU is low — managing both the instance count and the identical configuration as a single resource.
  - *Why A is incorrect:* Availability Sets distribute VMs across fault and update domains for resilience but do not manage instance count, provide autoscaling, or ensure VMs are identical in configuration. They are for resilience, not scaling.
  - *Why C is incorrect:* Azure Load Balancer distributes traffic across backend VMs but does not create VMs, manage VM count, or provide autoscaling. It is a traffic distribution layer, not a compute resource manager.
  - *Why D is incorrect:* Azure App Service with scale-out rules is a PaaS service for web applications. The scenario describes IaaS VM infrastructure — App Service does not deploy raw VMs.

---

### Question 14 (5 points)

What happens to managed disks attached to an Azure VM when the VM resource is deleted (but not the disks explicitly)?

- A) All managed disks are automatically deleted with the VM
- B) Managed disks are retained as orphaned resources in the resource group after the VM is deleted, unless "delete disk" is explicitly selected during VM deletion
- C) Managed disks are moved to Azure Blob Storage automatically when their VM is deleted
- D) Managed disks are detached and re-attached to another VM in the same resource group automatically

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* By default, managed disks are independent resources that persist after a VM is deleted. The Azure Portal offers a "Delete with VM" option when deleting a VM, but if not selected, the OS disk and any data disks remain in the resource group as unattached (orphaned) managed disks — which still incur storage costs.
  - *Why A is incorrect:* Automatic deletion of disks with the VM is opt-in, not the default behavior. Without explicitly enabling this option, disks persist after VM deletion.
  - *Why C is incorrect:* Managed disks are a separate storage resource type from Azure Blob Storage. They are never automatically converted to blobs or moved to a storage account.
  - *Why D is incorrect:* Azure does not automatically re-attach orphaned disks to other VMs. Disks must be manually attached to a new VM by an administrator.

---

### Question 15 (5 points)

A company needs VMs that can run for extended periods but must accept occasional interruptions of up to 30 seconds' notice. The workload is a batch data processing job that checkpoints progress every 5 minutes. Cost reduction is the top priority. Which VM pricing model is appropriate?

- A) Pay-as-you-go Standard VMs
- B) Azure Reserved Instances (1-year)
- C) Azure Spot VMs
- D) Azure Dedicated Hosts

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Spot VMs use spare Azure capacity at discounts up to 90% off pay-as-you-go rates. They can be evicted with 30 seconds' notice when Azure needs the capacity back. Batch processing jobs that checkpoint frequently can tolerate eviction — the job resumes from the last checkpoint on a new Spot VM instance, making this the ideal cost-minimizing option.
  - *Why A is incorrect:* Pay-as-you-go Standard VMs provide no eviction risk but also no discount. For a cost-priority workload that tolerates interruption, PAYG is unnecessarily expensive.
  - *Why B is incorrect:* Reserved Instances reduce per-hour cost for continuously running workloads through a 1 or 3-year commitment. They still incur charges whether the VM runs or not and do not provide the depth of discount that Spot pricing offers.
  - *Why D is incorrect:* Azure Dedicated Hosts provide physical server isolation for compliance and licensing reasons. They are significantly more expensive than standard VMs, the opposite of cost minimization.

---

### Question 16 (5 points)

When using an Azure VM Scale Set with Rolling upgrade policy, how are OS or application updates applied to the VM instances?

- A) All instances are updated simultaneously, causing a brief full-scale outage
- B) Instances are updated in batches according to the configured batch size, keeping a portion of instances available throughout the upgrade
- C) Updates are never applied automatically — each instance must be manually updated
- D) The Scale Set creates entirely new instances with the new configuration and then deletes the old instances all at once

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Rolling upgrade policy updates VM instances in configurable batches (e.g., 20% at a time). At any given moment, the majority of instances remain on the current version and serve traffic while the batch being updated is temporarily offline. This provides zero-downtime upgrade capability for production Scale Sets.
  - *Why A is incorrect:* That describes the Automatic upgrade policy without any rolling control — it would apply updates to all instances simultaneously, causing a full-scale service interruption. Rolling policy specifically avoids this.
  - *Why C is incorrect:* That describes the Manual upgrade policy, where the Scale Set updates the model but does not apply changes to existing instances until an administrator triggers the update per-instance. Rolling policy automates staged updates.
  - *Why D is incorrect:* Creating all-new instances and deleting old ones simultaneously describes a blue/green deployment pattern, not the Rolling upgrade policy. Rolling updates instances in place in batches without provisioning a parallel fleet.

---

### Question 17 (5 points)

Which Azure CLI command correctly deallocates a VM named "webserver01" in a resource group named "prod-rg" to stop compute billing?

- A) `az vm stop --name webserver01 --resource-group prod-rg`
- B) `az vm deallocate --name webserver01 --resource-group prod-rg`
- C) `az vm delete --name webserver01 --resource-group prod-rg`
- D) `az vm poweroff --name webserver01 --resource-group prod-rg`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `az vm deallocate` releases the VM's compute allocation from the physical host, stopping compute billing. This is the correct command when the goal is to stop paying for the VM's CPU and RAM while retaining the VM configuration and its disks.
  - *Why A is incorrect:* `az vm stop` shuts down the guest OS but does NOT deallocate the VM. The VM remains allocated on its physical host and compute billing continues at the full rate. This is the "Stopped (not deallocated)" state.
  - *Why C is incorrect:* `az vm delete` permanently destroys the VM resource. The VM cannot be restarted after deletion. This is irreversible and is not the correct command when the intent is to pause the VM temporarily.
  - *Why D is incorrect:* `az vm poweroff` is not a valid Azure CLI command. This may be confused with guest OS power commands. The correct CLI commands for VM state changes are `start`, `stop`, `deallocate`, `restart`, and `delete`.

---

### Question 18 (5 points)

A VM Scale Set is configured with minimum 3 instances, maximum 10 instances, and a scale-out rule triggering when average CPU exceeds 75% for 5 minutes. The Scale Set currently has 3 instances all running at 80% CPU for 7 minutes. A scale-out event fires and adds 2 instances. The cool-down period is 5 minutes. During the cool-down period, CPU on all instances rises to 90%. What happens?

- A) Another scale-out event fires immediately because CPU exceeds the threshold
- B) The cool-down period suppresses additional scale-out events; no new scaling occurs until the cool-down expires
- C) The Scale Set scales to the maximum of 10 instances immediately to handle the elevated CPU
- D) The Scale Set scales back in because the cool-down period requires load to drop before scale-out can fire again

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The cool-down period (5 minutes) is a stabilization window after a scaling event during which the autoscale engine ignores new scaling triggers. Even though CPU rises to 90%, no additional scale-out occurs until the cool-down expires. This prevents oscillation while new instances are starting and beginning to handle load.
  - *Why A is incorrect:* The cool-down period explicitly prevents this. Without cool-down protection, the system could fire scale-out events repeatedly in quick succession before the newly added instances have time to start and distribute load.
  - *Why C is incorrect:* Scaling to maximum immediately would bypass the configured cool-down and the incremental scale-out rules. Azure autoscale does not jump to maximum based on one metric reading.
  - *Why D is incorrect:* Cool-down periods suppress scale-OUT triggers, not enforce scale-IN. The system does not scale in during a cool-down; it simply pauses all autoscale evaluation until the cool-down window expires.

---

### Question 19 (5 points)

Which VM size attribute letter indicates that the VM has a local NVMe temporary disk in addition to standard temporary disk options?

- A) `s` (Premium Storage capable)
- B) `d` (local disk present)
- C) `a` (AMD processor)
- D) `m` (memory optimized sub-size)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The `d` attribute in an Azure VM size name (such as `Standard_D4ds_v5`) indicates that the VM includes a local NVMe or SSD temporary disk. This is useful for workloads requiring fast temporary scratch space, such as swap files, temp databases, or intermediate data processing.
  - *Why A is incorrect:* The `s` attribute indicates Premium SSD storage eligibility for managed data disks. It is about the managed disk tier that can be attached, not about local temporary disk presence.
  - *Why C is incorrect:* The `a` attribute indicates the VM uses an AMD EPYC processor rather than Intel. This is a processor architecture indicator, not a storage capability descriptor.
  - *Why D is incorrect:* The `m` attribute indicates a larger memory configuration within the same VM series — a memory-boosted variant. It is not related to local disk presence.

---

### Question 20 (5 points)

A web application team needs all VMs to be updated to a new OS image version without any downtime. The team wants Azure to automatically roll out updates in small batches and pause if health checks detect problems after each batch. Which Scale Set upgrade policy and feature combination achieves this?

- A) Manual upgrade policy with health extension
- B) Rolling upgrade policy with Application Health extension enabled
- C) Automatic upgrade policy without health monitoring
- D) Uniform orchestration with Spot eviction policy set to Deallocate

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Rolling upgrade policy updates instances in configurable batches. When the Application Health extension is enabled, Azure monitors each instance after its upgrade and will pause the rolling upgrade if instances report unhealthy. This combination provides zero-downtime updates with automatic safety gates.
  - *Why A is incorrect:* Manual upgrade policy does not automatically apply updates to instances. An administrator must manually trigger each instance's update, which cannot achieve automated rolling deployments.
  - *Why C is incorrect:* Automatic upgrade policy without health monitoring applies updates to all instances simultaneously or without safety checks, risking a full-scale outage if the new image has a defect.
  - *Why D is incorrect:* Spot eviction policy controls what happens when Azure reclaims Spot instances. It has no relationship to OS image upgrade strategy or rolling update behavior.
