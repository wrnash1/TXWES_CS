# Quiz: Module 01 - JavaScript Introduction & Execution
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which HTML tag is used to embed or reference client-side JavaScript code within a web page?
*   A) `<javascript>`
*   B) `<script>`
*   C) `<js>`
*   D) `<code class='javascript'>`
*   **Correct Answer:** B) The `<script>` tag is the standard HTML element used to embed or link external JavaScript code.
*   **Distractor Analysis:**
    *   *Why correct:* The `<script>` tag is the standard HTML element used to embed or link external JavaScript code.
    *   The other options represent non-existent HTML tags.

---

**Question 2**
Which of the following most accurately describes a **JS engine**?
*   A) A browser component that parses HTML and builds the DOM tree from markup
*   B) A runtime that reads, compiles, and executes JavaScript code (e.g., V8 in Chrome)
*   C) A JavaScript library that simplifies DOM selection using CSS-style queries
*   D) The `window` object that represents the global scope in a browser environment
*   **Correct Answer:** B) A runtime that reads, compiles, and executes JavaScript code (e.g., V8 in Chrome).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes an HTML parser, not a JS engine.
    *   *Why B is correct:* A JS engine is the browser's dedicated component that processes and runs JavaScript source code.
    *   *Why C is incorrect:* That describes a library like jQuery, not the JS engine itself.
    *   *Why D is incorrect:* `window` is the global object; the engine is the runtime that evaluates all JS code.

---

**Question 3**
A developer wants to confirm that a variable named `score` holds the value `42` at a specific point in their script. Which statement is most appropriate to add temporarily for this purpose?
*   A) `document.write(score);`
*   B) `alert(score);`
*   C) `console.log(score);`
*   D) `score.print();`
*   **Correct Answer:** C) `console.log(score);`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `document.write` injects content into the page body and can erase the page if called after load.
    *   *Why B is incorrect:* `alert()` works but is intrusive and blocks execution; not the standard debugging tool.
    *   *Why C is correct:* `console.log()` is the standard non-blocking way to inspect values in the browser DevTools console.
    *   *Why D is incorrect:* Numbers in JavaScript do not have a `.print()` method; this throws a TypeError.

---

**Question 4**
A student places a `<script src="app.js"></script>` tag in the `<head>` of their HTML file without any additional attributes. The script tries to access a `<div>` element in the `<body>`. What will happen?
*   A) The script runs successfully because the `<head>` executes after the `<body>`.
*   B) The script will fail because `<head>` scripts run before `<body>` elements are parsed, so the `<div>` is `null`.
*   C) The script runs in a separate thread and will wait for the DOM to finish loading.
*   D) The browser ignores scripts placed in the `<head>` and moves them to the bottom automatically.
*   **Correct Answer:** B) The script will fail because `<head>` scripts run before `<body>` elements are parsed, so the `<div>` is `null`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `<head>` is parsed before `<body>`, not after.
    *   *Why B is correct:* Without `defer` or moving the tag to the bottom of `<body>`, the script executes before those DOM elements exist.
    *   *Why C is incorrect:* JavaScript is single-threaded; there is no automatic background waiting without `defer` or event listeners.
    *   *Why D is incorrect:* The browser does not reorder script tags automatically.

---

**Question 5**
When does a JavaScript **execution context** get created?
*   A) Only once, when the browser first starts up
*   B) Every time a function is called or a script file begins executing
*   C) Only when a variable is declared with `var`
*   D) Whenever the browser receives a network response from a server
*   **Correct Answer:** B) Every time a function is called or a script file begins executing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Execution contexts are created dynamically during program execution, not just at browser startup.
    *   *Why B is correct:* The JS engine creates a new execution context for the global scope and for every function invocation, pushing it onto the call stack.
    *   *Why C is incorrect:* Variable declarations do not trigger a new execution context; function calls do.
    *   *Why D is incorrect:* Network responses can trigger callbacks, but the execution context is created when that callback function is called, not by the network event itself.
