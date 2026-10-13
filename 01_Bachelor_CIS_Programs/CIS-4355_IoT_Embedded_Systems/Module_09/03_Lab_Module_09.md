# Lab: Module 09 — IoT Wireless Networking

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Points:** 100

---

## Lab Overview

In this lab you will configure the ESP32 for three wireless modes: Wi-Fi Station mode with deep sleep power management, BLE advertising as a beacon, and BLE GATT server exposing a temperature characteristic. You will measure and compare power consumption patterns between Wi-Fi and BLE operation.

**Estimated time:** 2.5–3.5 hours

**Hardware required:**

- ESP32 DevKit V1
- DHT22 sensor (from Module 08 lab)
- USB cable
- Smartphone with a BLE scanner app (nRF Connect for Android or iOS, or LightBlue)

**Software required:**

- Arduino IDE with ESP32 board support
- DHT sensor library by Adafruit
- nRF Connect or LightBlue on your smartphone

---

## Part A — Wi-Fi Station Mode and Connection Diagnostics (20 points)

### Part A Objective

Connect the ESP32 to Wi-Fi and display detailed connection diagnostics including IP address, gateway, DNS, and RSSI. Implement a network health check that runs every 30 seconds.

### Part A Code

```cpp
// Part A: Wi-Fi Station Mode with diagnostics
#include <WiFi.h>

const char* SSID = "YourNetworkName";
const char* PASS = "YourPassword";

void printNetworkInfo() {
  Serial.println(F("--- Network Info ---"));
  Serial.printf("  SSID       : %s\n",   WiFi.SSID().c_str());
  Serial.printf("  IP Address : %s\n",   WiFi.localIP().toString().c_str());
  Serial.printf("  Subnet     : %s\n",   WiFi.subnetMask().toString().c_str());
  Serial.printf("  Gateway    : %s\n",   WiFi.gatewayIP().toString().c_str());
  Serial.printf("  DNS        : %s\n",   WiFi.dnsIP().toString().c_str());
  Serial.printf("  MAC        : %s\n",   WiFi.macAddress().c_str());
  Serial.printf("  RSSI       : %d dBm\n", WiFi.RSSI());
  Serial.printf("  Channel    : %d\n",   WiFi.channel());
  Serial.println(F("--------------------"));
}

bool connectWiFi(uint8_t maxAttempts = 20) {
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASS);
  Serial.print("Connecting");
  for (uint8_t i = 0; i < maxAttempts && WiFi.status() != WL_CONNECTED; i++) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  return WiFi.status() == WL_CONNECTED;
}

void setup() {
  Serial.begin(115200);
  delay(500);

  if (connectWiFi()) {
    Serial.println(F("Connected!"));
    printNetworkInfo();
  } else {
    Serial.println(F("Connection failed."));
  }
}

void loop() {
  delay(30000);
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println(F("WiFi lost — reconnecting..."));
    connectWiFi();
  }
  Serial.printf("[Health] RSSI: %d dBm  Uptime: %lu s\n",
                WiFi.RSSI(), millis() / 1000);
}
```

### Part A Expected Output

```text
Connecting..........
Connected!
--- Network Info ---
  SSID       : YourNetworkName
  IP Address : 192.168.1.105
  Subnet     : 255.255.255.0
  Gateway    : 192.168.1.1
  DNS        : 192.168.1.1
  MAC        : AA:BB:CC:DD:EE:FF
  RSSI       : -52 dBm
  Channel    : 6
--------------------
[Health] RSSI: -52 dBm  Uptime: 30 s
[Health] RSSI: -53 dBm  Uptime: 60 s
```

### Part A Deliverables

- Screenshot of Serial Monitor showing full network info block
- Move your ESP32 progressively farther from the router and record the RSSI at three distances (close, mid-room, far). Record your measurements in a table and indicate which RSSI range each falls into from the reading guide.

---

## Part B — Wi-Fi with Deep Sleep Power Cycling (25 points)

### Part B Objective

Implement the deep sleep / wake / transmit pattern. The ESP32 wakes from deep sleep, connects to Wi-Fi, reads the DHT22, sends data as an HTTP POST to a public test endpoint, then enters deep sleep for 60 seconds.

### Part B Code

