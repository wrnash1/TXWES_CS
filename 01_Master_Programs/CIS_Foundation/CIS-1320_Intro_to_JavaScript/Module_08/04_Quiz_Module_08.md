# Quiz: Module 08 — Arrays and Array Methods

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the output of the following code?

```javascript
const arr = [10, 20, 30, 40, 50];
const result = arr.slice(1, 3);
console.log(result);
console.log(arr.length);
```

- A) `[20, 30, 40]` then `5`
- B) `[20, 30]` then `5`
- C) `[20, 30]` then `3`
- D) `[20, 30, 40]` then `3`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `slice(1, 3)` extracts elements from index `1` up to but **not including** index `3`. That is indices `1` and `2` — values `20` and `30`. Index `3` (value `40`) is excluded.
- *Why B is correct:* `slice(1, 3)` returns `[20, 30]`. `slice` does not modify the original array, so `arr.length` remains `5`.
- *Why C is incorrect:* `slice` never modifies the original array. `arr.length` remains `5`, not `3`.
- *Why D is incorrect:* Both errors combined — index `3` is excluded, and `slice` does not change the original length.

---

### Question 2

What is the output of the following code?

```javascript
const arr = ['a', 'b', 'c', 'd', 'e'];
const removed = arr.splice(1, 2);
console.log(removed);
console.log(arr);
```

- A) `['b', 'c']` then `['a', 'b', 'c', 'd', 'e']`
- B) `['a', 'd', 'e']` then `['b', 'c']`
- C) `['b', 'c']` then `['a', 'd', 'e']`
- D) `2` then `['a', 'd', 'e']`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `splice` modifies the original array in-place. After removing two elements, `arr` no longer contains all five elements.
- *Why B is incorrect:* `splice` returns the removed elements (`['b', 'c']`), not the remaining elements. The remaining array `['a', 'd', 'e']` stays in `arr`.
- *Why C is correct:* `splice(1, 2)` removes `2` elements starting at index `1`. The removed elements `['b', 'c']` are returned. The original array is modified to `['a', 'd', 'e']`.
- *Why D is incorrect:* `splice` returns the removed elements as an array, not the count of removed elements.

---

### Question 3

What is the output of the following code?

```javascript
const nums = [1, 2, 3, 4, 5];
const doubled = nums.map(n => n * 2);
console.log(doubled);
console.log(nums);
```

