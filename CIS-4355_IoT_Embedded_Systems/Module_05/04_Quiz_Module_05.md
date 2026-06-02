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

End of Quiz – Module 05
