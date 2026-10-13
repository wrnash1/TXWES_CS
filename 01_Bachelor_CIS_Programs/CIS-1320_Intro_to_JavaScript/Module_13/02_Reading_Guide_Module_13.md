# Reading Guide: Module 13 — Asynchronous JavaScript

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-1320 &BULL; INTRODUCTION TO JAVASCRIPT PROGRAMMING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

JavaScript is single-threaded — it can only execute one piece of code at a time. Yet web applications routinely wait for network responses, timers, and user input without freezing. This works because of the **event loop**: a model that lets JavaScript hand off time-consuming operations to the browser, stay free to respond to other events, and resume when results are ready. Module 13 covers the tools that implement this model: `setTimeout`/`setInterval`, Promises, and `async`/`await`.

---

## 1. The Event Loop and Asynchronous Execution

### The Mental Model

JavaScript execution involves three components:

- **Call stack** — where currently executing code runs, one frame at a time
- **Web APIs** — browser-provided systems that handle timers, network requests, and DOM events outside the JS thread
- **Event queue (task queue)** — a queue of callbacks waiting to run once the call stack is empty

The **event loop** continuously checks: if the call stack is empty, it takes the next item from the queue and runs it.

### Why Async Does Not Mean Parallel

When you call `setTimeout`, `fetch`, or add an event listener, JavaScript registers the operation with the browser's Web API and immediately continues. The Web API handles the waiting. When the operation completes, the callback is placed in the event queue. The event loop runs it when the stack is clear.

```javascript
console.log('1 — synchronous');

setTimeout(() => {
  console.log('3 — from queue (after 0ms delay)');
}, 0);

console.log('2 — synchronous');
// Output: 1, 2, 3
```

Even `setTimeout(..., 0)` runs after all synchronous code in the current execution context finishes, because it goes through the queue.

---

## 2. `setTimeout` and `setInterval`

### `setTimeout`

```javascript
const id = setTimeout(callback, delayMs);
```

Schedules `callback` to run once after `delayMs` milliseconds. Returns a numeric ID.

```javascript
setTimeout(() => {
  console.log('Fires once after 2 seconds');
}, 2000);
```

### `setInterval`

```javascript
const id = setInterval(callback, intervalMs);
```

Schedules `callback` to run repeatedly every `intervalMs` milliseconds.

```javascript
let n = 0;
const id = setInterval(() => {
  n++;
  console.log('Tick', n);
  if (n >= 3) clearInterval(id);
}, 1000);
// Logs: Tick 1, Tick 2, Tick 3 — then stops
```

### Cancellation

```javascript
const timerId    = setTimeout(() => console.log('too late'), 5000);
clearTimeout(timerId);    // cancelled — callback never runs

const intervalId = setInterval(() => console.log('tick'), 1000);
clearInterval(intervalId);   // stops all future callbacks
```

Always store the return value if you may need to cancel.

---

## 3. Promises

A **Promise** is an object representing the eventual result of an asynchronous operation.

### Three States

| State | Meaning | Transitions to |
|---|---|---|
| Pending | Operation in progress | Fulfilled or Rejected |
| Fulfilled | Operation succeeded; has a value | (terminal — does not change) |
| Rejected | Operation failed; has a reason | (terminal — does not change) |

A Promise is **settled** once it reaches fulfilled or rejected. Settled Promises do not change state.

### Creating a Promise

```javascript
const p = new Promise((resolve, reject) => {
  // Perform async work here
  // Call resolve(value) on success
  // Call reject(error) on failure
});
```

The executor function runs synchronously. `resolve` and `reject` are functions provided by the Promise machinery.

```javascript
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

delay(1000).then(() => console.log('1 second passed'));
```

### Consuming a Promise: `.then`, `.catch`, `.finally`

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())   // .then receives fulfilled value
  .then(data => console.log(data))
  .catch(error => console.error(error))  // .catch receives rejection reason
  .finally(() => console.log('done'));   // runs regardless
