# Lab: Module 08 — Sensor Integration and Data Collection

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Points:** 100

---

## Lab Overview

In this lab you will connect multiple sensors to an ESP32, read them using different interface protocols (I2C, single-wire, and analog ADC), apply software calibration, and implement data smoothing. You will log the results to the Serial Monitor and demonstrate the difference between raw and smoothed readings.

**Estimated time:** 2–3 hours

**Hardware required:**

- ESP32 DevKit V1
- BMP280 pressure/temperature module (I2C)
- DHT22 temperature/humidity module
- LDR (light-dependent resistor) — bare component or breakout
- 10 kΩ resistor (for LDR voltage divider if using bare LDR)
- Breadboard and jumper wires
- USB cable

**Libraries required (install via Arduino Library Manager):**

- Adafruit BMP280 Library
- Adafruit Unified Sensor
- DHT sensor library by Adafruit

---

## Circuit Wiring

**BMP280 (I2C):**

- VCC → 3.3V rail
- GND → GND rail
- SDA → GPIO 21
- SCL → GPIO 22
- SDO → GND (sets I2C address to 0x76)
- CSB → 3.3V (selects I2C mode)

**DHT22 (single-wire):**

- VCC → 3.3V rail
- GND → GND rail
- DATA → GPIO 4

**LDR voltage divider:**

- One LDR leg → 3.3V rail
- Other LDR leg → GPIO 34 AND one end of 10 kΩ resistor
- Other end of 10 kΩ resistor → GND rail

The LDR and fixed resistor form a voltage divider. As light increases, LDR resistance decreases, GPIO 34 voltage increases. In darkness, LDR resistance is high and GPIO 34 is near 0V.

---

## Part A — I2C Scanner and BMP280 (25 points)

### Part A Objective

Run the I2C scanner to confirm BMP280 is detected, then read temperature, pressure, and calculated altitude.

### Part A Code

```cpp
// Part A: I2C Scanner + BMP280 readings
#include <Wire.h>
#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp;

void scanI2C() {
  Serial.println(F("--- I2C Bus Scan ---"));
  int found = 0;
  for (uint8_t addr = 8; addr < 120; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.printf("  Device at 0x%02X\n", addr);
      found++;
    }
  }
  Serial.printf("Scan complete: %d device(s) found\n\n", found);
}

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  scanI2C();

  if (!bmp.begin(0x76)) {
    Serial.println(F("BMP280 not found. Check wiring."));
    while (1);
  }

  // Configure for weather-station mode (low noise, 16x oversampling)
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,
                  Adafruit_BMP280::SAMPLING_X16,
                  Adafruit_BMP280::SAMPLING_X16,
                  Adafruit_BMP280::FILTER_X16,
                  Adafruit_BMP280::STANDBY_MS_500);

  Serial.println(F("BMP280 ready"));
  Serial.println(F("Temp(C) | Pressure(hPa) | Altitude(m)"));
  Serial.println(F("--------|--------------|------------"));
}

void loop() {
  float temp     = bmp.readTemperature();
  float pressure = bmp.readPressure() / 100.0f;
  float altitude = bmp.readAltitude(1013.25f);

  Serial.printf("%.2f\t| %.2f\t\t| %.1f\n", temp, pressure, altitude);
  delay(2000);
}
```

### Part A Expected Output

```text
--- I2C Bus Scan ---
  Device at 0x76
Scan complete: 1 device(s) found

BMP280 ready
Temp(C) | Pressure(hPa) | Altitude(m)
--------|--------------|------------
24.35   | 1009.87      | 27.3
24.36   | 1009.85      | 27.5
24.36   | 1009.86      | 27.4
```

### Part A Deliverables

- Screenshot of I2C scan showing BMP280 at 0x76
- Screenshot of 6+ BMP280 readings in the table format
- Written answer (1–2 sentences): What changes in the altitude reading when you press your hand over the BMP280 module? Why?

---

## Part B — DHT22 and Calibration (25 points)

### Part B Objective

Read the DHT22 and apply a two-point temperature calibration. Compare raw vs calibrated readings.

### Part B Code

