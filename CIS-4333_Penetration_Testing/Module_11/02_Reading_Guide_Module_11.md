# Reading Guide: Module 11 — Wireless Network Assessment

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4333 &BULL; PENETRATION TESTING & ETHICAL HACKING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This reading guide supports Module 11 and prepares you for the CompTIA PenTest+ exam's wireless attack content in Domain 3: Attacks and Exploits. Wireless assessments require understanding both the underlying protocols and the specific tools that exploit their weaknesses. This guide organizes the key concepts, vocabulary, and study questions you need to master.

---

## Primary Reading Topics

### 1. 802.11 Wireless Security Protocol History

Review the evolution of wireless security protocols. Key facts for the exam:

- WEP uses RC4 with a 24-bit IV and is completely broken due to IV collision attacks. Collecting 50,000–100,000 packets is sufficient for key recovery.
- WPA-TKIP was an interim fix and is also deprecated. The TKIP protocol has known weaknesses.
- WPA2-CCMP (AES) is the current mainstream standard. WPA2-Personal is vulnerable to offline dictionary attacks against the four-way handshake.
- WPA2-Enterprise uses 802.1X/RADIUS for per-user authentication. There is no shared PSK to crack, but evil twin attacks can capture EAP credentials.
- WPA3 uses SAE instead of the pre-shared key handshake, providing forward secrecy and resistance to offline dictionary attacks.

### 2. The WPA2 Four-Way Handshake

Understand what happens during WPA2-Personal authentication:

- The client and AP exchange four EAPOL frames
- The handshake contains material derived from the PSK using PBKDF2 with the SSID as a salt
- An attacker who captures the handshake can test password candidates offline without further interaction with the AP
- The SSID is used as the PBKDF2 salt, which means common SSIDs like "linksys" may have precomputed rainbow tables available
- Changing the SSID to something unique forces attackers to recompute hashes for each attempt

### 3. Aircrack-ng Suite

Review the purpose of each tool in the Aircrack-ng suite. The exam tests tool selection by name:

- `airmon-ng`: enables and manages monitor mode on wireless interfaces
- `airodump-ng`: passive packet capture and network enumeration
- `aireplay-ng`: frame injection including deauthentication, fake authentication, and ARP replay
- `aircrack-ng`: offline dictionary and brute-force attack against WPA2 handshakes and WEP keys
- `airbase-ng`: creates a software access point for evil twin and rogue AP scenarios

### 4. PMKID Attack

The PMKID attack is a more recent technique that does not require capturing a four-way handshake:

- The PMKID is derived from the PMK (itself derived from the PSK) combined with the AP and client MAC addresses
- A single EAPOL frame during the association process contains the PMKID
- Tools: `hcxdumptool` for capture, `hcxpcapngtool` for conversion, Hashcat with mode 22000 for cracking
- The PMKID attack requires only that the client attempt to associate — a full handshake completion is not required

### 5. Evil Twin and Rogue AP Attacks

Review the distinction between these two related attacks:

- Evil twin: rogue AP with the same SSID (and optionally BSSID spoofed) as a legitimate network, designed to intercept client connections
- `hostapd-wpe`: specifically designed for WPA2-Enterprise evil twin attacks; captures EAP credential exchanges from enterprise clients attempting to authenticate with the rogue RADIUS server
- Captive portal phishing: the rogue AP serves a fake login page to harvest credentials from clients who connect
- Key legal risk: RF signals may extend to areas beyond the authorized scope

### 6. WPS Vulnerabilities

Understand the WPS PIN design flaw in detail:

- The 8-digit PIN is verified in two halves: the AP confirms the first 4 digits before checking the second 4
- The last digit of the 8-digit PIN is a checksum, reducing the second half to 3 unknown digits
- Total brute-force space: `10^4 + 10^3 = 11,000` combinations rather than `10^8`
- Reaver and bully are the standard tools for WPS PIN attacks
- Many APs implement WPS lockout after repeated failures; some older models do not
- WPS attacks recover the WPA2-Personal PSK — they do not apply to WPA2-Enterprise

### 7. Bluetooth and Zigbee

Review these alternative wireless attack surfaces:

- Bluejacking (unsolicited messages), Bluesnarfing (data theft), Bluebugging (device control) — primarily historical attacks on classic Bluetooth
- BLE (Bluetooth Low Energy) advertising packets are broadcast continuously and may reveal device identity, capabilities, and location
- Zigbee mesh networks are used in IoT, industrial, and building automation contexts
- KillerBee is the primary Zigbee security research framework
- Physical penetration tests of data centers and industrial facilities may include Zigbee scoping

### 8. Legal Constraints

This is an exam-tested topic. Key points:

- Written authorization must explicitly include wireless testing and should specify authorized SSIDs and BSSIDs
- Deauthentication attacks disrupt service for legitimate users — coordinate timing with the client
- Evil twin deployments in shared facilities risk capturing traffic from unauthorized third parties
- Radio frequency propagation does not respect property boundaries — be aware of geographic scope
- The Computer Fraud and Abuse Act (CFAA) applies to unauthorized access to any wireless network

