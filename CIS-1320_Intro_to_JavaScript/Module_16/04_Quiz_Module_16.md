# Quiz: Module 16 - Final Exam Prep & JSE Certification Review
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which of the following JSE best practices should you follow when inserting user-supplied text into the DOM?
*   A) Use `innerHTML` because it is the most powerful DOM property and handles all content types
*   B) Use `textContent` because it treats the value as plain text and does not parse HTML tags, preventing XSS
*   C) Use `document.write()` because it is the most direct way to add content to the page
*   D) Use `setAttribute("value", ...)` because it stores content as an attribute rather than in the DOM tree
*   **Correct Answer:** B) Use `textContent` because it treats the value as plain text and does not parse HTML tags, preventing XSS.
*   **Distractor Analysis:**
    *   *Why correct:* `textContent` does not interpret the string as HTML, so injected `<script>` or event handler tags are rendered as visible characters rather than executed — this is the safe choice for untrusted input.
    *   The other options either present security risks or use inappropriate APIs for this purpose.

---

**Question 2**
Which of the following most accurately describes **JavaScript Core Operations** that are tested on the JSE exam?
*   A) The configuration settings stored in a `package.json` file that define how a Node.js project is built and run
*   B) The foundational language mechanics — variable scope, type coercion, function invocation, array/object manipulation, DOM interaction, and async patterns — that underpin every JavaScript program
*   C) The set of network protocols (HTTP, HTTPS, WebSockets) that JavaScript uses to communicate with backend servers
*   D) The browser-rendering pipeline steps (parsing, layout, painting, compositing) that determine how fast a web page loads
*   **Correct Answer:** B) The foundational language mechanics — variable scope, type coercion, function invocation, array/object manipulation, DOM interaction, and async patterns — that underpin every JavaScript program.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `package.json` is a Node.js/npm configuration concern; JSE tests the JavaScript language itself, not project tooling.
    *   *Why B is correct:* JSE Core Operations covers the language fundamentals every JavaScript developer must know: declarations, operators, control flow, functions, objects, the DOM, and asynchronous programming.
    *   *Why C is incorrect:* Network protocols are a web architecture topic; the JSE exam focuses on JavaScript language semantics, not HTTP or WebSocket specifications.
    *   *Why D is incorrect:* The browser rendering pipeline is a performance and browser internals topic, not a JavaScript language concept tested by the JSE.

---

**Question 3**
A developer is reviewing code for a final project. Which of the following changes represents the best JavaScript practice?
*   A) Replacing `let count = 0;` with `var count = 0;` to ensure the variable is globally accessible
*   B) Replacing `if (x == null)` with `if (x === null || x === undefined)` for a more explicit null/undefined check
*   C) Replacing `element.textContent = userInput` with `element.innerHTML = userInput` for richer display options
*   D) Replacing `try/catch` blocks with empty catch handlers to prevent error messages from reaching users
*   **Correct Answer:** B) Replacing `if (x == null)` with `if (x === null || x === undefined)` for a more explicit null/undefined check
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Switching to `var` for global access is an anti-pattern; use `let`/`const` and pass values explicitly.
    *   *Why B is correct:* While `x == null` already catches both `null` and `undefined` (due to loose equality), using strict checks makes the intent explicit and avoids relying on coercion rules.
    *   *Why C is incorrect:* Assigning user input to `innerHTML` is a security risk (XSS); `textContent` is the safer approach.
    *   *Why D is incorrect:* Empty catch handlers silently swallow errors, making debugging extremely difficult; errors should always be logged or handled.

---

**Question 4**
While doing final review for the JSE exam, a student reads this code and must predict the output:
```javascript
const obj = { x: 10 };
const fn = () => this.x;
console.log(fn.call(obj));
```
What is logged?
*   A) `10` because `call()` binds `this` to `obj`
*   B) `undefined` because arrow functions ignore `call()`, `apply()`, and `bind()` for `this` binding
*   C) A `TypeError` because arrow functions cannot be called with `call()`
*   D) `NaN` because `this.x` returns a string in arrow functions
*   **Correct Answer:** B) `undefined` because arrow functions ignore `call()`, `apply()`, and `bind()` for `this` binding.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `call()` can override `this` in regular functions, but arrow functions capture `this` lexically and cannot be rebound.
    *   *Why B is correct:* Arrow functions have no own `this`; `call()`, `apply()`, and `bind()` silently do nothing to change `this` in an arrow function. `this` refers to the outer scope's `this` (likely `undefined` in strict mode or the global object in non-strict), so `this.x` is `undefined`.
    *   *Why C is incorrect:* Arrow functions can be invoked with `call()` without error; `call()` simply has no effect on their `this`.
    *   *Why D is incorrect:* `this.x` returns `undefined` (not a string), and `undefined` logged directly prints as `undefined`, not `NaN`.

---

**Question 5**
Which of the following is the correct way to export a function `greet` from a JavaScript module file and import it in another file?
*   A) Export: `module.exports = greet;` — Import: `const greet = require("./module");`
*   B) Export: `export function greet() {}` — Import: `import { greet } from "./module.js";`
*   C) Export: `window.greet = greet;` — Import: `const greet = window.greet;`
*   D) Export: `export default greet;` — Import: `import { greet } from "./module.js";`
*   **Correct Answer:** B) Export: `export function greet() {}` — Import: `import { greet } from "./module.js";`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `module.exports`/`require` is CommonJS syntax used in Node.js, not ES6 module syntax used in browsers and the JSE exam.
    *   *Why B is correct:* Named exports use `export` on the declaration and are imported with curly braces `{ greet }` — this is the ES6 module syntax tested by the JSE.
    *   *Why C is incorrect:* Adding to `window` creates a global variable, not a module export; this is an anti-pattern and not a module system.
    *   *Why D is incorrect:* `export default` uses default export syntax, which must be imported without braces: `import greet from "./module.js"`. Importing a default export with `{ greet }` will result in `undefined`.
