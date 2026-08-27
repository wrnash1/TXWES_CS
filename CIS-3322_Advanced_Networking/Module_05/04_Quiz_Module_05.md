# Quiz: Module 05 - Spanning Tree Protocol (STP & RSTP)

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which criteria is evaluated FIRST during the root bridge election in Spanning Tree Protocol?

- A) System MAC Address
- B) Port Priority
- C) Bridge Priority Value
- D) Link Speed

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: MAC address is the tiebreaker used only when two switches have identical Bridge Priority values. It is never the first criterion evaluated.
- B is incorrect: Port Priority determines which port is used when two ports on the same switch offer equal-cost paths to the root. It is not used in root bridge election.
- C is correct: STP elects the root bridge by comparing Bridge IDs (BIDs). The BID begins with the Bridge Priority. The switch with the lowest priority wins. If priorities tie, the lowest MAC address is used.
- D is incorrect: Link speed determines STP path cost (used for Root Port selection), not root bridge election.

---

## Question 2

In Spanning Tree Protocol, which port role is placed in a blocking state to prevent Layer 2 loops and is neither a Root Port nor a Designated Port?

- A) Alternate Port — provides the best alternative path to root; transitions to forwarding if Root Port fails (RSTP term).
- B) Blocked Port — a non-root, non-designated port that discards frames to prevent switching loops.
- C) Backup Port — redundant port on the same switch providing a second connection to the same shared segment (RSTP term).
- D) Disabled Port — administratively shut down and does not participate in STP at all.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Alternate Port is the RSTP (802.1w) term for this role. In classic 802.1D, the equivalent is simply a Blocked port.
- B is correct: In IEEE 802.1D STP, any port that is not a Root Port or Designated Port enters the Blocking state to break loops. The port discards all frames except BPDUs.
- C is incorrect: Backup Port is an RSTP-specific term for a redundant connection to the same network segment as an existing Designated Port.
- D is incorrect: A Disabled port is administratively shut down via the `shutdown` command. A Blocked port is operationally up but discarding frames — these are distinct states.

---

## Question 3

A network engineer needs to verify domain name resolution by querying DNS records from a Cisco router. Which command is most appropriate?

- A) `traceroute`
- B) `nslookup`
- C) `netstat -ano`
- D) `ping`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `traceroute` traces the Layer 3 hop path to a destination but does not perform DNS lookups.
- B is correct: `nslookup` queries DNS servers to resolve hostnames and retrieve resource records. On Cisco IOS, `nslookup [hostname]` can be used to test DNS resolution.
- C is incorrect: `netstat -ano` displays active connections and listening ports on a host. It does not perform DNS queries.
- D is incorrect: `ping` tests ICMP reachability. It may use DNS resolution internally, but it does not provide detailed DNS record information.

---

## Question 4

A switch interface has an incorrect subnet mask configured. Which action resolves this issue?

- A) Release and renew the DHCP lease
- B) Change the DNS resolver to 8.8.8.8
- C) Correct the subnet mask configuration on the interface to match network segment parameters
- D) Reboot the switch

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Releasing a DHCP lease addresses IP address conflicts or expired leases. It does not correct a manually configured subnet mask error.
- B is incorrect: Changing the DNS resolver addresses name resolution failures, not subnet mask mismatches.
- C is correct: A subnet mask mismatch prevents a host from correctly identifying local versus remote addresses, breaking communication. The fix is to correct the mask on the misconfigured interface to match the network's design.
- D is incorrect: Rebooting a switch does not change a misconfigured subnet mask unless the running config is corrected first. The same incorrect mask will reload from the saved configuration.

---

## Question 5

An engineer wants to prevent a rogue switch connected to an access port from disrupting STP by sending BPDUs. Which STP security feature should be configured on the access port?

- A) Implement switch port security to restrict access based on MAC addresses
- B) Enable BPDU Guard on the access port
- C) Configure SSH and HTTPS for management access, disabling Telnet and HTTP
- D) Enable Root Guard on the access port

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Port security limits which MAC addresses can use a port but does not specifically respond to BPDU reception. A rogue switch could still form a trunk and send BPDUs even with port security limiting MACs.
- B is correct: BPDU Guard places a port in err-disabled state immediately when any BPDU is received. This directly protects PortFast-enabled access ports from unauthorized switch connections.
- C is incorrect: SSH/HTTPS secures management sessions but has no effect on Layer 2 BPDU processing.
- D is incorrect: Root Guard protects the root bridge topology by preventing a connected switch from claiming root bridge status. It does not go to err-disabled — the port enters root-inconsistent blocking state. BPDU Guard is the more aggressive protection for access ports.

