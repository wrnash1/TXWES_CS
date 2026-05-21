# Quiz: Module 10 - Hyper-V Virtualization

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A Hyper-V administrator needs to create a virtual machine that must use UEFI Secure Boot and will run Windows Server 2022 as the guest OS. Which VM generation should be selected?

A) Generation 1, because it uses a legacy BIOS compatible with all versions of Windows Server.
B) Generation 2, because it uses UEFI firmware and supports Secure Boot for modern Windows Server guests.
C) Generation 1 with a virtual TPM added, because TPM support upgrades the VM to UEFI functionality.
D) Generation 2 is only available for Linux guests; Windows Server guests must use Generation 1.

* **Correct Answer:** B) Generation 2, because it uses UEFI firmware and supports Secure Boot for modern Windows Server guests.
* **Distractor Analysis:**
  * *Why A is incorrect:* Generation 1 VMs use legacy BIOS emulation and do not support UEFI or Secure Boot regardless of guest OS version.
  * *Why C is incorrect:* Adding a virtual TPM to a Generation 1 VM does not change its firmware from BIOS to UEFI; a vTPM is available only on Generation 2 VMs.
  * *Why D is incorrect:* Generation 2 fully supports Windows Server 2019 and later as guest operating systems and is the recommended generation for modern Windows Server guests.

---

### Question 2

A Hyper-V host has three VMs that need to communicate with each other and with the Hyper-V host OS for management, but must have no access to the physical network. Which virtual switch type meets this requirement?

A) External, because it connects VMs to all available networks including other VMs and the host.
B) Internal, because it connects VMs to each other and to the Hyper-V host OS without bridging to the physical network adapter.
C) Private, because it connects VMs only to each other with no access to the host or physical network.
D) Bridged, because it creates a layer-2 bridge between VMs and the host management network only.

* **Correct Answer:** B) Internal, because it connects VMs to each other and to the Hyper-V host OS without bridging to the physical network adapter.
* **Distractor Analysis:**
  * *Why A is incorrect:* An External virtual switch binds to a physical NIC and gives VMs access to the external physical network, violating the isolation requirement.
  * *Why C is incorrect:* A Private virtual switch isolates VMs from the host OS entirely. Since the scenario requires host-to-VM management communication, Private does not meet the requirement.
  * *Why D is incorrect:* There is no "Bridged" virtual switch type in Hyper-V. The three supported types are External, Internal, and Private.

---

### Question 3

An administrator takes a checkpoint of a production SQL Server VM before applying a cumulative update. The update causes SQL Server to fail. Which checkpoint type ensures the database files were in a consistent state at the time of capture, enabling safe reversion?

A) Standard checkpoint, which captures raw memory and disk state at the instant it is taken.
B) Production checkpoint, which uses the guest OS Volume Shadow Copy Service (VSS) APIs to flush application writes before capturing disk state.
C) Hyper-V Replica checkpoint, which is created automatically on the replica host and is always application-consistent.
D) Any checkpoint type is equivalent for SQL Server VMs because the transaction log ensures consistency at restore time.

* **Correct Answer:** B) Production checkpoint, which uses the guest OS Volume Shadow Copy Service (VSS) APIs to flush application writes before capturing disk state.
* **Distractor Analysis:**
  * *Why A is incorrect:* A Standard checkpoint captures raw memory state mid-execution, which may include open SQL Server transactions. Reverting to it risks database inconsistency or corruption.
  * *Why C is incorrect:* Hyper-V Replica checkpoints are crash-consistent by default, not application-consistent. They are also created on the replica host for DR purposes, not on the primary VM for update rollback.
  * *Why D is incorrect:* SQL Server's transaction log allows crash recovery, but a Standard checkpoint reverted mid-transaction still imposes recovery work and can leave databases in an inconsistent state. Production checkpoints eliminate this risk.

---

### Question 4

An organization needs to move a running virtual machine from one Hyper-V host to another during business hours with no perceptible downtime for users. What technology enables this?

A) Hyper-V Replica with a planned failover, which gracefully shuts down the primary VM before switching.
B) Live Migration, which transfers the running VM's memory and device state to the destination host while the VM continues operating.
C) VM Export and Import, where the VM is exported on the source, stopped, imported on the destination, and restarted.
D) Storage Migration, which moves the VHDX files to shared storage accessible from both hosts.

* **Correct Answer:** B) Live Migration, which transfers the running VM's memory and device state to the destination host while the VM continues operating.
* **Distractor Analysis:**
  * *Why A is incorrect:* A planned Hyper-V Replica failover involves a graceful shutdown of the primary VM before cutover, producing a brief downtime. It is a DR operation, not a zero-downtime migration tool.
  * *Why C is incorrect:* Export and Import requires the VM to be shut down or paused; there is downtime between export completion and the VM starting on the new host.
  * *Why D is incorrect:* Storage Migration moves VHDX disk files from one storage path to another while the VM remains running on the same host. It does not migrate the VM between hosts.

---

### Question 5

An organization needs disaster recovery for a VM on an on-premises Hyper-V server with an RPO of approximately 5 minutes and no shared storage between sites. Which Hyper-V feature meets this requirement?

A) Live Migration in Stretched Cluster mode, which replicates VM state across sites continuously.
B) Hyper-V Replica, which asynchronously replicates VM changes to a secondary Hyper-V host at configurable intervals as low as 30 seconds.
C) Windows Server Backup scheduled every 5 minutes to a network share at the secondary site.
D) DFS Replication configured to replicate the VHDX files between sites at a 5-minute interval.

* **Correct Answer:** B) Hyper-V Replica, which asynchronously replicates VM changes to a secondary Hyper-V host at configurable intervals as low as 30 seconds.
* **Distractor Analysis:**
  * *Why A is incorrect:* A Stretched Cluster with Live Migration requires shared storage accessible from both sites, which the scenario explicitly excludes.
  * *Why C is incorrect:* Windows Server Backup creates volume-level snapshots for bare-metal recovery and is not designed for continuous VM replication; a 5-minute backup schedule would generate excessive I/O load on a production server.
  * *Why D is incorrect:* DFSR replicating live VHDX files that are actively written by a running VM produces corrupted replicas. Hyper-V Replica uses Hyper-V and VSS APIs specifically designed to replicate running VMs safely without corruption.
