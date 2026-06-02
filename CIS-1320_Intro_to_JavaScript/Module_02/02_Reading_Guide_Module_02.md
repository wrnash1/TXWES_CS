# Reading Guide: Module 02 — Variables, Constants, and Scope

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Every useful program stores and manipulates data. In JavaScript, named storage locations are called variables. How you declare a variable — with `var`, `let`, or `const` — determines where it can be accessed, whether it can be reassigned, and what happens if you try to read it before its declaration. These rules form the foundation of predictable, bug-free JavaScript code and are among the most heavily tested topics on the JSE certification exam.

---

## 1. The Three Declaration Keywords

JavaScript provides three keywords for declaring variables: `var`, `let`, and `const`. They were introduced at different points in the language's history and have meaningfully different behaviors.

### `let` — Block-Scoped, Reassignable

`let` is the standard modern keyword for declaring a variable you expect to reassign.

```javascript
let score = 0;
console.log(score);   // 0

score = 100;
console.log(score);   // 100
```

Rules for `let`:

- **Block-scoped:** The variable is only accessible within the `{}` block where it was declared.
- **Reassignable:** You can assign a new value as many times as needed.
- **Cannot be re-declared** in the same scope — attempting to do so is a `SyntaxError`.
- **Temporal Dead Zone (TDZ):** Accessing a `let` variable before its declaration line throws a `ReferenceError`.

### `const` — Block-Scoped, Non-Reassignable

`const` declares a binding that cannot be reassigned after initialization.

```javascript
const PI = 3.14159;
const courseName = 'CIS-1320 Introduction to JavaScript';

PI = 3;   // TypeError: Assignment to constant variable.
```

Rules for `const`:

- **Block-scoped:** Same as `let`.
- **Cannot be reassigned:** Any attempt to assign a new value throws a `TypeError`.
- **Must be initialized at declaration:** `const x;` with no value is a `SyntaxError`.
- **Cannot be re-declared** in the same scope.
- **Does not make objects or arrays immutable** — see Section 4.

**Best practice:** Use `const` by default. Switch to `let` only when you know you need to reassign the variable. Most variables in well-written JavaScript are `const`.

### `var` — Function-Scoped, Hoisted, Permissive

`var` is the original JavaScript declaration keyword from 1995. It has behaviors that regularly produce bugs and is not recommended for new code.

```javascript
var playerName = 'Alice';
var playerName = 'Bob';    // re-declaration — no error with var
console.log(playerName);   // Bob
```

Rules for `var`:

- **Function-scoped** (or globally scoped if outside all functions): `var` ignores block boundaries like `{}`, `if`, and `for` — it is accessible anywhere in the enclosing function.
- **Hoisted and initialized to `undefined`:** Accessing a `var` variable before its declaration returns `undefined` rather than throwing an error.
- **Can be re-declared** in the same scope without error.
- **Global `var` creates a `window` property** in browsers: `var x = 1` at the top level means `window.x === 1`.

---

## 2. Scope

**Scope** is the context that determines where a variable is visible and accessible. JavaScript has three main scope levels.

### Global Scope

A variable declared outside any function or block is in the global scope. Global variables are accessible from anywhere in the program.

```javascript
const appName = 'My App';    // global scope

function showName() {
  console.log(appName);      // accessible from inside a function
}

showName();                   // My App
console.log(appName);        // My App
```

In a browser, the global scope is the `window` object. Variables declared with `var` at the global level become properties of `window`. Variables declared with `let` or `const` at the global level do not become `window` properties — they live in the global scope but are not attached to `window`.

### Function Scope

Variables declared with `var` inside a function are confined to that function. They cannot be accessed from outside.

```javascript
function calculate() {
  var result = 42;
  console.log(result);   // 42
}

calculate();
console.log(result);   // ReferenceError: result is not defined
```

### Block Scope

Variables declared with `let` or `const` are confined to the nearest enclosing `{}` block. This includes blocks created by `if`, `for`, `while`, or any standalone `{}`.

