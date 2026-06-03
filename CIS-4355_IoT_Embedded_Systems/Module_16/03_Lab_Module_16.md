# Lab Activity: Module 16 — IoT Capstone Project

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Time:** 180–240 minutes (capstone project — work across multiple sessions)

---

## Objective

Assemble a complete, working four-tier IoT system by integrating the components built across Modules 12 through 15. The system must demonstrate: a secured device communicating over mTLS-authenticated MQTT, a cloud processing layer storing telemetry, at least one alert condition, and a dashboard visualization. You will then produce professional documentation for the system.

---

## Prerequisites

All previous lab deliverables completed:

- Module 12: CA and device certificates generated, Mosquitto TLS broker configured
- Module 13: FreeRTOS multi-task sketch working with queue and watchdog
- Module 14: TFLM inference running on ESP32 (or Python quantization lab complete)
- Module 15: Fleet management server and device shadow client working

---

## Part 1 — Integrate the Complete Device Firmware

### Step 1.1 — Create the capstone project

Create a new Arduino sketch `iot_capstone_m16` that combines the FreeRTOS task structure from Module 13 with the TLS MQTT client from Module 12 and the shadow client from Module 15.

The final task structure:

```cpp
// Priority 3 — Sensor Task: reads sensor every 30s, pushes to queue
void vSensorTask(void *pv);

// Priority 2 — MQTT Publish Task: dequeues readings, publishes telemetry
//              and checks for OTA/shadow delta on reconnect
void vMqttTask(void *pv);

// Priority 2 — Anomaly Task: maintains sliding window,
//              publishes anomaly event if z-score > 3.0
void vAnomalyTask(void *pv);

// Priority 1 — Shadow Task: subscribes to delta topic,
//              applies configuration changes
void vShadowTask(void *pv);
```

### Step 1.2 — MQTT topic hierarchy

Define topic constants that all tasks share:

```cpp
const char* TOPIC_TELEMETRY = "devices/device-001/telemetry";
const char* TOPIC_REPORTED  = "devices/device-001/shadow/reported";
const char* TOPIC_DELTA     = "devices/device-001/shadow/delta";
const char* TOPIC_ANOMALY   = "devices/device-001/anomaly";
```

### Step 1.3 — Telemetry message format

Each telemetry message must be a JSON object with these required fields:

```json
{
  "device_id": "device-001",
  "firmware_version": "v1.0.0",
  "timestamp_ms": 1717200000000,
  "temperature_c": 22.5,
  "humidity_pct": 45.2,
  "free_heap_bytes": 189432,
  "uptime_s": 3600,
  "reconnect_count": 0
}
```

### Step 1.4 — Anomaly detection

Implement a simple sliding-window z-score anomaly detector in `vAnomalyTask`:

```cpp
#define WINDOW_SIZE 10
float window[WINDOW_SIZE] = {0};
int   windowIdx = 0;
bool  windowFull = false;

void updateWindow(float value) {
    window[windowIdx] = value;
    windowIdx = (windowIdx + 1) % WINDOW_SIZE;
    if (windowIdx == 0) windowFull = true;
}

float computeMean() {
    int n = windowFull ? WINDOW_SIZE : windowIdx;
    if (n == 0) return 0.0f;
    float sum = 0;
    for (int i = 0; i < n; i++) sum += window[i];
    return sum / n;
}

float computeStdDev(float mean) {
    int n = windowFull ? WINDOW_SIZE : windowIdx;
    if (n < 2) return 1.0f;
    float sq = 0;
    for (int i = 0; i < n; i++) sq += (window[i]-mean)*(window[i]-mean);
    return sqrtf(sq / (n - 1));
}

float zScore(float value) {
    float mean = computeMean();
    float std  = computeStdDev(mean);
    return (std > 0) ? fabsf(value - mean) / std : 0.0f;
}
```

When `zScore(current_reading) > 3.0`, publish to `TOPIC_ANOMALY`:

```json
{"device_id":"device-001","timestamp_ms":1717200000000,
 "value":31.2,"z_score":3.45,"window_mean":22.5}
```

### Step 1.5 — Watchdog registration

Register all four tasks with the TWDT:

```cpp
// In each task's entry point, immediately after it starts:
esp_task_wdt_add(NULL);
// ... in the task loop:
esp_task_wdt_reset();
```

---

## Part 2 — Cloud Processing Layer

### Step 2.1 — Extend the fleet server from Module 15

Add telemetry storage to the fleet server:

```python
# Append to fleet_server.py — telemetry storage function
import csv

TELEMETRY_FILE = os.path.expanduser("~/iot-fleet-lab/telemetry.csv")

def store_telemetry(device_id, payload):
    """Append a telemetry record to the CSV store."""
    fieldnames = ["timestamp", "device_id", "temperature_c",
                  "humidity_pct", "free_heap_bytes", "uptime_s"]
    row = {
        "timestamp":      datetime.utcnow().isoformat(),
        "device_id":      device_id,
        "temperature_c":  payload.get("temperature_c", ""),
        "humidity_pct":   payload.get("humidity_pct", ""),
        "free_heap_bytes": payload.get("free_heap_bytes", ""),
        "uptime_s":       payload.get("uptime_s", "")
    }
    file_exists = os.path.exists(TELEMETRY_FILE)
    with open(TELEMETRY_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def check_telemetry_alerts(device_id, payload):
    """Threshold-based alerts on received telemetry."""
    temp = payload.get("temperature_c")
    heap = payload.get("free_heap_bytes", 999999)
    if temp is not None and temp > 35.0:
        print(f"[ALERT] {device_id}: High temperature {temp:.1f} C")
    if heap < 50000:
        print(f"[ALERT] {device_id}: Low heap {heap} bytes")
```

