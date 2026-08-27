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

## Question 11

A Cisco switch port is currently operating in `dynamic auto` mode. A second port on a neighboring switch is also in `dynamic auto` mode. What is the resulting operational mode of the link?

- A) Trunk — both sides are willing to trunk so a trunk forms
- B) Access — neither side actively negotiates, so no trunk forms and the port remains in access mode
- C) The link enters an err-disabled state because two auto ports cannot connect
- D) Trunk — DTP always forms a trunk when two switches are directly connected

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `dynamic auto` means "I will trunk if you ask me to." Neither side initiates DTP negotiation, so no trunk is formed. Both sides remain in access mode.
- B is correct: DTP `dynamic auto` is passive — it waits for the other side to initiate. When both sides are passive (`dynamic auto` or `dynamic auto`), neither initiates, so the result is access mode. A trunk only forms when at least one side is `dynamic desirable` or `trunk`.
- C is incorrect: Two `dynamic auto` ports do not cause err-disabled state. The port simply remains operational as an access port.
- D is incorrect: DTP does not automatically form a trunk between any two directly connected switches. The negotiation mode determines the outcome. Both-auto results in access mode.

---

## Question 12

Which Cisco IOS command verifies the current administrative and operational mode of a specific switch port, including whether it is in access or trunk mode and which VLAN it is in?

- A) `show vlan brief`
- B) `show interfaces GigabitEthernet0/1 switchport`
- C) `show interfaces trunk`
- D) `show cdp neighbors`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `show vlan brief` shows VLAN names and the access ports assigned to each VLAN. It does not show per-port switchport mode details (administrative mode, operational mode, or DTP configuration).
- B is correct: `show interfaces [interface] switchport` provides the full switchport profile for a single interface: administrative mode, operational mode, trunking encapsulation, access VLAN, native VLAN, and DTP status. This is the authoritative per-port verification command.
- C is incorrect: `show interfaces trunk` shows only ports currently operating in trunk mode. It does not show access port details and will not display ports in access mode.
- D is incorrect: `show cdp neighbors` shows neighboring Cisco devices. It has no relationship to switchport mode verification.

---

## Question 13

A network engineer needs to prevent a host from being placed in VLAN 1 as a result of automatic DTP negotiation. The port is connected to an end device. Which two commands harden the port against DTP-based VLAN attacks?

- A) `switchport mode trunk` and `switchport trunk allowed vlan 1`
- B) `switchport mode access` and `switchport nonegotiate`
- C) `switchport access vlan 1` and `no switchport`
- D) `spanning-tree portfast` and `switchport mode dynamic desirable`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Configuring the port as a trunk is the opposite of the goal. A trunk carries multiple VLANs and should not be connected to an end device. This would also increase the attack surface.
- B is correct: `switchport mode access` forces the port into access mode (cannot be negotiated to trunk). `switchport nonegotiate` disables DTP entirely on the port, preventing any DTP-based negotiation. Together these two commands harden the port against VLAN hopping attacks via DTP.
- C is incorrect: `switchport access vlan 1` would assign the port to VLAN 1, which is what we want to avoid. `no switchport` removes the Layer 2 configuration and converts the port to a Layer 3 routed port.
- D is incorrect: PortFast is a Spanning Tree optimization for access ports (not a VLAN security measure). `dynamic desirable` actively tries to form a trunk, which is the opposite of what is needed.

---

## Question 14

A switch has VLANs 10, 20, and 30 configured. An administrator enters `no vlan 20` in global configuration mode. What happens to ports currently assigned to VLAN 20?

- A) The ports are automatically reassigned to VLAN 1
- B) The ports remain assigned to VLAN 20, but traffic is not forwarded because VLAN 20 no longer exists in the database
- C) The ports are shut down and placed in err-disabled state
- D) The ports are automatically reassigned to the next numerically available VLAN

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Cisco IOS does not automatically reassign ports to VLAN 1 when a VLAN is deleted. The port retains its VLAN assignment in the configuration, but the VLAN no longer exists in the database.
- B is correct: When a VLAN is deleted with `no vlan`, the switch removes it from the VLAN database. Ports still assigned to the deleted VLAN remain in that assignment but are effectively inactive — no traffic is forwarded because the VLAN does not exist. `show vlan brief` will show these ports under an "inactive" state.
- C is incorrect: Deleting a VLAN does not place ports in err-disabled state. Err-disabled results from security or spanning tree violations, not VLAN deletion.
- D is incorrect: Cisco IOS does not automatically reassign ports to adjacent VLANs when a VLAN is deleted. The port retains its original VLAN assignment in configuration.

