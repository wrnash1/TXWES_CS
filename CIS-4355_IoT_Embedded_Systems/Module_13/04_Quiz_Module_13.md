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

### Question 11

A FreeRTOS task calls `vTaskDelete(NULL)` to delete itself. The task had a stack allocated from the heap. When is the stack memory actually returned to the heap, and what happens if this reclamation never occurs?

- A) The stack memory is returned to the heap immediately when `vTaskDelete(NULL)` executes, before the function returns, because the kernel handles memory cleanup synchronously.
- B) The stack memory is returned to the heap by the Idle Task on the next iteration after `vTaskDelete(NULL)` executes. If the Idle Task is permanently starved (never runs), deleted task stacks accumulate in a pending-deletion list, causing a heap memory leak that grows with each deletion.
- C) The stack memory is never returned automatically — the application must call `vPortFree(taskStackPointer)` explicitly after deleting a task to avoid a memory leak.
- D) FreeRTOS tracks all deleted task stacks and reclaims them in bulk when available heap falls below 20% of initial capacity, triggering a garbage collection pass.
- **Correct Answer:** B) Stack reclamation occurs in the Idle Task; Idle Task starvation causes a growing heap leak.
- **Distractor Analysis:**
  - *Why A is incorrect:* `vTaskDelete()` adds the task to a deletion list and returns. The reason it does not free the stack immediately is that the stack is still in use — the CPU is currently running on it. Only after the context switch away from the deleted task (handled at the next tick or yield) can the stack be safely freed.
  - *Why B is correct:* The Idle Task processes the deletion list on each of its iterations, calling `vPortFree()` on each pending deleted task's stack and TCB. This design means the Idle Task must periodically run for deleted task memory to be reclaimed. An application where a priority-1 or higher task never blocks permanently starves the Idle Task, causing stack memory from every `vTaskDelete()` call to accumulate on the pending-deletion list — a slow but real heap leak.
  - *Why C is incorrect:* Manual `vPortFree()` of a task's stack by the application is not supported and would be unsafe — the kernel manages TCB and stack allocation internally. The automatic reclamation via Idle Task is the correct and supported mechanism.
  - *Why D is incorrect:* FreeRTOS has no garbage collection mechanism and no heap-percentage threshold. It is a deterministic RTOS; deferred operations are triggered by specific events (Idle Task execution), not by heuristic thresholds.

---

### Question 12

An IoT device processes sensor data in a FreeRTOS task and stores the latest reading in a global variable `float g_latestTemp`. The task updates this variable once per second. A second task reads `g_latestTemp` to display it. The ESP32 is configured with `-O2` compiler optimization. Why might the display task read a stale value of `g_latestTemp` even without a race condition on the memory bus, and what is the correct fix?

- A) At `-O2` optimization level, the compiler may cache `g_latestTemp` in a CPU register for the display task, never re-reading it from memory. The fix is to declare `g_latestTemp` as `volatile float g_latestTemp`, forcing a memory read every time the variable is accessed.
- B) At `-O2` optimization level, the display task's reads are delayed by 1 tick to allow the processor pipeline to flush, causing the read to occur one second behind the write. The fix is to add `portMEMORY_BARRIER()` before each read.
- C) At `-O2` optimization level, floating-point operations are rounded to the nearest 32-bit integer boundary, causing the displayed value to differ from the stored value by up to 0.5 units. The fix is to use `double` instead of `float`.
- D) At `-O2` optimization level, the linker places `g_latestTemp` in read-only flash to reduce RAM usage, making the display task's reads return the initial (zero) value. The fix is to use `DRAM_ATTR float g_latestTemp`.
- **Correct Answer:** A) Compiler register caching causes stale reads; `volatile` forces re-read from memory.
- **Distractor Analysis:**
  - *Why A is correct:* The C compiler is permitted to assume that a variable not modified within the current code path does not change between reads. At `-O2`, it may keep `g_latestTemp` in a CPU register, never issuing a load instruction to re-read from RAM. This is correct behavior in a single-threaded context but wrong when another task (or ISR) modifies the variable concurrently. `volatile` tells the compiler that the variable's value can change at any time outside the current execution path, forcing a memory load on every access.
  - *Why B is incorrect:* There is no 1-tick pipeline delay for memory reads at the RTOS level. Pipeline hazards operate at the CPU microarchitecture level and are handled in hardware within nanoseconds, not at tick boundaries.
  - *Why C is incorrect:* `-O2` does not change floating-point precision or rounding behavior. Floating-point arithmetic follows IEEE 754 regardless of optimization level. The type `float` has 32-bit precision on ESP32 Xtensa regardless of optimization.
  - *Why D is incorrect:* The linker places global variables in DRAM by default. `DRAM_ATTR` is an ESP-IDF attribute used to force a variable into DRAM when it would otherwise be placed in IRAM (instruction RAM), not to force RAM placement of a variable that was already in flash. This scenario does not apply to a mutable global float.

