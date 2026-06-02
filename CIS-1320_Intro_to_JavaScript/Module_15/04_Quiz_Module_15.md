# Quiz: Module 15 — Error Handling & Debugging

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

Which error type is thrown when you try to access a property on `null`?

- A) `ReferenceError`
- B) `RangeError`
- C) `TypeError`
- D) `SyntaxError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `ReferenceError` occurs when a variable name is used that has never been declared — for example, `console.log(x)` where `x` does not exist. Accessing a property on `null` is not a naming problem; it is a type problem.
- *Why B is incorrect:* `RangeError` occurs when a numeric value is outside its legal range — for example, `new Array(-1)`. Null property access is not a range issue.
- *Why C is correct:* `null` has no properties. When you write `null.toString()` or `null.name`, JavaScript throws a `TypeError` because the operation (property access) is not valid for the type of value (null). The message will be "Cannot read properties of null".
- *Why D is incorrect:* `SyntaxError` occurs when the code is structurally malformed and cannot be parsed by the JavaScript engine. This error is thrown before any code executes. Accessing a property on `null` is a runtime error, not a syntax error.

---

### Question 2

What does the `finally` block guarantee?

```javascript
function load() {
  try {
    return 'data';
  } catch (err) {
    return 'error';
  } finally {
    console.log('done');
  }
}
load();
```

- A) `'done'` is logged only if no error is thrown
- B) `'done'` is logged only if an error is thrown
- C) `'done'` is logged regardless of whether an error was thrown
- D) `'done'` is never logged because `try` returns before `finally` runs

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `finally` is not conditional on success. It runs even when the `try` block succeeds.
- *Why B is incorrect:* `finally` is not a second `catch`. It does not run only on failure.
- *Why C is correct:* `finally` always executes — whether `try` completes normally, whether `catch` runs, or whether either block uses `return`. The `return 'data'` in `try` does not skip `finally`. `'done'` is logged on every call to `load()`, and then the function returns its value.
- *Why D is incorrect:* `return` in `try` does not prevent `finally` from executing. The `finally` block runs before the function actually returns. This is one of JavaScript's guarantees for `finally`.

---

### Question 3

A developer writes this code:

```javascript
throw 'something went wrong';
```

Why is this a poor practice compared to `throw new Error('something went wrong')`?

- A) Throwing a string causes a `SyntaxError`
- B) A thrown string cannot be caught by `catch`
- C) A thrown string lacks `.name`, `.message`, and `.stack` properties
- D) `throw` only accepts `Error` objects — throwing a string throws a `TypeError` instead

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `throw 'something went wrong'` is valid JavaScript syntax. It does not cause a `SyntaxError`.
- *Why B is incorrect:* A thrown string can be caught by a `catch` block. `catch (err)` receives whatever was thrown — a string, a number, an object, or an `Error` instance. The catch block does not restrict the type.
- *Why C is correct:* `Error` objects have `.name` (the error type), `.message` (the description), and `.stack` (the call stack trace at the time of the throw). A thrown string has none of these. Without `.stack`, you have no information about where the error originated. This makes debugging significantly harder. Always throw `Error` instances.
- *Why D is incorrect:* `throw` does not restrict its argument. JavaScript allows throwing any value — a string, a number, an object, or anything else. No secondary `TypeError` is generated.

---

### Question 4

What is the output of this code?

```javascript
class AppError extends Error {
  constructor(message) {
    super(message);
  }
}

