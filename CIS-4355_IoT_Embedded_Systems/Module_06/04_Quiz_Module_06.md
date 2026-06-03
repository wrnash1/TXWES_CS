# Quiz: Module 06 — Microcontroller Programming

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Format:** 10 questions, multiple choice, 4 options each

---

## Question 1

What is the maximum SRAM capacity of an Arduino Uno (ATmega328P)?

- A) 32 KB
- B) 8 KB
- C) 2 KB
- D) 512 bytes

### Answer 1

Correct Answer: C

### Distractor Analysis 1

- A is incorrect — 32 KB is the Uno's flash (program storage) capacity, not SRAM.
- B is incorrect — 8 KB is the SRAM of the ATmega2560 used in the Arduino Mega.
- C is correct — The ATmega328P has exactly 2,048 bytes (2 KB) of SRAM for variables, stack, and heap.
- D is incorrect — 512 bytes is too small; it would not be sufficient even for basic sketch startup.

---

## Question 2

Which keyword must be used when declaring a variable that is modified inside an Interrupt Service Routine?

- A) `static`
- B) `volatile`
- C) `const`
- D) `register`

### Answer 2

Correct Answer: B

### Distractor Analysis 2

- A is incorrect — `static` preserves a local variable's value between function calls but does not prevent compiler register caching.
- B is correct — `volatile` tells the compiler to always read the variable from memory, never cache it in a register, ensuring ISR updates are visible to main code.
- C is incorrect — `const` marks a variable as read-only, opposite of what is needed for ISR-modified state.
- D is incorrect — `register` is a deprecated hint asking the compiler to use a CPU register, which is precisely what you want to avoid for ISR-shared variables.

---

## Question 3

On an Arduino Uno, which function call correctly configures pin 7 as a digital input with the internal pull-up resistor enabled?

- A) `pinMode(7, INPUT);`
- B) `pinMode(7, OUTPUT);`
- C) `pinMode(7, INPUT_PULLUP);`
- D) `digitalWrite(7, HIGH);`

### Answer 3

Correct Answer: C

### Distractor Analysis 3

- A is incorrect — `INPUT` leaves the pin floating with no pull-up; it requires an external resistor and produces unreliable readings when nothing is connected.
- B is incorrect — `OUTPUT` drives the pin actively and would damage hardware connected to it as an input.
- C is correct — `INPUT_PULLUP` configures the pin as an input and connects the internal ~20–50 kΩ pull-up resistor to VCC.
- D is incorrect — `digitalWrite(7, HIGH)` can enable the pull-up when a pin is already set as INPUT, but calling it alone without a prior `pinMode` call is unreliable and not the correct approach.

---

## Question 4

A 10-bit ADC reads a value of 512 on an Arduino Uno with a 5V reference. What is the approximate input voltage?

- A) 2.00 V
- B) 2.50 V
- C) 2.56 V
- D) 3.33 V

### Answer 4

Correct Answer: B

### Distractor Analysis 4

- A is incorrect — 2.00V corresponds to an ADC reading of approximately 409.
- B is correct — Using the formula `V = (512 / 1023) × 5.0 ≈ 2.502V`, which rounds to 2.50V.
- C is incorrect — 2.56V results from a common off-by-one error dividing by 1000 instead of 1023; the correct divisor is 1023 for a 10-bit ADC.
- D is incorrect — 3.33V would require a reading of approximately 682 on a 10-bit ADC with 5V reference.

---

## Question 5

What is the purpose of the `F()` macro in Arduino code such as `Serial.println(F("Hello"));`?

- A) It converts the string to a floating-point number before printing
- B) It stores the string in flash memory instead of copying it to SRAM
- C) It forces the Serial port to flush its buffer immediately
- D) It increases the baud rate for faster serial transmission

### Answer 5

Correct Answer: B

### Distractor Analysis 5

- A is incorrect — The `F()` macro has nothing to do with floating-point conversion; that is a common misconception based on the letter F.
- B is correct — On AVR targets, `F()` wraps a string literal with `PROGMEM` storage, keeping it in flash and preventing it from consuming SRAM at runtime.
- C is incorrect — `Serial.flush()` is the function that waits for outgoing serial data to complete; `F()` does not affect serial buffering.
- D is incorrect — Baud rate is set only in `Serial.begin()`; the `F()` macro has no effect on transmission speed.

---

## Question 6

Which PWM-capable pins are available on the Arduino Uno?

- A) Pins 2, 4, 6, 8, 10, 12
- B) Pins 3, 5, 6, 9, 10, 11
- C) Pins 1, 3, 5, 7, 9, 11
- D) All 14 digital pins