---

### Question 13

A developer implements a deadlock by accident: Task A takes Mutex 1 then waits for Mutex 2; Task B takes Mutex 2 then waits for Mutex 1. Both tasks are now permanently blocked. What is the FreeRTOS behavior in this state, and which design pattern prevents this class of deadlock?

- A) FreeRTOS detects the circular wait condition and terminates the lower-priority task, releasing both mutexes and allowing the higher-priority task to proceed.
- B) Both tasks remain permanently blocked; the system does not deadlock because the Idle Task and any other tasks continue executing — only the two deadlocked tasks are frozen. The prevention pattern is consistent lock ordering: always acquire mutexes in the same global sequence across all tasks.
- C) FreeRTOS's priority inheritance mechanism detects that both tasks are waiting for each other and breaks the cycle by elevating the lower-priority task to execute first.
- D) The Task Watchdog Timer automatically detects the deadlock and triggers a system reset after the configured timeout, preventing permanent deadlock.
- **Correct Answer:** B) Only the deadlocked tasks freeze; consistent lock ordering prevents this class of deadlock.
- **Distractor Analysis:**
  - *Why A is incorrect:* FreeRTOS has no deadlock detection. The kernel does not analyze the mutex dependency graph and does not automatically terminate tasks. Task termination is the application's responsibility.
  - *Why B is correct:* A deadlock freezes only the participating tasks; other tasks (including the Idle Task and unrelated application tasks) continue executing normally. The system does not halt — it silently loses the functionality of the deadlocked tasks. The canonical prevention for circular-wait deadlock is consistent lock ordering: if every task that needs both Mutex 1 and Mutex 2 always acquires Mutex 1 first, Task B would have to wait for Task A to release Mutex 1 before acquiring it, breaking the circular dependency.
  - *Why C is incorrect:* Priority inheritance elevates a task that is holding a mutex when a higher-priority task is waiting for the same mutex. It does not detect or resolve circular waits. In a deadlock, both tasks are waiting — neither is making progress to release anything — so inheritance cannot break the cycle.
  - *Why D is incorrect:* The TWDT detects tasks that fail to call `esp_task_wdt_reset()` within the timeout. A deadlocked task that was registered with the TWDT would eventually trigger a reset, but only if the developer explicitly registered the task. TWDT is not a general deadlock detector; it is a liveness monitor for tasks that opt in. Relying on a watchdog reset to recover from deadlock is a last-resort fault recovery strategy, not a prevention technique.

---

### Question 14

A counting semaphore is initialized with a count of 3, representing 3 available DMA channels. Four tasks all attempt `xSemaphoreTake()` simultaneously. What is the outcome for the fourth task, and how would using a mutex instead of a counting semaphore differ for this use case?

- A) The fourth task takes the semaphore anyway — counting semaphores allow temporary over-allocation and track negative counts, deferring actual allocation until a channel becomes available.
- B) The fourth task blocks until another task calls `xSemaphoreGive()`, reducing the demand to 3 or fewer. A mutex would be incorrect for this use case because a mutex only allows one holder at a time — a counting semaphore correctly permits up to 3 simultaneous holders.
- C) The fourth task takes the semaphore and the count drops to -1. FreeRTOS internally allocates an additional DMA channel to satisfy the demand.
- D) All four tasks receive the semaphore simultaneously because FreeRTOS resolves contention on counting semaphores by time-slicing the count among all waiters.
- **Correct Answer:** B) The fourth task blocks; a mutex is wrong here because counting semaphores allow up to N simultaneous holders.
- **Distractor Analysis:**
  - *Why A is incorrect:* FreeRTOS counting semaphores do not permit negative counts or over-allocation. When the count reaches 0, the next `xSemaphoreTake()` call blocks. There is no deferred allocation concept in the kernel primitive.
  - *Why B is correct:* A counting semaphore with initial count N acts as a resource pool with N slots. The first three `xSemaphoreTake()` calls succeed (count goes from 3 to 0). The fourth task blocks because the count is 0. When any of the first three tasks calls `xSemaphoreGive()` (count goes back to 1), the fourth task unblocks and acquires the resource. A mutex is binary (count 0 or 1) — it only permits one holder at a time and would serialize all four tasks even when three DMA channels are independently available, which is unnecessary and reduces throughput.
  - *Why C is incorrect:* Counting semaphores track available resources; they do not allocate actual hardware resources. The semaphore count reflects what the application has declared to be available — it has no mechanism to create new DMA channels.
  - *Why D is incorrect:* FreeRTOS scheduling is priority-based, not count-sharing. If all four tasks are the same priority, the three that succeed do so in the order they called `xSemaphoreTake()` (approximately), and the fourth blocks. There is no count-splitting behavior.

