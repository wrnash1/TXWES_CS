# Video Script: Module 14 — Wireless Networking

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Estimated Duration: 23 Minutes

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash, and this is Module 14: Wireless Networking. Wireless is a significant CCNA exam topic — it falls under domain 2.0 Network Access and touches on concepts you will encounter in nearly every enterprise network you work in.

By the end of this module you will be able to:

* Identify the key characteristics of IEEE 802.11 wireless standards
* Explain WPA2 and WPA3 security protocols
* Describe the difference between autonomous and controller-based wireless architectures
* Understand the role of the Cisco Wireless LAN Controller
* Apply basic channel planning principles for 2.4 GHz and 5 GHz bands

Let's dive in.

---

## Segment 2: IEEE 802.11 Standards (1:30–6:00)

The IEEE 802.11 family defines how wireless LANs operate. Each amendment to the original 1997 standard has brought higher speeds, better range, or improved spectral efficiency. You need to know the key amendments for the CCNA exam.

### 802.11b

Released in 1999. Operates in the 2.4 GHz band. Maximum theoretical speed: 11 Mbps. Uses DSSS — Direct Sequence Spread Spectrum. This was the first widely deployed Wi-Fi standard. Largely obsolete today but still referenced on the exam for its characteristics.

### 802.11a

Also released in 1999 but less widely adopted initially. Operates in the 5 GHz band. Maximum speed: 54 Mbps. Uses OFDM — Orthogonal Frequency-Division Multiplexing. The 5 GHz band has more available channels and less interference from consumer devices, but shorter range due to higher frequency attenuation.

### 802.11g

Released in 2003. Operates in the 2.4 GHz band. Maximum speed: 54 Mbps. Uses OFDM like 802.11a but is backward compatible with 802.11b devices. Was the dominant standard through the mid-2000s.

### 802.11n — Wi-Fi 4

Released in 2009. Operates in both 2.4 GHz and 5 GHz. Maximum theoretical speed: 600 Mbps. Key innovation: MIMO — Multiple Input Multiple Output — which uses multiple antennas to send and receive multiple data streams simultaneously. Also introduced channel bonding using 40 MHz channels for higher throughput.

### 802.11ac — Wi-Fi 5

Released in 2013. Operates in 5 GHz only. Maximum theoretical speed: 6.9 Gbps. Key innovations: MU-MIMO allowing simultaneous transmission to multiple clients, wider channels up to 160 MHz, and up to 8 spatial streams. Became the dominant enterprise standard through the late 2010s.

### 802.11ax — Wi-Fi 6 and Wi-Fi 6E

Released in 2019. Operates in 2.4 GHz, 5 GHz, and — for Wi-Fi 6E — 6 GHz. Maximum theoretical speed: 9.6 Gbps. Key innovations: OFDMA — Orthogonal Frequency-Division Multiple Access — which divides channels into smaller Resource Units to serve multiple clients simultaneously within a single transmission. Also introduced BSS Coloring to reduce co-channel interference and Target Wake Time to improve battery life on IoT devices.

### 802.11 Standards Summary Table

| Standard | Band | Max Speed | Key Technology | Wi-Fi Name |
|---|---|---|---|---|
| 802.11b | 2.4 GHz | 11 Mbps | DSSS | — |
| 802.11a | 5 GHz | 54 Mbps | OFDM | — |
| 802.11g | 2.4 GHz | 54 Mbps | OFDM | — |
| 802.11n | 2.4/5 GHz | 600 Mbps | MIMO, OFDM | Wi-Fi 4 |
| 802.11ac | 5 GHz | 6.9 Gbps | MU-MIMO, OFDM | Wi-Fi 5 |
| 802.11ax | 2.4/5/6 GHz | 9.6 Gbps | OFDMA, MU-MIMO | Wi-Fi 6/6E |

---

## Segment 3: Wireless Security — WPA2 and WPA3 (6:00–10:00)

Wireless security has evolved considerably since the early days of WEP. For the CCNA exam you need to understand WPA2 and WPA3.

### WEP — What Went Wrong

WEP, Wired Equivalent Privacy, was the original 802.11 security protocol. It used RC4 encryption with a static key and was cracked in minutes using freely available tools. WEP is completely obsolete and should never be deployed.

