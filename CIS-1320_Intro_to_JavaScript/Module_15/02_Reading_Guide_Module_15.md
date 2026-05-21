# Reading Guide: Module 15 - Error Handling & Debugging
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 15 - Error Handling & Debugging**! This week you will learn how to write robust JavaScript that gracefully handles failures using `try/catch/finally`, how to throw custom errors, and how to use the browser's developer tools to step through code and find bugs. Error handling is a key JSE exam domain and a critical real-world skill.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **try block**: The code block wrapped in `try { ... }` that contains statements the developer expects might throw an error. If an exception is thrown anywhere inside the `try` block, execution immediately jumps to the matching `catch` block; remaining statements in `try` are skipped.
*   **catch clause**: The `catch (error) { ... }` block that runs when an exception is thrown in the corresponding `try` block. The `error` parameter receives the thrown value (typically an `Error` object). The `catch` block should handle or log the error, not silently ignore it.
*   **throw statement**: A statement that intentionally creates and throws an exception: `throw new Error("Invalid input")`. Any value can be thrown, but throwing an `Error` object (or a subclass like `TypeError` or `RangeError`) is best practice because it includes a stack trace.
*   **Stack trace**: The sequence of function calls recorded in an `Error` object's `.stack` property that shows exactly where and how an error occurred. Reading a stack trace from top to bottom reveals the call path: the innermost function where the error was thrown is listed first.
*   **Breakpoints**: Markers placed in the browser's DevTools Sources panel on specific lines of code. When script execution reaches a breakpoint, it pauses so the developer can inspect the values of variables, the call stack, and the scope chain in real time.
*   **Developer tools**: The built-in browser inspection tools (opened with F12 or Cmd+Option+I) that include the Console (for logs and error messages), Sources (for breakpoints and step-through debugging), Network (for HTTP requests), and Elements panels. Mastering DevTools is essential for efficient JavaScript debugging.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests the `finally` block. Know that `finally` runs after `try` and `catch` regardless of whether an error was thrown — even if the `try` block has a `return` statement, `finally` executes before the function actually returns. Use `finally` to release resources (close connections, hide spinners).
*   **Scenario Trap:** A common trap shows a `try/catch` where the catch block is empty (`catch (e) {}`). Recognize this as "swallowing the error" — the exception is silently discarded and no indication of failure is given to the user or developer, making bugs very hard to trace.
*   **Study Resource:** [MDN – try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) contains a clear breakdown of the syntax with `finally` examples. Also bookmark [Chrome DevTools – JavaScript debugging reference](https://developer.chrome.com/docs/devtools/javascript/) — the "Set breakpoints" and "Step through code" sections map directly to this module's lab tasks.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 8 – Bugs and Errors** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter covers strict mode, testing, exceptions, and selective error catching — all directly tested on the JSE exam.
*   **Required Video:** Watch the video lecture on **Error Handling & Debugging** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on try/catch/finally, custom throw, and DevTools breakpoints).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Implement a try/catch block to handle division by zero**: Write a function `divide(a, b)` that throws `new Error("Cannot divide by zero")` if `b === 0`; wrap a call to it in `try/catch` and log both the success result and the caught error message.
*   **Throw a custom error if user input is invalid**: Write a function that accepts an age parameter; if `age < 0 || age > 150`, throw a `RangeError("Age out of valid range")`; catch it and display a friendly message.
*   **Add debugger statements to trace variables**: Insert `debugger;` inside a loop that builds an array; open DevTools and step through the iterations, watching the array build in the Scope pane.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 8 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the error handling and debugging segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
