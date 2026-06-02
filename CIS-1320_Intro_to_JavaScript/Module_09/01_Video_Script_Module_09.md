# Video Script: CIS-1320 — Introduction to JavaScript

## Module 09 — Array Iteration and Callback Functions

**Estimated Duration:** 16–19 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Module 08 introduced `map`, `filter`, and `reduce`. Module 09 deepens the callback concept: what is a callback, how are functions passed as values, and how do `forEach`, `every`, `some`, and `flat`/`flatMap` fit in.
> - The callback concept demo (passing a named function vs inline arrow) is the conceptual core of this module — spend time on it.
> - `every` and `some` short-circuit behavior is tested on the JSE exam — write an example that makes the short-circuit visible (e.g., a callback with a `console.log`).
> - `forEach` vs `map` distinction: `forEach` returns `undefined`, `map` returns a new array. This appears on the exam.
> - Closures are introduced briefly here — just enough to explain why the callback "remembers" variables from its outer scope. Full closure module comes later.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 09 | Array Iteration and Callback Functions | CIS-1320"]**

"Module 09 deepens two ideas introduced in the previous module: callbacks and array iteration. Module 08 showed you `map`, `filter`, and `reduce`. This module explains the underlying mechanism — what a callback function actually is, how functions are passed as values, and how to use that pattern deliberately.

We will also add several array methods that complete the iteration toolkit: `forEach`, `every`, `some`, `flat`, and `flatMap`. By the end of this module, you will understand not just how to use these methods but why the callback pattern exists and what it enables. Let us start with the concept."

---

## [01:00 – 05:00] Part 1 — Callbacks: Functions as Values

**[SHOW SLIDE: "Callback Functions"]**

"A **callback** is a function passed as an argument to another function, to be called later. We touched on this in Module 06, but now we go deeper.

In JavaScript, functions are first-class values — you can store them in variables, pass them to other functions, and return them from functions. When you pass a function to `map` or `filter`, you are passing a callback.

**[DEMO]**

```javascript
// A named function used as a callback
function isEven(n) {
  return n % 2 === 0;
}

const nums = [1, 2, 3, 4, 5, 6];
const evens = nums.filter(isEven);   // passing the function, not calling it
console.log(evens);   // [2, 4, 6]
```

Notice: `isEven` is passed **without parentheses**. `filter(isEven)` passes the function itself. `filter(isEven())` would call it immediately and pass its return value — `false` — which is not what we want.

[PAUSE]

The same result with an inline arrow function:

```javascript
const evens2 = nums.filter(n => n % 2 === 0);
```

Both forms are equivalent. Named functions are better when the callback is complex or reused in multiple places. Arrow functions are better for short, one-use logic.

**[DEMO — writing a function that accepts a callback]**

```javascript
function applyToAll(arr, callback) {
  const result = [];
  for (const item of arr) {
    result.push(callback(item));
  }
  return result;
}

const doubled = applyToAll([1, 2, 3, 4], n => n * 2);
const squared = applyToAll([1, 2, 3, 4], n => n * n);

console.log(doubled);   // [2, 4, 6, 8]
console.log(squared);   // [1, 4, 9, 16]
```

`applyToAll` is a higher-order function — a function that takes another function as a parameter. This is exactly what `map`, `filter`, and `reduce` are. You can write your own.

[PAUSE]

**Callbacks and closures — a brief preview:**

```javascript
function makeMultiplier(factor) {
  return n => n * factor;   // the returned arrow function "closes over" factor
}

const triple = makeMultiplier(3);
const quadruple = makeMultiplier(4);

console.log(triple(5));     // 15 — factor is 3
console.log(quadruple(5));  // 20 — factor is 4
```

`triple` is a function that remembers `factor = 3` even after `makeMultiplier` has returned. The inner arrow function has access to `factor` from its enclosing scope — this is a **closure**. We will cover closures fully in Module 12, but you have been using them every time you pass an arrow function that references an outer variable."

---

## [05:00 – 09:00] Part 2 — `forEach`, `every`, `some`

**[SHOW SLIDE: "forEach, every, some"]**

"**`forEach`** calls a callback once for each element. It does not return a value — it is used purely for side effects:

**[DEMO]**

```javascript
const fruits = ['apple', 'banana', 'cherry'];

fruits.forEach((fruit, index) => {
  console.log(`${index}: ${fruit}`);
});
// 0: apple
// 1: banana
// 2: cherry
```

The callback receives `(element, index, array)` — the same three arguments as `map` and `filter`.

**`forEach` vs `map`** — the key distinction:

```javascript
const nums = [1, 2, 3];

const mapResult = nums.map(n => n * 2);
console.log(mapResult);   // [2, 4, 6] — new array

const forEachResult = nums.forEach(n => n * 2);
console.log(forEachResult);   // undefined — forEach always returns undefined
```

Use `forEach` when you need to perform a side effect for each element — logging, updating the DOM, writing to a variable. Use `map` when you need the transformed results as a new array.

[PAUSE]

**`every`** returns `true` if the callback returns truthy for **every** element. It short-circuits on the first falsy result:

```javascript
const scores = [85, 92, 78, 95, 88];

console.log(scores.every(s => s >= 70));   // true — all pass
console.log(scores.every(s => s >= 90));   // false — stops at 85 (first failure)
```