```

- `.then(onFulfilled)` — runs when fulfilled; receives the resolved value; returns a new Promise
- `.catch(onRejected)` — runs when rejected; receives the error
- `.finally(onSettled)` — runs in both cases; does not receive the value

### Promise Chaining

`.then` returns a new Promise. Whatever `.then`'s callback returns becomes the fulfilled value of that new Promise:

```javascript
Promise.resolve(5)
  .then(n => n * 2)     // 10
  .then(n => n + 1)     // 11
  .then(n => console.log(n));   // 11
```

### `Promise.all`

Runs multiple Promises concurrently. Resolves when all fulfill; rejects immediately if any rejects:

```javascript
Promise.all([
  fetch('/api/users').then(r => r.json()),
  fetch('/api/posts').then(r => r.json())
]).then(([users, posts]) => {
  console.log(users, posts);
}).catch(err => console.error('One failed:', err));
```

Total wait time equals the duration of the slowest request, not the sum.

### Other `Promise` Combinators

| Method | Resolves when | Rejects when |
|---|---|---|
| `Promise.all(arr)` | All fulfill | Any one rejects |
| `Promise.allSettled(arr)` | All settle (any state) | Never rejects |
| `Promise.race(arr)` | First one settles | First one rejects |
| `Promise.any(arr)` | First one fulfills | All reject |

---

## 4. `async` / `await`

`async` and `await` are syntactic sugar over Promises. They let you write async code that looks sequential.

### `async` Functions

Any function declared with `async` returns a Promise:

```javascript
async function greet() {
  return 'Hello';   // equivalent to Promise.resolve('Hello')
}

greet().then(msg => console.log(msg));   // 'Hello'
```

### `await`

`await` pauses execution of the `async` function until the awaited Promise settles. The rest of the program continues running — only the `async` function's execution is paused at that line.

```javascript
async function loadTodo() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const data     = await response.json();
  console.log(data.title);
}
```

`await` can only be used inside an `async` function. Using it at the top level (outside any function) requires a module context — in regular scripts, wrap code in an `async` IIFE if needed:

```javascript
(async () => {
  const data = await fetchSomething();
  console.log(data);
})();
```

### `.then` vs `async/await` — Side by Side

```javascript
// Promise chain
function getUser(id) {
  return fetch(`/api/users/${id}`)
    .then(res => res.json())
    .then(user => {
      console.log(user.name);
      return user;
    })
    .catch(err => console.error(err));
}

// Equivalent async/await
async function getUser(id) {
  try {
    const res  = await fetch(`/api/users/${id}`);
    const user = await res.json();
    console.log(user.name);
    return user;
  } catch (err) {
    console.error(err);
  }
}
```

Both are equivalent. `async/await` is generally preferred for readability when there are multiple sequential async steps.

---

## 5. Error Handling

### With `.catch`

```javascript
fetch('/api/data')
  .then(res => res.json())
  .then(data => process(data))
  .catch(error => console.error('Failed:', error.message));
