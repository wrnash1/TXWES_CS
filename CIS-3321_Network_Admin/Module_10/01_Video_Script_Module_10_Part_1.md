# Video Script: Module 10 — Network Services (Part 1 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

### SLIDE 1 — Welcome and Overview

Welcome back to CIS-3321 Network Administration. I'm Professor Nash. Module 10 covers Network Services — the background infrastructure that every IP network depends on: DHCP for address assignment, DNS for name resolution, NTP for time synchronization, and IPAM for centralized address management.

These services run silently behind the scenes. When they work, users never think about them. When they fail, nothing works — users cannot get IP addresses, cannot reach websites by name, authentication systems fail, and log entries become impossible to correlate. Understanding how each service works, how to configure it, and how to troubleshoot it is fundamental to network administration.

In Part 1, we cover DHCP in depth — the DORA process, scope configuration, options, reservations, and the relay agent. In Part 2, we cover DNS record types, the resolution hierarchy, NTP, and IPAM.

---

### SLIDE 2 — DHCP: What It Does and Why It Matters

**DHCP (Dynamic Host Configuration Protocol)** automates the assignment of IP addresses and network configuration parameters to clients when they connect to a network.

Without DHCP, every device on the network would require a manually configured static IP address, subnet mask, default gateway, and DNS server. For a network with 500 devices, that is 500 manual configurations — each one a potential typo that creates a duplicate IP address conflict or misconfigured gateway.

DHCP solves this by centralizing address management and automating delivery to clients on demand.

What DHCP delivers to each client:

- IP address
- Subnet mask
- Default gateway
- DNS server IP address(es)
- Lease duration
- Optional: domain name, NTP server, TFTP server (for IP phones and network devices), WINS server

DHCP uses UDP port 67 on the server side and UDP port 68 on the client side. All initial DHCP communication uses broadcasts because the client has no IP address yet.

---

### SLIDE 3 — The DORA Process

The DHCP address assignment process follows four steps, remembered by the acronym **DORA**:

**D — DHCP Discover**: The client broadcasts a DHCP Discover message to destination IP 255.255.255.255 (limited broadcast) and destination MAC ff:ff:ff:ff:ff:ff. The source IP is 0.0.0.0 because the client has no address yet. The message says: "I need an IP address — is there a DHCP server available?"

**O — DHCP Offer**: One or more DHCP servers on the network receive the Discover and respond with a DHCP Offer. The Offer includes a proposed IP address, subnet mask, gateway, DNS server, and lease duration. If multiple DHCP servers respond, the client receives multiple Offers.

**R — DHCP Request**: The client selects one of the Offers (typically the first one received) and broadcasts a DHCP Request message. The Request broadcasts rather than unicasts for an important reason: it notifies ALL servers that made an Offer. Servers whose Offers were not selected see the Request and know to reclaim their proposed address.

**A — DHCP Acknowledge**: The selected DHCP server sends a DHCP Acknowledge (ACK) to the client, confirming the lease. The client configures its network interface with the delivered parameters and begins using the assigned IP address.

This entire four-message exchange completes in under a second on a healthy network.

---

### SLIDE 4 — DHCP Lease Renewal

A DHCP lease is not permanent — it expires after the configured lease duration. Before expiration, the client attempts renewal:

**T1 (50% of lease duration)**: The client sends a unicast DHCP Request directly to the server that issued the lease. This is a renewal attempt — it does not go through the full DORA sequence. If the server acknowledges, the lease timer resets.

**T2 (87.5% of lease duration)**: If the T1 renewal failed (the original server was unreachable), the client broadcasts a DHCP Request to any available DHCP server. Any server can extend the lease at this point.

**Lease expiration**: If T2 also fails, the client must release its IP address and begin the full DORA process again from scratch. During this process the client has no IP address and cannot communicate on the network.

Practical implications:

- Short lease times (1–2 hours): More frequent renewals — appropriate for guest wireless networks where clients come and go frequently. Higher DHCP server load.
- Long lease times (8–24 hours): Fewer renewals — appropriate for stable desktop environments. If devices leave the network permanently, addresses are not reclaimed until lease expiration.

---

### SLIDE 5 — DHCP Scope Configuration

A **DHCP scope** is the pool of IP addresses and configuration parameters that the DHCP server is authorized to assign to a specific subnet.

Key scope components:

**Address pool (range)**: The range of IP addresses the server can assign. Example: 192.168.1.100 through 192.168.1.200.

**Exclusions**: Specific addresses within the pool range that are excluded from dynamic assignment. Use exclusions for devices with static IP addresses — routers, servers, printers, managed switches — that fall within the scope range. Example: exclude 192.168.1.100–192.168.1.110 for static-assigned infrastructure devices.

