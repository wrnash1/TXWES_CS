# Lab Activity: Module 13 — Real-Time Operating Systems (RTOS)

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Time:** 90–120 minutes

---

## Objective

Implement a complete FreeRTOS application on the ESP32 that demonstrates: multiple concurrent tasks with different priorities, a queue for inter-task communication, a mutex protecting a shared resource, and a Task Watchdog Timer for fault recovery. You will observe preemptive scheduling in action through serial output timestamps.

---

## Prerequisites

- ESP32 development board (any variant with at least 4 MB flash)
- ESP-IDF v5.x installed, or Arduino IDE with ESP32 board support package
- USB cable and serial monitor (115200 baud)
- Completed Module 12 lab (familiarity with the ESP32 build environment)

---

## Part 1 — Project Setup

### Step 1.1 — Create the project

Using Arduino IDE, create a new sketch and save it as `rtos_lab_m13`. If using ESP-IDF, create a new project with `idf.py create-project rtos_lab_m13`.

The complete application will use the Arduino-style entry point (`setup()` and `loop()`) while still using FreeRTOS APIs directly — both are fully supported.

### Step 1.2 — Include headers

```cpp
#include <Arduino.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/queue.h>
#include <freertos/semphr.h>
#include <esp_task_wdt.h>

// Watchdog timeout in seconds
#define WDT_TIMEOUT_S  5

// Queue length and item size
#define QUEUE_LENGTH   10
```

---

## Part 2 — Define the Shared Data Structure

```cpp
// Sensor reading passed through the queue
struct SensorReading {
  uint32_t timestamp_ms;
  float    temperature_c;
  uint8_t  sensor_id;
};

// Handles — global so all tasks can access
QueueHandle_t  xSensorQueue;
SemaphoreHandle_t xDisplayMutex;
```

---

## Part 3 — Sensor Task (Producer, Priority 3)

This task simulates a temperature sensor reading every 500 ms and sends the data into the queue.

```cpp
void vSensorTask(void *pvParameters) {
  // Register this task with the Task Watchdog Timer
  esp_task_wdt_add(NULL);

  SensorReading reading;
  reading.sensor_id = 1;
  float simTemp = 20.0f;

  for (;;) {
    // Simulate a sensor read
    reading.timestamp_ms  = (uint32_t)xTaskGetTickCount() * portTICK_PERIOD_MS;
    reading.temperature_c = simTemp + ((float)(esp_random() % 100) / 100.0f - 0.5f);
    simTemp += 0.1f;  // Slowly drifting temperature

    // Send to queue; block up to 100 ms if full
    if (xQueueSend(xSensorQueue, &reading, pdMS_TO_TICKS(100)) == pdPASS) {
      Serial.printf("[Sensor  T=%lu ms] Reading %.2f C queued\n",
                    reading.timestamp_ms, reading.temperature_c);
    } else {
      Serial.println("[Sensor  WARNING] Queue full — reading dropped");
    }

    // Feed the watchdog
    esp_task_wdt_reset();

    // Wait 500 ms before next reading
    vTaskDelay(pdMS_TO_TICKS(500));
  }
}
```

---

## Part 4 — Processing Task (Consumer + Producer, Priority 2)

This task dequeues raw readings, applies a calibration offset, and prints processed output while holding the display mutex.

```cpp
void vProcessingTask(void *pvParameters) {
  esp_task_wdt_add(NULL);

  SensorReading raw;
  const float CALIBRATION_OFFSET = 0.5f;

  for (;;) {
    // Block indefinitely waiting for a new reading
    if (xQueueReceive(xSensorQueue, &raw, portMAX_DELAY) == pdPASS) {
      float calibrated = raw.temperature_c + CALIBRATION_OFFSET;

      // Acquire display mutex before writing to serial (shared resource)
      if (xSemaphoreTake(xDisplayMutex, pdMS_TO_TICKS(200)) == pdTRUE) {
        Serial.printf("[Process T=%lu ms] Calibrated: %.2f C (raw: %.2f C)\n",
                      raw.timestamp_ms, calibrated, raw.temperature_c);
        xSemaphoreGive(xDisplayMutex);
      } else {
        // Could not acquire mutex within 200 ms — log and continue
        Serial.println("[Process WARNING] Display mutex timeout");
      }
    }

    esp_task_wdt_reset();
  }
}
```

---

## Part 5 — Status Task (Low Priority, Priority 1)

This task prints a heartbeat message every 3 seconds, demonstrating that a low-priority task still runs when higher-priority tasks are blocked.

```cpp
void vStatusTask(void *pvParameters) {
  esp_task_wdt_add(NULL);

  UBaseType_t stackHighWater;

  for (;;) {
    // Acquire display mutex
    if (xSemaphoreTake(xDisplayMutex, pdMS_TO_TICKS(500)) == pdTRUE) {
      // Report queue depth and stack headroom
      stackHighWater = uxTaskGetStackHighWaterMark(NULL);
      Serial.printf("[Status  T=%lu ms] Queue depth: %u | Stack free: %u words\n",
                    (uint32_t)xTaskGetTickCount() * portTICK_PERIOD_MS,
                    (unsigned)uxQueueMessagesWaiting(xSensorQueue),
                    (unsigned)stackHighWater);
      xSemaphoreGive(xDisplayMutex);
    }

    esp_task_wdt_reset();
    vTaskDelay(pdMS_TO_TICKS(3000));
  }
}
```