---

## Question 15

An 802.1Q frame arrives on a trunk port with a VLAN tag of 0. How does the receiving switch handle this frame?

- A) The frame is forwarded to all ports in VLAN 0 because 0 is a valid data VLAN
- B) The frame is treated as a native VLAN frame and forwarded to the configured native VLAN
- C) The frame is dropped because VLAN 0 is reserved and not a usable data VLAN
- D) The switch re-tags the frame with VLAN 1 before forwarding

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: VLAN 0 is reserved in the 802.1Q specification. There is no VLAN 0 in the VLAN database; it cannot be created or assigned as a data VLAN.
- B is incorrect: A VLAN tag of 0 in the 802.1Q header is a priority tag used for CoS markings with no VLAN assignment, not a native VLAN indicator. Native VLAN frames are sent without a VLAN tag (untagged), not with tag 0.
- C is correct: VLAN 0 is reserved by IEEE 802.1Q. The tag value of 0 in the VLAN ID field indicates a frame carrying only priority information (Class of Service) with no VLAN membership. It is not a usable data VLAN and Cisco IOS treats it as reserved.
- D is incorrect: Cisco IOS does not re-tag frames from VLAN 0 to VLAN 1. The VLAN 0 handling is defined by the 802.1Q standard as a priority-only frame designation.

---

## Question 16

A switch is operating in VTP server mode with VTP domain "CORP" and revision number 15. A new switch with VTP server mode, domain "CORP", and revision number 18 is connected to the network. What happens?

- A) The new switch ignores the existing switches because it is also in server mode
- B) The new switch's higher revision number causes it to overwrite the VLAN database on all other switches in the domain
- C) The existing switch with revision 15 becomes the VTP primary server and rejects the new switch
- D) VTP does not synchronize because two server-mode switches cannot be in the same domain

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: VTP server mode does not prevent synchronization with other VTP servers. Any VTP device in the same domain with a higher revision number will propagate its VLAN database to all other devices.
- B is correct: This describes the classic VTP revision number vulnerability. A device with a higher revision number (even a new or unauthorized switch) will overwrite the VLAN database on all switches in the domain. This is why VTP is considered dangerous — a misconfigured switch can delete all VLANs from a production network.
- C is incorrect: There is no concept of a "VTP primary server" that blocks other servers in VTP version 1 and 2. VTP version 3 introduced a primary server designation, but the default behavior in VTP v1/v2 is to accept any higher revision number.
- D is incorrect: Multiple VTP server-mode switches can and do coexist in the same domain. All servers in the domain accept updates from devices with higher revision numbers.

---

## Question 17

A network engineer configures `switchport trunk native vlan 99` on SW1's Gi0/1 interface. The neighboring SW2's Gi0/1 still has native VLAN 1. What symptom will occur and what log message will appear?

