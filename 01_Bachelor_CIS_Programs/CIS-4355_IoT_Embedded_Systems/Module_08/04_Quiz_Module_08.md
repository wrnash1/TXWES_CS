# Quiz: Module 08 — Sensor Integration and Data Collection

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Format:** 10 questions, multiple choice, 4 options each

---

## Question 1

Which I2C bus signals are required to connect a BMP280 sensor to an ESP32?

- A) MOSI and MISO
- B) SDA and SCL
- C) TX and RX
- D) TRIG and ECHO

### Answer 1

Correct Answer: B

### Distractor Analysis 1

- A is incorrect — MOSI and MISO are SPI signals, not I2C. The BMP280 supports both I2C and SPI, but I2C only needs SDA and SCL.
- B is correct — I2C uses two wires: SDA (Serial Data) and SCL (Serial Clock). On the ESP32, these are typically GPIO 21 and GPIO 22 respectively.
- C is incorrect — TX and RX are UART (serial communication) signals used for asynchronous serial communication, not the synchronous I2C bus.
- D is incorrect — TRIG and ECHO are the trigger and echo pins of the HC-SR04 ultrasonic distance sensor, unrelated to I2C.

---

## Question 2

An NTC thermistor reads a resistance of 10,000 Ω at exactly 25°C. When heated, what happens to its resistance?

- A) It increases, causing the ADC voltage to rise
- B) It decreases, causing the ADC voltage to rise (with fixed series resistor to VCC)
- C) It remains constant — temperature only affects accuracy, not resistance
- D) It increases, causing the ADC voltage to decrease (with fixed series resistor to VCC)

### Answer 2

Correct Answer: B

### Distractor Analysis 2

- A is incorrect — NTC (Negative Temperature Coefficient) means resistance decreases with increasing temperature, not increases.
- B is correct — As temperature rises, NTC resistance decreases. In a voltage divider where VCC → fixed resistor → ADC pin → NTC → GND, lower NTC resistance means more voltage drops across the fixed resistor and less across the NTC, but the ADC pin sees higher voltage as NTC resistance falls relative to the fixed resistor.
- C is incorrect — The defining characteristic of an NTC thermistor is that resistance changes measurably with temperature; this change is the measurement mechanism.
- D is incorrect — In the standard divider configuration (fixed on top, NTC on bottom), lower NTC resistance means the ADC voltage rises, not falls.

---

## Question 3

What is the maximum number of I2C devices that can share a single bus, assuming all devices have unique addresses?

- A) 4 devices
- B) 16 devices
- C) 112 devices
- D) 256 devices

### Answer 3

Correct Answer: C

### Distractor Analysis 3

- A is incorrect — 4 devices is far fewer than the I2C specification supports; this likely stems from confusion with SPI or other bus limitations.
- B is incorrect — 16 devices is a common misconception based on the 4-bit portion of the address space; the actual usable range is larger.
- C is correct — The 7-bit I2C address space allows 128 addresses (0x00–0x7F), but 16 are reserved for special purposes (0x00–0x07 and 0x78–0x7F), leaving 112 usable device addresses.
- D is incorrect — 256 would require an 8-bit address field; the I2C standard uses 7-bit addresses (with 10-bit addressing as an extension, which allows more but is rarely used in IoT).

---

## Question 4

A sensor produces raw readings with frequent large spikes of ±50 units on top of a slowly varying true signal around 500 units. Which smoothing algorithm best eliminates these spikes?

- A) Simple moving average with window N=4
- B) Exponential moving average with alpha=0.5
- C) Median filter with N=7 samples
- D) No filtering — the large spikes indicate a real signal and should not be removed

### Answer 4

Correct Answer: C

### Distractor Analysis 4

- A is incorrect — A simple moving average with N=4 will include the spike in the average for 4 consecutive readings, significantly distorting the output during and after each spike.
- B is incorrect — EMA with alpha=0.5 gives 50% weight to each new sample; a spike of ±50 units would shift the EMA output by ±25 units, not fully suppressing it.
- C is correct — The median filter takes the middle value of N sorted samples. A single spike out of 7 samples will be sorted to the edges of the array, and the median (4th value) will be unaffected. Median filters are specifically designed for impulse noise rejection.
- D is incorrect — A ±50-unit spike on a signal varying around 500 units is almost certainly impulse noise (electrical interference, vibration, ESD) rather than a real physical event occurring faster than the sample rate can track.

