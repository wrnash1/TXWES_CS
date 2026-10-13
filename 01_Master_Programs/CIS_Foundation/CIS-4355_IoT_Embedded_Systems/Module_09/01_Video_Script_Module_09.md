# Video Script: Module 09 — IoT Wireless Networking

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Estimated Duration:** 20–24 minutes

**Certification Alignment:** IoT Fundamentals / Embedded Systems

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4355. I'm Professor Nash. In Module 08 we connected sensors to microcontrollers. Now we cut the cord and go wireless.

IoT wireless networking is not one technology — it is a family of technologies, each optimized for a different set of trade-offs between range, data rate, power consumption, and cost. Today we cover the major options: Wi-Fi using the ESP32's built-in radio, Bluetooth Classic and BLE, Zigbee, Z-Wave, LoRaWAN, and cellular IoT — NB-IoT and LTE-M.

By the end of this module you will be able to connect an ESP32 to a Wi-Fi network, advertise a BLE beacon, and select the right wireless standard for any IoT deployment scenario based on its specific requirements.

---

## SEGMENT 2 — Wi-Fi on the ESP32 (1:30–5:00)

[SHOW HARDWARE: ESP32 DevKit, USB connected, Serial Monitor open showing Wi-Fi connection log]

The ESP32 has a built-in 802.11 b/g/n Wi-Fi radio that supports both Station mode (connecting to an existing access point) and Access Point mode (acting as an AP itself). The Wi-Fi library is part of the ESP32 Arduino core.

Station mode — connecting to your router — is the most common use case:

```cpp
#include <WiFi.h>

const char* SSID = "YourNetwork";
const char* PASS = "YourPassword";

void setup() {
  Serial.begin(115200);
  WiFi.begin(SSID, PASS);

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.printf("Connected! IP: %s\n", WiFi.localIP().toString().c_str());
  Serial.printf("RSSI: %d dBm\n", WiFi.RSSI());
}

void loop() {
  // Application code here
}
```

The `WiFi.RSSI()` value is the Received Signal Strength Indicator in dBm. Values around -30 to -50 dBm indicate excellent signal. Below -80 dBm, connections become unreliable.

Wi-Fi Access Point mode lets the ESP32 create its own network — useful for direct configuration from a phone without internet access:

```cpp
WiFi.softAP("ESP32-Config", "setup1234");
Serial.printf("AP IP: %s\n", WiFi.softAPIP().toString().c_str());
```

Wi-Fi power consumption is the ESP32's biggest drawback for battery-powered IoT. The Wi-Fi radio consumes 80–170 mA during active transmission. The solution is modem sleep and deep sleep: the ESP32 can turn off the Wi-Fi radio between transmissions, consuming only 10–20 mA, or enter deep sleep at under 10 µA and wake on a timer.

```cpp
// Deep sleep for 60 seconds, then wake and send one reading
esp_deep_sleep(60 * 1000000LL);  // microseconds
```

---

## SEGMENT 3 — Bluetooth and BLE (5:00–8:30)

