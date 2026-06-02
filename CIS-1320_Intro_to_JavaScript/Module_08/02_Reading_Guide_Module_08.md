# Reading Guide: Module 08 — Arrays and Array Methods

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

An array is an ordered, indexed collection of values. Arrays are the most frequently used data structure in JavaScript — every list of search results, every shopping cart, every set of chart data points is an array. JavaScript arrays are dynamic (they can grow or shrink), can hold mixed types, and come with a large library of built-in methods. This module covers the core methods you will use daily and that appear on the JSE certification exam.

---

## 1. Array Fundamentals

### Creating Arrays

```javascript
const empty = [];
const fruits = ['apple', 'banana', 'cherry'];
const mixed = [1, 'hello', true, null, { name: 'Alice' }];
```

Arrays are zero-indexed. The first element is at index `0`, the last at index `length - 1`.

### Accessing Elements

```javascript
const arr = [10, 20, 30, 40, 50];

console.log(arr[0]);              // 10
console.log(arr[4]);              // 50
console.log(arr[arr.length - 1]); // 50 — last element
console.log(arr[10]);             // undefined — out of bounds, no error
```

### `length` Property

`arr.length` returns the number of elements. It updates automatically when elements are added or removed.

---

## 2. Mutating Methods

These methods **modify the original array** and return various things:

### `push` and `pop` — Work at the End

```javascript
const stack = ['a', 'b'];

stack.push('c');       // adds to end; returns new length
stack.push('d', 'e'); // can push multiple elements
console.log(stack);   // ['a', 'b', 'c', 'd', 'e']

const last = stack.pop();   // removes and returns last element
console.log(last);          // 'e'
console.log(stack);         // ['a', 'b', 'c', 'd']
```

### `unshift` and `shift` — Work at the Beginning

```javascript
const queue = ['b', 'c'];

queue.unshift('a');   // adds to beginning; returns new length
console.log(queue);   // ['a', 'b', 'c']

const first = queue.shift();   // removes and returns first element
console.log(first);            // 'a'
console.log(queue);            // ['b', 'c']
```

`unshift`/`shift` are slower than `push`/`pop` on large arrays because inserting or removing at the front requires re-indexing every element.

### `splice` — Insert, Remove, or Replace at Any Position

```javascript
splice(startIndex, deleteCount, ...itemsToInsert)
```

```javascript
const letters = ['a', 'b', 'c', 'd', 'e'];

// Remove 2 elements starting at index 1
const removed = letters.splice(1, 2);
console.log(removed);   // ['b', 'c']
console.log(letters);   // ['a', 'd', 'e']

// Insert 'X' and 'Y' at index 1 without deleting
letters.splice(1, 0, 'X', 'Y');
console.log(letters);   // ['a', 'X', 'Y', 'd', 'e']
```

`splice` modifies the original array and returns the removed elements as an array.

### `sort` and `reverse`

```javascript
const nums = [3, 1, 4, 1, 5, 9];

nums.sort((a, b) => a - b);   // ascending — comparator required for numbers
console.log(nums);             // [1, 1, 3, 4, 5, 9]

nums.reverse();                // reverses in-place
console.log(nums);             // [9, 5, 4, 3, 1, 1]
```

**Warning:** Without a comparator, `sort` converts elements to strings and sorts lexicographically. `[10, 9, 2].sort()` produces `[10, 2, 9]` — `'10' < '2'` in string order. Always provide `(a, b) => a - b` for numeric arrays.

---

## 3. Non-Mutating Methods

These methods **return a new value and do not modify the original array**:

### `slice` — Copy a Portion

```javascript
slice(startIndex, endIndex)   // endIndex is exclusive
```

```javascript
const arr = [1, 2, 3, 4, 5];

console.log(arr.slice(1, 4));  // [2, 3, 4]
console.log(arr.slice(2));     // [3, 4, 5] — from index 2 to end
console.log(arr.slice(-2));    // [4, 5] — last 2 elements
console.log(arr);              // [1, 2, 3, 4, 5] — unchanged
```

