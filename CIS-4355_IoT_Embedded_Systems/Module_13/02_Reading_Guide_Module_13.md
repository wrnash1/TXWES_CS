# Reading Guide: Module 13 — Real-Time Operating Systems (RTOS)

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you should be able to:

- Explain the architectural difference between a bare-metal superloop and an RTOS task model
- Describe how a preemptive scheduler determines which task runs at any given moment
- Create and configure FreeRTOS tasks with appropriate priorities on the ESP32
- Implement safe inter-task communication using queues
- Apply semaphores and mutexes to solve synchronization and mutual exclusion problems
- Configure a Task Watchdog Timer to detect and recover from task hangs

---

## Section 1 — Why RTOS?

### The Superloop Limitation

Most beginner embedded programs use a single infinite loop — the superloop pattern — that calls each function in sequence. This architecture has a fundamental constraint: the loop executes tasks serially, so the latency of any one operation affects all others. If a network transmission takes 500 milliseconds, the entire system is blocked for 500 milliseconds.

For simple applications with one or two well-behaved tasks, the superloop is adequate. For IoT devices that must simultaneously sample sensors, process data, communicate over MQTT, manage a local display, and respond to hardware interrupts — each with different timing requirements — the superloop cannot meet all deadlines reliably.

### Real-Time Requirements

A **real-time system** is one where correctness depends not only on the logical result of a computation but also on the time at which that result is produced. An industrial robot arm controller must process encoder readings and update motor commands within microseconds; a slow-but-correct update is a dangerous-but-incorrect update. A medical alarm system must alert within a defined number of milliseconds, not "eventually."

Real-time systems are classified as:

**Hard real-time:** Missing a deadline is a system failure. Example: automotive airbag controller — the airbag must deploy within 30 milliseconds of collision detection, or the safety function fails entirely.

**Soft real-time:** Missing a deadline degrades performance but does not cause system failure. Example: an IoT dashboard that updates every second — a missed update cycle is undesirable but recoverable.

Most IoT applications are soft real-time, but many have individual functions — interrupt handling, alarm detection — that impose hard real-time requirements on specific tasks.

---

## Section 2 — RTOS Concepts

### Tasks

A **task** in FreeRTOS is a C function that runs as an independent execution unit. Each task has:

**Its own stack:** Local variables, function call frames, and return addresses for the task's execution context are stored in a dedicated memory region. Stack size is allocated at task creation and must be sufficient for the deepest call chain the task will execute, including interrupt stack frames.

**Its own state:** A task is in one of five states at any moment — Running (currently executing), Ready (ready to run, waiting for CPU), Blocked (waiting for a time delay or an event such as a queue receive), Suspended (removed from scheduling until explicitly resumed), or Deleted.

**Its own priority:** An integer from 0 (lowest) to configMAX_PRIORITIES - 1 (highest). The scheduler always runs the highest-priority Ready task.

Tasks are created with `xTaskCreate()` or `xTaskCreatePinnedToCore()` (ESP32-specific, for dual-core assignment). Every task function must contain an infinite loop and must never return — a task that returns without calling `vTaskDelete(NULL)` causes undefined behavior.

### The Scheduler

The FreeRTOS scheduler runs from a hardware timer interrupt — on the ESP32, this fires every 1 millisecond by default (configurable). At each tick, the scheduler evaluates which task should run:

1. If any task at a higher priority than the currently running task becomes Ready, the scheduler immediately preempts the current task and runs the higher-priority one. This is **preemption**.

2. If multiple tasks at the same priority are Ready, the scheduler rotates between them in round-robin fashion, giving each task a single time-slice tick. This is **time-slicing**.

3. A running task may voluntarily yield the CPU before its time slice expires by calling `vTaskDelay()`, `xQueueReceive()` with a blocking timeout, or `xSemaphoreTake()`. This is **cooperative yield** within a preemptive system.

The scheduler's context switch operation saves the current task's CPU register state (program counter, stack pointer, general registers) to its Task Control Block (TCB) and restores the TCB of the next task to run. On the ESP32 Xtensa LX6 core, a context switch takes approximately 1–2 microseconds.

### The Idle Task

FreeRTOS automatically creates an Idle Task at priority 0. The Idle Task runs only when no other task is Ready. Its functions include: executing the CPU sleep instruction to save power, processing deleted task cleanup, and running the `vApplicationIdleHook()` callback if configured. Your application should never block the Idle Task from running — if all tasks are blocked simultaneously, the Idle Task runs and can put the processor in low-power mode.

---

## Section 3 — Queues

### Queue Architecture

