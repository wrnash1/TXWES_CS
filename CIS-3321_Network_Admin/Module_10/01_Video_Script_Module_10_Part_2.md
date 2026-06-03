# Video Script: Module 10 — Network Services (Part 2 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 14 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

### SLIDE 1 — Welcome to Part 2

Welcome back. In Part 1 we covered DHCP and the foundational DNS concepts — the DORA process, scope configuration, relay agents, and all eight DNS record types. In Part 2 we complete the module with NTP, IPAM, Dynamic DNS, and the integration between these services. We also cover exam strategy for this domain.

These services are interconnected: DHCP assigns addresses and optionally delivers NTP server information. DHCP and DNS integrate through Dynamic DNS so that hostnames resolve correctly as devices move. IPAM centralizes management of all three. Understanding how they work together is as important as understanding each in isolation.

---

### SLIDE 2 — NTP: Network Time Protocol

**NTP (Network Time Protocol)** synchronizes the clocks of all devices on a network to a common time source. NTP uses **UDP port 123**.

Why does accurate time matter?

- **Kerberos authentication**: Kerberos tickets carry timestamps. If a client's clock differs from the domain controller's clock by more than **5 minutes**, the authentication attempt is rejected with a "clock skew too great" error. Workstations cannot log in.
- **Log correlation**: When troubleshooting an incident across ten devices, correlating events from different log sources requires that all devices agree on the time. A 3-second discrepancy on one device causes log entries to appear out of sequence and makes root-cause analysis unreliable.
- **Certificate validation**: TLS certificates have notBefore and notAfter timestamps. A device with a clock set to the wrong year may reject valid certificates or accept expired ones.
- **Digital signatures**: Signed documents, code-signing certificates, and timestamp authorities all depend on accurate system time.
- **Forensic evidence**: In security investigations, timestamp accuracy determines the order of events. Courts have rejected forensic evidence from systems with unsynchronized clocks.

NTP is not a luxury — it is a security and operational requirement.

---

### SLIDE 3 — The NTP Stratum Hierarchy

NTP organizes time sources into a hierarchy called **strata**, numbered 0 through 15. Lower stratum numbers indicate closer proximity to a reference clock and higher accuracy.

**Stratum 0 — Reference clocks**: Stratum 0 devices are not NTP servers — they are the physical time sources. They include GPS receivers, atomic clocks (cesium or rubidium), and CDMA radio signals. Stratum 0 devices connect directly to stratum 1 servers.

**Stratum 1 — Primary time servers**: These are NTP servers with a direct connection to a stratum 0 reference clock. They are considered authoritative and accurate to within microseconds of true time. Stratum 1 servers form the top tier of the public NTP pool.

**Stratum 2 — Secondary time servers**: Synchronize from one or more stratum 1 servers. Accuracy is slightly less but still suitable for enterprise use. These are typically the servers an organization's internal NTP infrastructure synchronizes to.

**Stratum 3 and higher**: Each tier synchronizes from the tier above. Accuracy degrades slightly at each hop. Stratum 15 is the maximum usable value; stratum 16 indicates unsynchronized.

**Enterprise NTP design**: A medium or large organization typically runs internal stratum 2 or stratum 3 servers that synchronize to public stratum 1 servers over the internet. Internal clients synchronize to the internal NTP servers rather than going directly to the internet. This reduces external bandwidth, provides fault isolation, and allows the organization to control NTP configuration centrally.

**Windows domain NTP hierarchy**: In an Active Directory domain, workstations synchronize to the domain controller. Domain controllers synchronize to the PDC Emulator role holder. The PDC Emulator synchronizes to an external stratum 1 or stratum 2 source.

---

### SLIDE 4 — NTP Operation and Security

NTP uses a polling mechanism. Clients send NTP requests to their configured server at regular intervals (default poll interval starts at 64 seconds, increases to up to 1024 seconds as the clock stabilizes). The server responds with its current timestamp, and the client calculates the offset and adjusts its local clock.

