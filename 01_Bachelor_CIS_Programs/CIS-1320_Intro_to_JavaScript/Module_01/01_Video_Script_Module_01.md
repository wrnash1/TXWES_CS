# Video Script: CIS-1320 — Introduction to JavaScript

## Module 01 — JavaScript Introduction and Execution

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use screen-share for all [DEMO] sections. Open VS Code and Chrome side-by-side.
> - [PAUSE] = hold 2 seconds of silence for emphasis or student note-taking.
> - Keep DevTools open throughout the demos — normalize it as part of the workflow.
> - Emphasize the `defer` pattern early. Students will use it in every lab this semester.
> - End with a clear summary of what the lab will ask them to do.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 01 | JavaScript Introduction and Execution | CIS-1320"]**

"Welcome to CIS-1320 — Introduction to JavaScript. I am Professor Nash, and over the next sixteen modules we are going to take you from writing your first line of JavaScript all the way through objects, arrays, DOM manipulation, asynchronous programming, and error handling — everything you need to earn the JSE certification from the JS Institute.

Module 01 is where we start at the very beginning. Today you will learn what JavaScript is, where it runs, how to get it into a web page, and how to use the browser developer tools to see your code working in real time. No prior experience required. Let us get started."

---

## [01:00 – 03:30] Part 1 — What Is JavaScript and Where Does It Run?

**[SHOW SLIDE: "JavaScript — The Language of the Web"]**

"JavaScript was created in 1995 by Brendan Eich at Netscape. The original goal was to add interactivity to web pages — things like validating a form before it is submitted, responding to a button click, or updating part of a page without reloading everything.

Today, JavaScript is one of the most widely used programming languages in the world. It runs in every web browser. It runs on servers through Node.js. It runs on mobile devices, smart TVs, and IoT hardware. But this course focuses on where it all started: the browser.

[PAUSE]

The most important concept for this module is the difference between **client-side** and **server-side** execution.

When you load a web page, your browser downloads HTML, CSS, and JavaScript from a web server. The HTML and CSS describe the structure and appearance of the page. The JavaScript runs inside **your browser** — on your computer, not the server. That is what client-side means. The code executes on the client, which is you.

When a form is submitted and the server runs code to validate it and store data in a database — that is server-side. Server-side JavaScript exists through Node.js, but in this course we are focused on the browser.

[PAUSE]

The component of the browser that actually reads and runs your JavaScript is called the **JavaScript engine**. Every major browser has one. Chrome uses a JS engine called V8. Firefox uses SpiderMonkey. Safari uses JavaScriptCore. These engines all do the same fundamental job: they receive your JavaScript source code, parse it, compile it, and execute it.

You do not need to interact with the engine directly — it runs automatically when your page loads. But understanding that it exists helps you understand why JavaScript behaves the way it does."

---

## [03:30 – 06:30] Part 2 — Three Ways to Include JavaScript in a Page

**[SHOW SLIDE: "Embedding JavaScript: Three Methods"]**

"To write JavaScript that runs in a browser, you need to get your code into an HTML file. There are three ways to do this.

**[DEMO — VS Code open with a blank HTML file]**

**Method 1: Inline JavaScript.**

This means writing JavaScript directly inside an HTML attribute — typically an event handler attribute like `onclick`.

```html
<button onclick="alert('Button clicked!')">Click me</button>
```

This works, and you will see it in legacy code. But it mixes your HTML and your JavaScript in the same place, which makes both harder to read and maintain. We avoid this pattern in modern development. The JSE exam expects you to know it exists, but not to use it as your primary approach.

[PAUSE]

**Method 2: Internal script block.**

You add a `<script>` element directly inside your HTML file and write your JavaScript between the opening and closing tags.

```html
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>My First Script</title>
</head>
<body>
  <h1>Hello</h1>

  <script>
    console.log('Script is running!');
  </script>
</body>
```

This keeps all your code in one file, which is convenient when you are learning or prototyping. For a small project or a single-page demo, this is perfectly acceptable.

[PAUSE]

**Method 3: External JavaScript file.**

This is the professional pattern. You write your JavaScript in a separate `.js` file and link it to your HTML using the `src` attribute on the `<script>` tag.

```html
<script src='app.js'></script>
```

And in `app.js`:

```javascript
console.log('External script loaded!');
```

The browser downloads `app.js` and executes it. The benefit is separation of concerns — your HTML handles structure, your CSS handles presentation, and your JavaScript handles behavior. This also lets multiple HTML pages share the same script file.

[PAUSE]

For this course, you will almost always use the external file approach. The exceptions are small demo experiments in the lab, where an internal script block is fine."

---

## [06:30 – 09:30] Part 3 — Script Tag Placement Matters

**[SHOW SLIDE: "Where You Put the Script Tag Changes What Happens"]**

"This is one of the most-tested concepts on the JSE exam, and it is also one that trips up real developers. Where you place your `<script>` tag in the HTML file determines when your JavaScript runs — and whether the DOM elements it needs actually exist yet.

[PAUSE]

Let me show you the problem.

**[DEMO — create index.html, script in `<head>`]**

```html
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Placement Demo</title>
  <script src='app.js'></script>
</head>
<body>
  <p id='message'>Hello from HTML</p>
</body>
</html>
```

And in `app.js`:

```javascript
const el = document.getElementById('message');
console.log(el);
```

Let me open this in Chrome and press F12 to open DevTools.

**[SHOW BROWSER — console shows `null`]**

