# Lab Activity: Module 09 — Array Iteration and Callback Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will work with callback functions as first-class values, observe the difference between named and inline callbacks, confirm that `forEach` returns `undefined`, make `every` and `some` short-circuit behavior visible with logging, and use `flat` and `flatMap` on nested data. A final integration exercise combines all methods on a realistic dataset.

By the end of this lab you will have:

- Passed named functions vs inline arrows to the same higher-order function
- Written your own higher-order function that accepts a callback
- Demonstrated that `forEach` returns `undefined` and `map` returns an array
- Made `every` and `some` short-circuit behavior visible with `console.log` inside the callback
- Used `flat` with depth arguments and observed the difference from `flatMap`
- Built a course analytics report using `forEach`, `every`, `some`, and `flatMap`

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 09 reading guide completed

---

## Part 1 — Callbacks as Values

### Step 1.1 — Create the Project

Create folder `module09-lab`. Inside it create `callbacks.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 09 — Callbacks</title>
  <script src="callbacks.js" defer></script>
</head>
<body>
  <h1>Callbacks — check the console</h1>
</body>
</html>
```

Create `callbacks.js`:

```javascript
// Callbacks as Values — Module 09 Lab

// --- SECTION 1: named vs inline callbacks ---
console.log('--- Section 1: named vs inline callbacks ---');

// Named callback function
function isOdd(n) {
  return n % 2 !== 0;
}

function double(n) {
  return n * 2;
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Using named callbacks
const odds = nums.filter(isOdd);
const doubled = nums.map(double);
console.log('odds (named callback):', odds);
console.log('doubled (named callback):', doubled);

// Same results with inline arrows
const odds2 = nums.filter(n => n % 2 !== 0);
const doubled2 = nums.map(n => n * 2);
console.log('odds (inline arrow):', odds2);
console.log('doubled (inline arrow):', doubled2);

// Both produce identical results
console.log('Results identical:', JSON.stringify(odds) === JSON.stringify(odds2));

// --- SECTION 2: passing without calling ---
console.log('\n--- Section 2: passing vs calling ---');

function isEven(n) {
  return n % 2 === 0;
}

// CORRECT — pass the function reference
const evens = nums.filter(isEven);
console.log('filter(isEven) — correct:', evens);

// WRONG — calling isEven() immediately passes its return value (false for no argument)
// isEven() returns false (no argument → NaN % 2 !== 0 → false)
// filter(false) interprets false as a non-function and throws
try {
  const bad = nums.filter(isEven());
  console.log('Should not reach here');
} catch (e) {
  console.error('filter(isEven()) error:', e.message);
}

// --- SECTION 3: writing your own higher-order function ---
console.log('\n--- Section 3: custom higher-order function ---');

function transform(arr, fn) {
  const result = [];
  for (const item of arr) {
    result.push(fn(item));
  }
  return result;
}

function applyIf(arr, predicate, fn) {
  const result = [];
  for (const item of arr) {
    result.push(predicate(item) ? fn(item) : item);
  }
  return result;
}

const values = [1, 2, 3, 4, 5, 6];

console.log('transform double:', transform(values, n => n * 2));
console.log('transform square:', transform(values, n => n ** 2));

// Double only odd numbers, leave evens unchanged
console.log('applyIf double-odds:', applyIf(values, n => n % 2 !== 0, n => n * 2));

// --- SECTION 4: closures in callbacks ---
console.log('\n--- Section 4: closure in callbacks ---');

function makeMultiplier(factor) {
  return n => n * factor;   // closes over factor
}

const triple = makeMultiplier(3);
const quadruple = makeMultiplier(4);

console.log('triple(5):', triple(5));     // 15
console.log('quadruple(5):', quadruple(5)); // 20

// Each function remembers its own factor
console.log('triple(10):', triple(10));   // 30
console.log('quadruple(10):', quadruple(10)); // 40

// Use in array method
const scores = [50, 60, 70, 80, 90];
const scaled = scores.map(makeMultiplier(1.1));
console.log('scores scaled by 1.1:', scaled.map(n => parseFloat(n.toFixed(1))));
```

### Step 1.2 — Open and Verify

Open `callbacks.html` in Live Server. Confirm:

- Section 1: named and inline callbacks produce identical results.
- Section 2: calling `isEven()` with parentheses throws a `TypeError` — the return value `false` is not a function.

### Screenshot 1

Take a screenshot of the full console output from `callbacks.js`. All four sections must be visible. Label this **Lab09-Part1**.

---

## Part 2 — `forEach` vs `map`

