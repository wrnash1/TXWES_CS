# Quiz: Module 13 — Asynchronous JavaScript

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the output of the following code?

```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
console.log('C');
```

- A) `A`, `B`, `C`
- B) `A`, `C`, `B`
- C) `B`, `A`, `C`
- D) `C`, `A`, `B`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Even though the `setTimeout` delay is 0 milliseconds, the callback is still placed in the event queue and only runs after the current synchronous code finishes. It does not interrupt the execution of `console.log('C')`.
- *Why B is correct:* `'A'` logs synchronously first. `setTimeout` registers its callback with the browser's timer API and immediately continues — it does not wait. `'C'` logs synchronously next. Only when the call stack is empty does the event loop pick up the queued callback and log `'B'`.
- *Why C is incorrect:* `'B'` cannot log first — it is in the event queue and cannot run until all synchronous code on the call stack has completed.
- *Why D is incorrect:* `'C'` is a synchronous statement that runs after `setTimeout` is called (but before the callback fires). `'A'` runs before `'C'`.

---

### Question 2

What are the three states of a Promise, in the correct order of possible transitions?

- A) Starting → Running → Finished
- B) Pending → Resolved → Rejected
- C) Pending → Fulfilled or Rejected (terminal)
- D) Open → Closed → Settled

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* These are not valid Promise state names. JavaScript's Promise specification defines three specific states: pending, fulfilled, and rejected.
- *Why B is incorrect:* `'Resolved'` is not a Promise state — it is sometimes used informally to mean "fulfilled," but the specification states are "pending," "fulfilled," and "rejected." Also, a Promise cannot go from fulfilled to rejected.
- *Why C is correct:* A Promise starts as **pending**. It transitions to **fulfilled** if `resolve` is called (with a value), or to **rejected** if `reject` is called (with a reason). Once fulfilled or rejected, the state is terminal — it never changes again.
- *Why D is incorrect:* These are not Promise state names. "Settled" is sometimes used to describe a Promise that has reached either fulfilled or rejected, but it is not itself a state.

---

### Question 3

What does the `.catch` handler receive as its argument?

```javascript
Promise.reject(new Error('something went wrong'))
  .catch(e => console.log(e.message));
```

