# Lab Activity: Module 15 — IoT Project Deployment and Management

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Time:** 90–120 minutes

---

## Objective

Simulate a production IoT fleet management workflow using a local Mosquitto MQTT broker and a Python-based fleet management server. You will: register devices in a simulated registry, implement device shadow (twin) synchronization on an ESP32, simulate an OTA update job, and implement health telemetry monitoring with threshold-based alerting.

---

## Prerequisites

- ESP32 development board
- Python 3.10+ with packages: `paho-mqtt`, `flask`, `influxdb-client` (or `json` for a simplified local version)
- Mosquitto broker from the Module 12 lab (with TLS certificates already generated)
- Arduino IDE with ESP32 board support
- `jq` command-line JSON processor: `sudo apt install jq` on Ubuntu

---

## Part 1 — Device Registry and Shadow Server

We will build a minimal Python fleet management server that stores device state in JSON files and synchronizes it to devices via MQTT.

### Step 1.1 — Create the server directory structure

```bash
mkdir -p ~/iot-fleet-lab/{registry,shadows,firmware}
cd ~/iot-fleet-lab
```

### Step 1.2 — Fleet management server

```python
# file: ~/iot-fleet-lab/fleet_server.py
import json
import os
import time
import paho.mqtt.client as mqtt
from datetime import datetime

BROKER   = "localhost"
PORT     = 8883
CA_CERT  = os.path.expanduser("~/iot-security-lab/certs/ca.crt")
CLI_CERT = os.path.expanduser("~/iot-security-lab/certs/device-001.crt")
CLI_KEY  = os.path.expanduser("~/iot-security-lab/certs/device-001.key")

REGISTRY_DIR = os.path.expanduser("~/iot-fleet-lab/registry")
SHADOWS_DIR  = os.path.expanduser("~/iot-fleet-lab/shadows")

def load_shadow(device_id):
    path = f"{SHADOWS_DIR}/{device_id}.json"
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"desired": {}, "reported": {}, "delta": {}}

def save_shadow(device_id, shadow):
    path = f"{SHADOWS_DIR}/{device_id}.json"
    shadow["delta"] = {
        k: v for k, v in shadow["desired"].items()
        if shadow["reported"].get(k) != v
    }
    with open(path, "w") as f:
        json.dump(shadow, f, indent=2)
    return shadow

def register_device(device_id, firmware_version="v1.0.0"):
    path = f"{REGISTRY_DIR}/{device_id}.json"
    record = {
        "device_id": device_id,
        "registered_at": datetime.utcnow().isoformat(),
        "firmware_version": firmware_version,
        "status": "active",
        "last_seen": None
    }
    with open(path, "w") as f:
        json.dump(record, f, indent=2)
    # Initialize shadow
    shadow = {
        "desired": {"firmware_target": firmware_version, "reporting_interval_s": 30},
        "reported": {},
        "delta": {}
    }
    save_shadow(device_id, shadow)
    print(f"[Registry] Registered {device_id}")
    return record

def on_message(client, userdata, msg):
    topic   = msg.topic
    payload = json.loads(msg.payload.decode())

    # Handle reported state updates from device
    if "/shadow/reported" in topic:
        device_id = topic.split("/")[1]
        shadow    = load_shadow(device_id)
        shadow["reported"].update(payload)
        shadow = save_shadow(device_id, shadow)

        # Update registry last_seen
        reg_path = f"{REGISTRY_DIR}/{device_id}.json"
        if os.path.exists(reg_path):
            with open(reg_path) as f:
                record = json.load(f)
            record["last_seen"] = datetime.utcnow().isoformat()
            record["firmware_version"] = payload.get(
                "firmware_version", record["firmware_version"])
            with open(reg_path, "w") as f:
                json.dump(record, f, indent=2)

        # Push delta back to device if desired != reported
        if shadow["delta"]:
            delta_topic = f"devices/{device_id}/shadow/delta"
            client.publish(delta_topic, json.dumps(shadow["delta"]))
            print(f"[Shadow] Pushed delta to {device_id}: {shadow['delta']}")
        else:
            print(f"[Shadow] {device_id} fully synchronized")

    # Handle health telemetry
    elif "/telemetry" in topic:
        device_id = topic.split("/")[1]
        check_health_alerts(device_id, payload)

def check_health_alerts(device_id, telemetry):
    free_heap   = telemetry.get("free_heap_bytes", 999999)
    reconnects  = telemetry.get("reconnect_count", 0)
    uptime      = telemetry.get("uptime_s", 0)

    if free_heap < 50000:
        print(f"[ALERT] {device_id}: Low heap memory — {free_heap} bytes free")
    if reconnects > 3:
        print(f"[ALERT] {device_id}: High reconnect count — {reconnects} in last hour")

# Setup MQTT client
client = mqtt.Client(client_id="fleet-server")
client.tls_set(ca_certs=CA_CERT, certfile=CLI_CERT, keyfile=CLI_KEY)
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("devices/+/shadow/reported")
client.subscribe("devices/+/telemetry")

# Register a test device
os.makedirs(REGISTRY_DIR, exist_ok=True)
os.makedirs(SHADOWS_DIR,  exist_ok=True)
register_device("device-001", "v1.0.0")

print("[Fleet Server] Listening for device updates...")
client.loop_forever()
```

