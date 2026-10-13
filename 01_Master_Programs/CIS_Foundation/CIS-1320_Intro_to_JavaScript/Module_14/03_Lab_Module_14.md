# Lab Activity: Module 14 — Promises and Async/Await: Patterns in Practice

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Lab Overview

This lab applies the Module 14 patterns: benchmarking sequential vs parallel execution, using all four Promise combinators, serializing with JSON, and building a search page with `AbortController`. Parts 1–3 use Node.js; Part 4 runs in the browser.

**Environment:**

- Parts 1–3: Node.js (`node filename.js`)
- Part 4: VS Code + Live Server + Chrome DevTools (Network tab)

---

## Part 1 — Sequential vs Parallel

**File:** `parallel.js`

**Learning objectives:** Measure the performance difference between sequential `await` and `Promise.all`; practice `await` inside vs outside loops.

### Section 1.1 — Timer Utility

Create `parallel.js`:

```javascript
// Simulate an async operation that takes `ms` milliseconds
function delay(ms, value) {
  return new Promise(resolve => setTimeout(() => resolve(value), ms));
}
```

### Section 1.2 — Sequential Execution

```javascript
// 1.2 — Sequential: each step waits for the previous
async function sequential() {
  const start = Date.now();

  const a = await delay(300, 'alpha');
  const b = await delay(200, 'beta');
  const c = await delay(250, 'gamma');

  const elapsed = Date.now() - start;
  console.log(`Sequential: ${a}, ${b}, ${c} — ${elapsed}ms`);
  // Elapsed ≈ 750ms (300 + 200 + 250)
}

sequential();
```

Run. Note the elapsed time is approximately the sum of all three delays.

### Section 1.3 — Parallel Execution

```javascript
// 1.3 — Parallel: all three start at the same time
async function parallel() {
  const start = Date.now();

  const [a, b, c] = await Promise.all([
    delay(300, 'alpha'),
    delay(200, 'beta'),
    delay(250, 'gamma')
  ]);

  const elapsed = Date.now() - start;
  console.log(`Parallel: ${a}, ${b}, ${c} — ${elapsed}ms`);
  // Elapsed ≈ 300ms (duration of the slowest)
}

parallel();
```

Run. Note the elapsed time is approximately the duration of the slowest single operation.

### Section 1.4 — `await` in a Loop vs `Promise.all`

```javascript
// 1.4 — await in loop (sequential — avoid for independent ops)
async function loopSequential(ids) {
  const start = Date.now();
  const results = [];
  for (const id of ids) {
    const result = await delay(100, `item-${id}`);
    results.push(result);
  }
  console.log(`Loop sequential: ${Date.now() - start}ms`, results);
  // Elapsed ≈ 500ms (5 × 100ms)
}

// map + Promise.all (parallel — correct for independent ops)
async function loopParallel(ids) {
  const start = Date.now();
  const results = await Promise.all(ids.map(id => delay(100, `item-${id}`)));
  console.log(`Loop parallel: ${Date.now() - start}ms`, results);
  // Elapsed ≈ 100ms (all fire at once)
}

const ids = [1, 2, 3, 4, 5];
loopSequential(ids);
loopParallel(ids);
```

Run. Confirm the loop sequential takes ~500ms and the parallel loop takes ~100ms for the same five items.

### Section 1.5 — When Sequential Is Correct

```javascript
// 1.5 — Sequential is necessary when each step depends on the previous
async function dependentSteps() {
  const token = await delay(100, 'auth-token-xyz');
  console.log('Got token:', token);

  // Uses the token from step 1
  const userId = await delay(100, `user-for-${token}`);
  console.log('Got userId:', userId);

  // Uses the userId from step 2
  const profile = await delay(100, `profile-for-${userId}`);
  console.log('Got profile:', profile);
}

dependentSteps();
```

Observe: these must be sequential because each step depends on the previous result. `Promise.all` would be wrong here.

---

## Part 2 — Promise Combinators

**File:** `combinators.js`

**Learning objectives:** Use `allSettled`, `race`, and `any`; observe their distinct behaviors with mixed resolve/reject inputs.

Create `combinators.js`:

```javascript
function resolve(value, ms) {
  return new Promise(r => setTimeout(() => r(value), ms));
}

function reject(reason, ms) {
  return new Promise((_, r) => setTimeout(() => r(new Error(reason)), ms));
}
```

