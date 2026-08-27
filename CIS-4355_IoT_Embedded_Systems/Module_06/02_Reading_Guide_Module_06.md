# Reading Guide: Module 06 — Microcontroller Programming

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Certification Target:** IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you will be able to:

1. Explain the Arduino IDE compile-upload toolchain and sketch structure
2. Write C/C++ embedded code using appropriate data types and memory strategies
3. Configure GPIO pins for digital input and output
4. Read analog sensor data using the ADC and convert to engineering units
5. Generate PWM signals for motor control and LED dimming
6. Implement interrupt service routines following best practices
7. Compare the Arduino Uno and ESP32 and select the appropriate platform for a given requirement
8. Apply memory management techniques for SRAM-constrained devices

---

## Section 1 — The Arduino IDE and Build Toolchain

### 1.1 What Happens When You Click Upload

The Arduino IDE performs four steps every time you compile and upload a sketch:

1. **Preprocessing** — The IDE wraps your sketch in boilerplate that calls `setup()` once and `loop()` repeatedly, then feeds it to the C++ preprocessor.
2. **Compilation** — `avr-g++` (for Uno) or `xtensa-esp32-elf-g++` (for ESP32) compiles your code into object files.
3. **Linking** — The linker combines your object files with the Arduino core library into a single ELF binary, then creates a HEX file.
4. **Upload** — `avrdude` (Uno) or `esptool.py` (ESP32) transfers the HEX/BIN file to the device over USB, writing it to flash memory.

### 1.2 Sketch Structure

Every sketch contains two mandatory functions. Additional helper functions can be defined outside them.

```cpp
// Global variables and includes go here
#include <Arduino.h>
int ledPin = 13;

void setup() {
  // Runs once on power-on or hardware reset
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Runs continuously until power removed
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
  delay(500);
}
```

### 1.3 The Serial Monitor

The Serial Monitor is your primary debugging tool. Open it from Tools > Serial Monitor and match the baud rate in your code.

```cpp
Serial.begin(115200);        // Initialize UART at 115200 baud
Serial.print("Value: ");     // Print without newline
Serial.println(analogRead(A0)); // Print with newline
Serial.printf("ADC=%d\n", analogRead(A0)); // ESP32 printf support
```

**Important:** Always call `Serial.begin()` before any `Serial.print()` calls. Printing without initialization produces garbage or causes a hang.

---

## Section 2 — C/C++ for Embedded Systems

### 2.1 Memory Regions

Microcontrollers have three distinct memory areas:

| Region | Uno Size | ESP32 Size | Stores |
|--------|----------|------------|--------|
| Flash (ROM) | 32 KB | 4 MB | Program code, PROGMEM strings |
| SRAM | 2 KB | 520 KB | Variables, stack, heap |
| EEPROM | 1 KB | Emulated (NVS) | Persistent config data |

### 2.2 Data Types and Sizes

Use fixed-width types from `<stdint.h>` to guarantee portable sizes across architectures:

| Type | Bits | Range | Use Case |
|------|------|-------|----------|
| `bool` | 8 | true/false | Flags and state |
| `uint8_t` | 8 | 0–255 | Sensor IDs, byte values |
| `int8_t` | 8 | -128–127 | Small signed values |
| `uint16_t` | 16 | 0–65535 | ADC readings, counts |
| `int16_t` | 16 | -32768–32767 | Signed sensor readings |
| `uint32_t` | 32 | 0–4,294,967,295 | Timestamps (millis) |
| `float` | 32 | ±3.4×10^38 | Sensor calculations |

**Avoid `int` when size matters.** On AVR (Uno), `int` is 16-bit. On ESP32, `int` is 32-bit. Code that assumes one or the other is non-portable.

### 2.3 The volatile Keyword

Variables modified by interrupt service routines (ISRs) or hardware must be declared `volatile`. This prevents the compiler from optimizing the variable into a CPU register and missing hardware updates.

```cpp
volatile uint8_t  encoderCount = 0;
volatile bool     dataReady    = false;
volatile uint32_t lastEdgeMs   = 0;
```

### 2.4 The PROGMEM Keyword (AVR Only)

On the Uno, every string literal you write in your code is copied from flash to SRAM at startup. For programs with many strings, this quickly exhausts the 2 KB SRAM budget.

The `F()` macro is the easiest solution:

```cpp
// Without F() — string lives in SRAM (costs RAM)
Serial.println("Temperature reading complete");

// With F() — string stays in flash (saves RAM)
Serial.println(F("Temperature reading complete"));
```

For larger read-only tables, use the full `PROGMEM` declaration with `pgm_read_byte()` or `pgm_read_word()` to access values.