```cpp
// Part B: DHT22 with two-point calibration
#include <DHT.h>

DHT dht(4, DHT22);

// --- Two-point calibration constants ---
// These are placeholder values — replace with your own measurements
// Compare DHT22 readings against the BMP280 from Part A as your reference
const float SENSOR_LOW  = 20.0f;  // DHT22 reading at your low reference point
const float KNOWN_LOW   = 20.5f;  // Reference (BMP280) reading at same condition
const float SENSOR_HIGH = 30.0f;  // DHT22 reading at high reference point
const float KNOWN_HIGH  = 30.8f;  // Reference (BMP280) reading at same condition

float calSlope  = 1.0f;
float calOffset = 0.0f;

void computeCalibration() {
  calSlope  = (KNOWN_HIGH - KNOWN_LOW) / (SENSOR_HIGH - SENSOR_LOW);
  calOffset = KNOWN_LOW - calSlope * SENSOR_LOW;
  Serial.printf("Calibration: slope=%.4f, offset=%.4f\n",
                calSlope, calOffset);
}

float applyCalibration(float raw) {
  return calSlope * raw + calOffset;
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  computeCalibration();
  Serial.println(F("Raw_C | Calibrated_C | Humidity_pct"));
  Serial.println(F("------|-------------|-------------"));
}

void loop() {
  float rawTemp  = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(rawTemp) || isnan(humidity)) {
    Serial.println(F("DHT read error — waiting 2s"));
    delay(2000);
    return;
  }

  float calTemp = applyCalibration(rawTemp);
  Serial.printf("%.2f  | %.2f\t\t| %.1f\n", rawTemp, calTemp, humidity);
  delay(3000);
}
```

### Part B Expected Output

```text
Calibration: slope=1.0267, offset=0.0133
Raw_C | Calibrated_C | Humidity_pct
------|-------------|-------------
24.50  | 25.17       | 58.3
24.50  | 25.17       | 58.4
24.60  | 25.27       | 58.2
```

### Part B Deliverables

- Screenshot of Serial Monitor showing raw and calibrated columns (at least 8 readings)
- The calibration constant values you used (slope, offset) and a brief explanation (2–3 sentences) of how you determined your reference readings

---

## Part C — LDR Smoothing Comparison (25 points)

### Part C Objective

Read the LDR analog input and compare three smoothing methods: no smoothing, EMA, and median filter. Display all three columns simultaneously.

### Part C Code

```cpp
// Part C: LDR raw vs EMA vs median filter comparison
const int LDR_PIN = 34;

// EMA
float ema   = 0.0f;
const float ALPHA = 0.1f;

// Circular buffer for moving average
const uint8_t WIN = 8;
float buf[WIN];
uint8_t bufIdx = 0;
float bufSum = 0.0f;

// Median filter helper
int cmpf(const void* a, const void* b) {
  return (*(float*)a > *(float*)b) ? 1 : -1;
}

float median5(int pin) {
  float s[5];
  for (uint8_t i = 0; i < 5; i++) {
    s[i] = analogRead(pin) * (3.3f / 4095.0f);
    delayMicroseconds(200);
  }
  qsort(s, 5, sizeof(float), cmpf);
  return s[2];
}

void setup() {
  Serial.begin(115200);
  // Pre-fill EMA and buffer with first reading
  float first = analogRead(LDR_PIN) * (3.3f / 4095.0f);
  ema = first;
  for (uint8_t i = 0; i < WIN; i++) buf[i] = first;
  bufSum = first * WIN;

  Serial.println(F("Raw_V | EMA_V | Median_V"));
  Serial.println(F("------|-------|----------"));
}

void loop() {
  float raw = analogRead(LDR_PIN) * (3.3f / 4095.0f);

  // Update EMA
  ema = ALPHA * raw + (1.0f - ALPHA) * ema;

  // Update moving average buffer
  bufSum -= buf[bufIdx];
  buf[bufIdx] = raw;
  bufSum += raw;
  bufIdx = (bufIdx + 1) % WIN;
  float mavg = bufSum / WIN;

  // Median of 5 samples
  float med = median5(LDR_PIN);

  Serial.printf("%.3f | %.3f | %.3f\n", raw, ema, med);
  delay(200);
}
```

### Part C Test Procedure

1. Run the sketch in normal room light. Observe baseline variation in all three columns.
2. Quickly cover and uncover the LDR with your hand to create fast transitions. Observe how each algorithm responds.
3. Tap the breadboard sharply once to create an impulse vibration spike. Observe whether the spike appears in each column.

### Part C Deliverables

- Screenshot showing at least 20 rows of three-column output
- Written analysis (3–5 sentences): How did the three algorithms behave differently during the hand-cover test? Which was fastest to respond? Which was slowest? How did each handle the tap-spike impulse?

