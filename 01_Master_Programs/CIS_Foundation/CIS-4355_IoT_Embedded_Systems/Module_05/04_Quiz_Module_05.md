# Quiz – Module 05: IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Format:** 10 questions, multiple choice, 4 options each
**Certification Alignment:** CompTIA IoT+ Domain 3

---

## Question 1

Which of the following best describes the LoRaWAN radio technology?

- A) A short-range mesh protocol using IEEE 802.15.4 at 2.4 GHz with AES-128 encryption, suited for dense indoor networks up to 100 meters per hop.
- B) A low-power wide-area network protocol using chirp spread-spectrum modulation, achieving kilometer-scale range at very low data rates with multi-year battery life.
- C) A licensed-spectrum cellular technology using LTE Cat-M1 bands that provides voice fallback capability on 4G infrastructure.
- D) A personal area network standard at 2.4 GHz with frequency-hopping spread spectrum optimized for wearables within 100 meters.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: This describes Zigbee — IEEE 802.15.4, 2.4 GHz, mesh, 100 m per hop. LoRaWAN achieves 2–15 km range and uses chirp spread spectrum, not IEEE 802.15.4.
- B is correct: LoRa uses chirp spread spectrum (CSS) modulation to achieve extraordinary receiver sensitivity, enabling 2–15 km range at 0.3–50 kbps data rates. Duty-cycled transmissions enable multi-year battery life on a small cell.
- C is incorrect: This describes LTE-M (Cat-M1), which uses licensed cellular spectrum and supports voice fallback. LoRaWAN operates on unlicensed ISM spectrum and is not cellular.
- D is incorrect: Frequency-hopping spread spectrum and 100 m range at 2.4 GHz describes Bluetooth Low Energy. LoRaWAN operates at 915 MHz (US) and achieves kilometers of range.

---

## Question 2

A deployment of 200 agricultural soil sensors must transmit daily moisture readings from fields up to 8 km from the nearest gateway, on AA batteries for 3 years, with no cellular coverage. Which technology is correct?

- A) Wi-Fi 802.11ac, because it offers the highest data rate for reliable delivery.
- B) Bluetooth Low Energy, because it consumes the least power of any radio technology.
- C) LoRaWAN, because it provides kilometer-scale range at ultra-low power with sufficient data rate for periodic sensor readings.
- D) Zigbee mesh, because each node can relay messages to cover the 8 km distance.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Wi-Fi consumes 170–300 mA during active transmission. Two AA batteries (approximately 5 Wh total energy) would last days at that draw rate, not 3 years.
- B is incorrect: BLE range is 10–100 m. The 8 km requirement far exceeds BLE capability regardless of its excellent power consumption.
- C is correct: LoRaWAN achieves 2–15 km range. A device transmitting one reading per day has an average current draw under 10 microamps, enabling multi-year battery life on AA cells.
- D is incorrect: Zigbee has a range of 10–100 m per hop. Covering 8 km would require approximately 80 relay nodes, each needing power. This is impractical for a battery-powered field sensor network.

---

## Question 3

A security audit finds that BLE door locks in a secure facility use "Just Works" pairing mode. What is the primary security risk?

- A) Just Works pairing uses WEP encryption, which is cryptographically broken.
- B) Just Works provides no man-in-the-middle authentication, allowing an attacker in range to intercept and manipulate the pairing key exchange.
- C) Just Works disables AES-128 encryption, transmitting all data in cleartext after pairing.
- D) Just Works requires a 6-digit PIN that can be brute-forced in under 60 seconds.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: BLE does not use WEP. WEP is a deprecated Wi-Fi security protocol. BLE uses AES-128 for link encryption after pairing.
- B is correct: BLE Just Works completes the key exchange without any user confirmation step. An attacker within Bluetooth range can perform a man-in-the-middle attack — intercepting the pairing exchange and injecting a key the attacker controls — without triggering any visible warning on either device.
- C is incorrect: Just Works still establishes AES-128 link encryption after the key exchange. The vulnerability is in the unauthenticated key exchange itself, not the absence of encryption.
- D is incorrect: The 6-digit PIN brute-force vulnerability applies to the legacy Passkey Entry mode. Just Works does not use a PIN at all.

---

## Question 4

IoT thermostats share a Wi-Fi network segment with employee laptops and financial servers. Which control most effectively limits the impact if a thermostat is compromised?

