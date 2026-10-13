# Reading Guide: Module 05 - Asynchronous JavaScript

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3340 &BULL; FULL STACK WEB DEVELOPMENT</text>
    
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


**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers the asynchronous programming model in JavaScript — the foundation of all network communication in web applications. You will learn the event loop and call stack, callbacks, Promises, async/await, the Fetch API, error handling patterns, and CORS. These skills are required for all remaining back-end and full-stack modules.

---

## 1. JavaScript's Single-Threaded Execution Model

JavaScript has one call stack and processes one instruction at a time. When an asynchronous operation (network request, timer, DOM event) is initiated, it is handed off to the browser's Web APIs. When the operation completes, its callback is placed in a queue. The event loop moves callbacks from the queue to the call stack only when the stack is empty.

### Execution Order Example

```javascript
console.log('1 — sync');

setTimeout(() => console.log('4 — setTimeout'), 0);

Promise.resolve().then(() => console.log('3 — Promise microtask'));

console.log('2 — sync');

// Output: 1, 2, 3, 4
```

Why: synchronous code runs first (1, 2). Then the microtask queue (Promise .then) runs (3). Then the macrotask queue (setTimeout) runs (4).

### Queue Priority

| Queue | Contents | Priority |
|---|---|---|
| Call stack | Currently executing synchronous code | Runs first — blocks all queues |
| Microtask queue | Promise `.then`, `catch`, `finally` callbacks | Drains completely before macrotasks |
| Macrotask queue | `setTimeout`, `setInterval`, DOM events, Fetch callbacks | Runs one task per event loop iteration |

---

## 2. Callbacks

Callbacks are functions passed as arguments to async functions, called when the operation completes. They are the original async pattern in JavaScript.

```javascript
// Timer callback
setTimeout(function() {
  console.log('Timer fired after 2 seconds');
}, 2000);

// Simulated async data fetch with callback
function getUser(id, callback) {
  setTimeout(function() {
    const user = { id, name: 'Alice', email: 'alice@example.com' };
    callback(null, user);  // convention: error-first callback (err, data)
  }, 500);
}

getUser(1, function(err, user) {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log('User:', user.name);
});
```

Callback hell — deeply nested callbacks become unreadable:

```javascript
getUser(1, function(err, user) {
  if (err) return handleError(err);
  getOrders(user.id, function(err, orders) {
    if (err) return handleError(err);
    getOrderDetails(orders[0].id, function(err, details) {
      if (err) return handleError(err);
      renderPage(user, orders, details); // three levels deep
    });
  });
});
```

Promises and async/await solve the callback hell problem.

---

## 3. Promises

A Promise represents the eventual completion or failure of an asynchronous operation. It has three states: pending, fulfilled (resolved with a value), and rejected (failed with a reason).

```javascript
// Creating a Promise
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Consuming with .then/.catch/.finally
delay(1000)
  .then(() => {
    console.log('1 second elapsed');
    return 'done';
  })
  .then(result => console.log('Result:', result))
  .catch(error => console.error('Error:', error))
  .finally(() => console.log('Always runs'));

// Chaining — each .then can return a new value or Promise
fetch('/api/users')
  .then(response => response.json())          // returns Promise<data>
  .then(users => users.filter(u => u.active)) // returns Array
  .then(active => renderUsers(active))
  .catch(error => showError(error));
```

### Promise Combinators

```javascript
// Promise.all — all must succeed; one failure rejects all
const [users, products] = await Promise.all([
  fetch('/api/users').then(r => r.json()),
  fetch('/api/products').then(r => r.json())
]);

// Promise.allSettled — waits for all, never rejects; reports each status
const results = await Promise.allSettled([
  fetch('/api/endpoint1').then(r => r.json()),
  fetch('/api/endpoint2').then(r => r.json())
]);
results.forEach(result => {
  if (result.status === 'fulfilled') console.log(result.value);
  if (result.status === 'rejected')  console.error(result.reason);
});

// Promise.race — resolves/rejects with the first settler
const fastest = await Promise.race([fetch('/api/1'), fetch('/api/2')]);

// Promise.any — resolves with first fulfillment; rejects only if all reject
const first = await Promise.any([fetch('/api/mirror1'), fetch('/api/mirror2')]);
```

---

## 4. Async/Await

`async/await` is syntactic sugar over Promises that makes asynchronous code read like synchronous code.

```javascript
// Rules:
// 1. async functions always return a Promise
// 2. await can only be used inside an async function
// 3. await pauses execution until the awaited Promise settles

async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }

  const user = await response.json();
  return user;
}

// Error handling with try/catch
async function loadUser(id) {
  try {
    const user = await fetchUser(id);
    displayUser(user);
  } catch (error) {
    console.error('Failed to load user:', error.message);
    showErrorBanner(error.message);
  }
}

// Parallel fetching — do NOT await sequentially when requests are independent
// SLOW — sequential (each awaits before starting the next):
const users    = await fetchUsers();
const products = await fetchProducts();

// FAST — parallel (both start simultaneously):
const [users, products] = await Promise.all([fetchUsers(), fetchProducts()]);
```

---

## 5. The Fetch API

The Fetch API is the browser's standard HTTP client. It replaces the older `XMLHttpRequest` API.

```javascript
// GET request
async function getItems() {
  const response = await fetch('https://api.example.com/items');
  if (!response.ok) throw new Error(`GET failed: ${response.status}`);
  return response.json();
}

// POST with JSON body
async function createItem(item) {
  const response = await fetch('https://api.example.com/items', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item)
  });
  if (!response.ok) throw new Error(`POST failed: ${response.status}`);
  return response.json();
}

// PUT — full replacement
async function updateItem(id, item) {
  const response = await fetch(`https://api.example.com/items/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item)
  });
  if (!response.ok) throw new Error(`PUT failed: ${response.status}`);
  return response.json();
}

