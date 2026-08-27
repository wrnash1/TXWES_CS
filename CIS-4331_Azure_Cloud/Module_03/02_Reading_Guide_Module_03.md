# Reading Guide: Module 03 - Azure Virtual Machines and Scale Sets

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## Introduction

Azure Virtual Machines (VMs) are the foundational IaaS compute service in Azure. Every other compute service — containers, functions, managed databases — runs on physical infrastructure that ultimately resembles what VMs expose at the surface. Understanding VMs deeply makes every other service easier to reason about.

This module also introduces VM Scale Sets, the mechanism for elastically scaling IaaS workloads. Scale Sets are tested on AZ-900 as the Azure answer to the question: how does IaaS handle dynamic demand?

---

## Section 1: Azure Virtual Machine Fundamentals

### 1.1 What Is an Azure VM?

An Azure Virtual Machine is a virtualized computing environment that runs on Microsoft's physical hardware in an Azure datacenter. It presents a complete virtual computer to the user, including virtual CPU, virtual RAM, virtual storage, and virtual network interfaces. The user manages everything from the OS upward; Microsoft manages the physical hardware and hypervisor.

Azure VMs support Windows Server, various Linux distributions (Ubuntu, Red Hat Enterprise Linux, SUSE, Debian, CentOS), and select other operating systems. The OS is typically deployed from a Marketplace image — a pre-built OS snapshot maintained by Microsoft or third-party publishers.

### 1.2 When to Use Azure VMs

Use Azure VMs when:

- Full operating system access is required (custom kernel modules, OS-level configuration)
- Migrating existing on-premises workloads with minimal code changes (lift-and-shift)
- Running applications with OS-specific dependencies that cannot be containerized
- Compliance requirements mandate that the customer manage and control the OS environment
- The workload requires persistent local file system state

Do not use Azure VMs when:

- The team only needs to deploy application code (use PaaS — Azure App Service)
- The workload is event-driven and short-duration (use Azure Functions)
- The workload requires containerization with orchestration (use Azure Kubernetes Service)

### 1.3 VM Pricing Components

The total cost of an Azure VM has multiple components:

| Component | Billing Model | Notes |
|---|---|---|
| Compute (CPU + RAM) | Per hour while allocated | Stops when VM is deallocated |
| OS disk | Per GB per month | Continues during deallocation |
| Data disks | Per GB per month | Continues during deallocation |
| Network egress | Per GB transferred out | Ingress is free |
| Public IP address | Per hour (Standard SKU) | Continues during deallocation |
| Bandwidth | Per GB for outbound | First 5 GB free |

---

## Section 2: VM Sizes and Families

### 2.1 VM Size Families

Azure organizes VM sizes into families based on the primary workload type they are optimized for. AZ-900 expects conceptual familiarity with the major families.

| Family | CPU:RAM Ratio | Primary Use Cases | Series Examples |
|---|---|---|---|
| General Purpose | Balanced | Dev/test, web servers, small databases | B (burstable), D, DC |
| Compute Optimized | High CPU | Batch processing, web servers, analytics | F |
| Memory Optimized | High RAM | Databases, large caches, in-memory analytics | E, M |
| Storage Optimized | High disk I/O | NoSQL, data warehousing | L |
| GPU | NVIDIA GPU | ML training, rendering, video encoding | N (NC, ND, NV) |
| High Performance Compute | Maximum CPU + InfiniBand | Scientific simulation, financial modeling | H |

### 2.2 VM Size Naming Convention

Azure VM sizes follow a structured naming pattern:

`[Tier]_[Family][vCPUs][Attributes]_[Version]`

Example: `Standard_D4s_v3`

- `Standard` — pricing tier (Standard vs. legacy Basic)
- `D` — family (General Purpose D-series)
- `4` — number of vCPUs
- `s` — Premium SSD-eligible
- `v3` — hardware generation version

Common attribute letters:

| Letter | Meaning |
|---|---|
| s | Premium SSD storage eligible |
| m | Large memory configuration |
| d | Local NVMe/SSD temporary disk |
| a | AMD processor |
| i | Isolated — dedicated physical host |
| l | Low memory |

### 2.3 Burstable VMs (B-Series)

The B-series is a special General Purpose family designed for workloads with variable CPU utilization. B-series VMs accumulate CPU credits when CPU usage is below baseline, then spend those credits to burst above baseline when needed.