- A) The string `'something went wrong'`
- B) The `Error` object passed to `reject`
- C) `undefined`
- D) `null`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.catch` receives the rejection reason — the entire value passed to `reject`. Here that is an `Error` object, not a plain string. `e.message` is `'something went wrong'`, but `e` itself is the `Error` object.
- *Why B is correct:* `Promise.reject(new Error('something went wrong'))` creates a rejected Promise with the `Error` object as its reason. The `.catch` callback receives that reason as its argument — the full `Error` object. Accessing `e.message` extracts the message string from it.
- *Why C is incorrect:* `.catch` always receives the rejection reason if one was provided. `reject` was called with an `Error`, so `e` is that `Error`.
- *Why D is incorrect:* `null` is not the rejection reason here. The reason is the `Error` object.

---

### Question 4

Which statement about `async` functions is correct?

- A) An `async` function runs on a separate thread from the rest of JavaScript
- B) An `async` function always returns a Promise
- C) `await` inside an `async` function pauses the entire JavaScript engine
- D) `async` functions cannot use `try/catch`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* JavaScript is single-threaded. `async` functions do not run on a separate thread — they run on the same thread and use the event loop to pause and resume without blocking.
- *Why B is correct:* Any function declared with `async` always returns a Promise. If the function body returns a plain value (e.g., `return 42`), it is automatically wrapped in `Promise.resolve(42)`. If it throws, the Promise is rejected.
- *Why C is incorrect:* `await` pauses only the **`async` function itself** — not the entire engine. The event loop continues; other callbacks and synchronous code can run while the `async` function is suspended waiting for a Promise to settle.
- *Why D is incorrect:* `try/catch` is the standard error-handling mechanism inside `async` functions. It catches both thrown errors and rejected Promises awaited within the `try` block.

---

### Question 5

A developer fetches data and sees no error in the console, but the response status is 404. Why?

```javascript
async function load() {
  const res = await fetch('/api/missing-resource');
  const data = await res.json();
  console.log(data);
}
```

- A) `fetch` always throws on 404 — the code is unreachable
- B) `fetch` only rejects on network failure; HTTP 404 resolves the Promise
- C) `res.json()` throws automatically for non-200 responses
- D) The 404 is silently ignored by the browser

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `fetch` does not throw or reject for HTTP error status codes. A 404 response is a valid HTTP response — the server responded; it just said "not found." `fetch` rejects only when no network response arrives at all (e.g., DNS failure, no connection).
- *Why B is correct:* `fetch` resolves the Promise as long as the server returns any HTTP response, including 4xx and 5xx errors. The developer must explicitly check `res.ok` (which is `false` for 404) and throw manually if appropriate. Without that check, the code continues past the failed request as if it succeeded.
- *Why C is incorrect:* `res.json()` attempts to parse the response body as JSON. If the 404 response body is empty or not valid JSON, it may throw a parse error — but that is a secondary issue, not the explanation for why the `fetch` Promise resolved.
- *Why D is incorrect:* The 404 is not ignored — it is present in `res.status` and `res.ok`. The developer chose not to check those properties, which is the bug.

---

### Question 6

What is the correct way to check for an HTTP error response after a `fetch` call?

- A) Wrap the `fetch` call in a `try/catch` — it throws for any non-200 status
- B) Check `response.status === 200` explicitly
- C) Check `response.ok` — it is `false` for status codes outside 200–299
- D) `fetch` returns `null` for error responses — check `if (!response)`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `fetch` does not throw for non-200 status codes. `try/catch` only catches network failures (no response at all). An HTTP 404 or 500 still resolves normally and is not caught.
- *Why B is incorrect:* While checking `status === 200` would catch some errors, it is overly strict. Status 201 (Created), 204 (No Content), and other 2xx codes are also successful. `response.ok` handles all 2xx codes correctly.
- *Why C is correct:* `response.ok` is a boolean property that is `true` for HTTP status codes 200–299 and `false` for anything else. It is the standard, idiomatic check for whether a `fetch` succeeded at the HTTP level. After checking it, throw an error manually to propagate the failure to your `catch` block.
- *Why D is incorrect:* `fetch` never returns `null`. It returns a Response object (or rejects the Promise on network failure). Checking `if (!response)` will always be falsy — the response object is always truthy.

---

### Question 7

What does `Promise.all([p1, p2, p3])` do if `p2` rejects?

- A) Waits for `p1` and `p3` to settle, then rejects with all three errors
- B) Ignores the rejection and resolves with the results of `p1` and `p3`
- C) Rejects immediately with `p2`'s reason; `p1` and `p3` continue but their results are ignored
- D) Throws a `SyntaxError` because one of the Promises failed

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.all` does not wait for all Promises to settle before rejecting. It rejects as soon as the first rejection occurs. Use `Promise.allSettled` to wait for all to settle regardless of outcome.
- *Why B is incorrect:* `Promise.all` fails fast — any rejection causes the whole thing to reject. It does not produce partial results.
- *Why C is correct:* `Promise.all` rejects immediately when any Promise in the array rejects. The rejection reason is `p2`'s error. `p1` and `p3` continue executing (they cannot be cancelled), but their results are discarded. The `.catch` or `try/catch` receives `p2`'s reason.
- *Why D is incorrect:* No `SyntaxError` is thrown. Rejections in Promises are handled through the rejection path (`.catch`), not as JavaScript syntax errors.

---

### Question 8

Where can `await` be used?

- A) Anywhere in a JavaScript file
- B) Only inside functions declared with `async`
- C) Only inside `.then` callbacks
- D) Only at the top level of a module, never inside functions

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `await` used outside an `async` function is a `SyntaxError` in classic scripts. It cannot be used in regular synchronous functions or at the top level of non-module scripts.
- *Why B is correct:* `await` is only valid inside functions declared with the `async` keyword. Inside an `async` function, `await` pauses that function's execution until the awaited Promise settles. Using `await` in a regular function or outside any function causes a `SyntaxError`.
- *Why C is incorrect:* `.then` callbacks are regular functions (not `async`). You cannot use `await` inside a plain `.then` callback. You would need to declare that callback as `async` — e.g., `.then(async res => { const data = await res.json(); })`.
- *Why D is incorrect:* This is partially true for ES modules (top-level `await` is valid in modules), but the correct general rule for this course is B — `await` is only valid inside `async` functions.

