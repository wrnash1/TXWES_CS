# Reading Guide: Module 02 - Microcontrollers – Arduino and Raspberry Pi Basics
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 02 – Microcontrollers: Arduino and Raspberry Pi Basics**! This module covers the hardware building blocks of embedded IoT systems: microcontrollers (MCUs) such as the Arduino Uno and microprocessors/SBCs such as the Raspberry Pi. You will learn how to interface with GPIO pins, how serial communication buses (I2C, SPI, UART) connect sensors and peripherals, and how the analog-to-digital converter (ADC) bridges the physical and digital worlds.

Understanding these interfaces is critical not only for building IoT prototypes but also for identifying hardware-level attack surfaces. Exposed debug ports (UART/JTAG), unsecured I2C buses, and default firmware credentials are common entry points for hardware attackers. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **General Purpose Input/Output (GPIO)**: Configurable digital pins on a microcontroller or SBC that can be individually set as input (reading a button or sensor signal) or output (driving an LED or relay). GPIO pins operate at logic-level voltages (3.3 V or 5 V) and must never exceed the MCU's rated voltage. Attackers who gain physical access to a device can probe GPIO pins with a logic analyzer to eavesdrop on sensor data or inject malicious signals.
*   **I2C Protocol**: A two-wire synchronous serial bus (Serial Data Line – SDA, Serial Clock Line – SCL) that supports multiple master and slave devices on the same bus using unique 7-bit or 10-bit addresses. I2C is commonly used to connect sensors (accelerometers, temperature sensors) and small displays to a microcontroller. Without pull-up resistors and bus isolation, an attacker with physical access can perform a man-in-the-middle attack by attaching a sniffer to the shared bus.
*   **SPI Bus**: A four-wire full-duplex synchronous serial bus (MISO, MOSI, SCK, and one CS line per slave) that achieves higher data rates than I2C at the cost of more wiring. SPI is commonly used for high-speed peripherals such as SD cards, flash memory, and display drivers. Each slave requires a dedicated Chip Select (CS) line, making bus arbitration simpler but pin usage higher.
*   **Analog-to-Digital Converter (ADC)**: A hardware circuit that samples a continuously varying analog voltage (e.g., from a thermistor or microphone) and converts it to a discrete binary value. Resolution is expressed in bits (e.g., 10-bit ADC on Arduino Uno produces values 0–1023 for 0–5 V). ADC accuracy depends on the reference voltage and sampling rate; noise on the power supply directly degrades measurement accuracy.

---

### 2. Certification Exam Tips
*   **I2C vs. SPI trade-offs:** Know the key differences: I2C uses 2 wires and supports multiple devices via addressing; SPI uses 4+ wires and achieves higher speeds with full-duplex operation. Exam scenarios may ask which bus is appropriate for a high-speed display (SPI) versus a low-speed temperature sensor network (I2C).
*   **Arduino vs. Raspberry Pi:** Arduino is a microcontroller running a single loop program with no OS — ideal for hard real-time sensor control and low power. Raspberry Pi is a Linux SBC capable of running Python, Node.js, and cloud clients — ideal for gateway functions and local ML inference. Know which platform is appropriate for which task.
*   **ADC resolution math:** Be able to calculate voltage resolution: for a 10-bit ADC with a 5 V reference, the resolution is 5 V / 1024 ≈ 4.9 mV per step. For a 12-bit ADC with 3.3 V reference: 3.3 V / 4096 ≈ 0.8 mV per step.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers hardware interface attack surfaces including exposed debug ports and insecure serial buses — directly relevant to the microcontroller attack surface examined in this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the hardware interface attack surface section, which covers UART/JTAG debug port exposure and physical bus eavesdropping threats relevant to Arduino and Raspberry Pi deployments.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes hands-on walkthroughs of GPIO programming, I2C sensor wiring, and SPI communication on both Arduino and Raspberry Pi platforms.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Trace pin connection layouts**: Wire a BME280 temperature/humidity sensor to a Raspberry Pi over I2C (SDA → GPIO2, SCL → GPIO3, 3.3 V, GND), verify the device appears at address 0x76 or 0x77 using `i2cdetect -y 1`, and document the pin-out diagram.
*   **Write sensor reading loop scripts using Python/C modules**: Write a Python script using the `smbus2` library to read temperature and humidity from the BME280 every 2 seconds and print formatted output; compare with the equivalent Arduino C sketch using the Wire library.
*   **Inspect communication timing**: Use a software logic analyzer (e.g., PulseView with a low-cost USB analyzer) to capture I2C transactions and measure the clock frequency, start/stop conditions, and ACK/NACK bytes on the SDA/SCL lines.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the hardware interface attack surface section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the microcontroller and GPIO sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review the lab wiring diagrams and pin-out documentation.
- [ ] Proceed to the weekly hands-on lab activity.
