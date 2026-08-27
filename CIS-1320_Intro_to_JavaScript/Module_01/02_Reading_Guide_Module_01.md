# Reading Guide: Module 01 — JavaScript Introduction and Execution

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Module 01 establishes the foundation on which every subsequent topic in this course is built. Before you can write programs that respond to user input, manipulate web pages, or fetch data from a server, you need to understand what JavaScript is, where it executes, and how to connect it to an HTML document. This reading guide covers those fundamentals in the depth required for both the JSE certification exam and real-world development practice.

Work through each section actively. When you encounter a code example, trace through it mentally before reading the explanation.

---

## 1. What JavaScript Is

JavaScript is a high-level, interpreted programming language originally created in 1995 by Brendan Eich while working at Netscape Communications. The original goal was modest: add small interactive behaviors to web pages, like validating a form before it was submitted. What Eich built in ten days became the only programming language natively supported by all web browsers, and today JavaScript is one of the most widely deployed languages in the world.

### ECMAScript — The Standard

JavaScript is an implementation of a standard called **ECMAScript**, maintained by a technical committee called TC39. ECMAScript defines the core language rules: syntax, data types, operators, and built-in objects. Browser vendors then implement that standard in their engines. When you hear "ES6" or "ES2015," that refers to the sixth edition of the ECMAScript standard, which introduced many of the modern features covered in this course (`let`, `const`, arrow functions, classes, and more).

The terms "JavaScript" and "ECMAScript" are often used interchangeably. Technically, ECMAScript is the standard; JavaScript is the name of the language as implemented in browsers.

### Where JavaScript Runs

JavaScript can run in two broad environments:

| Environment | Description | Examples |
|---|---|---|
| Browser (client-side) | Runs inside the user's web browser | Chrome, Firefox, Safari, Edge |
| Server-side | Runs outside the browser via a runtime | Node.js, Deno |

This course focuses on the browser environment. When you open a web page, your browser downloads HTML, CSS, and JavaScript. The HTML defines the structure of the page. The CSS defines the visual appearance. The JavaScript defines the behavior — what happens when a user clicks a button, types in a field, or scrolls the page. Because this code runs on the visitor's machine (the "client"), it is called **client-side** JavaScript.

---

## 2. The JavaScript Engine

Every browser contains a **JavaScript engine** — a specialized runtime that reads your JavaScript source code and executes it. The major engines are:

| Engine | Browser / Runtime |
|---|---|
| V8 | Google Chrome, Microsoft Edge, Node.js |
| SpiderMonkey | Mozilla Firefox |
| JavaScriptCore | Apple Safari |
| Chakra | Legacy Microsoft Edge (pre-Chromium) |

You do not interact with the engine directly; it runs automatically. But understanding what the engine does helps you reason about performance and behavior.

### How the Engine Processes Code

Modern JS engines use a multi-phase pipeline:

1. **Parsing** — The engine reads the source code character by character and builds an internal data structure called an Abstract Syntax Tree (AST). The AST represents the structure of your program. If the code has a syntax error, parsing fails here.

2. **Compilation (Just-In-Time, JIT)** — Unlike older interpreted languages that execute code line by line, modern JS engines compile code to optimized machine instructions before execution. This compilation happens at runtime — hence "just-in-time." The result is significantly faster execution than pure interpretation.

3. **Execution** — The compiled machine code runs. Variables are created, expressions are evaluated, functions are called.

This pipeline means JavaScript is both compiled and interpreted: you write source code (which is human-readable), the engine compiles it, and executes it — all happening in milliseconds when a page loads.

---

## 3. Three Ways to Include JavaScript in a Web Page

JavaScript code must be connected to an HTML document for the browser to load and run it. There are three methods. Each has appropriate use cases.

### Method 1 — Inline JavaScript (Avoid)

Inline JavaScript is written directly inside an HTML element's event attribute:

```html
<button onclick="alert('Clicked!')">Click me</button>
```

This works but violates the principle of **separation of concerns** — the idea that HTML (structure), CSS (presentation), and JavaScript (behavior) should live in separate files or blocks. Inline JavaScript is hard to maintain, hard to test, and considered poor practice in modern development. You will encounter it in old code; do not write it in new code.

### Method 2 — Internal Script Block

