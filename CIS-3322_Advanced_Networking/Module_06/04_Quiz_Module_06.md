# Quiz: Module 06 - EtherChannel Link Aggregation

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which protocol is the open standard for dynamically negotiating EtherChannel links?

- A) PAgP
- B) LACP
- C) RSTP
- D) VTP

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: PAgP (Port Aggregation Protocol) is Cisco-proprietary and only functions between Cisco devices.
- B is correct: LACP (Link Aggregation Control Protocol) is the IEEE 802.3ad (now 802.1AX) open standard for EtherChannel negotiation. It interoperates between any vendor's equipment.
- C is incorrect: RSTP (Rapid Spanning Tree Protocol, IEEE 802.1w) is a spanning tree optimization protocol, not related to link aggregation.
- D is incorrect: VTP (VLAN Trunking Protocol) is a Cisco protocol for propagating VLAN database information. It has nothing to do with link aggregation.

---

## Question 2

Which of the following most accurately describes the difference between LACP and PAgP?

- A) LACP is an open standard (IEEE 802.3ad) that works between any vendor's devices; PAgP is Cisco-proprietary and only works between Cisco switches. Both use negotiation modes with different mode names.
- B) LACP bundles up to 16 physical links; PAgP is limited to a maximum of 4 physical links per bundle regardless of platform.
- C) LACP operates at Layer 3 and negotiates IP-based link bundles between routers; PAgP operates at Layer 2 between switches.
- D) LACP requires matching VLAN IDs; PAgP allows member ports to belong to different VLANs if the port-channel is a trunk.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The primary distinction is vendor interoperability. LACP is IEEE standard (any vendor), PAgP is Cisco-only. LACP modes are active/passive; PAgP modes are desirable/auto.
- B is incorrect: While Cisco platforms often support up to 8 active links (16 total with standby in LACP), the 16-vs-4 comparison is not the defining difference between the two protocols.
- C is incorrect: Both LACP and PAgP operate at Layer 2 between directly connected switches. Neither is a Layer 3 protocol.
- D is incorrect: Both LACP and PAgP require identical configuration on all member ports, including matching VLAN settings. Neither allows mixed VLAN membership within a bundle.

---

## Question 3

An engineer needs to trace the Layer 3 hop-by-hop path to a remote network. Which command is most appropriate?

- A) `ping`
- B) `traceroute`
- C) `netstat -ano`
- D) `nslookup`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `ping` verifies end-to-end reachability but does not reveal intermediate hop addresses.
- B is correct: `traceroute` reveals each router hop along the path by sending packets with incrementing TTL values.
- C is incorrect: `netstat -ano` lists active TCP/UDP connections and listening ports on a host.
- D is incorrect: `nslookup` resolves DNS names to IP addresses.

---

## Question 4

A network engineer is troubleshooting a failed EtherChannel. `show etherchannel summary` shows the port-channel as `(D)` down with both member ports showing `(I)` standalone. SW1 is configured with `channel-group 1 mode passive` and SW2 is configured with `channel-group 1 mode passive`. What is the cause?

- A) The VLAN configuration on the member ports does not match
- B) Two LACP passive ports never form a channel because both wait for the other to initiate
- C) The port-channel interface has not been created manually on both switches
- D) Static EtherChannel requires the keyword on instead of passive

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: VLAN mismatch causes member ports to be suspended (s), not standalone (I). The I flag indicates the ports are not bundled at all because no channel has formed.
- B is correct: LACP passive mode means the port waits for its neighbor to initiate. Two passive ports both wait indefinitely and no channel is ever formed.
- C is incorrect: The port-channel interface is created automatically when `channel-group` is configured on member ports. It does not need to be created manually.
- D is incorrect: The issue is not about static versus dynamic configuration — it is about the passive + passive combination failing regardless of whether both sides are trying to use LACP.

---

## Question 5

An engineer needs to prevent attackers from capturing plaintext management passwords on the switch network. Which configuration directly addresses this threat?

- A) Configure SSH for terminal access and HTTPS for web interfaces, disabling Telnet and HTTP
- B) Implement switch port security to restrict MAC addresses on all member ports
- C) Configure SNMPv3 authPriv to encrypt SNMP management polling traffic
- D) Use `service password-encryption` to obfuscate passwords in the running configuration

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: SSH and HTTPS encrypt management sessions in transit, preventing credential capture by packet sniffers. Configure with `transport input ssh` on VTY lines.
- B is incorrect: Port security restricts MAC-based physical access but does not encrypt management traffic transmitted over the network.
- C is incorrect: SNMPv3 authPriv encrypts SNMP traffic specifically, but does not prevent Telnet or HTTP credential exposure.
- D is incorrect: `service password-encryption` applies a weak Vigenere cipher to passwords stored in the configuration file. It does not encrypt credentials during network transmission.

