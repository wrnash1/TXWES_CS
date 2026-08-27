# Lab: Module 06 — Microcontroller Programming

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Points:** 100

---

## Lab Overview

In this lab you will write, upload, and demonstrate three progressively complex Arduino/ESP32 programs that exercise digital I/O, analog reading, PWM output, and hardware interrupts. All three parts run on the same breadboard circuit.

**Estimated time:** 2–3 hours

**Hardware required:**

- Arduino Uno R3 or ESP32 DevKit V1 (either platform accepted)
- USB cable
- Half-size breadboard
- 1x red LED
- 1x green LED
- 2x 220 Ω resistors
- 1x 10 kΩ potentiometer
- 1x tactile pushbutton
- Jumper wires (10+)

---

## Circuit Wiring Diagram

Build the following circuit on your breadboard before writing any code.

**Red LED (PWM controlled):**

- LED anode (long leg) → 220 Ω resistor → Pin 9 (Uno) or GPIO 18 (ESP32)
- LED cathode (short leg) → GND rail

**Green LED (digital on/off):**

- LED anode → 220 Ω resistor → Pin 13 (Uno) or GPIO 2 (ESP32)
- LED cathode → GND rail

**Potentiometer:**

- Left pin → GND rail
- Center pin (wiper) → A0 (Uno) or GPIO 34 (ESP32)
- Right pin → 5V (Uno) or 3.3V (ESP32)

**Pushbutton:**

- One side → Pin 2 (Uno) or GPIO 4 (ESP32)
- Other side → GND rail
- (Use INPUT_PULLUP in code — no external resistor needed)

**Power:**

- Connect Arduino/ESP32 GND to breadboard GND rail
- Connect Arduino/ESP32 5V (Uno) or 3.3V (ESP32) to breadboard VCC rail

---

## Part A — Digital I/O and Serial Communication (25 points)

### Part A Objective

Toggle the green LED with the pushbutton using a software debounce routine and report state changes over Serial.

### Part A Code

```cpp
// Part A: Debounced Button → LED + Serial Report
// Works on both Arduino Uno and ESP32

#ifdef ESP32
  #define BUTTON_PIN  4
  #define GREEN_LED   2
#else
  #define BUTTON_PIN  2
  #define GREEN_LED   13
#endif

const uint32_t DEBOUNCE_MS = 50;

int      lastRawState   = HIGH;
int      confirmedState = HIGH;
uint32_t lastDebounce   = 0;
bool     ledState       = false;

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(GREEN_LED,  OUTPUT);
  digitalWrite(GREEN_LED, LOW);
  Serial.println(F("Part A ready. Press button to toggle LED."));
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  if (reading != lastRawState) {
    lastDebounce = millis();
  }

  if ((millis() - lastDebounce) > DEBOUNCE_MS) {
    if (reading != confirmedState) {
      confirmedState = reading;
      if (confirmedState == LOW) {
        ledState = !ledState;
        digitalWrite(GREEN_LED, ledState ? HIGH : LOW);
        Serial.print(F("Button pressed — LED is now: "));
        Serial.println(ledState ? F("ON") : F("OFF"));
      }
    }
  }

  lastRawState = reading;
}
```

### Part A Expected Serial Output

```text
Part A ready. Press button to toggle LED.
Button pressed — LED is now: ON
Button pressed — LED is now: OFF
Button pressed — LED is now: ON
```

### Part A Deliverables

- Upload code and demonstrate to instructor (in-person) or record a 30-second video showing button toggle and matching Serial Monitor output
- Screenshot of Serial Monitor with at least 4 state changes visible

---

## Part B — Analog Read and PWM Fade (35 points)

### Part B Objective

Read the potentiometer position and use the value to control the brightness of the red LED via PWM. Display the raw ADC value and calculated voltage in the Serial Monitor at 500ms intervals.

### Part B Code

```cpp
// Part B: Potentiometer → PWM LED + Serial Display
// Works on both Arduino Uno (10-bit ADC) and ESP32 (12-bit ADC)

#ifdef ESP32
  #define POT_PIN   34
  #define RED_LED   18
  #define ADC_MAX   4095
  #define V_REF     3.3f
  #define PWM_CHAN  0
  #define PWM_FREQ  5000
  #define PWM_RES   8
#else
  #define POT_PIN   A0
  #define RED_LED   9
  #define ADC_MAX   1023
  #define V_REF     5.0f
#endif

uint32_t lastPrint = 0;

void setup() {
  Serial.begin(115200);

#ifdef ESP32
  ledcSetup(PWM_CHAN, PWM_FREQ, PWM_RES);
  ledcAttachPin(RED_LED, PWM_CHAN);
#else
  pinMode(RED_LED, OUTPUT);
#endif

  Serial.println(F("Part B ready. Turn potentiometer."));
  Serial.println(F("Raw ADC | Voltage | PWM Duty"));
  Serial.println(F("--------|---------|----------"));
}

void loop() {
  int   raw     = analogRead(POT_PIN);
  float voltage = raw * (V_REF / (float)ADC_MAX);
  int   pwmVal  = map(raw, 0, ADC_MAX, 0, 255);

#ifdef ESP32
  ledcWrite(PWM_CHAN, pwmVal);
#else
  analogWrite(RED_LED, pwmVal);
#endif

  if (millis() - lastPrint >= 500) {
    lastPrint = millis();
    Serial.print(raw);
    Serial.print(F("\t\t"));
    Serial.print(voltage, 2);
    Serial.print(F("V\t\t"));
    Serial.println(pwmVal);
  }
}
```