---

## Part D — Combined Multi-Sensor Logger (25 points)

### Part D Objective

Combine Parts A, B, and C into a single sketch that reads all three sensors every 5 seconds and outputs structured JSON to the Serial Monitor.

### Part D Code

```cpp
// Part D: Multi-sensor JSON logger — BMP280 + DHT22 + LDR
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <DHT.h>

Adafruit_BMP280 bmp;
DHT dht(4, DHT22);

const int LDR_PIN  = 34;
float     ema_lux  = 0.0f;
const float ALPHA  = 0.15f;

// Calibration from Part B (update with your values)
const float CAL_SLOPE  = 1.0267f;
const float CAL_OFFSET = 0.0133f;

uint32_t seqNum = 0;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  dht.begin();

  if (!bmp.begin(0x76)) {
    Serial.println(F("{\"error\":\"BMP280 not found\"}"));
    while (1);
  }

  float first = analogRead(LDR_PIN) * (3.3f / 4095.0f);
  ema_lux = first;

  Serial.println(F("Multi-sensor logger ready. Output: JSON per line."));
}

void loop() {
  float bmpTemp  = bmp.readTemperature();
  float pressure = bmp.readPressure() / 100.0f;
  float altitude = bmp.readAltitude(1013.25f);
  float dhtRaw   = dht.readTemperature();
  float dhtCal   = CAL_SLOPE * dhtRaw + CAL_OFFSET;
  float humidity = dht.readHumidity();
  float rawLux   = analogRead(LDR_PIN) * (3.3f / 4095.0f);
  ema_lux = ALPHA * rawLux + (1.0f - ALPHA) * ema_lux;

  Serial.printf(
    "{\"seq\":%lu,\"bmp_c\":%.2f,\"hpa\":%.2f,\"alt_m\":%.1f,"
    "\"dht_raw\":%.2f,\"dht_cal\":%.2f,\"rh\":%.1f,\"lux_v\":%.3f}\n",
    seqNum++, bmpTemp, pressure, altitude,
    dhtRaw, dhtCal, humidity, ema_lux
  );

  delay(5000);
}
```

### Part D Expected Output

```text
Multi-sensor logger ready. Output: JSON per line.
{"seq":0,"bmp_c":24.35,"hpa":1009.87,"alt_m":27.3,"dht_raw":24.50,"dht_cal":25.17,"rh":58.3,"lux_v":1.243}
{"seq":1,"bmp_c":24.36,"hpa":1009.85,"alt_m":27.5,"dht_raw":24.50,"dht_cal":25.17,"rh":58.4,"lux_v":1.251}
```

### Part D Deliverables

- Screenshot of Serial Monitor showing at least 6 complete JSON lines
- Answer this question (2–3 sentences): The BMP280 temperature and DHT22 calibrated temperature may not match exactly even after calibration. What physical factors might cause a real difference between the two readings, beyond sensor accuracy?

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| **Part A** — I2C scan shows BMP280 at 0x76 | 5 |
| **Part A** — BMP280 readings in table format | 10 |
| **Part A** — Written altitude-pressure observation | 10 |
| **Part B** — Two-point calibration computed and applied | 10 |
| **Part B** — Raw and calibrated columns both displayed | 10 |
| **Part B** — Calibration constants explained | 5 |
| **Part C** — All three smoothing algorithms implemented | 10 |
| **Part C** — 20+ row screenshot showing all columns | 5 |
| **Part C** — Written algorithm comparison analysis | 10 |
| **Part D** — Combined sketch produces valid JSON | 10 |
| **Part D** — 6+ complete JSON lines in screenshot | 10 |
| **Part D** — Temperature discrepancy explanation | 5 |
| **TOTAL** | **100** |

---

## Troubleshooting Tips

**BMP280 not found at 0x76:** Check that SDO is tied to GND. If tied to VCC, address is 0x77. Use the I2C scanner to find the actual address. Verify SDA=GPIO21 and SCL=GPIO22.

**DHT22 reads NaN:** Wait at least 2 seconds between reads. Confirm pin matches DHTPIN define. Check VCC connection — DHT22 requires stable 3.3V.

**LDR always reads near 0V:** Verify the voltage divider — LDR and 10 kΩ resistor must be in series between 3.3V and GND. GPIO 34 connects to the midpoint. If both ends go to the same rail, you get 0V or 3.3V, not a varying voltage.

