# Reading Guide: Module 06 - EtherChannel Link Aggregation

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

EtherChannel is tested on the CCNA 200-301 primarily through configuration scenario questions and show-command interpretation. The exam frequently presents an EtherChannel that has failed to form and asks you to identify the cause. This guide covers the protocol options, mode negotiation matrix, configuration requirements, and all verification commands you need.

---

## 1. High-Yield Glossary

- **EtherChannel:** Cisco's link aggregation technology that bundles two to eight physical Ethernet links into one logical port-channel interface. STP sees the bundle as a single link, preventing blocking of member ports.

- **Port-channel interface:** The logical interface that represents an EtherChannel bundle. Configuration (VLANs, trunking, IP address) applied to the port-channel automatically applies to all member physical ports.

- **LACP (Link Aggregation Control Protocol):** IEEE 802.3ad (802.1AX) open standard for dynamic EtherChannel negotiation. Works between any vendor's equipment. Modes: active and passive.

- **PAgP (Port Aggregation Protocol):** Cisco-proprietary EtherChannel negotiation protocol. Works only between Cisco switches. Modes: desirable and auto.

- **Active mode (LACP):** The port actively sends LACP negotiation frames and attempts to form a bundle with the neighbor.

- **Passive mode (LACP):** The port waits for LACP frames from the neighbor. Forms a bundle only if the neighbor is in active mode.

- **Desirable mode (PAgP):** Actively sends PAgP frames and attempts to form a bundle. Equivalent to LACP active.

- **Auto mode (PAgP):** Waits for PAgP frames from the neighbor. Forms a bundle only if the neighbor is in desirable mode. Equivalent to LACP passive.

- **On mode (static):** Forces the ports into a bundle without any negotiation protocol. Both sides must be set to on. No mismatch detection — misconfigurations may not be detected automatically.

- **Load-balance method:** The hashing algorithm EtherChannel uses to distribute traffic across member links. Based on source MAC, destination MAC, source-destination MAC, source IP, destination IP, or source-destination IP.

- **Suspended port (s):** A member port that has been suspended from the EtherChannel bundle due to a configuration mismatch with other member ports. Visible as lowercase s in `show etherchannel summary` output.

- **channel-group:** The IOS command used on physical interfaces to add them to an EtherChannel bundle. Syntax: `channel-group [number] mode [mode]`.

---

## 2. EtherChannel Negotiation Mode Matrix

| SW1 Mode | SW2 Mode | Protocol | Result |
|---|---|---|---|
| active | active | LACP | Forms EtherChannel |
| active | passive | LACP | Forms EtherChannel |
| passive | passive | LACP | Does NOT form (both passive) |
| desirable | desirable | PAgP | Forms EtherChannel |
| desirable | auto | PAgP | Forms EtherChannel |
| auto | auto | PAgP | Does NOT form (both auto) |
| on | on | None (static) | Forms EtherChannel |
| on | active | Mixed | Does NOT form |
| on | passive | Mixed | Does NOT form |
| active | desirable | Mixed (incompatible) | Does NOT form |

Key exam combinations to memorize: passive + passive fails, auto + auto fails, on + on always works.

---

## 3. EtherChannel Member Port Requirements

All physical ports in an EtherChannel bundle must have identical configurations. Mismatches cause individual ports to be suspended (s flag in `show etherchannel summary`).

| Parameter | Requirement |
|---|---|
| Speed | All member ports must operate at the same speed |
| Duplex | All member ports must be full-duplex |
| Mode | All member ports must be either all access or all trunk |
| Access VLAN | If access mode, all ports must be in the same VLAN |
| Trunk allowed VLANs | If trunk mode, allowed VLAN lists must match |
| Native VLAN | If trunk mode, native VLANs must match |
| STP port cost | Should match; mismatches can cause unexpected STP behavior |

---

## 4. Cisco IOS EtherChannel Command Reference

| Task | Command | Mode |
|---|---|---|
| Add physical ports to channel group | `channel-group 1 mode active` | Interface config |
| Configure range of interfaces | `interface range Gi0/0 - 1` | Global config |
| Set load-balance method | `port-channel load-balance src-dst-ip` | Global config |
| Configure port-channel as trunk | `switchport mode trunk` (on port-channel) | Interface config |
| Set allowed VLANs on port-channel | `switchport trunk allowed vlan 10,20` | Interface config |
| View EtherChannel summary | `show etherchannel summary` | Privileged EXEC |
| View detailed channel information | `show etherchannel 1 detail` | Privileged EXEC |
| View port-channel interface status | `show interfaces port-channel 1` | Privileged EXEC |
| View load-balance method | `show etherchannel load-balance` | Privileged EXEC |
| View LACP neighbor info | `show lacp neighbor` | Privileged EXEC |
| View PAgP neighbor info | `show pagp neighbor` | Privileged EXEC |

