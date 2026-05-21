# Quiz: Module 07 - Sensor Integration and Data Collection
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What is the primary function of a Cloud IoT Gateway?
*   A) To compile device firmware binaries
*   B) To authenticate devices securely and ingest massive streams of telemetry data into cloud systems
*   C) To host web client pages
*   D) To execute local physical tasks
*   **Correct Answer:** B) Cloud IoT Gateways provide the connection bridge, managing client device security certificates and ingesting raw sensor metrics.
*   **Distractor Analysis:**
    *   *Why correct:* Cloud IoT Gateways authenticate devices via certificates or tokens and route telemetry from edge networks into cloud ingestion pipelines — they do not compile firmware, host web UIs, or directly actuate physical systems.
    *   Gateways translate between local sensor protocols (MQTT, Modbus, BACnet) and cloud APIs; firmware compilation is a developer workstation task unrelated to gateway operation.

---

**Question 2**
Which of the following is the most accurate definition of **signal conditioning** in an IoT sensor pipeline?
*   A) The process of encrypting sensor readings using AES-128 before transmission to a cloud broker to prevent eavesdropping on the telemetry stream.
*   B) Processing applied to raw sensor output — including amplification, low-pass filtering, and offset correction — to maximize ADC resolution utilization and reduce noise before analog-to-digital conversion.
*   C) The firmware routine that polls sensor registers over I2C at a fixed interval and stores readings in a ring buffer for batch upload.
*   D) A calibration table stored in non-volatile memory that maps each ADC output code to a corrected physical unit value using factory reference measurements.
*   **Correct Answer:** B) Processing applied to raw sensor output — including amplification, low-pass filtering, and offset correction — to maximize ADC resolution utilization and reduce noise before analog-to-digital conversion.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* AES-128 encryption is a data security control applied after data has been digitized and processed — it is not signal conditioning.
    *   *Why B is correct:* Signal conditioning is the analog-domain preparation stage: amplifying weak signals to fill the ADC input range, filtering out frequencies above the Nyquist limit, and removing DC offsets so quantization error is minimized.
    *   *Why C is incorrect:* This describes a firmware polling and buffering pattern — a digital software construct, not the analog signal conditioning step.
    *   *Why D is incorrect:* This describes a calibration lookup table — a correction applied to already-digitized values, not the analog conditioning before the ADC.

---

**Question 3**
A vibration monitoring system samples an industrial motor at 500 Hz. A mechanical engineer reports that the motor generates bearing fault signatures at frequencies up to 300 Hz. Is the current sampling rate sufficient to detect these faults, and why?
*   A) Yes, because 500 Hz exceeds the 300 Hz fault frequency, so the ADC captures at least one sample per fault cycle.
*   B) No, because the Nyquist theorem requires a sampling rate of at least twice the highest signal frequency of interest — 600 Hz minimum — to reconstruct 300 Hz content without aliasing.
*   C) Yes, because industrial vibration sensors include built-in anti-aliasing hardware that eliminates the need for the 2x Nyquist margin.
*   D) No, because vibration signals require a sampling rate 10 times the fault frequency (3,000 Hz) to meet IEC 61508 functional safety requirements.
*   **Correct Answer:** B) No, because the Nyquist theorem requires a sampling rate of at least twice the highest signal frequency of interest — 600 Hz minimum — to reconstruct 300 Hz content without aliasing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Capturing one sample per cycle is not sufficient for accurate signal reconstruction — the Nyquist criterion requires at least two samples per cycle (at the highest frequency) to avoid aliasing distortion.
    *   *Why B is correct:* The Nyquist-Shannon sampling theorem states f_s ≥ 2 × f_max. For 300 Hz content, f_s must be at least 600 Hz. At 500 Hz, 300 Hz signals would alias to 200 Hz, producing false low-frequency readings.
    *   *Why C is incorrect:* While anti-aliasing filters are commonly used, they reduce signal content above the filter cutoff — they do not change the mathematical Nyquist requirement for a given sampling rate.
    *   *Why D is incorrect:* The 10x oversampling guideline is a practical engineering rule of thumb for waveform fidelity, not a Nyquist requirement, and IEC 61508 specifies functional safety processes, not a minimum sampling rate multiple.

