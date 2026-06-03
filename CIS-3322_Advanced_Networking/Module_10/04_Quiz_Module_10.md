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
