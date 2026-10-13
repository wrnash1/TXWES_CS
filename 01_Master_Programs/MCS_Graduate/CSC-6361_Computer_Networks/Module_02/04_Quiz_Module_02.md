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

---

> **Instructor Note — Questions 11–20:** These 10 questions are worth **5 pts each** (50 pts total). Append to the existing quiz or enter as a separate section.

---

### Question 11 (Multiple Choice — 5 pts)
A network engineer runs `show spanning-tree vlan 10` on a distribution switch and sees the following in the output:
```
Role: Desg  State: BLK  Cost: 4  Prio.Nbr: 128.1
```
What does the `Desg` role combined with `BLK` state indicate?

- A) This port is the Designated port but is currently in Blocking state due to a topology change in progress — RSTP rapid convergence has not yet completed. ✅
- B) This port is blocked permanently and will never transition to forwarding.
- C) This port lost the root port election and is in Blocking state as an Alternate port.
- D) This port is in err-disabled state from a BPDU Guard violation.

**Answer:** A — In RSTP (Rapid PVST+), a port can temporarily be Designated but in Discarding/Blocking state while the proposal/agreement handshake completes. Once the downstream switch sends an Agreement BPDU, the Designated port transitions immediately to Forwarding. This brief Blocking state is normal during RSTP convergence and should clear within milliseconds on a healthy network.

**Distractor Analysis:**
- B: A permanently blocked port would be an Alternate or Backup role, not Designated.
- C: A port that lost root election is an Alternate port, not Designated.
- D: Err-disabled shows as "err-disabled" status, not as a role/state combination.

---

### Question 12 (Multiple Choice — 5 pts)
An engineer is migrating a campus network from Rapid PVST+ (120 VLANs) to MST. Which statement BEST describes why MST reduces switch CPU and memory utilization compared to Rapid PVST+?

- A) MST eliminates all STP instances, so no BPDU processing occurs. ❌
- B) MST maps multiple VLANs to a single STP instance, so instead of 120 separate STP calculations and BPDU streams, the switch runs only the configured number of MST instances (plus IST). ✅
- C) MST uses a faster BPDU format that consumes less processing time per BPDU. ❌
- D) MST disables STP on all non-root switches, reducing overall CPU load. ❌

**Answer:** B — Rapid PVST+ runs a complete, independent STP instance per VLAN — 120 VLANs means 120 simultaneous STP calculations, 120 sets of BPDUs, and 120 topology databases. MST maps VLANs to instances (e.g., instance 1 = VLANs 1–60, instance 2 = VLANs 61–120), reducing this to two STP calculations regardless of VLAN count.

---

### Question 13 (Scenario — 5 pts)
A junior engineer runs `show interfaces trunk` and sees the following on a distribution switch uplink:
```
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       auto         negotiate      not-trunking  1
```
The same port on the access switch is configured with `switchport mode trunk`. Why is the trunk not forming?

- A) The access switch is using 802.1Q; the distribution switch is using ISL. ❌
- B) One side is set to `auto` (DTP passive) and the other to `trunk` (DTP active). DTP requires at least one side to be active (`desirable` or `trunk`). The `auto` side will not initiate trunking. ✅
- C) The native VLAN (1) is not allowed on the trunk. ❌
- D) Both switches must be set to `switchport mode dynamic desirable` to form a trunk. ❌

**Answer:** B — `switchport mode auto` puts the port in DTP passive mode — it will respond to DTP requests but will not initiate. However, `switchport mode trunk` sends DTP frames soliciting a trunk from the other side. In practice, with one side `trunk` and one side `auto`, a trunk SHOULD form because `trunk` mode sends DTP actively. If status still shows `not-trunking`, the DTP frames may be blocked or the port may need `switchport mode trunk` explicitly on both sides with `switchport nonegotiate` to disable DTP negotiation entirely.

---

### Question 14 (Multiple Choice — 5 pts)
Which two conditions MUST match between all switches in an MST region for them to be considered part of the same MST region? (Select two)

- A) MST region name ✅
- B) MST revision number ✅
- C) VLAN names (not just VLAN numbers) ❌
- D) The bridge priority of the MST root for each instance ❌
- E) The number of active ports on each switch ❌

**Answer:** A and B — Three parameters must match for MST region membership: (1) region name, (2) revision number, and (3) the VLAN-to-instance mapping table. If any of these three differ between switches, they are treated as separate MST regions separated by a virtual Boundary port — which significantly complicates the STP topology.

---

### Question 15 (Multiple Choice — 5 pts)
A campus network engineer wants to prevent a specific access switch port from ever transitioning to the STP root port role, while still allowing it to participate in STP normally for its designated role. Which feature should be applied?

- A) BPDU Guard — shuts down the port when a BPDU is received. ❌
- B) Root Guard — prevents the port from becoming a root port; if a superior BPDU is received, the port enters root-inconsistent state instead. ✅
- C) Loop Guard — prevents forwarding when BPDUs stop arriving on a non-designated port. ❌
- D) PortFast — immediately transitions the port to forwarding, bypassing STP elections. ❌

**Answer:** B — Root Guard is applied on ports where an access or distribution device should NEVER become the STP root, typically on downlink ports from the core/distribution layer. If a device connected to that port advertises a superior BPDU (lower bridge ID), Root Guard blocks the port and places it in root-inconsistent state rather than allowing the topology to change.

---