- A) The trunk will not form because native VLAN mismatch prevents DTP negotiation
- B) The trunk forms but CDP generates a "Native VLAN mismatch" warning message on both switches
- C) SW1 drops all frames on VLAN 99 and SW2 drops all frames on VLAN 1
- D) The mismatch causes a broadcast storm between the two switches

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A native VLAN mismatch does not prevent the trunk from forming. The trunk is up at Layer 1 and Layer 2. The mismatch is detected by CDP and reported as a warning, but DTP does not check native VLAN consistency.
- B is correct: When native VLANs differ between trunk partners, the trunk operates but frames sent untagged by SW1 (expecting VLAN 99) will be received by SW2 and placed in VLAN 1 (SW2's native VLAN). This causes unexpected VLAN membership. CDP detects the discrepancy and logs a "native VLAN mismatch" message on both switches.
- C is incorrect: Frames are not dropped based on native VLAN mismatch. They are misassigned — frames intended for VLAN 99 end up in VLAN 1 on SW2, and vice versa.
- D is incorrect: A native VLAN mismatch does not cause broadcast storms. Broadcast storms are caused by Layer 2 loops without STP, not VLAN configuration discrepancies.

---

## Question 18

The maximum number of VLANs supported on a standard Cisco Catalyst switch is 4094. Why is VLAN 4094 given as the limit rather than 4096?

- A) Cisco reserves VLANs 4095 and 4096 for internal switch processes
- B) The 802.1Q VLAN ID field is 12 bits, allowing values 0–4095, but VLANs 0 and 4095 are reserved
- C) VLANs above 4000 require an extended VLAN range license on Cisco switches
- D) The 802.1Q specification limits trunk ports to 4094 simultaneous tagged VLANs for performance reasons

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Cisco does not reserve 4095 and 4096 for internal use. The limit is defined by the IEEE 802.1Q standard, not by Cisco's internal requirements.
- B is correct: The 802.1Q VLAN ID field is 12 bits, providing values 0 through 4095 (2^12 = 4096 values). VLAN 0 is reserved for priority-tagged frames (no VLAN membership) and VLAN 4095 (0xFFF) is reserved by the standard. This leaves VLANs 1 through 4094 as usable. VLAN 1 is the default and VLANs 1002–1005 are reserved for legacy protocols.
- C is incorrect: Extended VLAN range (1006–4094) may require VTP transparent or off mode on older IOS versions, but this is a VTP limitation, not a licensing restriction on modern Cisco Catalyst switches.
- D is incorrect: The 4094 VLAN limit is a specification limit, not a performance-based restriction. Cisco switches can forward traffic on all 4094 VLANs simultaneously within hardware capacity.

---

## Question 19

A frame arrives untagged on a trunk port configured with `switchport trunk native vlan 10`. Which VLAN does the switch assign this frame to?

- A) VLAN 1 (the default VLAN always receives untagged frames on trunk ports)
- B) VLAN 10 (the configured native VLAN receives all untagged frames on the trunk)
- C) The frame is dropped because trunk ports do not accept untagged frames
- D) The switch tags the frame with VLAN 1 before forwarding it

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The native VLAN is configurable. If the native VLAN is changed from VLAN 1 to VLAN 10, then VLAN 10 receives untagged frames on that trunk — not VLAN 1.
- B is correct: The native VLAN is the VLAN to which untagged frames received on a trunk port are assigned. By default this is VLAN 1, but after `switchport trunk native vlan 10`, all untagged frames received on that trunk are placed in VLAN 10.
- C is incorrect: Trunk ports do accept untagged frames — they assign them to the native VLAN. This is the entire purpose of the native VLAN concept on 802.1Q trunks.
- D is incorrect: The switch does not re-tag untagged frames with VLAN 1. It assigns them to the native VLAN internally for forwarding decisions. Frames leave the trunk toward the destination following standard 802.1Q tagging rules.

---

## Question 20

A network administrator wants to verify whether a trunk between SW1 and SW2 is correctly forwarding VLAN 30 traffic. The `show interfaces trunk` output on SW1 shows VLAN 30 in "Vlans allowed on trunk" but not in "Vlans in spanning tree forwarding state and not pruned." What does this indicate?

- A) VLAN 30 traffic is being blocked by Spanning Tree Protocol on this trunk
- B) VLAN 30 does not exist in the VLAN database on SW1
- C) The trunk is not carrying VLAN 30 because of a misconfigured native VLAN
- D) VLAN 30 is administratively shut down on this trunk

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The fourth row of `show interfaces trunk` — "Vlans in spanning tree forwarding state and not pruned" — shows only VLANs that are both active in the VLAN database AND in the STP forwarding state on that trunk. VLAN 30 appearing in row 1 (allowed) but absent from row 4 indicates STP is blocking VLAN 30 traffic on this specific trunk interface.
- B is incorrect: If VLAN 30 did not exist in the VLAN database, it would be absent from the "Vlans allowed and active in management domain" row (row 3), not just from row 4. VLAN 30 appearing in row 1 (allowed) could still mean it is blocked by STP in row 4.
- C is incorrect: Native VLAN misconfiguration affects untagged frame assignment. It does not cause a specific VLAN to be absent from the STP forwarding state row.
- D is incorrect: There is no concept of "administratively shutting down" a specific VLAN on a trunk in standard Cisco IOS. VLANs are either present in the database and active, or they are removed with `no vlan`.

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
