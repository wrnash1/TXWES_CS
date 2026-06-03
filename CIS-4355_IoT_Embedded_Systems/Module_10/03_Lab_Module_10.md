# Lab: Module 10 — Cloud Integration for IoT

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Points:** 100

---

## Lab Overview

In this lab you will connect an ESP32 to AWS IoT Core using mutual TLS authentication, publish sensor data as MQTT messages, view live messages in the AWS MQTT test client, implement Device Shadow updates, and create an IoT Rules Engine rule that routes temperature alerts to an SNS email notification.

**Estimated time:** 3–4 hours

**Hardware required:**

- ESP32 DevKit V1
- DHT22 sensor (from Module 08 lab)
- USB cable

**Software and accounts required:**

- Arduino IDE with ESP32 board support
- AWS account (free tier is sufficient — create one at aws.amazon.com if needed)
- ArduinoJson library (install via Library Manager)
- PubSubClient library
- DHT sensor library by Adafruit

**AWS services used (all free tier eligible for lab scale):**

- AWS IoT Core
- Amazon SNS (Simple Notification Service)
- Amazon CloudWatch Logs (optional, for debugging)

---

## Part A — AWS IoT Core Setup and Certificate Download (20 points)

### Part A Procedure

This part is completed entirely in the AWS Console — no code yet.

**Step 1: Create a Thing**

1. Sign in to the AWS Console and navigate to IoT Core
2. In the left panel: Manage > All devices > Things
3. Click "Create things" > "Create single thing"
4. Name the Thing: `esp32-sensor-01`
5. Leave device shadow as "No shadow" for now (we add it in Part C)
6. Click Next

**Step 2: Create and download certificates**

1. Choose "Auto-generate a new certificate"
2. Click "Create thing"
3. Download all four files:
   - Device certificate: `esp32-sensor-01.pem.crt`
   - Private key: `esp32-sensor-01.private.pem.key`
   - Amazon Root CA 1: `AmazonRootCA1.pem`
   - Amazon Root CA 3: `AmazonRootCA3.pem`
4. Click "Activate" to activate the certificate
5. These files cannot be re-downloaded — save them securely

**Step 3: Create and attach a policy**

1. Navigate to: Security > Policies > Create policy
2. Name: `esp32-sensor-policy`
3. Click "JSON" and paste:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Connect",
        "iot:Publish",
        "iot:Subscribe",
        "iot:Receive",
        "iot:GetThingShadow",
        "iot:UpdateThingShadow"
      ],
      "Resource": "*"
    }
  ]
}
```

4. Create the policy
5. Navigate to Security > Certificates, find your certificate, click it
6. Attach the policy `esp32-sensor-policy`
7. Attach the Thing `esp32-sensor-01`

**Step 4: Find your endpoint**

1. Navigate to Settings (bottom of left panel)
2. Copy the Endpoint URL — it looks like: `abc123xyz.iot.us-east-1.amazonaws.com`

### Part A Deliverables

- Screenshot of the AWS IoT Core Things page showing `esp32-sensor-01` registered
- Screenshot of the Certificates page showing the certificate with ACTIVE status
- Your endpoint URL (redact the account-specific prefix if concerned — just note the region)

---

## Part B — ESP32 Connecting and Publishing to AWS IoT Core (30 points)

### Part B Setup

Open the three downloaded certificate files in a text editor. You will paste the contents into the sketch as string constants.

### Part B Code

```cpp
// Lab 10 Part B: ESP32 to AWS IoT Core via MQTT over TLS
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <DHT.h>

// --- Wi-Fi ---
const char* WIFI_SSID = "YourNetwork";
const char* WIFI_PASS = "YourPassword";

// --- AWS IoT ---
const char* AWS_ENDPOINT = "YOUR-ENDPOINT.iot.us-east-1.amazonaws.com";
const char* THING_NAME   = "esp32-sensor-01";

// Paste certificate file contents between the quotes:
const char* ROOT_CA = R"EOF(
-----BEGIN CERTIFICATE-----
PASTE AMAZON ROOT CA 1 HERE
-----END CERTIFICATE-----
)EOF";

const char* DEVICE_CERT = R"EOF(
-----BEGIN CERTIFICATE-----
PASTE DEVICE CERTIFICATE HERE
-----END CERTIFICATE-----
)EOF";