---

## Section 3 — GPIO: Digital I/O

### 3.1 Pin Modes

Configure every pin you use before reading or writing it:

```cpp
pinMode(pin, OUTPUT);        // Drive high or low
pinMode(pin, INPUT);         // High-impedance input — needs external pull resistor
pinMode(pin, INPUT_PULLUP);  // Input with internal pull-up to VCC
```

On most ATmega/ESP32 devices, the internal pull-up resistor is 20–50 kΩ. This is typically sufficient for button circuits.

### 3.2 Digital Read and Write

```cpp
digitalWrite(pin, HIGH);  // 5V (Uno) or 3.3V (ESP32)
digitalWrite(pin, LOW);   // 0V (GND)
int state = digitalRead(pin);  // Returns HIGH (1) or LOW (0)
```

### 3.3 Button Debouncing

Mechanical buttons bounce — they make and break contact rapidly for 5–50 ms before settling. Raw `digitalRead()` sees dozens of transitions from a single press.

**Software debounce technique:**

```cpp
const int BUTTON_PIN  = 2;
const int DEBOUNCE_MS = 50;
int       lastState   = HIGH;
uint32_t  lastDebounce = 0;

void loop() {
  int reading = digitalRead(BUTTON_PIN);
  if (reading != lastState) {
    lastDebounce = millis();
  }
  if ((millis() - lastDebounce) > DEBOUNCE_MS) {
    // State has been stable for 50ms — it is valid
    if (reading == LOW) {
      Serial.println(F("Stable button press"));
    }
  }
  lastState = reading;
}
```

### 3.4 Maximum Current Per Pin

- **Arduino Uno (ATmega328P):** Maximum 40 mA per pin, 200 mA total across all pins. LEDs require a current-limiting resistor (typically 220–330 Ω for a 5V supply with a red LED).
- **ESP32:** Maximum 12 mA per pin recommended (40 mA absolute maximum). Always use a transistor or MOSFET for loads above 12 mA.

---

## Section 4 — Analog I/O and the ADC

### 4.1 ADC Resolution and Reference Voltage

The ADC converts an analog voltage into a digital integer. The number of steps depends on bit depth:

| Platform | ADC Bits | Steps | Voltage Range |
|----------|----------|-------|---------------|
| Arduino Uno | 10-bit | 1024 | 0–5V (default) |
| Arduino Due | 12-bit | 4096 | 0–3.3V |
| ESP32 | 12-bit | 4096 | 0–3.3V |

Conversion formula:

```text
Voltage = (ADC_reading / (2^bits - 1)) × V_ref
```

For Uno: `Voltage = (reading / 1023.0) × 5.0`

### 4.2 ADC Non-Linearity on ESP32

The ESP32 ADC has a known non-linearity, particularly at the extremes (near 0V and near 3.3V). For accurate measurements, calibrate using the `esp_adc_cal` library or limit input range to 0.1V–3.1V.

### 4.3 Sampling Rate

The Uno's ADC conversion takes approximately 100 microseconds (default prescaler setting), giving a maximum sample rate of about 9,600 samples per second. For higher-speed ADC work, reduce the prescaler:

```cpp
// Increase Uno ADC speed (reduces accuracy slightly)
// Set prescaler to 16: 1 MHz ADC clock -> ~77 KSPS
ADCSRA = (ADCSRA & ~0x07) | 0x04;
```

---

## Section 5 — PWM: Pulse Width Modulation

### 5.1 PWM Fundamentals

PWM creates a variable average voltage by switching a digital output on and off at a fixed frequency. The duty cycle is the fraction of time the output is HIGH.

```text
Average Voltage = Duty Cycle × Supply Voltage
```

Examples:

- Duty cycle 0% → 0V average
- Duty cycle 25% → 1.25V average (5V supply)
- Duty cycle 50% → 2.5V average
- Duty cycle 75% → 3.75V average
- Duty cycle 100% → 5V average

### 5.2 Arduino Uno PWM Pins and Frequencies

| Pin | Timer | Default Frequency |
|-----|-------|------------------|
| 3, 11 | Timer 2 | 490 Hz |
| 5, 6 | Timer 0 | 980 Hz |
| 9, 10 | Timer 1 | 490 Hz |

**Note:** Timer 0 drives `millis()` and `delay()`. Changing its frequency breaks timing functions.

### 5.3 ESP32 LEDC PWM

The ESP32 LEDC peripheral supports 16 channels with independently configurable frequencies and resolutions:

```cpp
ledcSetup(channel, frequency_hz, resolution_bits);
ledcAttachPin(gpio_pin, channel);
ledcWrite(channel, duty_cycle);  // 0 to (2^resolution - 1)
```

