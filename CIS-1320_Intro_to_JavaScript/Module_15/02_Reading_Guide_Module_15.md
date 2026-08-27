# Reading Guide: Module 15 — Error Handling & Debugging

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Every JavaScript program will eventually encounter unexpected conditions: invalid input, missing data, failed network requests, or programming mistakes. Module 15 covers two essential skills for professional JavaScript development: structured error handling (writing code that catches and responds to failures gracefully) and effective debugging (using tools to find and fix problems efficiently). Both skills are tested on the JSE certification exam.

---

## 1. JavaScript's Built-In Error Types

When JavaScript encounters a condition it cannot handle, it creates an `Error` object and throws it. The built-in error types each represent a distinct category of problem.

| Error Type | When It Occurs | Example |
|---|---|---|
| `SyntaxError` | Code is malformed and cannot be parsed | `eval('if (')` |
| `ReferenceError` | Variable used before declaration or out of scope | `console.log(x)` where `x` is not declared |
| `TypeError` | Operation is invalid for the value's type | `null.toString()`, calling a non-function |
| `RangeError` | Numeric value is outside its legal range | `new Array(-1)`, `(1).toFixed(200)` |
| `URIError` | Malformed URI string | `decodeURIComponent('%')` |
| `EvalError` | Misuse of `eval()` (rarely thrown in modern engines) | Historical; know the name |

`SyntaxError` is unique — it prevents the script from running at all. The other types are thrown at runtime and can be caught with `try/catch`.

### Error Object Properties

Every error object provides three properties:

```javascript
try {
  null.toString();
} catch (err) {
  console.log(err.name);    // 'TypeError'
  console.log(err.message); // 'Cannot read properties of null (reading 'toString')'
  console.log(err.stack);   // Multi-line string: error + call stack trace
}
```

- `name` — the error type as a string (`'TypeError'`, `'RangeError'`, etc.)
- `message` — a human-readable description
- `stack` — a string with the error message and the full call stack at the time of the throw (non-standard but universally supported)

---

## 2. `try / catch / finally`

The `try` statement is the primary mechanism for handling errors at runtime.

```javascript
try {
  // code that might throw
} catch (err) {
  // runs only if something threw; err is the thrown value
} finally {
  // runs always — whether or not an error occurred
}
```

### Key Behaviors

- The `catch` block only runs if something throws inside `try`.
- The `finally` block always runs — even if `catch` has a `return` statement, `finally` executes before the function returns.
- `catch` and `finally` are both optional, but at least one must be present.
- If `finally` contains a `return`, it overrides any `return` in `try` or `catch`.

```javascript
function readData() {
  try {
    return 'data';
  } finally {
    console.log('cleanup');   // always runs
  }
}

readData();   // logs 'cleanup', returns 'data'
```

### Omitting `catch`

```javascript
try {
  riskyOperation();
} finally {
  releaseResource();   // cleanup without handling the error
}
```

`try/finally` without `catch` lets the error propagate to the caller while still guaranteeing cleanup.

---

## 3. `throw`

The `throw` statement raises an error manually. You can throw any value, but always throw an `Error` object or a subclass.

```javascript
// Correct — throw Error objects
throw new Error('Something went wrong');
throw new TypeError('Expected a string, received: ' + typeof value);
throw new RangeError('Page number must be between 1 and ' + maxPage);

// Avoid — thrown primitives lack name, message, and stack
throw 'oops';    // string — no useful properties
throw 42;        // number — no useful properties
```

### Rethrowing

Catch only errors you can handle. If an error is unexpected, rethrow it:

```javascript
try {
  processData(input);
} catch (err) {
  if (err instanceof ValidationError) {
    showUserMessage(err.message);   // known — handle it
  } else {
    throw err;   // unknown — let it propagate
  }
}
```

Silently catching every error (`catch (err) { }`) hides bugs. Always rethrow what you cannot specifically handle.

---

## 4. Custom Error Classes

For application-specific errors, extend the built-in `Error` class:

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);              // sets this.message
    this.name = 'ValidationError';
    this.field = field;          // custom property
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

Two requirements:

