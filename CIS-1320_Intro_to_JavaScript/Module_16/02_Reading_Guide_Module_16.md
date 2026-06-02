# Reading Guide: Module 16 — Final Exam Prep & JSE Certification Review

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

This reading guide is your complete reference for the JSE certification exam. It consolidates the key testable concepts from Modules 01–15 organized by exam domain. Use it as a study checklist, a quick-reference sheet, and a source of practice prompts. Every concept listed here has appeared in a course quiz or lab.

**JSE Exam Facts:**

- 30 questions, 45 minutes
- Single-answer multiple choice
- Passing score: 70% (21 of 30 correct)
- No penalty for guessing — always answer every question
- Topics: JavaScript language fundamentals; no frameworks, no build tools

---

## Domain 1 — Variables, Data Types, and Operators

### Variables

| Declaration | Scope | Re-assignable | Hoisted |
|---|---|---|---|
| `var` | Function | Yes | Yes (as `undefined`) |
| `let` | Block | Yes | No (TDZ error) |
| `const` | Block | No | No (TDZ error) |

- `const` prevents reassignment of the binding, not mutation of the object. `const arr = []; arr.push(1)` is valid.
- `var` hoisting: the declaration moves to the top of the function, but the assignment does not. Accessing before the assignment returns `undefined`.

### Data Types

**Primitive types (7):** `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`

**`typeof` results:**

| Value | `typeof` Result |
|---|---|
| `'hello'` | `'string'` |
| `42` | `'number'` |
| `true` | `'boolean'` |
| `undefined` | `'undefined'` |
| `null` | `'object'` — historical bug |
| `Symbol()` | `'symbol'` |
| `function(){}` | `'function'` |
| `{}` or `[]` | `'object'` |

### Operators

- `===` strict equality — no type coercion. `==` loose equality — coerces types.
- `null == undefined` is `true`. `null === undefined` is `false`.
- `+` with a string operand: concatenation. `-`, `*`, `/`: numeric coercion.
- Nullish coalescing: `a ?? b` — returns `b` only if `a` is `null` or `undefined`.
- Optional chaining: `obj?.prop` — returns `undefined` if `obj` is null/undefined.
- Logical assignment: `a ||= b` (assign if `a` is falsy); `a &&= b` (assign if `a` is truthy); `a ??= b` (assign if `a` is null/undefined).

---

## Domain 2 — Control Flow

### `if / else if / else`

- Falsy values: `false`, `0`, `''`, `null`, `undefined`, `NaN`. Everything else is truthy.

### `switch`

- Uses `===` for comparison — no type coercion.
- Without `break`, execution falls through to the next case.
- `default` runs if no case matches; it does not need to be last.

### Loops

| Loop | Use For |
|---|---|
| `for` | Known iteration count |
| `while` | Condition-based, count unknown in advance |
| `do...while` | Must run at least once |
| `for...in` | Object property names (keys) |
| `for...of` | Iterable values (arrays, strings, Maps, Sets) |

- `for...in` iterates over enumerable string keys — use with plain objects.
- `for...of` iterates over values of any iterable — use with arrays and strings.
- `break` exits the loop entirely. `continue` skips to the next iteration.

---

## Domain 3 — Functions

### Declaration vs Expression vs Arrow

```javascript
function add(a, b) { return a + b; }          // declaration — hoisted
const add = function(a, b) { return a + b; };  // expression — not hoisted
const add = (a, b) => a + b;                   // arrow — not hoisted, no own `this`
```

### Parameters

- **Default:** `function greet(name = 'World')` — used when argument is `undefined`.
- **Rest:** `function sum(...nums)` — collects remaining arguments into an array. Must be last.
- **Spread:** `Math.max(...arr)` — expands iterable into individual arguments.

### `this` in Functions

- Regular function: `this` is determined by how it is called (the calling context).
- Arrow function: `this` is inherited from the lexical (surrounding) scope at definition time — no own `this`.
- Arrow functions cannot be used as constructors (`new` throws a `TypeError`).

### Closures

A function that captures variables from its surrounding scope. The inner function retains access to those variables even after the outer function has returned.

```javascript
function counter() {
  let count = 0;
  return () => ++count;
}
const increment = counter();
increment();   // 1
increment();   // 2
```

### Hoisting

- Function declarations are fully hoisted — callable before the `function` line.
- `let` and `const` declarations exist but are in the Temporal Dead Zone (TDZ) until the line is reached — accessing them throws a `ReferenceError`.

---

## Domain 4 — Arrays

### Key Array Methods

