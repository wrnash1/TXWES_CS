# Video Script: Module 11 — Wireless Network Assessment

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Segment 1 — Introduction (0:00–1:30)

Welcome back to CIS-4333 Penetration Testing. I am Professor Nash, and this is Module 11: Wireless Network Assessment.

Wireless networks present a unique challenge for security professionals. Unlike wired networks, the signal extends beyond the physical walls of the building. Anyone within radio range can attempt to interact with a wireless network without physically entering the facility. That makes wireless assessment a critical component of any comprehensive penetration test.

In this module we cover the 802.11 wireless standards and their security protocols, passive and active reconnaissance techniques, WPA2 handshake capture and offline cracking, evil twin and rogue access point attacks, WPS vulnerabilities, and the extended attack surface of Bluetooth and Zigbee. We also discuss the legal and ethical boundaries that govern wireless penetration testing.

This module aligns with CompTIA PenTest+ Domain 3: Attacks and Exploits.

---

## Segment 2 — 802.11 Standards and Security Protocols (1:30–4:00)

The 802.11 standard governs Wi-Fi communication. Different generations — 802.11a, b, g, n, ac, ax — define frequency bands, channel widths, and throughput capabilities. For security testing, what matters most is the authentication and encryption protocol in use.

### WEP

Wired Equivalent Privacy was the original wireless security standard. It uses RC4 stream cipher encryption with 24-bit initialization vectors. The IV space is small enough that collisions become statistically inevitable after collecting enough packets. Once enough IVs are collected, the key is mathematically recoverable. WEP is completely broken and should never be deployed. You may still encounter it in industrial or legacy environments.

### WPA and TKIP

Wi-Fi Protected Access with TKIP was introduced as an emergency patch for WEP hardware. TKIP is also deprecated and vulnerable to several attacks. Any network running WPA-TKIP should be treated as insecure.

### WPA2

WPA2 replaced TKIP with AES-CCMP, a significantly stronger cipher. WPA2 comes in two flavors. WPA2-Personal uses a pre-shared key — a password shared among all users. WPA2-Enterprise uses 802.1X with a RADIUS server for individual user authentication. WPA2-Personal is vulnerable to offline dictionary attacks against the four-way handshake. WPA2-Enterprise is much stronger but has its own attack vectors.

### WPA3

WPA3 replaces the WPA2 handshake with SAE — Simultaneous Authentication of Equals. SAE provides forward secrecy and is resistant to offline dictionary attacks. Even if traffic is captured, the pre-shared key cannot be derived from the handshake. WPA3 is the current standard for new deployments.

---

## Segment 3 — Wireless Reconnaissance (4:00–7:00)

Before any attack, we gather information about the target wireless environment.

### Passive Scanning

Passive scanning puts the wireless adapter into monitor mode and captures all 802.11 frames without transmitting. Monitor mode is enabled with:

```bash
airmon-ng start wlan0
```

This creates a monitor mode interface, typically named `wlan0mon`. From there, `airodump-ng` captures and displays nearby networks:

```bash
airodump-ng wlan0mon
```

The output shows BSSID (the MAC address of the access point), SSID (the network name), channel, encryption type, signal strength, and connected clients. This is your target list.

### Targeted Capture

Once you identify your target, lock onto its channel and BSSID:

```bash
airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w capture wlan0mon
```

The `-w capture` flag saves packets to files named `capture-01.cap`, `capture-01.csv`, and so on.

### Kismet

Kismet is an alternative wireless scanner that operates passively and provides a more feature-rich interface. It logs GPS coordinates alongside wireless data, useful for physical security assessments mapping wireless coverage to physical locations. Kismet also detects hidden SSIDs by capturing probe responses from connected clients.

---

## Segment 4 — WPA2 Handshake Capture and Cracking (7:00–11:00)

The WPA2 four-way handshake is the authentication exchange between a client and an access point during association. The handshake contains material derived from the pre-shared key through PBKDF2 key derivation. An attacker who captures the handshake can attempt offline dictionary attacks.