- A) Changing the Wi-Fi SSID to a non-descriptive name to obscure the network.
- B) Placing IoT devices on a dedicated VLAN with firewall rules permitting only required outbound cloud traffic and blocking lateral access to corporate segments.
- C) Enabling WPS on the access point to simplify thermostat onboarding.
- D) Using WPA2-Personal with a strong shared passphrase for all devices including thermostats.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Network scanners detect hidden SSIDs trivially. Obscuring the SSID provides no meaningful security barrier.
- B is correct: VLAN segmentation prevents a compromised thermostat from reaching financial servers or employee machines. Firewall rules at the VLAN boundary enforce least-privilege — the thermostat can only reach its designated cloud endpoint, not the rest of the network.
- C is incorrect: WPS has known PIN brute-force vulnerabilities and should be disabled on any network. Enabling it creates an additional attack surface.
- D is incorrect: A shared WPA2-Personal passphrase means every device — including compromised ones — has the same network-layer credential. Once the passphrase is known, there is no barrier to lateral movement within the network segment.

---

## Question 5

In a LoRaWAN network, which entity decrypts the application payload from an end device, and what key does it use?

- A) The LoRaWAN gateway, using the NwkSKey.
- B) The LoRaWAN network server, using the NwkSKey.
- C) The application server, using the AppSKey.
- D) The end device, using the AppEUI.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: LoRaWAN gateways are simple packet forwarders. They receive encrypted LoRa frames and forward them to the network server over IP. They do not hold session keys and do not decrypt payloads.
- B is incorrect: The network server holds the NwkSKey and uses it to verify MAC message integrity and decrypt MAC commands. It does not hold the AppSKey and cannot decrypt application payloads — by design.
- C is correct: The AppSKey (Application Session Key) is shared between the end device and the application server only. The application server uses AppSKey to decrypt the application payload. This design means network operators (who control network servers) cannot read application-layer data.
- D is incorrect: The AppEUI (Application Extended Unique Identifier) is a 64-bit identifier used for device activation, not an encryption key.

---

## Question 6

What is the key difference between NB-IoT and LoRaWAN regarding spectrum licensing and infrastructure?

- A) NB-IoT uses unlicensed 915 MHz spectrum; LoRaWAN uses licensed LTE spectrum.
- B) LoRaWAN uses unlicensed ISM spectrum with privately deployed gateways; NB-IoT uses licensed cellular spectrum operated by mobile carriers.
- C) Both use unlicensed spectrum but NB-IoT operates at 2.4 GHz while LoRaWAN operates at 915 MHz.
- D) LoRaWAN requires a SIM card; NB-IoT uses a DevEUI for network authentication.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The answer has the two protocols reversed. LoRaWAN uses unlicensed ISM spectrum; NB-IoT uses licensed LTE spectrum.
- B is correct: LoRaWAN operates on unlicensed ISM spectrum (915 MHz in the US) using privately owned or public community gateways. NB-IoT uses licensed cellular spectrum, relying on existing mobile carrier infrastructure (towers, core network). This means LoRaWAN has no per-device carrier fees but requires private gateway deployment; NB-IoT has carrier subscription costs but leverages existing infrastructure.
- C is incorrect: NB-IoT does not operate at 2.4 GHz. It uses licensed LTE bands (700 MHz, 850 MHz, 1900 MHz, etc. depending on carrier). 2.4 GHz is used by Wi-Fi, BLE, and Zigbee.
- D is incorrect: LoRaWAN devices use a DevEUI for identification, not a SIM card. NB-IoT uses a USIM card for authentication with the cellular network.

---

## Question 7

A LoRaWAN Class A device transmits an uplink. After the transmission completes, when does the device open its downlink receive windows?

- A) The device opens one receive window continuously for 30 seconds after each uplink.
- B) The device opens RX1 (1 second after uplink) and RX2 (2 seconds after uplink), each for approximately 0.5 seconds.
- C) The device polls the network server every 10 minutes for downlink messages.
- D) The device listens continuously except when transmitting, like a full-duplex radio.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A continuous 30-second receive window would consume battery power that makes multi-year battery life impossible. Class A uses two brief windows, not one extended one.
- B is correct: Class A is the most power-efficient LoRaWAN class. After each uplink, the device opens RX1 at T+1 second (on the same frequency/data rate as the uplink) and RX2 at T+2 seconds (on a fixed frequency/data rate). If no downlink is received in either window, the device returns to sleep.
- C is incorrect: Polling implies the device initiates a request on a fixed schedule. Class A receive windows are not polling — they are brief listening periods immediately following a device-initiated uplink.
- D is incorrect: Continuous listening describes LoRaWAN Class C, the highest power class. Class A listens only in the two brief windows after each uplink.

