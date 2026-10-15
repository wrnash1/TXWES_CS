# Video Script: CIS-1320 — Introduction to JavaScript

## Module 13 — Asynchronous JavaScript

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp &bull; JavaScript Programming Full Course &bull; Module 13</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=jS4aFq5-91M" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/jS4aFq5-91M" title="freeCodeCamp &bull; JavaScript Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp &bull; JavaScript Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening — The Single-Threaded Event Loop

JavaScript runs on a single thread. That means it can only do one thing at a time — it cannot run two pieces of code simultaneously. So how does a web page stay responsive while waiting for a network request to complete? How does `setTimeout` delay execution without freezing the page?

The answer is the **event loop** — JavaScript's mechanism for handling tasks that take time without blocking the rest of the program.

Here is the model:

- The **call stack** is where JavaScript executes code right now. Synchronous code runs here, one statement at a time.
- **Web APIs** (provided by the browser, not JavaScript itself) handle things that take time: network requests, timers, DOM events. When your code starts a timer or fetch, it hands off to the browser's Web API and continues.
- When the Web API finishes (timer expires, data arrives), it places the callback in the **event queue**.
- The **event loop** checks: is the call stack empty? If yes, take the next item from the queue and run it.

This is why asynchronous code does not block. You tell the browser 'go get this data, and call me back when you have it' — the browser handles the waiting; your JavaScript stays free to respond to user input.

Let us see this in code.

---

## Part 1 — `setTimeout` and `setInterval`

`setTimeout` and `setInterval` are the simplest asynchronous operations. They hand off to the browser's timer API and schedule callbacks.

```javascript
console.log('before');

setTimeout(() => {
  console.log('inside setTimeout — runs after 1 second');
}, 1000);   // delay in milliseconds

console.log('after');
```

Run this. The console shows:

```text
before
after
inside setTimeout — runs after 1 second
```

`'after'` prints before `'inside setTimeout'` even though it is written after the `setTimeout` call. JavaScript does not wait for the timer — it registers the callback with the browser and immediately continues to the next synchronous line.

**Zero delay — still async:**

```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
console.log('C');
```

Output: `A`, `C`, `B` — even with a zero millisecond delay. The callback goes into the event queue and runs only after the current synchronous code finishes.

```javascript
let count = 0;

const intervalId = setInterval(() => {
  count++;
  console.log('Tick:', count);
  if (count >= 5) {
    clearInterval(intervalId);
    console.log('Interval cleared');
  }
}, 500);
```

`setInterval` fires repeatedly every 500ms until `clearInterval` is called. Store the return value (the interval ID) so you can cancel it.

**`clearTimeout` and `clearInterval`:**

```javascript
const timerId = setTimeout(() => console.log('will not run'), 5000);
clearTimeout(timerId);   // cancelled before it fires
```

Both return a numeric ID. Pass that ID to `clearTimeout` or `clearInterval` to cancel.

---

## Part 2 — Promises

A **Promise** is an object that represents the eventual result of an asynchronous operation. It is in one of three states:

- **Pending** — the operation is in progress, result not yet known
- **Fulfilled** — the operation succeeded; the Promise has a value
- **Rejected** — the operation failed; the Promise has an error reason

A Promise transitions from pending to either fulfilled or rejected — once settled, it stays there.

```javascript
const myPromise = new Promise((resolve, reject) => {
  // Simulate async work with setTimeout
  setTimeout(() => {
    const success = true;
    if (success) {
      resolve('Operation succeeded!');   // fulfills with this value
    } else {
      reject(new Error('Operation failed'));   // rejects with this error
    }
  }, 1000);
});
```

The `Promise` constructor receives an **executor function** with two arguments: `resolve` (call to fulfill) and `reject` (call to reject).

```javascript
myPromise
  .then(value => {
    console.log('Fulfilled:', value);   // 'Operation succeeded!'
  })
  .catch(error => {
    console.error('Rejected:', error.message);
  })
  .finally(() => {
    console.log('Done — runs regardless of success or failure');
  });
```

`.then(onFulfilled)` — runs when the Promise fulfills; receives the resolved value.
`.catch(onRejected)` — runs when the Promise rejects; receives the error.
`.finally(onSettled)` — runs in both cases; good for cleanup (hiding a loading spinner, for example).

**Promise chaining:**

`.then` returns a new Promise, so you can chain:

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())    // parse JSON — also returns a Promise
  .then(data => console.log(data))
  .catch(error => console.error('Fetch failed:', error));
```

Each `.then` receives the value returned by the previous one.

**`Promise.all` — run multiple Promises in parallel:**

```javascript
const p1 = fetch('https://jsonplaceholder.typicode.com/todos/1').then(r => r.json());
const p2 = fetch('https://jsonplaceholder.typicode.com/todos/2').then(r => r.json());
const p3 = fetch('https://jsonplaceholder.typicode.com/todos/3').then(r => r.json());

