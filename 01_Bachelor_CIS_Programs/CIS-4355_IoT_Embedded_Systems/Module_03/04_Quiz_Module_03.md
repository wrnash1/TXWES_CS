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

---

### Question 11 (5 points)

Which C declaration is correct for a memory-mapped hardware register at address `0x40020C14` on a 32-bit ARM microcontroller, ensuring the compiler always reads and writes it from hardware memory?

- A) `uint32_t *GPIOB_ODR = 0x40020C14;`
- B) `volatile uint32_t *GPIOB_ODR = (volatile uint32_t *)0x40020C14;`
- C) `const uint32_t GPIOB_ODR = 0x40020C14;`
- D) `static uint32_t GPIOB_ODR = 0x40020C14;`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Assigning an integer literal to a pointer without a cast is a constraint violation in C. More importantly, omitting `volatile` lets the compiler cache the register value, causing reads to miss hardware updates.
  - B) The pointer type must be `volatile uint32_t *` and the address must be cast to the same type. The `volatile` qualifier tells the compiler that this memory location can change outside of program flow (hardware sets bits), so every read and write must go directly to the hardware address.
  - C) `const uint32_t` declares a constant integer value equal to the address — not a pointer to that address. Dereferencing is not possible with this declaration.
  - D) `static uint32_t` allocates a regular variable initialized to the address value. It is not a pointer and does not map to hardware. `static` only affects storage duration, not memory mapping.

---

### Question 12 (5 points)

A MicroPython script on an ESP32 reads a BME280 sensor via I2C inside a `while True` loop. After running for 6 hours the script crashes with a `MemoryError`. Which practice most likely caused this?

- A) Using `utime.sleep(1)` between readings, which exhausts the sleep timer resource.
- B) Repeatedly creating new objects (strings, lists, dictionaries) inside the loop without allowing the garbage collector to reclaim them, leading to heap exhaustion.
- C) Reading the BME280 too frequently — the sensor's internal buffer overflows into the MicroPython heap.
- D) The `machine.I2C()` object consumes 1 KB of RAM per read call, accumulating to a MemoryError after approximately 6 hours.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `utime.sleep()` releases the CPU during the delay. It does not consume a timer resource that could be exhausted.
  - B) Creating new Python objects (especially formatted strings with `f"{value:.2f}"` or building new lists each iteration) allocates heap memory. If the garbage collector cannot reclaim objects quickly enough — or if objects are inadvertently retained by a list — the heap fills and raises `MemoryError`. The fix is to pre-allocate objects before the loop and reuse them.
  - C) Sensor hardware has its own internal registers but no mechanism to overflow into the MCU heap. Sensor data is read into the MCU, not pushed by the sensor.
  - D) `machine.I2C()` is created once and its memory usage is constant per instance. It does not accumulate RAM per read call.

---

### Question 13 (5 points)

What is the decimal value of the expression `0b10110100 & 0b00001111` in C?

- A) 4
- B) 180
- C) 15
- D) 52

- **Correct Answer:** A
- **Distractor Analysis:**
  - A) `0b10110100` = 180. `0b00001111` = 15 (mask for lower nibble). Bitwise AND: `10110100 & 00001111 = 00000100` = 4. The upper nibble is zeroed; the lower nibble of 180 is `0100` = 4.
  - B) 180 is the value of the first operand before masking. AND cannot produce a result larger than either operand.
  - C) 15 is the value of the mask (second operand). The AND result depends on the corresponding bits of the first operand — not all lower bits of 180 are set, so the result is not 15.
  - D) 52 is not derivable from these two operands. `10110100 & 00001111 = 00000100` = 4, not 52.

---

### Question 14 (5 points)

Which of the following is the safest replacement for `strcpy(dest, src)` in embedded C when `dest` is a fixed-size buffer of length `N`?

- A) `memcpy(dest, src, N);`
- B) `sprintf(dest, "%s", src);`
- C) `strncpy(dest, src, N - 1); dest[N - 1] = '\0';`
- D) `gets(dest);`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `memcpy` copies exactly `N` bytes regardless of null terminator position. If `src` is shorter than `N`, garbage bytes are copied. If `src` is longer, the buffer is still truncated at `N` bytes but no null terminator is guaranteed.
  - B) `sprintf` with `%s` is no safer than `strcpy` — it writes until the null terminator of `src` with no bounds checking on `dest`. An oversized `src` causes the same overflow.
  - C) `strncpy(dest, src, N - 1)` copies at most `N - 1` characters, preventing overflow. The explicit `dest[N - 1] = '\0'` ensures null termination even if `src` was exactly `N - 1` characters long (since `strncpy` does not guarantee null termination when the limit is reached).
  - D) `gets()` is the most dangerous C standard library function — it performs no bounds checking at all and was removed from the C11 standard. It is never a safe replacement.

---

### Question 15 (5 points)

In MicroPython, which method correctly reads a single byte from I2C address `0x76` using a `machine.I2C` object named `i2c`?

- A) `i2c.readfrom(0x76, 1)`
- B) `i2c.recv(1, addr=0x76)`
- C) `i2c.read(0x76)`
- D) `i2c.transfer(0x76, bytearray(1))`

- **Correct Answer:** A
- **Distractor Analysis:**
  - A) `i2c.readfrom(addr, nbytes)` is the standard MicroPython `machine.I2C` method for reading `nbytes` bytes from the device at `addr`. It returns a `bytes` object of length `nbytes`.
  - B) `recv()` is a method on `machine.UART`, not `machine.I2C`. MicroPython I2C uses `readfrom` and `writeto`, not `recv` and `send`.
  - C) `i2c.read()` is not a method on the MicroPython `machine.I2C` object. This would raise an `AttributeError`.
  - D) `transfer()` is not a standard MicroPython I2C method. It resembles the CircuitPython API, which is a separate MicroPython variant with a different API surface.