---

### Question 9

What does the following `async` function return?

```javascript
async function compute() {
  return 42;
}

const result = compute();
```

- A) The number `42`
- B) `undefined`
- C) A Promise that resolves to `42`
- D) A Promise that rejects with `42`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `async` functions never return plain values directly. The return value is always wrapped in a Promise, even when the function body returns a primitive.
- *Why B is incorrect:* `compute()` does return a value — it returns a Promise. The Promise resolves to `42`, not `undefined`.
- *Why C is correct:* Any function declared with `async` automatically wraps its return value in `Promise.resolve(...)`. `return 42` inside an `async` function is equivalent to `return Promise.resolve(42)`. `result` is a Promise; calling `result.then(v => console.log(v))` logs `42`.
- *Why D is incorrect:* `return 42` is not a rejection. Rejection occurs when `reject` is called on a new Promise or when `throw` is used inside an `async` function.

---

### Question 10

A developer needs to fetch data from three independent API endpoints and use all three results together. Which approach is most efficient?

- A) Use three sequential `await` calls — wait for each before starting the next
- B) Use `Promise.all` with all three `fetch` calls — start them concurrently
- C) Use `setTimeout` to stagger the three requests
- D) Use `setInterval` to retry each request until it succeeds

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sequential `await` calls mean: start request 1, wait for it to finish, start request 2, wait, start request 3, wait. Total time = sum of all three response times. When the requests are independent, this wastes time.
- *Why B is correct:* `Promise.all([fetch(url1), fetch(url2), fetch(url3)])` starts all three requests at the same time. They run concurrently (the browser sends all three requests simultaneously). Total wait time equals the duration of the slowest single request, not their sum. This is the correct pattern for independent parallel operations.
- *Why C is incorrect:* Staggering requests with `setTimeout` adds artificial delay and still does not make the requests overlap in a coordinated way. `Promise.all` is the right tool.
- *Why D is incorrect:* `setInterval` is for repeating operations, not for making a single efficient parallel request. Retry logic is a separate concern from parallel loading.

---

### Question 11

What is the output of the following code?

```javascript
console.log('start');

Promise.resolve('done').then(v => console.log(v));

console.log('end');
```

- A) `start`, `done`, `end`
- B) `start`, `end`, `done`
- C) `done`, `start`, `end`
- D) `start`, `end`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Promise callbacks (microtasks) do not interrupt synchronous execution. `console.log('end')` is synchronous and runs before any Promise `.then` callback executes.
- *Why B is correct:* `'start'` logs synchronously first. `Promise.resolve('done').then(...)` schedules the `.then` callback as a microtask — it is deferred until after all current synchronous code finishes. `'end'` logs synchronously. Then the microtask queue runs and logs `'done'`.
- *Why C is incorrect:* `'done'` is deferred as a microtask. It cannot log before the synchronous `console.log('start')`.
- *Why D is incorrect:* `'done'` does eventually log — after the synchronous code completes, the microtask queue drains and the `.then` callback runs.

---

### Question 12

What does `Promise.allSettled([p1, p2, p3])` return when `p2` rejects?

