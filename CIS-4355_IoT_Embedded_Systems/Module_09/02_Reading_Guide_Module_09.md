# Reading Guide: Module 09 — IoT Wireless Networking

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4355 &BULL; INTERNET OF THINGS (IOT) & EMBEDDED SYSTEMS</text>
    
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


**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Certification Target:** IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you will be able to:

1. Configure the ESP32 Wi-Fi library for station mode and explain power management options
2. Describe BLE advertising, GATT hierarchy, and the difference between BLE beacons and connected profiles
3. Contrast Zigbee and Z-Wave mesh protocols on frequency, node limit, and market application
4. Explain LoRaWAN's spread-spectrum modulation, duty cycle constraints, and typical use cases
5. Differentiate NB-IoT and LTE-M on data rate, mobility support, and power consumption
6. Apply the network selection framework to choose the correct wireless technology for a given deployment scenario

---

## Section 1 — Wi-Fi (IEEE 802.11)

### 1.1 ESP32 Wi-Fi Modes

The ESP32 supports three Wi-Fi operating modes:

| Mode | Description | Use Case |
|------|-------------|----------|
| Station (STA) | Connects to existing access point | Most IoT deployments |
| Access Point (AP) | Creates its own Wi-Fi network | Local configuration, peer-to-peer |
| Station + AP | Both simultaneously | Mesh bridging, local API + cloud |

### 1.2 Wi-Fi Connection Management

Always implement reconnection logic for production devices:

```cpp
#include <WiFi.h>

const char* SSID = "NetworkName";
const char* PASS = "Password";

void ensureWiFi() {
  if (WiFi.status() == WL_CONNECTED) return;

  Serial.print("Reconnecting WiFi");
  WiFi.disconnect();
  WiFi.begin(SSID, PASS);

  uint8_t attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.printf("\nConnected. IP: %s RSSI: %d dBm\n",
      WiFi.localIP().toString().c_str(), WiFi.RSSI());
  } else {
    Serial.println("\nFailed — will retry next cycle");
  }
}
```

### 1.3 Wi-Fi Power Management

| Mode | Current | Description |
|------|---------|-------------|
| Active TX | 80–170 mA | Transmitting/receiving |
| Active RX | 60–80 mA | Receiving only |
| Modem sleep | 10–20 mA | CPU running, Wi-Fi paused between beacons |
| Light sleep | 0.8 mA | CPU paused, Wi-Fi active on schedule |
| Deep sleep | 5–10 µA | Everything off except RTC; wake on timer or GPIO |

For battery IoT devices using Wi-Fi, the standard pattern is:

1. Wake from deep sleep
2. Connect to Wi-Fi (takes 1–3 seconds)
3. Publish sensor data (MQTT or HTTP)
4. Disconnect and enter deep sleep for N minutes

This achieves average current consumption of under 1 mA for a device sampling every 5 minutes.

### 1.4 RSSI Signal Strength Guide

| RSSI (dBm) | Signal Quality |
|------------|----------------|
| -30 to -50 | Excellent |
| -50 to -60 | Good |
| -60 to -70 | Fair |
| -70 to -80 | Weak |
| Below -80 | Unreliable |

---

## Section 2 — Bluetooth Low Energy (BLE)

### 2.1 BLE vs Bluetooth Classic

| Feature | Bluetooth Classic | BLE |
|---------|------------------|-----|
| Data rate | 2–3 Mbps | 1–2 Mbps |
| Range | 10–100m | 10–50m |
| Power | 50–100 mA active | 0.01–15 mA |
| Connection setup | Pairing required | Optional |
| Use case | Audio, file transfer | Sensors, beacons, wearables |
| Profile examples | A2DP, HFP, SPP | GATT, GAP, iBeacon |

### 2.2 BLE Advertising

Advertisement packets are 31 bytes maximum and broadcast repeatedly at a configurable interval (advertising interval). No connection is required — scanners receive them passively.

Common advertisement data types:

- **Complete Local Name:** Human-readable device name
- **Service UUID:** Indicates what GATT services the device supports
- **Manufacturer Specific Data:** Custom payload (used by iBeacon, Eddystone)
- **TX Power Level:** Allows scanners to estimate distance

iBeacon format packs a 16-byte UUID, a 2-byte Major, and a 2-byte Minor into the Manufacturer Specific Data field. The combination uniquely identifies a location or asset.

### 2.3 GATT Hierarchy

```text
Profile (e.g., Environmental Sensing Profile)
  └── Service (e.g., 0x181A Environmental Sensing)
        ├── Characteristic (e.g., 0x2A6E Temperature)
        │     ├── Value (2 bytes, signed 16-bit, 0.01°C resolution)
        │     └── Descriptor (0x2902 Client Characteristic Config — enables notify)
        └── Characteristic (e.g., 0x2A6F Humidity)
              └── Value (2 bytes, unsigned 16-bit, 0.01% resolution)
```

A central device (phone or hub) connects, discovers services, reads or subscribes to characteristics, and receives notifications when values change.

### 2.4 BLE Server on ESP32

```cpp
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#define TEMP_SERVICE_UUID   "181A"
#define TEMP_CHAR_UUID      "2A6E"

BLECharacteristic* pTempChar;

void setup() {
  BLEDevice::init("TempSensor-Lab");
  BLEServer* pServer = BLEDevice::createServer();
  BLEService* pService = pServer->createService(TEMP_SERVICE_UUID);

  pTempChar = pService->createCharacteristic(
    TEMP_CHAR_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
  );
  pTempChar->addDescriptor(new BLE2902());

  pService->start();
  BLEDevice::getAdvertising()->start();
  Serial.println("BLE server running");
}

void loop() {
  int16_t tempRaw = (int16_t)(23.45f * 100);  // 0.01 degree resolution
  pTempChar->setValue((uint8_t*)&tempRaw, 2);
  pTempChar->notify();
  delay(5000);
}
```

---

## Section 3 — Zigbee

### 3.1 Network Topology

Zigbee networks consist of three device types:

| Device Type | Role | Power |
|-------------|------|-------|
| Coordinator | Starts and manages the network; one per network | Mains-powered |
| Router | Forwards messages; extends range | Mains-powered |
| End Device | Sensor or actuator; sleeps between events | Battery-powered |

The mesh topology means that end devices can communicate through multiple hops of routers, extending network coverage far beyond the radio range of a single device.

### 3.2 Zigbee vs Z-Wave

| Feature | Zigbee | Z-Wave |
|---------|--------|--------|
| Standard | Open (IEEE 802.15.4) | Proprietary (Silicon Labs) |
| Frequency | 2.4 GHz (global) | 800–900 MHz (sub-GHz) |
| Max nodes | 65,000 | 232 |
| Data rate | 250 kbps | 100 kbps |
| Wall penetration | Moderate | Good (sub-GHz) |
| Certification | Zigbee Alliance (now CSA) | Z-Wave Alliance |
| Ecosystem | Large, open | Premium home automation |

### 3.3 Zigbee in Smart Home

The Zigbee Alliance's Matter standard (formerly Project CHIP) is the convergence protocol that allows Zigbee, Z-Wave, and Thread devices to interoperate natively with Apple HomeKit, Google Home, and Amazon Alexa without cloud bridges.

---

## Section 4 — LoRaWAN

### 4.1 LoRa Physical Layer

LoRa uses Chirp Spread Spectrum (CSS) modulation. A chirp is a signal that continuously increases or decreases in frequency. The data is encoded in the rate of frequency change, not the frequency itself. This gives LoRa extraordinary interference rejection — it can decode signals 19.5 dB below the noise floor.

Spreading Factor (SF) controls the trade-off between range and data rate:

| SF | Range | Data Rate | Time on Air (20 bytes) |
|----|-------|-----------|----------------------|
| SF7 | Shortest | ~5.5 kbps | 56 ms |
| SF9 | Medium | ~1.8 kbps | 185 ms |
| SF12 | Longest | ~0.3 kbps | 1.5 s |

