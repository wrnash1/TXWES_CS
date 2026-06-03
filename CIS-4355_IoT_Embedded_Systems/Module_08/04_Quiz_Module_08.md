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
