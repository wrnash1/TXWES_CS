# Video Script: CIS-1320 — Introduction to JavaScript

## Module 14 — Promises and Async/Await: Patterns in Practice

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Chrome DevTools (Console + Network tabs) for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Module 13 introduced Promises and `async/await`. Module 14 deepens the practice: sequential vs parallel patterns, Promise combinators beyond `Promise.all`, error handling strategies, `AbortController` for fetch cancellation, and `JSON.stringify`/`JSON.parse` for working with API data.
> - The sequential vs parallel performance comparison is highly visual — show the timer output to make the difference concrete.
> - `AbortController` is modern and practical — keep the demo brief but include it.
> - `JSON.stringify` / `JSON.parse` are tested on the JSE exam. Cover the `replacer`/`reviver` briefly but focus on the common use cases.
> - `localStorage` with JSON — a natural practical combination. The lab uses this.
> - Unhandled Promise rejections: warn students. Node prints a warning; browsers may silently swallow them in older code. Always have a `.catch` or `try/catch`.
> - Do not cover `XMLHttpRequest` — it is fully legacy.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 14 | Promises and Async/Await: Patterns in Practice | CIS-1320"]**

"Module 13 gave you the foundation: the event loop, Promises, and `async/await`. Module 14 puts that foundation to work with real patterns you will use in every project: how to run async operations sequentially versus in parallel, how to handle errors at every level, how to cancel a fetch request in progress, and how to serialize and parse JSON data. By the end of this module, you will write async code that is not just functional but well-structured and production-ready."

---

## [01:30 – 06:30] Part 1 — Sequential vs Parallel Async Operations

**[SHOW SLIDE: "Sequential vs Parallel"]**

"One of the most common performance mistakes in async JavaScript: using `await` in a loop when the operations are independent, forcing them to run one after another when they could run together.

**[DEMO — Sequential (slow)]**

```javascript
async function loadSequential() {
  const start = Date.now();

  const res1 = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const todo1 = await res1.json();

  const res2 = await fetch('https://jsonplaceholder.typicode.com/todos/2');
  const todo2 = await res2.json();

  const res3 = await fetch('https://jsonplaceholder.typicode.com/todos/3');
  const todo3 = await res3.json();

  console.log(`Sequential: ${Date.now() - start}ms`);
  return [todo1, todo2, todo3];
}
```

Each `await` waits for the previous request to finish before starting the next. Total time ≈ sum of all three response times.

[PAUSE]

**[DEMO — Parallel (fast)]**

```javascript
async function loadParallel() {
  const start = Date.now();

  const [res1, res2, res3] = await Promise.all([
    fetch('https://jsonplaceholder.typicode.com/todos/1'),
    fetch('https://jsonplaceholder.typicode.com/todos/2'),
    fetch('https://jsonplaceholder.typicode.com/todos/3')
  ]);

  const [todo1, todo2, todo3] = await Promise.all([
    res1.json(), res2.json(), res3.json()
  ]);

  console.log(`Parallel: ${Date.now() - start}ms`);
  return [todo1, todo2, todo3];
}
```

All three requests fire simultaneously. Total time ≈ duration of the single slowest request.

[PAUSE]

**When sequential is the right choice:**

Sequential `await` is correct when each step depends on the previous result:

```javascript
async function authenticateAndLoad(credentials) {
  const token = await login(credentials);        // must complete first
  const profile = await loadProfile(token);      // needs token
  const settings = await loadSettings(profile.id);  // needs profile
  return { profile, settings };
}
```

Here the order matters — you cannot load the profile before you have the token. Sequential is correct.

**Rule: use `Promise.all` for independent operations; use sequential `await` for dependent operations.**"

---

## [06:30 – 10:30] Part 2 — Promise Combinators

**[SHOW SLIDE: "Promise Combinators"]**

"Module 13 introduced `Promise.all`. There are three more combinators worth knowing.

**[DEMO — `Promise.allSettled`]**