Higher resolution means more steps but lower maximum frequency. At 8-bit resolution, max frequency is roughly 312 kHz. At 16-bit resolution, max is about 1.2 kHz.

### 5.4 Servo Control with PWM

Standard hobby servos expect a 50 Hz PWM signal with pulse width 500–2500 µs:

```cpp
#include <Servo.h>
Servo myServo;

void setup() {
  myServo.attach(9);        // Attach to pin 9
}

void loop() {
  myServo.write(0);         // 0 degrees
  delay(1000);
  myServo.write(90);        // 90 degrees
  delay(1000);
  myServo.write(180);       // 180 degrees
  delay(1000);
}
```

---

## Section 6 — Interrupts

### 6.1 Interrupt Types

| Type | Trigger | Common Use |
|------|---------|------------|
| External (pin) | Signal edge on GPIO pin | Button press, encoder, sensor alert |
| Timer | Fixed time interval | Periodic sampling, watchdog |
| UART/SPI/I2C | Data received or sent | Protocol handling |
| ADC | Conversion complete | High-speed sampling |

### 6.2 External Interrupt Modes

```cpp
attachInterrupt(digitalPinToInterrupt(pin), ISR_function, mode);
```

Mode options:

- `RISING` — Trigger when pin transitions LOW to HIGH
- `FALLING` — Trigger when pin transitions HIGH to LOW
- `CHANGE` — Trigger on any transition
- `LOW` — Trigger continuously while pin is LOW (use with care)

### 6.3 ISR Best Practices Summary

```cpp
// CORRECT ISR pattern
volatile bool g_eventFlag = false;
volatile uint32_t g_eventTime = 0;

void IRAM_ATTR myISR() {   // IRAM_ATTR required on ESP32
  g_eventFlag = true;
  g_eventTime = millis();  // millis() is safe in ESP32 ISRs
}

void loop() {
  if (g_eventFlag) {
    g_eventFlag = false;
    // Do the actual work here, outside the ISR
    handleEvent(g_eventTime);
  }
}
```

**What NOT to do in ISRs:**

- Do not call `delay()` or `Serial.print()` on AVR
- Do not allocate memory (`new`, `malloc`)
- Do not call functions that themselves disable interrupts for long periods
- Do not perform floating-point math on AVR (slow and non-reentrant)

### 6.4 Timer Interrupts on Uno

Using the `TimerOne` library for periodic execution:

```cpp
#include <TimerOne.h>

volatile uint16_t sampleBuffer[64];
volatile uint8_t  sampleIndex = 0;

void sampleISR() {
  if (sampleIndex < 64) {
    sampleBuffer[sampleIndex++] = analogRead(A0);
  }
}

void setup() {
  Serial.begin(115200);
  Timer1.initialize(1000);       // 1000 µs = 1 kHz sample rate
  Timer1.attachInterrupt(sampleISR);
}
```

---

## Section 7 — ESP32 vs Arduino Uno Comparison

### 7.1 Hardware Specifications

| Feature | Arduino Uno R3 | ESP32 DevKit V1 |
|---------|----------------|-----------------|
| MCU | ATmega328P | Xtensa LX6 (dual-core) |
| Clock Speed | 16 MHz | 80–240 MHz |
| SRAM | 2 KB | 520 KB |
| Flash | 32 KB | 4 MB (typical) |
| EEPROM | 1 KB | NVS (emulated) |
| Supply Voltage | 5V | 3.3V |
| Digital I/O | 14 | Up to 34 |
| Analog Inputs | 6 (10-bit) | 18 (12-bit) |
| PWM Channels | 6 | 16 (LEDC) |
| UART | 1 | 3 |
| SPI | 1 | 4 |
| I2C | 1 | 2 |
| Wi-Fi | No | 802.11 b/g/n |
| Bluetooth | No | BT 4.2 + BLE |
| DAC | No | 2 channels (8-bit) |
| Touch Sensors | No | 10 capacitive |
| Price (approx.) | $5–$25 | $3–$12 |

### 7.2 FreeRTOS on ESP32

The ESP32 Arduino core runs FreeRTOS, enabling true multi-tasking:

```cpp
// Task on Core 1 — sensor reading
void sensorTask(void *pvParams) {
  for (;;) {
    int val = analogRead(34);
    Serial.printf("Sensor: %d\n", val);
    vTaskDelay(pdMS_TO_TICKS(500));
  }
}

// Task on Core 0 — WiFi/network handling
void networkTask(void *pvParams) {
  for (;;) {
    // Check MQTT, send data
    vTaskDelay(pdMS_TO_TICKS(100));
  }
}

void setup() {
  Serial.begin(115200);
  xTaskCreatePinnedToCore(sensorTask,  "Sensor",  4096, NULL, 1, NULL, 1);
  xTaskCreatePinnedToCore(networkTask, "Network", 8192, NULL, 1, NULL, 0);
}

void loop() { vTaskDelay(portMAX_DELAY); }  // Idle — tasks handle everything
```

