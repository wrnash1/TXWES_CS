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