- A) `[2, 4, 6, 8, 10]` then `[2, 4, 6, 8, 10]`
- B) `[2, 4, 6, 8, 10]` then `[1, 2, 3, 4, 5]`
- C) `[1, 2, 3, 4, 5]` then `[2, 4, 6, 8, 10]`
- D) `[2, 4, 6, 8, 10]` then `undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `map` returns a **new array** and does not modify the original. `nums` remains `[1, 2, 3, 4, 5]` after `map`.
- *Why B is correct:* `map` applies the callback to every element and returns a new array `[2, 4, 6, 8, 10]`. The original `nums` is unchanged.
- *Why C is incorrect:* The assignment is `const doubled = nums.map(...)`, so `doubled` holds the transformed array and `nums` holds the original — not the other way around.
- *Why D is incorrect:* `nums` still exists and holds `[1, 2, 3, 4, 5]`. `map` does not affect the variable it is called on.

---

### Question 4

What is the output of the following code?

```javascript
const scores = [55, 80, 90, 45, 70, 65];
const passing = scores.filter(s => s >= 60);
console.log(passing.length);
```

- A) `6`
- B) `4`
- C) `2`
- D) `3`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `6` is the length of the original array. `filter` returns a new, potentially shorter array.
- *Why B is correct:* The scores `>= 60` are `80`, `90`, `70`, and `65` — four values. `55` and `45` are excluded. The filtered array has length `4`.
- *Why C is incorrect:* Only two scores (`55` and `45`) fail the filter — two are excluded, not two are included.
- *Why D is incorrect:* Counting carefully: `55` fails, `80` passes, `90` passes, `45` fails, `70` passes, `65` passes — four pass, not three.

---

### Question 5

What is the output of the following code?

```javascript
const nums = [1, 2, 3, 4];
const result = nums.reduce((acc, cur) => acc + cur, 10);
console.log(result);
```

- A) `10`
- B) `10`
- C) `20`
- D) `14`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A/B is incorrect:* `10` is the initial value of the accumulator, not the final result. The callback runs for every element, adding each to the accumulator.
- *Why C is correct:* The initial accumulator is `10`. After each iteration: `10+1=11`, `11+2=13`, `13+3=16`, `16+4=20`. The final result is `20`.
- *Why D is incorrect:* `14` would be the result if the initial value were `0` (sum of `1+2+3+4=10`) or if only some elements were summed. With an initial value of `10`, all four elements are added to `10`.

---

### Question 6

What is the output of the following code?

```javascript
const arr = [3, 1, 4, 1, 5, 9, 2, 6];
arr.sort();
console.log(arr[0]);
```

- A) `1`
- B) `9`
- C) `2`
- D) `1` (but not reliably)

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct but requires nuance:* Without a comparator, `sort` converts elements to strings and sorts lexicographically. The string representations are `'1'`, `'1'`, `'2'`, `'3'`, `'4'`, `'5'`, `'6'`, `'9'`. In lexicographic order, `'1'` comes first. So `arr[0]` is `1`.
- *Why B is incorrect:* `9` sorts as the string `'9'`, which comes after all single-digit strings starting with lower digits. It would be at the end.
- *Why C is incorrect:* `'2'` sorts after `'1'` lexicographically. `arr[0]` is `1`, not `2`.
- *Why D is incorrect:* For single-digit integers, lexicographic and numeric sort happen to agree (both put `1` first). The problem with default sort is visible with multi-digit numbers like `10` — `'10'` sorts before `'2'` lexicographically but `10 > 2` numerically. For this specific array, `arr[0]` is reliably `1`.

---

### Question 7

What is the output of the following code?

```javascript
const a = [1, 2, 3];
const b = a;
b.push(4);
console.log(a.length);
```

- A) `3`
- B) `4`
- C) `0`
- D) `TypeError: Cannot push to a constant`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `b = a` does not copy the array — it creates a second reference to the same array. Pushing to `b` also pushes to `a`.
- *Why B is correct:* `b` and `a` point to the same array object in memory. `b.push(4)` appends `4` to the shared array. `a.length` is now `4`.
- *Why C is incorrect:* The array is never emptied. It grows from 3 to 4 elements.
- *Why D is incorrect:* `a` is declared with `const`, but `const` prevents reassigning the variable, not modifying the array. Pushing to a `const` array is allowed.

---

### Question 8

What is the output of the following code?

```javascript
const [x, , z] = [10, 20, 30, 40];
console.log(x, z);
```

- A) `10 20`
- B) `10 30`
- C) `10 40`
- D) `undefined undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The second variable position in `[x, , z]` is skipped by the empty slot between the commas. `z` receives the third element (`30`), not the second (`20`).
- *Why B is correct:* Array destructuring is positional. `x` receives index `0` (value `10`). The empty slot skips index `1` (value `20`). `z` receives index `2` (value `30`). Index `3` (value `40`) is ignored.
- *Why C is incorrect:* `40` is at index `3`. `z` receives index `2` (`30`), not index `3`.
- *Why D is incorrect:* Both `x` and `z` match valid indices in the array. Destructuring only returns `undefined` when the index is out of bounds or when a property does not exist.

---

### Question 9

What is the output of the following code?

```javascript
const nums = [3, 7, 1, 9, 4];
const found = nums.find(n => n > 5);
console.log(found);
```

- A) `[7, 9]`
- B) `7`
- C) `9`
- D) `true`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `find` returns the **first** element that satisfies the condition — a single value, not an array. `filter` would return all matching elements as an array.
- *Why B is correct:* `find` iterates from left to right and returns the first element where the callback returns truthy. `3 > 5` is false. `7 > 5` is true — `7` is returned immediately.
- *Why C is incorrect:* `9` also satisfies `n > 5`, but `find` stops at the first match. `7` appears before `9` in the array.
- *Why D is incorrect:* `find` returns the matching element value, not the boolean result of the condition. `filter` also returns values, not booleans.

---

### Question 10

