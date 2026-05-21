# Reading Guide: Module 01 - JavaScript Introduction & Execution
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 01 - JavaScript Introduction & Execution**! This week you will learn how JavaScript runs inside the browser, how to embed it in an HTML page, and how to use the browser console to observe program output. These fundamentals are the foundation for every concept tested on the JSE exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Script tag**: The HTML `<script>` element used to embed or link JavaScript code in a web page. It can appear in the `<head>` or `<body>`, and its placement affects when the script is parsed and executed relative to the page's HTML content.
*   **Client-side**: Code that runs in the user's web browser rather than on a server. JavaScript is the primary client-side programming language of the web, giving pages interactivity without requiring a round-trip to a server for every action.
*   **JS engine**: The runtime component of a browser (e.g., V8 in Chrome, SpiderMonkey in Firefox) that parses, compiles, and executes JavaScript code. Modern JS engines use just-in-time (JIT) compilation to convert JS source to machine instructions.
*   **console.log**: A built-in method that writes output to the browser's developer console. It is the primary tool for inspecting variable values, tracing execution flow, and debugging scripts during development.
*   **Execution context**: The internal environment that the JS engine creates to run a piece of code, containing the local variables, the value of `this`, and a reference to the outer scope. Every function call creates a new execution context pushed onto the call stack.
*   **Statements**: Individual instructions that the JavaScript engine executes in sequence. A statement typically ends with a semicolon and can be a declaration, an expression, a control structure, or a function call.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests whether you know *where* to place `<script>` tags and *why* placement matters (blocking HTML parsing). Know the difference between inline scripts and external `.js` files linked via the `src` attribute.
*   **Scenario Trap:** A common question shows code that runs before the DOM element it references exists. Recognize that a `<script>` in the `<head>` without `defer` or `async` will execute before `<body>` elements are available, causing `null` references.
*   **Study Resource:** For a concise visual walkthrough of how the JavaScript engine and browser work together, watch the free video series at [JavaScript.info — An Introduction to JavaScript](https://javascript.info/intro) (read the "Introduction" chapter; approximately 10 minutes).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 1 – Values, Types, and Operators** and the Introduction of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter establishes the basic vocabulary of JS you will use all semester.
*   **Required Video:** Watch the video lecture on **JavaScript Introduction & Execution** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (freeCodeCamp full-course video; watch the first ~30 minutes covering JS basics and setup).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a basic HTML page with an inline script tag**: Open VS Code, create `index.html`, add a `<script>` block inside the `<body>`, and verify the file opens in a browser.
*   **Use console.log to print "Hello, World!"**: Inside your script, write `console.log("Hello, World!");` and confirm the message appears in the browser's DevTools Console (F12).
*   **Verify script execution in browser console**: Open DevTools, switch to the Console tab, and observe that your log statement output appears without errors.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 1 and the Introduction of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the first ~30 minutes of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
