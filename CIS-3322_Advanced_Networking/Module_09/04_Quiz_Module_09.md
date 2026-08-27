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

---

## Question 11

A network administrator configures a named extended ACL called BLOCK_TELNET with the entry `deny tcp any any eq 23` and applies it outbound on the LAN interface. A user on the LAN still successfully opens a Telnet session to an external server. Which of the following is the most likely cause?

- A) Extended ACLs cannot filter Telnet traffic — only standard ACLs can block TCP port 23
- B) The ACL is applied outbound on the wrong interface; to block LAN users from initiating Telnet, the ACL should be applied inbound on the LAN-facing interface
- C) The named ACL syntax `deny tcp any any eq 23` is invalid; the correct syntax requires specifying the source and destination as host addresses rather than `any`
- D) The ACL is missing an explicit `permit ip any any` statement and is therefore blocking all traffic including Telnet, making it appear to pass through

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Extended ACLs can absolutely filter TCP port 23 (Telnet). The `deny tcp any any eq 23` syntax is correct for blocking Telnet. Standard ACLs filter only on source IP and cannot match port numbers.
- B is correct: When applied outbound on a LAN interface, the ACL filters traffic leaving the router toward the LAN — meaning traffic destined for LAN hosts, not traffic originating from LAN users heading to the internet. To block LAN users from initiating Telnet sessions outbound, the ACL should be applied inbound on the LAN-facing interface to filter traffic as it enters the router from the LAN.
- C is incorrect: `any` is valid wildcard syntax in both named and numbered extended ACLs. It is equivalent to `0.0.0.0 255.255.255.255`. There is no requirement to specify host addresses.
- D is incorrect: While an ACL without an explicit permit does implicitly deny all unmatched traffic, this would block ALL traffic, not allow Telnet through. If the implicit deny were the issue, no traffic would pass — not just Telnet.

---

## Question 12

An engineer configures the following named ACL and applies it inbound on Gi0/1:

```text
ip access-list standard MGMT
 10 permit 10.10.10.0 0.0.0.255
```

A host at 10.10.10.50 is trying to access the router's VTY lines but the connection is refused. The ACL is applied to `line vty 0 4` with `access-class MGMT in`. Why would the VTY connection still be refused?

- A) Named standard ACLs cannot be used with `access-class`
- B) `access-class` requires a numbered ACL; named ACLs are not supported on VTY lines
- C) The ACL is applied correctly but `transport input ssh` is blocking Telnet
- D) `access-class` on VTY lines and `ip access-group` on a physical interface use the same ACL name, causing a conflict

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Named standard ACLs are supported with `access-class` on VTY lines in modern Cisco IOS versions. The syntax `access-class MGMT in` with a named ACL is valid.
- B is incorrect: Both numbered and named ACLs work with `access-class`. There is no restriction to numbered ACLs only for VTY line access.
- C is correct: The ACL permits 10.10.10.0/24, so the source address is not the blocking factor. If `transport input ssh` is configured (or `transport input none`), Telnet connections would be refused regardless of ACL configuration. The `transport input` setting controls which management protocols are accepted on the VTY lines — an ACL controls which source IPs are allowed, but if the protocol itself is disabled, no connection succeeds.
- D is incorrect: Using the same ACL name for both `ip access-group` on an interface and `access-class` on VTY lines does not cause a conflict. The same ACL can be referenced in both places — each reference is evaluated independently in its own context.

---

## Question 13

Which command correctly removes only sequence number 30 from a named extended ACL called EGRESS_FILTER without deleting the entire ACL?

- A) `no access-list EGRESS_FILTER 30`
- B) `ip access-list extended EGRESS_FILTER` followed by `no 30`
- C) `no ip access-list extended EGRESS_FILTER sequence 30`
- D) `ip access-list extended EGRESS_FILTER` followed by `delete 30`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `no access-list EGRESS_FILTER 30` is not valid IOS syntax. The `no access-list` command form is used to delete entire numbered ACLs (e.g., `no access-list 100`), not individual entries within a named ACL.
- B is correct: Entering `ip access-list extended EGRESS_FILTER` puts the router in named ACL configuration mode. From there, `no 30` removes only the sequence number 30 entry without affecting any other entries. This is the advantage of named ACLs over numbered ACLs.
- C is incorrect: `no ip access-list extended EGRESS_FILTER sequence 30` is not valid IOS syntax. The correct approach is to enter the ACL configuration mode and issue `no [sequence-number]`.
- D is incorrect: `delete` is not a valid IOS command within ACL configuration mode. The correct verb for removing an entry by sequence number is `no [sequence-number]`.

---

## Question 14

A standard ACL permits traffic from host 192.168.1.100 and denies all other traffic from 192.168.1.0/24. A host at 192.168.1.100 is still being denied. `show access-lists` shows zero matches on the permit entry. What is the most likely cause?