The console shows `null`. The script ran when the browser was still in the `<head>` — before it ever read the `<p>` element in the `<body>`. The element did not exist yet when the script asked for it.

[PAUSE]

There are two common solutions. The old approach was to move the `<script>` tag to the **bottom of the `<body>`**, just before the closing `</body>` tag. By that point the browser has parsed all the HTML, so all the DOM elements exist.

The **modern approach** — and the one you will use in this course — is to keep the `<script>` in the `<head>` but add the `defer` attribute.

```html
<script src='app.js' defer></script>
```

`defer` tells the browser: download this script file in parallel while you continue parsing the HTML, and then execute it after the entire HTML document has been fully parsed. The script runs at the right time, and the download happens efficiently in the background.

**[DEMO — add `defer`, reload, console shows the paragraph element]**

Now the console shows the paragraph element correctly. That is `defer` in action.

[PAUSE]

There is also an `async` attribute. `async` downloads the script in parallel like `defer`, but executes it immediately when the download finishes — before the HTML is necessarily done parsing. This is useful for scripts that are completely independent of the DOM, like analytics trackers. For any script that touches the DOM, use `defer`, not `async`.

The rule is simple: **external scripts that interact with the page → `defer` in the `<head>`.**"

---

## [09:30 – 12:00] Part 4 — The Browser Console and `console.log`

**[SHOW SLIDE: "DevTools: Your Primary Development Tool"]**

"Let me spend a few minutes on the browser developer tools, because you will use these every single day as a JavaScript developer.

In Chrome — or any browser — press **F12**, or right-click anywhere on the page and choose Inspect. This opens DevTools. The tab we care about most right now is the **Console** tab.

**[DEMO — DevTools open, Console tab visible]**

The console is where your `console.log()` output appears. It is also where JavaScript errors get reported. And it is an interactive prompt — you can type JavaScript directly into the console and execute it immediately.

`console.log()` is a method that writes output to the console. You can pass it any value: a string, a number, a variable, or multiple values separated by commas.

```javascript
console.log('Hello, World!');
console.log(42);
console.log('Score:', 100);
console.log(2 + 3);
```

**[DEMO — type these into the console live, show results]**

Each of these prints immediately.

[PAUSE]

There are also `console.error()` and `console.warn()`. They work the same way but display with different formatting — errors show in red, warnings show in yellow. This makes it easy to spot problems in a busy console log.

```javascript
console.error('Something went wrong!');
console.warn('This value is unexpected.');
```

For the JSE exam: `console.log()` is used for general output and debugging. It is not shown to the end user — it only appears in DevTools. It does not modify the HTML page. It simply prints to the console."

---

## [12:00 – 14:00] Part 5 — Statements, Expressions, and Comments

**[SHOW SLIDE: "The Building Blocks of a JavaScript Program"]**

"Before we close out this module, let me introduce two foundational vocabulary terms you will see throughout the course.

A **statement** is a complete instruction that the JavaScript engine executes. Statements are the sentences of your program.

```javascript
let x = 5;               // variable declaration statement
console.log(x);          // expression statement
if (x > 3) {             // if statement
  console.log('big');
}
```

An **expression** is any piece of code that produces a value. Expressions can appear inside statements.

```javascript
2 + 3         // expression — produces 5
'Hello'       // expression — produces the string 'Hello'
x * 2         // expression — produces a number
```

Every expression is a value. Not every statement is an expression. That distinction will matter when we get to functions.

[PAUSE]

JavaScript also supports two comment styles:

```javascript
// This is a single-line comment. The engine ignores everything after //

/*
  This is a multi-line comment.
  It can span multiple lines.
  Use this for longer explanations.
*/
```

Comments are for humans, not the engine. Use them to explain why your code does something — especially when the logic is not immediately obvious.

[PAUSE]

One last thing about syntax: JavaScript statements can optionally end with a semicolon. The language has a feature called **Automatic Semicolon Insertion** that adds them in certain places if you leave them out. In this course, we always write semicolons explicitly. It prevents a class of subtle bugs and is considered a best practice."

---

## [14:00 – 15:30] Closing — What the Lab Covers

**[SHOW SLIDE: "Module 01 Lab Preview"]**

"This module's lab has four parts. You will build everything in VS Code and test it in your browser.

In Part 1, you will create your first HTML file with an internal script block, write your first `console.log()` statements, and verify the output in DevTools.

In Part 2, you will explore the DevTools Console interactively — running JavaScript expressions directly in the console and observing the output.

In Part 3, you will refactor your internal script to an external `.js` file, link it with a `<script src>` tag, and verify it still works.

In Part 4, you will experience the script-placement problem first-hand — a `<head>` script without `defer` returning `null` — and then fix it with `defer`.

Each part has a screenshot requirement. Open DevTools before you start and keep it open throughout.

The reading guide for this module covers all of today's concepts in detail: the JS engine, embedding methods, placement and `defer`, `console.log`, execution context, and the call stack. Work through the reading guide before starting the lab.

I will see you in Module 02. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 01 — JavaScript Introduction and Execution]**

---

## Additional Resources

- [MDN Web Docs — How JavaScript Works](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript) — authoritative overview of JavaScript in the browser
- [Eloquent JavaScript — Introduction](https://eloquentjavascript.net/00_intro.html) — free textbook introduction chapter
- [JavaScript.info — An Introduction to JavaScript](https://javascript.info/intro) — concise explanation of what JavaScript is and where it runs
- [Chrome DevTools Documentation](https://developer.chrome.com/docs/devtools/) — official guide to the browser developer tools