- A) A rejected Promise with `p2`'s error
- B) A fulfilled Promise with an array of result objects for all three, indicating each outcome
- C) A fulfilled Promise with the results of `p1` and `p3` only
- D) It throws a `TypeError` because mixed fulfilled/rejected arrays are not allowed

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.allSettled` never rejects. Unlike `Promise.all`, it waits for all Promises to settle regardless of outcome and always fulfills.
- *Why B is correct:* `Promise.allSettled` waits for all Promises to complete, then fulfills with an array of objects — one per Promise — each with `{ status: 'fulfilled', value }` or `{ status: 'rejected', reason }`. This allows you to inspect every outcome individually.
- *Why C is incorrect:* `Promise.allSettled` includes a result object for every Promise, including the rejected one. It does not filter out rejections.
- *Why D is incorrect:* `Promise.allSettled` is specifically designed for mixed outcomes. No error is thrown. It is the go-to method when you need results from all operations regardless of individual failures.

---

### Question 13

What does `await` do to the calling context when it encounters an unsettled Promise?

- A) It blocks the entire JavaScript thread until the Promise resolves
- B) It pauses only the `async` function — the event loop continues processing other tasks
- C) It converts the Promise to a synchronous value immediately
- D) It throws a `SyntaxError` if the Promise is still pending

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* JavaScript is single-threaded but non-blocking. `await` does not freeze the thread. The async function is suspended, but other event handlers and microtasks can run while it waits.
- *Why B is correct:* `await` suspends execution of the `async` function at that line and yields control back to the event loop. The event loop continues running other queued callbacks and microtasks until the awaited Promise settles, then resumes the `async` function with the resolved value.
- *Why C is incorrect:* `await` cannot convert an asynchronous operation to a synchronous value — it merely provides syntax that reads that way. The underlying mechanism is still asynchronous.
- *Why D is incorrect:* A pending Promise is the normal case for `await`. `await` is designed to wait for pending Promises — that is its entire purpose. No error is thrown.

---

### Question 14

What does the following code log?

```javascript
async function run() {
  return 'hello';
}

const result = run();
console.log(typeof result);
```

- A) `'string'`
- B) `'undefined'`
- C) `'object'`
- D) `'promise'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `run()` does not return the string `'hello'` directly. The `async` keyword wraps the return value in a Promise. `typeof Promise` is `'object'`, not `'string'`.
- *Why B is incorrect:* `result` is a Promise object — it is not `undefined`. `typeof undefined` is `'undefined'`, but a Promise instance is a defined value.
- *Why C is correct:* An `async` function always returns a Promise. `typeof` a Promise instance is `'object'` (Promises are objects). The resolved value is `'hello'`, but `result` itself is the Promise wrapper.
- *Why D is incorrect:* `typeof` does not return `'promise'`. The possible values of `typeof` are `'undefined'`, `'boolean'`, `'number'`, `'bigint'`, `'string'`, `'symbol'`, `'function'`, and `'object'`. There is no `'promise'` type.

---

### Question 15

A developer writes an `async` function without a `try/catch`. Inside, `await fetch(url)` throws due to a network error. What happens?

- A) The error is silently ignored
- B) The program crashes with an uncaught exception
- C) The `async` function returns a rejected Promise with the error
- D) The `async` function returns `undefined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Errors thrown inside `async` functions are not silently discarded. They become rejections in the returned Promise.
- *Why B is incorrect:* The error does not immediately crash the program. It produces a rejected Promise. If the caller does not handle the rejected Promise (no `.catch` and no `try/catch` at the call site), modern JavaScript environments will emit an `UnhandledPromiseRejectionWarning` — but the function itself just returns a rejected Promise.
- *Why C is correct:* Any uncaught `throw` (including a rejected `await`) inside an `async` function causes the function's returned Promise to reject with the thrown value. The caller can handle it with `.catch()` or by `await`-ing inside a `try/catch`.
- *Why D is incorrect:* The function does not return `undefined` — it returns a rejected Promise. `undefined` would only be the resolved value if the function returned nothing and succeeded.

---

### Question 16

Which method waits for the first Promise to fulfill (ignoring rejections until all have rejected)?

- A) `Promise.all`
- B) `Promise.race`
- C) `Promise.allSettled`
- D) `Promise.any`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.all` resolves when ALL Promises fulfill and rejects as soon as any one rejects. It does not ignore individual rejections.
- *Why B is incorrect:* `Promise.race` settles with the first Promise to settle — fulfilled OR rejected. If the first to settle is a rejection, `race` rejects immediately.
- *Why C is incorrect:* `Promise.allSettled` waits for all Promises to settle and never rejects. It fulfills with all outcomes, not just the first fulfillment.
- *Why D is correct:* `Promise.any` fulfills as soon as any one Promise fulfills. If some Promises reject, they are ignored as long as at least one fulfills. It only rejects if every Promise in the array rejects (with an `AggregateError`).

---

### Question 17

What is the purpose of `clearInterval(id)` in the following code?

```javascript
let count = 0;
const id = setInterval(() => {
  count++;
  if (count >= 5) clearInterval(id);
}, 1000);
```

