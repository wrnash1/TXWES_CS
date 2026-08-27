# Reading Guide: Module 09 — Array Iteration and Callback Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Module 08 introduced `map`, `filter`, and `reduce`. Module 09 examines the underlying mechanism: callback functions. A callback is any function passed as an argument to another function, to be called later. Understanding callbacks — why functions are values, how they carry their surrounding scope, and how to pass them intentionally — unlocks every higher-order pattern in JavaScript. This module also adds `forEach`, `every`, `some`, `flat`, and `flatMap` to complete the iteration toolkit.

---

## 1. Callbacks: Functions as Values

JavaScript functions are **first-class values**. This means a function can be:

- Stored in a variable: `const fn = n => n * 2;`
- Passed as an argument: `arr.map(fn)`
- Returned from another function: `return n => n * factor;`

A **callback** is a function passed to another function to be invoked at a specific point — on each iteration, when an event fires, or when an operation completes.

### Named vs Inline Callbacks

```javascript
// Named callback — defined separately, reusable
function isPositive(n) {
  return n > 0;
}

const nums = [-3, 0, 5, -1, 8];
const positives = nums.filter(isPositive);   // pass the function, not a call
```

```javascript
// Inline arrow — defined at the call site
const positives2 = nums.filter(n => n > 0);
```

Both are equivalent. Use named callbacks when the logic is complex or shared across multiple calls. Use inline arrows for short, single-use logic.

### Passing Without Calling

A critical distinction: `arr.filter(isPositive)` passes the function. `arr.filter(isPositive())` calls the function immediately and passes its return value — `false` in this case — which is wrong.

### Writing Your Own Higher-Order Function

Any function that accepts a callback is a higher-order function:

```javascript
function applyToAll(arr, transform) {
  const result = [];
  for (const item of arr) {
    result.push(transform(item));
  }
  return result;
}

console.log(applyToAll([1, 2, 3], n => n * 3));   // [3, 6, 9]
console.log(applyToAll([1, 2, 3], n => n ** 2));  // [1, 4, 9]
```

`applyToAll` is a reimplementation of `map`. Understanding this demystifies the built-in array methods.

### Closures and Callbacks

A callback "remembers" variables from its enclosing scope — this is a **closure**:

```javascript
function makeAdder(n) {
  return x => x + n;   // inner function closes over n
}

const add5 = makeAdder(5);
const add10 = makeAdder(10);

console.log(add5(3));    // 8
console.log(add10(3));   // 13
```

`add5` and `add10` are functions that each remember their own `n`. The inner arrow has access to `n` from `makeAdder`'s scope even after `makeAdder` returns. Closures are covered in depth in Module 12.

---

## 2. `forEach`

`forEach` calls a callback once for each element. It is used for **side effects** — it never returns a useful value:

```javascript
const fruits = ['apple', 'banana', 'cherry'];

fruits.forEach((fruit, index) => {
  console.log(`${index}: ${fruit}`);
});
// 0: apple
// 1: banana
// 2: cherry
```

The callback receives `(element, index, array)`:

| Parameter | What it holds |
|---|---|
| `element` | The current array element |
| `index` | The current index (0-based) |
| `array` | The original array |

### `forEach` vs `map`

This distinction is tested on the JSE exam:

| Method | Returns | Modifies original? | Use for |
|---|---|---|---|
| `forEach` | `undefined` | No | Side effects (logging, DOM updates) |
| `map` | New array | No | Transforming each element into a new value |

```javascript
const nums = [1, 2, 3];

const mapped = nums.map(n => n * 2);
console.log(mapped);   // [2, 4, 6]

const forEached = nums.forEach(n => n * 2);
console.log(forEached);   // undefined — forEach always returns undefined
```

Never assign the result of `forEach` to a variable expecting an array.

---

## 3. `every` and `some`

### `every` — Universal Check

`every` returns `true` if the callback returns truthy for **every** element. Returns `false` as soon as any callback returns falsy and stops iterating:

```javascript
const scores = [85, 92, 78, 95, 88];

console.log(scores.every(s => s >= 60));   // true — all pass
console.log(scores.every(s => s >= 90));   // false — stops at 85
```

On an empty array, `every` returns `true` (vacuously — there are no elements that fail).

### `some` — Existence Check

`some` returns `true` if the callback returns truthy for **at least one** element. Returns `true` as soon as any callback returns truthy and stops iterating:

```javascript
console.log(scores.some(s => s >= 90));   // true — stops at 92 (first match)
console.log(scores.some(s => s < 50));    // false — checks all, none qualify
```

On an empty array, `some` returns `false`.

### Short-Circuit Behavior

Both methods stop early to save work:

```javascript
const arr = [1, 2, 3, 4, 5];

// every stops as soon as a false is found
arr.every(n => {
  console.log('every:', n);
  return n < 3;   // false at n=3 — stops before checking 4 and 5
});
// Logs: 1, 2, 3

// some stops as soon as a true is found
arr.some(n => {
  console.log('some:', n);
  return n === 2;   // true at n=2 — stops before checking 3, 4, 5
});
// Logs: 1, 2
```

### `every` vs `some` Summary

| Method | Returns `true` when | Short-circuits on | Empty array |
|---|---|---|---|
| `every` | All elements pass | First falsy callback result | `true` |
| `some` | At least one passes | First truthy callback result | `false` |

---

## 4. `flat` and `flatMap`

### `flat` — Flatten Nested Arrays