Example: A `Standard_B1s` VM has a baseline of 10 percent CPU. During low utilization periods, it banks credits. During a software installation or traffic spike, it spends credits to temporarily run at 100 percent CPU.

B-series VMs are the most cost-effective choice for lab environments, development workstations, and applications with intermittent CPU demand.

---

## Section 3: VM Managed Disks

### 3.1 Disk Types

| Disk Type | Max IOPS (per disk) | Max Throughput | Monthly Cost (approx. 128 GB) | Best For |
|---|---|---|---|---|
| Standard HDD | 500 | 60 MB/s | ~$5 | Dev/test, backups |
| Standard SSD | 6,000 | 750 MB/s | ~$10 | Web servers, light workloads |
| Premium SSD | 20,000 | 900 MB/s | ~$19 | Production databases |
| Premium SSD v2 | 80,000 | 1,200 MB/s | Variable (per IOPS/throughput) | High-performance databases |
| Ultra Disk | 160,000 | 4,000 MB/s | Variable | SAP HANA, SQL Server Tier 1 |

### 3.2 Disk Roles

**OS Disk:** Contains the operating system. Attached to every VM. Persists across reboots and deallocation. Size is defined by the image (typically 30-128 GB for Windows, 30 GB for Linux). Can be resized after deployment.

**Temporary Disk:** Local SSD on the physical host. Extremely fast I/O. Data is lost on deallocation or live migration. On Linux: `/dev/sdb` mounted at `/mnt/resource`. On Windows: `D:\`. Size varies by VM size. Do not store persistent data here.

**Data Disks:** Additional managed disks for application data. Persistent and portable. Can be attached/detached from VMs. Maximum data disk count varies by VM size.

### 3.3 Managed vs. Unmanaged Disks

Modern Azure VMs use **managed disks** exclusively. Microsoft manages the storage account, replication, and placement. Unmanaged disks (stored as VHD blobs in a storage account) are legacy and should not be used for new deployments. AZ-900 focuses on managed disks.

---

## Section 4: VM Availability Options

### 4.1 Availability Comparison

| Option | Protection Level | SLA (2+ VMs) | Notes |
|---|---|---|---|
| No redundancy | None | 99.9% (Premium SSD) | Dev/test only |
| Availability Set | Rack + maintenance | 99.95% | Legacy; use for older workloads |
| Availability Zone | Datacenter-level | 99.99% | Recommended for new production |
| Azure Spot VM | None (evictable) | No SLA | Cost-optimized batch/test |

### 4.2 Fault Domains and Update Domains (Availability Sets)

An Availability Set distributes VMs across:

- **Fault Domains (FDs):** Physical racks with separate power and network. Default maximum: 2-3 FDs. VMs in different FDs survive a rack power failure.
- **Update Domains (UDs):** Groups of VMs that Microsoft restarts together during planned maintenance. Default: 5 UDs. Only one UD is restarted at a time, so at least 4/5 of your VMs are always running during maintenance.

### 4.3 Spot VMs

Azure Spot VMs use surplus Azure compute capacity at discounts up to 90 percent. Trade-offs:

- Microsoft can evict Spot VMs with 30 seconds' notice when capacity is needed
- No SLA commitment
- Appropriate for: batch jobs, rendering, CI/CD, training workloads, dev environments
- Not appropriate for: production web applications, databases, anything requiring consistent availability

---

## Section 5: VM Lifecycle and Power States

### 5.1 Power States

| Power State | Description | Compute Billed? | Storage Billed? |
|---|---|---|---|
| Running | VM is powered on and operating | Yes | Yes |
| Stopped (in-guest) | OS shutdown from inside the VM | Yes | Yes |
| Stopped (deallocated) | Azure released compute resources | No | Yes |
| Deallocated | Same as stopped/deallocated | No | Yes |
| Deleted | VM and optionally disks removed | No | No (if disks deleted) |

### 5.2 Stop vs. Deallocate — The Most Important Cost Distinction

**Stopping a VM** (using the guest OS shutdown or `az vm stop`) powers off the OS but keeps the VM's compute allocation on the physical host. Azure continues charging the full compute rate.

**Deallocating a VM** (using `az vm deallocate` or the "Stop" button in the Azure Portal) releases the compute allocation. Azure stops charging for compute. Storage disks, public IP addresses, and other attached resources may still incur charges.

In student and lab environments: always use `az vm deallocate` to avoid consuming subscription credits unnecessarily.

When a deallocated VM is restarted, it may be placed on a different physical host. This means the temporary disk contents are lost, and the public IP address may change (unless a static IP is assigned).

---

## Section 6: VM Scale Sets

### 6.1 What Is a VM Scale Set?

A Virtual Machine Scale Set (VMSS) is a group of identical, load-balanced Azure VMs managed as a single unit. Scale Sets enable:

- Automatic horizontal scaling based on metrics or schedules
- Centralized management of all instances (single update policy, single image)
- Integration with Azure Load Balancer and Application Gateway
- Distribution across Availability Zones for high availability

### 6.2 Scale Set Scaling Modes

| Mode | Description | Use Case |
|---|---|---|
| Manual | Set instance count directly | Predictable workloads with known capacity |
| Autoscale (metric-based) | Scale based on CPU, memory, custom metric | Variable demand workloads |
| Scheduled | Pre-scale at known times | Predictable peak periods (9 AM business hours start) |

### 6.3 Autoscale Rules

An autoscale profile consists of scale-out and scale-in rules:

**Scale-out rule example:** When average CPU percentage across all instances exceeds 75 percent for 5 minutes, add 2 instances. Apply a 5-minute cool-down after each scale-out event.

**Scale-in rule example:** When average CPU percentage drops below 25 percent for 10 minutes, remove 1 instance. Apply a 10-minute cool-down after each scale-in event. Never scale below minimum instance count.

**Cool-down period:** The time window after a scaling event during which the autoscale engine ignores further scaling triggers. This prevents oscillation where frequent small demand changes cause constant scale events.

### 6.4 Orchestration Modes

Azure VM Scale Sets support two orchestration modes:

**Uniform orchestration:** All instances use the same VM profile (same size, same image). Optimized for large-scale stateless workloads. Maximum 1,000 instances per Scale Set.

**Flexible orchestration:** Instances can have different configurations. Provides availability zone distribution and fault domain spread. Maximum 1,000 instances per region. This is the newer, recommended mode.

---

## Section 7: Azure VM Extensions

Azure VM extensions are small applications that provide post-deployment configuration and automation on Azure VMs. Common extensions:

| Extension | Purpose |
|---|---|
| Custom Script Extension | Run a script (bash or PowerShell) after deployment |
| Azure Monitor Agent | Send metrics and logs to Azure Monitor |
| Microsoft Antimalware | Install and configure Windows Defender |
| Azure Key Vault VM extension | Rotate certificates automatically |
| Desired State Configuration | Apply PowerShell DSC configurations |

Extensions are installed at VM creation time or added afterward using the Portal or CLI.

---

## Section 8: Azure CLI Commands — VM Management

```bash
# Create a resource group
az group create --name "lab03-rg" --location "eastus"