```javascript
if (true) {
  let insideIf = 'only here';
  const MAX = 100;
  console.log(insideIf);   // only here
}

console.log(insideIf);   // ReferenceError: insideIf is not defined
console.log(MAX);        // ReferenceError: MAX is not defined
```

### The `var` Scope Trap

`var` does not respect block boundaries. This is its most dangerous characteristic:

```javascript
if (true) {
  var leaked = 'I escaped the if block';
}
console.log(leaked);   // I escaped the if block — var leaked out

for (var i = 0; i < 3; i++) {}
console.log(i);   // 3 — var i persists after the loop

for (let j = 0; j < 3; j++) {}
console.log(j);   // ReferenceError: j is not defined
```

The `var` version of the loop counter persists after the loop ends. The `let` version is destroyed when the loop block closes. Use `let` in all loop declarations.

---

## 3. Hoisting

**Hoisting** is the behavior by which the JavaScript engine processes declarations before executing any code. During the compilation phase, the engine identifies all variable and function declarations and registers them in their scope — conceptually "moving" declarations to the top. However, only declarations are hoisted; the value assignments stay in place.

### `var` Hoisting — Declaration + `undefined` Initialization

```javascript
console.log(myVar);   // undefined
var myVar = 5;
console.log(myVar);   // 5
```

The engine transforms this internally to:

```javascript
var myVar;            // declaration hoisted, initialized to undefined
console.log(myVar);   // undefined
myVar = 5;            // assignment stays here
console.log(myVar);   // 5
```

Reading `myVar` before its assignment line returns `undefined` — not an error. This is one reason `var` is problematic: no error means no signal that something is wrong.

### `let` and `const` Hoisting — Temporal Dead Zone

`let` and `const` are also technically hoisted — the engine knows they exist — but they are placed in the **Temporal Dead Zone (TDZ)**. The TDZ is the region from the start of the scope to the declaration line. Any access to the variable while it is in the TDZ throws a `ReferenceError`.

```javascript
console.log(myLet);   // ReferenceError: Cannot access 'myLet' before initialization
let myLet = 5;
console.log(myLet);   // 5
```

```javascript
console.log(myConst);   // ReferenceError: Cannot access 'myConst' before initialization
const myConst = 10;
```

The TDZ gives you a clear, explicit error message rather than the silent `undefined` that `var` produces. This makes bugs easier to catch.

### Hoisting Comparison Table

| Keyword | Hoisted? | Initial value during TDZ | Access before declaration |
|---|---|---|---|
| `var` | Yes | `undefined` | Returns `undefined` |
| `let` | Yes (TDZ) | Uninitialized | `ReferenceError` |
| `const` | Yes (TDZ) | Uninitialized | `ReferenceError` |

---

## 4. `const` with Objects and Arrays

`const` prevents reassigning the variable binding — the name itself cannot point to a different value. However, if that value is an object or array, the internal contents of the object or array can be modified.

```javascript
const user = {
  name: 'Alice',
  score: 95
};

user.score = 100;         // OK — modifying a property
user.email = 'a@tx.edu';  // OK — adding a new property
console.log(user);        // { name: 'Alice', score: 100, email: 'a@tx.edu' }

user = { name: 'Bob' };   // TypeError: Assignment to constant variable.
```

The variable `user` always refers to the same object. What is inside that object can change. The `const` binding prevents `user` from being pointed at a completely different object.

The same applies to arrays:

```javascript
const scores = [90, 85, 92];
scores.push(88);           // OK — modifying the array
scores[0] = 95;            // OK — modifying an element
console.log(scores);       // [95, 85, 92, 88]

scores = [1, 2, 3];        // TypeError — cannot reassign the binding
```

This is a common JSE exam trap. Seeing `const` does not mean the data cannot change — only that the variable cannot be redirected to a different value.

---

## 5. Variable Naming Rules

### Syntax Rules (Required)