### Section 2.1 — `Promise.allSettled`

```javascript
// 2.1 — allSettled: waits for all, never rejects itself
async function testAllSettled() {
  const results = await Promise.allSettled([
    resolve('A succeeded', 100),
    reject('B failed',     200),
    resolve('C succeeded', 150)
  ]);

  results.forEach((r, i) => {
    if (r.status === 'fulfilled') {
      console.log(`Promise ${i}: fulfilled — ${r.value}`);
    } else {
      console.log(`Promise ${i}: rejected  — ${r.reason.message}`);
    }
  });
}

testAllSettled();
// Promise 0: fulfilled — A succeeded
// Promise 1: rejected  — B failed
// Promise 2: fulfilled — C succeeded
```

Run. Confirm all three results appear — the rejection did not abort the others.

### Section 2.2 — `Promise.all` vs `Promise.allSettled` Contrast

```javascript
// 2.2 — Promise.all rejects immediately when any rejects
async function testAll() {
  try {
    const results = await Promise.all([
      resolve('A', 100),
      reject('B failed', 200),
      resolve('C', 150)
    ]);
    console.log('Promise.all results:', results);   // never reaches here
  } catch (err) {
    console.log('Promise.all caught:', err.message);   // 'B failed'
  }
}

testAll();
```

Confirm: `Promise.all` reaches the catch; `Promise.allSettled` does not.

### Section 2.3 — `Promise.race`

```javascript
// 2.3 — race: first to settle wins
async function testRace() {
  const winner = await Promise.race([
    resolve('slow', 300),
    resolve('fast', 100),
    resolve('medium', 200)
  ]);
  console.log('Race winner:', winner);   // 'fast'
}

testRace();

// 2.4 — race with timeout pattern
function withTimeout(promise, ms) {
  const timeout = new Promise((_, reject) =>
    setTimeout(() => reject(new Error(`Timed out after ${ms}ms`)), ms)
  );
  return Promise.race([promise, timeout]);
}

async function testTimeout() {
  try {
    const result = await withTimeout(resolve('data', 500), 200);
    console.log('Result:', result);
  } catch (err) {
    console.log('Timeout caught:', err.message);   // 'Timed out after 200ms'
  }
}

testTimeout();
```

### Section 2.4 — `Promise.any`

```javascript
// 2.5 — any: first to fulfill wins; rejects only if ALL reject
async function testAny() {
  // Case 1: one succeeds
  const result = await Promise.any([
    reject('first fails', 100),
    resolve('second succeeds', 200),
    reject('third fails', 300)
  ]);
  console.log('Promise.any result:', result);   // 'second succeeds'
}

testAny();

// Case 2: all reject — produces AggregateError
async function testAnyAllFail() {
  try {
    await Promise.any([
      reject('A failed', 100),
      reject('B failed', 200)
    ]);
  } catch (err) {
    console.log('AggregateError:', err.constructor.name);
    console.log('Individual errors:', err.errors.map(e => e.message));
  }
}

testAnyAllFail();
```

---

## Part 3 — JSON

**File:** `json_demo.js`

**Learning objectives:** Practice `stringify` and `parse`; observe what gets omitted; use with a simulated `localStorage`.

Create `json_demo.js`:

### Section 3.1 — Basic Serialization

```javascript
// 3.1 — stringify and parse round-trip
const user = {
  id: 42,
  name: 'Alice',
  active: true,
  scores: [95, 87, 92],
  address: { city: 'Fort Worth', state: 'TX' }
};

const json = JSON.stringify(user);
console.log('JSON string:', json);
console.log('Type:', typeof json);   // 'string'

const parsed = JSON.parse(json);
console.log('Parsed name:', parsed.name);
console.log('Parsed city:', parsed.address.city);
console.log('Are they the same object?', user === parsed);   // false — new object
```

### Section 3.2 — What Gets Dropped

```javascript
// 3.2 — Functions and undefined are omitted; Date becomes a string
const obj = {
  name: 'Bob',
  greet: function() { return 'hi'; },  // omitted
  value: undefined,                     // omitted
  created: new Date(2025, 0, 15),       // ISO string
  score: Infinity,                      // null
  ratio: NaN                            // null
};

const serialized = JSON.stringify(obj);
console.log('Serialized:', serialized);
// {"name":"Bob","created":"2025-01-15T...","score":null,"ratio":null}

const back = JSON.parse(serialized);
console.log('greet present?', 'greet' in back);           // false
console.log('value present?', 'value' in back);           // false
console.log('created is Date?', back.created instanceof Date);  // false — string
```