# List available VM images (Ubuntu)
az vm image list --publisher Canonical --sku 22_04-lts --output table

# Create a Linux VM
az vm create \
  --resource-group "lab03-rg" \
  --name "myvm01" \
  --image "Ubuntu2204" \
  --size "Standard_B1s" \
  --admin-username "azureuser" \
  --generate-ssh-keys

# Create a Windows VM
az vm create \
  --resource-group "lab03-rg" \
  --name "mywinvm01" \
  --image "Win2022Datacenter" \
  --size "Standard_B2s" \
  --admin-username "azureadmin" \
  --admin-password "SecurePass123!"

# List VMs in resource group
az vm list --resource-group "lab03-rg" --output table

# Show VM details and current power state
az vm show \
  --resource-group "lab03-rg" \
  --name "myvm01" \
  --show-details

# Get instance view (shows power state)
az vm get-instance-view \
  --resource-group "lab03-rg" \
  --name "myvm01" \
  --query "instanceView.statuses[1]"

# Stop VM (compute still billed)
az vm stop --resource-group "lab03-rg" --name "myvm01"

# Deallocate VM (compute billing stops)
az vm deallocate --resource-group "lab03-rg" --name "myvm01"

# Start VM
az vm start --resource-group "lab03-rg" --name "myvm01"

# Resize a VM
az vm resize \
  --resource-group "lab03-rg" \
  --name "myvm01" \
  --size "Standard_B2s"