---

## Section 8 — Memory Management

### 8.1 SRAM Layout on AVR

```text
High address  ┌─────────────┐
              │   Stack     │ ← grows downward
              │     ↓       │
              ├ · · · · · · ┤
              │     ↑       │
              │    Heap     │ ← grows upward (malloc/new)
              ├─────────────┤
              │  .bss       │ ← zero-initialized globals
              ├─────────────┤
              │  .data      │ ← initialized globals
Low address   └─────────────┘
```

Stack grows toward heap. If they collide, the program corrupts data and crashes unpredictably.

### 8.2 Checking Available SRAM

```cpp
// Uno — check free memory between heap top and stack bottom
extern int __heap_start, *__brkval;
int freeRam() {
  int v;
  return (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
}

void setup() {
  Serial.begin(9600);
  Serial.print(F("Free RAM: "));
  Serial.print(freeRam());
  Serial.println(F(" bytes"));
}
```

### 8.3 Memory Optimization Checklist

- Use `F()` macro around all string literals in Serial.print calls
- Replace `String` with `char[]` throughout
- Declare large buffers as global arrays, not local variables
- Avoid recursion — it grows the stack unpredictably
- Use `uint8_t` instead of `int` for loop counters when range is 0–255
- Move lookup tables to PROGMEM on AVR

---

## Key Terms

| Term | Definition |
|------|------------|
| GPIO | General-Purpose Input/Output — configurable digital pins |
| ADC | Analog-to-Digital Converter — converts voltage to integer |
| DAC | Digital-to-Analog Converter — converts integer to voltage |
| PWM | Pulse Width Modulation — simulates analog via duty cycle |
| ISR | Interrupt Service Routine — function called by hardware event |
| SRAM | Static RAM — fast, volatile working memory |
| Flash | Non-volatile memory storing program code |
| PROGMEM | AVR directive storing data in flash instead of SRAM |
| FreeRTOS | Real-time OS used by ESP32 for task scheduling |
| Bootloader | Small program that receives and writes firmware over USB |
| Duty Cycle | Fraction of PWM period that signal is HIGH |
| Debouncing | Filtering out rapid mechanical switch noise |

---

## Review Questions

1. Why must variables modified by ISRs be declared `volatile`?
2. What is the difference between `INPUT` and `INPUT_PULLUP`?
3. An Arduino Uno has 2 KB of SRAM. A global `char msg[512]` array is declared. How much SRAM does this leave for the stack and heap?
4. Why should you avoid the `String` class on the Uno for long-running programs?
5. What does the `IRAM_ATTR` attribute do on the ESP32, and why is it required for ISRs?
6. A servo requires a 50 Hz PWM signal. Calculate the period in milliseconds and the pulse width for 90 degrees (1500 µs).
7. What is the maximum sample rate of the Uno ADC at its default prescaler setting?
8. How does FreeRTOS on the ESP32 differ from the Arduino single-loop model?

---

## 9. Supplemental Resources

**1. ESP32 Arduino Core Documentation — LEDC and Interrupt APIs**
[https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/](https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/)
The official Espressif Arduino-ESP32 core documentation. Covers the LEDC PWM API (`ledcSetup`, `ledcAttachPin`, `ledcWrite`), `IRAM_ATTR` ISR placement, FreeRTOS task creation, deep sleep, and all ESP32-specific extensions to the Arduino framework.

**2. AVR-libc Reference Manual — Interrupts and Memory**
[https://www.nongnu.org/avr-libc/user-manual/](https://www.nongnu.org/avr-libc/user-manual/)
The definitive reference for the AVR C library used by the Arduino Uno. Covers interrupt vectors, the `volatile` keyword, `PROGMEM` and `pgm_read_*` functions, stack/heap layout, and fixed-width integer types from `<stdint.h>`. Essential background for understanding the memory management techniques in Section 8.

**3. FreeRTOS API Reference**
[https://www.freertos.org/a00106.html](https://www.freertos.org/a00106.html)
The official FreeRTOS API documentation covering `xTaskCreatePinnedToCore()`, `vTaskDelay()`, `pdMS_TO_TICKS()`, queues, semaphores, and mutexes. The ESP32 Arduino core runs FreeRTOS v10. This reference is required for any multi-task ESP32 firmware beyond the examples in Section 7.