---

## Question 6

How many port states does IEEE 802.1w (RSTP) define, and what are they?

- A) Five states: Blocking, Listening, Learning, Forwarding, Disabled
- B) Four states: Blocking, Learning, Forwarding, Disabled
- C) Three states: Discarding, Learning, Forwarding
- D) Two states: Blocking and Forwarding

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Five port states (Blocking, Listening, Learning, Forwarding, Disabled) describe IEEE 802.1D classic STP, not RSTP.
- B is incorrect: Four states is not correct for either RSTP or 802.1D.
- C is correct: RSTP (802.1w) uses three port states. Discarding combines the Blocking, Listening, and Disabled states of 802.1D into a single state. Learning and Forwarding remain the same as in 802.1D.
- D is incorrect: Two states is not correct for any standard STP implementation.

---

## Question 7

An engineer configures `spanning-tree vlan 10 root primary` on SW1. What Bridge Priority value does this command set?

- A) 0 (minimum possible value)
- B) 4096
- C) 24576 (or lower if needed to win election)
- D) 32768 (default value, no change)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The `root primary` macro does not set priority to 0. Setting priority to 0 requires the explicit command `spanning-tree vlan 10 priority 0`.
- B is incorrect: 4096 is the value you get from `spanning-tree vlan 10 priority 4096` — that is explicit priority configuration, not the macro.
- C is correct: The `root primary` macro sets the priority to 24576. If another switch already has a priority lower than 24576, the macro reduces the priority further in increments of 4096 until it wins.
- D is incorrect: If `root primary` left the priority at default 32768, the switch would not necessarily become root. The macro must change the priority.

---

## Question 8

Which command would an engineer use to verify which switch is the current root bridge for VLAN 10 and what the port roles are on the local switch?

