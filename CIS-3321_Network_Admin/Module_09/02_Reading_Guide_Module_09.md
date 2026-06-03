# Reading Guide: Module 09 — Network Services: DNS, DHCP, and NTP

## Course: CIS-3321 Network Administration

Certification Alignment: CompTIA Network+ (N10-008)

---

### Introduction

Module 09 covers three foundational network services that every host depends on: DNS (name resolution), DHCP (automatic IP address assignment), and NTP (time synchronization). These services are individually invisible when working and catastrophic when broken. Together, they underpin authentication, connectivity, and nearly every higher-layer application. DNS, DHCP, and NTP topics appear in Domain 1 (Networking Concepts), Domain 2 (Network Implementation), and Domain 5 (Network Troubleshooting) of the CompTIA Network+ N10-008 exam.

---

### 1. Core Vocabulary

DNS (Domain Name System) — The distributed hierarchical system that translates human-readable hostnames (`www.example.com`) into IP addresses (`93.184.216.34`) and back.

DNS resolver — A client-side or recursive-server component that performs DNS queries on behalf of end-user applications. Also called a recursive resolver or caching name server.

Authoritative name server — The DNS server that holds the official DNS zone records for a domain. It is the final source of truth for that domain's records.

Root name server — Thirteen logical name server clusters at the top of the DNS hierarchy. They respond to queries for the root zone and refer resolvers to the correct TLD name server. Operated by IANA.

TLD name server — Name servers responsible for a top-level domain such as .com, .org, .edu, or .net. They refer resolvers to the authoritative name server for the specific domain.

Zone — A portion of the DNS namespace managed by a specific authoritative name server. A zone contains resource records for a domain and its subdomains.

Forward lookup zone — Resolves hostnames to IP addresses (the most common direction).

Reverse lookup zone — Resolves IP addresses back to hostnames. Uses the in-addr.arpa domain. Requires PTR records.

Resource record (RR) — An entry in a DNS zone. Each record has a name, type, class, TTL, and data field.

TTL (Time to Live) — The number of seconds a DNS response can be cached by a resolver before it must be re-queried. Lower TTL = more frequent re-queries. Higher TTL = less DNS traffic but slower propagation of changes.

Non-authoritative answer — A DNS response served from a resolver's cache rather than directly from the authoritative name server. This is normal behavior and does not indicate incorrect data.

NXDOMAIN — The DNS response code returned when a queried hostname does not exist in DNS. Distinct from a server error.

Recursive query — A DNS query in which the client asks the resolver to perform the full resolution process and return a complete answer.

Iterative query — A DNS query in which the server returns either the answer or a referral to another server. The querying resolver follows each referral itself.

DHCP (Dynamic Host Configuration Protocol) — A protocol that automatically assigns IP addresses and network configuration parameters (subnet mask, default gateway, DNS server, lease time) to clients. Operates over UDP ports 67 (server) and 68 (client).

DORA — The four-message DHCP exchange: Discover (client broadcasts), Offer (server responds with proposed address), Request (client accepts the offer), Acknowledgment (server confirms the assignment).

DHCP lease — The time period during which a client is permitted to use the assigned IP address. After 50% of the lease expires, the client attempts to renew with the same server.

DHCP scope — A defined range of IP addresses a DHCP server can assign to clients on a specific subnet.

DHCP reservation — A static DHCP assignment that maps a specific client MAC address to a specific IP address, ensuring the client always receives the same address via DHCP.

DHCP relay agent (ip helper-address) — A router configuration that forwards DHCP broadcast messages across subnet boundaries to a DHCP server on a different subnet.

APIPA (Automatic Private IP Addressing) — Windows feature that assigns a self-configured address in the 169.254.0.0/16 range when no DHCP server is reachable. APIPA hosts cannot communicate outside the local link.

DHCP snooping — A Layer 2 switch security feature that filters DHCP messages on untrusted ports, blocking rogue DHCP server responses from unauthorized devices.

NTP (Network Time Protocol) — The protocol used to synchronize clocks across network devices. Uses UDP port 123.

Stratum — A measure of an NTP source's accuracy and distance from a reference clock. Stratum 0 = atomic/GPS reference (not on network). Stratum 1 = primary server directly connected to stratum 0. Stratum 2 = synchronized to stratum 1. Each hop adds one to the stratum number.

Clock skew — The difference between a client's current clock and the correct time as reported by an NTP server.

Kerberos — The authentication protocol used by Active Directory Windows domains. Requires all participants to have synchronized clocks. Authentication fails if clock skew exceeds 5 minutes (default maximum tolerance).

