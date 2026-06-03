# Lab: Module 07 — IoT Communication Protocols

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Points:** 100

---

## Lab Overview

In this lab you will set up a local MQTT broker, publish sensor data from an ESP32, and subscribe to that data from a Python client running on your laptop. You will then modify the QoS level and observe the behavioral difference. Finally, you will add a Last Will and Testament message to detect simulated device failure.

**Estimated time:** 2–3 hours

**Hardware required:**

- ESP32 DevKit V1
- USB cable
- DHT11 or DHT22 temperature/humidity sensor
- 10 kΩ pull-up resistor (if using DHT11 bare sensor; not needed for DHT11 breakout module)
- Breadboard and jumper wires

**Software required:**

- Arduino IDE with ESP32 board support
- PubSubClient library (install via Arduino Library Manager)
- DHT sensor library by Adafruit (install via Arduino Library Manager)
- Python 3.x on your laptop
- `paho-mqtt` Python library (`pip install paho-mqtt`)
- Mosquitto MQTT broker (Windows: download from mosquitto.org; Linux/Mac: `sudo apt install mosquitto` or `brew install mosquitto`)

---

## Circuit Wiring

**DHT11/DHT22 breakout module (3-pin version):**

- VCC pin → 3.3V rail
- GND pin → GND rail
- DATA pin → GPIO 4 on ESP32

**DHT11/DHT22 bare sensor (4-pin):**

- Pin 1 (VCC) → 3.3V rail
- Pin 2 (DATA) → GPIO 4 on ESP32, with 10 kΩ resistor from DATA to 3.3V
- Pin 3 (NC) → not connected
- Pin 4 (GND) → GND rail

---

## Part A — Broker Setup and Basic Publish (25 points)

### Part A Setup

Start Mosquitto with the default configuration on your laptop.

On Windows, from Command Prompt:

```text
cd "C:\Program Files\mosquitto"
mosquitto -v
```

On Linux/Mac:

```text
mosquitto -v
```

The `-v` flag enables verbose logging so you can see connections and messages in the terminal.

Open a second terminal and subscribe to all topics using the wildcard `#`:

```text
mosquitto_sub -h localhost -t "#" -v
```

### Part A ESP32 Code

Upload this sketch to your ESP32. Replace `YourNetwork` and `YourPassword` with your actual Wi-Fi credentials. Replace the broker IP with your laptop's IP address on the same network.

```cpp
// Lab 07 Part A: MQTT Publisher with DHT sensor
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// --- Configuration ---
const char* WIFI_SSID     = "YourNetwork";
const char* WIFI_PASS     = "YourPassword";
const char* MQTT_BROKER   = "192.168.1.100";  // Your laptop IP
const int   MQTT_PORT     = 1883;
const char* CLIENT_ID     = "esp32-lab07";
const char* TOPIC_TEMP    = "lab07/esp32/temperature";
const char* TOPIC_HUMID   = "lab07/esp32/humidity";
const char* TOPIC_STATUS  = "lab07/esp32/status";

#define DHTPIN  4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

WiFiClient   wifiClient;
PubSubClient mqtt(wifiClient);

void connectWifi() {
  Serial.printf("Connecting to %s", WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.printf("\nConnected. IP: %s\n", WiFi.localIP().toString().c_str());
}

void connectMqtt() {
  while (!mqtt.connected()) {
    Serial.print("Connecting to MQTT broker...");
    if (mqtt.connect(CLIENT_ID)) {
      Serial.println("connected.");
      mqtt.publish(TOPIC_STATUS, "online", true);  // retained
    } else {
      Serial.printf("failed (rc=%d), retrying in 5s\n", mqtt.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectWifi();
  mqtt.setServer(MQTT_BROKER, MQTT_PORT);
  connectMqtt();
}

void loop() {
  if (!mqtt.connected()) connectMqtt();
  mqtt.loop();

  float temp  = dht.readTemperature();
  float humid = dht.readHumidity();

  if (isnan(temp) || isnan(humid)) {
    Serial.println("DHT read failed — check wiring");
    delay(2000);
    return;
  }

  char buf[16];

  snprintf(buf, sizeof(buf), "%.1f", temp);
  mqtt.publish(TOPIC_TEMP, buf);
  Serial.printf("Published temp: %s\n", buf);

  snprintf(buf, sizeof(buf), "%.1f", humid);
  mqtt.publish(TOPIC_HUMID, buf);
  Serial.printf("Published humid: %s\n", buf);

  delay(10000);  // publish every 10 seconds
}
```