# Delete a VM
az vm delete --resource-group "lab03-rg" --name "myvm01" --yes

# Delete the resource group and all resources
az group delete --name "lab03-rg" --yes --no-wait
```

Reference: learn.microsoft.com/en-us/cli/azure/vm

---

## Section 9: Service Comparison — Azure Compute Options

| Service | Model | OS Managed By | Use Case |
|---|---|---|---|
| Azure Virtual Machines | IaaS | Customer | Full OS control, legacy apps, lift-and-shift |
| Azure App Service | PaaS | Provider | Web apps, APIs, mobile backends |
| Azure Functions | PaaS (Serverless) | Provider | Event-driven, short-duration tasks |
| Azure Container Instances | PaaS | Provider | Single containers without orchestration |
| Azure Kubernetes Service | PaaS (managed control plane) | Provider (control plane) / Customer (worker nodes) | Containerized microservices |
| Azure Virtual Machine Scale Sets | IaaS | Customer | Elastic, load-balanced identical VM fleets |

---

## Section 10: AZ-900 Exam Tips

1. **IaaS identifier for VMs:** If a scenario mentions managing the operating system, patching the OS, or installing custom kernel modules, the answer involves Azure VMs (IaaS). If the scenario says "deploy code only," it is PaaS.

2. **Deallocate vs. stop:** The exam may test cost optimization. Stopping a VM (OS shutdown) does not stop compute billing. Deallocating a VM stops compute billing. This is a real-world operational detail that appears as a cost optimization question.

3. **Scale Set purpose:** VM Scale Sets provide automatic horizontal scaling (adding/removing VM instances). They do not handle vertical scaling (resizing individual VMs). The exam distinguishes these.

4. **Spot VM trade-off:** Spot VMs offer up to 90% cost savings but can be evicted. They are appropriate for fault-tolerant, interruption-tolerant workloads like batch processing. They are never appropriate for production applications requiring high availability.

5. **Availability option for 99.99% SLA:** Two or more VMs deployed to separate Availability Zones achieves the 99.99% SLA. Availability Sets achieve 99.95%. A single VM (even with Premium SSD) achieves only 99.9%.

6. **Temporary disk data loss:** Data on the temporary disk is lost when a VM is deallocated or migrated. This is a common exam trap — do not store persistent data on the temp disk.

7. **VM size family selection:** Match family to workload. High memory workload = Memory Optimized (E/M series). High CPU workload = Compute Optimized (F series). GPU required = N series. Know the conceptual mapping even if you do not memorize specific sizes.

8. **B-series burstable:** B-series VMs are cost-effective for workloads with variable CPU demand. They accumulate CPU credits during low utilization and spend them during bursts. They are not suitable for sustained high-CPU workloads.

---

## Section 11: Required Resources

- Azure Virtual Machines overview: learn.microsoft.com/en-us/azure/virtual-machines/overview
- VM sizes in Azure: learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
- VM Scale Sets overview: learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview
- Azure CLI VM reference: learn.microsoft.com/en-us/cli/azure/vm
- Microsoft Learn AZ-900 compute module: learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/

---

## Section 12: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the VM availability option SLA table (Section 4.1)
- [ ] Memorize the stop vs. deallocate billing table (Section 5.1)
- [ ] Understand all CLI commands in Section 8 — you will use them in the lab
- [ ] Complete the Microsoft Learn "Describe Azure compute and networking services" module
- [ ] Complete Lab Activity Module 03 (VM create, list, deallocate, start)
- [ ] Take Quiz Module 03
- [ ] Post Discussion Module 03 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure Virtual Machines documentation**
https://learn.microsoft.com/en-us/azure/virtual-machines/overview
The official Azure VM documentation hub covering VM creation, sizing, availability options, disks, networking, and management — the primary reference for all VM topics on AZ-104 and AZ-900.

**2. Microsoft Learn — Virtual Machine Scale Sets overview**
https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview
Complete coverage of Scale Set orchestration modes, autoscale configuration, upgrade policies, and the Application Health extension for zero-downtime deployments.

**3. Microsoft Learn — Azure VM sizes and types**
https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
The definitive reference for all Azure VM size families, including naming convention breakdown, attribute letters (s, d, a, m), and selection guidance for compute-optimized, memory-optimized, storage-optimized, and GPU workloads.