Which of the following correctly merges `arr1` and `arr2` into a new array without modifying either original?

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
```

- A) `const merged = arr1.push(...arr2);`
- B) `const merged = arr1 + arr2;`
- C) `const merged = [...arr1, ...arr2];`
- D) `const merged = arr1.concat; arr2;`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `arr1.push(...arr2)` modifies `arr1` in-place and returns the new length (a number), not a merged array. `merged` would be `6`, not `[1, 2, 3, 4, 5, 6]`.
- *Why B is incorrect:* The `+` operator on arrays coerces both to strings and concatenates them. `[1,2,3] + [4,5,6]` produces the string `'1,2,34,5,6'`.
- *Why C is correct:* `[...arr1, ...arr2]` creates a new array containing all elements of `arr1` followed by all elements of `arr2`. Neither original is modified.
- *Why D is incorrect:* `arr1.concat` without `()` is a reference to the method function, not a call. The semicolon then treats `arr2` as a separate statement. This does not produce a merged array.

---

### Question 11

What is the output of the following code?

```javascript
const arr = [1, 2, 3, 4, 5];
const result = arr.every(n => n > 0);
const result2 = arr.some(n => n > 4);
console.log(result, result2);
```

- A) `false` `true`
- B) `true` `false`
- C) `true` `true`
- D) `false` `false`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `every(n => n > 0)` returns `true` because all elements (`1`, `2`, `3`, `4`, `5`) satisfy `n > 0`.
- *Why B is incorrect:* `some(n => n > 4)` returns `true` because at least one element (`5`) satisfies `n > 4`.
- *Why C is correct:* `every` returns `true` when all elements pass the test — all five are greater than `0`. `some` returns `true` when at least one element passes the test — `5 > 4` is true.
- *Why D is incorrect:* Both `every` and `some` return `true` for this array and these conditions.

---

### Question 12

What is the output of the following code?

```javascript
const words = ['hello', 'world', 'foo'];
const result = words.map(w => w.toUpperCase()).join(' - ');
console.log(result);
```

- A) `['HELLO', 'WORLD', 'FOO']`
- B) `'HELLO-WORLD-FOO'`
- C) `'HELLO - WORLD - FOO'`
- D) `'hello - world - foo'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `map` produces a new array, but then `.join(' - ')` is chained, which converts the array to a string with the specified separator.
- *Why B is incorrect:* The separator passed to `join` is `' - '` (space-hyphen-space), not just `'-'`. The output includes spaces around the hyphens.
- *Why C is correct:* `map` produces `['HELLO', 'WORLD', 'FOO']`. `join(' - ')` joins with `' - '` as separator: `'HELLO - WORLD - FOO'`.
- *Why D is incorrect:* `map(w => w.toUpperCase())` converts each word to uppercase. The original lowercase strings are not preserved in the output.

---

### Question 13

What is the output of the following code?

```javascript
const arr = [1, [2, 3], [4, [5, 6]]];
console.log(arr.flat());
console.log(arr.flat(2));
```

- A) `[1, 2, 3, 4, 5, 6]` then `[1, 2, 3, 4, 5, 6]`
- B) `[1, [2, 3], [4, [5, 6]]]` then `[1, 2, 3, 4, 5, 6]`
- C) `[1, 2, 3, 4, [5, 6]]` then `[1, 2, 3, 4, 5, 6]`
- D) `[1, 2, 3, 4, 5, 6]` then `[1, 2, 3, 4, [5, 6]]`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `flat()` with no argument defaults to depth `1`. `[4, [5, 6]]` becomes `[4, [5, 6]]` after one level of flattening — the inner `[5, 6]` is not flattened in the first call.
- *Why B is incorrect:* `flat()` does flatten one level. `[2, 3]` and `[4, [5, 6]]` are unwrapped — the result is `[1, 2, 3, 4, [5, 6]]`, not the original.
- *Why C is correct:* `flat()` (depth 1): removes one level of nesting → `[1, 2, 3, 4, [5, 6]]`. `flat(2)` (depth 2): removes two levels → `[1, 2, 3, 4, 5, 6]`.
- *Why D is incorrect:* This reverses the results. Greater depth = more flattening, not less.

---

### Question 14

What is the output of the following code?

```javascript
const products = [
  { name: 'pen', price: 1.5 },
  { name: 'notebook', price: 3.0 },
  { name: 'ruler', price: 2.0 }
];
const total = products.reduce((sum, p) => sum + p.price, 0);
console.log(total);
```

- A) `3`
- B) `6.5`
- C) `1.5`
- D) `NaN`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The number of products is `3`, but `reduce` is summing the `price` values, not counting items.
- *Why B is correct:* Starting from `0`, each iteration adds the product's price: `0 + 1.5 = 1.5`, `1.5 + 3.0 = 4.5`, `4.5 + 2.0 = 6.5`. Final result: `6.5`.
- *Why C is incorrect:* `1.5` is the first product's price. `reduce` accumulates across all products.
- *Why D is incorrect:* All prices are valid numbers and the accumulator starts at `0`. No `NaN` is produced.

---

### Question 15

What is the output of the following code?

```javascript
const nums = [5, 3, 8, 1, 9, 2];
const sorted = [...nums].sort((a, b) => a - b);
console.log(sorted[0]);
console.log(nums[0]);
```