### Section 3.3 — Pretty Printing

```javascript
// 3.3 — Formatted output
console.log(JSON.stringify(user, null, 2));
```

### Section 3.4 — Simulated `localStorage`

```javascript
// 3.4 — localStorage pattern (simulated in Node with a plain object)
const storage = {};

function setItem(key, value) {
  storage[key] = JSON.stringify(value);
}

function getItem(key) {
  const raw = storage[key];
  return raw ? JSON.parse(raw) : null;
}

// Save preferences
setItem('prefs', { theme: 'dark', fontSize: 16, notifications: true });

// Load preferences
const prefs = getItem('prefs');
console.log('Theme:', prefs.theme);     // 'dark'
console.log('Font:', prefs.fontSize);   // 16

// Non-existent key
const missing = getItem('nonexistent');
console.log('Missing key:', missing);   // null
```

---

## Part 4 — Search with `AbortController`

**Files:** `index.html` + `lab14.js`

**Learning objectives:** Cancel in-flight fetch requests; centralize error handling; combine with JSON and localStorage.

### Setup

Create folder `module14_lab/` with:

**`index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 14 Lab</title>
  <style>
    body { font-family: sans-serif; max-width: 700px; margin: 2rem auto; padding: 0 1rem; }
    h1, h2 { color: #333; }
    input[type="text"] { padding: 0.5rem; width: 300px; font-size: 1rem; }
    #results { margin-top: 1rem; }
    .result-item { padding: 0.5rem 0.75rem; border-bottom: 1px solid #eee; cursor: pointer; }
    .result-item:hover { background: #f5f5f5; }
    .loading { color: #888; font-style: italic; }
    .error   { color: #c00; }
    #saved { margin-top: 1.5rem; }
    #saved-list { list-style: none; padding: 0; }
    #saved-list li { padding: 0.4rem 0; border-bottom: 1px solid #eee;
                     display: flex; justify-content: space-between; }
    button { padding: 0.3rem 0.7rem; cursor: pointer; margin: 0.2rem; }
    #prefs-panel { background: #f8f8f8; border: 1px solid #ddd;
                   padding: 0.75rem; margin-top: 1rem; border-radius: 4px; }
  </style>
</head>
<body>
  <h1>Module 14: Async Patterns</h1>

  <h2>User Search</h2>
  <input type="text" id="search-input" placeholder="Search users by name…">
  <div id="results"></div>

  <h2>Saved Users</h2>
  <ul id="saved-list"></ul>
  <button id="clear-saved">Clear Saved</button>

  <h2>Preferences</h2>
  <div id="prefs-panel">
    <label>Theme:
      <select id="theme-select">
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </label>
    <button id="save-prefs">Save Preferences</button>
    <p id="prefs-status"></p>
  </div>

  <script src="lab14.js"></script>
</body>
</html>
```

**`lab14.js`**

```javascript
// --- Part 4: AbortController, centralized fetch, JSON + localStorage ---

const BASE = 'https://jsonplaceholder.typicode.com';

// 4.1 — Centralized fetch wrapper with response.ok check
async function apiFetch(url, options = {}) {
  const res = await fetch(url, options);
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${url}`);
  return res.json();
}

// 4.2 — AbortController: cancel previous search on new input
let activeController = null;

async function searchUsers(query) {
  const resultsEl = document.getElementById('results');

  if (!query.trim()) {
    resultsEl.innerHTML = '';
    return;
  }

  // Cancel any in-flight request
  if (activeController) activeController.abort();
  activeController = new AbortController();

  resultsEl.innerHTML = '<p class="loading">Searching…</p>';

  try {
    // JSONPlaceholder does not support real search — fetch all and filter client-side
    const users = await apiFetch(`${BASE}/users`, {
      signal: activeController.signal
    });

    const filtered = users.filter(u =>
      u.name.toLowerCase().includes(query.toLowerCase()) ||
      u.username.toLowerCase().includes(query.toLowerCase())
    );

    if (filtered.length === 0) {
      resultsEl.innerHTML = '<p>No users found.</p>';
      return;
    }

    resultsEl.innerHTML = '';
    filtered.forEach(user => {
      const div = document.createElement('div');
      div.classList.add('result-item');
      div.textContent = `${user.name} (@${user.username}) — ${user.email}`;
      div.dataset.userId = user.id;
      div.dataset.userName = user.name;
      div.addEventListener('click', () => saveUser(user));
      resultsEl.appendChild(div);
    });
  } catch (err) {
    if (err.name === 'AbortError') return;   // expected — newer search started
    resultsEl.innerHTML = `<p class="error">Search failed: ${err.message}</p>`;
  }
}