Run the server in a terminal: `python3 ~/iot-fleet-lab/fleet_server.py`

---

## Part 2 — ESP32 Device Shadow Client

```cpp
// Module 15 Lab — Device Shadow Synchronization
// Flash to ESP32

#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <esp_ota_ops.h>

// --- Configuration ---
const char* WIFI_SSID     = "YOUR_SSID";
const char* WIFI_PASSWORD = "YOUR_PASSWORD";
const char* MQTT_BROKER   = "YOUR_SERVER_IP";
const int   MQTT_PORT     = 8883;
const char* DEVICE_ID     = "device-001";
const char* FW_VERSION    = "v1.0.0";

// Paste CA and device cert/key PEM strings here (from Module 12 lab)
const char* CA_CERT  = R"(-----BEGIN CERTIFICATE-----
...paste ca.crt content...
-----END CERTIFICATE-----)";
const char* DEV_CERT = R"(-----BEGIN CERTIFICATE-----
...paste device-001.crt content...
-----END CERTIFICATE-----)";
const char* DEV_KEY  = R"(-----BEGIN EC PRIVATE KEY-----
...paste device-001.key content...
-----END EC PRIVATE KEY-----)";

WiFiClientSecure wifiClient;
PubSubClient     mqttClient(wifiClient);

// Shadow state
int  reportingIntervalS = 60;   // default — will be overridden by shadow delta
int  reconnectCount     = 0;

void publishReported() {
    char topic[64];
    snprintf(topic, sizeof(topic), "devices/%s/shadow/reported", DEVICE_ID);

    StaticJsonDocument<256> doc;
    doc["firmware_version"]    = FW_VERSION;
    doc["reporting_interval_s"] = reportingIntervalS;
    doc["uptime_s"]            = (uint32_t)(esp_timer_get_time() / 1000000);
    doc["free_heap_bytes"]     = (int)esp_get_free_heap_size();

    char buf[256];
    serializeJson(doc, buf, sizeof(buf));
    mqttClient.publish(topic, buf);
    Serial.printf("[Shadow] Published reported state: %s\n", buf);
}

void publishTelemetry() {
    char topic[64];
    snprintf(topic, sizeof(topic), "devices/%s/telemetry", DEVICE_ID);

    StaticJsonDocument<128> doc;
    doc["uptime_s"]        = (uint32_t)(esp_timer_get_time() / 1000000);
    doc["free_heap_bytes"] = (int)esp_get_free_heap_size();
    doc["reconnect_count"] = reconnectCount;

    char buf[128];
    serializeJson(doc, buf, sizeof(buf));
    mqttClient.publish(topic, buf);
}

void onMqttMessage(char* topic, byte* payload, unsigned int length) {
    String payloadStr((char*)payload, length);
    Serial.printf("[MQTT] Received on %s: %s\n", topic, payloadStr.c_str());

    // Handle shadow delta
    if (String(topic).endsWith("/shadow/delta")) {
        StaticJsonDocument<256> delta;
        if (deserializeJson(delta, payloadStr) == DeserializationError::Ok) {
            if (delta.containsKey("reporting_interval_s")) {
                reportingIntervalS = delta["reporting_interval_s"];
                Serial.printf("[Shadow] Applied reporting_interval_s = %d\n",
                              reportingIntervalS);
            }
            // Confirm the change by publishing updated reported state
            publishReported();
        }
    }
}

void connectMQTT() {
    wifiClient.setCACert(CA_CERT);
    wifiClient.setCertificate(DEV_CERT);
    wifiClient.setPrivateKey(DEV_KEY);
    mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
    mqttClient.setCallback(onMqttMessage);

    while (!mqttClient.connected()) {
        Serial.print("[MQTT] Connecting...");
        if (mqttClient.connect(DEVICE_ID)) {
            Serial.println("connected");
            char deltaT[64];
            snprintf(deltaT, sizeof(deltaT), "devices/%s/shadow/delta", DEVICE_ID);
            mqttClient.subscribe(deltaT);
            publishReported();
        } else {
            reconnectCount++;
            Serial.printf("failed (rc=%d). Retry in 5s\n", mqttClient.state());
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\n[WiFi] Connected");
    connectMQTT();
}

void loop() {
    if (!mqttClient.connected()) {
        connectMQTT();
    }
    mqttClient.loop();

    static unsigned long lastReport = 0;
    if (millis() - lastReport > (unsigned long)reportingIntervalS * 1000UL) {
        publishReported();
        publishTelemetry();
        lastReport = millis();
    }
}
```

