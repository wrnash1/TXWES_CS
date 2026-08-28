# Reading Guide: Module 10 — Cloud Integration for IoT

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

1. Describe the AWS IoT Core architecture including Things, certificates, policies, and the Rules Engine
2. Explain mutual TLS (mTLS) device authentication using X.509 certificates
3. Implement Device Shadow updates from a microcontroller using the shadow MQTT topics
4. Write a basic AWS IoT Rules Engine SQL expression to filter and route telemetry
5. Compare AWS IoT Core and Azure IoT Hub on architecture, pricing tiers, and key features
6. Identify the direct connection pattern and gateway pattern for MQTT to cloud integration
7. Select between telemetry and command messaging patterns based on reliability requirements

---

## Section 1 — AWS IoT Core

### 1.1 Core Components

| Component | Description |
|-----------|-------------|
| Thing | Digital registry entry representing a physical device |
| Certificate | X.509 certificate used for device identity and TLS authentication |
| Policy | JSON document controlling what MQTT operations the certificate is authorized to perform |
| Thing Shadow | Per-device JSON document storing desired/reported/delta state |
| Rules Engine | SQL-like processor that routes messages to AWS services |
| Greengrass | Edge runtime that extends AWS IoT to local devices (Module 11) |

### 1.2 X.509 Certificate Authentication

AWS IoT Core uses mutual TLS for every connection. Both parties verify each other:

- The device verifies the AWS IoT Core server certificate (using Amazon Root CA)
- The AWS IoT Core broker verifies the device certificate

This eliminates username/password authentication. A compromised credential cannot be used because the attacker does not have the device's private key. Each device has a unique certificate, enabling per-device revocation without affecting other devices.

Certificate lifecycle:

1. **Create** — Generate certificate in AWS Console or using `aws iot create-keys-and-certificate`
2. **Download** — Download device cert, private key, and Root CA (one-time only)
3. **Attach policy** — Assign an IoT policy that defines allowed operations
4. **Attach thing** — Associate the certificate with a specific Thing registry entry
5. **Activate** — Certificate must be in ACTIVE status to allow connections
6. **Revoke** — If device is lost or compromised, set certificate to REVOKED

### 1.3 IoT Policy Structure

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "arn:aws:iot:us-east-1:123456789012:client/${iot:ClientId}"
    },
    {
      "Effect": "Allow",
      "Action": ["iot:Publish", "iot:Receive"],
      "Resource": "arn:aws:iot:us-east-1:123456789012:topic/sensors/${iot:ClientId}/*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/sensors/${iot:ClientId}/*"
    }
  ]
}
```

The `${iot:ClientId}` policy variable substitutes the MQTT client ID at runtime, allowing a single policy to be reused across all devices while preventing one device from publishing on another device's topic.

### 1.4 AWS IoT Core Pricing

| Dimension | Price (US East) |
|-----------|-----------------|
| Connectivity | $0.042 per million minutes connected |
| Messaging | $1.00 per million messages |
| Device Shadow operations | $1.25 per million operations |
| Rules Engine triggers | $0.15 per million rules triggered |
| Rules Engine actions | $0.15 per million actions executed |

For a fleet of 1,000 devices sending one message per minute: 1,000 × 60 × 24 × 30 = 43.2 million messages/month × $1.00/million = $43.20/month for messaging alone.

---

## Section 2 — Device Shadow

### 2.1 Shadow Document Structure

```json
{
  "state": {
    "desired": {
      "setpoint": 72,
      "fan_mode": "auto"
    },
    "reported": {
      "setpoint": 68,
      "fan_mode": "auto",
      "current_temp": 69.5,
      "battery_pct": 87
    },
    "delta": {
      "setpoint": 72
    }
  },
  "metadata": {
    "desired": { "setpoint": { "timestamp": 1717200000 } },
    "reported": { "setpoint": { "timestamp": 1717199400 } }
  },
  "version": 42,
  "timestamp": 1717200010
}
```

The `delta` section is automatically computed: it contains only the keys where `desired` differs from `reported`. This is the section the device should subscribe to and act on.

### 2.2 Shadow MQTT Topics

| Topic | Direction | Purpose |
|-------|-----------|---------|
| `$aws/things/{name}/shadow/update` | Device → AWS | Report state, update desired |
| `$aws/things/{name}/shadow/update/accepted` | AWS → Device | Confirms update was processed |
| `$aws/things/{name}/shadow/update/rejected` | AWS → Device | Reports error in update |
| `$aws/things/{name}/shadow/update/delta` | AWS → Device | New delta when desired != reported |
| `$aws/things/{name}/shadow/get` | Device → AWS | Request current shadow document |
| `$aws/things/{name}/shadow/get/accepted` | AWS → Device | Returns full shadow document |
| `$aws/things/{name}/shadow/delete` | Device → AWS | Delete the shadow |

### 2.3 Shadow Reconciliation Pattern

```cpp
// Subscribe to delta topic at connection
void onMqttConnect() {
  char deltaTopic[80];
  snprintf(deltaTopic, sizeof(deltaTopic),
    "$aws/things/%s/shadow/update/delta", THING_NAME);
  mqtt.subscribe(deltaTopic, 1);

  // Request current shadow on connect
  char getTopic[80];
  snprintf(getTopic, sizeof(getTopic),
    "$aws/things/%s/shadow/get", THING_NAME);
  mqtt.publish(getTopic, "");
}

