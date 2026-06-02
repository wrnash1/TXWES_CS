# Reading Guide: Module 10 - Access Control Lists

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 5: Security Fundamentals - 15%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

ACLs are tested on the CCNA 200-301 through configuration scenarios, placement questions, and `show access-lists` output interpretation. The exam frequently presents a topology and asks where an ACL should be applied or asks you to read ACL output and determine what traffic is permitted or denied. This guide covers all testable ACL concepts.

---

## 1. High-Yield Glossary

- **ACL (Access Control List):** An ordered list of permit and deny rules applied to a router interface. Each rule is called an ACE (Access Control Entry). The router processes packets against the list sequentially — the first matching entry determines the action.

- **Implicit deny:** The invisible `deny any any` entry at the end of every ACL. Any packet that does not match an explicit entry is dropped. An ACL with no permit statements blocks all traffic.

- **Standard ACL:** Filters traffic based on source IP address only. Numbered 1-99 and 1300-1999. Should be placed close to the destination.

- **Extended ACL:** Filters traffic based on source IP, destination IP, protocol (IP, TCP, UDP, ICMP), and port numbers. Numbered 100-199 and 2000-2699. Should be placed close to the source.

- **Named ACL:** An ACL identified by a descriptive name rather than a number. Supports individual entry deletion and resequencing using sequence numbers.

- **Wildcard mask:** A 32-bit mask used in ACL and OSPF statements. A 0 bit means the address bit must match; a 1 bit means any value is accepted.

- **host keyword:** ACL shorthand for wildcard 0.0.0.0 — matches exactly one IP address. Equivalent to `[address] 0.0.0.0`.

- **any keyword:** ACL shorthand for wildcard 255.255.255.255 — matches all IP addresses. Equivalent to `0.0.0.0 255.255.255.255`.

- **ACL direction:** An ACL is applied on an interface in one direction. `in` filters packets arriving on the interface before routing. `out` filters packets leaving the interface after routing.

- **Sequence number:** A number assigned to each ACE in a named ACL. Used to control ordering and to delete individual entries without deleting the entire ACL.

---

## 2. ACL Type and Placement Reference

| ACL Type | Matches | Number Range | Placement | Reason |
|---|---|---|---|---|
| Standard | Source IP only | 1-99, 1300-1999 | Close to destination | Cannot identify destination, so must be near destination to avoid over-blocking |
| Extended | Source IP, dest IP, protocol, port | 100-199, 2000-2699 | Close to source | Can precisely identify traffic, so stop it at the source before it wastes bandwidth |

---

## 3. ACL Syntax Reference

### Standard ACL

```ios
access-list 10 deny 192.168.20.0 0.0.0.255
access-list 10 permit any
```

### Extended ACL (deny specific port)

```ios
access-list 110 deny tcp 192.168.10.0 0.0.0.255 host 10.0.0.5 eq 23
access-list 110 permit ip any any
```

### Named Extended ACL

```ios
ip access-list extended BLOCK_TELNET
 10 deny tcp 192.168.10.0 0.0.0.255 any eq 23
 20 permit ip any any
```

### Apply ACL to Interface

```ios
interface GigabitEthernet0/0
 ip access-group 110 in
```

### Remove ACL from Interface

```ios
interface GigabitEthernet0/0
 no ip access-group 110 in
```

---

## 4. Extended ACL Protocol and Port Reference

| Protocol Keyword | Meaning |
|---|---|
| `ip` | Matches all IP traffic (use as final permit entry) |
| `tcp` | Matches only TCP segments |
| `udp` | Matches only UDP datagrams |
| `icmp` | Matches ICMP messages (ping, traceroute) |

| Port Keyword | Port Number | Protocol |
|---|---|---|
| `eq 80` | HTTP | TCP |
| `eq 443` | HTTPS | TCP |
| `eq 23` | Telnet | TCP |
| `eq 22` | SSH | TCP |
| `eq 53` | DNS | TCP/UDP |
| `eq 25` | SMTP | TCP |

---

## 5. IOS Command Reference

