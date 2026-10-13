# Video Script: Module 13 — Real-Time Operating Systems (RTOS)

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Duration:** 15–18 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **RTOS — Real-Time Operating Systems for IoT with FreeRTOS**

**Alt-text:** Instructor at desk. Title card in lower third reads "Module 13: Real-Time Operating Systems." A background monitor shows a task timeline with colored blocks representing preemptive scheduling.

**Audio:** "Welcome to Module 13. Today we explore Real-Time Operating Systems — RTOS — and specifically FreeRTOS running on the ESP32. When your embedded application grows beyond blinking an LED, you quickly encounter a fundamental problem: how do you read a sensor, process data, send it over MQTT, and respond to a button press — all apparently simultaneously — on a microcontroller with a single CPU core? The answer is an RTOS, and understanding how it works is one of the most important skills you can develop as an IoT engineer."

"By the end of this module you will be able to explain the difference between cooperative and preemptive scheduling, create FreeRTOS tasks on the ESP32 with appropriate priorities, use queues for inter-task communication, use semaphores and mutexes to protect shared resources, and configure a watchdog timer to recover from task hangs."

**Study Link:** [FreeRTOS Documentation — freertos.org](https://www.freertos.org/Documentation/RTOS_book.html)

---

### [02:00 – 04:30] What Is an RTOS?

**Visual:** Side-by-side diagram comparing a bare-metal superloop to an RTOS multi-task model.

**Alt-text:** Left panel labeled "Bare-Metal Superloop" shows a single loop with sequential function calls: read_sensor, process_data, send_mqtt, check_button, and delay_ms, all in order with a circular arrow. Right panel labeled "RTOS Multi-Task" shows three horizontal task bars running on a timeline: Task A (sensor), Task B (MQTT), Task C (UI), with a vertical arrow labeled Scheduler controlling which task runs at each time slice.

**Audio:** "In a bare-metal embedded application, you typically write a superloop — a `while(1)` that calls each function in sequence. This works for simple applications, but it has a critical limitation: if `send_mqtt()` blocks waiting for a network response for 500 milliseconds, none of the other functions run during that time. The sensor misses readings. A button press goes undetected. The system feels sluggish or misses real-time events."

"An RTOS solves this by introducing the concept of a **task** — an independent unit of execution with its own stack, its own local variables, and its own execution state. The RTOS **scheduler** rapidly switches between tasks, giving each task a slice of CPU time. From the perspective of each task, it appears to be running continuously. From the perspective of the hardware, only one task runs at any given moment, but the switching is so fast — typically every 1 millisecond — that the system behaves as though all tasks are running in parallel."

"The key property that makes an RTOS *real-time* is **determinism**: given a specific event, the RTOS guarantees a bounded response time. In a medical infusion pump, a pressure alarm must be processed within a few milliseconds regardless of what else the system is doing. An RTOS with correctly configured task priorities can provide this guarantee. A superloop cannot."

---

### [04:30 – 07:00] FreeRTOS Tasks and the Scheduler

**Visual:** Code slide showing `xTaskCreate()` with labeled parameters, then a priority diagram.

**Alt-text:** Code snippet on left half of slide showing the xTaskCreate function call with five parameters labeled: task function pointer, task name string, stack size in words, parameter pointer, priority, and task handle pointer. Right half shows a vertical priority scale from 0 (lowest, idle) at the bottom to 5 (highest, critical) at the top, with three task names placed at different priority levels.

**Audio:** "FreeRTOS is the most widely deployed RTOS in the world — it runs on billions of devices and is the default RTOS for the ESP32 in the ESP-IDF framework. Creating a task requires a single function call: `xTaskCreate()`."

"The parameters are: the task function — a C function that takes a void pointer argument and never returns, typically containing an infinite loop; the task name as a string for debugging; the stack size in 4-byte words — a task that calls complex functions needs a larger stack; an optional parameter passed to the task function; the task priority — a number from 0 (idle, lowest) to configMAX_PRIORITIES minus 1; and a task handle for later reference."

"Task priority is the most important configuration choice you make in an RTOS design. Higher priority tasks preempt lower priority tasks immediately. This means if a high-priority task is ready to run, it will interrupt any lower-priority task — the lower task is suspended mid-instruction, the high-priority task runs to completion or until it blocks, and then the lower-priority task resumes. This is **preemptive scheduling**."

"A common mistake is giving everything the same priority. If two equal-priority tasks both want to run, the scheduler uses **round-robin** time-slicing — they each get equal time slices. This is fine for tasks that are truly equal in importance, but it means neither can preempt the other even if one has a time-critical event to handle."

"Guidelines for priority assignment: use the highest priorities for tasks that respond to hardware interrupts or process safety-critical events; use medium priorities for tasks that do real-time data processing; use lower priorities for tasks that communicate over the network or update a display; and use the lowest priority for background maintenance tasks."

---

### [07:00 – 10:00] Queues — Inter-Task Communication

**Visual:** Animated diagram showing a producer task placing items into a queue and a consumer task removing them.

**Alt-text:** Two task boxes side by side: Sensor Task on the left labeled as producer, MQTT Task on the right labeled as consumer. Between them is a rectangular box divided into five cells representing the queue buffer. An arrow from Sensor Task points into the left end of the queue; an arrow from the right end of the queue points to MQTT Task. The queue shows three filled cells and two empty cells.

**Audio:** "Tasks need to exchange data, but directly writing to shared global variables is dangerous — we will cover why when we discuss mutexes. The safe way for one task to send data to another is a **queue**."

"A FreeRTOS queue is a thread-safe FIFO buffer. The producer task calls `xQueueSend()` to add an item; the consumer task calls `xQueueReceive()` to remove an item. If the queue is full when the producer tries to send, the producer can optionally block — suspending itself and yielding the CPU — until space becomes available. If the queue is empty when the consumer tries to receive, the consumer blocks until an item arrives."

"This blocking behavior is powerful: your sensor task can run at full speed, pushing readings into a queue as fast as it collects them, while your MQTT task processes readings at whatever rate the network allows. If the network is slow and the queue fills up, the sensor task automatically slows down by blocking on `xQueueSend()`. This is natural flow control with zero extra code."

"Queue items are copied by value — not by pointer. This is intentional: if you send a pointer into a queue and then modify the data the pointer refers to before the consumer reads it, the consumer receives corrupted data. Copying the value eliminates this race condition."

"For an IoT temperature sensor application, the queue element would typically be a struct containing the raw ADC reading, a timestamp, and a sensor ID. The sensor task fills this struct and sends it. The MQTT task receives it and serializes it to JSON for transmission."

---

### [10:00 – 13:00] Semaphores and Mutexes

**Visual:** Two diagrams side by side. Left shows a binary semaphore used for task synchronization. Right shows a mutex protecting a shared SPI bus.

**Alt-text:** Left diagram labeled "Binary Semaphore — Synchronization." An ISR box at the top has an arrow labeled "give" pointing to a semaphore symbol, and a Task box below has an arrow labeled "take" coming from the semaphore, with the task labeled as "unblocked." Right diagram labeled "Mutex — Mutual Exclusion." Task A and Task B boxes both have arrows pointing to a mutex lock symbol in the center, with Task A shown as "holding mutex" and Task B shown as "blocked — waiting."

**Audio:** "When two tasks access a shared resource — a peripheral like an SPI bus, a global data structure, or a file on flash — you need to ensure that only one task accesses it at a time. FreeRTOS provides two primitives for this: semaphores and mutexes."

"A **binary semaphore** has two states: available and taken. It is primarily used for **task synchronization** — signaling from one task or interrupt to another that an event has occurred. The classic pattern is: an interrupt service routine (ISR) detects that new sensor data is ready and calls `xSemaphoreGiveFromISR()`. A waiting task calls `xSemaphoreTake()` with a blocking timeout. The moment the ISR gives the semaphore, the blocked task wakes and processes the data. This eliminates polling — the task is idle until there is actual work to do."

"A **mutex** — mutual exclusion semaphore — is designed for protecting shared resources. Unlike a binary semaphore, a mutex has ownership: only the task that took the mutex can give it back. This ownership property enables **priority inheritance** — a critical RTOS feature that prevents **priority inversion**."

"Priority inversion is one of the most infamous bugs in real-time systems — it caused the Mars Pathfinder spacecraft to reset repeatedly in 1997. The scenario: a high-priority task waits for a resource held by a low-priority task. A medium-priority task preempts the low-priority task. Now the low-priority task cannot run to release the resource, so the high-priority task is blocked by a medium-priority task — the opposite of what priorities are supposed to guarantee."

"Mutex priority inheritance solves this: when a high-priority task blocks waiting for a mutex held by a low-priority task, the RTOS temporarily elevates the low-priority task's priority to match the high-priority waiter, allowing it to complete and release the mutex quickly."

---

### [13:00 – 15:30] Watchdog Timers

**Visual:** Timeline diagram showing a task feeding the watchdog, followed by a task hang scenario where the watchdog expires and triggers a reset.

**Alt-text:** A horizontal timeline with two phases. Phase 1 labeled "Normal Operation" shows a Task block repeating with a small "WDT feed" arrow between each repetition. Phase 2 labeled "Task Hang" shows the task block frozen, a "WDT expires" marker, and a "System Reset" event after a configurable timeout period.

**Audio:** "Even with a well-designed RTOS application, tasks can hang. A network call blocks indefinitely because the server never responds. A sensor read blocks waiting for an SPI transaction that never completes due to a hardware fault. An infinite loop bug is introduced in a firmware update."

"The **watchdog timer** is the hardware mechanism that recovers from these situations automatically. The watchdog is a hardware timer that counts down from a configured value — typically 5 to 30 seconds. If it reaches zero without being reset by software, it triggers a hardware reset of the microcontroller. Your firmware is responsible for periodically 'feeding' or 'kicking' the watchdog — calling a reset function to restart the countdown — as long as the system is operating correctly."

"FreeRTOS on the ESP32 includes a **Task Watchdog Timer** (TWDT) that monitors individual tasks. You register each critical task with the TWDT. Each task must call `esp_task_wdt_reset()` within a configured interval. If any registered task fails to check in — because it is hung, stuck in a blocking call, or caught in an infinite loop — the TWDT fires, logs diagnostics about which task failed, and resets the processor."

"In production IoT devices, the watchdog timer is your last line of defense against software faults that would otherwise leave the device offline indefinitely. A device that reboots itself and reconnects within 30 seconds is far more reliable than one that hangs permanently until a field technician visits."

---

### [15:30 – End] Summary and Lab Preview

**Visual:** Summary diagram showing all four concepts — tasks, queues, semaphores/mutexes, and watchdog — as components of a complete FreeRTOS application architecture.

**Alt-text:** A block diagram of a complete FreeRTOS application. Four task boxes: Sensor Task, Processing Task, MQTT Task, and UI Task. Arrows labeled Queue connect Sensor Task to Processing Task and Processing Task to MQTT Task. A mutex lock symbol is shared between Sensor Task and UI Task representing shared display access. A watchdog icon monitors all four tasks. A scheduler arrow governs all tasks from above.

**Audio:** "Let's recap Module 13. An RTOS enables multiple concurrent tasks on a single-core microcontroller using preemptive scheduling. Task priorities determine which task runs when multiple tasks are ready. Queues provide safe, blocking inter-task communication with natural flow control. Semaphores synchronize tasks with events; mutexes protect shared resources with priority inheritance. And watchdog timers provide hardware-enforced recovery from software faults."

"In this module's lab, you will implement a complete FreeRTOS application on the ESP32: a sensor simulation task that reads a value and sends it to a queue; an MQTT task that receives from the queue and publishes over TLS; a mutex protecting shared access to a display buffer; and a watchdog timer that resets the device if any task hangs."

**Key Terms for This Module:**

- RTOS — Real-Time Operating System
- Task, stack, task handle
- Preemptive scheduling vs. cooperative scheduling
- `xTaskCreate()`, task priority
- Queue — `xQueueCreate()`, `xQueueSend()`, `xQueueReceive()`
- Binary semaphore — task synchronization
- Mutex — mutual exclusion, priority inheritance
- Priority inversion
- Watchdog timer, Task Watchdog Timer (TWDT)
- `esp_task_wdt_reset()`
- FreeRTOS, ESP-IDF

"See you in Module 14 — Machine Learning for IoT with TinyML."

---
