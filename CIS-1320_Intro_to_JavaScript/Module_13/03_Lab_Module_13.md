# Lab Activity: Module 13 — Asynchronous JavaScript

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Lab Overview

This lab builds from `setTimeout` through Promises to `async/await` and `fetch`. Parts 1–3 use Node.js (no browser required); Part 4 runs in the browser with Live Server and calls a real public API.

**Environment:**

- Parts 1–3: Node.js in VS Code terminal (`node filename.js`)
- Part 4: VS Code + Live Server + Chrome DevTools (Network tab useful)

---

## Part 1 — `setTimeout`, `setInterval`, and Execution Order

**File:** `timers.js`

**Learning objectives:** Observe that async callbacks run after synchronous code; build a countdown; use `clearInterval`.

### Section 1.1 — Execution Order

Create `timers.js`:

```javascript
// 1.1 — Execution order demonstration
console.log('A — synchronous');

setTimeout(() => {
  console.log('C — setTimeout callback (1000ms)');
}, 1000);

setTimeout(() => {
  console.log('D — setTimeout callback (0ms)');
}, 0);

console.log('B — synchronous');
```

Run: `node timers.js`

Expected output — confirm this order:

```text
A — synchronous
B — synchronous
D — setTimeout callback (0ms)
C — setTimeout callback (1000ms)
```

`D` prints before `C` because it has a shorter delay, but both print after `A` and `B` — synchronous code always runs first.

### Section 1.2 — Countdown Timer

```javascript
// 1.2 — Countdown using setInterval
function countdown(from) {
  console.log(`Starting countdown from ${from}`);
  let current = from;

  const id = setInterval(() => {
    console.log(current);
    current--;
    if (current < 0) {
      clearInterval(id);
      console.log('Lift off!');
    }
  }, 500);
}

countdown(5);
```

Run. Confirm: `5`, `4`, `3`, `2`, `1`, `0`, `Lift off!` appear at 500ms intervals.

### Section 1.3 — `clearTimeout` Before Firing

```javascript
// 1.3 — Cancelling a timeout before it fires
const timerId = setTimeout(() => {
  console.log('This should NOT appear');
}, 2000);

clearTimeout(timerId);
console.log('Timer was cancelled');
```

Run. Only `'Timer was cancelled'` appears — the timeout callback never fires.

---

## Part 2 — Promises

**File:** `promises.js`

**Learning objectives:** Create Promises manually; consume with `.then/.catch/.finally`; chain `.then`; use `Promise.all`.

### Section 2.1 — Creating and Consuming a Promise

Create `promises.js`:

```javascript
// 2.1 — Manual Promise creation
function delayedDouble(n) {
  return new Promise((resolve, reject) => {
    if (typeof n !== 'number') {
      reject(new Error(`Expected a number, got ${typeof n}`));
      return;
    }
    setTimeout(() => {
      resolve(n * 2);
    }, 500);
  });
}

// Fulfillment path
delayedDouble(7)
  .then(result => console.log('Doubled:', result))   // 14
  .catch(error => console.error('Error:', error.message));

// Rejection path
delayedDouble('hello')
  .then(result => console.log('Should not run:', result))
  .catch(error => console.error('Caught:', error.message));
  // 'Caught: Expected a number, got string'
```

Run. Confirm the fulfillment path logs `14` and the rejection path logs the error message.

### Section 2.2 — `.finally`

```javascript
// 2.2 — .finally runs in both cases
function fetchSimulated(shouldFail) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (shouldFail) reject(new Error('Simulated failure'));
      else resolve({ data: 'some result' });
    }, 300);
  });
}

fetchSimulated(false)
  .then(result => console.log('Success:', result.data))
  .catch(err   => console.error('Error:', err.message))
  .finally(()  => console.log('Cleanup — always runs (success case)'));

fetchSimulated(true)
  .then(result => console.log('Success:', result.data))
  .catch(err   => console.error('Error:', err.message))
  .finally(()  => console.log('Cleanup — always runs (failure case)'));
```

Run. Confirm `.finally` logs in both cases.

### Section 2.3 — Promise Chaining

```javascript
// 2.3 — Chaining: each .then receives the return value of the previous
Promise.resolve(2)
  .then(n => {
    console.log('Step 1:', n);   // 2
    return n * 3;
  })
  .then(n => {
    console.log('Step 2:', n);   // 6
    return n + 10;
  })
  .then(n => {
    console.log('Step 3:', n);   // 16
  });
```

### Section 2.4 — `Promise.all`

```javascript
// 2.4 — Promise.all: all must fulfill
function slowAdd(a, b, delay) {
  return new Promise(resolve => setTimeout(() => resolve(a + b), delay));
}

Promise.all([
  slowAdd(1, 2, 300),   // resolves to 3
  slowAdd(4, 5, 100),   // resolves to 9
  slowAdd(7, 8, 200)    // resolves to 15
]).then(results => {
  console.log('All results:', results);   // [3, 9, 15]
  console.log('Sum:', results.reduce((a, b) => a + b, 0));   // 27
});

// Promise.all rejects immediately if any Promise rejects
Promise.all([
  Promise.resolve('ok'),
  Promise.reject(new Error('one failed')),
  Promise.resolve('also ok')
]).catch(err => console.error('Promise.all rejected:', err.message));
```

