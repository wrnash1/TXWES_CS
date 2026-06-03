# Reading Guide: Module 10 — Network Services

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Network+ (N10-008)

---

### Purpose

This reading guide provides vocabulary, reference tables, and study tools to support your understanding of the network services covered in Module 10: DHCP, DNS, NTP, and IPAM. These services form the operational backbone of every IP network and represent a significant portion of the Network+ exam.

---

### Core Vocabulary

**DHCP (Dynamic Host Configuration Protocol)**: Protocol that automatically assigns IP addresses and network configuration parameters to clients. Uses UDP port 67 (server) and UDP port 68 (client).

**DORA**: Acronym for the four-step DHCP address assignment process: Discover, Offer, Request, Acknowledge.

**DHCP Discover**: First message in the DORA process. Sent as a broadcast from the client (source IP 0.0.0.0) to find available DHCP servers.

**DHCP Offer**: Server response to a Discover, proposing an IP address, subnet mask, gateway, DNS server, and lease duration.

**DHCP Request**: Client broadcast selecting one Offer and notifying all other servers that their offers were declined.

**DHCP Acknowledge (ACK)**: Server confirmation that the client may use the offered parameters. Lease timer starts.

**Lease**: The period of time a DHCP client is authorized to use an assigned IP address.

**T1 timer**: 50% of lease duration. Client sends a unicast renewal request to the original DHCP server.

**T2 timer**: 87.5% of lease duration. Client broadcasts a renewal request to any available DHCP server if T1 renewal failed.

**DHCP scope**: The defined pool of IP addresses and configuration parameters that a DHCP server is authorized to assign for a specific subnet.

**Exclusion**: An IP address or range within the scope that is reserved for static assignment and excluded from dynamic distribution.

**Reservation**: A binding between a specific MAC address and a specific IP address, ensuring the same client always receives the same address via DHCP.

**DHCP option**: Configuration parameters included with a lease. Key options: Option 3 (default gateway), Option 6 (DNS server), Option 15 (domain name), Option 42 (NTP server), Option 66/67 (TFTP/boot file for VoIP and PXE).

**DHCP relay agent**: A router interface configuration that forwards DHCP broadcasts from one subnet to a DHCP server on a different subnet. Configured using `ip helper-address` on Cisco IOS.

**ip helper-address**: Cisco IOS command applied to a router interface to specify the IP address of the DHCP server to which DHCP broadcasts should be unicasted.

**giaddr**: The "gateway IP address" field in a relayed DHCP packet. Contains the relay agent's IP address, which the DHCP server uses to determine which scope to assign from.

**APIPA (Automatic Private IP Addressing)**: The 169.254.0.0/16 range self-assigned by Windows clients when DHCP fails. An APIPA address indicates the client received no DHCP response.

**DHCP scope exhaustion**: Condition where all IP addresses in a DHCP scope are currently leased and no addresses are available for new clients.

**DHCP starvation attack**: An attacker sends DHCP Discovers with spoofed MAC addresses, exhausting the scope. Legitimate clients cannot obtain addresses.

**DHCP Snooping**: A Cisco switch security feature that classifies ports as trusted (connected to legitimate DHCP servers) or untrusted (connected to clients) and drops DHCP Offers from untrusted ports.

**DHCP Snooping binding table**: A table maintained by the switch recording MAC address, IP address, VLAN, port, and lease duration for each active DHCP lease. Used by DAI (Dynamic ARP Inspection) and IP Source Guard.

**DNS (Domain Name System)**: A distributed hierarchical database that translates hostnames to IP addresses. Operates on UDP port 53 (queries) and TCP port 53 (zone transfers, large responses).

**Root zone**: The top of the DNS hierarchy. 13 sets of root name servers managed by various organizations. Knows which servers are authoritative for every TLD.

**TLD (Top-Level Domain)**: .com, .org, .edu, .gov, country codes. TLD servers know which servers are authoritative for each domain under their TLD.

**Authoritative name server**: Holds the actual DNS records for a specific domain and responds with authoritative answers.

**Recursive resolver**: The DNS server queried by client devices (typically provided by ISP or configured as 8.8.8.8/1.1.1.1). Performs iterative queries on behalf of clients and caches results.

**TTL (Time to Live)**: The duration (in seconds) that a DNS record may be cached by resolvers and clients.

**Non-authoritative answer**: A DNS response served from a resolver's cache rather than directly from the authoritative name server. Valid and normal — does not indicate an error.

**A record**: Maps a hostname to an IPv4 address.

**AAAA record**: Maps a hostname to an IPv6 address (quad-A, four times the size of an A record).

**CNAME record**: Creates an alias pointing one hostname to another hostname.

**MX record**: Identifies the mail server(s) responsible for accepting email for a domain. Includes a priority value (lower number = higher priority).

**NS record**: Identifies the authoritative name servers for a domain.

