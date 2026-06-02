# Reading Guide: Module 09 - WAN Technologies and VPNs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 4: IP Services / Domain 5: Security Fundamentals)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

WAN technologies and VPNs are tested on the CCNA 200-301 primarily at the conceptual level. You will not be asked to configure full IPsec policies on the exam, but you will need to identify the correct WAN technology for a scenario, distinguish between AH and ESP, and understand GRE tunnel behavior and configuration. This guide covers all testable WAN and VPN concepts.

---

## 1. High-Yield Glossary

- **WAN (Wide Area Network):** A network spanning large geographic distances. Organizations typically lease WAN connectivity from a service provider. WAN links connect geographically separated sites.

- **Metro Ethernet:** A carrier WAN service that extends Ethernet connectivity across a metropolitan area. The customer side uses standard Ethernet interfaces. Service types include E-Line (point-to-point), E-LAN (multipoint), and E-Tree (hub-and-spoke).

- **E-Line:** Metro Ethernet point-to-point service between exactly two customer sites. Equivalent to a leased line using Ethernet interfaces.

- **E-LAN:** Metro Ethernet multipoint-to-multipoint service where all sites appear on the same Ethernet segment. Any site can communicate directly with any other site.

- **E-Tree:** Metro Ethernet hub-and-spoke service. Spoke sites can communicate with the hub but not directly with other spokes.

- **Site-to-Site VPN:** A permanent encrypted tunnel between two network endpoints (routers or firewalls). Connects entire networks. Always-on. IPsec is the most common framework used.

- **Remote Access VPN:** Allows individual users to connect securely to a corporate network from a remote location. Uses SSL/TLS or IPsec client software.

- **IPsec (Internet Protocol Security):** A suite of protocols providing authentication, integrity, and encryption for IP communications. Used to secure site-to-site VPN tunnels.

- **IKE (Internet Key Exchange):** The IPsec protocol responsible for negotiating security associations, authenticating peers, and exchanging encryption keys before data transmission begins.

- **AH (Authentication Header):** An IPsec protocol that provides data integrity and origin authentication but does not encrypt the payload. Traffic protected by AH alone is readable in plaintext.

- **ESP (Encapsulating Security Payload):** An IPsec protocol that provides encryption in addition to integrity and authentication. The preferred protocol in production VPN deployments.

- **Transport mode:** An IPsec mode that encrypts only the packet payload. The original IP header is preserved. Used for host-to-host encryption.

- **Tunnel mode:** An IPsec mode that encrypts the entire original IP packet and adds a new outer IP header. Used for site-to-site VPNs between routers.

- **GRE (Generic Routing Encapsulation):** A Cisco tunneling protocol that encapsulates any Layer 3 protocol within IP packets. Creates a virtual point-to-point link over any WAN. Supports multicast (needed for OSPF/EIGRP). Provides no encryption.

- **GRE over IPsec:** The combination of GRE for tunnel creation (enabling routing protocols) and IPsec for encryption. The most common method for running dynamic routing protocols over an encrypted WAN link.

- **DMVPN (Dynamic Multipoint VPN):** A Cisco scalable VPN architecture using GRE, NHRP (Next Hop Resolution Protocol), and IPsec. Enables spoke-to-spoke dynamic tunnels without pre-configuring each spoke pair. Tested at the conceptual level on CCNA.

---

## 2. WAN Technology Comparison

| Technology | Topology | Provider-Managed | Customer Interface | Bandwidth | Notes |
|---|---|---|---|---|---|
| Leased line (T1/E1) | Point-to-point | Yes | Serial | Fixed | Expensive; dedicated |
| Metro Ethernet E-Line | Point-to-point | Yes | Ethernet | Scalable | Familiar interface |
| Metro Ethernet E-LAN | Multipoint | Yes | Ethernet | Scalable | Any-to-any |
| Internet (broadband) | Any-to-any | No | Ethernet/DSL | Variable | Requires VPN for security |
| MPLS | Any-to-any | Yes | Ethernet/Serial | Scalable | Provider routes traffic |

---

## 3. IPsec Protocol Comparison

| Protocol | Provides Authentication | Provides Integrity | Provides Encryption | Exam Keyword |
|---|---|---|---|---|
| AH | Yes | Yes | No | Authentication only |
| ESP | Yes | Yes | Yes | Encryption + Authentication |

The CCNA exam most frequently tests the AH versus ESP distinction. In production environments, ESP is almost always used because it provides all three security services.

---

## 4. IPsec Mode Comparison

| Mode | What Is Encrypted | New Header | Use Case |
|---|---|---|---|
| Transport | Payload only | No (original preserved) | Host-to-host encryption |
| Tunnel | Entire original packet | Yes (new outer IP header) | Site-to-site VPN between routers |

