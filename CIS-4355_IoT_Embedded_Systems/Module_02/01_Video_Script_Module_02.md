# Video Script – Module 02: Microcontrollers – Arduino and Raspberry Pi Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA IoT+ Domain 2 – Embedded Systems and Microcontrollers

---

## Segment 1: Introduction and Learning Objectives [00:00 – 02:00]

Welcome back to CIS-4355. I am Professor Nash. In Module 01 we built the architectural framework for IoT systems. Now in Module 02 we zoom into the Perception layer and get hands-on with the two most widely used hardware platforms in IoT education and prototyping: the Arduino and the Raspberry Pi.

These two platforms represent two fundamentally different approaches to embedded computing. Understanding when to use each one — and why — is a skill that appears in interview questions, capstone projects, and on the CompTIA IoT+ exam.

By the end of this video you will be able to:

- Describe the hardware architecture of an Arduino Uno and a Raspberry Pi 4.
- Explain the difference between a microcontroller and a single-board computer.
- Identify the GPIO pins on each platform and describe their capabilities.
- Read and explain a basic Arduino sketch structure in C++.
- Read and explain a basic Raspberry Pi Python GPIO script.
- Choose the appropriate platform for a given IoT application requirement.

Let us get started.

---

## Segment 2: Microcontrollers vs. Single-Board Computers [02:00 – 06:30]

[SHOW DIAGRAM]

Before we touch code, we need to understand the fundamental difference between these two device categories, because confusing them on an exam or in a job interview is a meaningful error.

### What Is a Microcontroller?

A microcontroller is a single integrated circuit that contains a CPU, RAM, flash memory for program storage, and peripheral interfaces all on one chip. The Arduino Uno's heart is the ATmega328P microcontroller made by Microchip. Here are its key specifications:

- CPU: 8-bit AVR RISC running at 16 MHz
- Flash memory: 32 KB, stores your program permanently after upload
- SRAM: 2 KB, runtime working memory
- EEPROM: 1 KB, non-volatile user data storage
- Digital I/O pins: 14 (6 capable of PWM output)
- Analog input pins: 6 (10-bit ADC, 0 to 5V range)
- Communication interfaces: UART, SPI, I2C
- Operating voltage: 5V
- No operating system

That last point — no operating system — is critical. When you upload code to an Arduino, your program is the only thing running on that chip. There is no scheduler, no file system, no network stack unless you explicitly add a library for it. This simplicity is both a strength and a limitation.

Strengths of microcontrollers: deterministic real-time behavior, extremely low power consumption (tens of milliamps at 5V), instantaneous startup with no boot delay, and very low per-unit cost.

Limitations: cannot run complex applications, no native networking, limited memory makes JSON parsing and string manipulation challenging, limited debugging tools.

### What Is a Single-Board Computer?

A single-board computer integrates a full computer system onto a single printed circuit board: a multi-core CPU, substantial RAM, storage interface, GPU, USB ports, display output, Ethernet, Wi-Fi, and Bluetooth. The Raspberry Pi 4 Model B is the dominant single-board computer in IoT education and prototyping.

Raspberry Pi 4 key specifications:

- CPU: 64-bit ARM Cortex-A72 quad-core at 1.8 GHz
- RAM: 2, 4, or 8 GB LPDDR4
- Storage: microSD card or USB solid-state drive
- Connectivity: Gigabit Ethernet, dual-band Wi-Fi, Bluetooth 5.0, four USB ports, two micro-HDMI outputs
- GPIO: 40-pin header with 27 usable programmable GPIO pins
- Operating system: Raspberry Pi OS (Linux-based) or other Linux distributions

The Raspberry Pi runs a full Linux operating system. This means you can run Python, Node.js, databases, web servers, MQTT brokers, and virtually any software that compiles for ARM. It is a full general-purpose computer roughly the size of a credit card.

Strengths: full operating system, built-in networking, runs the entire Linux software ecosystem, Python and SSH remote access, high computational power for analytics.

Limitations: higher power consumption (3 to 7 watts idle, up to 15 watts peak), 15 to 30 second boot time, not suited for hard real-time control where microsecond timing is required, higher cost per unit.

[SHOW DIAGRAM]

The practical decision rule: use Arduino-class microcontrollers when you need real-time control, battery operation, or sub-millisecond timing. Use Raspberry Pi-class single-board computers when you need networking, complex software, file storage, or need to run multiple services simultaneously.

---

## Segment 3: Arduino Hardware and Pin Layout [06:30 – 10:30]