| Method | Returns | Mutates? | Purpose |
|---|---|---|---|
| `map(fn)` | New array (same length) | No | Transform each element |
| `filter(fn)` | New array (≤ original length) | No | Keep elements that pass test |
| `reduce(fn, init)` | Single value | No | Accumulate to one value |
| `forEach(fn)` | `undefined` | No | Side effects only |
| `find(fn)` | First matching element or `undefined` | No | Find element |
| `findIndex(fn)` | Index or `-1` | No | Find index |
| `some(fn)` | `boolean` | No | True if any element passes |
| `every(fn)` | `boolean` | No | True if all elements pass |
| `includes(val)` | `boolean` | No | Membership test |
| `indexOf(val)` | Index or `-1` | No | Find index by value |
| `slice(start, end)` | New array | No | Copy a portion |
| `splice(start, n, ...)` | Removed elements | Yes | Remove/insert in place |
| `push(...items)` | New length | Yes | Add to end |
| `pop()` | Removed element | Yes | Remove from end |
| `shift()` | Removed element | Yes | Remove from beginning |
| `unshift(...items)` | New length | Yes | Add to beginning |
| `sort(fn)` | Same array | Yes | Sort in place |
| `reverse()` | Same array | Yes | Reverse in place |
| `flat(depth)` | New array | No | Flatten nested arrays |
| `flatMap(fn)` | New array | No | Map then flatten one level |
| `join(sep)` | String | No | Concatenate with separator |

### Destructuring and Spread

```javascript
const [first, second, ...rest] = [1, 2, 3, 4];
const copy = [...original];
const combined = [...arr1, ...arr2];
```

---

## Domain 5 — Objects

### Creation and Access

```javascript
const user = { name: 'Alice', age: 30 };
user.name;           // dot notation
user['name'];        // bracket notation — required for dynamic keys

const key = 'age';
user[key];           // 30 — dynamic property access
```

### Object Methods

- `Object.keys(obj)` — array of own enumerable property names
- `Object.values(obj)` — array of own enumerable values
- `Object.entries(obj)` — array of `[key, value]` pairs
- `Object.assign(target, ...sources)` — copies properties into target (shallow)
- `Object.freeze(obj)` — prevents modification of properties

### Destructuring

```javascript
const { name, age } = user;
const { name: fullName, role = 'viewer' } = user;  // rename + default
```

### Spread and Rest in Objects

```javascript
const copy    = { ...original };
const merged  = { ...defaults, ...overrides };  // overrides wins on conflict

function configure({ host = 'localhost', port = 3000 } = {}) { ... }
```

### `this` in Object Methods

```javascript
const obj = {
  value: 10,
  double() { return this.value * 2; },          // this = obj
  doubleArrow: () => this.value * 2             // this = outer scope (not obj)
};
```

---

## Domain 6 — Classes and Prototypes

### Class Syntax

```javascript
class Shape {
  constructor(color) {
    this.color = color;
  }
  describe() {
    return `A ${this.color} shape`;
  }
  static create(color) {
    return new Shape(color);
  }
}

class Circle extends Shape {
  constructor(color, radius) {
    super(color);       // required before using this
    this.radius = radius;
  }
  area() {
    return Math.PI * this.radius ** 2;
  }
  describe() {
    return super.describe() + ` (circle, r=${this.radius})`;
  }
}
```

### Key Points

- `super()` in a subclass constructor must be called before accessing `this`.
- `super.method()` calls the parent class's version of the method.
- Static methods belong to the class, not instances — call as `Shape.create()`, not `shape.create()`.
- `instanceof` checks the prototype chain — `new Circle() instanceof Shape` is `true`.
- Private fields: `#field` — accessible only inside the class body.

---

## Domain 7 — DOM Manipulation

### Selecting Elements

```javascript
document.getElementById('id')          // Element or null
document.querySelector('.class')       // First match or null
document.querySelectorAll('p')         // Static NodeList
```

### Content

- `element.textContent` — plain text; safe for any content including user input
- `element.innerHTML` — parsed as HTML; XSS risk with user data

### Attributes and Classes

```javascript
element.getAttribute('href')
element.setAttribute('href', '/page')
element.removeAttribute('disabled')
element.dataset.userId              // reads data-user-id attribute

element.classList.add('active')
element.classList.remove('active')
element.classList.toggle('active')
element.classList.contains('active')
```

### Creating and Inserting

```javascript
const el = document.createElement('div');
el.textContent = 'Hello';
parent.appendChild(el);              // add as last child
parent.prepend(el);                  // add as first child
parent.insertBefore(el, ref);        // before a reference node
el.remove();                         // remove from DOM
el.replaceWith(newEl);               // replace in place
```

### Traversal

```javascript
element.parentElement
element.children            // HTMLCollection of child elements
element.firstElementChild
element.lastElementChild
element.nextElementSibling
element.previousElementSibling
```

