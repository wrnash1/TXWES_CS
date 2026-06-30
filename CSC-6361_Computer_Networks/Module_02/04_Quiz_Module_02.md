# Quiz: Module 02 – Campus Network Design: VLANs, STP & EtherChannel
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: Sunday, November 1, 2026 at 11:59 PM CST

---

> **Instructor Note:** Enter into Canvas as a timed Quiz (30 min, 1 attempt, randomize question order). All questions are CCNP Enterprise–style scenario questions.

---

### Question 1 (Multiple Choice — 10 pts)
A network engineer adds a previously decommissioned switch back into a production VTP domain without resetting its configuration. Shortly after, all VLANs on every switch in the domain disappear. What is the most likely cause?

- A) The reintroduced switch is running an incompatible IOS version.
- B) The reintroduced switch has a higher VTP configuration revision number, causing all switches to sync to its (empty) VLAN database. ✅
- C) The reintroduced switch is in VTP Client mode and cannot receive VLAN updates.
- D) A BPDU storm occurred, causing all switches to flush their MAC tables.

**Answer:** B — When a VTP Server with a higher revision number is introduced, all VTP clients sync to that switch's database. If the switch was previously used in a lab with many VLANs added and deleted, its revision number could be very high and its VLAN database may be empty, wiping all VLANs.

**Distractor Analysis:**
- A: IOS incompatibility does not cause VLAN deletion.
- C: VTP Client mode would cause the switch to receive updates, not overwrite them.
- D: BPDU storms affect STP, not VLAN databases.

---

### Question 2 (Multiple Choice — 10 pts)
A multilayer switch has the following STP configuration. What is the bridge priority for VLAN 20?

```
spanning-tree vlan 20 root primary
```
The default bridge priority on the switch before this command was 32768. Which of the following best describes the resulting priority?

- A) 0 — `root primary` sets priority to zero.
- B) 4096 — always sets to the lowest possible priority increment.
- C) 24576 or lower — Cisco IOS sets it to 24576 or 4096 below the current root, whichever is lower. ✅
- D) 32768 — `root primary` does not change the priority value.

**Answer:** C — The `spanning-tree vlan X root primary` macro checks the current root's priority and sets the local bridge to either 24576, or 4096 below the current root's priority, whichever is lower. It does NOT simply set priority to 0 or 4096.

---

### Question 3 (Multiple Choice — 10 pts)
An engineer runs `show etherchannel summary` and sees this output:

```
Po1(SU)   LACP    Gi0/1(P)    Gi0/2(D)
```
What does the `D` flag on Gi0/2 indicate?

- A) The port is in a down state and not bundled. ✅
- B) The port is designated and forwarding traffic.
- C) The port is in dynamic mode waiting for negotiation.
- D) The port is the primary active link in the EtherChannel.

**Answer:** A — In `show etherchannel summary` output, `D` means the port is "down" (not bundled in the port-channel). Common causes: link failure, speed/duplex mismatch, or LACP negotiation failure. `P` means "in port-channel" (bundled and active).

---

### Question 4 (Scenario — 10 pts)
A network administrator reports that after adding a new access switch (SW-NEW) to the campus, traffic patterns changed dramatically and some ports on core switches began forwarding traffic they should not. `show spanning-tree vlan 10` on a core switch now shows "Root ID: SW-NEW." What happened, and what should the engineer do?

- A) SW-NEW has a lower MAC address than the core switch, making it root. Apply `spanning-tree guard loop` on the core switch. ❌
- B) SW-NEW was assigned a lower bridge priority than the core switch. Reset SW-NEW's priority to the default. ❌
- C) SW-NEW was connected without a bridge priority configured, and its MAC address happened to be lower than the core switch, making it root. Apply `spanning-tree guard root` on the ports facing the access layer to prevent this. ✅
- D) SW-NEW received a BPDU with a lower root ID and relayed it to the core switch.

**Answer:** C — Without explicit priority configuration, STP root election is decided by the lowest MAC address. A new switch with a lower MAC can unintentionally become root. Root Guard on distribution/core ports facing the access layer prevents any access switch from claiming root.

---

### Question 5 (Multiple Choice — 10 pts)
Which two statements correctly describe RSTP (802.1W) compared to classic STP (802.1D)? (Select two)

- A) RSTP uses a 5-state model: Blocking, Listening, Learning, Forwarding, Disabled. ❌
- B) RSTP achieves rapid convergence through a proposal/agreement handshake between directly connected switches. ✅
- C) RSTP replaces the Blocking, Listening states with a single Discarding state. ✅
- D) RSTP requires a 30-second max-age timer before a port can transition to Forwarding.
- E) RSTP does not support PortFast for edge ports.

**Answer:** B and C — RSTP uses a 3-state model (Discarding, Learning, Forwarding) and achieves rapid convergence via direct handshake instead of waiting for timers.

