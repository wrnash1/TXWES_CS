# Video Script – Module 05: IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA IoT+ Domain 3 – IoT Connectivity

---

## Segment 1: Introduction and Learning Objectives [00:00 – 02:00]

Welcome to Module 05. I am Professor Nash. In Module 04 we learned the application-layer protocols that IoT systems use: MQTT, CoAP, HTTP/REST. Now we go one layer deeper — the radio technologies that physically carry those messages.

Radio selection is one of the most consequential engineering decisions in any IoT deployment. The wrong choice means dead batteries, out-of-range devices, or bills for cellular data that eclipse the value of the sensor data being collected.

By the end of this video you will be able to:

- Describe the physical characteristics of Wi-Fi, Bluetooth Low Energy, LoRaWAN, and NB-IoT.
- Compare these technologies on range, bandwidth, power consumption, and spectrum type.
- Explain the LoRaWAN network architecture including end nodes, gateways, and the network server.
- Explain how NB-IoT differs from LoRaWAN in terms of spectrum and network infrastructure.
- Identify the security vulnerabilities specific to each radio technology.
- Choose the appropriate wireless technology for a given IoT application.

Let us start at the technology most of you already use every day: Wi-Fi.

---

## Segment 2: Wi-Fi in IoT [02:00 – 06:30]

[SHOW DIAGRAM]

Wi-Fi is the IEEE 802.11 family of wireless LAN standards. Every home router, campus network, and corporate office runs Wi-Fi. The latest generation is Wi-Fi 6 (802.11ax), operating at up to 9.6 Gbps on 2.4, 5, and 6 GHz bands.

### Wi-Fi Strengths in IoT

Wi-Fi's strengths are high bandwidth and ubiquitous infrastructure. Security cameras, smart TVs, gateways, and Raspberry Pi edge nodes use Wi-Fi because:

- Gigabit-class bandwidth is available.
- Infrastructure already exists in most buildings.
- Full TCP/IP stack with no gateway intermediary needed.
- Easy integration with cloud services directly from the device.

### Wi-Fi Limitations in IoT

Wi-Fi is power-hungry. An ESP8266 Wi-Fi module draws 170–260 mA when actively transmitting. That is enough to drain an AA battery in hours. Battery-powered IoT sensors cannot use always-on Wi-Fi.

Wi-Fi range is limited to 30–100 meters indoors, and even less through walls. Outdoor range is better with directional antennas but is still measured in hundreds of meters, not kilometers.

### Wi-Fi Security for IoT

WPA3 is the current recommended security standard. WPA2 is still widely deployed and acceptable when configured correctly. Key security requirements for IoT Wi-Fi deployments:

- Use WPA2-Enterprise or WPA3 with individual device credentials. Avoid WPA2-Personal shared passphrases, which give every device on the network the same key.
- Network segmentation: IoT devices should be on a dedicated VLAN with firewall rules blocking lateral movement to corporate segments. A compromised smart thermostat should not be able to reach financial servers.
- Disable WPS (Wi-Fi Protected Setup). WPS has known PIN brute-force vulnerabilities.

The Wi-Fi SSID and password configuration is one of the most commonly hardcoded credentials found in IoT device firmware — a direct OWASP IoT #1 violation.

---

## Segment 3: Bluetooth Low Energy [06:30 – 10:30]

[SHOW DIAGRAM]

Bluetooth Low Energy (BLE) is defined in the Bluetooth Core Specification. It operates at 2.4 GHz in the same ISM band as Wi-Fi and Zigbee, using 40 channels of 2 MHz each with adaptive frequency hopping to avoid interference.

### BLE vs. Classic Bluetooth

Classic Bluetooth (BR/EDR) is designed for continuous audio streaming: headphones, car speakers, keyboards. It maintains a persistent connection and draws 20–40 mA continuously.

BLE is designed for periodic, short-burst data transmission from constrained devices. A BLE sensor can operate on a coin cell battery for two to five years by waking briefly to transmit a reading and returning to deep sleep immediately. Current draw during sleep is under 10 microamps.

