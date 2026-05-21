# Reading Guide: Module 10 - Hyper-V Virtualization

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 10 – Hyper-V Virtualization**! This week's study material covers Microsoft's built-in hypervisor, Hyper-V, which allows Windows Server to host multiple virtual machines on a single physical host. Hyper-V is a core component of both on-premises data centers and Azure, and VM management scenarios are tested on the AZ-800 exam.

As a student, you will learn how to create and manage VMs, configure virtual switches and virtual hard disks, work with checkpoints, and understand live migration and Hyper-V Replica for high availability. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Hyper-V Role**: A Type-1 (bare-metal) hypervisor built into Windows Server and Windows 10/11 Pro and Enterprise. When enabled, Hyper-V runs between the hardware and the host OS, giving the host OS itself the same hardware access as any other VM (the host becomes the "parent partition").
* **Virtual Switch (vSwitch)**: A software-defined network switch inside Hyper-V that connects VMs to each other and to external networks. Types: External (connects VMs to the physical network), Internal (connects VMs to the host only), and Private (connects VMs to each other only, no host access).
* **Generation 1 vs. Generation 2 VMs**: Generation 1 VMs use legacy BIOS and support a wide range of older OS versions. Generation 2 VMs use UEFI and Secure Boot, offer faster boot times and better security, and are required for Shielded VMs — but only support Windows Server 2012 and newer Linux distributions.
* **Checkpoint (Snapshot)**: A saved state of a VM at a specific point in time, including memory contents, disk state, and device configuration. Standard checkpoints capture the running memory state; Production checkpoints use the guest OS's backup APIs (VSS) for application-consistent saves.
* **Live Migration**: The process of moving a running VM from one Hyper-V host to another with no downtime. Requires both hosts to be joined to a failover cluster or configured for Hyper-V live migration, with access to shared storage or Storage Spaces Direct.
* **Hyper-V Replica**: An asynchronous replication feature that continuously replicates a VM from a primary Hyper-V host to a replica host at another site. Provides disaster recovery capability without requiring shared storage or a failover cluster.

---

### 2. Certification Exam Tips

* **Virtual switch type selection**: AZ-800 presents network isolation scenarios. If a VM must reach the physical network, use an External vSwitch. If VMs only need to communicate with each other and the host (e.g., a lab environment), use Internal. If VMs must be completely isolated from the host and external network, use Private.
* **Generation 2 and Secure Boot**: Generation 2 VMs enable Secure Boot by default, which can prevent Linux VMs from booting if the correct template is not selected. Know that you must change the Secure Boot template to "Microsoft UEFI Certificate Authority" for Linux Gen 2 VMs.
* **Production checkpoints vs. standard checkpoints**: For production workloads running databases or applications, always use Production checkpoints — they use VSS to create an application-consistent backup point. Standard checkpoints capture raw memory state and can leave applications in an inconsistent state.
* **Microsoft Learn Reference**: Review Hyper-V documentation at [Microsoft Learn – Hyper-V on Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server) for VM configuration, networking, and high availability guidance.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the Hyper-V overview and VM management documentation at [Microsoft Learn: Hyper-V on Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server). Focus on virtual switch types, VM generations, checkpoints, and live migration.
* **Required Video:** Watch the video lecture on **Hyper-V Virtualization** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will enable the Hyper-V role, create a Generation 2 VM, attach a virtual hard disk (VHDX), configure an External virtual switch, and take a Production checkpoint. You will also explore VM settings using both Hyper-V Manager and PowerShell (`New-VM`, `Set-VMMemory`, `Checkpoint-VM`).

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the Hyper-V documentation at [Microsoft Learn: Hyper-V on Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server).
* [ ] Watch the video lecture on **Hyper-V Virtualization** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