```cpp
// Part B: Deep sleep + Wi-Fi + HTTP POST
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

const char* SSID     = "YourNetworkName";
const char* PASS     = "YourPassword";
const char* POST_URL = "https://httpbin.org/post";  // Free echo endpoint

#define DHTPIN  4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// RTC memory persists across deep sleep
RTC_DATA_ATTR uint32_t bootCount = 0;

void setup() {
  Serial.begin(115200);
  dht.begin();
  bootCount++;

  Serial.printf("\n=== Boot #%lu ===\n", bootCount);

  // Read sensor
  float temp  = dht.readTemperature();
  float humid = dht.readHumidity();
  if (isnan(temp)) temp = -99.0f;
  if (isnan(humid)) humid = -99.0f;

  // Connect WiFi
  WiFi.begin(SSID, PASS);
  uint32_t wifiStart = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - wifiStart < 10000) {
    delay(200);
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.printf("WiFi OK (%lu ms)  RSSI: %d dBm\n",
                  millis() - wifiStart, WiFi.RSSI());

    // Build JSON payload
    char payload[128];
    snprintf(payload, sizeof(payload),
      "{\"boot\":%lu,\"temp\":%.2f,\"humid\":%.1f}",
      bootCount, temp, humid);

    // HTTP POST
    HTTPClient http;
    http.begin(POST_URL);
    http.addHeader("Content-Type", "application/json");
    int code = http.POST(payload);
    Serial.printf("POST response: %d\n", code);
    http.end();
    WiFi.disconnect(true);
  } else {
    Serial.println(F("WiFi failed — skipping POST"));
  }

  Serial.println(F("Entering deep sleep for 60 seconds..."));
  Serial.flush();
  esp_deep_sleep(60 * 1000000LL);
}

void loop() {
  // Never reached — deep sleep restarts in setup()
}
```

### Part B Expected Output

```text
=== Boot #1 ===
WiFi OK (1843 ms)  RSSI: -54 dBm
POST response: 200
Entering deep sleep for 60 seconds...

=== Boot #2 ===
WiFi OK (1721 ms)  RSSI: -53 dBm
POST response: 200
Entering deep sleep for 60 seconds...
```

### Part B Deliverables

- Screenshot of Serial Monitor showing at least 3 complete boot cycles
- Written analysis (3–4 sentences): How long does the Wi-Fi connection take each boot cycle? Calculate the approximate average current draw for this device assuming: Wi-Fi + HTTP active for 4 seconds at 150 mA, then deep sleep for 56 seconds at 10 µA. Is this device practical on a 2000 mAh battery? How long would it last?

---

## Part C — BLE Advertising Beacon (25 points)

### Part C Objective

Configure the ESP32 as a BLE beacon that advertises a device name and the Environmental Sensing service UUID. Observe it on a smartphone BLE scanner.

### Part C Code

```cpp
// Part C: BLE Advertising Beacon
#include <BLEDevice.h>
#include <BLEAdvertising.h>
#include <BLEUtils.h>

void setup() {
  Serial.begin(115200);

  // Initialize BLE with device name
  BLEDevice::init("TXWES-Beacon-01");

  BLEAdvertising* pAdv = BLEDevice::getAdvertising();

  // Advertise Environmental Sensing Service (UUID 0x181A)
  BLEUUID envSensingUUID((uint16_t)0x181A);
  pAdv->addServiceUUID(envSensingUUID);
  pAdv->setScanResponse(true);
  pAdv->setMinPreferred(0x06);  // Helps with iOS connectivity
  pAdv->setMinInterval(160);    // 160 × 0.625ms = 100ms interval
  pAdv->setMaxInterval(320);    // 320 × 0.625ms = 200ms interval

  BLEDevice::startAdvertising();

  Serial.println(F("BLE beacon advertising: TXWES-Beacon-01"));
  Serial.println(F("Service UUID: 0x181A (Environmental Sensing)"));
  Serial.println(F("Open nRF Connect on your phone to verify."));
}

void loop() {
  delay(5000);
  Serial.println(F("Still advertising..."));
}
```

### Part C Test Procedure

1. Upload and run the sketch
2. Open nRF Connect (or LightBlue) on your smartphone
3. Tap Scan
4. Look for "TXWES-Beacon-01" in the device list
5. Tap the device to see its advertisement details
6. Verify the 0x181A service UUID appears in the advertisement data

### Part C Deliverables

- Screenshot from nRF Connect or LightBlue showing the ESP32 device "TXWES-Beacon-01" in the scan list with its RSSI
- Screenshot of the advertisement details showing the 0x181A service UUID
- Screenshot of ESP32 Serial Monitor showing "Still advertising..." messages

---

## Part D — BLE GATT Server with Temperature Characteristic (30 points)

### Part D Objective

Implement a full BLE GATT server that exposes a temperature characteristic from the DHT22. A smartphone app should be able to read and subscribe to live temperature updates.

### Part D Code