- A) `show vlan brief`
- B) `show interfaces trunk`
- C) `show spanning-tree vlan 10`
- D) `show mac address-table vlan 10`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show vlan brief` displays VLAN IDs and port assignments. It contains no STP information.
- B is incorrect: `show interfaces trunk` shows trunk port status and allowed VLANs. It does not show STP state.
- C is correct: `show spanning-tree vlan 10` displays the root bridge BID, the local switch's BID, hello/forward/max age timers, and per-port roles and states for VLAN 10.
- D is incorrect: `show mac address-table vlan 10` shows Layer 2 MAC-to-port mappings for VLAN 10. It contains no STP topology information.

---

## Question 9

Three switches (SW1, SW2, SW3) are connected in a triangle. All have default Bridge Priority 32768. Their MAC addresses are: SW1=0011.1111.AAAA, SW2=0022.2222.BBBB, SW3=0033.3333.CCCC. Which switch becomes the root bridge?

- A) SW1, because 0011.1111.AAAA is the lowest MAC address
- B) SW3, because 0033.3333.CCCC is the highest MAC address
- C) SW2, because it is in the middle of the triangle topology
- D) The election cannot complete because all three have the same priority

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: When Bridge Priorities are equal, the switch with the lowest MAC address wins. SW1's MAC (0011.1111.AAAA) is numerically lower than SW2's (0022.2222.BBBB) and SW3's (0033.3333.CCCC).
- B is incorrect: The highest MAC address loses the election, not wins it.
- C is incorrect: Physical position in the topology (middle, corner, etc.) has no bearing on root bridge election.
- D is incorrect: Equal priorities do not prevent election completion. The MAC address tiebreaker always resolves the election.

---

## Question 10

What is the primary purpose of PortFast, and why must it be restricted to access ports only?

- A) PortFast speeds up trunk negotiation by skipping DTP overhead; it must not be used on access ports because DTP only applies to trunk ports
- B) PortFast allows a port to skip STP Listening and Learning states to reach Forwarding immediately; it must only be used on access ports because enabling it on a switch-to-switch link bypasses STP and can create a bridging loop
- C) PortFast disables BPDU processing permanently on a port; it must not be used on trunk ports because trunk ports must process BPDUs for VLAN pruning
- D) PortFast enables RSTP rapid transition without BPDU exchange; it must only be used on access ports because trunk ports do not support RSTP rapid transitions

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: PortFast has nothing to do with DTP or trunk negotiation. It is an STP port-state optimization.
- B is correct: PortFast skips the 30-second Listening and Learning phase, bringing the port directly to Forwarding. If used on a switch-to-switch link, both switches skip STP processing and frames can loop indefinitely.
- C is incorrect: PortFast does not disable BPDU processing — the port still receives BPDUs (which is why BPDU Guard can trigger). It only skips the state transition delay.
- D is incorrect: PortFast is a Cisco feature that bypasses STP state transitions. It is not the same as RSTP rapid transition (which uses proposal/agreement BPDU exchanges).

---

## Question 11

A switch port is in the STP Blocking state. Which of the following statements correctly describes what a Blocking port does?

- A) It discards all frames including BPDUs
- B) It receives BPDUs but does not forward user data frames
- C) It forwards user data but drops BPDUs to prevent loops
- D) It processes BPDUs and forwards user data for critical VLANs only

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A Blocking port does NOT discard BPDUs. It continues to receive and process BPDUs so the switch can monitor the spanning tree topology and know when to transition to a different state if a root port or designated port fails.
- B is correct: A port in the Blocking state receives and processes BPDUs (to detect topology changes) but does not forward user data frames. This is the key distinction: user traffic is blocked, but STP control traffic is not.
- C is incorrect: This description is the opposite of correct behavior. BPDUs must be processed by blocking ports to maintain STP topology awareness; user frames are the traffic that is blocked.
- D is incorrect: There is no VLAN-based exemption from the Blocking state for critical VLANs in standard 802.1D STP. Per-VLAN spanning tree (PVST+) runs separate STP instances per VLAN, but each instance independently blocks or forwards on each port.

---

## Question 12

On a Cisco switch running PVST+, an engineer enters `spanning-tree vlan 10 priority 24576`. The current root bridge for VLAN 10 has priority 28672. What is the result?

- A) The command is rejected because 24576 is not a valid STP priority value
- B) The local switch becomes the root bridge for VLAN 10 because 24576 is lower than 28672
- C) The local switch becomes the secondary root for VLAN 10 but does not claim the root role
- D) The change takes effect only after the spanning-tree timers expire (up to 50 seconds)

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 24576 is a valid STP priority. Cisco STP priorities must be multiples of 4096 in the range 0–61440. 24576 = 4096 x 6, which is a valid multiple.
- B is correct: The bridge with the lowest bridge priority wins the root bridge election. If the current root has priority 28672 and this switch is set to 24576, this switch will send superior BPDUs and claim the root bridge role for VLAN 10.
- C is incorrect: A switch configured with the `spanning-tree vlan priority` command does not have a "secondary root" option in this command form. The `spanning-tree vlan root secondary` macro sets the priority to 28672, not 24576.
- D is incorrect: PVST+ root bridge changes take effect immediately after the switch sends superior BPDUs. The root election does not wait for timer expiration.

---

## Question 13

Which RSTP port role is directly equivalent to the 802.1D Non-Designated Blocked port that is discarding user frames?

- A) Alternate port
- B) Backup port
- C) Designated port
- D) Root port

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The RSTP Alternate port is a port that has received a superior BPDU from a different switch and is therefore in the Discarding state. It provides a backup path to the root bridge. In 802.1D terms, it is the non-designated port on a segment that is blocked.
- B is incorrect: The RSTP Backup port is a port that receives a superior BPDU from the same switch (on the same shared segment). This can only occur on a hub-connected topology where the same switch has two ports on the same shared collision domain — an uncommon modern scenario.
- C is incorrect: The Designated port is the forwarding port on each network segment. It is not blocked.
- D is incorrect: The Root port is the forwarding port with the best path to the root bridge on each non-root switch. It is not blocked.

---

## Question 14

An engineer runs `show spanning-tree vlan 20` on SW2 and sees the following output:

```text
VLAN0020
  Root ID    Priority    32788
             Address     0011.1111.AAAA
             Cost        19
             Port        Fa0/1 (FastEthernet0/1)
