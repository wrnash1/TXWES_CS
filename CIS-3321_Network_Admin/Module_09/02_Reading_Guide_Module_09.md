# Reading Guide: Module 09 - Network Services – DNS, DHCP, and NTP
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 09 – Network Services: DNS, DHCP, and NTP**! DNS, DHCP, and NTP are foundational infrastructure services that every enterprise network depends on. The CompTIA Network+ N10-009 exam tests these services in depth — including DNS record types, DHCP lease mechanics, and the role of time synchronization in network security. Understanding these services is also essential for real-world troubleshooting, since failures in DNS or DHCP cause connectivity problems that are commonly misdiagnosed.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **DNS (Domain Name System)**: A distributed, hierarchical naming system that translates human-readable hostnames (e.g., www.example.com) into IP addresses. DNS uses UDP port 53 for standard queries and TCP port 53 for zone transfers and large responses.
*   **DNS Resolution Process**: When a client queries a hostname, it first checks the local cache, then the hosts file, then sends a recursive query to its configured DNS resolver. The resolver queries root servers → TLD servers → authoritative name servers to resolve the name.
*   **A Record**: A DNS resource record that maps a hostname to an IPv4 address. The most fundamental DNS record type.
*   **AAAA Record**: A DNS resource record that maps a hostname to an IPv6 address. (Quad-A record.)
*   **CNAME Record (Canonical Name)**: A DNS record that creates an alias pointing one hostname to another hostname. Used to have multiple names resolve to the same server (e.g., www.example.com → webserver.example.com).
*   **MX Record (Mail Exchanger)**: A DNS record that specifies the mail server responsible for accepting email for a domain. Has a priority value — lower numbers have higher priority.
*   **PTR Record (Pointer Record)**: A DNS record used for reverse DNS lookup — resolves an IP address back to a hostname. Stored in the in-addr.arpa zone for IPv4.
*   **SOA Record (Start of Authority)**: A DNS record that identifies the authoritative name server for a zone and contains administrative parameters including the zone serial number, refresh interval, and TTL defaults.
*   **TTL (Time to Live)**: The duration in seconds that a DNS record may be cached by a resolver before it must be re-queried from the authoritative server. Lower TTL = faster propagation of changes; higher TTL = reduced DNS query load.
*   **DHCP (Dynamic Host Configuration Protocol)**: A network service that automatically assigns IP addresses and configuration parameters (subnet mask, default gateway, DNS server) to clients. Uses UDP port 67 (server) and UDP port 68 (client).
*   **DHCP DORA Process**: The four-step DHCP lease acquisition process: (1) **Discover** — client broadcasts to find DHCP servers; (2) **Offer** — server responds with an available IP; (3) **Request** — client broadcasts requesting the offered IP; (4) **Acknowledge** — server confirms the lease.
*   **DHCP Lease**: A time-limited assignment of an IP address to a client. At 50% of the lease duration, the client attempts to renew with the original server. At 87.5%, it broadcasts a rebind request to any DHCP server.
*   **DHCP Reservation**: A static IP assignment tied to a client's MAC address within the DHCP server. The client always receives the same IP via DHCP without manual static configuration on the client.
*   **DHCP Scope**: The pool of IP addresses a DHCP server is configured to assign within a specific subnet. Includes the IP range, exclusions, lease duration, and options (gateway, DNS).
*   **DHCP Relay Agent (IP Helper)**: A router or Layer 3 switch configuration that forwards DHCP broadcast messages from clients to a DHCP server on a different subnet. Since DHCP uses broadcasts, a relay is required when the server is not on the same subnet as the client.
*   **NTP (Network Time Protocol)**: A protocol that synchronizes clocks across network devices. Uses UDP port 123. Accurate time is critical for security (certificate validation, Kerberos authentication, log correlation) and network operations.
*   **NTP Stratum**: The hierarchical distance of an NTP server from the reference time source. Stratum 0 = atomic/GPS clock (reference clock, not on the network). Stratum 1 = server directly synced to Stratum 0. Stratum 2 = server synced to Stratum 1. Lower stratum = more accurate.
*   **DNS Poisoning (Cache Poisoning)**: An attack where forged DNS responses are injected into a resolver's cache, causing clients to resolve legitimate domain names to attacker-controlled IP addresses. Mitigated by DNSSEC.
*   **DNSSEC (DNS Security Extensions)**: An extension to DNS that uses digital signatures to authenticate DNS responses, preventing cache poisoning attacks. Resolvers can verify that DNS data has not been tampered with.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** DNS and DHCP fall under **Domain 1.0 – Networking Concepts (23%)** and **Domain 2.0 – Network Implementations (20%)**. NTP falls under **Domain 4.0 – Network Security (19%)** in the context of security dependencies.
*   **DNS record types — the most-tested DNS content**: A = IPv4 address. AAAA = IPv6 address. CNAME = alias. MX = mail server. PTR = reverse lookup. SOA = zone authority. The exam gives you a scenario and asks which record type to create.
*   **DHCP DORA is mandatory memorization**: The exam tests each step by name and function. Remember: all four steps use broadcast except the server's Offer (unicast to the client's MAC) and the final Acknowledge.
*   **DHCP relay agent = IP helper**: The exam frequently presents a scenario where clients on VLAN 10 cannot get DHCP leases from a server on VLAN 1. The answer is always to configure an IP helper address (`ip helper-address`) on the VLAN 10 router interface pointing to the DHCP server.
*   **NTP and security**: The exam may ask why NTP is important in a security context. Kerberos authentication (used in Active Directory) fails if clocks differ by more than 5 minutes. Certificate validation requires accurate time. Log correlation for forensics requires synchronized timestamps across devices.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers DNS record types, DHCP operation, and NTP in the Networking Concepts and Network Implementations sections.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **DNS, DHCP, and Network Time** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the DNS resolution hierarchy, DHCP DORA sequence diagrams, and the NTP stratum model.
*   **Required Video:** Watch Professor Messer's **DNS**, **DHCP**, and **NTP** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will use `nslookup` and `dig` to query DNS A, AAAA, MX, and PTR records; observe DHCP DORA traffic in Wireshark; configure a DHCP scope and reservation on a Windows Server; and verify NTP synchronization status using `w32tm /query /status` (Windows) or `timedatectl` (Linux).

---

### 3. Study Checklist
*   [ ] Memorize all DNS record types: A, AAAA, CNAME, MX, PTR, SOA — and their use cases.
*   [ ] Know the DHCP DORA process steps in order with the function of each message.
*   [ ] Understand DHCP relay agent (IP helper) and when it is required.
*   [ ] Know NTP stratum levels and why accurate time synchronization is a security requirement.
*   [ ] Know DNS ports (UDP/TCP 53) and DHCP ports (UDP 67/68).
*   [ ] Read the **DNS, DHCP, and NTP** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's DNS, DHCP, and NTP videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
