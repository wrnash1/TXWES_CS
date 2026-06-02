# Quiz: Module 05 — Loops and Iteration

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

How many times does the following loop execute?

```javascript
for (let i = 0; i <= 4; i++) {
  console.log(i);
}
```

- A) 4 times
- B) 5 times
- C) 6 times
- D) 0 times

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Four iterations would result from `i < 4` starting at `0` (values 0, 1, 2, 3). The condition here is `i <= 4`, which includes `4` as a valid value.
- *Why B is correct:* `i` starts at `0` and the condition is `i <= 4`. The loop runs for `i = 0, 1, 2, 3, 4` — five iterations. When `i` becomes `5`, `5 <= 4` is false and the loop ends.
- *Why C is incorrect:* Six iterations would result from `i <= 5` starting at `0`. The upper bound here is `4`, not `5`.
- *Why D is incorrect:* `0 <= 4` is true on the first check, so the loop runs immediately.

---

### Question 2

What is the output of the following code?

```javascript
for (let i = 1; i < 4; i++) {
  console.log(i);
}
```

- A) `1`, `2`, `3`, `4`
- B) `1`, `2`, `3`
- C) `0`, `1`, `2`, `3`
- D) `1`, `2`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The condition is `i < 4`, which is false when `i === 4`. The value `4` is never printed.
- *Why B is correct:* `i` starts at `1`. The condition `i < 4` is true for `i = 1, 2, 3`. When `i` becomes `4`, `4 < 4` is false and the loop ends. Output: `1`, `2`, `3`.
- *Why C is incorrect:* `i` is initialized to `1`, not `0`. The value `0` is never part of this loop.
- *Why D is incorrect:* When `i = 3`, `3 < 4` is still true, so `3` is printed before `i` becomes `4`.

---

### Question 3

What is the output of the following code?

```javascript
let x = 0;

while (x < 3) {
  console.log(x);
  x++;
}
```

- A) `0`, `1`, `2`, `3`
- B) `0`, `1`, `2`
- C) `1`, `2`, `3`
- D) The loop runs forever

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* When `x === 3`, the condition `3 < 3` is false. The loop exits before printing `3`.
- *Why B is correct:* `x` starts at `0`. The body runs for `x = 0, 1, 2`. After printing `2`, `x++` makes `x = 3`, then `3 < 3` is false and the loop ends.
- *Why C is incorrect:* `x` starts at `0`. The first iteration prints `0` before `x++` increments it to `1`.
- *Why D is incorrect:* `x++` is present inside the loop, so `x` increases each iteration. The condition `x < 3` will eventually become false.

---

### Question 4

What is the output of the following code?

```javascript
let count = 5;

do {
  console.log('count is', count);
  count++;
} while (count < 3);
```

- A) Nothing is printed
- B) `count is 5` then `count is 6`
- C) `count is 5`
- D) `count is 5` printed indefinitely

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `do-while` always executes the body at least once regardless of the condition. Even though `5 < 3` is immediately false, the body runs before the condition is checked.
- *Why B is incorrect:* After the body runs once, `count` becomes `6`. Then the condition `6 < 3` is checked — still false. The loop ends. `count is 6` is never printed.
- *Why C is correct:* The body runs once (printing `count is 5`), `count++` makes `count = 6`, then `6 < 3` is false. The loop ends after one execution.
- *Why D is incorrect:* The loop does not run indefinitely because `count++` increments `count`, and `count < 3` starts false and stays false. There is no infinite loop here.

---

### Question 5

What is the output of the following code?

```javascript
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}
```

- A) `0`, `1`, `2`, `3`, `4`
- B) `0`, `1`, `2`, `3`
- C) `0`, `1`, `2`
- D) `3`, `4`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `break` at `i === 3` exits the loop before printing `3`. Values `3` and `4` are never reached.
- *Why B is incorrect:* When `i === 3`, the `if` block runs `break` before `console.log(i)`. The value `3` is never printed.
- *Why C is correct:* The loop runs for `i = 0` (prints `0`), `i = 1` (prints `1`), `i = 2` (prints `2`). When `i = 3`, the `if` condition is true and `break` exits the loop immediately — before `console.log(3)` runs.
- *Why D is incorrect:* `break` exits the loop when `i === 3`. Nothing after that point runs.

---

### Question 6

What is the output of the following code?

```javascript
for (let i = 0; i < 6; i++) {
  if (i % 3 === 0) {
    continue;
  }
  console.log(i);
}
```