[SHOW HARDWARE: ESP32 with BLE active, phone's Bluetooth scanner showing ESP32 advertising]

The ESP32 supports both Bluetooth Classic (BR/EDR) and Bluetooth Low Energy. In IoT, BLE is far more common because of its dramatically lower power consumption.

Bluetooth Classic creates a persistent connection with continuous data streaming — think audio headsets and file transfer. BLE is designed for intermittent, small data transfers — think heart rate monitors, temperature beacons, and proximity sensors.

BLE has three key concepts:

**Advertising:** A BLE peripheral broadcasts small packets (advertisement packets) every 20ms to 10 seconds. Scanners in range receive these without pairing. This is how beacons work — broadcasting a UUID and optional data with no connection required.

**GATT (Generic Attribute Profile):** When a central device (like a phone) connects to a peripheral (like a sensor), they communicate through a structured hierarchy: Profile → Service → Characteristic → Descriptor. Each characteristic has a UUID, a value, and optional notify/indicate properties.

**Profiles:** Standardized collections of services. The Heart Rate Profile, Environmental Sensing Profile, and Device Information Profile are defined by the Bluetooth SIG and supported natively by most smartphones.

BLE Beacon on ESP32:

```cpp
#include <BLEDevice.h>
#include <BLEAdvertising.h>

BLEAdvertising* pAdv;

void setup() {
  BLEDevice::init("TempSensor-01");
  pAdv = BLEDevice::getAdvertising();
  pAdv->addServiceUUID("181A");  // Environmental Sensing UUID
  pAdv->setScanResponse(true);
  pAdv->setMinPreferred(0x06);
  BLEDevice::startAdvertising();
  Serial.println("BLE advertising started");
}

void loop() {
  delay(1000);
}
```

BLE advertising at 1-second intervals consumes roughly 0.1 mA average — dramatically less than Wi-Fi's 80–170 mA.

---

## SEGMENT 4 — Zigbee (8:30–10:30)

Zigbee is an IEEE 802.15.4-based mesh networking protocol designed for low-power, low-data-rate sensor networks. It operates on the 2.4 GHz band (global) and 868/915 MHz bands (regional).

Key Zigbee features:

- **Mesh topology:** Each node can act as a router, forwarding messages for other nodes. This extends range far beyond direct radio line-of-sight.
- **Low power:** End devices (sensors) can sleep for long periods, waking only to transmit. Typical current draw: 30 mA during TX, 1 µA in sleep.
- **Maximum nodes:** Up to 65,000 nodes per network — essential for large industrial deployments.
- **Data rate:** 250 kbps — adequate for sensor data but not video or audio.

Zigbee is the dominant protocol in smart home products (Philips Hue, IKEA Tradfri, SmartThings) and industrial wireless sensor networks. The Zigbee Alliance is now the Connectivity Standards Alliance, which also manages the Matter standard.

The main limitation: Zigbee requires a coordinator (gateway) to connect the mesh network to the internet or a cloud platform.

---

## SEGMENT 5 — Z-Wave (10:30–12:00)

Z-Wave is a proprietary mesh networking protocol designed specifically for home automation. It operates at 800–900 MHz — below the crowded 2.4 GHz band — giving it better wall penetration than Zigbee or Wi-Fi.

Z-Wave characteristics:

- Maximum 232 nodes per network
- Data rate: 100 kbps
- Interference-free: operates at sub-GHz frequencies away from Wi-Fi and Bluetooth
- Interoperability: Z-Wave Alliance certification guarantees devices from different manufacturers work together
- Power: similar to Zigbee — very low for sleeping end devices

Z-Wave is popular in premium home automation systems and smart locks. Its proprietary nature means higher chip costs than Zigbee, which uses an open standard.

---

## SEGMENT 6 — LoRaWAN (12:00–15:00)

LoRaWAN is where IoT gets exciting for long-range applications. LoRa (Long Range) is a spread-spectrum radio modulation technique. LoRaWAN is the network protocol built on top of LoRa.

LoRaWAN specifications:

- **Range:** 2–5 km in urban environments; up to 15 km in rural line-of-sight
- **Data rate:** 0.3–50 kbps (very low — messages are short, infrequent)
- **Power:** Extremely low — a coin cell can power a LoRa sensor for years
- **Frequency:** 915 MHz (US), 868 MHz (EU), 433 MHz (Asia)
- **Topology:** Star of stars — end devices transmit to gateways; gateways connect to the cloud

LoRaWAN uses the Chirp Spread Spectrum modulation, which gives it remarkable resistance to interference and the ability to decode signals 20 dB below the noise floor. This is how it achieves multi-kilometer range with milliwatt power levels.

The trade-off: duty cycle regulations limit transmissions to 1% of the time in many regions. A LoRa sensor sending a 20-byte payload once every 10 minutes is typical. LoRaWAN is not suitable for streaming data or frequent updates.

Major LoRaWAN network providers: The Things Network (free community network), Helium (crypto-incentivized), and private enterprise networks.

---

## SEGMENT 7 — Cellular IoT: NB-IoT and LTE-M (15:00–17:30)

Cellular IoT uses licensed spectrum — the same infrastructure as your mobile phone — to connect IoT devices.

**NB-IoT (Narrowband IoT):** Designed for static, infrequent-reporting devices. 20–200 kbps data rate. Deep indoor penetration. Very low power — devices can sleep for years on a battery. Example use cases: utility meters, parking sensors, asset trackers that update once per hour.

**LTE-M (LTE Cat-M1):** Designed for mobile and voice-capable IoT. 1 Mbps data rate. Supports handover between towers (device can move). Lower latency than NB-IoT. Example use cases: wearables, vehicle tracking, mobile health monitors.

Both NB-IoT and LTE-M use SIM cards and require a carrier contract. Per-device monthly costs range from $1–$10 depending on data usage.

The major advantage over LoRaWAN: cellular IoT uses existing infrastructure. Anywhere there is cellular coverage, your device works. No gateway needed. The disadvantage: cost and power consumption are higher than LoRaWAN, though still far lower than LTE/4G.

---

## SEGMENT 8 — Network Selection Framework (17:30–20:00)

Here is how to select the right wireless technology for any IoT deployment:

| Technology | Range | Data Rate | Power | Cost/device | Best Use Case |
|------------|-------|-----------|-------|-------------|---------------|
| Wi-Fi | 50m | 54+ Mbps | High | Low | Mains-powered, high-data devices |
| BLE | 10–50m | 1–2 Mbps | Very low | Low | Beacons, wearables, phone proximity |
| Zigbee | 10–100m mesh | 250 kbps | Low | Low | Smart home mesh, large sensor grids |
| Z-Wave | 30–100m mesh | 100 kbps | Low | Medium | Premium home automation |
| LoRaWAN | 2–15 km | 0.3–50 kbps | Extremely low | Low | Rural sensors, smart cities, agriculture |
| NB-IoT | Cellular | 200 kbps | Very low | Medium + carrier | Utility meters, static trackers |
| LTE-M | Cellular | 1 Mbps | Low | Medium + carrier | Mobile trackers, wearables |

Ask three questions:

- How far does the data need to travel? Meters — BLE or Zigbee. Kilometers — LoRaWAN or cellular.
- How much data? Small infrequent packets — any low-power option. Streaming — Wi-Fi or LTE-M.
- Does the device move? No — any technology. Yes, globally — cellular. Yes, locally — BLE or Zigbee mesh.

---

## SEGMENT 9 — Wrap-Up and Preview (20:00–22:00)

Let's recap. Wi-Fi gives the ESP32 full internet connectivity but at high power cost. BLE enables energy-efficient proximity sensing, beacons, and phone connectivity. Zigbee and Z-Wave provide mesh networking for dense smart home and industrial deployments. LoRaWAN enables multi-kilometer range at extremely low power for infrequent, small payloads. NB-IoT and LTE-M bring cellular reliability to IoT without the cost of full 4G.

The selection framework — range, data rate, power, cost, and mobility — gives you a principled way to choose.

In Module 10 we take these connected devices to the cloud. We will configure AWS IoT Core, create device certificates, set up shadow states, and build rules that trigger Lambda functions from sensor data. That is where the full IoT pipeline — sensor to cloud to action — comes together.

See you there.

---

## PRODUCTION NOTES

- B-roll: nRF Sniffer showing BLE advertisement packets; LoRa gateway on rooftop; phone BLE scanner showing ESP32 device
- Slide: wireless technology comparison table with range circles visualization
- Demo: ESP32 connecting to Wi-Fi and printing RSSI; BLE scanner on phone showing advertised device name
- Closed captions: verify LoRaWAN, NB-IoT, LTE-M, GATT, BLE, Zigbee, Z-Wave, chirp spread spectrum
- Run time target: 21 minutes
