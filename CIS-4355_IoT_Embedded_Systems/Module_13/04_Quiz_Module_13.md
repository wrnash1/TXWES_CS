# Quiz: Module 13 — Real-Time Operating Systems (RTOS)

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

### Question 1

A FreeRTOS application has three tasks: Task A at priority 5, Task B at priority 3, and Task C at priority 1. Task A and Task C are both in the Blocked state waiting for separate queue receives. Task B is in the Running state. Task A's queue receives an item. What happens next, and why?

- A) Task A becomes Ready and is added to the end of the run queue. The scheduler will execute Task A after Task B completes its current time slice.
- B) Task A becomes Ready and immediately preempts Task B, because Task A has a higher priority. Task B is suspended mid-execution and resumes only after Task A blocks or yields.
- C) Task A becomes Ready but cannot run until Task B voluntarily calls `vTaskDelay()` or yields, because preemption only occurs at tick boundaries.
- D) Task A becomes Ready and is swapped with Task C, since both are lower priority than Task B and the scheduler balances the run queue by promoting the longest-waiting task.
- **Correct Answer:** B) Task A immediately preempts Task B.
- **Distractor Analysis:**
  - *Why A is incorrect:* This describes cooperative scheduling, not preemptive scheduling. In FreeRTOS's preemptive mode, a higher-priority task that becomes Ready immediately preempts any lower-priority running task. There is no waiting for the current time slice to complete.
  - *Why B is correct:* When a queue item arrives and unblocks Task A (priority 5), the FreeRTOS scheduler immediately detects that a higher-priority task is now Ready. It saves Task B's context and switches to Task A. Task B resumes only when Task A enters a Blocked or Suspended state. This is the defining characteristic of preemptive scheduling.
  - *Why C is incorrect:* Preemption in FreeRTOS occurs at every tick interrupt and on any event that makes a higher-priority task Ready — not only when the running task voluntarily yields. The tick ISR checks for higher-priority Ready tasks after every tick.
  - *Why D is incorrect:* FreeRTOS scheduling is strictly priority-based. There is no "load balancing" or longest-wait promotion in the base scheduler. Task C (priority 1) is not involved in the scheduling decision between Task A (priority 5) and Task B (priority 3).

---

### Question 2

An IoT application stores the current GPS coordinate in a global `struct GpsCoord { float lat; float lon; }` that is updated by a GPS task and read by an MQTT publishing task. The developer argues that because the ESP32 is a 32-bit processor and each float is 32 bits, each field update is atomic, so no mutex is needed. What is wrong with this reasoning?

- A) Nothing is wrong — 32-bit reads and writes are indeed atomic on ARM Cortex-M processors, and since each struct field is independently 32-bit aligned, no mutex is required.
- B) The reasoning is flawed because the struct contains two fields. The GPS task updates `lat` and then `lon` as two separate 32-bit operations. If the RTOS preempts between the two writes, the MQTT task may read a `lat` from the new fix paired with a `lon` from the previous fix — a partially updated, geographically invalid coordinate.
- C) The reasoning is flawed because FreeRTOS disables all interrupts during task preemption, which makes 32-bit stores non-atomic even for individually aligned fields.
- D) The reasoning is valid for the struct fields but fails because the ESP32's Wi-Fi stack accesses GPS data on core 0 simultaneously, and cross-core memory access is never atomic.
- **Correct Answer:** B) Two separate 32-bit writes are not an atomic update of the entire struct.
- **Distractor Analysis:**
  - *Why A is incorrect:* Individual 32-bit field writes may be atomic, but the struct update as a whole is not. Atomicity of individual writes does not guarantee the atomicity of composite updates that span multiple writes.
  - *Why B is correct:* The GPS coordinate is only meaningful as a lat/lon pair. Two individually atomic writes do not compose into an atomically consistent struct update. A preemption between the two writes leaves the struct in an intermediate state: the new latitude paired with the old longitude. A mutex wrapping both writes ensures the reader always sees either the complete previous coordinate or the complete new one — never a mix.
  - *Why C is incorrect:* FreeRTOS does not disable interrupts during task preemption of normal tasks. The context switch is triggered by the tick ISR and occurs at tick boundaries or at scheduler-aware blocking calls. Individual 32-bit aligned stores are still atomic at the hardware level.
  - *Why D is incorrect:* While cross-core access is a valid concern on the dual-core ESP32, it is a separate issue. The primary flaw identified in the question is the two-write non-atomicity of the struct update, which exists even on a single-core system.

