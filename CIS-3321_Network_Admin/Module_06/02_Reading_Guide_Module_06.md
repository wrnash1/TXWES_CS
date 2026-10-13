# Reading Guide: Module 06 – Wireless Networking: 802.11 Standards and Security
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 06 covers wireless networking — a significant portion of the CompTIA Network+ exam. You must know the 802.11 standard generations by name, frequency band, maximum theoretical speed, and key features. Equally important are wireless security protocols — the exam tests your ability to identify which encryption standard is appropriate and recognize the vulnerabilities of legacy protocols. Channel planning and the difference between WPA2-Personal and WPA2-Enterprise are directly tested.

---

### 1. Core Vocabulary

**802.11a** — 5 GHz only; 54 Mbps maximum; OFDM modulation. Less range than 2.4 GHz standards.

**802.11b** — 2.4 GHz only; 11 Mbps maximum; DSSS modulation. Legacy standard with good range.

**802.11g** — 2.4 GHz only; 54 Mbps maximum; OFDM. Backward compatible with 802.11b.

**802.11n (Wi-Fi 4)** — 2.4 GHz and 5 GHz dual-band; up to 600 Mbps; MIMO (up to 4 spatial streams); introduced channel bonding (40 MHz channels).

**802.11ac (Wi-Fi 5)** — 5 GHz only; up to 3.5 Gbps; MU-MIMO; beamforming; channels up to 160 MHz.

**802.11ax (Wi-Fi 6)** — 2.4, 5, and 6 GHz; up to 9.6 Gbps; OFDMA for multi-client efficiency in dense environments.

**Wi-Fi 6E** — Wi-Fi 6 extended to the newly opened 6 GHz band (1,200 MHz of new spectrum).

**MIMO** — Multiple-Input Multiple-Output. Uses multiple antennas to transmit multiple spatial streams simultaneously to increase throughput.

**MU-MIMO** — Multi-User MIMO. Allows an AP to communicate with multiple clients simultaneously rather than sequentially.

**OFDMA** — Orthogonal Frequency Division Multiple Access. Wi-Fi 6 feature dividing channels into sub-carriers (Resource Units) to serve multiple clients per transmission cycle.

**Beamforming** — AP focuses its radio signal toward a specific client device rather than broadcasting equally in all directions.

**SSID (Service Set Identifier)** — Human-readable wireless network name broadcast in beacon frames. Hiding the SSID provides negligible security benefit.

