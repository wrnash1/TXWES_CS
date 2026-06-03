# Discussion Forum: Module 13 — Real-Time Operating Systems (RTOS)

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Overview

This week's discussion asks you to apply FreeRTOS design principles to three realistic IoT engineering scenarios. Each scenario involves a real trade-off or failure mode that practicing engineers encounter. Strong initial posts demonstrate understanding of *why* a design decision is correct — not just *what* the correct answer is.

---

## Scenario 1 — The Industrial Sensor Priority Design

You are designing a FreeRTOS application for an ESP32 deployed in a natural gas pipeline monitoring system. The application must perform five functions:

- Read a pressure sensor via SPI every 100 ms — any missed reading is a safety gap
- Read a temperature sensor via I2C every 500 ms — informational, not safety-critical
- Transmit readings to a cloud backend over MQTT every 10 seconds — network operations may block for up to 2 seconds
- Update a local OLED display with current readings — purely cosmetic
- Blink a status LED to indicate connectivity — purely cosmetic

The ESP32 has 520 KB of SRAM, and each task requires approximately 4 KB of stack.

Discuss the following:

- Assign a FreeRTOS priority (1–5) to each of the five functions, implemented as separate tasks. Justify each assignment based on the timing requirements and consequences of missing a deadline.
- The MQTT task may block for up to 2 seconds waiting for a server acknowledgment. What mechanism prevents this blocking from starving the pressure sensor task? Explain the mechanism in technical terms.
- If the SPI and I2C sensors share the same SPI bus (a common hardware design), what FreeRTOS primitive do you use to prevent the two sensor tasks from accessing the bus simultaneously? Why can't you use a binary semaphore for this purpose?

Your initial post should be 175–225 words and address all three questions with specific FreeRTOS API references where appropriate.

---

## Scenario 2 — Diagnosing a Watchdog Reset Loop

A field-deployed ESP32 IoT device that monitors air quality in a building starts rebooting every 45 seconds. The device's serial log (captured over UART) shows the following before each reset:

```text
E (45023) task_wdt: Task watchdog got triggered. The following tasks/users did not reset the watchdog in time:
E (45023) task_wdt:  - IDLE (CPU 0)
E (45023) task_wdt: Tasks currently running:
E (45023) task_wdt: CPU 0: CO2_ProcessTask
E (45023) task_wdt: CPU 1: IDLE
```

The `CO2_ProcessTask` reads CO2 sensor data, applies a calibration algorithm, and uploads results to an S3 bucket using HTTP POST. The TWDT timeout is configured to 30 seconds.

Discuss the following:

- Based on the watchdog log, which task caused the reset and why? Explain what "IDLE (CPU 0) did not reset the watchdog" means in the context of the FreeRTOS Task Watchdog Timer.
- What is the most likely root cause of the CO2_ProcessTask running continuously without yielding for more than 30 seconds?
- Propose two specific code-level fixes: one that addresses the root cause of the continuous run, and one that adds a safety net so this class of problem is detected faster in the future.

Your initial post should be 175–225 words. Do not just say "add a vTaskDelay" — explain the specific mechanism at play.

---

## Scenario 3 — Queue Depth and System Sizing

You are adding a data logging feature to an ESP32 environmental monitoring system. A sensor task produces 20 readings per second (one every 50 ms). A logging task writes each reading to a microSD card via SPI, which takes between 5 ms (fast write) and 80 ms (slow write when the card performs internal block erasure). You need to size the FreeRTOS queue between the sensor task and the logging task.

Discuss the following:

- During a worst-case 80 ms SD write, how many readings does the sensor task produce? How does this determine the minimum queue depth needed to prevent data loss?
- If you size the queue for the minimum depth from the previous calculation, what happens during an extended period of slow writes — for example, if the SD card performs 10 consecutive slow writes in a row?
- A classmate suggests using `xQueueOverwrite()` instead of `xQueueSend()` so that the sensor task never blocks and always publishes the most recent reading. Evaluate this suggestion: in what application is it appropriate, and in what application is it a data integrity problem?

Your initial post should be 175–225 words. Peer responses should include a specific queue depth recommendation with arithmetic justification.

---

## Discussion Instructions

### Initial Post

Due: Wednesday at 11:59 PM

Choose one scenario (or address all three for extra credit). Write 175–225 words per scenario addressed. Your post must include:

- Specific FreeRTOS API names or concepts (task priorities, queue operations, semaphore types, watchdog functions)
- Technical reasoning, not just conclusions
- At least one trade-off or limitation of your proposed approach

### Peer Responses

Due: Sunday at 11:59 PM

Reply to at least two classmates (minimum 60 words each). In your replies:

- Verify their priority assignment arithmetic (Scenario 1) or queue depth calculation (Scenario 3)
- Identify any FreeRTOS API they referenced incorrectly
- Propose an alternative design choice and explain its trade-offs

---

## Discussion Rubric (10 Points Total)

### Initial Post — 6 Points

- 5–6 pts: Addresses all sub-questions for the chosen scenario. Correct use of FreeRTOS terminology and API names. Technical justification with explicit trade-off acknowledgment. Meets 175-word minimum.
- 3–4 pts: Addresses most sub-questions. FreeRTOS concepts referenced but not always precisely. Some justification present.
- 0–2 pts: Post is missing, below minimum length, or does not engage technically with the scenario.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies verifying or constructively challenging the technical content. Each meets the 60-word minimum.
- 2 pts: One substantive reply, or two replies that only agree without adding technical content.
- 0 pts: No peer responses submitted.

---
