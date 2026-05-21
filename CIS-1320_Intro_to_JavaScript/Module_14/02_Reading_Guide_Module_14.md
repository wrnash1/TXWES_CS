# Reading Guide: Module 14 - Promises & Async/Await
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 14 - Promises & Async/Await**! This week you will learn JavaScript's modern approach to handling asynchronous operations. Promises replace "callback hell" with a clean, chainable interface, and the ES2017 `async`/`await` syntax makes asynchronous code read almost like synchronous code. Both are heavily tested on the JSE exam and are used in every real-world web application.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Promise state**: A Promise is always in one of three mutually exclusive states: `pending` (the operation has not completed yet), `fulfilled` (the operation succeeded and a value is available), or `rejected` (the operation failed and a reason/error is available). Once a Promise transitions from `pending` to either `fulfilled` or `rejected`, it is "settled" and its state cannot change.
*   **resolve/reject**: The two functions passed as arguments to a Promise's executor function. Calling `resolve(value)` transitions the Promise to `fulfilled` with that value; calling `reject(reason)` transitions it to `rejected` with that reason/error.
*   **then/catch**: Instance methods on a Promise used to register callbacks. `.then(onFulfilled, onRejected)` registers a handler that runs when the Promise is fulfilled. `.catch(onRejected)` is shorthand for `.then(null, onRejected)` and handles rejections. Both return a new Promise, enabling chaining.
*   **async keyword**: A keyword placed before a function declaration or expression to mark it as asynchronous. An `async` function always returns a Promise, even if its body `return`s a plain value (which is wrapped automatically). It enables the use of `await` inside the function.
*   **await expression**: An operator used inside an `async` function to pause execution of that function until a Promise resolves. The expression `const data = await fetch(url)` suspends only the enclosing `async` function — other code in the program continues running. If the awaited Promise rejects, the error can be caught with `try/catch`.
*   **fetch API**: A modern, Promise-based browser API for making HTTP requests: `fetch(url)` returns a Promise that resolves to a `Response` object. The response body must be parsed separately (e.g., `response.json()` returns another Promise). It replaces the older `XMLHttpRequest` API.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests Promise chaining. Understand that each `.then()` returns a new Promise, and the value returned from a `.then()` callback becomes the resolved value of that new Promise, available to the next `.then()` in the chain. Returning a new Promise from `.then()` causes the chain to wait for it.
*   **Scenario Trap:** A common mistake is forgetting to `return` inside a `.then()` callback. Without `return`, the next `.then()` in the chain receives `undefined` as its value. The exam may show a chain where data silently disappears because of a missing `return`.
*   **Study Resource:** [javascript.info – Promises, async/await](https://javascript.info/async) is a comprehensive chapter with clear diagrams of Promise states and chaining. Work through the interactive tasks at the end of the "Promise chaining" page before the lab — they are very similar to JSE exam questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 11 – Asynchronous Programming** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). The "Promises" and "Async Functions" sections explain the concepts this module builds on.
*   **Required Video:** Watch the video lecture on **Promises & Async/Await** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on Promise creation, `.then`/`.catch` chaining, `async`/`await`, and the Fetch API).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create and resolve a custom Promise**: Write `new Promise((resolve, reject) => { setTimeout(() => resolve("done"), 1000); })` and attach a `.then()` to log the result.
*   **Fetch data from a public API using fetch and then()**: Use `fetch("https://api.github.com/users/octocat")` followed by `.then(r => r.json()).then(data => console.log(data.name))` to retrieve and display a GitHub user's name.
*   **Refactor fetch calls using async/await syntax**: Convert the Fetch chain from the previous step into an `async` function using `await` and wrap it in `try/catch` to handle network errors.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the Promises and async/await sections of Chapter 11 in [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the Promises, async/await, and Fetch API segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