---

### Question 15

An ESP32 task with priority 3 is pinned to APP_CPU (core 1). The Wi-Fi stack task runs on PRO_CPU (core 0) at priority 22. The priority-3 task calls a function in the ESP-IDF network stack that internally acquires a Wi-Fi mutex on PRO_CPU. If the Wi-Fi mutex is held by a Wi-Fi stack task during a channel scan, how long might the priority-3 task wait, and why does pinning to APP_CPU not protect against this delay?

- A) The priority-3 task will wait at most 1 tick (1 ms) because inter-core mutexes always have a 1-tick maximum hold time enforced by the FreeRTOS SMP scheduler.
- B) The priority-3 task may wait for the duration of the Wi-Fi channel scan (up to hundreds of milliseconds) because the Wi-Fi mutex is a cross-core spinlock or semaphore protecting shared radio hardware state. Pinning to APP_CPU only prevents task preemption from PRO_CPU tasks — it does not prevent blocking on cross-core primitives protecting shared state.
- C) The priority-3 task will not wait at all because cross-core mutex operations are asynchronous on the ESP32 — the task proceeds with a copy of the shared state while the Wi-Fi stack completes the scan.
- D) The priority-3 task will trigger a priority inheritance elevation of the Wi-Fi stack task, giving it priority 3, which causes the channel scan to pause since Wi-Fi tasks should be lower priority than application tasks.
- **Correct Answer:** B) The task may wait hundreds of milliseconds; core pinning does not prevent cross-core primitive blocking.
- **Distractor Analysis:**
  - *Why A is incorrect:* There is no enforced 1-tick maximum hold time on any FreeRTOS mutex or spinlock. Hold durations are determined by application behavior. The Wi-Fi stack's channel scan can take 50–500 ms depending on the number of channels and SSID count, and its mutex may be held for most of that duration.
  - *Why B is correct:* The ESP32's FreeRTOS SMP implementation uses spinlocks (`portMUX_TYPE`) for cross-core critical sections and semaphores for longer-held resources. A priority-3 application task that calls into the network stack can block on the Wi-Fi mutex regardless of which core it runs on, because the mutex is protecting shared radio driver state — not core-local data. Pinning to APP_CPU prevents the Wi-Fi task from preempting the application task on core 1, but blocking on a shared mutex is a voluntary wait, independent of core affinity.
  - *Why C is incorrect:* Cross-core mutex operations in ESP-IDF are not asynchronous. They are standard blocking primitives. There is no "copy of shared state" mechanism — shared state in the radio driver is accessed under lock.
  - *Why D is incorrect:* FreeRTOS priority inheritance elevates the holder of a mutex when a higher-priority task is waiting for that same mutex. However, on the ESP32 SMP implementation with `portMUX_TYPE` spinlocks (used in the Wi-Fi driver), priority inheritance is not applied. Additionally, the Wi-Fi task at priority 22 is already higher priority than the application task at priority 3, so inheritance would not elevate it further.

---

### Question 16

What is the minimum stack size consideration when creating a FreeRTOS task that will call `printf()` (or `Serial.printf()` on Arduino-ESP32), and what tool in the ESP-IDF/FreeRTOS API confirms whether the configured stack size was sufficient after the task has run?

