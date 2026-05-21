# Reading Guide: Module 08 - Midterm Prep & Arrays
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 08 - Midterm Prep & Arrays**! This week combines midterm review with a focused study of JavaScript arrays — ordered, indexed collections that are essential to nearly every program. You will master the core mutating and non-mutating array methods tested on the JSE exam, and reinforce your knowledge of all prior modules.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Array literal**: A syntax that creates an array by listing elements inside square brackets, separated by commas (e.g., `const fruits = ["apple", "banana", "cherry"]`). Elements can be of any type and can be mixed. The array index starts at `0`.
*   **Array index**: A zero-based integer position used to access or modify an element in an array (e.g., `fruits[0]` is `"apple"`). Accessing an index that does not exist returns `undefined` without throwing an error.
*   **push/pop**: `push()` adds one or more elements to the **end** of an array and returns the new length. `pop()` removes and returns the **last** element, mutating the array in place. Both operate on the tail of the array.
*   **shift/unshift**: `shift()` removes and returns the **first** element of an array, shifting all other elements down by one index. `unshift()` adds one or more elements to the **beginning** and returns the new length. Both operate on the head of the array.
*   **array.length**: A property (not a method) that returns the number of elements in an array. It is automatically updated when elements are added or removed. Setting `arr.length = 0` is a quick way to empty an array.
*   **Review concepts**: Use this module to revisit Modules 01–07: variable scope, data types, operators, control flow, loops, functions, and objects. The midterm will sample questions from all of these areas alongside the new array content.

---

### 2. Certification Exam Tips
*   **Focus Area:** Know the return values of `push`, `pop`, `shift`, and `unshift` — not just what they do to the array. `push` and `unshift` return the **new length**; `pop` and `shift` return the **removed element**. The JSE exam asks about return values, not just side effects.
*   **Scenario Trap:** Do not confuse `slice` (non-mutating, returns a copy of a portion) with `splice` (mutating, removes/inserts elements in place). Both appear on the exam and have similar names but very different behaviors.
*   **Study Resource:** [MDN – Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) is the complete reference for every array method. Before the midterm, scan the method list and make sure you recognize `slice`, `splice`, `indexOf`, `includes`, `join`, and `reverse` in addition to the primary four covered this week.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 4 – Data Structures: Objects and Arrays** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). The second half of the chapter focuses on arrays and the built-in methods tested on the midterm.
*   **Required Video:** Watch the video lecture on **Midterm Prep & Arrays** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (review array creation, indexing, and the four mutating methods: push/pop/shift/unshift).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create an array of fruits and manipulate elements**: Declare `const fruits = ["apple", "banana", "cherry"]` and access each element by index.
*   **Add elements using push and unshift**: Use `fruits.push("date")` to add to the end, then `fruits.unshift("avocado")` to add to the front; log the array and its length after each operation.
*   **Remove elements using pop and shift**: Use `fruits.pop()` and `fruits.shift()` and capture their return values in variables; log the removed elements and the modified array.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 4 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the arrays segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review all prior module notes for the midterm.
- [ ] Proceed to the weekly hands-on lab activity.
