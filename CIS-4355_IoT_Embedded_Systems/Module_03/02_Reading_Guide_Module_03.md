# Reading Guide: Module 03 - Embedded Programming – C and MicroPython Basics
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 03 – Embedded Programming: C and MicroPython Basics**! This module covers the two primary programming environments for IoT devices: C/C++ for resource-constrained microcontrollers (Arduino, STM32, ESP32) and MicroPython for slightly more capable boards (ESP8266, Raspberry Pi Pico). You will learn how memory constraints shape code design, how pointers and bitwise operations enable low-level hardware control, and how register mapping allows direct peripheral access without a hardware abstraction layer.

Understanding these fundamentals is essential for both developing reliable embedded software and for recognizing security vulnerabilities. Buffer overflows, use-after-free errors, and uninitialized pointer dereferences — all rooted in C's manual memory model — are among the most exploited vulnerability classes in embedded and IoT firmware.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Memory Constraints**: Embedded MCUs typically provide 2 KB to 256 KB of RAM and 32 KB to 2 MB of flash storage — orders of magnitude less than desktop systems. These constraints force developers to avoid dynamic memory allocation, minimize stack depth, use fixed-size buffers, and prefer static data structures. Exceeding available RAM causes stack overflow or heap corruption, which are common sources of firmware crashes and security vulnerabilities.
*   **Pointers**: Variables that store memory addresses rather than data values. In C, pointers enable direct memory manipulation, passing large data structures by reference, and accessing hardware registers. Pointer misuse (null dereference, dangling pointers, out-of-bounds arithmetic) is a leading cause of embedded system crashes and exploitable vulnerabilities such as buffer overflows.
*   **Bitwise Operations**: Operations that manipulate individual bits of an integer value using AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shift (`<<`, `>>`) operators. In embedded programming, bitwise operations are used to set, clear, toggle, or test specific bits in hardware control registers — for example, setting bit 5 of PORTB to enable a GPIO output without disturbing other bits.
*   **Register Mapping**: The technique of accessing a microcontroller's hardware peripheral control registers directly via memory-mapped I/O addresses, typically using volatile pointer casts in C (e.g., `volatile uint32_t *GPIO_ODR = (uint32_t*)0x40020C14`). Register mapping gives maximum performance and minimal code size but requires consulting the MCU's reference manual for exact addresses and bit field definitions.
*   **Static Allocation**: Allocating all variables, arrays, and buffers at compile time in global or local static scope rather than using `malloc()`/`free()` at runtime. Static allocation eliminates heap fragmentation, makes memory usage deterministic and auditable, and is the required practice in safety-critical and MISRA-C compliant embedded code.

---

### 2. Certification Exam Tips
*   **C vs. MicroPython trade-offs:** C gives full hardware access, deterministic timing, and minimal overhead — essential for hard real-time and safety-critical applications. MicroPython offers rapid prototyping, a built-in REPL, and garbage collection at the cost of latency unpredictability and higher memory usage. Know when each is appropriate.
*   **Buffer overflow recognition:** Exam scenarios often describe code that copies user input into a fixed-size array without bounds checking (`strcpy`, `gets`). Recognize these as buffer overflow vulnerabilities — the correct mitigation is `strncpy` with explicit length limits or safe string libraries.
*   **Volatile keyword:** Know that `volatile` tells the compiler not to optimize away reads/writes to a variable, which is critical for memory-mapped hardware registers and interrupt service routine shared variables.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers firmware vulnerabilities including insecure C coding patterns, buffer overflows, and hardcoded secrets embedded in compiled firmware — all relevant to this module's programming topics.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — review the firmware security section covering insecure C coding practices, unsafe string functions, and how binary firmware images are analyzed for hardcoded credentials and memory vulnerabilities.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) covers both C-based Arduino sketches and MicroPython scripting for ESP32/Pico, demonstrating GPIO control, serial communication, and sensor interfacing in both languages.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a C script compiling bitwise shifts toggling flags**: Write an Arduino sketch that uses bitwise OR to set a GPIO output bit in a control register, bitwise AND with NOT to clear it, and XOR to toggle it, then observe the LED state change without using the `digitalWrite()` abstraction.
*   **Manage memory pointers without leaks**: Write a C function that allocates a struct on the stack, passes it to a helper via pointer, modifies a field, and returns — then verify in a MicroPython equivalent that the same logic uses no manual allocation while comparing code size and execution time.
*   **Verify memory usage**: Use the Arduino IDE's compiled sketch size output and `avr-size` to inspect `.text` (flash) and `.data`/`.bss` (RAM) segment sizes; confirm that static arrays are in `.bss` and that total RAM usage stays below the MCU's limit.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the firmware vulnerability section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the embedded C and MicroPython sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review the lab instructions and prepare the development environment.
- [ ] Proceed to the weekly hands-on lab activity.