Update `on_message` to call `store_telemetry` and `check_telemetry_alerts` when a telemetry message arrives.

### Step 2.2 — Anomaly alert handler

Add an anomaly topic subscriber:

```python
# In on_message, add handler for anomaly topic
elif "/anomaly" in topic:
    device_id = topic.split("/")[1]
    print(f"[ANOMALY ALERT] {device_id}: {payload}")
    # In production: send email/SMS/PagerDuty notification
```

Subscribe to `devices/+/anomaly` in the client setup.

---

## Part 3 — Dashboard Visualization

### Step 3.1 — Generate a time-series chart from telemetry CSV

```python
# file: ~/iot-fleet-lab/dashboard.py
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import os

TELEMETRY_FILE = os.path.expanduser("~/iot-fleet-lab/telemetry.csv")

timestamps = []
temperatures = []
humidity_values = []

with open(TELEMETRY_FILE) as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["temperature_c"]:
            timestamps.append(datetime.fromisoformat(row["timestamp"]))
            temperatures.append(float(row["temperature_c"]))
        if row["humidity_pct"]:
            humidity_values.append(float(row["humidity_pct"]))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.plot(timestamps, temperatures, "r-o", markersize=3, label="Temperature (C)")
ax1.axhline(y=35.0, color="red", linestyle="--", alpha=0.5, label="Alert threshold")
ax1.set_ylabel("Temperature (°C)")
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_title("IoT Capstone Dashboard — device-001")

if humidity_values and len(humidity_values) == len(timestamps):
    ax2.plot(timestamps, humidity_values, "b-o", markersize=3, label="Humidity (%)")
    ax2.set_ylabel("Humidity (%)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.expanduser("~/iot-fleet-lab/dashboard.png"), dpi=150)
plt.show()
print("Dashboard saved to ~/iot-fleet-lab/dashboard.png")
```

Run after collecting at least 5 minutes of telemetry: `python3 ~/iot-fleet-lab/dashboard.py`

---

## Part 4 — System Test and Validation

### Step 4.1 — End-to-end test sequence

Run this validation sequence and capture serial/terminal output at each step:

1. Start the fleet management server: `python3 ~/iot-fleet-lab/fleet_server.py`
2. Flash the ESP32 capstone firmware and open serial monitor.
3. Confirm all four tasks start and the device connects to the broker over TLS.
4. Observe telemetry messages appearing in the fleet server terminal and being written to `telemetry.csv`.
5. Push a shadow desired update to change `reporting_interval_s` to 10 and confirm the ESP32 applies it.
6. Simulate an anomaly: modify `vSensorTask` to inject a reading of 45.0 C once. Confirm the anomaly alert appears in the fleet server terminal.
7. Run the dashboard script and confirm the chart shows the temperature spike.

### Step 4.2 — Verify watchdog behavior

Temporarily comment out the `esp_task_wdt_reset()` call in `vMqttTask`. Reflash. Confirm the TWDT fires after 5 seconds with the task name in the panic log. Revert the change before final submission.

---

## Part 5 — Architecture Documentation

Complete the following documentation deliverables:

### Architecture Diagram

Draw a four-tier architecture diagram (hand-drawn or digital) containing every component in your system, labeled with:

- Component names and technologies (e.g., "ESP32 / FreeRTOS 4 tasks")
- All communication paths with protocol, port, and security mechanism
- The MQTT topic hierarchy

### Security Analysis (OWASP IoT Top 10)

For each of the 10 OWASP IoT categories, write one sentence classifying your system:

- "Fully mitigated — [specific control implemented]"
- "Partially mitigated — [what is done, what gap remains]"
- "Not yet addressed — [risk level and planned mitigation]"

### Architecture Decision Records

Write three ADRs for decisions you made in the capstone:

1. Task priority assignment — why you chose the specific priority values
2. MQTT QoS level — why you used QoS 1 (or your chosen level) for telemetry
3. Anomaly detection method — why you chose z-score over an autoencoder for this implementation

Each ADR must include: Decision, Context, Options Considered, Decision Rationale, Limitations.

### Known Limitations

Document three known limitations of your system using this format:

- Issue: what the gap is
- Risk: impact if exploited or triggered
- Planned resolution: how you would address it with more time
- Current workaround: what reduces the risk now

---

## Troubleshooting Guide

- **All four tasks start but telemetry never appears at the broker** — Check that `vMqttTask` successfully connects before publishing. Add `Serial.println(mqttClient.state())` to diagnose connection state codes.
- **Shadow delta received but configuration not applied** — Ensure the delta handler updates the task-shared variable atomically. Use a mutex or atomic read/write if the variable is accessed from multiple tasks.
- **Dashboard chart shows no data** — Confirm `telemetry.csv` was created and has content: `cat ~/iot-fleet-lab/telemetry.csv | head -5`.
- **Z-score always 0** — The window is not full yet (needs 10 readings). Check `windowFull` flag before publishing anomaly events.

---

## Deliverables

Submit the following as a single PDF to the Canvas LMS capstone assignment:

1. Complete Arduino source code for the four-task capstone firmware.
2. Screenshot of fleet server terminal showing: device registration, telemetry arriving, shadow synchronization, and anomaly alert.
3. Dashboard chart image (`dashboard.png`) showing at least 5 minutes of temperature data with the anomaly spike visible.
4. Architecture diagram (four-tier, fully labeled).
5. OWASP IoT Top 10 analysis — all 10 categories classified with one sentence each.
6. Three Architecture Decision Records (ADR format, as specified above).
7. Three known limitations (using the specified format).
8. Written reflection (200–300 words): What is the most important design decision you made in this capstone, and what would you change if you were building this for production deployment at 10,000 devices?

---