`flat(depth)` returns a new array with sub-arrays flattened up to `depth` levels:

```javascript
const nested = [1, [2, 3], [4, [5, 6]]];

console.log(nested.flat());       // [1, 2, 3, 4, [5, 6]] — one level (default)
console.log(nested.flat(2));      // [1, 2, 3, 4, 5, 6] — two levels
console.log(nested.flat(Infinity)); // [1, 2, 3, 4, 5, 6] — all levels
```

`flat` does not modify the original array.

### `flatMap` — Map Then Flatten One Level

`flatMap` applies a callback to each element, then flattens the result one level. It is equivalent to `.map(...).flat(1)` but more efficient:

```javascript
const sentences = ['Hello world', 'foo bar'];
const words = sentences.flatMap(s => s.split(' '));
console.log(words);   // ['Hello', 'world', 'foo', 'bar']
```

Compare with `map`:

```javascript
const wordsNested = sentences.map(s => s.split(' '));
console.log(wordsNested);   // [['Hello', 'world'], ['foo', 'bar']] — nested
```

`flatMap` is useful when each element maps to a variable number of results that should be merged into a single flat output.

---

## 5. The Callback Signature Pattern

All array iteration methods pass the same three arguments to their callbacks: `(element, index, array)`. You only need to declare the parameters you use:

```javascript
const items = ['a', 'b', 'c'];

// Only element
items.forEach(item => console.log(item));

// Element and index
items.forEach((item, i) => console.log(i, item));

// Element, index, and full array (rarely needed)
items.forEach((item, i, arr) => {
  console.log(`${i}/${arr.length}: ${item}`);
});
```

---

## 6. Choosing the Right Iteration Method

| Goal | Method |
|---|---|
| Side effect for each element | `forEach` |
| Transform every element into a new value | `map` |
| Keep elements that pass a test | `filter` |
| Accumulate all elements into one value | `reduce` |
| Check if ALL elements pass | `every` |
| Check if AT LEAST ONE element passes | `some` |
| Find the first matching element | `find` |
| Find the index of the first match | `findIndex` |
| Flatten nested arrays | `flat` |
| Map and flatten in one step | `flatMap` |

---

## 7. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 5: Higher-Order Functions](https://eloquentjavascript.net/05_higher_order.html)**
  The primary OER textbook chapter for this module. Covers abstracting repetition, higher-order functions, `filter`, `map`, `reduce`, and composability. Includes the motivating problem of writing functions that accept other functions as arguments.

- **[MDN Web Docs — Array.prototype.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)**
  Complete reference for `forEach` including callback signature `(element, index, array)`, return value (`undefined`), and behavior with sparse arrays. Includes runnable examples.

- **[MDN Web Docs — Array.prototype.every() and some()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)**
  Full reference for `every` and `some` with examples demonstrating short-circuit behavior, empty-array edge cases, and comparisons with `filter`.

- **[javascript.info — Array methods](https://javascript.info/array-methods)**
  Deep dive covering `forEach`, `filter`, `map`, `reduce`, `find`, `findIndex`, `every`, `some`, `flat`, `flatMap`, and method chaining. Includes interactive exercises for each method and clear tables comparing when to use each.

- **[MDN Web Docs — Callback function](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)**
  Concise MDN glossary entry explaining what a callback is, the distinction between synchronous and asynchronous callbacks, and examples of passing functions as arguments to array methods.

---

## 8. JSE Certification Exam Tips

1. **`forEach` always returns `undefined`** — assigning its result gives `undefined`, not an array. This is a common trap and appears on the exam.

2. **`map` always returns a new array of the same length** — even if the callback returns `undefined` for some elements.

3. **`every` short-circuits on the first false** — it does not run the callback on every element when it encounters a failure.

4. **`some` short-circuits on the first true** — it stops as soon as it finds a match.

5. **`every` on empty array returns `true`; `some` on empty array returns `false`** — this is the mathematically correct vacuous behavior.

6. **`flat()` with no argument flattens one level** — `flat(Infinity)` flattens all levels.

7. **`flatMap` only flattens one level** — it is not the same as `.map(...).flat(Infinity)`.

8. **Named functions passed as callbacks must not include `()`** — `arr.filter(isEven)` passes the function; `arr.filter(isEven())` calls it immediately and passes the return value.

9. **Callback arguments are `(element, index, array)`** — only declare what you need. Missing arguments are simply not bound, not an error.

10. **Closures in callbacks** — a callback that references a variable from an outer scope (e.g., `const threshold = 60; scores.filter(s => s >= threshold)`) forms a closure. The callback "remembers" `threshold` even when called by `filter`.

---

## 9. Study Checklist

- [ ] Watch the Module 09 video lecture by Professor Nash.
- [ ] Read Chapter 5 (Higher-Order Functions) of [Eloquent JavaScript](https://eloquentjavascript.net/05_higher_order.html).
- [ ] Read [MDN — Array.prototype.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach).
- [ ] Read [MDN — Array.prototype.every()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every).
- [ ] Read [MDN — Array.prototype.some()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some).
- [ ] Read [MDN — Array.prototype.flatMap()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap).
- [ ] Open the console and confirm `forEach` returns `undefined` while `map` returns an array.
- [ ] Write a `every` callback with a `console.log` inside — observe when it stops iterating.
- [ ] Write a `flatMap` example and compare it to the equivalent `map` output.
- [ ] Complete the Module 09 Lab.
- [ ] Complete the Module 09 Quiz.
