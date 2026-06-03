# Quiz: Module 11 — Switching: VLANs, STP, and EtherChannel

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Question 1

A network administrator needs to segment a company's 48-port switch so that the Finance department (ports 1–12), the HR department (ports 13–24), and the Engineering department (ports 25–36) cannot exchange traffic at Layer 2 with each other, even though all devices are on the same physical switch. Which technology accomplishes this?

A) Subnetting — assigning each group a different IP subnet prevents Layer 2 communication between groups

B) VLANs — creating separate VLANs for each department creates separate broadcast domains, preventing Layer 2 communication between groups

C) Port Security — limiting the MAC addresses on each port prevents cross-department communication

D) STP — Spanning Tree blocks ports between departments to prevent cross-department traffic

Correct Answer: B) VLANs — creating separate VLANs for each department creates separate broadcast domains, preventing Layer 2 communication between groups

Distractor Analysis:

Why A is incorrect: Subnetting is a Layer 3 concept. Devices on different subnets still share the same Layer 2 broadcast domain if they are on the same switch with no VLAN segmentation. Layer 3 routing would allow communication between subnets; VLANs are needed to isolate at Layer 2.

Why C is incorrect: Port Security limits the number of MAC addresses on a port, preventing MAC flooding attacks. It does not create separate broadcast domains or prevent traffic between ports assigned to the same VLAN.

Why D is incorrect: STP prevents Layer 2 loops. It does not isolate traffic between departments or create separate broadcast domains. STP operates within a VLAN, not between them.

---

### Question 2

A switch administrator configures a trunk port and sees this warning in the console: "Native VLAN mismatch on FastEthernet0/1 (1), with FastEthernet0/1 (10) on remote switch." What does this indicate and what is the correct action?

A) The switch is running two different spanning tree instances and the native VLAN configuration has no effect on security

B) The trunk port native VLAN is VLAN 1 on this switch and VLAN 10 on the remote switch — they must be set to the same unused VLAN on both ends

C) The trunk port can only carry traffic for the native VLAN and must be reconfigured to carry additional VLANs

D) VLAN 10 is not in the allowed VLAN list on the trunk — adding it to the allowed list will resolve the warning

Correct Answer: B) The trunk port native VLAN is VLAN 1 on this switch and VLAN 10 on the remote switch — they must be set to the same unused VLAN on both ends

Distractor Analysis:

Why A is incorrect: A native VLAN mismatch is a real operational and security problem. Untagged traffic from one switch is placed into a different VLAN on the other switch. This can cause traffic to leak between VLANs and is exploited in VLAN hopping double-tagging attacks.

Why C is incorrect: A trunk port carries traffic for all allowed VLANs, not just the native VLAN. The native VLAN is simply the VLAN whose frames are sent untagged on the trunk.

Why D is incorrect: The warning is about the native VLAN configuration, not the allowed VLAN list. Allowed VLAN issues produce different messages. The fix is matching the native VLAN ID on both ends.

---

### Question 3

An attacker connects to a switch access port and configures their laptop's NIC to send DTP negotiation frames. The port negotiates into trunk mode and the attacker begins receiving traffic from all VLANs. Which attack is this, and what configuration prevents it?

A) MAC flooding attack — prevented by enabling Port Security with a maximum of one MAC address per port

B) DHCP starvation attack — prevented by enabling DHCP Snooping on all access ports

C) Switch spoofing VLAN hopping attack — prevented by disabling DTP and setting all access ports to static access mode

D) ARP poisoning attack — prevented by enabling Dynamic ARP Inspection on all access VLANs

Correct Answer: C) Switch spoofing VLAN hopping attack — prevented by disabling DTP and setting all access ports to static access mode

Distractor Analysis:

Why A is incorrect: MAC flooding fills the MAC address table to force flooding behavior. It is unrelated to DTP negotiation or trunk formation.

Why B is incorrect: DHCP starvation sends many DHCP Discover packets to exhaust a DHCP scope. It does not involve trunking or VLAN access.

Why D is incorrect: ARP poisoning sends gratuitous ARP replies to associate the attacker's MAC with a legitimate IP. It does not involve DTP or trunk negotiation.

---

### Question 4

A network administrator runs show spanning-tree vlan 10 and sees that the switch has a Bridge Priority of 32778 and no Root Bridge indicator is shown. A different switch on the network shows "This bridge is the root" with Bridge Priority 24576. Which switch is the Root Bridge and why?

A) The local switch is the Root Bridge because 32778 is higher than 24576, and STP always elects the switch with the highest priority

B) The remote switch is the Root Bridge because 24576 is lower than 32778, and STP elects the switch with the lowest Bridge ID

C) The switch with the lowest MAC address is always the Root Bridge regardless of priority

D) Neither switch is the Root Bridge because the priority values must be equal before STP elects a Root Bridge

