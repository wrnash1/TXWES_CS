# Quiz: Module 14 — Wireless Networking

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points.

---

## Question 1

Which IEEE 802.11 amendment was the first to introduce MIMO technology and dual-band operation in both 2.4 GHz and 5 GHz?

A. 802.11a

B. 802.11g

C. 802.11n

D. 802.11ac

Correct Answer: C — 802.11n (Wi-Fi 4), released in 2009, introduced MIMO — Multiple Input Multiple Output — and was the first standard to support both 2.4 GHz and 5 GHz bands. It also introduced 40 MHz channel bonding for higher throughput up to 600 Mbps.

Distractor Analysis:

* A — 802.11a operates only in the 5 GHz band and uses OFDM but not MIMO. Max speed is 54 Mbps.
* B — 802.11g operates in 2.4 GHz only, uses OFDM, and does not support MIMO. Max speed is 54 Mbps.
* D — 802.11ac introduced MU-MIMO but operates in 5 GHz only and was released in 2013, after 802.11n.

---

## Question 2

A wireless engineer is designing an enterprise network that requires each employee to authenticate with their individual Active Directory credentials before gaining Wi-Fi access. Which wireless security mode meets this requirement?

A. WPA2-Personal with a strong passphrase

B. WPA3-Personal with SAE

C. WPA2-Enterprise with 802.1X

D. WEP with dynamic key rotation

Correct Answer: C — WPA2-Enterprise with 802.1X uses a RADIUS server to authenticate each user or device individually against a credential store such as Active Directory. This provides per-user authentication, unlike PSK modes where everyone shares the same password.

Distractor Analysis:

* A — WPA2-Personal uses a shared PSK. All employees would share one password, which is not per-user authentication.
* B — WPA3-Personal with SAE is stronger than WPA2-PSK but still uses a shared key, not individual credentials.
* D — WEP is completely broken and should never be used regardless of key rotation.

---

## Question 3

What is the primary security advantage of WPA3-SAE over WPA2-PSK?

A. WPA3-SAE uses a longer encryption key (256-bit vs. 128-bit).

B. WPA3-SAE is resistant to offline dictionary attacks even if the authentication handshake is captured.

C. WPA3-SAE does not require a password, eliminating brute-force risk entirely.

D. WPA3-SAE encrypts only the management frames, while WPA2-PSK encrypts all frames.

Correct Answer: B — WPA3-SAE uses the Dragonfly key exchange protocol. Even if an attacker captures the SAE handshake, they cannot use it for offline dictionary attacks to guess the password. WPA2-PSK's four-way handshake can be captured and attacked offline.

Distractor Analysis:

* A — Both WPA2-Personal and WPA3-Personal use 128-bit AES-CCMP. WPA3-Enterprise adds a 192-bit mode, but that does not apply to WPA3-Personal.
* C — WPA3-SAE still uses a password; SAE changes the key exchange mathematics, not the presence of a password.
* D — Both WPA2 and WPA3 encrypt data frames. SAE specifically strengthens the key derivation process.

---

## Question 4

An enterprise is deploying wireless APs across 50 branch offices. The network team wants centralized configuration management, automatic channel selection, and seamless client roaming. Which architecture should they choose?

A. Autonomous APs with individual CLI configuration at each site

B. Controller-based architecture with lightweight APs and a Cisco WLC

C. Autonomous APs managed via a central TFTP server for configuration files

D. Standalone APs with WPA2-Enterprise providing centralized management

Correct Answer: B — A controller-based architecture with a Cisco WLC centralizes all configuration, RF management (including automatic channel selection via RRM), and client roaming management. Lightweight APs offload intelligence to the WLC via CAPWAP tunnels.

Distractor Analysis:

* A — Autonomous APs require individual management. With 50 sites this does not scale and provides no automatic channel management or seamless roaming.
* C — TFTP can deploy configuration files but does not provide centralized RF management, roaming, or real-time policy enforcement.
* D — WPA2-Enterprise provides authentication security, not wireless infrastructure management. It has no bearing on channel selection or roaming.

---

## Question 5

Which two UDP ports does CAPWAP use, and what type of traffic does each carry?

A. UDP 5246 for data traffic; UDP 5247 for control traffic

B. UDP 5246 for control traffic; UDP 5247 for data traffic

C. UDP 1812 for control traffic; UDP 1813 for data traffic

D. UDP 5246 for both control and data traffic using DSCP markings to differentiate

Correct Answer: B — CAPWAP uses UDP 5246 for the control tunnel (configuration, firmware, keepalives between AP and WLC) and UDP 5247 for the data tunnel (client data frames when centrally switched through the WLC).

