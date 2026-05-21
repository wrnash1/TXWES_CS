# Quiz: Module 05 - IoT Networking – Wi-Fi, Bluetooth, LoRaWAN, NB-IoT
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What is the communication pattern utilized in the MQTT protocol?
*   A) Client-Server HTTP request-response over TCP
*   B) Publish-Subscribe via a central broker
*   C) Peer-to-peer streaming with no intermediary
*   D) File transfer using FTP commands
*   **Correct Answer:** B) Clients publish data to topics on a central broker, which routes messages to all matching subscribers.
*   **Distractor Analysis:**
    *   *Why correct:* Clients publish data to topics on a central broker, which routes messages to subscribed clients without direct publisher-to-subscriber connections.
    *   HTTP uses a synchronous Request-Response pattern; MQTT's pub-sub model decouples senders from receivers entirely.

---

**Question 2**
Which of the following is the most accurate definition of **LoRaWAN long-range** networking?
*   A) A short-range mesh protocol using IEEE 802.15.4 at 2.4 GHz with AES-128 encryption, suited for dense indoor sensor networks up to 100 m per hop.
*   B) A low-power wide-area network protocol using chirp spread-spectrum modulation, achieving kilometer-scale range at very low data rates with multi-year battery life.
*   C) A licensed-spectrum cellular technology using LTE Cat-M1 bands that provides IoT connectivity with voice fallback capability on existing 4G infrastructure.
*   D) A personal area network standard operating at 2.4 GHz with frequency-hopping spread spectrum, optimized for wearables and health monitors within 100 m.
*   **Correct Answer:** B) A low-power wide-area network protocol using chirp spread-spectrum modulation, achieving kilometer-scale range at very low data rates with multi-year battery life.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Zigbee's IEEE 802.15.4 mesh networking, not LoRaWAN.
    *   *Why B is correct:* LoRaWAN uses LoRa modulation (chirp spread spectrum) for 2–15 km range at 0.3–50 kbps, with AES-128 session keys for security.
    *   *Why C is incorrect:* This describes NB-IoT or LTE-M, which use licensed cellular spectrum — not LoRaWAN's unlicensed ISM band.
    *   *Why D is incorrect:* This describes Bluetooth Low Energy (BLE), not LoRaWAN.

---

**Question 3**
A deployment of 200 agricultural soil sensors must transmit daily moisture readings from fields up to 8 km from the nearest gateway, running on AA batteries for 3 years with no cellular coverage. Which wireless technology is most appropriate?
*   A) Wi-Fi 802.11ac, because it offers the highest data rate for reliable delivery.
*   B) Bluetooth Low Energy (BLE), because it consumes the least power of any radio technology.
*   C) LoRaWAN, because it provides kilometer-scale range at ultra-low power with a suitable LPWAN data rate for periodic sensor readings.
*   D) Zigbee mesh, because each node can relay messages across the 8 km distance through intermediate hops.
*   **Correct Answer:** C) LoRaWAN, because it provides kilometer-scale range at ultra-low power with a suitable LPWAN data rate for periodic sensor readings.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Wi-Fi consumes 50–300 mA during transmission — battery life would be days or weeks, not years.
    *   *Why B is incorrect:* BLE range is typically 10–100 m, far short of the 8 km requirement, regardless of its low power draw.
    *   *Why C is correct:* LoRaWAN achieves 2–15 km range, uses duty-cycled transmissions drawing microamps on average, and a daily reading requires only seconds of radio-on time per day.
    *   *Why D is incorrect:* Zigbee nodes relay within ~100 m per hop; achieving 8 km would require ~80 relay nodes, which is impractical and power-expensive.

---

**Question 4**
A security audit of a smart building's BLE access control system finds that all door locks use "Just Works" BLE pairing mode. What is the primary security risk?
*   A) BLE Just Works pairing uses WEP encryption, which is cryptographically broken.
*   B) Just Works pairing provides no man-in-the-middle authentication, allowing an attacker in range to intercept and manipulate the pairing exchange.
*   C) BLE Just Works mode disables AES-128 encryption, sending all data in cleartext.
*   D) Just Works pairing requires a 6-digit PIN that can be brute-forced in under 60 seconds.
*   **Correct Answer:** B) Just Works pairing provides no man-in-the-middle authentication, allowing an attacker in range to intercept and manipulate the pairing exchange.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* BLE does not use WEP; it uses AES-128. WEP is a deprecated Wi-Fi protocol.
    *   *Why B is correct:* BLE Just Works completes pairing without numeric confirmation or passkey, so an attacker can perform a MITM attack, impersonating either the central or peripheral device during the key exchange.
    *   *Why C is incorrect:* Just Works still uses AES-128 for link encryption after pairing; the vulnerability is in the unauthenticated key exchange, not the absence of encryption.
    *   *Why D is incorrect:* The 6-digit PIN brute-force vulnerability applies to the legacy "Passkey Entry" mode, not Just Works.

---

**Question 5**
An IoT deployment places smart thermostats on the same Wi-Fi network segment as employee laptops and financial servers. Which security control most effectively limits the blast radius if a thermostat is compromised?
*   A) Changing the Wi-Fi SSID to a non-descriptive name to obscure the network from attackers.
*   B) Placing IoT devices on a dedicated VLAN with firewall rules that permit only required outbound cloud traffic and block lateral access to corporate segments.
*   C) Enabling WPS on the access point to simplify device onboarding and reduce configuration errors.
*   D) Using WPA2-Personal with a strong shared passphrase across all devices including the thermostats.
*   **Correct Answer:** B) Placing IoT devices on a dedicated VLAN with firewall rules that permit only required outbound cloud traffic and block lateral access to corporate segments.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Obscuring the SSID provides no real security; network scanners detect hidden networks trivially.
    *   *Why B is correct:* Network segmentation via VLAN prevents a compromised thermostat from reaching financial servers or employee machines — this is the OWASP IoT-recommended isolation control.
    *   *Why C is incorrect:* WPS has known PIN brute-force vulnerabilities and should be disabled, not enabled, on networks with IoT devices.
    *   *Why D is incorrect:* A shared WPA2 passphrase means all devices — including compromised thermostats — share the same network access credentials, providing no lateral movement protection.