---

## Question 8

Which Wi-Fi security protocol replaced WPA2-Personal's Pre-Shared Key with SAE (Simultaneous Authentication of Equals), providing forward secrecy against offline dictionary attacks?

- A) WEP (Wired Equivalent Privacy)
- B) WPA (Wi-Fi Protected Access, original)
- C) WPA2-Enterprise
- D) WPA3-Personal

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: WEP is the original and now completely broken Wi-Fi security protocol from the 1990s. It uses RC4 encryption with static keys and is trivially crackable.
- B is incorrect: Original WPA used TKIP which has known vulnerabilities and is deprecated. It did not introduce SAE.
- C is incorrect: WPA2-Enterprise uses 802.1X authentication with a RADIUS server. It does not use SAE. WPA2-Enterprise is strong but distinct from WPA3-Personal.
- D is correct: WPA3-Personal introduced SAE (also known as Dragonfly Key Exchange), which replaces the WPA2 PSK handshake. SAE provides forward secrecy — even if the network passphrase is later compromised, previously captured session traffic cannot be decrypted.

---

## Question 9

What is the primary purpose of NB-IoT's Power Saving Mode (PSM)?

- A) PSM reduces the transmission power to minimum to comply with ISM band duty cycle regulations.
- B) PSM allows an NB-IoT device to negotiate an extended sleep period with the network, eliminating keepalive traffic and enabling multi-year battery life on a cellular connection.
- C) PSM switches the device from licensed LTE spectrum to unlicensed ISM spectrum during periods of inactivity.
- D) PSM encrypts the device's SIM credentials when the radio is idle to prevent SIM cloning attacks.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: PSM is an NB-IoT power management feature, not a regulatory compliance mechanism. Duty cycle limits apply to unlicensed spectrum such as LoRaWAN, not to licensed NB-IoT cellular bands.
- B is correct: In PSM, the device negotiates a timer with the network. During the PSM period the device's radio is completely powered off with no network registration. The device wakes, transmits a burst, then sleeps again. Average current consumption drops to microamps, enabling battery life measured in years on a cellular network.
- C is incorrect: NB-IoT devices do not switch between licensed and unlicensed spectrum. They are bound to the licensed LTE spectrum by their modem hardware and SIM credentials.
- D is incorrect: PSM is a radio power management feature with no cryptographic function.

---

## Question 10

A BLE asset-tracking beacon is deployed in a hospital supply room. A security researcher notices that she can enumerate all beacons using a Bluetooth scanner app, read their advertised Device Name and serial number, and determine which medical supplies each beacon is attached to. Which OWASP IoT Top 10 item does this represent?

- A) OWASP IoT #4 – Lack of Secure Update Mechanism
- B) OWASP IoT #6 – Insufficient Privacy Protection
- C) OWASP IoT #10 – Lack of Physical Hardening
- D) OWASP IoT #1 – Weak, Guessable, or Hardcoded Passwords

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: OWASP IoT #4 relates to how firmware updates are delivered and authenticated, not to data exposed in advertisement packets.
- B is correct: OWASP IoT #6 (Insufficient Privacy Protection) covers scenarios where devices expose sensitive or identifying information without appropriate access controls. BLE beacons advertising supply type, location, and serial number in plaintext allow passive enumeration of hospital inventory by anyone with a Bluetooth scanner — a privacy and operational security concern.
- C is incorrect: OWASP IoT #10 (Lack of Physical Hardening) addresses exposed debug ports, accessible storage, and tamper detection. Passive BLE advertisement exposure is a data privacy issue, not a physical interface vulnerability.
- D is incorrect: OWASP IoT #1 addresses device authentication credentials (passwords, keys). The issue here is not authentication failure but data exposure through unprotected advertising packets.

---

---

### Question 11 (5 points)

A LoRaWAN gateway has a GPS receiver and records the precise receive time for every uplink frame. Which network function uses this timestamp data to determine which gateway received the uplink first?