**`some`** returns `true` if the callback returns truthy for **at least one** element. It short-circuits on the first truthy result:

```javascript
console.log(scores.some(s => s >= 90));   // true — stops at 92 (first match)
console.log(scores.some(s => s < 50));    // false — checks all, none qualify
```

[PAUSE]

**Short-circuit behavior:**

Both `every` and `some` stop iterating as soon as the outcome is determined:

```javascript
const arr = [1, 2, 3, 4, 5];

// every stops at the first false — logs 1, 2, 3 then returns false
arr.every(n => {
  console.log('every checking:', n);
  return n < 3;
});

// some stops at the first true — logs 1 then returns true
arr.some(n => {
  console.log('some checking:', n);
  return n === 1;
});
```

This makes `every` and `some` efficient for existence and validation checks — they do the minimum work needed to answer the question."

---

## [09:00 – 13:00] Part 3 — `flat` and `flatMap`

**[SHOW SLIDE: "flat and flatMap"]**

"**`flat`** flattens nested arrays into a single array. By default it flattens one level deep:

**[DEMO]**

```javascript
const nested = [1, [2, 3], [4, [5, 6]]];

console.log(nested.flat());      // [1, 2, 3, 4, [5, 6]] — one level
console.log(nested.flat(2));     // [1, 2, 3, 4, 5, 6] — two levels
console.log(nested.flat(Infinity)); // [1, 2, 3, 4, 5, 6] — all levels
```

`flat(depth)` accepts a depth argument. `Infinity` flattens all levels regardless of nesting depth.

[PAUSE]

**`flatMap`** is `map` followed by `flat(1)` — it maps each element to an array and then flattens one level:

```javascript
const sentences = ['Hello world', 'foo bar baz'];
const words = sentences.flatMap(s => s.split(' '));
console.log(words);   // ['Hello', 'world', 'foo', 'bar', 'baz']
```

If you had used `map` instead:

```javascript
const wordsNested = sentences.map(s => s.split(' '));
console.log(wordsNested);   // [['Hello', 'world'], ['foo', 'bar', 'baz']]
```

`map` produces an array of arrays. `flatMap` maps and flattens in one step, producing a flat array.

Another example — expanding each product into its individual units:

```javascript
const orders = [
  { product: 'widget', qty: 3 },
  { product: 'gadget', qty: 2 }
];

const units = orders.flatMap(order =>
  Array.from({ length: order.qty }, () => order.product)
);
console.log(units);   // ['widget', 'widget', 'widget', 'gadget', 'gadget']
```"

---

## [13:00 – 16:00] Part 4 — Callback Patterns in Practice

**[SHOW SLIDE: "Callback Patterns"]**

"Let us put everything together with a realistic example. We have an array of students with test scores and we want to perform several operations:

**[DEMO]**

```javascript
const students = [
  { name: 'Alice', scores: [92, 88, 95] },
  { name: 'Bob',   scores: [72, 65, 78] },
  { name: 'Carol', scores: [55, 62, 48] }
];

// Are ALL students passing? (avg >= 60)
const avg = scores => scores.reduce((s, n) => s + n, 0) / scores.length;

const allPassing = students.every(s => avg(s.scores) >= 60);
console.log('All passing:', allPassing);   // false — Carol fails

// Is ANY student at risk? (avg < 70)
const anyAtRisk = students.some(s => avg(s.scores) < 70);
console.log('Any at risk:', anyAtRisk);   // true — Carol and Bob

// Log details for each student
students.forEach(s => {
  const a = avg(s.scores).toFixed(1);
  console.log(`${s.name}: avg ${a}`);
});

// All scores flattened into one array
const allScores = students.flatMap(s => s.scores);
console.log('All scores:', allScores);
console.log('Class max:', Math.max(...allScores));
```

Each method has a clear role: `every` for universal validation, `some` for existence checks, `forEach` for side effects, `flatMap` for flattening nested data. Choosing the right method makes your intent immediately readable — anyone who sees `every` knows you are checking a universal condition."

---

## [16:00 – 17:30] Closing — Lab Preview

**[SHOW SLIDE: "Module 09 Lab Preview"]**

"The Module 09 lab has four parts.

Part 1 works with callbacks as values — you will pass named functions vs inline arrows to the same higher-order function and compare the results.

Part 2 covers `forEach` and its distinction from `map` — you will confirm that `forEach` returns `undefined` and observe when each is appropriate.

Part 3 covers `every` and `some` with visible short-circuit behavior — you will log inside the callback to see exactly when iteration stops.

Part 4 covers `flat` and `flatMap` on nested data, and puts the whole module together in a student analytics exercise.

The quiz focuses on `forEach` vs `map` return values, `every`/`some` short-circuiting, and `flatMap` output. Read the reading guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 09 — Array Iteration and Callback Functions]**

---

## Additional Resources

- [MDN — Array.prototype.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
- [MDN — Array.prototype.every()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
- [MDN — Array.prototype.some()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
- [MDN — Array.prototype.flat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)
- [MDN — Array.prototype.flatMap()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
- [Eloquent JavaScript — Chapter 5: Higher-Order Functions](https://eloquentjavascript.net/05_higher_order.html)