### Part A Expected Output

In the mosquitto_sub terminal on your laptop you should see:

```text
lab07/esp32/status online
lab07/esp32/temperature 23.5
lab07/esp32/humidity 61.0
lab07/esp32/temperature 23.6
lab07/esp32/humidity 61.0
```

### Part A Deliverables

- Screenshot of mosquitto_sub terminal showing at least 5 temperature and humidity message pairs
- Screenshot of ESP32 Serial Monitor showing successful MQTT connection and publish confirmations

---

## Part B — Python Subscriber and JSON Payload (30 points)

### Part B Python Subscriber

Create a file called `lab07_subscriber.py` on your laptop:

```python
# Lab 07 Part B: MQTT Python subscriber with JSON logging
import paho.mqtt.client as mqtt
import json
import datetime

BROKER  = "localhost"
PORT    = 1883
TOPIC   = "lab07/#"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to broker (rc={rc})")
    client.subscribe(TOPIC)
    print(f"Subscribed to: {TOPIC}")

def on_message(client, userdata, msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(client_id="python-lab07")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
```

Run it with `python lab07_subscriber.py`.

### Part B JSON Payload Modification

Modify the ESP32 sketch to publish a JSON payload instead of a bare value. Replace the publish section in `loop()`:

```cpp
// Replace the two snprintf/publish calls with this JSON version
char jsonBuf[80];
snprintf(jsonBuf, sizeof(jsonBuf),
  "{\"device\":\"esp32-lab07\",\"temp\":%.1f,\"humid\":%.1f}",
  temp, humid);
mqtt.publish("lab07/esp32/reading", jsonBuf);
Serial.printf("Published: %s\n", jsonBuf);
```

Update the Python subscriber to parse the JSON:

```python
def on_message(client, userdata, msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    if msg.topic == "lab07/esp32/reading":
        data = json.loads(msg.payload.decode())
        print(f"[{ts}] Device: {data['device']}, "
              f"Temp: {data['temp']}°C, Humid: {data['humid']}%")
    else:
        print(f"[{ts}] {msg.topic}: {msg.payload.decode()}")
```

### Part B Expected Output

```text
Connected to broker (rc=0)
Subscribed to: lab07/#
[14:23:10] Device: esp32-lab07, Temp: 23.5°C, Humid: 61.0%
[14:23:20] Device: esp32-lab07, Temp: 23.6°C, Humid: 61.0%
[14:23:30] Device: esp32-lab07, Temp: 23.5°C, Humid: 61.2%
```

### Part B Deliverables

- Screenshot of Python subscriber terminal showing parsed JSON output (at least 5 readings)
- The modified ESP32 `.ino` file with JSON payload

---

## Part C — Last Will and Testament (20 points)

### Part C LWT Configuration

Add a Last Will and Testament to the ESP32 sketch so other clients detect when the device goes offline.

Modify the `connectMqtt()` function:

```cpp
void connectMqtt() {
  // Set LWT BEFORE calling connect()
  mqtt.setWill(TOPIC_STATUS, "offline", true, 1);

  while (!mqtt.connected()) {
    Serial.print("Connecting to MQTT broker...");
    if (mqtt.connect(CLIENT_ID)) {
      Serial.println("connected.");
      mqtt.publish(TOPIC_STATUS, "online", true);
    } else {
      Serial.printf("failed (rc=%d), retrying in 5s\n", mqtt.state());
      delay(5000);
    }
  }
}
```

### Part C Test Procedure