Run. Confirm all three results arrive together, and the rejection causes the `.catch` to fire.

---

## Part 3 — `async` / `await`

**File:** `async_await.js`

**Learning objectives:** Write `async` functions; use `await`; handle errors with `try/catch`; compare to `.then` chains.

### Section 3.1 — Basic `async/await`

Create `async_await.js`:

```javascript
// 3.1 — Basic async/await
function simulateFetch(value, delay = 300) {
  return new Promise((resolve) => setTimeout(() => resolve(value), delay));
}

async function processData() {
  console.log('Starting...');

  const step1 = await simulateFetch('raw data', 300);
  console.log('Step 1:', step1);

  const step2 = await simulateFetch(step1.toUpperCase(), 200);
  console.log('Step 2:', step2);

  const step3 = await simulateFetch(`[${step2}]`, 100);
  console.log('Step 3:', step3);

  return step3;
}

processData().then(final => console.log('Final result:', final));
```

Run. Confirm each step logs in order — the `await` makes sequential async steps read like synchronous code.

### Section 3.2 — `try/catch` Error Handling

```javascript
// 3.2 — Error handling with try/catch
function riskyOperation(succeed) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (succeed) resolve('success value');
      else reject(new Error('operation failed'));
    }, 200);
  });
}

async function runSafe(succeed) {
  try {
    const result = await riskyOperation(succeed);
    console.log('Got:', result);
    return result;
  } catch (error) {
    console.error('Caught in try/catch:', error.message);
    return null;
  } finally {
    console.log('finally block ran');
  }
}

runSafe(true);    // logs 'Got: success value', then finally
runSafe(false);   // logs error message, then finally
```

### Section 3.3 — `async` Function Always Returns a Promise

```javascript
// 3.3 — async return value is always a Promise
async function addAsync(a, b) {
  return a + b;   // wrapped in Promise.resolve automatically
}

const result = addAsync(3, 4);
console.log('Is a Promise?', result instanceof Promise);   // true

result.then(val => console.log('Value:', val));   // 7
```

### Section 3.4 — Parallel with `Promise.all` inside `async`

```javascript
// 3.4 — await Promise.all for concurrent operations
async function loadAll() {
  const [a, b, c] = await Promise.all([
    simulateFetch(10, 300),
    simulateFetch(20, 100),
    simulateFetch(30, 200)
  ]);

  console.log('a:', a, 'b:', b, 'c:', c);
  console.log('Total:', a + b + c);
}

loadAll();
```

Run. Confirm all three values arrive together (total wait ≈ 300ms, not 600ms).

---

## Part 4 — `fetch` in the Browser

**Files:** `index.html` + `lab13.js`

**Learning objectives:** Use `fetch` to call a real API; handle loading state; check `response.ok`; render data to the DOM; handle errors gracefully.

### Setup

Create a folder `module13_lab/` with the following files:

**`index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 13 Lab</title>
  <style>
    body { font-family: sans-serif; max-width: 700px; margin: 2rem auto; padding: 0 1rem; }
    h1, h2 { color: #333; }
    button { padding: 0.4rem 0.9rem; margin: 0.25rem; cursor: pointer; }
    input[type="number"] { padding: 0.4rem; width: 80px; }
    .card { border: 1px solid #ccc; padding: 1rem; border-radius: 6px; margin: 0.5rem 0; background: #fafafa; }
    .loading { color: #888; font-style: italic; }
    .error   { color: #c00; font-weight: bold; }
    .done    { text-decoration: line-through; color: #888; }
    #todo-list { list-style: none; padding: 0; }
    #todo-list li { padding: 0.4rem 0.6rem; border-bottom: 1px solid #eee; cursor: pointer; }
    #todo-list li:hover { background: #f5f5f5; }
  </style>
</head>
<body>
  <h1>Module 13: Async JavaScript</h1>

  <h2>Single User Fetch</h2>
  <label>User ID (1–10): <input type="number" id="user-id" value="1" min="1" max="10"></label>
  <button id="fetch-user-btn">Fetch User</button>
  <div id="user-output"></div>

  <h2>Todo List (User's Todos)</h2>
  <button id="fetch-todos-btn">Fetch Todos for User 1</button>
  <div id="todos-loading" class="loading" style="display:none">Loading todos...</div>
  <ul id="todo-list"></ul>

  <h2>Error Handling Demo</h2>
  <button id="fetch-bad-btn">Fetch Non-Existent User (ID 999)</button>
  <div id="error-output"></div>

  <script src="lab13.js"></script>
</body>
</html>
```

**`lab13.js`**

```javascript
// --- Part 4: fetch in the browser ---

const BASE = 'https://jsonplaceholder.typicode.com';

// Utility: show content in a container
function show(id, html) {
  document.getElementById(id).innerHTML = html;
}
```

