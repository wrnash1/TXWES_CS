# Reading Guide: Module 07 - Sensor Integration and Data Collection
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 07 – Sensor Integration and Data Collection**! This module covers how IoT systems acquire real-world data through sensors, how raw analog and digital signals are conditioned and converted for processing, and how collected data is transmitted reliably to edge nodes or cloud backends. Sensor selection, signal conditioning, and sampling strategy directly determine data quality — and poor data quality at the collection layer propagates errors throughout the entire IoT pipeline.

You will learn how temperature, humidity, pressure, motion, and gas sensors interface with microcontrollers through I2C, SPI, and analog GPIO pins, how ADC resolution and sampling rate govern measurement accuracy, and how sensor fusion combines multiple data streams into higher-confidence readings. Security considerations — including sensor data integrity, spoofing attacks on analog inputs, and secure transmission of collected readings — are woven throughout.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Sensor Transducer**: A device that converts a physical quantity (temperature, pressure, light, acceleration) into an electrical signal — typically a voltage or current — that a microcontroller can read. Transducers are characterized by sensitivity (output change per unit input change), linearity (how closely the output follows a straight line across the measurement range), and response time (how quickly the output tracks a changing input).
*   **Signal Conditioning**: The processing applied to a raw sensor output before analog-to-digital conversion, including amplification (boosting weak millivolt signals to the ADC's full-scale range), filtering (removing high-frequency noise with a low-pass RC filter), and offset correction (removing DC bias). Proper signal conditioning maximizes ADC resolution utilization and reduces quantization error.
*   **Sampling Rate and Nyquist Theorem**: The frequency at which an ADC takes discrete measurements of a continuous analog signal. The Nyquist theorem states that the sampling rate must be at least twice the highest frequency component of interest to avoid aliasing — the false reconstruction of low-frequency signals from undersampled high-frequency content. For a 50 Hz vibration sensor, a minimum sampling rate of 100 Hz is required.
*   **Sensor Fusion**: The algorithmic combination of data from multiple sensors measuring the same or complementary physical quantities to produce a more accurate, reliable, or higher-dimensional output than any single sensor can provide. A common example is combining a 3-axis accelerometer with a 3-axis gyroscope using a complementary or Kalman filter to produce stable orientation estimates for a drone or wearable device.
*   **Data Aggregation and Decimation**: Techniques used at edge nodes to reduce the volume of raw sensor data before transmission to the cloud. Aggregation computes summary statistics (mean, min, max, standard deviation) over a time window and transmits only the summary. Decimation discards every N-th sample to reduce bandwidth at the cost of temporal resolution. Both techniques reduce cloud storage costs and transmission energy but require careful design to avoid discarding anomalous events.

---

### 2. Certification Exam Tips
*   **ADC resolution and voltage range math:** ADC resolution = full-scale voltage / 2^n bits. A 10-bit ADC with a 3.3 V reference has 3.3 V / 1024 = 3.22 mV per step. Exam questions frequently ask you to calculate the minimum detectable voltage change or the number of steps for a given voltage range.
*   **I2C vs SPI for sensors:** I2C uses 2 wires (SDA, SCL) and supports up to 127 devices on one bus — ideal for multiple low-speed sensors. SPI uses 4 wires (MISO, MOSI, SCK, CS) per device and supports higher data rates — preferred for high-speed ADCs or displays. Know which to choose given a constraint on pin count or data rate.
*   **Nyquist and aliasing:** Always check that the sampling rate is at least 2x the signal bandwidth. Anti-aliasing low-pass filters with a cutoff at half the sampling rate prevent aliasing before the ADC.
*   **Sensor spoofing attacks:** Physical sensors can be manipulated — shining a strong light on a light-dependent resistor, blowing air on a temperature sensor, or injecting a signal on an analog wire. Defense requires anomaly detection (readings outside physically plausible bounds) and cross-validation with independent sensors.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure physical interfaces, which includes vulnerabilities in exposed sensor buses (I2C, SPI, UART) that allow an attacker with physical access to intercept or inject sensor data.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insecure physical interface and insufficient data protection sections, which cover vulnerabilities in sensor buses, unprotected debug ports, and unencrypted sensor telemetry relevant to this module.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) demonstrates reading temperature and humidity sensors over I2C, performing ADC readings on a Raspberry Pi, and aggregating sensor data before cloud transmission.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Read a sensor over I2C and log raw data**: Using a Raspberry Pi and a BME280 temperature/humidity/pressure sensor, install the `smbus2` Python library, scan the I2C bus with `i2cdetect -y 1` to confirm the sensor address (typically 0x76 or 0x77), read raw register values, and apply the manufacturer's compensation formula to produce calibrated readings.
*   **Apply a moving-average filter to reduce noise**: Record 100 ADC samples at 10 Hz from a light sensor, compute a 5-sample moving average in Python, and plot raw vs. filtered data to visualize noise reduction.
*   **Demonstrate data aggregation**: Collect 60 seconds of temperature readings at 1 Hz, compute min/max/mean/standard deviation over the window, and compare the bandwidth required to transmit all 60 raw readings versus the 4-value summary.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the insecure physical interface section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the sensor integration sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Calculate ADC resolution for a 12-bit ADC with a 3.3 V reference before the lab.
- [ ] Proceed to the weekly hands-on lab activity.