[SHOW DIAGRAM]

Let me walk through the physical Arduino Uno board so you can orient yourself before the lab.

### Power Pins

- Vin: External power input, 7 to 12V recommended.
- 5V output: Regulated 5V rail. Use this to power 5V-logic sensors.
- 3.3V output: Regulated 3.3V rail for 3.3V sensors.
- GND: Ground reference. Every sensor's ground wire must connect to an Arduino GND pin to complete the circuit.

### Digital I/O Pins (D0 through D13)

Digital pins operate in two modes you select in your code:

- INPUT mode: reads HIGH (5V) or LOW (0V) from an external circuit.
- OUTPUT mode: drives HIGH (5V) or LOW (0V) to power a component.

Pins 0 and 1 are shared with the UART used for USB communication with the PC. Avoid using them as general GPIO when the serial monitor is active.

Pins 3, 5, 6, 9, 10, and 11 support PWM (Pulse Width Modulation). PWM approximates an analog output by rapidly switching a digital pin between HIGH and LOW, with the duty cycle controlling average power. You use PWM to dim LEDs smoothly or control servo motor position.

### Analog Input Pins (A0 through A5)

The analog pins connect to the ATmega328P's 10-bit ADC. They convert a voltage in the range of 0 to 5V into a digital integer from 0 to 1023. You use analog inputs to read sensors that output varying voltages: thermistors, potentiometers, photoresistors, gas sensors.

### Communication Bus Interfaces

- I2C: Pins A4 (SDA) and A5 (SCL). Supports up to 127 devices on one two-wire bus. Most modern sensors use I2C.
- SPI: Pins 10 (SS/CS), 11 (MOSI), 12 (MISO), 13 (SCK). Faster than I2C, used for SD cards, displays, and high-speed sensors.
- UART: Pins 0 (RX) and 1 (TX). Serial communication with other devices and with a computer over USB.

---

## Segment 4: Arduino Sketch Structure and Blink Example [10:30 – 14:30]

[SHOW CODE]

Every Arduino program is called a sketch. Every sketch has exactly two required functions: `setup()` and `loop()`.

The `setup()` function runs exactly once when the board powers on or resets. Use it to configure pin modes, initialize serial communication, and set initial output states.

The `loop()` function runs repeatedly and continuously, as fast as the microcontroller can execute it, until power is removed. All ongoing sensor reading, control logic, and communication goes here.

Here is the classic Blink sketch:

```cpp
// Blink – illuminate the built-in LED for 1 second, then off for 1 second
// Arduino Uno: built-in LED is on digital pin 13

const int LED_PIN = 13;  // name the pin for readability

void setup() {
    pinMode(LED_PIN, OUTPUT);  // configure pin 13 as a digital output
}

void loop() {
    digitalWrite(LED_PIN, HIGH);  // set pin 13 to 5V: LED on
    delay(1000);                  // pause 1000 ms
    digitalWrite(LED_PIN, LOW);   // set pin 13 to 0V: LED off
    delay(1000);                  // pause 1000 ms
}
```

Line-by-line explanation:

`const int LED_PIN = 13;` declares a named constant rather than scattering the literal number 13 throughout the code. If you change the pin, you change one line.

`pinMode(LED_PIN, OUTPUT)` configures the I/O direction register of the ATmega328P for pin 13. You must call this in `setup()` before using the pin for output.

`digitalWrite(LED_PIN, HIGH)` drives pin 13 to 5V, completing the circuit through the LED's series resistor to ground, illuminating it.

`delay(1000)` halts all execution for 1,000 milliseconds. During this time nothing else runs. For a simple blink demo this is acceptable. For production IoT code that must read multiple sensors concurrently you would replace `delay()` with a non-blocking approach using `millis()`.

`digitalWrite(LED_PIN, LOW)` pulls pin 13 to 0V, extinguishing the LED.

The `loop()` function then returns to its first line and executes again — this is an infinite cycle.

For the full Arduino language reference covering every built-in function, visit arduino.cc/reference.

---

## Segment 5: Raspberry Pi GPIO and Python Script [14:30 – 18:30]

[SHOW DIAGRAM]

The Raspberry Pi 4's GPIO header is a 40-pin connector along the top edge of the board. Not all 40 pins are programmable GPIO.

Of the 40 pins:

- 2 pins deliver 5V power (physical pins 2 and 4).
- 2 pins deliver 3.3V power (physical pins 1 and 17).
- 8 pins are ground (physical pins 6, 9, 14, 20, 25, 30, 34, 39).
- 27 pins are programmable GPIO.
- Several GPIO pins have alternate hardware functions: I2C on GPIO 2 and 3, SPI on GPIO 10, 9, 11, and 8, UART on GPIO 14 and 15, hardware PWM on GPIO 12, 13, 18, and 19.

Critical safety rule: Raspberry Pi GPIO pins operate at 3.3V logic levels. If you connect a 5V sensor output signal directly to a GPIO input pin, you will damage the Raspberry Pi. Use a voltage divider or a dedicated level-shifter module for any 5V signal.

### Python GPIO Blink Script

[SHOW CODE]

The standard Python library for GPIO control on Raspberry Pi is RPi.GPIO, which comes pre-installed on Raspberry Pi OS. For complete documentation visit raspberrypi.com/documentation.

```python
# blink.py
# Blink an LED connected to GPIO pin 17 of a Raspberry Pi
# Circuit: GPIO 17 -> 330-ohm resistor -> LED anode -> LED cathode -> GND

import RPi.GPIO as GPIO
import time

LED_PIN = 17  # BCM GPIO number (not the physical pin position number)

GPIO.setmode(GPIO.BCM)           # use Broadcom chip GPIO numbering
GPIO.setup(LED_PIN, GPIO.OUT)    # configure GPIO 17 as a digital output
GPIO.output(LED_PIN, GPIO.LOW)   # initialize LED to off state

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED on (3.3V)
        time.sleep(1)                    # wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # LED off (0V)
        time.sleep(1)                    # wait 1 second
except KeyboardInterrupt:
    pass  # user pressed Ctrl+C: exit loop cleanly

GPIO.cleanup()  # reset all configured GPIO pins to input (safe state)
```

Two important design decisions in this script:

First, `GPIO.setmode(GPIO.BCM)` uses the Broadcom chip-level GPIO numbers that appear on all standard Raspberry Pi pinout diagrams. The alternative is `GPIO.BOARD`, which numbers pins by their physical position on the 40-pin connector. BCM is the convention used in Raspberry Pi documentation and in virtually all online examples.

Second, the `try/except KeyboardInterrupt` block combined with `GPIO.cleanup()` is not optional. Without cleanup, GPIO pins left configured as OUTPUT can remain driven HIGH after your script exits, potentially damaging connected components or causing confusing behavior the next time the script runs. Always call `GPIO.cleanup()` in your exit path.

---

## Segment 6: Choosing the Right Platform [18:30 – 20:30]

[SHOW DIAGRAM]

Let me give you a practical decision framework for choosing between Arduino and Raspberry Pi.

Use an Arduino-class microcontroller when:

- Battery life is the primary constraint and you need months to years of operation.
- The application requires hard real-time response in microseconds or single-digit milliseconds.
- The task is simple, well-defined, and fixed: read one sensor, transmit one reading, repeat.
- Per-unit cost must be minimized (an Arduino Nano clone costs under two dollars).
- The device runs unattended with no keyboard or display.

Use a Raspberry Pi-class single-board computer when:

- Full networking is required: HTTP servers, MQTT brokers, WebSocket clients.
- The application needs complex Python libraries, databases, or machine learning inference.
- You need to coordinate multiple sensors or run multiple concurrent services.
- You need an SSH-accessible Linux environment for development and debugging.
- A reliable power supply is available and power consumption is not a constraint.

In professional IoT deployments you often use both together. The microcontroller handles time-critical sensing and actuation at the Perception layer. The Raspberry Pi serves as the edge gateway, collecting data over serial or I2C, processing it, and forwarding results to the cloud. This combined architecture appears in your Module 07 lab.

---

## Segment 7: Summary and Lab Preview [20:30 – 22:00]

The core distinction: microcontrollers like the ATmega328P in the Arduino Uno run one program directly on bare hardware with no OS, providing deterministic real-time behavior at very low power. Single-board computers like the Raspberry Pi run a full Linux OS offering rich networking, software ecosystems, and computational power at the cost of higher power consumption and boot overhead.

Arduino sketches require `setup()` for one-time initialization and `loop()` for continuous execution. GPIO pins on both platforms support digital input, digital output, analog input via ADC, PWM output, and hardware communication buses.

In this week's lab you will wire and upload a blink sketch to an Arduino that varies blink rate using an analog potentiometer, and write a Raspberry Pi Python GPIO script with proper cleanup. Detailed instructions and rubric are in the Lab file.

In Module 03, we level up to reading real temperature sensor data with MicroPython. See you there.

---

End of Module 02 Video Script