**Reservations**: A reservation binds a specific IP address to a specific client MAC address. The client always receives the same IP address from DHCP. This combines the convenience of DHCP (client still uses DHCP, no manual static configuration required on the device) with the predictability of a static address. Common use: IP printers, VOIP phones, servers that benefit from consistency but whose administrators prefer not to configure static IPs on the device itself.

**DHCP options**: Configuration parameters delivered with the lease:

- Option 3: Default gateway (router)
- Option 6: DNS server
- Option 15: Domain name
- Option 42: NTP server
- Option 66/67: TFTP server and boot file (for VoIP phones, PXE boot)

---

### SLIDE 6 — DHCP Relay Agent

A critical design constraint of DHCP: the initial Discover and Request messages are broadcasts. **Routers do not forward broadcasts between subnets by default.** This means if the DHCP server is on a different subnet than the client, the DHCP Discover never reaches the server.

The solution is a **DHCP relay agent** (also called a BOOTP relay or IP helper).

A DHCP relay agent is a configuration on the router interface closest to the clients. When the router interface receives a DHCP broadcast, the relay agent intercepts it and forwards it as a unicast to the DHCP server's IP address. The DHCP server sees the relay agent's IP address as the source, which it uses to determine which scope to assign from (the scope that matches the relay agent's subnet). The server sends its reply back to the relay agent, which forwards it to the client.

Cisco IOS relay agent configuration:

```text
interface GigabitEthernet0/0
 ip helper-address 10.0.0.5
```

This single command on the client-facing interface causes the router to relay all DHCP broadcasts from that subnet to the DHCP server at 10.0.0.5.

Without a relay agent, every subnet in the enterprise would need its own local DHCP server. With relay agents, a single centralized DHCP server can serve all subnets across the entire enterprise.

---

### SLIDE 7 — DHCP Troubleshooting

Several DHCP failure scenarios appear on the exam and in practice:

**APIPA address (169.254.x.x)**: When a Windows client sends a DHCP Discover but receives no Offer after a timeout period, it self-assigns an APIPA (Automatic Private IP Addressing) address in the 169.254.0.0/16 range. The client can only communicate with other hosts on the same APIPA range — it has no default gateway and cannot reach the internet or cross-subnet resources. Seeing 169.254.x.x is the definitive indicator that DHCP failed.

Common DHCP failure causes:

- DHCP server is down or unreachable
- The relay agent (ip helper-address) is not configured or configured with the wrong server IP
- The DHCP scope is exhausted — all addresses in the pool are leased and no addresses are available for new clients
- The DHCP service is stopped on the server
- Firewall rules blocking UDP 67/68

**DHCP scope exhaustion**: Check the server's lease table for the number of active leases vs. total scope addresses. If the scope is full, either expand the scope or shorten lease durations to reclaim expired leases faster.

**DHCP starvation attack**: An attacker sends large numbers of DHCP Discovers with spoofed source MAC addresses, each requesting a new IP address, exhausting the DHCP scope. Legitimate clients cannot obtain addresses. Countermeasure: DHCP Snooping on managed switches — validates DHCP messages and limits the rate of Discovers per port.

---

### SLIDE 8 — DHCP Snooping

**DHCP Snooping** is a Cisco switch security feature that protects the network from rogue DHCP servers and DHCP starvation attacks.

How DHCP Snooping works:

Switch ports are classified as:

- **Trusted ports**: Connected to legitimate DHCP servers or uplink trunk ports to the distribution layer where the DHCP server resides. DHCP Offers and Acknowledges are permitted on trusted ports.
- **Untrusted ports**: All access ports connected to client devices. DHCP Offers from untrusted ports are dropped — a client device should never be sending DHCP Offers. Only DHCP Discovers and Requests are permitted from untrusted ports.

The **DHCP Snooping binding table**: As legitimate DHCP leases are assigned, the switch records each binding: MAC address, IP address, VLAN, port, and lease duration. This binding table is also used by Dynamic ARP Inspection (DAI) to validate ARP packets.

Benefits:

1. Prevents rogue DHCP servers (sending Offers from untrusted ports is blocked)
2. Prevents DHCP starvation (rate-limits Discovers per untrusted port)
3. Creates the binding table used by DAI and IP Source Guard

DHCP Snooping is enabled per-VLAN:

```text
ip dhcp snooping
ip dhcp snooping vlan 10,20
interface GigabitEthernet0/1
 ip dhcp snooping trust
```

---

### SLIDE 9 — DNS: The Domain Name System

**DNS (Domain Name System)** is the distributed hierarchical database that translates human-readable hostnames into IP addresses. Without DNS, users would need to memorize IP addresses for every resource they access.

DNS operates on UDP port 53 for standard queries (up to 512 bytes). Responses exceeding 512 bytes, and zone transfers between DNS servers, use TCP port 53.

DNS hierarchy:

- **Root zone (.)**: 13 sets of root name servers managed by various organizations worldwide. They know which servers are authoritative for every top-level domain.
- **Top-Level Domain (TLD)**: .com, .org, .edu, .gov, country codes (.us, .uk). TLD servers know which servers are authoritative for each domain under their TLD.
- **Authoritative name server**: Holds the actual DNS records for a specific domain. For example, the authoritative name servers for txwes.edu know the IP address of every host in that domain.
- **Recursive resolver** (also called a caching resolver): The DNS server your device queries — typically provided by your ISP or configured as a public resolver like 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare). The resolver does the iterative work of querying root → TLD → authoritative on behalf of clients.

