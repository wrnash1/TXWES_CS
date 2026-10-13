# Video Script: CIS-1320 — Introduction to JavaScript

## Module 16 — Final Exam Prep & JSE Certification Review

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - This is the final module. The tone should be encouraging and confident — students have covered the full curriculum.
> - Use slides for the domain review sections. No live coding demos are needed, but console snippets are appropriate for the tricky-question walkthroughs.
> - Structure: brief intro → JSE exam overview → domain-by-domain rapid review → tricky question types → exam day advice → closing.
> - Keep each domain rapid — this is a memory jog, not reteaching. Students have the reading guides for depth.
> - The "tricky question types" section is high-value — focus on the patterns that distinguish correct answers from plausible-but-wrong distractors.
> - End on an encouraging note. Many students underestimate their readiness at this stage.

---

## [00:00 – 02:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 16 | Final Exam Prep & JSE Certification Review | CIS-1320"]**

"This is the last module of CIS-1320. By this point, you have covered every major topic in the JSE certification exam: variables, operators, control flow, functions, arrays, objects, classes, the DOM, events, asynchronous JavaScript, and error handling. Module 16 is not new material — it is the review and consolidation session that ties everything together and prepares you to walk into the exam with confidence.

Here is what we are doing in this video. First, I will give you a brief overview of the JSE exam itself. Then we will do a rapid domain-by-domain review — hitting the most-tested concepts in each area. After that, I will walk through the question types that trip students up most often. And I will close with exam day strategy.

Let me start with the exam itself."

---

## [02:00 – 04:00] The JSE Exam — What to Expect

**[SHOW SLIDE: "JSE Certified Associate — Exam Overview"]**

"The JSE — Certified Associate in JavaScript Programming exam is offered by OpenEDG through the JS Institute. Here is what you need to know about the format.

The exam has 30 questions in 45 minutes. Questions are single-answer multiple choice. There is no partial credit and no penalty for guessing — always answer every question. The passing score is 70%, which means you need 21 correct answers.

The exam tests pure JavaScript — the language itself. It does not test frameworks, libraries, or browser-specific APIs beyond what the language specifies. It does not test advanced ES2022+ features. It focuses on: data types and operators, control flow, functions, arrays, objects, classes, basic DOM interaction, and error handling.

You have already done more preparation in this course than the exam requires. The labs, quizzes, and reading guides have covered every domain."

---

## [04:00 – 08:30] Domain 1–4 Rapid Review: Language Fundamentals

**[SHOW SLIDE: "Domain Review: Language Fundamentals"]**

"Let me move through each domain quickly. These are the concepts that appear most frequently.

**Variables and Data Types:**

`let` is block-scoped, can be reassigned. `const` is block-scoped, cannot be reassigned — but objects and arrays declared with `const` can still be mutated. `var` is function-scoped and hoisted; avoid it in new code.

The seven primitive types: `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`. Everything else is an object. `typeof null` returns `'object'` — this is a historical bug in the language, not a design choice.

[PAUSE]

**Operators:**

`===` is strict equality — no type coercion. `==` is loose equality — applies type coercion. Exam questions love `null == undefined` (true) and `null === undefined` (false).

`+` with a string concatenates — even if one operand is a number. `-`, `*`, `/` coerce strings to numbers.

Nullish coalescing: `a ?? b` returns `b` only if `a` is `null` or `undefined`. Optional chaining: `obj?.prop` returns `undefined` instead of throwing if `obj` is null or undefined.

[PAUSE]

**Control Flow:**

`switch` uses strict equality for comparison. Remember `break` — without it, execution falls through to the next case.

`for...in` iterates over an object's enumerable property names (keys). `for...of` iterates over the values of an iterable (array, string, Map, Set). Do not confuse them.

[PAUSE]

**Functions:**

Arrow functions do not have their own `this` — they inherit `this` from the surrounding context. Regular functions have their own `this`. This distinction matters for methods inside classes and event handlers.

Default parameters: `function greet(name = 'World')`. Rest parameters: `function sum(...nums)` — collects remaining arguments into an array. Spread operator: `Math.max(...arr)` — expands an array into individual arguments."

---

## [08:30 – 12:30] Domain 5–7 Rapid Review: Arrays, Objects, Classes

**[SHOW SLIDE: "Domain Review: Arrays, Objects, Classes"]**

"**Arrays and Array Methods:**

Know the return value of every array method:

- `map` returns a new array — same length, transformed values. Does not mutate.
- `filter` returns a new array — only elements that pass the test. Does not mutate.
- `reduce` returns a single accumulated value. Does not mutate.
- `forEach` returns `undefined` — use it for side effects only.
- `find` returns the first matching element, or `undefined`.
- `findIndex` returns the index of the first match, or `-1`.
- `some` returns `true` if any element passes. `every` returns `true` if all elements pass.
- `push`/`pop` mutate and return the new length / removed element. `shift`/`unshift` same, for the beginning.
- `slice` returns a new array (non-mutating). `splice` mutates in place.
- `includes` returns boolean. `indexOf` returns index or `-1`.

[PAUSE]

**Objects:**

`Object.keys(obj)` returns an array of the object's own enumerable property names. `Object.values(obj)` returns an array of values. `Object.entries(obj)` returns an array of `[key, value]` pairs.

Destructuring: `const { name, age } = user` — extracts properties by name. Rename: `const { name: fullName } = user`. Default: `const { role = 'viewer' } = user`.

Spread to copy or merge: `const copy = { ...original }`. `const merged = { ...defaults, ...overrides }`.

`this` inside an object method refers to the object. In an arrow function, `this` is inherited from the outer scope — which can be a problem when you want the method to refer to its own object.