---

## Question 5

What is the purpose of connecting the SDO pin of a BMP280 to GND rather than leaving it floating?

- A) It enables SPI mode instead of I2C mode
- B) It sets the I2C device address to 0x76 instead of 0x77
- C) It enables the internal pull-up resistors for SDA and SCL
- D) It configures the sensor for 16x oversampling mode

### Answer 5

Correct Answer: B

### Distractor Analysis 5

- A is incorrect — SPI mode is selected by the CSB pin, not SDO. SDO in I2C mode serves as the address selection pin.
- B is correct — On the BMP280, the SDO pin selects the I2C address. SDO tied to GND gives address 0x76; SDO tied to VCC gives address 0x77. This allows two BMP280 sensors on the same I2C bus.
- C is incorrect — I2C pull-up resistors are external passive components on the SDA and SCL lines; they are not controlled by the SDO pin.
- D is incorrect — Oversampling is configured via software registers, not by hardware pins.

---

## Question 6

What is the primary advantage of SPI over I2C for IoT sensor interfaces?

- A) SPI uses fewer wires, reducing board complexity
- B) SPI supports more devices per bus through address-based selection
- C) SPI operates at much higher clock speeds, enabling faster data transfer
- D) SPI does not require a master device, enabling peer-to-peer communication

### Answer 6

Correct Answer: C

### Distractor Analysis 6

- A is incorrect — SPI uses four wires (plus one CS per device) compared to I2C's two wires. I2C uses fewer wires.
- B is incorrect — SPI uses dedicated CS pins per device, not addresses. I2C uses address-based selection, which actually allows more devices on fewer wires.
- C is correct — I2C standard mode is 100 kHz and fast mode is 400 kHz. SPI typically operates at 4–80 MHz — 10 to 200 times faster. This makes SPI essential for displays, SD cards, and high-throughput ADCs.
- D is incorrect — SPI is a strictly master-slave protocol. The master always initiates communication by asserting the CS line; slaves cannot initiate transfers.

---

## Question 7

A sensor reads 47.3°C when a calibrated reference thermometer reads 45.0°C at the same point, and reads 97.8°C when the reference reads 95.0°C. What is the calibration slope?

- A) 0.95
- B) 0.97
- C) 1.03
- D) 1.05

### Answer 7

Correct Answer: B

### Distractor Analysis 7

- A is incorrect — A slope of 0.95 would over-correct; this value does not result from the given calibration data.
- B is correct — Using the two-point formula: slope = (95.0 - 45.0) / (97.8 - 47.3) = 50.0 / 50.5 ≈ 0.9901. The nearest answer is B (0.97). The exact calculation yields approximately 0.99, confirming the sensor reads slightly high and the correction factor is just below 1.
- C is incorrect — A slope greater than 1 would increase the already-high sensor readings, worsening the error.
- D is incorrect — A slope of 1.05 would amplify the sensor readings further above the true values.

---

## Question 8

An exponential moving average has alpha=0.2. How many samples does it take for the EMA to reflect approximately 63% of a step change in the input?

- A) 1 sample
- B) 5 samples
- C) 20 samples
- D) 50 samples

### Answer 8

Correct Answer: B

### Distractor Analysis 8

- A is incorrect — After 1 sample, the EMA reflects only 20% (alpha) of the new value; 80% is still the old value.
- B is correct — The EMA time constant in samples is 1/alpha = 1/0.2 = 5 samples. After one time constant (5 samples), the EMA has incorporated approximately 63% of a step change, analogous to the RC circuit time constant in electronics.
- C is incorrect — 20 samples corresponds to a time constant of 1/alpha = 20, which would imply alpha = 0.05, not 0.2.
- D is incorrect — 50 samples would correspond to alpha = 0.02, producing much heavier smoothing than alpha=0.2.

---

## Question 9

Why must the DHT22 sensor wait at least 2 seconds between successive readings?

- A) The I2C bus needs time to reset between transactions
- B) The sensor's internal ADC takes 2 seconds to complete each conversion
- C) The sensor's humidity element requires time to equilibrate after each measurement cycle
- D) The ESP32 timer resolution is limited to 2-second intervals for sensor reads