### Part B Expected Serial Output

```text
Part B ready. Turn potentiometer.
Raw ADC | Voltage | PWM Duty
--------|---------|----------
0       0.00V    0
256     1.25V    63
512     2.50V    127
768     3.75V    191
1023    5.00V    255
```

### Part B Deliverables

- Screenshot of Serial Monitor showing at least 10 readings spanning low, mid, and high potentiometer positions
- Brief written observation (2–3 sentences): Does the LED brightness change smoothly? At what ADC reading does it appear half-brightness to your eye?

---

## Part C — Hardware Interrupt and Timed Sampling (40 points)

### Part C Objective

Use a hardware interrupt on the button pin to count button presses. Independently, use `millis()` (non-blocking timing) to sample the potentiometer every 250ms and display a running average of the last 8 readings. Demonstrate that the interrupt counter increments correctly regardless of the sampling code's timing.

### Part C Code

```cpp
// Part C: Interrupt counter + non-blocking ADC sampling with running average
// Works on both Arduino Uno and ESP32

#ifdef ESP32
  #define BUTTON_PIN  4
  #define POT_PIN     34
  #define ADC_MAX     4095
  #define V_REF       3.3f
  #define ISR_ATTR    IRAM_ATTR
#else
  #define BUTTON_PIN  2
  #define POT_PIN     A0
  #define ADC_MAX     1023
  #define V_REF       5.0f
  #define ISR_ATTR
#endif

// Interrupt state
volatile uint32_t g_pressCount  = 0;
volatile uint32_t g_lastPressMs = 0;

// Sampling state
const uint8_t  BUF_SIZE    = 8;
uint16_t       sampleBuf[BUF_SIZE];
uint8_t        sampleIdx   = 0;
uint32_t       lastSample  = 0;
const uint32_t SAMPLE_MS   = 250;

void ISR_ATTR buttonISR() {
  uint32_t now = millis();
  // Simple ISR debounce: ignore edges within 50ms of previous
  if (now - g_lastPressMs > 50) {
    g_pressCount++;
    g_lastPressMs = now;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), buttonISR, FALLING);

  // Pre-fill sample buffer
  for (uint8_t i = 0; i < BUF_SIZE; i++) {
    sampleBuf[i] = analogRead(POT_PIN);
  }

  Serial.println(F("Part C ready."));
  Serial.println(F("Press count | Avg ADC | Avg Voltage"));
  Serial.println(F("------------|---------|------------"));
}

void loop() {
  if (millis() - lastSample >= SAMPLE_MS) {
    lastSample = millis();

    // Add new sample to circular buffer
    sampleBuf[sampleIdx % BUF_SIZE] = analogRead(POT_PIN);
    sampleIdx++;

    // Compute running average
    uint32_t sum = 0;
    for (uint8_t i = 0; i < BUF_SIZE; i++) sum += sampleBuf[i];
    uint16_t avg     = sum / BUF_SIZE;
    float    avgVolts = avg * (V_REF / (float)ADC_MAX);

    // Read volatile safely (disable interrupts briefly on AVR)
    noInterrupts();
    uint32_t count = g_pressCount;
    interrupts();

    Serial.print(count);
    Serial.print(F("\t\t"));
    Serial.print(avg);
    Serial.print(F("\t\t"));
    Serial.println(avgVolts, 3);
  }
}
```

### Part C Expected Serial Output

```text
Part C ready.
Press count | Avg ADC | Avg Voltage
------------|---------|------------
0           511      2.498
0           512      2.503
1           511      2.498
1           710      3.472
2           890      4.351
```

### Part C Deliverables

- Screenshot of Serial Monitor showing at least 12 rows with press count incrementing at button presses
- Written answer (3–5 sentences): What would happen if you tried to handle the button count using `digitalRead()` polling inside `loop()` with a 250ms delay? Why is the interrupt approach more reliable?

---

## Submission Instructions

Submit the following to the course LMS by the due date:

1. A single `.ino` file or `.zip` containing all three parts (combined into one sketch with `#define PART_A`, `PART_B`, `PART_C` guards, or three separate sketch folders)
2. Three Serial Monitor screenshots (one per part)
3. Part B written observation
4. Part C written answer
5. A photo of your assembled breadboard circuit

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| **Part A** — Code compiles and uploads | 5 |
| **Part A** — Debounce implemented correctly (not just digitalRead) | 10 |
| **Part A** — Serial output matches expected format | 10 |
| **Part B** — ADC read and voltage conversion correct | 10 |
| **Part B** — PWM range mapped 0–255 from full pot range | 10 |
| **Part B** — Serial output includes raw, voltage, and PWM columns | 10 |
| **Part B** — Written brightness observation | 5 |
| **Part C** — ISR implemented with volatile variable | 10 |
| **Part C** — Non-blocking sampling using millis() (no delay()) | 10 |
| **Part C** — Running average of 8 samples computed correctly | 10 |
| **Part C** — Written interrupt vs polling explanation | 10 |
| **Breadboard photo submitted** | 5 |
| **Code quality** — comments, naming, no unused variables | 5 |
| **TOTAL** | **100** |

---

## Troubleshooting Tips

**LED does not light up:** Check resistor orientation and confirm pin number matches your `#define`. Use a multimeter to verify 5V at the pin when HIGH is written.

**ADC always reads 0 or 1023:** Confirm the potentiometer wiper is connected to the analog pin. Verify power and ground on the outer potentiometer terminals.

**Button ISR never fires:** Confirm `attachInterrupt` uses `digitalPinToInterrupt(pin)` not the raw pin number. On ESP32, confirm pin supports interrupts (avoid GPIO 6–11).

**Serial output garbled:** Baud rate in Serial Monitor must match `Serial.begin()` value exactly.

**ESP32 crashing on ISR:** Add `IRAM_ATTR` to your ISR function declaration.

---

## Part 9 — Challenge Exercise

### Challenge 1: FreeRTOS Dual-Task Sensor System (ESP32)

Extend the Part C sketch to run sensor sampling and serial reporting as separate FreeRTOS tasks pinned to different cores.

1. Create a task named `sensorTask` pinned to Core 1 with stack size 4096. This task reads the potentiometer ADC every 250 ms, updates a shared `volatile uint16_t g_adcAvg` running average, and calls `vTaskDelay(pdMS_TO_TICKS(250))` instead of `delay()`.
2. Create a task named `reportTask` pinned to Core 0 with stack size 2048. This task reads `g_pressCount` and `g_adcAvg` every 500 ms and prints the formatted row to Serial. Use `portENTER_CRITICAL()` / `portEXIT_CRITICAL()` around the read of `g_pressCount` instead of `noInterrupts()`/`interrupts()`, and explain in a comment why this is the preferred approach in a FreeRTOS context.
3. Remove the sampling and reporting logic from `loop()` entirely. Verify that the Serial Monitor output continues to print at the expected rate and that button presses still increment the counter correctly.
4. Use `uxTaskGetStackHighWaterMark(NULL)` inside each task to print the minimum free stack words remaining after 10 iterations. Explain what would happen if the stack size was set too small.

### Challenge 2: EEPROM/NVS Persistent Counter

Make the button press counter survive a power cycle by storing it in non-volatile memory.

1. On the Arduino Uno: use the `EEPROM` library. In `setup()`, read the stored count from address 0 (stored as a `uint32_t` across four bytes using `EEPROM.get()`). Initialize `g_pressCount` to this value. In the ISR (or a save routine called from `loop()` when count changes), write the updated value back using `EEPROM.put(0, g_pressCount)`.
2. On the ESP32: use the `Preferences` library instead of `EEPROM`. In `setup()`, open a namespace `"counters"`, read key `"presses"` as `uint32_t`, and initialize `g_pressCount`. Save the value back when it changes using `prefs.putUInt("presses", g_pressCount)`.
3. Power-cycle the device and verify the counter resumes from the saved value. Screenshot the Serial Monitor showing a non-zero starting count.
4. In 3–5 sentences, explain the EEPROM write endurance limit (approximately 100,000 write cycles on AVR) and describe an optimization strategy — such as write-coalescing or a dirty-flag pattern — that would extend the EEPROM lifetime for a device that accumulates thousands of button presses per day.

### Reflection Questions

1. Part C used `noInterrupts()`/`interrupts()` to safely read the 32-bit `g_pressCount` from `loop()`. Why is this necessary on an 8-bit AVR but arguably less critical on the 32-bit ESP32 (though still a good practice)?
2. After completing Challenge 1, did moving sensor sampling to a dedicated FreeRTOS task change the timing accuracy of your 250 ms sample interval compared to the `millis()`-based approach in Part C? Explain why FreeRTOS `vTaskDelay()` may introduce small timing variations and how `vTaskDelayUntil()` would improve accuracy.
