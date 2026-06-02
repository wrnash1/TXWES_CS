# Lab Activity – Module 03: Embedded Programming – C and MicroPython Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Points:** 100
**Submission:** Canvas – Module 03 Lab Assignment

---

## Overview

In this lab you will write MicroPython code to read a DHT11 temperature and humidity sensor and display formatted output on the serial console. You will also write an Arduino C sketch demonstrating bitwise register operations and analyze a piece of vulnerable embedded C code for buffer overflow risks. These exercises build the practical firmware skills required for the CompTIA IoT+ exam and the Module 09 security capstone.

---

## Learning Objectives

By completing this lab you will be able to:

- Write a complete MicroPython sensor-reading script with error handling and formatted output.
- Use the `dht`, `machine`, and `utime` MicroPython modules correctly.
- Demonstrate all four bitwise operations (set, clear, toggle, test) in an Arduino C sketch.
- Identify a buffer overflow vulnerability in C code and propose the correct fix.
- Explain the tradeoffs between C and MicroPython for embedded IoT firmware.

---

## Prerequisites

- Completed Module 03 video lecture and reading guide.
- MicroPython hardware option: ESP32 or Raspberry Pi Pico with MicroPython firmware, Thonny IDE.
- MicroPython simulation option: Wokwi simulator (wokwi.com) supports MicroPython on ESP32.
- Arduino hardware option: Arduino Uno, USB cable, Arduino IDE.
- Arduino simulation option: Wokwi simulator supports Arduino sketches.

---

## Part 1: MicroPython DHT11 Sensor Reader (40 points)

### Part 1 Background

The DHT11 sensor outputs temperature in Celsius as an integer and relative humidity as an integer percentage. MicroPython's built-in `dht` module handles the sensor's single-wire communication protocol. The `machine.Pin()` function creates a GPIO pin object. The `utime.sleep()` function provides second-level delays, and `utime.ticks_ms()` provides millisecond-level timing.

### Part 1 Hardware

Connect the DHT11 as follows:

- DHT11 VCC pin to 3.3V
- DHT11 GND pin to GND
- DHT11 DATA pin to GPIO 4 (on ESP32) or GP4 (on Pico)
- 10k ohm pull-up resistor between DATA and 3.3V

For Wokwi simulation: add a DHT11 component and connect it to GPIO 4.

### Part 1 Code Task

Write a complete MicroPython script that satisfies all of the following requirements:

- Imports `dht`, `machine`, and `utime`.
- Creates a DHT11 sensor object on GPIO pin 4.
- Runs in an infinite loop.
- Each iteration calls `sensor.measure()` to trigger a reading.
- Reads temperature in Celsius and converts to Fahrenheit using the formula: F = (C × 9 / 5) + 32.
- Reads relative humidity.
- Prints output in this exact format (values are examples):

```text
Temperature: 24 C  (75.2 F)
Humidity:    58 %
----------------------------------------
```

- Wraps the measurement in a `try/except OSError` block that prints a friendly error message if the sensor fails to respond instead of crashing.
- Waits 2 seconds between readings using `utime.sleep(2)`.
- Includes a comment above each logical section of code explaining what it does.

The starter template is provided below. Replace every comment marked with TASK:

```python
# Module 03 Lab – MicroPython DHT11 sensor reader
# Course: CIS-4355 IoT and Embedded Systems

# TASK 1: Import dht, machine, and utime modules

# TASK 2: Create DHT11 sensor object on GPIO pin 4

print("DHT11 initialized. Reading every 2 seconds.")
print("-" * 40)

while True:
    # TASK 3: Inside a try block, call sensor.measure()
    # TASK 4: Read temperature (Celsius) and humidity from sensor
    # TASK 5: Calculate Fahrenheit from Celsius
    # TASK 6: Print formatted output (Temperature line, Humidity line, separator)
    # TASK 7: Add except OSError handler that prints an error message
    # TASK 8: Sleep 2 seconds
    pass  # remove this line when your code is complete
```

### Part 1 Deliverables

- Complete Python script with all TASK sections implemented and commented.
- Screenshot of the Thonny console or Wokwi serial output showing at least 5 successful readings.
- If a read error was triggered, a screenshot showing the error message output (not a Python traceback).

### Part 1 Grading Rubric

| Criterion | Points |
|---|---|
| All 8 TASK sections correctly implemented | 20 |
| Output format matches specification exactly | 8 |
| OSError handled without crashing — friendly message printed | 6 |
| Code is fully commented (one comment per logical section) | 6 |
| Total | 40 |

---

## Part 2: Arduino C Bitwise Operations Sketch (30 points)

### Part 2 Background

The Arduino IDE includes a Serial Monitor (Tools menu, 9600 baud) that lets you print text output from your sketch for debugging. Bitwise operations on a variable called `reg` simulate the type of register manipulation used in real embedded firmware, without needing direct register access.

