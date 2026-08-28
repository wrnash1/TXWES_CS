# Reading Guide: Module 09 — Access Control Lists (ACLs)

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3322 &BULL; ADVANCED NETWORKING & INFRASTRUCTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Overview

Access Control Lists are the primary traffic filtering mechanism on Cisco IOS routers and Layer 3 switches. They enforce security policy by permitting or denying packets based on header fields. The CCNA 200-301 exam tests ACL concepts across multiple domains including IP Services and Security Fundamentals. This guide covers all testable ACL topics: standard and extended syntax, wildcard masks, interface placement, IPv6 ACLs, and troubleshooting.

---

## 1. ACL Processing Rules

### Top-Down Processing

The router evaluates each ACL statement sequentially from the first entry to the last. The moment a packet matches any statement, the router takes the permit or deny action and stops processing the ACL. No additional statements are evaluated.

### Implicit Deny Any

Every ACL ends with an invisible `deny any` (IPv4) or `deny ipv6 any any` (IPv6) statement. This statement does not appear in the running configuration but is always enforced. Any packet that does not match an explicit statement is dropped.

### One ACL Per Direction Per Interface

A router interface can have one inbound ACL and one outbound ACL. Attempting to apply a second ACL in the same direction on the same interface replaces the first.

---

## 2. Standard ACL Reference

### Number Ranges

| Range     | Type                          |
|-----------|-------------------------------|
| 1–99      | Standard IPv4 ACL             |
| 1300–1999 | Standard IPv4 ACL (expanded)  |

### Syntax

```text
access-list <number> {permit | deny} {host <ip> | <network> <wildcard> | any}
```

### Named Standard ACL Syntax

```text
ip access-list standard <name>
  [sequence] {permit | deny} {host <ip> | <network> <wildcard> | any}
```

### Placement Rule

Place standard ACLs **as close to the destination as possible** because they can only match on source IP. Placing them near the source would block the matched source from reaching all destinations, not just the intended target.

---

## 3. Extended ACL Reference

### Number Ranges

| Range     | Type                           |
|-----------|--------------------------------|
| 100–199   | Extended IPv4 ACL              |
| 2000–2699 | Extended IPv4 ACL (expanded)   |

### Syntax

```text
access-list <number> {permit | deny} <protocol>
  <src-network> <src-wildcard> <dst-network> <dst-wildcard>
  [eq | lt | gt | neq | range] <port>
```

### Common Protocol Keywords

| Keyword | Protocol                       |
|---------|-------------------------------|
| ip      | All IP traffic (any protocol) |
| tcp     | TCP only                      |
| udp     | UDP only                      |
| icmp    | ICMP only                     |
| ospf    | OSPF routing protocol         |

### Common Port Keywords and Numbers

| Keyword | Port Number | Protocol |
|---------|-------------|----------|
| ftp     | 21          | TCP      |
| ssh     | 22          | TCP      |
| telnet  | 23          | TCP      |
| smtp    | 25          | TCP      |
| dns     | 53          | TCP/UDP  |
| http    | 80          | TCP      |
| https   | 443         | TCP      |
| snmp    | 161         | UDP      |

### Placement Rule

Place extended ACLs **as close to the source as possible** to drop unwanted traffic early and conserve bandwidth.

---

## 4. Wildcard Mask Reference

### Bit Meaning

- 0 bit = router MUST match this bit in the packet address
- 1 bit = router IGNORES this bit in the packet address

### Common Wildcard Masks

| Network        | Prefix | Wildcard Mask   |
|----------------|--------|-----------------|
| Host match     | /32    | 0.0.0.0         |
| /30 network    | /30    | 0.0.0.3         |
| /29 network    | /29    | 0.0.0.7         |
| /28 network    | /28    | 0.0.0.15        |
| /27 network    | /27    | 0.0.0.31        |
| /26 network    | /26    | 0.0.0.63        |
| /25 network    | /25    | 0.0.0.127       |
| /24 network    | /24    | 0.0.0.255       |
| /23 network    | /23    | 0.0.1.255       |
| /22 network    | /22    | 0.0.3.255       |
| /16 network    | /16    | 0.0.255.255     |
| /8 network     | /8     | 0.255.255.255   |
| Any address    | any    | 255.255.255.255 |

### Calculation Method

To derive the wildcard from a subnet mask: subtract each octet of the subnet mask from 255.