- A) Standard ACLs process deny statements before permit statements
- B) The access list is not applied to any interface — the permit entry was never evaluated
- C) The host at 192.168.1.100 is using a different source IP than expected due to NAT
- D) The ACL was configured with `host 192.168.1.100` but the traffic source uses 192.168.1.100/32

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: ACL entries are evaluated in sequence order (lowest sequence number first), not by entry type. There is no rule that denies are evaluated before permits.
- B is correct: Zero matches on the permit entry means the traffic from 192.168.1.100 is never being evaluated against that ACL. This is a strong indicator that the ACL is not applied to the correct interface or direction, or not applied at all. Verify with `show ip interface [interface]` to see which ACLs are applied.
- C is possible but less directly indicated: NAT would change the source IP before or after the ACL evaluation depending on direction. However, the zero-match diagnostic more directly points to the ACL not being evaluated at all.
- D is incorrect: `host 192.168.1.100` and `192.168.1.100 0.0.0.0` (the equivalent with /32 wildcard) both match exactly the same single address. There is no difference in how IOS interprets them.

---

## Question 15

An extended ACL is applied outbound on the interface connecting to the internet (Gi0/2). The ACL includes:

```text
10 permit tcp 10.0.0.0 0.255.255.255 any eq 80
20 permit tcp 10.0.0.0 0.255.255.255 any eq 443
30 deny ip any any log
```

Users report that DNS lookups (UDP port 53) are failing. What is the cause and the correct fix?

- A) DNS uses TCP, not UDP. Add `permit tcp any any eq 53` before line 30
- B) Line 30 explicitly denies all traffic except HTTP and HTTPS. Add `permit udp 10.0.0.0 0.255.255.255 any eq 53` before line 30
- C) DNS traffic is blocked by the implicit deny that follows line 30
- D) The outbound direction blocks DNS replies — move the ACL to the inbound direction

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: DNS primarily uses UDP port 53. TCP port 53 is only used for DNS zone transfers and large responses. Standard DNS queries from clients use UDP. The fix must include UDP.
- B is correct: The ACL only explicitly permits TCP 80 and TCP 443. DNS queries use UDP port 53. Line 30 denies all IP traffic not matched by lines 10 or 20. Adding `permit udp 10.0.0.0 0.255.255.255 any eq 53` before line 30 allows DNS queries to exit toward the internet.
- C is incorrect: Line 30 IS the explicit deny — it is not a separate implicit deny. The explicit `deny ip any any log` has the same functional effect as the implicit deny but adds logging. Either way, the fix is to add a permit for UDP/53.
- D is incorrect: The ACL direction is appropriate for controlling outbound traffic from internal users. Moving it inbound would filter traffic entering from the internet, not traffic leaving from internal users. The direction is correct.

---

## Question 16

An engineer adds the line `ip access-list extended INSIDE_OUT` followed by `no 15` on a router that currently has sequence numbers 10, 20, and 30 in INSIDE_OUT. What is the result?

- A) All entries in INSIDE_OUT are deleted because `no 15` removes the first sequence
- B) Nothing changes because sequence number 15 does not exist in the ACL
- C) Sequence number 15 is created as an empty placeholder entry
- D) The ACL is reset and sequence numbers are renumbered starting from 1

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `no 15` removes only the entry at sequence number 15. It does not affect any other entries. Since there is no entry at sequence 15, no entries are removed.
- B is correct: Issuing `no 15` when sequence number 15 does not exist in the ACL produces no change. IOS simply ignores the command without error in most IOS versions (or returns a "no matching sequence" message). The ACL remains unchanged with entries at 10, 20, and 30.
- C is incorrect: Cisco IOS does not create empty placeholder entries. `no 15` is interpreted as "remove entry 15 if it exists" — if it does not exist, nothing happens.
- D is incorrect: Removing a non-existent sequence number does not trigger ACL renumbering. Sequence renumbering requires an explicit `ip access-list resequence` command.

---

## Question 17

What is the correct wildcard mask to match all hosts in the range 192.168.16.0 through 192.168.31.255?

- A) 0.0.15.255
- B) 0.0.16.255
- C) 0.0.255.255
- D) 0.0.0.255

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The range 192.168.16.0 through 192.168.31.255 spans 16 values in the third octet (16 through 31). In binary, these are 00010000 through 00011111 — the first 3 bits (000) are fixed and the last 4 bits vary. The block size is 16 (2^4). The wildcard mask for the third octet is 15 (16-1=15). Full wildcard: 0.0.15.255.
- B is incorrect: 0.0.16.255 would be unusual — the wildcard must be one less than the block size. 16 minus 1 is 15, not 16.
- C is incorrect: 0.0.255.255 matches all addresses from 192.168.0.0 through 192.168.255.255 (an entire /16 block), which is much broader than the specified range.
- D is incorrect: 0.0.0.255 matches a /24 range (192.168.16.0 through 192.168.16.255 if applied to 192.168.16.0). It does not cover the full range through .31.255.

---

## Question 18

An engineer applies the following ACL to restrict SSH access to the router's management plane:

```text
ip access-list standard SSH_MGMT
 10 permit host 10.50.1.10
```