```

One `.catch` at the end of a chain handles rejections from any preceding `.then`.

### With `try/catch` in `async` Functions

```javascript
async function loadData() {
  try {
    const res  = await fetch('/api/data');
    const data = await res.json();
    return data;
  } catch (error) {
    console.error('Failed:', error.message);
    return null;
  }
}
```

`try/catch` with `async/await` catches both rejected Promises and synchronous `throw` statements inside the block.

### The `response.ok` Check

`fetch` only rejects on network failure (no connection, DNS error). An HTTP error response — 404, 500, 403 — still **resolves** the Promise. You must check `response.ok` manually:

```javascript
async function safeFetch(url) {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`HTTP error: ${res.status}`);
  }
  return res.json();
}
```

`response.ok` is `true` for status codes 200–299. For anything outside that range, it is `false`. This check must be explicit — `fetch` will not throw for you on 4xx/5xx.

---

## 6. `fetch` in Practice

### Basic GET Request

```javascript
async function getTodo(id) {
  const res  = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

### POST Request with JSON Body

```javascript
async function createTodo(title) {
  const res = await fetch('https://jsonplaceholder.typicode.com/todos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, completed: false, userId: 1 })
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

### Response Properties

| Property / Method | Description |
|---|---|
| `response.ok` | `true` if status 200–299 |
| `response.status` | HTTP status code (200, 404, 500…) |
| `response.json()` | Returns a Promise resolving to parsed JSON |
| `response.text()` | Returns a Promise resolving to a string |
| `response.headers` | A Headers object for reading response headers |

---

## 7. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 11: Asynchronous Programming](https://eloquentjavascript.net/11_async.html)**
  The primary OER textbook chapter for this module. Covers callbacks, Promises, `async`/`await`, and the event loop with detailed explanations of why asynchronous code is necessary and how it works under the hood.

- **[MDN Web Docs — Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)**
  Comprehensive guide covering Promise creation, chaining, error handling, `Promise.all`, `Promise.allSettled`, `Promise.race`, and common pitfalls. Includes runnable examples and a comparison with callback-based patterns.

- **[MDN Web Docs — async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)**
  Full reference for `async`/`await` syntax including how async functions implicitly return Promises, how `await` suspends the function, and how errors in async functions become rejections.

- **[MDN Web Docs — Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)**
  Complete guide to the `fetch` API: making GET and POST requests, reading response bodies, checking `response.ok`, handling headers, and working with JSON. Includes the pattern for checking HTTP errors that `fetch` does not throw automatically.

- **[javascript.info — Promises, async/await](https://javascript.info/async)**
  A structured series covering Promises from the ground up, chaining, error handling, `async`/`await`, and Promise combinators (`all`, `allSettled`, `race`, `any`). Each section includes interactive exercises and clear diagrams of Promise state transitions.

---

## 8. JSE Certification Exam Tips

1. **Event loop execution order** — synchronous code always runs first; callbacks in the queue run after. `setTimeout(..., 0)` still runs after all current synchronous code.

2. **Promise states** — pending, fulfilled, rejected. Once settled, a Promise cannot change state. Know all three.

3. **`resolve` fulfills; `reject` rejects** — in the Promise constructor, calling `resolve(value)` fulfills the Promise; calling `reject(reason)` rejects it.

4. **`.then` returns a new Promise** — enabling chaining. The return value of the callback becomes the next `.then`'s value.

5. **`.catch` at the end of a chain** catches any rejection in any preceding `.then`.

6. **`async` functions always return a Promise** — even if the body is synchronous.

7. **`await` pauses the `async` function, not the whole program** — the rest of the JavaScript engine continues executing; only the current `async` function is suspended.

8. **`await` can only be used inside `async` functions** — using it elsewhere is a `SyntaxError`.

9. **`fetch` does not reject on HTTP errors** — only on network failure. Always check `response.ok` or `response.status`.

10. **`Promise.all` rejects immediately if any Promise rejects** — the other Promises are not cancelled, but the `.catch` fires as soon as the first rejection occurs.

---

## 9. Study Checklist

- [ ] Watch the Module 13 video lecture by Professor Nash.
- [ ] Read Chapter 11 (Asynchronous Programming) of [Eloquent JavaScript](https://eloquentjavascript.net/11_async.html).
- [ ] Read [MDN — Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises).
- [ ] Read [MDN — async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).
- [ ] In the Console, run: `console.log(1); setTimeout(() => console.log(2), 0); console.log(3);` — confirm the output order.
- [ ] Create a Promise manually and call `.then` and `.catch` on it — verify that each fires in the right case.
- [ ] Rewrite a `.then` chain as `async/await` — confirm both produce the same result.
- [ ] Fetch `https://jsonplaceholder.typicode.com/todos/1` with `async/await`, check `response.ok`, and render `data.title` to the page.
- [ ] Test the `response.ok` check by fetching a non-existent resource (e.g., `/todos/99999`) and verify the error path fires.
- [ ] Complete the Module 13 Lab.
- [ ] Complete the Module 13 Quiz.
