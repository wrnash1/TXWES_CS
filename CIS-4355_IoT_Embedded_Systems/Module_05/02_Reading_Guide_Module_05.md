# Reading Guide: Module 05 - IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 05 – IoT Networking: Wi-Fi, Bluetooth, LoRaWAN, NB-IoT**! This module compares the four dominant wireless technologies used in IoT deployments, analyzing each on the dimensions that matter most for design decisions: range, power consumption, data rate, topology, and security model. Choosing the wrong radio technology is one of the most common and costly mistakes in IoT product design.

You will learn why LoRaWAN can send a sensor reading kilometers with a coin-cell battery while Wi-Fi drains the same battery in hours, why Bluetooth Low Energy is ideal for wearables but impractical for outdoor industrial sensors, and where NB-IoT fills the gap between cellular and LPWAN technologies. Security considerations — from WPA3 Wi-Fi hardening to LoRaWAN session key management — are woven throughout.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Bluetooth Low Energy (BLE)**: A short-range (typically 10–100 m) wireless personal area network technology optimized for intermittent, low-volume data exchange at minimal power. BLE operates in the 2.4 GHz ISM band using frequency-hopping spread spectrum across 40 channels. It is commonly used in wearables, asset tracking beacons, and health monitors. Security uses AES-128 encryption; pairing modes range from "Just Works" (no authentication — vulnerable to MITM attacks) to Numeric Comparison and Passkey Entry.
*   **Zigbee Mesh Networking**: A self-forming, self-healing mesh network built on the IEEE 802.15.4 standard, operating at 2.4 GHz with a typical range of 10–100 m per hop. Zigbee devices are classified as Coordinator (one per network, manages keys), Router (relays messages), or End Device (leaf node, may sleep). AES-128 encryption protects the network layer. Dense mesh networks extend effective range by multi-hop relaying, making Zigbee practical for building automation with hundreds of nodes.
*   **LoRaWAN Long-Range**: A low-power wide-area network (LPWAN) protocol stack built on the LoRa chirp spread-spectrum radio modulation. LoRaWAN devices transmit at very low data rates (0.3–50 kbps) but achieve ranges of 2–15 km in urban environments and up to 40 km in line-of-sight rural settings, with battery life measured in years. The LoRaWAN specification defines security using two 128-bit AES session keys — one for network authentication (NwkSKey) and one for application payload encryption (AppSKey).
*   **Wi-Fi Constraints for IoT**: IEEE 802.11 Wi-Fi provides high bandwidth (tens to hundreds of Mbps) and ubiquitous infrastructure integration but consumes 50–300 mA during active transmission — prohibitive for battery-powered IoT nodes. Security best practices for IoT Wi-Fi devices include WPA3-Personal or WPA3-Enterprise, disabling WPS (Wi-Fi Protected Setup, which has known PIN brute-force vulnerabilities), using unique per-device credentials, and placing IoT devices on a dedicated VLAN isolated from corporate networks.
*   **Energy Harvesting and Duty Cycling**: Techniques used to extend the operational life of battery-powered IoT nodes. Duty cycling wakes the radio only for the minimum time needed to transmit, then returns to deep sleep. Energy harvesting captures ambient energy (solar, vibration, RF) to supplement or replace batteries. Understanding duty cycle math — e.g., a node transmitting 10 ms every 60 s has a duty cycle of 0.017% — is essential for battery-life estimation questions.

---

### 2. Certification Exam Tips
*   **Range vs. power trade-off matrix:** Memorize: BLE = short range, ultra-low power; Wi-Fi = short-medium range, high power, high throughput; Zigbee = short range per hop but mesh extends coverage, low power; LoRaWAN = very long range, ultra-low power, very low data rate; NB-IoT = cellular coverage, low power, licensed spectrum. Exam scenarios test protocol selection given range and power constraints.
*   **Security weaknesses by protocol:** BLE "Just Works" pairing = MITM vulnerability; Wi-Fi WPS PIN = brute-force vulnerability; LoRaWAN replay attacks if frame counters are not validated; Zigbee key transport in the clear during joining = network key exposure risk.
*   **LoRaWAN class types:** Class A (baseline, lowest power — uplink-triggered downlink window); Class B (scheduled receive windows using beacon); Class C (always-on receive — highest power). Know which class suits which application.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure network services and weak ecosystem interfaces — both directly relevant to improperly secured Wi-Fi, BLE, and LoRaWAN deployments discussed in this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insecure network services and ecosystem interface sections, which cover vulnerabilities arising from misconfigured Wi-Fi, unprotected BLE pairing, and exposed LoRaWAN join procedures.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes a comparative walkthrough of IoT wireless technologies covering range, power profiles, and typical deployment scenarios for BLE, Wi-Fi, Zigbee, and LoRaWAN.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Compare wireless parameters (range, power, bandwidth) for IoT**: Build a comparison table for BLE, Wi-Fi (802.11n), Zigbee, and LoRaWAN covering frequency band, typical range, peak current draw, maximum data rate, and security mechanism; then map each to two real-world IoT use cases.
*   **Analyze mesh routing topologies**: Using a Zigbee or Thread simulation tool (e.g., the TI Z-Stack simulator or Wireshark with a Zigbee sniffer), capture a multi-hop message transmission and trace the source, intermediate router, and destination node addresses in the captured frames.
*   **Verify network link ranges**: Use an RSSI (Received Signal Strength Indicator) measurement script on a Raspberry Pi with a BLE or Wi-Fi adapter to log signal strength at 1 m intervals from an access point, and plot the path loss curve to identify the effective range boundary at –80 dBm.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the insecure network services section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the wireless technology comparison sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Build the wireless parameter comparison table before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
