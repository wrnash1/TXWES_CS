# Video Script: Module 09 - WAN Technologies and VPNs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 4: IP Services / Domain 5: Security Fundamentals)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for GRE tunnel configuration demonstration
- Show physical packet flow diagrams for GRE encapsulation
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: WAN Fundamentals and Connectivity Types [00:00 - 04:00]

Welcome to Module 09. I am Professor Nash. Today we step outside the LAN and look at how organizations connect geographically separated sites — that is, WAN technologies and virtual private networks.

A WAN, or Wide Area Network, connects sites that span cities, countries, or continents. The connection between your corporate office and a branch two states away is a WAN link. Unlike a LAN, the organization typically does not own the physical infrastructure — they lease connectivity from a service provider.

[SHOW DIAGRAM: A map-style diagram showing a headquarters building and three branch offices connected by lines representing WAN links. Labels show WAN provider cloud in the middle. Two site connections use Metro Ethernet and one uses a leased line]

The CCNA 200-301 exam focuses on four primary WAN connection categories:

- Leased lines: dedicated point-to-point connections; expensive but guaranteed bandwidth
- Metro Ethernet: carrier-provided Ethernet service across a metropolitan area
- Internet-based WAN: uses the public internet with VPNs for security
- Broadband (cable, DSL, fiber): lower-cost connectivity for smaller sites

For the exam, understand the trade-offs between these options: cost, bandwidth, reliability, and security.

---

## Section 2: Metro Ethernet [04:00 - 08:00]

[SHOW DIAGRAM: A carrier network cloud labeled "Metro Ethernet Provider." Three customer sites connect to the cloud using standard Ethernet interfaces. Labels indicate E-Line (point-to-point) between Site A and Site B, and E-LAN (multipoint) connecting all three sites]

Metro Ethernet is a WAN technology that extends Ethernet connectivity across a metropolitan area network operated by a service provider. The key advantage is that the customer side uses standard Ethernet interfaces — the same hardware used in the LAN — simplifying configuration and reducing equipment costs.

Metro Ethernet service types:

- E-Line: point-to-point Ethernet service between two sites. Equivalent to a leased line using Ethernet.
- E-LAN: multipoint-to-multipoint service where all sites appear to be on the same Ethernet segment. Used for any-to-any communication.
- E-Tree: hub-and-spoke topology where spokes can communicate with the hub but not directly with each other.

CCNA Exam Tip: The CCNA tests Metro Ethernet at the conceptual level. You need to know the service type names (E-Line, E-LAN, E-Tree) and their topologies. You will not be asked to configure the provider side.

---

## Section 3: VPNs and IPsec Framework [08:00 - 14:00]

[SHOW DIAGRAM: Two router icons labeled HQ Router and Branch Router connected by a line labeled "IPsec VPN Tunnel" crossing through an "Internet" cloud. Small lock icons on the tunnel indicate encryption. Arrows show traffic entering unencrypted on the LAN side and leaving encrypted across the internet]

A Virtual Private Network creates a secure, encrypted tunnel through an untrusted network — typically the public internet — to connect two sites as if they were directly connected. There are two main VPN models:

- Site-to-Site VPN: connects entire networks. Always-on. Configured on routers or firewalls at each site.
- Remote Access VPN: connects individual users to the corporate network. Used for remote workers.

For the CCNA exam, the focus is on site-to-site VPNs and the IPsec framework.

### IPsec Components

IPsec is not a single protocol — it is a framework of protocols working together:

- IKE (Internet Key Exchange): negotiates the security association, exchanges encryption keys, and authenticates peers before any traffic is sent
- AH (Authentication Header): provides data integrity and origin authentication but no encryption — the payload is readable
- ESP (Encapsulating Security Payload): provides integrity, authentication, and encryption — the most commonly used IPsec protocol

CCNA Exam Tip: The most tested IPsec distinction on the CCNA is AH versus ESP. AH = Authentication only, no encryption. ESP = Encryption plus authentication. In production, ESP is almost always used because it provides confidentiality. AH alone leaves traffic readable.

### IPsec Modes

- Transport mode: encrypts only the payload, preserving the original IP header. Used for host-to-host encryption.
- Tunnel mode: encrypts the entire original IP packet and adds a new IP header. Used for site-to-site VPNs.

---

## Section 4: GRE Tunnels [14:00 - 19:00]

[SHOW DIAGRAM: Two routers R1 and R2 connected via the internet. A tunnel interface labeled "Tunnel0" is drawn as a logical overlay above the physical connection. OSPF neighbor relationship is shown running over the Tunnel0 interface. Original IP packet shown being wrapped in a GRE header and then an outer IP header]

GRE — Generic Routing Encapsulation — is a tunneling protocol that encapsulates virtually any Layer 3 protocol inside IP packets. The result is a virtual point-to-point link between two routers that can carry routing protocol traffic (including OSPF hello packets and LSAs) across a WAN.

Key GRE characteristics:

- Supports multicast and broadcast (IPsec alone does not)
- No encryption — GRE is plaintext by design
- Commonly combined with IPsec for encrypted dynamic routing tunnels

### GRE Configuration

On R1 (source: 203.0.113.1, destination: 203.0.113.2):

```ios
R1(config)# interface Tunnel0
R1(config-if)# tunnel mode gre ip
R1(config-if)# tunnel source 203.0.113.1
R1(config-if)# tunnel destination 203.0.113.2
R1(config-if)# ip address 172.16.0.1 255.255.255.252
R1(config-if)# no shutdown
```

On R2 (source: 203.0.113.2, destination: 203.0.113.1):

```ios
R2(config)# interface Tunnel0
R2(config-if)# tunnel mode gre ip
R2(config-if)# tunnel source 203.0.113.2
R2(config-if)# tunnel destination 203.0.113.1
R2(config-if)# ip address 172.16.0.2 255.255.255.252
R2(config-if)# no shutdown
```

The tunnel interface is a logical interface — it has its own IP address in a separate subnet. Once the tunnel is up, you can configure OSPF or static routes using the tunnel interface as the next hop.

CCNA Exam Tip: GRE tunnels support multicast, which is why they are used to run OSPF or EIGRP across a WAN. IPsec tunnels alone do not support multicast by default. When you need dynamic routing protocols over an encrypted WAN link, the typical solution is GRE over IPsec.

---

## Section 5: Verification and Exam Strategy [19:00 - 22:00]

Key verification commands for GRE tunnels:

```ios
R1# show interface Tunnel0
R1# show ip interface brief
R1# show ip route
```

The tunnel interface should show `up/up`. If the tunnel shows `up/down`, the underlying routing to the tunnel destination may be missing.

Common GRE tunnel issues:

- Tunnel source or destination misconfigured (wrong IP address)
- No route to the tunnel destination in the routing table
- Tunnel source and destination swapped on one end

For exam strategy on WAN and VPN questions: the CCNA tests conceptual understanding of these technologies, not detailed IPsec CLI syntax. Know the difference between AH and ESP, understand what GRE provides (and lacks), and be able to identify the correct WAN service type for a given scenario.

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 09 Complete
Next: Module 10 - Access Control Lists
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