// Debounce: wait 300ms after last keystroke before searching
let debounceTimer = null;
document.getElementById('search-input').addEventListener('input', (e) => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => searchUsers(e.target.value), 300);
});
```

### Section 4.3 — Save Users with `localStorage`

```javascript
// 4.3 — Save and display users using localStorage + JSON
function getSavedUsers() {
  const raw = localStorage.getItem('savedUsers');
  return raw ? JSON.parse(raw) : [];
}

function saveUser(user) {
  const saved = getSavedUsers();
  if (saved.find(u => u.id === user.id)) {
    document.getElementById('prefs-status').textContent = `${user.name} already saved.`;
    return;
  }
  saved.push({ id: user.id, name: user.name, email: user.email });
  localStorage.setItem('savedUsers', JSON.stringify(saved));
  renderSaved();
}

function renderSaved() {
  const list = document.getElementById('saved-list');
  const saved = getSavedUsers();
  list.innerHTML = '';

  if (saved.length === 0) {
    list.innerHTML = '<li>No saved users.</li>';
    return;
  }

  saved.forEach(user => {
    const li = document.createElement('li');
    li.innerHTML = `<span>${user.name} — ${user.email}</span>`;

    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Remove';
    removeBtn.addEventListener('click', () => {
      const updated = getSavedUsers().filter(u => u.id !== user.id);
      localStorage.setItem('savedUsers', JSON.stringify(updated));
      renderSaved();
    });

    li.appendChild(removeBtn);
    list.appendChild(li);
  });
}

document.getElementById('clear-saved').addEventListener('click', () => {
  localStorage.removeItem('savedUsers');
  renderSaved();
});

// Initialize saved list on load
renderSaved();
```

### Section 4.4 — Preferences with `localStorage`

```javascript
// 4.4 — Persist preferences with localStorage
function loadPrefs() {
  const raw = localStorage.getItem('labPrefs');
  return raw ? JSON.parse(raw) : { theme: 'light' };
}

function applyPrefs(prefs) {
  document.getElementById('theme-select').value = prefs.theme;
  document.body.style.background = prefs.theme === 'dark' ? '#1a1a1a' : '';
  document.body.style.color      = prefs.theme === 'dark' ? '#f0f0f0' : '';
}

document.getElementById('save-prefs').addEventListener('click', () => {
  const prefs = { theme: document.getElementById('theme-select').value };
  localStorage.setItem('labPrefs', JSON.stringify(prefs));
  applyPrefs(prefs);
  document.getElementById('prefs-status').textContent = 'Preferences saved.';
});

// Apply saved preferences on load
applyPrefs(loadPrefs());
```

Save both files. Open with Live Server. Test:

1. Type a name letter by letter — confirm only one network request fires per completed search (check Network tab: earlier requests are cancelled with `(canceled)` status)
2. Click a result to save it — confirm it appears in the Saved Users list
3. Reload the page — confirm saved users persist
4. Switch theme and save — confirm background toggles and survives reload

---

## Part 9 — Challenge Exercise

This section is **optional**. It extends the lab with advanced problems that apply Promise combinators, JSON, and async patterns in more demanding scenarios.

### Step 9.1 — Generic `apiFetch` with Timeout and Retry

Extend the `apiFetch` wrapper to support both a configurable timeout and automatic retry with exponential backoff — combining `AbortController`, `Promise.race`, and loop-based retry logic into a single production-grade utility:

```javascript
async function apiFetch(url, options = {}, { timeout = 5000, retries = 2 } = {}) {
  let lastError;

  for (let attempt = 0; attempt <= retries; attempt++) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    try {
      const res = await fetch(url, { ...options, signal: controller.signal });
      clearTimeout(timeoutId);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      clearTimeout(timeoutId);

      if (err.name === 'AbortError') {
        lastError = new Error(`Request timed out after ${timeout}ms`);
      } else {
        lastError = err;
      }

      if (attempt < retries) {
        const delay = Math.pow(2, attempt) * 300;
        await new Promise(r => setTimeout(r, delay));
      }
    }
  }

  throw lastError;
}
```

Test it with:

1. A valid URL and a timeout of 10000ms — should succeed on the first attempt.
2. A valid URL with a timeout of 1ms — should time out and retry twice before failing.
3. An invalid URL — should fail with an HTTP error after retries.

Log a message before each retry to confirm the backoff delays are increasing.

### Step 9.2 — Multi-Source Data Aggregation with `Promise.allSettled`

Simulate an analytics dashboard that loads data from five independent endpoints. Some may fail. Use `Promise.allSettled` to collect all available results and render what succeeded, while gracefully noting what failed:

```javascript
const endpoints = [
  { label: 'Users',        url: `${BASE}/users` },
  { label: 'Posts',        url: `${BASE}/posts?_limit=5` },
  { label: 'Comments',     url: `${BASE}/comments?_limit=5` },
  { label: 'Todos',        url: `${BASE}/todos?_limit=5` },
  { label: 'Bad Endpoint', url: `${BASE}/nonexistent` },
];