DNS TTL (Time to Live): Each DNS record has a TTL value specifying how long resolvers and clients may cache the record. Short TTL (60 seconds) means changes propagate quickly. Long TTL (86400 seconds = 24 hours) reduces query load but delays propagation of changes.

---

### SLIDE 10 — DNS Resolution Process

Let's walk through exactly what happens when your browser navigates to txwes.edu:

1. The browser checks its local DNS cache — is txwes.edu already cached from a recent lookup? If yes, skip to step 8.

2. The OS checks its hosts file (/etc/hosts on Linux/macOS, C:\Windows\System32\drivers\etc\hosts on Windows) — is there a local override entry? If yes, use that entry.

3. The OS sends a recursive DNS query to the configured resolver (for example, 8.8.8.8).

4. The resolver checks its own cache. If the answer is cached and the TTL has not expired, it returns the cached answer immediately (non-authoritative answer).

5. If not cached, the resolver sends an iterative query to a root name server: "Who is authoritative for .edu?"

6. The root server responds with the addresses of the .edu TLD servers.

7. The resolver queries the .edu TLD server: "Who is authoritative for txwes.edu?" The TLD server responds with the addresses of txwes.edu's authoritative name servers.

8. The resolver queries txwes.edu's authoritative name server: "What is the IP address of txwes.edu?" The authoritative server returns the A record.

9. The resolver caches the result (respecting the TTL) and returns it to the client.

10. The client's OS caches the result and passes the IP address to the browser.

The entire process typically completes in 50–200 milliseconds. Subsequent lookups for the same name return cached results instantly.

---

### SLIDE 11 — DNS Record Types

DNS stores different types of records for different purposes. These record types are directly and frequently tested on the Network+ exam:

**A record**: Maps a hostname to an IPv4 address. The most fundamental record type.
Example: `www.txwes.edu → 54.160.205.12`

**AAAA record**: Maps a hostname to an IPv6 address (four times the size of an A record — hence "quad A").
Example: `www.txwes.edu → 2600:1f18:4b:1e00::1`

**CNAME (Canonical Name)**: Creates an alias pointing one hostname to another. The resolver follows the CNAME chain until it reaches an A or AAAA record.
Example: `mail.txwes.edu → CNAME → txwes-edu.mail.protection.outlook.com`

**MX (Mail Exchanger)**: Identifies the mail server responsible for accepting email for a domain. Includes a priority value — lower number means higher priority (tried first).
Example: `txwes.edu MX 10 mail.txwes.edu`

**NS (Name Server)**: Identifies the authoritative name servers for a domain.
Example: `txwes.edu NS ns1.txwes.edu`

**PTR (Pointer)**: Reverse DNS lookup — maps an IP address to a hostname. Stored in the in-addr.arpa zone.
Example: `12.205.160.54.in-addr.arpa → www.txwes.edu`

**TXT (Text)**: Stores arbitrary text. Used for SPF (Sender Policy Framework — specifies which mail servers may send email for a domain), DKIM (email signing), and domain ownership verification.
Example: `txwes.edu TXT "v=spf1 include:_spf.google.com ~all"`

**SOA (Start of Authority)**: Administrative metadata for the zone — primary name server, admin email, serial number, and refresh/retry timers. Every zone has exactly one SOA record.

---

### SLIDE 12 — Part 1 Summary

Let's review Part 1:

DHCP: Automates IP address assignment. DORA sequence: Discover (broadcast) → Offer (server proposes) → Request (client selects, broadcasts) → Acknowledge (server confirms). UDP ports 67 (server) and 68 (client).

DHCP scope: Address pool, exclusions for static devices, reservations for MAC-bound assignments, options for gateway/DNS/NTP.

DHCP relay agent: `ip helper-address` on router interface allows broadcasts to cross subnet boundaries to a centralized DHCP server.

APIPA (169.254.x.x): The definitive sign that DHCP failed.

DHCP Snooping: Trusted vs. untrusted ports; blocks rogue DHCP servers and starvation attacks; creates binding table.

DNS: Hierarchical distributed database. Root → TLD → Authoritative → Recursive resolver. UDP 53, TCP 53 for zone transfers.

DNS record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), NS (name server), PTR (reverse), TXT (SPF/DKIM), SOA (zone authority).

In Part 2: NTP, IPAM, and DNS/DHCP integration — plus exam strategy for these services.

---

*End of Part 1 — Continue to Part 2*
