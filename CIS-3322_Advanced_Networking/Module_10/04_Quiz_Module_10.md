# Quiz: Module 10 — NAT and PAT

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Questions: 10 | Points: 10 (1 point each)

---

## Question 1

An engineer runs `show ip nat translations` and sees the following entry:

```text
Pro  Inside global      Inside local       Outside local    Outside global
tcp  203.0.113.5:1055   10.1.1.20:52341    8.8.8.8:443      8.8.8.8:443
```

Which address is the inside local address?

- A) 203.0.113.5
- B) 10.1.1.20
- C) 8.8.8.8
- D) 203.0.113.5:1055

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 203.0.113.5 is the inside global address — the public IP representing the internal host as seen from the internet side of the router.
- B is correct: 10.1.1.20 is the inside local address — the private IP address of the internal host as seen from inside the network. This is the RFC 1918 address actually assigned to the host's interface.
- C is incorrect: 8.8.8.8 appears in both outside local and outside global columns. It is the address of the external destination server, not the internal host.
- D is incorrect: 203.0.113.5:1055 is the inside global address with its translated port number. The port number is a PAT artifact, and the full address:port combination is not a standalone address type.

---

## Question 2

Which keyword in a Cisco IOS NAT command distinguishes PAT from dynamic NAT?

- A) `dynamic`
- B) `pool`
- C) `overload`
- D) `static`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The keyword `dynamic` is not used in the `ip nat inside source` command syntax. Dynamic NAT is implied by using a pool without the overload keyword — there is no explicit `dynamic` keyword.
- B is incorrect: The `pool` keyword is used in both dynamic NAT and PAT with a named pool. It identifies the address pool to use for translation but does not by itself enable PAT behavior.
- C is correct: The `overload` keyword appended to the `ip nat inside source` command enables Port Address Translation. Without `overload`, only one inside host can use each pool address at a time (dynamic NAT). With `overload`, multiple inside hosts share each address using unique port numbers.
- D is incorrect: The `static` keyword is used in a completely different command form — `ip nat inside source static <local> <global>` — to create permanent one-to-one mappings. It has nothing to do with enabling PAT.

---

## Question 3

A network engineer configures NAT on a router but internal hosts still cannot reach the internet. The engineer runs `show ip nat statistics` and sees the following:

```text
Total active translations: 0 (0 static, 0 dynamic; 0 extended)
Outside interfaces:
Inside interfaces:
Hits: 0  Misses: 0
```

What is the most likely cause?

- A) The ip nat inside source list command is missing the overload keyword
- B) The ACL used in the NAT rule does not match any inside host addresses
- C) Neither `ip nat inside` nor `ip nat outside` has been applied to any interface
- D) The NAT pool has been exhausted by too many active translations

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: A missing `overload` keyword would cause dynamic NAT behavior (one-to-one from pool), not a total absence of translations. The statistics would show translations if the ACL and interfaces were correctly configured.
- B is incorrect: An ACL mismatch would result in zero translations, but the `show ip nat statistics` output would still show the correct inside and outside interfaces. The fact that both lists are empty points to a more fundamental issue.
- C is correct: The empty "Outside interfaces" and "Inside interfaces" lines confirm that `ip nat inside` and `ip nat outside` have not been applied to any interfaces. NAT requires the router to know which side is inside and which is outside before it can identify traffic eligible for translation. Without these markings, NAT never triggers regardless of the translation rule.
- D is incorrect: Pool exhaustion would show active translations at the maximum pool size and a translation failure counter incrementing. The output shows zero translations and zero hits, which rules out pool exhaustion.

---

## Question 4

A company has one public IP address assigned by their ISP: 198.51.100.1. They have 500 internal hosts in the 10.0.0.0/16 network. Which NAT configuration allows all 500 hosts to access the internet simultaneously using the single public IP?