Static NAT — A permanent one-to-one mapping between a private IP address and a specific public IP address. Used for servers that must be reachable at a consistent public address.

Dynamic NAT — A many-to-many NAT configuration in which internal hosts are assigned public IPs from a pool when they initiate connections. The assigned public IP changes each session.

PAT (Port Address Translation) — Also called NAT Overload. Many internal hosts share a single public IP address, differentiated by unique source port numbers. The standard deployment method for outbound internet access.

IPAM (IP Address Management) — Software or systems used to track, manage, and audit IP address allocation across a network. Often integrates with DHCP and DNS.

DDNS (Dynamic DNS) — A service that automatically updates DNS A records when a host's IP address changes. Used when DHCP assigns addresses dynamically but DNS must remain current.

---

### 2. DNS Record Types

| Record Type | Full Name | Purpose | Example |
|-------------|-----------|---------|---------|
| A | Address | Maps hostname to IPv4 address | `www.example.com` → `93.184.216.34` |
| AAAA | IPv6 Address | Maps hostname to IPv6 address | `www.example.com` → `2606:2800::/32` |
| CNAME | Canonical Name | Creates an alias to another hostname | `ftp.example.com` → `www.example.com` |
| MX | Mail Exchanger | Identifies mail server for a domain; includes priority value | `example.com` MX 10 `mail.example.com` |
| NS | Name Server | Identifies authoritative name servers for a zone | `example.com` NS `ns1.example.com` |
| PTR | Pointer | Reverse lookup: maps IP to hostname | `34.216.184.93.in-addr.arpa` → `www.example.com` |
| TXT | Text | Stores arbitrary text; used for SPF, DKIM, DMARC | `v=spf1 include:example.com ~all` |
| SOA | Start of Authority | Zone metadata: primary NS, admin email, serial, refresh/retry/expire timers | One per zone |

---

### 3. DNS Resolution Hierarchy

When a resolver has no cached answer, it follows this path:

Step 1 — Client queries the local recursive resolver (configured by DHCP or manually).

Step 2 — Resolver queries a root name server for the TLD (.com, .org, etc.). Root server returns a referral to the correct TLD name server.

Step 3 — Resolver queries the TLD name server (e.g., .com). TLD server returns a referral to the domain's authoritative name server.

Step 4 — Resolver queries the authoritative name server for the domain (e.g., example.com). Authoritative server returns the final answer.

Step 5 — Resolver caches the response (per TTL) and returns the answer to the client.

Step 6 — Client receives the IP address and initiates a connection.

---

### 4. DHCP DORA Process

| Message | Sender | Destination | Content |
|---------|--------|-------------|---------|
| Discover | Client | 255.255.255.255 (broadcast) | "I need an IP address" — no source IP yet |
| Offer | Server | 255.255.255.255 (broadcast) | "Here is 192.168.1.10, lease 8 hours" |
| Request | Client | 255.255.255.255 (broadcast) | "I accept the offer from server 192.168.1.1" |
| Acknowledgment | Server | Client IP or broadcast | "Confirmed. Use 192.168.1.10 for 8 hours" |

Note: Discover and Request are broadcast because the client has no IP address yet. Multiple DHCP servers may send Offers; the client selects one and broadcasts the Request to inform all servers which offer was accepted.

---

### 5. DHCP Relay Agent Operation

DHCP uses broadcast. Routers do not forward broadcasts by default. When a DHCP client is on a different subnet than the DHCP server, a relay agent is required.

The ip helper-address command on a Cisco router interface:

- Intercepts DHCP Discover broadcasts arriving on that interface
- Converts the broadcast to a unicast packet addressed to the DHCP server
- Inserts the giaddr (gateway interface address) field — the IP of the router's interface facing the client
- Forwards the unicast packet to the DHCP server

The DHCP server uses the giaddr to determine which scope to assign from. Each relay-facing interface IP must correspond to a subnet that has a configured scope on the DHCP server.

---

### 6. NTP Stratum Hierarchy

| Stratum | Description | Example | Typical Accuracy |
|---------|-------------|---------|-----------------|
| 0 | Reference clock (not on network) | GPS receiver, atomic clock, CDMA signal | Nanoseconds |
| 1 | Primary NTP server, directly connected to stratum 0 | time.nist.gov | Microseconds |
| 2 | Synchronized to stratum 1 | Corporate NTP server | Milliseconds |
| 3 | Synchronized to stratum 2 | Branch office NTP server | Milliseconds |
| 4–15 | Successively further from reference | Client workstations | Varies |
| 16 | Unsynchronized | A device that has lost its time source | N/A |

