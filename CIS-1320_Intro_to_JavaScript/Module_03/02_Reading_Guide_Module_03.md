# Reading Guide: Module 03 - Data Types & Operators
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 03 - Data Types & Operators**! This week you will explore JavaScript's built-in data types, how the language automatically converts types in certain situations (type coercion), and how operators are used to perform calculations and comparisons. Mastering these topics is essential for writing correct comparisons and avoiding common bugs on the JSE exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Primitive types**: The six basic, immutable value types in JavaScript: `string`, `number`, `boolean`, `null`, `undefined`, `symbol` (and `bigint` in ES2020). Primitives are compared by value, not by reference, so two variables holding `"hello"` are considered equal.
*   **Type coercion**: JavaScript's automatic conversion of a value from one data type to another when an operator or function expects a different type. For example, `"5" + 3` produces `"53"` (string concatenation) because the number `3` is coerced to a string.
*   **Strict equality**: The `===` operator that compares both value and type without any coercion. `"5" === 5` is `false` because one is a string and the other is a number. This is the preferred equality check in modern JavaScript to avoid coercion surprises.
*   **Arithmetic operators**: Symbols used to perform math operations: `+` (addition/concatenation), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulo/remainder), and `**` (exponentiation). The `+` operator is special because it also concatenates strings.
*   **typeof operator**: A unary operator that returns a string representing the data type of its operand (e.g., `typeof 42` returns `"number"`, `typeof null` returns `"object"` — a known historical quirk). Useful for type-checking before performing operations.
*   **null vs undefined**: `null` is an explicit assignment meaning "no value" — a developer intentionally sets it. `undefined` means a variable has been declared but not yet assigned a value, or a function parameter was not provided. Both are falsy but are not strictly equal to each other.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam heavily tests the difference between `==` (loose equality, allows coercion) and `===` (strict equality, no coercion). Memorize a handful of surprising `==` results: `0 == false` is `true`, `"" == false` is `true`, `null == undefined` is `true`, but `null === undefined` is `false`.
*   **Scenario Trap:** Watch for questions that mix the `+` operator with numbers and strings. Adding a number to a string always produces a string; this is not an error in JavaScript. For example, `1 + 2 + "3"` evaluates to `"33"` because addition is left-to-right.
*   **Study Resource:** The [MDN JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures) reference page is the authoritative source for this topic. Read the "Primitive values" section to see all seven primitive types with examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 1 – Values, Types, and Operators** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter systematically covers every primitive type and the operators tested on the JSE exam.
*   **Required Video:** Watch the video lecture on **Data Types & Operators** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on the data types and comparison operator segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Verify the type of variables using the typeof operator**: Declare variables of different types and log `typeof` for each to observe the returned string.
*   **Demonstrate type coercion using the + operator with numbers and strings**: Try `console.log(5 + "3")` and `console.log(5 - "3")` to see when coercion converts to string vs. number.
*   **Compare values using == and ===**: Write comparison expressions like `0 == false`, `0 === false`, `null == undefined`, and `null === undefined`; log results and explain why each evaluates as it does.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 1 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the data types and operators segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