**LDR always reads near 3.3V:** The LDR and resistor may be swapped. Swap which one connects to 3.3V vs GND.

**Median function crashes:** Ensure the variable-length array in `median5()` is supported by your ESP32 Arduino core version. If not, replace with a fixed-size global array `float medBuf[5]`.

---

## Part 9 — Challenge Exercise

### Challenge 1: MQTT Telemetry Publisher for Multi-Sensor Logger

Extend the Part D combined sketch to publish the JSON sensor readings over MQTT instead of (or in addition to) the Serial Monitor.

1. Add the `PubSubClient` library to your sketch. Configure the ESP32 to connect to your local Mosquitto broker (from Module 07 Lab) on port 1883. Use the topic `lab08/esp32/sensors` for the JSON payload already produced in Part D. Publish every 5 seconds matching the existing `delay(5000)` interval.

2. Add a Last Will and Testament before calling `mqtt.connect()` so that `lab08/esp32/status` publishes `"offline"` (retained, QoS 1) on ungraceful disconnect. Publish `"online"` (retained) immediately after a successful connection.

3. On your laptop, run this Python subscriber to log the data to a CSV file:

```python
# lab08_logger.py — subscribe to lab08/# and write CSV
import paho.mqtt.client as mqtt
import csv, datetime, json, sys

BROKER = "localhost"
OUTFILE = "sensor_log.csv"

fieldnames = ["timestamp", "seq", "bmp_c", "hpa", "alt_m",
              "dht_raw", "dht_cal", "rh", "lux_v"]

with open(OUTFILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    def on_message(client, userdata, msg):
        if msg.topic == "lab08/esp32/sensors":
            data = json.loads(msg.payload.decode())
            data["timestamp"] = datetime.datetime.now().isoformat()
            writer.writerow({k: data.get(k, "") for k in fieldnames})
            f.flush()
            print(data)

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, 1883)
    client.subscribe("lab08/#")
    print(f"Logging to {OUTFILE} — Ctrl+C to stop")
    client.loop_forever()
```

4. Run the logger for at least 2 minutes (24+ readings). Open `sensor_log.csv` in a spreadsheet or with Python `pandas` and plot the `dht_cal` and `bmp_c` columns together. Describe in 2–3 sentences whether the two temperature sensors track each other closely and what physical lag you observe in the DHT22 calibrated column versus the BMP280.

### Challenge 2: BME280 Dew Point and Comfort Index Calculation

Replace the BMP280 in your circuit with a BME280 (which adds a humidity channel) and compute derived environmental metrics.

1. Install the `Adafruit BME280 Library` and update your sketch to read `bme.readHumidity()` in addition to temperature and pressure. Confirm both sensors are on the same I2C bus (BME280 default address is 0x76 — confirm with I2C scanner).

2. Add a dew point calculation using the Magnus formula. Add this function to your sketch:

```cpp
float dewPoint(float tempC, float relHumidity) {
  // Magnus formula constants (valid 0-60°C)
  const float a = 17.27f;
  const float b = 237.7f;
  float gamma = (a * tempC / (b + tempC)) + log(relHumidity / 100.0f);
  return (b * gamma) / (a - gamma);
}
```

Call it with your calibrated BME280 temperature and humidity. Add `"dew_c"` to the JSON output string.

3. Add a simple comfort index to the JSON output. Define comfort zones:

```text
Dew point < 10°C  → "dry"
10–16°C           → "comfortable"
16–21°C           → "humid"
> 21°C            → "oppressive"
```

Add a `"comfort"` string field to the JSON payload. Verify in the Serial Monitor that the comfort label changes when you breathe on the sensor (briefly raising local humidity).

4. Calculate how many bytes per day are saved by using CBOR encoding instead of the expanded JSON (which now has 9 fields including `dew_c` and `comfort`). Assume one reading every 5 seconds. Include this calculation in your written submission.

### Reflection Questions

1. In Challenge 1 you used `delay(5000)` to pace MQTT publishes. Explain why this approach blocks Wi-Fi keepalive packets and describe the `mqtt.loop()` call requirement. What is the preferred non-blocking alternative using `millis()`?

2. The Magnus formula in Challenge 2 is valid between 0°C and 60°C. What would happen if you passed a temperature of −10°C into the formula, and how would you add input validation to prevent the function from returning a physically meaningless result?
