# Quiz: Module 05 - Loops & Iteration
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
What is the primary characteristic of a do-while loop compared to a standard while loop?
*   A) It executes the code block at least once before checking the condition
*   B) It does not check any conditions
*   C) It only runs if the condition is false
*   D) It cannot run indefinitely
*   **Correct Answer:** A) A do-while loop evaluates its condition after executing the body, ensuring the block runs at least once.
*   **Distractor Analysis:**
    *   *Why correct:* A do-while loop evaluates its condition after executing the body, ensuring the block runs at least once.
    *   The other options represent incorrect looping behaviors.

---

**Question 2**
Which of the following most accurately describes a **for loop** in JavaScript?
*   A) A loop that repeatedly runs its body an indefinite number of times until a `break` statement is encountered
*   B) A loop construct with an initialization, a condition, and an update expression in its header, running the body while the condition is truthy
*   C) A loop that iterates over the keys of an object and executes a callback for each key-value pair
*   D) A special function that calls itself recursively until a base case is reached
*   **Correct Answer:** B) A loop construct with an initialization, a condition, and an update expression in its header, running the body while the condition is truthy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That partially describes a `while(true)` loop; a standard `for` loop terminates when its condition becomes false, not just on `break`.
    *   *Why B is correct:* The `for` loop header has three clauses: `for (init; condition; update)`, and the body runs as long as the condition is truthy.
    *   *Why C is incorrect:* That describes `for...in` (iterates object keys) or `for...of` (iterates iterable values), which are specialized variants.
    *   *Why D is incorrect:* That describes a recursive function, not a loop.

---

**Question 3**
How many times will the following loop execute?
```javascript
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```
*   A) 4 times
*   B) 5 times
*   C) 6 times
*   D) The loop runs forever because `i` keeps incrementing
*   **Correct Answer:** B) 5 times
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using `<` instead of `<=` would yield 4 iterations starting at 1; with `<=`, it runs for i = 1, 2, 3, 4, 5.
    *   *Why B is correct:* The loop runs for `i` values 1, 2, 3, 4, 5 — exactly five iterations before `i` becomes 6 and the condition `i <= 5` is false.
    *   *Why C is incorrect:* Six iterations would require `i <= 6` or starting at `i = 0` with `i <= 5`.
    *   *Why D is incorrect:* The condition `i <= 5` eventually becomes false when `i` reaches 6, so the loop terminates.

---

**Question 4**
While working on **Loops & Iteration**, a developer writes the following code and reports the browser tab freezes:
```javascript
let i = 0;
while (i < 10) {
  console.log(i);
}
```
What is the most effective fix?
*   A) Change `while` to `do-while` to ensure the condition is checked at the end.
*   B) Add `i++;` inside the loop body so the loop variable increments toward the exit condition.
*   C) Change the condition from `i < 10` to `i === 10` to limit the loop more precisely.
*   D) Wrap the `while` loop in a `try/catch` block to catch the infinite loop error.
*   **Correct Answer:** B) Add `i++;` inside the loop body so the loop variable increments toward the exit condition.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Switching to `do-while` does not fix the missing increment; it would still loop forever.
    *   *Why B is correct:* Without `i++`, `i` stays at `0` forever and the condition `i < 10` is always true; adding the increment makes the loop terminate after 10 iterations.
    *   *Why C is incorrect:* Changing to `i === 10` means the condition is `false` from the start (since `i = 0`), so the body never runs at all.
    *   *Why D is incorrect:* An infinite loop is not a thrown exception; `try/catch` cannot catch it.

---

**Question 5**
What does the `continue` statement do inside a loop?
*   A) Exits the loop immediately and skips all remaining iterations
*   B) Skips the rest of the current iteration and proceeds to the next iteration of the loop
*   C) Restarts the loop from the beginning, resetting the loop variable to its initial value
*   D) Pauses loop execution until a user input event is received
*   **Correct Answer:** B) Skips the rest of the current iteration and proceeds to the next iteration of the loop.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes the `break` statement, not `continue`.
    *   *Why B is correct:* `continue` causes the engine to jump past any remaining code in the current loop body and move to the next iteration (update expression for `for`, condition check for `while`).
    *   *Why C is incorrect:* `continue` does not reset the loop counter; it simply moves to the next iteration without resetting.
    *   *Why D is incorrect:* JavaScript loops do not pause for user input; that requires asynchronous event handling, not `continue`.