```javascript
const promises = [
  Promise.resolve('success 1'),
  Promise.reject(new Error('failure')),
  Promise.resolve('success 2')
];

Promise.allSettled(promises).then(results => {
  results.forEach(result => {
    if (result.status === 'fulfilled') {
      console.log('Fulfilled:', result.value);
    } else {
      console.log('Rejected:', result.reason.message);
    }
  });
});
```

`allSettled` waits for every Promise to settle — it never rejects itself. Each result has a `status` (`'fulfilled'` or `'rejected'`) and either `value` or `reason`. Use this when you want all results regardless of which ones failed.

[PAUSE]

**[DEMO — `Promise.race`]**

```javascript
function fetchWithTimeout(url, timeoutMs) {
  const fetchPromise = fetch(url);
  const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => reject(new Error(`Timeout after ${timeoutMs}ms`)), timeoutMs)
  );

  return Promise.race([fetchPromise, timeoutPromise]);
}

fetchWithTimeout('https://jsonplaceholder.typicode.com/todos/1', 3000)
  .then(res => res.json())
  .then(data => console.log('Got:', data.title))
  .catch(err => console.error('Failed:', err.message));
```

`Promise.race` settles with the first Promise to settle — fulfilled or rejected. Here we race the fetch against a timeout. If the fetch takes longer than 3 seconds, the timeout wins and rejects the race.

[PAUSE]

**[DEMO — `Promise.any`]**

```javascript
// Try multiple sources — use whichever responds first successfully
Promise.any([
  fetch('https://jsonplaceholder.typicode.com/todos/1'),
  fetch('https://jsonplaceholder.typicode.com/todos/2')
]).then(res => {
  console.log('First successful response:', res.url);
}).catch(err => {
  console.error('All failed:', err);   // AggregateError
});
```

`Promise.any` fulfills with the first fulfilled Promise. It only rejects if all Promises reject (with an `AggregateError`). Useful for redundancy: try multiple sources, use whichever succeeds first.

[PAUSE]

**Combinator Summary:**

| Method | Resolves when | Rejects when |
|---|---|---|
| `Promise.all` | All fulfill | Any one rejects (fast fail) |
| `Promise.allSettled` | All settle (any outcome) | Never |
| `Promise.race` | First one settles | First one rejects |
| `Promise.any` | First one fulfills | All reject |

"

---

## [10:30 – 14:30] Part 3 — JSON: `stringify` and `parse`

**[SHOW SLIDE: "JSON.stringify and JSON.parse"]**

"JSON — JavaScript Object Notation — is the standard data format for web APIs. Every `fetch` response you have worked with returns JSON. `JSON.stringify` converts a JavaScript value to a JSON string; `JSON.parse` converts a JSON string back to a JavaScript value.

**[DEMO]**

```javascript
const user = {
  name: 'Alice',
  age: 30,
  active: true,
  scores: [95, 87, 92],
  address: { city: 'Dallas', state: 'TX' }
};

// Convert to JSON string
const json = JSON.stringify(user);
console.log(json);
// '{"name":"Alice","age":30,"active":true,"scores":[95,87,92],"address":{"city":"Dallas","state":"TX"}}'

// Convert back to JavaScript object
const parsed = JSON.parse(json);
console.log(parsed.name);          // 'Alice'
console.log(parsed.address.city);  // 'Dallas'
```

[PAUSE]

**What JSON can and cannot represent:**

```javascript
const obj = {
  fn: () => 'hello',   // functions are omitted
  undef: undefined,     // undefined values are omitted
  date: new Date(),     // Date becomes an ISO string
  num: Infinity,        // becomes null
  name: 'Bob'          // strings survive fine
};

console.log(JSON.stringify(obj));
// '{"date":"2025-01-15T...","num":null,"name":"Bob"}'
// fn and undef are gone
```

Functions and `undefined` are silently dropped. Dates become ISO strings (not `Date` objects after parsing — just strings). Know these for the exam.

[PAUSE]

**Formatting with indent:**

```javascript
console.log(JSON.stringify(user, null, 2));
// Pretty-printed with 2-space indentation
```

**Using with `localStorage`:**

```javascript
// Save to localStorage
localStorage.setItem('preferences', JSON.stringify({ theme: 'dark', fontSize: 16 }));

// Read back
const prefs = JSON.parse(localStorage.getItem('preferences'));
console.log(prefs.theme);   // 'dark'
```

