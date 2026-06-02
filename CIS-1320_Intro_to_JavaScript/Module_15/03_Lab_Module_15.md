# Lab Activity: Module 15 — Error Handling & Debugging

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

This lab has three parts:

- **Part 1** — Error types and `try/catch/finally` (Node.js)
- **Part 2** — Custom error classes and `throw` (Node.js)
- **Part 3** — Console debugging methods and Chrome DevTools (Browser)

**Lab environment:** VS Code + Node.js (Parts 1–2) and VS Code + Live Server + Chrome DevTools (Part 3).

---

## Part 1 — Error Types and `try/catch/finally`

**File:** `lab15_errors.js` — run with `node lab15_errors.js`

### 1.1 — Triggering and Identifying Error Types

Create `lab15_errors.js`. Each section below uses a function that deliberately causes an error. Your job is to catch each one and log its `name` and `message`.

```javascript
// Section 1.1 — Triggering and catching each error type

// --- ReferenceError ---
function triggerReference() {
  try {
    console.log(doesNotExist);
  } catch (err) {
    console.log('Caught:', err.name, '—', err.message);
  }
}

// --- TypeError ---
function triggerType() {
  try {
    null.toString();
  } catch (err) {
    console.log('Caught:', err.name, '—', err.message);
  }
}

// --- RangeError ---
function triggerRange() {
  try {
    new Array(-1);
  } catch (err) {
    console.log('Caught:', err.name, '—', err.message);
  }
}

// --- URIError ---
function triggerURI() {
  try {
    decodeURIComponent('%');
  } catch (err) {
    console.log('Caught:', err.name, '—', err.message);
  }
}

// --- SyntaxError via eval ---
function triggerSyntax() {
  try {
    eval('if (');
  } catch (err) {
    console.log('Caught:', err.name, '—', err.message);
  }
}

triggerReference();
triggerType();
triggerRange();
triggerURI();
triggerSyntax();
```

Run the file. You should see five lines, each identifying the error type and message.

**Checkpoint:** Confirm you see `ReferenceError`, `TypeError`, `RangeError`, `URIError`, and `SyntaxError` in your output.

---

### 1.2 — `instanceof` — Responding to Specific Error Types

Add this section to `lab15_errors.js`:

```javascript
// Section 1.2 — Handling specific error types with instanceof

function parseAndProcess(input) {
  try {
    if (typeof input !== 'string') throw new TypeError('Expected a string');
    const num = Number(input);
    if (isNaN(num)) throw new RangeError('Cannot convert to a valid number');
    if (num < 0 || num > 100) throw new RangeError('Number must be 0–100');
    return num * 2;
  } catch (err) {
    if (err instanceof TypeError) {
      console.log('Type problem:', err.message);
      return null;
    } else if (err instanceof RangeError) {
      console.log('Range problem:', err.message);
      return null;
    } else {
      throw err;   // unexpected — rethrow
    }
  }
}

console.log(parseAndProcess('42'));      // 84
console.log(parseAndProcess(99));        // Type problem: Expected a string → null
console.log(parseAndProcess('abc'));     // Range problem: Cannot convert to a valid number → null
console.log(parseAndProcess('150'));     // Range problem: Number must be 0–100 → null
```

**Checkpoint:** Confirm that each call produces the expected output and returns the right value.

---

### 1.3 — `finally` — Cleanup That Always Runs

Add this section:

```javascript
// Section 1.3 — finally always runs

function withCleanup(shouldFail) {
  console.log('--- withCleanup(' + shouldFail + ') ---');
  try {
    console.log('try block: executing');
    if (shouldFail) throw new Error('Deliberate failure');
    console.log('try block: succeeded');
    return 'success';
  } catch (err) {
    console.log('catch block:', err.message);
    return 'recovered';
  } finally {
    console.log('finally block: always runs');
  }
}

const r1 = withCleanup(false);
console.log('Result:', r1);
console.log();

const r2 = withCleanup(true);
console.log('Result:', r2);
```

**Expected output:**

```text
--- withCleanup(false) ---
try block: executing
try block: succeeded
finally block: always runs
Result: success

--- withCleanup(true) ---
try block: executing
catch block: Deliberate failure
finally block: always runs
Result: recovered
```

**Checkpoint:** Confirm `finally` appears in the output for both calls, including the path with no error.

---

### 1.4 — Rethrowing Unknown Errors

Add this section:

```javascript
// Section 1.4 — rethrowing errors you cannot handle

function processInput(value) {
  try {
    if (typeof value !== 'number') throw new TypeError('Expected a number');
    if (value < 0) throw new RangeError('Value cannot be negative');
    return Math.sqrt(value);
  } catch (err) {
    if (err instanceof TypeError || err instanceof RangeError) {
      console.log('Handled known error:', err.message);
      return NaN;
    }
    throw err;   // rethrow anything unexpected
  }
}

console.log(processInput(16));       // 4
console.log(processInput('hello'));  // Handled known error: Expected a number → NaN
console.log(processInput(-4));       // Handled known error: Value cannot be negative → NaN
```

**Checkpoint:** All three calls produce output without crashing. The rethrow path is tested by the lab — you will not see it trigger here because all inputs produce known errors.

---

## Part 2 — Custom Error Classes and `throw`

**File:** `lab15_custom.js` — run with `node lab15_custom.js`

### 2.1 — Defining Custom Error Classes

Create `lab15_custom.js`:

```javascript
// Custom error classes

class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

class NotFoundError extends Error {
  constructor(resource, id) {
    super(`${resource} with id "${id}" not found`);
    this.name = 'NotFoundError';
    this.resource = resource;
    this.id = id;
  }
}

class PermissionError extends Error {
  constructor(action) {
    super(`You do not have permission to: ${action}`);
    this.name = 'PermissionError';
    this.action = action;
  }
}

// Quick test — confirm properties
const ve = new ValidationError('Email is required', 'email');
console.log(ve.name);      // 'ValidationError'
console.log(ve.message);   // 'Email is required'
console.log(ve.field);     // 'email'
console.log(ve instanceof ValidationError);  // true
console.log(ve instanceof Error);            // true
```

**Checkpoint:** All five `console.log` lines produce the expected output. Confirm both `instanceof` checks are `true` — custom errors inherit from `Error`.

---

### 2.2 — Form Validation with Custom Errors

Add a simulated form validation workflow:

```javascript
// Section 2.2 — form validation with custom errors

function validateUser(user) {
  if (!user || typeof user !== 'object') {
    throw new TypeError('user must be an object');
  }
  if (!user.name || user.name.trim() === '') {
    throw new ValidationError('Name is required', 'name');
  }
  if (typeof user.age !== 'number' || user.age < 0 || user.age > 150) {
    throw new ValidationError('Age must be a number between 0 and 150', 'age');
  }
  if (!user.email || !user.email.includes('@')) {
    throw new ValidationError('A valid email address is required', 'email');
  }
  return true;
}

const testCases = [
  { name: 'Alice', age: 30, email: 'alice@example.com' },
  { name: '',      age: 30, email: 'bob@example.com' },
  { name: 'Carol', age: -5, email: 'carol@example.com' },
  { name: 'Dave',  age: 25, email: 'not-an-email' },
  null
];

testCases.forEach((input, i) => {
  try {
    const valid = validateUser(input);
    console.log(`Case ${i}: valid`);
  } catch (err) {
    if (err instanceof ValidationError) {
      console.log(`Case ${i}: ValidationError on field "${err.field}" — ${err.message}`);
    } else if (err instanceof TypeError) {
      console.log(`Case ${i}: TypeError — ${err.message}`);
    } else {
      throw err;
    }
  }
});
```

**Expected output:**

```text
Case 0: valid
Case 1: ValidationError on field "name" — Name is required
Case 2: ValidationError on field "age" — Age must be a number between 0 and 150
Case 3: ValidationError on field "email" — A valid email address is required
Case 4: TypeError — user must be an object
```

**Checkpoint:** All five cases produce the expected output. Notice that case 4 (null input) throws a `TypeError`, not a `ValidationError`, and the `instanceof` chain handles each differently.

---

### 2.3 — Simulated Data Store with `NotFoundError`

Add a simulated lookup:

```javascript
// Section 2.3 — simulated data store

const store = {
  users: [
    { id: 1, name: 'Alice', role: 'admin' },
    { id: 2, name: 'Bob',   role: 'editor' }
  ]
};

function getUser(id) {
  const user = store.users.find(u => u.id === id);
  if (!user) throw new NotFoundError('User', id);
  return user;
}

function deleteUser(id, requestingRole) {
  if (requestingRole !== 'admin') {
    throw new PermissionError('delete users');
  }
  const user = getUser(id);   // may throw NotFoundError
  store.users = store.users.filter(u => u.id !== id);
  return `Deleted user: ${user.name}`;
}

// Test cases
const ops = [
  () => getUser(1),
  () => getUser(99),
  () => deleteUser(2, 'admin'),
  () => deleteUser(1, 'editor'),
];

ops.forEach((op, i) => {
  try {
    const result = op();
    console.log(`Op ${i}:`, typeof result === 'object' ? result.name : result);
  } catch (err) {
    console.log(`Op ${i}: ${err.name} — ${err.message}`);
  }
});
```