Correct Answer: B) The remote switch is the Root Bridge because 24576 is lower than 32778, and STP elects the switch with the lowest Bridge ID

Distractor Analysis:

Why A is incorrect: STP elects the switch with the lowest Bridge ID as Root Bridge — not the highest. A lower priority value wins the election. This is consistent with how lower administrative distance is preferred in routing.

Why C is incorrect: MAC address is the tiebreaker only when priorities are equal. When priorities differ, priority is the determining factor. Setting a lower priority is how administrators control Root Bridge placement.

Why D is incorrect: STP does not require equal priorities before electing a Root Bridge. In fact, equal priorities (all 32768 default) means the MAC address tiebreaker decides — which is why administrators manually set the priority on the intended Root Bridge.

---

### Question 5

A switch port connected to a PC is configured with PortFast. The next morning, a user plugged an unmanaged 5-port hub into that port and connected three PCs to the hub. After one hour, the port is in err-disabled state. What feature caused this, and why?

A) Port Security — the port detected more than one MAC address (three PCs through the hub) and disabled due to a security violation

B) BPDU Guard — the unmanaged hub generated a broadcast storm that triggered BPDU Guard

C) BPDU Guard — a BPDU was received on the PortFast port from the hub, which should never happen on an access port connected to an end device

D) Root Guard — the hub's MAC address matched the Root Bridge address, triggering a topology protection mechanism

Correct Answer: A) Port Security — the port detected more than one MAC address (three PCs through the hub) and disabled due to a security violation

Distractor Analysis:

Why B is incorrect: BPDU Guard responds specifically to receiving BPDU packets, not broadcast storms. An unmanaged hub does not generate BPDUs — it simply floods all traffic to all ports.

Why C is incorrect: An unmanaged hub does not participate in STP and does not generate BPDUs. BPDU Guard triggers only when STP BPDU frames are received. A managed switch connected to a PortFast port would trigger BPDU Guard.

Why D is incorrect: Root Guard prevents a port from becoming a Root Port if a superior BPDU is received. It is not triggered by MAC address matching.

Note: In this scenario with an unmanaged hub, Port Security (if configured with maximum 1 MAC) would trigger. If the maximum were higher, the hub itself would not trigger Port Security. The exam question targets recognizing which Layer 2 security feature applies to which scenario.

---

### Question 6

An administrator configures EtherChannel between two switches using channel-group 1 mode passive on both sides. The channel does not form. What is the reason?

A) LACP Passive mode does not support trunk encapsulation and requires access mode ports

B) Both sides are set to Passive mode — LACP requires at least one side to be in Active mode to initiate negotiation

C) Passive mode is only valid for PAgP — LACP requires Active or Desirable mode

D) Channel-group 1 is already in use on both switches and a different group number must be used

Correct Answer: B) Both sides are set to Passive mode — LACP requires at least one side to be in Active mode to initiate negotiation

Distractor Analysis:

Why A is incorrect: LACP Passive mode works with trunk ports. Trunk encapsulation is independent of LACP negotiation.

Why C is incorrect: Passive is an LACP mode (not PAgP). PAgP uses Desirable and Auto modes. Passive is the correct LACP terminology — but both sides being Passive means neither side sends LACP frames to initiate the channel.

Why D is incorrect: Each switch uses its own channel-group numbering. Both switches can use group number 1 independently — the numbers do not need to match between switches.

---

### Question 7

A network engineer runs show etherchannel summary and sees this output for a Port-Channel:

```text
Po1(SU)    LACP    Fa0/1(P)    Fa0/2(P)    Fa0/3(D)    Fa0/4(P)
```

What does the (D) flag on Fa0/3 indicate, and what is the impact on the EtherChannel?

A) Fa0/3 is in Discarding state — it will not carry traffic until STP converges

B) Fa0/3 is down (link failure) — the EtherChannel continues operating with three active members instead of four

C) Fa0/3 is in Desirable mode — it is negotiating using PAgP while the other ports use LACP

D) Fa0/3 is a duplicate port and has been removed from the bundle to prevent a loop

Correct Answer: B) Fa0/3 is down (link failure) — the EtherChannel continues operating with three active members instead of four

Distractor Analysis:

Why A is incorrect: STP Discarding state is an RSTP concept and is not shown in EtherChannel summary output. The EtherChannel summary flag (D) specifically means the physical port link is down.

Why C is incorrect: Desirable is a PAgP mode keyword, not an EtherChannel summary flag letter. All ports in the same EtherChannel must use the same negotiation protocol — mixing LACP and PAgP in one bundle is not possible.

Why D is incorrect: EtherChannel does not remove duplicate ports based on MAC matching. A port showing (D) has lost its physical link — a cable or transceiver failure, not a protocol decision.

---

### Question 8

