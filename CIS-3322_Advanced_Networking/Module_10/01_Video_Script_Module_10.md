# Video Script: Module 10 — NAT and PAT

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Cisco CCNA 200-301

---

## Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash. Module 10 covers Network Address Translation and Port Address Translation — two mechanisms that have fundamentally shaped how the internet works with private IPv4 addressing.

[SHOW SLIDE: "Module 10 — NAT and PAT"]

Without NAT, every device on a corporate network would need a globally routable public IP address. IPv4 address exhaustion made that impossible long ago. NAT allows thousands of internal hosts to share one or a small pool of public IP addresses when accessing the internet.

By the end of this module you will be able to:

- Explain the difference between static NAT, dynamic NAT, and PAT

- Configure and verify all three NAT types on a Cisco IOS router

- Understand inside local, inside global, outside local, and outside global address terminology

- Configure NAT64 for IPv6-to-IPv4 translation

- Troubleshoot common NAT failures using IOS verification commands

[PAUSE — 3 seconds]

Let's start with the address translation concepts.

---

## Section 1: NAT Address Terminology (1:30–4:00)

[SHOW SLIDE: "NAT Address Types — Four Terms"]

Before configuring NAT you must understand four address terms. These appear on the CCNA exam in output interpretation questions.

**Inside local**: the private IP address assigned to an internal host as seen from inside the network. Example: 192.168.1.10.

**Inside global**: the public IP address that represents the internal host as seen from outside the network (the internet). Example: 203.0.113.5.

**Outside global**: the public IP address of the external destination server as seen from outside. Example: 8.8.8.8.

**Outside local**: the IP address of an external destination as seen from inside the network. In most deployments this equals the outside global.

[SHOW TOPOLOGY: Internal host 192.168.1.10 → R1 NAT router → Internet → Server 8.8.8.8]

When an internal host at 192.168.1.10 sends a packet to 8.8.8.8, the NAT router translates the source. The packet leaves R1 with source 203.0.113.5 (inside global). The reply comes back to 203.0.113.5 and R1 translates it back to 192.168.1.10 before forwarding it to the host.

[PAUSE — 3 seconds]

Understanding these four terms is essential for reading `show ip nat translations` output.

---

## Section 2: Static NAT (4:00–7:00)

[SHOW SLIDE: "Static NAT — One-to-One Permanent Mapping"]

Static NAT creates a permanent one-to-one mapping between one inside local address and one inside global address. It is used when an internal server must always be reachable from the internet at a specific public IP address — for example, a web server or mail server.

Configuration requires three steps:

**Step 1: Define the static translation mapping.**

```text
Router(config)# ip nat inside source static 192.168.1.100 203.0.113.10
```

This tells the router: whenever you see traffic from inside source 192.168.1.100, translate it to 203.0.113.10. And whenever traffic arrives destined for 203.0.113.10, translate it to 192.168.1.100.

**Step 2: Mark the inside interface.**

```text
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip nat inside
```

**Step 3: Mark the outside interface.**

```text
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip nat outside
```

[SHOW SLIDE: "Static NAT — Use Cases"]

Static NAT is bidirectional by design. Internet users can initiate connections to the inside global address and the router forwards them to the internal server. This makes static NAT appropriate for hosting public-facing services on internal infrastructure.

---

## Section 3: Dynamic NAT (7:00–10:00)

[SHOW SLIDE: "Dynamic NAT — Pool of Public Addresses"]

Dynamic NAT translates internal addresses to a pool of public addresses on a first-come, first-served basis. When an internal host initiates a connection, the router picks an available address from the pool and creates a temporary translation. When the connection ends, the address returns to the pool for reuse.

Configuration steps:

**Step 1: Define the pool of public addresses.**

```text
Router(config)# ip nat pool PUBLIC_POOL 203.0.113.20 203.0.113.30
  netmask 255.255.255.0
```

**Step 2: Create an ACL to identify inside hosts that should be translated.**

```text
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
```

**Step 3: Link the ACL to the pool.**

```text
Router(config)# ip nat inside source list 1 pool PUBLIC_POOL
```

**Step 4: Mark inside and outside interfaces** (same as static NAT).

[SHOW SLIDE: "Dynamic NAT Limitation"]

Dynamic NAT has a critical limitation: if all addresses in the pool are in use, additional inside hosts cannot get translated and their connections are dropped. Dynamic NAT is rarely used in enterprise environments today because PAT achieves much better address utilization.

---

## Section 4: PAT — Port Address Translation (10:00–14:00)

[SHOW SLIDE: "PAT — Many-to-One Translation Using Port Numbers"]

PAT, also called NAT overload, translates multiple inside addresses to a single outside IP address by using unique source port numbers to distinguish connections. This is how virtually every home router and most enterprise routers work today.

When 100 internal hosts all send traffic through a PAT router using a single public IP, the router tracks each connection by creating a unique combination of the public IP plus a translated source port. Reply traffic comes back to the public IP with a specific port number, and the router knows exactly which internal host to forward it to.

**PAT using an interface address:**

