# Quiz: Module 01 — JavaScript Introduction and Execution

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** This quiz covers Module 01 material. Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

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

---

### Question 11

Which of the following is a valid way to write a **multi-line comment** in JavaScript?

- A) `// This is line 1 // This is line 2`
- B) `<!-- This is a comment -->`
- C) `/* This spans multiple lines */`
- D) `** This is a block comment **`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `//` starts a single-line comment that runs only to the end of that line. Using `//` again on the same line does not extend a comment; it just adds another `//` inside an already-commented line.
- *Why B is incorrect:* `<!-- -->` is an HTML comment. The JavaScript engine does not recognize this syntax as a comment; it will produce a syntax error in a `.js` file.
- *Why C is correct:* `/* ... */` is the multi-line block comment syntax in JavaScript. Everything between `/*` and `*/` is ignored by the engine, regardless of how many lines it spans.
- *Why D is incorrect:* `** ... **` has no special meaning in JavaScript. Asterisks are the exponentiation operator (`**`) and part of the multiplication operator (`*`), not comment delimiters.

---

### Question 12

What is the correct JavaScript engine used in **Google Chrome** and **Node.js**?

- A) SpiderMonkey
- B) JavaScriptCore
- C) Chakra
- D) V8

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* SpiderMonkey is the JavaScript engine developed by Mozilla and used in Firefox, not Chrome.
- *Why B is incorrect:* JavaScriptCore (also called Nitro) is Apple's engine, used in Safari and WebKit-based browsers.
- *Why C is incorrect:* Chakra was Microsoft's engine used in the legacy (pre-Chromium) Edge browser. Modern Edge uses V8 via the Chromium project.
- *Why D is correct:* V8 is Google's open-source JavaScript engine, used in Chrome, Microsoft Edge (Chromium), Opera, and the Node.js server-side runtime.

---

### Question 13

A developer writes `type="text/javascript"` on their `<script>` tag in an HTML5 document. What is the effect?

- A) It enables strict mode for that script
- B) It makes the script execute faster
- C) It has no effect; `type="text/javascript"` is the default and is unnecessary in HTML5
- D) It causes the browser to interpret the content as plain text rather than executing it

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Strict mode is enabled by writing `'use strict';` as the first statement inside a script or function. The `type` attribute does not control strict mode.
- *Why B is incorrect:* The `type` attribute has no impact on engine optimization or execution speed.
- *Why C is correct:* In HTML5, `text/javascript` is the default MIME type for script elements. Writing `type="text/javascript"` is perfectly valid but entirely redundant. Most style guides and linters flag it as unnecessary.
- *Why D is incorrect:* `type="text/plain"` would prevent execution by telling the browser to treat the content as plain text. `type="text/javascript"` is the opposite — it explicitly declares the content as JavaScript, which is also the default.

---

### Question 14

What happens when a JavaScript runtime encounters a **syntax error** during the parsing phase?

- A) The engine skips the malformed line and continues executing the rest of the script
- B) The engine logs a warning and replaces the syntax error with a no-op
- C) The engine throws a `SyntaxError` and the entire script fails to execute
- D) The engine attempts to auto-correct the error using ASI before failing

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* JavaScript does not skip syntax errors. A syntax error in any part of a script prevents the entire script from being parsed and executed.
- *Why B is incorrect:* The engine does not substitute no-ops for invalid syntax. A syntax error is fatal to the script.
- *Why C is correct:* Parsing happens before any code runs. If the parser finds a syntax error — a piece of code that violates the grammatical rules of the language — it throws a `SyntaxError`. Because parsing must succeed before execution begins, no part of that script runs.
- *Why D is incorrect:* Automatic Semicolon Insertion (ASI) handles only missing semicolons in specific locations defined by the grammar. It does not correct arbitrary syntax errors such as mismatched braces, invalid operator sequences, or malformed expressions.

---

### Question 15

Which statement correctly describes **Node.js**?

- A) A browser plugin that extends Chrome's JavaScript capabilities
- B) A server-side JavaScript runtime built on the V8 engine
- C) A JavaScript testing framework for unit tests
- D) An alternative to HTML and CSS for building web pages

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Node.js is not a browser plugin. It is a standalone runtime installed on a server or developer machine, completely separate from any browser.
- *Why B is correct:* Node.js is an open-source runtime environment that runs JavaScript outside the browser, on servers or desktop machines. It is built on Chrome's V8 engine and provides APIs for file system access, networking, and more — capabilities unavailable to in-browser JavaScript.
- *Why C is incorrect:* While test frameworks like Jest run on Node.js, Node.js itself is a general-purpose runtime, not a testing framework.
- *Why D is incorrect:* Node.js is a JavaScript runtime, not a markup or styling technology. It has no relationship to HTML or CSS.

---

### Question 16

Consider the following code. What is the output in the browser console?

```javascript
console.log(typeof 42);
console.log(typeof 'hello');
console.log(typeof true);
```