Example: subnet mask 255.255.255.0 → wildcard = 255-255, 255-255, 255-255, 255-0 = 0.0.0.255

---

## 5. ACL Application Commands

### Standard Command Reference

| Task                              | Command                                              | Mode           |
|-----------------------------------|------------------------------------------------------|----------------|
| Create numbered standard ACL      | `access-list 10 permit 10.1.1.0 0.0.0.255`          | Global config  |
| Create numbered extended ACL      | `access-list 110 permit tcp any any eq 443`          | Global config  |
| Create named standard ACL         | `ip access-list standard NAME`                       | Global config  |
| Create named extended ACL         | `ip access-list extended NAME`                       | Global config  |
| Apply ACL to interface (inbound)  | `ip access-group 110 in`                             | Interface      |
| Apply ACL to interface (outbound) | `ip access-group 110 out`                            | Interface      |
| Apply ACL to VTY lines            | `access-class 10 in`                                 | Line VTY       |
| Remove ACL from interface         | `no ip access-group 110 in`                          | Interface      |
| Delete entire numbered ACL        | `no access-list 110`                                 | Global config  |
| Delete named ACL line             | `no 20` (inside named ACL config)                    | Named ACL      |
| View all ACLs with counters       | `show access-lists`                                  | Privileged EXEC|
| View ACL on interface             | `show ip interface GigabitEthernet0/0`               | Privileged EXEC|
| Clear hit counters                | `clear access-list counters 110`                     | Privileged EXEC|

---

## 6. IPv6 ACL Reference

### Key Differences from IPv4 ACLs

| Feature               | IPv4 ACL                  | IPv6 ACL                          |
|-----------------------|---------------------------|-----------------------------------|
| Numbered ACLs         | Supported                 | Not supported — named only        |
| Application command   | `ip access-group`         | `ipv6 traffic-filter`             |
| Implicit NDP permits  | None                      | Two implicit NDP permits          |
| Default deny          | `deny any`                | `deny ipv6 any any`               |

### Implicit IPv6 Permit Statements

All IPv6 ACLs include these two invisible permits before the implicit deny:

```text
permit icmp any any nd-na
permit icmp any any nd-ns
```

These allow Neighbor Discovery Protocol (NDP) to function. If you deny all ICMPv6, IPv6 neighbor resolution breaks and the network stops working.

### IPv6 ACL Configuration

```text
ipv6 access-list RESTRICT_V6
  deny tcp any any eq 23
  permit ipv6 any any

interface GigabitEthernet0/0
  ipv6 traffic-filter RESTRICT_V6 in
```

---

## 7. ACL Troubleshooting Flowchart

```text
SYMPTOM: Traffic blocked unexpectedly
         |
         v
Is an ACL applied to the interface?
  NO  --> Check show ip interface; ACL not applied — apply it
  YES --> Continue
         |
         v
Is the ACL applied in the correct direction (in vs out)?
  NO  --> Remove and reapply with correct direction keyword
  YES --> Continue
         |
         v
Run: show access-lists
Are hit counters incrementing on the deny line?
  YES --> That deny line is matching traffic it should not
       --> Check order: specific entries must be above general entries
  NO  --> Check if permit entry is above or below the deny entry
         |
         v
Is there a permit any / permit ip any any at the end?
  NO  --> Implicit deny is dropping all unmatched traffic — add permit
  YES --> Continue
         |
         v
Verify interface with: show ip interface Gi0/0
Confirm the correct ACL number or name is applied
         |
         v
Test connectivity — issue is resolved
```

---

## 8. Scenario Configuration Examples

### Standard ACL — Permit One Host, Deny a Subnet

```text
ip access-list standard PERMIT_HOST_ONLY
  10 permit host 10.1.1.5
  20 deny 10.1.1.0 0.0.0.255
  30 permit any
```

This permits only host 10.1.1.5 from the 10.1.1.0/24 network. All other hosts in that subnet are denied. All other traffic is permitted.

### Extended ACL — Restrict Inbound Traffic on WAN Interface

```text
ip access-list extended INBOUND_WAN
  10 permit tcp any 192.168.0.0 0.0.255.255 established
  20 permit icmp any any echo-reply
  30 deny ip any any log
```

This permits only TCP replies to sessions initiated by internal hosts, permits ICMP echo-reply (ping responses), and logs and drops everything else.

