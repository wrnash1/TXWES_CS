# Quiz: Module 04 - Control Flow & Conditionals
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which of the following values is evaluated as 'truthy' in a JavaScript conditional statement?
*   A) 0
*   B) '' (empty string)
*   C) [] (empty array)
*   D) null
*   **Correct Answer:** C) In JavaScript, empty arrays `[]` and empty objects `{}` are truthy, whereas 0, empty strings, null, and undefined are falsy.
*   **Distractor Analysis:**
    *   *Why correct:* In JavaScript, empty arrays `[]` and empty objects `{}` are truthy, whereas 0, empty strings, null, and undefined are falsy.
    *   0, empty string, and null are all falsy values.

---

**Question 2**
Which of the following most accurately describes **truthy vs falsy** values in JavaScript?
*   A) Truthy values are those that were explicitly assigned `true`; falsy values were explicitly assigned `false`.
*   B) A value is falsy if JavaScript automatically converts it to `0` during arithmetic; all other values are truthy.
*   C) Every value has an inherent boolean interpretation: six specific values (`false`, `0`, `""`, `null`, `undefined`, `NaN`) are falsy; all other values — including empty arrays and objects — are truthy.
*   D) Truthy and falsy only apply to variables declared with `var`; `let` and `const` variables always evaluate as truthy.
*   **Correct Answer:** C) Every value has an inherent boolean interpretation: six specific values (`false`, `0`, `""`, `null`, `undefined`, `NaN`) are falsy; all other values — including empty arrays and objects — are truthy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Truthy/falsy applies to any value used in a boolean context, not just those explicitly assigned `true` or `false`.
    *   *Why B is incorrect:* Truthy/falsy is a boolean concept separate from numeric coercion; many values coerce to `0` but are still truthy (e.g., `"0"` is truthy).
    *   *Why C is correct:* JavaScript's specification defines exactly six falsy primitives; everything else — including objects, arrays, and non-empty strings — is truthy.
    *   *Why D is incorrect:* Truthy/falsy behavior applies to all values regardless of how the variable was declared.

---

**Question 3**
What happens in a `switch` statement when a matching `case` does not include a `break` statement?
*   A) The program throws a SyntaxError because `break` is required in every `case`.
*   B) Execution stops at the end of the matching case's code block automatically.
*   C) Execution falls through into the next `case` block and continues until a `break` or the end of the `switch` is reached.
*   D) The `default` case runs immediately after the matching case.
*   **Correct Answer:** C) Execution falls through into the next `case` block and continues until a `break` or the end of the `switch` is reached.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `break` is optional in `switch` cases; omitting it is valid JavaScript syntax.
    *   *Why B is incorrect:* Unlike other languages, JavaScript's `switch` does not automatically stop at the end of a case.
    *   *Why C is correct:* Fall-through is a deliberate JavaScript behavior; the engine continues executing subsequent case bodies until it hits a `break` or the closing `}`.
    *   *Why D is incorrect:* `default` only runs if no case matches or if fall-through reaches it; it does not jump automatically after a match.

---

**Question 4**
While working on **Control Flow & Conditionals** in a production environment, you encounter a bug where an `if` block executes even when the condition should be false. Which of the following is the most likely cause?
*   A) The `if` block is missing a `return` statement.
*   B) An assignment operator `=` was used instead of a comparison operator `===` inside the condition.
*   C) The condition uses `&&` when `||` should have been used.
*   D) The `else` clause is missing from the statement.
*   **Correct Answer:** B) An assignment operator `=` was used instead of a comparison operator `===` inside the condition.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A missing `return` affects function output, not whether a condition evaluates to true or false.
    *   *Why B is correct:* `if (x = 5)` assigns `5` to `x` and evaluates the assigned value (`5` is truthy), so the block always runs regardless of `x`'s original value.
    *   *Why C is incorrect:* Swapping `&&` and `||` changes which combination of conditions triggers the block but does not cause unconditional execution.
    *   *Why D is incorrect:* The absence of an `else` clause has no effect on whether the `if` block runs.

---

**Question 5**
Which of the following correctly rewrites `let label = (score >= 60) ? "Pass" : "Fail";` using an `if/else` statement?
*   A) `if (score >= 60) { label = "Pass" || "Fail"; }`
*   B) `if (score >= 60) { let label = "Pass"; } else { let label = "Fail"; }`
*   C) `let label; if (score >= 60) { label = "Pass"; } else { label = "Fail"; }`
*   D) `let label = if (score >= 60) "Pass"; else "Fail";`
*   **Correct Answer:** C) `let label; if (score >= 60) { label = "Pass"; } else { label = "Fail"; }`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `"Pass" || "Fail"` always evaluates to `"Pass"` because `"Pass"` is truthy; the else branch is never reached.
    *   *Why B is incorrect:* Declaring `let label` inside each block creates block-scoped variables that are inaccessible outside the `if/else`; the outer `label` is never assigned.
    *   *Why C is correct:* Declaring `label` before the `if` statement and assigning inside each branch correctly mirrors the ternary's behavior.
    *   *Why D is incorrect:* Using `if/else` as an expression on the right-hand side of an assignment is a syntax error in JavaScript.