An internal script block places JavaScript directly inside the HTML file using `<script>` tags:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Internal Script Demo</title>
</head>
<body>
  <h1>My Page</h1>

  <script>
    console.log('Hello from an internal script!');
    const greeting = 'Welcome';
    console.log(greeting);
  </script>
</body>
```

Everything between `<script>` and `</script>` is JavaScript. The browser's parser switches from HTML parsing mode to JavaScript execution mode when it encounters the opening `<script>` tag.

Internal scripts are convenient for small prototypes or learning exercises where having a single self-contained file is useful. For production code, external files are preferred.

### Method 3 — External JavaScript File (Preferred)

The external approach separates JavaScript into its own `.js` file and links it to the HTML page:

**index.html:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>External Script Demo</title>
  <script src="app.js" defer></script>
</head>
<body>
  <h1>My Page</h1>
  <p id="message">Hello</p>
</body>
</html>
```

**app.js:**

```javascript
const el = document.getElementById('message');
console.log(el.textContent);   // Hello
```

The `src` attribute specifies the path to the JavaScript file, relative to the HTML file. The browser downloads and executes `app.js` when it processes the `<script>` tag.

Benefits of external files:

- Clean separation of structure and behavior
- A single `.js` file can be linked from multiple HTML pages
- Browsers cache external files, improving performance on repeat visits
- Code is easier to read, test, and maintain

---

## 4. Script Tag Placement and Execution Timing

Where you place the `<script>` tag in the HTML document determines *when* the JavaScript runs relative to the HTML parsing. This is a heavily tested JSE exam concept and a practical concern in every project.

### The Problem with `<head>` Placement (Without `defer`)

When the browser encounters a `<script>` tag during HTML parsing, it **stops** parsing the HTML and executes the script immediately. If your script tries to access a DOM element that hasn't been parsed yet, the element does not exist — you get `null`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <script src="app.js"></script>   <!-- runs before <body> is parsed -->
</head>
<body>
  <p id="greeting">Hello</p>      <!-- doesn't exist yet when script runs -->
</body>
</html>
```

```javascript
// app.js
const el = document.getElementById('greeting');
console.log(el);   // null — the <p> doesn't exist yet
```

This is the classic null-reference mistake caused by script placement.

### Solution 1 — Bottom of `<body>`

The traditional fix is to move the `<script>` tag to the very bottom of the `<body>`:

```html
<body>
  <p id="greeting">Hello</p>
  <!-- ... rest of page content ... -->

  <script src="app.js"></script>   <!-- all DOM elements exist by here -->
</body>
```

The script runs after the browser has parsed all the HTML. This approach works, but it delays the *start* of downloading the script until the HTML is almost fully parsed, which can be slightly slower.

### Solution 2 — `defer` Attribute (Recommended)

The modern approach uses the `defer` attribute on a `<script>` tag in the `<head>`:

```html
<head>
  <script src="app.js" defer></script>
</head>
```

`defer` instructs the browser to:

1. **Download** `app.js` in parallel while HTML parsing continues (no blocking)
2. **Execute** `app.js` after the entire HTML document has been fully parsed

The result: the script downloads efficiently and runs at the right time, with full access to all DOM elements. Multiple `defer` scripts execute in the order they appear in the HTML.

### The `async` Attribute

A second attribute, `async`, also causes parallel downloading but has different execution timing:

```html
<head>
  <script src="analytics.js" async></script>
