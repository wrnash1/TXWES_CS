# Quiz: Module 09 - Array Iteration & Callback Functions
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which array iteration method creates and returns a new array containing only elements that pass a logical condition?
*   A) map()
*   B) filter()
*   C) forEach()
*   D) reduce()
*   **Correct Answer:** B) The `filter()` method returns a new array with elements that return true for the callback's condition.
*   **Distractor Analysis:**
    *   *Why correct:* The `filter()` method returns a new array with elements that return true for the callback's condition.
    *   map transforms all elements. forEach iterates without returning a new array. reduce accumulates values.

---

**Question 2**
Which of the following most accurately describes the **forEach method** in JavaScript?
*   A) A method that transforms each element using a callback and returns a new array of the same length
*   B) A method that calls a callback on each element for side effects and always returns `undefined`
*   C) A method that accumulates array elements into a single value based on a reducer function
*   D) A method that creates a sorted copy of the array based on a comparison callback
*   **Correct Answer:** B) A method that calls a callback on each element for side effects and always returns `undefined`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes `map()`, which produces a new array of transformed values.
    *   *Why B is correct:* `forEach` is intended for side effects (logging, DOM updates, etc.); it does not collect return values and always returns `undefined`.
    *   *Why C is incorrect:* That describes `reduce()`, which produces a single accumulated result.
    *   *Why D is incorrect:* That describes `sort()`, which reorders elements in place using a comparator function.

---

**Question 3**
What is the output of the following code?
```javascript
const nums = [1, 2, 3];
const doubled = nums.map(n => n * 2);
console.log(doubled);
console.log(nums);
```
*   A) `[2, 4, 6]` then `[2, 4, 6]` (both are mutated)
*   B) `[2, 4, 6]` then `[1, 2, 3]` (map returns a new array; original is unchanged)
*   C) `undefined` then `[1, 2, 3]` (map returns undefined like forEach)
*   D) `[1, 2, 3]` then `[2, 4, 6]` (map mutates the original and returns it)
*   **Correct Answer:** B) `[2, 4, 6]` then `[1, 2, 3]` (map returns a new array; original is unchanged).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `map` does not mutate the original array; it produces a brand-new array.
    *   *Why B is correct:* `map` returns a new array with transformed values; the original `nums` is never modified.
    *   *Why C is incorrect:* `map` returns the new array, not `undefined`; that is the behavior of `forEach`.
    *   *Why D is incorrect:* `map` does not mutate in place; the original is always preserved.

---

**Question 4**
While working on **Array Iteration**, a developer wants to calculate the total of all prices in an array. Which method is most appropriate?
*   A) `filter()` — returns only the price values that meet a condition
*   B) `map()` — transforms each price into a formatted string for display
*   C) `reduce()` — accumulates all prices into a single total sum
*   D) `forEach()` — iterates over prices and returns the final computed total
*   **Correct Answer:** C) `reduce()` — accumulates all prices into a single total sum.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `filter` returns a subset array matching a condition; it does not produce a single number.
    *   *Why B is incorrect:* `map` transforms each element into a new value but returns an array, not a single total.
    *   *Why C is correct:* `reduce((total, price) => total + price, 0)` is the idiomatic way to sum an array into one value.
    *   *Why D is incorrect:* `forEach` always returns `undefined`; you cannot use its return value to get a total.

---

**Question 5**
Which of the following correctly uses `filter` to get all strings longer than 4 characters from `["hi", "hello", "hey", "world"]`?
*   A) `arr.map(s => s.length > 4)`
*   B) `arr.filter(s => s.length > 4)`
*   C) `arr.forEach(s => s.length > 4)`
*   D) `arr.reduce(s => s.length > 4)`
*   **Correct Answer:** B) `arr.filter(s => s.length > 4)`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `map` with a boolean callback produces `[false, true, false, true]` — an array of booleans, not the matching strings.
    *   *Why B is correct:* `filter` keeps elements for which the callback returns truthy; `s.length > 4` is `true` for `"hello"` and `"world"`, so the result is `["hello", "world"]`.
    *   *Why C is incorrect:* `forEach` returns `undefined`; the boolean expression inside is computed but its result is discarded.
    *   *Why D is incorrect:* `reduce` requires an accumulator pattern and would not work correctly with just a condition callback as written.