### VTY Line Restriction — Allow Only Management Subnet

```text
access-list 5 permit 10.0.0.0 0.0.0.255

line vty 0 4
  access-class 5 in
  transport input ssh
```

Only hosts in the 10.0.0.0/24 subnet can open SSH sessions to the router's VTY lines.

---

## 9. CCNA Exam Tips

**Tip 1 — Standard vs extended placement.** Standard ACL = close to destination. Extended ACL = close to source. This is the most tested ACL placement rule on the exam.

**Tip 2 — Implicit deny.** The implicit deny any is always present even though it does not appear in the running config. Any packet not explicitly permitted is dropped. Always add `permit ip any any` or `permit any` at the end of your ACL when you want unmatched traffic to pass.

**Tip 3 — access-class vs access-group.** VTY lines use `access-class`. Interfaces use `access-group`. The exam tests whether you know the difference. Mixing them up prevents the ACL from having any effect.

**Tip 4 — Named ACL line editing.** Named ACLs support inserting and deleting individual sequence-numbered lines. Numbered ACLs require the entire ACL to be deleted and recreated. In production and on scenario questions, named ACLs are preferred.

**Tip 5 — IPv6 ACL differences.** IPv6 ACLs are always named, use `ipv6 traffic-filter`, and have implicit NDP permit statements. Forgetting these NDP permits is a common troubleshooting scenario on the exam.

**Tip 6 — show access-lists counters.** Match counters are reset on router reload but can also be manually cleared with `clear access-list counters`. Use counters to confirm which lines are matching traffic during troubleshooting.

**Tip 7 — First match wins.** ACL processing is top-down, first match wins. Order matters critically. A `permit any` placed before a specific `deny` statement makes the deny unreachable. The router hits the permit first and never evaluates the deny.

**Tip 8 — One ACL per direction per interface.** You can apply one inbound ACL and one outbound ACL to the same interface but you cannot apply two ACLs in the same direction. The second application overwrites the first without warning.

---

## 10. Study Checklist

Work through each item before taking the Module 09 quiz.

- [ ] Write a numbered standard ACL from memory to permit a /24 network and deny a host
- [ ] Write a named extended ACL to permit HTTPS from one subnet to any destination and deny all Telnet
- [ ] Calculate wildcard masks for /24, /27, /28, and /30 networks from memory
- [ ] Explain the standard ACL placement rule and why it exists
- [ ] Explain the extended ACL placement rule and why it differs from standard
- [ ] Configure an IPv6 ACL and explain the implicit NDP permit statements
- [ ] Identify the difference between `access-group` and `access-class`
- [ ] Trace the ACL troubleshooting flowchart through a sample failure scenario
- [ ] Complete the Module 09 Packet Tracer lab
- [ ] Post your Module 09 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and practice questions: professormesser.com
- Cisco IOS ACL configuration guide: cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html

---

## 11. Supplemental Resources

The following open educational resources extend ACL concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Enterprise Networking, Security, and Automation, Chapter 4 (ACL Concepts)** (skillsforall.com): This free chapter covers standard and extended ACL configuration, wildcard mask calculation, ACL placement rules, and the named ACL line-editing workflow with interactive Packet Tracer activities.

2. **Jeremy's IT Lab — ACLs (Days 34–35)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): Two video lessons covering standard ACLs, extended ACLs, named ACL syntax, placement rules, VTY `access-class`, and IPv6 ACL differences. Jeremy's ACL series includes exam-style scenario walkthroughs and wildcard mask drills.

3. **Cisco Learning Network — ACL Study Group** (learningnetwork.cisco.com): Community discussion threads covering ACL placement traps, implicit deny behavior, wildcard mask edge cases, and CCNA exam scenario questions. The ACL troubleshooting threads are particularly useful for understanding common exam-style misconfigurations.

4. **Cisco IOS Security Configuration Guide — Access Control Lists** (cisco.com): Cisco's official security configuration guide covering extended ACL syntax for all protocol types, reflexive ACLs, time-based ACLs, and `show access-lists` counter interpretation with complete CLI examples.

5. **PacketLife.net — ACL Cheat Sheet** (packetlife.net/media/library/20/access_control_lists.pdf): A freely available one-page reference card covering standard and extended ACL syntax, wildcard mask quick calculations, ACL placement guidelines, and common protocol/port numbers tested on the CCNA exam.