Distractor Analysis:

* A — This reverses the port assignments. 5246 is always control; 5247 is always data.
* C — UDP 1812 and 1813 are RADIUS authentication and accounting ports, not CAPWAP.
* D — CAPWAP uses two separate UDP ports; it does not multiplex both functions on a single port.

---

## Question 6

In a Cisco controller-based wireless deployment using split-MAC architecture, which function is handled by the access point rather than the WLC?

A. Client association processing

B. Roaming database management

C. Encryption and decryption of data frames

D. RF power level adjustment

Correct Answer: C — In split-MAC, the AP handles real-time functions that cannot tolerate latency — including encryption and decryption of 802.11 data frames, beacon generation, and probe responses. The WLC handles non-real-time functions like association, roaming, and RF management.

Distractor Analysis:

* A — Client association processing is a non-real-time function handled by the WLC in split-MAC.
* B — Roaming database management is centralized at the WLC, which maintains a global client view.
* D — RF power adjustment is part of RRM and is managed by the WLC, not the individual AP.

---

## Question 7

Which 802.11 amendment introduced OFDMA to improve efficiency in high-density client environments?

A. 802.11n

B. 802.11ac

C. 802.11ax

D. 802.11g

Correct Answer: C — 802.11ax (Wi-Fi 6) introduced OFDMA — Orthogonal Frequency-Division Multiple Access. OFDMA divides each channel into smaller Resource Units, allowing an AP to transmit to multiple clients simultaneously within a single channel, significantly improving efficiency in dense environments.

Distractor Analysis:

* A — 802.11n introduced MIMO and channel bonding but uses OFDM, not OFDMA.
* B — 802.11ac uses OFDM with MU-MIMO for multi-user capability but not OFDMA.
* D — 802.11g uses OFDM on a single-user basis. No multi-user or multi-access enhancements.

---

## Question 8

A network administrator is planning channel assignments for a 2.4 GHz wireless deployment with six APs in close physical proximity. Which set of channels should be used to minimize co-channel interference?

A. Channels 1, 2, 3, 4, 5, 6

B. Channels 1, 6, and 11 only, rotating among the six APs

C. Channels 1, 4, 7, 10, 1, 4

D. Any six consecutive channels starting at channel 1

Correct Answer: B — In the 2.4 GHz band, only channels 1, 6, and 11 are non-overlapping. In a dense deployment all APs must use only these three channels, rotating the assignments among adjacent APs to minimize co-channel interference. Adjacent APs on the same channel interfere severely.

Distractor Analysis:

* A — Channels 1 through 6 all overlap with each other significantly. Using consecutive channels causes maximum interference.
* C — Channels 4, 7, and 10 overlap with channels 1, 6, and 11 respectively. This pattern does not create non-overlapping cells.
* D — Any set of consecutive channels in 2.4 GHz will overlap; only channels 1, 6, 11 have non-overlapping spacing.

---

## Question 9

A lightweight AP has just been powered on and is searching for its WLC. In what order does the AP use the following discovery methods?

A. DNS lookup → DHCP Option 43 → broadcast → NVRAM

B. Broadcast → DHCP Option 43 → DNS lookup → NVRAM

C. NVRAM → broadcast → DHCP Option 43 → DNS lookup

D. DHCP Option 43 → broadcast → NVRAM → DNS lookup

Correct Answer: B — The standard AP discovery sequence is: (1) broadcast CAPWAP Discovery Request on the local subnet, (2) check DHCP Option 43 for WLC IP, (3) DNS lookup for CISCO-CAPWAP-CONTROLLER, (4) check NVRAM for a previously joined WLC. Note that Packet Tracer may simplify this sequence.

Distractor Analysis:

* A — DNS does not precede DHCP Option 43 in the Cisco AP join process.
* C — NVRAM is checked last (or as a fallback), not first.
* D — DHCP Option 43 is not the first method. Broadcast is attempted first on the local subnet.

---

## Question 10

A Cisco lightweight AP is configured in FlexConnect mode at a remote branch office. The WAN link to the WLC fails. What happens to wireless clients connected to this AP?

A. All clients are immediately deauthenticated and must reconnect when the WLC is reachable.

B. The AP reboots and enters standalone mode using factory default settings.

C. The AP continues to serve clients using its locally cached configuration.

D. The AP forwards all traffic to the nearest autonomous AP for processing.