const char* PRIVATE_KEY = R"EOF(
-----BEGIN RSA PRIVATE KEY-----
PASTE PRIVATE KEY HERE
-----END RSA PRIVATE KEY-----
)EOF";

// --- MQTT Topics ---
const char* TOPIC_TELEMETRY = "sensors/esp32-sensor-01/telemetry";

// --- Sensor ---
DHT dht(4, DHT22);

WiFiClientSecure tlsClient;
PubSubClient     mqtt(tlsClient);

void connectWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.printf("\nWi-Fi connected: %s\n", WiFi.localIP().toString().c_str());
}

void connectMQTT() {
  tlsClient.setCACert(ROOT_CA);
  tlsClient.setCertificate(DEVICE_CERT);
  tlsClient.setPrivateKey(PRIVATE_KEY);
  mqtt.setServer(AWS_ENDPOINT, 8883);

  Serial.print("Connecting to AWS IoT Core");
  while (!mqtt.connected()) {
    if (mqtt.connect(THING_NAME)) {
      Serial.println("\nConnected to AWS IoT Core!");
    } else {
      Serial.printf(".");
      delay(2000);
    }
  }
}

uint32_t seqNum = 0;

void publishTelemetry() {
  float temp  = dht.readTemperature(true);   // Fahrenheit
  float humid = dht.readHumidity();

  if (isnan(temp) || isnan(humid)) {
    Serial.println(F("DHT read error"));
    return;
  }

  char payload[160];
  snprintf(payload, sizeof(payload),
    "{\"seq\":%lu,\"device\":\"%s\","
    "\"temp_f\":%.1f,\"humidity\":%.1f}",
    seqNum++, THING_NAME, temp, humid);

  bool ok = mqtt.publish(TOPIC_TELEMETRY, payload);
  Serial.printf("Published [%s]: %s\n", ok ? "OK" : "FAIL", payload);
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectWiFi();
  connectMQTT();
}

void loop() {
  if (!mqtt.connected()) connectMQTT();
  mqtt.loop();
  publishTelemetry();
  delay(10000);  // Publish every 10 seconds
}
```

### Part B Test with AWS MQTT Test Client

1. In the AWS IoT Core console, navigate to MQTT test client (left panel)
2. Under "Subscribe to a topic", enter `sensors/esp32-sensor-01/telemetry`
3. Click Subscribe
4. Run your ESP32 sketch
5. Within 15 seconds, messages should appear in the test client window

### Part B Expected Serial Output

```text
Connecting to WiFi.........
Wi-Fi connected: 192.168.1.105
Connecting to AWS IoT Core...
Connected to AWS IoT Core!
Published [OK]: {"seq":0,"device":"esp32-sensor-01","temp_f":75.4,"humidity":58.3}
Published [OK]: {"seq":1,"device":"esp32-sensor-01","temp_f":75.5,"humidity":58.2}
```

### Part B Deliverables

- Screenshot of ESP32 Serial Monitor showing successful connection and at least 3 published messages
- Screenshot of AWS MQTT Test Client showing live messages from the ESP32

---

## Part C — Device Shadow Updates (25 points)

### Part C Objective

Add Device Shadow reporting to the sketch. The ESP32 will report its current temperature and humidity to the shadow on every reading. You will verify the shadow state in the AWS Console.

### Part C Code Addition

Add these functions to the Part B sketch and call them after `connectMQTT()` and in `loop()`:

```cpp
// Device Shadow topics
char shadowUpdateTopic[80];
char shadowGetAccepted[80];

void setupShadowTopics() {
  snprintf(shadowUpdateTopic, sizeof(shadowUpdateTopic),
    "$aws/things/%s/shadow/update", THING_NAME);
  snprintf(shadowGetAccepted, sizeof(shadowGetAccepted),
    "$aws/things/%s/shadow/get/accepted", THING_NAME);
}