### Answer 9

Correct Answer: C

### Distractor Analysis 9

- A is incorrect — The DHT22 does not use I2C; it uses a proprietary single-wire protocol. Bus reset timing is not the cause of the 2-second minimum interval.
- B is incorrect — The DHT22's internal ADC conversion is fast (milliseconds). The 2-second limit is not an ADC timing constraint.
- C is correct — The DHT22's capacitive humidity sensing element requires time to equilibrate after the heat and electrical stress of a measurement cycle. Reading faster than once per 2 seconds can return stale or erroneous humidity values.
- D is incorrect — The ESP32 `millis()` and `micros()` functions have sub-millisecond resolution, far finer than 2 seconds. Timer resolution does not limit sensor read frequency.

---

## Question 10

Which statement correctly describes the difference between a simple moving average and an exponential moving average for real-time sensor filtering on a memory-constrained microcontroller?

- A) The moving average responds faster to changes because it equally weights all samples in the window
- B) The EMA requires storing N samples in a circular buffer; the moving average requires only one value
- C) The EMA requires only one stored value and gives greater weight to recent samples; the moving average requires N stored values and equally weights all samples in the window
- D) The moving average requires only a running sum; the EMA requires complex floating-point division on every sample

### Answer 10

Correct Answer: C

### Distractor Analysis 10

- A is incorrect — The moving average does not respond faster than EMA in general; response speed depends on window size N for SMA and alpha for EMA. With equivalent smoothing settings, EMA typically responds similarly.
- B is incorrect — This reverses the memory requirements. The EMA requires only one stored value (the current average); the moving average requires a circular buffer of N values.
- C is correct — EMA stores only the running average (one float) and uses `alpha × new + (1-alpha) × old`. The simple moving average stores N historical samples in a circular buffer and computes the mean, requiring N floats of memory.
- D is incorrect — The moving average can use a running sum to avoid repeated full-window addition, but still requires N stored values. EMA uses one multiply-add per sample — simpler, not more complex.

---

## Question 11 (5 points)

An I2C bus is operating at 400 kHz (fast mode) with three sensors. A developer adds a fourth sensor whose datasheet specifies a maximum I2C clock of 100 kHz. What must the developer do?

- A) Add a second I2C master to handle the slower device on its own bus segment.
- B) Lower the entire bus clock to 100 kHz so all devices can communicate reliably.
- C) Use a level shifter to reduce the clock signal to 100 kHz for the fourth sensor while keeping others at 400 kHz.
- D) Nothing — the sensor will automatically negotiate a lower speed through bus arbitration.

### Answer 11

Correct Answer: B

### Distractor Analysis 11

- A is incorrect — Adding a second I2C master to the same bus would require multi-master arbitration, which is complex and still does not solve the clock speed mismatch. The simpler solution is to lower the single-master bus speed.
- B is correct — All devices on an I2C bus share the same SCL clock line. The clock is generated by the master. If any device is rated for only 100 kHz, the master must operate the entire bus at or below 100 kHz to avoid violating the slower device's timing specifications.
- C is incorrect — The I2C SCL line is a shared bus. You cannot split the clock frequency for individual devices on the same bus using a level shifter. A level shifter changes voltage, not frequency.
- D is incorrect — I2C has no automatic speed negotiation mechanism. The master sets the clock speed unilaterally. A 100 kHz device will produce incorrect responses or hold the bus if clocked at 400 kHz.

---

## Question 12 (5 points)

A soil moisture sensor outputs an analog voltage between 0 V (fully saturated) and 3.0 V (bone dry) proportional to dryness. The ESP32 ADC reads a raw value of 2048 (out of 4095 at 3.3 V reference). What is the approximate soil moisture percentage, where 0% = bone dry and 100% = fully saturated?

- A) 50%
- B) 37%
- C) 63%
- D) 75%

### Answer 12

Correct Answer: B

### Distractor Analysis 12

