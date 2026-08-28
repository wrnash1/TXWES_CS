# Video Script: Module 09 — Network Services: DNS, DHCP, and NTP

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Part 2 of 2 | Estimated Duration: 11–13 minutes

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 09 Part 2 — NTP, NAT, and Network Services Wrap-Up"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 09. In Part 1 we covered DNS record types, the resolution hierarchy, and the DHCP DORA process. Now in Part 2 we add NTP for time synchronization and NAT for address translation. NTP and NAT both appear frequently on the Network+ exam, and NAT in particular has three subtypes you need to distinguish.

---

### Section 2: NTP — Network Time Protocol

[00:45 – 04:00]

[SHOW DIAGRAM: An NTP hierarchy showing three levels. Level 0 (Stratum 0) shows a GPS satellite and atomic clock labeled "Reference Clock — not on the network." Level 1 (Stratum 1) shows two NTP servers labeled "Primary NTP Servers — synchronized directly to Stratum 0." Level 2 (Stratum 2) shows four NTP servers. Level 3 (Stratum 3) shows eight client devices labeled "End devices and infrastructure."]

[Alt-text: A four-level NTP stratum diagram. Stratum 0 shows a GPS satellite and atomic clock icon labeled Reference Clock. Stratum 1 shows two server icons labeled Primary NTP Servers synchronized directly to Stratum 0. Stratum 2 shows four server icons labeled Secondary NTP Servers synchronized to Stratum 1. Stratum 3 shows eight device icons including workstations and network switches. Downward arrows between each stratum represent time synchronization flowing down the hierarchy.]

NTP — Network Time Protocol — synchronizes clocks across all devices in a network. Accurate time is not just a convenience — it is a security requirement.

Why time synchronization matters:

Authentication and certificates — TLS certificates have valid-from and valid-to dates. A device with a clock off by more than a few minutes may reject valid certificates or accept expired ones. Kerberos authentication, used in Active Directory, fails if the time difference between client and server exceeds five minutes.

Log correlation — When investigating a security incident across multiple devices, accurate timestamps allow reconstruction of the event sequence. If each device has a different time, log correlation becomes impossible.

Replay attack prevention — IPsec and Kerberos use timestamps to reject replayed authentication packets. Without accurate time, replay protection fails.

NTP uses a hierarchical stratum model. Stratum 0 is the reference clock (GPS receiver or atomic clock). Stratum 0 devices are not on the network — they feed time to Stratum 1 servers directly. Stratum 1 servers synchronize to Stratum 0. Stratum 2 servers synchronize to Stratum 1. Most enterprise network devices synchronize to Stratum 2 or Stratum 3 servers.

NTP uses UDP port 123. Stratum 16 indicates unsynchronized.

> Network+ Exam Tip: NTP uses UDP port 123. Stratum 1 is most accurate on the network. Kerberos fails if clock skew exceeds 5 minutes.

---

### Section 3: NAT — Network Address Translation

[04:00 – 09:00]

[SHOW DIAGRAM: Two side-by-side diagrams. Left: Static NAT — one private IP maps permanently to one public IP. Right: PAT (NAT Overload) — multiple private IPs share a single public IP, differentiated by unique source port numbers.]

[Alt-text: Two NAT diagrams. Left diagram labeled Static NAT shows one private IP 192.168.1.10 mapping through a NAT router to one public IP 203.0.113.10, labeled One-to-one permanent mapping. Right diagram labeled PAT / NAT Overload shows three private IP addresses (192.168.1.10, 192.168.1.11, 192.168.1.12) all translating through a NAT router to the single public IP 203.0.113.1 with unique translated source port numbers. Labeled Many-to-one mapping using unique port numbers.]

NAT — Network Address Translation — modifies IP address information in packet headers as traffic passes through a router, allowing private-addressed devices to use public IP addresses for internet access.

The three types you must know:

Static NAT — A one-to-one permanent mapping between a single private IP and a single public IP. Used when an internal server must be reachable from the internet at a specific public IP. Example: web server at 192.168.1.10 permanently mapped to 203.0.113.10.

Dynamic NAT — Maps private IPs to a pool of public IPs on demand. The mapping is created when a client initiates a connection and released when it ends. Requires as many public IPs as concurrent outside connections.

PAT (Port Address Translation) / NAT Overload — Maps many private IPs to a single public IP using unique source port numbers to track each session. This is how home routers and most enterprise edge routers work. When an internal host at 192.168.1.10 port 1500 sends traffic outbound, the NAT router rewrites the source IP to the public IP and assigns a unique translated source port. Return traffic is forwarded back using the translation table.

Inside local — The private IP of an internal host as seen from the inside network.

Inside global — The public IP of an internal host as seen from outside after translation.

> Network+ Exam Tip: PAT (NAT Overload) allows thousands of internal hosts to share a single public IP. Static NAT is always the answer when an internal server must be reachable at a fixed public address.

---

### Section 4: IPAM and DNS/DHCP Integration

[09:00 – 11:30]

[SHOW DIAGRAM: A three-box flow diagram showing DHCP Server, IPAM (IP Address Management), and DNS Server with bidirectional arrows labeled Dynamic DNS Updates.]

[Alt-text: A three-box horizontal flow diagram. Left box labeled DHCP Server. Center box labeled IPAM with text: Centralized tracking of IP assignments and scope utilization. Right box labeled DNS Server. Bidirectional arrows between DHCP and IPAM and between IPAM and DNS are labeled Dynamic DNS Updates.]

IPAM — IP Address Management — is a framework for tracking IP address allocation, DNS records, and DHCP scope utilization across an enterprise network.

Dynamic DNS (DDNS) — When DHCP assigns a new address to a client, it can automatically notify the DNS server to create or update the A and PTR records. This keeps DNS synchronized with DHCP assignments without manual updates.

DHCP starvation — An attack where a malicious device sends large numbers of DHCP Discover messages with spoofed MAC addresses, exhausting all available addresses in the DHCP scope. DHCP Snooping (covered in Module 08) mitigates this attack.

Module 09 key takeaways: DNS resolves hostnames using a hierarchical query process. DHCP automates address assignment using the DORA sequence. NTP uses UDP 123 and the stratum hierarchy. PAT (NAT Overload) allows many private IPs to share one public IP. Dynamic DNS keeps A and PTR records current as DHCP assignments change.

Module 10 covers routing protocols — static routes, OSPF, and BGP.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

End of Part 2