An attacker on VLAN 10 sends a frame with two 802.1Q tags. The outer tag is VLAN 1 (the native VLAN of the uplink trunk). The inner tag is VLAN 50 (the victim VLAN). What happens when Switch A receives this frame on the trunk, and why does this constitute a security vulnerability?

A) Switch A drops the frame because double-tagged frames are rejected by 802.1Q as malformed

B) Switch A strips the outer VLAN 1 tag (native VLAN, sent untagged) and forwards the frame — Switch B receives the frame tagged with VLAN 50 and delivers it to devices in VLAN 50 without routing

C) Switch A recognizes the double tag and generates an SNMP alert but forwards the frame normally

D) Switch A forwards the frame to the router for inter-VLAN routing since the destination VLAN differs from the source VLAN

Correct Answer: B) Switch A strips the outer VLAN 1 tag (native VLAN, sent untagged) and forwards the frame — Switch B receives the frame tagged with VLAN 50 and delivers it to devices in VLAN 50 without routing

Distractor Analysis:

Why A is incorrect: 802.1Q does not have a mechanism to detect or drop double-tagged frames. The first switch simply processes the outermost tag and forwards based on it, stripping that tag. This is how the attack exploits normal switch behavior.

Why C is incorrect: Standard 802.1Q switches do not inspect frame contents for embedded tags or generate alerts based on double-tagging. This detection requires specialized security tools.

Why D is incorrect: The frame never reaches a router. The attack bypasses Layer 3 routing entirely — that is precisely what makes it a vulnerability. Traffic crosses VLAN boundaries at Layer 2 using the switch's own tag-stripping behavior.

---

### Question 9

A network administrator needs to ensure that a specific workstation always receives the OSPF routing advertisements from the correct switch. The administrator wants to prevent any switch on the network from accidentally becoming Root Bridge due to a misconfigured or malicious low-priority BPDU. Which STP feature should be applied to the uplink ports on access layer switches facing the distribution layer?

A) PortFast — immediately moves ports to Forwarding state so legitimate BPDUs are processed faster

B) BPDU Guard — disables any port that receives a BPDU to prevent unauthorized STP participation

C) Root Guard — prevents ports from becoming Root Ports if a superior BPDU is received, protecting the intended Root Bridge placement

D) BPDU Filter — prevents all BPDUs from being sent or received, ensuring the access switch cannot affect the Root Bridge election

Correct Answer: C) Root Guard — prevents ports from becoming Root Ports if a superior BPDU is received, protecting the intended Root Bridge placement

Distractor Analysis:

Why A is incorrect: PortFast bypasses STP convergence timers for access ports connected to end devices. It does not protect against Root Bridge manipulation on uplink ports. PortFast should never be enabled on switch-to-switch uplinks.

Why B is incorrect: BPDU Guard is appropriate for access ports connected to end devices (in combination with PortFast). On a switch uplink port, BPDU Guard would disable the port the moment any legitimate STP BPDU arrived, breaking connectivity to the distribution layer.

Why D is incorrect: BPDU Filter suppresses BPDUs entirely on a port. This disables STP loop detection on that port — a dangerous configuration on an uplink. If a loop forms, the port would not participate in correcting it.

---

### Question 10

A company has two distribution switches connected to each other and to 10 access layer switches. The STP topology is stable. A new server is connected to an access port on one of the distribution switches. The port is configured with PortFast and immediately becomes active. The server begins sending frames. Which statement correctly describes the behavior of the access port after PortFast is applied?

A) The port bypasses the Blocking and Listening states, skips the Learning state, and immediately enters Forwarding — the server can send and receive traffic within seconds of connecting

B) The port bypasses the Blocking state only, still transitions through Listening (15 sec) and Learning (15 sec) before entering Forwarding — total delay is 30 seconds instead of 50

C) The port immediately enters Forwarding state, skipping all STP states including Learning — the switch's MAC address table cannot be populated for this port

D) The port enters Forwarding immediately and ignores all future BPDUs — even if a switch is plugged in later, STP reconvergence will not occur on this port

Correct Answer: A) The port bypasses the Blocking and Listening states, skips the Learning state, and immediately enters Forwarding — the server can send and receive traffic within seconds of connecting

Distractor Analysis:

Why B is incorrect: PortFast bypasses Listening AND Learning states, not just Blocking. A 30-second delay still represents only skipping Blocking (Max Age), not the full PortFast behavior. With PortFast, the port enters Forwarding immediately.

Why C is incorrect: PortFast allows the port to enter Forwarding immediately, but the switch still populates its MAC address table normally as frames arrive on the port. Learning is a state, not a permanent capability — bypassing the Learning state does not disable MAC learning.

Why D is incorrect: PortFast does not permanently ignore BPDUs. PortFast simply skips the initial convergence delay. If BPDU Guard is not configured and a switch is plugged in, the port will process BPDUs and may reconverge normally. BPDU Guard (if configured) would err-disable the port when the BPDU is received.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