1. Upload the modified sketch and confirm `lab07/esp32/status online` appears in the subscriber
2. While the ESP32 is running, physically unplug it from USB (do not do a clean shutdown)
3. Wait approximately 10–30 seconds for the broker to detect the ungraceful disconnect
4. Observe that `lab07/esp32/status offline` appears in the subscriber terminal

### Part C Expected Output

```text
[14:25:00] lab07/esp32/status: online
[14:25:00] Device: esp32-lab07, Temp: 23.5°C, Humid: 61.0%
[14:25:10] Device: esp32-lab07, Temp: 23.5°C, Humid: 61.0%
--- (ESP32 unplugged here) ---
[14:25:45] lab07/esp32/status: offline
```

### Part C Deliverables

- Screenshot showing the `offline` LWT message appearing after unplug
- Written answer (2–3 sentences): Why does the LWT message not appear immediately when the ESP32 is unplugged? What determines the delay?

---

## Part D — QoS Comparison Observation (25 points)

### Part D Setup

Modify the Python subscriber to log timestamps with millisecond precision and add a counter to detect missed messages:

```python
import paho.mqtt.client as mqtt
import datetime
import time

BROKER = "localhost"
PORT   = 1883

msg_count = 0

def on_message(client, userdata, msg):
    global msg_count
    msg_count += 1
    ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{ts}] #{msg_count} QoS={msg.qos} {msg.topic}: "
          f"{msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("lab07/esp32/reading", qos=0)
client.loop_forever()
```

Run two publish tests, each for 2 minutes:

**Test 1:** Publish with QoS 0 (default in PubSubClient). Count messages received.

**Test 2:** Intentionally introduce packet loss by temporarily disconnecting and reconnecting Wi-Fi on the ESP32 during publishing. Observe whether QoS 0 messages are lost.

### Part D Written Analysis

Answer these four questions (3–4 sentences each):

1. How many messages did you publish in each test versus how many the subscriber received?
2. Did you observe any duplicate messages? Under what QoS level would you expect duplicates?
3. For a home temperature monitoring app that checks readings every 10 minutes, which QoS level is most appropriate? Justify using the QoS definitions from the reading.
4. For a medical device that sends a "patient alarm" MQTT message when a sensor threshold is exceeded, which QoS level is required? Why is QoS 1 insufficient here?

### Part D Deliverables

- Screenshots of subscriber output for both QoS tests
- Written analysis answering all four questions

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| **Part A** — Broker running, ESP32 connects and publishes | 10 |
| **Part A** — mosquitto_sub screenshot with 5+ message pairs | 10 |
| **Part A** — Serial Monitor screenshot showing connection | 5 |
| **Part B** — JSON payload correctly formatted and published | 10 |
| **Part B** — Python subscriber parses and displays JSON fields | 10 |
| **Part B** — 5+ parsed readings in screenshot | 10 |
| **Part C** — LWT configured before connect() call | 5 |
| **Part C** — offline message appears after unplug | 10 |
| **Part C** — Written explanation of LWT delay | 5 |
| **Part D** — Both QoS test screenshots provided | 10 |
| **Part D** — Written analysis answers all four questions | 15 |
| **TOTAL** | **100** |

---

## Troubleshooting Tips

**Mosquitto refuses connections:** On Windows, the default Mosquitto config may only listen on localhost. Create a `mosquitto.conf` file with `listener 1883` and `allow_anonymous true`, then run `mosquitto -c mosquitto.conf -v`.

**ESP32 cannot find broker:** Confirm both devices are on the same Wi-Fi network. Use `ipconfig` (Windows) or `ifconfig` (Mac/Linux) to find your laptop IP.

**DHT reads NaN:** Check VCC and GND connections. Verify pin number matches `DHTPIN` define. DHT11 needs a 10 kΩ pull-up on DATA pin if using a bare sensor (not a breakout module).

**LWT delay is very long:** The broker detects ungraceful disconnect after the Keep-Alive timer expires (default 60 seconds) plus some broker-side processing time.

**Python not receiving messages:** Confirm `client.subscribe()` is called inside `on_connect`, not in the main script body, to ensure re-subscription after reconnect.
