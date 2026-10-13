# Reading Guide: Module 06 — Functions and Arrow Functions

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-1320 &BULL; INTRODUCTION TO JAVASCRIPT PROGRAMMING</text>
    
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


## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

A function is a named, reusable block of code that accepts input, performs work, and optionally returns a result. Functions are the primary unit of organization in JavaScript programs. Instead of duplicating logic in multiple places, you define it once and call it whenever needed. JavaScript provides three syntaxes for defining functions: function declarations, function expressions, and arrow functions. Understanding each — including how they differ in hoisting and `this` behavior — is essential for both day-to-day coding and the JSE exam.

---

## 1. Function Declarations

### Syntax

```javascript
function functionName(parameter1, parameter2) {
  // body
  return value;
}
```

A function declaration uses the `function` keyword, a name, a comma-separated parameter list in parentheses, and a body enclosed in braces.

### Parameters, Arguments, and Return Values

Three terms appear frequently and are tested on the JSE exam:

| Term | Definition | Example |
|---|---|---|
| Parameter | Variable listed in the function definition — a placeholder | `name` in `function greet(name)` |
| Argument | Actual value passed when calling the function | `'Alice'` in `greet('Alice')` |
| Return value | Value the function sends back to its caller via `return` | `'Hello, Alice!'` |

```javascript
function greet(name) {          // name is the parameter
  return 'Hello, ' + name + '!';
}

const msg = greet('Alice');     // 'Alice' is the argument
console.log(msg);               // 'Hello, Alice!' is the return value
```

### The `return` Statement

`return` exits the function and sends a value back to the caller. It can appear anywhere in the body:

```javascript
function classify(n) {
  if (n < 0) {
    return 'negative';   // early return
  }
  if (n === 0) {
    return 'zero';
  }
  return 'positive';
}
```

The early return pattern handles special cases at the top and lets the main logic flow cleanly without deep nesting.

### Functions Without `return` Return `undefined`

If a function has no `return` statement — or has a bare `return` with no value — it returns `undefined`:

```javascript
function logMessage(msg) {
  console.log(msg);
  // no return
}

const result = logMessage('Hi');
console.log(result);   // undefined
```

This is a common bug source: assigning the result of a function that has no `return` and then trying to use the result as a value.

---

## 2. Function Expressions

### Function Expression Syntax

```javascript
const functionName = function(parameter1, parameter2) {
  return value;
};
```

A function expression assigns a function to a variable. The function itself is typically anonymous (no name after `function`).

```javascript
const multiply = function(a, b) {
  return a * b;
};

console.log(multiply(4, 5));   // 20
```

The function is called the same way regardless of whether it was created with a declaration or an expression.

### Hoisting — The Critical Difference

**Function declarations are hoisted completely.** The entire function definition is moved to the top of its scope before execution. This means a function declaration can be called on a line that appears before the definition in the source file:

```javascript
console.log(square(4));   // 16 — works before the declaration

function square(n) {
  return n * n;
}
```

**Function expressions assigned to `const` or `let` are not hoisted.** The variable is created (and enters the Temporal Dead Zone) but the function value is not assigned until the line is reached. Calling the variable before its initialization throws a `ReferenceError`:

```javascript
console.log(cube(3));   // ReferenceError: Cannot access 'cube' before initialization

const cube = function(n) {
  return n * n * n;
};
```

### Hoisting Summary

| Form | Hoisted? | Callable before definition? | Error if called early? |
|---|---|---|---|
| Function declaration | Yes — completely | Yes | No |
| Function expression (`const`/`let`) | No — TDZ | No | `ReferenceError` |
| Arrow function expression (`const`/`let`) | No — TDZ | No | `ReferenceError` |

Best practice: define functions before calling them, regardless of hoisting. Relying on hoisting makes code harder to follow.

---

## 3. Arrow Functions

Arrow functions (introduced in ES6) provide a shorter syntax for function expressions. The `=>` replaces the `function` keyword.

### Arrow Function Forms

```javascript
// Full form — multiple parameters, multi-statement body
const add = (a, b) => {
  return a + b;
};

// Concise form — single expression body (implicit return)
const add = (a, b) => a + b;

// Single parameter — parentheses optional
const double = n => n * 2;

// No parameters — empty parentheses required
const greetWorld = () => 'Hello, world!';
```

