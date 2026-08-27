# Reading Guide – Module 03: Embedded Programming – C and MicroPython Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Certification Target:** CompTIA IoT+ Domain 2

---

## Introduction

Module 03 covers the two primary programming languages used in IoT embedded development: C/C++ for resource-constrained microcontrollers such as the Arduino Uno and ESP32, and MicroPython for microcontrollers with sufficient flash and RAM to run an interpreter (ESP32, Raspberry Pi Pico). You will learn the specific language features and patterns that embedded programming demands, and you will learn to recognize the security vulnerabilities that arise when those patterns are misused. Both topics appear on the CompTIA IoT+ exam.

---

## 1. Core Glossary

- **Memory Constraint:** The condition of embedded MCUs having orders-of-magnitude less RAM and flash than desktop systems. Arduino Uno: 2 KB SRAM / 32 KB flash. ESP32: 520 KB SRAM / 4 MB flash. This forces developers to use fixed-size buffers, avoid deep recursion, prefer stack and static allocation over heap, and pack data structures tightly.

- **Pointer:** A variable that stores a memory address. In C, pointers enable direct hardware register access, efficient passing of large data structures by reference, and dynamic data structures. Pointer errors (null dereference, out-of-bounds arithmetic, dangling pointers) are the most common source of embedded firmware crashes.

- **Bitwise Operation:** An operation that manipulates individual bits of an integer value. The six bitwise operators in C: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), left shift (`<<`), right shift (`>>`). Used extensively in embedded C to set, clear, toggle, and test individual bits in hardware control registers without disturbing adjacent bits.

- **Register Mapping:** Accessing microcontroller hardware peripheral registers directly via their memory-mapped I/O addresses. Requires `volatile` qualified pointer casts in C so the compiler does not optimize out reads and writes to hardware addresses.

- **Static Allocation:** Allocating all memory at compile time in global scope or with the `static` keyword. Memory usage is deterministic and auditable. Contrast with dynamic allocation (`malloc`/`free`) which introduces heap fragmentation risk.

- **volatile keyword:** A C qualifier that instructs the compiler not to optimize away reads or writes to a variable because its value can change outside normal program flow — from an interrupt service routine or a hardware register. Every memory-mapped peripheral register in embedded C must be declared `volatile`.

- **Buffer Overflow:** A vulnerability where code writes beyond the end of a fixed-size array into adjacent memory. In embedded systems with no stack canaries or ASLR, buffer overflows directly corrupt return addresses or adjacent variables. The `strcpy()` and `gets()` functions are unsafe because they perform no bounds checking.

- **Integer Overflow:** When arithmetic on a fixed-width integer exceeds its representable range, wrapping around. A `uint8_t` value of 255 plus 1 wraps to 0. If the wrapped value is used as an array index, the resulting out-of-bounds access corrupts memory.

- **MicroPython:** A lean implementation of Python 3 designed to run on microcontrollers with as little as 256 KB of flash and 16 KB of RAM. Implements a subset of Python 3 plus hardware-specific modules (`machine`, `utime`, `network`). Created by Damien George in 2013.

- **REPL (Read-Eval-Print Loop):** An interactive interpreter prompt available over USB in MicroPython. Allows developers to type Python commands one at a time and see immediate results — without a compile/upload cycle. Dramatically accelerates hardware bring-up and debugging.

- **DHT11:** A low-cost digital temperature and humidity sensor. Communicates over a single-wire protocol. Measures temperature: 0–50°C (±2°C accuracy), humidity: 20–90% RH (±5% accuracy). Requires at minimum 1 second between successive readings.

- **Interrupt Service Routine (ISR):** A function that executes asynchronously in response to a hardware interrupt event (timer expiry, pin state change, UART receive). ISRs must be short and must not call blocking functions. Variables shared between an ISR and the main program must be declared `volatile`.

---

## 2. IoT Protocol Comparison Table

| Attribute | MQTT | CoAP | HTTP/REST | AMQP |
|---|---|---|---|---|
| Transport | TCP | UDP | TCP | TCP |
| Pattern | Publish/subscribe | Request/response | Request/response | Queue + pub/sub |
| Overhead | Very low | Very low | High | Medium |
| Suitable for constrained MCU | Yes | Yes | No | No |
| Broker required | Yes | No | No | Yes |
| Security transport | TLS | DTLS | TLS | TLS/SASL |