</head>
```

`async` executes the script immediately when its download completes, regardless of whether HTML parsing is finished. This is appropriate for scripts that are completely independent — like third-party analytics or advertisement scripts. It is **not** appropriate for scripts that read or modify DOM elements, because the DOM may not be ready.

### Comparison Table

| Placement / Attribute | Download | Execution timing | DOM available? | Order preserved? |
|---|---|---|---|---|
| `<head>` without attribute | Blocks parsing | Immediately during parse | No | Yes |
| End of `<body>` | After HTML parsed | After HTML parsed | Yes | Yes |
| `<head>` with `defer` | Parallel | After HTML parsed | Yes | Yes |
| `<head>` with `async` | Parallel | Immediately on download | Maybe | No |

**Rule of thumb:** Use `<script src="..." defer>` in the `<head>` for any script that interacts with the page.

---

## 5. The Browser Console and `console` Methods

The browser developer tools — opened with **F12** in Chrome and Firefox — provide a console that is central to JavaScript development. The Console tab shows script output and errors, and accepts interactive JavaScript input.

### `console.log()`

`console.log()` writes output to the console. It accepts any number of arguments separated by commas:

```javascript
console.log('Hello, World!');          // Hello, World!
console.log(42);                       // 42
console.log(2 + 3);                    // 5
console.log('Value:', 42, 'and', 99);  // Value: 42 and 99
console.log(true, false, null);        // true false null
```

`console.log()` is the primary tool for:

- Verifying that your code ran a particular line
- Inspecting variable values at a specific point in execution
- Tracing the flow of logic through a program

It is a debugging tool, not a user-facing output method. End users do not see the console unless they open DevTools themselves.

### Other `console` Methods

| Method | Purpose | Output Style |
|---|---|---|
| `console.log()` | General output and debugging | Plain text |
| `console.error()` | Error messages | Red with error icon |
| `console.warn()` | Warning messages | Yellow with warning icon |
| `console.info()` | Informational messages | Blue info icon |
| `console.dir()` | Shows object properties in a tree | Interactive expandable tree |
| `console.table()` | Shows array/object as a table | Tabular layout |

```javascript
console.error('File not found');
console.warn('Deprecated function called');
console.table([{name: 'Alice', score: 95}, {name: 'Bob', score: 87}]);
```

### The Interactive Console Prompt

You can type JavaScript directly into the Console tab and press Enter to execute it immediately. This is useful for quick experiments:

```text
> 2 + 2
  4
> 'Hello'.toUpperCase()
  'HELLO'
> let x = 10; x * 3
  30
```

Each expression you type is evaluated and the result is printed on the line below.

---

## 6. Execution Context and the Call Stack

### Execution Context

When the JavaScript engine runs a piece of code, it creates an **execution context** — an internal environment that contains:

- All variables and function declarations available in that scope
- The value of the `this` keyword
- A reference to the outer scope

The first execution context created is the **Global Execution Context (GEC)**. It is created when the script first begins running and represents the top-level code — everything not inside a function.

Every time a **function is called**, the engine creates a new **Function Execution Context (FEC)** for that call. This context contains the function's local variables, its parameters, and its own `this` value.

### The Call Stack

Execution contexts are managed on the **call stack** — a Last-In, First-Out (LIFO) data structure. When a function is called, its context is *pushed* onto the stack. When the function returns, its context is *popped* off the stack. The engine always executes the context at the top of the stack.

```javascript
function greet(name) {
  return 'Hello, ' + name;
}

function welcome() {
  const result = greet('Alice');
  console.log(result);
}

welcome();
```

Execution order on the call stack:

1. Global context is created, `welcome` and `greet` are defined
2. `welcome()` is called → `welcome`'s context is pushed
3. Inside `welcome`, `greet('Alice')` is called → `greet`'s context is pushed
4. `greet` returns `'Hello, Alice'` → `greet`'s context is popped
5. `console.log(result)` runs in `welcome`'s context
6. `welcome` returns → its context is popped
7. Stack returns to global context

Understanding the call stack becomes important when you read stack traces in error messages — they show you the exact chain of function calls that led to the error.

---

## 7. Statements and Expressions

### Statements

A **statement** is a complete instruction that the JavaScript engine executes. Statements form the "sentences" of your program. Every statement tells the engine to *do* something.

Common statement types:

```javascript
let x = 10;                    // variable declaration statement
x = 20;                        // assignment statement
console.log(x);                // expression statement (a call)
if (x > 5) { console.log('big'); }   // if statement
for (let i = 0; i < 3; i++) { }      // for statement
function greet() { }           // function declaration statement
return x;                      // return statement (inside a function)
```

In JavaScript, most statements end with a semicolon. The language has **Automatic Semicolon Insertion (ASI)** — a mechanism that adds semicolons in certain places if you omit them. However, ASI has edge cases that can introduce subtle bugs. Best practice is to always write semicolons explicitly.

### Expressions

An **expression** is any code that evaluates to a value. Expressions can appear inside statements.

```javascript
42                             // numeric literal — value: 42
'hello'                        // string literal — value: 'hello'
2 + 3                          // arithmetic expression — value: 5
x * 2                          // variable expression — value depends on x
'hello'.toUpperCase()          // method call expression — value: 'HELLO'
x > 5                          // comparison expression — value: true or false
```

A key distinction: an expression *produces* a value. A statement *performs* an action. Many statements contain expressions — for example, `console.log(x)` is an expression statement where `console.log(x)` is an expression (a function call that returns `undefined`).

---

## 8. JavaScript Comments

Comments are text in source code that the JavaScript engine ignores completely. They exist for human readers: you, your teammates, or your future self.

### Single-Line Comments

Use `//` for single-line comments. Everything from `//` to the end of that line is ignored:

```javascript
// This is a complete-line comment explaining what follows
let price = 9.99;   // This is an end-of-line comment

// console.log('This line is commented out and will not run');
```

### Multi-Line Comments

Use `/* */` for blocks that span multiple lines:

```javascript
/*
  This function calculates the area of a rectangle.
  Parameters:
    width  - the width of the rectangle
    height - the height of the rectangle
  Returns:
    The area as a number.
*/
function rectArea(width, height) {
  return width * height;
}
```

### When to Comment

Write comments to explain *why* — not *what*. The code already shows what it is doing. Comments should add context that the code cannot express by itself.

Good comment: `// Subtract 1 because array indexes start at 0`
Unhelpful comment: `// Add x and y` (directly before `return x + y`)

---

## 9. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module. All links are zero-cost and do not require account creation.

- **[MDN Web Docs — What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)**
  The definitive introductory article from Mozilla. Covers the history of JavaScript, client-side vs. server-side use cases, the browser execution model, and examples of what JavaScript can do. Essential reading for any beginner.

- **[Eloquent JavaScript — Introduction](https://eloquentjavascript.net/00_intro.html)**
  The free online textbook used as the primary OER for this course. The introduction chapter covers the philosophy of programming, what JavaScript is, and sets the context for everything covered in Module 01.

- **[javascript.info — An Introduction to JavaScript](https://javascript.info/intro)**
  A comprehensive, beginner-friendly resource. The "Introduction" section explains what JavaScript is, its relationship to ECMAScript, what it can and cannot do in the browser, and how it compares to other languages.

- **[MDN Web Docs — `<script>`: The Script element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)**
  Full reference documentation for the HTML `<script>` element, including all attributes (`src`, `defer`, `async`, `type`, `nomodule`), usage examples, and browser compatibility tables.

- **[Google Chrome DevTools — Console Overview](https://developer.chrome.com/docs/devtools/console/)**
  Google's official documentation for the Chrome DevTools Console. Covers the REPL, filtering output, `console` API methods, and best practices for using the console as a debugging tool.

---

## 10. JSE Certification Exam Tips

### Exam Format

The JSE (Certified Associate in JavaScript Programming) exam is delivered by the OpenEDG / JS Institute. Key parameters:

- **Questions:** approximately 30–45 multiple-choice and code-output questions
- **Time:** 45–75 minutes (varies by version)
- **Passing score:** 70%
- **Question types:** single-best-answer, multiple-correct-answer, code output, drag-and-drop, fill-in

### Module 01 Traps Most Tested on the Exam

1. **Script placement returns `null`.** A `<script>` in `<head>` without `defer` runs before `<body>` elements exist. `document.getElementById('x')` returns `null` in this case.

2. **`defer` vs. `async` distinction.** `defer` runs after full HTML parse, in order. `async` runs immediately on download, in any order. Know which is correct for DOM-dependent scripts.

3. **`console.log()` does not modify the page.** It writes to DevTools only — end users do not see it.

4. **The `src` attribute makes a script external.** The `type` attribute (`type="text/javascript"`) is optional in HTML5 and does not need to be written.

5. **Inline JavaScript in event attributes is a pattern to recognize, not to use.** Know that `onclick="..."` embeds JavaScript but is considered poor practice.

6. **Statements vs. expressions.** An expression produces a value. A statement performs an action. A function call can be either — it is an expression (produces a return value) that appears as an expression statement.

---

## 11. Study Checklist

- [ ] Watch the Module 01 video lecture by Professor Nash.
- [ ] Read the Introduction chapter of [Eloquent JavaScript](https://eloquentjavascript.net/00_intro.html).
- [ ] Read the [MDN article: What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [ ] Identify the JS engine used by the browser you will use for this course.
- [ ] Open browser DevTools (F12) and find the Console tab.
- [ ] Type three expressions directly into the console and observe the output.
- [ ] Memorize the `defer` vs. `async` comparison table above.
- [ ] Complete the Module 01 Lab.
- [ ] Complete the Module 01 Quiz.