---

## Domain 8 — Events

### Adding and Removing Listeners

```javascript
const handler = () => console.log('clicked');
btn.addEventListener('click', handler);
btn.removeEventListener('click', handler);   // same reference required
```

### Event Object Properties

- `event.type` — event name (`'click'`, `'keydown'`, etc.)
- `event.target` — element where the event originated
- `event.currentTarget` — element where the listener is attached
- `event.key` — key name for keyboard events
- `event.preventDefault()` — cancels browser default action
- `event.stopPropagation()` — stops bubbling

### Bubbling and Delegation

Events bubble from the target element up through parent elements. Events that do not bubble: `focus`, `blur`, `mouseenter`, `mouseleave`.

```javascript
list.addEventListener('click', event => {
  const item = event.target.closest('li');
  if (item) handleItem(item);
});
```

Delegation — one listener handles all child elements, including future ones.

---

## Domain 9 — Asynchronous JavaScript

### Event Loop

Synchronous code runs first. `setTimeout` callbacks and Promise `.then` handlers wait in the queue and run only after the call stack is empty. `setTimeout(..., 0)` still runs after all synchronous code.

### Promises

```javascript
new Promise((resolve, reject) => {
  // resolve(value) or reject(reason)
})
  .then(value => ...)
  .catch(err => ...)
  .finally(() => ...);
```

### Combinators

| Combinator | Fulfills When | Rejects When | Use For |
|---|---|---|---|
| `Promise.all` | All fulfill | Any rejects | All required, fail-fast |
| `Promise.allSettled` | All settle | Never | Partial results acceptable |
| `Promise.race` | First settles | First rejects | Timeout pattern |
| `Promise.any` | First fulfills | All reject (AggregateError) | Redundancy/fallback |

### `async/await`

```javascript
async function load() {
  try {
    const res = await fetch('/api/data');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error(err.message);
  }
}
```

- `async` functions always return a Promise.
- `await` is only valid inside an `async` function.
- `fetch` resolves for any HTTP response including errors — always check `response.ok`.
- Sequential `await` for dependent steps; `Promise.all` for independent parallel steps.

---

## Domain 10 — Error Handling

### Error Types

| Type | When Thrown |
|---|---|
| `TypeError` | Operation invalid for the value's type (`null.name`) |
| `ReferenceError` | Undeclared variable used |
| `RangeError` | Numeric value out of valid range |
| `SyntaxError` | Code cannot be parsed (prevents execution) |
| `URIError` | Malformed URI string |
| `EvalError` | Misuse of `eval()` (rare) |

### `try / catch / finally`

- `finally` always executes — even when `try` returns.
- If `finally` contains `return`, it overrides `try`/`catch` returns.
- Rethrow errors you cannot specifically handle.

### Custom Errors

```javascript
class AppError extends Error {
  constructor(message) {
    super(message);          // required — sets .message and .stack
    this.name = 'AppError';  // required — defaults to 'Error' without this
  }
}
```

`instanceof` works for custom error classes: `err instanceof AppError`.

---

## High-Frequency Exam Topics — Quick Reference

These are the specific facts that distinguish correct answers from plausible distractors on the JSE exam:

1. `typeof null === 'object'` — a language bug, not intentional design
2. `forEach` returns `undefined` — not a new array
3. `const` with objects — prevents reassignment, not mutation
4. Arrow functions have no own `this` — they cannot be constructors
5. `for...in` gives keys; `for...of` gives values
6. `super()` must be called before `this` in a subclass constructor
7. `Promise.all` fails fast; `Promise.allSettled` never rejects
8. `fetch` resolves on 404 — always check `response.ok`
9. `finally` always runs — even after `return`
10. Custom errors must set `this.name` — it defaults to `'Error'`
11. `event.target` vs `event.currentTarget` — origin vs listener element
12. `var` hoisting — declaration hoisted, assignment is not
13. `null == undefined` is `true`; `null === undefined` is `false`
14. `SyntaxError` cannot be caught in normal code — prevents script parsing
15. `removeEventListener` requires the same function reference

---

## Study Plan — Final Week

- [ ] Watch the Module 16 video lecture.
- [ ] Review the "High-Frequency Exam Topics" list above and verify you can explain each one.
- [ ] Re-take all course quizzes (Modules 01–15) without looking at notes — aim for 100% on each.
- [ ] Review any quiz questions you answered incorrectly — read the distractor analysis.
- [ ] Write five small programs from memory: a closure counter, a Promise chain, an async/await fetch, an event-delegated list, and a custom error class.
- [ ] Read [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) sections for any topics that feel uncertain.
- [ ] Schedule and complete the JSE exam (see Lab 16).