**PTR record**: Reverse DNS record. Maps an IP address to a hostname. Stored in the in-addr.arpa zone.

**TXT record**: Stores arbitrary text. Used for SPF (Sender Policy Framework), DKIM, and domain ownership verification.

**SOA record (Start of Authority)**: Contains administrative metadata for a DNS zone: primary name server, admin email, serial number, and refresh/retry/expire timers. Every zone has exactly one SOA record.

**Zone transfer**: Replication of DNS zone data from a primary to a secondary DNS server. AXFR (full transfer) and IXFR (incremental transfer) both use TCP port 53.

**AXFR**: Full zone transfer — transfers the entire zone database. Used when a secondary first comes online.

**IXFR**: Incremental zone transfer — transfers only records that changed since the secondary's last serial number.

**SOA serial number**: An integer in the SOA record that is incremented each time zone data changes. Secondary servers compare their serial number to the primary's to determine whether a zone transfer is needed.

**Split-brain DNS (split-horizon)**: Maintaining separate internal and external DNS zone data for the same domain. Internal clients receive private IP addresses; external clients receive public IP addresses.

**DNS forwarding**: Configuring a DNS server to pass unresolvable queries to a specific upstream resolver rather than performing iterative resolution itself.

**Conditional forwarding**: Configuring a DNS server to forward queries for specific domains to specific DNS servers while resolving all other queries normally.

**DDNS (Dynamic DNS)**: Automatic creation or update of DNS records when DHCP assigns new IP addresses. Prevents DNS records from becoming stale as device addresses change.

**Secure DDNS**: DDNS implementation using Kerberos authentication to prevent unauthorized clients from updating DNS records they do not own.

**NTP (Network Time Protocol)**: Protocol that synchronizes device clocks across a network. Uses UDP port 123.

**Stratum**: The NTP hierarchy tier. Lower stratum = closer to the reference clock = higher accuracy.

**Stratum 0**: Physical reference clocks (GPS receiver, atomic clock). Not NTP servers — connect directly to stratum 1 servers.

**Stratum 1**: Primary NTP servers with a direct connection to a stratum 0 reference. Highest-accuracy NTP tier.

**Stratum 2**: Secondary NTP servers that synchronize from stratum 1. Suitable for enterprise internal time infrastructure.

**Clock skew**: The difference between a device's local clock and the authoritative time source. Kerberos authentication fails when clock skew exceeds 5 minutes.

**Clock slewing**: A gradual correction NTP applies for small time offsets — speeds up or slows the clock until it matches the reference.

**Clock stepping**: An immediate hard reset of the clock applied when the offset is large.

**NTP amplification attack**: An attacker uses forged NTP requests to cause NTP servers to flood a victim with large responses. Countermeasure: restrict NTP responses using ACLs.

**IPAM (IP Address Management)**: The administrative practice and software systems for planning, tracking, and managing IP address space. Integrates with DHCP and DNS servers to provide centralized visibility and management.

---

### DHCP Options Reference

| Option Number | Parameter Delivered |
|---------------|---------------------|
| Option 1 | Subnet mask |
| Option 3 | Default gateway (router) |
| Option 6 | DNS server IP address(es) |
| Option 15 | Domain name |
| Option 42 | NTP server |
| Option 44 | WINS server (legacy Windows) |
| Option 66 | TFTP server name (VoIP, PXE boot) |
| Option 67 | Boot file name (VoIP, PXE boot) |

---

### DHCP Service Comparison — Lease Duration Trade-offs

| Lease Duration | Appropriate For | Advantage | Disadvantage |
|----------------|-----------------|-----------|--------------|
| Short (1–2 hours) | Guest wireless, conference rooms, high-turnover environments | Addresses reclaimed quickly; accurate utilization | Higher DHCP server load; more frequent renewal traffic |
| Medium (8 hours) | Standard workday offices | Balance of reclamation speed and server load | Addresses tied up for workday even if device leaves |
| Long (24 hours+) | Stable server environments, desktop-only networks | Minimal DHCP traffic; stable addressing | Long reclamation time; scope may exhaust if devices leave without releasing |

---

### DNS Record Type Quick Reference

| Record Type | Maps | Primary Use Case |
|-------------|------|-----------------|
| A | Hostname → IPv4 address | Standard forward lookup |
| AAAA | Hostname → IPv6 address | IPv6 forward lookup |
| CNAME | Hostname → another hostname (alias) | Web/mail aliases, CDN pointing |
| MX | Domain → mail server hostname | Email delivery routing |
| NS | Domain → name server hostname | Zone delegation |
| PTR | IP address → hostname | Reverse DNS lookup |
| TXT | Domain → arbitrary text | SPF, DKIM, domain verification |
| SOA | Zone → administrative metadata | Zone authority, serial, timers |

---

### DNS Port Reference