---

## Question 6

An engineer applies VLAN and trunk configuration directly to the physical member interfaces (Gi0/1 and Gi0/2) instead of applying it to port-channel 1. What is the likely outcome?

- A) The configuration will work normally because port-channel interfaces inherit settings from member ports
- B) The configuration may be overridden by the port-channel interface settings, causing inconsistent behavior
- C) IOS will reject any configuration entered on physical member ports once they are in a channel group
- D) The EtherChannel will form but only Gi0/1 will carry VLAN traffic

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Configuration flows from port-channel to member ports, not the reverse. Settings applied directly to member ports may conflict with or be overridden by port-channel settings.
- B is correct: Cisco best practice and Cisco's own documentation state that all VLAN, trunking, and STP settings should be applied to the port-channel interface. Configuration applied to individual member ports can cause inconsistency and may not take effect.
- C is incorrect: IOS does not reject all configuration on member ports — you can still enter commands. The problem is behavioral inconsistency, not rejection.
- D is incorrect: EtherChannel load balancing distributes all active flows across all member links. The bundle does not segment VLAN traffic to specific physical links.

---

## Question 7

Which `show etherchannel summary` output flag indicates that a member port has been suspended due to a configuration mismatch?

- A) P (bundled in port-channel)
- B) I (standalone, not bundled)
- C) s (suspended)
- D) D (down)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: P means the port is operating normally as a bundled member of the EtherChannel.
- B is incorrect: I means the port is standalone — it is up as an individual interface but not participating in any EtherChannel bundle.
- C is correct: Lowercase s in `show etherchannel summary` indicates the port has been suspended due to a configuration mismatch with other member ports. Common causes: speed mismatch, VLAN mismatch, duplex mismatch.
- D is incorrect: D on the port-channel interface means the entire channel group is down. Lowercase s applies to individual member ports.

---

## Question 8

An engineer is configuring EtherChannel load balancing. The network primarily carries web traffic where multiple clients access a single web server. Which load-balance method would most effectively distribute traffic across member links in this scenario?

- A) `dst-mac`
- B) `src-mac`
- C) `src-ip`
- D) `src-dst-ip`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `dst-mac` hashes based on destination MAC. When all traffic goes to one server, the destination MAC is always the same, meaning all traffic hashes to the same link.
- B is incorrect: `src-mac` hashes based on source MAC. This distributes well for many unique client MACs but performs poorly if all clients are behind a single NAT device with one MAC.
- C is correct: `src-ip` hashes based on source IP address. With many clients each having a unique IP, traffic from different clients will hash to different links, distributing the load effectively.
- D is incorrect: `src-dst-ip` also distributes well but may produce the same result as `dst-mac` in scenarios with one destination. `src-ip` is more effective when there are many unique source IPs and one destination.

---

## Question 9

What is the maximum number of active physical links that Cisco Catalyst switches typically support in a single EtherChannel bundle?

- A) 2
- B) 4
- C) 8
- D) 16

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: 2 links is the minimum for EtherChannel to provide redundancy, but it is not the maximum.
- B is incorrect: 4 is a common misconception associated with older or lower-end platforms.
- C is correct: Most Cisco Catalyst platforms support up to 8 active links per EtherChannel bundle. LACP also supports up to 8 additional standby links (for 16 total configured, 8 active).
- D is incorrect: 16 is the total LACP link count (8 active + 8 standby), not the number of active links simultaneously carrying traffic.

---

## Question 10

A network engineer wants to verify that the LACP neighbor on the other end of a port-channel has the same system ID and port priorities. Which command provides this information?

- A) `show etherchannel summary`
- B) `show interfaces port-channel 1`
- C) `show lacp neighbor`
- D) `show spanning-tree interface port-channel 1`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show etherchannel summary` provides a high-level status overview with flags but does not show detailed LACP neighbor information.
- B is incorrect: `show interfaces port-channel 1` shows physical interface statistics for the logical port-channel but not LACP negotiation details or neighbor identity.
- C is correct: `show lacp neighbor` displays the LACP system ID, port priority, and operational state of the LACP partner (neighbor) on the other end of the EtherChannel.
- D is incorrect: `show spanning-tree interface port-channel 1` shows STP role and state for the port-channel. It does not contain LACP neighbor information.