// DELETE
async function deleteItem(id) {
  const response = await fetch(`https://api.example.com/items/${id}`, {
    method: 'DELETE'
  });
  if (!response.ok) throw new Error(`DELETE failed: ${response.status}`);
  // 204 No Content — do not parse body
}
```

### Response Methods

| Method | Returns | Use for |
|---|---|---|
| `response.json()` | Promise resolving to parsed JSON | JSON API responses |
| `response.text()` | Promise resolving to string | HTML, plain text, CSV |
| `response.blob()` | Promise resolving to Blob | Binary data, images |
| `response.ok` | Boolean | `true` if status is 200-299 |
| `response.status` | Number | The HTTP status code |
| `response.statusText` | String | The HTTP status message |
| `response.headers.get('key')` | String or null | Read a response header |

---

## 6. CORS and AWS API Gateway

Cross-Origin Resource Sharing (CORS) is a browser security mechanism. A browser-side `fetch()` call to a different origin is blocked unless the server's response includes an `Access-Control-Allow-Origin` header.

```text
Browser origin: https://myapp.com
API origin:     https://api.myapp.com  <- different subdomain = different origin
```

When the API Gateway endpoint is missing CORS configuration, the request succeeds on the server (you can see it in CloudWatch logs) but the browser blocks the response — this confuses many developers who check the server and see no errors.

To enable CORS in an Express API (Module 07 and Module 08):

```javascript
const cors = require('cors');
app.use(cors({ origin: 'https://myapp.com' }));
```

In API Gateway (Module 14), enable CORS on the resource and ensure your Lambda function returns the headers:

```javascript
return {
  statusCode: 200,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
};
```

---

## 7. Loading States and Error Handling Patterns

```javascript
async function loadPageContent() {
  const loadingEl  = document.querySelector('#loading');
  const errorEl    = document.querySelector('#error');
  const contentEl  = document.querySelector('#content');

  loadingEl.hidden = false;
  errorEl.hidden   = true;
  contentEl.hidden = true;

  try {
    const data = await fetchJSON('/api/content');
    renderContent(data);
    contentEl.hidden = false;
  } catch (error) {
    errorEl.textContent = `Error: ${error.message}. Please try again.`;
    errorEl.hidden      = false;
  } finally {
    loadingEl.hidden = true;
  }
}

async function fetchJSON(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response.json();
}
```

---

## 8. Exam and Interview Tips

1. Even a `setTimeout` with a 0ms delay is asynchronous. The callback always runs after the current synchronous code completes, because it is placed in the callback queue.

2. Promise `.then` callbacks are microtasks. `setTimeout` callbacks are macrotasks. The microtask queue drains completely before any macrotask runs.

3. An `async` function always returns a Promise. If the function body returns a non-Promise value, that value is wrapped in `Promise.resolve(value)` automatically.

4. Missing `await` before a `fetch()` call is the most common bug in async code. Without `await`, the variable holds an unresolved Promise object, not the data.

5. Always check `response.ok` before calling `response.json()`. A 404 or 500 response still resolves the `fetch()` Promise — Fetch only rejects for network failures, not HTTP error statuses.

6. In the DVA-C02 exam: when a question describes a Lambda function that "sometimes returns before the async work completes," the root cause is a Lambda handler that does not properly return a Promise or use async/await. Lambda waits for the returned Promise to settle.

7. `Promise.all` rejects as soon as any Promise rejects. `Promise.allSettled` always fulfills with an array of result objects. Use `allSettled` when you want results from all requests even if some fail.

8. CORS errors are server-side misconfigurations. The browser blocks the response — not the request. The request reaches the server. Check CloudWatch logs to confirm the request arrived, then fix the CORS headers in API Gateway or the Express server.

---

## 9. Study Checklist

- [ ] Explain the event loop, call stack, microtask queue, and macrotask queue
- [ ] Draw the execution order for mixed synchronous, Promise, and setTimeout code
- [ ] Create a Promise manually with `new Promise(resolve, reject)`
- [ ] Chain `.then()`, `.catch()`, and `.finally()` on a Promise
- [ ] Use `Promise.all` and `Promise.allSettled`
- [ ] Write an `async` function with `try/catch` error handling
- [ ] Write `fetch()` calls for GET, POST, PUT, and DELETE
- [ ] Check `response.ok` before parsing the response body
- [ ] Explain the CORS error mechanism and how to fix it in Express and API Gateway
- [ ] Complete Lab 05 and Discussion 05 before the module deadline

---

## 10. Supplemental Resources

The following free, open-access resources go deeper on Module 05 topics:

**1. MDN Web Docs — Using the Fetch API**
[https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
Authoritative reference covering all Fetch options, the `Response` interface, checking `response.ok`, reading response bodies, and handling CORS — directly aligned to the Lab 05 POST and error handling tasks.

**2. MDN Web Docs — Using Promises**
[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
The official guide explaining Promise chaining, error propagation through `.catch()`, `Promise.all`, `Promise.allSettled`, and the relationship between async/await and Promises.

**3. javascript.info — Promises, async/await**
[https://javascript.info/async](https://javascript.info/async)
A free, structured course section covering the event loop, callbacks, Promises, and async/await with interactive exercises. Includes detailed diagrams of the microtask queue vs. macrotask queue covered in Module 05.

**4. web.dev — Cross-Origin Resource Sharing (CORS)**
[https://web.dev/articles/cross-origin-resource-sharing](https://web.dev/articles/cross-origin-resource-sharing)
Google's in-depth article on CORS preflight requests, simple vs. preflighted requests, and the specific headers required — essential background for connecting browser fetch calls to AWS API Gateway endpoints.
