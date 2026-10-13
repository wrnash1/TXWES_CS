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

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Device Staged Rollout Simulation

Extend the fleet server to manage ten simulated devices through a canary → pilot → general availability rollout, with automatic halt logic if the canary error rate exceeds the defined threshold.

1. Register ten devices (`device-001` through `device-010`) in the fleet server. Inject a simulated firmware version discrepancy: devices `device-001` through `device-008` report `firmware_version: "v1.0.0"` and devices `device-009` and `device-010` report `firmware_version: "v1.1.0"` (already updated). Write a helper function `query_fleet(firmware_version)` that returns a list of device IDs from the registry JSON files whose `firmware_version` matches the given string.

1. Implement a staged rollout controller in Python. The canary stage targets `device-001` only. After a 10-second simulated monitoring window, check whether `device-001`'s shadow `reported.firmware_version` matches `v1.1.0`. If so, advance to pilot (add `device-002` through `device-004`). After another 10-second window, verify all three pilot devices report `v1.1.0` and advance to GA (remaining devices). If any stage fails, set a `rollout_halted` flag and log the reason.

   ```python
   STAGES = [
       {"name": "canary", "devices": ["device-001"],                          "window_s": 10},
       {"name": "pilot",  "devices": ["device-002","device-003","device-004"], "window_s": 10},
       {"name": "ga",     "devices": [f"device-{i:03d}" for i in range(5,9)], "window_s": 5},
   ]

   def run_rollout(client, target_version):
       for stage in STAGES:
           print(f"[Rollout] Starting {stage['name']} stage — {len(stage['devices'])} device(s)")
           for dev in stage["devices"]:
               shadow = load_shadow(dev)
               shadow["desired"]["firmware_target"] = target_version
               shadow = save_shadow(dev, shadow)
               delta_topic = f"devices/{dev}/shadow/delta"
               client.publish(delta_topic, json.dumps(shadow["delta"]))
           time.sleep(stage["window_s"])
           confirmed = [
               d for d in stage["devices"]
               if load_shadow(d)["reported"].get("firmware_version") == target_version
           ]
           if len(confirmed) < len(stage["devices"]):
               failed = set(stage["devices"]) - set(confirmed)
               print(f"[Rollout] HALTED at {stage['name']} — {failed} did not confirm update")
               return False
           print(f"[Rollout] {stage['name']} passed — advancing")
       print(f"[Rollout] Complete — all devices on {target_version}")
       return True
   ```

1. Simulate a canary failure: modify `device-001`'s shadow file so its `reported.firmware_version` remains `"v1.0.0"` after the canary window (do not update it). Verify that `run_rollout()` prints the HALTED message and returns `False` without publishing the delta to pilot or GA devices. Then restore `device-001`'s reported version and verify the full rollout completes successfully.

1. In your lab report, write a 3–4 sentence analysis answering: what additional real-world metric (beyond firmware version confirmation) would you add as a canary halt condition, and what specific threshold value would you set? Justify your threshold using the alert calibration methodology described in the reading guide.

---

### Challenge 2: Automated Decommissioning Pipeline

Implement a decommission script that executes all four required decommissioning steps for a device and produces a tamper-evident audit log of each action.

1. Write a Python function `decommission_device(device_id)` that performs the four decommissioning steps in sequence. Each step must write an entry to a local `decommission_audit.log` file with a UTC ISO-8601 timestamp, the device ID, the step name, and a status of `"completed"` or `"failed"`. Step 1 marks the registry entry `status` field as `"revoked"` and adds a `revoked_at` timestamp. Step 2 renames the shadow file to `<device_id>.shadow.archived` (preserving data while removing it from the active shadows directory). Step 3 writes a data disposition record stating whether data was retained or deleted and the applicable retention reason. Step 4 overwrites the registry file with a minimal tombstone record containing only `device_id`, `status: "decommissioned"`, `decommissioned_at`, and `data_disposition`.

   ```python
   import hashlib

   def decommission_device(device_id, retain_data=True, retention_reason="compliance-7yr"):
       audit = []
       def log_step(step, status, detail=""):
           entry = {
               "ts": datetime.utcnow().isoformat() + "Z",
               "device_id": device_id,
               "step": step,
               "status": status,
               "detail": detail,
           }
           audit.append(entry)
           print(f"[Decommission] {step}: {status} — {detail}")

       # Step 1 — Certificate revocation (simulated: mark registry status)
       reg_path = f"{REGISTRY_DIR}/{device_id}.json"
       try:
           with open(reg_path) as f:
               record = json.load(f)
           record["status"]    = "revoked"
           record["revoked_at"] = datetime.utcnow().isoformat() + "Z"
           with open(reg_path, "w") as f:
               json.dump(record, f, indent=2)
           log_step("certificate_revocation", "completed", "status=revoked")
       except Exception as e:
           log_step("certificate_revocation", "failed", str(e))

       # Step 2 — Registry/shadow archival
       shadow_src  = f"{SHADOWS_DIR}/{device_id}.json"
       shadow_arch = f"{SHADOWS_DIR}/{device_id}.shadow.archived"
       try:
           os.rename(shadow_src, shadow_arch)
           log_step("registry_deletion", "completed", f"shadow archived to {shadow_arch}")
       except Exception as e:
           log_step("registry_deletion", "failed", str(e))

       # Step 3 — Data disposition record
       disposition = "retained" if retain_data else "deleted"
       log_step("data_handling", "completed",
                f"disposition={disposition} reason={retention_reason}")

       # Step 4 — Physical security (simulated: write tombstone + checksum)
       tombstone = {
           "device_id":        device_id,
           "status":           "decommissioned",
           "decommissioned_at": datetime.utcnow().isoformat() + "Z",
           "data_disposition": disposition,
       }
       tombstone_str  = json.dumps(tombstone, sort_keys=True)
       tombstone["sha256"] = hashlib.sha256(tombstone_str.encode()).hexdigest()
       with open(reg_path, "w") as f:
           json.dump(tombstone, f, indent=2)
       log_step("physical_security", "completed", f"tombstone written sha256={tombstone['sha256'][:16]}...")

       # Write audit log
       with open("decommission_audit.log", "a") as f:
           for entry in audit:
               f.write(json.dumps(entry) + "\n")
       return audit
   ```

1. Run `decommission_device("device-001")`. Inspect `decommission_audit.log` and the contents of the registry file. Verify: (a) the registry tombstone contains a `sha256` field, (b) the shadow file no longer exists at its original path, and (c) all four step entries appear in the audit log with `status: "completed"`.

1. Simulate a failure: delete the shadow file for `device-002` before calling `decommission_device("device-002")`. Verify that the audit log records `"status": "failed"` for the `registry_deletion` step while the other three steps still complete. Write a 2–3 sentence explanation of why partial completion is preferable to aborting on first error in a decommissioning workflow.

---

### Reflection Questions

1. In Challenge 1, the rollout controller checks `reported.firmware_version` by reading the local JSON shadow file rather than subscribing to an MQTT confirmation topic. Explain one advantage and one disadvantage of the file-based polling approach compared to an MQTT subscription approach for determining rollout gate status. In a production fleet of 50,000 devices, which approach scales better, and why?

2. In Challenge 2, Step 4 writes a SHA-256 checksum of the tombstone record into the tombstone itself. Explain what tamper-evidence property this provides and what it does not provide. Specifically: if an attacker with write access to the registry directory modifies the tombstone, how would the tamper be detected, and what additional mechanism would be required to make the audit log itself tamper-evident against an attacker with write access to the log file?
