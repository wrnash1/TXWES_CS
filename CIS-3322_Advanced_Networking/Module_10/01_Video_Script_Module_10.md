# Video Script: Module 10 - Access Control Lists

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 5: Security Fundamentals - 15%)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for all ACL configuration and verification demonstrations
- Show `show access-lists` output with match counters incrementing live
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: What ACLs Do and Why They Matter [00:00 - 03:30]

Welcome to Module 10. I am Professor Nash. Today we configure one of the most commonly used security tools in Cisco IOS: Access Control Lists.

An ACL is an ordered list of rules. Each rule — called an Access Control Entry, or ACE — either permits or denies traffic based on criteria you define. The router processes each packet against the ACL entries from top to bottom. The first matching entry wins. If no entry matches, the implicit deny at the end drops the packet.

[SHOW DIAGRAM: A router with an interface labeled "Gi0/0 inbound." A stream of packets approaching the interface. Each packet is evaluated against ACL entries in order: first entry is checked (no match, arrow continues), second entry is checked (match, permit arrow goes through), and a final implicit deny block at the bottom stops any unmatched traffic]

ACLs are used for:

- Traffic filtering: permit or deny specific traffic types
- Route filtering: control what routes are advertised in routing protocols
- VPN interesting traffic: define which traffic triggers a VPN tunnel
- Quality of Service: classify traffic for QoS treatment

Today we focus on the security use case — filtering traffic at router interfaces.

---

## Section 2: Standard vs Extended ACLs [03:30 - 09:00]

[SHOW DIAGRAM: Two columns. Left column labeled "Standard ACL" shows a packet with only the Source IP highlighted as the matching criteria. Right column labeled "Extended ACL" shows a packet with Source IP, Destination IP, Protocol, and Port Number all highlighted as matching criteria]

There are two types of ACLs for traffic filtering:

### Standard ACLs

- Filter based on source IP address only
- Cannot match destination, protocol, or port
- Numbered range: 1 to 99 and 1300 to 1999
- Placement rule: apply close to the destination

Why close to the destination? Because a standard ACL can only see the source IP. If you place it close to the source, you might block traffic from that source to ALL destinations — including ones you want to allow. Placing it near the destination ensures you only block the specific traffic you intend.

### Extended ACLs

- Filter based on source IP, destination IP, protocol, and port number
- Numbered range: 100 to 199 and 2000 to 2699
- Placement rule: apply close to the source

Why close to the source? Extended ACLs can precisely identify what traffic to block. Placing them at the source stops unwanted traffic immediately, before it wastes bandwidth crossing the network.

CCNA Exam Tip: This placement rule is one of the most frequently tested ACL topics on the CCNA. Standard ACL = close to destination. Extended ACL = close to source. Memorize this.

---

## Section 3: ACL Syntax and Configuration [09:00 - 15:00]

[SHOW DIAGRAM: Topology with R1 connecting to two LAN segments: 192.168.10.0/24 (Engineering) and 192.168.20.0/24 (Sales). A server at 192.168.30.1 is on a third segment. Arrow showing we want to block Sales from reaching the server but allow Engineering]

### Standard ACL Configuration

Block the Sales subnet (192.168.20.0/24) from reaching 192.168.30.0/24:

```ios
R1(config)# access-list 10 deny 192.168.20.0 0.0.0.255
R1(config)# access-list 10 permit any
```

Apply it close to the destination (the server's segment):

```ios
R1(config)# interface GigabitEthernet0/2
R1(config-if)# ip access-group 10 out
```

### Extended ACL Configuration

Block only Telnet (TCP port 23) from Sales to the server, while permitting everything else:

```ios
R1(config)# access-list 110 deny tcp 192.168.20.0 0.0.0.255 host 192.168.30.1 eq 23
R1(config)# access-list 110 permit ip any any
```

Apply it close to the source (Sales segment interface, inbound):

```ios
R1(config)# interface GigabitEthernet0/1
R1(config-if)# ip access-group 110 in
```

CCNA Exam Tip: Every ACL has an implicit `deny any any` at the end. If your only ACL entry is a deny statement, all other traffic is also blocked. Always add an explicit `permit ip any any` at the end of an ACL unless your intent is to block everything that did not match a permit.

### Named ACLs

Named ACLs use descriptive names instead of numbers and allow individual entries to be deleted or resequenced:

```ios
R1(config)# ip access-list extended BLOCK_TELNET
R1(config-ext-nacl)# deny tcp 192.168.20.0 0.0.0.255 any eq 23
R1(config-ext-nacl)# permit ip any any
```

Named ACLs are easier to manage in production — you can remove a single entry by sequence number without deleting and recreating the entire ACL.

---

## Section 4: Wildcard Masks in ACLs [15:00 - 18:30]

ACL wildcard masks follow the same logic as OSPF wildcard masks. A 0 bit means the address bit must match. A 1 bit means any value is accepted.

Examples:

- `host 192.168.10.5` = exactly 192.168.10.5 (wildcard 0.0.0.0)
- `192.168.10.0 0.0.0.255` = any address in the 192.168.10.0/24 range
- `any` = all addresses (wildcard 255.255.255.255)
- `192.168.0.0 0.0.255.255` = any address in the 192.168.0.0/16 range

CCNA Exam Tip: The keyword `host` is shorthand for a wildcard of 0.0.0.0 — it matches exactly one IP address. The keyword `any` is shorthand for a wildcard of 255.255.255.255 — it matches all IP addresses. You will see both on the exam and must recognize them as wildcard shortcuts.

---

## Section 5: Verification and Troubleshooting [18:30 - 22:00]

Key verification commands:

```ios
R1# show access-lists
R1# show ip interface GigabitEthernet0/1
R1# show running-config | section access-list
```

### Interpreting show access-lists

```text
Extended IP access list 110
    10 deny tcp 192.168.20.0 0.0.0.255 host 192.168.30.1 eq telnet (8 matches)
    20 permit ip any any (1432 matches)
```

The match counter shows how many packets matched each entry. A zero-match deny entry may indicate the ACL is never being hit — verify placement and direction.

### Common ACL Mistakes

- Wrong direction (in vs out): use `show ip interface` to confirm the applied direction
- ACL applied to wrong interface: check which interface faces the intended traffic
- Implicit deny blocking all traffic: missing `permit ip any any` at the end
- Shadowed entry: a deny statement earlier in the list is catching traffic that was intended to match a permit entry lower in the list

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 10 Complete
Next: Module 11 - NAT and PAT Configurations
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