---

## Part 3 — Push a Shadow Update and Observe Synchronization

### Step 3.1 — Publish a desired state change from the server side

With the fleet server running and the ESP32 connected, push a desired state change using the MQTT CLI:

```bash
mosquitto_pub \
  --host localhost --port 8883 \
  --cafile ~/iot-security-lab/certs/ca.crt \
  --cert ~/iot-security-lab/certs/device-001.crt \
  --key ~/iot-security-lab/certs/device-001.key \
  --topic "devices/device-001/shadow/desired" \
  --message '{"reporting_interval_s": 10}'
```

The fleet server receives this, updates the shadow, computes the delta (desired 10 vs. reported 30), and pushes the delta to the device.

### Step 3.2 — Observe ESP32 serial output

The ESP32 should print:

```text
[MQTT] Received on devices/device-001/shadow/delta: {"reporting_interval_s":10}
[Shadow] Applied reporting_interval_s = 10
[Shadow] Published reported state: {"firmware_version":"v1.0.0","reporting_interval_s":10,...}
```

Then observe that the device begins reporting every 10 seconds instead of 30. The fleet server prints: `[Shadow] device-001 fully synchronized`.

---

## Part 4 — Simulate an OTA Job and Staged Rollout

### Step 4.1 — Create a simulated firmware v1.1.0 marker

```bash
echo '{"version":"v1.1.0","changes":"Bug fix: reduced reconnect loop"}' \
  > ~/iot-fleet-lab/firmware/v1.1.0_manifest.json
```

### Step 4.2 — Push the OTA desired state

```bash
mosquitto_pub \
  --host localhost --port 8883 \
  --cafile ~/iot-security-lab/certs/ca.crt \
  --cert ~/iot-security-lab/certs/device-001.crt \
  --key ~/iot-security-lab/certs/device-001.key \
  --topic "devices/device-001/shadow/desired" \
  --message '{"firmware_target":"v1.1.0"}'
```

The fleet server computes the delta (desired `v1.1.0` vs. reported `v1.0.0`) and pushes it to the device. The ESP32 logs the delta receipt. In a real deployment, the device would download the firmware from the repository URL in the delta. For this simulation, modify the `FW_VERSION` constant to `v1.1.0` and reflash to simulate the update completing.

### Step 4.3 — Document the canary gate decision

In your lab report, answer: based on the simulated OTA workflow, what two metrics would you monitor during the 24-hour canary stage before expanding to the full fleet? Explain the specific threshold values you would set and why.

---

## Troubleshooting Guide

- **Fleet server: Connection refused** — Ensure Mosquitto is running (`ps aux | grep mosquitto`) and the TLS configuration uses absolute paths from your Module 12 lab.
- **ESP32: MQTT connect failed (rc=-2)** — The broker hostname or port is incorrect. Verify `MQTT_BROKER` is the IP address (not hostname) of your development machine.
- **Shadow delta not received by ESP32** — Confirm the ESP32 subscribed to the correct delta topic (`devices/device-001/shadow/delta`). Check the fleet server output for "[Shadow] Pushed delta" confirmation.
- **Python: json.JSONDecodeError on message** — The MQTT payload may be empty or malformed. Add `if not msg.payload: return` at the top of `on_message`.

---

## Deliverables

Submit the following to the Canvas LMS assignment portal:

1. Screenshot of the fleet server terminal showing: device registration, initial shadow push, and the "fully synchronized" confirmation after the ESP32 applies the reporting interval change.
2. Screenshot of the ESP32 serial monitor showing the shadow delta received and applied, and the new reporting interval in effect.
3. The contents of the device registry JSON file (`~/iot-fleet-lab/registry/device-001.json`) after the synchronization, showing the `last_seen` timestamp.
4. Written answers (150–200 words): Answer the canary gate monitoring question from Step 4.3. Include specific metric names, threshold values, and justify why each threshold was chosen.
5. Written answer (75–100 words): In the A/B partition OTA scheme, what prevents the device from permanently booting a defective firmware image that crashes on startup? Trace the exact sequence of bootloader decisions that causes automatic rollback.

---