void reportShadowState(float tempF, float humid) {
  char payload[200];
  snprintf(payload, sizeof(payload),
    "{\"state\":{\"reported\":{"
    "\"temp_f\":%.1f,"
    "\"humidity\":%.1f,"
    "\"uptime_s\":%lu"
    "}}}",
    tempF, humid, millis() / 1000);

  bool ok = mqtt.publish(shadowUpdateTopic, payload);
  Serial.printf("Shadow update [%s]\n", ok ? "OK" : "FAIL");
}
```

Call `setupShadowTopics()` in `setup()` after `connectMQTT()`, and call `reportShadowState(temp, humid)` inside `publishTelemetry()`.

### Part C Verification

In the AWS IoT Core console:

1. Navigate to Manage > All devices > Things > `esp32-sensor-01`
2. Click the "Device Shadow" tab
3. Click "Classic Shadow"
4. You should see the shadow document with your reported state updating

### Part C Deliverables

- Screenshot of the AWS Console Shadow document showing reported temperature and humidity
- Answer (2–3 sentences): What would happen to the Device Shadow if you added a `desired` section from the AWS Console — for example, setting `{"desired": {"alert_threshold": 85}}` — and the ESP32 were offline at that moment? When would the device see this change?

---

## Part D — IoT Rules Engine Alert (25 points)

### Part D Objective

Create an IoT Rules Engine rule that sends an SNS email notification whenever a temperature reading exceeds 80°F.

### Part D Step 1 — Create SNS Topic

1. Navigate to Amazon SNS > Topics > Create topic
2. Type: Standard, Name: `iot-temp-alerts`
3. Create topic
4. Click "Create subscription": Protocol = Email, Endpoint = your email address
5. Check your email and confirm the subscription

### Part D Step 2 — Create IoT Rule

1. Navigate to IoT Core > Message routing > Rules > Create rule
2. Name: `HighTempAlert`
3. SQL statement:

```sql
SELECT
  device,
  temp_f,
  humidity,
  timestamp() AS ts
FROM 'sensors/+/telemetry'
WHERE temp_f > 80
```

4. Set rule action: "Simple Notification Service (SNS)"
5. Select the `iot-temp-alerts` topic
6. Create or select an IAM role that allows IoT to publish to SNS
7. Create the rule

### Part D Test

To trigger the rule without physically heating the sensor, temporarily change the threshold in your sketch to a value below current room temperature:

```cpp
// Temporary test: always publish a "high" temperature to trigger rule
snprintf(payload, sizeof(payload),
  "{\"seq\":%lu,\"device\":\"%s\","
  "\"temp_f\":%.1f,\"humidity\":%.1f}",
  seqNum++, THING_NAME, 85.0f, humid);  // Hardcode 85°F for testing
```

Upload and run the sketch. Within 1–2 minutes, you should receive an SNS email notification.

### Part D Expected Email

```text
Subject: AWS Notification - Subscription Confirmation

{"device":"esp32-sensor-01","temp_f":85.0,"humidity":58.3,"ts":1717200000000}
```

### Part D Deliverables

- Screenshot of the IoT Rules Engine showing the `HighTempAlert` rule with ACTIVE status
- Screenshot of the SNS email notification received in your inbox
- Screenshot of the SNS subscription showing CONFIRMED status

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| **Part A** — Thing registered, certificate ACTIVE | 10 |
| **Part A** — Policy created and attached | 10 |
| **Part B** — ESP32 connects to AWS IoT Core | 10 |
| **Part B** — Serial Monitor shows published messages | 10 |
| **Part B** — AWS MQTT Test Client screenshot with live data | 10 |
| **Part C** — Shadow document visible in AWS Console | 10 |
| **Part C** — Shadow shows reported temperature and humidity | 10 |
| **Part C** — Written shadow behavior explanation | 5 |
| **Part D** — IoT Rule created with correct SQL | 10 |
| **Part D** — SNS email received with payload | 10 |
| **Part D** — SNS subscription confirmed | 5 |
| **TOTAL** | **100** |

---

## Troubleshooting Tips

**MQTT connection fails silently:** The most common cause is a certificate not properly embedded. Check for extra blank lines at the beginning or end of the certificate strings. The certificate must start exactly with `-----BEGIN CERTIFICATE-----`.

**mqtt.state() returns -2:** This means the broker refused the connection. Verify the endpoint URL is exact and the certificate is ACTIVE in the console.

**Shadow update publishes OK but shadow is empty:** Confirm the JSON structure has the exact path `{"state":{"reported":{...}}}` — Shadow ignores updates that are not in this exact structure.

**SNS rule never triggers:** Verify the IAM role attached to the rule has `sns:Publish` permission on the topic ARN. Also confirm the rule SQL `WHERE` clause condition is met by your test data.

**Certificate download missed:** If you did not download the private key when creating the certificate, you must create a new certificate — the private key cannot be retrieved after initial creation.