- A) `number` then `string` then `boolean`
- B) `Number` then `String` then `Boolean`
- C) `int` then `char` then `bool`
- D) `42` then `hello` then `true`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The `typeof` operator returns a lowercase string identifying the type of its operand. `typeof 42` returns `"number"`, `typeof 'hello'` returns `"string"`, and `typeof true` returns `"boolean"`. These are the exact string values defined by the ECMAScript specification.
- *Why B is incorrect:* JavaScript type names returned by `typeof` are all lowercase. `"Number"`, `"String"`, and `"Boolean"` (capitalized) are the constructor function names, not the `typeof` result strings.
- *Why C is incorrect:* `int`, `char`, and `bool` are type names from languages like C or Java. JavaScript does not use these names.
- *Why D is incorrect:* `typeof` returns the type name, not the value itself.

---

### Question 17

What is **Automatic Semicolon Insertion (ASI)** in JavaScript?

- A) A feature that rewrites your code to follow a specific style guide automatically
- B) A mechanism where the parser inserts semicolons at certain line endings if they are missing
- C) An IDE feature in VS Code that adds semicolons when you press the Tab key
- D) A runtime process that adds semicolons to prevent stack overflow errors

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* ASI has nothing to do with code style or formatting. It is a grammatical rule in the language specification, not a linter or formatter.
- *Why B is correct:* ASI is a rule defined in the ECMAScript specification that instructs the parser to insert a semicolon automatically when a line ending is reached under specific conditions — typically when the parser would otherwise produce a syntax error. While ASI works correctly in most cases, it has well-known edge cases that can cause bugs, which is why explicit semicolons are recommended.
- *Why C is incorrect:* IDE code completion is separate from ASI. VS Code extensions and formatters may auto-insert semicolons, but that is not what the term "ASI" refers to.
- *Why D is incorrect:* ASI is a parse-time grammar rule, not a runtime mechanism, and has no relationship to stack overflow prevention.

---

### Question 18

Which browser tool is used to interactively type and evaluate JavaScript expressions without editing any file?

- A) The Elements panel in DevTools
- B) The Sources panel in DevTools
- C) The Console tab in DevTools
- D) The Network panel in DevTools

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The Elements panel shows the live DOM tree and CSS styles. It allows you to inspect and edit HTML/CSS visually but does not execute JavaScript expressions.
- *Why B is incorrect:* The Sources panel displays the JavaScript source files, allows setting breakpoints, and stepping through code — but it is for reading and debugging files, not for evaluating ad-hoc expressions.
- *Why C is correct:* The Console tab contains a REPL (Read-Eval-Print Loop) input prompt. Any JavaScript expression you type and press Enter is immediately evaluated by the V8 engine and the result is displayed. Variables declared here persist in the console's global scope for the rest of the session.
- *Why D is incorrect:* The Network panel shows HTTP request and response traffic. It is used for performance analysis and API debugging, not for executing JavaScript.

---

### Question 19

What does the **Abstract Syntax Tree (AST)** represent during JavaScript parsing?

- A) The visual hierarchy of HTML elements on the page
- B) A tree data structure representing the syntactic structure of the source code
- C) A list of all variables declared in the program sorted alphabetically
- D) The call stack state at a given point during execution

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The DOM (Document Object Model) represents the hierarchy of HTML elements. The AST is a separate concept that represents the structure of JavaScript code, not HTML elements.
- *Why B is correct:* The AST is a tree-shaped data structure the parser builds by analyzing JavaScript source code. Each node in the tree represents a syntactic construct — a variable declaration, a function call, a binary expression, etc. The engine uses the AST to generate machine code during JIT compilation.
- *Why C is incorrect:* Variable names are captured in scope records and symbol tables during compilation, not in the AST directly. The AST represents the full program structure, not just a list of variables.
- *Why D is incorrect:* The call stack is a runtime concept — a record of which function contexts are currently active during execution. The AST is a compile-time concept created before any code runs.

---

### Question 20

A developer links two external scripts in the `<head>` of their HTML, both with the `defer` attribute:

```html
<script src="utility.js" defer></script>
<script src="main.js" defer></script>
```

In what order will these scripts execute relative to each other?

- A) `main.js` first, then `utility.js` — `defer` reverses document order
- B) Whichever finishes downloading first executes first — order is unpredictable
- C) `utility.js` first, then `main.js` — `defer` preserves document order
- D) Both execute simultaneously in parallel threads

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `defer` does not reverse order. It explicitly preserves the document order of execution.
- *Why B is incorrect:* That describes the behavior of `async`, not `defer`. With `async`, scripts execute as soon as they download regardless of order. With `defer`, the browser waits until all deferred scripts have downloaded and the HTML is fully parsed, then executes them in document order.
- *Why C is correct:* The ECMAScript and HTML specifications guarantee that multiple `defer` scripts execute in the order they appear in the document. `utility.js` appears first and will execute first; `main.js` executes second. This is why `defer` is preferred when one script depends on another.
- *Why D is incorrect:* JavaScript is single-threaded. Scripts cannot execute simultaneously. Even if two scripts download in parallel (network requests are concurrent), their execution happens sequentially on the single JavaScript thread.