---

## 5. GRE Tunnel Configuration Reference

### Router R1 (source 203.0.113.1, destination 203.0.113.2)

```ios
R1(config)# interface Tunnel0
R1(config-if)# tunnel mode gre ip
R1(config-if)# tunnel source 203.0.113.1
R1(config-if)# tunnel destination 203.0.113.2
R1(config-if)# ip address 172.16.0.1 255.255.255.252
R1(config-if)# no shutdown
```

### Router R2 (source 203.0.113.2, destination 203.0.113.1)

```ios
R2(config)# interface Tunnel0
R2(config-if)# tunnel mode gre ip
R2(config-if)# tunnel source 203.0.113.2
R2(config-if)# tunnel destination 203.0.113.1
R2(config-if)# ip address 172.16.0.2 255.255.255.252
R2(config-if)# no shutdown
```

Key configuration rules:

- R1's `tunnel source` equals R2's `tunnel destination` and vice versa
- The tunnel interface IP address is in a subnet separate from all physical interfaces
- `tunnel mode gre ip` is the default and is often omitted, but is explicit best practice

---

## 6. IOS Command Reference

| Task | Command | Mode |
|---|---|---|
| Create tunnel interface | `interface Tunnel0` | Global config |
| Set tunnel mode | `tunnel mode gre ip` | Interface config |
| Set local tunnel endpoint | `tunnel source [IP or interface]` | Interface config |
| Set remote tunnel endpoint | `tunnel destination [IP address]` | Interface config |
| Assign IP to tunnel | `ip address 172.16.0.1 255.255.255.252` | Interface config |
| Verify tunnel state | `show interface Tunnel0` | Privileged EXEC |
| Verify IP and state of all interfaces | `show ip interface brief` | Privileged EXEC |
| Verify routing table | `show ip route` | Privileged EXEC |

---

## 7. GRE Tunnel Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Tunnel is up/down | No route to the tunnel destination IP | Add route to reach the physical WAN endpoint |
| Tunnel source/dest reversed | One end has source/destination swapped | Ensure source on one end equals destination on other |
| Routing protocols fail across tunnel | Passive interface configured on tunnel | Remove passive-interface from Tunnel0 |
| Traffic reaches tunnel but is unencrypted | GRE only — no IPsec configured | Add IPsec configuration for encryption |

---

## 8. CCNA Exam Tips

1. AH provides authentication and integrity but no encryption. ESP provides encryption plus authentication and integrity. On the exam, when a question mentions "encryption" in the context of IPsec, the answer involves ESP.

2. GRE tunnels support multicast and broadcast, making them suitable for running OSPF or EIGRP across a WAN. IPsec tunnels alone do not support multicast by default. The combination "GRE over IPsec" provides both dynamic routing support and encryption.

3. A GRE tunnel interface shows `up/down` when there is no route to the tunnel destination address. The fix is to ensure a route exists to reach the physical IP address used as the tunnel endpoint.

4. Metro Ethernet service types appear frequently in scenario questions. E-Line = point-to-point, E-LAN = multipoint-to-multipoint (any-to-any), E-Tree = hub-and-spoke. Match the service type to the topology requirement.

5. IPsec Tunnel mode encapsulates the entire original IP packet inside a new outer IP packet. This is the mode used for site-to-site VPNs between routers, where the original source and destination addresses of the LAN hosts are hidden from the public internet.

6. A site-to-site VPN is always-on and connects entire networks (subnet to subnet). A remote access VPN connects individual users on demand. The CCNA tests the distinction between these two deployment models.

7. DMVPN is a Cisco-proprietary scalable VPN solution. The exam tests awareness: DMVPN uses GRE + NHRP + IPsec, supports spoke-to-spoke dynamic tunnels, and is scalable compared to full-mesh static VPN configurations. Full configuration syntax is not tested on CCNA.

8. Tunnel mode (not to be confused with transport mode) is the IPsec mode for network-to-network VPNs. It adds a new outer IP header pointing to the VPN endpoints, while the inner IP header carries the original LAN-to-LAN traffic.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] List the three Metro Ethernet service types and their topologies from memory
- [ ] Explain the difference between AH and ESP including what each provides and does not provide
- [ ] Write the complete GRE tunnel configuration from memory for two routers
- [ ] Explain why GRE is used with OSPF/EIGRP and why IPsec alone is insufficient for dynamic routing
- [ ] Describe IPsec transport mode vs tunnel mode and the use case for each
- [ ] Identify three common GRE tunnel failures and their fixes
- [ ] Complete the Module 09 Packet Tracer lab activity
- [ ] Post your Module 09 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com
