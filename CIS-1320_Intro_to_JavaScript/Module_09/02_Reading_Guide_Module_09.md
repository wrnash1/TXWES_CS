# Reading Guide: Module 09 - Array Iteration & Callback Functions
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 09 - Array Iteration & Callback Functions**! This week you will learn JavaScript's higher-order array methods — `forEach`, `map`, `filter`, and `reduce` — which accept callback functions to process each element. These functional programming patterns are tested extensively on the JSE exam because they replace verbose `for` loops with concise, expressive code.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **forEach method**: An array method that calls a provided callback function once for each element in the array, in order. It always returns `undefined` and is used for side effects (logging, DOM updates) rather than transforming data. It cannot be stopped mid-iteration with `break`.
*   **map method**: An array method that calls a callback on every element and returns a **new array** containing each return value. The original array is not mutated. Use `map` when you need to transform every element into a new value (e.g., doubling all numbers).
*   **filter method**: An array method that calls a callback on every element and returns a **new array** containing only the elements for which the callback returned a truthy value. The length of the result may be less than or equal to the original. The original array is not mutated.
*   **reduce method**: An array method that processes each element with a callback and accumulates a single return value (the "accumulator"). Accepts an optional initial value for the accumulator. Used to sum numbers, flatten arrays, group items, or build objects from arrays.
*   **Callback execution**: The pattern of passing a function as an argument to another function, which then calls ("executes") it at the appropriate time. Higher-order array methods like `map`, `filter`, and `reduce` receive callbacks and call them for each element, often passing `(element, index, array)` as arguments.

---

### 2. Certification Exam Tips
*   **Focus Area:** Know the return values of each iteration method: `forEach` returns `undefined`; `map` returns a new array of the same length; `filter` returns a new array of equal or shorter length; `reduce` returns a single accumulated value. The JSE exam asks which method to use for a given transformation task.
*   **Scenario Trap:** A common trap is using `forEach` where `map` is needed. `forEach` returns `undefined` — assigning the result of `forEach` to a variable will always give `undefined`, not a transformed array. Use `map` when you need the new array.
*   **Study Resource:** [javascript.info – Array methods](https://javascript.info/array-methods) provides clear, concise explanations with runnable examples for every array method, including `map`, `filter`, and `reduce`. The "Tasks" at the end of the page are excellent JSE-style practice questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 5 – Higher-Order Functions** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter introduces callbacks and builds up to `filter`, `map`, and `reduce` with detailed examples.
*   **Required Video:** Watch the video lecture on **Array Iteration & Callback Functions** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on the forEach, map, filter, and reduce segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Iterate over an array using forEach**: Use `forEach` to log each element of a names array with its index.
*   **Create a new array of squared numbers using map**: Given `[1, 2, 3, 4, 5]`, use `map` to produce `[1, 4, 9, 16, 25]` and log the new array.
*   **Filter out odd numbers from a list**: Given `[1, 2, 3, 4, 5, 6]`, use `filter(n => n % 2 === 0)` to return only even numbers and confirm the original array is unchanged.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 5 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the array iteration segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
