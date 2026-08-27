# Quiz: Module 09 — Array Iteration and Callback Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

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

---

### Question 11

What is the output of the following code?

```javascript
const arr = [];
const result = arr.some(n => n > 0);
console.log(result);
```

- A) `true`
- B) `undefined`
- C) `null`
- D) `false`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `some` returns `true` only when at least one element satisfies the callback. An empty array has no elements, so no element can satisfy the condition. There is nothing to return `true` for.
- *Why B is incorrect:* `some` always returns a boolean — never `undefined`. Unlike `forEach`, `some` always produces a `true` or `false` result.
- *Why C is incorrect:* `some` never returns `null`. Its return type is strictly boolean.
- *Why D is correct:* On an empty array, `some` returns `false` by convention — there is no element that satisfies the condition. This is the counterpart to `every` returning `true` on an empty array.

---

### Question 12

What is the output of the following code?

```javascript
const nums = [1, 2, 3];
const result = nums.map((n, i) => `${i}:${n}`);
console.log(result);
```

- A) `['1:0', '2:1', '3:2']`
- B) `['0:1', '1:2', '2:3']`
- C) `[0, 1, 2]`
- D) `['0:1', '1:2']`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The template literal is `` `${i}:${n}` `` — `i` (the index) comes first, then `n` (the value). At index `0` the value is `1`, producing `'0:1'` not `'1:0'`.
- *Why B is correct:* The callback receives `(element, index)`. At index `0` the element is `1` → `'0:1'`; index `1`, element `2` → `'1:2'`; index `2`, element `3` → `'2:3'`.
- *Why C is incorrect:* The callback returns a string, not just the index. `map` collects the string results, not the `i` values alone.
- *Why D is incorrect:* `map` processes every element and returns an array of the same length. Three elements produce three results, not two.

---

### Question 13

Which of the following best describes why `flatMap` is more efficient than `.map(...).flat(1)`?

- A) `flatMap` flattens to unlimited depth, while `.flat(1)` only flattens one level
- B) `flatMap` skips `undefined` values that `map` would include
- C) `flatMap` avoids creating the intermediate array that `.map()` would produce before flattening
- D) `flatMap` uses a different sorting algorithm internally

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `flatMap` only flattens one level — it is equivalent to `.map(...).flat(1)`, not `.flat(Infinity)`. Unlimited depth requires `flat(Infinity)` explicitly.
- *Why B is incorrect:* Both `map` and `flatMap` include `undefined` values returned by the callback. Neither skips `undefined` automatically.
- *Why C is correct:* `.map(...).flat(1)` builds a full intermediate mapped array in memory, then creates another array during the flatten step. `flatMap` combines both operations in a single pass, avoiding the intermediate allocation.
- *Why D is incorrect:* Sorting is unrelated to `flatMap`. Neither `map` nor `flatMap` reorders elements.

---

### Question 14

What is the output of the following code?

```javascript
function double(n) {
  return n * 2;
}

const result = [1, 2, 3].map(double);
console.log(result);
```

- A) `TypeError` — `double` is not a valid callback syntax
- B) `[2, 4, 6]`
- C) `undefined`
- D) `[1, 2, 3]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Passing a named function reference as a callback is perfectly valid. `map(double)` passes `double` to `map`, which calls `double(element, index, array)` for each element. The extra `index` and `array` arguments are harmlessly ignored.
- *Why B is correct:* `map` calls `double(1)`, `double(2)`, `double(3)` in turn. Each returns `n * 2`, producing `[2, 4, 6]`.
- *Why C is incorrect:* `map` returns a new array, not `undefined`. `forEach` returns `undefined`; `map` does not.
- *Why D is incorrect:* `double` multiplies each element by `2`. The original values `[1, 2, 3]` are transformed, not returned as-is.

---

### Question 15

What is the output of the following code?

```javascript
const words = ['cat', 'elephant', 'ant', 'hippopotamus'];
const result = words.filter(w => w.length > 4).map(w => w.toUpperCase());
console.log(result);
```

- A) `['CAT', 'ELEPHANT', 'ANT', 'HIPPOPOTAMUS']`
- B) `['elephant', 'hippopotamus']`
- C) `['ELEPHANT', 'HIPPOPOTAMUS']`
- D) `['CAT', 'ANT']`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `filter(w => w.length > 4)` removes `'cat'` (3) and `'ant'` (3). Only words longer than 4 characters pass through to `map`.
- *Why B is incorrect:* `map(w => w.toUpperCase())` transforms every surviving element to uppercase. The final result contains uppercase strings, not the original lowercase ones.
- *Why C is correct:* `filter` keeps `'elephant'` (8 chars) and `'hippopotamus'` (12 chars). `map` then uppercases both, producing `['ELEPHANT', 'HIPPOPOTAMUS']`.
- *Why D is incorrect:* `'cat'` and `'ant'` both have 3 characters — neither passes `w.length > 4`. They are excluded by `filter`.

---

### Question 16

What is the output of the following code?

```javascript
const arr = [1, 2, 3, 4, 5];

