# Quiz: Module 01 — JavaScript Introduction and Execution

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** This quiz covers Module 01 material. Choose the single best answer for each question.

---

### Question 1

What is the correct HTML element used to embed or link JavaScript in a web page?

- A) `<javascript>`
- B) `<js src="app.js">`
- C) `<script>`
- D) `<code type="js">`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* There is no `<javascript>` HTML element. This does not exist in any HTML specification.
- *Why B is incorrect:* There is no `<js>` element. The `src` attribute pattern is correct syntax but only works on the `<script>` element.
- *Why C is correct:* `<script>` is the standard HTML element for embedding JavaScript. It can contain inline code between the tags or link an external file via the `src` attribute: `<script src="app.js"></script>`.
- *Why D is incorrect:* `<code>` is a presentational element for displaying code-formatted text. It does not execute JavaScript.

---

### Question 2

A developer places `<script src="main.js"></script>` inside the `<head>` of their HTML document without any additional attributes. The script contains `document.getElementById('header')`. What will this expression return?

- A) The `<head>` element, because the script is in the head
- B) `undefined`, because the element has not been declared yet
- C) `null`, because the script runs before the `<body>` elements are parsed
- D) An empty string, because the element exists but has no value yet

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `document.getElementById()` searches the entire document by ID attribute value, not by the location of the script tag. It has nothing to do with where the script is placed structurally.
- *Why B is incorrect:* `document.getElementById()` returns `null` when an element is not found — not `undefined`. `undefined` is returned when a variable is declared but not assigned.
- *Why C is correct:* A `<script>` in `<head>` without `defer` or `async` executes immediately during HTML parsing. At that point the browser has not yet parsed the `<body>`, so no body elements exist in the DOM. `getElementById` returns `null` for any element that does not exist.
- *Why D is incorrect:* `getElementById` does not return empty strings. Its only possible return values are an element reference or `null`.

---

### Question 3

What is the purpose of `console.log()` in JavaScript?

- A) It writes text directly onto the visible web page for users to read
- B) It opens a popup dialog box displaying a message to the user
- C) It writes output to the browser's developer tools console for debugging
- D) It sends a log entry to the web server for storage

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `console.log()` does not modify the HTML document or display anything on the visible page. Users do not see console output unless they open DevTools themselves.
- *Why B is incorrect:* That describes `alert()`, which opens a modal dialog. `console.log()` is silent to the end user.
- *Why C is correct:* `console.log()` writes to the browser's developer tools console (opened with F12). It is primarily a debugging tool for developers to inspect values and trace code execution.
- *Why D is incorrect:* `console.log()` operates entirely client-side within the browser. It does not make network requests or communicate with any server.

---

### Question 4

What does the `defer` attribute do when added to a `<script>` tag in the `<head>`?

- A) It prevents the script from ever executing unless the user clicks a button
- B) It downloads the script in parallel and executes it immediately when the download finishes
- C) It downloads the script in parallel and executes it after the entire HTML document is parsed
- D) It delays the script download until after the page is fully displayed

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `defer` has nothing to do with user interaction. The script executes automatically.
- *Why B is incorrect:* That describes the `async` attribute, not `defer`. `async` executes the script as soon as it downloads, which may be before the HTML parsing is complete.
- *Why C is correct:* `defer` instructs the browser to download the script file while continuing to parse the HTML (non-blocking download), and then execute the script after the full HTML document has been parsed and the DOM is ready. Multiple deferred scripts execute in document order.
- *Why D is incorrect:* `defer` delays execution — not the download. The download begins immediately but runs in parallel with HTML parsing.

---

### Question 5

Which JavaScript embedding method is considered best practice for production web applications?

- A) Inline JavaScript in HTML event attributes: `<button onclick="doSomething()">`
- B) An internal `<script>` block placed anywhere in the HTML file
- C) An external `.js` file linked with `<script src="app.js" defer>`
- D) Placing all JavaScript inside HTML comments: `<!-- let x = 5; -->`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Inline event attributes mix HTML and JavaScript in the same place, violating separation of concerns. They are difficult to maintain, impossible to cache, and cannot be easily reused across elements.
- *Why B is incorrect:* Internal script blocks are fine for small experiments and learning, but in production they cannot be cached separately, are harder to test, and pollute the HTML file with logic.
- *Why C is correct:* External `.js` files achieve clean separation of structure (HTML) and behavior (JavaScript). They can be cached by the browser, shared across multiple pages, and tested independently. The `defer` attribute ensures correct execution timing.
- *Why D is incorrect:* Content inside HTML comments is completely ignored by the browser. JavaScript inside `<!-- -->` will not execute.

---

### Question 6

What is the primary job of a JavaScript engine in a browser?