```text
Router(config)# access-list 1 permit 192.168.0.0 0.0.255.255
Router(config)# ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

The keyword `overload` enables PAT. Using `interface` instead of a pool means the router uses whatever IP address is currently assigned to that interface as the public translation address.

**PAT using a pool:**

```text
Router(config)# ip nat pool PAT_POOL 203.0.113.1 203.0.113.1 netmask 255.255.255.0
Router(config)# ip nat inside source list 1 pool PAT_POOL overload
```

[SHOW SLIDE: "PAT Port Tracking Table"]

The PAT translation table entry looks like this:

```text
Pro Inside global        Inside local         Outside local        Outside global
tcp 203.0.113.1:1024     192.168.1.10:55321   8.8.8.8:443          8.8.8.8:443
tcp 203.0.113.1:1025     192.168.1.20:49812   8.8.8.8:443          8.8.8.8:443
```

Both internal hosts appear as the same public IP but with different source ports. The router uses those port numbers to sort return traffic back to the correct host.

[PAUSE — 3 seconds]

PAT supports approximately 65,000 simultaneous connections per public IP address based on the TCP/UDP port range. One public IP address can support a large enterprise.

---

## Section 5: NAT64 (14:00–16:00)

[SHOW SLIDE: "NAT64 — IPv6 to IPv4 Translation"]

NAT64 allows IPv6-only hosts to communicate with IPv4 destinations. As organizations migrate to IPv6, they need a mechanism to reach IPv4-only internet services. NAT64 provides that bridge.

A NAT64-capable router translates IPv6 packets from internal IPv6 hosts into IPv4 packets before forwarding them to IPv4 destinations. The router maintains a translation state similar to PAT.

The CCNA tests NAT64 at the conceptual level. You need to understand:

- NAT64 translates between IPv6 and IPv4

- It is used during IPv6 transition when IPv6 hosts must reach IPv4-only services

- A companion protocol called DNS64 synthesizes AAAA records for IPv4 hosts so that IPv6 clients can resolve them

The Cisco IOS command to enable NAT64 starts with:

```text
Router(config)# nat64 enable
```

However, full NAT64 configuration syntax is beyond CCNA scope. Know the concept and purpose.

---

## Section 6: NAT Verification Commands (16:00–18:30)

[SHOW SLIDE: "NAT Verification — Key Commands"]

The primary NAT verification commands are:

```text
Router# show ip nat translations
Router# show ip nat translations verbose
Router# show ip nat statistics
Router# debug ip nat
```

`show ip nat translations` displays the current translation table. Each entry shows the protocol, inside global, inside local, outside local, and outside global addresses and port numbers.

`show ip nat statistics` shows totals for translations created, expired, and failed. It also shows which interfaces are marked inside and outside.

Sample output from `show ip nat statistics`:

```text
Total active translations: 47 (1 static, 46 dynamic; 46 extended)
Outside interfaces: GigabitEthernet0/1
Inside interfaces: GigabitEthernet0/0
Hits: 12345  Misses: 0
```

`debug ip nat` shows real-time translation events. Be careful — on high-traffic routers this can generate thousands of lines per second. Use it in lab environments or during controlled maintenance windows.

---

## Section 7: NAT Troubleshooting (18:30–21:30)

[SHOW SLIDE: "NAT Troubleshooting — Common Failures"]

The most common NAT configuration mistakes are:

**Missing inside or outside interface designation.** If you configure the translation rule but forget to apply `ip nat inside` and `ip nat outside` to interfaces, NAT never triggers. Check with `show ip nat statistics` — it shows which interfaces are marked.

**ACL not matching the correct addresses.** If the ACL in the `ip nat inside source list` command does not match the source addresses of your internal hosts, those hosts are not translated. Use `show access-lists` to verify hit counts.

**Routing after NAT.** After translation, the packet with the public source address must be routable to the internet. If there is no default route pointing toward the internet, translated packets are dropped.

**Pool exhaustion with dynamic NAT.** If all pool addresses are in use, new translations fail silently. Monitor with `show ip nat statistics` and look for translation failure counters.

[SHOW SLIDE: "NAT Troubleshooting Commands Summary"]

```text
Router# show ip nat translations
Router# show ip nat statistics
Router# show ip interface GigabitEthernet0/0
Router# show access-lists 1
Router# clear ip nat translation *
```

`clear ip nat translation *` removes all dynamic NAT translations. Use this during troubleshooting to force re-establishment of translations and confirm the configuration works correctly.

[PAUSE — 3 seconds]

---

## Conclusion (21:30–23:00)

[SHOW SLIDE: "Module 10 Summary"]

Let's wrap up Module 10. Today you learned:

- Static NAT creates permanent one-to-one mappings for hosting internal servers

- Dynamic NAT maps internal hosts to a pool of public addresses — limited by pool size

- PAT (overload) allows thousands of internal hosts to share one public IP using port numbers

- The four NAT address terms: inside local, inside global, outside local, outside global

- NAT64 bridges IPv6 hosts to IPv4 destinations during transition

- Verify NAT with `show ip nat translations` and `show ip nat statistics`

[SHOW SLIDE: "CCNA Exam Focus Areas"]

For the CCNA exam: know how to read `show ip nat translations` output, identify PAT configuration by the `overload` keyword, and distinguish the four address types. These appear frequently in scenario and output interpretation questions.

Your lab this module has you configure static NAT, PAT, and verify the translation table. The reading guide includes a complete command reference and troubleshooting checklist.

[PAUSE — 3 seconds]

See you in Module 11 where we cover DHCP and DNS. Take care.

---

*End of Module 10 Video Script*