### Part 2 Code Task

Write an Arduino sketch that demonstrates all four bitwise operations on a `uint8_t` variable. The sketch must:

- Declare a `uint8_t` variable named `reg` initialized to `0b00000000`.
- In `setup()`, initialize Serial at 9600 baud.
- In `loop()`, perform the following sequence of operations and print `reg` after each step in binary format using `Serial.println(reg, BIN)`:

Step 1: Set bit 0 (LSB) of `reg` using OR. Print label "Set bit 0:" and the binary value.

Step 2: Set bit 7 (MSB) of `reg` using OR. Print label "Set bit 7:" and the binary value.

Step 3: Clear bit 0 of `reg` using AND with NOT. Print label "Clear bit 0:" and the binary value.

Step 4: Toggle bit 3 of `reg` using XOR. Print label "Toggle bit 3 (first):" and the binary value.

Step 5: Toggle bit 3 again using XOR. Print label "Toggle bit 3 (second):" and the binary value.

Step 6: Test if bit 7 is set. Print "Bit 7 is SET" if true, "Bit 7 is CLEAR" if false.

Step 7: Reset `reg` to `0b00000000` and print "Reset. Pausing 5 seconds."

- After the sequence, `delay(5000)` so the output is readable before repeating.

```cpp
// Module 03 Lab – Bitwise operations demonstration
// Course: CIS-4355 IoT and Embedded Systems

uint8_t reg = 0b00000000;

void setup() {
    // TASK 1: Initialize Serial at 9600 baud
}

void loop() {
    // TASK 2: Set bit 0 with OR, print result
    // TASK 3: Set bit 7 with OR, print result
    // TASK 4: Clear bit 0 with AND/NOT, print result
    // TASK 5: Toggle bit 3 with XOR (first), print result
    // TASK 6: Toggle bit 3 with XOR (second), print result
    // TASK 7: Test bit 7 and print SET or CLEAR
    // TASK 8: Reset reg to 0, print message, delay 5000 ms
}
```

### Part 2 Deliverables

- Complete Arduino sketch with all 8 TASK sections implemented.
- Serial Monitor screenshot showing one complete pass through the sequence with correct binary values.

### Part 2 Grading Rubric

| Criterion | Points |
|---|---|
| All 8 TASK sections correctly implemented using bitwise operators (not arithmetic) | 18 |
| Binary output values are correct for each step | 8 |
| Serial Monitor screenshot shows complete output sequence | 4 |
| Total | 30 |

---

## Part 3: Vulnerable C Code Analysis (30 points)

### Part 3 Instructions

Examine the following embedded C function and answer the three questions below. Write your answers in complete sentences with specific technical details.

```c
// Simulated UART command handler from an embedded device
#include <string.h>
#include <stdint.h>

void processCommand(char *input) {
    char cmdBuffer[32];
    uint8_t counter = 0;

    strcpy(cmdBuffer, input);   // line A

    while (cmdBuffer[counter] != '\0') {
        counter++;              // line B
    }

    if (counter > 200) {        // line C
        // log overflow condition
    }
}
```

Question 1: Identify the specific vulnerability on line A. Name the vulnerability type, explain precisely what can happen when `input` contains 40 bytes of data, and identify which OWASP IoT Top 10 item this violation maps to.

Question 2: Identify the vulnerability on line C. The variable `counter` is declared as `uint8_t`. What is the maximum value a `uint8_t` can hold? If `input` contained 260 bytes, what would `counter` equal after the while loop on line B terminates? Explain why the overflow check `if (counter > 200)` would fail to detect a 260-byte input.

Question 3: Rewrite the `processCommand` function to eliminate both vulnerabilities. Your corrected version must use a length-bounded string copy, use an appropriately sized integer type for `counter`, and add an input length validation check before any copy operation. Explain each change you made and why it eliminates the vulnerability.

### Part 3 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Vulnerability correctly identified, overflow scenario accurately described, OWASP item correctly cited | 10 |
| Question 2: uint8_t max value stated, counter wrap-around value calculated correctly, failure of overflow check explained | 10 |
| Question 3: Corrected function eliminates both vulnerabilities with correct implementation and explanation | 10 |
| Total | 30 |

---

## Submission Checklist

- [ ] Part 1: Complete MicroPython script, console output screenshot.
- [ ] Part 2: Complete Arduino sketch, Serial Monitor screenshot.
- [ ] Part 3: All three questions answered in complete sentences.

---

## Overall Grading Summary

| Part | Description | Points |
|---|---|---|
| 1 | MicroPython DHT11 sensor reader | 40 |
| 2 | Arduino bitwise operations sketch | 30 |
| 3 | Vulnerable C code analysis | 30 |
| Total | | 100 |

---

End of Lab – Module 03