### Step 2.1 — Create `foreach_demo.js`

Update your HTML `src` to `foreach_demo.js`:

```javascript
// forEach vs map — Module 09 Lab

// --- SECTION 1: forEach for side effects ---
console.log('--- Section 1: forEach ---');

const products = [
  { name: 'Widget',    price: 12.00 },
  { name: 'Gadget',    price: 45.00 },
  { name: 'Doohickey', price: 8.50  }
];

// forEach — side effect only (logging)
products.forEach((product, index) => {
  console.log(`${index + 1}. ${product.name}: $${product.price}`);
});

// forEach with external accumulation (side effect = updating outer variable)
let total = 0;
products.forEach(p => {
  total += p.price;
});
console.log('Total via forEach:', total.toFixed(2));

// --- SECTION 2: forEach always returns undefined ---
console.log('\n--- Section 2: forEach return value ---');

const nums = [1, 2, 3, 4, 5];

const forEachResult = nums.forEach(n => n * 2);
console.log('forEach result:', forEachResult);   // undefined

const mapResult = nums.map(n => n * 2);
console.log('map result:', mapResult);   // [2, 4, 6, 8, 10]

// Common mistake: using forEach when map is needed
const badDoubles = [];
nums.forEach(n => badDoubles.push(n * 2));   // works but verbose
console.log('badDoubles (forEach + push):', badDoubles);

const goodDoubles = nums.map(n => n * 2);   // cleaner
console.log('goodDoubles (map):', goodDoubles);

// --- SECTION 3: using the index parameter ---
console.log('\n--- Section 3: index in forEach ---');

const cities = ['Dallas', 'Austin', 'Houston', 'San Antonio'];

cities.forEach((city, index) => {
  const label = index === 0 ? ' (first)' : index === cities.length - 1 ? ' (last)' : '';
  console.log(`${index}: ${city}${label}`);
});

// --- SECTION 4: choosing forEach vs map ---
console.log('\n--- Section 4: when to use which ---');

const temperatures = [98.6, 101.2, 99.8, 102.4, 97.5];
const threshold = 100.4;

// forEach — just log which readings are high (side effect, no new array)
console.log('High readings:');
temperatures.forEach((temp, i) => {
  if (temp > threshold) {
    console.log(`  Reading ${i + 1}: ${temp}°F — FEVER`);
  }
});

// map — transform all readings to Celsius (need new array)
const celsius = temperatures.map(f => parseFloat(((f - 32) * 5 / 9).toFixed(1)));
console.log('Temperatures in Celsius:', celsius);
```

### Step 2.2 — Confirm the Key Behavior

Confirm that Section 2 clearly shows `forEachResult` is `undefined` while `mapResult` is an array.

### Screenshot 2

Take a screenshot of the full console output from `foreach_demo.js`. All four sections must be visible. Label this **Lab09-Part2**.

---

## Part 3 — `every`, `some`, and Short-Circuiting

### Step 3.1 — Create `every_some.js`

Update your HTML `src` to `every_some.js`:

```javascript
// every and some — Module 09 Lab

// --- SECTION 1: basic every and some ---
console.log('--- Section 1: every and some ---');

const scores = [85, 92, 78, 95, 88, 71];

console.log('All >= 70:', scores.every(s => s >= 70));   // true
console.log('All >= 90:', scores.every(s => s >= 90));   // false
console.log('Some >= 90:', scores.some(s => s >= 90));   // true
console.log('Some < 60:', scores.some(s => s < 60));     // false

// --- SECTION 2: short-circuit with visible logging ---
console.log('\n--- Section 2: short-circuit behavior ---');

const arr = [2, 4, 6, 7, 8, 10];

console.log('every: checking if all are even...');
const allEven = arr.every(n => {
  console.log('  every checking:', n);
  return n % 2 === 0;
});
console.log('every result:', allEven);
// Should stop at 7 — the first odd number

console.log('\nsome: checking if any are odd...');
const anyOdd = arr.some(n => {
  console.log('  some checking:', n);
  return n % 2 !== 0;
});
console.log('some result:', anyOdd);
// Should stop at 7 — the first odd number

// --- SECTION 3: every and some on empty arrays ---
console.log('\n--- Section 3: empty array behavior ---');

const empty = [];
console.log('every on empty:', empty.every(n => n > 0));   // true (vacuous)
console.log('some on empty:', empty.some(n => n > 0));     // false

// --- SECTION 4: practical every / some ---
console.log('\n--- Section 4: practical uses ---');

const users = [
  { name: 'Alice', verified: true,  age: 28 },
  { name: 'Bob',   verified: true,  age: 17 },
  { name: 'Carol', verified: false, age: 32 },
  { name: 'Dave',  verified: true,  age: 22 }
];

// Is every user verified?
const allVerified = users.every(u => u.verified);
console.log('All verified:', allVerified);   // false — Carol is not

// Is any user under 18?
const hasMinor = users.some(u => u.age < 18);
console.log('Has minor:', hasMinor);   // true — Bob is 17

// Can we show adult content? (every user must be >= 18 AND verified)
const canShowAdult = users.every(u => u.age >= 18 && u.verified);
console.log('Can show adult content:', canShowAdult);   // false

// Is there at least one admin? (none have admin role here)
const hasAdmin = users.some(u => u.role === 'admin');
console.log('Has admin:', hasAdmin);   // false — role property is undefined

// --- SECTION 5: combining every, some, filter ---
console.log('\n--- Section 5: combining methods ---');

const inventory = [
  { item: 'Widget',    qty: 50, price: 12 },
  { item: 'Gadget',    qty: 0,  price: 45 },
  { item: 'Doohickey', qty: 3,  price: 8  },
  { item: 'Gizmo',     qty: 25, price: 30 }
];

const anyOutOfStock = inventory.some(i => i.qty === 0);
const allAffordable = inventory.every(i => i.price < 50);
const lowStock = inventory.filter(i => i.qty > 0 && i.qty < 10);

console.log('Any out of stock:', anyOutOfStock);
console.log('All under $50:', allAffordable);
console.log('Low stock items:', lowStock.map(i => `${i.item} (${i.qty})`));
```

### Step 3.2 — Observe the Short-Circuit

In Section 2, count the `every checking` lines. They should stop at `7` (four lines: 2, 4, 6, 7). Same for `some checking` — it should stop at `7`. This proves neither method continues after the outcome is determined.

### Screenshot 3

Take a screenshot of the full console output from `every_some.js`. All five sections must be visible. Label this **Lab09-Part3**.

---

## Part 4 — `flat`, `flatMap`, and Integration

### Step 4.1 — Create `flat_demo.js`

Update your HTML `src` to `flat_demo.js`:

```javascript
// flat, flatMap, and Integration — Module 09 Lab

// --- SECTION 1: flat with depth ---
console.log('--- Section 1: flat ---');

const level1 = [1, [2, 3], [4, 5]];
const level2 = [1, [2, [3, 4]], [5, [6, 7]]];
const level3 = [1, [2, [3, [4, [5]]]]];

console.log('level1.flat():', level1.flat());     // [1,2,3,4,5] — one level, complete
console.log('level2.flat():', level2.flat());     // [1,2,[3,4],5,[6,7]] — one level
console.log('level2.flat(2):', level2.flat(2));   // [1,2,3,4,5,6,7] — two levels
console.log('level3.flat(Infinity):', level3.flat(Infinity));  // fully flat

// flat does not modify original
const original = [1, [2, 3]];
const flattened = original.flat();
console.log('original unchanged:', original);

// --- SECTION 2: flatMap ---
console.log('\n--- Section 2: flatMap ---');

const sentences = [
  'The quick brown fox',
  'jumps over the lazy dog',
  'JavaScript is fun'
];

// map produces nested arrays
const mapResult = sentences.map(s => s.split(' '));
console.log('map result:', mapResult);   // [['The','quick',...], ...]

// flatMap produces a flat array
const words = sentences.flatMap(s => s.split(' '));
console.log('flatMap result:', words);

// flatMap — expand each order into individual items
const orders = [
  { product: 'A', qty: 3 },
  { product: 'B', qty: 1 },
  { product: 'C', qty: 2 }
];

const lineItems = orders.flatMap(o =>
  Array.from({ length: o.qty }, () => o.product)
);
console.log('line items:', lineItems);   // ['A','A','A','B','C','C']

// --- SECTION 3: flatMap only flattens one level ---
console.log('\n--- Section 3: flatMap depth ---');

const data = [[1, 2], [3, [4, 5]]];
console.log('flatMap result:', data.flatMap(x => x));   // [1, 2, 3, [4, 5]]
// The [4,5] nested inside [3,[4,5]] is NOT flattened further
// Use .flat(2) or .flat(Infinity) for deeper flattening

// --- SECTION 4: integration — course analytics ---
console.log('\n--- Section 4: integration ---');

const courses = [
  {
    name: 'CIS-1310 Python',
    students: [
      { name: 'Alice', scores: [92, 88, 95, 91] },
      { name: 'Bob',   scores: [72, 65, 78, 70] },
      { name: 'Carol', scores: [85, 91, 89, 94] }
    ]
  },
  {
    name: 'CIS-1320 JavaScript',
    students: [
      { name: 'Dave',  scores: [88, 91, 85, 93] },
      { name: 'Eve',   scores: [55, 62, 48, 60] },
      { name: 'Frank', scores: [78, 82, 74, 80] }
    ]
  }
];

const avg = arr => arr.reduce((s, n) => s + n, 0) / arr.length;

// All scores across all courses (flatMap × 2)
const allScores = courses.flatMap(c => c.students.flatMap(s => s.scores));
console.log('Total scores collected:', allScores.length);
console.log('Overall average:', avg(allScores).toFixed(1));
console.log('Overall max:', Math.max(...allScores));
console.log('Overall min:', Math.min(...allScores));

// Per-course summary using forEach
courses.forEach(course => {
  const courseScores = course.students.flatMap(s => s.scores);
  const passing = course.students.filter(s => avg(s.scores) >= 60);
  const allPass = course.students.every(s => avg(s.scores) >= 60);
  const anyStruggling = course.students.some(s => avg(s.scores) < 70);

  console.log(`\n${course.name}:`);
  console.log(`  Course avg: ${avg(courseScores).toFixed(1)}`);
  console.log(`  Passing: ${passing.length}/${course.students.length}`);
  console.log(`  All passing: ${allPass}`);
  console.log(`  Any struggling (<70): ${anyStruggling}`);
});
```

