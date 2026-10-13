# Video Script – Module 03: Embedded Programming – C and MicroPython Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** CompTIA IoT+ Domain 2 – Embedded Systems Programming

---

## Segment 1: Introduction and Learning Objectives [00:00 – 02:00]

Welcome to Module 03. I am Professor Nash. In Module 02 you wired up hardware and ran blink sketches. Now we go deeper into the programming side of embedded systems. By the end of this module you will be able to write real sensor-reading code in both C (for Arduino) and MicroPython (for microcontrollers that run MicroPython, such as the ESP32 and Raspberry Pi Pico).

By the end of this video you will be able to:

- Explain why C is the dominant language for constrained microcontrollers.
- Use pointers, bitwise operations, and memory-efficient data structures in Arduino C++ sketches.
- Describe MicroPython and explain how it differs from CPython and from C.
- Write a MicroPython script to read a DHT11 temperature and humidity sensor and print results to the serial console.
- Identify the key security risks in embedded C programming: buffer overflows, integer overflows, and use-after-free vulnerabilities.

Let us start with why C is everywhere in embedded systems.

---

## Segment 2: Why C Dominates Embedded Programming [02:00 – 06:00]

[SHOW DIAGRAM]

C has been the dominant language for embedded systems since the 1970s and remains so today. There are three reasons: predictable memory layout, direct hardware access, and deterministic performance.

### Predictable Memory Layout

In C you control exactly where variables live in memory. Stack variables, static variables, and heap allocations each have distinct behaviors. On a microcontroller with 2 KB of SRAM — like the ATmega328P in the Arduino Uno — every byte matters. C gives you the tools to use memory efficiently.

Python and Java manage memory automatically through garbage collection. This is convenient but unpredictable. A garbage collector can pause execution at any moment to reclaim memory. For a microcontroller controlling a motor or reading a safety sensor, an unexpected pause of even a few milliseconds is unacceptable.

### Direct Hardware Access

C can write directly to memory-mapped hardware registers. On an AVR microcontroller, controlling a GPIO pin at the lowest level means writing a bit to the Port Data Register at a specific address. This is one line of C code. No OS abstraction layer is required.

```c
PORTB |= (1 << PB5);  // set pin PB5 HIGH by setting bit 5 of PORTB register
```

### Deterministic Performance

C compiles to machine code. The compiled program runs at the processor's native speed with predictable instruction timing. On an 8-bit AVR at 16 MHz, you can calculate exactly how many clock cycles a code path will take. This is essential for time-critical applications: generating precise PWM signals, implementing communication protocols in software, or measuring pulse widths with microsecond accuracy.

---

## Segment 3: Key C Concepts for Embedded Programming [06:00 – 11:00]

[SHOW CODE]

Let me walk through the embedded C concepts you need to know for the lab and the exam.

### Pointers and Memory Addresses

A pointer is a variable that holds the memory address of another variable. In embedded C, pointers appear constantly because they let you pass sensor buffers without copying data, access hardware registers directly, and implement efficient data structures in minimal memory.

```c
uint8_t sensorBuffer[8];       // 8-byte array on the stack
uint8_t *ptr = sensorBuffer;   // ptr holds the address of sensorBuffer[0]

// dereference: read the value at the address ptr points to
uint8_t firstByte = *ptr;

// pointer arithmetic: advance to the next element
uint8_t secondByte = *(ptr + 1);
```

### Bitwise Operations

Bitwise operations let you control individual bits within a register. This is how you configure hardware peripherals and set or clear GPIO pin states efficiently.

```c
uint8_t config = 0b00000000;   // start with all bits zero

config |= (1 << 3);            // set bit 3:    config = 0b00001000
config &= ~(1 << 3);           // clear bit 3:  config = 0b00000000
config ^= (1 << 2);            // toggle bit 2: config = 0b00000100

// check if bit 5 is set:
if (config & (1 << 5)) {
    // bit 5 is HIGH
}
```

