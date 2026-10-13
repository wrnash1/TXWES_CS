# Video Script: CIS-1320 — Introduction to JavaScript

## Module 15 — Error Handling & Debugging

**Estimated Duration:** 20–24 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Chrome DevTools (Console + Sources tabs) for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - This module covers two distinct but related skills: error handling in code (try/catch/throw/custom errors) and debugging tools (DevTools, console methods, debugger statement).
> - For the DevTools demo, use a simple browser page — the lab's `index.html` works well. Show the Sources panel with an actual breakpoint so students see the debugger in a real context.
> - The JSE exam tests: error type names and when each occurs, try/catch/finally behavior, throw mechanics, and custom Error subclasses.
> - `console.table` and `console.group` are genuinely useful — show real examples, not trivial ones.
> - Do NOT spend time on `window.onerror` or `process.on('uncaughtException')` — those are out of scope for JSE.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 15 | Error Handling & Debugging | CIS-1320"]**

"Every program encounters unexpected conditions. A network request fails. A user passes the wrong type of value. A property is accessed on `undefined`. Module 15 is about two complementary skills: writing code that handles errors gracefully, so your application can recover rather than crash, and using debugging tools effectively, so you can find and fix problems quickly.

By the end of this module, you will know JavaScript's built-in error types, how to catch and throw errors with `try/catch/finally`, how to create custom error classes, and how to use Chrome DevTools and `console` methods to diagnose problems in running code. These skills apply to every project from this point forward."

---

## [01:30 – 05:30] Part 1 — JavaScript Error Types

**[SHOW SLIDE: "JavaScript Built-In Error Types"]**

"When JavaScript encounters a problem it cannot resolve, it throws an error. The error is an object — an instance of one of the built-in error classes. There are six you need to know for the JSE exam.

**[DEMO — open Chrome DevTools Console]**

`SyntaxError` — the code itself is malformed. The engine cannot even parse it.

```javascript
// SyntaxError — not caught by try/catch; prevents the script from running
// eval can demonstrate it:
try {
  eval('if (');
} catch (err) {
  console.log(err.name);    // 'SyntaxError'
  console.log(err.message); // 'Unexpected end of input' (varies by engine)
}
```

SyntaxErrors in your actual script files halt execution before any code runs. You see them in the console before any output appears.

[PAUSE]

`ReferenceError` — you tried to use a variable that does not exist.

```javascript
try {
  console.log(undeclaredVariable);
} catch (err) {
  console.log(err.name);    // 'ReferenceError'
  console.log(err.message); // 'undeclaredVariable is not defined'
}
```

[PAUSE]

`TypeError` — the operation is not valid for the type of value you have.

```javascript
try {
  null.toUpperCase();
} catch (err) {
  console.log(err.name);    // 'TypeError'
  console.log(err.message); // "Cannot read properties of null"
}

try {
  const num = 42;
  num();   // calling a non-function
} catch (err) {
  console.log(err.name);    // 'TypeError'
}
```

TypeError is the most common error you will encounter in real applications.

[PAUSE]

`RangeError` — a numeric value is outside the valid range.

```javascript
try {
  const arr = new Array(-1);
} catch (err) {
  console.log(err.name);    // 'RangeError'
  console.log(err.message); // 'Invalid array length'
}

try {
  (1234).toFixed(200);   // toFixed accepts 0–100
} catch (err) {
  console.log(err.name);    // 'RangeError'
}
```

[PAUSE]

`URIError` — malformed URI string passed to `decodeURIComponent` or similar functions.

```javascript
try {
  decodeURIComponent('%');
} catch (err) {
  console.log(err.name);   // 'URIError'
}
```

`EvalError` — historically from `eval()` misuse. Rarely seen in practice but listed in the specification. Know the name.

[PAUSE]

**Every error object has three key properties:**

```javascript
try {
  null.toString();
} catch (err) {
  console.log(err.name);    // 'TypeError'
  console.log(err.message); // 'Cannot read properties of null'
  console.log(err.stack);   // Full stack trace as a string
}
```

`name` identifies the error type. `message` describes what went wrong. `stack` is a multi-line string showing the call stack at the moment the error was thrown — invaluable for debugging."

---

## [05:30 – 10:00] Part 2 — `try/catch/finally` and `throw`

**[SHOW SLIDE: "try / catch / finally"]**

"The `try` block contains code that might throw. The `catch` block runs only if something throws. The `finally` block runs always — whether an error occurred or not.

**[DEMO]**

```javascript
function divide(a, b) {
  try {
    if (b === 0) throw new Error('Division by zero');
    return a / b;
  } catch (err) {
    console.error('Caught:', err.message);
    return null;
  } finally {
    console.log('divide() completed');   // runs whether or not there was an error
  }
}

console.log(divide(10, 2));  // logs 'divide() completed', returns 5
console.log(divide(10, 0));  // logs 'Caught: Division by zero', logs 'divide() completed', returns null
```