**Expected output:**

```text
Op 0: Alice
Op 1: NotFoundError — User with id "99" not found
Op 2: Deleted user: Bob
Op 3: PermissionError — You do not have permission to: delete users
```

**Checkpoint:** Each operation throws or returns as expected. Notice that `NotFoundError` and `PermissionError` both have custom properties (`resource`, `id`, `action`) available on the caught error if you need them.

---

## Part 3 — Console Methods and Chrome DevTools

**Files:** `index.html` + `lab15_debug.js`

Create both files in a folder called `lab15_browser`.

### 3.1 — Project Setup

**`index.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lab 15 — Debugging</title>
  <style>
    body { font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }
    button { margin: 4px; padding: 8px 16px; cursor: pointer; }
    #output { margin-top: 20px; padding: 12px; background: #f4f4f4; border-radius: 4px;
               min-height: 60px; white-space: pre-wrap; font-family: monospace; font-size: 14px; }
    .error { color: red; }
  </style>
</head>
<body>
  <h1>Lab 15 — Debugging Tools</h1>
  <p>Open DevTools (F12) and watch the Console as you click each button.</p>

  <h2>Console Methods</h2>
  <button onclick="demoConsoleMethods()">Run console demos</button>
  <button onclick="demoTable()">console.table</button>
  <button onclick="demoTimer()">console.time</button>
  <button onclick="demoAssert()">console.assert</button>

  <h2>Error Handling</h2>
  <button onclick="demoTryCatch()">try/catch demo</button>
  <button onclick="demoCustomError()">Custom error</button>

  <h2>Breakpoints</h2>
  <button onclick="demoDebugger()">Run with debugger</button>

  <div id="output">Output will appear here...</div>

  <script src="lab15_debug.js"></script>
</body>
</html>
```

**`lab15_debug.js`:**

```javascript
const output = document.getElementById('output');

function print(msg, isError = false) {
  const line = document.createElement('div');
  line.textContent = msg;
  if (isError) line.classList.add('error');
  output.appendChild(line);
}

function clearOutput() {
  output.innerHTML = '';
}
```

Open with Live Server. Open DevTools (F12) before clicking any button.

---

### 3.2 — Console Methods Demo

Add to `lab15_debug.js`:

```javascript
function demoConsoleMethods() {
  clearOutput();
  print('Check the DevTools Console tab for styled output.');

  console.log('console.log — standard output');
  console.warn('console.warn — yellow warning');
  console.error('console.error — red error with stack trace');

  console.group('Grouped Output');
    console.log('This is inside a group');
    console.warn('A warning inside the group');
    console.log('Last item in group');
  console.groupEnd();

  console.log('Back to top level after groupEnd');
}

function demoTable() {
  clearOutput();
  print('Check the DevTools Console tab for a table.');

  const products = [
    { id: 1, name: 'Widget',  price: 9.99,  inStock: true },
    { id: 2, name: 'Gadget',  price: 24.99, inStock: false },
    { id: 3, name: 'Gizmo',   price: 14.99, inStock: true }
  ];

  console.table(products);
  // In DevTools, you will see a sortable grid with columns: id, name, price, inStock
}

function demoTimer() {
  clearOutput();
  print('Timing a sort operation — see Console for result.');

  const data = Array.from({ length: 10000 }, () => Math.random());

  console.time('sort-10000');
  data.sort((a, b) => a - b);
  console.timeEnd('sort-10000');   // 'sort-10000: X.XXXms'
}

function demoAssert() {
  clearOutput();
  print('Running assertions — see Console.');

  const value = 42;
  console.assert(value > 0,   'value should be positive');      // passes — no output
  console.assert(value < 10,  'value should be less than 10');  // fails — logs error
  console.assert(value === 42, 'value should equal 42');         // passes — no output
}
```

Click each button with DevTools open. In the Console:

- Notice `warn` has a yellow background, `error` has a red background.
- `console.group` creates a collapsible section — click the triangle to collapse it.
- `console.table` renders the products array as a grid with column headers.
- `console.time`/`timeEnd` prints the elapsed time in milliseconds.
- `console.assert` only prints when the condition is `false`.

**Checkpoint:** You have seen all five console method types. Confirm `console.assert` produces output only for the middle assertion.

---

### 3.3 — Error Handling in the Browser

