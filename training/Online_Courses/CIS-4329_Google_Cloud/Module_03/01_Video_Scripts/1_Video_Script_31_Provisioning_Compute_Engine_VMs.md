### 1. Video Script 3.1: Provisioning Compute Engine VMs
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 3. We've planned our architecture; now it's time to build it. Compute Engine is Google's IaaS offering. Provisioning a VM is simple in the console, but for the ACE exam, you need to understand the underlying mechanics of machine types, disks, and startup scripts."
**Visual:** Screencast of the GCP Console creating a VM instance.
**[Alt-text: Screencast of the 'Create an instance' page in GCP. The instructor highlights the 'Machine configuration' section showing the E2 series, and the 'Boot disk' section showing Debian Linux.]**
**Audio:** "When you create a VM, you choose a Machine Family. E2 is for general-purpose workloads. N2 is for high performance. M2 is for memory-optimized databases. You also choose a Boot Disk, which defines the operating system image (like Debian or Windows) and the disk type (Standard HDD, Balanced Persistent Disk, or SSD). Finally, you can inject a Startup Script—a bash script that runs automatically the first time the VM boots, perfect for installing Apache or updating packages without manual intervention."

---