arr.some(n => {
  console.log(n);
  return n === 3;
});
```

- A) Logs `1`, `2`, `3`, `4`, `5`
- B) Logs `1`, `2`, `3`
- C) Logs `3`
- D) Logs nothing

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `some` short-circuits as soon as the callback returns truthy. When `n === 3` is `true`, `some` stops — `4` and `5` are never visited.
- *Why B is correct:* `some` evaluates `n === 3` for `1` (false), `2` (false), `3` (true). On the `true` result it immediately returns and stops iterating. Only `1`, `2`, and `3` are logged.
- *Why C is incorrect:* `some` logs every element it visits, starting from the beginning. It must check `1` and `2` before reaching `3`.
- *Why D is incorrect:* The callback contains a `console.log` that runs for every element visited. Three elements are visited, so three lines are logged.

---

### Question 17

What is the output of the following code?

```javascript
const matrix = [[1, 2], [3, 4], [5, 6]];
const result = matrix.flatMap(row => row);
console.log(result);
```

- A) `[[1, 2], [3, 4], [5, 6]]`
- B) `[1, 2, 3, 4, 5, 6]`
- C) `[1, 3, 5]`
- D) `[[1, 2, 3, 4, 5, 6]]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That is the original array, unchanged. `flatMap` both maps and flattens, so the result cannot be identical to the input when the callback returns arrays.
- *Why B is correct:* The callback `row => row` returns each sub-array as-is. `flatMap` then flattens one level, spreading each `[1,2]`, `[3,4]`, `[5,6]` into the result. The output is `[1, 2, 3, 4, 5, 6]`.
- *Why C is incorrect:* `[1, 3, 5]` would be the first element of each sub-array. The callback returns the entire row, not just the first element.
- *Why D is incorrect:* `flatMap` flattens the outer level, not re-wraps everything in one more array. The result is a simple flat array.

---

### Question 18

What is the output of the following code?

```javascript
const items = ['apple', 'banana', 'cherry'];
items.forEach((item, index, arr) => {
  if (index === 0) arr[2] = 'grape';
  console.log(item);
});
```

- A) `apple`, `banana`, `cherry`
- B) `apple`, `banana`, `grape`
- C) `grape`, `banana`, `cherry`
- D) `apple`, `grape`, `banana`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `forEach` captures the element values at the time each iteration runs. When `index === 0`, `arr[2]` is mutated to `'grape'`, but `item` for that iteration is already `'apple'`. For index `1`, `item` is `'banana'`. For index `2`, even though `arr[2]` is now `'grape'`, `item` has already been bound to the original `'cherry'` value for that iteration.
- *Why B is incorrect:* The `item` parameter for index `2` reflects the value at the time that iteration begins. The mutation at index `0` changes the array but `forEach` has already queued `'cherry'` for position `2`; the logged value depends on implementation but the spec says element is read at the start of each call — `'cherry'` was already scheduled.
- *Why C is incorrect:* The mutation happens during the first iteration, after `apple` is already logged. `grape` replaces index `2`, not index `0`.
- *Why D is incorrect:* No element is logged at the position of index `1` before the mutation affects index `2`. `banana` is still logged at index `1` unchanged.

---

### Question 19

Which of the following best explains the difference between `find` and `filter`?

- A) `find` searches from the end of the array; `filter` searches from the beginning
- B) `find` returns the first matching element or `undefined`; `filter` returns all matching elements in a new array
- C) `find` modifies the original array; `filter` does not
- D) `find` accepts only named functions; `filter` accepts arrow functions

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both `find` and `filter` iterate from the beginning of the array (index 0). `findLast` searches from the end, but that is a separate method.
- *Why B is correct:* `find` stops at the first element where the callback returns truthy and returns that element (or `undefined` if none match). `filter` iterates the entire array and returns a new array of all elements where the callback returned truthy.
- *Why C is incorrect:* Neither `find` nor `filter` modifies the original array. Both are non-mutating methods.
- *Why D is incorrect:* Both methods accept any callable: named functions, anonymous functions, arrow functions, or method references. Callback syntax is not restricted by which method is used.

---

### Question 20

What is the output of the following code?

```javascript
const threshold = 10;
const nums = [5, 15, 8, 20, 3];
const result = nums.filter(n => n > threshold);
console.log(result);
```

- A) `[5, 8, 3]`
- B) `[15, 20]`
- C) `[10, 15, 20]`
- D) `TypeError` — `threshold` is not accessible inside the arrow function

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `[5, 8, 3]` are the elements that are NOT greater than `10`. `filter` keeps elements where the callback returns truthy — the opposite set.
- *Why B is correct:* The arrow function `n => n > threshold` forms a closure over `threshold`. It can access `threshold` from the enclosing scope. `15 > 10` and `20 > 10` are both `true`, so the result is `[15, 20]`.
- *Why C is incorrect:* `10` itself fails the condition `n > threshold` (`10 > 10` is `false`). Only strictly greater values are included.
- *Why D is incorrect:* Arrow functions close over variables from their enclosing scope. `threshold` is declared in the same scope as the `filter` call, so the callback can access it without any error.
