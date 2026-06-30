# Video Script: Module 05 – QoS, High Availability & Network Automation
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 1 of 2 | Estimated Duration: 15–18 minutes
## Week 5: November 16–22, 2026 | Due: Sunday, November 22, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 05 Part 1: Quality of Service (QoS) & High Availability | Texas Wesleyan University | Graduate Level"]

---

### Section 1: Quality of Service — The Business Case

[00:00 – 02:00]
[SHOW SLIDE: Network traffic types — voice, video, data — competing for bandwidth]

Welcome to Module 05. This module covers two topics that are central to real production networks: **Quality of Service (QoS)** and **High Availability (HA)**. Plus, we introduce the emerging discipline of **network automation** — the skill set that separates modern network engineers from traditional ones.

Without QoS, all traffic is treated equally — a 4K video stream competes for bandwidth with a VoIP call and a file download. The result: degraded voice quality, video buffering, and user frustration. QoS allows you to prioritize traffic types and guarantee minimum bandwidth to critical applications.

---

### Section 2: QoS — DiffServ Model (CCNP Level)

[02:00 – 08:00]
[SHOW DIAGRAM: DSCP marking through an enterprise — PC marks traffic → switch trusts marking → WAN applies QoS policy]

[Alt-text: A flow diagram showing: PC running VoIP app → Cisco IP Phone (marks traffic as DSCP EF) → Access Switch (trusts QoS marking from phone) → Distribution Switch (applies queuing policy) → WAN Router (shapes/polices toward ISP). DSCP values shown in each packet header icon.]

The **DiffServ (Differentiated Services)** model, defined in IETF RFC 2474, is the enterprise QoS standard. DiffServ uses a 6-bit field in the IP header called the **DSCP (Differentiated Services Code Point)** to mark each packet with a per-hop behavior (PHB).

**Why DiffServ instead of IntServ (RSVP)?**
IntServ reserves bandwidth per-flow using RSVP signaling. This doesn't scale beyond a few hundred flows. DiffServ marks packets and lets each router apply class-based policies — no per-flow state, scales to millions of packets. DiffServ is the enterprise and internet standard.

**Common DSCP Values:**

| DSCP Value | Name | Per-Hop Behavior | Use Case |
|---|---|---|---|
| 46 (101110) | EF | Expedited Forwarding | VoIP RTP (strict priority, low latency) |
| 34 (100010) | AF41 | Assured Forwarding | Interactive video (videoconferencing) |
| 26 (011010) | AF31 | Assured Forwarding | Critical data applications |
| 18 (010010) | AF21 | Assured Forwarding | Business data |
| 10 (001010) | AF11 | Assured Forwarding | Bulk data |
| 0 (000000) | BE/DF | Best Effort / Default | Standard internet traffic |
| 48 (110000) | CS6 | Class Selector 6 | Network control (OSPF, BGP) |

**The MQC — Modular QoS CLI:**
Cisco's QoS configuration uses a three-step framework called MQC (Modular QoS CLI):
1. **Class Map:** Define which traffic belongs to which class.
2. **Policy Map:** Define what to do with each class (mark, queue, police, shape).
3. **Service Policy:** Apply the policy to an interface.

```
! Step 1: Class Maps — identify traffic
class-map match-any VOICE-TRAFFIC
 match dscp ef

class-map match-any VIDEO-TRAFFIC
 match dscp af41

class-map match-any CRITICAL-DATA
 match dscp af31

! Step 2: Policy Map — define actions per class
policy-map WAN-QOS
 class VOICE-TRAFFIC
  priority percent 20      ! Strict priority (LLQ) — voice gets first-out always
  police rate percent 20   ! Police voice to 20% — never let it exceed its allocation
 class VIDEO-TRAFFIC
  bandwidth percent 30     ! Minimum bandwidth guaranteed
 class CRITICAL-DATA
  bandwidth percent 20
 class class-default
  fair-queue               ! CBWFQ for all remaining traffic

! Step 3: Apply outbound on the WAN interface
interface GigabitEthernet0/0
 service-policy output WAN-QOS
```

**Traffic Policing vs. Traffic Shaping:**
| Feature | Policing | Shaping |
|---|---|---|
| What it does | Drops or marks packets exceeding the rate | Buffers packets exceeding the rate and sends them later |
| Delay introduced | None | Yes (buffering adds delay) |
| Packet loss | Yes (drops excess) | Minimal (buffers instead of dropping) |
| Use case | Inbound at carrier demarcation (enforce SLA) | Outbound toward carrier (smooth bursty traffic) |
| Applied where | Typically inbound | Typically outbound |

---