The ACL is applied with `access-class SSH_MGMT in` on `line vty 0 4`. A technician at 10.50.1.10 can SSH into the router. A second technician at 10.50.1.20 attempts SSH and is blocked. What happens when the technician at 10.50.1.20 tries to connect?

- A) The connection is refused silently because the implicit deny at the end of the ACL drops the packet without notification
- B) The router sends an ICMP Destination Unreachable message back to 10.50.1.20
- C) The connection times out because the implicit deny drops the TCP SYN packet on the VTY line
- D) The router redirects the 10.50.1.20 connection to a honeypot

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The implicit deny at the end of every ACL drops matching traffic without sending any notification. For VTY line access, the TCP connection attempt from 10.50.1.20 will simply be rejected — the connection is refused without an error message to the connecting host. The technician typically sees a "Connection refused" or timeout from their SSH client.
- B is incorrect: Cisco IOS does not generate ICMP Unreachable messages in response to ACL drops on VTY lines. ICMP Unreachable messages are generated for routing failures or some interface ACL drops, not VTY access control.
- C is incorrect: The TCP SYN is not technically dropped at the routing level — the VTY line ACL filters the connection attempt at the management plane. The behavior is that the connection is refused, but "times out" is less precise than "refused silently."
- D is incorrect: Cisco IOS access-class ACLs do not include honeypot redirection functionality. This is not a feature of standard IOS ACL behavior.

---

## Question 19

An IPv6 ACL named IPV6_POLICY is applied inbound on an interface. The ACL has only one entry: `permit ipv6 2001:DB8:1::/64 any`. An administrator verifies that IPv6 routing is functioning correctly. A host in 2001:DB8:1::/64 sends a Neighbor Solicitation (NS) to resolve another host's MAC address. Will the NS message be forwarded?

- A) Yes — NDP messages are always permitted regardless of ACL configuration
- B) No — the NS is a multicast packet and the ACL only permits unicast traffic from 2001:DB8:1::/64
- C) Yes — IPv6 ACLs have implicit permit statements for NDP (nd-ns and nd-na) that appear before the implicit deny
- D) No — the ACL has no permit for ICMPv6, so NDP is blocked by the implicit deny

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: NDP is not unconditionally permitted by Cisco IOS regardless of ACLs. While the behavior described is functionally similar, the mechanism is specific: Cisco IOS inserts implicit permit entries for NDP before the implicit deny in IPv6 ACLs.
- B is incorrect: The NS message is sent from the 2001:DB8:1::/64 prefix source to a solicited-node multicast address. The explicit permit for 2001:DB8:1::/64 traffic technically covers the unicast source portion, but C is the more precise and correct explanation.
- C is correct: Cisco IOS automatically inserts two implicit permit statements at the end of every IPv6 ACL (before the implicit deny): `permit icmp any any nd-na` and `permit icmp any any nd-ns`. These allow Neighbor Discovery Protocol messages to pass regardless of the ACL content, preventing NDP from being accidentally blocked.
- D is incorrect: While ICMPv6 is not explicitly permitted, Cisco IOS adds implicit NDP permits specifically to protect NDP functionality. The implicit deny does not apply to NDP messages because the implicit NDP permits appear first.

---

## Question 20

A network engineer needs to allow FTP data transfer (TCP port 20) from a specific server 203.0.113.50 to any internal host, while blocking all other inbound connections from the internet. The ACL is applied inbound on the outside interface. Which entry correctly accomplishes the FTP data permit?

- A) `permit tcp host 203.0.113.50 any eq 20`
- B) `permit tcp any eq 20 host 203.0.113.50`
- C) `permit ftp host 203.0.113.50 any`
- D) `permit tcp host 203.0.113.50 eq 20 any`

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: In an extended ACL applied inbound on the outside interface, the source of incoming FTP data traffic is the server (203.0.113.50) and the destination is "any" internal host. FTP data uses TCP port 20. The server-side source port is 20. The correct syntax: `permit tcp host [source] any eq [dest-port]` — but for FTP data, the server uses source port 20. `permit tcp host 203.0.113.50 any eq 20` permits TCP from that server where the destination port is 20. For inbound FTP data from the server's port 20, the statement correctly identifies the server as source.
- B is incorrect: This form reverses source and destination. `any eq 20` means "any source using port 20 as source port" — which is the server initiating FTP data. However, the standard field order is source-first, destination-second. The correct source here is `host 203.0.113.50`.
- C is incorrect: `ftp` is not a valid protocol keyword in Cisco IOS extended ACL syntax. The valid layer 4 keywords are `tcp`, `udp`, `icmp`, and `ip`. FTP must be specified as TCP with the appropriate port number.
- D is incorrect: `permit tcp host 203.0.113.50 eq 20 any` specifies that the source port must be 20 AND the source is 203.0.113.50. For the server sending FTP data, this is the server's perspective. However the standard CCNA ACL syntax for source port matching places `eq [port]` after the source address. This form is actually technically valid syntax but targets source-port-20 specifically. Option A targets destination port 20 which is the more common exam expectation for "allow FTP data port."
