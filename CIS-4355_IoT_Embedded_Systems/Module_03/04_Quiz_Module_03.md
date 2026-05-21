# Quiz: Module 03 - Embedded Programming – C and MicroPython Basics
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Why is static memory allocation preferred over dynamic allocation (malloc) in high-reliability embedded systems?
*   A) Static memory runs slower than heap-allocated memory on ARM Cortex-M cores.
*   B) Dynamic allocation risks heap fragmentation and runtime memory exhaustion, causing unpredictable crashes.
*   C) The C language does not support dynamic memory allocation on any platform.
*   D) Pointers are not allowed in safety-critical embedded code under any standard.
*   **Correct Answer:** B) Dynamic allocation risks heap fragmentation and runtime memory exhaustion, causing unpredictable crashes.
*   **Distractor Analysis:**
    *   *Why correct:* Microcontrollers have tiny RAM; heap fragmentation over long uptimes can trigger out-of-memory failures that are impossible to predict at compile time.
    *   Dynamic memory is supported in C but avoided in embedded code because failures are non-deterministic and hard to test exhaustively.

---

**Question 2**
Which of the following is the most accurate definition of **register mapping** in embedded C programming?
*   A) A technique of accessing microcontroller hardware peripheral control registers directly via their memory-mapped I/O addresses using volatile pointer casts.
*   B) A compiler optimization that places frequently used variables into CPU cache to reduce RAM access latency.
*   C) The process of assigning unique I2C bus addresses to multiple sensors sharing the same SDA/SCL lines.
*   D) A Python decorator that maps function calls to GPIO pin toggle events on a Raspberry Pi.
*   **Correct Answer:** A) A technique of accessing microcontroller hardware peripheral control registers directly via their memory-mapped I/O addresses using volatile pointer casts.
*   **Distractor Analysis:**
    *   *Why A is correct:* Register mapping lets C code set individual peripheral control bits (e.g., enabling a UART transmitter) by writing to the documented hardware register address, avoiding overhead from HAL abstraction layers.
    *   *Why B is incorrect:* This describes CPU caching, which is a microarchitecture optimization, not a programming technique under developer control on most MCUs.
    *   *Why C is incorrect:* This describes I2C device addressing, which is a hardware configuration, not register mapping.
    *   *Why D is incorrect:* Python decorators are a language feature; they are unrelated to memory-mapped hardware register access.

---

**Question 3**
An embedded C developer writes `char buf[16]; strcpy(buf, userInput);` where `userInput` is received from a network packet. Which vulnerability does this introduce?
*   A) Integer overflow in the loop counter used to terminate the copy.
*   B) Buffer overflow: if userInput exceeds 15 bytes, strcpy writes past the end of buf, corrupting adjacent stack memory.
*   C) Race condition: two threads may call strcpy simultaneously on the same buffer.
*   D) Null pointer dereference: strcpy returns NULL when the source string is empty.
*   **Correct Answer:** B) Buffer overflow: if userInput exceeds 15 bytes, strcpy writes past the end of buf, corrupting adjacent stack memory.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* strcpy does not use an explicit integer loop counter exposed to the caller; the overflow risk is in destination bounds, not a counter variable.
    *   *Why B is correct:* strcpy performs no bounds checking; input longer than 15 bytes (plus null terminator) overwrites adjacent stack variables or the return address, enabling code execution attacks.
    *   *Why C is incorrect:* A race condition requires concurrent access; this code is a sequential single-threaded buffer overflow regardless of threading.
    *   *Why D is incorrect:* strcpy does not return NULL on empty input; it copies zero bytes and null-terminates normally.

---

**Question 4**
Which bitwise operation correctly clears bit 3 of a uint8_t register variable `reg` without affecting any other bits?
*   A) reg = reg | (1 << 3);
*   B) reg = reg & ~(1 << 3);
*   C) reg = reg ^ (1 << 3);
*   D) reg = reg >> 3;
*   **Correct Answer:** B) reg = reg & ~(1 << 3);
*   **Distractor Analysis:**
    *   *Why A is incorrect:* OR sets a bit to 1; it cannot clear a bit to 0.
    *   *Why B is correct:* `~(1 << 3)` produces a mask with all bits set except bit 3; ANDing with reg forces bit 3 to 0 while leaving all other bits unchanged.
    *   *Why C is incorrect:* XOR toggles the bit — if bit 3 was already 0, XOR would set it to 1.
    *   *Why D is incorrect:* A right-shift moves all bits, destroying the original value rather than clearing a single bit in place.

---

**Question 5**
When designing an IoT firmware update mechanism in C, which practice best mitigates the risk of an attacker delivering a malicious firmware image over the network?
*   A) Compressing the firmware binary with gzip before transmission to reduce its size.
*   B) Verifying a cryptographic signature (e.g., ECDSA over SHA-256) on the received firmware image before writing it to flash.
*   C) Storing the firmware update URL in a compile-time constant to prevent runtime URL manipulation.
*   D) Using dynamic memory allocation (malloc) to buffer the incoming image for flexible sizing.
*   **Correct Answer:** B) Verifying a cryptographic signature (e.g., ECDSA over SHA-256) on the received firmware image before writing it to flash.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Compression reduces size but provides no authentication — an attacker can compress a malicious image equally.
    *   *Why B is correct:* A signature check with a key burned into the device ensures only firmware signed by the legitimate manufacturer can be installed, blocking unsigned or tampered images.
    *   *Why C is incorrect:* A hardcoded URL prevents runtime redirection but does not validate that the content at that URL is authentic or unmodified.
    *   *Why D is incorrect:* Dynamic allocation introduces memory fragmentation risk and does not address firmware authenticity; static buffers with signature checks are the secure pattern.