### `splice` vs `slice`

| Method | Modifies original? | Returns |
|---|---|---|
| `splice(start, count)` | Yes | Removed elements |
| `slice(start, end)` | No | New sub-array |

### `indexOf` and `includes`

```javascript
const colors = ['red', 'green', 'blue', 'green'];

console.log(colors.indexOf('green'));   // 1 — first occurrence
console.log(colors.indexOf('purple')); // -1 — not found

console.log(colors.includes('blue'));   // true
console.log(colors.includes('purple')); // false
```

Use `includes` for existence checks; use `indexOf` when you need the position.

### `join`

```javascript
const words = ['Hello', 'world'];
console.log(words.join(' '));   // 'Hello world'
console.log(words.join('-'));   // 'Hello-world'
console.log(words.join(''));    // 'Helloworld'
```

### `concat`

```javascript
const a = [1, 2];
const b = [3, 4];
const c = a.concat(b, [5, 6]);
console.log(c);   // [1, 2, 3, 4, 5, 6]
console.log(a);   // [1, 2] — unchanged
```

---

## 4. Higher-Order Methods: `map`, `filter`, `reduce`

These three methods accept a callback function and are the cornerstone of functional-style JavaScript. **None of them modify the original array.**

### `map` — Transform Every Element

`map` calls the callback on every element and returns a **new array of the same length** containing the results:

```javascript
const prices = [10, 25, 50];
const discounted = prices.map(price => price * 0.9);
console.log(discounted);   // [9, 22.5, 45]
console.log(prices);       // [10, 25, 50] — unchanged
```

The callback receives `(currentValue, index, array)`. Typically only `currentValue` is used.

### `filter` — Keep Elements That Pass a Test

`filter` calls the callback on every element and returns a **new array containing only elements where the callback returned truthy**:

```javascript
const scores = [72, 85, 91, 68, 55, 99];
const passing = scores.filter(score => score >= 60);
console.log(passing);   // [72, 85, 91, 68, 99]
console.log(scores);    // unchanged
```

The filtered array may be shorter than the original.

### `reduce` — Accumulate to a Single Value

`reduce` calls the callback on every element, passing the result of the previous call as the accumulator:

```javascript
reduce(callback, initialValue)
// callback receives: (accumulator, currentValue, index, array)
```

```javascript
const nums = [1, 2, 3, 4, 5];
const sum = nums.reduce((acc, cur) => acc + cur, 0);
console.log(sum);   // 15
```

Trace through the execution:

| Iteration | `acc` | `cur` | Returns |
|---|---|---|---|
| 1 | 0 (initial) | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 6 | 4 | 10 |
| 5 | 10 | 5 | 15 |

`reduce` is the most general method — it can produce any type of output, including objects:

```javascript
const letters = ['a', 'b', 'a', 'c', 'b', 'a'];
const counts = letters.reduce((acc, letter) => {
  acc[letter] = (acc[letter] ?? 0) + 1;
  return acc;
}, {});
console.log(counts);   // { a: 3, b: 2, c: 1 }
```

### `map` vs `filter` vs `reduce` — Summary

| Method | Returns | Use when |
|---|---|---|
| `map` | New array, same length | Transforming every element |
| `filter` | New array, same or shorter | Selecting elements by condition |
| `reduce` | Single value (any type) | Accumulating all elements into one result |

### Chaining Higher-Order Methods

Because `map` and `filter` return arrays, they can be chained:

```javascript
const products = [
  { name: 'Widget', price: 12, inStock: true },
  { name: 'Gadget', price: 45, inStock: false },
  { name: 'Doohickey', price: 8, inStock: true }
];

const availableNames = products
  .filter(p => p.inStock)
  .map(p => p.name);

console.log(availableNames);   // ['Widget', 'Doohickey']
```

---

## 5. `find` and `findIndex`

