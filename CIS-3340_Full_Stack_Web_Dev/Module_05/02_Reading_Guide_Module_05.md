# Reading Guide: Module 05 - Asynchronous JavaScript
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 05 - Asynchronous JavaScript**! This module covers how JavaScript manages operations that take time to complete — such as network requests, file reads, and timers — without freezing the browser UI. You will learn the call stack, the event loop, callback patterns, Promises, and the modern `async`/`await` syntax that makes asynchronous code readable and maintainable. Asynchronous programming is central to every full-stack application: your React front-end will use `fetch()` with async/await to call AWS API Gateway endpoints, and your Node.js server will use async patterns for database queries and S3 operations.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Call stack**: The LIFO (Last In, First Out) data structure that the JavaScript engine uses to track the execution context of currently running functions. When a function is invoked, a new frame is pushed onto the stack; when it returns, its frame is popped. Because JavaScript is single-threaded, only one function executes at a time — whatever is on top of the call stack.
*   **Event loop**: The browser mechanism that continuously monitors both the call stack and the callback queue (also called the task queue). When the call stack is empty, the event loop picks the next callback from the queue and pushes it onto the stack for execution. This is how asynchronous callbacks (from `setTimeout`, `fetch`, DOM events, etc.) are eventually executed without blocking synchronous code.
*   **Callback queue**: The queue where asynchronous callback functions wait until the call stack is empty and the event loop can schedule them. `setTimeout` callbacks, `setInterval` handlers, and resolved I/O callbacks are placed in this queue (or the microtask queue, in the case of Promises) after their triggering condition is met.
*   **Promises**: Objects that represent the eventual result (or failure) of an asynchronous operation. A Promise can be in one of three states: **Pending** (operation in progress), **Fulfilled** (operation completed successfully with a value), or **Rejected** (operation failed with a reason/error). Promises are chained with `.then()` for success handlers and `.catch()` for error handlers, enabling sequential async operations without deeply nested callbacks.
*   **async/await constructs**: Syntactic sugar built on top of Promises that allows asynchronous code to be written in a synchronous-looking style. An `async` function always returns a Promise. Inside it, `await` pauses execution of that function until the awaited Promise settles, then resumes with the resolved value. `try`/`catch` blocks handle rejections, making error handling clean and readable.
*   **Error handling**: The practice of anticipating and gracefully managing failures in asynchronous operations using `.catch()` on Promise chains or `try`/`catch` blocks inside `async` functions. Unhandled Promise rejections cause silent failures in production applications — always attach error handling to every asynchronous operation.

---

### 2. Certification Exam Tips
*   **Async Patterns in AWS SDK Calls:** The DVA-C02 exam frequently presents scenarios involving the AWS SDK for JavaScript (v3), which uses Promises and async/await for all service calls — including `S3Client.send()`, `DynamoDBClient.send()`, and `LambdaClient.send()`. Understanding how async/await works is required to write and debug Lambda functions that call other AWS services.
*   **Lambda Execution Context and the Event Loop:** AWS Lambda functions are executed synchronously from the runtime's perspective — a Lambda handler that returns before all async operations complete will silently drop results. Always `await` all async operations inside a Lambda handler, or return a Promise that resolves only after all work is complete.
*   **Study Resource:** The MDN guide on Promises is the most thorough free reference. [MDN — Using Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) covers chaining, error handling, and common pitfalls like forgetting to `return` a Promise inside `.then()`.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Asynchronous JavaScript** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/) — Parts 2 and 3 cover fetching data and Node.js async patterns extensively.
*   **Required Video:** Watch the async JavaScript section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering callbacks, Promises, and async/await with practical examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will apply asynchronous JavaScript concepts directly:
*   **Write callback loops**: Implement `setTimeout`-based delayed callbacks and nested callbacks to observe callback sequencing — then identify the "callback hell" problem that Promises solve.
*   **Write fetch calls returning Promises**: Use `fetch('https://jsonplaceholder.typicode.com/todos/1')` to make an HTTP GET request, chain `.then(res => res.json())` to parse the JSON response, and chain a second `.then()` to render the data to the DOM.
*   **Refactor promises using async/await syntax and try-catch blocks**: Convert your `.then()` Promise chain into an `async` function using `await` for each asynchronous step, and wrap the entire function body in a `try`/`catch` block to handle network errors gracefully.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read the section covering **Asynchronous JavaScript** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/).
- [ ] Watch the async JavaScript section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Experiment with `fetch()` in the browser Console against a public API (e.g., `https://api.github.com/users/github`) before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