- A) Adaptive Data Rate (ADR) — to select the fastest spreading factor for the next uplink.
- B) Network server deduplication — to select the best copy of a frame received by multiple gateways.
- C) Application server decryption — to verify that the AppSKey has not expired since the last session.
- D) End device join procedure — to authenticate the device's DevEUI against the network registry.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) ADR uses RSSI and SNR measurements to optimize the spreading factor. It does not use gateway receive timestamps for this purpose.
  - B) When multiple gateways receive the same uplink, the network server deduplicates the copies. It compares the arrival timestamps and RSSI/SNR values to select the highest quality copy, while the others are discarded. The GPS-timestamped fine-timestamp also enables geolocation features.
  - C) AppSKey expiry is managed through session lifecycle mechanisms (re-join), not through timestamps in forwarded packets.
  - D) The join procedure (OTAA) uses AppKey and JoinEUI/DevEUI in a separate message flow. Gateway timestamps are not part of the join authentication.

---

### Question 12 (5 points)

Which BLE pairing mode uses a physical secondary channel — such as NFC tap or QR code scan — to exchange keys, providing the strongest protection against over-the-air interception?

- A) Just Works
- B) Passkey Entry
- C) Numeric Comparison
- D) Out-of-Band (OOB)

- **Correct Answer:** D
- **Distractor Analysis:**
  - A) Just Works performs the key exchange entirely over Bluetooth with no user interaction and no secondary channel. It is the weakest pairing mode — fully vulnerable to MITM attacks.
  - B) Passkey Entry requires the user to enter a 6-digit PIN displayed on one device into the other. The PIN exchange happens over the Bluetooth channel, which can be intercepted during pairing.
  - C) Numeric Comparison requires both devices to display the same 6-digit number and the user to confirm. It provides MITM protection but relies on the user comparing numbers correctly.
  - D) OOB pairing exchanges cryptographic data over a secondary channel that an attacker cannot intercept wirelessly — typically NFC tap or scanning a QR code. An attacker would need physical access to intercept the OOB channel, making it the most secure pairing mode.

---

### Question 13 (5 points)

A LoRaWAN end device using OTAA (Over-the-Air Activation) completes a Join procedure. Which two session keys are derived from this join, and from what inputs are they generated?

- A) NwkSKey and AppSKey, both derived from the AppKey combined with the JoinNonce, NetID, and DevNonce using AES-128.
- B) DevEUI and AppEUI, exchanged in plaintext during the join to identify the device to the network.
- C) Network key and device key, pre-loaded at manufacturing and never changed after deployment.
- D) TLS client certificate and TLS server certificate, generated during the DTLS handshake over the join channel.

- **Correct Answer:** A
- **Distractor Analysis:**
  - A) In OTAA, the device and join server (application server) both hold the AppKey. After a successful join, both sides derive NwkSKey and AppSKey using AES-128 encryption of the JoinNonce (from join accept), the NetID, and the DevNonce (random value sent in the join request). The derived keys are unique per join session.
  - B) DevEUI and AppEUI are identifiers, not session keys. They are transmitted during the join request but do not serve as encryption keys.
  - C) Pre-loaded unchanging keys describe ABP (Activation by Personalization), not OTAA. OTAA derives fresh keys on every join, providing better forward secrecy.
  - D) LoRaWAN uses AES-128 symmetric keys, not TLS certificates. DTLS is used by CoAP, not LoRaWAN.

---

### Question 14 (5 points)

Wi-Fi 6 (802.11ax) introduced BSS Coloring to improve performance in dense IoT deployments. What does BSS Coloring do?

- A) It assigns each access point a color code that the operating system uses to select the best visual theme for the network management dashboard.
- B) It adds a color identifier to each Wi-Fi frame so devices can quickly distinguish between frames from their own Basic Service Set and overlapping BSSs, reducing unnecessary backoff and improving channel reuse.
- C) It color-codes IoT device categories (sensors, actuators, gateways) so the router can apply QoS policies based on device type.
- D) It maps each SSID to a specific color on the 2.4 GHz spectrum to prevent channel overlap between neighboring networks.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) BSS Coloring has nothing to do with user interface themes. It is a radio-layer mechanism.
  - B) In dense environments, 802.11 radios waste airtime backing off for frames from other networks that do not actually affect them. BSS Coloring adds a 6-bit color field to PHY headers. Devices can quickly identify frames from other BSSs as foreign and skip unnecessary deferral, dramatically improving throughput in dense IoT deployments with many overlapping networks.
  - C) Device type classification for QoS is a separate network policy function. BSS Coloring has no knowledge of device categories.
  - D) BSS Coloring does not manipulate the radio spectrum or channel assignments. It is a MAC/PHY layer identifier that aids in medium access decisions.

---

### Question 15 (5 points)

