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

End of Quiz — Module 14