A FreeRTOS queue is a kernel-managed FIFO buffer that enables safe data transfer between tasks (and between interrupt service routines and tasks). Queues are created with `xQueueCreate(length, itemSize)` where `length` is the maximum number of items and `itemSize` is the size in bytes of each item (which must be uniform — all items in a queue are the same type).

Key properties:

**Thread safety:** All queue operations are protected by the FreeRTOS scheduler. You never need to disable interrupts or acquire a separate lock before calling `xQueueSend()` or `xQueueReceive()`.

**Blocking:** Both send and receive operations accept a `xTicksToWait` timeout parameter. If a task attempts to send to a full queue, it blocks for up to that many ticks before giving up. If a task attempts to receive from an empty queue, it blocks until an item arrives or the timeout expires. A timeout of `portMAX_DELAY` blocks indefinitely.

**Copy semantics:** Queue items are copied into the queue buffer on send and copied out on receive. The sender's copy and the receiver's copy are independent — modifying the sender's struct after sending does not affect the item already in the queue.

### ISR-Safe Queue Operations

Interrupt Service Routines cannot use the standard `xQueueSend()` function because it may block, and ISRs must never block. ISR-safe variants — `xQueueSendFromISR()` and `xQueueReceiveFromISR()` — take an additional `pxHigherPriorityTaskWoken` pointer parameter. After the ISR completes, if this flag is set to `pdTRUE`, the ISR should call `portYIELD_FROM_ISR()` to trigger an immediate context switch to the unblocked task.

### Queue Sets

When a task needs to receive from multiple queues, a **Queue Set** allows blocking on any of several queues simultaneously. The task calls `xQueueSelectFromSet()`, which blocks until any queue in the set has an item, then returns a handle identifying which queue is ready. This pattern is the FreeRTOS equivalent of a `select()` call in network programming.

---

## Section 4 — Semaphores and Mutexes

### Binary Semaphores — Signaling

A binary semaphore is a synchronization primitive with two operations: Give (signal that an event occurred) and Take (wait for an event). Unlike a mutex, a binary semaphore has no ownership — any task or ISR can give it, and any task can take it.

The primary use case is **event notification**: an ISR detects a hardware event and gives a semaphore; a waiting task takes the semaphore and processes the event. This pattern avoids polling (continuously checking a flag in a loop), which wastes CPU cycles, and avoids processing in the ISR itself (which must be kept short).

Counting semaphores generalize this: they maintain a count that increments on Give and decrements on Take, blocking when the count reaches zero. They are used for resource pool management — if you have three available DMA channels, a counting semaphore initialized to 3 allows three tasks to acquire channels simultaneously; the fourth waits.

### Mutexes — Mutual Exclusion

A **mutex** (mutual exclusion semaphore) is a lock that protects a shared resource from concurrent access. Unlike a binary semaphore:

**Ownership:** Only the task that took the mutex may give it back. Attempting to give a mutex from a different task is undefined behavior.

**Priority inheritance:** When a high-priority task blocks waiting for a mutex held by a low-priority task, the RTOS temporarily raises the low-priority task's priority to equal the high-priority waiter. This ensures the low-priority task can preempt medium-priority tasks to release the mutex promptly, preventing priority inversion.

**Recursive mutexes:** A task that holds a recursive mutex may take it again without deadlocking. Each take must be paired with a give. Use `xSemaphoreCreateRecursiveMutex()` and the `xSemaphoreTakeRecursive()` / `xSemaphoreGiveRecursive()` variants.

### Priority Inversion — The Mars Pathfinder Case

In August 1997, the Mars Pathfinder lander experienced repeated system resets after landing. Engineers eventually traced the root cause to priority inversion in the VxWorks RTOS:

- A low-priority task held a shared-bus mutex.
- A high-priority task (the "bc_dist" meteorological data collection task) needed the mutex.
- A medium-priority task (the "ASI/MET" task) was running, preventing the low-priority task from executing.
- The high-priority task was therefore blocked by a medium-priority task — exactly backwards from intended behavior.
- The watchdog detected the high-priority task was not completing within its deadline and reset the system.

The fix was to enable priority inheritance on the mutex — a configuration option that existed in VxWorks but had not been set. This is why FreeRTOS mutexes include priority inheritance by default and why understanding the difference between semaphores (no inheritance) and mutexes (with inheritance) is not a theoretical exercise.

---

## Section 5 — Watchdog Timers

### Hardware Watchdog

The hardware watchdog timer is a peripheral built into most microcontrollers. It counts down from a loaded value. If the firmware fails to reload the counter (feed/kick the watchdog) before it reaches zero, the timer asserts a hardware reset signal. This hardware mechanism operates independently of the CPU — even if the CPU is executing a runaway loop or is stuck in a faulted state, the watchdog fires.

