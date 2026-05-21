# Quiz: Module 05 - Asynchronous JavaScript
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
What state does a JavaScript Promise enter once it has completed successfully?
*   A) Pending
*   B) Fulfilled
*   C) Rejected
*   D) Resolved
*   **Correct Answer:** B) A Promise transitions from Pending to **Fulfilled** when its asynchronous operation completes successfully, providing the resolved value to `.then()` handlers.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Pending is the initial state of a Promise while the operation is still in progress — not a completion state.
    *   *Why B is correct:* Fulfilled is the specific terminal state for a successfully completed Promise — it exposes the resolved value.
    *   *Why C is incorrect:* Rejected is the terminal state for a failed Promise — it exposes the error reason to `.catch()` handlers.
    *   *Why D is incorrect:* "Resolved" is an informal/general term for a Promise that has settled (either fulfilled or rejected), but it is not one of the three formal Promise states defined in the specification.

---

**Question 2**
Which of the following is the most accurate definition of the **call stack** in JavaScript?
*   A) A browser security model that prevents scripts from one origin from making network requests to a different origin without explicit server permission.
*   B) The LIFO (Last In, First Out) data structure used by the JavaScript engine to track function execution contexts — each function call adds a frame, and each return removes one.
*   C) The queue where resolved Promise callbacks wait before the event loop moves them onto the call stack for execution.
*   D) A deployment pattern where two identical production environments alternate receiving live traffic to enable zero-downtime releases.
*   **Correct Answer:** B) The LIFO (Last In, First Out) data structure used by the JavaScript engine to track function execution contexts — each function call adds a frame, and each return removes one.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes the Same-Origin Policy / CORS model — not the call stack.
    *   *Why B is correct:* The call stack is the execution context tracker — JavaScript's single thread runs exactly what is on top of this stack.
    *   *Why C is incorrect:* This describes the microtask queue (or callback queue), not the call stack.
    *   *Why D is incorrect:* This describes a blue/green deployment strategy — a DevOps concept unrelated to JavaScript runtime.

---

**Question 3**
A developer writes the following code but the console logs print in the wrong order. What is the root cause?

```js
console.log('A');
setTimeout(() => console.log('B'), 0);
console.log('C');
```

*   A) `setTimeout` with `0ms` delay executes synchronously before the next `console.log`.
*   B) `setTimeout` callbacks are placed in the callback queue and only run after the call stack is fully empty — even a 0ms delay defers execution past synchronous code.
*   C) `console.log` calls are asynchronous and execute in an unpredictable order.
*   D) The JavaScript engine processes the last statement first (LIFO ordering) — `'C'` logs before `'A'`.
*   **Correct Answer:** B) `setTimeout` callbacks are placed in the callback queue and only run after the call stack is fully empty — even a 0ms delay defers execution past synchronous code.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A `0ms` delay does not mean synchronous execution — it means "run as soon as the call stack is empty," which is always after synchronous code completes.
    *   *Why B is correct:* The event loop only moves the setTimeout callback from the queue to the stack after all synchronous statements finish, producing the output: A → C → B.
    *   *Why C is incorrect:* `console.log` is a synchronous call — it executes immediately in order.
    *   *Why D is incorrect:* The call stack is LIFO for function frames within a call, but sequential statements execute top-to-bottom, not in reverse.

---

**Question 4**
An async function fetches data from an API but silently returns `undefined` instead of the expected data. What is the most likely cause?
*   A) The `async` keyword was omitted from the function declaration.
*   B) The developer forgot to use `await` before the `fetch()` call — the function returned before the Promise resolved, so the data was never captured.
*   C) The fetch API is not available inside async functions — `XMLHttpRequest` must be used instead.
*   D) The `try`/`catch` block automatically returns `undefined` on success when no explicit `return` statement is present.
*   **Correct Answer:** B) The developer forgot to use `await` before the `fetch()` call — the function returned before the Promise resolved, so the data was never captured.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If the `async` keyword were omitted, using `await` inside would throw a syntax error — not silently return `undefined`.
    *   *Why B is correct:* Without `await`, the `fetch()` call returns a Promise object immediately; the variable assigned to it holds an unresolved Promise, not the data.
    *   *Why C is incorrect:* The Fetch API works perfectly inside async functions — in fact, async/await is the recommended way to consume `fetch()`.
    *   *Why D is incorrect:* A `try`/`catch` block does not change the return value behavior — if there is no error, the `catch` block is skipped entirely.

---

**Question 5**
When calling an AWS API Gateway endpoint from a browser front-end using `fetch()`, the request succeeds on the server but the browser blocks the response. What is the most likely cause and fix?
*   A) The `fetch()` call used `async/await` instead of `.then()` — switching to `.then()` will resolve the block.
*   B) The API Gateway endpoint is missing CORS headers (`Access-Control-Allow-Origin`) in its response — the browser's Same-Origin Policy blocks the response until the server explicitly permits the cross-origin request.
*   C) The AWS Lambda function behind the API must be written in Node.js; Python Lambda responses are automatically blocked by browsers.
*   D) The browser blocks all HTTPS API responses unless the front-end application is also served from HTTPS — switching both to HTTP will fix the issue.
*   **Correct Answer:** B) The API Gateway endpoint is missing CORS headers (`Access-Control-Allow-Origin`) in its response — the browser's Same-Origin Policy blocks the response until the server explicitly permits the cross-origin request.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `async/await` and `.then()` are equivalent — the choice of syntax has no effect on CORS enforcement.
    *   *Why B is correct:* Browsers enforce the Same-Origin Policy on responses — API Gateway must include `Access-Control-Allow-Origin: *` (or a specific origin) in its response headers, configured under the API Gateway CORS settings.
    *   *Why C is incorrect:* Lambda runtime (Node.js vs. Python) does not affect CORS — the response headers are what matter, regardless of the runtime language.
    *   *Why D is incorrect:* Mixing HTTP and HTTPS does cause mixed-content blocking, but this scenario describes a CORS block (successful server response, browser-side rejection) — not a protocol mismatch.