Add to `lab15_debug.js`:

```javascript
function demoTryCatch() {
  clearOutput();

  function safeDivide(a, b) {
    try {
      if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
      }
      if (b === 0) throw new RangeError('Division by zero');
      return a / b;
    } catch (err) {
      console.error(err.name + ':', err.message);
      return null;
    } finally {
      console.log('safeDivide() completed');
    }
  }

  const results = [
    safeDivide(10, 2),
    safeDivide(10, 0),
    safeDivide('ten', 2)
  ];

  results.forEach((r, i) => {
    print(`Result ${i}: ${r}`);
  });
}

class AppValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'AppValidationError';
    this.field = field;
  }
}

function demoCustomError() {
  clearOutput();

  function validateUsername(name) {
    if (typeof name !== 'string') throw new TypeError('Username must be a string');
    if (name.trim().length < 3) throw new AppValidationError('Username must be at least 3 characters', 'username');
    if (name.includes(' ')) throw new AppValidationError('Username cannot contain spaces', 'username');
    return name.trim().toLowerCase();
  }

  const inputs = ['alice', 'ab', 'hello world', 42];
  inputs.forEach(input => {
    try {
      const result = validateUsername(input);
      print('Valid username: ' + result);
    } catch (err) {
      if (err instanceof AppValidationError) {
        print('Validation (' + err.field + '): ' + err.message, true);
      } else {
        print('Error (' + err.name + '): ' + err.message, true);
      }
    }
  });
}
```

Click each button and observe the output in both the page and DevTools Console.

**Checkpoint:** `demoTryCatch` shows results 5, null, null on the page. `demoCustomError` shows one valid result and three errors, with the last one identified as a `TypeError` rather than `AppValidationError`.

---

### 3.4 — Breakpoints and the `debugger` Statement

Add to `lab15_debug.js`:

```javascript
function demoDebugger() {
  clearOutput();
  print('Check the DevTools Sources tab — execution paused on debugger statement.');

  const orders = [
    { id: 'A1', items: [{ name: 'Widget', price: 9.99 }, { name: 'Gadget', price: 24.99 }] },
    { id: 'A2', items: [{ name: 'Gizmo', price: 14.99 }] },
    { id: 'A3', items: [] }
  ];

  function calculateOrderTotal(order) {
    debugger;   // execution pauses here when DevTools is open
    return order.items.reduce((total, item) => total + item.price, 0);
  }

  orders.forEach(order => {
    const total = calculateOrderTotal(order);
    print(`Order ${order.id}: $${total.toFixed(2)}`);
  });
}
```

**Debugging exercise:**

1. Make sure DevTools is open on the Sources tab.
2. Click **Run with debugger**.
3. Execution pauses at the `debugger` line.
4. In the **Scope** panel on the right, find `order` — expand it to see the `id` and `items` properties.
5. In the **Call Stack** panel, you will see `calculateOrderTotal` called from the anonymous function inside `forEach`.
6. Press **F10** (Step Over) to execute `return order.items.reduce(...)` and return to the `forEach` callback.
7. Press **F8** (Resume) to continue to the next call of `calculateOrderTotal` (for order A2).
8. Press **F8** two more times to complete all three orders.
9. The page now shows three totals.

**Setting a manual breakpoint (alternative exercise):**

1. Remove the `debugger` statement from `calculateOrderTotal`.
2. In DevTools → Sources, find `lab15_debug.js`.
3. Click on the line number for `return order.items.reduce(...)` to set a blue breakpoint marker.
4. Click the button again — execution pauses at the breakpoint you set.
5. Step through as before.

**Checkpoint:** You have used both a `debugger` statement and a manual breakpoint to pause execution inside a running function. You have inspected the `order` variable in the Scope panel.

---

## Summary

| Concept | Key Point |
|---|---|
| Error types | Six built-in types; `name` identifies which |
| `try/catch/finally` | `catch` runs on throw; `finally` always runs |
| `throw` | Throw `Error` objects, not primitives |
| Custom errors | `extends Error`; call `super(message)`; set `this.name` |
| `instanceof` | Works for both built-in and custom error classes |
| Rethrowing | Rethrow errors you cannot specifically handle |
| `console.table` | Renders arrays of objects as a grid |
| `console.group` | Groups related log output into collapsible sections |
| `console.time` | Measures elapsed time to the millisecond |
| `console.assert` | Logs an error only if condition is false |
| Breakpoints | Pause execution; inspect Scope and Call Stack |
| `debugger` | Programmatic breakpoint; remove before production |