1. Call `super(message)` first — this initializes `this.message` and the stack trace.
2. Set `this.name` explicitly — without it, `err.name` defaults to `'Error'`, losing the distinction.

### Using Custom Errors

```javascript
function validateAge(age) {
  if (typeof age !== 'number') {
    throw new ValidationError('Age must be a number', 'age');
  }
  if (age < 0 || age > 150) {
    throw new ValidationError('Age must be between 0 and 150', 'age');
  }
}

try {
  validateAge('twenty');
} catch (err) {
  if (err instanceof ValidationError) {
    console.error(`Field "${err.field}": ${err.message}`);
  } else {
    throw err;
  }
}
```

`instanceof` works with custom error classes the same way it works with `TypeError` and `RangeError`.

---

## 5. `console` Methods for Debugging

The `console` object provides output methods beyond `log`:

| Method | Output Style | Use For |
|---|---|---|
| `console.log(...)` | Standard | General output during development |
| `console.warn(...)` | Yellow warning | Non-fatal issues worth noting |
| `console.error(...)` | Red error + stack trace | Errors and unexpected states |
| `console.table(arrayOfObjects)` | Formatted table grid | Inspecting arrays of objects |
| `console.group(label)` | Expandable group start | Grouping related log output |
| `console.groupEnd()` | Group end | Closes the current group |
| `console.time(label)` | Timer start (no output) | Measuring elapsed time |
| `console.timeEnd(label)` | Prints elapsed ms | Ends the named timer |
| `console.assert(condition, msg)` | Error if condition false | Sanity checks in development |

```javascript
// console.table
const users = [
  { name: 'Alice', role: 'admin' },
  { name: 'Bob',   role: 'editor' }
];
console.table(users);   // renders as a sortable grid in DevTools

// console.group
console.group('Validation');
  console.log('Checking name...');
  console.warn('Email is missing');
console.groupEnd();

// console.time
console.time('sort');
data.sort((a, b) => a.value - b.value);
console.timeEnd('sort');   // 'sort: 0.234ms'

// console.assert
console.assert(items.length > 0, 'Expected items to be non-empty');
```

---

## 6. Chrome DevTools — Sources Panel and Breakpoints

The Sources panel in Chrome DevTools lets you pause execution and inspect program state.

### Setting a Breakpoint

1. Open DevTools (F12 or Ctrl+Shift+I).
2. Click the **Sources** tab.
3. Open your JavaScript file from the file tree on the left.
4. Click a line number in the gutter — a blue marker appears.
5. Trigger the code (reload the page, click a button, etc.).
6. Execution pauses at the breakpoint.

### Debugger Panels

When paused, three panels appear on the right:

- **Scope** — all variables in the current and enclosing scopes with live values
- **Call Stack** — the chain of function calls that led to this line
- **Watch** — expressions you add manually; evaluated every time execution pauses

### Stepping Controls

| Button | Shortcut | Action |
|---|---|---|
| Resume | F8 | Continue to next breakpoint or end |
| Step Over | F10 | Execute current line, stay in current function |
| Step Into | F11 | Enter the function called on this line |
| Step Out | Shift+F11 | Complete current function, return to caller |

### The `debugger` Statement

```javascript
function processOrder(order) {
  debugger;   // pauses here when DevTools is open
  return order.items.reduce((total, item) => total + item.price, 0);
}
```

`debugger` is a programmatic breakpoint. It only activates when DevTools is open. Remove it before deploying — it pauses execution for all users if left in production code.

---

## 7. Common Bugs and Defensive Patterns

### Null/Undefined Property Access

```javascript
const user = null;

// Throws: TypeError: Cannot read properties of null
user.name;

// Safe: optional chaining
const name = user?.name;             // undefined
const city = user?.address?.city;    // undefined
```

Optional chaining (`?.`) short-circuits to `undefined` if the left-hand side is `null` or `undefined`.

### Type Coercion Surprises

```javascript
'5' + 3       // '53'  — + with a string concatenates
'5' - 3       // 2     — - coerces string to number
0 == ''       // true  — loose equality, both coerce to falsy
0 === ''      // false — strict equality, different types
null == undefined   // true  — special case
null === undefined  // false
```

Use `===` by default. Reserve `==` only for the deliberate `null == undefined` check.

