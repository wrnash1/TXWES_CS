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

## Part 9 — Challenge Exercise

### Challenge 1: OWASP IoT Top 10 Gap Analysis and Remediation ADR

Perform a rigorous OWASP IoT Top 10 analysis of the capstone system and produce a professional ADR for each identified gap, prioritized by risk.

1. For each of the ten OWASP IoT Top 10 categories, classify the capstone system as Fully Mitigated, Partially Mitigated, or Not Addressed. Record your classification in a Markdown table with five columns: `Category`, `OWASP Number`, `Classification`, `Evidence`, and `Residual Risk`. The Evidence column must reference a specific capstone component (e.g., "mTLS with per-device X.509 certificate in Mosquitto broker config"), not a general statement. The Residual Risk column must be one of: None, Low, Medium, High.

   | Category | OWASP # | Classification | Evidence | Residual Risk |
   |---|---|---|---|---|
   | Weak Passwords | #1 | Fully Mitigated | Per-device X.509 mTLS; no password-based auth | None |
   | Insecure Network Services | #2 | ... | ... | ... |
   | ... | | | | |

1. Identify the two highest residual risk categories from your analysis. For each, write a complete ADR using the five-element format from the reading guide (Decision, Context, Options Considered, Decision Rationale, Limitations). The ADR must document a specific, implementable remediation — not a general statement like "implement better security." For example, if the residual risk is certificate renewal (OWASP #4 or general lifecycle management), the ADR must specify: the renewal trigger mechanism (device shadow desired state push vs. certificate expiry alert), the renewal protocol (ACME, AWS ACM PCA, or manual re-provisioning), and the rollback procedure if renewal fails.

1. For the highest-risk gap identified, add a fourth ADR for the workaround that will be used until the full remediation is implemented. The workaround ADR must include a "sunset condition" — the specific, measurable event that will trigger switching from the workaround to the full remediation (e.g., "This workaround is retired when the automated certificate monitoring alert described in ADR-005 is deployed and verified for 30 days without a missed expiry event").

1. In your lab report, write a 3–4 sentence analysis of which OWASP category represents the most systemic challenge for IoT deployments at scale — not just for this capstone, but for the industry broadly — and justify your choice using a concrete real-world IoT incident as supporting evidence.

---

### Challenge 2: Production Readiness Checklist and Architecture Review Board Simulation

Produce the documentation a production IoT system would require before receiving approval for fleet-wide deployment, and simulate an Architecture Review Board (ARB) challenge process.

1. Write a Production Readiness Checklist for the capstone system covering six dimensions. For each dimension, define the specific pass/fail criterion and evaluate the capstone system against it (Pass, Fail, or Partial with explanation). The six dimensions are:

   - **Security**: All OWASP Top 10 categories at Medium residual risk or below
   - **Reliability**: Watchdog timer covers all tasks; MQTT task reconnects within 30 seconds of network loss
   - **Observability**: All alert conditions have documented thresholds; telemetry covers all four monitoring categories from Module 15
   - **Operations**: Certificate expiry monitoring alert in place; decommissioning procedure documented and tested
   - **Scalability**: Architecture supports 100 devices without code changes; broker configured for concurrent connections
   - **Documentation**: Architecture diagram complete; three ADRs written; OWASP analysis complete; known limitations documented

1. Assign each dimension a traffic-light status (Green/Yellow/Red) based on the capstone evaluation. A "Green" requires a full Pass; "Yellow" requires Partial; "Red" requires Fail. Write a one-sentence deployment recommendation: either "Approved for canary deployment (1% of fleet)" if all dimensions are Yellow or better, "Approved for pilot deployment (10% of fleet)" if all dimensions are Green, or "Not approved — remediate [list specific Red dimensions] before deployment."

1. Simulate three ARB challenge questions. For each question, write a 3–5 sentence technical response that references specific capstone components, code, or documentation:

   - Challenge A: "The z-score anomaly detector uses a 10-sample window. At a 30-second reporting interval, this means the detector has no valid history for the first 5 minutes of device operation. How does the system behave during this warm-up period, and is this acceptable for your use case?"
   - Challenge B: "The decommissioning procedure in Module 15 marks the certificate as revoked in a local registry file. How does the broker know the certificate has been revoked if the CRL is not published to the broker? What is the lag between registry revocation and broker enforcement, and what attack is possible during that lag?"
   - Challenge C: "The telemetry CSV grows indefinitely. At 30-second intervals, 100 devices would generate approximately 10,400 rows per hour. What is the projected storage consumption after 90 days, and what retention policy would you implement?"

---

### Reflection Questions

1. The Production Readiness Checklist in Challenge 2 evaluates the capstone against six dimensions independently. In a real production deployment, these dimensions interact: improving Security (client certificate validation on every API endpoint) may reduce Scalability (certificate validation adds latency to every request). Describe one specific trade-off in the capstone system where improving one dimension of the checklist would degrade another dimension, and explain how you would resolve the conflict using the ADR format (without writing the full ADR — just identify the decision, the competing dimensions, and the rationale direction).

2. The ARB simulation in Challenge 2 tests your ability to defend design decisions under adversarial questioning. In a professional engineering context, an ARB question you cannot answer is more valuable than one you can — it identifies a real gap in the system design. Identify one additional ARB question about the capstone system that you would not be able to answer confidently with the current implementation, explain why that question is important (what risk it exposes), and describe what you would need to build or measure to answer it.
