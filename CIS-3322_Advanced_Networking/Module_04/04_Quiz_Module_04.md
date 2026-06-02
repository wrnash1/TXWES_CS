# Quiz: Module 04 - Switching Concepts & VLANs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which frame-tagging standard is used to carry traffic for multiple VLANs over a single physical switch port connection?

- A) ISL (Inter-Switch Link)
- B) 802.11
- C) 802.1Q
- D) LACP

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: ISL is a Cisco legacy VLAN tagging protocol that encapsulates the entire Ethernet frame. It has been deprecated in favor of IEEE 802.1Q and is not supported on modern Cisco switches.
- B is incorrect: IEEE 802.11 is the standard for wireless LAN (Wi-Fi) operation. It has nothing to do with VLAN trunking.
- C is correct: IEEE 802.1Q is the industry-standard frame-tagging protocol used on VLAN trunk links. It inserts a 4-byte tag into the Ethernet frame identifying the VLAN ID (12 bits, supporting VLAN IDs 1-4094).
- D is incorrect: LACP (Link Aggregation Control Protocol) is the IEEE standard for EtherChannel link bundling. It is not related to VLAN tagging.

---

## Question 2

Which of the following most accurately describes DTP (Dynamic Trunking Protocol)?

- A) A Cisco-proprietary protocol that allows adjacent switch ports to automatically negotiate 802.1Q trunk formation using modes such as dynamic auto and dynamic desirable.
- B) An IEEE standard that allows a switch to forward frames based on destination MAC addresses by learning source MACs from incoming frames.
- C) A Cisco protocol that propagates VLAN configuration from a VTP server to all VTP client switches in the same management domain.
- D) An IEEE spanning-tree enhancement that places ports connected to end hosts directly into forwarding state, bypassing listening and learning.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: DTP is Cisco-proprietary and handles trunk negotiation between adjacent Cisco switches. Security best practice is to disable DTP on user-facing ports with `switchport nonegotiate`.
- B is incorrect: This describes the basic Layer 2 MAC address learning and forwarding process of a switch, not DTP.
- C is incorrect: This describes VTP (VLAN Trunking Protocol), which synchronizes the VLAN database across switches. VTP and DTP are separate protocols.
- D is incorrect: This describes PortFast, which is an STP optimization for access ports, not DTP.

---

## Question 3

An engineer needs to trace the hop-by-hop Layer 3 path from a source to a remote destination. Which command is most appropriate?

- A) `nslookup`
- B) `traceroute`
- C) `netstat -ano`
- D) `ping`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `nslookup` performs DNS lookups and resolves hostnames to IP addresses. It does not show routing paths.
- B is correct: `traceroute` (or `tracert` on Windows) reveals the hop-by-hop path by sending packets with incrementing TTL values to identify each intermediate router.
- C is incorrect: `netstat -ano` lists active network connections and listening ports on a host. It has no routing path functionality.
- D is incorrect: `ping` tests end-to-end reachability but does not display intermediate hop addresses.

---

## Question 4

A network engineer configures SW1 GigabitEthernet0/1 as `switchport mode dynamic auto` and SW2 GigabitEthernet0/1 also as `switchport mode dynamic auto`. What is the resulting state of the link?

- A) Both ports form a 802.1Q trunk
- B) Both ports remain as access ports
- C) One port becomes trunk and the other remains access
- D) The ports enter an error-disabled state

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Two `dynamic auto` ports both wait passively for the other side to initiate trunk negotiation. Since neither side initiates, no trunk forms.
- B is correct: `Dynamic auto` mode means the port will form a trunk only if the other side actively requests it (using `dynamic desirable` or `trunk` mode). Two passive ports result in both remaining as access ports.
- C is incorrect: DTP negotiation is symmetric between two `dynamic auto` ports — both sides behave identically and neither becomes trunk.
- D is incorrect: `dynamic auto` on both sides does not cause an error-disabled state. The ports simply operate in access mode.

---

## Question 5

A network administrator wants to prevent attackers from capturing plaintext management passwords on the switch network. Which configuration directly addresses this threat?

- A) Configure SSH for terminal access and HTTPS for web interfaces, disabling Telnet and HTTP
- B) Implement switch port security to restrict MAC addresses on all ports
- C) Disable DTP on all switch ports with `switchport nonegotiate`
- D) Enable VTP transparent mode on all switches

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: SSH and HTTPS encrypt management sessions, preventing credential capture by packet sniffers. Configure with `line vty 0 4` then `transport input ssh` on Cisco IOS.
- B is incorrect: Port security restricts MAC-based access but does not encrypt management traffic. Telnet passwords are still transmitted in plaintext over a port-secured port.
- C is incorrect: Disabling DTP prevents unauthorized trunk formation (a VLAN hopping defense), but does not encrypt management credentials.
- D is incorrect: VTP transparent mode prevents VLAN database propagation attacks but does not protect management session credentials from sniffing.

---

## Question 6

An administrator runs `show vlan brief` on a switch and notices that GigabitEthernet0/1 (which is the trunk port to the distribution switch) is not listed under any VLAN. What does this indicate?