### Implicit Return

When an arrow function body is a single expression (no braces), the expression's value is returned automatically — no `return` keyword needed. This is called an **implicit return**:

```javascript
const square = n => n * n;
console.log(square(5));   // 25
```

When braces are added, the implicit return disappears. An explicit `return` is required:

```javascript
const square = n => {
  return n * n;   // explicit return required inside braces
};
```

### Arrow Function Shorthand Rules Summary

| Situation | Syntax |
|---|---|
| Multiple parameters | `(a, b) => expression` |
| Single parameter | `n => expression` (parentheses optional) |
| No parameters | `() => expression` (parentheses required) |
| Multi-statement body | `(a, b) => { statements; return value; }` |
| Single-expression body | `(a, b) => expression` (implicit return) |

### Arrow Functions and `this`

Arrow functions do not have their own `this` binding. They inherit `this` from the lexical scope where they were defined. This is an important distinction from regular functions, which receive their own `this` depending on how they are called. The practical consequence — and the JSE exam implication — is:

- Use arrow functions for callbacks, utility functions, and situations where you want to inherit the outer `this`.
- Use regular functions when you need the function to have its own `this` — for example, as object methods.

The `this` keyword is covered in depth in the Objects module.

---

## 4. Default Parameters

Default parameters (ES6) specify a fallback value for a parameter when the corresponding argument is `undefined`:

```javascript
function greet(name = 'stranger') {
  return 'Hello, ' + name + '!';
}

console.log(greet('Alice'));     // 'Hello, Alice!'
console.log(greet());            // 'Hello, stranger!'
console.log(greet(undefined));   // 'Hello, stranger!' — undefined triggers default
console.log(greet(null));        // 'Hello, null!' — null does NOT trigger default
```

### Default Parameter Rules

| Argument passed | Default used? |
|---|---|
| Argument omitted | Yes |
| `undefined` passed explicitly | Yes |
| `null` passed | No — `null` is a value |
| `0` passed | No — `0` is a value |
| `''` passed | No — `''` is a value |
| Any other value | No |

Default parameters trigger only when the argument is `undefined`. This matches the same distinction as the `??` operator from Module 04.

### Default Parameters as Expressions

A default parameter can be any valid expression, including a reference to an earlier parameter:

```javascript
function box(width, height = width) {
  return width * height;
}

console.log(box(5, 3));   // 15 — explicit height
console.log(box(5));      // 25 — height defaults to width (5)
```

---

## 5. Rest Parameters

Rest parameters collect any number of remaining arguments into a real array. The syntax is `...parameterName` and it must be the last parameter:

```javascript
function sum(...numbers) {
  let total = 0;
  for (const n of numbers) {
    total += n;
  }
  return total;
}

console.log(sum(1, 2, 3));         // 6
console.log(sum(10, 20, 30, 40));  // 100
console.log(sum());                // 0
```

### Rest Parameter Rules

- The rest parameter must be the **last** parameter in the list.
- There can be only one rest parameter per function.
- It collects all remaining arguments as a genuine `Array` instance.

```javascript
function logFirst(first, second, ...rest) {
  console.log('first:', first);
  console.log('second:', second);
  console.log('rest:', rest);
}

logFirst('a', 'b', 'c', 'd', 'e');
// first: a
// second: b
// rest: ['c', 'd', 'e']
```

### Rest vs `arguments`

Older JavaScript code used the `arguments` object — an array-like object available inside regular functions that contained all passed arguments. Rest parameters replaced this pattern:

| Feature | `arguments` | Rest parameter |
|---|---|---|
| Type | Array-like object | Real `Array` |
| Arrow functions | Not available | Available |
| Naming | Always `arguments` | Developer-chosen |
| Partial collection | No — always all arguments | Yes — collects the remaining args |

Use rest parameters in modern JavaScript. Avoid `arguments`.

---

## 6. Scope in Functions

Function bodies create their own scope. Variables declared with `let` or `const` inside a function are not accessible outside:

```javascript
function computeArea(r) {
  const pi = 3.14159;   // local to computeArea
  return pi * r * r;
}

console.log(computeArea(5));   // 78.53975
console.log(pi);               // ReferenceError: pi is not defined
```

Functions can read variables from their outer scope (closure), but outer code cannot read variables from inside a function. This is the principle of **encapsulation** — keeping implementation details private.

---

## 7. Functions as Values

In JavaScript, functions are **first-class values** — they can be stored in variables, passed as arguments to other functions, and returned from functions:

```javascript
const operations = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
};

console.log(operations.add(5, 3));       // 8
console.log(operations.multiply(4, 6));  // 24
```

Passing a function as an argument to another function creates a **callback**:

```javascript
function applyTwice(fn, value) {
  return fn(fn(value));
}

const addTen = n => n + 10;
console.log(applyTwice(addTen, 5));   // 25 — addTen(addTen(5)) = addTen(15) = 25
```

`applyTwice` receives the function `addTen` as its first argument and calls it twice. This pattern — passing functions as values — is fundamental to JavaScript's array methods (`forEach`, `map`, `filter`) covered in later modules.

---

## 8. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 3: Functions](https://eloquentjavascript.net/03_functions.html)**
  The primary OER textbook. Covers function declarations, expressions, arrow functions, closures, the call stack, and recursion with detailed explanations and exercises.

- **[MDN Web Docs — Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)**
  Comprehensive guide covering all function syntax forms, closures, default parameters, rest parameters, arguments object, and getter/setter functions.

- **[MDN Web Docs — Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)**
  Full reference for arrow functions including concise vs. block body syntax, lexical `this`, and limitations (cannot be used as constructors, no `arguments` object).

- **[javascript.info — Functions](https://javascript.info/function-basics)**
  Beginner-friendly introduction to function declarations, expressions, and return values, followed by an explanation of function naming best practices.

- **[javascript.info — Closures](https://javascript.info/closure)**
  In-depth explanation of the lexical environment, closure mechanics, and practical applications including the counter and memoization patterns demonstrated in this module.

---

## 9. JSE Certification Exam Tips

1. **Function declaration hoisting** — function declarations are hoisted completely and can be called before their definition. Function expressions and arrow functions are not.

2. **`ReferenceError` on early call** — calling a `const` function expression before its definition throws `ReferenceError: Cannot access 'X' before initialization`, not `undefined`.

3. **Implicit return in arrow functions** — only when there are no braces. The moment you add `{}`, you need an explicit `return`.

4. **Default parameter triggers** — a default is used when the argument is `undefined` (omitted or explicitly `undefined`). `null`, `0`, and `''` do not trigger defaults.

5. **Rest parameter position** — rest must be the last parameter. `function f(...a, b)` is a `SyntaxError`.

6. **Functions without `return` return `undefined`** — assigning the result of such a function gives `undefined`, not an error.

7. **Parameters vs arguments** — the exam distinguishes between them. Parameter = definition placeholder; argument = call-time value.

8. **Arrow functions have no `this`** — they inherit `this` from their enclosing context. This is a frequent interview and exam topic.

9. **`arguments` object not available in arrow functions** — only in regular functions. Use rest parameters instead.

10. **Function expressions require semicolons** — `const f = function() {};` ends with a semicolon because it is a variable declaration (a statement), not a function declaration.

---

## 10. Study Checklist

- [ ] Watch the Module 06 video lecture by Professor Nash.
- [ ] Read Chapter 3 (Functions) of [Eloquent JavaScript](https://eloquentjavascript.net/03_functions.html).
- [ ] Read [MDN — Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions).
- [ ] Read [MDN — Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).
- [ ] Open the console and call a function declaration before its definition — confirm it works.
- [ ] Open the console and call a `const` function expression before its definition — confirm the `ReferenceError`.
- [ ] Write an arrow function in all four forms (full, concise, single param, no params).
- [ ] Test a default parameter with `undefined` and `null` — confirm which triggers the default.
- [ ] Write a rest parameter function with three fixed parameters and a rest that collects the remainder.
- [ ] Complete the Module 06 Lab.
- [ ] Complete the Module 06 Quiz.
