# Video Script: Module 06 — Microcontroller Programming

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Estimated Duration:** 20–24 minutes

**Certification Alignment:** IoT Fundamentals / Embedded Systems

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4355. I'm Professor Nash, and today we are digging into one of the most hands-on topics in this entire course — microcontroller programming.

If you have never written code that directly controls a physical pin on a chip, today changes that. By the end of this video you will understand how to write C and C++ code in the Arduino IDE, how to work with GPIO pins, how to read analog sensors, how to generate PWM signals for motors and LEDs, and how to use interrupts to respond to hardware events in real time.

We will also compare two of the most popular platforms you will use in this course: the classic Arduino Uno and the much more powerful ESP32. Knowing when to reach for each one is a real professional skill.

Let's get started.

---

## SEGMENT 2 — The Arduino IDE and Toolchain (1:30–4:00)

[SHOW HARDWARE: Arduino Uno board side-by-side with ESP32 DevKit on a white background, USB cables attached]

The Arduino IDE is the development environment that made embedded programming accessible to millions of people. When you write code here, a few things happen behind the scenes that are worth understanding.

First, your sketch — that is what Arduino calls a source file — is compiled by a version of GCC, the GNU Compiler Collection, targeting your specific microcontroller architecture. For the Uno, that is AVR. For the ESP32, that is Xtensa LX6 or RISC-V depending on which variant you have.

Second, the IDE links in the Arduino core library, which wraps low-level register operations into friendly function calls like `digitalWrite` and `analogRead`.

Third, the compiled binary is uploaded over USB using a bootloader that lives in a reserved section of flash memory. On the Uno, that bootloader is Optiboot. On the ESP32, it is the Espressif bootloader.

Every Arduino sketch has exactly two required functions:

```cpp
void setup() {
  // Runs once at power-on or reset
}

void loop() {
  // Runs repeatedly, forever
}
```

`setup()` is where you configure pins, initialize serial communication, and connect to hardware. `loop()` is your main execution loop — it runs as fast as the processor allows unless you add delays.

One important thing beginners miss: there is no operating system here. When `loop()` runs, it owns the CPU completely. There is no scheduler, no multitasking, no garbage collector. This is both a strength and a constraint. You have deterministic timing, but you must manage everything yourself.

---

## SEGMENT 3 — C/C++ for Embedded Systems (4:00–6:30)

Let me talk about the language itself. The Arduino ecosystem uses C and C++, but embedded C has important differences from desktop C.

First: memory is extremely tight. An Arduino Uno has only 2 kilobytes of SRAM and 32 kilobytes of flash. That sentence bears repeating — two kilobytes of RAM. A single integer array of 1,000 elements would consume 2 KB all by itself and crash your program.

Second: there is no dynamic memory allocator you should trust. On the Uno, using `malloc` or `new` in a long-running embedded program leads to heap fragmentation. Prefer stack-allocated variables and global arrays of known size.

Third: the `PROGMEM` keyword lets you store read-only data in flash rather than SRAM. For string literals and lookup tables, this is essential on memory-constrained devices.

```cpp
// Storing a string in flash memory on AVR
#include <avr/pgmspace.h>
const char greeting[] PROGMEM = "Hello from flash!";
```

Fourth: data types matter because registers are 8-bit on the Uno. Use `uint8_t`, `uint16_t`, and `uint32_t` from `<stdint.h>` for portable, predictable sizes.

```cpp
uint8_t  sensorId   = 42;      // 8-bit unsigned, 0-255
uint16_t adcReading = 1023;    // 16-bit unsigned
uint32_t timestamp  = 0;       // 32-bit unsigned, good for millis()
```

Fifth: global variables persist across loop iterations. This is how you share state between your main loop and interrupt service routines. Variables modified by ISRs must be declared `volatile`.

```cpp
volatile bool buttonPressed = false;
```

The `volatile` keyword tells the compiler not to cache this variable in a register — always read it fresh from memory, because hardware can change it at any time.

---

## SEGMENT 4 — GPIO: Digital I/O (6:30–9:00)

[SHOW HARDWARE: Arduino Uno with an LED on pin 13 and a pushbutton on pin 2, breadboard visible]

GPIO stands for General-Purpose Input/Output. These are the numbered pins along the edge of your microcontroller board. Each pin can be configured as either an input or an output.

You configure a pin's direction in `setup()` using `pinMode()`:

```cpp
void setup() {
  pinMode(13, OUTPUT);        // LED
  pinMode(2,  INPUT_PULLUP);  // Button with internal pull-up resistor
}
```

`INPUT_PULLUP` is worth understanding. Most microcontrollers have internal resistors that can be connected to the 3.3V or 5V rail. When a button is not pressed, the pin reads HIGH. When pressed and connected to ground, it reads LOW. This eliminates the need for an external pull-up resistor in many circuits.

In `loop()`, you read and write pins:

```cpp
void loop() {
  int buttonState = digitalRead(2);
  if (buttonState == LOW) {
    digitalWrite(13, HIGH);  // LED on
  } else {
    digitalWrite(13, LOW);   // LED off
  }
}
```

Timing note: `digitalWrite` on an Uno takes roughly 4 microseconds because it includes safety checks and pin-mapping lookups. If you need faster GPIO toggling — for bit-banging a protocol — you can write directly to port registers:

```cpp
// AVR direct port manipulation — much faster
PORTB |=  (1 << PB5);   // Set pin 13 HIGH
PORTB &= ~(1 << PB5);   // Set pin 13 LOW
```

This is advanced territory, but it illustrates that the Arduino abstraction has a cost.

---

## SEGMENT 5 — Analog I/O and ADC (9:00–11:00)

Most physical world signals are not digital — they exist on a continuous spectrum. Temperature, light level, pressure — these all produce analog voltages. To read them, microcontrollers have an Analog-to-Digital Converter, or ADC.

The Uno's ADC is 10-bit, meaning it maps 0–5V to the integer range 0–1023. The ESP32's ADC is 12-bit, giving 0–4095 over 0–3.3V.

```cpp
int rawValue = analogRead(A0);
float voltage = rawValue * (5.0 / 1023.0);  // Convert to volts
```

A very common mistake: students assume the ADC is linear and perfectly accurate. In practice, ADC readings have noise — random fluctuations of a few counts. You will deal with this in Module 08 when we cover sensor calibration and smoothing.

For analog output, the Uno does not have a true DAC. Instead it uses PWM, which we cover in the next segment. The ESP32 does have a two-channel true DAC on pins 25 and 26:

```cpp
// ESP32 true DAC output
#include <driver/dac.h>
dac_output_enable(DAC_CHANNEL_1);       // GPIO 25
dac_output_voltage(DAC_CHANNEL_1, 128); // 0-255, maps to 0-3.3V
```

---

## SEGMENT 6 — PWM: Pulse Width Modulation (11:00–13:00)

[SHOW HARDWARE: Arduino with LED fading, oscilloscope screen showing PWM waveform at 50% duty cycle]

PWM is one of the most useful techniques in embedded development. The idea is simple: instead of a true analog voltage, you switch a pin on and off very rapidly. The ratio of on-time to off-time is called the duty cycle.

A 50% duty cycle means the pin is HIGH half the time and LOW half the time. If the switching happens fast enough — typically 500 Hz to 50 kHz — the average voltage seen by a load like an LED or motor is halfway between 0V and 5V.

On the Arduino Uno, pins 3, 5, 6, 9, 10, and 11 support PWM. You use `analogWrite()` with a value from 0 to 255:

```cpp
void loop() {
  // Fade LED up
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(9, brightness);
    delay(10);
  }
  // Fade LED down
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(9, brightness);
    delay(10);
  }
}
```

The ESP32 has a dedicated LEDC PWM peripheral that is much more flexible:

```cpp
// ESP32 LEDC PWM
const int pwmPin     = 18;
const int pwmChannel = 0;
const int pwmFreq    = 5000;  // 5 kHz
const int pwmRes     = 8;     // 8-bit: 0-255

void setup() {
  ledcSetup(pwmChannel, pwmFreq, pwmRes);
  ledcAttachPin(pwmPin, pwmChannel);
}

void loop() {
  ledcWrite(pwmChannel, 128);  // 50% duty cycle
}
```

PWM is used for motor speed control, LED dimming, servo positioning, buzzer tones, and analog signal generation.

---

## SEGMENT 7 — Interrupts (13:00–16:00)

Here is a problem: what if you need to respond to a button press immediately, no matter what the main loop is doing? You cannot just poll in `loop()` — if the loop has a 500ms delay for some other reason, you might miss a 10ms button press entirely.

The solution is hardware interrupts. An interrupt temporarily pauses the main loop, jumps to a special function called an Interrupt Service Routine (ISR), runs it, then resumes where it left off.

On the Arduino Uno, pins 2 and 3 support external interrupts. On the ESP32, any GPIO pin can be an interrupt source.

```cpp
volatile bool buttonFlag = false;

void IRAM_ATTR buttonISR() {
  buttonFlag = true;
}

void setup() {
  Serial.begin(115200);
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), buttonISR, FALLING);
}

void loop() {
  if (buttonFlag) {
    buttonFlag = false;
    Serial.println("Button press detected!");
  }
}
```

Four critical ISR rules you must memorize:

**Rule 1:** ISRs must be short. Do not read sensors or send serial data inside an ISR. Set a flag, then handle it in `loop()`.

**Rule 2:** Variables shared between ISRs and main code must be `volatile`.

**Rule 3:** On the ESP32, ISRs must be placed in IRAM using the `IRAM_ATTR` attribute, so they can execute even when flash is busy with other operations.

