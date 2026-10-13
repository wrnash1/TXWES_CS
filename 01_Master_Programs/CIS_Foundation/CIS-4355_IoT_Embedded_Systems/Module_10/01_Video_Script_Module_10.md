# Video Script: Module 10 — Cloud Integration for IoT

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Estimated Duration:** 20–24 minutes

**Certification Alignment:** IoT Fundamentals / Embedded Systems

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4355. I'm Professor Nash. We have built embedded systems that read sensors and communicate wirelessly. Now it is time to connect them to the cloud — where data is stored, analyzed, and acted upon.

In this module we cover three major cloud IoT platforms: AWS IoT Core, Azure IoT Hub, and Google Cloud IoT. We focus on AWS IoT Core in depth because it is the most widely adopted and richest in features. We will also look at the pattern of connecting MQTT from a device to cloud, and how device shadow state works — a critical concept for reliably managing thousands of remote devices.

---

## SEGMENT 2 — Why Cloud Integration? (1:30–3:00)

Your ESP32 can read a temperature sensor every 10 seconds. But what does it do with that data?

Without cloud integration: the data disappears the moment it is overwritten in the device's small buffer. You cannot view historical trends. You cannot alert on threshold crossings. You cannot compare readings across 100 devices. You cannot trigger actuators based on patterns. You cannot integrate with billing, ERP, or safety systems.

With cloud integration: every reading is stored in a time-series database. Dashboards show trends. Rules engines trigger alerts, emails, Lambda functions, and database writes automatically. Device shadow state lets you know the last-known status of any device even when it is offline. Fleet management tools let you push firmware updates to thousands of devices simultaneously.

Cloud integration is what turns a sensor into an IoT solution.

---

## SEGMENT 3 — AWS IoT Core Architecture (3:00–7:00)

[SHOW HARDWARE: Browser open to AWS IoT Core console, ESP32 connected to laptop, Serial Monitor visible]

AWS IoT Core is Amazon's managed IoT platform. It provides a fully managed MQTT broker that scales to billions of messages and millions of devices without you managing any server infrastructure.

The core components:

**Things:** A Thing is the digital representation of a physical device in AWS IoT Core. It has a name, attributes, and a certificate for authentication. When you register a device, you create a Thing.

**Certificates:** AWS IoT Core uses mutual TLS (mTLS) for device authentication. Every device gets a unique X.509 certificate. The device presents this certificate when connecting to the broker. The broker verifies it against the AWS Certificate Authority. There are no usernames or passwords.

**Policies:** An IAM-like policy attached to a certificate controls what MQTT topics the device can publish to, subscribe to, and connect with.

**Rules Engine:** A SQL-like rule engine that inspects incoming MQTT messages and triggers actions: write to DynamoDB, invoke a Lambda function, send an SNS notification, republish to another topic, write to S3, forward to Kinesis Data Streams.

**Device Shadow:** A persistent JSON document stored in AWS IoT Core that represents the desired and reported state of a device. We will come back to this in detail.

The MQTT endpoint for AWS IoT Core is unique per account: `<account-prefix>.iot.<region>.amazonaws.com` on port 8883 (TLS).

---

## SEGMENT 4 — Connecting an ESP32 to AWS IoT Core (7:00–10:30)

Let me walk through what it takes to connect an ESP32 to AWS IoT Core. This is more involved than connecting to Mosquitto, but the extra steps buy you enterprise-grade security.

Step 1: In the AWS Console, navigate to IoT Core and create a Thing named `esp32-sensor-01`.

Step 2: Create a certificate. Download four files: the device certificate (.pem.crt), the private key (.pem.key), the Amazon Root CA 1 certificate, and the Amazon Root CA 3 certificate. These are downloaded once — keep them secure.

Step 3: Create a policy and attach it to the certificate. A minimal policy for publishing:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["iot:Connect", "iot:Publish", "iot:Subscribe", "iot:Receive"],
    "Resource": "arn:aws:iot:us-east-1:123456789:*"
  }]
}
```

Step 4: Attach the certificate to the Thing and activate it.

Step 5: In your ESP32 sketch, embed the certificate and private key as char arrays (or load from SPIFFS), configure the TLS client, and connect:

```cpp
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