| Operation | Protocol | Port |
|-----------|----------|------|
| Standard DNS query (under 512 bytes) | UDP | 53 |
| DNS query with large response | TCP | 53 |
| Zone transfer (AXFR/IXFR) | TCP | 53 |

---

### NTP Stratum Hierarchy Reference

| Stratum | Description | Accuracy | Example |
|---------|-------------|----------|---------|
| 0 | Reference clock (not an NTP server) | Microseconds | GPS receiver, cesium atomic clock |
| 1 | Primary NTP server (connected to stratum 0) | ~1 microsecond | time.nist.gov, pool.ntp.org servers |
| 2 | Secondary NTP server (syncs from stratum 1) | ~10 microseconds | Enterprise internal NTP server |
| 3 | Tertiary (syncs from stratum 2) | ~100 microseconds | Branch office NTP relay |
| 15 | Maximum usable stratum | Degraded | Bottom of usable hierarchy |
| 16 | Unsynchronized | N/A | Clock has no valid reference |

---

### Key Protocol Ports — Module 10

| Protocol | Port | Transport |
|----------|------|-----------|
| DHCP Server | 67 | UDP |
| DHCP Client | 68 | UDP |
| DNS (queries) | 53 | UDP |
| DNS (zone transfers) | 53 | TCP |
| NTP | 123 | UDP |

---

### DHCP Troubleshooting Reference

| Symptom | Most Likely Cause | Diagnostic/Fix |
|---------|------------------|----------------|
| Client shows 169.254.x.x | DHCP server unreachable | Check server status, relay agent, scope exhaustion |
| Client on different subnet cannot get address | Missing or wrong `ip helper-address` | Configure relay agent on router interface |
| All addresses in use, new clients fail | Scope exhaustion | Expand scope range or shorten lease duration |
| Clients get wrong gateway or DNS | Scope options misconfigured | Check Options 3 and 6 in scope configuration |
| Rogue DHCP server assigning addresses | No DHCP Snooping | Enable DHCP Snooping; configure trusted ports |

---

### Exam Tips

1. APIPA (169.254.x.x) is the definitive indicator that DHCP failed. Every question describing this IP range is asking about DHCP failure — not static IP misconfiguration.

2. DHCP uses broadcasts for Discover and Request. Routers do not forward broadcasts by default. `ip helper-address` is the only solution for multi-subnet DHCP without a local DHCP server on every subnet.

3. A non-authoritative DNS answer is normal and correct. It means the resolver answered from cache. It does not indicate an error or stale data (until TTL expires).

4. DNS record type association — memorize by use case: email routing = MX, IPv6 = AAAA, alias = CNAME, reverse lookup = PTR, SPF = TXT.

5. Zone transfers always use TCP port 53, not UDP. Standard queries use UDP. Both use port 53.

6. NTP clock skew exceeding 5 minutes causes Kerberos authentication to fail. The error message will say "clock skew too great" or "there are no logon servers available." The fix is NTP, not DNS or DHCP.

7. NTP stratum 0 is a reference clock, not an NTP server. Stratum 1 is the highest tier of NTP servers. Stratum 16 means unsynchronized.

8. DHCP Snooping trusted ports: only the port connected to the legitimate DHCP server and uplink/trunk ports should be trusted. All access ports to end devices must be untrusted.

9. For the DORA sequence: the Request message is broadcast (not unicast) because it notifies ALL servers that made Offers which Offer was selected, allowing non-selected servers to reclaim their proposed addresses.

10. IPAM questions on the exam are conceptual: know that IPAM integrates DHCP + DNS management, provides utilization visibility, generates alerts before scope exhaustion, and maintains audit logs.

---

### Study Checklist

Work through this checklist before the quiz:

- [ ] Can you describe all four steps of DORA and explain why each step uses broadcast or unicast?
- [ ] Can you explain T1 and T2 lease renewal timers and what happens if both fail?
- [ ] Can you explain what an exclusion is vs. a reservation and when to use each?
- [ ] Can you name at least five DHCP options and their numbers?
- [ ] Can you explain what `ip helper-address` does and why it is needed?
- [ ] Can you identify what 169.254.x.x means and what caused it?
- [ ] Can you explain DHCP Snooping trusted vs. untrusted ports?
- [ ] Can you trace the full DNS resolution path from client to authoritative server?
- [ ] Can you list all eight DNS record types with their purpose?
- [ ] Can you explain the difference between authoritative and non-authoritative DNS answers?
- [ ] Can you explain DNS zone transfers and which use TCP vs. UDP?
- [ ] Can you describe split-brain DNS and why it is used?
- [ ] Can you explain NTP stratum levels 0, 1, and 2?
- [ ] Can you state the Kerberos clock skew tolerance and which protocol enforces it?
- [ ] Can you describe what IPAM does and what problem it solves?
- [ ] Can you identify what Dynamic DNS is and why it is needed?
- [ ] Can you state the port numbers for DHCP, DNS (UDP and TCP), and NTP?

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