const err = new AppError('oops');
console.log(err.name);
console.log(err instanceof AppError);
console.log(err instanceof Error);
```

- A) `'AppError'`, `true`, `true`
- B) `'Error'`, `true`, `true`
- C) `'AppError'`, `false`, `true`
- D) `undefined`, `true`, `false`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The constructor calls `super(message)` but does not set `this.name`. Without `this.name = 'AppError'`, the `name` property defaults to `'Error'` — inherited from the base `Error` class.
- *Why B is correct:* `name` defaults to `'Error'` because `this.name` is never reassigned in the constructor. Both `instanceof` checks are `true` because `AppError extends Error`, making every `AppError` instance also an instance of `Error`. This demonstrates why you must always explicitly set `this.name` in custom error constructors.
- *Why C is incorrect:* `err.name` is `'Error'`, not `'AppError'`, because the constructor omits `this.name = 'AppError'`. And `err instanceof AppError` is `true` — the object was constructed with `new AppError(...)`.
- *Why D is incorrect:* `name` is `'Error'` (not `undefined`), and `err instanceof Error` is `true` (not `false`). Custom errors inherit from `Error` through the prototype chain.

---

### Question 5

A developer wants to distinguish a `ValidationError` from a `TypeError` in a catch block. Which technique is correct?

- A) `if (err.type === 'ValidationError')`
- B) `if (err instanceof ValidationError)`
- C) `if (err.constructor === 'ValidationError')`
- D) `if (typeof err === 'ValidationError')`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Error objects do not have a `.type` property by default. Unless `ValidationError` explicitly sets `this.type`, this check always returns `undefined` and the condition is never true.
- *Why B is correct:* `instanceof` checks the prototype chain. `err instanceof ValidationError` returns `true` if `err` was created with `new ValidationError(...)`. This is the standard pattern for distinguishing error types — the same approach used with built-in types like `err instanceof TypeError`.
- *Why C is incorrect:* `err.constructor` is a function (the class), not a string. Comparing a function to the string `'ValidationError'` always returns `false`. The correct check would be `err.constructor === ValidationError` (no quotes), but `instanceof` is preferred.
- *Why D is incorrect:* `typeof err` returns `'object'` for any error instance — it does not return the class name. `typeof` identifies primitive types (`'string'`, `'number'`, `'boolean'`, `'undefined'`, `'symbol'`, `'bigint'`) and `'function'`; it returns `'object'` for all objects including error instances.

---

### Question 6

Which `console` method renders an array of objects as a sortable table in Chrome DevTools?

- A) `console.log`
- B) `console.dir`
- C) `console.table`
- D) `console.group`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `console.log` prints objects in an expandable tree format in DevTools. It does not create a table layout with columns and rows.
- *Why B is incorrect:* `console.dir` displays an interactive listing of an object's properties. It is useful for inspecting DOM elements but does not render a tabular grid.
- *Why C is correct:* `console.table(arrayOfObjects)` renders the data as a formatted table in DevTools with column headers matching the object property names. Each object becomes a row. Columns are sortable by clicking the header. This is the most efficient way to inspect an array of structured data.
- *Why D is incorrect:* `console.group(label)` creates a collapsible section in the console — it groups other log messages. It does not display data in a table format.

---

### Question 7

What does the `debugger` statement do in production code where Chrome DevTools is closed?

- A) It throws a `ReferenceError` because `debugger` is not defined
- B) It pauses execution and waits indefinitely until a debugger connects
- C) It is silently ignored — execution continues normally
- D) It logs a warning to the console

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `debugger` is a reserved keyword in JavaScript — it is part of the language syntax. It does not throw a `ReferenceError`. It is recognized and handled by the engine.
- *Why B is incorrect:* Without an attached debugger, `debugger` does not pause or block execution. In Node.js without `--inspect`, it is also silently ignored.
- *Why C is correct:* The `debugger` statement is only active when a JavaScript debugger is connected. In a browser with DevTools closed, or in Node.js without the inspector, `debugger` is a no-op — the engine recognizes it and skips past it. This is why it must be removed before deploying to production: in a user's browser with DevTools open, it would pause their session.
- *Why D is incorrect:* `debugger` does not produce console output of any kind. It has no visible effect when no debugger is attached.

---

### Question 8

A developer uses `console.assert` as follows:

```javascript
const items = [1, 2, 3];
console.assert(items.length > 5, 'Expected more than 5 items, got:', items.length);
```

What happens?

- A) An error is thrown and execution stops
- B) Nothing is logged — the assertion passes
- C) An assertion error is logged to the console; execution continues
- D) The message is logged to the console as a normal `console.log`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `console.assert` does not throw an error. It logs a message to the console but does not interrupt execution. The program continues running after the assertion.
- *Why B is incorrect:* `items.length > 5` is `3 > 5`, which is `false`. The assertion fails, so output is produced. Nothing would be logged only if the condition were `true`.
- *Why C is correct:* When `console.assert(condition, ...)` is called with a false condition, it logs an assertion failed message along with the provided arguments to the console (in red, like `console.error`). Execution then continues normally on the next line.
- *Why D is incorrect:* Failed assertions are displayed with assertion error styling (red) in DevTools — not as plain `console.log` output. Passing assertions produce no output at all.

---

### Question 9

Which error type is thrown by `decodeURIComponent('%')`?

- A) `TypeError`
- B) `SyntaxError`
- C) `RangeError`
- D) `URIError`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `TypeError` is thrown for type mismatches, such as calling a non-function or accessing a property on null. `decodeURIComponent('%')` receives a string argument (the correct type) — the problem is that the string is a malformed URI sequence.
- *Why B is incorrect:* `SyntaxError` relates to JavaScript code that cannot be parsed. A malformed URI passed to `decodeURIComponent` is not a syntax error in the code itself.
- *Why C is incorrect:* `RangeError` occurs when a value is outside its legal numeric range — for example, `new Array(-1)`. URI decoding is not a range operation.
- *Why D is correct:* `URIError` is thrown specifically by URI handling functions (`decodeURI`, `decodeURIComponent`, `encodeURI`, `encodeURIComponent`) when given malformed URI strings. The `%` character without the required two following hex digits (`%XX`) is a malformed escape sequence, which triggers `URIError`.

---

### Question 10

A developer writes a custom error class but forgets one step:

```javascript
class NetworkError extends Error {
  constructor(message, statusCode) {
    super(message);
    // this.name is NOT set here
    this.statusCode = statusCode;
  }
}

const err = new NetworkError('Not found', 404);
console.log(err.name);
```

What is logged?

- A) `'NetworkError'`
- B) `'Error'`
- C) `undefined`
- D) A `TypeError` is thrown because `name` cannot be read

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `err.name` would be `'NetworkError'` only if the constructor explicitly sets `this.name = 'NetworkError'`. Without that line, the name is inherited from `Error.prototype.name`.
- *Why B is correct:* When a class extends `Error` and does not override `this.name`, the `name` property is inherited from `Error.prototype`, which has the value `'Error'`. The subclass name is not automatically inferred from the class declaration — it must be set explicitly with `this.name = 'NetworkError'` inside the constructor.
- *Why C is incorrect:* `name` is not `undefined`. It is inherited from `Error.prototype.name`, which has the default string value `'Error'`.
- *Why D is incorrect:* No error is thrown when reading `err.name`. The property exists on the prototype chain and returns `'Error'` as a string.
