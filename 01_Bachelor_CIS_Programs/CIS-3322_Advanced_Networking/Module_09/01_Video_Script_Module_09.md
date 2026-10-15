# Video Script: Module 09 — Access Control Lists (ACLs)

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Cisco CCNA 200-301

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course &bull; Module 09</strong>
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

---

## Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash, and in Module 09 we are covering one of the most operationally critical topics on the CCNA exam: Access Control Lists, or ACLs.

ACLs are the primary packet-filtering mechanism on Cisco IOS routers and Layer 3 switches. They allow you to permit or deny traffic based on source address, destination address, protocol, and port number. Every enterprise network uses ACLs to enforce security policy at the network layer.

By the end of this module you will be able to:

- Distinguish standard ACLs from extended ACLs

- Write and apply numbered and named ACLs

- Understand inbound versus outbound interface placement

- Use wildcard masks correctly

- Configure IPv6 ACLs

- Troubleshoot common ACL problems

[PAUSE — 3 seconds]

Let's start with the fundamentals.

---

## Section 1: ACL Processing Logic (1:30–4:00)

An ACL is an ordered list of statements. When a packet arrives at an interface where an ACL is applied, the router tests the packet against each statement from top to bottom. The first match wins. If the packet matches a permit statement, it is forwarded. If it matches a deny statement, it is dropped. If no statement matches, the packet is dropped by the implicit deny any at the end of every ACL.

That implicit deny is invisible — you will not see it in the running configuration — but it is always there.

Think of ACL processing like a bouncer checking a list. The bouncer reads from the top. The first rule that fits the guest either lets them in or turns them away. Once a decision is made, the bouncer stops reading. That last invisible rule is "turn away anyone not on the list.

[PAUSE — 3 seconds]

ACLs can be applied to:

- Routed interfaces (physical, subinterface, SVI)

- VTY lines for management access control

- Route redistribution filters

- NAT pool selection — covered in Module 10

---

## Section 2: Standard ACLs (4:00–7:30)

Standard ACLs filter traffic based solely on the **source IP address**. They use access list numbers 1–99 and 1300–1999 in the expanded range.

The syntax for a numbered standard ACL is:

```
Router(config)# access-list <1-99> {permit | deny} <source> <wildcard>
```

To permit host 192.168.1.10:

```
Router(config)# access-list 10 permit 192.168.1.10
```

To permit the entire 10.0.0.0/8 network:

```
Router(config)# access-list 10 permit 10.0.0.0 0.255.255.255
```

The `0.255.255.255` is the wildcard mask. A zero bit means "must match." A one bit means "ignore." We will cover wildcard masks in detail shortly.

**Critical placement rule for standard ACLs**: place them as close to the destination as possible. Because standard ACLs filter only on source address, placing them close to the source could block traffic from that source to ALL destinations, not just the one you intend.

[PAUSE — 3 seconds]

Named standard ACLs offer the same filtering capability but are far easier to manage:

```
Router(config)# ip access-list standard BLOCK_SALES
Router(config-std-nacl)# deny 192.168.10.0 0.0.0.255
Router(config-std-nacl)# permit any
```

Named ACLs allow you to delete individual lines using sequence numbers, which is a significant operational advantage over numbered ACLs.

---

## Section 3: Extended ACLs (7:30–11:00)

Extended ACLs filter on multiple fields simultaneously:

- Source IP address

- Destination IP address

- Protocol such as IP, TCP, UDP, or ICMP

- Source and destination port numbers

Extended ACLs use numbers 100–199 and 2000–2699.

The full syntax is:

```
Router(config)# access-list <100-199> {permit | deny} <protocol>
  <source> <src-wildcard> <destination> <dst-wildcard>
  [eq | lt | gt | neq | range] <port>
```

To permit HTTP traffic from 192.168.1.0/24 to any destination:

```
Router(config)# access-list 110 permit tcp 192.168.1.0 0.0.0.255 any eq 80
```

To deny Telnet from any source to the 10.0.0.0/8 network:

```
Router(config)# access-list 110 deny tcp any 10.0.0.0 0.255.255.255 eq 23
Router(config)# access-list 110 permit ip any any
```

**Critical placement rule for extended ACLs**: place them as close to the source as possible. This drops unwanted traffic early before it consumes bandwidth traversing the network toward its destination.

[PAUSE — 3 seconds]

Named extended ACLs follow the same pattern with added sequence number support:

```
Router(config)# ip access-list extended FILTER_WEB
Router(config-ext-nacl)# 10 permit tcp 192.168.1.0 0.0.0.255 any eq 443
Router(config-ext-nacl)# 20 deny tcp any any eq 23
Router(config-ext-nacl)# 30 permit ip any any
```

Sequence numbers 10, 20, 30 allow you to insert a new rule between existing ones by choosing a number that falls between them, without recreating the entire ACL.

---

## Section 4: Wildcard Masks (11:00–13:30)

Wildcard masks are the inverse of subnet masks in concept but they are used differently. Think of them as match masks:

- Bit value 0 means the router MUST match this bit in the address

- Bit value 1 means the router IGNORES this bit

Common wildcard mask examples:

| Subnet Mask     | Wildcard Mask   | Meaning              |
|-----------------|-----------------|----------------------|
| 255.255.255.255 | 0.0.0.0         | Match exact host     |
| 255.255.255.0   | 0.0.0.255       | Match /24 network    |
| 255.255.0.0     | 0.0.255.255     | Match /16 network    |
| 255.0.0.0       | 0.255.255.255   | Match /8 network     |
| 0.0.0.0         | 255.255.255.255 | Match any address    |

The keywords `host` and `any` are useful shortcuts:

- `host 10.1.1.5` is equivalent to `10.1.1.5 0.0.0.0`

- `any` is equivalent to `0.0.0.0 255.255.255.255`

You can also write non-contiguous wildcard masks to match specific bit patterns across octets. These are less common on the CCNA but you should understand the concept because the exam occasionally presents scenarios that test whether you can read an unusual mask correctly.

---

## Section 5: Applying ACLs to Interfaces (13:30–15:30)

After creating an ACL, you must apply it to an interface to activate it. The command is `ip access-group`:

```
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip access-group 110 in
```

The direction `in` means the ACL filters packets as they enter the interface. The direction `out` means the ACL filters packets as they exit the interface.

[SHOW TOPOLOGY: Router R1 with Gi0/0 connected to LAN and Gi0/1 connected to WAN]

Inbound processing means the packet arrives at Gi0/0 and the ACL runs before the routing table is consulted. If denied, the packet is dropped immediately without ever entering the routing process. This is more efficient.

Outbound processing means the packet hits the routing table first, gets forwarded toward Gi0/1, and then the ACL runs at the exit point. If denied, the packet has already consumed routing resources.

For VTY line access control the command changes to `access-class`:

```
Router(config)# line vty 0 4
Router(config-line)# access-class 10 in
```

Note: `access-class` is used for VTY lines, not `access-group`. This is a frequently tested distinction on the exam.

---

## Section 6: IPv6 ACLs (15:30–18:00)

IPv6 ACLs work differently from IPv4 ACLs in three important ways.

First, all IPv6 ACLs are named. There are no numbered IPv6 ACLs.

Second, IPv6 ACLs include two implicit permit statements before the implicit deny. These permit `icmp any any nd-na` and `icmp any any nd-ns`, which allow Neighbor Discovery Protocol to function. IPv6 neighbor resolution depends on ICMPv6 NDP, so these must remain permitted.

Third, IPv6 ACLs are applied with `ipv6 traffic-filter` instead of `ip access-group`.

Configuration example:

```
Router(config)# ipv6 access-list BLOCK_TELNET_V6
Router(config-ipv6-acl)# deny tcp any any eq 23
Router(config-ipv6-acl)# permit ipv6 any any

Router(config)# interface GigabitEthernet0/0
Router(config-if)# ipv6 traffic-filter BLOCK_TELNET_V6 in
```

If you write an IPv6 ACL that accidentally denies all ICMPv6, you will break IPv6 neighbor resolution. The network will appear to be down even though routing is configured correctly. Always remember the hidden NDP permit statements when troubleshooting IPv6 connectivity failures.

[PAUSE — 3 seconds]

---

## Section 7: ACL Troubleshooting (18:00–21:30)

The most important verification and troubleshooting commands for ACLs are:

```
Router# show access-lists
Router# show access-lists 110
Router# show ip interface GigabitEthernet0/0
Router# show running-config | section access-list
Router# debug ip packet detail
```

`show access-lists` displays every configured ACL along with match counters showing how many packets matched each line. A counter incrementing when you expect a permit confirms that traffic is matching the correct rule.

`show ip interface` shows which ACL is applied to each interface in each direction. Always verify this when troubleshooting to confirm the correct ACL is active in the correct direction.

The most common ACL mistakes in production and on the CCNA exam:

**Mistake 1: Wrong order.** Specific entries must come before general entries. A `deny host 10.1.1.1` entry must appear before `deny 10.1.1.0 0.0.0.255`.

**Mistake 2: Wrong direction.** Applying inbound when outbound is needed or vice versa produces confusing results.

**Mistake 3: Wrong interface.** The ACL is on the correct router but applied to the wrong interface entirely.

**Mistake 4: Missing permit any.** Forgetting to add a `permit any` or `permit ip any any` at the end means the implicit deny blocks all unmatched traffic.

**Mistake 5: Editing numbered ACLs.** You cannot insert a line into a numbered ACL without deleting and recreating it. Named ACLs solve this problem.

[PAUSE — 3 seconds]

To clear ACL hit counters without removing the ACL:

```
Router# clear access-list counters 110
```

---

## Conclusion (21:30–23:00)

Let's wrap up Module 09. Today you learned:

- Standard ACLs filter on source IP only and should be placed close to the destination

- Extended ACLs filter on source, destination, protocol, and port — place them close to the source

- Wildcard masks use zero bits to enforce matches and one bits to ignore bits

- Named ACLs support sequence-number-based line insertion and deletion

- IPv6 ACLs are always named, applied with `ipv6 traffic-filter`, and include implicit NDP permit statements

- Troubleshoot with `show access-lists` and `show ip interface`

For the CCNA exam, pay close attention to ACL placement rules, the implicit deny any, and the difference between `access-group` and `access-class`. These are consistently tested.

Your lab this module has you configure and verify both standard and extended ACLs in a multi-router topology. The reading guide includes a complete command reference table and a troubleshooting flowchart.

[PAUSE — 3 seconds]

I'll see you in Module 10 where we cover NAT and PAT. Take care.

---

*End of Module 09 Video Script*
