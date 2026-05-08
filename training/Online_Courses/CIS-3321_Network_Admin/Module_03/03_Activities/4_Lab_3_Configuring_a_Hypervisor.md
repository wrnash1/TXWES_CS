### 4. Lab 3: Configuring a Hypervisor
**Objective:** Solidify the understanding of virtualization by reviewing hypervisor networking settings.
**Instructions:**
1. Open Oracle VirtualBox.
2. Go to **File -> Host Network Manager**.
3. Create a new Host-Only Ethernet Adapter. Note the IPv4 Address (usually 192.168.56.1).
4. Select one of your existing Linux VMs. Go to **Settings -> Network -> Adapter 2**.
5. Check "Enable Network Adapter" and attach it to the "Host-only Adapter" you just created.
6. Boot the VM and ensure it received an IP address from that network.
**Deliverable:** Take a screenshot of the VM's terminal showing it pinging the host machine at `192.168.56.1`. Submit to Blackboard.

---
