# Quiz: Module 09 — Access Control Lists (ACLs)

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Questions: 10 | Points: 10 (1 point each)

---

## Question 1

A network engineer needs to block all traffic from the 172.16.5.0/24 subnet from reaching the server farm at 10.10.10.0/24. All other traffic should be permitted. The engineer uses a standard ACL. Where should this ACL be applied?

- A) Inbound on the interface closest to the source subnet 172.16.5.0/24
- B) Outbound on the interface closest to the server farm 10.10.10.0/24
- C) Inbound on the interface closest to the server farm 10.10.10.0/24
- D) Outbound on the interface closest to the source subnet 172.16.5.0/24

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Applying a standard ACL inbound near the source would filter all traffic from that source regardless of destination. The standard ACL cannot distinguish which destination the traffic is headed to, so applying it near the source would block the source from reaching all destinations, not just the server farm.
- B is correct: Standard ACLs filter based on source IP address only. Placing the ACL outbound on the interface connected to the server farm ensures it only blocks the source subnet from reaching that specific destination. Traffic from the same source to other destinations is unaffected.
- C is incorrect: An inbound ACL on the server farm interface would filter traffic entering from outside toward the router, which would not be the direction of traffic destined for the server farm. Outbound is the correct direction for traffic flowing toward the connected segment.
- D is incorrect: Outbound on the source interface sends traffic away from the source subnet. Traffic from LAN hosts exits the router toward their destinations on different interfaces, not back out the LAN interface.

---

## Question 2

An engineer types the following command on a Cisco router:

```text
access-list 115 permit tcp 10.1.0.0 0.0.255.255 any eq 443
```

Which traffic does this entry permit?

- A) All TCP traffic from any source to the 10.1.0.0/16 network on port 443
- B) HTTPS traffic from any host in the 10.1.0.0/16 network to any destination
- C) All traffic from 10.1.0.0/16 to any destination using any protocol
- D) TCP traffic from any source destined for port 443 on hosts in 10.1.0.0/16

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The source and destination positions are reversed. In an extended ACL, the first address field is source and the second is destination. The source here is 10.1.0.0 0.0.255.255, not the destination.
- B is correct: Access list 115 is an extended ACL (100–199). The statement permits TCP traffic where the source is any address in 10.1.0.0/16 (wildcard 0.0.255.255 matches the first two octets exactly), the destination is any address, and the destination port is 443 (HTTPS).
- C is incorrect: The protocol keyword `tcp` restricts this entry to TCP traffic only, not all IP protocols. The keyword `ip` would match all protocols.
- D is incorrect: The `eq 443` qualifier applies to the destination port, and the destination is `any`, not 10.1.0.0/16. The 10.1.0.0/16 is the source field in this statement.

---

## Question 3

A network administrator wants to configure a standard ACL that permits exactly two hosts — 192.168.1.50 and 192.168.1.75 — and denies all others. Which configuration is correct?

- A) `access-list 20 permit 192.168.1.50` then `access-list 20 permit 192.168.1.75`
- B) `access-list 20 permit 192.168.1.50 0.0.0.255` then `access-list 20 permit 192.168.1.75 0.0.0.255`
- C) `access-list 20 permit 192.168.1.0 0.0.0.255`
- D) `access-list 20 permit host 192.168.1.50 192.168.1.75`

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: Each `permit` statement with a host address and no wildcard (or using the `host` keyword which implies 0.0.0.0 wildcard) matches exactly one IP address. Two separate permit statements cover both hosts. The implicit deny any at the end drops all other traffic.
- B is incorrect: The wildcard `0.0.0.255` matches any host in the 192.168.1.0/24 network, not just the two specified hosts. This would permit the entire subnet.
- C is incorrect: This permits the entire 192.168.1.0/24 subnet, not just the two specified hosts.
- D is incorrect: This is not valid ACL syntax. You cannot specify two host addresses in a single permit statement without a separate wildcard mask for each.

---

## Question 4

An engineer applies `ip access-group 101 in` on GigabitEthernet0/0 of R1. ACL 101 has only one entry: `deny tcp any any eq 23`. Traffic from the 10.1.1.0/24 LAN connected to Gi0/0 that is not Telnet is also being blocked. What is the most likely cause?