---

### Question 16 (5 points)

What is the output of the following C code on an 8-bit AVR microcontroller?

```c
uint8_t x = 200;
x += 100;
```

- A) 300
- B) 255 (saturates at maximum)
- C) 44
- D) Undefined behavior — the addition is prohibited by the C standard.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `uint8_t` cannot represent 300. The result wraps modulo 256.
  - B) Unsigned integer arithmetic in C uses modular (wrap-around) arithmetic, not saturation. Saturation would require explicit clamping code such as `if (x > 155) x = 255; else x += 100;`.
  - C) 200 + 100 = 300. 300 mod 256 = 44. The result stored in `x` is 44. This is defined unsigned overflow behavior under the C standard.
  - D) Unsigned integer overflow is explicitly well-defined in the C standard as modular arithmetic modulo 2^N. Only signed integer overflow is undefined behavior.

---

### Question 17 (5 points)

Why must variables shared between an Interrupt Service Routine (ISR) and the main program be declared `volatile` in C?

- A) To allocate the variable in interrupt-safe RAM, which is protected from race conditions by hardware.
- B) To prevent the compiler from optimizing away reads of the variable in the main program, ensuring the main program always sees the value written by the ISR.
- C) To grant the ISR write permission to the variable, which is otherwise read-only from interrupt context.
- D) To double-buffer the variable so the ISR and main program each access a separate copy.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) There is no "interrupt-safe RAM" hardware partition on AVR or ARM MCUs. `volatile` is a compiler directive, not a hardware memory attribute.
  - B) Without `volatile`, the compiler may determine that the main program never writes a flag variable and optimize the `while (!flag)` spin-wait into an infinite loop — it never re-reads `flag` from RAM. `volatile` forces every access to actually read/write the memory location, ensuring the ISR's write is visible to the main loop.
  - C) C variables have no concept of per-context access permissions enforced by `volatile`. Both the main program and the ISR share the same memory address.
  - D) `volatile` does not create double-buffering. Both contexts access the same single memory location — that is exactly why race conditions must be managed separately with atomic operations or interrupt disable/enable guards.

---

### Question 18 (5 points)

Which MicroPython module provides the `sleep_ms()` and `ticks_ms()` functions for millisecond-level timing?

- A) `time`
- B) `machine`
- C) `utime`
- D) `os`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) The standard Python `time` module is available in CPython but not in all MicroPython builds. On hardware targets, `utime` is the standard module providing millisecond and microsecond timing functions.
  - B) `machine` provides hardware peripherals (Pin, ADC, I2C, SPI, Timer) but not general-purpose timing functions like `sleep_ms()` or `ticks_ms()`.
  - C) `utime` is the MicroPython timing module. It provides `utime.sleep()`, `utime.sleep_ms()`, `utime.sleep_us()`, `utime.ticks_ms()`, `utime.ticks_diff()`, and related functions for measuring elapsed time without integer overflow issues.
  - D) `os` provides filesystem and operating system interface functions. It has no timing capabilities.

---

### Question 19 (5 points)

A production IoT device ships with a Wi-Fi password stored as a plain string literal in compiled firmware: `const char WIFI_PASS[] = "CorpNet2024!";`. What tool can an attacker use to extract this credential from the firmware binary file without executing the firmware?

- A) `gdb` — the GNU debugger, which requires the firmware to be running on the device.
- B) `objdump` with disassembly mode, which requires the source code to decompile.
- C) `strings` — a standard Unix utility that extracts printable character sequences from any binary file, regardless of format.
- D) `openssl` — which decrypts the credential from the firmware's encrypted storage section.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `gdb` requires a running target or a core dump. It cannot extract static strings from an offline binary without connecting to the live firmware.
  - B) `objdump` can disassemble machine code but requires the ELF symbol table for meaningful output. `strings` requires no format knowledge and works on raw flash dumps.
  - C) The `strings` utility scans any binary file for sequences of printable ASCII characters above a minimum length threshold. Hardcoded string literals — passwords, API keys, URLs — are stored verbatim in the firmware's `.rodata` section and are trivially extracted. This is why hardcoded credentials violate OWASP IoT Top 10 item 1.
  - D) Plain string literals are not encrypted in standard firmware builds. `openssl` decrypts data using a key — it cannot extract plaintext credentials that were never encrypted to begin with.

---

### Question 20 (5 points)

Which of the following best describes the purpose of a watchdog timer (WDT) in an embedded IoT device?

- A) It measures elapsed time for scheduling sensor readings at precise intervals.
- B) It automatically resets the microcontroller if the firmware fails to "pet" (reset) the watchdog within a configured timeout period, recovering from hung or crashed firmware states.
- C) It monitors the I2C bus for unexpected slave devices and raises an interrupt if an unknown address responds.
- D) It prevents the CPU from entering deep sleep mode during active data transmission.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Interval scheduling is performed by `millis()`, hardware timers, or `utime.ticks_ms()`. The watchdog is a fault recovery mechanism, not a scheduler.
  - B) A watchdog timer counts down continuously. The firmware must periodically reset (pet) the counter before it reaches zero. If the firmware hangs, crashes, or enters an infinite loop, the counter expires and the hardware forces a system reset. This is a fundamental reliability mechanism in production IoT firmware.
  - C) I2C bus monitoring is not a watchdog function. Watchdog timers have no awareness of bus activity. Detecting unexpected I2C devices is an application-level security check.
  - D) Deep sleep entry is controlled by explicit power management API calls (e.g., `machine.deepsleep()` in MicroPython). The watchdog does not govern sleep mode transitions.

---

End of Quiz – Module 03
