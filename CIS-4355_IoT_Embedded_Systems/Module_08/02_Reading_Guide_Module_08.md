# Reading Guide: Module 08 — Sensor Integration and Data Collection

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Certification Target:** IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you will be able to:

1. Identify the major IoT sensor categories and select the appropriate sensor for a given measurement requirement
2. Explain ADC operation and convert raw ADC readings to engineering units
3. Describe the I2C bus protocol, address scheme, and wire configuration
4. Describe the SPI bus protocol and compare it to I2C on speed, pin count, and use cases
5. Apply two-point calibration to correct sensor offset and gain errors
6. Implement moving average, exponential moving average, and median filter algorithms in C++
7. Select the appropriate smoothing algorithm based on noise characteristics

---

## Section 1 — Sensor Categories

### 1.1 Temperature and Humidity Sensors

| Sensor | Interface | Temp Accuracy | Humidity Accuracy | Range |
|--------|-----------|--------------|-------------------|-------|
| DHT11 | Single-wire | ±2°C | ±5% RH | 0–50°C |
| DHT22 | Single-wire | ±0.5°C | ±2–5% RH | -40–80°C |
| BMP280 | I2C / SPI | ±1°C | None | -40–85°C |
| BME280 | I2C / SPI | ±1°C | ±3% RH | -40–85°C |
| DS18B20 | 1-Wire | ±0.5°C | None | -55–125°C |
| SHT31 | I2C | ±0.3°C | ±2% RH | -40–125°C |

The DHT sensors use a proprietary single-wire protocol. They require a 10 kΩ pull-up resistor on the data line when using bare sensors (not breakout modules). They cannot be read faster than once every 2 seconds.

The BME280 is preferred over the BMP280 for applications requiring both temperature/humidity and pressure, as it adds humidity sensing at minimal cost increase.

### 1.2 Motion Sensors

**PIR (Passive Infrared):** Detects changes in infrared radiation from warm bodies. Digital output — HIGH when motion detected, LOW otherwise. Adjustable sensitivity and hold-time via potentiometers. Range 3–7 meters. Supply voltage 5V (most modules level-shift output to 3.3V for ESP32 compatibility).

**Doppler Radar (RCWL-0516):** Uses microwave radar for presence detection through walls and non-metallic barriers. More expensive and power-hungry than PIR but works in darkness and detects subtle motion.

**MPU6050 (IMU):** 6-axis inertial measurement unit. Combines 3-axis accelerometer (±2g to ±16g configurable) and 3-axis gyroscope (±250 to ±2000°/s configurable). I2C interface at address 0x68 (AD0=LOW) or 0x69 (AD0=HIGH). On-board Digital Motion Processor (DMP) handles sensor fusion.

### 1.3 Light Sensors

**LDR (Light-Dependent Resistor):** Resistance decreases with increasing light. Used in a voltage divider with ADC. Inexpensive but not calibrated — output varies by part and temperature. Good for relative light detection (light vs dark).

**BH1750:** Digital ambient light sensor over I2C. Outputs calibrated lux values (0–65535 lux). Two I2C addresses: 0x23 (ADDR=LOW) and 0x5C (ADDR=HIGH). Resolution modes: 1 lux, 0.5 lux, 4 lux.

**VEML7700:** High-accuracy ambient light sensor with 0.0036 lux resolution. I2C interface. Recommended for precision light metering applications.

### 1.4 Pressure and Altitude

The BMP280 provides pressure accuracy of ±1 hPa relative. Converting pressure to altitude uses the barometric formula:

```text
altitude = 44330 × (1 - (P / P0)^(1/5.255))
```

Where P is the measured pressure and P0 is the sea-level reference pressure (standard: 1013.25 hPa). This formula gives altitude above sea level in meters.

### 1.5 Distance Sensors

**HC-SR04 Ultrasonic:** Emits a 40 kHz burst and measures echo return time. Range 2cm–400cm. Accuracy ±3mm. Operates at 5V; voltage divider needed for 3.3V microcontroller ECHO pin.

```cpp
// HC-SR04 distance measurement
const int TRIG = 5;
const int ECHO = 18;

float readDistanceCm() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long duration = pulseIn(ECHO, HIGH, 30000);  // 30ms timeout
  return duration * 0.0343f / 2.0f;
}
```

**VL53L0X (Time-of-Flight):** Laser ranging sensor over I2C. Range up to 2m. Accuracy ±3%. Not affected by target color or reflectivity. Default I2C address 0x29; address programmable per unit.

---

## Section 2 — ADC Fundamentals and Signal Conditioning

### 2.1 ADC Conversion

The ADC maps a voltage range to a digital integer:

```text
digital_value = round(V_in / V_ref × (2^n - 1))
```

Where n is the ADC resolution in bits. The inverse (converting reading to voltage):

```text
V_in = digital_value × V_ref / (2^n - 1)
```

