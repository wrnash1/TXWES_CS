# Reading Guide: Module 02 - Variables, Constants, and Scope
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 02 - Variables, Constants, and Scope**! This week you will learn how JavaScript stores and manages data using `var`, `let`, and `const`, and how the scope of a variable determines where it can be read or written. These rules are heavily tested on the JSE exam and are critical for writing predictable, bug-free code.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **var keyword**: The original ES5 way to declare a variable in JavaScript. Variables declared with `var` are function-scoped (or globally scoped if declared outside a function), are hoisted to the top of their scope, and can be re-declared without error — behaviors that can lead to subtle bugs.
*   **let keyword**: Introduced in ES6, `let` declares a block-scoped variable that can be reassigned but cannot be re-declared in the same scope. It is hoisted but remains in a "temporal dead zone" until its declaration line is reached, preventing access before declaration.
*   **const keyword**: An ES6 keyword that declares a block-scoped binding that cannot be reassigned after initialization. Note that `const` does not make objects or arrays immutable — their internal properties can still be changed; only the variable binding itself is locked.
*   **Block scope**: The rule that variables declared with `let` or `const` are only accessible within the nearest pair of curly braces `{}` (the block) that contains them. Code outside that block cannot read or write the variable.
*   **Hoisting**: JavaScript's behavior of moving declarations (but not initializations) to the top of their scope during the compilation phase. `var` declarations are hoisted and initialized to `undefined`; `let` and `const` declarations are hoisted but remain uninitialized in the temporal dead zone.
*   **Global variable**: A variable declared outside any function or block, making it accessible from anywhere in the program. In browsers, global `var` variables become properties of the `window` object. Overusing globals is a common source of naming conflicts and hard-to-trace bugs.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam frequently tests the behavioral differences between `var`, `let`, and `const` — especially in loops and conditionals. Know that `var` in a `for` loop leaks into the enclosing function scope, while `let` is confined to the loop block.
*   **Scenario Trap:** Watch for questions that show code accessing a `let` or `const` variable before its declaration line. Recognizing the temporal dead zone (which throws a `ReferenceError`) is a key distinction from `var` (which returns `undefined` when accessed before its line).
*   **Study Resource:** The MDN Web Docs article [let - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) contains a clear explanation of block scope and the temporal dead zone with runnable examples — read the "Description" section before the lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 2 – Program Structure** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). Pay particular attention to the sections on bindings (variables) and scope.
*   **Required Video:** Watch the video lecture on **Variables, Constants, and Scope** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (freeCodeCamp full-course video; focus on the `var`/`let`/`const` and scope segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Declare variables using var, let, and const**: Write three declarations, assign values, then log them to confirm each stores data correctly.
*   **Demonstrate block scope behavior of let vs var**: Place `let x = 1` and `var y = 1` inside an `if` block; log both outside the block to see that `x` throws a `ReferenceError` while `y` is accessible.
*   **Trigger a TypeError by reassigning a const variable**: Declare `const PI = 3.14;` then attempt `PI = 3;` and observe the browser console error.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 2 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the variables and scope segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