A campus deploys NB-IoT parking sensors. An operator notes that each sensor has a 15-year battery life target but currently contacts the network every 10 seconds to send a "no change" heartbeat. Which NB-IoT feature should be configured to extend battery life while still reporting occupancy changes within 30 seconds?

- A) Enable eDRX (Extended Discontinuous Reception) with a 20-second cycle to reduce listening intervals while meeting the 30-second response window.
- B) Disable the cellular modem entirely and use LoRaWAN instead.
- C) Increase the transmission power to reduce the number of retransmissions required, lowering average energy.
- D) Configure the SIM card for roaming mode to connect to a less congested carrier tower.

- **Correct Answer:** A
- **Distractor Analysis:**
  - A) eDRX allows the device to negotiate with the network to sleep for configurable intervals (seconds to minutes) between checks for downlink pages, instead of listening every few hundred milliseconds. A 20-second eDRX cycle means the sensor checks for network pages every 20 seconds — well within the 30-second response requirement — while consuming a small fraction of the current drawn by continuous reception.
  - B) Replacing NB-IoT with LoRaWAN is a complete technology change that may not be appropriate for an urban cellular-covered campus. The question asks for an NB-IoT feature, not a technology migration.
  - C) Increasing transmission power increases per-transmission energy consumption. It reduces retransmissions only in poor signal conditions — it does not help when the issue is the frequency of heartbeat transmissions.
  - D) Roaming mode selects a different carrier tower but does not change the power consumption pattern. PSM and eDRX are the correct power-saving features.

---

### Question 16 (5 points)

A smart meter uses Zigbee to communicate with a home area network (HAN) hub. Which Zigbee device role does the smart meter most likely occupy, and what communication constraint follows from that role?

- A) Zigbee Coordinator, meaning only one smart meter can exist per HAN network.
- B) Zigbee Router, meaning the smart meter can relay messages from other Zigbee devices in the home.
- C) Zigbee End Device, meaning the smart meter cannot route traffic for other devices and must communicate through a parent router or coordinator.
- D) Zigbee Gateway, meaning the smart meter bridges Zigbee to Ethernet and requires a wired uplink.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) The Coordinator is a single network-initializing device. Smart meters are leaf nodes, not coordinators. The HAN hub typically plays the coordinator role.
  - B) Router devices must be mains-powered to stay awake and forward packets at any time. Smart meters in residential settings are typically mains-powered, so they could technically be routers, but in Zigbee smart energy profiles, meters are standardly specified as end devices communicating with the hub.
  - C) In Zigbee Smart Energy profile (used for smart meters and HAN devices), the utility meter registers as an end device or router depending on the deployment. As an end device, it cannot relay messages for other nodes and must associate with a router or coordinator as its parent. This is the standard exam answer for smart meter Zigbee role.
  - D) Zigbee Gateway is not a Zigbee protocol device role — it is an informal term for a bridge device that is architecturally separate from the Zigbee network topology roles.

---

### Question 17 (5 points)

An IoT device provisioning system uses WPS Push Button Configuration (PBC) to connect new devices to the Wi-Fi network. What specific attack does this enable, and what is the recommended mitigation?

- A) WPS PBC enables a replay attack on HTTPS provisioning packets; disable HTTPS on the management interface.
- B) WPS PBC is vulnerable to a race-condition attack where any device within range that sends a WPS PBC request within the 2-minute window can join the network; disable WPS entirely and use WPA3-Personal for new device onboarding.
- C) WPS PBC broadcasts the WPA2 passphrase in cleartext during the button press; encrypt the provisioning channel with TLS.
- D) WPS PBC requires physical access to the device, making it immune to remote attacks.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) WPS PBC does not interact with HTTPS provisioning. The vulnerability is in the WPS protocol itself, not in a web management interface.
  - B) WPS PBC opens a 2-minute enrollment window after the button is pressed. During this window, any device that initiates a WPS exchange can join the network — there is no device authentication. An attacker with a WPS-capable device within radio range during this window can enroll an unauthorized device. WPS also has a separate PIN brute-force vulnerability. The mitigation is to disable WPS entirely.
  - C) The WPA2 passphrase is never broadcast. WPS PBC generates a new session key during the enrollment handshake. The vulnerability is race condition enrollment, not passphrase disclosure.
  - D) WPS PBC does not require physical device access — only proximity within Wi-Fi range. This makes it remotely exploitable by any attacker near the building during the 2-minute window.

---

### Question 18 (5 points)

What is the maximum payload size for a LoRaWAN message at SF7 BW125 (the highest data rate setting), and why does the payload size decrease at higher spreading factors?

