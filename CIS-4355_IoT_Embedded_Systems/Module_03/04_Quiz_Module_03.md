# Quiz – Module 03: Embedded Programming – C and MicroPython Basics

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Format:** 10 questions, multiple choice, 4 options each
**Certification Alignment:** CompTIA IoT+ Domain 2

---

## Question 1

Why is static memory allocation preferred over dynamic allocation using `malloc()` in high-reliability embedded firmware?

- A) Static memory executes faster because it bypasses the CPU cache.
- B) Dynamic allocation risks heap fragmentation and non-deterministic runtime memory exhaustion that cannot be fully tested at compile time.
- C) The C language does not support dynamic memory allocation on ARM or AVR microcontrollers.
- D) Pointers are prohibited in safety-critical embedded code under all embedded coding standards.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Memory access speed is determined by the hardware memory bus and caching hardware, not whether the allocation is static or dynamic. The reason to prefer static allocation is determinism, not speed.
- B is correct: On an MCU with 2 KB of SRAM, repeated `malloc()`/`free()` cycles fragment the heap. Over time, even if total free memory is sufficient, no single contiguous block may be available. This produces a runtime crash that static allocation makes impossible.
- C is incorrect: C absolutely supports `malloc()` and `free()` on embedded platforms. The avoidance is a best practice, not a language limitation.
- D is incorrect: Pointers are used extensively in embedded code and in MISRA-C compliant firmware. The restriction is on dynamic allocation, not on pointers themselves.

---

## Question 2

Which of the following correctly defines register mapping in embedded C programming?

- A) Accessing microcontroller peripheral control registers directly via their memory-mapped I/O addresses using `volatile` pointer casts in C.
- B) A compiler optimization that places frequently used variables into CPU registers to reduce SRAM access latency.
- C) Assigning unique I2C bus addresses to multiple devices sharing the same SDA and SCL lines.
- D) A Python decorator that maps function calls to GPIO pin state changes on a Raspberry Pi.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: Register mapping means accessing the exact memory address of a hardware peripheral register using a C pointer cast, for example `volatile uint32_t *GPIOB_ODR = (uint32_t *)0x40020C14`. The `volatile` qualifier prevents the compiler from caching the value and missing hardware updates.
- B is incorrect: Register allocation (the compiler optimization) is an unrelated concept performed automatically by the compiler. It does not involve peripheral hardware registers.
- C is incorrect: I2C device addressing is a hardware configuration concept unrelated to memory-mapped I/O register access.
- D is incorrect: Python decorators are a Python language feature with no connection to memory-mapped hardware register programming.

---

## Question 3

An embedded C function contains `char buf[16]; strcpy(buf, userInput);` where `userInput` is received from a network packet. What vulnerability does this introduce?

- A) Integer overflow in the implicit loop counter used by `strcpy` to iterate over the string.
- B) Buffer overflow: if `userInput` exceeds 15 characters, `strcpy` writes past the end of `buf`, corrupting adjacent stack memory.
- C) Race condition: concurrent calls to `strcpy` from multiple threads will corrupt each other's buffers.
- D) Null pointer dereference: `strcpy` returns NULL when the source string is empty.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `strcpy` does not expose an integer loop counter to the caller. The vulnerability is in writing beyond the destination buffer boundary, not in a counter variable.
- B is correct: `strcpy` copies bytes until it encounters a null terminator with no regard for the destination buffer size. If `userInput` is 40 bytes, `strcpy` writes 40 bytes into a 16-byte buffer, overwriting 24 bytes of adjacent stack memory. This can corrupt the function's return address, enabling code execution.
- C is incorrect: A race condition requires concurrent access. This code has a single-threaded sequential buffer overflow regardless of whether threads are present.
- D is incorrect: `strcpy` does not return NULL on empty input. It copies zero bytes (only the null terminator) and returns a pointer to the destination buffer.

---

## Question 4

Which bitwise expression correctly clears bit 3 of a `uint8_t` variable `reg` without affecting any other bits?

- A) `reg = reg | (1 << 3);`
- B) `reg = reg & ~(1 << 3);`
- C) `reg = reg ^ (1 << 3);`
- D) `reg = reg >> 3;`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The OR operator sets bits to 1. `reg | (1 << 3)` forces bit 3 HIGH regardless of its previous state. It cannot clear a bit.
- B is correct: `(1 << 3)` produces `0b00001000`. The bitwise NOT `~(1 << 3)` produces `0b11110111`. ANDing `reg` with this mask forces bit 3 to 0 and preserves all other bits unchanged.
- C is incorrect: XOR toggles a bit. If bit 3 is already 0, `reg ^ (1 << 3)` sets it to 1. If it is 1, XOR clears it. XOR does not unconditionally clear.
- D is incorrect: A right shift moves all bits, producing an entirely different value. It does not clear a specific bit in place.

---

## Question 5

A MicroPython script reads a DHT11 sensor in a `while True` loop with no exception handling. The sensor occasionally fails to produce a valid reading and raises an `OSError`. What happens on the next failed reading?

- A) MicroPython automatically retries the measurement three times before raising the exception.
- B) The uncaught `OSError` propagates to the top level and terminates the script, stopping all sensor readings.
- C) MicroPython's garbage collector catches the exception and resumes the loop automatically.
- D) The `dht` module returns 0 for both temperature and humidity instead of raising an exception.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: The `dht` module does not implement automatic retry logic. It raises `OSError` on the first failure.
- B is correct: An uncaught exception in MicroPython propagates up the call stack. If no `except` clause handles it at any level, it reaches the REPL or top-level handler, which prints a traceback and terminates script execution. A production IoT sensor must wrap `sensor.measure()` in `try/except OSError` to continue operating after occasional sensor communication failures.
- C is incorrect: The garbage collector manages memory, not exception handling. Python's GC has no ability to catch or suppress exceptions.
- D is incorrect: The `dht` module raises `OSError` on timing failures. It does not return default values silently.

