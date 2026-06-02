# Lab Activity – Module 02: Microcontrollers – Arduino and Raspberry Pi Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Points:** 100
**Submission:** Canvas – Module 02 Lab Assignment

---

## Overview

In this lab you will write and test real embedded code on both the Arduino and Raspberry Pi platforms. You will blink an LED with a rate controlled by an analog potentiometer on the Arduino, and write a Python GPIO blink script with proper cleanup on the Raspberry Pi. You will also analyze GPIO security considerations relevant to production IoT deployments.

---

## Learning Objectives

By completing this lab you will be able to:

- Write, upload, and run a complete Arduino sketch in C++ using `analogRead()` and `digitalWrite()`.
- Wire an LED with a current-limiting resistor to an Arduino digital output pin.
- Write a Raspberry Pi Python GPIO script using RPi.GPIO with correct BCM numbering and cleanup.
- Explain the purpose of `GPIO.cleanup()` and `GPIO.setmode()`.
- Identify the security risk posed by exposed UART and JTAG debug interfaces on production devices.

---

## Required Materials

For the Arduino portion (physical hardware option):

- Arduino Uno or compatible board
- USB cable (Type A to Type B)
- Solderless breadboard
- 1 LED (any color)
- 1 resistor, 330 ohm
- 1 potentiometer, 10 kilohm
- Jumper wires

For the Raspberry Pi portion (physical hardware option):

- Raspberry Pi (any model with 40-pin GPIO header, running Raspberry Pi OS)
- 1 LED
- 1 resistor, 330 ohm
- Breadboard and jumper wires

Simulation alternative: If you do not have physical hardware, use Wokwi (wokwi.com) for Arduino simulation and Sense HAT emulator in Raspberry Pi Desktop for the Pi portion. Screenshot your simulation output for submission.

---

## Part 1: Arduino Blink with Potentiometer Rate Control (35 points)

### Part 1 Background

The Arduino `analogRead()` function reads from analog pins A0–A5 and returns an integer from 0 to 1023 corresponding to 0–5V. By mapping this value to a delay duration you can create a blink rate that changes as you turn a potentiometer knob.

### Part 1 Circuit

Wire the circuit as follows:

- Potentiometer: left pin to 5V, center (wiper) pin to A0, right pin to GND.
- LED circuit: digital pin 9 to 330-ohm resistor to LED anode; LED cathode to GND.

### Part 1 Code Task

Write an Arduino sketch that does all of the following:

- Reads the potentiometer value from analog pin A0 once each loop iteration.
- Maps the raw ADC value (0–1023) to a delay range of 100 ms to 1000 ms.
- Blinks the LED on pin 9 using the mapped delay as both the ON and OFF duration.
- Prints the raw ADC value and the mapped delay to the Serial Monitor at 9600 baud each iteration.

The following starter sketch structure is provided. You must fill in the four marked sections:

```cpp
// Module 02 Lab – Potentiometer-controlled LED blink rate
// Course: CIS-4355 IoT and Embedded Systems

const int POT_PIN = A0;   // potentiometer wiper connected to analog pin A0
const int LED_PIN = 9;    // LED connected to digital pin 9 (PWM-capable)

void setup() {
    // TASK 1: Initialize Serial at 9600 baud
    // TASK 2: Set LED_PIN as OUTPUT
}

void loop() {
    // TASK 3: Read the potentiometer value into an integer variable named rawValue
    // TASK 4: Map rawValue (0-1023) to a delay between 100 and 1000 ms
    //         Store result in an integer variable named blinkDelay
    // Print both values to Serial Monitor in this format:
    //   Raw: <rawValue>   Delay: <blinkDelay> ms

    // Blink the LED using blinkDelay for both ON and OFF durations
    digitalWrite(LED_PIN, HIGH);
    delay(blinkDelay);
    digitalWrite(LED_PIN, LOW);
    delay(blinkDelay);
}
```

### Part 1 Deliverables

- Your complete, working sketch source code (copy and paste into your submission document).
- A screenshot of the Arduino IDE Serial Monitor showing at least 5 lines of output with varying Raw and Delay values as you turn the potentiometer.
- A photo of your wired circuit (or a Wokwi simulation screenshot showing the circuit and running code).

### Part 1 Grading Rubric

| Criterion | Points |
|---|---|
| All four TASK sections correctly implemented | 16 |
| Serial Monitor output screenshot shows correct format with varying values | 9 |
| Circuit photo or simulation screenshot provided | 5 |
| Code uses named constants for pin numbers (not bare integers) | 5 |
| Total | 35 |

---

## Part 2: Raspberry Pi Python GPIO Blink Script (35 points)

### Part 2 Background