---

### Question 6 (Multiple Choice — 10 pts)
A campus network runs Rapid PVST+ with DS1 as the root for VLANs 10–20 and DS2 as root for VLANs 30–40. An engineer wants to implement MST to reduce the number of STP instances. Which MST configuration on all switches will correctly replicate the existing traffic engineering?

- A)
```
spanning-tree mst configuration
 name CAMPUS
 revision 1
 instance 1 vlan 10-20
 instance 2 vlan 30-40
spanning-tree mst 1 priority 4096  ! On DS1
spanning-tree mst 2 priority 4096  ! On DS2
```
✅

- B)
```
spanning-tree mode mst
 name CAMPUS
 revision 1
 instance 1 vlan 10-20
 instance 2 vlan 30-40
```
without setting priorities ❌

- C) MST cannot replicate per-VLAN traffic engineering. ❌
- D) MST instances must use the same priority on all switches. ❌

**Answer:** A — MST requires entering the `spanning-tree mst configuration` block (not inline with `spanning-tree mode`), then setting per-instance priorities separately. The configuration must be identical on all switches in the region.

---

### Question 7 (Multiple Choice — 10 pts)
A network engineer needs to prevent Layer 2 loops if a Spanning Tree BPDU is not received on a non-designated port for an extended period (indicating the upstream switch may have stopped sending BPDUs). Which STP feature addresses this specific scenario?

- A) BPDU Guard — shuts down a port when a BPDU is received. ❌
- B) Root Guard — prevents a port from becoming a root port. ❌
- C) Loop Guard — prevents a non-designated port from transitioning to forwarding if BPDUs stop being received. ✅
- D) PortFast — immediately transitions an access port to forwarding. ❌

**Answer:** C — Loop Guard prevents a port from transitioning to forwarding if it stops receiving BPDUs (which could happen if a unidirectional link failure causes BPDUs to stop arriving). Without Loop Guard, the port would time out and move to forwarding, creating a loop.

---

### Question 8 (Scenario — 10 pts)
An engineer configures EtherChannel on two switches and runs `show etherchannel summary`. Both ports show as `I` (stand-alone). The engineer verifies that both interfaces are up/up and the cable is good. What are the two most likely causes? (Select two)

- A) The LACP mode on one switch is set to `passive` and the other is also set to `passive`. ✅
- B) The interfaces have different native VLANs configured. ✅
- C) The switches are running different versions of IOS. ❌
- D) LACP is not supported on these switch models. ❌
- E) The `channel-group` numbers are different (e.g., group 1 on one switch, group 2 on the other). ❌ (Different group numbers are acceptable — only the mode and port configurations must match)

**Answer:** A and B — `passive/passive` will not form LACP (neither initiates). Native VLAN mismatch between channel members causes the EtherChannel to not bundle.

---

### Question 9 (Short Answer — 10 pts)
Explain the purpose of the 802.1Q **native VLAN** and describe a specific security risk associated with the default native VLAN configuration. What is the recommended best practice to mitigate this risk? (2–3 sentences minimum)

**Model Answer:** The native VLAN on a trunk port is the VLAN whose traffic is transmitted **untagged**. The default native VLAN on Cisco switches is VLAN 1. A security attack called **VLAN hopping** exploits this: if an attacker connects to an access port in VLAN 1 and sends double-tagged 802.1Q frames, the outer VLAN 1 tag is stripped at the first trunk, and the inner VLAN tag is used to forward the frame into any target VLAN — bypassing VLAN segmentation. The recommended mitigation is to set the native VLAN to an **unused, dedicated VLAN** (e.g., VLAN 999) that has no devices assigned to it: `switchport trunk native vlan 999`.

---

### Question 10 (Short Answer — 10 pts)
A campus switch running Rapid PVST+ has a port connected to an IP phone. The IP phone itself has an internal switch that connects to a PC. What STP configuration should be applied to the switch port connected to the phone, and what risk exists if PortFast is incorrectly applied to a trunk port connecting two switches? (3–4 sentences)

**Model Answer:** The port connecting to an IP phone should be configured as an **access port** with the voice VLAN and data VLAN properly tagged (`switchport voice vlan X`), and `spanning-tree portfast` should be enabled because the phone and PC are end devices — they will never be root bridges. PortFast allows the port to immediately transition to Forwarding, eliminating the 30-second STP delay that would otherwise prevent IP phone boot from completing. However, if PortFast is incorrectly applied to a **trunk port connecting two switches**, and that trunk port receives a BPDU from the downstream switch, the local switch may enter a Topology Change state improperly and cause network disruptions. More critically, if BPDU Guard is also enabled globally via `spanning-tree portfast bpduguard default`, the trunk port would be placed in `err-disabled` state the moment a BPDU is received — taking down the inter-switch link entirely.
