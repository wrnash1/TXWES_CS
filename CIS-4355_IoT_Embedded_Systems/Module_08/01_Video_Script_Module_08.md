# Video Script: Module 08 — Sensor Integration and Data Collection

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Estimated Duration:** 20–24 minutes

**Certification Alignment:** IoT Fundamentals / Embedded Systems

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4355. I'm Professor Nash. In the last two modules we covered how microcontrollers work and how they communicate. Now we connect them to the physical world — sensors.

Sensors are the eyes and ears of any IoT system. Without them, your microcontroller is just a very expensive calculator. In this module we cover the major categories of IoT sensors, how to wire and read them using I2C and SPI bus protocols, how to calibrate sensors for real accuracy, and how to use data smoothing algorithms to turn noisy raw readings into reliable measurements.

This module is where embedded systems engineering gets genuinely interesting, because you are no longer just moving bits around — you are measuring reality.

---

## SEGMENT 2 — Sensor Types Overview (1:30–4:00)

[SHOW HARDWARE: Tray with DHT22, PIR module, LDR, BMP280, MPU6050, HC-SR04 sensors arranged side by side]

The IoT sensor landscape is enormous, but most sensors fall into a handful of categories.

**Temperature and humidity sensors** are among the most common. The DHT11 and DHT22 use a single-wire protocol and provide both temperature and humidity in one package. The DHT11 is cheap and less accurate: plus or minus 2°C temperature and 5% humidity. The DHT22 is more expensive and more accurate — plus or minus 0.5°C and 2–5% humidity — with a wider range. For higher precision or barometric pressure, the BMP280 and BME280 use I2C.

**Motion and presence sensors** include PIR (Passive Infrared) sensors that detect movement by sensing changes in infrared radiation emitted by warm bodies. PIR sensors produce a digital HIGH signal when motion is detected, with adjustable sensitivity and time-delay potentiometers.

**Light sensors** range from simple LDRs (Light-Dependent Resistors) that change resistance with illumination, to digital sensors like the BH1750 which outputs calibrated lux values over I2C.

**Pressure sensors** like the BMP280 measure atmospheric pressure to derive altitude. They are also used in weather stations, drones, and industrial process monitoring.

**Inertial measurement units** — IMUs like the MPU6050 — combine a 3-axis accelerometer and a 3-axis gyroscope in a single I2C package. They are used in robotics, drones, activity trackers, and any application requiring motion or orientation sensing.

**Distance sensors** include the HC-SR04 ultrasonic sensor, which measures distance by timing an ultrasonic pulse echo, and the VL53L0X laser Time-of-Flight sensor for higher precision over shorter ranges.

---

## SEGMENT 3 — ADC and Signal Conditioning (4:00–6:00)

Most sensors produce an analog output — a voltage that varies proportionally with the measured quantity. To read that voltage, your microcontroller uses its Analog-to-Digital Converter.

For an NTC thermistor — a resistor whose resistance drops as temperature rises — you form a voltage divider with a fixed resistor and read the midpoint voltage:

```cpp
// NTC thermistor temperature using Steinhart-Hart simplified equation
const float SERIES_R   = 10000.0;
const float NOMINAL_R  = 10000.0;
const float NOMINAL_T  = 25.0;    // degrees C at nominal resistance
const float B_COEFF    = 3950.0;

float readNTCTemp(int pin) {
  int   raw  = analogRead(pin);
  float volt = raw * (3.3f / 4095.0f);       // ESP32 12-bit
  float R    = SERIES_R / (3.3f / volt - 1.0f);

  float s = R / NOMINAL_R;
  s = logf(s);
  s /= B_COEFF;
  s += 1.0f / (NOMINAL_T + 273.15f);
  return (1.0f / s) - 273.15f;
}
```

The Steinhart-Hart simplified equation is the standard way to convert NTC thermistor resistance to temperature. A simple linear conversion from ADC count to temperature is incorrect for thermistors — do not use it.

---

## SEGMENT 4 — I2C Protocol (6:00–9:00)

[SHOW HARDWARE: ESP32 with BMP280 and MPU6050 wired on the same two-wire I2C bus, SDA and SCL labeled]

I2C — pronounced "I-squared-C" — stands for Inter-Integrated Circuit. It is a two-wire serial bus protocol invented by Philips in 1982. Despite its age, it remains the dominant bus for connecting sensors to microcontrollers.