**BSS (Basic Service Set)** — A single AP and its associated clients. Identified by a BSSID (the AP's MAC address).

**ESS (Extended Service Set)** — Multiple APs sharing the same SSID, enabling seamless client roaming across a campus or building.

**IBSS (Independent Basic Service Set)** — Ad-hoc wireless network where devices communicate directly without an AP.

**WEP (Wired Equivalent Privacy)** — 1997 wireless encryption using RC4 with static 40-bit or 104-bit keys. Completely broken — crackable in minutes. Never use.

**WPA** — Wi-Fi Protected Access (2003). Uses TKIP (RC4-based with per-packet key mixing). Deprecated. Do not use.

**TKIP (Temporal Key Integrity Protocol)** — WPA encryption protocol using RC4 with per-packet key mixing. Deprecated.

**WPA2** — Current minimum standard (2004). Uses AES-CCMP. Two modes: Personal (PSK) and Enterprise (802.1X/RADIUS).

**AES-CCMP** — Advanced Encryption Standard with Counter Mode CBC-MAC Protocol. Used by WPA2. Block cipher with 128-bit keys. Currently unbroken by practical means.

**WPA3** — Current best practice (2018). Uses SAE (Simultaneous Authentication of Equals). Provides forward secrecy. WPA3-Enterprise uses 192-bit encryption.

**SAE (Simultaneous Authentication of Equals)** — WPA3 key exchange replacing PSK. Based on Dragonfly key exchange. Eliminates offline dictionary attacks and provides forward secrecy.

**Forward Secrecy** — A property where past sessions cannot be decrypted even if the long-term key (passphrase) is later compromised. WPA3 provides forward secrecy; WPA2-PSK does not.

**WPA2-Personal (PSK)** — Uses a shared pre-shared key. All users share the same passphrase. Simple to deploy; no individual credential tracking.

**WPA2-Enterprise (802.1X)** — Uses RADIUS server for individual user authentication via EAP. Each user has unique credentials that can be independently revoked.

**802.1X** — Port-based Network Access Control framework. Requires an authenticator (AP), a supplicant (client), and an authentication server (RADIUS). Used in both wired and wireless enterprise security.

**RADIUS** — Remote Authentication Dial-In User Service. Authentication server used in WPA2/WPA3-Enterprise. Receives credential validation requests from APs and returns approve/deny decisions.

**EAP (Extensible Authentication Protocol)** — Authentication framework used with 802.1X. Common types: EAP-TLS (certificate-based, highest security), PEAP (protected EAP, password-based).

**Captive Portal** — Web page presented to users on guest/public networks requiring acceptance of terms of service before internet access is granted.

**Evil Twin** — Rogue access point broadcasting the same SSID as a legitimate network to intercept user traffic.

**Deauthentication Attack** — Attacker sends forged deauthentication frames to disconnect clients from an AP. Used to capture WPA2 4-way handshake for offline cracking.

**802.11w (Management Frame Protection)** — Standard that authenticates 802.11 management frames to prevent deauthentication and disassociation attacks.

**WIPS (Wireless Intrusion Prevention System)** — System that detects and responds to unauthorized APs, clients, and wireless attacks.

**Channel** — A specific radio frequency sub-band used for wireless communication. In 2.4 GHz, 11 channels exist in the US; only channels 1, 6, and 11 are non-overlapping.

**Co-channel Interference** — Interference caused by two APs operating on the same or overlapping channels within range of each other.

**Omnidirectional Antenna** — Radiates signal equally in all horizontal directions. Used in most APs and client devices.

**Directional Antenna** — Focuses signal in a specific direction. Used for point-to-point building-to-building wireless links.

**CAPWAP** — Control and Provisioning of Wireless Access Points. Protocol used to manage multiple APs from a central Wireless LAN Controller (WLC). Uses DTLS encryption for control traffic.

---

### 2. 802.11 Standard Comparison Table

| Standard  | Common Name | Band(s)          | Max Speed    | Key Technology            |
|-----------|-------------|------------------|--------------|---------------------------|
| 802.11a   | —           | 5 GHz            | 54 Mbps      | OFDM                      |
| 802.11b   | —           | 2.4 GHz          | 11 Mbps      | DSSS                      |
| 802.11g   | —           | 2.4 GHz          | 54 Mbps      | OFDM; backward compat b   |
| 802.11n   | Wi-Fi 4     | 2.4 and 5 GHz    | 600 Mbps     | MIMO, 40 MHz channels     |
| 802.11ac  | Wi-Fi 5     | 5 GHz only       | 3.5 Gbps     | MU-MIMO, beamforming, 160 MHz |
| 802.11ax  | Wi-Fi 6/6E  | 2.4, 5, 6 GHz   | 9.6 Gbps     | OFDMA, improved MU-MIMO   |

---

### 3. Wireless Security Protocol Comparison Table

| Protocol  | Encryption    | Key Management            | Vulnerabilities                    | Status          |
|-----------|---------------|---------------------------|------------------------------------|-----------------|
| WEP       | RC4 (static)  | Static 40/104-bit key     | IV reuse, crackable in minutes     | Broken — never use |
| WPA       | TKIP (RC4)    | Per-packet key mixing     | TKIP vulnerabilities, deprecated   | Deprecated      |
| WPA2      | AES-CCMP      | PSK or 802.1X/RADIUS      | PSK offline dictionary attack      | Minimum standard |
| WPA3      | AES-GCMP-256  | SAE (Dragonfly)           | No known practical attacks         | Current best practice |

---

### 4. WPA2-Personal vs. WPA2-Enterprise

| Feature                    | WPA2-Personal (PSK)          | WPA2-Enterprise (802.1X)          |
|----------------------------|------------------------------|-----------------------------------|
| Authentication method      | Shared passphrase             | Individual credentials via RADIUS |
| Server required            | No                           | RADIUS authentication server      |
| Per-user credential revocation | No (must rekey all)       | Yes (revoke individual user)      |
| Audit trail                | None (shared key)            | Per-user authentication log       |
| Resistance to insider threat | Low                         | High                              |
| Deployment complexity      | Simple                       | Requires RADIUS infrastructure    |
| Best for                   | Home, small office            | Enterprise, education, healthcare |

---

### 5. Channel Planning — 2.4 GHz Non-Overlapping Channels

The 2.4 GHz band contains 11 channels in the US. Each channel is approximately 22 MHz wide. Channels are spaced 5 MHz apart. Only three channels are non-overlapping:

- Channel 1: Center frequency 2.412 GHz
- Channel 6: Center frequency 2.437 GHz
- Channel 11: Center frequency 2.462 GHz

When deploying multiple APs in the same area, assign channels 1, 6, and 11 in rotation. Never assign adjacent channels (e.g., 1, 2, 3) to neighboring APs.

The 5 GHz band has 24+ non-overlapping 20 MHz channels (regulatory domain dependent). This is one reason 5 GHz is preferred for high-density deployments.

---

### 6. Common Wireless Attacks Reference

| Attack                  | Description                                                  | Mitigation                                    |
|-------------------------|--------------------------------------------------------------|-----------------------------------------------|
| Evil Twin (Rogue AP)    | Attacker AP broadcasts legitimate SSID to intercept traffic  | 802.1X authentication, WIPS, certificate pinning |
| Deauth Flood            | Forged deauthentication frames disconnect clients            | 802.11w Management Frame Protection           |
| WPA2-PSK Dictionary     | Offline attack on captured 4-way handshake                   | Long passphrase; upgrade to WPA3-SAE          |
| War Driving             | Scanning for open/weak APs while mobile                      | WPA2-AES minimum; disable SSID broadcast      |
| SSID Spoofing           | Creating AP with same SSID as legitimate network             | WIPS; 802.1X (prevents credential capture)   |
| Captive Portal Phishing | Rogue captive portal harvests credentials                    | HTTPS-only portals; certificate validation    |

---

### 7. Certification Exam Tips

**Tip 1:** 802.11ac is 5 GHz ONLY. 802.11n is dual-band (2.4 AND 5 GHz). This is the most commonly tested distinction between the two standards.

**Tip 2:** Channels 1, 6, and 11 are the three non-overlapping channels in the US 2.4 GHz band. This is tested directly. Any answer with channels 1, 2, 3 or other combinations is wrong.

**Tip 3:** WPA2-AES is the minimum secure wireless configuration. WEP is completely broken and always the wrong answer in a security scenario. WPA-TKIP is deprecated.

**Tip 4:** WPA2-Enterprise with 802.1X/RADIUS allows individual credential revocation. WPA2-PSK does not. When the exam describes an enterprise needing to revoke one user's access, 802.1X is always the answer.

**Tip 5:** WPA3-SAE provides forward secrecy — previously captured traffic cannot be decrypted if the passphrase is later compromised. WPA2-PSK does not provide forward secrecy.

**Tip 6:** SSID hiding (disabling broadcast) provides virtually no security benefit. Clients still probe for the SSID, making it discoverable with passive monitoring.

**Tip 7:** 802.11w (Management Frame Protection) prevents deauthentication attacks by authenticating management frames. This is the specific mitigation for deauth flood attacks.

**Tip 8:** OFDMA is the key technology introduced by Wi-Fi 6 (802.11ax) for high-density environments. It allows multiple clients to use sub-channels simultaneously, reducing contention.

---

### 8. Required Reading and Viewing

**Required Reading:** Computer Networking: Principles, Protocols and Practice — read the sections on wireless networking standards and security. Focus on the 802.11 standard comparison and WPA2/WPA3 mechanisms.

**Required Viewing:** Professor Messer's Network+ N10-008 video series — watch the wireless standards and wireless security segments. Available free at professormesser.com.

**Supplemental Reference:** CompTIA official N10-008 exam objectives at comptia.org — review Domain 2.0 Network Implementations for wireless objectives.

---

### 9. Study Checklist

- [ ] Memorize the 802.11 standards table — name, frequency band, max speed, key technology
- [ ] Distinguish 802.11ac (5 GHz only) from 802.11n (dual-band) — this distinction is a common exam trap
- [ ] Know all four wireless security protocols (WEP, WPA, WPA2, WPA3) and the vulnerability of each
- [ ] Explain the difference between WPA2-Personal (PSK) and WPA2-Enterprise (802.1X/RADIUS)
- [ ] Memorize the three non-overlapping 2.4 GHz channels: 1, 6, and 11
- [ ] Describe the Evil Twin attack and the deauthentication attack with their mitigations
- [ ] Explain what forward secrecy means and which wireless standard provides it
- [ ] Watch Professor Messer's wireless standards and security videos at professormesser.com
- [ ] Read the wireless networking chapter in the OER textbook
- [ ] Complete the Lab 06 wireless scanning activity
- [ ] Post your Module 06 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 06 Quiz

---

## 9. Supplemental Resources

The following free resources extend Module 06 content on wireless standards, security, and RF fundamentals.

**1. Professor Messer — Wireless Networking Free Videos (N10-008)**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer covers 802.11 standards, WEP/WPA/WPA2/WPA3, wireless attacks (Evil Twin, deauthentication), and WIPS in videos directly aligned to Network+ exam objectives.

**2. Wi-Fi Alliance — Wi-Fi 6 and Wi-Fi 6E Technical Overview**
URL: https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-6
Relevance: The Wi-Fi Alliance's free official resources explain 802.11ax (Wi-Fi 6) improvements including OFDMA, MU-MIMO enhancements, and 6 GHz band introduction in Wi-Fi 6E. The definitive vendor-neutral source for Wi-Fi certification information.

**3. Cisco — Wireless LAN Design Guide (Free)**
URL: https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Mobility/WiFiDeployGuide.html
Relevance: Cisco's free enterprise wireless design guide covers channel planning, cell sizing, site survey methodology, and high-density wireless design — directly applicable to the exam objectives on wireless deployment planning.

**4. Wireshark 802.11 Wireless Packet Analysis**
URL: https://wiki.wireshark.org/CaptureSetup/WLAN
Relevance: Free Wireshark documentation on capturing 802.11 wireless frames in monitor mode. Capturing real 802.11 management frames (beacons, probe requests, authentication frames) reinforces the frame-level understanding of wireless protocols tested on the exam.

**5. IEEE 802.11 Standard Overview — IEEE Xplore (Free Summary)**
URL: https://standards.ieee.org/ieee/802.11/7028/
Relevance: The IEEE standards page for 802.11 provides free access to the standard summary and scope document. The full standard requires purchase, but the overview and amendment history clarify the evolution from 802.11a/b/g through 802.11ax.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