### WPA and WPA2

WPA — Wi-Fi Protected Access — was an interim fix introduced in 2003 using TKIP encryption. WPA2, standardized in 2004 as IEEE 802.11i, introduced AES-CCMP encryption — the standard used in enterprise wireless to this day.

WPA2 operates in two modes:

* WPA2-Personal uses a pre-shared key. Everyone on the network shares the same passphrase. Good for home and small office, but weaker for enterprise because if one device is compromised, all devices are at risk.
* WPA2-Enterprise uses 802.1X and RADIUS authentication. Each user or device has unique credentials. The gold standard for enterprise deployments. Requires a RADIUS server such as Cisco ISE.

### WPA3

WPA3 was introduced in 2018 and addresses several WPA2 weaknesses. Key improvements:

* SAE — Simultaneous Authentication of Equals — replaces PSK with a more secure key exchange resistant to offline dictionary attacks even if an attacker captures the four-way handshake.
* 192-bit security suite — WPA3-Enterprise offers a 192-bit minimum security mode for high-security environments such as government and finance.
* Forward secrecy — Even if a long-term key is compromised, past sessions cannot be decrypted.
* OWE — Opportunistic Wireless Encryption — encrypts open networks without requiring a password. Used for public guest networks.

### Wireless Security Summary Table

| Standard | Encryption | Authentication |
|---|---|---|
| WEP | RC4 (broken) | Static key |
| WPA | TKIP | PSK or 802.1X |
| WPA2-Personal | AES-CCMP | PSK |
| WPA2-Enterprise | AES-CCMP | 802.1X/RADIUS |
| WPA3-Personal | AES-CCMP + SAE | SAE |
| WPA3-Enterprise | AES-GCMP-256 | 802.1X/RADIUS |

---

## Segment 4: Autonomous vs. Controller-Based Architecture (10:00–14:30)

When you deploy Wi-Fi in an enterprise you have two fundamental architectural choices: autonomous access points or a controller-based architecture.

### Autonomous Access Points

An autonomous AP is a self-contained device that handles all wireless functions independently. Each AP has its own configuration stored locally, manages its own RF settings, and authenticates clients locally or against a RADIUS server directly.

This works for very small deployments — a single office with two or three APs. But imagine managing 200 APs individually. You would have to log into each one separately to change the SSID password, update firmware, or adjust radio settings. Autonomous APs do not scale to enterprise environments.

### Controller-Based Architecture

In a controller-based architecture, lightweight access points — LAPs — offload most intelligence to a Wireless LAN Controller. The APs use the CAPWAP protocol — Control and Provisioning of Wireless Access Points — to communicate with the WLC.

CAPWAP uses two UDP tunnels:

* UDP 5246 carries control traffic — configuration, firmware updates, and management
* UDP 5247 carries client data traffic when the data plane is centralized at the WLC

The WLC provides centralized configuration management, automatic RF optimization, seamless client roaming, consistent security policy enforcement, and guest WLAN management with web authentication portals.

### Split-MAC Architecture

In a controller-based system, the MAC layer functions are divided between the AP and the WLC:

* The AP handles real-time functions — beacons, probe responses, and encryption and decryption of data frames
* The WLC handles non-real-time functions — client association, authentication, roaming decisions, and RF management

This split allows the WLC to maintain a global view of all clients and RF conditions across the entire wireless network.

---

## Segment 5: Cisco WLC Configuration Concepts (14:30–18:30)

The Cisco Wireless LAN Controller manages lightweight APs and provides a centralized GUI for WLAN management. Let's walk through the key configuration components.

### WLAN Configuration on the WLC

WLANs on the WLC are numbered 1 through 512. Each WLAN has an SSID, a security policy (WPA2-Personal, WPA2-Enterprise, WPA3, or Open), a VLAN mapping via a dynamic interface, a QoS profile, and optionally a RADIUS server assignment for 802.1X authentication.

For the CCNA exam you should understand the GUI workflow and the key parameters rather than WLC CLI commands, since WLC configuration is primarily GUI-driven.

### AP Operating Modes