Kerberos authentication in Active Directory requires all domain members to be within 5 minutes of domain controller time. When clock skew exceeds this threshold, Kerberos tickets are rejected and authentication fails. The "clock skew too great" error is a Kerberos-specific error, not a generic NTP error.

---

### 7. NAT Comparison Table

| NAT Type | Mapping | Use Case | Public IP Stability |
|----------|---------|----------|---------------------|
| Static NAT | 1 private → 1 public (permanent) | Servers requiring fixed public address | Always the same |
| Dynamic NAT | 1 private → 1 public (from pool, per session) | Outbound access when public IPs available | Changes per session |
| PAT / NAT Overload | Many private → 1 public (differentiated by port) | Outbound internet access for entire network | Shared single IP |

---

### 8. Exam Tips

Exam Tip 1: DHCP uses UDP 67 (server) and UDP 68 (client). DNS uses UDP 53 for queries and TCP 53 for zone transfers. NTP uses UDP 123. These port numbers appear on the exam.

Exam Tip 2: APIPA range is 169.254.0.0/16. Any workstation showing a 169.254.x.x address failed to reach a DHCP server. The exam tests whether you know the cause and the troubleshooting step (check DHCP server connectivity and relay agent configuration).

Exam Tip 3: A non-authoritative DNS answer is not an error. It is a cached response from a resolver. An authoritative answer comes directly from the zone's authoritative name server.

Exam Tip 4: DHCP snooping blocks rogue DHCP servers by restricting DHCP server responses to trusted switch ports only. This is the correct answer to "rogue DHCP server" security questions.

Exam Tip 5: The ip helper-address command must be configured on the Layer 3 interface of the VLAN where clients reside — not on the DHCP server side. The server does not need any special relay configuration.

Exam Tip 6: MX records must point to a hostname (not an IP). That hostname must have a valid A record. A broken A record for the MX target causes email delivery failure even though the MX record itself is correct.

Exam Tip 7: Kerberos clock skew is exactly 5 minutes (300 seconds). The exam tests this specific value. NTP drift beyond 5 minutes causes "clock skew too great" authentication failures.

Exam Tip 8: Static NAT is the correct choice when an internal server must be reachable at a consistent public IP by external partners. PAT (NAT Overload) is correct for outbound internet access by many internal clients sharing one public IP.

---

### 9. Reading and Viewing Resources

CompTIA Network+ N10-008 Exam Objectives — Domain 1.6 (DNS), Domain 1.7 (DHCP, NTP), Domain 2.1 (NAT types)

Professor Messer — Network+ Study Groups (free video series): DNS, DHCP, and NTP explanations aligned to N10-008

Mike Meyers — CompTIA Network+ All-in-One Exam Guide, 8th Edition: Chapter 19 (DNS), Chapter 20 (DHCP), Chapter 23 (NTP and time services)

RFC 1034 and RFC 1035 — Original DNS specification documents (authoritative but dense; reference for exam-depth understanding)

RFC 2131 — DHCP specification (defines DORA, relay agent behavior, lease renewal)

RFC 5905 — NTP Version 4 specification (stratum definitions, authentication, best-practice deployment)

---

### 10. Study Checklist

Before moving to the next module, confirm you can do each of the following:

- [ ] Describe all six steps in the full DNS resolution hierarchy (client to root to TLD to authoritative)
- [ ] List all eight DNS record types and their functions from memory
- [ ] Explain the difference between a recursive query and an iterative query
- [ ] Define TTL and explain how it affects DNS caching behavior
- [ ] Explain what a non-authoritative answer means and why it is not an error
- [ ] Describe the DORA process message by message including source/destination addresses
- [ ] Explain why DHCP Discover is a broadcast and what address it uses
- [ ] Explain what ip helper-address does and where it must be configured
- [ ] Explain APIPA: what triggers it, what address range it uses, and what it prevents
- [ ] Describe the NTP stratum hierarchy from stratum 0 through client workstations
- [ ] State the Kerberos maximum clock skew tolerance value (5 minutes)
- [ ] Distinguish Static NAT, Dynamic NAT, and PAT by mapping type and use case
- [ ] State the port numbers for DNS (UDP/TCP 53), DHCP (UDP 67/68), and NTP (UDP 123)
- [ ] Explain what DHCP snooping does and what attack it prevents
- [ ] Explain what DDNS does and why it is needed in dynamic IP environments

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