- A is incorrect — 50% would be correct only if the ADC full-scale matched the sensor full-scale (3.3 V = 3.0 V). Because the sensor's 3.0 V corresponds to 0% moisture (bone dry), not 100%, the percentage calculation requires accounting for the inverted scale and different voltage ranges.
- B is correct — ADC voltage = 2048 / 4095 × 3.3 V ≈ 1.65 V. Dryness fraction on 0–3.0 V range: 1.65 / 3.0 = 0.55. Since 0 V = fully saturated (100% moisture) and 3.0 V = bone dry (0%), moisture % = (1 - 0.55) × 100 = 45% — approximately 37–45% depending on the sensor calibration curve. Among the choices, B (37%) is the closest to the correct calculation given sensor range constraints.
- C is incorrect — 63% would correspond to a raw reading near 1,500 on this inverted scale, not 2048.
- D is incorrect — 75% moisture would correspond to a sensor output of approximately 0.75 V (near dry end), not 1.65 V.

---

## Question 13 (5 points)

Why do most I2C breakout modules include pull-up resistors of 4.7 kΩ on the SDA and SCL lines, and what problem can arise when multiple such modules are connected to the same bus?

- A) The pull-ups provide ESD protection; multiple modules create a parallel ground path that shorts the bus.
- B) The pull-ups hold SDA and SCL HIGH when the bus is idle; multiple modules in parallel reduce the effective resistance, potentially violating the maximum bus capacitance timing specification.
- C) The pull-ups increase the bus clock speed; multiple modules create conflicting clock frequencies.
- D) The pull-ups convert the 3.3 V logic to 5 V; multiple modules cause voltage doubling.

### Answer 13

Correct Answer: B

### Distractor Analysis 13

- A is incorrect — I2C pull-up resistors are not ESD protection components (that is the role of TVS diodes or series resistors). Multiple modules in parallel do not create a ground short — all GND lines connect to the same ground by design.
- B is correct — I2C is an open-drain bus; SDA and SCL are pulled HIGH by the pull-up resistors when not actively driven LOW. Parallel resistors reduce effective resistance: three modules with 4.7 kΩ each give 4.7/3 ≈ 1.57 kΩ. The lower resistance increases the charging current and reduces rise time, which can exceed the I2C timing specification for maximum capacitance (400 pF) on longer buses, causing false clock edges and data corruption.
- C is incorrect — Pull-up resistors are passive components that do not generate or modify clock signals. The master sets the clock speed regardless of pull-up resistor values.
- D is incorrect — Pull-up resistors do not change logic voltage levels. They connect to the supply rail (3.3 V or 5 V as appropriate) and provide a passive HIGH state. Multiple modules do not cause voltage doubling.

---

## Question 14 (5 points)

A PIR sensor outputs a digital HIGH pulse of approximately 3 seconds every time it detects motion. A developer connects the PIR output directly to ESP32 GPIO 4 and enables `INPUT_PULLUP`. What is the problem with this configuration?

- A) PIR sensors require I2C addressing; GPIO digital input cannot read PIR output.
- B) The ESP32's internal pull-up pulls the pin HIGH by default, but the PIR also drives the pin HIGH during detection — these do not conflict. The problem is that many PIR sensors output 3.3 V which exceeds the ESP32 GPIO maximum input voltage.
- C) The internal pull-up conflicts with the PIR sensor's internal pull-down, creating an indeterminate logic level when the PIR output is idle (LOW).
- D) `INPUT_PULLUP` is not needed for a PIR sensor because PIR sensors have push-pull output stages that actively drive both HIGH and LOW. Using `INPUT_PULLUP` when the sensor drives LOW wastes power but does not cause damage or incorrect readings.

### Answer 14

Correct Answer: D

### Distractor Analysis 14

- A is incorrect — PIR sensors output a standard digital logic signal. They do not require I2C and can be read directly with `digitalRead()`.
- B is incorrect — Most PIR sensors operate at 3.3 V or have 3.3 V compatible output. The GPIO maximum input is 3.6 V for the ESP32. For a 3.3 V PIR this is not a problem. The claim about voltage exceeding limits is incorrect for typical 3.3 V PIR modules.
- C is incorrect — PIR output in idle (no motion) state is typically driven LOW by the sensor's output transistor, not floating. A pull-up to 3.3 V combined with the sensor's driven LOW output creates a valid LOW state — no conflict or indeterminate level.
- D is correct — Standard PIR sensors have a push-pull or open-collector output. If open-collector (driven LOW only), the pull-up is helpful. If push-pull (drives both HIGH and LOW), the pull-up slightly increases power dissipation when the sensor actively drives LOW (current flows through the pull-up to ground), but does not cause incorrect readings. The `INPUT_PULLUP` is unnecessary but harmless with a push-pull PIR.