// Certificate strings — paste from downloaded files
const char* ROOT_CA = R"(-----BEGIN CERTIFICATE-----
...Amazon Root CA 1...
-----END CERTIFICATE-----)";

const char* DEVICE_CERT = R"(-----BEGIN CERTIFICATE-----
...Device certificate...
-----END CERTIFICATE-----)";

const char* PRIVATE_KEY = R"(-----BEGIN RSA PRIVATE KEY-----
...Private key...
-----END RSA PRIVATE KEY-----)";

const char* AWS_ENDPOINT = "YOUR-ID.iot.us-east-1.amazonaws.com";

WiFiClientSecure tlsClient;
PubSubClient     mqtt(tlsClient);

void connectAWS() {
  tlsClient.setCACert(ROOT_CA);
  tlsClient.setCertificate(DEVICE_CERT);
  tlsClient.setPrivateKey(PRIVATE_KEY);

  mqtt.setServer(AWS_ENDPOINT, 8883);
  while (!mqtt.connected()) {
    if (mqtt.connect("esp32-sensor-01")) {
      Serial.println("Connected to AWS IoT Core");
    } else {
      Serial.printf("Failed, rc=%d\n", mqtt.state());
      delay(5000);
    }
  }
}
```

Once connected, publishing to AWS follows the same MQTT `publish()` pattern as Mosquitto. The difference is the broker verifies the device's identity cryptographically on every connection.

---

## SEGMENT 5 — Device Shadow (10:30–13:00)

Device Shadow is one of the most powerful and underappreciated features of cloud IoT platforms.

A Device Shadow is a JSON document stored in AWS IoT Core that has two key sections: `desired` and `reported`.

- `desired`: The state you want the device to be in. Written by your application or cloud rules.
- `reported`: The state the device actually is in. Written by the device.

Why does this matter? Consider a thermostat. You set the target temperature to 72°F from a phone app. The thermostat happens to be offline — battery low, poor signal. With Device Shadow, your app writes `{"desired": {"setpoint": 72}}` to the shadow. The cloud stores it. When the thermostat reconnects, it reads the shadow, sees the pending desired state, applies it, then reports back `{"reported": {"setpoint": 72, "current_temp": 69.5}}`.

Without Device Shadow, the command is lost. With it, commands are durable and reconciled automatically.

```cpp
// Publishing reported state to shadow
const char* SHADOW_UPDATE = "$aws/things/esp32-sensor-01/shadow/update";

void reportState(float temp, float humid) {
  char payload[128];
  snprintf(payload, sizeof(payload),
    "{\"state\":{\"reported\":{\"temperature\":%.2f,\"humidity\":%.1f}}}",
    temp, humid);
  mqtt.publish(SHADOW_UPDATE, payload);
}
```

The shadow also has a `delta` section — AWS IoT automatically computes the difference between desired and reported and publishes it to the delta topic. Your device can subscribe to this topic and only act when there is an actual difference to reconcile.

---

## SEGMENT 6 — AWS IoT Rules Engine (13:00–15:00)

The Rules Engine is the automation backbone of AWS IoT Core. You write SQL-like rules that filter and route incoming MQTT messages to over 15 AWS services.

Example: Write every temperature reading above 80°F to a DynamoDB table and send an SNS email alert:

```sql
SELECT
  topic(3) AS device_id,
  temperature,
  timestamp() AS ts
