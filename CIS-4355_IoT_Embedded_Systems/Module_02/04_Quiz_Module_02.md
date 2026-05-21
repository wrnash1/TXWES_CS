# Quiz: Module 02 - Microcontrollers – Arduino and Raspberry Pi Basics
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
How many data wire lines are used in the I2C communication protocol?
*   A) One wire
*   B) Two wires (SDA and SCL)
*   C) Four wires (MISO, MOSI, SCK, CS)
*   D) Eight wires
*   **Correct Answer:** B) I2C uses a Serial Data (SDA) line and a Serial Clock (SCL) line, supporting multiple master/slave nodes on the same bus.
*   **Distractor Analysis:**
    *   *Why correct:* I2C uses a Serial Data (SDA) line and a Serial Clock (SCL) line, supporting multiple master/slave nodes.
    *   SPI uses four wire lines (MISO, MOSI, SCK, CS); 1-Wire protocols use a single data line.

---

**Question 2**
Which of the following is the most accurate definition of an **analog-to-digital converter (ADC)**?
*   A) A hardware circuit that samples a continuously varying analog voltage and converts it to a discrete binary number for processing by a microcontroller.
*   B) A two-wire serial bus that connects multiple sensor devices using unique addresses on shared SDA and SCL lines.
*   C) A software interrupt routine that executes when a GPIO pin changes state from low to high.
*   D) A technique for reducing power consumption by switching a microcontroller to a low-power sleep state between sensor readings.
*   **Correct Answer:** A) A hardware circuit that samples a continuously varying analog voltage and converts it to a discrete binary number for processing by a microcontroller.
*   **Distractor Analysis:**
    *   *Why A is correct:* An ADC bridges the analog physical world (voltage from a sensor) and the digital MCU world; resolution (bits) determines measurement precision.
    *   *Why B is incorrect:* This describes the I2C bus, not an ADC.
    *   *Why C is incorrect:* This describes a GPIO interrupt handler, not an ADC.
    *   *Why D is incorrect:* This describes a sleep/power-saving mode, not an ADC.

---

**Question 3**
A developer needs to interface a high-speed SPI-connected display and three I2C temperature sensors to a single Raspberry Pi. Which statement is correct?
*   A) SPI and I2C cannot coexist on the same Raspberry Pi.
*   B) The three I2C sensors must each have unique 7-bit bus addresses; the SPI display uses a dedicated chip-select (CS) line.
*   C) I2C requires four wires per device; SPI requires only two.
*   D) SPI supports up to 127 devices on a single bus without additional chip-select lines.
*   **Correct Answer:** B) The three I2C sensors must each have unique 7-bit bus addresses; the SPI display uses a dedicated chip-select (CS) line.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Raspberry Pi exposes both I2C and SPI buses simultaneously on its GPIO header; they operate independently.
    *   *Why B is correct:* I2C uses addressing (up to 127 unique addresses per bus); SPI slaves are selected by pulling their CS line low — both buses can coexist.
    *   *Why C is incorrect:* I2C uses only 2 wires (SDA, SCL) shared across all devices; SPI uses 4 lines (plus one CS per slave).
    *   *Why D is incorrect:* SPI has no built-in addressing; each additional SPI slave requires its own dedicated CS GPIO pin.

---

**Question 4**
An embedded device is shipped with a UART debug port enabled and accessible via exposed header pins. Which IoT security risk does this represent?
*   A) Increased power consumption from the UART transmitter circuit.
*   B) Unauthorized physical access to a root shell or bootloader, enabling firmware extraction and modification.
*   C) Reduced I2C bus speed due to UART clock interference.
*   D) Incompatibility with cloud MQTT brokers that do not support serial transports.
*   **Correct Answer:** B) Unauthorized physical access to a root shell or bootloader, enabling firmware extraction and modification.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* UART power draw is negligible and is not a security risk.
    *   *Why B is correct:* Exposed UART ports are listed in OWASP IoT Top 10 (Insecure Physical Interfaces) — attackers can attach a USB-to-UART adapter and access a root shell or interrupt the bootloader.
    *   *Why C is incorrect:* UART and I2C operate on separate hardware peripherals with no shared clock.
    *   *Why D is incorrect:* UART is a local hardware interface; cloud MQTT connectivity is separate and unaffected.

---

**Question 5**
When selecting between Arduino and Raspberry Pi for a battery-powered remote temperature sensor that must run for 6 months on two AA batteries, which platform and justification is most appropriate?
*   A) Raspberry Pi 4, because it runs full Linux and can send HTTPS requests natively.
*   B) Arduino (ATmega328P), because microcontrollers can enter deep sleep drawing microamps between readings, whereas a Linux SBC draws hundreds of milliamps continuously.
*   C) Raspberry Pi Zero W, because its small size reduces battery drain proportionally to its physical footprint.
*   D) Arduino Mega, because more GPIO pins provide redundant power supply paths that extend battery life.
*   **Correct Answer:** B) Arduino (ATmega328P), because microcontrollers can enter deep sleep drawing microamps between readings, whereas a Linux SBC draws hundreds of milliamps continuously.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Raspberry Pi 4 draws 500–700 mA at idle — two AA batteries (roughly 3 Wh total) would last only a few hours.
    *   *Why B is correct:* An ATmega328P in power-down sleep draws ~0.1 µA; waking every 60 seconds to take a reading makes months-long battery life achievable.
    *   *Why C is incorrect:* Physical size does not determine power consumption; a Pi Zero W still runs Linux and draws 80–150 mA.
    *   *Why D is incorrect:* Additional GPIO pins do not create power supply paths; the Mega draws more current than the Uno due to its larger chip.