- Must begin with a letter (a–z, A–Z), an underscore `_`, or a dollar sign `$`
- Can contain letters, digits (0–9), underscores, and dollar signs
- Cannot begin with a digit
- Cannot be a reserved keyword (`let`, `const`, `var`, `if`, `else`, `return`, `function`, etc.)
- Are case-sensitive: `score`, `Score`, and `SCORE` are three distinct variables

Valid identifiers: `score`, `player1`, `_count`, `$total`, `isActive`, `MAX_SPEED`

Invalid identifiers: `1stPlace` (starts with digit), `my-score` (hyphen), `let` (reserved keyword)

### Conventions (Recommended)

| Style | Pattern | Used for |
|---|---|---|
| camelCase | `playerScore`, `totalAmount` | Variables and function names |
| UPPER_SNAKE_CASE | `MAX_RETRIES`, `DEFAULT_TIMEOUT` | Module-level constants |
| PascalCase | `PlayerProfile`, `UserAccount` | Class names (covered later) |

JavaScript convention strongly favors camelCase for variables. Code that uses underscores for regular variable names (`player_score`) is valid but non-conventional and harder to read by other JavaScript developers.

### Meaningful Names

Use names that describe what the variable holds:

```javascript
// Poor naming
const a = 3.14159;
const b = 10;
const c = a * b * b;

// Good naming
const PI = 3.14159;
const radius = 10;
const area = PI * radius * radius;
```

---

## 6. Comprehensive `var` vs. `let` vs. `const` Comparison

| Feature | `var` | `let` | `const` |
|---|---|---|---|
| Introduced | ES1 (1997) | ES6 (2015) | ES6 (2015) |
| Scope | Function (or global) | Block | Block |
| Hoisted | Yes (initialized to `undefined`) | Yes (TDZ) | Yes (TDZ) |
| Reassignable | Yes | Yes | No |
| Re-declarable in same scope | Yes | No (SyntaxError) | No (SyntaxError) |
| Must initialize at declaration | No | No | Yes |
| Creates `window` property | Yes (global) | No | No |
| Recommended for new code | No | When reassignment needed | Default choice |

---

## 7. JSE Certification Exam Tips

1. **`var` leaks out of blocks.** A `var` declared inside an `if` or `for` block is accessible after that block closes. A `let` or `const` is not — it throws `ReferenceError`.

2. **Accessing `var` before its line returns `undefined`.** This is hoisting in action. It is not an error; it returns the hoisted-but-uninitialized value.

3. **Accessing `let` or `const` before their line throws `ReferenceError`.** The Temporal Dead Zone prevents access. The error message says "Cannot access before initialization."

4. **`const` reassignment throws `TypeError`.** The error message says "Assignment to constant variable." Know this exact error type.

5. **`const` with objects — properties can still be changed.** Only the binding is constant. If the exam shows `const obj = {}; obj.x = 1;`, that is valid. If it shows `obj = {}`, that is a TypeError.

6. **Re-declaring `let` in the same scope is a `SyntaxError`.** This is caught at parse time, before any code runs.

7. **`var` in a `for` loop leaks the counter.** After `for (var i = 0; i < 5; i++) {}`, `i` is `5` in the outer scope. After `for (let j = 0; j < 5; j++) {}`, `j` is not defined outside the loop.

---

## 8. Study Checklist

- [ ] Watch the Module 02 video lecture by Professor Nash.
- [ ] Read Chapter 2 (Program Structure) of [Eloquent JavaScript](https://eloquentjavascript.net/02_program_structure.html).
- [ ] Read the MDN articles for [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).
- [ ] Open the browser console and reproduce the hoisting examples from Section 3.
- [ ] Open the browser console and reproduce the block scope examples from Section 2.
- [ ] Verify the `const` + object mutation behavior from Section 4 with your own experiment.
- [ ] Memorize the comparison table in Section 6.
- [ ] Complete the Module 02 Lab.
- [ ] Complete the Module 02 Quiz.