FROM 'sensors/+/data'
WHERE temperature > 80
```

This rule subscribes to the wildcard topic `sensors/+/data`, extracts the device ID from the third topic level, adds a timestamp, and routes to DynamoDB and SNS simultaneously.

The Rules Engine enables serverless IoT architectures: no constantly-running server is needed to process device data. The cloud reacts to events as they arrive.

---

## SEGMENT 7 — Azure IoT Hub (15:00–17:30)

Azure IoT Hub is Microsoft's equivalent to AWS IoT Core. The core concepts map closely:

- **Device Twin** = Device Shadow (desired/reported/delta pattern)
- **Message Routing** = Rules Engine (route to Event Hub, Service Bus, Blob Storage)
- **IoT Hub → Stream Analytics → Cosmos DB** = common analytics pipeline
- **Device Provisioning Service (DPS)** = automatic zero-touch device provisioning

Azure IoT Hub has three tiers: Free (8,000 messages/day), Standard S1 ($25/month, 400,000 messages/day), and Standard S2 ($250/month, 6 million messages/day per unit).

A key Azure IoT Hub feature: the Hub supports both MQTT and AMQP (Advanced Message Queuing Protocol). AMQP provides higher throughput for gateway devices that batch messages from hundreds of downstream sensors.

The Device Twin format in Azure is essentially the same as AWS Device Shadow — a JSON document with `desired` and `reported` sections, plus auto-computed `properties.reported` diff.

---

## SEGMENT 8 — Google Cloud IoT (17:30–19:00)

Google Cloud IoT (formerly Google Cloud IoT Core) was a managed MQTT broker service that Google deprecated in 2023. Google's current recommendation for IoT workloads is Cloud Pub/Sub (for message ingestion) combined with Cloud IoT services from partners or self-managed MQTT brokers.

The historical Google Cloud IoT approach is worth understanding because it introduced the concept of JWT-based device authentication — instead of X.509 certificates, devices signed a JWT with an RSA or EC private key for a short-lived token. This reduced the key management overhead for some deployments.

For new Google Cloud IoT deployments, the modern stack is: device → Pub/Sub → Cloud Functions or Dataflow → BigQuery for analytics.

---

## SEGMENT 9 — MQTT to Cloud Patterns (19:00–21:00)

Let me summarize the key patterns for connecting MQTT devices to cloud platforms.

**Direct connection:** Device connects directly to the cloud broker (AWS IoT Core, Azure IoT Hub) using mutual TLS and an X.509 certificate. Best for devices with sufficient RAM for TLS (ESP32 and above). Simplest architecture.

**Gateway pattern:** A local gateway (Raspberry Pi, industrial PC, or cloud-managed edge device) aggregates data from many small devices over local protocols (Zigbee, BLE, LoRaWAN) and connects to the cloud on their behalf. The gateway holds the cloud credentials. The small devices can be much simpler — no TLS stack required.

**Shadow/twin reconciliation:** Use Device Shadow or Device Twin for all state management. Never rely on real-time command delivery to a device that may be offline. Write desired state to the shadow; let the device reconcile on next connection.

**Telemetry vs commands:** Telemetry is device-to-cloud, frequent, OK to lose occasional readings. Commands are cloud-to-device, infrequent, must be durable (use QoS 1 or Device Shadow). Design your topic structure and QoS levels to reflect this distinction.

---

## SEGMENT 10 — Wrap-Up and Preview (21:00–23:00)

Let's recap. Cloud IoT platforms — AWS IoT Core, Azure IoT Hub, Google Cloud IoT — provide managed MQTT brokers, certificate-based device authentication, device shadow/twin state management, and rules engines that route messages to databases, functions, and alerts. The Device Shadow pattern is critical for reliable remote device management. MQTT to cloud follows either a direct TLS connection or a gateway aggregation pattern.

In Module 11 we move to edge computing — where intelligence moves from the cloud back to the device itself. You will learn about AWS Greengrass, Azure IoT Edge, TensorFlow Lite for on-device machine learning inference, and Over-the-Air firmware updates. This is the frontier of IoT right now.

See you there.

---

## PRODUCTION NOTES

- Screen capture: AWS IoT Core console showing Thing creation, certificate download, policy attachment
- Screen capture: MQTT test client in AWS console showing incoming messages from ESP32
- Screen capture: Rules Engine SQL editor with sample rule
- Demo: ESP32 Serial Monitor connecting to AWS IoT Core with TLS
- Closed captions: verify IoT Core, mTLS, X.509, Device Shadow, AMQP, DPS, DynamoDB, Lambda, SNS
- Run time target: 22 minutes
