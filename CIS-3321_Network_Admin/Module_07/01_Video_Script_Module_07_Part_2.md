# Video Script: Module 07 – WAN and Cloud Connectivity

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Part 2 of 2 | Estimated Duration: 11–13 minutes

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 07 Part 2 — VPN Technologies: IPsec, SSL/TLS, and Remote Access"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 07. In Part 1 we covered WAN technology types — MPLS, DSL, Metro Ethernet, SD-WAN — and the three cloud service models with their deployment variants. Now in Part 2 we tackle VPN technologies. VPNs are one of the most directly tested topics on the Network+ exam. You need to know the difference between IPsec Tunnel mode and Transport mode, when to use SSL/TLS VPN vs. IPsec, and how common tunneling protocols like GRE and L2TP work.

---

### Section 2: VPN Fundamentals

[00:45 – 03:30]

[SHOW DIAGRAM: A topology showing two corporate sites connected through a cloud labeled "Public Internet." A labeled tunnel arrow passes through the cloud between the two site edge routers, labeled "VPN Tunnel." The tunnel has icons showing: Encapsulation (wrapping), Encryption (padlock), and Authentication (key).]

[Alt-text: A network topology diagram showing two corporate office buildings connected through a public internet cloud. A thick arrow labeled VPN Tunnel passes between the two buildings through the cloud. Three icons along the tunnel arrow are labeled Encapsulation (a wrapped package icon), Encryption (a padlock icon), and Authentication (a key icon). Below the diagram a label reads "VPN creates a secure logical path over untrusted public infrastructure."]

A VPN (Virtual Private Network) creates a secure, encrypted logical connection across an untrusted network — typically the public internet — to simulate a private leased-line connection between two endpoints.

Three properties define a VPN:

**Encapsulation** — The original packet is wrapped inside a new packet for transit across the intermediate network. The original source and destination may be hidden inside the outer header.

**Encryption** — The payload (and in Tunnel mode, the entire original packet) is encrypted so that an eavesdropper on the public internet sees only ciphertext.

**Authentication** — Both endpoints verify each other's identity before the tunnel is established. VPNs use pre-shared keys, digital certificates, or user credentials for authentication.

VPNs come in two primary use cases:

**Site-to-Site VPN** — Connects two entire networks. The VPN gateways (routers or firewalls at each site) establish the tunnel. Individual end-user devices need no special VPN software — they simply send traffic to their local gateway, which encrypts and forwards it through the tunnel to the remote site gateway. Used to connect branch offices.

**Remote-Access VPN** — Connects an individual user's device to the corporate network. The user runs a VPN client that establishes an encrypted tunnel to the corporate VPN concentrator. All or some of the user's traffic is then routed through the corporate network.

---

### Section 3: IPsec — Modes and Protocols

[03:30 – 07:00]

[SHOW DIAGRAM: Two side-by-side packet diagrams. Left: IPsec Transport Mode — shows the original IP header visible, followed by an IPsec header, followed by the encrypted payload. Right: IPsec Tunnel Mode — shows a new outer IP header with VPN gateway addresses, followed by an IPsec header, followed by the entire original packet (original IP header + payload) encrypted inside.]

[Alt-text: Two packet structure diagrams side by side. Left diagram labeled IPsec Transport Mode shows three boxes: Original IP Header (white/unencrypted), IPsec Header, and Encrypted Payload (shaded). A label below reads "Original IP header is visible — source and destination IP addresses are exposed." Right diagram labeled IPsec Tunnel Mode shows four boxes: New Outer IP Header with VPN gateway IPs (white/unencrypted), IPsec Header, then a large shaded box containing both the Original IP Header and Original Payload encrypted together. A label below reads "Entire original packet is encrypted — only VPN gateway addresses are visible."]

IPsec (Internet Protocol Security) is the dominant protocol suite for VPN encryption at Layer 3. IPsec operates in two modes:

**Transport Mode** — Only the IP payload is encrypted. The original IP header (with source and destination addresses) remains in plaintext. Transport mode is used for host-to-host communications — for example, encrypting traffic between two servers on the same network. The original source and destination IP addresses are visible to the transit network.

**Tunnel Mode** — The entire original IP packet — both the header and the payload — is encrypted and encapsulated inside a new outer IP packet. The new outer IP header uses the VPN gateway addresses. The original source and destination addresses are completely hidden from anyone observing the transit network. Tunnel mode is used for site-to-site VPNs.

> Network+ Exam Tip: Site-to-site VPNs use IPsec Tunnel mode. When the exam says "hide the internal IP addresses from the transit network," the answer is Tunnel mode. Transport mode leaves the original IP header visible.

IPsec uses two sub-protocols:

**AH (Authentication Header)** — Provides authentication and integrity for the IP packet header and payload. Does not encrypt the payload — it only verifies that the packet has not been tampered with. AH alone does not provide confidentiality.

**ESP (Encapsulating Security Payload)** — Provides encryption, authentication, and integrity for the payload. ESP is the component that actually encrypts the data. In most deployments, ESP is used without AH because ESP provides authentication on its own.

**IKE (Internet Key Exchange)** — The protocol used to negotiate and establish IPsec security associations (SAs). IKEv1 uses two phases; IKEv2 is simplified and more efficient. Key exchange happens over UDP port 500. NAT traversal (NAT-T) uses UDP port 4500.

---

### Section 4: VPN Protocols — GRE, L2TP, SSL/TLS