```cpp
// Part D: BLE GATT Server — Temperature characteristic
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <DHT.h>

DHT dht(4, DHT22);

#define ENV_SERVICE_UUID   "0000181a-0000-1000-8000-00805f9b34fb"
#define TEMP_CHAR_UUID     "00002a6e-0000-1000-8000-00805f9b34fb"
#define HUMID_CHAR_UUID    "00002a6f-0000-1000-8000-00805f9b34fb"

BLECharacteristic* pTempChar;
BLECharacteristic* pHumidChar;
bool deviceConnected = false;

class ServerCallbacks : public BLEServerCallbacks {
  void onConnect(BLEServer* pServer) {
    deviceConnected = true;
    Serial.println(F("Central connected"));
  }
  void onDisconnect(BLEServer* pServer) {
    deviceConnected = false;
    Serial.println(F("Central disconnected — restarting advertising"));
    BLEDevice::startAdvertising();
  }
};

void setup() {
  Serial.begin(115200);
  dht.begin();

  BLEDevice::init("TXWES-TempSensor");
  BLEServer* pServer = BLEDevice::createServer();
  pServer->setCallbacks(new ServerCallbacks());

  BLEService* pService = pServer->createService(ENV_SERVICE_UUID);

  // Temperature characteristic — read + notify, signed int16, 0.01°C
  pTempChar = pService->createCharacteristic(
    TEMP_CHAR_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
  );
  pTempChar->addDescriptor(new BLE2902());

  // Humidity characteristic — read + notify, uint16, 0.01%
  pHumidChar = pService->createCharacteristic(
    HUMID_CHAR_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
  );
  pHumidChar->addDescriptor(new BLE2902());

  pService->start();
  BLEDevice::getAdvertising()->start();
  Serial.println(F("GATT server running. Connect with nRF Connect."));
}

void loop() {
  float temp  = dht.readTemperature();
  float humid = dht.readHumidity();

  if (!isnan(temp) && !isnan(humid)) {
    int16_t  tempRaw  = (int16_t)(temp  * 100);
    uint16_t humidRaw = (uint16_t)(humid * 100);

    pTempChar->setValue((uint8_t*)&tempRaw,  sizeof(tempRaw));
    pHumidChar->setValue((uint8_t*)&humidRaw, sizeof(humidRaw));

    if (deviceConnected) {
      pTempChar->notify();
      pHumidChar->notify();
    }

    Serial.printf("T: %.2f C  H: %.1f %%  Connected: %s\n",
                  temp, humid, deviceConnected ? "YES" : "NO");
  }
  delay(3000);
}
```

### Part D Test Procedure

1. Upload and run the sketch
2. Open nRF Connect on your smartphone
3. Tap Scan and connect to "TXWES-TempSensor"
4. Navigate to the Environmental Sensing service (UUID 181A)
5. Enable notifications on the Temperature characteristic (UUID 2A6E) by tapping the bell icon
6. Enable notifications on the Humidity characteristic (UUID 2A6F)
7. Observe live values updating every 3 seconds

### Part D Deliverables

- Screenshot of nRF Connect showing the device connected and service visible
- Screenshot of the Temperature characteristic showing a notification value (the raw int16 bytes)
- Screenshot of ESP32 Serial Monitor showing temperature/humidity readings with "Connected: YES"
- Written answer (2–3 sentences): The temperature raw value in nRF Connect appears as a hex byte sequence, not a decimal number. For example, 23.45°C would be stored as 2345 decimal = 0x0929. How would a phone app convert this raw bytes back to a human-readable temperature value?

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| **Part A** — Network info displays all 7 fields | 10 |
| **Part A** — RSSI measured at 3 distances with table | 10 |
| **Part B** — Deep sleep restart cycle working (3+ boots shown) | 10 |
| **Part B** — HTTP POST returns 200 | 5 |
| **Part B** — Written power consumption calculation | 10 |
| **Part C** — BLE beacon visible in nRF Connect screenshot | 10 |
| **Part C** — Service UUID 0x181A visible in advertisement | 5 |
| **Part C** — Serial Monitor screenshot | 5 |
| **Part D** — GATT server connects and sends notifications | 10 |
| **Part D** — nRF Connect screenshot with characteristic values | 10 |
| **Part D** — Written bytes-to-temperature explanation | 5 |
| **Code quality** — comments, readable variable names | 10 |
| **TOTAL** | **100** |

---

## Troubleshooting Tips

**Wi-Fi never connects:** Confirm SSID and password are exact (case-sensitive). Verify the network is 2.4 GHz — ESP32 does not support 5 GHz Wi-Fi. Check RSSI; if below -80 dBm, move closer to the router.

**Deep sleep does not wake:** On some DevKit boards, GPIO 0 is pulled low during flashing and may interfere with deep sleep. Hold down the BOOT button if the board won't come out of deep sleep after programming.

