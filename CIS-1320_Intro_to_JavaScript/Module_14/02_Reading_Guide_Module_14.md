# Reading Guide: Module 14 — Promises and Async/Await: Patterns in Practice

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Module 13 established the foundations: the event loop, Promise states, and `async/await` syntax. Module 14 applies those foundations to practical patterns: choosing between sequential and parallel execution, using all four Promise combinators, serializing data with JSON, cancelling fetch requests with `AbortController`, and structuring error handling in multi-step async workflows. These patterns appear in every production JavaScript application.

---

## 1. Sequential vs Parallel Async Execution

The most common performance mistake with `async/await` is using sequential `await` for operations that are actually independent.

### Sequential — When You Must Wait for Each Step

```javascript
async function getUserAndPosts(userId) {
  const user  = await fetchUser(userId);         // step 1 must complete
  const posts = await fetchPosts(user.id);       // step 2 needs user.id
  return { user, posts };
}
```

Total time = `fetchUser` duration + `fetchPosts` duration. Correct here because step 2 depends on step 1.

### Parallel — When Operations Are Independent

```javascript
async function getDashboardData() {
  const [user, stats, notifications] = await Promise.all([
    fetchUser(1),
    fetchStats(1),
    fetchNotifications(1)
  ]);
  return { user, stats, notifications };
}
```

Total time ≈ duration of the slowest single request. Correct here because all three requests are independent.

### The Performance Difference

If each request takes 200ms:

- Sequential: 200 + 200 + 200 = **600ms**
- Parallel: max(200, 200, 200) = **200ms**

**Rule:** Use `Promise.all` (parallel) for independent operations. Use sequential `await` when each step depends on the result of the previous.

### `await` in Loops

A common pattern that accidentally forces sequential execution:

```javascript
// SEQUENTIAL — each waits for the previous (600ms for 3 items)
async function loadAllSequential(ids) {
  const results = [];
  for (const id of ids) {
    const data = await fetch(`/api/item/${id}`).then(r => r.json());
    results.push(data);
  }
  return results;
}

// PARALLEL — all fire at once (200ms for 3 items)
async function loadAllParallel(ids) {
  return Promise.all(ids.map(id =>
    fetch(`/api/item/${id}`).then(r => r.json())
  ));
}
```

Using `await` inside a `for...of` loop makes every iteration wait for the previous. Use `map` + `Promise.all` for independent array processing.

---

## 2. Promise Combinators

All four combinators accept an array (or iterable) of Promises.

### `Promise.all`

Fulfills when all fulfill; rejects immediately when any rejects:

```javascript
Promise.all([p1, p2, p3])
  .then(([r1, r2, r3]) => { /* all succeeded */ })
  .catch(err => { /* first rejection */ });
```

Use when you need all results and a single failure should abort everything.

### `Promise.allSettled`

Waits for all Promises to settle regardless of outcome. Never rejects:

```javascript
Promise.allSettled([p1, p2, p3]).then(results => {
  results.forEach(r => {
    if (r.status === 'fulfilled') console.log(r.value);
    else console.log(r.reason.message);
  });
});
```

Each result object has:

- `{ status: 'fulfilled', value: ... }`
- `{ status: 'rejected', reason: ... }`

Use when you want to process each result individually, regardless of whether others failed.

### `Promise.race`

Settles with the first Promise to settle — fulfilled or rejected:

```javascript
function withTimeout(promise, ms) {
  const timeout = new Promise((_, reject) =>
    setTimeout(() => reject(new Error(`Timeout after ${ms}ms`)), ms)
  );
  return Promise.race([promise, timeout]);
}
```

Use for implementing timeouts, or when you want the fastest of several equivalent sources.

### `Promise.any`

Fulfills with the first fulfilled Promise. Rejects only when all reject (with `AggregateError`):

```javascript
Promise.any([fetchFromPrimary(), fetchFromBackup()])
  .then(result => console.log('Got result:', result))
  .catch(err => console.error('All failed:', err));
// err is an AggregateError with an .errors array
```

Use for redundancy: try multiple sources, accept whichever succeeds first.

### Combinator Summary

| Method | Fulfills when | Rejects when | Use for |
|---|---|---|---|
| `Promise.all` | All fulfill | Any rejects | All required, fail-fast |
| `Promise.allSettled` | All settle | Never | Process each result individually |
| `Promise.race` | First settles | First rejects | Timeouts, fastest source |
| `Promise.any` | First fulfills | All reject | Redundancy, fallback sources |

---

## 3. JSON: `stringify` and `parse`

JSON (JavaScript Object Notation) is the standard format for exchanging data with web APIs and for persisting structured data.

### `JSON.stringify(value)`

Converts a JavaScript value to a JSON string:

```javascript
const obj = { name: 'Alice', age: 30, active: true };
const json = JSON.stringify(obj);
// '{"name":"Alice","age":30,"active":true}'
```

### `JSON.parse(string)`

Converts a JSON string back to a JavaScript value:

```javascript
const parsed = JSON.parse('{"name":"Alice","age":30}');
console.log(parsed.name);   // 'Alice'
console.log(typeof parsed); // 'object'
```

### What JSON Preserves and What It Drops

| JavaScript value | JSON result |
|---|---|
| String, number, boolean, `null` | Preserved |
| Array, plain object | Preserved (recursively) |
| `undefined` (as a value or property) | Omitted / becomes `null` in arrays |
| Function | Omitted entirely |
| `Date` object | Converted to ISO 8601 string (NOT a Date after parse) |
| `Infinity`, `NaN` | Becomes `null` |
| `Symbol` | Omitted |