### Step 4.2 — Verify Key Outputs

Confirm:

- Section 2: `map` produces an array of arrays; `flatMap` produces a flat array from the same input.
- Section 4: `allScores.length` equals the total number of individual score entries across all students in both courses.

### Screenshot 4

Take a screenshot of the full console output from `flat_demo.js`. All four sections must be visible. Label this **Lab09-Part4**.

---

## Deliverables

Submit the following to the Module 09 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `callbacks.js` | Named vs inline callbacks, passing vs calling, custom higher-order function, closures |
| `foreach_demo.js` | `forEach` for side effects, `undefined` return demo, `forEach` vs `map` comparison |
| `every_some.js` | Basic `every`/`some`, visible short-circuit with logging, empty array behavior, practical uses |
| `flat_demo.js` | `flat` with depth args, `flatMap` vs `map`, integration with course analytics |
| Lab09-Part1.png | Console — callbacks including `TypeError` from calling with `()` |
| Lab09-Part2.png | Console — `forEach` returning `undefined` clearly visible |
| Lab09-Part3.png | Console — `every`/`some` short-circuit logs stopping early |
| Lab09-Part4.png | Console — `flat`/`flatMap` and course analytics integration |

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In Part 1 Section 2, `nums.filter(isEven())` threw a `TypeError`. Explain exactly what happened: what did `isEven()` evaluate to, what was passed to `filter`, and why did that cause an error? What is the correct syntax?

2. In Part 2, `forEach` returned `undefined` while `map` returned an array. Based on what you observed, describe in one sentence each the rule for when to use `forEach` and when to use `map`. What property of the task determines which is correct?

3. In Part 3 Section 2, the `every` callback stopped logging at `7`. Explain the short-circuit rule: what does `every` do as soon as one callback returns falsy? How is `some`'s short-circuit rule the mirror image of this?

4. In Part 4 Section 2, using `map` on the `sentences` array produced nested arrays, but `flatMap` produced a flat array. Describe in your own words what `flatMap` does that `map` alone does not. Give one scenario — from the lab or from your own imagination — where `flatMap` makes code significantly cleaner than the alternative.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `filter(isEven())` does not throw — just returns empty array | `isEven` takes a number argument; called with no argument returns `false`, and `filter(false)` in some browsers silently returns `[]` | Check your browser version; the behavior is technically a `TypeError` per spec |
| `every` does not stop early | Callback always returns a truthy value | Check the condition — if all elements pass the test, `every` does check all of them |
| `flatMap` still produces nested arrays | Nesting is more than one level deep | `flatMap` only flattens one level; use `.map(...).flat(2)` for deeper nesting |
| `forEach` accumulator gives wrong total | Arrow function body uses `{}` but `total` is declared outside | Ensure `total` is declared in the outer scope and mutated inside `forEach` |
| Course analytics `allScores.length` is wrong | One `flatMap` instead of two nested | Scores are inside `students` inside `courses` — need `flatMap` on both levels |