Cisco lightweight APs can operate in several modes:

* Local mode is the default. The AP serves clients and performs background scanning on other channels during off-channel periods.
* Monitor mode: the AP does not serve clients. It is dedicated to scanning all channels for rogue APs and security threats.
* Sniffer mode: the AP captures all 802.11 frames and forwards them to a Wireshark packet analyzer on a remote host.
* Rogue Detector: the AP listens on the wired network to correlate rogue APs detected on wireless with rogue devices seen on the wire.
* FlexConnect: the AP can switch traffic locally when the WLC connection is lost. Good for branch offices with unreliable WAN links.

### AP Discovery and Join Process

When a lightweight AP powers on it follows this process to find its WLC:

1. AP sends a CAPWAP Discovery Request broadcast on the local subnet.
2. AP checks DHCP Option 43 — DHCP can provide the WLC IP address in Option 43.
3. AP performs a DNS lookup for CISCO-CAPWAP-CONTROLLER.localdomain.
4. AP checks NVRAM for a previously known WLC IP address.
5. WLC responds with a Discovery Response and the AP negotiates a CAPWAP tunnel.

---

## Segment 6: Channel Planning (18:30–21:30)

Channel planning is critical for wireless performance. Co-channel interference — multiple APs using the same channel in overlapping coverage areas — is the primary cause of wireless performance degradation in enterprise deployments.

### 2.4 GHz Band

The 2.4 GHz band has 11 channels in the US (channels 1 through 11). Each channel is 22 MHz wide with only 5 MHz center-to-center spacing, which means most channels overlap significantly. Only channels 1, 6, and 11 are non-overlapping. In any dense deployment, every AP must use only channels 1, 6, or 11.

### 5 GHz Band

The 5 GHz band has many more non-overlapping channels — up to 24 in the US depending on regulatory domain. This is one of the primary advantages of 5 GHz over 2.4 GHz for enterprise deployments. Common non-overlapping 20 MHz channels include 36, 40, 44, 48, 52, 56, 60, and 64 in the UNII-1 and UNII-2 bands.

### Channel Width Tradeoffs

* 20 MHz channels are standard width, most compatible, and produce the lowest co-channel interference. Best for dense deployments.
* 40 MHz bonds two channels to double throughput but halves the available non-overlapping channels.
* 80 MHz is used by 802.11ac and is suitable for high throughput in low-density areas.
* 160 MHz offers maximum throughput for 802.11ac/ax but is practical only in very low-density environments.

For dense enterprise deployments, 20 MHz in 2.4 GHz and 40 MHz in 5 GHz are typical best practice.

### Transmit Power Considerations

APs should use the minimum transmit power necessary to cover the intended area. Excessive transmit power increases co-channel interference with neighboring APs. Cisco's Radio Resource Management feature on the WLC automatically adjusts power and channel assignments dynamically based on real-time RF conditions.

---

## Segment 7: Module Summary (21:30–23:00)

This module covered the foundational wireless networking concepts you need for the CCNA exam.

The 802.11 standard family progressed from 802.11b at 11 Mbps in 2.4 GHz through 802.11ax at 9.6 Gbps across 2.4, 5, and 6 GHz. Key technology milestones: OFDM in 802.11a/g, MIMO in 802.11n, MU-MIMO in 802.11ac, and OFDMA in 802.11ax.

WPA2 uses AES-CCMP and supports both Personal (PSK) and Enterprise (802.1X/RADIUS) modes. WPA3 adds SAE for stronger personal authentication, forward secrecy, and OWE for encrypted open networks.

Autonomous APs work independently and do not scale. Controller-based architectures use CAPWAP on UDP 5246 and 5247 to centralize management on the WLC. The MAC layer is split between the AP for real-time functions and the WLC for non-real-time functions.

Channel planning in 2.4 GHz is restricted to channels 1, 6, and 11 to avoid co-channel interference. The 5 GHz band offers many more non-overlapping channels and is preferred for high-density enterprise deployments.

Your lab this module puts you inside Packet Tracer configuring a WLC and associating lightweight APs. Module 15 moves us into network automation and programmability. See you there.

---

Script End — Module 14 | Approximate runtime: 23 minutes
