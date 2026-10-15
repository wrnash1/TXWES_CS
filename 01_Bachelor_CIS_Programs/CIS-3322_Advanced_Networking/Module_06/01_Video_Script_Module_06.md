# Video Script: Module 06 - EtherChannel Link Aggregation

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course &bull; Module 06</strong>
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
**Estimated Duration:** 21 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1: Introduction - The Problem EtherChannel Solves
Welcome to Module 06. I am Professor Nash. Today we cover EtherChannel — Cisco's link aggregation technology that combines multiple physical Ethernet links into one logical channel.

Here is the problem. Between two switches, you might have redundant cables for reliability. But STP blocks all but one of those links. You are paying for redundancy but getting no bandwidth benefit from it. EtherChannel solves this by bundling those redundant links into a single logical port-channel that STP sees as one interface. STP does not block anything because there is only one logical link.

Today's topics:

- What EtherChannel is and how STP interacts with it
- LACP versus PAgP negotiation protocols and mode combinations
- Static (on/on) EtherChannel configuration
- Port-channel interface configuration
- Load-balancing algorithms
- Cisco IOS configuration and verification commands

---

## Section 2: LACP and PAgP Protocol Comparison
EtherChannel can be formed using three methods: LACP (dynamic, open standard), PAgP (dynamic, Cisco-proprietary), or static (no protocol, manual).

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

## Section 3: EtherChannel Configuration

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

## Section 4: EtherChannel Requirements and Load Balancing
### EtherChannel Member Port Requirements

All member ports in an EtherChannel must have matching configurations. A mismatch causes the channel to fail or ports to be suspended.

Matching requirements:

- Speed and duplex (all must be the same)
- VLAN membership or trunk settings (access VLAN or allowed VLAN list must match)
- STP settings (port cost, port priority)
- Native VLAN (on trunk EtherChannels)

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

## Section 5: Verification and Lab Preview
```ios
SW1# show etherchannel summary
SW1# show etherchannel 1 detail
SW1# show interfaces port-channel 1
SW1# show etherchannel load-balance
```

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