`localStorage` only stores strings. `JSON.stringify`/`JSON.parse` is the standard pattern to store and retrieve objects."

---

## [14:30 – 18:00] Part 4 — `AbortController` and Fetch Cancellation

**[SHOW SLIDE: "AbortController"]**

"Once you call `fetch`, the request is in flight. What if the user navigates away, or a newer request supersedes the old one? `AbortController` lets you cancel a fetch that is no longer needed.

**[DEMO]**

```javascript
// Create a controller
const controller = new AbortController();
const signal = controller.signal;

// Pass signal to fetch
fetch('https://jsonplaceholder.typicode.com/todos/1', { signal })
  .then(res => res.json())
  .then(data => console.log('Received:', data.title))
  .catch(err => {
    if (err.name === 'AbortError') {
      console.log('Fetch was aborted');
    } else {
      console.error('Fetch failed:', err.message);
    }
  });

// Abort the request (e.g., user clicked Cancel)
controller.abort();
```

When `abort()` is called, the fetch Promise rejects with an `AbortError`. Check `err.name === 'AbortError'` to distinguish an intentional cancellation from a real network error.

[PAUSE]

**Practical pattern — replace previous request on user input:**

```javascript
let currentController = null;

async function searchUsers(query) {
  // Cancel the previous search if it's still in flight
  if (currentController) {
    currentController.abort();
  }

  currentController = new AbortController();

  try {
    const res = await fetch(
      `https://jsonplaceholder.typicode.com/users?q=${query}`,
      { signal: currentController.signal }
    );
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const users = await res.json();
    renderResults(users);
  } catch (err) {
    if (err.name !== 'AbortError') {
      console.error('Search failed:', err.message);
    }
    // AbortError is expected — silently ignore
  }
}
```

Every new search aborts the previous one. Only the latest result renders."

---

## [18:00 – 21:00] Part 5 — Error Handling Strategies

**[SHOW SLIDE: "Async Error Handling"]**

"Unhandled Promise rejections cause silent failures. Every async operation needs an error path.

**[DEMO — Levels of error handling]**

```javascript
// Level 1: per-operation try/catch
async function loadUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error(`loadUser(${id}) failed:`, err.message);
    return null;   // return a safe default
  }
}

// Level 2: caller-level catch
async function initPage() {
  const user = await loadUser(1);
  if (!user) {
    showErrorMessage('Could not load user profile');
    return;
  }
  renderProfile(user);
}
```

[PAUSE]

**Centralized error handler:**

```javascript
async function apiFetch(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${url}`);
  return res.json();
}

// All callers get the same error behavior
async function loadPage() {
  try {
    const [user, posts] = await Promise.all([
      apiFetch('/api/user/1'),
      apiFetch('/api/posts?user=1')
    ]);
    render(user, posts);
  } catch (err) {
    showError(err.message);
  }
}
```

Centralizing the `response.ok` check in `apiFetch` means callers never forget it."

---

## [21:00 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 14 Lab Preview"]**

"The Module 14 lab has four parts.

Part 1 benchmarks sequential vs parallel fetches — you will time both approaches and observe the difference.

Part 2 covers the Promise combinators — you will use `allSettled`, `race`, and `any` on controlled Promises.

Part 3 covers JSON — you will practice `stringify` and `parse`, observe what gets dropped, and use `localStorage` to persist preferences.

Part 4 is the integration — a search page with `AbortController` that cancels in-flight requests when a new search fires, with centralized error handling and a graceful loading state.

The quiz tests sequential vs parallel performance, `allSettled` vs `all` behavior, JSON conversion rules, `AbortController` abort error detection, and structured error handling. Read the guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 14 — Promises and Async/Await: Patterns in Practice]**

---

## Additional Resources

- [MDN — Promise.allSettled()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
- [MDN — AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
- [MDN — JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
- [MDN — JSON.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
- [MDN — Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Eloquent JavaScript — Chapter 11: Asynchronous Programming](https://eloquentjavascript.net/11_async.html)