[PAUSE]

**Classes:**

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound.`;
  }
}

class Dog extends Animal {
  speak() {
    return `${this.name} barks.`;
  }
}
```

`super()` in a subclass constructor calls the parent constructor — required before using `this`. `super.method()` calls the parent class's method. Subclass instances pass `instanceof` checks for both the subclass and the parent class."

---

## [12:30 – 16:30] Domain 8–10 Rapid Review: DOM, Events, Async

**[SHOW SLIDE: "Domain Review: DOM, Events, Async"]**

"**DOM:**

`getElementById` returns one element or `null`. `querySelector` returns the first matching element or `null`. `querySelectorAll` returns a static `NodeList` of all matches.

`textContent` sets plain text — safe for user data. `innerHTML` parses as HTML — never use it with user-provided strings (XSS risk).

`classList.add`, `remove`, `toggle`, `contains`. `setAttribute`, `getAttribute`, `removeAttribute`. `dataset.propertyName` for `data-*` attributes.

[PAUSE]

**Events:**

`addEventListener(type, handler)` — multiple listeners per element. `removeEventListener` requires the same function reference — arrow functions defined inline cannot be removed.

Event bubbling: events propagate from the target up through parent elements. `event.target` is the element that was actually clicked. `event.currentTarget` is the element that has the listener.

`event.preventDefault()` cancels the browser's default action. `event.stopPropagation()` stops the event from bubbling further up.

Event delegation: one listener on a parent element handles events from all children, including dynamically added ones. Use `event.target.closest(selector)` to find which child triggered the event.

[PAUSE]

**Async JavaScript:**

The event loop: synchronous code runs first; callbacks from `setTimeout` and Promises go to the queue and run only after the call stack is empty.

`Promise.all` — rejects immediately if any Promise rejects. `Promise.allSettled` — always fulfills with all results. `Promise.race` — settles with the first. `Promise.any` — fulfills with the first success; rejects with `AggregateError` if all fail.

`async` functions always return a Promise. `await` pauses the async function, not the engine. `try/catch` inside async functions catches rejected Promises.

`fetch` resolves for any HTTP response, including 404. Always check `response.ok`."

---

## [16:30 – 19:30] Domain 11 Rapid Review: Error Handling

**[SHOW SLIDE: "Domain Review: Error Handling"]**

"**Error Types:**

`TypeError` — wrong type for the operation. `ReferenceError` — variable not declared. `RangeError` — value out of valid range. `SyntaxError` — code cannot be parsed. `URIError` — malformed URI. `EvalError` — historical.

`SyntaxError` cannot be caught in normal code — it prevents the script from running. Other types can be caught with `try/catch`.

**`try/catch/finally`:**

`finally` always runs — even if `try` returns, `finally` executes before the function returns. Catch only what you can specifically handle; rethrow the rest.

**Custom Errors:**

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}
```

`super(message)` initializes `.message` and the stack. `this.name = 'ValidationError'` sets the name — without it, `err.name` defaults to `'Error'`."

---

## [19:30 – 22:30] Tricky Question Types

**[SHOW SLIDE: "Watch Out For These"]**

"Let me walk through the question patterns that produce the most wrong answers.

**`typeof null` is `'object'`** — not `'null'`. This is a language quirk every exam tests.

**`var` hoisting** — `var` declarations are hoisted to the top of their function. The declaration is hoisted, not the assignment. So accessing a `var` before its assignment line returns `undefined`, not a `ReferenceError`.

**`forEach` returns `undefined`** — many students confuse `forEach` with `map`. If a question shows `const result = [1,2,3].forEach(x => x * 2)`, the result is `undefined`, not `[2, 4, 6]`.

**`const` with objects** — `const` prevents reassignment of the variable, not mutation of the object. `const arr = []; arr.push(1)` is valid. `const arr = []; arr = [1]` throws.

**Arrow functions and `this`** — an arrow function inside a class method does not rebind `this`. A regular function does rebind `this`. On exam questions that show a method containing a callback, check whether the callback is an arrow function or a regular function.

**`Promise.all` vs `Promise.allSettled`** — `Promise.all` rejects on the first rejection. `Promise.allSettled` never rejects; it always returns all results. Know which is which.

**`event.target` vs `event.currentTarget`** — `target` is where the event originated. `currentTarget` is where the listener is attached. In a delegated event handler on a `<ul>`, clicking a `<li>` gives `target` as the `<li>` and `currentTarget` as the `<ul>`."

---

## [22:30 – 24:00] Exam Day Strategy

**[SHOW SLIDE: "Exam Day"]**

"A few practical notes for exam day.

You have 45 minutes for 30 questions — that is 90 seconds per question. Most questions take 20–30 seconds. Spend your remaining time on the ones you flagged.

Read every question stem carefully. Exam questions often contain the word 'not' — 'which of the following does NOT...' — and it is easy to miss it under time pressure.

If you are unsure, eliminate the distractors you know are wrong. In most questions, two options are clearly wrong and two are plausible. Knowing what is wrong is as useful as knowing what is right.

There is no penalty for guessing. Never leave a question blank. Your best guess is always better than a blank.

The exam tests concepts, not syntax memorization. If you understand why `Promise.all` fails fast, you can answer any question about it even if the exact phrasing is unfamiliar.

You are ready. The course has covered everything. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 16 — Final Exam Prep & JSE Certification Review]**

---

## Additional Resources

- [JSE Exam Page — JS Institute](https://js.institute/jse)
- [OpenEDG Testing Portal](https://edube.org)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Eloquent JavaScript (free online)](https://eloquentjavascript.net)
- [JavaScript.info](https://javascript.info)