---

## Part 6 — setup() and loop()

```cpp
void setup() {
  Serial.begin(115200);
  vTaskDelay(pdMS_TO_TICKS(500));  // Allow serial to stabilize

  Serial.println("\n=== FreeRTOS Lab — Module 13 ===");

  // Initialize Task Watchdog Timer
  esp_task_wdt_init(WDT_TIMEOUT_S, true);  // true = panic on timeout

  // Create queue: 10 SensorReading items
  xSensorQueue  = xQueueCreate(QUEUE_LENGTH, sizeof(SensorReading));
  xDisplayMutex = xSemaphoreCreateMutex();

  if (xSensorQueue == NULL || xDisplayMutex == NULL) {
    Serial.println("[FATAL] Failed to create RTOS primitives — halting");
    while (1) {}
  }

  // Create tasks — pinned to APP_CPU (core 1) to isolate from Wi-Fi stack
  xTaskCreatePinnedToCore(vSensorTask,     "SensorTask",     4096, NULL, 3, NULL, 1);
  xTaskCreatePinnedToCore(vProcessingTask, "ProcessingTask", 4096, NULL, 2, NULL, 1);
  xTaskCreatePinnedToCore(vStatusTask,     "StatusTask",     4096, NULL, 1, NULL, 1);

  Serial.println("[Setup] All tasks created. Scheduler running.");
}

void loop() {
  // loop() runs in the Arduino main task — give it lowest useful priority
  // and yield frequently so it does not starve other tasks
  vTaskDelay(pdMS_TO_TICKS(10000));
}
```

---

## Part 7 — Observe Scheduling Behavior

### Step 7.1 — Build and flash

Build and flash the sketch to your ESP32. Open the serial monitor at 115200 baud.

### Step 7.2 — Expected output pattern

```text
=== FreeRTOS Lab — Module 13 ===
[Setup] All tasks created. Scheduler running.
[Sensor  T=500 ms] Reading 20.23 C queued
[Process T=500 ms] Calibrated: 20.73 C (raw: 20.23 C)
[Sensor  T=1000 ms] Reading 20.37 C queued
[Process T=1000 ms] Calibrated: 20.87 C (raw: 20.37 C)
[Sensor  T=1500 ms] Reading 20.44 C queued
[Process T=1500 ms] Calibrated: 20.94 C (raw: 20.44 C)
[Status  T=3000 ms] Queue depth: 0 | Stack free: 1892 words
```

Observe that the Sensor Task (priority 3) and Processing Task (priority 2) interleave naturally, and the Status Task (priority 1) only runs when both higher-priority tasks are blocked.

### Step 7.3 — Simulate a queue overflow

Temporarily change the sensor task delay from 500 ms to 50 ms (10x faster). Rebuild and flash. Observe the "Queue full — reading dropped" warning appearing in the serial output, demonstrating the queue's built-in flow control behavior.

Revert the delay to 500 ms.

### Step 7.4 — Simulate a watchdog trigger

Temporarily add an intentional hang to the sensor task — add `while(1){}` after the `xQueueSend()` call and remove the `esp_task_wdt_reset()` call. Rebuild and flash. Observe the watchdog timer triggering after 5 seconds with a panic message and backtrace identifying the "SensorTask" as the offending task.

Revert the change before submitting your deliverables.

---

## Part 8 — Priority Demonstration (Analysis Exercise)

In your lab report, answer the following questions based on your observations:

1. When the Processing Task is blocked on `xQueueReceive(portMAX_DELAY)`, which task runs? How do you know from the serial output?
2. If you set all three tasks to priority 1, predict what the output pattern would look like. Then make the change, observe the result, and compare it to your prediction. What changed and why?
3. The Sensor Task uses priority 3. What would happen if you created a new task at priority 4 that ran an infinite loop with `vTaskDelay(pdMS_TO_TICKS(1))` but no watchdog feed? Explain the consequences without implementing it.

---

## Troubleshooting Guide

- **Error: Guru Meditation Error: Core panic** — This is expected in Step 7.4 when you deliberately hang the sensor task. If it occurs unexpectedly, check that all tasks call `esp_task_wdt_reset()` within the 5-second timeout.
- **Error: xQueueCreate returns NULL** — Insufficient heap memory. Reduce queue length or task stack sizes. Check available heap with `ESP.getFreeHeap()`.
- **Serial output garbled or interleaved mid-line** — The mutex is not being held during the entire `Serial.printf()` call. Ensure `xSemaphoreTake()` is called before and `xSemaphoreGive()` is called after each serial print block.
- **Status Task never prints** — Higher-priority tasks are not blocking long enough to let the Status Task run. Verify `vTaskDelay()` calls are present in Sensor and Processing tasks.

---

## Deliverables

Submit the following to the Canvas LMS assignment portal:

1. Complete source code for the FreeRTOS lab application.
2. Screenshot of the serial monitor showing at least 10 seconds of output from normal operation (Step 7.2).
3. Screenshot of the serial monitor showing the queue overflow warning from Step 7.3.
4. Screenshot of the watchdog panic output from Step 7.4, with the offending task name visible in the panic message.
5. Written answers to the three analysis questions in Part 8 (150–200 words total).

---
