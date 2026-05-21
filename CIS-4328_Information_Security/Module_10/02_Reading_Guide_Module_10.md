# Reading Guide: Module 10 - Wireless and Mobile Security
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 10 – Wireless and Mobile Security**! Wireless networks and mobile devices introduce unique attack surfaces that differ from wired infrastructure. SY0-701 tests wireless security in Domain 3 (Security Architecture) and Domain 4 (Security Operations) — expect scenario questions on selecting the correct Wi-Fi security protocol, identifying wireless attack types, and securing mobile device deployments.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **WPA3 (Wi-Fi Protected Access 3)**: The current generation Wi-Fi security standard, replacing WPA2. WPA3-Personal uses Simultaneous Authentication of Equals (SAE) instead of the Pre-Shared Key (PSK) handshake, eliminating offline dictionary attacks against captured handshakes. WPA3-Enterprise uses 192-bit cryptographic strength. SY0-701 tests WPA3 as the correct answer whenever the question asks for the strongest or most current wireless security protocol.
*   **Evil Twin Attack**: A wireless attack in which an attacker deploys a rogue access point with the same SSID (network name) as a legitimate network, tricking nearby devices into connecting to the attacker's AP instead. Once connected, all traffic flows through the attacker, enabling credential theft and man-in-the-middle interception. Mitigation includes 802.1X certificate-based authentication and VPN enforcement on untrusted networks.
*   **Deauthentication (Deauth) Attack**: A wireless denial-of-service attack that exploits the unauthenticated management frames in 802.11 by sending forged deauthentication frames to disconnect legitimate clients from an access point. The disconnected clients may then reconnect to an evil twin. WPA3 and 802.11w (Management Frame Protection) protect against deauth attacks by authenticating management frames.
*   **Mobile Device Management (MDM)**: A software platform that allows IT administrators to remotely configure, monitor, enforce security policies on, and wipe mobile devices (smartphones, tablets) enrolled in the corporate environment. MDM capabilities tested on SY0-701 include remote wipe, containerization (separating corporate and personal data), geofencing, screen lock enforcement, and application allowlisting.
*   **Bluetooth Attack Types**: SY0-701 tests three Bluetooth attacks: Bluejacking — unsolicited messages sent to a discoverable device (nuisance, not a data theft attack); Bluesnarfing — unauthorized access to data (contacts, emails, calendar) on a Bluetooth device without pairing consent; Bluebugging — full remote control of a device's functions (calls, messages) via a Bluetooth exploit. Mitigation: disable Bluetooth when not in use; use non-discoverable mode.
*   **BYOD (Bring Your Own Device) Security**: A mobile security policy model where employees use personal devices for work. BYOD introduces risks of mixing personal and corporate data, loss of corporate data when employees leave, and unmanaged device vulnerabilities. Security controls include MDM enrollment, containerization, network access control (NAC), and acceptable use policies that define what the organization can and cannot do to a personal device.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Wireless and mobile security falls under **Domain 3 – Security Architecture (18%)** and **Domain 4 – Security Operations (28%)** of SY0-701. Expect scenario questions comparing Wi-Fi security protocols and selecting MDM controls for a given mobile risk.
*   **Wireless Protocol Order:** WEP (broken, never use) → WPA (TKIP, deprecated) → WPA2 (AES/CCMP, acceptable) → WPA3 (SAE, current standard). If a question asks for the strongest available protocol, WPA3 is correct. If a legacy device cannot support WPA3, WPA2-AES is the next best choice — never WEP or WPA-TKIP.
*   **Evil Twin vs. Rogue AP:** A rogue AP is any unauthorized access point connected to the corporate network (an insider threat — someone plugging in a cheap AP). An evil twin is an external attacker's AP mimicking a legitimate SSID to capture client connections. Both are detected by wireless intrusion detection systems (WIDS), but they represent different threats.
*   **MDM Scenario Trap:** Questions about lost/stolen devices test remote wipe. Questions about separating corporate email from personal apps test containerization. Questions about restricting device use to a geographic area test geofencing. Match the control to the specific risk described.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include wireless protocol comparison tables, Bluetooth attack summaries, and MDM policy scenarios that map directly to SY0-701 exam questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Wireless and Mobile Security" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on Wi-Fi protocol evolution, wireless attack types, and mobile device management controls.
*   **Required Video:** Watch the wireless and mobile security video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos include network diagrams showing evil twin attack flows and MDM architecture in enterprise deployments.

---

### Lab & Command Integration
In this week's hands-on lab, you will analyze wireless network configurations, identify insecure protocols in a simulated environment, and evaluate MDM policy settings for a BYOD scenario. Recognizing weak wireless configurations and selecting appropriate remediation is a direct SY0-701 performance-based question skill.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to select the correct wireless security protocol and mobile control for any given scenario.
- [ ] Read the "Wireless and Mobile Security" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the wireless and mobile security video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: WPA3 = SAE, strongest; Evil Twin = rogue SSID clone; Bluesnarfing = data theft via Bluetooth; MDM remote wipe = lost device response.
- [ ] Proceed to the weekly hands-on lab activity.