---

## Question 6

What is the purpose of the `volatile` qualifier when declaring a memory-mapped hardware register pointer in C?

- A) It marks the pointer as read-only so the compiler prevents accidental writes to hardware registers.
- B) It tells the compiler that the variable's value can change outside normal program flow, preventing the compiler from caching the value in a CPU register and missing hardware updates.
- C) It allocates the pointer in volatile (battery-backed) SRAM to preserve its value across power cycles.
- D) It enables the pointer to be shared safely between two threads without a mutex.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `volatile` does not make a variable read-only. The `const` qualifier makes a variable read-only. `volatile` and `const` are orthogonal and can both be applied to the same variable.
- B is correct: Without `volatile`, an optimizing compiler may see that a register variable is written once and never read again in C code, and optimize out the write. For a hardware register, that write was the entire point. `volatile` prevents this optimization by telling the compiler that an external agent (hardware) may read or change this memory location at any time.
- C is incorrect: "Volatile memory" in everyday electronics means memory that loses its state when power is removed (like RAM). The C `volatile` keyword is a compiler qualifier with no connection to battery-backed storage.
- D is incorrect: `volatile` does not provide thread safety or mutual exclusion. A mutex or atomic operation is required for safe multi-threaded access.

---

## Question 7

A `uint8_t` counter variable counts bytes received in a UART buffer. An attacker sends exactly 260 bytes. What value does the counter hold after processing all 260 bytes?

- A) 260
- B) 255
- C) 4
- D) 0

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: A `uint8_t` can only hold values from 0 to 255. It cannot represent 260.
- B is incorrect: 255 is the maximum value of a `uint8_t`. Incrementing beyond 255 wraps around to 0, not stays at 255 (that would be saturation behavior, not unsigned wrap-around).
- C is correct: `uint8_t` is an 8-bit unsigned integer with a maximum value of 255. Counting from 0: after 256 increments the value wraps to 0. After 260 increments the value is 260 - 256 = 4. An overflow check like `if (counter > 200)` would evaluate `4 > 200`, which is false, so the overflow goes undetected.
- D is incorrect: The counter would reach 0 after exactly 256 increments, not 260.

---

## Question 8

Which of the following firmware update practices best protects an IoT device against installation of a malicious firmware image delivered over a network connection?

- A) Compressing the firmware image with gzip before transmission to reduce download time.
- B) Storing the download URL as a compile-time constant to prevent runtime URL redirection.
- C) Verifying a cryptographic signature (such as ECDSA with SHA-256) on the received firmware image before writing it to flash.
- D) Using dynamic memory allocation to buffer the entire firmware image in RAM before writing.

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: Compression reduces size and bandwidth but provides no authentication. An attacker can compress a malicious image equally well.
- B is incorrect: A hardcoded URL prevents the device from being redirected to a different server at runtime, but it does not validate whether the content at the legitimate URL is authentic. A server compromise or a network interception still allows a malicious image to be delivered.
- C is correct: A cryptographic signature created by the manufacturer's private key and verified by a public key stored in the device's secure flash ensures that only images signed by the legitimate manufacturer can be installed. Even if the delivery channel is compromised, an unsigned image will be rejected before flash write.
- D is incorrect: Buffering in RAM before writing is a common implementation pattern but has no security benefit. Static buffers with signature verification are the secure approach.

---

## Question 9

In MicroPython on an ESP32, which module provides GPIO pin control, ADC reading, and hardware timer functions?

- A) `os`
- B) `sys`
- C) `machine`
- D) `network`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: The `os` module in MicroPython provides filesystem operations, not hardware GPIO control.
- B is incorrect: The `sys` module provides Python runtime information (version, path, exception handling) but not hardware peripheral access.
- C is correct: The `machine` module is MicroPython's hardware abstraction layer. It provides `machine.Pin()` for GPIO, `machine.ADC()` for analog input, `machine.I2C()` and `machine.SPI()` for communication buses, and `machine.Timer()` for hardware timers.
- D is incorrect: The `network` module handles Wi-Fi and network interface configuration. It does not provide GPIO or ADC access.

---

## Question 10

An embedded developer needs to read a 10-bit ADC value on an Arduino Uno and map it to a servo angle between 0 and 180 degrees. Which Arduino function performs this mapping in one call?

- A) `constrain(value, 0, 180)`
- B) `map(value, 0, 1023, 0, 180)`
- C) `analogWrite(value, 180)`
- D) `scale(value, 1023, 180)`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: `constrain(value, low, high)` clamps a value within a range. It does not scale the value — it would simply return `value` as long as it is between 0 and 180, and clamp to 0 or 180 outside that range.
- B is correct: `map(value, fromLow, fromHigh, toLow, toHigh)` linearly maps a value from one range to another. `map(value, 0, 1023, 0, 180)` converts the full 10-bit ADC range (0–1023) to the servo angle range (0–180).
- C is incorrect: `analogWrite(pin, value)` writes a PWM duty cycle to a PWM-capable pin. It takes a pin number and a duty cycle value (0–255), not a source range and target range.
- D is incorrect: `scale()` is not an Arduino built-in function.

---

End of Quiz – Module 03
