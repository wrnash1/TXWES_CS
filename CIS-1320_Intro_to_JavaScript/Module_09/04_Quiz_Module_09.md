# Quiz: Module 09 — Array Iteration and Callback Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the output of the following code?

```javascript
const nums = [1, 2, 3, 4, 5];
const result = nums.forEach(n => n * 2);
console.log(result);
```

- A) `[2, 4, 6, 8, 10]`
- B) `[1, 2, 3, 4, 5]`
- C) `undefined`
- D) `0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `forEach` does not collect the callback's return values into a new array. That is what `map` does. The callback returns `n * 2` on each call, but `forEach` discards those return values.
- *Why B is incorrect:* `forEach` does not return the original array either. It always returns `undefined`, regardless of what the callback does.
- *Why C is correct:* `forEach` always returns `undefined`. It is designed for side effects — performing actions on each element — not for producing a result.
- *Why D is incorrect:* `0` has no relationship to `forEach`'s return value. `forEach` never returns a number.

---

### Question 2

What is the output of the following code?

```javascript
const arr = [10, 20, 30, 40, 50];
const result = arr.every(n => n > 5);
console.log(result);
```

- A) `false`
- B) `[10, 20, 30, 40, 50]`
- C) `5`
- D) `true`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Every element in the array (`10`, `20`, `30`, `40`, `50`) is greater than `5`. The condition `n > 5` returns `true` for all of them, so `every` returns `true`.
- *Why B is incorrect:* `every` returns a boolean, not an array. It tests a condition across all elements.
- *Why C is incorrect:* `5` is the value used in the comparison, not the return value of `every`.
- *Why D is correct:* `every` checks whether the callback returns truthy for every element. Since all five values are greater than `5`, every iteration returns `true`, and `every` returns `true`.

---

### Question 3

What is the output of the following code?

```javascript
const arr = [1, 3, 5, 6, 7];
const result = arr.every(n => {
  console.log(n);
  return n % 2 !== 0;
});
```

- A) Logs `1`, `3`, `5`, `6`, `7` — then `result` is `false`
- B) Logs `1`, `3`, `5`, `6` — then `result` is `false`
- C) Logs `1`, `3`, `5` — then `result` is `true`
- D) Logs nothing — `result` is `false`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `every` short-circuits as soon as the callback returns falsy. When `n = 6`, `6 % 2 !== 0` is `false`. The loop stops — `7` is never checked.
- *Why B is correct:* `every` iterates `1` (odd → true), `3` (odd → true), `5` (odd → true), `6` (even → false). At `6`, the condition fails and `every` immediately returns `false`. `7` is never reached.
- *Why C is incorrect:* After `5` the callback returns `true`. The loop does not stop on `true` with `every` — it continues until it finds a `false` or exhausts the array. It finds `false` at `6`.
- *Why D is incorrect:* The callback does log each element as it is checked. Iteration is visible through the logs.

---

### Question 4

What is the output of the following code?

```javascript
const arr = [4, 8, 15, 16, 23];
const result = arr.some(n => n > 10);
console.log(result);
```

- A) `false`
- B) `15`
- C) `true`
- D) `[15, 16, 23]`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `15` is greater than `10`, so at least one element satisfies the condition. `some` returns `true` because it found a match.
- *Why B is incorrect:* `some` returns a boolean, not the matching element. `find` would return the matching element.
- *Why C is correct:* `some` checks whether at least one element satisfies the callback. `4 > 10` is false, `8 > 10` is false, `15 > 10` is true — `some` short-circuits and returns `true`.
- *Why D is incorrect:* `some` returns a boolean, not an array. `filter` would return the array of matching elements.

---

### Question 5

What is the output of the following code?

```javascript
const result = [].every(n => n > 0);
console.log(result);
```

- A) `false`
- B) `undefined`
- C) `null`
- D) `true`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* An empty array has no elements that fail the condition. There is nothing to disprove the claim "all elements are > 0." `every` vacuously returns `true`.
- *Why B is incorrect:* `every` always returns a boolean. It never returns `undefined`.
- *Why C is incorrect:* `every` never returns `null`. The result is always `true` or `false`.
- *Why D is correct:* By mathematical convention, a universal statement over an empty set is vacuously true. `every` on an empty array always returns `true` — there are no counterexamples.

---

### Question 6

What is the output of the following code?

```javascript
const nested = [1, [2, 3], [4, [5, 6]]];
console.log(nested.flat());
```

- A) `[1, 2, 3, 4, 5, 6]`
- B) `[1, [2, 3], [4, [5, 6]]]`
- C) `[1, 2, 3, 4, [5, 6]]`
- D) `1, 2, 3, 4, 5, 6`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `flat()` with no argument (or `flat(1)`) only flattens one level. The inner `[5, 6]` is nested two levels deep — one level inside `[4, [5, 6]]` and one level inside `nested`. After one level of flattening, `[5, 6]` still remains as an array.
- *Why B is incorrect:* `flat()` does flatten the first level — `[2, 3]` and `[4, [5, 6]]` are unpacked into `nested`. The result is not the unchanged original.
- *Why C is correct:* `flat(1)` unpacks the direct sub-arrays: `[2, 3]` becomes `2, 3` and `[4, [5, 6]]` becomes `4, [5, 6]`. The `[5, 6]` remains because it was nested two levels deep.
- *Why D is incorrect:* `flat` returns an array, not a comma-separated sequence. The result is `[1, 2, 3, 4, [5, 6]]`.

---

### Question 7

What is the output of the following code?

```javascript
const sentences = ['hello world', 'foo bar'];
const result = sentences.flatMap(s => s.split(' '));
console.log(result);
```

- A) `[['hello', 'world'], ['foo', 'bar']]`
- B) `['hello world', 'foo bar']`
- C) `['hello', 'world', 'foo', 'bar']`
- D) `['hello', 'world']`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* That would be the result of `map`, not `flatMap`. `map` returns `[['hello', 'world'], ['foo', 'bar']]` — an array of arrays. `flatMap` maps then flattens one level.
- *Why B is incorrect:* That is the original array, unchanged. `flatMap` applies the callback and flattens.
- *Why C is correct:* `flatMap` applies `s.split(' ')` to each string, producing `['hello', 'world']` and `['foo', 'bar']`. The one-level flatten merges them into `['hello', 'world', 'foo', 'bar']`.
- *Why D is incorrect:* Only the first sentence's words. Both sentences are processed — `flatMap` iterates all elements.

---

### Question 8

A function `isAdult` is defined as:

```javascript
function isAdult(age) {
  return age >= 18;
}
```

Which of the following correctly uses `isAdult` as a callback to filter an array?

```javascript
const ages = [15, 22, 17, 30, 16, 25];
```

- A) `ages.filter(isAdult())`
- B) `ages.filter('isAdult')`
- C) `ages.filter(isAdult)`
- D) `ages.filter(return isAdult)`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `isAdult()` calls the function immediately with no argument. `isAdult(undefined)` evaluates to `false` (since `undefined >= 18` is `false`). `filter(false)` receives a non-function and throws a `TypeError`.
- *Why B is incorrect:* `'isAdult'` is a string, not a function reference. `filter` requires a function as its argument. Passing a string throws a `TypeError`.
- *Why C is correct:* `isAdult` (without parentheses) is a reference to the function. `filter` receives the function and calls it for each element, passing the element as the argument. This is the correct callback syntax.
- *Why D is incorrect:* `return isAdult` is not valid syntax outside a function body. You cannot use `return` as part of an expression passed to another function.

---

### Question 9

What is the output of the following code?

```javascript
const nums = [2, 4, 6, 8];
nums.forEach((n, i) => {
  if (i === 2) return;
  console.log(n);
});
```

- A) `2`, `4`
- B) `2`, `4`, `8`
- C) `2`, `4`, `6`, `8`
- D) Nothing is printed

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `return` inside a `forEach` callback exits the current callback invocation — it does not exit the entire `forEach` loop. After skipping index `2`, the loop continues to index `3`.
- *Why B is correct:* `return` inside a `forEach` callback only skips the rest of that iteration — similar to `continue` in a `for` loop. When `i === 2`, the callback returns early and `6` is not logged. The loop continues, and `8` (at index `3`) is logged.
- *Why C is incorrect:* `6` is skipped because of the `return` when `i === 2`.
- *Why D is incorrect:* The loop runs for all indices. Only the iteration at `i === 2` is short-circuited via `return`. The other three log their values.

---

### Question 10

Which method is most appropriate for this task: "Check whether all products in an array have a price greater than zero"?

- A) `forEach`
- B) `map`
- C) `some`
- D) `every`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `forEach` does not return a value. To check whether all products satisfy a condition, you need a method that produces a boolean result.
- *Why B is incorrect:* `map` transforms every element into a new value and returns a new array. It does not check whether all elements satisfy a condition.
- *Why C is incorrect:* `some` checks whether **at least one** element satisfies the condition. "All products have a price greater than zero" is a universal claim — it requires `every`.
- *Why D is correct:* `every` returns `true` if the callback returns truthy for every element. `products.every(p => p.price > 0)` directly answers "do all products have a positive price?" with a single boolean.