### Answer 6

Correct Answer: B

### Distractor Analysis 6

- A is incorrect — Pins 2, 4, 8, and 12 are general digital I/O only; they are not connected to hardware timer compare units.
- B is correct — The ATmega328P's three timers expose compare outputs on pins 3, 5, 6, 9, 10, and 11; these are marked with a tilde (~) on the Uno board.
- C is incorrect — This is a plausible-looking odd-numbered pattern but does not match the actual timer output pin assignments.
- D is incorrect — Only 6 of the 14 digital pins have hardware PWM capability on the Uno.

---

## Question 7

On the ESP32, what attribute must be added to an ISR function declaration to ensure it executes correctly when the flash cache is busy?

- A) `PROGMEM`
- B) `ICACHE_RAM_ATTR`
- C) `IRAM_ATTR`
- D) `__interrupt__`

### Answer 7

Correct Answer: C

### Distractor Analysis 7

- A is incorrect — `PROGMEM` is an AVR-specific directive for storing data in flash; it has no meaning on the ESP32 and does not affect ISR placement.
- B is incorrect — `ICACHE_RAM_ATTR` is an older ESP8266 attribute sometimes seen in legacy code; the current ESP32 IDF and Arduino core use `IRAM_ATTR`.
- C is correct — `IRAM_ATTR` places the function in internal RAM (IRAM), which is always accessible even when the SPI flash cache is disabled during a flash write or cache miss.
- D is incorrect — `__interrupt__` is not a valid GCC or ESP32 attribute; it appears in some other embedded toolchains but not in the ESP32 ecosystem.

---

## Question 8

What is the clock speed of the ESP32 Xtensa LX6 processor at its maximum configuration?

- A) 16 MHz
- B) 80 MHz
- C) 160 MHz
- D) 240 MHz

### Answer 8

Correct Answer: D

### Distractor Analysis 8

- A is incorrect — 16 MHz is the clock speed of the Arduino Uno's ATmega328P, not the ESP32.
- B is incorrect — 80 MHz is a valid ESP32 clock setting but is not the maximum; it is often used to reduce power consumption.
- C is incorrect — 160 MHz is another valid intermediate ESP32 clock setting but still not the maximum.
- D is correct — The ESP32 Xtensa LX6 dual-core processor can be configured to run at up to 240 MHz, its maximum rated frequency.

---

## Question 9

Which of the following statements about `delay()` is correct in the context of embedded Arduino programming?

- A) `delay()` uses a hardware timer interrupt and does not block the CPU
- B) `delay()` is safe to call inside an Interrupt Service Routine
- C) `delay()` blocks the CPU for the specified milliseconds and prevents other code from running
- D) `delay()` on the ESP32 puts the CPU into deep sleep to save power

### Answer 9

Correct Answer: C

### Distractor Analysis 9

- A is incorrect — `delay()` does rely on the timer0 overflow interrupt to count milliseconds, but the CPU spins in a busy-wait loop and is fully blocked from executing other code during the delay.
- B is incorrect — Calling `delay()` inside an ISR is explicitly prohibited because `delay()` itself depends on the timer interrupt being serviced, causing a deadlock.
- C is correct — `delay()` is a blocking call; the processor idles in a loop checking `millis()` until the specified time has elapsed, preventing any other loop() code from executing.
- D is incorrect — `delay()` does not invoke any low-power sleep mode; `esp_deep_sleep_start()` is the correct ESP32 deep sleep function.

---

## Question 10

In a FreeRTOS task on the ESP32, which function should replace `delay(500)` to yield the CPU to other tasks while waiting?

- A) `sleep(500)`
- B) `yield()`
- C) `vTaskDelay(pdMS_TO_TICKS(500))`
- D) `taskYIELD()`

### Answer 10

Correct Answer: C

### Distractor Analysis 10

- A is incorrect — `sleep(500)` is a POSIX function measured in seconds (not milliseconds) that does not exist in the FreeRTOS/ESP32 Arduino environment.
- B is incorrect — `yield()` in the Arduino framework triggers a single cooperative scheduler pass but does not block for a specified duration; it would create a busy-spin rather than a timed delay.
- C is correct — `vTaskDelay(pdMS_TO_TICKS(500))` suspends the calling task for 500 milliseconds while allowing the FreeRTOS scheduler to run other tasks, making it the non-blocking equivalent of `delay()` in a multi-task environment.
- D is incorrect — `taskYIELD()` forces an immediate context switch to another ready task but does not introduce any time delay; the current task would be rescheduled immediately if it is the highest-priority ready task.
