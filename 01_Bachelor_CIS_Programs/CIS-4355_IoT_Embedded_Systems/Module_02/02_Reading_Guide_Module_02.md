# Reading Guide – Module 02: Microcontrollers – Arduino and Raspberry Pi Basics

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
**Instructor:** Professor Nash
**Certification Target:** CompTIA IoT+ Domain 2

---

## Introduction

Module 02 takes you from IoT architecture theory into the hardware that sits at the Perception layer. You will learn how microcontrollers and single-board computers work, how their GPIO and communication interfaces function, and how these hardware details connect to real security vulnerabilities. Work through every section carefully – several quiz questions require you to perform calculations and interpret code, not just recall definitions.

---

## 1. Core Glossary

- **Microcontroller (MCU):** A single integrated circuit containing a CPU, RAM, flash memory for program storage, and peripheral interfaces. Runs a single program directly on hardware with no operating system. Examples: ATmega328P (Arduino Uno), ESP32, STM32, PIC16F.

- **Single-Board Computer (SBC):** A complete computer system on one circuit board including a multi-core CPU, substantial RAM, storage interface, and full connectivity. Runs a general-purpose operating system. Examples: Raspberry Pi 4, Raspberry Pi Zero 2 W, BeagleBone Black.

- **GPIO (General Purpose Input/Output):** Programmable digital pins on an MCU or SBC that can be individually configured as input or output. Logic level is 3.3V or 5V depending on the platform. Must never be driven above the rated logic level or the pin will be permanently damaged.

- **PWM (Pulse Width Modulation):** A technique for approximating an analog output using a digital pin by rapidly switching it between HIGH and LOW. The duty cycle (percentage of time HIGH) controls the average power delivered. Used for LED dimming, motor speed control, and servo positioning.

- **I2C (Inter-Integrated Circuit):** A two-wire synchronous serial bus using a Serial Data Line (SDA) and a Serial Clock Line (SCL). Supports multiple devices on the same bus via unique 7-bit (or 10-bit) addresses. Standard speeds: 100 kHz (standard mode), 400 kHz (fast mode), 1 MHz (fast-mode plus). Requires pull-up resistors on both lines.

- **SPI (Serial Peripheral Interface):** A four-wire full-duplex synchronous serial bus using MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), and SS/CS (Slave Select/Chip Select). Each slave device requires a dedicated CS line. Faster than I2C but uses more wires.

- **UART (Universal Asynchronous Receiver-Transmitter):** An asynchronous serial interface using TX (transmit) and RX (receive) lines. Communication is configured by baud rate (bits per second), data bits, parity, and stop bits. Used for device-to-device communication and debug consoles. Exposed UART ports are a major hardware attack surface.

- **ADC (Analog-to-Digital Converter):** A hardware circuit that samples a continuously varying analog voltage and converts it to a binary integer. Resolution is expressed in bits: a 10-bit ADC produces values from 0 to 1023; a 12-bit ADC produces values from 0 to 4095.

- **Sketch:** The term used in the Arduino ecosystem for a C/C++ program. Consists of at minimum a `setup()` function that runs once on power-up and a `loop()` function that runs continuously.

- **BCM Numbering:** The Broadcom chip-level GPIO numbering system used in Raspberry Pi documentation and the RPi.GPIO Python library. Refers to the GPIO signal number on the Broadcom SoC, not the physical position of the pin on the 40-pin header.

- **Voltage Divider:** A resistor circuit that reduces a higher voltage signal to a lower level. Used to protect 3.3V Raspberry Pi GPIO pins from 5V sensor output signals. Output voltage = Vin × (R2 / (R1 + R2)).

- **Level Shifter:** A dedicated integrated circuit that safely converts logic signals between voltage levels (5V to 3.3V and vice versa) with proper bidirectional support for I2C buses.

---

## 2. IoT Protocol Comparison Table

| Attribute | MQTT | CoAP | HTTP/REST | AMQP |
|---|---|---|---|---|
| Transport | TCP | UDP | TCP | TCP |
| Message pattern | Publish/subscribe | Request/response | Request/response | Queue + pub/sub |
| Overhead | Very low | Very low | High | Medium |
| QoS options | 0, 1, 2 | CON/NON acknowledgment | None native | Persistent delivery |
| Broker required | Yes | No | No | Yes |
| Best for constrained MCU | Yes (with library) | Yes | No | No |
| Standard port (plain) | 1883 | 5683 | 80 | 5672 |
| Standard port (TLS) | 8883 | 5684 | 443 | 5671 |

