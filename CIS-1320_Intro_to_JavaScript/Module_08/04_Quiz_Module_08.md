# Quiz: Module 08 - Midterm Prep & Arrays
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which array method adds one or more elements to the *beginning* of an array and returns the new length?
*   A) push()
*   B) pop()
*   C) shift()
*   D) unshift()
*   **Correct Answer:** D) The `unshift()` method adds elements to the front of the array; `push()` adds them to the end.
*   **Distractor Analysis:**
    *   *Why correct:* The `unshift()` method adds elements to the front of the array; `push()` adds them to the end.
    *   push adds to the end. pop removes from the end. shift removes from the front.

---

**Question 2**
Which of the following most accurately describes **push/pop** array methods in JavaScript?
*   A) `push()` adds an element to the beginning of an array; `pop()` removes the first element
*   B) `push()` adds one or more elements to the end of an array and returns the new length; `pop()` removes and returns the last element
*   C) `push()` and `pop()` both return `undefined` and modify the array without providing a return value
*   D) `push()` creates a new array by appending an element; `pop()` creates a new array with the last element removed
*   **Correct Answer:** B) `push()` adds one or more elements to the end of an array and returns the new length; `pop()` removes and returns the last element.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Those are the behaviors of `unshift()` (add to front) and `shift()` (remove from front), not `push`/`pop`.
    *   *Why B is correct:* `push` targets the tail and returns the new `length`; `pop` targets the tail and returns the removed element.
    *   *Why C is incorrect:* Both methods have meaningful return values — `push` returns the new length; `pop` returns the removed element.
    *   *Why D is incorrect:* Both `push` and `pop` mutate the original array in place; they do not create new arrays.

---

**Question 3**
What is the value of `arr` and the return value of the call in the following code?
```javascript
const arr = [1, 2, 3];
const result = arr.push(4, 5);
```
*   A) `arr` is `[1, 2, 3]` and `result` is `[1, 2, 3, 4, 5]`
*   B) `arr` is `[1, 2, 3, 4, 5]` and `result` is `5` (the new length)
*   C) `arr` is `[4, 5, 1, 2, 3]` and `result` is `5`
*   D) `arr` is unchanged and `result` is a new array `[1, 2, 3, 4, 5]`
*   **Correct Answer:** B) `arr` is `[1, 2, 3, 4, 5]` and `result` is `5` (the new length).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `push` mutates the original array; `arr` changes. The return value is the new length, not the array itself.
    *   *Why B is correct:* `push` appends elements to the end of the array and returns the resulting length (`5`).
    *   *Why C is incorrect:* `push` appends to the end, not the beginning. Prepending is done with `unshift`.
    *   *Why D is incorrect:* `push` mutates the original array; it does not create a new one.

---

**Question 4**
While working on **Arrays**, a developer needs to extract a portion of an array without modifying the original. Which method is most appropriate?
*   A) `splice()` — removes and returns the portion from the original array
*   B) `pop()` — removes and returns the last element
*   C) `slice()` — returns a shallow copy of a portion of the array without mutating the original
*   D) `shift()` — removes and returns the first element
*   **Correct Answer:** C) `slice()` — returns a shallow copy of a portion of the array without mutating the original.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `splice()` modifies the original array in place (removes or inserts elements); it does not preserve the original.
    *   *Why B is incorrect:* `pop()` removes only the last element and mutates the array.
    *   *Why C is correct:* `slice(start, end)` returns a new array containing elements from `start` up to (but not including) `end`; the original array is unchanged.
    *   *Why D is incorrect:* `shift()` removes only the first element and mutates the array.

---

**Question 5**
What does `arr.length` return for `const arr = ["a", "b", "c"]`?
*   A) `2` (the index of the last element)
*   B) `3` (the total number of elements)
*   C) `"abc"` (all elements concatenated)
*   D) `undefined` (length is not a property of arrays, only strings)
*   **Correct Answer:** B) `3` (the total number of elements).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The last index is `2`, but `length` reports the count of elements, not the last index.
    *   *Why B is correct:* `arr.length` always returns the total number of elements; for a three-element array it is `3`.
    *   *Why C is incorrect:* `arr.join("")` would produce `"abc"`; `length` is a numeric count.
    *   *Why D is incorrect:* Arrays in JavaScript have a `length` property just like strings; it is one of the most frequently used array properties.