**Clock slewing vs. stepping**: If the offset is small (typically under 128 milliseconds), NTP applies a gradual correction called a **slew** — it speeds up or slows the clock slightly until it matches the reference. If the offset is large, NTP performs a **step** — an immediate hard reset of the clock. By default, ntpd will only step the clock once at startup; if the offset is too large during operation, the process exits rather than step the clock (to protect applications that depend on monotonic time).

**NTP security concerns**:

**NTP amplification attack**: An attacker sends forged NTP requests to publicly accessible NTP servers using the victim's IP address as the source. The NTP servers send their (much larger) responses to the victim, overwhelming it with traffic. NTP amplification can achieve amplification factors of up to 4,000:1.

**Countermeasure**: Configure NTP servers to restrict which clients they respond to. Use access control lists to limit NTP responses to known internal networks only. Disable the `monlist` command (a legacy NTP debug command that returns a list of recently queried hosts — it was the primary tool for amplification attacks).

**NTP authentication**: NTPv3 and NTPv4 support MD5-keyed message authentication. Configuring shared keys between NTP clients and servers ensures that clock updates come from trusted sources and prevents man-in-the-middle time manipulation.

---

### SLIDE 5 — IPAM: IP Address Management

**IPAM (IP Address Management)** is the administrative practice — and often the software system — for planning, tracking, and managing IP addresses across an entire network.

Why IPAM matters: In a network with hundreds of subnets and thousands of devices, tracking which IP addresses are assigned, which are reserved, which are available, and which scope they belong to becomes unmanageable with spreadsheets. IPAM provides a centralized database that integrates with DHCP and DNS to give administrators a real-time view of address space utilization.

**IPAM capabilities**:

- Subnet discovery and scanning — IPAM discovers existing subnets and scans for active hosts
- Address space visualization — tree-view of supernets, subnets, and individual addresses
- DHCP scope management — create, modify, and monitor scopes from a single console across multiple DHCP servers
- DNS record management — view and modify DNS zones and records centrally
- Utilization reporting — alerts when a scope exceeds 80% or 90% utilization before exhaustion
- Audit logging — records who changed which address, when, and why
- Role-based access control — different administrators manage different regions of the address space

**IPAM integration with DHCP and DNS**: In Microsoft environments, Windows Server IPAM integrates directly with Windows Server DHCP and DNS. It can manage multiple DHCP servers and DNS servers from a single IPAM console, consolidating address management across the enterprise.

The Network+ exam expects you to understand what IPAM is and why organizations use it — not detailed configuration of specific IPAM products.

---

### SLIDE 6 — Dynamic DNS (DDNS)

**Dynamic DNS (DDNS)** is the mechanism by which DHCP and DNS are integrated — when a DHCP server assigns an IP address to a client, it (or the client itself) automatically creates or updates a DNS A record so the hostname resolves to the newly assigned address.

Without DDNS, DNS records for DHCP clients would quickly become stale. A workstation receives 192.168.1.105 today; DNS has an A record pointing `workstation01.txwes.edu` to that address. Tomorrow, after the lease expires and the workstation receives 192.168.1.112, the old DNS record still points to .105 — which may now belong to a different device. Name resolution breaks.

**How DDNS works in a Microsoft environment**:

1. The client receives a DHCP lease
2. The client sends a DNS Update message to the DNS server requesting that its A record be updated to match its new IP address
3. The DHCP server (optionally, depending on configuration) sends a DNS Update to create or update the PTR record (reverse DNS) for the client
4. The DNS server updates its zone database

**DDNS security concern**: Allowing any client to update DNS records creates an opportunity for rogue devices to poison DNS by registering false records. In Microsoft environments, DNS records created by DDNS are protected using **Secure DDNS** — only the client that created the record (authenticated via Kerberos) can update or delete it. Rogue clients cannot overwrite legitimate records.

---

### SLIDE 7 — DNS Forwarding and Conditional Forwarding

Two DNS configuration patterns appear on the exam and in practice:

**DNS forwarding**: When an internal DNS resolver cannot find an answer in its own zones or cache, it forwards the query to another DNS server rather than performing iterative resolution itself. For example, an internal DNS server that handles `txwes.edu` queries might forward all other queries to 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare) rather than performing root-server lookups.

Benefits: Faster for internet queries (public resolvers have large caches), simpler configuration, reduces external iterative query load.

**Conditional forwarding**: A DNS server is configured to forward queries for specific domains to specific DNS servers, while resolving all other queries normally. This is critical for multi-organization environments:

- A company that merges with a partner organization configures conditional forwarding so that queries for `partner.com` go to the partner's internal DNS server. Internal client A can resolve `server.partner.com` without the partner's DNS being publicly accessible.
- A company's split-brain DNS uses conditional forwarding to ensure internal resolvers handle internal queries while public queries go to public resolvers.

**Split-brain DNS (split-horizon DNS)**: An organization maintains two versions of DNS zone data for the same domain — an internal version with RFC 1918 private addresses, and an external version with public IP addresses. Internal clients querying `mail.txwes.edu` receive the internal private IP (10.10.1.25); external clients querying the same name receive the public IP (54.160.205.12). This architecture hides internal addressing from the public internet while keeping internal name resolution functional.

---

### SLIDE 8 — DNS Redundancy and High Availability

DNS is too critical to run on a single server. DNS zone transfer is the mechanism for replicating zone data between primary and secondary DNS servers.

**Primary DNS server**: Holds the authoritative, read-write copy of the zone database. All record modifications are made here.

**Secondary DNS server**: Holds a read-only copy of the zone, replicated from the primary. It answers queries identically to the primary. Clients that cannot reach the primary automatically query the secondary.

**Zone transfer process**:

- **AXFR (Full Zone Transfer)**: The secondary requests the entire zone. Uses TCP port 53. Typically happens when a secondary first comes online.
- **IXFR (Incremental Zone Transfer)**: The secondary requests only changes since the last transfer, referenced by the serial number in the SOA record. More efficient for large zones.

The **SOA serial number** is critical: every time a record in the zone changes, the primary increments the serial number. The secondary compares its serial number to the primary's during refresh checks. If the primary has a higher serial number, the secondary initiates a zone transfer to get the updated records.

**DNS caching and negative caching**: Resolvers cache positive answers (TTL-based) and negative answers (NXDOMAIN responses). The negative cache TTL is controlled by the **minimum TTL** field in the zone's SOA record. Negative caching prevents repeated queries for nonexistent names from hammering authoritative servers.

---

### SLIDE 9 — Module 10 Exam Strategy

The network services domain tests both conceptual knowledge and scenario application. Here are the patterns that appear most frequently:

**DHCP exam traps**:

Trap 1: The question describes a client with 169.254.x.x — the answer is always DHCP failure, never a static IP misconfiguration unless the question specifies static configuration.

Trap 2: Multi-VLAN DHCP questions test whether you know `ip helper-address` is the solution. If clients on one VLAN cannot get DHCP but another VLAN works fine, the relay agent is misconfigured or missing.

Trap 3: DHCP Snooping questions ask which ports should be trusted. The answer is always the port connected to the legitimate DHCP server and uplink/trunk ports — never access ports to end devices.

**DNS exam traps**:

Trap 1: "Non-authoritative answer" does not mean the data is wrong or expired. It means the data came from cache. This is normal operation.

Trap 2: The question asks which record type does X. Memorize: MX = mail, PTR = reverse lookup (IP to name), CNAME = alias (one hostname to another), TXT = SPF/DKIM/verification, AAAA = IPv6.

Trap 3: Zone transfers use TCP 53, not UDP 53. Standard queries use UDP 53. Know both.

**NTP exam traps**:

Trap 1: "Clock skew too great" always indicates NTP failure affecting Kerberos authentication. The maximum tolerance is 5 minutes (300 seconds).

Trap 2: NTP uses UDP port 123 — not TCP. It is a connectionless protocol.