- A) `ip nat inside source list 1 pool SINGLE overload` with pool 198.51.100.1 to 198.51.100.1
- B) `ip nat inside source static 10.0.0.0 198.51.100.1`
- C) `ip nat inside source list 1 pool SINGLE` with pool 198.51.100.1 to 198.51.100.1 and no overload
- D) Five hundred static NAT mappings, one per host

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: PAT with `overload` allows all 500 hosts to share the single public IP address simultaneously. The pool is defined with the single IP address as both start and end, and the `overload` keyword enables port multiplexing to distinguish each host's sessions.
- B is incorrect: Static NAT creates a permanent one-to-one mapping. Mapping the entire network address 10.0.0.0 to one public IP is not valid static NAT syntax and would not allow 500 hosts to communicate simultaneously.
- C is incorrect: Dynamic NAT without `overload` allows only one inside host per pool address at a time. With a single address in the pool, only one of the 500 hosts could be translated at any given moment.
- D is incorrect: 500 static mappings would require 500 public IP addresses — one per host. The scenario specifies only one public IP address is available.

---

## Question 5

Which NAT type is most appropriate for an organization hosting an internal web server that must always be accessible from the internet at the same public IP address?

- A) PAT with overload
- B) Dynamic NAT with a pool
- C) Static NAT
- D) NAT64

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: PAT is designed for outbound internet access from many internal hosts. PAT translations are created dynamically when inside hosts initiate connections and are not permanent. External hosts cannot reliably initiate connections to PAT-translated addresses.
- B is incorrect: Dynamic NAT assigns pool addresses on a first-come, first-served basis. The public IP address assigned to the web server would change each time the translation expires and re-forms. A consistent public IP is not guaranteed.
- C is correct: Static NAT creates a permanent, bidirectional one-to-one mapping between the inside local and inside global address. The web server always has the same public IP address. External users can always initiate connections to that address and the router consistently forwards them to the internal server.
- D is incorrect: NAT64 is a translation mechanism for IPv6-to-IPv4 communication during network migration. It is not the appropriate tool for making an IPv4 internal server reachable from the IPv4 internet.

---

## Question 6

An engineer uses the command `ip nat inside source list 10 interface GigabitEthernet0/1 overload`. What does the `interface GigabitEthernet0/1` portion of this command specify?

- A) The interface that should have `ip nat inside` applied to it
- B) The interface whose IP address is used as the inside global address for PAT translations
- C) The interface that monitors NAT translation statistics
- D) The interface where the NAT access list is applied for traffic matching

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The `interface` keyword in this command context specifies the source of the public IP address used for translation — it does not configure the inside designation on that interface. The `ip nat inside` and `ip nat outside` commands are applied separately in interface configuration mode.
- B is correct: Using `interface GigabitEthernet0/1` in the PAT command tells the router to dynamically use whatever IP address is currently assigned to that interface as the inside global address. This is particularly useful when the outside interface gets its IP via DHCP from the ISP and the public IP may change.
- C is incorrect: NAT statistics are collected globally and are not tied to a specific monitoring interface. `show ip nat statistics` reports overall totals regardless of which interface keyword was used in the NAT command.
- D is incorrect: The access list in the `ip nat inside source list` command is a numbered or named ACL that identifies which inside hosts are eligible for translation. The interface keyword does not affect where the ACL is applied.

---

## Question 7

Review the following partial configuration:

```text
access-list 5 permit 172.16.0.0 0.0.255.255
ip nat inside source list 5 interface Serial0/0/0 overload
interface GigabitEthernet0/0
  ip nat inside
interface Serial0/0/0
  ip nat outside
```

A host at 172.16.50.100 initiates a TCP connection to 93.184.216.34 on port 80. Which inside global address will appear in the NAT translation table for this session?

- A) 172.16.50.100
- B) The IP address currently assigned to Serial0/0/0
- C) The IP address currently assigned to GigabitEthernet0/0
- D) 93.184.216.34

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 172.16.50.100 is the inside local address — the original private address of the host. NAT replaces the inside local with an inside global address. The inside local is not the translated address.
- B is correct: The PAT command uses `interface Serial0/0/0` as the source of the inside global address. Whatever IP address is assigned to Serial0/0/0 (the outside WAN interface) becomes the public source address in the translated packet. The router also assigns a unique source port to distinguish this session.
- C is incorrect: GigabitEthernet0/0 is marked as the inside interface. Its IP address (172.16.x.x likely) is the inside network gateway address and is never used as the inside global in this NAT configuration.
- D is incorrect: 93.184.216.34 is the outside global (destination) address. It is the server being contacted and has no role as the inside global translation address.

---