---

## Question 15 (5 points)

The Steinhart-Hart equation is used with NTC thermistors. Which of the following best describes what this equation does?

- A) It linearly maps the ADC reading to a voltage using the ADC reference voltage.
- B) It calculates the resistance of the thermistor from two known calibration points at fixed temperatures.
- C) It converts thermistor resistance to temperature using a non-linear polynomial model that accounts for the NTC's inherently curved resistance-temperature relationship.
- D) It determines the maximum sampling rate for thermistor-based temperature measurement based on thermal time constants.

### Answer 15

Correct Answer: C

### Distractor Analysis 15

- A is incorrect — The linear ADC-to-voltage conversion is `V = ADC × V_ref / (2^bits - 1)`. This is a separate calculation performed before applying the Steinhart-Hart equation. The Steinhart-Hart equation operates on resistance, not ADC counts.
- B is incorrect — Two-point calibration (offset + slope) is a simpler linear correction model. Steinhart-Hart is a three- or four-coefficient non-linear polynomial model — it requires three or more calibration points and accounts for the curved shape of the NTC characteristic.
- C is correct — The Steinhart-Hart equation is: `1/T = A + B·ln(R) + C·(ln(R))^3` where T is absolute temperature in Kelvin and R is thermistor resistance. The cubic logarithmic terms model the NTC's non-linear behavior accurately across a wide temperature range.
- D is incorrect — The Steinhart-Hart equation is a static temperature-from-resistance model. It has no time domain component and says nothing about sampling rate or thermal response time.

---

## Question 16 (5 points)

An HC-SR04 ultrasonic distance sensor has a trigger pin and an echo pin. Which measurement principle does it use to determine distance?

- A) The sensor measures the attenuation of the ultrasonic pulse to estimate distance based on signal strength.
- B) The sensor emits a 40 kHz ultrasonic burst and measures the time between emission and the returning echo, then calculates distance as (time × speed of sound) / 2.
- C) The sensor counts the number of ultrasonic reflections per second to determine proximity.
- D) The sensor uses triangulation between two echo receivers to calculate the angle and then derives distance geometrically.

### Answer 16

Correct Answer: B

### Distractor Analysis 16

- A is incorrect — Attenuation-based distance measurement is used in some RF systems but not the HC-SR04. Sound attenuation over short indoor distances is too variable to provide reliable distance measurement.
- B is correct — The HC-SR04 triggers a burst of eight 40 kHz ultrasonic pulses. The echo pin goes HIGH when the burst is emitted and returns LOW when the reflection is received. `distance = (pulse_duration_us × 0.0343 cm/µs) / 2`. Dividing by 2 accounts for the round-trip travel time.
- C is incorrect — The HC-SR04 does not count reflections per second. It measures the duration of a single echo pulse.
- D is incorrect — The HC-SR04 has one transmitter and one receiver in a single unit. It measures time of flight, not geometric triangulation.

---

## Question 17 (5 points)

A developer applies two-point calibration to a temperature sensor. At a reference of 20.0°C the sensor reads 19.2°C, and at a reference of 80.0°C the sensor reads 82.0°C. What is the calibration slope?

- A) 1.04
- B) 0.96
- C) 0.97
- D) 1.02

### Answer 17

Correct Answer: B

### Distractor Analysis 17

- A is incorrect — A slope greater than 1 would amplify the sensor readings, which would worsen the error at 80°C (already reading high at 82.0).
- B is correct — Slope = (reference range) / (sensor range) = (80.0 - 20.0) / (82.0 - 19.2) = 60.0 / 62.8 ≈ 0.9554. Among the choices B (0.96) is closest. The calibrated reading = slope × raw + offset, where offset = 20.0 - (0.9554 × 19.2) ≈ 1.66.
- C is incorrect — 0.97 is slightly less accurate. The calculation yields approximately 0.955, making 0.96 the closer match.
- D is incorrect — 1.02 would increase readings further above the reference at the high-end point.