---

### Question 3

A developer creates a FreeRTOS queue with a length of 5 and an item size of `sizeof(SensorReading)`. The producer task sends items every 100 ms. The consumer task processes each item and takes 600 ms per item. What happens to the queue over time, and what is the eventual outcome?

- A) The queue fills up at a rate of one item per 100 ms while the consumer processes at one per 600 ms. After 500 ms (5 items), the queue is full. The producer task blocks on `xQueueSend()` until the consumer processes an item, naturally throttling the producer to the consumer's processing rate of one item per 600 ms.
- B) The queue fills up and, when full, new items overwrite the oldest item in the queue, ensuring the consumer always receives the most recent readings rather than backlogged ones.
- C) The queue fills up and the producer task crashes with a stack overflow because blocking on `xQueueSend()` causes recursive task reentry.
- D) The queue fills up and the FreeRTOS scheduler automatically increases the consumer task's priority to match the producer's rate, preventing queue overflow.
- **Correct Answer:** A) The producer blocks on `xQueueSend()`, naturally throttling to the consumer's rate.
- **Distractor Analysis:**
  - *Why A is correct:* When `xQueueSend()` is called with a non-zero `xTicksToWait` on a full queue, the calling task enters the Blocked state and is removed from the scheduler's run queue until space becomes available. The moment the consumer dequeues an item, the producer unblocks and sends its item. This is the natural flow control behavior of FreeRTOS queues — no additional code is required to prevent queue overflow when the producer is faster than the consumer.
  - *Why B is incorrect:* FreeRTOS queues are strict FIFOs — they do not overwrite on overflow. The `xQueueOverwrite()` API exists for single-item "mailbox" queues (length 1) and is a separate, explicitly chosen pattern. Standard multi-item queues never silently overwrite.
  - *Why C is incorrect:* Blocking on `xQueueSend()` suspends the task cleanly — it does not cause stack overflow or recursion. The task simply waits in the Blocked state.
  - *Why D is incorrect:* FreeRTOS does not automatically adjust task priorities based on queue depth. Priority management is the application developer's responsibility. The scheduler has no built-in queue-aware dynamic priority system.

---

### Question 4

What is the critical difference between a binary semaphore and a mutex in FreeRTOS, and in which scenario does this difference prevent a system fault?

- A) A mutex can be given from an ISR using `xSemaphoreGiveFromISR()`, while a binary semaphore cannot. This is critical when hardware interrupt handlers need to signal a task to process incoming data.
- B) A mutex enforces ownership — only the task that took it can give it — and includes priority inheritance. A binary semaphore has no ownership and no inheritance. This prevents priority inversion when a high-priority task needs a resource held by a low-priority task.
- C) A binary semaphore can be created with a count greater than 1 (making it a counting semaphore), while a mutex is permanently binary. This allows semaphores to manage pools of identical resources.
- D) A mutex blocks the scheduler when acquired, preventing any context switch until it is released. A binary semaphore does not block the scheduler, allowing preemption to continue during the protected section.
- **Correct Answer:** B) Mutex has ownership and priority inheritance; semaphore does not — preventing priority inversion.
- **Distractor Analysis:**
  - *Why A is incorrect:* This is backwards. Binary semaphores have ISR-safe give variants (`xSemaphoreGiveFromISR()`); mutexes do NOT have ISR-safe variants and must never be used from ISRs. The ISR-safety advantage belongs to the semaphore, not the mutex.
  - *Why B is correct:* The ownership property ensures that a mutex is always released by the task that acquired it, preventing accidental release from a wrong context. Priority inheritance is the key safety property: when a high-priority task blocks on a mutex held by a low-priority task, the RTOS temporarily elevates the low-priority task's priority to prevent medium-priority tasks from starving the low-priority task and thereby indirectly blocking the high-priority one. This is the Mars Pathfinder fix.
  - *Why C is incorrect:* This describes a counting semaphore, which is a separate primitive created with `xSemaphoreCreateCounting()`. A binary semaphore is always binary (count of 0 or 1). This distinction is about semaphore types, not the semaphore-vs-mutex distinction.
  - *Why D is incorrect:* A mutex does not block the scheduler. Both mutexes and semaphores allow preemption to continue. The acquiring task may be preempted by a higher-priority task while holding a mutex — priority inheritance then ensures the holder is elevated to complete its critical section promptly.