### Forgotten `await`

```javascript
// Missing await — result is a Promise, not the data
async function load() {
  const data = fetch('/api/items');   // forgot await
  console.log(data.length);           // TypeError
}

// Correct
async function load() {
  const data = await fetch('/api/items');
  const json = await data.json();
  console.log(json.length);
}
```

### Guard Clauses — Validate at Entry

```javascript
function processOrder(order) {
  if (!order) throw new TypeError('order is required');
  if (!Array.isArray(order.items)) throw new TypeError('order.items must be an array');

  return order.items.reduce((total, item) => total + item.price, 0);
}
```

Guard clauses at the top of functions catch invalid input immediately with a clear message, rather than failing unpredictably inside the function body.

---

## 8. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[MDN Web Docs — Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)**
  Complete reference for the `Error` constructor, the six built-in error types (`SyntaxError`, `ReferenceError`, `TypeError`, `RangeError`, `URIError`, `EvalError`), the `name`/`message`/`stack` properties, and creating custom error classes with `extends Error`.

- **[MDN Web Docs — try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)**
  Full reference for the `try/catch/finally` statement. Covers `catch` binding, optional `catch` binding (ES2019), `finally` execution guarantees, and interaction between `return` and `finally`.

- **[javascript.info — Error handling, "try...catch"](https://javascript.info/try-catch)**
  Clear walkthrough of the try/catch/finally mechanics, the error object, rethrowing, and custom error classes. Includes exercises on building a validation error hierarchy with `instanceof` dispatch.

- **[Chrome Developers — Debug JavaScript](https://developer.chrome.com/docs/devtools/javascript/)**
  Official Google guide to debugging JavaScript in Chrome DevTools. Covers setting line breakpoints, conditional breakpoints, logpoints, stepping controls, the Scope and Watch panels, and the Call Stack.

- **[MDN Web Docs — console](https://developer.mozilla.org/en-US/docs/Web/API/console)**
  Complete reference for all `console` methods — `log`, `warn`, `error`, `table`, `group`/`groupEnd`, `time`/`timeEnd`, `assert`, `count`, `dir`, `trace`. Includes browser compatibility and styling with `%c`.

---

## 9. JSE Certification Exam Tips

1. **Know all six error types** — `SyntaxError`, `ReferenceError`, `TypeError`, `RangeError`, `URIError`, `EvalError`. Know which situation triggers each.

2. **`finally` always runs** — even if `try` returns, `finally` executes before the function returns. If `finally` also returns, its return value wins.

3. **`throw` can throw any value** — but throwing an `Error` instance is the correct practice. Thrown strings have no `name`, `message`, or `stack`.

4. **Custom errors require `super(message)` and `this.name`** — without `this.name = 'MyError'`, the name defaults to `'Error'`.

5. **`instanceof` works for custom errors** — `err instanceof ValidationError` works exactly like `err instanceof TypeError`.

6. **Rethrowing** — always rethrow errors you cannot specifically handle. Silent `catch` hides bugs.

7. **`SyntaxError` cannot be caught by `try/catch` in your script** — it prevents the script from parsing. It can only be caught around `eval()` calls.

8. **`console.error` does not throw** — it logs styled output. It does not stop execution.

9. **`debugger` requires DevTools to be open** — in a running application without DevTools, `debugger` is silently ignored.

10. **Optional chaining** (`?.`) does not suppress all TypeErrors — only those from null/undefined property access on the left side.

---

## 10. Study Checklist

- [ ] Watch the Module 15 video lecture by Professor Nash.
- [ ] Read [MDN — Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error).
- [ ] Read [MDN — try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch).
- [ ] Trigger each of the six error types in the DevTools console.
- [ ] Write a `try/catch/finally` block — confirm `finally` runs in both the error and no-error paths.
- [ ] Write a custom error class — confirm `instanceof` identifies it correctly.
- [ ] Use `console.table` on an array of objects.
- [ ] Set a breakpoint in the Sources panel and step through code.
- [ ] Use the `debugger` statement and confirm it pauses execution.
- [ ] Complete the Module 15 Lab.
- [ ] Complete the Module 15 Quiz.