### 2.2 ESP32 ADC Non-Linearity

The ESP32 ADC has a known non-linearity, especially near 0V and near 3.3V. For accurate measurements:

- Limit input range to 100mV–3000mV
- Use the `esp_adc_cal` library for factory calibration correction
- Average multiple readings to reduce quantization noise

### 2.3 NTC Thermistor Signal Chain

NTC (Negative Temperature Coefficient) thermistors change resistance with temperature. The standard circuit is a voltage divider:

```text
        VCC (3.3V)
          |
       [R_fixed]  (10kΩ)
          |
          +----> ADC pin
          |
       [R_NTC]   (resistance varies with temperature)
          |
         GND
```

The Steinhart-Hart simplified B-parameter equation converts resistance to temperature (in Kelvin):

```text
1/T = 1/T0 + (1/B) × ln(R/R0)
```

Where T0 = 298.15K (25°C), R0 = nominal resistance at T0, B = B-coefficient from datasheet.

---

## Section 3 — I2C Protocol

### 3.1 Electrical Characteristics

I2C uses open-drain signal lines. Neither the master nor slave drives a line HIGH — instead, pull-up resistors passively pull both lines to VCC. A device pulls the line LOW by enabling its open-drain output transistor. This allows any device to pull the bus LOW without contention.

Pull-up resistor guidelines:

| Bus Speed | Capacitance | Pull-up Resistance |
|-----------|-------------|-------------------|
| 100 kHz | < 200 pF | 4.7 kΩ |
| 400 kHz | < 100 pF | 2.2 kΩ |
| 1 MHz (Fast+) | < 50 pF | 1 kΩ |

Most I2C breakout modules include 4.7 kΩ pull-up resistors. When multiple modules are stacked on the same bus, parallel pull-ups reduce effective resistance and may cause signal integrity issues at 400 kHz.

### 3.2 I2C Transaction Structure

Every I2C transaction follows this pattern:

```text
START | ADDRESS (7 bits) | R/W (1 bit) | ACK | DATA bytes | STOP
```

The master generates START, sends the 7-bit slave address plus a read/write bit. The addressed slave acknowledges (pulls SDA LOW). Data bytes follow, each acknowledged by the receiver. The master generates STOP.

### 3.3 I2C Address Assignment

Common sensor addresses:

| Sensor | Default Address | Configurable? |
|--------|----------------|---------------|
| BMP280 | 0x76 (SDO=GND) / 0x77 (SDO=VCC) | Yes |
| BME280 | 0x76 / 0x77 | Yes |
| MPU6050 | 0x68 (AD0=GND) / 0x69 (AD0=VCC) | Yes |
| BH1750 | 0x23 / 0x5C | Yes |
| SHT31 | 0x44 / 0x45 | Yes |
| OLED SSD1306 | 0x3C / 0x3D | Yes |
| PCF8574 I/O expander | 0x20–0x27 | Yes (3 pins) |

Use the I2C scanner sketch to discover addresses on your bus:

```cpp
#include <Wire.h>

void setup() {
  Wire.begin(21, 22);
  Serial.begin(115200);
  Serial.println("I2C Scanner");

  for (uint8_t addr = 8; addr < 120; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.printf("Device found at 0x%02X\n", addr);
    }
  }
  Serial.println("Scan complete");
}

void loop() {}
```

---

## Section 4 — SPI Protocol

### 4.1 SPI Signal Definitions

| Signal | Direction | Description |
|--------|-----------|-------------|
| SCK | Master → Slave | Clock generated by master |
| MOSI | Master → Slave | Data from master to slave |
| MISO | Slave → Master | Data from slave to master |
| CS/SS | Master → Slave | Active-LOW chip select; one per device |

SPI is full duplex — data is simultaneously transmitted and received on every clock edge. This enables very high throughput for displays and storage.

### 4.2 SPI Modes

SPI has four modes defined by Clock Polarity (CPOL) and Clock Phase (CPHA):

| Mode | CPOL | CPHA | Clock idle | Data sampled on |
|------|------|------|-----------|-----------------|
| 0 | 0 | 0 | LOW | Rising edge |
| 1 | 0 | 1 | LOW | Falling edge |
| 2 | 1 | 0 | HIGH | Falling edge |
| 3 | 1 | 1 | HIGH | Rising edge |

Most sensors use Mode 0 or Mode 3. Always check the datasheet — using the wrong mode produces garbage data.

### 4.3 Multiple SPI Devices

```cpp
// Multiple SPI devices on same bus, different CS pins
const int CS_SD   = 5;
const int CS_DISP = 17;

void setup() {
  SPI.begin();
  pinMode(CS_SD,   OUTPUT);
  pinMode(CS_DISP, OUTPUT);
  digitalWrite(CS_SD,   HIGH);  // Deselect both
  digitalWrite(CS_DISP, HIGH);

  SD.begin(CS_SD);
  // tft.begin(CS_DISP);
}
```

