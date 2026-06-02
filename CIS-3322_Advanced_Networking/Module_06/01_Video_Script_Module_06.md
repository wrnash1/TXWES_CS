# Video Script: Module 06 - EtherChannel Link Aggregation

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Estimated Duration:** 21 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for all EtherChannel demonstrations
- Show `show etherchannel summary` output with flag legend highlighted
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: Introduction - The Problem EtherChannel Solves [00:00 - 03:00]

Welcome to Module 06. I am Professor Nash. Today we cover EtherChannel — Cisco's link aggregation technology that combines multiple physical Ethernet links into one logical channel.

Here is the problem. Between two switches, you might have redundant cables for reliability. But STP blocks all but one of those links. You are paying for redundancy but getting no bandwidth benefit from it. EtherChannel solves this by bundling those redundant links into a single logical port-channel that STP sees as one interface. STP does not block anything because there is only one logical link.

[SHOW DIAGRAM: Two switches with three physical cables between them. Left side shows STP blocking two of the three cables. Right side shows EtherChannel bundling all three into one logical port-channel, with bandwidth labeled as 3 Gbps combined]

Today's topics:

- What EtherChannel is and how STP interacts with it
- LACP versus PAgP negotiation protocols and mode combinations
- Static (on/on) EtherChannel configuration
- Port-channel interface configuration
- Load-balancing algorithms
- Cisco IOS configuration and verification commands

---

## Section 2: LACP and PAgP Protocol Comparison [03:00 - 08:00]

EtherChannel can be formed using three methods: LACP (dynamic, open standard), PAgP (dynamic, Cisco-proprietary), or static (no protocol, manual).

[SHOW DIAGRAM: Three-column comparison table: LACP, PAgP, and Static (On) with rows for Standard, Vendor, Modes, and Compatibility]

### LACP - Link Aggregation Control Protocol

LACP is the IEEE 802.3ad (now 802.1AX) standard. It works between any vendor's equipment. LACP uses two modes:

- Active: actively sends LACP frames and attempts to form a bundle
- Passive: waits for LACP frames from the other side; forms bundle only if other side is active

Mode combinations that form a channel: active + active, active + passive.
Mode combination that does NOT form a channel: passive + passive.

### PAgP - Port Aggregation Protocol

PAgP is Cisco-proprietary. It only works between Cisco switches. PAgP uses two modes:

- Desirable: actively sends PAgP frames and attempts to form a bundle
- Auto: waits for PAgP frames; forms bundle only if other side is desirable

Mode combinations that form a channel: desirable + desirable, desirable + auto.
Mode combination that does NOT form a channel: auto + auto.

### Static EtherChannel

Using mode `on` forces the ports into a bundle without any negotiation protocol. Both sides must be set to `on`. Static EtherChannel provides no negotiation and no mismatch detection — if the other side is not configured as `on`, the channel may enter a non-functioning state silently.

CCNA Exam Tip: The exam tests passive + passive (LACP) and auto + auto (PAgP) — both fail to form a channel because both sides wait passively. Memorize these failure combinations.

---

## Section 3: EtherChannel Configuration [08:00 - 13:30]

[SHOW DIAGRAM: Two switches (SW1 and SW2) with Gi0/0 and Gi0/1 bundled into Port-Channel 1 on each switch]

To configure EtherChannel using LACP on SW1:

```ios
SW1# configure terminal
SW1(config)# interface range GigabitEthernet0/0 - 1
SW1(config-if-range)# channel-group 1 mode active
SW1(config-if-range)# end
```

This automatically creates a Port-Channel 1 logical interface. Now configure the port-channel interface:

```ios
SW1(config)# interface port-channel 1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20,30
SW1(config-if)# end
```

Repeat on SW2 (use `mode active` or `mode passive` — one active + one passive works):

```ios
SW2(config)# interface range GigabitEthernet0/0 - 1
SW2(config-if-range)# channel-group 1 mode passive
SW2(config-if-range)# end
SW2(config)# interface port-channel 1
SW2(config-if)# switchport mode trunk
SW2(config-if)# switchport trunk allowed vlan 10,20,30
SW2(config-if)# end
```

CCNA Exam Tip: Always configure the trunk settings on the port-channel interface, not on the individual member physical interfaces. Settings on the port-channel interface propagate to all member ports automatically.

---

## Section 4: EtherChannel Requirements and Load Balancing [13:30 - 18:00]

### EtherChannel Member Port Requirements

All member ports in an EtherChannel must have matching configurations. A mismatch causes the channel to fail or ports to be suspended.

Matching requirements:

- Speed and duplex (all must be the same)
- VLAN membership or trunk settings (access VLAN or allowed VLAN list must match)
- STP settings (port cost, port priority)
- Native VLAN (on trunk EtherChannels)

[SHOW DIAGRAM: Two switches with three cables. One cable labeled with a speed mismatch (100 Mbps vs 1 Gbps). The show etherchannel summary output shows that mismatched port as "S" (suspended)]

### Load Balancing

EtherChannel distributes traffic across member links using a hash computed from frame header fields. The hash determines which physical link each flow uses.

Common load-balance methods:

- `src-mac` — hash based on source MAC address
- `dst-mac` — hash based on destination MAC address
- `src-dst-mac` — hash based on both source and destination MAC (default on most platforms)
- `src-ip` — hash based on source IP
- `dst-ip` — hash based on destination IP
- `src-dst-ip` — hash based on source and destination IP

Configure load balance:

```ios
SW1(config)# port-channel load-balance src-dst-ip
```

CCNA Exam Tip: EtherChannel does not split individual packet streams across links. Each flow always uses the same physical link determined by the hash. Bandwidth aggregation happens across multiple concurrent flows. A single large file transfer will not use more than one link's bandwidth.

---

## Section 5: Verification and Lab Preview [18:00 - 21:00]

```ios
SW1# show etherchannel summary
SW1# show etherchannel 1 detail
SW1# show interfaces port-channel 1
SW1# show etherchannel load-balance
```

[SHOW DIAGRAM: Terminal output of show etherchannel summary with flag legend at top showing D=down, S=layer2, U=in use, P=bundled, I=standalone, s=suspended]

The `show etherchannel summary` output shows:

- Channel group number and protocol (LACP, PAgP, or none/static)
- Port-channel status flags (SU = Layer 2 in use, D = down)
- Member port status flags (P = bundled in port-channel, s = suspended, I = individual)

If a port shows `s` (suspended), there is a configuration mismatch between that port and the other member ports.

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 06 Complete
Next: Module 07 - Inter-VLAN Routing Solutions
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