---

### Question 5

The Mars Pathfinder mission experienced repeated system resets in 1997 due to priority inversion. Three tasks were involved. Which of the following correctly describes the three-task scenario and explains why priority inheritance would have prevented the resets?

- A) A high-priority communications task and a medium-priority display task both needed a shared serial bus. The medium-priority task held the bus for extended transmissions, starving the high-priority task. Priority inheritance would have given the display task maximum priority, causing it to finish faster.
- B) A low-priority meteorological data task held a shared-bus mutex. A high-priority data distribution task needed the mutex. A medium-priority communications task preempted the low-priority task. Priority inheritance would have temporarily elevated the low-priority task to high priority, allowing it to preempt the medium-priority task and release the mutex quickly.
- C) The high-priority task held a mutex indefinitely due to a software bug. The medium-priority task tried to acquire the mutex and blocked. The low-priority task ran in the idle slot. Priority inheritance would have detected the indefinite hold and automatically released the mutex after a timeout.
- D) Two high-priority tasks competed for the same mutex using a try-lock without blocking, causing a livelock where neither task could proceed. Priority inheritance would have given one task exclusive access by detecting the livelock condition.
- **Correct Answer:** B) Low-priority task held mutex; high-priority task needed it; medium-priority task prevented the low-priority task from running.
- **Distractor Analysis:**
  - *Why A is incorrect:* This describes resource contention between a high and medium priority task — a simpler starvation scenario without the three-tier inversion pattern. Priority inversion requires exactly three priority levels: a high task blocked by a low task while a medium task runs.
  - *Why B is correct:* This accurately describes the Mars Pathfinder scenario. The "bc_dist" (high priority) task needed a shared-bus mutex held by the "ASI/MET" (low priority) task. The "T_TASK" (medium priority) was running, preventing the low-priority task from executing and releasing the mutex. The high-priority task was therefore effectively blocked by a medium-priority task. Priority inheritance would have elevated the low-priority holder to high priority, allowing it to preempt the medium-priority task, release the mutex, and unblock the high-priority task within milliseconds.
  - *Why C is incorrect:* Priority inheritance does not include automatic mutex release on timeout — that would violate the principle of ownership and could corrupt the shared resource. The fix to an indefinitely held mutex is application-level bug correction, not an RTOS feature.
  - *Why D is incorrect:* Livelock from competing try-lock operations is a different concurrency problem, not priority inversion. Priority inheritance is specifically the solution to the three-tier priority inversion scenario, not to livelock.

---

### Question 6

A FreeRTOS task registered with the ESP32 Task Watchdog Timer (TWDT) has a 5-second timeout. The task performs a network HTTP request that normally completes in 200 ms but occasionally blocks for up to 30 seconds when the remote server is unresponsive. What is the correct design to handle this without triggering a false watchdog reset?