- A) `printf()` requires no special stack consideration; it operates in the kernel heap and does not use the task stack. Stack size only matters for local variable allocation.
- B) `printf()` uses significant stack space — typically 512–2048 bytes — for its internal format buffer and floating-point conversion routines. The stack size must include headroom for the deepest `printf()` call chain. `uxTaskGetStackHighWaterMark(taskHandle)` returns the minimum free stack words observed since task creation; a value near zero indicates a stack overflow risk.
- C) `printf()` uses a shared global buffer in the ESP-IDF newlib implementation, so all tasks share the same print buffer and no task-specific stack allocation is needed.
- D) `printf()` stack usage can be measured by calling `xPortGetFreeHeapSize()` before and after the first `printf()` call; the difference is the required stack allocation.
- **Correct Answer:** B) `printf()` uses 512–2048 bytes of stack; `uxTaskGetStackHighWaterMark()` reports minimum free stack headroom.
- **Distractor Analysis:**
  - *Why A is incorrect:* `printf()` uses the task's own stack — not the kernel heap — for its call frame, format buffer, and floating-point conversion state. On the ESP32 with newlib, a single `printf()` with a floating-point format specifier (`%f`) can consume over 1 KB of stack in deep call chains.
  - *Why B is correct:* FreeRTOS stack sizing is one of the most common causes of hard-to-diagnose bugs. The tool is `uxTaskGetStackHighWaterMark(taskHandle)`, which returns the minimum number of stack words that have ever been free in the task's lifetime (measured by checking a watermark canary pattern painted at the end of the stack). A return value of less than 20–50 words indicates the task is close to overflowing. Values near 0 or unexpected crashes often indicate the stack was already overflowed.
  - *Why C is incorrect:* newlib's `printf()` uses re-entrant implementations in ESP-IDF that store per-thread context on the calling task's stack, not in a shared global buffer. A shared global buffer would cause corruption if two tasks called `printf()` simultaneously.
  - *Why D is incorrect:* `xPortGetFreeHeapSize()` returns free heap memory, not task stack space. Task stacks are allocated from the heap at creation time as a fixed block; they are not tracked by the runtime allocator on a per-call basis.

---

### Question 17

A FreeRTOS application has a high-priority Task H (priority 5) and a low-priority Task L (priority 1) sharing a mutex. Task L holds the mutex and then calls `vTaskDelay(pdMS_TO_TICKS(10000))` — a 10-second delay — while still holding the mutex. Task H is waiting for the mutex with `portMAX_DELAY`. What is the consequence, and what coding rule does this scenario violate?

- A) FreeRTOS automatically releases the mutex when a task enters the Blocked state from `vTaskDelay()`, so Task H acquires the mutex immediately and there is no delay.
- B) Task H waits the full 10 seconds because Task L holds the mutex while delayed. Priority inheritance elevates Task L to priority 5 during the wait, but since Task L is in the Blocked state (sleeping), the elevated priority cannot help it run sooner — it still waits the full 10 seconds. This violates the rule that mutex critical sections must be as brief as possible and must not include blocking calls.
- C) The Task Watchdog Timer detects that Task H has been waiting for a mutex for more than 5 seconds and kills Task L, releasing the mutex automatically.
- D) After 1 second of waiting, FreeRTOS times out Task H's mutex acquire and returns `pdFAIL`, allowing Task H to proceed without the mutex.
- **Correct Answer:** B) Task H waits the full 10 seconds; priority inheritance cannot help a sleeping task; holding a mutex across a delay violates critical section discipline.
- **Distractor Analysis:**
  - *Why A is incorrect:* FreeRTOS does not automatically release mutexes when a task blocks. The mutex remains held by Task L throughout its `vTaskDelay()`. If FreeRTOS released mutexes automatically on blocking, it would violate the mutual exclusion guarantee — shared resources would be accessible before the holder had finished its critical section.
  - *Why B is correct:* Priority inheritance works by allowing the mutex holder to preempt lower-priority tasks. However, a task in the Blocked state (sleeping) cannot be preempted or run — it is not in the Ready state. Elevating Task L's priority to 5 has no effect while Task L is blocked for 10 seconds. The mutex will not be released until `vTaskDelay()` returns and Task L explicitly gives it. The rule violated is: never hold a mutex across a blocking call, I/O operation, or delay. Critical sections must be fast and non-blocking.
  - *Why C is incorrect:* The TWDT monitors tasks for liveness failures (not calling `esp_task_wdt_reset()`). It does not monitor or time out mutex wait operations. Task L is alive — it is simply sleeping — so the TWDT would not trigger on it.
  - *Why D is incorrect:* Task H called `xSemaphoreTake(mutex, portMAX_DELAY)`, which means it will wait indefinitely. It will not time out unless the application uses a finite timeout value. `portMAX_DELAY` explicitly means "wait forever."