- A) 222 bytes at SF7; higher SF uses smaller frames to reduce collision probability in the gateway receive buffer.
- B) 51 bytes at all spreading factors; LoRaWAN enforces a fixed maximum payload regardless of data rate.
- C) 242 bytes at SF7; lower payload limits at higher spreading factors are enforced by regional duty cycle regulations, not physics.
- D) 222 bytes at SF7; higher spreading factors have much longer time-on-air per symbol, making long payloads exceed the duty cycle limits imposed by regional regulations.

- **Correct Answer:** D
- **Distractor Analysis:**
  - A) Collision probability at the gateway is managed by the network server through deduplication and channel planning, not by reducing frame size. The payload size limit is driven by duty cycle compliance.
  - B) LoRaWAN payload limits are not fixed — they vary by data rate and regional parameters. At SF12 the practical maximum payload is 51 bytes in many regions; at SF7 it is 222 bytes (LoRaWAN Regional Parameters for US915).
  - C) The duty cycle limit is the correct regulatory mechanism, but the direction is wrong. Higher spreading factors have longer time-on-air, not shorter. To stay within the duty cycle (e.g., 1% in EU868), long transmissions must carry less data or the device must wait longer between transmissions.
  - D) At SF12, each symbol takes 32x longer than at SF7. A 222-byte payload at SF12 would have a time-on-air of several seconds, violating regional duty cycle limits. LoRaWAN regional parameters reduce the maximum payload at higher SFs to keep transmissions within allowed duty cycles.

---

### Question 19 (5 points)

A building has Zigbee smart lighting. An attacker obtains the Zigbee network key through a social engineering attack on an employee. What can the attacker do with this key?

- A) Decrypt all past Zigbee network traffic captured before the key was compromised, because Zigbee provides forward secrecy.
- B) Only subscribe to Zigbee advertising packets — the network key does not grant access to joined device communications.
- C) Decrypt and inject Zigbee network layer traffic, potentially issuing commands to lights and other devices on the network.
- D) Access the LoRaWAN network server because Zigbee and LoRaWAN share the same AES-128 key infrastructure.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Zigbee does not provide forward secrecy. The network key is a static shared secret. If captured, all past traffic can be decrypted with it — but the question says the attacker obtained the key, not past traffic, so this option is describing a property that actually makes the situation worse, not better.
  - B) The Zigbee network key encrypts all network layer frames between joined devices. An attacker with the key can decrypt any network-layer message and craft valid encrypted commands. It is not limited to advertising packets.
  - C) The Zigbee network key is used to encrypt and authenticate network layer frames. With the key, an attacker can decrypt all Zigbee network traffic and craft valid encrypted commands — including turning lights on/off, triggering alarms, or jamming device responses. The link key (if configured) provides additional per-device protection, but network-layer access is fully compromised.
  - D) Zigbee and LoRaWAN are entirely separate protocols with separate key management systems. Compromising a Zigbee key has no effect on a LoRaWAN deployment.

---

### Question 20 (5 points)

An IoT developer is choosing between LoRaWAN OTAA (Over-the-Air Activation) and ABP (Activation by Personalization) for a fleet of 1,000 sensors. Which statement correctly identifies the security tradeoff?

- A) ABP is more secure because the session keys are generated fresh on every power cycle.
- B) OTAA is more secure because each join generates unique session keys, and the frame counter resets cleanly after each join; ABP's hardcoded session keys and static frame counters create replay attack risks after device reset.
- C) Both activation methods provide equivalent security because both use AES-128 session keys.
- D) ABP is preferred for large deployments because the join procedure creates network overhead that OTAA eliminates.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) In ABP, session keys are hardcoded at manufacturing and never change. A device reset in ABP does not generate new keys; the same keys are used for the entire device lifetime.
  - B) OTAA generates a fresh NwkSKey and AppSKey on every join. This provides session key freshness and limits the impact of key compromise. ABP devices have static keys stored in firmware — extractable by physical access — and the frame counter is typically reset to 0 on device reboot, enabling replay attacks unless the network server disables frame counter checking.
  - C) Both use AES-128, but key management differences create very different security postures. OTAA's key derivation and session freshness make it substantially more secure than ABP despite using the same cipher.
  - D) While OTAA does add join overhead, this is a minor operational concern. Security best practice is to use OTAA. ABP's frame counter and static key issues are more significant problems than OTAA join overhead for a 1,000-device fleet.

---

End of Quiz – Module 05
