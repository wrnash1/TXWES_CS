# Quiz: Module 13 — Asynchronous JavaScript

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