- A) It pauses the interval temporarily
- B) It cancels all pending timers in the program
- C) It stops the specific interval from firing additional callbacks
- D) It resets `count` to zero

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `clearInterval` permanently cancels the interval — there is no way to resume it. If you need to pause and resume, you would need to cancel it and create a new `setInterval`.
- *Why B is incorrect:* `clearInterval(id)` only cancels the specific interval identified by `id`. Other intervals and timeouts are unaffected.
- *Why C is correct:* `clearInterval(id)` cancels the interval timer identified by `id`. After this call, no more callbacks are scheduled. The specific condition here cancels the interval after 5 ticks.
- *Why D is incorrect:* `clearInterval` has no effect on variables. `count` retains its current value — `5` — after the interval is cancelled.

---

### Question 18

What is wrong with the following code?

```javascript
function loadData() {
  const data = await fetch('/api/data').then(r => r.json());
  return data;
}
```

- A) `fetch` cannot be used with `.then` and `await` simultaneously
- B) `await` can only be used inside a function declared with the `async` keyword
- C) `.then` is not a valid method on a fetch response
- D) `return data` will return `undefined` because `await` is not a valid keyword here

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Mixing `await` with `.then` is valid inside an `async` function — though redundant. The issue here is not the combination but the missing `async` keyword.
- *Why B is correct:* `await` is only valid inside functions declared with `async`. Using `await` inside a regular function declaration causes a `SyntaxError`. The fix is to add `async` before `function loadData()`.
- *Why C is incorrect:* `.then` is valid on a Promise, and `fetch` returns a Promise. `fetch(...).then(r => r.json())` is perfectly valid syntax.
- *Why D is incorrect:* The actual error is a `SyntaxError` at parse time — the code never executes. `data` would not be `undefined`; the script would fail to run at all.

---

### Question 19

After calling `clearTimeout(timerId)`, what happens if the callback's delay had not yet expired?

- A) The callback fires once immediately before being cancelled
- B) The callback is scheduled to fire at the next available opportunity
- C) The callback never fires — the timer is permanently cancelled
- D) `clearTimeout` only works if called before `setTimeout`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `clearTimeout` does not trigger an early firing. The callback is simply discarded — it never runs.
- *Why B is incorrect:* `clearTimeout` permanently cancels the timer. There is no rescheduling or delayed execution. The callback is dropped entirely.
- *Why C is correct:* `clearTimeout(timerId)` cancels the pending timer. If the delay has not yet expired, the callback will never be called. If the delay has already expired and the callback is already in the queue, `clearTimeout` may or may not prevent it from running depending on whether the event loop has already dequeued it — but typically, calling `clearTimeout` before the callback runs is sufficient to cancel it.
- *Why D is incorrect:* `clearTimeout` is designed to be called after `setTimeout` and before the callback fires. That is its normal usage.

---

### Question 20

A developer writes the following code and notices the requests fire one after the other, not simultaneously:

```javascript
async function loadAll() {
  const u = await fetch('/api/user').then(r => r.json());
  const p = await fetch('/api/posts').then(r => r.json());
  const c = await fetch('/api/comments').then(r => r.json());
  return { u, p, c };
}
```

Which refactoring makes all three requests run concurrently?

- A) Use `setTimeout` to start each request at the same time
- B) Move the `await` keywords outside the `async` function
- C) Use `Promise.all` to start all three `fetch` calls before awaiting any of them
- D) Use `setInterval` to repeat the requests until all three respond

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `setTimeout` staggers callbacks by time but does not guarantee concurrent execution and adds unnecessary complexity. `Promise.all` is the correct tool.
- *Why B is incorrect:* `await` cannot be used outside `async` functions. This would cause a `SyntaxError`.
- *Why C is correct:* The sequential version awaits each request before starting the next. The fix is: `const [u, p, c] = await Promise.all([fetch('/api/user').then(r => r.json()), fetch('/api/posts').then(r => r.json()), fetch('/api/comments').then(r => r.json())]);` — all three `fetch` calls start simultaneously, and `Promise.all` waits for all three to complete.
- *Why D is incorrect:* `setInterval` repeats operations on a timer. It is not a mechanism for concurrent parallel requests.
