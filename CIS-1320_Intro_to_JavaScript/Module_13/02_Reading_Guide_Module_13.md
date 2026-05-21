# Reading Guide: Module 13 - Asynchronous JavaScript
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 13 - Asynchronous JavaScript**! This week you will learn how JavaScript handles tasks that take time — timers, network requests, and I/O — without blocking the rest of the program. Understanding the event loop, callback queue, and timer functions is foundational for every more advanced async topic (Promises, async/await) covered in the following modules.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Synchronous block**: Code that executes sequentially, line by line, where each statement completes before the next begins. Long-running synchronous operations (such as a CPU-intensive loop) block the entire thread and freeze the browser's UI until they finish.
*   **Callback queue**: A data structure (also called the "task queue" or "message queue") that holds callback functions waiting to be executed after their asynchronous trigger has completed (e.g., a timer expiring or a network request finishing). The event loop moves items from this queue to the call stack only when the stack is empty.
*   **Event loop**: The runtime mechanism that continuously monitors the call stack and the callback queue. When the call stack is empty, the event loop takes the next pending callback from the queue and pushes it onto the stack for execution. This is what enables JavaScript's non-blocking asynchronous model.
*   **setTimeout**: A browser/Node.js function that schedules a callback to run after a specified delay in milliseconds: `setTimeout(fn, delay)`. The callback is placed in the callback queue after the delay; it runs only when the call stack is empty, so the actual delay may be longer than specified.
*   **setInterval**: A function that schedules a callback to run repeatedly at a fixed interval in milliseconds: `setInterval(fn, interval)`. It returns a numeric ID that can be passed to `clearInterval(id)` to stop it. Used for clocks, animations, and polling.
*   **Stack execution**: The call stack is a LIFO (last-in, first-out) data structure that tracks the currently executing functions. When a function is invoked, a frame is pushed; when it returns, the frame is popped. If the stack is not empty, the event loop waits before pushing new tasks.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests execution order with timers. Know that `setTimeout(fn, 0)` does NOT run immediately — it queues `fn` in the callback queue, so synchronous code after the `setTimeout` call runs first. Classic question: what logs first in code that has both synchronous statements and a `setTimeout` with a 0ms delay?
*   **Scenario Trap:** A common trap places a `setTimeout` inside a loop and asks what happens. Because `var` is function-scoped, all timeouts share the same `i` variable and log the same final value. Using `let` (block-scoped) or a closure fixes the issue — this is a common JSE interview scenario.
*   **Study Resource:** [javascript.info – Event loop: microtasks and macrotasks](https://javascript.info/event-loop) is an excellent visual explanation of how the call stack, callback queue, and event loop interact. Read the first two sections (the "Event loop" concept and the "Use case 1" example) before the lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 11 – Asynchronous Programming** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). The early sections on callbacks and the event loop directly match the JSE exam content for this module.
*   **Required Video:** Watch the video lecture on **Asynchronous JavaScript** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on the event loop, setTimeout, setInterval, and asynchronous execution order segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a delayed alert using setTimeout**: Write `setTimeout(() => console.log("3 seconds passed"), 3000)` and confirm the log appears 3 seconds after page load.
*   **Implement a digital clock using setInterval**: Use `setInterval` to call a function every 1000ms that reads `new Date().toLocaleTimeString()` and updates a `<p>` element's text.
*   **Demonstrate non-blocking execution order in console logs**: Write `console.log("A")`, then `setTimeout(() => console.log("B"), 0)`, then `console.log("C")`; observe that the output is A → C → B.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 11 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the asynchronous execution and timer segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