The ESP32 has two hardware watchdog timers:

**Main System Watchdog (MWDT):** Associated with the Timer Group peripheral. Used by ESP-IDF to detect full system hangs.

**RTC Watchdog (RWDT):** Clocked by the RTC oscillator. Can wake the system from deep sleep if it fails to resume normal operation within a timeout — useful for detecting failures during low-power wake sequences.

### Task Watchdog Timer (TWDT)

FreeRTOS adds a software-level Task Watchdog Timer that monitors individual tasks. You register tasks of interest with `esp_task_wdt_add(NULL)` (within the task to register itself) or `esp_task_wdt_add(taskHandle)` (from outside). Each registered task must call `esp_task_wdt_reset()` within the configured timeout period (default 5 seconds in ESP-IDF).

If any registered task fails to reset the TWDT — because it is blocked, hung, or caught in an infinite loop without a yield — the TWDT handler fires. It logs the backtrace of the offending task for debugging, then triggers a system reset.

Important: the TWDT only monitors tasks you explicitly register. Unregistered tasks can hang indefinitely without triggering the TWDT. Register all tasks that perform operations with potential blocking risk: network operations, sensor reads, flash writes.

---

## Section 6 — ESP32 FreeRTOS Specifics

The ESP32 is a dual-core SoC (System on Chip) with two Xtensa LX6 cores: core 0 (Protocol CPU, often called "PRO_CPU") and core 1 (Application CPU, "APP_CPU"). FreeRTOS on the ESP32 runs symmetrically on both cores, with each core having its own scheduler instance.

`xTaskCreate()` creates a task that the scheduler may assign to either core. `xTaskCreatePinnedToCore(... , coreID)` pins a task to a specific core — 0 or 1, or `tskNO_AFFINITY` for either. Pin time-critical tasks to APP_CPU (core 1) to avoid interference from the Wi-Fi and Bluetooth stack, which runs primarily on PRO_CPU (core 0).

The ESP-IDF framework automatically starts the FreeRTOS scheduler and creates the main application task, the Wi-Fi event loop task, and several system tasks. Your `app_main()` function runs inside the main application task and has full access to all FreeRTOS APIs.

---

## Key Terms

- **RTOS** — Real-Time Operating System; enables deterministic, concurrent task execution on embedded hardware
- **Task** — independent execution unit in FreeRTOS with its own stack and priority
- **Preemptive scheduling** — scheduler can interrupt a running task to execute a higher-priority task
- **Context switch** — saving one task's CPU state and restoring another's
- **Task Control Block (TCB)** — data structure storing a task's state, priority, and stack pointer
- **Queue** — thread-safe FIFO buffer for inter-task communication; uses copy semantics
- **Binary semaphore** — two-state signaling primitive for task synchronization
- **Counting semaphore** — multi-state resource pool management
- **Mutex** — ownership-based lock with priority inheritance; protects shared resources
- **Priority inversion** — a high-priority task blocked by a low-priority task due to resource contention
- **Priority inheritance** — temporary priority elevation to prevent inversion
- **Watchdog timer** — hardware countdown timer that resets the system if not periodically fed
- **TWDT** — Task Watchdog Timer; per-task deadline monitoring in ESP-IDF
- **Idle task** — FreeRTOS priority-0 task running when no other task is ready

---

## Review Questions

1. A superloop calls three functions in sequence: `read_sensor()` (1 ms), `transmit_wifi()` (500 ms), and `update_display()` (2 ms). What is the worst-case latency for a new sensor reading to begin processing?
2. In FreeRTOS, what happens immediately when a task with priority 5 becomes Ready while a task with priority 3 is running?
3. Why must the task function in FreeRTOS contain an infinite loop and never return?
4. What is the difference between `xQueueSend()` and `xQueueSendFromISR()`? When must you use the ISR variant?
5. Explain why FreeRTOS queues use copy semantics rather than pointer semantics, and what race condition copy semantics prevent.
6. What is the key operational difference between a binary semaphore and a mutex that makes a mutex safer for protecting shared resources?
7. Describe the Mars Pathfinder priority inversion scenario: which three tasks were involved, what resource was contended, and what was the observable symptom?
8. A task calls `xSemaphoreTake(mutex, portMAX_DELAY)` and blocks indefinitely. Another task holds the mutex and is itself blocked waiting for a hardware event for 60 seconds. What happens to a third high-priority task that also needs the mutex?
9. What is the purpose of `esp_task_wdt_reset()`, and what are the consequences if a registered task fails to call it within the configured timeout?
10. On the ESP32 dual-core architecture, why is it often advisable to pin time-critical application tasks to APP_CPU (core 1) rather than PRO_CPU (core 0)?

---