- A) The ACL is applied in the wrong direction — it should be outbound
- B) The ACL number 101 is in the standard range and cannot filter by port
- C) The implicit deny any at the end of the ACL is dropping all non-Telnet traffic
- D) The `deny tcp` entry must be changed to `deny ip` to match all protocols

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Inbound on Gi0/0 is the correct direction to filter traffic entering from the LAN. The direction is appropriate for the stated goal.
- B is incorrect: ACL number 101 is in the extended ACL range (100–199). Extended ACLs can filter by protocol and port. The configuration is valid.
- C is correct: The ACL contains only a single deny statement. After that entry, the implicit deny any drops all remaining traffic regardless of protocol. There is no `permit ip any any` entry to allow legitimate non-Telnet traffic. The fix is to add `access-list 101 permit ip any any` after the deny statement.
- D is incorrect: Changing the deny to `deny ip` would actually make the problem worse by explicitly denying all IP traffic in addition to what the implicit deny already drops. The issue is the missing permit, not the protocol keyword on the deny.

---

## Question 5

Which command correctly restricts management access to a router's VTY lines to only hosts in the 10.0.0.0/24 subnet?

- A) `ip access-group 5 in` applied to the VTY interface
- B) `access-class 5 in` applied under `line vty 0 4`
- C) `ip access-group 5 in` applied under `line vty 0 4`
- D) `access-class 5 in` applied to all physical interfaces

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `ip access-group` is the command for physical and logical Layer 3 interfaces. VTY lines are not physical interfaces and do not use this command.
- B is correct: The `access-class` command is the correct command to apply an ACL to VTY lines. It is entered in line configuration mode (`line vty 0 4`) and filters incoming connection attempts by source IP address.
- C is incorrect: `ip access-group` is not valid syntax under `line vty` configuration mode. The correct command is `access-class`.
- D is incorrect: Applying `access-class` to physical interfaces is not valid. Physical interfaces use `ip access-group`. Even if it were valid, applying it to physical interfaces would not restrict VTY management access specifically.

---

## Question 6

What is the correct wildcard mask to match all hosts in the 192.168.4.0/26 subnet?

- A) 0.0.0.255
- B) 0.0.0.128
- C) 0.0.0.63
- D) 255.255.255.192

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: 0.0.0.255 matches the entire 192.168.4.0/24 subnet (256 hosts), not a /26 (64 hosts).
- B is incorrect: 0.0.0.128 matches a /25 subnet (128 hosts). A /26 has 64 host addresses.
- C is correct: A /26 subnet mask is 255.255.255.192. Subtracting from 255: 255-255, 255-255, 255-255, 255-192 = 0.0.0.63. The wildcard mask 0.0.0.63 correctly identifies all 64 addresses in a /26 network.
- D is incorrect: 255.255.255.192 is the subnet mask for a /26 network, not the wildcard mask. Wildcard masks are conceptually the inverse of subnet masks.

---

## Question 7

An IPv6 ACL named FILTER_V6 is configured with a single entry: `deny tcp any any eq 23`. After applying it to an interface, administrators report that IPv6 routing between directly connected devices on that segment has stopped working. What is the most likely cause?

- A) The ACL is blocking OSPFv3 hello packets because OSPF uses TCP
- B) The deny entry is blocking all ICMPv6 traffic including Neighbor Discovery Protocol messages
- C) IPv6 ACLs cannot block Telnet — only IPv4 ACLs can filter by port number
- D) The ACL implicit deny is blocking the IPv6 NDP packets because there is no explicit permit for ICMPv6 nd-na and nd-ns

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: OSPFv3 uses IP protocol 89, not TCP. A TCP deny entry does not affect OSPF traffic.
- B is incorrect: The deny entry specifically targets TCP port 23. ICMPv6 uses IP protocol 58, not TCP. The explicit deny entry itself does not block ICMPv6.
- C is incorrect: IPv6 ACLs can absolutely filter by protocol and port number using the same syntax as IPv4 extended ACLs.
- D is correct: IPv6 ACLs include two implicit permit statements for NDP (nd-na and nd-ns) before the implicit deny. However, the implicit deny any at the end drops all traffic that does not match an explicit permit. The ACL has no `permit ipv6 any any` entry, so the implicit deny is dropping NDP traffic that would normally be covered by the implicit NDP permits only when those permits exist in the right position. The fix is to add `permit ipv6 any any` before the implicit deny takes effect, or to verify that the NDP implicit permits are active. In this scenario the missing explicit permit ipv6 any any is causing all non-Telnet traffic including routing-adjacent ICMPv6 to be dropped.

---

## Question 8

A network engineer needs to insert a new ACL entry between sequence numbers 10 and 20 in an existing ACL. Which ACL type supports this operation without deleting and recreating the entire ACL?

