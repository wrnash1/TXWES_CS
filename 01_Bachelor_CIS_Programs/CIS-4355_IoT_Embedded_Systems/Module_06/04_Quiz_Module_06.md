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

---

## Question 11 (5 points)

An Arduino Uno sketch calls `analogWrite(9, 128)`. What approximate average voltage appears at pin 9?

- A) 1.28 V
- B) 2.5 V
- C) 3.3 V
- D) 5.0 V

### Answer 11

Correct Answer: B

### Distractor Analysis 11

- A is incorrect — 1.28 V would require a duty cycle of approximately 25.6%, corresponding to a value near 65, not 128.
- B is correct — `analogWrite` accepts values 0–255. A value of 128 is approximately 50% duty cycle. Average voltage = 0.50 × 5.0 V = 2.5 V.
- C is incorrect — 3.3 V is the ESP32 supply voltage and would correspond to a duty cycle of 66%, not 50%.
- D is incorrect — 5.0 V corresponds to full duty cycle (analogWrite value 255), not 128.

---

## Question 12 (5 points)

What is the primary difference between the `Serial.print()` and `Serial.println()` functions on an Arduino?

- A) `Serial.print()` sends data at 9600 baud; `Serial.println()` sends at 115200 baud.
- B) `Serial.println()` appends a carriage-return and newline (`\r\n`) after the output; `Serial.print()` does not.
- C) `Serial.print()` sends binary data; `Serial.println()` converts all values to ASCII text.
- D) `Serial.println()` flushes the hardware UART transmit buffer after each call; `Serial.print()` does not.

### Answer 12

Correct Answer: B

### Distractor Analysis 12

- A is incorrect — Both functions use the same baud rate configured in `Serial.begin()`. The baud rate is a property of the serial port, not the individual print function.
- B is correct — `Serial.println()` is a convenience wrapper that calls `Serial.print()` then sends `\r\n` (CR+LF). This moves the Serial Monitor cursor to the next line. Both functions otherwise behave identically for value formatting.
- C is incorrect — Both `Serial.print()` and `Serial.println()` convert numeric values to human-readable ASCII text by default. `Serial.write()` is the function that sends raw binary bytes.
- D is incorrect — Neither `Serial.print()` nor `Serial.println()` automatically flush the UART buffer. `Serial.flush()` is the explicit flush function.

---

## Question 13 (5 points)

A developer writes `int sensorVal = analogRead(A0);` on an Arduino Uno, then checks `if (sensorVal > 1024)`. Under what condition can this comparison ever evaluate to true?

- A) When the analog input voltage exceeds 5V, the ADC saturates and returns values above 1023.
- B) Never — the Uno's 10-bit ADC returns values from 0 to 1023 inclusive; no valid reading can exceed 1023.
- C) When the ADC reference voltage is reduced below 5V using `analogReference()`, causing readings to scale above 1023.
- D) When the `int` variable overflows if several readings are added together before the comparison.

### Answer 13

Correct Answer: B

### Distractor Analysis 13

- A is incorrect — Connecting a voltage above 5V to an analog pin damages the ATmega328P; the ADC does not return values above 1023 under normal operation. The pin has protection diodes that clamp the voltage.
- B is correct — A 10-bit ADC produces 2^10 = 1024 discrete steps: 0 through 1023. The maximum possible return value from `analogRead()` is 1023. The comparison `sensorVal > 1024` can never be true for a valid Uno ADC reading.
- C is incorrect — Reducing the reference voltage with `analogReference()` causes the same input voltage to map to a higher integer value, potentially reaching 1023 at a lower voltage — but still never exceeding 1023.
- D is incorrect — The question is about a single `analogRead()` result, not an accumulated sum. A single reading stored in `int` cannot exceed 1023.

---

## Question 14 (5 points)

On the ESP32, why should GPIO pins 6 through 11 be avoided for general-purpose I/O in most applications?

- A) These pins operate at 1.8 V logic level and cannot drive standard 3.3 V peripherals.
- B) These pins are internally connected to the SPI flash memory chip and modifying them can corrupt the firmware or crash the device.
- C) These pins have no internal pull-up resistors and require external 10 kΩ resistors on every circuit.
- D) These pins are reserved by the Bluetooth hardware and become unavailable whenever BLE is active.

### Answer 14

Correct Answer: B

### Distractor Analysis 14