## Question 8

An engineer needs to remove all dynamic NAT translations from the translation table to test a configuration change. Which command accomplishes this without removing static NAT entries?

- A) `no ip nat inside source list 1 pool MYPOOL`
- B) `clear ip nat translation *`
- C) `clear ip nat translation inside 192.168.1.0 203.0.113.0`
- D) `reload`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: This command removes the NAT translation rule from the configuration entirely. It would prevent any future translations from occurring. The goal is to clear existing dynamic entries, not remove the configuration.
- B is correct: `clear ip nat translation *` removes all dynamic NAT and PAT translation entries from the translation table. Static NAT entries — created with `ip nat inside source static` — are not removed by this command. They are permanent until the static mapping is removed from the configuration.
- C is incorrect: This syntax attempts to clear a specific translation entry but uses network addresses rather than host addresses and is not valid syntax for this purpose. Specific entry removal requires the full inside local and inside global host addresses with protocol and ports for extended entries.
- D is incorrect: Reloading the router would clear all dynamic translations (and many other things) but is destructive, causes outages, and is not an acceptable solution for clearing NAT translations during a configuration change.

---

## Question 9

Which statement correctly describes NAT64?

- A) NAT64 translates between private IPv4 addresses and public IPv4 addresses, eliminating the need for RFC 1918 addressing
- B) NAT64 translates between IPv6 source addresses and IPv4 destination addresses, allowing IPv6-only hosts to communicate with IPv4-only internet services
- C) NAT64 is a Cisco-proprietary feature that translates between 6-bit and 4-bit network prefixes for legacy protocol support
- D) NAT64 is identical to PAT but uses 64-bit port numbers to support a larger number of simultaneous sessions

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The function described — translating between private and public IPv4 — is standard NAT/PAT. NAT64 is specifically about IPv6-to-IPv4 translation and has nothing to do with RFC 1918 private addressing.
- B is correct: NAT64 is a transition mechanism that enables IPv6-only hosts to initiate connections to IPv4-only destinations. The NAT64 router translates the IPv6 packet headers to IPv4 before forwarding to the IPv4 internet. DNS64 complements this by synthesizing AAAA records for IPv4 hosts.
- C is incorrect: NAT64 is an IETF-standardized protocol (RFC 6146), not Cisco-proprietary. The "64" refers to IPv6 and IPv4, not bit widths of network prefixes.
- D is incorrect: NAT64 is not related to PAT or to port number sizes. TCP and UDP use 16-bit port numbers in both IPv4 and IPv6 — this has not changed.

---

## Question 10

A router has the following NAT configuration. A host at 10.1.1.15 tries to reach a server at 172.20.5.5 through the NAT router, but the connection fails. `show ip nat translations` shows no entries for this host.

```text
access-list 100 permit ip 10.1.1.0 0.0.0.255 any
ip nat inside source list 100 interface GigabitEthernet0/1 overload
interface GigabitEthernet0/0
  ip address 10.1.1.1 255.255.255.0
  ip nat inside
interface GigabitEthernet0/1
  ip address 203.0.113.1 255.255.255.252
  ip nat outside
```

What is the most likely cause of the failure?

- A) Extended ACL 100 cannot be used with NAT — only standard ACLs are permitted
- B) The destination 172.20.5.5 is a private address and NAT cannot translate traffic to private destinations
- C) No default route exists on the router, so translated packets have no path to reach 172.20.5.5
- D) The overload keyword is preventing the host from being translated because the translation table is full

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Cisco IOS supports both standard and extended ACLs in NAT commands. Using an extended ACL (100–199) with `ip nat inside source list` is valid. Extended ACLs can actually provide more precise control over which traffic is eligible for translation.
- B is incorrect: NAT does not restrict translations based on whether the destination is a private or public address. The NAT rule translates the source address regardless of the destination. If routing exists to 172.20.5.5, the translation will occur.
- C is correct: After PAT translates the source address, the router must route the packet to the destination 172.20.5.5. If no route exists (no default route and no specific route to 172.20.5.5), the router drops the packet. The translation table would show no entry because the NAT process depends on the packet being successfully routable after translation. Adding a default route or a specific route to the 172.20.0.0 network would resolve this.
- D is incorrect: PAT does not have a practical translation limit for a single active host connection. The overload mechanism supports tens of thousands of simultaneous connections per public IP. A single host at 10.1.1.15 would not exhaust the table.

