# Quiz: Module 15 - Error Handling & Debugging
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which block in a try/catch statement runs regardless of whether an exception was thrown or caught?
*   A) try
*   B) catch
*   C) finally
*   D) throw
*   **Correct Answer:** C) The `finally` block is executed immediately after try/catch, whether an error occurs or not.
*   **Distractor Analysis:**
    *   *Why correct:* The `finally` block is executed immediately after try/catch, whether an error occurs or not.
    *   try and catch execution depend on the occurrence of errors. throw launches an exception.

---

**Question 2**
Which of the following most accurately describes **developer tools** in the context of JavaScript debugging?
*   A) Third-party libraries (like React DevTools or Redux DevTools) that must be installed as browser extensions before they can be used
*   B) Built-in browser panels (Console, Sources, Network, Elements) opened with F12 that allow developers to log values, set breakpoints, step through code, and inspect network requests
*   C) A Node.js command-line utility that compiles and minifies JavaScript before deployment
*   D) A special IDE plugin available only in VS Code that highlights syntax errors before the code runs in a browser
*   **Correct Answer:** B) Built-in browser panels (Console, Sources, Network, Elements) opened with F12 that allow developers to log values, set breakpoints, step through code, and inspect network requests.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Browser DevTools are built-in and require no installation; third-party dev tools extensions are separate products.
    *   *Why B is correct:* Every modern browser ships with a complete DevTools suite accessible via F12 (or Cmd+Option+I on Mac) that includes all these panels for debugging.
    *   *Why C is incorrect:* That describes tools like webpack, esbuild, or the Node.js CLI — not browser DevTools.
    *   *Why D is incorrect:* Syntax highlighting and linting in VS Code are editor features; browser DevTools are runtime debugging tools that run in the browser.

---

**Question 3**
A developer writes the following and the `console.log` in the `catch` block never runs, even when `parseJSON` is called with invalid input. What is the most likely reason?
```javascript
try {
  const data = parseJSON(input);
} catch (e) {}
```
*   A) The `catch` block does not have a `finally` block, so it is skipped entirely.
*   B) The catch block is empty (swallows the error silently), so the log statement was never added and failures go unnoticed.
*   C) `try/catch` only works for synchronous code; `parseJSON` must be asynchronous.
*   D) The `catch` parameter `e` must be declared with `const` before the block to be accessible.
*   **Correct Answer:** B) The catch block is empty (swallows the error silently), so the log statement was never added and failures go unnoticed.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `finally` is optional; its absence does not cause `catch` to be skipped.
    *   *Why B is correct:* An empty `catch {}` catches the error and discards it silently. There is no `console.log` in the block because it was never written — the developer simply has no error handling logic.
    *   *Why C is incorrect:* `try/catch` works for synchronous exceptions; for async errors in `async` functions, `try/catch` also works with `await`. The scenario here is about the empty catch, not async behavior.
    *   *Why D is incorrect:* The catch parameter does not need to be declared with `const`; it is automatically scoped to the catch block.

---

**Question 4**
While working on **Error Handling**, a developer wants to throw a meaningful error when a function receives a negative number. Which code is most appropriate?
*   A) `if (n < 0) { console.error("Negative number"); }`
*   B) `if (n < 0) { return -1; }`
*   C) `if (n < 0) { throw new RangeError("Number must be non-negative"); }`
*   D) `if (n < 0) { catch(new Error("Negative")); }`
*   **Correct Answer:** C) `if (n < 0) { throw new RangeError("Number must be non-negative"); }`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `console.error` logs a message but does not interrupt execution; the function continues running with the invalid input.
    *   *Why B is incorrect:* Returning a sentinel value (`-1`) is an older pattern that is easy to miss; callers may not check the return value and the error goes undetected.
    *   *Why C is correct:* `throw new RangeError(...)` creates a meaningful exception with a message and stack trace; any calling code can catch it with `try/catch` and handle it appropriately.
    *   *Why D is incorrect:* `catch` is not a function you call; it is a clause in a `try/catch` statement. This code would throw a `SyntaxError`.

---

**Question 5**
What information is most useful in a JavaScript **stack trace**?
*   A) The total memory consumed by the program at the time of the error
*   B) The sequence of function calls that led to the error, including file names and line numbers
*   C) A list of all variables declared in the global scope at the time the error occurred
*   D) The HTTP status code returned by the most recent network request before the error
*   **Correct Answer:** B) The sequence of function calls that led to the error, including file names and line numbers.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Memory usage is reported in the Performance and Memory panels of DevTools, not in a stack trace.
    *   *Why B is correct:* A stack trace lists the call chain from the innermost function (where the error originated) back to the top-level caller, with each frame showing the function name, file, and line number.
    *   *Why C is incorrect:* Global variables are visible in the Scope pane of DevTools during debugging; the stack trace shows the call chain, not a variable inventory.
    *   *Why D is incorrect:* HTTP status codes are visible in the Network panel; they are unrelated to a JavaScript execution stack trace.