- A) Increase the TWDT timeout to 35 seconds to accommodate the worst-case 30-second block, ensuring the task never triggers a false reset.
- B) Use a non-blocking or timeout-bounded HTTP request (set a connection and response timeout of 4 seconds), call `esp_task_wdt_reset()` before the request, and handle the timeout error gracefully — retry or reconnect. This keeps the watchdog window achievable while bounding the potential block duration.
- C) Remove the network task from TWDT monitoring, since network tasks are expected to block for unpredictable durations and watchdog monitoring of such tasks is not appropriate.
- D) Call `esp_task_wdt_reset()` from inside the HTTP library's socket receive callback — since this function is called periodically during a long transfer, it will feed the watchdog during the blocking period.
- **Correct Answer:** B) Apply a 4-second HTTP timeout and call `esp_task_wdt_reset()` before the request.
- **Distractor Analysis:**
  - *Why A is incorrect:* Increasing the TWDT timeout to 35 seconds defeats the purpose of the watchdog. A 35-second unresponsive system is operationally equivalent to a hung system. The goal of watchdog design is to keep the detection window as short as is practically achievable, not to expand it to cover worst-case blocking scenarios.
  - *Why B is correct:* The correct approach is to bound the blocking behavior at the application level — not to expand the watchdog window. Setting HTTP connection and response timeouts to 4 seconds ensures the task will always return within that window, then calling `esp_task_wdt_reset()` after each attempted request maintains the watchdog contract. If the server is unresponsive, the task gets a timeout error it can handle gracefully, rather than blocking indefinitely.
  - *Why C is incorrect:* Removing network tasks from TWDT monitoring eliminates protection against actual hangs in those tasks — infinite blocking on a broken socket, for example. Network tasks should be monitored; their blocking must be bounded by application-level timeouts, not by exempting them from watchdog supervision.
  - *Why D is incorrect:* HTTP library socket callbacks may not be called at all if the server stops sending data entirely — exactly the scenario that causes indefinite blocking. Relying on callbacks to feed the watchdog makes the watchdog's behavior dependent on the remote server, which is precisely the risk we are trying to mitigate.

---

### Question 7

What is the purpose of the FreeRTOS Idle Task, and what consequence follows if an application task holds the CPU continuously at a priority above 0 without ever blocking or yielding?

- A) The Idle Task manages task deletion and low-power sleep. If an application task runs continuously without yielding, the Idle Task never executes, preventing memory reclamation for deleted tasks and eliminating CPU sleep — increasing power consumption and potentially leaking memory from previously deleted tasks.
- B) The Idle Task serves as the default task when all other tasks are blocked. If an application task runs without yielding, it consumes its full time slice and then the Idle Task runs normally at the next tick boundary.
- C) The Idle Task monitors all other tasks for stack overflow. If an application task never yields, the Idle Task detects this as abnormal behavior and terminates the runaway task automatically.
- D) The Idle Task runs application cleanup code registered with `vApplicationIdleHook()`. A continuously running task prevents cleanup from occurring but has no other operational consequence.
- **Correct Answer:** A) Idle Task handles deletion cleanup and sleep; starvation causes memory leaks and no sleep.
- **Distractor Analysis:**
  - *Why A is correct:* The Idle Task has two critical responsibilities beyond running `vApplicationIdleHook()`: it calls `vPortFree()` to reclaim stack memory for tasks that were deleted using `vTaskDelete()`, and it executes the CPU idle/sleep instruction to reduce power consumption. A task that runs continuously without blocking at priority 1 or higher prevents the Idle Task from ever executing, causing: stack memory from all deleted tasks to accumulate (heap leak), and the CPU to never enter low-power sleep (elevated power consumption). For battery-powered IoT devices this is a critical defect.
  - *Why B is incorrect:* In preemptive FreeRTOS, a task that never blocks and runs at any priority above 0 will consume every available CPU cycle. Since the Idle Task is priority 0, it only runs when no higher-priority task is Ready. A continuous priority-1 task permanently starves the Idle Task.
  - *Why C is incorrect:* The Idle Task does not monitor other tasks for misbehavior or automatically terminate them. Stack overflow detection is a separate FreeRTOS feature (canary values at stack boundaries) that operates independently of the Idle Task.
  - *Why D is incorrect:* While the `vApplicationIdleHook()` consequence is correct, this answer understates the impact by saying "no other operational consequence." The memory leak from deleted task stacks and the loss of CPU sleep are significant operational consequences, not minor oversights.