---

## 3. Arduino vs. Raspberry Pi Comparison

| Attribute | Arduino Uno (ATmega328P) | Raspberry Pi 4 Model B |
|---|---|---|
| Device type | Microcontroller | Single-board computer |
| CPU | 8-bit AVR at 16 MHz | 64-bit ARM quad-core at 1.8 GHz |
| RAM | 2 KB SRAM | 2–8 GB LPDDR4 |
| Program storage | 32 KB flash | microSD / USB SSD |
| Operating system | None | Linux (Raspberry Pi OS) |
| Idle power | ~50 mA at 5V (~0.25 W) | ~500–700 mA at 5V (~3 W) |
| Boot time | Instant | 15–30 seconds |
| GPIO pins | 14 digital, 6 analog | 27 programmable GPIO |
| GPIO voltage | 5V logic | 3.3V logic |
| Built-in networking | No | Wi-Fi + Gigabit Ethernet |
| Real-time capability | Hard real-time | Soft real-time only (Linux scheduler) |
| Primary language | C/C++ (Arduino framework) | Python, C, Node.js, any Linux language |
| Cost (approximate) | USD 5–25 | USD 35–80 |
| Best use case | Battery sensors, real-time control | Edge gateway, complex analytics |

---

## 4. Communication Interface Reference

| Interface | Wires | Speed | Addressing | Full Duplex | Typical Use |
|---|---|---|---|---|---|
| I2C | 2 (SDA, SCL) | 100 kHz – 1 MHz | 7-bit address | No (half-duplex) | Sensors, EEPROMs, displays |
| SPI | 4+ (MOSI, MISO, SCK, CS) | 10 MHz+ | Chip select pin | Yes | SD cards, displays, ADCs |
| UART | 2 (TX, RX) | Configured by baud rate | None (point-to-point) | Yes | Debug consoles, GPS modules |
| 1-Wire | 1 (data + power) | ~16 kbps | 64-bit ROM address | Half-duplex | DS18B20 temperature sensor |
| I2S | 3 (SCK, WS, SD) | Audio-grade | None | Yes | Digital microphones, DACs |

---

## 5. ADC Calculations Reference

The Arduino Uno uses a 10-bit ADC with a 5V reference by default.

Voltage resolution = Reference voltage divided by (2 raised to the number of bits).

For a 10-bit ADC with 5V reference: resolution = 5 / 1024 = 0.00488 V per step (approximately 4.9 mV).

To convert a raw ADC reading to voltage: voltage = (raw reading / 1023) × 5.0

For a 12-bit ADC with 3.3V reference: resolution = 3.3 / 4096 = 0.000806 V per step (approximately 0.8 mV).

Exam tip: memorize the formula for resolution and be able to apply it to 10-bit and 12-bit examples with both 5V and 3.3V references.

---

## 6. OWASP IoT Top 10 Reference

All 10 items are described in the Module 01 Reading Guide. The items most relevant to Module 02 hardware topics:

1. **OWASP IoT #1 – Weak, Guessable, or Hardcoded Passwords** – Default credentials on device management interfaces reached via serial or network connections.

2. **OWASP IoT #2 – Insecure Network Services** – Unnecessary open services exposed on the device network stack. On an embedded Linux device (Raspberry Pi) this includes unnecessary open SSH ports, Telnet, or HTTP management.

3. **OWASP IoT #4 – Lack of Secure Update Mechanism** – Firmware pushed to microcontrollers without signature verification or over unencrypted channels.

4. **OWASP IoT #10 – Lack of Physical Hardening** – Exposed JTAG and UART debug ports on microcontroller boards. An attacker with a USB-to-UART adapter and physical access can read root shell output, interrupt the bootloader, and extract or modify firmware. This is one of the most commonly exploited hardware vulnerabilities in IoT device audits.

---

## 7. Sensor Types Reference

| Category | Example Part | Signal | Interface | Typical Arduino Code |
|---|---|---|---|---|
| Temperature | DS18B20 | Digital (Dallas 1-Wire) | 1-Wire | OneWire + DallasTemperature libraries |
| Temp + humidity | DHT22 | Digital (single-wire protocol) | GPIO + timing | DHT library |
| Temp + humidity + pressure | BME280 | Digital | I2C or SPI | Adafruit BME280 library |
| Gas / smoke | MQ-2 | Analog voltage | ADC pin | analogRead() |
| Ultrasonic distance | HC-SR04 | Digital pulse width | 2 GPIO pins | pulseIn() |
| Light intensity | BH1750 | Digital | I2C | BH1750 library |
| Accelerometer | MPU-6050 | Digital | I2C | MPU6050 library |