### BLE in IoT

BLE is the dominant protocol for:

- Wearables (fitness trackers, smartwatches, continuous glucose monitors).
- Beacon deployments (proximity marketing, indoor positioning, asset tracking).
- Smart home accessories (door locks, light bulbs, environmental sensors).
- Medical devices (heart rate monitors, pulse oximeters).

Range is 10–100 meters. For longer range, BLE 5.0 introduced a Long Range mode (coded PHY) that extends range to approximately 400 meters at lower data rate.

### BLE Topology

BLE uses a central/peripheral model. A central device (smartphone, gateway) initiates connections and typically controls the communication. A peripheral device (sensor) advertises its presence and waits to be connected.

BLE Mesh (Bluetooth Mesh Networking) extends BLE to multi-hop relay networks for building automation use cases, competing with Zigbee and Thread.

### BLE Security

BLE pairing modes:

- Just Works: no authentication during key exchange. Vulnerable to man-in-the-middle attacks where an attacker in range intercepts and replaces the key exchange. Acceptable only for non-sensitive applications.
- Passkey Entry: one device displays a 6-digit PIN that the user enters on the other. Protects against passive eavesdropping.
- Numeric Comparison: both devices display the same 6-digit number for the user to confirm. Prevents MITM.
- Out-of-Band (OOB): key exchange using a separate channel (NFC, QR code). Strongest against wireless MITM attacks.

For IoT access control and medical applications, Numeric Comparison or OOB pairing is required.

---

## Segment 4: LoRaWAN [10:30 – 15:00]

[SHOW DIAGRAM]

LoRaWAN is the defining LPWAN (Low Power Wide Area Network) technology for outdoor IoT. It enables sensors to transmit over 2–15 kilometers on a single battery charge that lasts years. This is the radio technology that makes practical IoT deployments over large areas economically viable.

### LoRa Physical Layer

LoRa is a proprietary chirp spread spectrum modulation technique developed by Semtech. It encodes each bit across a wide frequency range using a chirp signal whose frequency increases or decreases over time. This spread-spectrum approach provides extraordinary sensitivity — LoRa receivers can decode signals 20 dB below the noise floor. This is why LoRa achieves such impressive range: it can hear signals that are essentially indistinguishable from noise to a conventional receiver.

The cost is data rate: 0.3 to 50 kbps depending on spreading factor and bandwidth settings. LoRa is for infrequent, small payloads. You send a 20-byte sensor reading once per hour, not a live video stream.

### LoRaWAN Network Architecture

LoRaWAN adds the MAC and network layer on top of LoRa. The architecture has three tiers:

End devices: the sensors and actuators with LoRa radios. They transmit uplink messages to any gateway within range.

Gateways: receive LoRa transmissions from all end devices in range and forward them over IP (Ethernet, LTE) to the network server. Multiple gateways can receive the same end device transmission, providing redundancy. Unlike Zigbee gateways, LoRaWAN gateways are simple packet forwarders — they do not interpret or process the messages.

Network server: the intelligence of the network. It deduplicates messages received by multiple gateways, manages device addresses, and routes decrypted payloads to the application server.

### LoRaWAN Security

LoRaWAN uses two layers of AES-128 encryption:

- Network session key: encrypts MAC commands and protects the network layer frame counter.
- Application session key: encrypts the payload. The network server never sees the plaintext application payload — only the application server can decrypt it.

LoRaWAN operates on unlicensed spectrum (915 MHz in the US, 868 MHz in Europe). This means no monthly carrier fees but also no guaranteed interference protection.

---

## Segment 5: NB-IoT [15:00 – 18:30]

[SHOW DIAGRAM]

NB-IoT (Narrowband IoT) is a cellular IoT technology standardized by 3GPP as part of LTE Release 13. Where LoRaWAN operates on unlicensed ISM spectrum, NB-IoT uses licensed cellular spectrum — the same frequencies as 4G LTE networks.