---

### Question 8

Two FreeRTOS tasks — Task A (priority 4) and Task B (priority 2) — both require the same mutex-protected resource. Task B is currently holding the mutex. Task A tries to acquire it and blocks. A Task C at priority 3 is Ready and starts running. With FreeRTOS mutex priority inheritance enabled, what happens?

- A) Task C runs to completion because it has a higher priority than Task B. After Task C finishes, Task B resumes, releases the mutex, and Task A finally runs.
- B) When Task A blocks on the mutex, the RTOS elevates Task B's priority to 4 (matching Task A). Task B now has higher priority than Task C, preempts Task C, and runs until it releases the mutex. Task A then acquires the mutex and runs.
- C) Task C runs while Task A and Task B both remain blocked. After Task C finishes, Task B resumes at its original priority 2, releases the mutex, and Task A runs.
- D) The RTOS detects that Task A will be blocked by Task B for an indeterminate time and automatically elevates Task A to the maximum priority to ensure it runs as soon as any mutex becomes available.
- **Correct Answer:** B) Task B's priority is elevated to 4, preempting Task C, enabling fast mutex release.
- **Distractor Analysis:**
  - *Why A is incorrect:* Without priority inheritance, this would be correct — and would be a priority inversion. Task A (highest priority) would be blocked by the medium-priority Task C running, even though Task C has no relationship to the contended resource. Priority inheritance was designed specifically to prevent this scenario.
  - *Why B is correct:* When Task A blocks on the mutex held by Task B, FreeRTOS immediately elevates Task B's effective priority to match Task A's priority (4). Now Task B has priority 4, which is higher than Task C's priority 3. Task B preempts Task C and runs until it releases the mutex. Task A then acquires the mutex and runs. After Task A releases the mutex, Task B's priority returns to its original level (2). This ensures that the resource holder can always complete its critical section faster than any lower-priority unrelated task.
  - *Why C is incorrect:* This describes the broken scenario without priority inheritance — the priority inversion problem. Task A is effectively blocked by Task C despite Task C having nothing to do with the resource. Priority inheritance exists precisely to prevent this.
  - *Why D is incorrect:* Priority inheritance elevates the resource *holder* (Task B), not the resource *waiter* (Task A). Elevating the waiter would accomplish nothing because Task A is blocked — it cannot run regardless of its priority until it acquires the mutex.

---

### Question 9

A developer is implementing an interrupt-driven sensor on the ESP32. The interrupt fires when new data is available. The data must be processed by a FreeRTOS task. Which implementation correctly handles this pattern, and what would go wrong with the alternative?

