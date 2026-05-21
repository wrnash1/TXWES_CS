# Quiz: Module 13 - Asynchronous JavaScript
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
What is the purpose of the Event Loop in the JavaScript runtime environment?
*   A) To compile JavaScript source code into machine code
*   B) To monitor the call stack and callback queue, pushing queued tasks when the stack is empty
*   C) To handle garbage collection and memory allocation
*   D) To execute SQL queries directly on the browser database
*   **Correct Answer:** B) The event loop continuously checks if the execution call stack is empty; if it is, it pulls tasks from the callback queue to run.
*   **Distractor Analysis:**
    *   *Why correct:* The event loop continuously checks if the execution call stack is empty; if it is, it pulls tasks from the callback queue to run.
    *   The other options represent compiler, memory manager, or database functions.

---

**Question 2**
Which of the following most accurately describes `setInterval` in JavaScript?
*   A) A function that pauses JavaScript execution for a specified number of milliseconds before continuing
*   B) A function that schedules a callback to execute repeatedly at a fixed interval (in ms) until `clearInterval` is called
*   C) A method on the `Date` object that returns the time elapsed since a previous timestamp
*   D) A property of the `window` object that stores the current time interval of the browser's render cycle
*   **Correct Answer:** B) A function that schedules a callback to execute repeatedly at a fixed interval (in ms) until `clearInterval` is called.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* JavaScript has no synchronous `sleep`-style pause; `setInterval` is asynchronous and does not block execution.
    *   *Why B is correct:* `setInterval(fn, ms)` places `fn` in the callback queue after every `ms` milliseconds; `clearInterval(id)` stops it.
    *   *Why C is incorrect:* Elapsed time is computed with `Date.now()` or `performance.now()`, not with `setInterval`.
    *   *Why D is incorrect:* `setInterval` is a function for scheduling callbacks, not a property related to the browser's rendering cycle.

---

**Question 3**
What will be the order of output for the following code?
```javascript
console.log("1");
setTimeout(() => console.log("2"), 0);
console.log("3");
```
*   A) `1`, `2`, `3`
*   B) `2`, `1`, `3`
*   C) `1`, `3`, `2`
*   D) The output order is undefined and varies by browser
*   **Correct Answer:** C) `1`, `3`, `2`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Even with a 0ms delay, the setTimeout callback is placed in the callback queue and does not run until the synchronous code finishes.
    *   *Why B is incorrect:* The setTimeout callback never runs before synchronous code; `2` will not appear first.
    *   *Why C is correct:* The two synchronous `console.log` calls run first (outputting `1` then `3`); only after the call stack is empty does the event loop move the setTimeout callback to the stack (outputting `2`).
    *   *Why D is incorrect:* The order is deterministic — synchronous code always runs before any timer callbacks, even with a 0ms delay.

---

**Question 4**
While working on **Asynchronous JavaScript**, a developer uses the following code in a loop:
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
```
What is logged?
*   A) `0`, `1`, `2` (each timeout logs the value of `i` at the time it was set)
*   B) `3`, `3`, `3` (all timeouts share the same `var i` which has become 3 by the time they run)
*   C) `undefined`, `undefined`, `undefined` (timer callbacks cannot access outer variables)
*   D) A `ReferenceError` because `i` is out of scope inside the arrow function
*   **Correct Answer:** B) `3`, `3`, `3` (all timeouts share the same `var i` which has become 3 by the time they run).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If `let` were used, each iteration would capture its own block-scoped `i`; `var` creates a single function-scoped variable shared by all callbacks.
    *   *Why B is correct:* `var i` is hoisted to the function/global scope; by the time all three timeouts fire (after the loop completes), `i` has already been incremented to `3`.
    *   *Why C is incorrect:* Arrow functions do capture outer variables via closure; the problem is they all close over the same `var i`.
    *   *Why D is incorrect:* `i` is accessible (it is `var`-scoped and exists throughout the function/global scope); no `ReferenceError` occurs.

---

**Question 5**
What is the difference between `setTimeout` and `setInterval`?
*   A) `setTimeout` runs a callback every N milliseconds; `setInterval` runs it only once after N milliseconds
*   B) `setTimeout` schedules a callback to run once after a delay; `setInterval` schedules a callback to run repeatedly at a fixed interval
*   C) `setTimeout` is synchronous (blocks the thread); `setInterval` is asynchronous (non-blocking)
*   D) `setTimeout` is available only in Node.js; `setInterval` is available only in browsers
*   **Correct Answer:** B) `setTimeout` schedules a callback to run once after a delay; `setInterval` schedules a callback to run repeatedly at a fixed interval.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The descriptions are reversed.
    *   *Why B is correct:* `setTimeout` fires its callback exactly once; `setInterval` fires its callback repeatedly until `clearInterval` is called.
    *   *Why C is incorrect:* Both `setTimeout` and `setInterval` are asynchronous and non-blocking; neither pauses the execution thread.
    *   *Why D is incorrect:* Both functions are available in browsers and Node.js (Node.js added them to its global scope for compatibility).