Trap 3: Stratum 0 is a reference clock, not an NTP server. Stratum 1 is the highest-accuracy NTP server tier.

**IPAM exam traps**:

The exam treats IPAM conceptually. Know what it is (centralized IP address management integrating DHCP and DNS), what problem it solves (address space visibility and management at scale), and that it provides utilization alerts, audit logging, and multi-server management.

---

### SLIDE 10 — Troubleshooting Network Services: Integrated Scenarios

**Scenario 1 — User cannot access any network resources after moving to a new desk:**

Symptoms: Cannot ping anything. IP shows 169.254.x.x. Conclusion: DHCP failure.

Troubleshooting path: (1) Is the client on the correct VLAN? A move may have plugged into a port with a different VLAN assignment. (2) Is there a relay agent configured on the VLAN interface? (3) Is the DHCP scope exhausted? Check the server's lease count. (4) Is the DHCP service running? (5) Are firewall rules blocking UDP 67/68?

**Scenario 2 — Authentication failures "clock skew too great" starting at 6:30 AM:**

Symptoms: Domain logins fail across multiple sites. Error message specifically says clock skew.

Troubleshooting path: (1) Check NTP service status on domain controllers. (2) Check if the PDC Emulator can reach its external NTP source. (3) Check if branch office clocks have drifted. (4) Manually force NTP sync (Windows: `w32tm /resync /force`). (5) Confirm the fix resolved authentication.

Root cause pattern: Branch office VPN connectivity outage → NTP clients could not reach internal NTP servers → clocks drifted during the outage window → Kerberos rejected tickets after 5-minute threshold was exceeded when VPN restored.

**Scenario 3 — Users can reach intranet servers by IP but not by hostname:**

Symptoms: ping 10.10.1.50 succeeds; ping intranet.txwes.edu fails.

Troubleshooting path: (1) Run `nslookup intranet.txwes.edu` — does the resolver respond? (2) If the resolver is unreachable, check if the internal DNS server is down. (3) If the resolver responds but with the wrong address (public IP instead of private IP), check split-brain DNS configuration — the client may be querying the external DNS server instead of the internal one. (4) Check whether the DHCP-delivered DNS server option (Option 6) is pointing to the correct internal resolver.

**Scenario 4 — New devices receive IP addresses but cannot reach the internet:**

Symptoms: `ipconfig` shows 192.168.10.x address, correct subnet mask, but default gateway is 0.0.0.0.

Conclusion: DHCP scope Option 3 (default gateway) is not configured or is configured with the wrong value.

Troubleshooting path: Check the DHCP scope options on the server. Verify Option 3 (router) is set to the correct gateway IP. Force the client to release and renew after correcting the scope.

---

### SLIDE 11 — Part 2 Summary

NTP: Synchronizes device clocks using the stratum hierarchy. Stratum 0 = reference clock (GPS/atomic). Stratum 1 = primary NTP server. UDP port 123. Kerberos fails when clock skew exceeds 5 minutes. NTP amplification attack countermeasure: restrict NTP responses with ACLs.

IPAM: Centralized IP address management integrating DHCP and DNS. Provides utilization reporting, audit logging, multi-server management, and subnet visualization.

Dynamic DNS (DDNS): Automatic DNS record updates when DHCP assigns new addresses. Secure DDNS in Active Directory environments prevents unauthorized record updates.

DNS forwarding: Passes unresolvable queries to an upstream resolver. Conditional forwarding: sends queries for specific domains to specific DNS servers. Split-brain DNS: separate internal and external zone data for the same domain.

DNS zone transfers: AXFR (full, TCP 53) and IXFR (incremental, TCP 53). SOA serial number controls replication.

Exam strategy: 169.254.x.x = DHCP failed. Non-authoritative = cached (not wrong). MX = mail. Clock skew = NTP/Kerberos. NTP = UDP 123. Zone transfers = TCP 53.

This completes Module 10 and the Network Services domain. Module 11 begins the Routing Protocols domain.

---

*End of Part 2 — Module 10 Complete*