// Handle delta — apply desired state changes
void onDeltaMessage(const char* topic, byte* payload, unsigned int len) {
  // Parse JSON delta and apply
  // e.g., {"state":{"setpoint":72}} -> set thermostat to 72
  // Then publish reported state to confirm
  reportState(currentSetpoint, currentTemp);
}
```

### 2.4 Named vs Classic Shadows

AWS IoT Core supports multiple named shadows per Thing in addition to the classic (unnamed) shadow. Named shadows allow different subsystems of a device to have independent state documents:

- `$aws/things/hvac-unit-01/shadow/name/setpoints`
- `$aws/things/hvac-unit-01/shadow/name/schedule`
- `$aws/things/hvac-unit-01/shadow/name/diagnostics`

---

## Section 3 — AWS IoT Rules Engine

### 3.1 Rule SQL Syntax

```sql
SELECT
  topic(2) AS device_id,     -- Extract 2nd topic level as device_id
  temperature,               -- From message payload
  humidity,
  timestamp() AS ts,         -- AWS IoT function
  newuuid() AS reading_id    -- AWS IoT function
FROM 'sensors/+/telemetry'   -- MQTT topic filter
WHERE temperature > 25       -- Optional filter
```

### 3.2 Rule Actions

| Action | Use Case |
|--------|----------|
| DynamoDB | Persist readings to a NoSQL table |
| Lambda | Custom processing: ML inference, enrichment, validation |
| SNS | Email/SMS alerts on threshold events |
| S3 | Archive raw data for long-term storage |
| Kinesis Data Streams | High-volume real-time stream processing |
| CloudWatch | Log metrics for monitoring and alerting |
| IoT Core republish | Route to another MQTT topic |
| SQS | Queue messages for batch processing |

### 3.3 Error Action

Every rule should include an error action — a secondary action that handles messages the rule fails to process (malformed JSON, missing fields, downstream service unavailable):

```json
{
  "errorAction": {
    "sqs": {
      "queueUrl": "https://sqs.us-east-1.amazonaws.com/123/iot-errors",
      "roleArn": "arn:aws:iam::123:role/iot-error-role",
      "useBase64": false
    }
  }
}
```

---

## Section 4 — Azure IoT Hub

### 4.1 Architecture Comparison

| Feature | AWS IoT Core | Azure IoT Hub |
|---------|-------------|---------------|
| Device registry | Thing | Device |
| State synchronization | Device Shadow | Device Twin |
| Message routing | Rules Engine (SQL) | Message Routing (query) |
| Protocol support | MQTT, HTTPS | MQTT, AMQP, HTTPS |
| Device provisioning | Fleet Provisioning | Device Provisioning Service (DPS) |
| Edge runtime | Greengrass | IoT Edge |
| Free tier | No (pay per use) | 8,000 msg/day free |

### 4.2 Azure IoT Hub Tiers

| Tier | Messages/day | Price | Use Case |
|------|-------------|-------|----------|
| Free (F1) | 8,000 | $0/month | Development, testing |
| Basic B1 | 400,000 | ~$10/month | Production, device-to-cloud only |
| Standard S1 | 400,000 | ~$25/month | Full features including C2D |
| Standard S2 | 6,000,000 | ~$250/month | High-volume production |

### 4.3 Device Twin

Azure Device Twin follows the same desired/reported/delta pattern as AWS Device Shadow:

```json
{
  "deviceId": "esp32-sensor-01",
  "properties": {
    "desired": {
      "setpoint": 72,
      "$version": 5
    },
    "reported": {
      "setpoint": 68,
      "firmware_version": "1.2.3",
      "$version": 12
    }
  },
  "tags": {
    "location": "building_A/floor_2/room_14"
  }
}
```

Tags are metadata written by the backend application (not the device) and used for querying groups of devices.

### 4.4 IoT Hub Message Routing

Azure IoT Hub routes messages based on message properties or body content:

```text
Query: $twin.tags.location = 'building_A/floor_2/room_14' AND temperature > 25
Route to: Event Hub endpoint for real-time processing
```

---

## Section 5 — MQTT to Cloud Integration Patterns

### 5.1 Direct Connection Pattern

```text
[IoT Device] --mTLS MQTT--> [Cloud Broker] --> [Rules/Routing] --> [Storage/Analytics]
```

Requirements for the device:

- Sufficient RAM for TLS stack (minimum ~50 KB, ESP32 is adequate)
- Ability to store X.509 certificates securely
- Reliable internet connectivity

Advantages: simple architecture, device is a first-class cloud citizen with its own identity.

Disadvantages: TLS overhead for each connection, certificate management at scale.

### 5.2 Gateway Pattern

```text
[BLE/Zigbee Sensors] --> [Local Gateway] --mTLS MQTT--> [Cloud Broker]
```

The gateway (Raspberry Pi, industrial gateway, AWS Greengrass device) holds a single cloud certificate. Local sensors connect over BLE, Zigbee, LoRaWAN, or local MQTT — no TLS required at the sensor level.

Advantages: Sensors can be ultra-simple (no TLS, no IP stack). Gateway aggregates and batches messages for efficiency.

Disadvantages: Gateway is a single point of failure. Requires gateway hardware and maintenance.

### 5.3 Telemetry vs Command Patterns

| Characteristic | Telemetry | Command |
|---------------|-----------|---------|
| Direction | Device to cloud | Cloud to device |
| Frequency | High (seconds to minutes) | Low (rare events) |
| Loss tolerance | High (missing one reading is OK) | Low (every command must arrive) |
| QoS | QoS 0 or 1 | QoS 1 + Device Shadow |
| Delivery mechanism | MQTT publish | Shadow desired state |

---

## Key Terms

| Term | Definition |
|------|------------|
| AWS IoT Core | Amazon's managed IoT MQTT broker and rules engine service |
| Thing | AWS IoT Core registry entry representing a physical device |
| mTLS | Mutual TLS — both client and server authenticate with certificates |
| X.509 | Certificate format used for device identity in IoT platforms |
| Device Shadow | AWS IoT persistent JSON document storing device desired/reported state |
| Device Twin | Azure IoT Hub equivalent of AWS Device Shadow |
| Rules Engine | AWS IoT SQL processor that routes messages to AWS services |
| Delta | Auto-computed difference between desired and reported state |
| Azure IoT Hub | Microsoft's managed IoT message broker and device registry |
| DPS | Device Provisioning Service — Azure zero-touch device enrollment |
| Greengrass | AWS edge computing runtime extending IoT Core to local devices |
| IoT Edge | Azure edge computing runtime equivalent to AWS Greengrass |

---

## Review Questions

1. Why does AWS IoT Core use X.509 certificates instead of username/password for device authentication? What specific security advantage does this provide?
2. A Device Shadow `desired` section contains `{"fan_mode": "high"}` while the `reported` section contains `{"fan_mode": "auto"}`. What will the `delta` section contain, and what should the device do when it receives the delta?
3. Write a Rules Engine SQL expression that selects all temperature readings above 90°F from the topic `plant/+/sensors`, extracts the plant name from the second topic level, and adds a timestamp.
4. Compare the free tier limitations of AWS IoT Core vs Azure IoT Hub. Which is more useful for a student lab project with 5 devices sending 1 message per minute?
5. Explain the gateway pattern. When would you choose it over direct device-to-cloud MQTT connection?
6. A thermostat is offline for 3 hours. During that time, a user changes the target temperature via a phone app. How does Device Shadow ensure the thermostat eventually applies the new temperature? Walk through each step.
7. What is the purpose of the `${iot:ClientId}` policy variable in an AWS IoT Core policy, and why is it more secure than using a wildcard `*` for all resources?
8. An IoT Rules Engine rule processes 50 million messages per month. Using AWS IoT Core pricing, calculate the monthly cost for just the messaging and rules engine actions (assume each message triggers one rule with one action).

---

## 9. Supplemental Resources

**1. AWS IoT Core Developer Guide — Device Provisioning and Certificates**
[https://docs.aws.amazon.com/iot/latest/developerguide/iot-provision.html](https://docs.aws.amazon.com/iot/latest/developerguide/iot-provision.html)
Amazon's official documentation for registering Things, creating X.509 certificates, attaching IoT policies, and implementing Device Shadow. Covers both single-device and fleet provisioning patterns (just-in-time provisioning, JITR) referenced in Sections 1–3 of this guide.

**2. Azure IoT Hub Developer Guide — Device Twins and Direct Methods**
[https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins)
Microsoft's reference for Azure IoT Hub Device Twins, including the desired/reported/delta property model, device-to-cloud and cloud-to-device messaging patterns, and the Device Provisioning Service (DPS). Directly supports Section 4 of this reading guide on Azure IoT integration.

**3. NIST SP 800-213 — IoT Device Cybersecurity Guidance for the Federal Government**
[https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-213.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-213.pdf)
NIST's IoT device security baseline covering device identity, configuration management, data protection, and logical access controls. Provides the policy-level framework behind the technical controls (mTLS, X.509, Device Shadow policies) covered throughout this module.