### Capturing the Handshake

Run airodump-ng against the target BSSID. The top-right corner of the output shows "WPA handshake: AA:BB:CC:DD:EE:FF" when a handshake is captured. You can wait for a client to naturally disconnect and reconnect, or you can force it.

### Deauthentication Attack

The 802.11 standard does not authenticate management frames by default. An attacker can send spoofed deauthentication frames that appear to come from the legitimate AP. The client disconnects and immediately reconnects, generating a fresh handshake.

```bash
aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c CC:DD:EE:FF:00:11 wlan0mon
```

The `-a` flag specifies the AP BSSID, `-c` specifies the client MAC, and `10` sends ten deauthentication frames. Watch airodump-ng — the handshake indicator appears within seconds.

### Offline Cracking with Aircrack-ng

```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
```

Aircrack-ng tests each password in the wordlist, derives the expected PBKDF2 output, and compares it to the captured handshake material. If the PSK is in the wordlist, it is recovered.

### Offline Cracking with Hashcat

Hashcat uses GPU acceleration for dramatically faster cracking. First, convert the capture file to Hashcat format using `hcxpcapngtool`:

```bash
hcxpcapngtool -o hash.hc22000 capture-01.cap
hashcat -m 22000 hash.hc22000 /usr/share/wordlists/rockyou.txt
```

A modern GPU can test tens of millions of passwords per second against WPA2 hashes.

### PMKID Attack

The PMKID attack does not require capturing a four-way handshake. The PMKID is a value derived from the PMK and the AP's BSSID that appears in the first EAPOL frame during association. The tool `hcxdumptool` captures PMKIDs passively:

```bash
hcxdumptool -i wlan0mon -o pmkid.pcapng --enable_status=1
hcxpcapngtool -o hash.hc22000 pmkid.pcapng
hashcat -m 22000 hash.hc22000 rockyou.txt
```

The PMKID attack is more efficient than handshake capture because it works from a single frame without requiring a connected client.

---

## Segment 5 — Evil Twin and Rogue Access Point Attacks (11:00–14:00)

### Evil Twin

An evil twin attack creates a rogue access point with the same SSID as a legitimate network. Clients configured to auto-connect to known networks may connect to the attacker's AP instead of the real one.

The attacker uses `hostapd` to configure the rogue AP and `dnsmasq` to serve DHCP and DNS. Once clients connect, the attacker can perform man-in-the-middle interception, serve a fake captive portal to harvest credentials, or downgrade HTTPS connections.

`hostapd-wpe` is a specialized tool for WPA2-Enterprise evil twin attacks. It masquerades as a legitimate RADIUS server and captures the EAP credential exchange — including the username and password hash — when enterprise clients attempt to authenticate.

### Rogue AP in Authorized Engagements

During physical security assessments, a tester may deploy a rogue AP inside the building to demonstrate that employees' devices will auto-connect to it, exposing their network traffic. This must always be explicitly authorized in the Rules of Engagement.

---

## Segment 6 — WPS PIN Attacks (14:00–16:00)

Wi-Fi Protected Setup was designed to simplify device pairing through a push-button mechanism and an 8-digit PIN. The design contains a critical flaw: the AP verifies the first four digits of the PIN independently from the last four. The final digit is a checksum. This splits the attack space from `10^8` possibilities to roughly `10^4 + 10^3` — approximately 11,000 total guesses.

Reaver automates the WPS PIN attack:

```bash
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv
```

Against a vulnerable AP with no WPS lockout, Reaver recovers the WPS PIN and, consequently, the WPA2 PSK. Many routers have WPS enabled by default and some never lock out after failed PIN attempts.

WPS attacks target WPA2-Personal only. WPA2-Enterprise does not use a PSK and is not vulnerable to WPS PIN recovery.

---

## Segment 7 — Bluetooth and Zigbee Attack Surface (16:00–18:00)

### Bluetooth

Bluetooth testing is an emerging area on the PenTest+ exam. Key attack categories include:

Bluejacking sends unsolicited messages to discoverable devices. Bluesnarfing gains unauthorized access to data on a Bluetooth device. Bluebugging takes full control of a device. These classic attacks primarily affect older Bluetooth implementations.

Modern Bluetooth Low Energy (BLE) introduces new attack surfaces. BLE devices often transmit advertising packets continuously. Tools like `hcitool`, `bluetoothctl`, and `btlejack` enumerate BLE devices, read GATT characteristics, and can perform man-in-the-middle attacks on unencrypted BLE communications.

### Zigbee

Zigbee is a low-power mesh network protocol used in IoT and industrial control systems — smart lighting, building automation, industrial sensors. Because Zigbee networks often run in environments where security was not the primary design consideration, they represent a significant attack surface.

Key Zigbee attack tools include KillerBee and Zbstumbler. Attackers can sniff Zigbee traffic, replay captured packets, and in some cases inject commands into the mesh network. During physical penetration tests of data centers and industrial facilities, Zigbee assessment may be explicitly scoped.

---

## Segment 8 — Legal and Ethical Constraints (18:00–20:00)

Wireless penetration testing carries significant legal risk because the attack surface is not bounded by a network perimeter. Radio signals propagate beyond property boundaries.

Written authorization is non-negotiable. The authorization document must explicitly include wireless testing and should specify the SSIDs and BSSIDs authorized for testing. Testing neighboring networks — even accidentally — could violate the Computer Fraud and Abuse Act.

Deauthentication attacks disrupt wireless connectivity for legitimate users. During business hours, a poorly timed deauth flood can cause visible service disruption. Coordinate timing with the client. Some engagements restrict deauth attacks to after-hours windows.

Evil twin deployments in shared facilities — office parks, coworking spaces, hotels — can inadvertently capture traffic from users of adjacent tenants who are not part of the engagement. This is a serious ethical and legal concern. Minimize RF output to the target facility and cease operations immediately if unintended connections occur.

Document all wireless testing activity with timestamps, BSSID targets, and techniques used. This protects you legally and supports your report findings.

---

## Segment 9 — Reporting Wireless Findings (20:00–21:30)

Wireless findings should document:

- Network name (SSID) and BSSID of the tested access point
- Security protocol in use (WEP, WPA2-Personal, WPA2-Enterprise, WPA3)
- Attack technique used and result
- For cracked PSKs: the recovered password and the wordlist used (demonstrates password policy weakness)
- For rogue AP connections: the number of clients that connected and what traffic was captured
- Business impact statement
- Remediation recommendation

For WPA2-Personal cracking: recommend migrating to WPA3 or implementing WPA2-Enterprise with 802.1X, and enforcing a minimum passphrase length of 20 characters to make offline cracking impractical.

For WPS vulnerabilities: recommend disabling WPS on all access points.

---

## Segment 10 — Module Summary (21:30–24:00)

Let us recap the key concepts from this module:

- 802.11 security protocol evolution: WEP is broken, WPA-TKIP is deprecated, WPA2-Personal is vulnerable to offline cracking, WPA3 resists offline attacks
- Passive reconnaissance with airodump-ng and Kismet to enumerate targets
- WPA2 handshake capture via natural reconnection or deauthentication, followed by offline cracking with aircrack-ng or hashcat
- PMKID attack as an efficient alternative to handshake capture
- Evil twin and rogue AP attacks for credential capture
- WPS PIN attack using Reaver against the 11,000-combination design flaw
- Bluetooth and Zigbee as emerging attack surfaces in IoT and industrial environments
- Legal requirements: written authorization must explicitly cover wireless testing

Your lab this week uses a TryHackMe wireless room to work through handshake capture and cracking without requiring physical wireless hardware. Your quiz tests your knowledge of protocols, tools, and attack techniques. Your discussion asks you to analyze a real wireless security incident.

See you in Module 12, where we cover post-exploitation and privilege escalation.

---

*End of Module 11 Video Script*