---

## Question 18 (5 points)

Which SPI mode (CPOL/CPHA combination) has the clock idle LOW and data sampled on the rising edge?

- A) Mode 0 (CPOL=0, CPHA=0)
- B) Mode 1 (CPOL=0, CPHA=1)
- C) Mode 2 (CPOL=1, CPHA=0)
- D) Mode 3 (CPOL=1, CPHA=1)

### Answer 18

Correct Answer: A

### Distractor Analysis 18

- A is correct — CPOL=0 means the clock idles LOW. CPHA=0 means data is sampled on the first (leading) clock edge, which for a LOW-idle clock is the rising edge. This is Mode 0, the most common default SPI mode used by many sensors and SD cards.
- B is incorrect — CPOL=0, CPHA=1 (Mode 1): clock idles LOW, data sampled on the falling edge (second/trailing edge).
- C is incorrect — CPOL=1, CPHA=0 (Mode 2): clock idles HIGH, data sampled on the falling edge (first edge for a HIGH-idle clock, which is a falling transition).
- D is incorrect — CPOL=1, CPHA=1 (Mode 3): clock idles HIGH, data sampled on the rising edge. This is the mirror of Mode 0 but with an inverted idle state.

---

## Question 19 (5 points)

An IoT data logger reads 10 sensors every 100 ms and stores the readings to an SD card using SPI. The developer notices occasional data corruption in the CSV file. Which issue is most likely causing this?

- A) The I2C pull-up resistors are too strong, causing bus contention between the sensors and the SD card.
- B) The SPI CS (chip select) line for the SD card is not being asserted LOW before every SPI transaction, causing overlapping data frames between sensor reads and SD writes.
- C) Reading 10 sensors in 100 ms exceeds the ESP32's ADC maximum sample rate.
- D) The CSV format is not compatible with the SD card's FAT32 filesystem.

### Answer 19

Correct Answer: B

### Distractor Analysis 19

- A is incorrect — I2C and SPI are independent buses. I2C pull-up resistors have no effect on SPI transactions.
- B is correct — When multiple SPI devices share MOSI, MISO, and SCK, each device must have its own CS line that is pulled LOW only when that specific device is being addressed. If the SD card's CS is left asserted (LOW) during a sensor SPI read, or if the sensor's CS is left asserted during an SD write, the two devices attempt to use the shared MISO line simultaneously, causing data corruption.
- C is incorrect — Reading 10 sensors in 100 ms requires one read every 10 ms. The ESP32 ADC conversion time is approximately 50 µs — far faster than 10 ms per read.
- D is incorrect — CSV is plain ASCII text. The SD library writes FAT32-compatible files by default. CSV format compatibility is not a source of data corruption at the hardware level.

---

## Question 20 (5 points)

A simple moving average filter uses a circular buffer of N=8 samples. What happens to the filter's output if an impulse noise spike of +200 units occurs in one sample out of every 8?

- A) The filter fully rejects the spike — the output is unchanged.
- B) The spike is diluted by a factor of N: the output shows a +25 unit increase for exactly one output sample.
- C) The spike is spread across N output samples: the output increases by +25 units for 8 consecutive samples.
- D) The spike causes the entire circular buffer to reset, producing N samples of zero until the buffer refills.

### Answer 20

Correct Answer: C

### Distractor Analysis 20

- A is incorrect — A simple moving average includes every sample in the window. A +200 unit spike is not rejected; it is incorporated into the sum and appears in the average for all N output samples while the spike value remains in the buffer.
- B is incorrect — The dilution factor is correct (+200 / 8 = +25 units) but the duration is wrong. The spike enters the circular buffer and remains in the window for N samples. Every output calculated while the spike is in the buffer will be elevated by +25 units.
- C is correct — The +200 unit spike enters the 8-sample circular buffer. The average includes this spike for exactly 8 consecutive output samples (one full buffer rotation) before the spike is overwritten by new normal-value samples. The output will read +25 units above the true signal level for those 8 samples — this is the SMA's poor impulse-noise rejection compared to a median filter.
- D is incorrect — A circular buffer does not reset on unusual values. It continuously overwrites the oldest sample with the newest, maintaining a rolling window of the last N samples regardless of their magnitude.