Correct Answer: C — FlexConnect mode allows APs to cache WLAN configuration and continue serving clients locally even when the CAPWAP tunnel to the WLC is unavailable. Client data is switched locally to the branch LAN. This is specifically why FlexConnect is used at remote sites with unreliable WAN links.

Distractor Analysis:

* A — This describes the behavior of a Local mode AP, not FlexConnect. In Local mode, clients would lose connectivity when the WLC tunnel drops.
* B — FlexConnect APs do not reboot when the WLC becomes unreachable; they enter a connected-standalone state using cached config.
* D — APs do not forward traffic to other APs for processing; each AP handles its own clients independently.

---

---

## Question 11

An 802.11ac wireless client associates with an AP and negotiates a connection using only a single spatial stream with a 40 MHz channel. A second client associates with the same AP using three spatial streams with an 80 MHz channel. What correctly describes the difference in their maximum PHY rates?

A. Both clients achieve the same maximum PHY rate because they share the same AP.

B. The three-stream 80 MHz client achieves a significantly higher maximum PHY rate than the single-stream 40 MHz client.

C. The single-stream 40 MHz client achieves a higher rate because narrower channels have less interference.

D. Channel width has no effect on PHY rate — only the number of spatial streams determines throughput.

Correct Answer: B — 802.11ac PHY rate depends on two primary factors: the number of spatial streams (MIMO) and the channel width. More spatial streams and wider channels multiply the available throughput. A three-stream 80 MHz configuration achieves far greater maximum PHY rate than a single-stream 40 MHz configuration. For reference, 802.11ac single-stream 40 MHz = ~200 Mbps; three-stream 80 MHz ≈ 1.3 Gbps.

Distractor Analysis:

* A — Clients on the same AP negotiate independently. Each client's PHY rate is determined by its own negotiated parameters, not a shared rate.
* C — Narrower channels reduce the frequency resource available for data, directly limiting maximum PHY rate. Wider channels provide more subcarriers and higher throughput, assuming signal quality is sufficient.
* D — Both spatial streams and channel width significantly affect PHY rate. Ignoring channel width is incorrect.

---

## Question 12

A wireless client is associated with an AP on channel 6 in the 2.4 GHz band. A neighboring AP is operating on channel 8. What type of interference does this cause?

A. Co-channel interference — both APs are competing for the same non-overlapping channel.

B. Adjacent-channel interference — channels 6 and 8 overlap in frequency, causing interference.

C. Multipath interference — the signal bounces between the two APs before reaching the client.

D. No interference — channels 6 and 8 are always at least 5 MHz apart and do not overlap.

Correct Answer: B — In the 2.4 GHz band, each channel is 22 MHz wide but spaced only 5 MHz apart. Channels 6 and 8 overlap significantly in frequency range — a channel must be at least 5 channels away (25 MHz) to be non-overlapping. Channels 6 and 8 are only 2 channels (10 MHz) apart, causing adjacent-channel interference, which is actually more damaging than co-channel interference because it produces partial overlapping signals that cannot be decoded cleanly.

Distractor Analysis:

* A — Co-channel interference occurs when two APs use exactly the same channel. Channels 6 and 8 are different channels, so this is adjacent-channel, not co-channel interference.
* C — Multipath is caused by signal reflections from objects in the environment, not by two APs on different channels.
* D — Channels 6 and 8 are not sufficiently separated. Only channels 1, 6, and 11 are non-overlapping in the North American 2.4 GHz band.

---

## Question 13

Which wireless AP deployment mode is most appropriate for an AP located at a small branch office that must continue serving local clients even when the CAPWAP tunnel to the WLC is down?

A. Local mode

B. Monitor mode

C. FlexConnect mode

D. Sniffer mode

Correct Answer: C — FlexConnect (previously called HREAP — Hybrid Remote Edge AP) is specifically designed for remote branch deployments. When the WAN link to the WLC goes down, a FlexConnect AP enters connected-standalone mode and continues forwarding traffic using its cached WLAN configuration. Client data is switched locally to the branch LAN, not through the WLC tunnel.

Distractor Analysis:

* A — Local mode APs require a continuous CAPWAP tunnel to the WLC. If the tunnel drops, clients are deauthenticated and lose connectivity.
* B — Monitor mode is a passive mode where the AP only listens to traffic for intrusion detection and rogue AP detection. It does not serve clients.
* D — Sniffer mode captures 802.11 frames for analysis by tools like Wireshark. It does not serve wireless clients in any mode.

---

## Question 14

A network engineer observes that several wireless clients have poor connectivity when located far from the AP, even though the AP's transmit power is at maximum. What 802.11 mechanism allows the AP to negotiate a lower data rate with distant clients to maintain the connection?