---

### Question 18

On the ESP32 dual-core FreeRTOS implementation, two tasks each pinned to different cores (Task A on core 0, Task B on core 1) both modify the same global integer `int g_counter` without any synchronization. What is the class of bug this creates, and what is the lightweight synchronization primitive appropriate for a single shared integer counter?

- A) There is no bug — the ESP32 has cache coherence between cores, ensuring that any write to `g_counter` by Task A is immediately visible to Task B.
- B) This creates a data race — both tasks can read-modify-write `g_counter` concurrently, producing lost updates. The appropriate primitive is a `portMUX_TYPE` spinlock (or an atomic operation via `__atomic_fetch_add()`) rather than a full mutex, since the critical section is only a single increment.
- C) There is no bug for increment operations because `++g_counter` compiles to a single instruction on Xtensa LX6 and is therefore inherently atomic.
- D) This creates a stack corruption bug — each core's stack pointer advances independently, causing the two cores to overwrite each other's stack frames when both write to a global variable simultaneously.
- **Correct Answer:** B) Data race producing lost updates; use spinlock or atomic operation for a single-integer critical section.
- **Distractor Analysis:**
  - *Why A is incorrect:* The ESP32's L1 data cache is not automatically coherent between cores for all access patterns. ESP-IDF uses spinlocks and memory barriers explicitly because cache coherence cannot be assumed for all shared data without synchronization. Even with coherent caches, a read-modify-write sequence is not atomic and suffers from the lost-update problem.
  - *Why B is correct:* A read-modify-write sequence (`g_counter++`) on a shared variable without synchronization is the textbook definition of a data race. Both cores may read the same value, independently increment, and both write back the same incremented value — resulting in one increment being lost. For a single integer, `portMUX_TYPE` spinlocks provide low-overhead mutual exclusion, and GCC atomic builtins (`__atomic_fetch_add(&g_counter, 1, __ATOMIC_SEQ_CST)`) provide lock-free atomicity using the Xtensa EXCL instruction sequence.
  - *Why C is incorrect:* `++g_counter` compiles to at least three instructions on any modern CPU: load, increment, store. These three instructions are not atomic as a group. A context switch or cross-core interference can occur between the load and the store.
  - *Why D is incorrect:* A global variable is in the data segment (.bss or .data), not on any task's stack. Concurrent writes to global variables affect the variable's value, not stack memory. Stack corruption arises from stack overflow or incorrect pointer arithmetic, not from global variable contention.

---

### Question 19

A developer wants to transmit a large struct (`typedef struct { float data[256]; uint32_t id; } BigPacket_t;`) through a FreeRTOS queue. The struct is 1028 bytes. The queue is created with `xQueueCreate(10, sizeof(BigPacket_t))`. What is the memory cost of this queue, and what is an alternative design that reduces queue memory usage while preserving thread safety?