```javascript
const obj = {
  name: 'Bob',
  greet: () => 'hello',    // omitted
  created: new Date(),     // becomes ISO string
  score: Infinity          // becomes null
};

const json = JSON.stringify(obj);
// '{"name":"Bob","created":"2025-01-15T...","score":null}'
// greet is gone

const back = JSON.parse(json);
console.log(back.created instanceof Date);   // false — it's a string
```

### Pretty Printing

```javascript
JSON.stringify(obj, null, 2)   // 2-space indent
JSON.stringify(obj, null, 4)   // 4-space indent
```

The second argument (`null`) is a replacer (array of keys to include, or a function). Usually `null` to include everything.

### `JSON.stringify` / `JSON.parse` with `localStorage`

`localStorage` only stores strings. Use JSON to store objects:

```javascript
// Save
const prefs = { theme: 'dark', lang: 'en', fontSize: 16 };
localStorage.setItem('prefs', JSON.stringify(prefs));

// Load
const raw = localStorage.getItem('prefs');
const loaded = raw ? JSON.parse(raw) : null;
console.log(loaded?.theme);   // 'dark'
```

Always guard against `null` from `getItem` — the key may not exist yet.

---

## 4. `AbortController` — Cancelling Fetch Requests

Once a `fetch` call is made, the request is in flight. `AbortController` lets you cancel it.

### Basic Usage

```javascript
const controller = new AbortController();

fetch('/api/data', { signal: controller.signal })
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => {
    if (err.name === 'AbortError') {
      console.log('Request was cancelled');
    } else {
      throw err;   // re-throw real errors
    }
  });

// Cancel the request
controller.abort();
```

When `abort()` is called, the fetch Promise rejects with a `DOMException` whose `name` is `'AbortError'`. Always check `err.name === 'AbortError'` to distinguish intentional cancellation from network errors.

### Pattern: Cancel Previous Request on New Input

```javascript
let activeController = null;

async function search(query) {
  if (activeController) activeController.abort();
  activeController = new AbortController();

  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
      signal: activeController.signal
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    if (err.name === 'AbortError') return;   // expected — a newer search started
    throw err;
  }
}
```

Each new `search` call aborts the previous one. Only the latest result processes.

---

## 5. Structured Error Handling

### The `response.ok` Wrapper Function

Centralizing the HTTP error check prevents callers from forgetting it:

```javascript
async function apiFetch(url, options = {}) {
  const res = await fetch(url, options);
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`HTTP ${res.status}: ${text || url}`);
  }
  return res.json();
}
```

### Error Boundaries in Multi-Step Workflows

```javascript
async function initDashboard(userId) {
  try {
    // Critical data — if this fails, abort
    const user = await apiFetch(`/api/users/${userId}`);

    // Non-critical data — degrade gracefully
    const [posts, notifications] = await Promise.allSettled([
      apiFetch(`/api/posts?user=${userId}`),
      apiFetch(`/api/notifications?user=${userId}`)
    ]).then(results => results.map(r =>
      r.status === 'fulfilled' ? r.value : []
    ));

    render(user, posts, notifications);
  } catch (err) {
    showError('Could not load dashboard: ' + err.message);
  }
}
```

Critical requests use `Promise.all` (fail together) or individual `await` with `try/catch`. Non-critical requests use `Promise.allSettled` so a failure in one does not break the others.

### Unhandled Promise Rejections

A rejected Promise with no `.catch` or `try/catch` is an **unhandled rejection**:

```javascript
// BAD — if fetch fails, the rejection is unhandled
async function loadData() {
  const data = await fetch('/api/data').then(r => r.json());
  render(data);
}
loadData();   // no .catch, no try/catch at the call site
```

Node.js prints a warning and may crash. Browsers may log a console error. Always handle rejections:

```javascript
loadData().catch(err => showError(err.message));
// or wrap loadData's body in try/catch
```

---

## 6. JSE Certification Exam Tips

1. **Sequential `await` vs `Promise.all`** — sequential forces operations to run one after another; `Promise.all` runs them concurrently. Know when each is correct.

2. **`Promise.allSettled` never rejects** — it always fulfills with an array of result objects. Each has `status`, `value` (fulfilled), or `reason` (rejected).

3. **`Promise.race` settles with the first to settle** — if the first is a rejection, the race rejects. Use for timeouts.

4. **`Promise.any` fulfills with the first to fulfill** — rejects only when all reject, with `AggregateError`.

5. **`JSON.stringify` drops functions and `undefined` properties** — they are silently omitted. `Date` objects become ISO strings.

6. **`JSON.parse` produces plain objects** — a serialized `Date` becomes a string after parsing, not a `Date` object.

7. **`AbortController.abort()` causes `AbortError`** — check `err.name === 'AbortError'` to identify intentional cancellations.

8. **`fetch` does not reject on HTTP errors** — always check `response.ok`. This applies to all combinator patterns.

9. **`await` in `for...of` is sequential** — use `map + Promise.all` for parallel array processing.

10. **Every async call site needs an error path** — unhandled rejections are bugs. Either `try/catch` the `async` function body or add `.catch` at the call site.

---

## 7. Study Checklist

- [ ] Watch the Module 14 video lecture by Professor Nash.
- [ ] Read [MDN — Promise.allSettled()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled).
- [ ] Read [MDN — AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).
- [ ] Read [MDN — JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).
- [ ] Time a sequential vs parallel fetch in the browser — confirm the difference.
- [ ] Test `Promise.allSettled` with a mix of resolved and rejected Promises — inspect each result object.
- [ ] Serialize an object with a function and a Date — confirm the function is omitted and the Date becomes a string.
- [ ] Implement `AbortController` on a fetch — confirm `AbortError` is thrown and caught correctly.
- [ ] Store preferences in `localStorage` with `JSON.stringify` and retrieve with `JSON.parse`.
- [ ] Complete the Module 14 Lab.
- [ ] Complete the Module 14 Quiz.