The RPi.GPIO library provides a Python interface to the Raspberry Pi's GPIO pins. GPIO pins operate at 3.3V logic. The BCM numbering scheme is used throughout Raspberry Pi documentation and must be set explicitly with `GPIO.setmode(GPIO.BCM)`.

### Part 2 Circuit

Wire the circuit as follows:

- GPIO pin 17 (BCM) to 330-ohm resistor to LED anode; LED cathode to GND (physical pin 6).

Physical pin 11 on the 40-pin header is BCM GPIO 17. Confirm this on the official pinout diagram at raspberrypi.com/documentation before wiring.

### Part 2 Code Task

Write a complete Python script that does all of the following:

- Sets the GPIO mode to BCM.
- Configures GPIO pin 17 as an output.
- Initializes the pin to LOW (LED off).
- Enters a loop that blinks the LED: 0.5 seconds ON, 0.5 seconds OFF.
- Handles KeyboardInterrupt (Ctrl+C) gracefully so the script exits without a Python traceback.
- Calls `GPIO.cleanup()` before the script terminates to reset all GPIO pins.
- Prints "LED ON" and "LED OFF" to the terminal on each state change.

```python
# Module 02 Lab – Raspberry Pi GPIO LED blink
# Course: CIS-4355 IoT and Embedded Systems
# Complete all TASK sections below

import RPi.GPIO as GPIO
import time

LED_PIN = 17  # BCM GPIO 17 = physical pin 11

# TASK 1: Set GPIO mode to BCM
# TASK 2: Configure LED_PIN as output and initialize LOW

try:
    while True:
        # TASK 3: Set LED HIGH, print "LED ON", sleep 0.5 seconds
        # TASK 4: Set LED LOW, print "LED OFF", sleep 0.5 seconds
        pass  # remove this line when you add your code

except KeyboardInterrupt:
    pass  # TASK 5: ensure clean exit on Ctrl+C

# TASK 6: Call GPIO.cleanup()
```

### Part 2 Deliverables

- Your complete Python script with all TASK sections implemented.
- A terminal screenshot showing at least 6 lines of alternating "LED ON" / "LED OFF" output.
- A photo of your wired circuit on the Raspberry Pi (or emulator screenshot).
- A one-paragraph written explanation (4–6 sentences) answering: Why must `GPIO.cleanup()` always be called? What happens to the GPIO pins if you skip it? How does BCM numbering differ from BOARD numbering and why does the choice matter?

### Part 2 Grading Rubric

| Criterion | Points |
|---|---|
| All six TASK sections correctly implemented | 18 |
| Terminal output screenshot shows correct alternating output | 7 |
| Circuit photo or emulator screenshot provided | 4 |
| Written explanation answers all three questions accurately | 6 |
| Total | 35 |

---

## Part 3: Hardware Security Analysis (30 points)

### Part 3 Instructions

Answer each question in complete sentences with specific technical detail. Minimum 3 sentences per answer.

Question 1: A deployed IoT sensor device has an accessible UART header on its circuit board that, when connected with a USB-to-UART adapter, provides a Linux root shell. Identify which OWASP IoT Top 10 item this represents, explain exactly how an attacker would exploit it step by step, and propose two concrete mitigations that a hardware engineer could implement before production deployment.

Question 2: A developer uses a shared I2C bus to connect five sensors to a Raspberry Pi in a medical monitoring device. Explain the attack that becomes possible if an attacker gains physical access to the I2C bus traces on the PCB, what data they could capture or inject, and what defensive design choices would reduce this risk.

Question 3: An Arduino Uno in a commercial product ships with default firmware that echoes all sensor readings to its UART at 115200 baud. The UART RX pin also accepts commands from a trusted host. Describe the threat model for this design, identify the specific vulnerability if the RX pin accepts commands without authentication, and explain how a firmware developer would implement command authentication using a pre-shared secret.

### Part 3 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Correct OWASP item identified, exploitation steps accurate, two valid mitigations | 10 |
| Question 2: Attack correctly described, data exposure identified, defensive design valid | 10 |
| Question 3: Threat model accurate, vulnerability correctly identified, authentication method described | 10 |
| Total | 30 |

---

## Submission Checklist

- [ ] Part 1: Arduino sketch source code, Serial Monitor screenshot, circuit photo.
- [ ] Part 2: Python script source code, terminal output screenshot, circuit photo, written explanation.
- [ ] Part 3: All three security analysis answers in complete sentences.

---

## Overall Grading Summary

| Part | Description | Points |
|---|---|---|
| 1 | Arduino blink with potentiometer | 35 |
| 2 | Raspberry Pi Python GPIO blink | 35 |
| 3 | Hardware security analysis | 30 |
| Total | | 100 |

---

End of Lab – Module 02
