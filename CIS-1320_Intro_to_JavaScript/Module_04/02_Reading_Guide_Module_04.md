# Reading Guide: Module 04 - Control Flow & Conditionals
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 04 - Control Flow & Conditionals**! This week you will learn how to make your programs take different paths based on conditions, using `if/else`, `switch`, the ternary operator, and logical operators. Understanding truthy and falsy values is a key JSE exam topic that underlies all conditional logic in JavaScript.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **if statement**: The fundamental conditional construct that executes a block of code only when its boolean expression evaluates to `true`. The `if` block may be followed by zero or more `else if` clauses and an optional `else` clause to handle alternative conditions.
*   **else if clause**: An additional condition tested only when all preceding `if` and `else if` conditions are `false`. Multiple `else if` clauses chain conditions together, and only the first matching branch runs.
*   **switch statement**: A control structure that evaluates one expression and compares its value against a series of `case` labels using strict equality. Execution falls through to subsequent cases unless a `break` statement is present; a `default` label handles unmatched values.
*   **Ternary operator**: A concise three-part expression with the syntax `condition ? valueIfTrue : valueIfFalse`. It is the only JavaScript operator that takes three operands and is commonly used to assign a value based on a condition in a single line.
*   **Logical operators**: `&&` (AND), `||` (OR), and `!` (NOT) are used to combine or negate boolean expressions. `&&` returns the first falsy operand or the last value; `||` returns the first truthy operand or the last value — both use short-circuit evaluation.
*   **Truthy vs falsy**: In JavaScript, every value is inherently truthy or falsy when used in a boolean context. The six falsy values are: `false`, `0`, `""` (empty string), `null`, `undefined`, and `NaN`. Every other value — including empty arrays `[]` and empty objects `{}` — is truthy.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam frequently shows `switch` statements and asks what executes when a `break` is missing. Know that without `break`, execution "falls through" into the next case's code even if its condition does not match.
*   **Scenario Trap:** A common trap is presenting code like `if (x = 5)` (single `=` assignment) instead of `if (x === 5)`. The assignment always evaluates to the assigned value (`5`, which is truthy), so the block always runs regardless of `x`'s original value.
*   **Study Resource:** The [MDN – if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) and [MDN – switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch) reference pages each include interactive examples. Read both and pay attention to the "fall-through" and "truthy/falsy" sections.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 2 – Program Structure** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). The sections on conditional execution cover `if`, `else`, `switch`, and short-circuit evaluation in detail.
*   **Required Video:** Watch the video lecture on **Control Flow & Conditionals** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on the if/else, switch, and ternary segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a conditional block evaluating test grades**: Given a numeric score, use `if/else if/else` to output a letter grade ("A", "B", "C", "D", or "F").
*   **Implement a switch statement mapping weekdays**: Accept a number 1–7 and use a `switch` to log the corresponding day name; add a `default` for invalid inputs.
*   **Rewrite an if/else block using a ternary operator**: Convert a two-branch `if/else` that assigns a value into a single ternary expression.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 2 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the control flow segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