- A) Correct: Process the sensor data entirely inside the ISR. Alternative: Use a semaphore — but semaphore signaling from ISRs is not supported in FreeRTOS and will crash the system.
- B) Correct: Give a binary semaphore from the ISR using `xSemaphoreGiveFromISR()`, then call `portYIELD_FROM_ISR()` if a higher-priority task was unblocked. The processing task blocks on `xSemaphoreTake()`. Alternative: Processing in the ISR itself — ISRs must be kept short; running complex processing inside an ISR blocks all lower-priority interrupts and can cause missed events or system instability.
- C) Correct: Create a dedicated ISR task pinned to core 0 using `xTaskCreatePinnedToCore()`. The ISR itself is empty; the ISR task polls a hardware register every microsecond. Alternative: Semaphores add latency compared to polling.
- D) Correct: Disable the interrupt inside the ISR and re-enable it from the processing task after the data is consumed. Alternative: Leaving the interrupt enabled can cause the ISR to fire again while the processing task is running, corrupting the sensor buffer.
- **Correct Answer:** B) Give semaphore from ISR; process in task. Processing inside ISR is incorrect.
- **Distractor Analysis:**
  - *Why A is incorrect:* `xSemaphoreGiveFromISR()` is fully supported in FreeRTOS and is the idiomatic pattern for interrupt-to-task signaling. ISR-safe variants of all synchronization primitives exist for exactly this purpose.
  - *Why B is correct:* The standard FreeRTOS interrupt-to-task pattern: ISR stays minimal (give semaphore, yield if needed), processing task does all heavy work. `portYIELD_FROM_ISR(pxHigherPriorityTaskWoken)` ensures that if the semaphore give unblocked a high-priority task, the context switch happens immediately on ISR exit rather than waiting for the next tick.
  - *Why C is incorrect:* Polling a hardware register every microsecond from a high-priority task wastes 100% of one core's CPU time in a busy loop. This is the opposite of interrupt-driven design and eliminates the power and responsiveness benefits of hardware interrupts.
  - *Why D is incorrect:* Disabling and re-enabling interrupts is a valid technique for very specific scenarios, but it is not the standard FreeRTOS pattern and introduces significant risk: if the processing task takes a long time, the sensor's interrupt is disabled during that entire period and new data events are missed.

---

### Question 10

An ESP32 application creates three tasks, all at the same priority level (priority 2), and all three tasks perform continuous computation without any blocking calls. After running for 1 minute, a developer notices the serial output shows the three tasks alternating output in a predictable round-robin pattern, each getting equal time. A fourth task is added at priority 2 that publishes data over MQTT — a network operation that blocks on socket send for 50–200 ms. How does the scheduler handle this fourth task differently from the three compute tasks, and what is the net effect on the system?

- A) The fourth task, being at the same priority as the others, gets exactly one tick (1 ms) of CPU time per round-robin cycle. The MQTT blocking call completes within 1 ms or is forcibly interrupted by the scheduler.
- B) When the MQTT task blocks on its socket send, it exits the Running state and enters the Blocked state, voluntarily yielding the CPU. The scheduler runs the remaining three tasks in round-robin while the MQTT task is blocked. When the socket send completes (unblocking the MQTT task), it rejoins the round-robin pool. The net effect is that the three compute tasks run slightly faster while the MQTT task is blocked, and all four tasks share CPU fairly when the MQTT task is active.
- C) Adding a fourth task at the same priority degrades all tasks proportionally — each task now receives 25% of CPU time (down from 33%), so all four tasks slow down equally including the MQTT task.
- D) The MQTT task's blocking behavior triggers priority boosting by the FreeRTOS scheduler — after each blocking call, the task's priority is incremented to ensure it catches up with the compute tasks that ran while it was blocked.
- **Correct Answer:** B) The MQTT task voluntarily yields when blocked; other tasks fill that CPU time; system remains fair and efficient.
- **Distractor Analysis:**
  - *Why A is incorrect:* FreeRTOS does not forcibly interrupt a blocking system call after 1 ms. When a task blocks on a socket operation, it remains in the Blocked state until the OS event (socket send completion) wakes it, regardless of tick boundaries.
  - *Why B is correct:* This describes the key advantage of blocking system calls in an RTOS: a blocking task voluntarily gives up the CPU, allowing other tasks to use the time productively. The three compute tasks benefit from the MQTT task's absence during its blocked period. When the MQTT task unblocks, it re-enters the round-robin pool. This is more efficient than a superloop where the blocking network call would stall the entire application.
  - *Why C is incorrect:* This analysis assumes all four tasks always compete for CPU simultaneously. Because the MQTT task spends significant time in the Blocked state (50–200 ms per send), it is absent from competition during those periods. The compute tasks effectively share 100% of CPU while the MQTT task is blocked.
  - *Why D is incorrect:* FreeRTOS has no built-in "catch-up" priority boosting mechanism for tasks that were blocked. Priority management is entirely the application developer's responsibility. The scheduler does not adjust priorities based on CPU time debt.

---
