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

---

## Question 11

An engineer configures EtherChannel between SW1 and SW2 using LACP. SW1's Gi0/1 and Gi0/2 are configured as `channel-group 1 mode active`. SW2's Fa0/1 and Fa0/2 are configured as `channel-group 1 mode passive`. After checking `show etherchannel summary`, the engineer sees an "I" flag next to the port-channel. What does the "I" flag indicate?

- A) The channel is in an inactive suspended state due to a configuration mismatch
- B) The channel is functioning independently without any LACP negotiation
- C) The channel is bundled and in-service
- D) The channel is using individual mode (not bundled)

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The "I" flag in `show etherchannel summary` stands for "stand-alone/individual" which appears when ports are not bundled. However, more accurately in the context of a misconfiguration, ports that fail to bundle are often suspended (shown as "s" in the individual port flags). The "I" for in-use correctly applies when the channel is functioning, but the question's context of a mismatch causing "I" would indicate the ports are in individual mode — not bundled.
- B is incorrect: Individual mode means the ports operate as standalone interfaces, not as a bundle. This is correct for what "I" represents but the question asks what the flag indicates in the context of a misconfiguration.
- C is incorrect: A bundled and in-service EtherChannel shows the "SU" flags — S for "layer 2" and U for "in use." The "I" flag does not indicate a healthy bundled state.
- D is correct per CCNA definition: The "I" flag in the `show etherchannel summary` output under the Protocol column indicates the channel is in Individual mode — the ports are not bundled and each is operating independently. This typically results from a negotiation failure due to mismatched modes or parameters.

---

## Question 12

What is the effect of configuring EtherChannel load balancing using `port-channel load-balance src-dst-ip` on a Cisco switch?

- A) Traffic is distributed based on the source MAC address only
- B) Traffic is distributed based on a hash of both source and destination IP addresses
- C) Each flow alternates between member links in a round-robin fashion for maximum distribution
- D) The load balancing algorithm changes automatically based on traffic type

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The `src-dst-ip` method uses both source and destination IP addresses, not source MAC address only. The `src-mac` or `dst-mac` methods use MAC addresses.
- B is correct: `src-dst-ip` instructs the switch to compute a hash based on both the source IP and destination IP of each frame. Frames with the same source-destination IP pair will always use the same physical link. This provides good distribution when communicating with multiple different hosts.
- C is incorrect: EtherChannel does not use round-robin per-packet load balancing in Cisco IOS. It uses per-flow hash-based balancing. All packets in the same flow (same hash result) use the same member link. Per-packet alternation would cause out-of-order delivery.
- D is incorrect: The load balancing algorithm is static once configured. It does not change automatically based on traffic type. Changing the method requires manual reconfiguration with `port-channel load-balance`.

---

## Question 13

A network administrator is troubleshooting an EtherChannel that fails to form between SW1 and SW2. The member ports on SW1 are configured as trunk ports with VLAN 10 and 20 allowed. The member ports on SW2 are configured as trunk ports with VLAN 10, 20, and 30 allowed. What will happen?

- A) The EtherChannel forms but VLAN 30 is silently pruned from all frames
- B) The EtherChannel forms because trunk configuration differences are permitted
- C) The EtherChannel does not form because the allowed VLAN list must be identical on all member ports
- D) The EtherChannel forms but generates a CDP warning about the VLAN mismatch

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: EtherChannel does not silently prune VLANs to resolve a configuration mismatch. If the allowed VLAN lists differ, the channel fails to form or ports become suspended.
- B is incorrect: All configuration parameters on member ports including the allowed VLAN list, trunk encapsulation, and native VLAN must be identical. Differences cause the EtherChannel to not form or ports to be suspended.
- C is correct: One of the CCNA-tested EtherChannel requirements is that all member ports must have identical configurations. The allowed VLAN list must match exactly. If SW1 allows VLANs 10,20 and SW2 allows VLANs 10,20,30, the EtherChannel will fail — either not forming at all or showing ports as suspended (flag "s") in `show etherchannel summary`.
- D is incorrect: CDP does not generate warnings about EtherChannel VLAN mismatch. The EtherChannel mechanism itself detects the inconsistency and prevents bundling.