The `<<` operator shifts the value 1 left by the bit position number. This is the standard idiom for creating bit masks in embedded C.

### Fixed-Width Integer Types

On embedded systems you must use fixed-width types rather than relying on `int`. The size of `int` is compiler- and architecture-dependent. A `uint8_t` is always 8 bits, a `uint16_t` is always 16 bits, and a `uint32_t` is always 32 bits. These types are defined in `stdint.h` and are available in the Arduino environment.

```c
uint8_t  sensorId   = 42;       // always 8 bits unsigned, range 0-255
uint16_t rawAdc     = 1023;     // always 16 bits unsigned
int32_t  timestamp  = 1717300800; // always 32 bits signed
```

### Static Memory Allocation

In resource-constrained embedded programming, dynamic memory allocation (`malloc`, `free`) is avoided. Dynamic allocation can fragment the heap over time, leading to allocation failures that are difficult to debug. The standard practice is to allocate all buffers statically at compile time.

```c
static char txBuffer[64];    // 64-byte transmit buffer, allocated at compile time
static uint16_t readings[16]; // 16-element ADC reading buffer
```

---

## Segment 4: Introduction to MicroPython [11:00 – 15:00]

[SHOW DIAGRAM]

MicroPython is a lean implementation of Python 3 designed to run directly on microcontrollers with modest resources: as little as 256 KB of flash and 16 KB of RAM. It was created by Damien George in 2013 and has grown into a mature platform supported on the ESP32, ESP8266, Raspberry Pi Pico, STM32, and many other chips.

### How MicroPython Differs from CPython

CPython — the standard Python interpreter you run on a desktop or Raspberry Pi — is optimized for a full operating system environment. It depends on OS services for file I/O, networking, and threading.

MicroPython runs on bare metal with no OS. It implements a subset of CPython, omitting modules that assume OS availability and adding modules specific to microcontroller hardware: `machine` for GPIO and peripherals, `utime` for microsecond timing, `network` for Wi-Fi on chips like the ESP32.

### How MicroPython Differs from C

The tradeoff with MicroPython compared to C is execution speed and memory overhead. MicroPython code is interpreted (or compiled to bytecode) at runtime, making it roughly 10–100 times slower than equivalent C code for computation-heavy tasks. However, for most IoT sensor-reading and network-publishing workflows, the bottleneck is not CPU speed but I/O wait time (waiting for a sensor to respond or a network packet to arrive). In those cases MicroPython's development speed advantage far outweighs its execution speed disadvantage.

MicroPython is also substantially easier to debug. You can connect to the REPL (Read-Eval-Print Loop) over USB and type Python commands interactively, testing sensor reads and GPIO operations one line at a time. There is no compile-upload cycle.

---

## Segment 5: MicroPython DHT11 Sensor Example [15:00 – 19:30]

[SHOW CODE]

Let us write real MicroPython code to read a DHT11 temperature and humidity sensor and print the results to the serial console. This is the exact code you will study and modify in the lab.

The DHT11 is a very common, inexpensive sensor that measures temperature (0–50°C, accuracy ±2°C) and relative humidity (20–90% RH, accuracy ±5%). It communicates over a single-wire protocol, outputting a 40-bit serial data frame approximately 80 ms after a start pulse.