### NB-IoT Characteristics

Bandwidth: 200 kHz channel.
Data rate: up to 250 kbps downlink, 20 kbps uplink (typical IoT payloads).
Power consumption: NB-IoT supports Power Saving Mode (PSM) and extended Discontinuous Reception (eDRX), allowing battery life of 5–10 years.
Coverage: NB-IoT uses licensed cellular infrastructure already deployed by carriers. Indoor penetration is exceptional — NB-IoT can reach deep indoors and underground where LoRaWAN might not.

### NB-IoT vs. LoRaWAN

| Attribute | LoRaWAN | NB-IoT |
|---|---|---|
| Spectrum | Unlicensed ISM (free) | Licensed cellular (carrier fee) |
| Uplink data rate | 0.3–50 kbps | Up to 20 kbps |
| Coverage deployment | Private gateways or public networks | Mobile carrier infrastructure |
| Security | AES-128 (two-layer) | LTE security (KASUMI/AES) |
| Regulatory risk | Subject to ISM duty cycle limits | Guaranteed carrier QoS |
| Best for | Rural, private networks, low cost | Urban/indoor, carrier-grade SLA needed |

### NB-IoT Security

NB-IoT inherits the LTE security architecture: mutual authentication between device and network using 128-bit keys stored in a SIM card (USIM). The device authenticates to the network using the USIM challenge-response protocol, and the network authenticates to the device. This is stronger than LoRaWAN's pre-shared key model in that the device can verify it is talking to a legitimate network.

The SIM card containing the NB-IoT credentials becomes a physical security asset that must be protected from extraction and cloning.

---

## Segment 6: Network Segmentation and IoT Wi-Fi Security [18:30 – 20:30]

[SHOW DIAGRAM]

Before we close, I want to reinforce the most critical networking security concept for IoT: network segmentation.

The scenario: you have 50 IP cameras, 30 smart HVAC sensors, and 20 badge readers all connected to a corporate Wi-Fi network. On the same network are employee laptops and a file server containing sensitive data. One of the IP cameras gets compromised through an unpatched firmware vulnerability. What can an attacker do?

Without segmentation: the attacker can scan the entire network, attempt to authenticate to the file server, intercept traffic from other devices, and use the compromised camera as a pivot point into the corporate network. This is called lateral movement.

With segmentation: the IoT devices are on a dedicated VLAN. Firewall rules allow the cameras to send video to a specific cloud endpoint and nothing else. The compromised camera cannot reach the employee laptops or the file server. The blast radius is contained.

The implementation: configure a dedicated IoT VLAN on your managed switch, assign all IoT device Wi-Fi to an SSID that maps to that VLAN, and apply firewall rules at the VLAN boundary.

This is a testable concept on CompTIA IoT+ and an expected control in any professional IoT security review.

---

## Segment 7: Summary and Lab Preview [20:30 – 22:30]

Wi-Fi: high bandwidth, high power, 30–100 m, requires network segmentation. Use for gateways, cameras, and edge nodes with power supply.

BLE: very low power, 10–100 m, 1–2 Mbps, coin-cell battery life. Use for wearables, beacons, and short-range sensors. Require authenticated pairing modes for sensitive applications.

LoRaWAN: extremely low power, 2–15 km, 0.3–50 kbps, unlicensed spectrum. Use for outdoor wide-area sensor deployments where cellular is unavailable or too expensive.

NB-IoT: low power, cellular coverage, up to 200 kbps, licensed spectrum. Use where carrier-grade SLA and indoor penetration matter.

In this week's lab you will analyze a wireless technology selection scenario, evaluate a Wi-Fi network security configuration, and trace a LoRaWAN uplink message from end device through gateway to network server.

See you in Module 06 where we move to the cloud and cover AWS IoT Core, Azure IoT Hub, and Google Cloud IoT.

---

End of Module 05 Video Script