- A) `1` then `1`
- B) `1` then `5`
- C) `5` then `5`
- D) `9` then `5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `[...nums]` creates a new array. Sorting the copy does not affect the original `nums`. `nums[0]` remains `5`.
- *Why B is correct:* `[...nums]` makes a shallow copy, then `.sort((a, b) => a - b)` sorts it in ascending order: `[1, 2, 3, 5, 8, 9]`. `sorted[0]` is `1`. The original `nums` is unchanged, so `nums[0]` is still `5`.
- *Why C is incorrect:* `sorted[0]` is `1` after ascending sort.
- *Why D is incorrect:* `9` is the maximum, which would be `sorted[sorted.length - 1]` in ascending order, not `sorted[0]`.

---

### Question 16

What is the output of the following code?

```javascript
const arr = ['a', 'b', 'c'];
arr.forEach((item, index) => {
  arr[index] = item.toUpperCase();
});
console.log(arr);
```

- A) `['a', 'b', 'c']`
- B) `['A', 'B', 'C']`
- C) `undefined`
- D) `TypeError: arr is read-only`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `forEach` executes the callback for each element. The callback mutates `arr[index]` in-place, so the array is modified.
- *Why B is correct:* `forEach` provides `item` and `index` to the callback. For each element, `arr[index] = item.toUpperCase()` replaces the lowercase letter with its uppercase equivalent. After all three iterations, `arr` is `['A', 'B', 'C']`.
- *Why C is incorrect:* `forEach` always returns `undefined`, but this code logs `arr`, not the return value of `forEach`.
- *Why D is incorrect:* `arr` is declared with `const` but its elements are mutable. Modifying elements via index assignment is permitted.

---

### Question 17

What is the output of the following code?

```javascript
const arr = [1, 2, 3, 4, 5];
const result = arr.findIndex(n => n > 3);
console.log(result);
```

- A) `4`
- B) `3`
- C) `[4, 5]`
- D) `true`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `4` is the value of the element at index `3`, not the index itself. `findIndex` returns the index, not the value.
- *Why B is correct:* `findIndex` returns the index of the first element that satisfies the predicate. `1 > 3` = false, `2 > 3` = false, `3 > 3` = false, `4 > 3` = true. Index `3` is returned.
- *Why C is incorrect:* `findIndex` returns a single number (the index), not an array of matching values. `filter` would return matching values as an array.
- *Why D is incorrect:* `findIndex` returns the index (a number), not a boolean. It returns `-1` when no match is found, and `0` or a positive integer when found.

---

### Question 18

What is the output of the following code?

```javascript
const matrix = [[1, 2], [3, 4], [5, 6]];
const flat = matrix.flatMap(row => row);
console.log(flat);
```

- A) `[[1, 2], [3, 4], [5, 6]]`
- B) `[1, 2, 3, 4, 5, 6]`
- C) `[[1, 3, 5], [2, 4, 6]]`
- D) `[1, 2, 3, 4, 5, 6, undefined]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `flatMap` maps and then flattens one level. The mapping `row => row` returns each row as-is, so it is equivalent to `flat()` — the nested arrays are flattened one level.
- *Why B is correct:* `flatMap(row => row)` applies `identity` (returns the row unchanged) and then flattens one level. Each `[1,2]`, `[3,4]`, `[5,6]` is unpacked into the result: `[1, 2, 3, 4, 5, 6]`.
- *Why C is incorrect:* `flatMap` does not transpose the matrix. It flattens the rows sequentially.
- *Why D is incorrect:* `flatMap` does not add `undefined`. All rows have values and the flatten is clean.

---

### Question 19

What is the output of the following code?

```javascript
const arr = [1, 2, 3, 2, 1];
console.log(arr.indexOf(2));
console.log(arr.lastIndexOf(2));
console.log(arr.includes(5));
```

- A) `1`, `3`, `false`
- B) `1`, `3`, `true`
- C) `2`, `2`, `false`
- D) `0`, `4`, `false`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `indexOf(2)` returns the index of the first occurrence of `2`: index `1`. `lastIndexOf(2)` returns the index of the last occurrence of `2`: index `3`. `includes(5)` returns `false` because `5` is not in the array.
- *Why B is incorrect:* `includes(5)` is `false` because `5` does not appear in `[1, 2, 3, 2, 1]`.
- *Why C is incorrect:* `indexOf(2)` returns the index (`1`), not the value. The value `2` is at index `1`.
- *Why D is incorrect:* The first `2` is at index `1`, not `0`. Index `0` holds `1`.

---

### Question 20

What is the output of the following code?

```javascript
const numbers = [10, 20, 30, 40, 50];
const result = numbers
  .filter(n => n > 15)
  .map(n => n / 10)
  .reduce((sum, n) => sum + n, 0);
console.log(result);
```

- A) `14`
- B) `15`
- C) `140`
- D) `10`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `filter(n => n > 15)` → `[20, 30, 40, 50]`. `map(n => n / 10)` → `[2, 3, 4, 5]`. `reduce((sum, n) => sum + n, 0)` → `0 + 2 + 3 + 4 + 5 = 14`.
- *Why B is incorrect:* `15` is not produced. The correct sum of `[2, 3, 4, 5]` with initial value `0` is `14`.
- *Why C is incorrect:* `140` would result if `map` were not applied — summing `[20, 30, 40, 50]` directly equals `140`. But after `map`, the values are divided by `10`.
- *Why D is incorrect:* `10` is `20 / 10 / 2` — not the full chain sum. The reduce accumulates all four mapped values.