---

## Section 5 — Sensor Calibration

### 5.1 Types of Sensor Error

| Error Type | Description | Correction |
|------------|-------------|------------|
| Offset error | Reading is consistently X units above or below true value | Subtract constant |
| Gain error | Reading is correct at one point but drifts at others | Multiply by scale factor |
| Linearity error | Response curve is non-linear | Lookup table or polynomial |
| Drift | Calibration shifts over time (temperature, aging) | Periodic recalibration |
| Hysteresis | Reading differs depending on direction of change | Average ascending and descending sweeps |

### 5.2 Two-Point Calibration Procedure

1. Obtain two reference measurements (R_low, R_high) from a traceable reference instrument
2. Record the sensor output at the same two conditions (S_low, S_high)
3. Compute the linear correction: `slope = (R_high - R_low) / (S_high - S_low)` and `offset = R_low - slope * S_low`
4. Apply to every reading: `corrected = slope * raw + offset`

### 5.3 Storing Calibration in NVS (ESP32)

```cpp
#include <Preferences.h>

Preferences prefs;

void saveCalibration(float slope, float offset) {
  prefs.begin("cal", false);
  prefs.putFloat("slope",  slope);
  prefs.putFloat("offset", offset);
  prefs.end();
}

float loadSlope() {
  prefs.begin("cal", true);
  float v = prefs.getFloat("slope", 1.0f);  // default slope = 1.0
  prefs.end();
  return v;
}
```

---

## Section 6 — Data Smoothing Algorithms

### 6.1 Algorithm Comparison

| Algorithm | Memory | CPU | Noise rejection | Spike rejection | Lag |
|-----------|--------|-----|----------------|-----------------|-----|
| Simple Moving Average | N floats | Low | Good | Poor | N/2 samples |
| Exponential Moving Average | 1 float | Minimal | Good | Poor | Depends on alpha |
| Median filter | N floats + sort | Medium | Moderate | Excellent | N/2 samples |
| Kalman filter | 4+ floats | High | Excellent | Good | Minimal |

### 6.2 Choosing Alpha for EMA

The EMA time constant (in samples) is approximately `1/alpha`. To achieve the equivalent noise rejection of an N-sample moving average:

```text
alpha ≈ 2 / (N + 1)
```

For an 8-sample equivalent: alpha = 2/9 ≈ 0.22. For a 16-sample equivalent: alpha = 2/17 ≈ 0.12.

### 6.3 Outlier Rejection

Before smoothing, reject obvious outliers using a sigma-based test:

```cpp
bool isOutlier(float value, float mean, float stddev, float threshold) {
  return fabsf(value - mean) > threshold * stddev;
}
```

A threshold of 3.0 (three-sigma) rejects values more than three standard deviations from the running mean, which eliminates over 99.7% of true outliers while retaining valid readings.

---

## Key Terms

| Term | Definition |
|------|------------|
| ADC | Analog-to-Digital Converter — converts voltage to digital integer |
| NTC | Negative Temperature Coefficient thermistor — resistance decreases with temperature |
| Steinhart-Hart | Equation converting NTC thermistor resistance to temperature |
| I2C | Two-wire serial bus protocol (SDA + SCL) with device addressing |
| SPI | Four-wire high-speed serial bus (MOSI, MISO, SCK, CS) |
| MOSI | Master Out Slave In — SPI data line from master to slave |
| MISO | Master In Slave Out — SPI data line from slave to master |
| Calibration | Process of correcting systematic sensor error using reference measurements |
| EMA | Exponential Moving Average — weighted blend of current and previous value |
| Median filter | Returns middle value of N sorted samples — rejects impulse noise |
| PIR | Passive Infrared sensor — detects body heat changes for motion sensing |
| LDR | Light-Dependent Resistor — resistance inversely proportional to illumination |

---

## Review Questions

1. Why does the DHT22 require a minimum 2-second interval between readings?
2. An LDR reads 2048 out of 4095 on an ESP32 ADC with 3.3V reference. What voltage is at the ADC pin?
3. Explain why two BMP280 sensors can coexist on the same I2C bus when a third BMP280 cannot.
4. A sensor reads 23.5°C when a reference thermometer reads 24.8°C, and reads 73.2°C when the reference reads 75.0°C. Calculate the two-point calibration slope and offset.
5. Why do most I2C breakout modules include 4.7 kΩ pull-up resistors, and what problem can occur if three such modules are stacked on the same bus?
6. An accelerometer reading shows random spikes of ±5g superimposed on a steady 1g reading. Which smoothing algorithm is most appropriate and why?
7. What is the effect of setting EMA alpha to 0.01 versus 0.9? Which provides faster response to a sudden real change in the measured value?
8. Why should you limit ESP32 ADC input to the range 100mV–3000mV rather than the full 0–3.3V range?