- A) `0`, `3`
- B) `1`, `2`, `4`, `5`
- C) `0`, `1`, `2`, `3`, `4`, `5`
- D) `1`, `2`, `3`, `4`, `5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `0 % 3 === 0` and `3 % 3 === 0` are both true, so `continue` skips those iterations. `0` and `3` are the values that are skipped — not printed.
- *Why B is correct:* When `i` is divisible by 3 (`i = 0` and `i = 3`), `continue` skips `console.log`. The remaining values `1`, `2`, `4`, `5` are printed.
- *Why C is incorrect:* `continue` prevents printing when `i % 3 === 0`, so `0` and `3` are skipped.
- *Why D is incorrect:* `3 % 3 === 0` is true, so `3` is also skipped by `continue`. Only `1`, `2`, `4`, `5` are printed.

---

### Question 7

What is the output of the following code?

```javascript
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 2) {
      break;
    }
    console.log(i, j);
  }
}
```

- A) `0 0`, `0 1`, `1 0`, `1 1`, `2 0`, `2 1`
- B) `0 0`, `0 1`, `0 2`, `1 0`, `1 1`, `1 2`, `2 0`, `2 1`, `2 2`
- C) `0 0`, `0 1`
- D) `0 0`, `1 0`, `2 0`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `break` at `j === 2` exits only the inner loop. The outer loop continues for `i = 0, 1, 2`. For each value of `i`, the inner loop prints `j = 0` and `j = 1` before `j = 2` triggers `break`. Result: six pairs total.
- *Why B is incorrect:* `j = 2` is never printed because `break` fires before `console.log`. The inner loop exits at `j = 2` every time.
- *Why C is incorrect:* `break` exits the inner loop, not the outer loop. After the inner loop exits with `i = 0`, the outer loop continues to `i = 1` and `i = 2`.
- *Why D is incorrect:* This would be the result if `break` also exited the outer loop (only printing `j = 0` for each `i`). But `break` fires at `j = 2`, which means `j = 0` and `j = 1` both print for each iteration of `i`.

---

### Question 8

What is the output of the following code?

```javascript
const arr = ['a', 'b', 'c'];

for (const idx in arr) {
  console.log(idx, typeof idx);
}
```

- A) `a string`, `b string`, `c string`
- B) `0 number`, `1 number`, `2 number`
- C) `0 string`, `1 string`, `2 string`
- D) `a number`, `b number`, `c number`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `for...in` iterates the **keys** (indices) of the array, not the values. The values `'a'`, `'b'`, `'c'` are not produced by `for...in`.
- *Why B is incorrect:* `for...in` always produces keys as **strings**, even when used on an array. The typeof of array indices from `for...in` is `'string'`, not `'number'`.
- *Why C is correct:* `for...in` on an array yields the array's index keys as strings: `'0'`, `'1'`, `'2'`. `typeof '0'` is `'string'`. This is the key trap — indices look like numbers but are returned as strings.
- *Why D is incorrect:* `for...in` produces keys, not values, and those keys are strings, not numbers.

---

### Question 9

Which of the following correctly iterates over the **values** of an array using a modern loop?

```javascript
const nums = [10, 20, 30];
```

- A) `for (const i in nums) { console.log(nums[i]); }`
- B) `for (const n of nums) { console.log(n); }`
- C) `for (const n in nums) { console.log(n); }`
- D) `while (nums) { console.log(nums); }`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This uses `for...in`, which produces string index keys. `nums[i]` would access the values, but it relies on string-to-number coercion of the index. This works coincidentally but is not the correct pattern and can fail with array-like objects. It is not the idiomatic answer.
- *Why B is correct:* `for...of` iterates the values of an iterable directly. `n` takes the value `10`, then `20`, then `30`. This is the correct and idiomatic pattern for iterating array values.
- *Why C is incorrect:* `for...in` on `nums` produces the string keys `'0'`, `'1'`, `'2'` — not the values `10`, `20`, `30`. `console.log(n)` would print the index strings, not the array values.
- *Why D is incorrect:* `nums` is an array object, which is truthy, so `while (nums)` would run forever — an infinite loop. This does not iterate the array.

---

### Question 10

What is the output of the following code?

```javascript
const book = { title: 'Eloquent JavaScript', pages: 472, free: true };

for (const prop in book) {
  console.log(prop);
}
```

- A) `'Eloquent JavaScript'`, `472`, `true`
- B) `title`, `pages`, `free`
- C) `title: 'Eloquent JavaScript'`, `pages: 472`, `free: true`
- D) `0`, `1`, `2`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `for...in` iterates the **property names** (keys), not the values. The values `'Eloquent JavaScript'`, `472`, `true` are accessed via `book[prop]`, not produced by the loop variable itself.
- *Why B is correct:* `for...in` on a plain object yields each enumerable property name as a string: `'title'`, `'pages'`, `'free'`. `console.log(prop)` prints each key.
- *Why C is incorrect:* `for...in` does not produce `key: value` pairs. It produces only the key. To get both key and value together, you would need `console.log(prop, ':', book[prop])`.
- *Why D is incorrect:* `0`, `1`, `2` are array indices. `book` is a plain object — `for...in` on a plain object produces the property names, not numeric indices.