---

## Key Vocabulary

Review and be able to define each of the following terms:

- 802.11 standard
- WEP (Wired Equivalent Privacy)
- WPA-TKIP
- WPA2-CCMP (AES)
- WPA2-Personal (PSK)
- WPA2-Enterprise (802.1X)
- WPA3 (SAE)
- Four-way handshake
- PBKDF2
- PMK (Pairwise Master Key)
- PTK (Pairwise Transient Key)
- PMKID
- Monitor mode
- Managed mode
- airodump-ng
- airmon-ng
- aireplay-ng
- aircrack-ng
- Deauthentication attack
- Evil twin
- Rogue access point
- hostapd-wpe
- WPS (Wi-Fi Protected Setup)
- Reaver
- BSSID
- SSID
- Bluejacking
- Bluesnarfing
- BLE (Bluetooth Low Energy)
- Zigbee
- KillerBee

---

## Study Questions

These questions are for self-study and are not submitted. Use them to prepare for the quiz.

1. Why is WEP considered completely broken? What specific cryptographic weakness enables the IV collision attack?

2. A WPA2-Personal network uses the SSID "linksys" and a 12-character passphrase. Why is the SSID relevant to the difficulty of cracking the handshake?

3. Explain the WPS PIN design flaw in your own words. Why does verifying the PIN in two halves reduce the attack space from 100 million to approximately 11,000?

4. What is the difference between a deauthentication attack and an evil twin attack? Could they be used together? Explain.

5. What does `airmon-ng start wlan0` do, and why is this step required before running `airodump-ng`?

6. A tester wants to crack a WPA2 handshake as quickly as possible. Should they use aircrack-ng or Hashcat, and why?

7. Why is WPA2-Enterprise resistant to the offline handshake cracking attack that targets WPA2-Personal?

8. What is the PMKID attack and what advantage does it have over traditional handshake capture?

9. What legal risk exists when conducting an evil twin attack in an office building that houses multiple tenant organizations?

10. Name two differences between classic Bluetooth attacks (Bluejacking, Bluesnarfing) and modern BLE attack techniques.

---

## Recommended Resources

The following free resources supplement the lecture material:

- Aircrack-ng documentation: aircrack-ng.org/documentation.html
- hcxtools documentation (PMKID attack): github.com/ZerBea/hcxtools
- TryHackMe Pentesting Learning Path (Wi-Fi Hacking room): tryhackme.com
- Offensive Security wireless tutorials: kali.org/tools/aircrack-ng
- WPS vulnerability research: sviehb.wordpress.com/2011/12/27/wi-fi-protected-setup-pin-brute-force-vulnerability

TryHackMe's Wi-Fi Hacking room is strongly recommended as a browser-accessible lab that walks through the aircrack-ng workflow, handshake capture, and offline cracking without requiring physical wireless hardware.

---

## CompTIA PenTest+ Exam Objectives Covered

The following PT0-002 exam objective is the primary focus:

- 3.2: Given a scenario, research attack vectors and perform wireless attacks

This objective explicitly tests: WPA cracking, evil twin attacks, deauthentication, WPS PIN attacks, Bluetooth enumeration, and the legal requirements for wireless testing. Wireless attacks appear as scenario questions requiring you to select the correct tool or technique for a given situation.

---

---

## 9. Supplemental Resources

**1. Aircrack-ng Official Documentation and Wiki**
[https://www.aircrack-ng.org/documentation.html](https://www.aircrack-ng.org/documentation.html)
The official Aircrack-ng documentation covers every tool in the suite — airmon-ng, airodump-ng, aireplay-ng, and aircrack-ng — with usage examples and flag reference. It is the authoritative source for the wireless assessment workflow covered in Module 11 and directly applicable to PT0-002 Domain 3 wireless attack objectives.

**2. hcxtools and hcxdumptool — PMKID Attack Documentation**
[https://github.com/ZerBea/hcxtools](https://github.com/ZerBea/hcxtools)
The hcxtools repository documents the modern WPA2 PMKID capture-and-crack workflow that complements the traditional four-way handshake approach. Understanding PMKID-based attacks (no deauthentication required) is directly relevant to PT0-002 wireless attack scenarios and the Module 11 lab.

**3. TryHackMe — Wifi Hacking 101 Room**
[https://tryhackme.com/room/wifihacking101](https://tryhackme.com/room/wifihacking101)
TryHackMe's Wifi Hacking 101 room provides guided hands-on practice with the full aircrack-ng workflow — monitor mode, handshake capture, and offline cracking — in a browser-accessible environment that does not require physical wireless hardware. Completing this room reinforces all Module 11 lab exercises and builds command-line fluency with wireless assessment tools.

*End of Module 11 Reading Guide*
