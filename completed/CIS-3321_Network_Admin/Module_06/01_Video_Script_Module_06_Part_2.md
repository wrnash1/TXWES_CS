# Video Script: Module 06 – Wireless Networking: 802.11 Standards and Security
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 11–13 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 06 Part 2 — Wireless Security Protocols, WPA2/WPA3, and Wireless Threats"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 06. In Part 1 we covered the 802.11 standard generations, frequency band trade-offs, and channel planning. Now in Part 2 we tackle wireless security — the progression from WEP to WPA3, the difference between Personal and Enterprise modes, and the common wireless attacks you need to recognize for the exam.

---

### Section 2: Wireless Security — The Evolution from WEP to WPA3

[00:45 – 05:30]

[SHOW DIAGRAM: A timeline showing the progression of wireless security standards. Left to right: WEP (1997, RC4 static key, broken), WPA (2003, TKIP/RC4, deprecated), WPA2 (2004, AES-CCMP, current minimum), WPA3 (2018, SAE, current best practice).]

[Alt-text: A horizontal timeline diagram. From left to right: WEP introduced in 1997 using RC4 with static keys, labeled Completely Broken. WPA introduced in 2003 using TKIP with RC4, labeled Deprecated. WPA2 introduced in 2004 using AES-CCMP, labeled Current Minimum Standard. WPA3 introduced in 2018 using SAE (Simultaneous Authentication of Equals) and forward secrecy, labeled Current Best Practice.]

**WEP (Wired Equivalent Privacy)** — Introduced in 1997 as part of the original 802.11 standard. WEP uses the RC4 stream cipher with a static 40-bit or 104-bit key. The fundamental flaw: the same short initialization vector (IV) is reused frequently, making it trivially easy for an attacker to collect enough packets to crack the key mathematically. Free tools can crack WEP in under five minutes with sufficient traffic. WEP should never be used under any circumstances. Its presence on any network is a critical security vulnerability.

**WPA (Wi-Fi Protected Access)** — Introduced in 2003 as an emergency replacement for WEP. WPA uses TKIP (Temporal Key Integrity Protocol), which still uses RC4 underneath but adds per-packet key mixing and a message integrity check. This patched the most obvious WEP weaknesses without requiring new hardware, but TKIP has since been shown to have its own vulnerabilities. WPA-TKIP is deprecated and should not be used.

**WPA2** — Introduced in 2004 and became mandatory for all new Wi-Fi certified devices in 2006. WPA2 replaces TKIP with AES-CCMP — the Advanced Encryption Standard with Counter Mode CBC-MAC Protocol. AES is a block cipher standardized by NIST, and in WPA2 configuration it uses 128-bit encryption. WPA2 is the current minimum acceptable wireless security standard. WPA2-AES on its own is not crackable by practical means.

**WPA3** — Introduced in 2018. WPA3 replaces the Pre-Shared Key (PSK) handshake in Personal mode with SAE (Simultaneous Authentication of Equals) — based on Dragonfly key exchange. SAE eliminates the offline dictionary attack vulnerability of WPA2-PSK and provides forward secrecy — meaning even if the password is later compromised, previously captured traffic cannot be decrypted. WPA3-Enterprise uses 192-bit encryption. WPA3 is the current best practice for new deployments.

---

### Section 3: WPA2-Personal vs. WPA2-Enterprise

[05:30 – 08:00]

[SHOW DIAGRAM: Two topology diagrams side by side. Left: WPA2-Personal — a client connects to an AP using a shared passphrase (PSK). No server required. Right: WPA2-Enterprise — a client connects to an AP, which contacts a RADIUS server for authentication. The client provides individual credentials. The RADIUS server approves or denies access.]

[Alt-text: Two network diagrams. Left diagram is labeled WPA2-Personal. A client device connects to an AP labeled PSK, with a pre-shared passphrase shown between them and a label that reads "All users share the same passphrase." Right diagram is labeled WPA2-Enterprise. A client device connects to an AP, which connects to a RADIUS Authentication Server. The client provides individual username and password or certificate credentials. A label reads "Each user has unique credentials."]