- A is incorrect — ESP32 GPIO pins operate at 3.3 V logic. Pins 6–11 are not at a different voltage level; the issue is their internal connection, not their voltage.
- B is correct — On most ESP32 module variants (WROOM, WROVER), GPIO 6–11 are connected to the integrated SPI flash memory (CLK, CMD, and DATA lines). Driving them with application code interferes with flash access and causes crashes, watchdog resets, or flash corruption.
- C is incorrect — The ESP32 has configurable internal pull-up and pull-down resistors on most GPIO pins. Pins 6–11 are avoided for connectivity reasons, not for lack of pull resistors.
- D is incorrect — Bluetooth uses dedicated RF circuitry, not GPIO pins 6–11. The Wi-Fi and BLE radios do not share GPIO with the SPI flash bus.

---

## Question 15 (5 points)

Which statement correctly describes the behavior of `noInterrupts()` and `interrupts()` when used to protect a multi-byte variable read on an Arduino Uno?

- A) `noInterrupts()` disables only external GPIO interrupts while allowing timer interrupts to continue.
- B) `noInterrupts()` disables all maskable hardware interrupts globally; `interrupts()` re-enables them, creating an atomic section for safely reading multi-byte variables shared with ISRs.
- C) `noInterrupts()` has no effect on AVR; only the `cli()` assembly instruction can disable interrupts.
- D) `noInterrupts()` must be paired with a mutex rather than `interrupts()` to prevent priority inversion.

### Answer 15

Correct Answer: B

### Distractor Analysis 15

- A is incorrect — `noInterrupts()` globally disables all maskable hardware interrupts on the AVR, including timer interrupts. It is not selective by interrupt source.
- B is correct — On AVR, `noInterrupts()` executes the `cli` assembly instruction, disabling the global interrupt enable flag. `interrupts()` executes `sei`. The brief window between them is an atomic critical section — an ISR cannot preempt a read of a multi-byte `volatile` variable (such as `uint32_t`) during this window, preventing torn reads.
- C is incorrect — `noInterrupts()` is the Arduino wrapper for `cli()`. They are functionally identical on AVR. The statement is false.
- D is incorrect — Mutexes are an RTOS concurrency primitive used in multi-threaded environments. On the single-threaded AVR Arduino model, `noInterrupts()`/`interrupts()` is the correct and complete solution for ISR-to-main synchronization.

---

## Question 16 (5 points)

A developer notices that their Uno sketch gradually slows down and eventually freezes after several hours of operation. The sketch uses `String` objects to build and concatenate sensor log messages. What is the most likely cause?

- A) The ATmega328P's crystal oscillator drifts over time, reducing the clock speed gradually.
- B) The `String` class dynamically allocates and reallocates heap memory; repeated small allocations fragment the 2 KB SRAM heap until no contiguous block is large enough to allocate, causing undefined behavior or a crash.
- C) `String` objects are stored in flash, and after 10,000 write cycles the flash sector becomes read-only.
- D) The `+` operator on `String` objects enables hardware floating-point acceleration, which overheats the AVR after extended use.

### Answer 16

Correct Answer: B

### Distractor Analysis 16

- A is incorrect — AVR crystal oscillators are stable to ±50 ppm over temperature. Clock drift does not cause gradual slowdown or freezing over hours of operation.
- B is correct — Each `String` concatenation (e.g., `str += value`) allocates a new, larger heap block and frees the old one. On a 2 KB SRAM AVR, this quickly fragments the heap. Over hours of operation, the allocator cannot find a contiguous block large enough for the next `String`, the allocation silently fails or returns null, and the sketch corrupts memory and eventually crashes. This is the most commonly cited reason to avoid `String` on constrained AVR devices.
- C is incorrect — `String` objects are runtime heap-allocated variables in SRAM, not in flash. Flash write endurance applies to EEPROM writes and OTA firmware updates, not to SRAM `String` operations.
- D is incorrect — The AVR ATmega328P has no hardware floating-point unit and no thermal protection circuitry. The `String` class uses integer operations internally, not floating-point.

---

## Question 17 (5 points)

What does the `map(value, fromLow, fromHigh, toLow, toHigh)` Arduino function return when `value` is outside the `fromLow`–`fromHigh` range?

- A) It clamps the return value to `toLow` or `toHigh` to prevent out-of-range output.
- B) It returns -1 to indicate an error condition.
- C) It extrapolates linearly beyond the output range, potentially returning values outside `toLow`–`toHigh`.
- D) It wraps the value modulo `toHigh` to stay within the output range.

### Answer 17

Correct Answer: C

### Distractor Analysis 17

- A is incorrect — `map()` does not clamp. This is a common misconception. To clamp the output, you must call `constrain()` after `map()`.
- B is incorrect — `map()` never returns -1 as an error code. It performs the linear extrapolation regardless of whether the input is within the declared range.
- C is correct — The Arduino `map()` function performs a linear transformation without bounds checking. If `value` is below `fromLow` or above `fromHigh`, the function extrapolates — returning a value below `toLow` or above `toHigh` respectively. This is intentional and documented behavior.
- D is incorrect — `map()` uses no modulo arithmetic. It applies a single linear formula: `(value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow`.