---

## Question 11

A router has a static NAT entry: `ip nat inside source static 192.168.1.100 203.0.113.50`. An external host initiates a TCP connection to 203.0.113.50. What address does the router forward this packet to?

- A) 203.0.113.50
- B) 192.168.1.100
- C) The router's inside interface IP address
- D) The router drops the packet because static NAT only supports outbound traffic

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: 203.0.113.50 is the inside global (public) address. The purpose of static NAT is to translate inbound connections destined for the public address to the corresponding private address. The router does not forward to 203.0.113.50 internally.
- B is correct: Static NAT creates a permanent bidirectional mapping. When an external host sends traffic to 203.0.113.50, the NAT router rewrites the destination to 192.168.1.100 (the inside local address) and forwards the packet to the internal host. This is what makes static NAT suitable for hosting servers.
- C is incorrect: The inside interface IP is the router's own LAN address, not a translated destination. The router does not redirect inbound NAT traffic to itself.
- D is incorrect: Static NAT is explicitly bidirectional. Unlike PAT (which only allows inside-initiated outbound sessions), static NAT allows external hosts to initiate connections to the mapped public IP.

---

## Question 12

Which command displays the current NAT translation table including port numbers for PAT sessions?

- A) `show ip nat statistics`
- B) `show ip nat translations verbose`
- C) `show ip nat translations`
- D) `debug ip nat`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show ip nat statistics` shows summary counters — total active translations, hit/miss counts, and interface markings. It does not display individual translation entries with port numbers.
- B is incorrect: Adding the `verbose` keyword to `show ip nat translations` provides additional detail about translation aging timers, but the standard command without verbose already shows port numbers in PAT entries.
- C is correct: `show ip nat translations` displays the full translation table including protocol, inside local address with port, inside global address with port, outside local address, and outside global address for all active NAT and PAT sessions. This is the primary verification command for NAT troubleshooting.
- D is incorrect: `debug ip nat` generates real-time translation event output to the console. It is a diagnostic tool, not a display command. Using it on a busy router generates enormous output and is not suitable for reading the translation table.

---

## Question 13

A router performs PAT using a pool named INTERNET_POOL containing addresses 198.51.100.5 through 198.51.100.8 with the `overload` keyword. Currently 10,000 simultaneous sessions are active through 198.51.100.5. A new inside host initiates a connection. How does the router handle the new session?

- A) The router drops the new connection because 198.51.100.5 is fully utilized
- B) The router assigns the next pool address (198.51.100.6) and begins using it
- C) The router continues using 198.51.100.5 and assigns a new unique port number to the new session
- D) The router sends an ICMP Destination Unreachable message to the inside host

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: With PAT using a pool, the router does not abandon a pool address unless its port space is truly exhausted (all 65,535 ports in use simultaneously, which is extremely rare). But in standard pool-based PAT operation, when one address fills up, the router moves to the next address in the pool.
- B is correct: PAT with a pool exhausts addresses sequentially. After the current address's port space becomes full, the router begins allocating from the next address in the pool (198.51.100.6). Each pool address can support tens of thousands of simultaneous sessions before the router advances.
- C is incorrect: The router would continue using .5 if port space remains available on it. However, if .5 is truly saturated, it advances to .6. The exact behavior depends on implementation, but the defined pool behavior is to move to the next address when needed.
- D is incorrect: NAT/PAT does not send ICMP Unreachable messages when a pool address is in use. The router either continues with the current address or moves to the next pool address.

---

## Question 14

Which RFC 1918 private address range can be subnetted to provide subnets with up to 65,534 host addresses each?

- A) 10.0.0.0/8
- B) 172.16.0.0/12
- C) 192.168.0.0/16
- D) All three RFC 1918 ranges support subnets of this size

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: 10.0.0.0/8 is a single Class A private block providing 16,777,216 total addresses. Subnetting it to /16 (for example) provides 256 subnets each with 65,534 usable host addresses. The /8 prefix length gives the most flexibility for creating large subnets.
- B is incorrect: 172.16.0.0/12 spans 172.16.0.0 through 172.31.255.255 and provides 1,048,576 addresses. Subnetting to /17 or larger would approach but not exceed 65,534 hosts per subnet from within this block.
- C is incorrect: 192.168.0.0/16 spans 192.168.0.0 through 192.168.255.255. Each natural /24 provides 254 hosts. A /16 subnet of this range provides 65,534 hosts but uses the entire RFC 1918 192.168.0.0/16 block — leaving no address space for additional subnets in that range.
- D is incorrect: Only 10.0.0.0/8 is large enough to contain multiple subnets each with 65,534 hosts. The other ranges are too small to support multiple such large subnets.

---

## Question 15

An engineer configures NAT with the following commands. After configuration, inside hosts can reach some internet destinations but not others. `show ip nat translations` shows entries being created correctly.

```text
ip route 0.0.0.0 0.0.0.0 203.0.113.254
ip nat inside source list 1 interface Serial0/0/0 overload
```

What is the most likely cause of the partial connectivity?

- A) The ACL is blocking some destinations but not others
- B) The inside interface is missing the ip nat inside command
- C) The ISP is rejecting translated packets because the source IP is a private address
- D) Some destination servers are blocking PAT-translated source addresses

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: The ACL used in NAT identifies inside hosts eligible for translation — it is not a destination filter. All inside hosts permitted by ACL 1 are translated regardless of destination. A NAT ACL cannot selectively block some internet destinations.
- B is incorrect: If the inside interface were missing `ip nat inside`, no translations would be created at all. The question states that `show ip nat translations` confirms entries are being created correctly, which means interface markings are working.
- C is incorrect: The purpose of PAT is to replace the private source address with the public interface address. ISPs see the translated public IP as the source, not the RFC 1918 address. If the inside global address were private, this would cause routing issues — but the command uses the serial interface which presumably has a public IP from the ISP.
- D is correct: Some destination servers apply IP reputation filtering, geographic blocks, or antispoofing rules that may block certain source addresses. If translations are confirmed working but specific destinations fail, the most likely cause is destination-side filtering. This is a real-world scenario where NAT is working correctly but some services block the source IP.

---

## Question 16

A network engineer wants to verify which interfaces are marked as NAT inside and NAT outside on a router. Which command provides this information?

- A) `show ip interface brief`
- B) `show ip nat statistics`
- C) `show running-config | section nat`
- D) `show ip nat translations`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `show ip interface brief` displays interface IP addresses and line protocol status. It does not indicate NAT inside/outside interface markings.
- B is correct: `show ip nat statistics` displays summary information including the explicit lists of interfaces marked as inside and outside. The output includes an "Inside interfaces:" line and an "Outside interfaces:" line listing each marked interface by name. This is the fastest way to confirm NAT interface markings.
- C is incorrect: While `show running-config | section nat` would show the `ip nat inside` and `ip nat outside` commands embedded in each interface stanza, it requires parsing the full output. `show ip nat statistics` is the direct command that lists interface markings in one place.
- D is incorrect: `show ip nat translations` displays the active translation table entries. It shows address and port mappings but does not indicate which interfaces are marked inside or outside.

---

## Question 17

When PAT is in use and an internal host at 10.0.0.5:52200 connects to a web server, the router creates a translation entry. The same router also has an internal host at 10.0.0.8 that happens to use source port 52200 for a different web connection. How does the router differentiate the two sessions in its translation table?

- A) The router assigns different inside global port numbers to each session even if the inside local port numbers match
- B) The router can only handle one session per source port number and drops the second connection
- C) The router changes the destination port of one session to differentiate them
- D) The router uses a different inside global IP address for each session

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: PAT tracks sessions using the combination of inside local IP address, inside local port, inside global IP address, and inside global port. Even if two inside hosts happen to choose the same source port, the router assigns different inside global port numbers in the translation table to distinguish the sessions. This is the core mechanism that allows thousands of simultaneous connections through a single public IP.
- B is incorrect: PAT does not limit one session per source port. Port uniqueness is maintained on the inside global (public) side, not the inside local (private) side. Multiple inside hosts can use the same source port simultaneously.
- C is incorrect: PAT never modifies the destination port. Changing the destination port would break the connection because the server would receive traffic on the wrong port and reject it.
- D is incorrect: Standard PAT uses a single inside global IP address (or a pool). Assigning different public IPs per session would be dynamic NAT, not PAT. PAT multiplexes sessions through the same public IP using port differentiation.

---

## Question 18

A Cisco router has the following configuration. Which of the following statements correctly describes the behavior when host 192.168.10.50 sends traffic to 8.8.8.8?

```text
access-list 10 permit 192.168.10.0 0.0.0.255
ip nat inside source list 10 pool PUBLIC overload
ip nat pool PUBLIC 203.0.113.20 203.0.113.25 netmask 255.255.255.248
interface GigabitEthernet0/0
  ip nat inside