`finally` always runs. Even if the `catch` block has a `return`, `finally` still executes before the function returns. Use `finally` for cleanup that must happen regardless of outcome — closing a connection, hiding a loading spinner, releasing a lock.

[PAUSE]

**Throwing errors:**

```javascript
throw new Error('Something went wrong');
throw new TypeError('Expected a string');
throw new RangeError('Value must be between 0 and 100');
```

You can throw any value — a string, a number — but always prefer `new Error(message)` or a subclass. Error objects give you `.name`, `.message`, and `.stack`. A thrown string gives you nothing useful.

[PAUSE]

**Rethrowing — when you can handle it, handle it; when you cannot, rethrow:**

```javascript
async function loadUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    if (err.name === 'AbortError') return null;   // expected — handle it
    throw err;   // unexpected — let the caller deal with it
  }
}
```

Catching every error and silently swallowing it is a common mistake. If you do not know how to handle an error, rethrow it.

[PAUSE]

**Checking error type in catch:**

```javascript
try {
  someOperation();
} catch (err) {
  if (err instanceof TypeError) {
    console.error('Type problem:', err.message);
  } else if (err instanceof RangeError) {
    console.error('Range problem:', err.message);
  } else {
    throw err;   // unexpected type — rethrow
  }
}
```

Use `instanceof` to check the class of the error, or `err.name` to check the name string."

---

## [10:00 – 13:00] Part 3 — Custom Error Classes

**[SHOW SLIDE: "Custom Error Classes"]**

"When you build a real application, you often need to distinguish your own errors from JavaScript's built-in ones. The standard approach is to extend the `Error` class.

**[DEMO]**

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);          // sets this.message
    this.name = 'ValidationError';
    this.field = field;
  }
}

class NotFoundError extends Error {
  constructor(resource, id) {
    super(`${resource} with id ${id} not found`);
    this.name = 'NotFoundError';
    this.resource = resource;
    this.id = id;
  }
}
```

Two steps are required: call `super(message)` to initialize the base Error, and then set `this.name` to your class's name. Without `this.name = 'ValidationError'`, the name will default to `'Error'`.

[PAUSE]

```javascript
function validateAge(age) {
  if (typeof age !== 'number') {
    throw new ValidationError('Age must be a number', 'age');
  }
  if (age < 0 || age > 150) {
    throw new ValidationError('Age must be between 0 and 150', 'age');
  }
  return true;
}

try {
  validateAge('twenty');
} catch (err) {
  if (err instanceof ValidationError) {
    console.log(`Validation failed on field: ${err.field}`);
    console.log(err.message);
  } else {
    throw err;
  }
}
```

Custom errors let callers use `instanceof` to respond specifically to your errors versus unexpected system errors. This is the same pattern used in mature libraries and frameworks."

---

## [13:00 – 17:30] Part 4 — Console Methods and DevTools

**[SHOW SLIDE: "Console and Debugging Tools"]**

"The `console` object has more than just `log`. Knowing all of its methods makes debugging significantly more efficient.

**[DEMO — Chrome DevTools Console]**

```javascript
console.log('Standard output');
console.warn('This will be yellow — a warning');
console.error('This will be red — an error');
```

`warn` and `error` are styled differently in DevTools. `error` also produces a stack trace in the console.

[PAUSE]

```javascript
const users = [
  { name: 'Alice', age: 30, role: 'admin' },
  { name: 'Bob',   age: 25, role: 'editor' },
  { name: 'Carol', age: 28, role: 'viewer' }
];

console.table(users);   // renders as a formatted table in DevTools
```

`console.table` is extremely useful for arrays of objects. Scrolling through `console.log` output for 50 objects is miserable; `console.table` puts them in a sortable grid.

[PAUSE]

```javascript
console.group('User Processing');
  console.log('Starting validation...');
  console.warn('Age field missing for user 2');
  console.log('Validation complete');
console.groupEnd();