Higher SF = longer range but slower and longer airtime. LoRaWAN networks use Adaptive Data Rate (ADR) to automatically select the optimal SF for each device's location.

### 4.2 LoRaWAN Network Architecture

```text
[LoRa End Device] --radio--> [LoRa Gateway] --IP--> [Network Server] --> [Application Server]
```

Gateways are not bridges — they are transparent radio receivers. A single gateway can receive transmissions from thousands of end devices simultaneously (different SF and frequencies). The network server handles deduplication when multiple gateways receive the same transmission.

### 4.3 Duty Cycle Constraints

Most regional LoRa regulations limit duty cycle to 1% per sub-band. A 1% duty cycle means:

```text
Max TX time per hour = 3600 seconds × 0.01 = 36 seconds
```

For an SF12 message with 1.5s time on air: maximum 24 messages per hour per sub-band. Plan LoRaWAN payloads for infrequent, compact messages. Use CBOR or custom binary encoding to minimize payload size.

---

## Section 5 — Cellular IoT

### 5.1 NB-IoT vs LTE-M Comparison

| Feature | NB-IoT | LTE-M |
|---------|--------|-------|
| Peak data rate | 250 kbps down / 20 kbps up | 1 Mbps down / 1 Mbps up |
| Latency | 1.5–10 seconds | 10–15 ms |
| Mobility | Stationary (no handover) | Full mobility with handover |
| Voice | No | Yes (VoLTE) |
| Power (eDRX) | 10 years on battery | 10 years on battery |
| Coverage | Better indoor penetration | Slightly less penetration |
| Cost | Lower | Slightly higher |
| Best for | Utility meters, parking | Wearables, vehicle tracking |

### 5.2 Power Save Mode (PSM) and eDRX

Both NB-IoT and LTE-M support two deep sleep mechanisms:

**PSM (Power Saving Mode):** Device negotiates a sleep period with the network (minutes to hours). During sleep, it is unreachable for downlink messages. After waking, it sends data and sleeps again.

**eDRX (Extended Discontinuous Reception):** Device wakes periodically (seconds to minutes) to check for downlink messages, then sleeps. Allows some bi-directional communication at low power.

For a device sending hourly readings with PSM enabled, average current consumption can be under 5 µA, comparable to LoRaWAN.

---

## Section 6 — Network Selection Framework

### 6.1 Decision Criteria

Apply these criteria in order when selecting a wireless technology:

1. **Range:** How far must data travel? Meter-range (BLE, Zigbee) vs building-range (Wi-Fi, Z-Wave) vs kilometer-range (LoRaWAN) vs anywhere (cellular)
2. **Data volume:** Kilobytes per hour (LoRaWAN) vs megabytes per hour (Wi-Fi, LTE-M) vs continuous streaming (Wi-Fi, LTE-M)
3. **Power budget:** Battery life in days (Wi-Fi deep sleep) vs months (BLE, Zigbee) vs years (LoRaWAN, NB-IoT)
4. **Existing infrastructure:** Is cellular coverage available? Is a LoRa gateway deployed? Is Wi-Fi available?
5. **Cost per node:** Module cost, carrier cost (cellular), network infrastructure cost
6. **Mobility:** Static (any technology) vs moving locally (Zigbee, BLE) vs moving globally (cellular)

### 6.2 Technology Comparison Summary

| Technology | Range | Power | Data Rate | Infrastructure | Cost |
|------------|-------|-------|-----------|---------------|------|
| Wi-Fi | 50m | High | High | Existing AP | Low |
| BLE | 50m | Very low | Medium | Phone/hub | Low |
| Zigbee | Mesh | Low | Low | Gateway | Low |
| Z-Wave | Mesh | Low | Low | Gateway | Medium |
| LoRaWAN | 15km | Extremely low | Very low | Gateway/network | Low |
| NB-IoT | Cellular | Very low | Low | Carrier | Medium+SIM |
| LTE-M | Cellular | Low | Medium | Carrier | Medium+SIM |