- A) Numbered standard ACL (range 1–99)
- B) Numbered extended ACL (range 100–199)
- C) Named ACL (standard or extended)
- D) Both numbered and named ACLs support in-place line insertion

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Numbered ACLs do not support line insertion. To add a statement between existing entries in a numbered ACL, the entire ACL must be deleted with `no access-list <number>` and recreated in the desired order.
- B is incorrect: Numbered extended ACLs have the same limitation. Inserting a line at a specific sequence position requires deleting and recreating the entire list.
- C is correct: Named ACLs (both standard and extended) support sequence-number-based line editing. You can enter the named ACL configuration mode and issue a new statement with a sequence number that falls between two existing entries. For example, `15 deny host 10.1.1.5` inserts between sequence 10 and sequence 20.
- D is incorrect: Only named ACLs support this operation. Numbered ACLs do not support in-place sequence insertion or deletion.

---

## Question 9

Review this ACL output from `show access-lists`:

```text
Extended IP access list OUTBOUND_FILTER
    10 permit tcp 10.0.0.0 0.255.255.255 any eq 80 (432 matches)
    20 permit tcp 10.0.0.0 0.255.255.255 any eq 443 (871 matches)
    30 deny ip any any (0 matches)
```

A network administrator reports that ICMP ping tests from internal hosts (10.x.x.x) to external destinations are failing. What does the output indicate?

- A) The ACL is not applied to any interface because match counters show zero on line 30
- B) ICMP traffic is being dropped by line 30 because there is no permit entry for ICMP
- C) Line 10 and line 20 are permitting too much traffic and need to be restricted further
- D) The ACL is only filtering outbound HTTP and HTTPS — all other traffic is being forwarded normally

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Zero matches on line 30 does not mean the ACL is unapplied. It means no traffic has yet matched that line during the counter period (or counters were recently cleared). The ACL could still be applied and actively filtering.
- B is correct: The ACL explicitly permits only TCP port 80 and TCP port 443 from internal hosts. ICMP uses IP protocol 1, not TCP, and there is no permit for ICMP or for `ip any any`. The implicit deny any (represented here as line 30 `deny ip any any`) drops all non-HTTP and non-HTTPS traffic, including ICMP pings. Adding `permit icmp 10.0.0.0 0.255.255.255 any` before line 30 would resolve the issue.
- C is incorrect: Lines 10 and 20 are correctly scoped to HTTP and HTTPS. They are not overly permissive and are not the cause of the ICMP failure.
- D is incorrect: The explicit `deny ip any any` at line 30 actively blocks all traffic that does not match lines 10 or 20. The network is not forwarding other traffic normally — it is dropping it.

---

## Question 10

An engineer configures the following ACL on R1 and applies it inbound on the interface connected to the HR subnet (172.16.10.0/24):

```text
ip access-list extended HR_FILTER
  10 deny tcp host 172.16.10.55 any eq 443
  20 permit ip 172.16.10.0 0.0.0.255 any
```

A user at 172.16.10.55 reports they can still reach HTTPS websites. The `show access-lists HR_FILTER` output shows 0 matches on line 10 and increasing matches on line 20. What is the most likely cause?

- A) The ACL is applied in the outbound direction instead of inbound
- B) The host 172.16.10.55 is actually using a different source IP address due to DHCP reassignment
- C) The ACL is applied to the wrong interface — it should be on the interface toward the internet
- D) Line 20 uses `permit ip` which matches all IP traffic from the entire subnet before the host-specific deny on line 10 can be evaluated

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The question states the ACL is applied inbound, and inbound on the HR subnet interface is the correct direction to filter traffic from HR hosts. Direction is not the problem here.
- B is possible but less likely: DHCP reassignment is a valid operational concern but the question focuses on ACL logic and the show output provides a clearer diagnostic — zero matches on line 10 indicates the traffic is not reaching that entry.
- C is correct: The zero matches on line 10 combined with the increasing matches on line 20 indicate that traffic from 172.16.10.55 is matching line 20 and being permitted, which means the ACL logic is running but the specific deny is not being hit. The most operationally likely cause in a real scenario is that the ACL is applied to the wrong interface and never sees the HTTPS traffic from that host. If the ACL were on the correct inbound interface facing the HR subnet, line 10 would fire for any HTTPS traffic from .55.
- D is incorrect: Line 10 is a deny for a specific host. Line 20 permits the broader subnet. Because line 10 comes first in sequence order, it would be evaluated before line 20 for traffic from host .55. If the ACL were processing traffic from .55, line 10 would match first.