I2C uses just two wires: SDA (Serial Data) and SCL (Serial Clock). Both are open-drain with pull-up resistors to VCC, typically 4.7 kΩ. The master — your microcontroller — initiates all communication. Slaves respond when addressed by their unique 7-bit I2C address.

Up to 112 devices can share a single I2C bus, which is I2C's greatest advantage over single-wire protocols.

```cpp
#include <Wire.h>
#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);  // ESP32: SDA=GPIO21, SCL=GPIO22

  if (!bmp.begin(0x76)) {
    Serial.println(F("BMP280 not found — check wiring and I2C address"));
    while (1);
  }
}

void loop() {
  float temp     = bmp.readTemperature();
  float pressure = bmp.readPressure() / 100.0f;  // Pa to hPa
  float altitude = bmp.readAltitude(1013.25f);

  Serial.printf("%.2f C  %.2f hPa  %.1f m\n", temp, pressure, altitude);
  delay(2000);
}
```

BMP280 wiring: VCC to 3.3V, GND to GND, SDA to GPIO 21, SCL to GPIO 22, SDO to GND (selects I2C address 0x76).

I2C has a bus speed limitation: 100 kHz standard mode, 400 kHz fast mode. For high-speed peripherals like displays and SD cards, SPI is required.

---

## SEGMENT 5 — SPI Protocol (9:00–11:30)

SPI — Serial Peripheral Interface — uses four wires and reaches speeds of 10–80 MHz, far exceeding I2C's 400 kHz.

The four SPI signals are MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), and CS (Chip Select — one pin per device). Unlike I2C which uses addresses, SPI uses dedicated chip select lines. This eliminates address conflicts but adds a GPIO pin per device.

SPI is the preferred interface for SD card modules, high-frequency ADCs, TFT displays, and RF modules.

```cpp
#include <SPI.h>
#include <SD.h>

const int CS_PIN = 5;

void setup() {
  Serial.begin(115200);
  if (!SD.begin(CS_PIN)) {
    Serial.println(F("SD card init failed"));
    return;
  }
  File f = SD.open("/data.csv", FILE_WRITE);
  if (f) {
    f.println("timestamp,temperature,humidity");
    f.close();
    Serial.println(F("Log file created on SD card"));
  }
}
```

| Feature | I2C | SPI |
|---------|-----|-----|
| Wires | 2 (SDA, SCL) | 4 (MOSI, MISO, SCK, CS) |
| Max speed | 400 kHz | 10–80 MHz |
| Multiple devices | Address-based, up to 112 | One CS pin per device |
| Pull-up resistors | Required | Not required |
| Best for | Slow sensors, many devices | Fast peripherals, displays, SD |

---

## SEGMENT 6 — Sensor Calibration (11:30–14:00)

Raw sensor readings almost always require calibration before they are useful. Calibration establishes the relationship between a sensor's output and the true physical value.

**Offset correction:** Many sensors read a constant amount above or below the true value. Measure the sensor at a known reference, then subtract the difference.

```cpp
const float TEMP_OFFSET = -1.5f;  // Measured offset vs reference thermometer

float getCalibratedTemp() {
  return dht.readTemperature() + TEMP_OFFSET;
}
```

**Two-point calibration:** Measure the sensor at two known reference points and compute a linear correction:

```cpp
const float KNOWN_LOW   = 0.0f;
const float SENSOR_LOW  = 0.3f;
const float KNOWN_HIGH  = 100.0f;
const float SENSOR_HIGH = 99.1f;

float calibrate(float raw) {
  float slope  = (KNOWN_HIGH - KNOWN_LOW) / (SENSOR_HIGH - SENSOR_LOW);
  float offset = KNOWN_LOW - slope * SENSOR_LOW;
  return slope * raw + offset;
}
```

Two-point calibration corrects both offset and gain (span) errors simultaneously. It is the minimum calibration method for any sensor going into production.

Humidity sensors drift over time and respond differently at temperature extremes. Plan to recalibrate them every 6–12 months against a known reference.

---

## SEGMENT 7 — Data Smoothing Algorithms (14:00–17:30)

Even a well-calibrated sensor produces noisy readings. Electrical noise, physical vibration, and quantization error all contribute. Data smoothing algorithms reduce noise without significantly distorting the underlying signal.

**Simple Moving Average:** Average the last N readings. Easy to implement and effective for slowly varying signals. Larger N gives more noise rejection but slower response to real changes.