---

**Question 4**
A security researcher demonstrates that by pointing a 1,000-lux flashlight at the ambient light sensor of a smart building's HVAC controller, they can force the controller to misread daytime as nighttime and trigger after-hours HVAC setback mode during business hours. Which security control most directly prevents this sensor spoofing attack?
*   A) Encrypting the sensor reading with HMAC-SHA256 before transmitting it to the HVAC controller over I2C.
*   B) Implementing anomaly detection that cross-validates the light sensor reading against a real-time clock schedule and flags readings that contradict expected daytime/nighttime patterns.
*   C) Replacing the I2C light sensor with an SPI light sensor, because SPI uses a dedicated chip-select line that prevents signal injection.
*   D) Increasing the ADC sampling rate from 1 Hz to 100 Hz so that the spoofed flash is captured as only a brief transient and averaged out.
*   **Correct Answer:** B) Implementing anomaly detection that cross-validates the light sensor reading against a real-time clock schedule and flags readings that contradict expected daytime/nighttime patterns.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* HMAC-SHA256 provides integrity for data in transit — it does not prevent the physical manipulation of the sensor's optical input that is the root cause of this attack.
    *   *Why B is correct:* Cross-validating sensor readings against corroborating data sources (real-time clock, multiple sensors, historical baselines) detects physically implausible readings. A light sensor reporting nighttime conditions at 2 PM on a Tuesday is an anomaly regardless of how the data was transmitted.
    *   *Why C is incorrect:* The choice of I2C vs SPI is an electrical interface decision; it has no bearing on the sensor's vulnerability to physical light manipulation from outside the device.
    *   *Why D is incorrect:* Increasing sampling rate and averaging reduces transient noise but does not prevent a sustained bright-light attack — averaging 100 spoofed readings per second still produces a spoofed average.

---

**Question 5**
An edge node collects temperature readings from 200 sensors at 10 Hz for 60 seconds, producing 120,000 raw data points. A data engineer proposes transmitting only the per-sensor min, max, mean, and standard deviation computed over the 60-second window rather than the raw readings. What is the primary trade-off of this aggregation approach?
*   A) The aggregated summary cannot be transmitted securely because standard TLS does not support compressed IoT payloads.
*   B) Aggregation reduces bandwidth and cloud storage by replacing 120,000 raw points with 800 summary values per cycle, but individual anomalous readings within the window are lost and cannot be reconstructed.
*   C) The standard deviation calculation requires floating-point arithmetic that exceeds the computational capacity of most ARM Cortex-M0 microcontrollers.
*   D) Transmitting statistical summaries instead of raw data violates GDPR data minimization principles because summaries retain more personal information than individual readings.
*   **Correct Answer:** B) Aggregation reduces bandwidth and cloud storage by replacing 120,000 raw points with 800 summary values per cycle, but individual anomalous readings within the window are lost and cannot be reconstructed.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* TLS supports any payload content including compressed or aggregated data — there is no restriction on IoT summary payloads.
    *   *Why B is correct:* The core trade-off of aggregation is lossy compression — the 800 summary values (200 sensors × 4 statistics) are 150x smaller than the raw data, saving bandwidth and storage, but a spike reading that lasted only one sample within the window is invisible in the aggregate.
    *   *Why C is incorrect:* Standard deviation involves a square root, which is computationally heavier than integer operations, but ARM Cortex-M0 and M4 cores are fully capable of floating-point aggregation at 10 Hz sample rates.
    *   *Why D is incorrect:* Temperature sensor readings from industrial equipment are not personal data under GDPR; data minimization applies to personal information, not machine telemetry.