```python
# dht11_read.py
# MicroPython: read DHT11 temperature and humidity sensor
# Hardware: DHT11 DATA pin -> GPIO 4 on ESP32 or Raspberry Pi Pico
#           DHT11 VCC -> 3.3V,  DHT11 GND -> GND
#           10k ohm pull-up resistor between DATA and 3.3V

import dht          # MicroPython built-in DHT sensor driver
import machine      # MicroPython machine module for GPIO and hardware access
import utime        # MicroPython microsecond-precision time functions

# Create a DHT11 sensor object bound to GPIO pin 4
sensor = dht.DHT11(machine.Pin(4))

print("DHT11 sensor initialized on GPIO 4")
print("Reading every 2 seconds. Press Ctrl+C to stop.")
print("-" * 40)

while True:
    try:
        sensor.measure()                   # trigger one measurement (takes ~80ms)
        temp_c  = sensor.temperature()     # returns temperature in Celsius (integer)
        temp_f  = temp_c * 9 / 5 + 32     # convert to Fahrenheit
        humidity = sensor.humidity()       # returns relative humidity as integer percent

        print("Temperature: {:d} C  ({:.1f} F)".format(temp_c, temp_f))
        print("Humidity:    {:d} %".format(humidity))
        print("-" * 40)

    except OSError as e:
        # DHT sensors occasionally fail to respond; catch and report rather than crash
        print("Sensor read error: {}".format(e))

    utime.sleep(2)   # DHT11 requires minimum 1 second between readings; use 2 for margin
```

Let me walk through the key elements.

`import dht` loads MicroPython's built-in DHT sensor driver, which handles the timing-critical single-wire protocol that DHT sensors use.

`machine.Pin(4)` creates a pin object for GPIO 4. In MicroPython the `machine` module provides all hardware access, replacing the platform-specific libraries you would use on a Raspberry Pi.

`sensor.measure()` triggers a measurement. The sensor holds its data line LOW for 18 ms as a start signal, then the sensor responds with 40 bits of data. The DHT library handles all of this timing internally.

The `try/except OSError` block is critical. DHT sensors occasionally miss a reading if the timing is disturbed. Without error handling, one missed reading would crash your program. With error handling, your program prints a warning and continues to the next reading.

`utime.sleep(2)` waits 2 seconds before the next reading. The DHT11 datasheet requires at least 1 second between measurements; using 2 seconds provides a comfortable margin.

---

## Segment 6: Embedded C Security Vulnerabilities [19:30 – 21:30]

Before we close, I need to cover three security vulnerabilities that are specific to embedded C programming. These appear on the CompTIA IoT+ exam and in real-world IoT security audits.

### Buffer Overflow

A buffer overflow occurs when code writes more data into a fixed-size array than the array can hold, corrupting adjacent memory. On a full OS, stack canaries and ASLR provide some protection. On most microcontrollers there is no such protection — a buffer overflow overwrites whatever memory is adjacent, potentially corrupting program state or enabling code execution.

```c
char rxBuffer[32];
// UNSAFE: no bounds check on the incoming string length
strcpy(rxBuffer, incomingData);  // if incomingData > 32 bytes: buffer overflow
```

The fix: use length-bounded functions and always validate input lengths before writing.

### Integer Overflow

Integer overflow occurs when arithmetic on a fixed-width integer exceeds its range and wraps around. On a `uint8_t`, 255 + 1 wraps to 0. If this wrapped value is used as an array index or a loop counter, the resulting out-of-bounds access can corrupt memory.

### Use-After-Free

Although dynamic allocation is avoided in most embedded C, when it is used, use-after-free is a common error: freeing a pointer and then reading or writing through it afterward. The memory may have been reassigned, producing unpredictable behavior.

---

## Segment 7: Summary and Lab Preview [21:30 – 23:00]

C provides predictable memory layout, direct hardware register access, and deterministic timing — all critical for constrained microcontrollers. MicroPython provides Python syntax on microcontrollers, trading execution speed for development speed and interactive debugging, making it ideal for rapid IoT prototyping.

Key C embedded programming patterns: use fixed-width integer types, use static memory allocation, use bitwise operations for register control, avoid dynamic allocation, and always bounds-check input.

In this week's lab you will write MicroPython code to read a DHT11 sensor, format the output, and add error handling for missed readings. You will also analyze a piece of unsafe embedded C code and identify the buffer overflow vulnerability.

See you in Module 04 where we cover IoT messaging protocols in depth: MQTT, CoAP, HTTP/REST, and Zigbee.

---

End of Module 03 Video Script