**BLE not visible on phone:** Ensure Bluetooth is enabled on the phone and the app has Location permission (required by Android for BLE scanning). Restart the app if the device does not appear within 30 seconds.

**GATT characteristics read 0x0000:** The DHT22 may not be initialized correctly or may return NaN. Verify the DHT22 is wired correctly from Module 08 and that `dht.begin()` is called before the first read.

**nRF Connect shows raw bytes:** This is correct behavior — GATT characteristics return binary data. The app displays it as hex. Your written deliverable in Part D explains the conversion.

---

## Part 9 — Challenge Exercise

### Challenge 1: LoRaWAN Simulation with TTN and a Single-Channel Packet Forwarder

Simulate a LoRaWAN uplink path using a software packet forwarder and The Things Network (TTN) free tier.

1. Create a free account on [The Things Network console](https://console.thethingsnetwork.org/) and register a new application. Within the application, register a new end device with device type "Other" and manually specify a DevEUI, AppEUI, and AppKey (generate random values using the TTN console's key generator). Set activation mode to OTAA.

2. On your laptop, install the `ttn-lw-cli` tool or use the TTN HTTP integration. Write a Python script that simulates an OTAA join by sending a crafted uplink payload to the TTN application via the MQTT integration. Use the TTN-provided MQTT broker (`eu1.cloud.thethings.network`, port 8883 with TLS). Subscribe to `v3/{app_id}@{tenant_id}/devices/{device_id}/up` and confirm you can receive the simulated uplink JSON.

3. Add a downlink scheduler: publish a JSON downlink message to `v3/{app_id}@{tenant_id}/devices/{device_id}/down/push` that contains a 2-byte payload representing a target temperature setpoint (e.g., `0x1A 0x00` = 26°C). Print the received downlink in your subscriber terminal.

4. Write a 3–4 sentence analysis comparing the security of this simulated OTAA flow (MQTT over TLS to TTN) with the plaintext MQTT broker used in Module 07. Specifically address what additional protection OTAA and TLS provide over ABP and plain MQTT.

### Challenge 2: BLE Beacon Proximity Alert on Raspberry Pi

Use a Raspberry Pi (or laptop with a Bluetooth adapter) as a BLE scanner to detect the ESP32 beacon from Part C and trigger an action when RSSI exceeds a threshold.

1. On the Raspberry Pi (or laptop with BlueZ), install `bluepy` or `bleak` Python library (`pip install bleak`). Write a Python scanner that continuously scans for BLE advertisements and filters for your ESP32 beacon by its advertised name (`ESP32-Lab09`) or service UUID (`0x181A`):

```python
import asyncio
from bleak import BleakScanner

TARGET_NAME = "ESP32-Lab09"
RSSI_THRESHOLD = -65  # dBm — "near" threshold

async def scan():
    while True:
        devices = await BleakScanner.discover(timeout=2.0)
        for d in devices:
            if d.name and TARGET_NAME in d.name:
                status = "NEAR" if d.rssi >= RSSI_THRESHOLD else "FAR"
                print(f"[{status}] {d.name}: {d.rssi} dBm")
        await asyncio.sleep(1)

asyncio.run(scan())
```

2. Extend the script to log each detection event to a CSV file with columns `timestamp`, `rssi`, `status`. Move the ESP32 closer and farther from the scanner and verify that the `NEAR`/`FAR` status transitions at approximately the -65 dBm threshold.

3. Add a simple action trigger: when the device transitions from `FAR` to `NEAR`, print `"ALERT: ESP32 beacon entered proximity"` to the terminal (or send an MQTT message to `lab09/beacon/proximity` with payload `"entered"`). When it transitions from `NEAR` to `FAR`, send `"exited"`. Track state to avoid repeated alerts on every scan cycle.

4. In 2–3 sentences, explain why RSSI-based proximity detection is imprecise and describe two physical factors that can cause the measured RSSI to vary by 10–15 dBm even when the device is at a constant distance.

### Reflection Questions

1. In Part B you used Wi-Fi deep sleep with a full reconnect cycle on each wake. The reconnect takes approximately 500–2000 ms for DHCP and TCP handshake. Describe how you could reduce this reconnect latency using static IP configuration and stored credentials, and estimate the battery life improvement in percentage terms given a 2-second versus 0.5-second active window.

2. The ESP32 BLE GATT server in Part D used the NOTIFY property for the temperature characteristic. If instead you had used INDICATE, what change would occur in the ESP32 firmware behavior when `pCharacteristic->indicate()` is called, and how would this affect throughput for a sensor sending data at 10 Hz?