---

## 5. Interpreting show etherchannel summary Output

Sample output:

```text
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG

Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP      Gi0/0(P)    Gi0/1(P)
```

Key flag interpretations:

- `SU` on port-channel: S = Layer 2, U = in use (active and passing traffic)
- `P` on member ports: bundled in port-channel (operating normally)
- `s` on a member port: suspended due to configuration mismatch
- `I` on a member port: standalone — not bundled (EtherChannel not formed)
- `D` on port-channel: down (no active members)

---

## 6. EtherChannel Benefits and Limitations

Benefits:

- Bandwidth aggregation: 2 x 1G links provide 2 Gbps total throughput across multiple flows
- Redundancy: if one physical member link fails, traffic continues on remaining links without STP reconvergence
- STP sees one logical link: no port blocking, full use of all member physical links
- Single management interface: configure once on port-channel, applies to all members

Limitations:

- Maximum 8 active links per EtherChannel on Cisco Catalyst switches (16 standby with LACP)
- All member links must be same speed and connect to same neighboring device
- Individual flows are not split: a single TCP connection uses only one physical link
- Misconfigurations are not always visually obvious without running show commands

---

## 7. CCNA Exam Tips

1. Two passive LACP ports will NOT form a channel. Two auto PAgP ports will NOT form a channel. The exam always tests at least one of these failure combinations.

2. EtherChannel configuration belongs on the port-channel interface, not on individual physical member ports. Applying trunk or VLAN settings directly to physical member ports (instead of port-channel) is a common misconfiguration.

3. A suspended `s` flag on a member port in `show etherchannel summary` means a configuration mismatch. Compare the member port's settings to those on the port-channel interface and other member ports.

4. Static EtherChannel (mode on + on) does not use any negotiation protocol. There is no automatic detection of misconfiguration. If the other side is not `on`, the channel may appear up locally but pass no traffic.

5. Load balancing distributes traffic per-flow, not per-packet. Each flow (identified by its src/dst IP or MAC pair) always uses the same physical link. A single file transfer will not exceed one link's speed.

6. EtherChannel and STP work together. STP treats the port-channel as a single logical interface. If STP needs to block a link between two switches, it blocks the entire port-channel, not just one physical member.

7. The `show etherchannel summary` flag SU on the port-channel means Layer 2 in-use. RU means Layer 3 in-use (when the port-channel has an IP address instead of being a Layer 2 trunk).

8. PAgP and LACP modes cannot be mixed on the same channel group. If one side uses LACP active and the other uses PAgP desirable, the channel will not form.

---

## 8. Study Checklist

Work through each item before taking the quiz.

- [ ] Complete the negotiation mode matrix from memory and check it against the reference table
- [ ] Write the full configuration to create a two-port LACP EtherChannel trunk between two switches (all commands including port-channel configuration)
- [ ] Interpret a sample `show etherchannel summary` output and identify which ports are bundled, suspended, and down
- [ ] Explain why two passive LACP ports do not form a channel
- [ ] Describe EtherChannel load balancing and explain why a single file download cannot exceed one link's bandwidth
- [ ] List five parameters that must match on all EtherChannel member ports
- [ ] Complete the Module 06 Packet Tracer lab activity
- [ ] Post your Module 06 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 9. Supplemental Resources

The following open educational resources extend EtherChannel and link aggregation concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Switching, Routing, and Wireless Essentials, Chapter 6 (EtherChannel)** (skillsforall.com): This free chapter covers LACP, PAgP, static EtherChannel, and load balancing with Packet Tracer activities for configuring and verifying port-channel bundles.

2. **Jeremy's IT Lab — EtherChannel (Day 23)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): A focused video lesson covering PAgP vs. LACP negotiation modes, static EtherChannel, the `show etherchannel summary` flag interpretation, and common EtherChannel misconfiguration troubleshooting.

3. **Cisco Learning Network — EtherChannel and LACP Study Resources** (learningnetwork.cisco.com): Community discussions on EtherChannel configuration issues, mode compatibility matrices, and exam-focused questions on PAgP vs. LACP selection for mixed-vendor environments.

4. **Cisco IOS Configuration Guide — EtherChannel** (cisco.com): Cisco's official IOS configuration guide for EtherChannel covers all supported load balancing methods, LACP system priority, port priority, and hot-standby port behavior with CLI examples.

5. **GNS3 Labs — EtherChannel with LACP** (gns3.com/marketplace/featured): GNS3 community lab files for EtherChannel with LACP on Cisco IOS virtual routers and switches, allowing testing of multi-link aggregation without physical hardware.