```

What does "Cost 19" represent in this output?

- A) The path cost from SW2's root port to the root bridge
- B) The priority added to 20 to form the Bridge ID priority for VLAN 20
- C) The link cost of SW2's uplink interface (Fa0/1) only
- D) The total hop count from SW2 to the root bridge

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: In `show spanning-tree` output, the "Cost" field under Root ID represents the total accumulated path cost from the local switch to the root bridge. A cost of 19 means there is one 100 Mbps link between SW2 and the root bridge (100 Mbps = STP port cost 19).
- B is incorrect: The "Priority 32788" under Root ID is the root bridge's bridge priority (32768 + VLAN ID 20 = 32788). The cost 19 is not related to the priority calculation.
- C is incorrect: The cost 19 is the total path cost to the root bridge, not just the cost of the local uplink. If there were intermediate switches, their link costs would be added together.
- D is incorrect: STP uses path cost (based on link speed), not hop count, as the metric. A cost of 19 corresponds to a 100 Mbps link cost, not a hop count of 19.

---

## Question 15

BPDU Guard is enabled on a PortFast-configured access port. A Cisco IP phone is connected, and the phone's internal switch sends BPDUs. What will happen to the port?

- A) The port ignores BPDUs because PortFast disables BPDU processing
- B) The port enters err-disabled state because BPDU Guard shuts down any port that receives a BPDU
- C) The phone becomes the root bridge for the access VLAN because it sends BPDUs
- D) The port transitions from PortFast directly to STP Listening state

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: PortFast does not disable BPDU reception. The port still receives and processes BPDUs. BPDU Guard is specifically designed to detect unexpected BPDUs on PortFast ports.
- B is correct: BPDU Guard immediately places the port in err-disabled state when any BPDU is received. This prevents devices from accidentally influencing the spanning tree topology. IP phones with built-in switches are a classic source of unexpected BPDUs.
- C is incorrect: The phone would not become the root bridge in this scenario because BPDU Guard reacts faster than the root bridge election. The port is shut down before the phone can influence the topology.
- D is incorrect: PortFast ports do not transition through Listening state when BPDUs are received — they are shut down by BPDU Guard instead.

---

## Question 16

What is the total convergence time of 802.1D STP when a link failure occurs, and how does RSTP improve upon this?

- A) 802.1D converges in approximately 50 seconds (15s Listening + 15s Learning + 20s MaxAge); RSTP converges in 1–2 seconds using proposal/agreement exchanges
- B) 802.1D converges in approximately 30 seconds (two 15-second forward delay timers); RSTP converges in approximately 30 seconds as well but with fewer states
- C) 802.1D converges in 10 seconds using BackboneFast; RSTP converges in 2 seconds using UplinkFast
- D) 802.1D converges in approximately 50 seconds; RSTP requires the same time but adds rapid aging of MAC tables

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: 802.1D convergence after a topology change is up to 50 seconds: the MaxAge timer (20 seconds) to detect that the root is unreachable, plus Listening (15 seconds) plus Learning (15 seconds) before Forwarding. RSTP eliminates the timer-based waiting by using a proposal/agreement handshake between directly connected switches, achieving convergence in approximately 1–2 seconds.
- B is incorrect: 30 seconds describes only the two forward delay timers (Listening + Learning). If the link failure causes the root port to be lost, the MaxAge timer (20 seconds) must also expire before the alternate path can be activated, making the total up to 50 seconds.
- C is incorrect: BackboneFast and UplinkFast are Cisco proprietary STP optimizations for 802.1D, not features of RSTP. RSTP is a separate protocol standard (IEEE 802.1w) that achieves 1–2 second convergence.
- D is incorrect: RSTP does not require the same time as 802.1D. The proposal/agreement mechanism in RSTP eliminates timer dependency entirely for point-to-point links, achieving sub-second convergence in most topologies.

---

## Question 17

An engineer wants to configure SW1 to automatically use the lowest available priority and become the root bridge for VLAN 30 without manually specifying a priority number. Which command accomplishes this?

- A) `spanning-tree vlan 30 priority 0`
- B) `spanning-tree vlan 30 root primary`
- C) `spanning-tree vlan 30 root secondary`
- D) `spanning-tree vlan 30 priority 4096`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `priority 0` does set the lowest possible priority, but it is a manual approach. The question asks for the automatic command. Additionally, priority 0 will always win regardless of whether other switches have been configured, which can cause unexpected behavior.
- B is correct: `spanning-tree vlan 30 root primary` is a Cisco macro that automatically sets the switch's priority to 24576 (or lower than the current root's priority if needed) to ensure the local switch wins the root election. It is the recommended command for intentionally designating a root bridge.
- C is incorrect: `root secondary` sets the priority to 28672 to make the switch the secondary (backup) root, not the primary root. It is designed to take over if the primary fails.
- D is incorrect: Priority 4096 is lower than the default (32768) but may not be low enough to beat an existing root bridge. The `root primary` macro is the appropriate tool to ensure the local switch wins.

---

## Question 18

In an RSTP topology, which port type enables rapid transition to Forwarding state using the proposal/agreement mechanism without waiting for timer expiration?

- A) Shared port (connected to a hub)
- B) Edge port (connected to an end device with PortFast enabled)
- C) Point-to-point port (full-duplex link between two switches)
- D) Alternate port (discarding state backup to the root)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Shared ports (half-duplex, hub-connected) cannot use RSTP rapid transitions. They must fall back to 802.1D timer-based behavior because the proposal/agreement mechanism requires reliable point-to-point communication.
- B is incorrect: Edge ports (PortFast) transition immediately to Forwarding because they are connected to end devices, not because of the proposal/agreement mechanism. Edge ports skip spanning tree state transitions entirely — they do not participate in proposal/agreement.
- C is correct: Point-to-point ports are full-duplex links between two switches. RSTP uses the proposal/agreement BPDU exchange on point-to-point links to achieve rapid convergence: the upstream switch proposes, the downstream switch agrees and synchronizes its ports, and the upstream port transitions to Forwarding. This is the core RSTP rapid convergence mechanism.
- D is incorrect: Alternate ports are in Discarding state and provide backup paths to the root. They cannot initiate proposal/agreement exchanges.

---

## Question 19

After a topology change is detected in 802.1D STP, Topology Change Notifications (TCNs) are sent toward the root bridge. What action does the root bridge take upon receiving a TCN?

- A) The root bridge immediately recalculates the spanning tree from scratch
- B) The root bridge sets the Topology Change (TC) bit in its BPDUs, causing all switches to shorten their MAC address aging timer to 15 seconds
- C) The root bridge sends a Topology Change Acknowledgment (TCA) only to the switch that sent the TCN
- D) The root bridge broadcasts the full MAC address table to all switches to synchronize forwarding databases

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The root bridge does not recalculate the spanning tree from scratch on every TCN. Full recalculation (triggered by superior BPDU reception) is different from TCN processing.
- B is correct: When the root bridge receives a TCN, it sets the TC bit in its Config BPDUs. All switches receiving BPDUs with the TC bit set shorten their MAC aging timer from the default (300 seconds) to the Forward Delay (15 seconds). This forces rapid MAC table flushing so that stale entries pointing to a failed link are quickly removed.
- C is incorrect: The root bridge sends the TCA to the switch that generated the TCN (via the designated switch on that segment), but it also sets the TC bit in all its BPDUs to notify the entire topology.
- D is incorrect: STP does not transmit MAC address tables between switches. MAC address learning is independent and occurs locally on each switch.

---

## Question 20

An engineer runs `show spanning-tree` and sees a port in the "BLK" state for VLAN 10. The engineer expects this port to be forwarding. What is the correct next step to diagnose the issue without making any configuration changes?

- A) Run `spanning-tree vlan 10 priority 4096` to force the port to forward
- B) Run `show spanning-tree vlan 10 detail` to identify the port role, the port that sent the superior BPDU, and the root bridge ID
- C) Run `no shutdown` on the port to clear the Blocking state
- D) Run `spanning-tree portfast` on the port to force it to Forward immediately

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Changing the bridge priority is a configuration change and may cause unintended topology effects. The question asks for a diagnostic step without making configuration changes.
- B is correct: `show spanning-tree vlan 10 detail` provides comprehensive diagnostic information: the root bridge ID, the port's role and state, the cost, the port priority, and the ID of the device whose BPDU is causing the port to block. This information is needed to determine whether the blocking is correct or the result of a misconfiguration.
- C is incorrect: `no shutdown` clears an administratively down state. A port in Blocking state is not shut down — STP is actively managing its state. `no shutdown` would have no effect on an STP Blocking port.
- D is incorrect: `spanning-tree portfast` is a configuration change that should only be applied to access ports connected to end devices. Applying it to a switch-to-switch link bypasses STP and can create a bridging loop.