---

## Question 18 (5 points)

The ESP32 has two Xtensa LX6 cores. Which core does the `loop()` function and most Arduino sketch code run on by default?

- A) Core 0, leaving Core 1 reserved for the radio (Wi-Fi/BT) stack.
- B) Core 1, with Core 0 typically handling the Wi-Fi/BT radio stack and system tasks.
- C) Both cores simultaneously in a symmetric multiprocessing arrangement for all sketch code.
- D) The Arduino framework dynamically migrates the `loop()` function between cores based on load.

### Answer 18

Correct Answer: B

### Distractor Analysis 18

- A is incorrect — The assignment is reversed. The Arduino `loop()` runs on Core 1 in the default ESP32 Arduino framework configuration.
- B is correct — By default in the ESP32 Arduino framework, the Arduino `setup()` and `loop()` functions run on Core 1 (also called the Application Core). Core 0 (the Protocol Core) runs the Wi-Fi and Bluetooth stack and FreeRTOS system tasks. Developers can explicitly pin user tasks to Core 0 or Core 1 using `xTaskCreatePinnedToCore()`.
- C is incorrect — The Arduino `loop()` function runs on a single core. Symmetric multiprocessing for sketch code requires explicit FreeRTOS task creation with core pinning.
- D is incorrect — The ESP32 scheduler does not dynamically migrate tasks between cores. Core affinity is set at task creation time.

---

## Question 19 (5 points)

A sketch must read the potentiometer ADC value and decide whether to turn on a fan motor that draws 800 mA at 12 V. What component is required between the Arduino GPIO pin and the fan motor, and why?

- A) A 330 Ω current-limiting resistor — to limit current to 40 mA through the GPIO pin.
- B) A logic-level MOSFET or transistor — because the GPIO pin can source at most 40 mA and the motor requires 800 mA at a voltage the Arduino cannot supply.
- C) A 10 kΩ pull-up resistor — to boost the GPIO output voltage to 12 V for the motor.
- D) A capacitor — to filter ADC noise before the motor control signal reaches the motor winding.

### Answer 19

Correct Answer: B

### Distractor Analysis 19

- A is incorrect — A current-limiting resistor would restrict current to the motor, preventing it from operating at rated torque, and would still allow 12 V to be applied to a 5 V GPIO pin. Resistors do not isolate voltage levels or amplify current.
- B is correct — The Arduino GPIO pin can source or sink at most 40 mA at 5 V. The motor requires 800 mA at 12 V — 20 times more current than the pin can provide, at more than double the voltage. A logic-level N-channel MOSFET (such as the IRLZ44N) allows a 5 V gate signal to switch a 12 V, 800 mA load using an external power supply, protecting the microcontroller.
- C is incorrect — A pull-up resistor connects a signal to a supply voltage and affects logic level thresholds. It cannot step up voltage from 5 V to 12 V, and it provides no current amplification.
- D is incorrect — Capacitors are used for power supply decoupling and filter analog signals. They do not provide the current amplification or voltage isolation required for motor control.

---

## Question 20 (5 points)

What does `digitalPinToInterrupt(pin)` return, and why must it be used instead of the raw pin number in `attachInterrupt()`?

- A) It returns the GPIO voltage level (HIGH or LOW) at the pin, used for edge-triggered interrupt configuration.
- B) It returns the hardware interrupt vector number corresponding to the GPIO pin, because interrupt vector numbers do not always equal GPIO pin numbers on Arduino boards.
- C) It returns the pin's PWM channel number, which the interrupt system uses for timer-based triggering.
- D) It converts a BCM pin number to a physical header pin number for Raspberry Pi compatibility.

### Answer 20

Correct Answer: B

### Distractor Analysis 20

- A is incorrect — `digitalPinToInterrupt()` returns a hardware index, not a voltage level. `digitalRead()` is used to read voltage levels.
- B is correct — On the Arduino Uno, only pins 2 and 3 support external interrupts (INT0 and INT1 respectively). `attachInterrupt(0, ...)` means interrupt 0 (pin 2), not pin 0. On other boards (Mega, Micro, ESP32), the mapping is different. `digitalPinToInterrupt(pin)` performs the correct translation for whatever board is being compiled, making the code portable.
- C is incorrect — PWM channels are unrelated to interrupt vector assignment. The two systems are independent peripheral subsystems.
- D is incorrect — `digitalPinToInterrupt()` is an Arduino function with no connection to the Raspberry Pi or BCM numbering. BCM numbering is specific to RPi.GPIO on Raspberry Pi.
