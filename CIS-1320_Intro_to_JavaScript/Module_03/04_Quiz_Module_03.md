# Quiz: Module 03 - Data Types & Operators
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
What is the difference between the double-equality operator (==) and the triple-equality operator (===) in JavaScript?
*   A) == performs type coercion before comparing; === compares both value and type without coercion
*   B) === performs type coercion; == does not
*   C) == is used for strings; === is used for numbers
*   D) There is no difference; they are interchangeable
*   **Correct Answer:** A) The strict equality operator (===) requires both operands to be of the same type and value, whereas == performs type coercion first.
*   **Distractor Analysis:**
    *   *Why correct:* The strict equality operator (===) requires both operands to be of the same type and value, whereas == performs type coercion first.
    *   B is inverted. C is false because both operators can be used with any type. D is incorrect.

---

**Question 2**
Which of the following most accurately describes the **typeof operator** in JavaScript?
*   A) An operator that converts a value to a specific type, such as turning a string into a number
*   B) A unary operator that returns a string naming the data type of its operand (e.g., `"number"`, `"string"`, `"boolean"`)
*   C) A comparison operator that checks if two values share the same type, returning `true` or `false`
*   D) A method on every object that lists all the property names it contains
*   **Correct Answer:** B) A unary operator that returns a string naming the data type of its operand (e.g., `"number"`, `"string"`, `"boolean"`).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes explicit type conversion functions like `Number()` or `String()`, not `typeof`.
    *   *Why B is correct:* `typeof` is a prefix operator that evaluates its operand and returns a type label as a string.
    *   *Why C is incorrect:* `typeof` does not return a boolean; it returns a string. Comparing types uses `===` on the `typeof` result.
    *   *Why D is incorrect:* That describes `Object.keys()` or `for...in`, not `typeof`.

---

**Question 3**
What is the result of evaluating `"10" - 4` in JavaScript?
*   A) `"104"` (string concatenation)
*   B) `NaN` (Not a Number)
*   C) `6` (numeric subtraction after coercion)
*   D) A TypeError is thrown because you cannot subtract from a string
*   **Correct Answer:** C) `6` (numeric subtraction after coercion)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* String concatenation only occurs with `+`; the `-` operator forces numeric conversion.
    *   *Why B is incorrect:* `NaN` results when coercion fails (e.g., `"abc" - 4`); `"10"` coerces cleanly to `10`.
    *   *Why C is correct:* The `-` operator has no string meaning, so JS coerces `"10"` to the number `10` and computes `10 - 4 = 6`.
    *   *Why D is incorrect:* JavaScript does not throw a TypeError here; it silently coerces the string operand.

---

**Question 4**
While working on **Data Types & Operators** in a production environment, you encounter a system alert indicating a **TypeError** error. Which of the following is the most effective troubleshooting action to resolve this issue?
*   A) Perform explicit type checking (e.g., `typeof x === "number"`) or conversion (e.g., `Number(x)`) before executing operations on mixed data types.
*   B) Ensure the requested key exists in the object before accessing it, using optional chaining (`?.`) or a conditional check.
*   C) Verify that the array index is within bounds before accessing the element.
*   D) Reboot the development environment and clear the browser cache.
*   **Correct Answer:** A) Perform explicit type checking (e.g., `typeof x === "number"`) or conversion (e.g., `Number(x)`) before executing operations on mixed data types.
*   **Distractor Analysis:**
    *   *Why A is correct:* A `TypeError` in JavaScript typically means an operation was applied to a value of the wrong type. Checking or converting the type first prevents the error.
    *   *Why B is incorrect:* Checking for missing object keys prevents `undefined` access errors, not `TypeError` from type mismatches.
    *   *Why C is incorrect:* Bounds checking prevents out-of-range index errors, which is a separate issue from type mismatch.
    *   *Why D is incorrect:* Rebooting does not fix a code-level type error; the root cause must be corrected in the logic.

---

**Question 5**
What does `typeof null` return in JavaScript?
*   A) `"null"`
*   B) `"undefined"`
*   C) `"object"`
*   D) `"boolean"`
*   **Correct Answer:** C) `"object"`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* There is no `"null"` type string returned by `typeof`; this is a common but wrong assumption.
    *   *Why B is incorrect:* `typeof undefined` returns `"undefined"`; `null` and `undefined` are different values.
    *   *Why C is correct:* `typeof null === "object"` is a well-known historical bug in JavaScript that has never been corrected for backward-compatibility reasons.
    *   *Why D is incorrect:* `typeof false` returns `"boolean"`; `null` is not a boolean value.