---

## Question 14

An engineer enters `channel-group 1 mode on` on both ends of a two-link EtherChannel. What negotiation protocol is used?

- A) LACP (IEEE 802.3ad)
- B) PAgP (Cisco-proprietary)
- C) No negotiation protocol — static EtherChannel without LACP or PAgP
- D) DTP (Dynamic Trunking Protocol) is used to negotiate the channel

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: LACP is used when `mode active` or `mode passive` is configured. The `on` keyword explicitly bypasses LACP negotiation.
- B is incorrect: PAgP is used when `mode desirable` or `mode auto` is configured. The `on` keyword bypasses PAgP negotiation.
- C is correct: `channel-group mode on` creates a static EtherChannel with no negotiation protocol. Both sides are forced into the bundle without any LACP or PAgP exchange. The `show etherchannel summary` output will show a dash (—) in the Protocol column for static channels.
- D is incorrect: DTP is used for switchport trunk negotiation (access vs. trunk mode). It is not related to EtherChannel negotiation.

---

## Question 15

`show etherchannel summary` on SW1 shows the following:

```text
Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)       LACP        Gi0/1(P)  Gi0/2(P)  Gi0/3(s)  Gi0/4(s)
```

What does the "(s)" flag on Gi0/3 and Gi0/4 indicate?

- A) The ports are suspended due to a configuration mismatch
- B) The ports are standby LACP ports — configured but not actively forwarding, waiting in reserve
- C) The ports are in err-disabled state
- D) The ports are shut down administratively

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Suspended ports due to mismatch show a different error state. The "s" lowercase flag in the Ports column indicates LACP hot-standby, not a mismatch condition.
- B is correct: LACP supports up to 8 active member links ("P" flag) and up to 8 additional standby links ("s" flag). Standby ports are configured and ready to become active if an active member fails, but they do not forward traffic while in standby.
- C is incorrect: Err-disabled ports would not appear in the EtherChannel bundle at all, or would show an error indication. Err-disabled is a separate switch port state.
- D is incorrect: Administratively shut-down ports would not participate in EtherChannel at all. The "s" flag indicates an active LACP standby state, not administrative shutdown.

---

## Question 16

After configuring an EtherChannel between two switches, the engineer notices that traffic from some hosts always uses the same physical link regardless of the number of active member ports. Why?

- A) EtherChannel is misconfigured — it should round-robin between all links for every frame
- B) This is expected behavior: EtherChannel uses a hash algorithm that consistently maps specific source-destination pairs to the same physical link
- C) The switch is faulty — contact Cisco TAC for hardware replacement
- D) This indicates the load-balance method is set to `dst-mac` and all traffic has the same destination MAC

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Per-frame round-robin is not how Cisco EtherChannel operates. Round-robin per packet would cause out-of-order delivery within a TCP flow. Hash-based per-flow distribution is the design choice.
- B is correct: EtherChannel uses a hashing algorithm (configurable via `port-channel load-balance`) to assign each flow to a specific physical link. The same source-destination pair always produces the same hash and therefore always uses the same link. This ensures in-order delivery within each flow.
- C is incorrect: This is not a hardware fault. Hash-based distribution is the designed and documented behavior of Cisco EtherChannel load balancing.
- D is partially correct in premise: If `dst-mac` load balancing is configured and all traffic goes to the same destination MAC (e.g., a default gateway), all traffic will use one link. However, option B is the more accurate and complete explanation of why specific source-destination pairs consistently use the same link.

---

## Question 17

Which command globally changes the EtherChannel load balancing method on a Cisco switch to use both source and destination MAC addresses?

- A) `port-channel load-balance src-dst-mac` applied under port-channel interface configuration
- B) `port-channel load-balance src-dst-mac` applied in global configuration mode
- C) `etherchannel load-balance src-dst-mac` applied in global configuration mode
- D) `interface port-channel 1 load-balance src-dst-mac`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The `port-channel load-balance` command is a global configuration command, not an interface-level command. It applies to all EtherChannel bundles on the switch.
- B is correct: `port-channel load-balance src-dst-mac` is entered in global configuration mode and affects all EtherChannel bundles on the switch simultaneously. The available methods vary by platform but include `src-mac`, `dst-mac`, `src-dst-mac`, `src-ip`, `dst-ip`, and `src-dst-ip`.
- C is incorrect: The command begins with `port-channel`, not `etherchannel`. `etherchannel` is not the correct IOS command prefix for the load-balance method.
- D is incorrect: This is not valid IOS syntax. Load balancing is configured globally, not per port-channel interface.

