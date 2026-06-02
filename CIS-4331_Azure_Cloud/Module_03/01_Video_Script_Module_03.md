# Video Script: Module 03 - Azure Virtual Machines and Scale Sets

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 22-24 minutes
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 03: Azure Virtual Machines and Scale Sets"]**

Welcome to Module 03. I'm Professor Nash. Today we get hands-on with the most fundamental Azure compute service: Azure Virtual Machines. This is the IaaS workhorse — the service that gives you a full virtual server in Azure that you control from the OS up.

We are also going to cover VM Scale Sets, which are how Azure handles automatic horizontal scaling for VM-based workloads. Both are heavily tested on AZ-900, and both are required for the lab today where you will actually deploy, manage, and deallocate VMs using Azure CLI commands.

By the end of this module you will be able to:

- Describe what an Azure Virtual Machine is and when to use it
- Select an appropriate VM size for a given workload
- Deploy a VM using Azure CLI and the Azure Portal
- List, start, stop, and deallocate VMs using CLI commands
- Explain what VM Scale Sets are and how they enable auto-scaling
- Identify the difference between vertical and horizontal scaling

---

## [01:30 - 05:30] Azure Virtual Machines — Core Concepts

**[SLIDE: "Azure Virtual Machines"]**

An Azure Virtual Machine is a software emulation of a physical computer. It runs on Microsoft's physical hardware in an Azure datacenter, but from your perspective it behaves like a dedicated server. You choose the operating system, you install software on it, you configure networking and storage, and you are responsible for managing and patching the OS. That is the IaaS model we covered in Module 01.

Virtual Machines are the right choice when you need:

- Full OS control (custom kernel modules, specific OS versions)
- Lift-and-shift migration from on-premises servers
- Applications that require persistent state on the local file system
- Legacy applications that cannot be containerized or refactored for PaaS

**[SLIDE: "VM Size Families"]**

Azure organizes VM sizes into families based on workload type. The size you choose determines CPU count, RAM, temporary disk, maximum data disks, and network bandwidth. AZ-900 expects you to understand these family categories conceptually:

**General Purpose** — balanced CPU-to-memory ratio. Suitable for testing, development, small to medium databases, and low-to-medium traffic web servers. Series: B (burstable), D, DC.

**Compute Optimized** — high CPU-to-memory ratio. Suitable for medium traffic web servers, batch processing, application servers, analytics. Series: F.

**Memory Optimized** — high memory-to-CPU ratio. Suitable for relational databases, large caches, in-memory analytics. Series: E, M.

**Storage Optimized** — high disk throughput and IOPS. Suitable for NoSQL databases, data warehousing, large transactional databases. Series: L.

**GPU** — NVIDIA GPU acceleration. Suitable for machine learning training, graphic rendering, video encoding. Series: N.

**High Performance Compute** — highest CPU performance with optional InfiniBand networking. Series: H.

**[SLIDE: "VM Naming Convention"]**

Understanding the VM size naming convention helps you decode any size you encounter. A size like `Standard_D4s_v3` breaks down as:

- `Standard` — pricing tier (vs. Basic, which is legacy)
- `D` — family (General Purpose)
- `4` — vCPU count
- `s` — Premium SSD eligible
- `v3` — version of the hardware generation

So `Standard_D4s_v3` is a General Purpose VM with 4 vCPUs, Premium SSD support, on generation 3 hardware.

---

## [05:30 - 10:00] Deploying a VM with Azure CLI

**[SHOW CODE — Azure CLI commands]**

Let me walk through the core CLI commands you will use in today's lab. I am going to create a resource group, create a Linux VM in it, and then show you how to list, stop, deallocate, and start VMs.

First, create a resource group:

```bash
az group create \
  --name "lab03-rg" \
  --location "eastus"
```

Now deploy an Ubuntu VM into that group:

```bash
az vm create \
  --resource-group "lab03-rg" \
  --name "lab03-vm01" \
  --image "Ubuntu2204" \
  --size "Standard_B1s" \
  --admin-username "azureuser" \
  --generate-ssh-keys \
  --output json
```

Let me explain the parameters:

- `--image "Ubuntu2204"` specifies Ubuntu 22.04 LTS as the OS image. You can use `az vm image list --output table` to see available images.
- `--size "Standard_B1s"` selects the smallest burstable general-purpose VM. For labs and testing, this keeps cost low.
- `--generate-ssh-keys` automatically creates an SSH key pair if one does not already exist at `~/.ssh/id_rsa`.
- `--output json` returns the full VM details including public IP after creation.

**[SHOW CODE — Listing and managing VMs]**

After the VM is created, here are the essential management commands:

```bash
# List all VMs in a resource group
az vm list --resource-group "lab03-rg" --output table

# Show VM details including status
az vm show \
  --resource-group "lab03-rg" \
  --name "lab03-vm01" \
  --show-details \
  --output json

# Stop (graceful OS shutdown) — still billed for compute
az vm stop \
  --resource-group "lab03-rg" \
  --name "lab03-vm01"

# Deallocate (release compute resources) — compute billing stops
az vm deallocate \
  --resource-group "lab03-rg" \
  --name "lab03-vm01"

# Start a deallocated VM
az vm start \
  --resource-group "lab03-rg" \
  --name "lab03-vm01"
```

**[SLIDE: "Stop vs. Deallocate — Critical Cost Difference"]**

This is one of the most important practical concepts for controlling Azure VM costs. When you **stop** a VM through the OS (or using `az vm stop`), the VM is powered off but the underlying compute resources — the CPU and memory allocation on the physical host — are still reserved for you. Azure continues billing for the VM compute at the full hourly rate.

When you **deallocate** a VM (using `az vm deallocate` or stopping it through the Azure Portal using the "Stop" button), Azure releases the compute resources back to the pool. Compute billing stops. You only pay for the storage disks while the VM is deallocated.

In student subscriptions and lab environments, always **deallocate** VMs when you are not using them. A forgotten stopped (but not deallocated) VM will consume your student credit.

---

## [10:00 - 14:00] VM Disks and Storage

**[SLIDE: "VM Disk Types"]**

Every Azure VM has an OS disk, a temporary disk, and optionally one or more data disks.

**OS Disk** stores the operating system. It is a managed disk, persists across VM reboots, and survives deallocation. When you delete the VM, you can choose to delete or retain the OS disk.

**Temporary Disk** is a local SSD on the physical host that provides fast I/O but is ephemeral — data on the temp disk is lost when the VM is deallocated or moved. On Linux it appears as `/dev/sdb` mounted at `/mnt/resource`. Do not store important data here.

**Data Disks** are additional managed disks you attach to a VM for application data storage. They are persistent and can be detached and re-attached to other VMs.

**[SLIDE: "Managed Disk Tiers"]**

| Disk Type | Max IOPS | Max Throughput | Use Case |
|---|---|---|---|
| Standard HDD | 500 IOPS | 60 MB/s | Dev/test, non-critical |
| Standard SSD | 6,000 IOPS | 750 MB/s | Web servers, lightly used apps |
| Premium SSD | 20,000 IOPS | 900 MB/s | Production databases, I/O intensive |
| Ultra Disk | 160,000 IOPS | 2,000 MB/s | SAP HANA, SQL Server, mission-critical |

For AZ-900, know that Premium SSD requires a VM size with the `s` designation (like `Standard_D4s_v3`).

---

## [14:00 - 18:00] VM Scale Sets

**[SLIDE: "The Scaling Problem"]**

Imagine you run a web application on a single Azure VM. On a normal weekday, the VM handles traffic comfortably. But on Friday afternoon when 10,000 users hit your application simultaneously, that single VM is overwhelmed. You need more compute. But you can only have one of two things at a time: too much capacity (wasting money) or too little (causing outages). Neither is acceptable.

VM Scale Sets solve this by managing a group of identical, load-balanced VMs that can automatically grow or shrink based on demand.

**[SLIDE: "Azure Virtual Machine Scale Sets"]**

A **Virtual Machine Scale Set** is a group of load-balanced VMs that are all identical — same image, same size, same configuration. Scale Sets support:

- **Automatic scaling** — rules trigger scale-out (add VMs) when CPU exceeds a threshold, and scale-in (remove VMs) when CPU drops below a threshold
- **Manual scaling** — set the number of instances directly
- **Scheduled scaling** — pre-scale for known peak periods (Black Friday, semester registration)

Scale Sets integrate with Azure Load Balancer or Azure Application Gateway to distribute traffic across all running instances.

**[SLIDE: "Scale Set Configuration Concepts"]**

When creating a Scale Set, key decisions include:

**Instance count:** Minimum (floor), maximum (ceiling), and default count. Azure scales between minimum and maximum automatically.

**Scale-out rule:** Define the metric (CPU percentage, memory, custom metric) and threshold that triggers adding instances. Example: add 2 instances when average CPU exceeds 75 percent for 5 minutes.

**Scale-in rule:** Define the metric and threshold that triggers removing instances. Example: remove 1 instance when average CPU drops below 25 percent for 10 minutes.

**Cool-down period:** A time window after a scaling event during which no additional scaling events fire. This prevents rapid oscillation.

**Upgrade policy:** Controls how Scale Set instances are updated — Automatic, Rolling, or Manual.

**[SHOW PORTAL — Navigate to Scale Sets in the Azure Portal, show the scaling configuration panel]**

Here in the Portal you can see the Scale Set scaling configuration. The horizontal axis is time, and you can see the instance count changing over time in response to the metrics you configure. Azure's autoscale engine evaluates metrics every minute and makes scaling decisions based on your rules.

---

## [18:00 - 21:00] Availability Options for VMs

**[SLIDE: "VM Availability Options"]**

When deploying Azure VMs for production workloads, you must choose an availability option. We introduced this in Module 02 — now let's connect it to VM deployment decisions.

**No redundancy:** Single VM with no availability configuration. SLA is 99.9% with Premium SSD. Suitable only for dev/test environments.

**Availability Set:** Distributes VMs across fault domains (separate racks) and update domains within a single datacenter. SLA is 99.95% for two or more VMs. Protects against rack-level hardware failure and planned maintenance.

**Availability Zones:** Distributes VMs across physically separate datacenters within the same region. SLA is 99.99% for two or more VMs. Protects against datacenter-level failure.

For new production deployments in zone-supported regions, always use Availability Zones.

**[SLIDE: "Azure Spot VMs"]**

One pricing concept that appears on AZ-900: Azure Spot VMs use unused Azure compute capacity at discounts up to 90 percent compared to pay-as-you-go prices. The tradeoff is that Microsoft can evict your Spot VM with 30 seconds' notice when capacity is needed. Spot VMs are appropriate for batch processing, rendering, and testing workloads that can tolerate interruption — never for production applications requiring consistent availability.

---

## [21:00 - 23:00] Lab Preview

**[SLIDE: "Module 03 Lab"]**

In today's lab you will:

1. Create a resource group using `az group create`
2. Deploy a Linux VM using `az vm create` with specific size and image parameters
3. List your VMs using `az vm list`
4. Stop and deallocate the VM using `az vm deallocate`
5. Start the VM again using `az vm start`
6. Check VM power state using `az vm get-instance-view`
7. Delete the resource group and all resources when complete

These are exactly the CLI commands tested on the AZ-900 practical knowledge items. Every professional working with Azure VMs runs these commands routinely. By the end of the lab, you will have deployed and managed a real Azure VM from the command line.

---

## [23:00 - 24:00] Closing

**[INSTRUCTOR ON CAMERA]**

You now understand Azure Virtual Machines — how to size them, deploy them, manage their lifecycle, and scale them with VM Scale Sets. The stop-versus-deallocate distinction is critically important for your student subscription budget — please use `az vm deallocate`, not `az vm stop`, when you are finished with lab VMs.

In Module 04, we move to Azure Container Services — Docker containers and Azure Kubernetes Service. Containers give you the PaaS efficiency of not managing an OS combined with the portability of packaging your application and its dependencies together. See you there.

---

**References:**

- learn.microsoft.com/en-us/azure/virtual-machines/overview
- learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview
- learn.microsoft.com/en-us/cli/azure/vm