[07:00 – 09:30]

[SHOW DIAGRAM: A comparison table of VPN protocols. Columns: Protocol, Layer, Encryption, Port/Protocol, Use Case. Rows: IPsec (Layer 3, AES/3DES, UDP 500/4500, site-to-site and remote access), GRE (Layer 3, None, IP Protocol 47, multiprotocol tunneling), L2TP/IPsec (Layer 2+3, IPsec encryption, UDP 1701 + UDP 500/4500, remote access), SSL/TLS VPN (Layer 4-7, TLS encryption, TCP 443, remote access/clientless).]

[Alt-text: A five-row comparison table with columns labeled Protocol, OSI Layer, Encryption, Port or Protocol, and Primary Use Case. Row 1: IPsec — Layer 3, AES or 3DES encryption, UDP 500 for IKE and UDP 4500 for NAT-T, used for site-to-site and remote-access VPNs. Row 2: GRE — Layer 3, no encryption natively, IP Protocol 47, used to tunnel multiprotocol traffic over IP networks. Row 3: L2TP/IPsec — combines Layer 2 (L2TP) with Layer 3 (IPsec) encryption, requires UDP 1701 for L2TP and UDP 500/4500 for IPsec, used for remote access. Row 4: SSL/TLS VPN — operates at Layer 4 through 7, TLS encryption, TCP port 443, used for remote access and clientless browser-based VPN.]

**GRE (Generic Routing Encapsulation)** — A tunneling protocol developed by Cisco that encapsulates any network layer protocol inside an IP packet. GRE itself provides no encryption — it is purely an encapsulation mechanism. GRE tunnels are often combined with IPsec to add encryption. GRE uses IP Protocol 47 (not a TCP or UDP port — it is its own IP protocol number). Common use case: routing non-IP protocols or multicast traffic across an IP-only WAN.

**L2TP/IPsec** — L2TP (Layer 2 Tunneling Protocol) by itself provides no encryption. L2TP is almost always combined with IPsec for encryption, creating L2TP/IPsec. L2TP creates a tunnel for Layer 2 frames; IPsec encrypts the content. Used primarily for remote-access VPNs on older operating systems (Windows built-in VPN client). Requires UDP 1701 for L2TP and UDP 500/4500 for IPsec — problematic in environments that block non-HTTPS ports.

**SSL/TLS VPN** — Uses TLS (Transport Layer Security) — the same protocol that secures HTTPS web traffic — to create the VPN tunnel over TCP port 443. Because port 443 is allowed through virtually every firewall, SSL VPN traverses restrictive networks that block IPsec ports. Two modes: full-tunnel (routes all traffic through VPN) and split-tunnel (only corporate traffic routes through VPN). Also supports clientless mode — users access resources through a web browser without installing a VPN client. Most modern remote-access VPN deployments use SSL/TLS.

> Network+ Exam Tip: When the exam describes a hotel or coffee shop firewall that only allows port 80 and 443, and a remote user needs VPN access, the answer is always SSL/TLS VPN on TCP 443. IPsec and L2TP use ports that would be blocked.

---

### Section 5: Split Tunneling and VPN Concentrators

[09:30 – 11:30]

[SHOW DIAGRAM: Two diagrams side by side. Left: Full-Tunnel VPN — all traffic from the remote user's laptop goes through the VPN tunnel to the corporate network; even general internet browsing routes through the corporate firewall before reaching the internet. Right: Split-Tunnel VPN — corporate traffic goes through the VPN tunnel; general internet traffic goes directly to the internet without passing through the corporate network.]

[Alt-text: Two network flow diagrams. Left diagram labeled Full-Tunnel VPN shows a remote laptop with all traffic (labeled Corporate Traffic and Internet Traffic) flowing into a single VPN tunnel arrow pointing to the corporate network, then out through the corporate firewall to the internet. Right diagram labeled Split-Tunnel VPN shows a remote laptop with two traffic flow arrows: one labeled Corporate Traffic going through the VPN tunnel to the corporate network, and a second labeled Internet Traffic going directly to the public internet bypassing the corporate network entirely.]

**Full-Tunnel VPN** — All traffic from the remote device is routed through the VPN tunnel to the corporate network. Internet browsing also goes through the corporate gateway. Advantage: all traffic is inspected by corporate security controls. Disadvantage: adds latency to general internet traffic, and increases load on the corporate internet link.

**Split-Tunnel VPN** — Only traffic destined for corporate network resources is routed through the VPN tunnel. All other internet traffic goes directly to the internet from the user's device. Advantage: reduces corporate bandwidth usage and latency for internet traffic. Disadvantage: traffic to the internet bypasses corporate security controls — a security risk if the user's device is compromised.

**VPN Concentrator** — A dedicated device (or software function on a firewall/router) that terminates multiple VPN client connections at the corporate network edge. A concentrator can handle thousands of simultaneous remote-access VPN sessions, performing encryption/decryption for all clients.

Module 07 key takeaways: MPLS provides guaranteed QoS for enterprise WAN. IaaS/PaaS/SaaS define customer responsibility boundaries. IPsec Tunnel mode hides internal IP headers. GRE provides encapsulation without encryption. SSL/TLS VPN uses TCP 443 for firewall traversal. Split-tunnel sends only corporate traffic through the VPN.

Module 08 covers network security — firewalls, IDS/IPS, and security architectures.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