- A) Rendering HTML and CSS into visual pixels on the screen
- B) Managing network requests and caching downloaded resources
- C) Parsing, compiling, and executing JavaScript source code
- D) Storing web application data in the browser's local storage

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Rendering HTML and CSS is performed by the browser's rendering engine (e.g., Blink in Chrome, Gecko in Firefox) — a separate component from the JS engine.
- *Why B is incorrect:* Network requests and caching are handled by the browser's networking stack, not the JS engine.
- *Why C is correct:* The JS engine (V8 in Chrome, SpiderMonkey in Firefox) receives JavaScript source code, parses it into an Abstract Syntax Tree, compiles it to machine instructions via JIT compilation, and executes it.
- *Why D is incorrect:* `localStorage` is a browser API that JavaScript can call, but the storage mechanism itself is not part of the JS engine.

---

### Question 7

What is the difference between the `defer` and `async` attributes on a `<script>` tag?

- A) `defer` is for external files only; `async` works with both internal and external scripts
- B) `defer` executes after HTML parsing is complete in document order; `async` executes immediately on download in any order
- C) `defer` downloads the script first; `async` starts executing immediately without downloading
- D) They are identical — both cause the script to execute after the DOM is fully loaded

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both `defer` and `async` only apply to external scripts (scripts with a `src` attribute). Neither attribute has any effect on inline script blocks.
- *Why B is correct:* Both attributes cause the browser to download the script in parallel (non-blocking). The difference is execution timing: `defer` executes after the full HTML document is parsed, maintaining document order. `async` executes as soon as its download completes, potentially before parsing is done, in no guaranteed order relative to other scripts.
- *Why C is incorrect:* Both attributes trigger parallel downloads. Neither begins executing without first completing the download.
- *Why D is incorrect:* They are not identical. `async` can execute before the DOM is ready, which causes the same null-reference problems as a `<head>` script without any attribute. Only `defer` guarantees DOM readiness.

---

### Question 8

What output does the following code produce in the browser console?

```javascript
console.log('Result:', 3 + 4);
console.log('String:', 'Hello' + ' ' + 'World');
console.log('Boolean:', 10 > 5);
```

- A) `Result: 34` then `String: Hello World` then `Boolean: true`
- B) `Result: 7` then `String: Hello World` then `Boolean: true`
- C) `Result: 7` then `String: HelloWorld` then `Boolean: 1`
- D) `TypeError` — cannot concatenate strings and numbers

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `3 + 4` is numeric addition — both operands are numbers, so the result is `7`, not the string `'34'`. String concatenation with `+` only occurs when at least one operand is a string.
- *Why B is correct:* `3 + 4` evaluates to `7` (numeric addition). `'Hello' + ' ' + 'World'` evaluates to `'Hello World'` (string concatenation). `10 > 5` evaluates to `true` (a boolean). `console.log('label:', value)` prints the label followed by a space and the value.
- *Why C is incorrect:* The space character `' '` between `'Hello'` and `'World'` is a third string operand — it is concatenated like the others, producing `'Hello World'` with a space, not `'HelloWorld'`. Booleans are displayed as `true`/`false`, not as `1`/`0`.
- *Why D is incorrect:* `console.log('Result:', 3 + 4)` has a string label and a separate numeric expression. They are passed as two arguments to `console.log`, not added together. No type error occurs.

---

### Question 9

When does the JavaScript engine create a new execution context?

- A) Every time a variable is declared with `let` or `const`
- B) Once when the browser first launches, and never again
- C) Every time a function is called, and once for the global scope when the script begins
- D) Every time a `console.log()` statement is executed

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Variable declarations do not create execution contexts. They create variable bindings inside an existing context.
- *Why B is incorrect:* Execution contexts are created dynamically during program execution as functions are called. A single browser session may create thousands of execution contexts.
- *Why C is correct:* The engine creates the Global Execution Context when the script starts. It then creates a new Function Execution Context every time a function is invoked. These function contexts are pushed onto the call stack and popped when the function returns.
- *Why D is incorrect:* `console.log()` is a function call — and like any function, calling it does create a function execution context internally. But this is because it is a function call, not because it is a `console.log` specifically. Variable declarations, by contrast, do not create contexts.

---

### Question 10

What is an **expression** in JavaScript?

- A) A complete instruction that tells the engine to perform an action, ending with a semicolon
- B) Any piece of code that evaluates to a value
- C) A named block of reusable code defined with the `function` keyword
- D) A line of code that is preceded by `//` and ignored by the engine

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That describes a **statement**. Statements are complete instructions; expressions are value-producing code fragments. Not all statements end with semicolons (e.g., `if` statements, `for` loops), though expression statements typically do.
- *Why B is correct:* An expression is any syntactically valid unit of code that resolves to a value. Examples: `42`, `'hello'`, `x + 1`, `Math.sqrt(9)`, `a > b`. Expressions can appear inside statements.
- *Why C is incorrect:* That describes a function declaration, which is a specific type of statement.
- *Why D is incorrect:* That describes a comment. Comments are not code — they are ignored by the engine entirely and produce no value.