**Rule 4:** Avoid `delay()` inside ISRs — it relies on the SysTick timer, which itself uses interrupts.

Timer interrupts fire on a schedule rather than in response to a pin event. These are excellent for periodic tasks like sampling a sensor every 100 milliseconds without blocking the main loop.

---

## SEGMENT 8 — ESP32 vs Arduino Comparison (16:00–19:00)

[SHOW HARDWARE: Side-by-side ESP32 DevKit V1 and Arduino Uno R3, labels pointing to key components]

Let's do a direct comparison between the two platforms you will use most in this course.

The Arduino Uno uses an ATmega328P microcontroller running at 16 MHz with a single core. It has 2 KB of SRAM, 32 KB of flash, and 1 KB of EEPROM. It runs at 5V. It has 14 digital I/O pins and 6 analog input pins. No wireless connectivity at all.

The ESP32 uses a dual-core Xtensa LX6 processor running at up to 240 MHz. It has 520 KB of SRAM, typically 4 MB of flash, and a wide array of peripherals. It runs at 3.3V. It has up to 34 configurable GPIO pins, built-in Wi-Fi 802.11 b/g/n, Bluetooth 4.2 including BLE, a touch-sensing peripheral, a hall effect sensor, and two DAC channels.

When should you use each?

Use Arduino Uno when:

- You need 5V logic compatibility with older sensors
- The task is simple and power budget is generous
- You are learning fundamentals without connectivity complexity
- You need extremely predictable timing on a single task

Use ESP32 when:

- You need Wi-Fi or Bluetooth connectivity
- You need more processing power for FFT, encryption, or signal processing
- You have multiple concurrent tasks that benefit from dual-core operation
- You need more GPIO pins or advanced peripherals

One critical difference: the ESP32 runs FreeRTOS under the hood. This means you can create actual tasks with priorities and stack sizes, rather than relying on a single `loop()` function:

```cpp
// ESP32 FreeRTOS task
void sensorTask(void *parameter) {
  while (true) {
    int reading = analogRead(34);
    Serial.println(reading);
    vTaskDelay(100 / portTICK_PERIOD_MS);  // Non-blocking 100ms delay
  }
}

void setup() {
  Serial.begin(115200);
  xTaskCreatePinnedToCore(sensorTask, "SensorTask", 10000, NULL, 1, NULL, 1);
}

void loop() {
  // Core 0 — can run independently
}
```

This is fundamentally more powerful than the Arduino single-loop model.

---

## SEGMENT 9 — Memory Constraints and Best Practices (19:00–21:30)

Memory management in embedded systems is a survival skill. Let me give you a quick checklist.

Always monitor SRAM usage. The Arduino IDE shows flash usage but not always SRAM. Use this function to check free heap at runtime:

```cpp
// AVR (Uno) — free memory check
extern int __heap_start, *__brkval;
int freeMemory() {
  int v;
  return (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
}

// ESP32 — free heap
void printHeap() {
  Serial.print("Free heap: ");
  Serial.println(ESP.getFreeHeap());
}
```

If your program crashes randomly, starts behaving erratically, or resets unexpectedly — suspect stack overflow from SRAM exhaustion.

Best practices for memory-constrained embedded code:

First: use the `F()` macro for string literals in Serial.print calls on Uno — this keeps strings in flash instead of copying them to SRAM:

```cpp
Serial.println(F("This string stays in flash memory"));
```

Second: avoid `String` objects on the Uno. They use dynamic allocation and fragment the heap. Use character arrays instead.

Third: pre-allocate buffers at compile time. A global `char buf[64]` is always safer than runtime `String` concatenation.

Fourth: on the ESP32, call `ESP.getFreeHeap()` regularly during development to catch memory leaks before they reach production.

---

## SEGMENT 10 — Wrap-Up and Preview (21:30–23:00)

Let's recap what we covered today.

We walked through the Arduino IDE toolchain and how a sketch gets compiled and uploaded. We discussed C and C++ for embedded systems — tight memory, volatile variables, and data type choices. We covered digital GPIO, analog ADC reads, PWM for simulated analog output, and hardware interrupts for real-time response.

We compared the Arduino Uno and ESP32 side by side — knowing their trade-offs helps you make the right hardware choice for any project. And we finished with memory management best practices that will save you hours of debugging.

In Module 07, we move up the stack to IoT communication protocols — MQTT, CoAP, HTTP, and WebSockets. You will learn how your embedded device talks to the internet and to other devices. That is where the "Internet" in IoT really begins.

See you there.

---

## PRODUCTION NOTES

- Slide transitions: cut between code segments, fade between hardware demonstrations
- B-roll needed: close-up of Uno and ESP32 boards, USB cable insertion, LED fading demo, oscilloscope PWM waveform
- Serial Monitor window capture: show live output when button pressed
- Closed captions: auto-generate, verify technical terms (GPIO, PWM, ISR, SRAM, FreeRTOS)
- Run time target: 22 minutes
