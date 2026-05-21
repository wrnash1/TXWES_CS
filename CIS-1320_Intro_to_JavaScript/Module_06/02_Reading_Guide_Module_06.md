# Reading Guide: Module 06 - Functions & Arrow Functions
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 06 - Functions & Arrow Functions**! This week you will learn how to define reusable blocks of code using function declarations, function expressions, and the ES6 arrow function syntax. Understanding how functions handle parameters, return values, and `this` binding is a major focus area for the JSE exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Function declaration**: A named function defined with the `function` keyword at the statement level (e.g., `function greet() {}`). Function declarations are hoisted entirely — both the name and the body — so they can be called before the line where they are written in the source code.
*   **Function expression**: A function assigned to a variable (e.g., `const greet = function() {}`). Unlike declarations, function expressions are not hoisted with their body; calling the variable before the assignment throws a `TypeError` (for `const`/`let`) or returns `undefined` (for `var`).
*   **Arrow function**: An ES6 shorthand syntax for writing function expressions: `const fn = (params) => expression`. Arrow functions do not have their own `this`, `arguments`, or `prototype` bindings — they inherit `this` from the surrounding lexical scope, making them ideal for callbacks.
*   **Parameters**: The named variables listed inside a function's parentheses in its definition (e.g., `function add(a, b)`). Parameters act as local variables inside the function body. If a caller provides fewer arguments than parameters, the missing ones are `undefined` unless defaults are provided.
*   **Return statement**: The `return` keyword immediately exits a function and optionally sends a value back to the caller. A function without a `return` statement (or with a bare `return;`) returns `undefined` implicitly.
*   **Default arguments**: ES6 allows parameters to have fallback values if no argument (or `undefined`) is passed: `function greet(name = "World")`. Default values are evaluated each time the function is called, not once when the function is defined.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests the lexical `this` binding of arrow functions. In a regular function, `this` depends on how the function is called; in an arrow function, `this` is fixed to the enclosing scope where the arrow function was defined. Know the practical consequence: arrow functions cannot be used as object methods when you need `this` to refer to the object.
*   **Scenario Trap:** A common question shows a function called before its declaration and asks what happens. Remember: function *declarations* are fully hoisted (callable before the line); function *expressions* stored in `const`/`let` are in the temporal dead zone (calling them throws a `ReferenceError`).
*   **Study Resource:** Read [MDN – Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) and compare with [MDN – function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function). The "No separate `this`" section of the arrow function article is directly tested on the JSE exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 3 – Functions** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter covers declarations, expressions, closures, and recursion in depth.
*   **Required Video:** Watch the video lecture on **Functions & Arrow Functions** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on function declaration, expression, arrow function, and default parameter segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Define a function using standard function declaration**: Write `function square(n) { return n * n; }` and call it before its definition to confirm hoisting works.
*   **Create an arrow function to calculate tax**: Write `const calcTax = (price, rate = 0.08) => price * rate;` and test it with and without the second argument.
*   **Use default parameters in a greeting function**: Write a function `greet(name = "Guest")` that returns `"Hello, " + name + "!"` and call it with and without an argument.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 3 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the functions and arrow functions segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