interface GigabitEthernet0/1
  ip nat outside
```

- A) The host's source address is translated to an address between 203.0.113.20 and 203.0.113.25 with a unique port number
- B) The host's traffic is dropped because it does not have a static mapping
- C) The host's source address is translated to 203.0.113.20 only, regardless of other active sessions
- D) The pool addresses are added to the host's traffic as additional source addresses

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: The configuration uses PAT (`overload`) with a named pool containing addresses 203.0.113.20 through 203.0.113.25. The router selects an address from the pool and assigns a unique source port, creating a PAT entry in the translation table. Multiple inside hosts share pool addresses with port differentiation.
- B is incorrect: Static mappings are required only for static NAT. This configuration uses dynamic PAT with an ACL that matches the 192.168.10.0/24 subnet. Host .50 matches ACL 10 and is eligible for translation.
- C is incorrect: The pool contains six addresses (.20 through .25). The router uses them sequentially as needed. It does not restrict all sessions to .20 unless only one address were in the pool.
- D is incorrect: NAT translates (replaces) the source address — it does not add addresses. The original inside local address is replaced by the inside global address in the outbound packet header.

---

## Question 19

What is the primary limitation of dynamic NAT (without overload) compared to PAT?

- A) Dynamic NAT does not support TCP connections — only UDP
- B) Dynamic NAT requires a public IP address for each simultaneous inside connection
- C) Dynamic NAT cannot translate RFC 1918 addresses from the 10.0.0.0/8 range
- D) Dynamic NAT only works with static routing and is incompatible with OSPF

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Dynamic NAT supports TCP, UDP, ICMP, and other protocols. Protocol support is not the distinguishing factor between NAT types.
- B is correct: Dynamic NAT creates one-to-one address translations from a pool. Each simultaneous inside connection consumes one public IP address from the pool. If the pool has 10 addresses, only 10 inside hosts can be translated at the same time. The 11th host must wait for a pool address to become available. PAT solves this by multiplexing thousands of connections onto each pool address using port tracking.
- C is incorrect: Dynamic NAT translates any private address that matches the ACL criteria, including all RFC 1918 ranges (10.x.x.x, 172.16-31.x.x, 192.168.x.x). There is no restriction on which private range is used.
- D is incorrect: NAT is independent of the routing protocol in use. Whether the router uses OSPF, EIGRP, static routes, or BGP has no bearing on NAT functionality.

---

## Question 20

An engineer runs `show ip nat translations` and notices that translation entries for active sessions disappear after a few minutes, then reappear when new traffic is generated. What is the normal explanation for this behavior?

- A) The NAT process is malfunctioning and needs to be restarted
- B) NAT translation entries have idle timers and are removed after a configurable period of inactivity
- C) The router is running low on memory and is purging translation entries to free resources
- D) The ACL is periodically removing and reapplying itself, causing translations to reset

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Translation entries timing out and being recreated when traffic resumes is normal NAT behavior, not a malfunction. The NAT process is working correctly.
- B is correct: NAT and PAT translation entries have aging timers. Dynamic UDP translations typically expire after 5 minutes of inactivity. Dynamic TCP translations after 24 hours (configurable). Once a translation expires, the entry is removed from the table. When the inside host generates new traffic, a new translation is created. This is expected behavior and does not indicate a problem.
- C is incorrect: Low memory would cause different symptoms — potentially affecting routing table maintenance or causing IOS instability. NAT aging is a design feature, not a memory management behavior.
- D is incorrect: ACLs do not periodically reapply themselves. ACLs are static configuration entries that evaluate packets — they do not cause translations to reset.