### Section 3: DSCP Marking at the Access Layer

[08:00 – 11:00]
[SHOW DIAGRAM: IP phone marking EF, PC in same VLAN unmarked, switch trust policy]

One of the most common CCNP exam topics is **QoS trust boundaries**. The question: which device in the network should mark traffic, and which devices should trust or re-mark those markings?

**Trust Boundary Principle:**
- **Trust the phone, not the PC.** IP phones (Cisco 7900 series, etc.) mark voice RTP traffic as DSCP EF automatically. The switch should trust the phone's markings.
- **Do NOT trust the PC** on the same Ethernet port. A user could manually mark their BitTorrent traffic as DSCP EF to get priority treatment — the switch should re-mark untrusted PC traffic to DSCP 0 (best effort).

```
! On the access switch — trust QoS markings from the IP phone port
mls qos trust dscp
! Or for Cisco phones specifically:
mls qos trust cos

! Apply per-interface trust policy (Catalyst 2960-style):
interface FastEthernet0/1
 mls qos trust device cisco-phone
```

---

### Section 4: High Availability — HSRP, VRRP, and GLBP

[11:00 – 15:00]
[SHOW DIAGRAM: HSRP — Active router, Standby router, Virtual IP as gateway for hosts]

[Alt-text: Two distribution switches labeled "DS1 (Active — HSRP)" and "DS2 (Standby — HSRP)." Both switches have arrows pointing to a laptop labeled "End Device — Default Gateway: 10.10.10.254 (Virtual IP)." An arrow between DS1 and DS2 is labeled "HSRP Hello Messages." A dotted arrow shows "If DS1 fails → DS2 becomes Active."]

**FHRP — First Hop Redundancy Protocols:**
End devices need a default gateway. If that gateway fails, the device loses connectivity — even if there is a backup router. FHRPs solve this by presenting a single **virtual IP and MAC address** shared between two (or more) routers. If the active router fails, the standby takes over seamlessly.

**HSRP (Hot Standby Router Protocol):**
- Cisco proprietary (IOS).
- Two routers: **Active** (handles traffic) and **Standby** (monitors Active, takes over on failure).
- Preemption: the higher-priority router can take back the Active role when it comes back online.

```
! On DS1 (should be Active):
interface Vlan10
 ip address 10.10.10.1 255.255.255.0
 standby 1 ip 10.10.10.254          ! Virtual IP (gateway for hosts)
 standby 1 priority 110             ! Higher than default 100 → DS1 is Active
 standby 1 preempt                  ! DS1 takes back Active role if it recovers

! On DS2 (Standby):
interface Vlan10
 ip address 10.10.10.2 255.255.255.0
 standby 1 ip 10.10.10.254
 standby 1 priority 90              ! Lower → DS2 is Standby
 standby 1 preempt
```

**VRRP (Virtual Router Redundancy Protocol):**
- Open standard (IEEE, RFC 5798) — equivalent to HSRP but vendor-neutral.
- Configuration nearly identical to HSRP.
- Called "Master" and "Backup" instead of "Active" and "Standby."

**GLBP (Gateway Load Balancing Protocol):**
- Cisco proprietary.
- Unlike HSRP/VRRP, GLBP provides **actual load balancing** across multiple routers simultaneously.
- Multiple **Active Virtual Forwarders (AVFs)** each respond to ARP requests with a different virtual MAC address — different hosts use different gateways.

```
interface Vlan10
 standby version 2
 glbp 1 ip 10.10.10.254
 glbp 1 priority 150
 glbp 1 preempt
 glbp 1 load-balancing round-robin
```

**BFD — Bidirectional Forwarding Detection:**
HSRP/VRRP failover relies on hello timers (default: 3-second hello, 10-second dead timer). BFD provides sub-second link failure detection. BFD is configured separately and then associated with HSRP:
```
bfd interval 300 min_rx 300 multiplier 3   ! 300ms intervals, 3 missed = failure (900ms)
standby 1 bfd
```

---

### Section 5: Part 1 Summary

[15:00 – 16:00]
[SHOW SLIDE: Key terms recap]

In Part 1 you learned:
- **DiffServ QoS** using DSCP markings, MQC configuration, LLQ for voice, CBWFQ for data.
- **Policing vs. Shaping** — when to use each and the difference in packet handling.
- **QoS Trust Boundaries** — where to mark and where to trust.
- **HSRP, VRRP, GLBP** — FHRP design, configuration, preemption, and BFD for fast failover.

In Part 2 we cover **Network Automation** — Python for networking, Ansible playbooks, REST APIs, and NETCONF/YANG.

---
*End of Part 1 — Module 05*
