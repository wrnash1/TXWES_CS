# Quiz: Module 02 - Variables, Constants, and Scope
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which keyword was introduced in ES6 to declare block-scoped variables that can be reassigned?
*   A) var
*   B) let
*   C) const
*   D) define
*   **Correct Answer:** B) The `let` keyword declares block-scoped variables that can be reassigned.
*   **Distractor Analysis:**
    *   *Why correct:* The `let` keyword declares block-scoped variables that can be reassigned.
    *   var is function-scoped and hoisted. const cannot be reassigned. define is not a variable declaration keyword.

---

**Question 2**
Which of the following most accurately describes a **global variable** in JavaScript?
*   A) A variable declared inside a function that is accessible only within that function's scope
*   B) A variable declared with `const` that cannot be changed anywhere in the program
*   C) A variable declared outside any function or block, making it accessible from anywhere in the script
*   D) A variable that is automatically created by the browser for every HTML element on the page
*   **Correct Answer:** C) A variable declared outside any function or block, making it accessible from anywhere in the script.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes a local variable, not a global variable.
    *   *Why B is incorrect:* `const` restricts reassignment but has nothing to do with being global; `const` can be block-scoped.
    *   *Why C is correct:* A global variable lives in the outermost scope and is reachable from every function and block in the file.
    *   *Why D is incorrect:* The browser does not automatically create variables for DOM elements; you must query them explicitly.

---

**Question 3**
What is the output of the following code?
```javascript
console.log(x);
var x = 5;
```
*   A) `5`
*   B) `ReferenceError: x is not defined`
*   C) `undefined`
*   D) `null`
*   **Correct Answer:** C) `undefined`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The assignment `x = 5` has not run yet at the time of the log; only the declaration is hoisted.
    *   *Why B is incorrect:* A `ReferenceError` would occur with `let` or `const`, not `var`; `var` is hoisted and initialized to `undefined`.
    *   *Why C is correct:* `var` declarations are hoisted and initialized to `undefined` before any code runs, so the log prints `undefined`.
    *   *Why D is incorrect:* `null` is an explicit assignment; hoisting does not initialize a variable to `null`.

---

**Question 4**
A developer writes the following code inside a function:
```javascript
if (true) {
  let message = "Hello";
}
console.log(message);
```
What will happen?
*   A) Logs `"Hello"` because `let` variables are always accessible after their block ends.
*   B) Logs `undefined` because `let` variables are hoisted to the function scope.
*   C) Throws a `ReferenceError` because `message` is block-scoped and not accessible outside the `if` block.
*   D) Logs `null` because `let` variables are initialized to `null` outside their block.
*   **Correct Answer:** C) Throws a `ReferenceError` because `message` is block-scoped and not accessible outside the `if` block.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `let` is block-scoped; it is destroyed when the block ends.
    *   *Why B is incorrect:* `let` is hoisted into a temporal dead zone, not promoted to function scope like `var`.
    *   *Why C is correct:* Attempting to access a `let` variable outside its block throws `ReferenceError: message is not defined`.
    *   *Why D is incorrect:* JavaScript does not initialize `let` to `null` outside its scope; the variable simply does not exist there.

---

**Question 5**
Which statement about `const` in JavaScript is correct?
*   A) A `const` variable cannot hold an object because objects are mutable.
*   B) A `const` declaration must include an initial value at the time of declaration.
*   C) A `const` variable can be reassigned as long as the new value is the same type.
*   D) A `const` variable is function-scoped, just like `var`.
*   **Correct Answer:** B) A `const` declaration must include an initial value at the time of declaration.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `const` can hold objects and arrays; only the binding (reference) is fixed, not the object's contents.
    *   *Why B is correct:* Declaring `const x;` without a value causes a `SyntaxError`; `const` requires initialization at declaration.
    *   *Why C is incorrect:* `const` prohibits all reassignment regardless of type; even `const x = 5; x = 5;` throws a `TypeError`.
    *   *Why D is incorrect:* `const` is block-scoped like `let`, not function-scoped like `var`.