### Question 16 (Scenario — 5 pts)
An engineer configures EtherChannel between two switches using PAgP. SW1 has `channel-group 1 mode desirable` and SW2 has `channel-group 1 mode on`. Both ports are up/up but the EtherChannel shows `I` (stand-alone). What is the cause?

- A) PAgP and static mode (`on`) are incompatible — `on` mode disables PAgP negotiation entirely, while `desirable` expects PAgP exchanges. ✅
- B) The channel-group number must be the same on both switches for PAgP to work. ❌
- C) `desirable` mode requires both sides to use `active` mode instead. ❌
- D) PAgP requires explicit `channel-protocol pagp` configuration on both interfaces. ❌

**Answer:** A — `mode on` uses a static (unconditional) EtherChannel with no negotiation protocol. `mode desirable` uses PAgP. These two modes cannot interoperate — `on` mode does not send or process PAgP PDUs. For a successful static EtherChannel, both sides must use `on`. For PAgP, both sides must use `desirable` or one `desirable` and one `auto`.

---

### Question 17 (Multiple Choice — 5 pts)
Inter-VLAN routing is configured on a multilayer switch using SVIs. A host in VLAN 10 (10.10.10.100/24) can ping its default gateway (10.10.10.1 — DS1 SVI) but cannot ping a host in VLAN 20 (10.10.20.50). `show ip route` on DS1 shows connected routes for both VLAN 10 and VLAN 20. What is the most likely cause?

- A) `ip routing` is not enabled on DS1. ❌ (routes would not appear without `ip routing`)
- B) The VLAN 20 SVI on DS1 is in a down/down state, likely because no active access or trunk port is assigned to VLAN 20. ✅
- C) The 10.10.20.50 host has the wrong default gateway. ❌ (would cause return traffic failure, not initial ping failure if host has valid gateway)
- D) ACLs are blocking ICMP between VLANs. ❌ (could be true but "most likely" is SVI state)

**Answer:** B — An SVI is only up/up if at least one port in that VLAN is active and in forwarding state. If VLAN 20 exists in the VLAN database but no active port carries VLAN 20 traffic (e.g., no trunk allows it or no access port is assigned), the VLAN 20 SVI goes down/down and the connected route disappears or becomes unreachable. Verify with `show interfaces vlan 20` and `show vlan brief`.

---

### Question 18 (Multiple Choice — 5 pts)
A network engineer is troubleshooting a VTP domain issue. After checking `show vtp status` on all switches, they find one switch has VTP mode set to "Transparent" while all others are "Server" or "Client." Which statement BEST describes the behavior of the Transparent switch?

- A) The Transparent switch will override the VTP Server's database because Transparent mode has the highest authority. ❌
- B) The Transparent switch maintains its own local VLAN database independently, ignores VTP advertisements it receives, but forwards VTP advertisements from other switches through its trunk ports unchanged. ✅
- C) The Transparent switch cannot create VLANs locally — it can only use VLANs received from the VTP Server. ❌
- D) The Transparent switch will cause all VTP clients to lose their VLAN databases if its revision number is higher. ❌

**Answer:** B — VTP Transparent mode is a "pass-through" mode. The switch does not participate in VTP domain synchronization, stores its VLAN database locally (not affected by VTP advertisements), but does forward VTP frames through trunk ports so that VTP Servers and Clients on either side of the Transparent switch can still synchronize with each other.

---

### Question 19 (Short Answer — 5 pts)
Explain what a **Topology Change Notification (TCN)** BPDU is in Spanning Tree, what triggers it, and what effect it has on the MAC address table. Why can a high rate of TCNs degrade network performance? (2–3 sentences)

**Model Answer:** A TCN BPDU is sent by a non-root switch toward the root bridge when a port that was in Forwarding state transitions to a different state (e.g., a link goes down or a PortFast port goes up/down), signaling that the Layer 2 topology has changed. Upon receiving acknowledgment from the root, all switches in the STP domain age out their MAC address tables much faster than normal (reducing the MAC aging timer from 300 seconds to the Forward Delay of 15 seconds), forcing them to re-learn MAC addresses by flooding unknown unicast frames. A high rate of TCNs — commonly caused by unstable access ports, PortFast not being enabled on end-device ports, or flapping uplinks — causes repeated MAC table flushes and flooding storms that degrade network performance for all connected devices, as every flooded frame consumes bandwidth on every switch port in the affected VLAN.

---

### Question 20 (Short Answer — 5 pts)
A network architect proposes replacing all Layer 2 EtherChannel links in the campus distribution layer with routed Layer 3 point-to-point links running OSPF. What are two specific advantages of this design over Layer 2 EtherChannel, and what is one trade-off that must be considered? (3–4 sentences)

**Model Answer:** Two advantages of routed Layer 3 links over Layer 2 EtherChannel are: (1) **STP elimination** — Layer 3 links do not participate in Spanning Tree, removing the risk of STP topology changes, loops, and convergence delays from the distribution layer entirely; and (2) **per-destination load balancing** — OSPF equal-cost multi-path (ECMP) load balances on a per-flow or per-destination basis without the hash-based constraints of EtherChannel, which can cause uneven distribution when flows are skewed. The primary trade-off is **VLAN transport** — Layer 3 point-to-point links cannot carry trunk traffic between distribution switches, meaning VLANs that need to span multiple distribution switches must be re-routed at Layer 3 rather than bridged at Layer 2, which requires careful SVI design and may increase routing complexity for applications that depend on Layer 2 adjacency.