WPA2 (and WPA3) offer two operational modes.

**Personal mode (WPA2-PSK)** — Uses a single shared passphrase configured on the access point. Every user knows the same password. Simple to set up and appropriate for small offices and home networks. Disadvantages: everyone knows the same key, revoking access for one user requires changing the password for everyone, and there is no per-user audit trail.

**Enterprise mode (WPA2-Enterprise / WPA2-802.1X)** — Uses 802.1X authentication with a RADIUS (Remote Authentication Dial-In User Service) server. Each user authenticates with individual credentials — typically a username and password, or digital certificates. The AP acts as an authenticator, passing credentials to the RADIUS server, which approves or denies access. Advantages: individual credentials can be revoked without affecting other users, authentication attempts are logged per user, and EAP (Extensible Authentication Protocol) methods like EAP-TLS (certificate-based) provide the highest security.

For enterprise environments with more than a handful of users, WPA2-Enterprise with 802.1X is the correct choice. The Network+ exam tests this distinction heavily.

> **Network+ Exam Tip:** When a scenario describes a corporation needing to revoke a specific employee's wireless access without affecting other users, the answer is always WPA2-Enterprise (or WPA3-Enterprise) with 802.1X/RADIUS. WPA2-PSK cannot do this without changing the shared key for everyone.

---

### Section 4: Wireless Threats and Attacks

[08:00 – 10:30]

[SHOW SLIDE: List of wireless attack types with brief descriptions]

The Network+ exam tests several common wireless attacks. Let's cover the ones you must know.

**Evil Twin (Rogue AP)** — An attacker sets up an access point broadcasting the same SSID as a legitimate network. Users connect to the attacker's AP, believing it is the real network. The attacker can then intercept all traffic (man-in-the-middle). Mitigation: WIPS (Wireless Intrusion Prevention Systems), 802.1X authentication so credentials can't be captured.

**Deauthentication Attack (Deauth Flood)** — 802.11 management frames (including deauthentication frames) are not authenticated in legacy standards. An attacker can forge deauthentication frames to disconnect clients from a legitimate AP. Used as part of WPA2-PSK cracking — the attacker forces clients to reauthenticate, capturing the 4-way handshake for offline cracking. Mitigation: 802.11w (Management Frame Protection).

**War Driving** — Driving through an area with a Wi-Fi-enabled device, scanning for open or weakly secured access points and logging their locations. The discovered networks can then be targeted for attacks.

**SSID Spoofing/Hiding** — Hiding the SSID (disabling broadcast) provides minimal security. Clients still broadcast probe requests that contain the SSID, making it detectable with passive scanning tools.

**Captive Portal Attacks** — Attackers set up a rogue captive portal that mimics a legitimate one, harvesting credentials when users "log in" to gain internet access.

**WPA2-PSK Cracking** — If an attacker captures the 4-way handshake (via a deauth attack that forces reauthentication), they can run an offline dictionary attack against the handshake. Mitigation: long, complex passphrases; upgrade to WPA3.

---

### Section 5: Lab Preview and Module Closing

[SHOW SLIDE: Lab overview — wireless scan command output]

In this week's lab, you will use the netsh wlan show networks command on Windows or the iwlist command on Linux to scan for nearby Wi-Fi networks. You will identify the SSID, 802.11 standard, frequency band, channel, and security type for each discovered network. This directly connects the theory from the lecture to observable real-world networks.

Module 06 key takeaways: 802.11ac is 5 GHz only; 802.11n is dual-band. Wi-Fi 6 (802.11ax) uses OFDMA for dense environments. 2.4 GHz non-overlapping channels are 1, 6, and 11. WEP is completely broken — never use it. WPA2-AES is the minimum acceptable standard. WPA3-SAE provides forward secrecy. WPA2-Enterprise (802.1X) provides per-user credentials for enterprise networks.

Module 07 covers WAN connectivity and cloud technologies.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