---

## 3. C vs. MicroPython Comparison

| Attribute | Embedded C (Arduino/AVR) | MicroPython (ESP32/Pico) |
|---|---|---|
| Execution model | Compiled to native machine code | Bytecode interpreted at runtime |
| Relative speed | Fastest (native code) | 10–100x slower than C |
| Memory overhead | Minimal (bytes of overhead) | ~100–200 KB interpreter overhead |
| Memory management | Manual (static and stack preferred) | Automatic garbage collection |
| Real-time capability | Hard real-time | Soft real-time (GC pauses) |
| Debugging | Serial print, JTAG debugger | Interactive REPL over USB |
| Hardware access | Direct register access via pointers | `machine` module abstraction |
| Typical platforms | Arduino Uno, ATtiny, STM32 | ESP32, Raspberry Pi Pico, ESP8266 |
| Development speed | Slower (compile/upload cycle) | Faster (REPL, no compile step) |
| Best for | Safety-critical, real-time, battery | Rapid prototype, Wi-Fi IoT, medium compute |

---

## 4. Bitwise Operation Quick Reference

| Operation | Symbol | Use in Embedded C | Example |
|---|---|---|---|
| Set bit N | `reg \|= (1 << N)` | Turn on a hardware feature bit | `PORTB \|= (1 << 5)` sets PB5 HIGH |
| Clear bit N | `reg &= ~(1 << N)` | Turn off a hardware feature bit | `PORTB &= ~(1 << 5)` sets PB5 LOW |
| Toggle bit N | `reg ^= (1 << N)` | Flip a bit to opposite state | `PORTB ^= (1 << 5)` toggles PB5 |
| Test bit N | `if (reg & (1 << N))` | Check if a status flag is set | `if (PINB & (1 << 4))` reads pin PB4 |
| Mask lower N bits | `reg & ((1 << N) - 1)` | Extract a bit field value | `reg & 0x0F` extracts lower nibble |

---

## 5. OWASP IoT Top 10 Reference (Firmware Focus)

The following OWASP IoT items are most directly relevant to embedded programming:

1. **OWASP IoT #1 – Weak, Guessable, or Hardcoded Passwords:** Credentials embedded in compiled firmware as string literals are extractable by running `strings` on the binary. Mitigation: store credentials in a separate encrypted partition or provision via secure manufacturing.

2. **OWASP IoT #4 – Lack of Secure Update Mechanism:** Firmware images downloaded without signature verification can be replaced with attacker-controlled code. Mitigation: ECDSA or RSA signature verification on every image before flash write.

3. **OWASP IoT #5 – Use of Insecure or Outdated Components:** Third-party C libraries with known CVEs (buffer overflows, format string vulnerabilities) embedded in firmware. Mitigation: maintain a software bill of materials (SBOM) and track library CVEs.

4. **OWASP IoT #10 – Lack of Physical Hardening:** Firmware extractable via exposed JTAG/UART if flash is not encrypted and readout protection is not enabled. Mitigation: enable flash readout protection (RDP), lock JTAG in production builds.

---

## 6. Sensor Types Reference

| Sensor | Interface | MicroPython Module | C Library |
|---|---|---|---|
| DHT11 / DHT22 | Single-wire GPIO | `dht` (built-in) | DHT Arduino library |
| BME280 | I2C or SPI | `bme280` | Adafruit BME280 |
| DS18B20 | 1-Wire GPIO | `ds18x20` + `onewire` | DallasTemperature |
| HC-SR04 | GPIO (trigger + echo) | `machine.time_pulse_us()` | `pulseIn()` |
| MQ-2 gas sensor | Analog | `machine.ADC()` | `analogRead()` |
| MPU-6050 | I2C | `mpu6050` (third-party) | MPU6050 library |

---

## 7. IIoT Purdue Model Reference