A. OFDMA resource unit allocation

B. Dynamic Rate Shifting (DRS)

C. Beamforming

D. Band steering

Correct Answer: B — Dynamic Rate Shifting (also called rate adaptation or link adaptation) is the mechanism by which an 802.11 client and AP dynamically negotiate a lower modulation and coding scheme (MCS) as signal quality degrades with distance or interference. Lower rates (e.g., 6 Mbps) are more robust than higher rates (e.g., 300 Mbps) because they use simpler modulation that requires less SNR.

Distractor Analysis:

* A — OFDMA (used in 802.11ax) divides channels into resource units for multi-user access. It improves efficiency in dense environments but does not specifically address the distance-related rate degradation scenario.
* C — Beamforming focuses the transmitted signal in the direction of the client to improve signal strength. While it can help with distance, DRS is the specific mechanism that adjusts the data rate in response to changing signal conditions.
* D — Band steering encourages dual-band clients to prefer the 5 GHz band over 2.4 GHz. It does not adjust transmission rates for distant clients.

---

## Question 15

In a Cisco WLC-based deployment, a network administrator creates a WLAN and maps it to a VLAN interface on the WLC. What is the purpose of this VLAN mapping?

A. It allows the WLC to enforce 802.1X authentication for each client separately per VLAN.

B. It ensures that client traffic from that WLAN is tagged with the corresponding VLAN ID when it exits the WLC toward the distribution switch.

C. It maps wireless channels to VLANs to prevent co-channel interference.

D. It binds the SSID name to a specific AP group so the SSID is only broadcast by designated APs.

Correct Answer: B — In a centrally switched (Local mode) deployment, all client data from an AP is tunneled via CAPWAP to the WLC. At the WLC, each WLAN is mapped to a specific VLAN interface. When the WLC sends the client's traffic to the wired network, it tags it with the VLAN ID of the mapped interface. This integrates wireless traffic into the correct Layer 2 segment on the wired network, enabling routing and policy enforcement by VLAN.

Distractor Analysis:

* A — 802.1X authentication is configured separately in the WLAN security settings, not through VLAN mapping. VLAN mapping determines where client traffic goes, not how clients authenticate.
* C — VLAN assignment and RF channel assignment are entirely separate settings. Channels are managed by the RRM subsystem.
* D — AP group assignments control which APs broadcast which SSIDs. This is a separate configuration from WLAN-to-VLAN interface mapping.

---

## Question 16

An enterprise deploys both 2.4 GHz and 5 GHz radios on all APs. A dual-band capable laptop connects to the 2.4 GHz band even though the 5 GHz band is available. Which WLC feature encourages dual-band clients to connect to the 5 GHz band instead?

A. RRM (Radio Resource Management)

B. Band steering

C. FlexConnect

D. Client load balancing

Correct Answer: B — Band steering is a WLC feature that detects dual-band capable clients and encourages them to associate with the 5 GHz radio rather than the 2.4 GHz radio. The WLC can delay or decline probe responses on 2.4 GHz for dual-band clients to push them toward the less-congested 5 GHz band, which offers more non-overlapping channels and typically less interference.

Distractor Analysis:

* A — RRM manages AP transmit power and channel selection to minimize interference. It does not influence which band individual clients connect to.
* C — FlexConnect is an AP deployment mode for remote branches. It has nothing to do with band preference for individual clients.
* D — Client load balancing distributes clients across multiple APs to prevent one AP from becoming overloaded. It does not steer clients between frequency bands.

---

## Question 17

A new lightweight AP is added to an enterprise network. The WLC is on a different subnet than the AP's management VLAN. DHCP is configured with Option 43 on the AP's VLAN pointing to the WLC's management IP. After the AP receives a DHCP lease, it still fails to join the WLC. What is the most likely cause?

A. The CAPWAP control UDP port 5246 is being blocked by an ACL between the AP and WLC.

B. The AP must be in autonomous mode before being converted to lightweight mode by the WLC.

C. Option 43 can only provide the WLC IP if the WLC is on the same subnet as the AP.

D. The AP cannot use DHCP to discover the WLC — a static IP must be assigned to the AP.

Correct Answer: A — CAPWAP uses UDP 5246 (control) and 5247 (data) between the AP and WLC. If any ACL or firewall between the AP's subnet and the WLC's subnet is blocking these UDP ports, the CAPWAP tunnel cannot be established. DHCP Option 43 successfully delivered the WLC IP (the AP knows where to go) but the CAPWAP session cannot complete. Verifying and permitting UDP 5246/5247 in any inter-VLAN ACL resolves this.

