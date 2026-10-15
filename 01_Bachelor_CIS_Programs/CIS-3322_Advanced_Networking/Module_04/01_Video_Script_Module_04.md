# Video Script: Module 04 - Switching Concepts & VLANs

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course &bull; Module 04</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ" title="Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1: Introduction - Why VLANs Matter
Welcome to Module 04. I am Professor Nash. Today we cover VLANs and switching concepts — topics that account for a significant portion of the CCNA 200-301 Network Access domain.

Without VLANs, every device on a switch shares the same broadcast domain. A 200-port switch with no VLANs means that every broadcast — ARP requests, DHCP discovery, STP BPDUs — reaches all 200 devices simultaneously. That creates performance problems and security risks. VLANs solve both.

Today's topics:

- How switches build and use MAC address tables
- VLAN concepts and port types (access and trunk)
- 802.1Q frame tagging
- Native VLAN configuration and security
- DTP (Dynamic Trunking Protocol) and when to disable it
- Full Cisco IOS VLAN and trunk configuration walkthrough

---

## Section 2: Layer 2 Switching Fundamentals
Before we configure VLANs, let us briefly review how switches forward frames at Layer 2.

When a frame arrives on a switch port, the switch reads the source MAC address and records it in the MAC address table along with the incoming port number. This is called MAC address learning. When a frame arrives with a destination MAC that is already in the table, the switch forwards it only to the correct port — this is unicast forwarding. When the destination MAC is unknown, the switch floods the frame out all ports except the source port — this is unknown unicast flooding.

Key MAC address table behaviors:

- Entries age out after 300 seconds by default (configurable)
- Broadcast frames (destination FF:FF:FF:FF:FF:FF) are always flooded within the VLAN
- Multicast frames are flooded unless IGMP snooping is enabled

CCNA Exam Tip: A switch that receives a frame with a destination MAC that is not in its MAC address table will flood the frame. This is not a failure — it is expected behavior for unknown unicast destinations.

---

## Section 3: VLANs and Port Types
A VLAN is a logical broadcast domain created within a switch. Devices in the same VLAN communicate at Layer 2 as if they are on the same physical segment, regardless of which physical ports or switches they connect to. Devices in different VLANs cannot communicate without a Layer 3 device (a router or multilayer switch) routing between them.

### Access Ports

An access port belongs to exactly one VLAN. When a PC connects to a switch access port, the PC sends untagged Ethernet frames. The switch internally associates those frames with the assigned VLAN. When the switch forwards the frame to a trunk port, it adds an 802.1Q tag identifying the VLAN.

Configure an access port:

```ios
SW1(config)# interface FastEthernet0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
```

### Trunk Ports

A trunk port carries traffic for multiple VLANs simultaneously. Trunk ports are used on uplinks between switches and between switches and routers (for Router-on-a-Stick inter-VLAN routing). Each frame on a trunk has an 802.1Q tag identifying its VLAN.

Configure a trunk port:

```ios
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20,30
```

CCNA Exam Tip: Access ports strip the 802.1Q tag before delivering frames to end devices. End devices (PCs, printers) never see the VLAN tag. Only switches and routers handle tagged frames on trunk links.

---

## Section 4: Native VLAN and DTP
### Native VLAN

The native VLAN is the one VLAN on an 802.1Q trunk that sends frames without a tag. By default, the native VLAN is VLAN 1 on Cisco switches. Both ends of a trunk must agree on the native VLAN — a mismatch generates a CDP warning:

```text
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1
```

The security concern: if the native VLAN on a trunk is also the access VLAN of a connected end device, an attacker can craft double-tagged frames to "hop" from one VLAN to another. Best practice is to change the native VLAN to an unused VLAN number (such as VLAN 999) that no end devices belong to.

```ios
SW1(config-if)# switchport trunk native vlan 999
```

### DTP - Dynamic Trunking Protocol

DTP is Cisco-proprietary and allows two switches to automatically negotiate whether to form a trunk. The four DTP modes are:

- `switchport mode trunk` — always a trunk; sends DTP frames
- `switchport mode access` — never a trunk; sends DTP frames
- `switchport mode dynamic desirable` — actively tries to form a trunk
- `switchport mode dynamic auto` — forms a trunk only if the other side actively requests it

Two ports set to `dynamic auto` will NOT form a trunk — both sides are passive. This is a common CCNA exam trap.

Security best practice: disable DTP on all user-facing ports and any port that should not form a trunk:

```ios
SW1(config-if)# switchport mode access
SW1(config-if)# switchport nonegotiate
```

CCNA Exam Tip: On user-facing access ports, always use `switchport mode access` plus `switchport nonegotiate`. This hard-codes the port as an access port and disables DTP, preventing a rogue switch from establishing an unauthorized trunk.

---

## Section 5: Verification Commands and Lab Preview
These commands verify your VLAN and trunk configuration:

```ios
SW1# show vlan brief
SW1# show interfaces trunk
SW1# show interfaces FastEthernet0/1 switchport
SW1# show mac address-table
```

`show vlan brief` shows all VLANs and their assigned ports but does not show trunk ports — trunk ports do not appear in VLAN assignments because they carry multiple VLANs.

`show interfaces trunk` shows only trunk ports, their 802.1Q encapsulation status, native VLAN, and the VLANs allowed and active on each trunk.

This week's Packet Tracer lab walks you through creating VLANs, assigning access ports, configuring trunks, and verifying the full configuration on a two-switch topology. You will also interpret `show vlan brief` output to identify misconfigured ports.

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 04 Complete
Next: Module 05 - Spanning Tree Protocol (STP and RSTP)
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