- Level 0: Physical process – sensors and actuators. Microcontrollers (Arduino, PIC, STM32) operate here.
- Level 1: Intelligent devices – PLCs, RTUs. Firmware written in C, ladder logic, or IEC 61131-3.
- Level 2: Control systems – SCADA HMI. May run Windows Embedded or Linux.
- Level 3: Manufacturing operations – MES, historians.
- Level 3.5: Industrial DMZ – security buffer between OT and IT.
- Level 4–5: Business and enterprise IT.

Buffer overflow vulnerabilities in Level 0 and Level 1 firmware are a primary attack vector against IIoT systems. Patching these is extremely difficult because devices are often long-lived and require physical access to update.

---

## 8. Exam Tips for Module 03

1. `strcpy()` and `gets()` are unsafe in embedded C because they perform no bounds checking. The safe alternatives are `strncpy(dest, src, sizeof(dest) - 1)` and `fgets()`.

2. A `volatile` qualifier on a hardware register pointer prevents the compiler from caching the register value in a CPU register and missing updates from hardware. Omitting `volatile` on a hardware register is a common bug.

3. Static allocation means allocating at compile time (global variables, `static` local variables, fixed-size arrays). Dynamic allocation means `malloc()`/`free()` at runtime. Embedded systems prefer static for determinism.

4. Clearing bit N uses AND with NOT: `reg &= ~(1 << N)`. Setting bit N uses OR: `reg |= (1 << N)`. Toggling uses XOR: `reg ^= (1 << N)`.

5. MicroPython's garbage collector can introduce unpredictable pauses. For time-critical code, pre-allocate all objects before entering the time-sensitive section to avoid triggering GC mid-execution.

6. A `uint8_t` has range 0–255. Adding 1 to 255 produces 0 (unsigned overflow). A `int8_t` has range -128 to 127. These are facts you must have memorized for integer overflow exam questions.

7. The DHT11 requires a minimum of 1 second between measurements. Triggering it faster causes read errors that should be caught with exception handling in MicroPython or error-code checking in C.

8. Hardcoded API keys, passwords, or Wi-Fi credentials in firmware are extractable using the `strings` utility on the binary file. This is a critical security flaw covered under OWASP IoT #1.

---

## 9. Study Checklist

- [ ] Memorize all 12 glossary terms with particular focus on volatile, buffer overflow, and integer overflow.
- [ ] Practice all five bitwise operations in the quick reference table from memory.
- [ ] Study the C vs. MicroPython comparison table — be able to explain which is better for real-time control and which is better for rapid prototyping.
- [ ] Review the four OWASP IoT items in the firmware focus section and connect each to a specific embedded programming practice.
- [ ] Review the sensor types table and identify which interface each sensor uses.
- [ ] Review all 8 exam tips.
- [ ] Complete the Module 03 Lab (MicroPython DHT11 script and C buffer overflow analysis).
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 10. Official References

- Arduino language reference at arduino.cc/reference
- Raspberry Pi documentation at raspberrypi.com/documentation
- OWASP IoT Security Project at owasp.org/www-project-internet-of-things
- MicroPython documentation at docs.micropython.org (informational — no direct URL linking required for exam)

---

## 9. Supplemental Resources

**1. MicroPython Documentation — machine Module**
[https://docs.micropython.org/en/latest/library/machine.html](https://docs.micropython.org/en/latest/library/machine.html)
The official reference for MicroPython's hardware abstraction layer. Covers `Pin`, `ADC`, `I2C`, `SPI`, `UART`, `Timer`, and `WDT` classes with examples. Required reading before any MicroPython hardware lab.

**2. MISRA C:2012 Guidelines Overview (MISRA Consortium)**
[https://www.misra.org.uk/misra-c/](https://www.misra.org.uk/misra-c/)
MISRA C is the embedded C coding standard used in automotive, aerospace, and industrial safety-critical firmware. The overview page describes the rationale for rules banning `malloc()`, `gets()`, and other unsafe patterns that directly align with Module 03 security content.

**3. Wokwi ESP32 and Arduino Simulator**
[https://wokwi.com/](https://wokwi.com/)
A browser-based simulator supporting Arduino C sketches and MicroPython on ESP32 and Raspberry Pi Pico. Includes DHT22, BME280, I2C OLED, and dozens of other components. No hardware required — full serial monitor output and pin state visualization.

---

End of Reading Guide – Module 03