Distractor Analysis:

* B — Lightweight APs ship from Cisco ready to run LWAPP/CAPWAP. They do not need to be in autonomous mode first. Conversion goes the other direction (autonomous to lightweight using the conversion tool).
* C — DHCP Option 43 works across subnets — it is a DHCP option delivered in the DHCP response, which can already traverse subnets via a relay agent. The WLC can be on any routable subnet.
* D — Lightweight APs can use DHCP for their management IP. Using a static IP is optional, not required, and does not affect WLC discovery when Option 43 or other discovery methods are available.

---

## Question 18

A wireless network uses WPA2-Enterprise with EAP-TLS authentication. Which statement correctly describes EAP-TLS?

A. EAP-TLS requires only a server-side certificate — clients authenticate with username and password.

B. EAP-TLS requires mutual certificate authentication — both the client and the authentication server present digital certificates.

C. EAP-TLS is the same as WPA3-SAE but uses TLS for the key exchange instead of Dragonfly.

D. EAP-TLS is used only for IoT devices because it requires no user interaction during authentication.

Correct Answer: B — EAP-TLS (Extensible Authentication Protocol — Transport Layer Security) is the strongest EAP method. It requires mutual certificate authentication: the RADIUS/authentication server presents a certificate to the client, AND the client presents a certificate to the server. This makes it highly secure but also operationally complex because each client device must have a valid certificate installed. PEAP, by contrast, requires only a server-side certificate.

Distractor Analysis:

* A — Describes PEAP (Protected EAP), where only the server presents a certificate and clients authenticate with username/password inside the TLS tunnel. EAP-TLS requires both sides to present certificates.
* C — EAP-TLS and WPA3-SAE are completely different protocols addressing different security goals. EAP-TLS is used in WPA2/WPA3-Enterprise for user/device authentication; SAE is used in WPA3-Personal for password-based key exchange.
* D — EAP-TLS requires a certificate on every device, which is typically managed for employees and corporate devices. It is often used for corporate laptops, not IoT devices (which typically use MAB or simpler methods due to certificate management complexity).

---

## Question 19

Which command on a Cisco WLC CLI verifies the number of APs currently associated to the controller?

A. `show ap summary`

B. `show wlan summary`

C. `show interface summary`

D. `show capwap connections`

Correct Answer: A — `show ap summary` on the WLC CLI displays a list of all associated APs including their name, AP model, number of clients, state (Registered), and the CAPWAP tunnel uptime. This is the primary command to verify AP registration status.

Distractor Analysis:

* B — `show wlan summary` lists configured WLANs (SSIDs), their IDs, status, and security profile. It shows WLAN configuration, not AP registration.
* C — `show interface summary` lists WLC logical interfaces (management, AP-manager, VLAN interfaces). It does not show AP connection status.
* D — `show capwap connections` is not a standard WLC CLI command. CAPWAP tunnel status is verified through `show ap summary` and `show ap join stats summary`.

---

## Question 20

An organization needs to deploy a wireless network in a large open warehouse with high ceilings and metal shelving that causes significant multipath reflection. Which antenna type is most appropriate for the APs mounted near the ceiling to provide even coverage throughout the warehouse floor?

A. Directional Yagi antennas aimed across the length of the warehouse

B. Omnidirectional antennas providing 360-degree horizontal coverage from ceiling-mounted APs

C. Patch antennas mounted on the metal shelving units pointed toward the center aisle

D. Dipole antennas mounted externally on the building's exterior walls

Correct Answer: B — Ceiling-mounted APs in an open warehouse benefit from omnidirectional antennas that radiate signal in 360 degrees horizontally and in a donut-shaped pattern vertically. This provides uniform coverage across the warehouse floor from above without needing precise aiming. Cisco ceiling-mount APs with omnidirectional antennas are the standard solution for large open floor environments.

Distractor Analysis:

* A — Yagi antennas are highly directional with a narrow beam. They are ideal for point-to-point links or outdoor long-distance connections, not for blanketing a wide floor area with even coverage.
* C — Mounting antennas on metal shelving in a warehouse introduces RF interference from the metal itself and creates unpredictable coverage patterns. Ceiling mounting is the preferred approach.
* D — Exterior wall mounting with dipole antennas would result in the signal primarily being directed toward the inside wall, not uniformly distributed across the warehouse interior. Indoor ceiling mounting is the correct approach.

---

End of Quiz — Module 14