```cpp
const uint8_t WINDOW = 8;
float         buf[WINDOW];
uint8_t       idx = 0;
float         runSum = 0.0f;

float smoothedRead(int pin) {
  float newest = analogRead(pin) * (3.3f / 4095.0f);
  runSum -= buf[idx];
  buf[idx] = newest;
  runSum += newest;
  idx = (idx + 1) % WINDOW;
  return runSum / WINDOW;
}
```

**Exponential Moving Average (EMA):** Blends each new reading with the previous average using a smoothing factor alpha between 0 and 1. EMA requires only one stored value — ideal for memory-constrained devices.

```cpp
float ema   = 0.0f;
const float ALPHA = 0.1f;  // 0 = maximum smoothing, 1 = no smoothing

float emaUpdate(float newValue) {
  ema = ALPHA * newValue + (1.0f - ALPHA) * ema;
  return ema;
}
```

**Median filter:** Take N readings and return the middle value. Excellent for rejecting impulse noise (spikes) that corrupt moving averages. Costs more CPU time due to sorting.

```cpp
int cmpFloat(const void* a, const void* b) {
  return (*(float*)a > *(float*)b) ? 1 : -1;
}

float medianFilter(int pin, uint8_t n) {
  float s[n];
  for (uint8_t i = 0; i < n; i++) {
    s[i] = analogRead(pin) * (3.3f / 4095.0f);
    delayMicroseconds(100);
  }
  qsort(s, n, sizeof(float), cmpFloat);
  return s[n / 2];
}
```

EMA is the right default for most IoT sensors — low memory, fast, configurable. Use median filter when impulse spikes are the dominant noise source.

---

## SEGMENT 8 — Multi-Sensor Data Logger (17:30–20:00)

[SHOW HARDWARE: ESP32 with BMP280 on I2C, DHT22 on GPIO 4, LDR on GPIO 34 — all on the same breadboard]

Here is all three concepts together — I2C sensor, single-wire sensor, and analog ADC — publishing JSON to Serial:

```cpp
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <DHT.h>

Adafruit_BMP280 bmp;
DHT dht(4, DHT22);

const int LDR_PIN  = 34;
float     ema_lux  = 0.0f;
const float ALPHA  = 0.15f;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  dht.begin();
  bmp.begin(0x76);
}

void loop() {
  float pressure = bmp.readPressure() / 100.0f;
  float bmpTemp  = bmp.readTemperature();
  float dhtTemp  = dht.readTemperature();
  float humidity = dht.readHumidity();
  float rawLux   = analogRead(LDR_PIN) * (3.3f / 4095.0f);
  ema_lux = ALPHA * rawLux + (1.0f - ALPHA) * ema_lux;

  Serial.printf(
    "{\"bmp_c\":%.2f,\"hpa\":%.1f,\"dht_c\":%.1f,\"rh\":%.1f,\"lux_v\":%.3f}\n",
    bmpTemp, pressure, dhtTemp, humidity, ema_lux
  );
  delay(5000);
}
```

Each sensor uses a different physical interface — I2C, proprietary single-wire, and analog ADC — all managed by the same microcontroller on the same board.

---

## SEGMENT 9 — Wrap-Up and Preview (20:00–22:00)

Let's recap. We surveyed the major IoT sensor categories — temperature, humidity, motion, light, pressure, and IMU. We covered ADC signal conditioning including the Steinhart-Hart equation for thermistors. We compared I2C and SPI bus protocols and identified when each is appropriate. We applied two-point sensor calibration to correct offset and gain errors. And we implemented three smoothing algorithms — moving average, EMA, and median filter — to tame noisy ADC readings.

In Module 09 we move to wireless networking: Wi-Fi, Bluetooth BLE, Zigbee, Z-Wave, LoRaWAN, and cellular IoT. You will program the ESP32's built-in Wi-Fi and BLE radios and understand the trade-offs between different wireless standards for IoT applications.

See you there.

---

## PRODUCTION NOTES

- B-roll: I2C bus on oscilloscope showing SDA/SCL waveforms; BMP280 chip close-up; LDR in light vs darkness
- Demo: Arduino Serial Plotter showing raw ADC vs EMA smoothed value side-by-side
- Demo: Serial Monitor output of multi-sensor logger updating every 5 seconds
- Closed captions: verify I2C, SPI, MOSI, MISO, NTC, Steinhart-Hart, EMA, BMP280, DHT22, LDR
- Run time target: 21 minutes