- A) GigabitEthernet0/1 is shut down and not forwarding traffic
- B) GigabitEthernet0/1 is configured as a trunk port and trunk ports do not appear in show vlan brief
- C) GigabitEthernet0/1 has not been assigned to any VLAN and is inactive
- D) The VLAN database is empty and needs to be repopulated

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: An interface that is shut down would still appear in `show vlan brief` if it were configured as an access port. The absence from VLAN assignment is about port mode, not operational state.
- B is correct: Trunk ports carry multiple VLANs and are not listed under any specific VLAN in `show vlan brief`. Use `show interfaces trunk` to verify trunk port configuration.
- C is incorrect: A trunk port is actively carrying all allowed VLANs; it is not inactive simply because it doesn't appear in `show vlan brief`.
- D is incorrect: The VLAN database state is unrelated to a trunk port's absence from `show vlan brief` output.

---

## Question 7

A trunk link between SW1 and SW2 has a native VLAN mismatch — SW1 uses VLAN 1 and SW2 uses VLAN 99 as the native VLAN. What is the most likely observable symptom of this misconfiguration?

- A) The trunk link goes into err-disabled state
- B) CDP generates a native VLAN mismatch warning and untagged traffic may be misassigned
- C) All VLANs including tagged VLANs stop passing traffic across the trunk
- D) Both switches automatically renegotiate the native VLAN to match

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Native VLAN mismatch does not cause err-disabled. Err-disabled is triggered by specific security or hardware events.
- B is correct: A native VLAN mismatch generates a CDP warning (`%CDP-4-NATIVE_VLAN_MISMATCH`) and causes untagged frames to be assigned to different VLANs on each side, potentially creating traffic confusion. Tagged VLAN traffic is unaffected.
- C is incorrect: Tagged VLAN traffic on the trunk continues to flow correctly. Only untagged (native VLAN) traffic is affected by the mismatch.
- D is incorrect: Native VLANs are not automatically negotiated. You must manually configure matching native VLANs on both ends of the trunk.

---

## Question 8

Which command correctly assigns FastEthernet0/5 to VLAN 30 as an access port on a Cisco switch?

- A) `vlan 30` followed by `interface FastEthernet0/5`
- B) `interface FastEthernet0/5` then `switchport mode access` then `switchport access vlan 30`
- C) `interface FastEthernet0/5` then `switchport trunk allowed vlan 30`
- D) `vlan 30` then `switchport access FastEthernet0/5`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `vlan 30` creates the VLAN in the VLAN database but does not configure port assignment. The VLAN and port configuration are separate steps.
- B is correct: The correct sequence is to enter the interface, set the mode to access, and then assign the access VLAN. Both commands are required.
- C is incorrect: `switchport trunk allowed vlan 30` is used on trunk ports to specify which VLANs are allowed, not on access ports.
- D is incorrect: `switchport access` is not a global command. It must be entered in interface configuration mode on the specific interface.

---

## Question 9

What is the purpose of changing the native VLAN on a trunk from VLAN 1 to an unused VLAN such as VLAN 999?

- A) To allow more than 4094 VLANs to operate on the trunk
- B) To improve trunk negotiation speed between switches
- C) To mitigate VLAN hopping attacks that exploit double-tagged frames on the native VLAN
- D) To enable VTP to synchronize VLAN databases faster

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The number of supported VLANs (1-4094) is determined by the 12-bit VLAN ID field in the 802.1Q header. Changing the native VLAN does not affect this limit.
- B is incorrect: Native VLAN configuration has no effect on DTP negotiation speed.
- C is correct: VLAN hopping via double-tagging exploits the fact that a switch strips the outer 802.1Q tag (native VLAN) and forwards the inner-tagged frame to another VLAN. Using an unused VLAN as the native VLAN ensures no end devices are on that VLAN, eliminating the attack vector.
- D is incorrect: VTP synchronization speed is unaffected by native VLAN configuration.

---

## Question 10

A network engineer runs `show interfaces trunk` on SW1 and sees the following entry: Gi0/1 appears in "Vlans allowed on trunk" as 1-4094 but in "Vlans allowed and active in management domain" as only 10,20. What is the most likely explanation?

- A) VLANs other than 10 and 20 do not exist in the VLAN database on SW1
- B) Spanning Tree Protocol is blocking all VLANs except 10 and 20
- C) The trunk encapsulation failed and only two VLANs can be carried
- D) VLAN pruning has removed all VLANs except 10 and 20 from the trunk

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: "Vlans allowed on trunk" shows the configured allowed VLAN list. "Vlans allowed and active" shows only the VLANs that exist in the VLAN database. VLANs not created with the `vlan` command will not appear in the active list.
- B is incorrect: STP blocking status is shown in the fourth row of `show interfaces trunk` output ("Vlans in spanning tree forwarding state"). A VLAN missing from the active list is a VLAN database issue, not an STP issue.
- C is incorrect: Trunk encapsulation failure would prevent the trunk from forming at all. It would not selectively allow only two VLANs.
- D is incorrect: VTP pruning removes VLANs from trunks to conserve bandwidth, but pruned VLANs are shown as absent in the fourth row, not the third row. The third row (active) reflects VLAN database existence.