| Task | Command | Mode |
|---|---|---|
| Create numbered standard ACL | `access-list 10 permit/deny [src] [wildcard]` | Global config |
| Create numbered extended ACL | `access-list 110 permit/deny [proto] [src] [wild] [dst] [wild] [port]` | Global config |
| Create named ACL | `ip access-list standard/extended [name]` | Global config |
| Add ACE to named ACL | `[seq] permit/deny [criteria]` | Named ACL config |
| Delete ACE from named ACL | `no [sequence-number]` | Named ACL config |
| Apply ACL to interface | `ip access-group [name/num] in/out` | Interface config |
| Remove ACL from interface | `no ip access-group [name/num] in/out` | Interface config |
| View ACL entries and match counts | `show access-lists` | Privileged EXEC |
| View ACL applied to interface | `show ip interface [id]` | Privileged EXEC |
| Delete entire ACL | `no access-list [number]` | Global config |
| Reset ACL match counters | `clear access-list counters` | Privileged EXEC |

---

## 6. ACL Processing Rules

ACLs follow these rules when applied to an interface:

1. Packets are evaluated against ACEs from the top (lowest sequence number) to bottom
2. The first matching ACE determines the action (permit or deny) — no further entries are checked
3. If no ACE matches, the implicit deny any any drops the packet
4. Only one ACL can be applied per interface per direction (one inbound, one outbound)
5. An ACL is processed before routing (inbound) or after routing (outbound)

---

## 7. Interpreting show access-lists Output

```text
Extended IP access list 110
    10 deny tcp 192.168.20.0 0.0.0.255 host 10.0.0.5 eq telnet (12 matches)
    20 permit ip any any (3847 matches)
```

Key elements:

- The number before each entry is the sequence number
- The number in parentheses is the match counter — how many packets matched this entry
- A match counter of 0 may mean the ACL is not being applied to the intended traffic
- The entry marked `(0 matches)` on a deny rule may mean traffic is being caught by an earlier permit entry

---

## 8. CCNA Exam Tips

1. Standard ACL near destination, extended ACL near source. This placement rule is tested on nearly every CCNA attempt. Internalize the reason: standard ACLs cannot filter destination, so placing them at the source would block traffic to all destinations from that source.

2. The implicit deny drops all traffic that does not match an explicit ACE. Always add `permit ip any any` (or the appropriate permit) at the end of an ACL that is intended to only block specific traffic, not all traffic.

3. ACL direction (`in` vs `out`) matters. `in` filters packets arriving before routing. `out` filters packets leaving after routing. Getting the direction wrong is a common exam and production mistake. Use `show ip interface` to verify applied direction.

4. Named ACLs allow you to edit individual entries using sequence numbers. Numbered ACLs do not — to modify a numbered ACL, you must delete the entire ACL with `no access-list [number]` and recreate it.

5. The `host` keyword is equivalent to wildcard 0.0.0.0 (exact match). The `any` keyword is equivalent to wildcard 255.255.255.255 (match all). Both appear frequently in CCNA questions and on production equipment.

6. An ACL applied `in` on interface Gi0/0 filters traffic entering R1 on that interface. If you want to filter traffic leaving toward a LAN, apply the ACL `out` on the LAN-facing interface.

7. Only the first matching ACE is applied to a packet. Entry order matters. A `permit any` entered before a `deny` statement will catch all traffic first, making the deny unreachable (shadowed).

8. `show access-lists` shows match counters for each ACE. Use this during troubleshooting to confirm whether the ACL is being hit. Zero matches on a deny entry may indicate the ACL is applied on the wrong interface or in the wrong direction.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Write the placement rule for standard and extended ACLs from memory with the reasoning
- [ ] Write a standard ACL that blocks one subnet and permits all other traffic, then apply it to an interface in the outbound direction
- [ ] Write an extended ACL that blocks Telnet from one source subnet to one destination host and permits all other traffic, then apply it inbound
- [ ] Explain what implicit deny means and when you must add an explicit permit at the end
- [ ] Explain the difference between numbered and named ACLs in terms of editability
- [ ] Interpret a sample `show access-lists` output and identify what traffic is being blocked
- [ ] Complete the Module 10 Packet Tracer lab activity
- [ ] Post your Module 10 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com
