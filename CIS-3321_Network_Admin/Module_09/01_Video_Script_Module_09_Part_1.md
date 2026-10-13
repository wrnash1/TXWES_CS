# Video Script: Module 09 — Network Services: DNS, DHCP, and NTP

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Part 1 of 2 | Estimated Duration: 13–15 minutes

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 09: Network Services — DNS, DHCP, and NTP | Texas Wesleyan University"]

---

### Section 1: Introduction

[00:00 – 01:00]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 09. I am Professor Nash. Every time you open a browser and type a website name, three invisible infrastructure services work together to make that connection happen — DNS resolves the hostname to an IP address, DHCP assigned your device an address in the first place, and NTP ensures every device on the network agrees on the current time. These services run silently in the background, and when they fail, users cannot reach anything. Module 09 covers all three in depth. Part 1 focuses on DNS — the naming system that makes the internet navigable — and DHCP, which automates address assignment. Part 2 covers NTP and NAT, two additional services critical for enterprise network operation.

---

### Section 2: DNS — The Naming System

[01:00 – 06:00]

[SHOW DIAGRAM: A hierarchical DNS tree. At the top is a root node labeled "." (dot). Below it are two branches: .com and .org. Under .com are two sub-branches: example.com and google.com. Under example.com is www.example.com. Arrows labeled "recursive query" trace the path from a client to the resolver, then from the resolver to the root, TLD, and authoritative servers in sequence. Each server level is labeled: Root Name Server, TLD Name Server (.com), Authoritative Name Server (example.com), Resolver.]

[Alt-text: A DNS hierarchy diagram with five levels. The top node is the root (dot). The second level shows .com and .org top-level domains. The third level under .com shows example.com and google.com. The fourth level under example.com shows www.example.com. Six labeled arrows trace the DNS resolution path: (1) Client to Resolver, (2) Resolver to Root, (3) Root to Resolver with referral to TLD, (4) Resolver to TLD Server, (5) TLD to Resolver with referral to authoritative server, (6) Resolver to Authoritative Server returning the IP address.]

DNS — the Domain Name System — is a distributed, hierarchical database that translates human-readable hostnames into IP addresses. Without DNS, users would need to memorize the IP address of every website they visit.

The DNS resolution process works in six steps:

Step 1 — The client sends a recursive query to its configured DNS resolver. The resolver is typically the client's default gateway or a service like 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare).

Step 2 — The resolver checks its cache. If the answer is cached and the TTL has not expired, it returns the answer immediately. If not, it begins iterative queries.

Step 3 — The resolver queries a root name server, asking where to find the .com TLD servers.

Step 4 — The root server responds with the address of the .com TLD name servers.

Step 5 — The resolver queries the .com TLD server, asking for the authoritative name server for example.com.

Step 6 — The resolver queries the authoritative name server for example.com, which returns the IP address. The resolver caches the result (respecting the TTL) and returns it to the client.

DNS uses UDP port 53 for standard queries and TCP port 53 for zone transfers and responses exceeding 512 bytes.

> Network+ Exam Tip: The client sends a recursive query to its resolver. The resolver uses iterative queries to the root, TLD, and authoritative servers. A "Non-authoritative answer" in nslookup output means the answer came from the resolver's cache, not directly from the authoritative name server.

---

### Section 3: DNS Record Types

[06:00 – 09:30]

[SHOW DIAGRAM: A table showing eight DNS record types with columns for record type abbreviation, full name, purpose, and example.]

[Alt-text: A DNS record type reference table with four columns: Record Type abbreviation, Full Name, Purpose, Example. The eight rows cover A, AAAA, CNAME, MX, NS, PTR, TXT, and SOA records with descriptions and examples for each.]

You need to know these DNS record types for the Network+ exam:

A record — Maps a hostname to an IPv4 address. The most common record type.

AAAA record — Maps a hostname to an IPv6 address.

CNAME record — A canonical name record creates an alias pointing one hostname to another. The resolver follows the CNAME chain until it reaches an A or AAAA record.

MX record — Mail Exchanger record. Identifies the mail server responsible for accepting email for a domain. Includes a priority value — lower number means higher priority.

NS record — Name Server record. Identifies the authoritative name servers for a domain.

PTR record — Pointer record. Maps an IP address back to a hostname (reverse DNS lookup). Stored in the in-addr.arpa zone. Used by email servers and network administrators.

TXT record — Text record. Stores arbitrary text. Widely used for SPF records (Sender Policy Framework — prevents email spoofing), DKIM records (email signing), and domain verification.

SOA record — Start of Authority. Contains administrative metadata about the DNS zone: the primary name server, admin contact email, serial number, and refresh timers.

> Network+ Exam Tip: MX records are always the answer when the question involves email delivery. PTR records are always the answer for reverse DNS lookup. TXT records are the answer for SPF and DKIM email authentication.

---

### Section 4: DHCP — Dynamic Host Configuration Protocol

[09:30 – 13:30]

[SHOW DIAGRAM: The DHCP DORA four-step process showing a client PC and DHCP Server with four arrows: DISCOVER (broadcast from client), OFFER (server to client), REQUEST (broadcast from client), ACK (server to client). Below the arrows, a lease parameters box lists IP Address, Subnet Mask, Default Gateway, DNS Server, and Lease Duration.]

[Alt-text: A DHCP sequence diagram with a client PC on the left and a DHCP Server on the right. Four horizontal arrows trace the DORA process. Arrow 1 labeled DISCOVER points right (client broadcasts to find any DHCP server). Arrow 2 labeled OFFER points left (server proposes an IP and configuration). Arrow 3 labeled REQUEST points right (client broadcasts acceptance of the offer). Arrow 4 labeled ACK points left (server confirms the lease). A box below lists the parameters in the ACK: IP Address, Subnet Mask, Default Gateway, DNS Server IP, Lease Duration.]

DHCP automates the assignment of IP addresses and network configuration parameters to clients.

The DHCP process follows the DORA sequence:

DISCOVER — The client broadcasts a DHCP Discover message (destination IP 255.255.255.255). The client has no IP address and is looking for any DHCP server.

OFFER — One or more DHCP servers respond with a DHCP Offer, proposing an available IP address with subnet mask, default gateway, DNS server, and lease duration.

REQUEST — The client broadcasts a DHCP Request, indicating which server's offer it accepts. Broadcasting (rather than unicasting) allows other servers that sent Offers to know their offer was not accepted and reclaim the address.

ACK — The chosen server sends a DHCP Acknowledgment confirming the lease. The client configures its interface with the delivered parameters.

At 50% of the lease duration, the client attempts a unicast renewal with the issuing server. At 87.5% of the lease (T2), the client broadcasts a renewal to any available DHCP server.

DHCP uses UDP port 67 (server) and UDP port 68 (client).

DHCP Relay Agent — When the DHCP server is on a different subnet, the local router acts as a relay agent (ip helper-address in Cisco IOS). The relay agent intercepts the broadcast DHCP Discover and forwards it as a unicast to the DHCP server. Without a relay agent, broadcast DHCP messages cannot cross subnet boundaries.

> Network+ Exam Tip: DHCP uses UDP ports 67 and 68. DORA is the acronym. When a Windows client cannot reach a DHCP server, it self-assigns an APIPA address in the 169.254.0.0/16 range. Seeing 169.254.x.x means DHCP failed.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

End of Part 1