---

## Question 18

A network engineer needs to create an EtherChannel between a Cisco switch and a non-Cisco switch that supports IEEE 802.3ad link aggregation. Which channel mode on the Cisco side is required?

- A) `channel-group 1 mode desirable`
- B) `channel-group 1 mode active`
- C) `channel-group 1 mode on`
- D) `channel-group 1 mode auto`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: PAgP `desirable` mode is Cisco-proprietary. Non-Cisco switches do not support PAgP. This configuration will not form an EtherChannel with a non-Cisco device.
- B is correct: LACP `active` mode uses the IEEE 802.3ad standard, which is supported by virtually all enterprise switch vendors. Configuring the Cisco switch in `active` mode allows it to form an LACP EtherChannel with any 802.3ad-compliant non-Cisco switch.
- C is incorrect: Static `on` mode works only when both sides are also configured as `on`. Non-Cisco switches running 802.3ad would use LACP PDUs, not static mode. The static mode on the Cisco switch and LACP on the non-Cisco switch would be incompatible.
- D is incorrect: PAgP `auto` mode is passive PAgP — it waits for the other side to initiate PAgP negotiation. Non-Cisco switches do not speak PAgP. This mode will not form an EtherChannel with a non-Cisco 802.3ad device.

---

## Question 19

An EtherChannel bundle (port-channel 1) is configured as a trunk carrying VLANs 10 and 20. From STP's perspective, how does the spanning tree algorithm treat this bundle?

- A) STP treats each physical member link as a separate interface with independent port costs and roles
- B) STP treats the port-channel as a single logical interface with one port cost and one port role
- C) STP is disabled on EtherChannel bundles to prevent port-cost calculation conflicts
- D) STP assigns the lowest port cost to whichever physical link is currently active

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: If STP treated each physical link independently, the redundant links within the bundle would be blocked by STP rather than all forwarding together. EtherChannel is specifically designed to present a single logical link to STP.
- B is correct: From STP's perspective, the port-channel (Po1) is a single logical interface. STP calculates port cost based on the total bandwidth of the bundle (e.g., two 1 Gbps links = 2 Gbps port-channel, with a lower aggregate STP cost). STP assigns one port role (Root, Designated, or Alternate) to the entire port-channel.
- C is incorrect: STP is not disabled on port-channel interfaces. The port-channel participates in spanning tree as a single logical port.
- D is incorrect: The STP cost for a port-channel is based on the aggregate bandwidth of all active member links, not the single lowest cost link.

---

## Question 20

An engineer enters the following commands on SW1:

```ios
interface range GigabitEthernet0/1 - 2
 channel-group 2 mode passive
```

No corresponding configuration exists on SW2. What is the result?

- A) The EtherChannel forms because passive mode can operate without a partner
- B) The EtherChannel does not form — LACP passive mode requires the partner to actively initiate (active mode)
- C) The ports become err-disabled because passive mode is not a valid channel mode
- D) The ports form a static EtherChannel because passive mode defaults to static if no partner responds

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: LACP passive mode is analogous to DTP `dynamic auto`. It waits for the other side to initiate. If SW2 has no channel-group configuration, there is no LACP PDU sent, and passive mode will not self-activate.
- B is correct: LACP `passive` mode means the port will respond to LACP PDUs but will not initiate them. If SW2 has no EtherChannel or LACP configuration, it never sends LACP PDUs, so SW1's passive ports have nothing to respond to. The channel remains inactive.
- C is incorrect: LACP passive is a valid channel mode. The ports do not enter err-disabled state just because no EtherChannel forms. The interfaces operate as normal individual access or trunk ports.
- D is incorrect: LACP passive does not fall back to static mode. If no LACP partner is detected, the ports operate as individual interfaces without any EtherChannel behavior.