Promise.all([p1, p2, p3])
  .then(([todo1, todo2, todo3]) => {
    console.log(todo1.title, todo2.title, todo3.title);
  })
  .catch(error => console.error('One failed:', error));
```

`Promise.all` takes an array of Promises. It resolves when **all** fulfill (with an array of results), or rejects as soon as **any** one rejects.

---

## Part 3 — `async` / `await`

`async` and `await` are syntactic sugar over Promises. They let you write asynchronous code that reads like synchronous code — no `.then` chains, no callback nesting.

```javascript
async function getData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const data = await response.json();
  console.log(data);
}

getData();
```

Two rules:

1. `await` can only be used inside an `async` function.
2. `await` pauses execution of the `async` function until the Promise settles — but does NOT block the rest of the program. Other code continues running.

Promise chain version:

```javascript
function getDataPromise() {
  return fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(res => res.json())
    .then(data => {
      console.log(data);
      return data;
    });
}
```

Equivalent `async/await` version:

```javascript
async function getDataAsync() {
  const res  = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const data = await res.json();
  console.log(data);
  return data;
}
```

Same behavior — different syntax. `async/await` reads top to bottom like synchronous code, making it easier to follow and debug.

```javascript
async function safeFetch(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed:', error.message);
    return null;
  }
}

safeFetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(data => console.log('Got:', data));
```

Notice `!response.ok` — `fetch` only rejects on network errors (no connection). A 404 or 500 HTTP response still **resolves** the Promise. You must check `response.ok` (true for 200–299 status codes) and throw manually if needed.

**`async` functions always return a Promise:**

```javascript
async function add(a, b) {
  return a + b;   // equivalent to: return Promise.resolve(a + b)
}

add(2, 3).then(result => console.log(result));   // 5
```

Even if the body is synchronous, calling an `async` function returns a Promise.

---

## Part 4 — `fetch` in Practice

The `fetch` API is the standard browser tool for making HTTP requests. Let us build a complete working example.

```javascript
async function loadUser(id) {
  const output = document.getElementById('output');
  output.textContent = 'Loading...';

  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);

    const user = await response.json();

    output.innerHTML = `
      <h3>${user.name}</h3>
      <p>Email: ${user.email}</p>
      <p>City: ${user.address.city}</p>
    `;
  } catch (error) {
    output.textContent = `Error: ${error.message}`;
  }
}

document.getElementById('load-btn').addEventListener('click', () => {
  loadUser(Math.ceil(Math.random() * 10));
});
```

This function:

1. Shows 'Loading...' immediately
2. Fetches a user from the API
3. Renders the result as HTML on success
4. Displays the error message on failure

**`Promise.all` for parallel fetches:**

```javascript
async function loadMultiple() {
  const ids = [1, 2, 3];
  const urls = ids.map(id => `https://jsonplaceholder.typicode.com/todos/${id}`);

  try {
    const responses = await Promise.all(urls.map(url => fetch(url)));
    const todos = await Promise.all(responses.map(r => r.json()));
    todos.forEach(todo => console.log(todo.title));
  } catch (error) {
    console.error('A fetch failed:', error);
  }
}
```

`Promise.all` fires all three requests at the same time — total wait time is the duration of the slowest request, not the sum.

---

## Closing — Lab Preview

The Module 13 lab has four parts.

Part 1 covers `setTimeout` and `setInterval` — you will observe the async execution order, build a countdown timer, and practice `clearInterval`.

Part 2 covers Promises — you will create Promises manually, practice `.then/.catch/.finally` chaining, and observe the three states.

Part 3 covers `async/await` — you will rewrite Promise chains as `async/await`, practice `try/catch`, and handle the `response.ok` check.

Part 4 is the integration — a fetch-driven page that loads data from a public API, renders it to the DOM, and handles loading and error states.

The quiz focuses on the event loop execution order, Promise states, `.then/.catch` vs `try/catch`, `async/await` syntax rules, and the `response.ok` check. Read the reading guide — asynchronous JavaScript is one of the densest topics in the course and the guide covers it carefully. Good luck.

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 13 — Asynchronous JavaScript]**

---

## Additional Resources

- [MDN — Asynchronous JavaScript overview](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- [MDN — Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [MDN — async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [MDN — fetch()](https://developer.mozilla.org/en-US/docs/Web/API/fetch)
- [Eloquent JavaScript — Chapter 11: Asynchronous Programming](https://eloquentjavascript.net/11_async.html)
- [JSONPlaceholder — free test API](https://jsonplaceholder.typicode.com/)
