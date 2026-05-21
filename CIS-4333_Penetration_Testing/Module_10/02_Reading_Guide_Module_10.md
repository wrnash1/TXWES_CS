# Reading Guide: Module 10 - Wireless Network Penetration Testing
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 10 - Wireless Network Penetration Testing**! Wireless networks are a pervasive and frequently misconfigured attack surface. Enterprise Wi-Fi deployments using WPA2-Enterprise can be complex to secure, and many organizations still operate networks using weaker protocols or insecure configurations. Wireless penetration testing evaluates the security of 802.11 Wi-Fi networks by testing authentication, encryption, and client isolation controls. This module maps to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**) and covers the wireless attack techniques the exam tests directly.

Wireless attacks are particularly relevant in physical-access and insider-threat scenarios — an attacker within radio range of a target network can attempt authentication bypass, capture handshakes for offline cracking, or set up rogue access points to intercept credentials.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **WPA2 Four-Way Handshake Capture**: During WPA2-Personal (PSK) authentication, a four-packet exchange occurs between the client and access point that contains material derived from the pre-shared key. By passively monitoring or actively forcing a client to re-authenticate (using a deauthentication attack), a tester can capture this handshake and attempt to crack the PSK offline using a wordlist attack with Hashcat or Aircrack-ng. Capturing the handshake requires the tester's wireless adapter to be in monitor mode.

*   **Evil Twin / Rogue Access Point**: An attack in which the tester creates a wireless access point with the same SSID (and optionally the same BSSID) as a legitimate network to trick clients into connecting to an attacker-controlled network. Once connected, the attacker can perform a Man-in-the-Middle (MitM) attack to intercept credentials, capture unencrypted traffic, or serve fake captive portal login pages. Tools like `hostapd-wpe` automate rogue AP deployment for WPA2-Enterprise credential capture.

*   **WPS PIN Attack**: Wi-Fi Protected Setup (WPS) is a feature designed to simplify device pairing that contains a design flaw — the 8-digit PIN is verified in two halves, reducing the brute-force space from 10^8 to approximately 11,000 combinations. The `reaver` and `bully` tools exploit this flaw to recover the WPS PIN and, consequently, the WPA2 PSK. Many routers have WPS enabled by default. This vulnerability is a standard PT0-002 wireless exam topic.

*   **Deauthentication Attack (802.11 Deauth)**: The 802.11 management frame standard does not require authentication by default, allowing an attacker to spoof deauthentication frames to disconnect clients from an access point. Penetration testers use this technique to force clients to re-authenticate, generating a fresh WPA2 handshake for capture. The command `aireplay-ng --deauth 10 -a <BSSID> -c <client_MAC> <interface>` sends deauthentication frames. This is a necessary step when the tester cannot wait for organic client re-authentication.

*   **Aircrack-ng Suite**: The standard open-source wireless auditing toolkit used in penetration testing. Key tools in the suite include: `airmon-ng` (puts the wireless adapter into monitor mode), `airodump-ng` (scans for networks and captures packets), `aireplay-ng` (injects frames including deauthentication), and `aircrack-ng` (offline dictionary/brute-force attack against captured WPA2 handshakes or WEP IVs). PT0-002 expects testers to know the purpose of each tool in the suite.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002**. Wireless attacks appear in scenario questions — know the attack names, which protocols they target, and which tools execute them.
*   **WEP vs. WPA vs. WPA2 vs. WPA3:** WEP is completely broken (RC4 stream cipher with weak IV handling). WPA/TKIP is deprecated and crackable. WPA2-Personal uses AES-CCMP and is vulnerable to offline PSK cracking via captured handshakes. WPA2-Enterprise uses 802.1X/RADIUS and is much stronger — the primary attack is the Evil Twin/rogue AP to capture RADIUS credentials. WPA3 uses SAE (Simultaneous Authentication of Equals) and is resistant to offline dictionary attacks.
*   **Monitor Mode vs. Managed Mode:** Wireless adapters normally operate in managed mode (connecting to APs). Monitor mode enables the adapter to passively capture all 802.11 frames in range regardless of SSID. Monitor mode is required before running `airodump-ng` or capturing handshakes.
*   **Exam Trap — WPS Attack Targets WPA2-Personal, Not Enterprise:** WPS PIN attacks recover the PSK — they only work against WPA2-Personal networks. WPA2-Enterprise does not use a PSK and is not vulnerable to WPS attacks.
*   **PMKID Attack:** A newer WPA2 cracking technique that does not require capturing a four-way handshake — it extracts the PMKID from a single EAPOL frame during association. The tool `hcxdumptool` captures PMKIDs. This is more efficient than waiting for a handshake capture.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Wi-Fi Hacking" and related wireless rooms provide browser-accessible guided practice with the Aircrack-ng suite, WPA2 handshake capture, and wireless attack methodology in a legal lab environment.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Wireless Attacks section for content covering WPA2 cracking, rogue APs, and deauthentication attacks mapped to PT0-002 domain 3.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Wireless Hacking rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — all labs run in your browser without requiring a dedicated wireless adapter or physical lab setup. The wireless rooms walk through the Aircrack-ng workflow, handshake capture concepts, and Evil Twin attack methodology with guided instructions.
*   **Required Video:** Watch the Wireless Attacks segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the wireless security content covering WPA2, deauthentication attacks, WPS vulnerabilities, and rogue access points.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Enable monitor mode: `airmon-ng start wlan0`**: You will configure your wireless adapter to capture all 802.11 frames in the environment, a required prerequisite for all subsequent wireless attack steps. You will verify the monitor mode interface is active before proceeding.
*   **Capture nearby networks and identify targets: `airodump-ng wlan0mon`**: You will scan the wireless environment to enumerate nearby access points — recording BSSID, SSID, channel, encryption type, and connected clients. You will select a lab target based on this output and focus further capture on that channel.
*   **Capture WPA2 handshake and attempt offline crack**: You will run `airodump-ng` against the target BSSID and optionally send deauthentication frames to force a handshake, then run `aircrack-ng -w wordlist.txt capture.cap` to attempt offline dictionary cracking — documenting whether the PSK was recovered and what it demonstrates about password policy strength.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Wireless Hacking rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Wireless Attacks section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