console.time('sort-operation');
const sorted = users.slice().sort((a, b) => a.age - b.age);
console.timeEnd('sort-operation');   // logs: 'sort-operation: 0.123ms'
```

`console.group` / `console.groupEnd` creates an expandable/collapsible group in the console — useful for grouping related output. `console.time` / `console.timeEnd` measures elapsed time precisely.

[PAUSE]

```javascript
const value = 42;
console.assert(value > 100, 'Expected value to be > 100, got:', value);
// logs an assertion error to the console if the condition is false
// nothing is logged if the condition is true
```

`console.assert` is useful for quick sanity checks during development. It logs an error with your message if the condition is false, and does nothing if it is true.

[PAUSE]

**[SWITCH TO SOURCES PANEL — DevTools]**

Now let me show you the Sources panel. This is where you use breakpoints to pause execution and inspect the program state step by step.

Open DevTools → Sources tab. You will see your JavaScript files listed on the left. Click a file name to open it. Click the line number in the gutter to set a breakpoint — a blue marker appears.

When the browser runs code that hits the breakpoint, execution pauses. The current line is highlighted. On the right panel, you see:

- **Scope** — all variables currently in scope with their values
- **Call Stack** — the chain of function calls that got you here
- **Watch** — expressions you want to monitor

The toolbar buttons:

- **Resume** (F8) — continue to the next breakpoint or end
- **Step Over** (F10) — run the current line, stay at the same level
- **Step Into** (F11) — enter the function being called on this line
- **Step Out** (Shift+F11) — finish the current function, return to caller

[PAUSE]

**The `debugger` statement:**

```javascript
function calculateTotal(items) {
  debugger;   // execution pauses here when DevTools is open
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

The `debugger` statement triggers a breakpoint programmatically. It only has an effect when DevTools is open. Remove it before shipping to production — it will pause all users' browsers if left in.

Use `debugger` when you want to pause at a specific point without clicking through the Sources panel, or when the line number is in generated code that is hard to find."

---

## [17:30 – 20:30] Part 5 — Common Bugs and Defensive Patterns

**[SHOW SLIDE: "Common Bugs and Defensive Code"]**

"Let me walk through the bugs you will encounter most often.

**[DEMO]**

**Accessing a property on `undefined` or `null`:**

```javascript
const user = null;

// This throws TypeError
user.name;

// Defensive: optional chaining
const name = user?.name;         // undefined — no error
const city = user?.address?.city; // undefined — no error

// Defensive: check before use
if (user) {
  console.log(user.name);
}
```

Optional chaining (`?.`) short-circuits to `undefined` if the left side is null or undefined. It does not silence all TypeErrors — only those from null/undefined property access.

[PAUSE]

**Type coercion surprises:**

```javascript
console.log('5' + 3);    // '53'  — string concatenation, not addition
console.log('5' - 3);    // 2     — arithmetic coerces string to number
console.log(0 == '');    // true  — loose equality, both coerce to 0
console.log(0 === '');   // false — strict equality, different types
console.log(null == undefined);  // true  — special case in ==
console.log(null === undefined); // false
```

Use `===` by default. `==` with mixed types produces surprises like these.

[PAUSE]

**Forgetting `await`:**

```javascript
async function loadData() {
  const data = fetch('/api/items');   // forgot await — data is a Promise
  console.log(data.length);           // TypeError: Promise has no .length
}
```

If you are getting `[object Promise]` in your output or `undefined` where you expect data, you most likely forgot `await`.

[PAUSE]

**`parseInt` with missing radix:**

```javascript
parseInt('08');    // might be 0 in older engines (octal interpretation)
parseInt('08', 10); // always 8 — always provide the radix
```

Always pass `10` as the second argument to `parseInt`. Without it, the behavior for strings starting with `0` is engine-dependent in old code.

[PAUSE]

**Defensive guard clauses — validate at function entry:**

```javascript
function processOrder(order) {
  if (!order) throw new TypeError('order is required');
  if (typeof order.id !== 'number') throw new TypeError('order.id must be a number');
  if (!Array.isArray(order.items)) throw new TypeError('order.items must be an array');

  // now safe to proceed
  return order.items.reduce((total, item) => total + item.price, 0);
}
```

Guard clauses at the top of a function make expectations explicit and fail fast with a clear message rather than throwing a confusing error three function calls later."

---

## [20:30 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 15 Lab Preview"]**

"The Module 15 lab has three parts.

Part 1 covers error types and try/catch — you will trigger each built-in error type deliberately, practice catching them by type with `instanceof`, and build a rethrowing pattern.

Part 2 covers custom errors — you will implement `ValidationError` and `NotFoundError` classes and use them in a simulated form validation workflow.

Part 3 covers debugging — you will use `console.table`, `console.group`, `console.time`, and the `debugger` statement, then step through code in Chrome DevTools using breakpoints.

The quiz tests error type identification, try/catch/finally behavior, throw mechanics, custom Error subclasses, and console methods. Read the guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 15 — Error Handling & Debugging]**

---

## Additional Resources

- [MDN — Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [MDN — try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
- [MDN — throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
- [MDN — console](https://developer.mozilla.org/en-US/docs/Web/API/console)
- [Chrome DevTools — JavaScript Debugging](https://developer.chrome.com/docs/devtools/javascript/)
- [Eloquent JavaScript — Chapter 8: Bugs and Errors](https://eloquentjavascript.net/08_error.html)