```javascript
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 3, name: 'Carol' }
];

const found = users.find(u => u.id === 2);
console.log(found);   // { id: 2, name: 'Bob' }

const idx = users.findIndex(u => u.id === 2);
console.log(idx);     // 1

// Not found
const missing = users.find(u => u.id === 99);
console.log(missing);   // undefined
```

`find` returns the first matching element or `undefined`. `findIndex` returns the index or `-1`.

---

## 6. Spread Operator with Arrays

The spread operator `...` expands an array into individual elements:

### Copying an Array

```javascript
const original = [1, 2, 3];
const copy = [...original];
copy.push(4);
console.log(original);   // [1, 2, 3] — unaffected
console.log(copy);       // [1, 2, 3, 4]
```

Assigning `const copy = original` does NOT copy — both variables would point to the same array.

### Merging Arrays

```javascript
const a = [1, 2];
const b = [3, 4];
const merged = [...a, ...b, 5, 6];
console.log(merged);   // [1, 2, 3, 4, 5, 6]
```

### Spreading into Function Arguments

```javascript
const nums = [3, 1, 4, 1, 5];
console.log(Math.max(...nums));   // 5
console.log(Math.min(...nums));   // 1
```

---

## 7. Array Destructuring

Array destructuring extracts elements by position:

```javascript
const [first, second, third] = [10, 20, 30];
console.log(first, second, third);   // 10, 20, 30
```

### Skipping Elements

```javascript
const [a, , c] = [1, 2, 3];   // skip index 1
console.log(a, c);             // 1, 3
```

### Default Values

```javascript
const [x = 0, y = 0, z = 0] = [5, 10];
console.log(x, y, z);   // 5, 10, 0 — z used default
```

### Rest in Destructuring

```javascript
const [head, ...tail] = [1, 2, 3, 4, 5];
console.log(head);   // 1
console.log(tail);   // [2, 3, 4, 5]
```

### Swapping Variables

```javascript
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b);   // 2, 1
```

---

## 8. JSE Certification Exam Tips

1. **Zero-based indexing** — first element is index `0`, last is `length - 1`. Accessing `arr[arr.length]` returns `undefined`.

2. **`splice` modifies; `slice` does not** — `splice` changes the original and returns removed elements. `slice` returns a new sub-array without modification.

3. **`map` always returns a new array of the same length** — even if the callback returns `undefined` for some elements. It never filters.

4. **`filter` returns a new array that may be shorter** — only elements where the callback returns truthy are included.

5. **`reduce` requires a return statement in multi-line callbacks** — if the callback uses braces, the accumulator update must be returned or the next iteration's `acc` will be `undefined`.

6. **`sort` without a comparator sorts lexicographically** — `[10, 9, 2].sort()` produces `[10, 2, 9]`. Always use `(a, b) => a - b` for numbers.

7. **`indexOf` and `includes` use strict equality** — they will not find `NaN` with `indexOf` (NaN !== NaN), but `Array.prototype.includes` does find `NaN`.

8. **Spread creates a shallow copy** — nested objects inside the array are still shared references. Modifying a nested object in the copy also modifies the original.

9. **Array destructuring is positional** — unlike object destructuring (which matches by name), array destructuring assigns by position. Order matters.

10. **Chaining `map`, `filter`, and `reduce`** — because `map` and `filter` return arrays, they can be chained. `reduce` is typically last in a chain because it returns a non-array value.

---

## 9. Study Checklist

- [ ] Watch the Module 08 video lecture by Professor Nash.
- [ ] Read Chapter 4 (Data Structures) of [Eloquent JavaScript](https://eloquentjavascript.net/04_data.html).
- [ ] Read [MDN — Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).
- [ ] Read [MDN — Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).
- [ ] Read [MDN — Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce).
- [ ] Open the console and verify that `splice` changes the original but `slice` does not.
- [ ] Write a `reduce` accumulator trace table manually for a 4-element array.
- [ ] Chain `filter` and `map` on an array of objects.
- [ ] Demonstrate the variable swap using array destructuring.
- [ ] Complete the Module 08 Lab.
- [ ] Complete the Module 08 Quiz.