### Section 4.1 — Fetch a Single User

```javascript
// 4.1 — Fetch and render a user by ID
async function fetchUser(id) {
  const output = document.getElementById('user-output');
  output.innerHTML = '<p class="loading">Loading...</p>';

  try {
    const res = await fetch(`${BASE}/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status} — user ${id} not found`);

    const user = await res.json();

    output.innerHTML = `
      <div class="card">
        <strong>${user.name}</strong> (@${user.username})<br>
        Email: ${user.email}<br>
        City: ${user.address.city}<br>
        Company: ${user.company.name}
      </div>
    `;
  } catch (error) {
    output.innerHTML = `<p class="error">Error: ${error.message}</p>`;
  }
}

document.getElementById('fetch-user-btn').addEventListener('click', () => {
  const id = parseInt(document.getElementById('user-id').value);
  fetchUser(id);
});

// Load user 1 on startup
fetchUser(1);
```

Save and open with Live Server. Confirm user 1 renders. Change the ID and click Fetch User.

### Section 4.2 — Fetch Todos and Render a List

```javascript
// 4.2 — Fetch todos for user 1 and render with click-to-complete
async function fetchTodos(userId) {
  const listEl   = document.getElementById('todo-list');
  const loadingEl = document.getElementById('todos-loading');

  listEl.innerHTML = '';
  loadingEl.style.display = 'block';

  try {
    const res = await fetch(`${BASE}/todos?userId=${userId}&_limit=10`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const todos = await res.json();
    loadingEl.style.display = 'none';

    todos.forEach(todo => {
      const li = document.createElement('li');
      li.textContent = todo.title;
      if (todo.completed) li.classList.add('done');
      li.dataset.id = todo.id;

      // Click to toggle done state locally
      li.addEventListener('click', () => li.classList.toggle('done'));

      listEl.appendChild(li);
    });
  } catch (error) {
    loadingEl.style.display = 'none';
    listEl.innerHTML = `<li class="error">Failed to load: ${error.message}</li>`;
  }
}

document.getElementById('fetch-todos-btn').addEventListener('click', () => {
  fetchTodos(1);
});
```

Confirm the loading indicator appears briefly, then a list of 10 todos renders. Click a todo to toggle strikethrough.

### Section 4.3 — Error Handling Demo

```javascript
// 4.3 — Deliberately trigger an HTTP error
async function fetchBadUser() {
  const output = document.getElementById('error-output');
  output.innerHTML = '<p class="loading">Fetching user 999...</p>';

  try {
    const res = await fetch(`${BASE}/users/999`);

    // JSONPlaceholder returns 200 with empty body for missing resources
    // Real APIs typically return 404 — we simulate the check here
    const data = await res.json();

    if (!data || Object.keys(data).length === 0) {
      throw new Error('User 999 not found (empty response)');
    }

    output.innerHTML = `<p>Got: ${JSON.stringify(data)}</p>`;
  } catch (error) {
    output.innerHTML = `<p class="error">Handled error: ${error.message}</p>`;
  }
}

document.getElementById('fetch-bad-btn').addEventListener('click', fetchBadUser);
```

### Section 4.4 — `Promise.all` for Parallel Fetches

```javascript
// 4.4 — Fetch multiple users in parallel
async function fetchMultipleUsers() {
  const ids = [1, 2, 3];

  try {
    const responses = await Promise.all(
      ids.map(id => fetch(`${BASE}/users/${id}`))
    );

    // Check all responses
    responses.forEach(res => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
    });

    const users = await Promise.all(responses.map(r => r.json()));

    console.log('All three users loaded in parallel:');
    users.forEach(u => console.log(` - ${u.name} (${u.email})`));
  } catch (error) {
    console.error('Parallel fetch failed:', error.message);
  }
}

// Run on load — results in console only
fetchMultipleUsers();
```

Open DevTools → Network tab. Confirm three `/users/` requests fire nearly simultaneously (not sequentially).

---

## Lab Completion Checklist

- [ ] `setTimeout` callbacks run after synchronous code even with 0ms delay
- [ ] `setInterval` countdown ticks 5→0 then clears itself
- [ ] `clearTimeout` prevents the callback from firing
- [ ] Promise fulfillment path logs correct result; rejection path reaches `.catch`
- [ ] `.finally` runs in both fulfilled and rejected cases
- [ ] Promise chain passes values through each `.then`
- [ ] `Promise.all` resolves with array of all results when all fulfill
- [ ] `Promise.all` reaches `.catch` when any one rejects
- [ ] `async/await` sequential steps run in order
- [ ] `try/catch` in `async` function catches rejected Promise
- [ ] `async` function return value confirmed as a Promise instance
- [ ] `Promise.all` inside `async` runs operations concurrently
- [ ] Browser: user card renders on load and updates on new ID + click
- [ ] Browser: loading indicator shows and hides correctly for todos
- [ ] Browser: todo list renders 10 items; click toggles done style
- [ ] Browser: error case renders error message (not a crash)
- [ ] Browser: Network tab confirms parallel requests fire simultaneously