async function loadDashboard() {
  const promises = endpoints.map(ep =>
    apiFetch(ep.url).then(data => ({ label: ep.label, data }))
  );

  const results = await Promise.allSettled(promises);

  results.forEach(result => {
    if (result.status === 'fulfilled') {
      console.log(`✓ ${result.value.label}: ${result.value.data.length} items`);
    } else {
      console.warn(`✗ ${result.reason.message}`);
    }
  });
}

loadDashboard();
```

Observe in the console that 4 of 5 endpoints succeed and the bad endpoint logs a warning. Extend the function to render the successful results to the page and display an error count badge showing how many sources failed.

### Step 9.3 — JSON Schema Validator

Write a `validateSchema(data, schema)` function that validates a parsed JSON object against a simple schema definition. The schema specifies required fields and their expected types:

```javascript
const userSchema = {
  id:       'number',
  name:     'string',
  email:    'string',
  active:   'boolean',
};

function validateSchema(data, schema) {
  const errors = [];

  for (const [key, expectedType] of Object.entries(schema)) {
    if (!(key in data)) {
      errors.push(`Missing required field: "${key}"`);
    } else if (typeof data[key] !== expectedType) {
      errors.push(`Field "${key}": expected ${expectedType}, got ${typeof data[key]}`);
    }
  }

  return { valid: errors.length === 0, errors };
}
```

Fetch a user from the API, run it through the validator, and log whether it conforms to the schema:

```javascript
async function validateUser(id) {
  const user = await apiFetch(`${BASE}/users/${id}`);
  const result = validateSchema(user, userSchema);

  if (result.valid) {
    console.log(`User ${id} is valid.`);
  } else {
    console.warn(`User ${id} has schema errors:`, result.errors);
  }
}

validateUser(1);
```

Then test the validator against a malformed object:

```javascript
const bad = { id: '1', name: 'Alice', email: null };
console.log(validateSchema(bad, userSchema));
// Should show errors for id (string not number), email (null is not string), and missing active
```

Extend the schema to support `nullable: true` on individual fields — allow the field to be either the expected type or `null`.

---

## Lab Completion Checklist

- [ ] Sequential run time ≈ sum of all delays; parallel ≈ slowest single delay
- [ ] `await` inside `for...of` loop confirmed as sequential (~500ms)
- [ ] `map + Promise.all` confirmed as parallel (~100ms)
- [ ] Sequential dependency example shows each step uses previous result
- [ ] `Promise.allSettled` returns all three results including the rejection
- [ ] `Promise.all` catches immediately on first rejection; others never logged
- [ ] `Promise.race` returns the fastest result (`'fast'`)
- [ ] `withTimeout` rejects when the delay exceeds the timeout
- [ ] `Promise.any` resolves with the first success despite earlier rejections
- [ ] `Promise.any` all-fail case produces `AggregateError`
- [ ] `JSON.stringify` drops functions and `undefined`; Date → ISO string; `Infinity` → `null`
- [ ] `JSON.parse` produces a plain object (Date remains a string)
- [ ] Simulated localStorage round-trip works for objects and returns `null` for missing keys
- [ ] Browser: search input triggers fetch; typing quickly shows canceled requests in Network tab
- [ ] Browser: clicking a result saves it; reload persists the saved list
- [ ] Browser: saving preferences applies theme and survives reload