---

## Key Terms

| Term | Definition |
|------|------------|
| RSSI | Received Signal Strength Indicator — radio signal level in dBm |
| BLE | Bluetooth Low Energy — low-power Bluetooth for IoT and wearables |
| GATT | Generic Attribute Profile — BLE data hierarchy: service, characteristic, descriptor |
| Beacon | BLE device broadcasting advertisement packets without a connection |
| Zigbee | IEEE 802.15.4-based open mesh networking protocol |
| Z-Wave | Proprietary sub-GHz mesh protocol for home automation |
| LoRa | Long Range radio modulation using Chirp Spread Spectrum |
| LoRaWAN | Network protocol layer built on LoRa physical layer |
| Spreading Factor | LoRa parameter controlling range vs data rate trade-off |
| NB-IoT | Narrowband IoT — cellular standard for static, low-data devices |
| LTE-M | LTE Cat-M1 — cellular standard for mobile IoT devices |
| PSM | Power Saving Mode — cellular sleep mechanism for battery-powered IoT |
| ADR | Adaptive Data Rate — LoRaWAN automatic SF optimization |

---

## Review Questions

1. An ESP32 running on a 3000 mAh battery transmits one MQTT reading per minute over Wi-Fi using deep sleep between readings. The connection cycle takes 2 seconds at 150 mA and the deep sleep draws 10 µA for 58 seconds. Calculate the average current draw and estimate battery life in days.
2. Explain the difference between a BLE advertisement packet and a GATT characteristic notification. When is each used?
3. Why can a Zigbee network support up to 65,000 nodes while Z-Wave is limited to 232? What architectural feature enables Zigbee's larger node count?
4. A LoRaWAN sensor uses SF12 and sends a 20-byte payload. Time on air is 1.5 seconds. The duty cycle limit is 1%. What is the maximum number of messages this sensor can send per hour?
5. What is the key operational difference between NB-IoT and LTE-M that makes LTE-M suitable for vehicle tracking but NB-IoT unsuitable?
6. A farmer wants to monitor soil moisture in 50 fields across a 500-acre property. Each sensor sends a 10-byte reading once per hour. There is no cellular coverage on the property. Which wireless technology is most appropriate? Justify using at least three criteria.
7. What does an RSSI of -82 dBm indicate about Wi-Fi signal quality, and what practical steps can you take to improve it?
8. Explain why LoRaWAN gateways are described as "transparent" and what happens when two gateways receive the same transmission from the same end device.

---

## 9. Supplemental Resources

**1. The Things Network — LoRaWAN Documentation**
[https://www.thethingsnetwork.org/docs/](https://www.thethingsnetwork.org/docs/)
The Things Network's comprehensive LoRaWAN reference covering OTAA vs ABP activation, spreading factors, duty cycle limits, gateway architecture, and the Things Stack server. Includes hands-on quick-start guides for Arduino and MicroPython devices and a public community network for lab testing.

**2. Nordic Semiconductor — BLE Fundamentals (Bluetooth Low Energy)**
[https://academy.nordicsemi.com/courses/bluetooth-low-energy-fundamentals/](https://academy.nordicsemi.com/courses/bluetooth-low-energy-fundamentals/)
Free online course from Nordic Semiconductor covering the BLE stack in depth: GAP advertising, GATT hierarchy (services, characteristics, descriptors), security pairing modes, and power optimization strategies. Directly supports Section 2 of this reading guide on BLE GATT and advertising.

**3. Zigbee Alliance — Zigbee Specification Overview**
[https://zigbeealliance.org/solution/zigbee/](https://zigbeealliance.org/solution/zigbee/)
The Connectivity Standards Alliance (formerly Zigbee Alliance) overview of the Zigbee protocol stack, device types (Coordinator, Router, End Device), network topologies, and application profiles. Covers the AES-128 security model and the 65,000-node addressing space discussed in Section 3 of this guide.