- A) The queue allocates 10 × 1028 = 10,280 bytes of heap for the item buffer. An alternative is to allocate items from a memory pool, enqueue only a pointer (`void*`) using a queue of pointer size (4 bytes per slot), and manage pool reclamation explicitly.
- B) The queue allocates 10 bytes of heap because FreeRTOS queues store items as references, not copies. The 1028-byte struct is stored at its original location and the queue holds a pointer to it.
- C) The queue allocates 10,280 bytes but the data is compressed in the queue buffer using zlib at enqueue time, reducing effective memory usage by approximately 70%.
- D) The queue size is limited to the system's tick rate in bytes; a 1028-byte struct cannot be queued and `xQueueCreate()` will return NULL for item sizes above 512 bytes.
- **Correct Answer:** A) 10,280 bytes allocated; use a memory pool with pointer queue to reduce usage.
- **Distractor Analysis:**
  - *Why A is correct:* FreeRTOS queues use copy semantics — the entire item is copied into the queue buffer at `xQueueSend()` time. A queue of length 10 with 1028-byte items requires 10 × 1028 = 10,280 bytes of heap just for the item storage, plus the queue control block overhead (~100 bytes). For the ESP32 with 520 KB of SRAM, this is manageable for small queues, but scales poorly. The alternative is a statically allocated memory pool (array of `BigPacket_t`) plus a mutex or pool semaphore; tasks write into pool slots and enqueue only the pointer, keeping the queue buffer at 10 × 4 = 40 bytes. The receiver is responsible for returning the slot to the pool after use.
  - *Why B is incorrect:* FreeRTOS queues explicitly use value (copy) semantics, not reference semantics. This is a deliberate design choice: pointer semantics require the sender to keep the pointed-to data valid until the receiver processes it, creating implicit lifetime coupling and race conditions. Copy semantics eliminate this problem at the cost of memory.
  - *Why C is incorrect:* FreeRTOS has no built-in compression in its queue implementation. Compression would require CPU time in the critical path of every enqueue and dequeue, which contradicts the deterministic timing requirements of an RTOS.
  - *Why D is incorrect:* There is no queue item size limit tied to the tick rate or a 512-byte cap. `xQueueCreate()` returns NULL only if there is insufficient heap to allocate the queue buffer — not because of item size restrictions in the API.

---

### Question 20

A FreeRTOS application on the ESP32 creates a task with `xTaskCreate()` (no core affinity). The task creates a Wi-Fi connection and then calls `esp_mqtt_client_publish()` in a loop every second. After several hours, the system crashes with a `LoadProhibited` exception from inside the Wi-Fi driver. No watchdog fires, no memory warning appears. What is the most likely root cause, and how should the developer investigate?

- A) The crash is caused by the Wi-Fi driver running out of free heap due to MQTT message buffering. The developer should add `Serial.printf("Free heap: %d\n", esp_get_free_heap_size())` in the loop and monitor for heap exhaustion before the crash.
- B) The `LoadProhibited` exception indicates a NULL or invalid pointer dereference in the Wi-Fi driver. After several hours, this pattern typically indicates a slow heap corruption or use-after-free caused by a task freeing a buffer still referenced by the Wi-Fi driver. The developer should enable heap corruption detection via `CONFIG_HEAP_CORRUPTION_DETECTION=comprehensive` in `sdkconfig` and reproduce the crash.
- C) The crash is caused by the MQTT task running on PRO_CPU and interfering with the Wi-Fi driver's internal interrupt handler, which is pinned to PRO_CPU. The fix is to pin the MQTT task to APP_CPU using `xTaskCreatePinnedToCore()`.
- D) The `LoadProhibited` exception indicates the task's stack has grown into the heap segment. The developer should reduce the task's stack size by half and monitor whether the crash recurs.
- **Correct Answer:** B) Slow heap corruption or use-after-free; investigate with comprehensive heap corruption detection.
- **Distractor Analysis:**
  - *Why A is incorrect:* Heap exhaustion typically manifests as a failed allocation returning NULL followed by a null-pointer dereference shortly thereafter — not as a `LoadProhibited` exception deep inside the Wi-Fi driver after hours of runtime. Heap exhaustion would also typically trigger allocator assertions in debug builds before a crash. Monitoring free heap is a useful diagnostic step but not the primary explanation for this crash pattern.
  - *Why B is correct:* A `LoadProhibited` exception from inside a kernel or driver component after many hours of stable operation is the classic signature of heap corruption: a buffer overwrite or use-after-free that corrupts a pointer stored in a driver structure, which is dereferenced hours later during a routine operation. ESP-IDF's `CONFIG_HEAP_CORRUPTION_DETECTION=comprehensive` fills freed blocks with a pattern and checks it on subsequent allocations, often catching the corruption at the point of write rather than at the point of crash.
  - *Why C is incorrect:* The Wi-Fi driver is designed to be called from any task on any core in ESP-IDF; it uses its own internal locking. Running an MQTT task on PRO_CPU is not inherently incorrect and would not cause `LoadProhibited` exceptions. Core interference with interrupt handlers is prevented by the kernel's interrupt mask mechanism.
  - *Why D is incorrect:* Stack overflow and heap incursion would more typically manifest as stack canary violations (detected by FreeRTOS stack overflow checking), garbled local variables, or return address corruption — not as a pointer dereference inside the Wi-Fi driver structure. Reducing stack size would make stack overflow more likely, not less.