---

## 8. IIoT Purdue Model Reference

The Purdue Enterprise Reference Architecture (PERA) defines security zones for industrial environments:

- Level 0: Physical process – sensors and actuators (equivalent to IoT Perception layer).
- Level 1: Intelligent devices – PLCs, RTUs running control logic.
- Level 2: Control systems – SCADA HMI workstations, DCS.
- Level 3: Manufacturing operations – MES, historians.
- Level 3.5: Industrial DMZ – buffer zone separating OT and IT.
- Level 4: Business logistics – ERP, supply chain.
- Level 5: Enterprise network – corporate IT, internet.

Embedded microcontrollers in industrial IoT map to Level 0 and Level 1. Raspberry Pi-based edge gateways typically sit at Level 2 or the Level 3.5 DMZ.

---

## 9. Exam Tips for Module 02

1. The I2C bus uses 2 wires. SPI uses 4 wires plus one CS line per additional slave. Never confuse these.

2. An Arduino Uno's ADC is 10 bits with a 5V reference. Know how to calculate voltage resolution: 5V / 1024 = ~4.9 mV per step.

3. Raspberry Pi GPIO is 3.3V logic. Connecting a 5V signal directly will damage the chip. Always use a level shifter or voltage divider.

4. The `GPIO.cleanup()` call in Python is not optional — skipping it leaves pins in undefined states and can damage hardware.

5. BCM numbering refers to the Broadcom chip GPIO number, not the physical pin position. GPIO 17 is physical pin 11 on the 40-pin header.

6. UART debug ports exposed on a device are OWASP IoT Top 10 item 10 (Lack of Physical Hardening). Mitigation: disable debug interfaces in production firmware and apply epoxy to port pads.

7. Microcontrollers provide hard real-time guarantees. Raspberry Pi runs Linux with a non-real-time scheduler — it cannot guarantee microsecond-level timing.

8. When a quiz scenario describes battery-powered operation for months or years, the answer is always a microcontroller, never a Linux SBC.

---

## 10. Study Checklist

- [ ] Memorize all 12 glossary terms and apply each to a real hardware example.
- [ ] Study the Arduino vs. Raspberry Pi comparison table and know all five rows that differ between the platforms.
- [ ] Review the communication interface table and be able to state the wire count and addressing method for I2C and SPI.
- [ ] Practice the ADC resolution calculation for 10-bit/5V and 12-bit/3.3V configurations.
- [ ] Review OWASP IoT Top 10 items 1, 2, 4, and 10 in relation to hardware interfaces.
- [ ] Read the sensor types table and identify the interface used for DHT22, BME280, and MQ-2.
- [ ] Review the Purdue Model section and place Arduino and Raspberry Pi at their correct levels.
- [ ] Review all 8 exam tips.
- [ ] Complete the Module 02 Lab (both Arduino blink sketch and Raspberry Pi Python GPIO script).
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 11. Official References

- Arduino language reference and tutorials at arduino.cc/reference
- Raspberry Pi GPIO documentation and hardware specification at raspberrypi.com/documentation
- OWASP IoT Security Project at owasp.org/www-project-internet-of-things

---

## 9. Supplemental Resources

**1. Arduino Language Reference**
[https://www.arduino.cc/reference/en/](https://www.arduino.cc/reference/en/)
The complete official reference for all Arduino built-in functions, data types, and operators. Covers `setup()`, `loop()`, `analogRead()`, `digitalWrite()`, `millis()`, and every other core function. Bookmark this and use it as your primary lookup during labs.

**2. Raspberry Pi GPIO Pinout — pinout.xyz**
[https://pinout.xyz/](https://pinout.xyz/)
An interactive visual reference for the Raspberry Pi 40-pin GPIO header showing BCM numbers, physical pin positions, and alternate functions (I2C, SPI, UART, PWM) for every pin. Essential when wiring circuits to confirm BCM-to-physical mappings.

**3. RPi.GPIO Python Library Documentation**
[https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
The official usage guide for the RPi.GPIO Python library covering `setmode()`, `setup()`, `input()`, `output()`, `cleanup()`, and event detection. Directly relevant to Part 2 of the Module 02 lab.

---

End of Reading Guide – Module 02
