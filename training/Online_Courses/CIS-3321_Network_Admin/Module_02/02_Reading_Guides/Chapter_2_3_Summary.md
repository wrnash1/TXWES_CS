# Reading Guide: Chapters 2 & 3 - Network Implementations
**Course:** CIS 3321 - Network Administration
**Certification Alignment:** CompTIA Network+ (N10-008) Domain 2.0

## High-Yield Concepts
Focus on the following concepts to prepare for the Domain 2.0 section of the Network+ exam.

### 1. Networking Devices at the OSI Layers
You must know exactly which device operates at which layer:
*   **Layer 1 (Physical):** Hubs, Repeaters, Cables.
*   **Layer 2 (Data Link):** Switches, Bridges, Access Points. (They make forwarding decisions based on **MAC Addresses**).
*   **Layer 3 (Network):** Routers, Layer 3 Switches. (They make routing decisions based on **IP Addresses**).
*   **Layer 7 (Application):** Firewalls, Proxies, Load Balancers.

### 2. IPv4 Address Classes (Legacy but tested)
*   **Class A:** 1.0.0.0 to 126.255.255.255 (Default mask /8)
*   **Class B:** 128.0.0.0 to 191.255.255.255 (Default mask /16)
*   **Class C:** 192.0.0.0 to 223.255.255.255 (Default mask /24)
*   *Note: 127.x.x.x is reserved for the loopback address (testing your own NIC).*

### 3. Private IP Address Ranges (RFC 1918)
These addresses cannot be routed on the public internet. You **MUST** memorize these:
*   **10.x.x.x:** 10.0.0.0 - 10.255.255.255 (1 private Class A network)
*   **172.16.x.x:** 172.16.0.0 - 172.31.255.255 (16 private Class B networks)
*   **192.168.x.x:** 192.168.0.0 - 192.168.255.255 (256 private Class C networks)

### 4. IPv6 Basics
IPv4 addresses ran out. IPv6 solves this.
*   IPv6 addresses are **128 bits** long (compared to IPv4's 32 bits).
*   They are written in Hexadecimal (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
*   **Link-Local Address:** Starts with `fe80::`. Every IPv6 device automatically generates one of these to talk to devices on the same local network.

## Key Terms Glossary
*   **VLAN (Virtual LAN):** Logically separating a single physical switch into multiple isolated broadcast domains.
*   **802.1Q:** The IEEE standard for VLAN trunking (tagging frames with their VLAN ID).
*   **ARP (Address Resolution Protocol):** The protocol used to find the MAC address associated with a known IP address.
*   **PoE (Power over Ethernet):** Sending electrical power over standard Cat5e/Cat6 ethernet cables to power devices like IP cameras or Access Points (802.3af/at standards).
