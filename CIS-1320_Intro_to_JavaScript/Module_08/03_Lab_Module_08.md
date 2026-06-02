# Lab Activity: Module 08 — Arrays and Array Methods

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will build scripts that use every array method covered in Module 08. You will verify first-hand which methods mutate the original array and which do not, trace through a `reduce` accumulator manually before running the code, and chain `map` and `filter` on a realistic dataset. You will also use the spread operator for array copies and merges, and apply array destructuring including the variable-swap pattern.

By the end of this lab you will have:

- Used `push`, `pop`, `shift`, `unshift`, and `splice` on live arrays
- Compared `splice` vs `slice` and confirmed mutation behavior
- Used `indexOf`, `includes`, `find`, `findIndex`, `join`, and `sort`
- Transformed data with `map`, filtered data with `filter`, and accumulated with `reduce`
- Chained `filter` and `map` on an array of objects
- Copied and merged arrays with the spread operator
- Applied array destructuring with skipping, defaults, and the swap pattern

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 08 reading guide completed

---

## Part 1 — Mutating and Non-Mutating Methods

### Step 1.1 — Create the Project

Create folder `module08-lab`. Inside it create `arrays.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 08 — Arrays</title>
  <script src="arrays.js" defer></script>
</head>
<body>
  <h1>Arrays — check the console</h1>
</body>
</html>
```

Create `arrays.js`:

```javascript
// Array Basics and Mutation — Module 08 Lab

// --- SECTION 1: array creation and access ---
console.log('--- Section 1: array basics ---');

const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'];

console.log('Length:', planets.length);
console.log('First:', planets[0]);
console.log('Last:', planets[planets.length - 1]);
console.log('Out of bounds:', planets[100]);   // undefined — no error

// --- SECTION 2: push, pop, unshift, shift ---
console.log('\n--- Section 2: push/pop/unshift/shift ---');

const tasks = ['Write tests', 'Review PR'];
console.log('Initial:', [...tasks]);

tasks.push('Deploy');
console.log('After push:', [...tasks]);

const done = tasks.pop();
console.log('Popped:', done);
console.log('After pop:', [...tasks]);

tasks.unshift('Plan sprint');
console.log('After unshift:', [...tasks]);

const first = tasks.shift();
console.log('Shifted:', first);
console.log('After shift:', [...tasks]);

// --- SECTION 3: splice vs slice ---
console.log('\n--- Section 3: splice vs slice ---');

const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
console.log('Original:', [...colors]);

// slice — does NOT modify original
const warm = colors.slice(0, 3);
console.log('slice(0, 3):', warm);
console.log('Original after slice:', [...colors]);   // unchanged

// splice — DOES modify original
const removed = colors.splice(2, 2);   // remove 2 elements starting at index 2
console.log('splice removed:', removed);
console.log('Original after splice:', [...colors]);   // changed!

// splice to insert
colors.splice(2, 0, 'INSERTED_1', 'INSERTED_2');
console.log('After splice insert:', [...colors]);

// --- SECTION 4: indexOf, includes ---
console.log('\n--- Section 4: indexOf and includes ---');

const nums = [5, 10, 15, 20, 15, 25];

console.log('indexOf(15):', nums.indexOf(15));     // 2 — first occurrence
console.log('indexOf(99):', nums.indexOf(99));     // -1 — not found
console.log('includes(20):', nums.includes(20));   // true
console.log('includes(99):', nums.includes(99));   // false

// indexOf uses strict equality
const mixed = [1, '1', true, null];
console.log('indexOf("1"):', mixed.indexOf('1'));   // 1 — string '1'
console.log('indexOf(1):', mixed.indexOf(1));       // 0 — number 1

// --- SECTION 5: sort and join ---
console.log('\n--- Section 5: sort and join ---');

const scores = [45, 90, 12, 78, 34, 56];

// WRONG — sort without comparator converts to strings
const wrongSort = [...scores].sort();
console.log('String sort (wrong):', wrongSort);

// CORRECT — numeric comparator
const ascending = [...scores].sort((a, b) => a - b);
const descending = [...scores].sort((a, b) => b - a);
console.log('Ascending:', ascending);
console.log('Descending:', descending);

const fruits = ['banana', 'apple', 'cherry', 'date'];
console.log('Alphabetical:', [...fruits].sort());

const csv = ascending.join(', ');
console.log('join result:', csv);
```

### Step 1.2 — Open and Verify

Open `arrays.html` in Live Server. Confirm:

- Section 3: the original `colors` array changes after `splice` but not after `slice`.
- Section 5: the wrong sort (`[45, 90, 12, 78, 34, 56].sort()`) does NOT produce a numerically sorted result — it sorts lexicographically.

### Screenshot 1

Take a screenshot of the full console output from `arrays.js`. All five sections must be visible. Label this **Lab08-Part1**.

---

## Part 2 — `map`, `filter`, and `reduce`

### Step 2.1 — Create `higher_order.js`

Update your HTML `src` to `higher_order.js`:

```javascript
// map, filter, reduce — Module 08 Lab

const products = [
  { name: 'Widget',    price: 12.00, category: 'tools',      inStock: true  },
  { name: 'Gadget',    price: 45.00, category: 'electronics', inStock: false },
  { name: 'Doohickey', price: 8.50,  category: 'tools',      inStock: true  },
  { name: 'Thingamajig', price: 99.99, category: 'electronics', inStock: true },
  { name: 'Whatsit',   price: 5.00,  category: 'tools',      inStock: false },
  { name: 'Gizmo',     price: 30.00, category: 'electronics', inStock: true  }
];

// --- SECTION 1: map ---
console.log('--- Section 1: map ---');

// Extract all names
const names = products.map(p => p.name);
console.log('All names:', names);

// Apply 10% discount to all prices
const discounted = products.map(p => ({
  ...p,
  price: parseFloat((p.price * 0.9).toFixed(2))
}));
console.log('Discounted prices:', discounted.map(p => `${p.name}: $${p.price}`));

// Original unchanged
console.log('Original prices unchanged:', products.map(p => `${p.name}: $${p.price}`));

// --- SECTION 2: filter ---
console.log('\n--- Section 2: filter ---');

// Only in-stock products
const available = products.filter(p => p.inStock);
console.log('In stock:', available.map(p => p.name));

// Only tools
const tools = products.filter(p => p.category === 'tools');
console.log('Tools:', tools.map(p => p.name));

// Affordable in-stock items (price <= 20)
const affordable = products.filter(p => p.inStock && p.price <= 20);
console.log('Affordable and in stock:', affordable.map(p => `${p.name} $${p.price}`));

// --- SECTION 3: reduce ---
console.log('\n--- Section 3: reduce ---');

// Sum all prices
const totalValue = products.reduce((acc, p) => acc + p.price, 0);
console.log('Total inventory value: $' + totalValue.toFixed(2));

// Count by category
const byCategory = products.reduce((acc, p) => {
  acc[p.category] = (acc[p.category] ?? 0) + 1;
  return acc;
}, {});
console.log('Count by category:', byCategory);

// Most expensive product
const mostExpensive = products.reduce((acc, p) => p.price > acc.price ? p : acc);
console.log('Most expensive:', mostExpensive.name, '$' + mostExpensive.price);

// In-stock total value
const inStockValue = products
  .filter(p => p.inStock)
  .reduce((acc, p) => acc + p.price, 0);
console.log('In-stock inventory value: $' + inStockValue.toFixed(2));

// --- SECTION 4: chaining map and filter ---
console.log('\n--- Section 4: chaining ---');

// Names of in-stock electronics, uppercased
const result = products
  .filter(p => p.inStock && p.category === 'electronics')
  .map(p => p.name.toUpperCase());
console.log('In-stock electronics (uppercase):', result);

// Price list for available tools, sorted ascending
const toolPrices = products
  .filter(p => p.inStock && p.category === 'tools')
  .map(p => p.price)
  .sort((a, b) => a - b);
console.log('Available tool prices (asc):', toolPrices);

// --- SECTION 5: find and findIndex ---
console.log('\n--- Section 5: find and findIndex ---');

const gadget = products.find(p => p.name === 'Gadget');
console.log('Found:', gadget);

const firstAffordable = products.find(p => p.price < 10);
console.log('First under $10:', firstAffordable?.name);

const expensiveIdx = products.findIndex(p => p.price > 50);
console.log('First index where price > 50:', expensiveIdx);

const notFound = products.find(p => p.price > 1000);
console.log('Find with no match:', notFound);   // undefined
```

### Step 2.2 — Manually Trace the `reduce` in Section 3

Before running the code, work out the `totalValue` reduce manually on paper:

- Initial accumulator: `0`
- Step 1: `0 + 12.00 = 12.00`
- Step 2: `12.00 + 45.00 = 57.00`
- Continue through all six products

Compare your manual total to the console output. They should match.

### Screenshot 2

Take a screenshot of the full console output from `higher_order.js`. All five sections must be visible. Label this **Lab08-Part2**.

---

## Part 3 — Spread Operator and Destructuring

### Step 3.1 — Create `spread_destruct.js`

Update your HTML `src` to `spread_destruct.js`:

```javascript
// Spread and Array Destructuring — Module 08 Lab

// --- SECTION 1: copying arrays with spread ---
console.log('--- Section 1: spread copy ---');

const original = [1, 2, 3, 4, 5];

// Assignment — NOT a copy (same reference)
const sameRef = original;
sameRef.push(99);
console.log('original after sameRef.push:', original);   // [1,2,3,4,5,99] — mutated!

// Spread — creates a new array
const spreadCopy = [...original];
spreadCopy.push(100);
console.log('original after spreadCopy.push:', original);   // unchanged
console.log('spreadCopy:', spreadCopy);

// --- SECTION 2: merging arrays with spread ---
console.log('\n--- Section 2: spread merge ---');

const evens = [2, 4, 6];
const odds = [1, 3, 5];

const combined = [...odds, ...evens];
const withExtra = [0, ...odds, ...evens, 7, 8, 9];

console.log('combined:', combined);
console.log('withExtra:', withExtra);

// Spread into Math functions
const values = [34, 12, 78, 56, 90, 23];
console.log('max:', Math.max(...values));
console.log('min:', Math.min(...values));

// --- SECTION 3: basic array destructuring ---
console.log('\n--- Section 3: array destructuring ---');

const rgb = [255, 128, 0];
const [red, green, blue] = rgb;
console.log(`R: ${red}, G: ${green}, B: ${blue}`);

// Partial destructuring
const [first, second] = [10, 20, 30, 40];
console.log('first:', first, 'second:', second);   // remaining elements ignored

// --- SECTION 4: skip, defaults, rest in destructuring ---
console.log('\n--- Section 4: skip, defaults, rest ---');

// Skipping elements
const [a, , c, , e] = [1, 2, 3, 4, 5];
console.log('a:', a, 'c:', c, 'e:', e);   // 1, 3, 5

// Default values
const [x = 10, y = 20, z = 30] = [100, 200];
console.log('x:', x, 'y:', y, 'z:', z);   // 100, 200, 30

// Rest in destructuring
const [head, ...tail] = [1, 2, 3, 4, 5];
console.log('head:', head);   // 1
console.log('tail:', tail);   // [2, 3, 4, 5]

// --- SECTION 5: the variable swap ---
console.log('\n--- Section 5: variable swap ---');

let playerA = 'Alice';
let playerB = 'Bob';
console.log('Before swap:', playerA, playerB);

[playerA, playerB] = [playerB, playerA];
console.log('After swap:', playerA, playerB);   // Bob Alice

// Practical swap — exchange two array values
const seats = ['Charlie', 'Diana', 'Eve', 'Frank'];
console.log('Before:', [...seats]);
[seats[0], seats[3]] = [seats[3], seats[0]];
console.log('After swap seats[0] and seats[3]:', seats);

// --- SECTION 6: destructuring function return values ---
console.log('\n--- Section 6: destructuring return values ---');

function minMax(arr) {
  const sorted = [...arr].sort((a, b) => a - b);
  return [sorted[0], sorted[sorted.length - 1]];
}

const [minimum, maximum] = minMax([34, 78, 12, 90, 56]);
console.log('min:', minimum, 'max:', maximum);

// Ignore the max
const [minOnly] = minMax([5, 8, 3, 11, 2]);
console.log('min only:', minOnly);
```

### Step 3.2 — Observe the Reference Trap

In Section 1, confirm that mutating `sameRef` also mutates `original` — because they are the same array. The spread copy in the second half does not have this problem.

### Screenshot 3

Take a screenshot of the full console output from `spread_destruct.js`. All six sections must be visible. Label this **Lab08-Part3**.

---

## Part 4 — Integration: Student Grade Analyzer

### Step 4.1 — Create `grade_analyzer.js`

Update your HTML `src` to `grade_analyzer.js`. This exercise uses all array methods together:

```javascript
// Student Grade Analyzer — Module 08 Lab Integration

const students = [
  { name: 'Alice',   scores: [92, 88, 95, 91, 87] },
  { name: 'Bob',     scores: [72, 65, 78, 70, 68] },
  { name: 'Carol',   scores: [55, 62, 48, 70, 59] },
  { name: 'Dave',    scores: [88, 91, 85, 93, 90] },
  { name: 'Eve',     scores: [60, 75, 80, 72, 68] },
  { name: 'Frank',   scores: [45, 52, 38, 60, 55] }
];

// Helper: compute average of an array of numbers
const average = nums => nums.reduce((sum, n) => sum + n, 0) / nums.length;

// Helper: letter grade from average
const letterGrade = avg => {
  if (avg >= 90) return 'A';
  if (avg >= 80) return 'B';
  if (avg >= 70) return 'C';
  if (avg >= 60) return 'D';
  return 'F';
};

// --- STEP 1: enrich each student with computed fields ---
const enriched = students.map(s => ({
  ...s,
  avg: parseFloat(average(s.scores).toFixed(1)),
  grade: letterGrade(average(s.scores)),
  highest: Math.max(...s.scores),
  lowest: Math.min(...s.scores)
}));

console.log('--- Enriched student records ---');
enriched.forEach(s => {
  console.log(`${s.name}: avg=${s.avg} (${s.grade}) | high=${s.highest} low=${s.lowest}`);
});

// --- STEP 2: filter passing students (avg >= 60) ---
const passing = enriched.filter(s => s.avg >= 60);
const failing = enriched.filter(s => s.avg < 60);

console.log('\n--- Passing students ---');
passing.forEach(s => console.log(`  ${s.name} (${s.avg})`));

console.log('\n--- Failing students ---');
failing.forEach(s => console.log(`  ${s.name} (${s.avg})`));

// --- STEP 3: class statistics with reduce ---
const allAverages = enriched.map(s => s.avg);
const classAvg = parseFloat(average(allAverages).toFixed(1));

const [classLow, classHigh] = [
  Math.min(...allAverages),
  Math.max(...allAverages)
];

const gradeDist = enriched.reduce((acc, s) => {
  acc[s.grade] = (acc[s.grade] ?? 0) + 1;
  return acc;
}, {});

console.log('\n--- Class Statistics ---');
console.log('Class average:', classAvg);
console.log('Highest average:', classHigh);
console.log('Lowest average:', classLow);
console.log('Grade distribution:', gradeDist);

// --- STEP 4: rank students by average (non-mutating sort) ---
const ranked = [...enriched].sort((a, b) => b.avg - a.avg);

console.log('\n--- Class Ranking ---');
ranked.forEach((s, i) => {
  console.log(`  ${i + 1}. ${s.name} — ${s.avg} (${s.grade})`);
});

// --- STEP 5: top scorer using find ---
const topStudent = ranked[0];
const bottomStudent = ranked[ranked.length - 1];

console.log('\n--- Awards ---');
console.log('Top student:', topStudent.name, topStudent.avg);
console.log('Most room to improve:', bottomStudent.name, bottomStudent.avg);
```

### Step 4.2 — Verify Key Behaviors

Confirm:

- The `ranked` sort does not change `enriched` — use `[...enriched]` to verify the original order is preserved.
- `gradeDist` correctly counts each letter grade.
- `passing` and `failing` together have the same total count as `students`.

### Screenshot 4

Take a screenshot of the full console output from `grade_analyzer.js`. All five sections must be visible. Label this **Lab08-Part4**.

---

## Deliverables

Submit the following to the Module 08 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `arrays.js` | Basics, push/pop/unshift/shift, splice vs slice, indexOf/includes, sort comparison |
| `higher_order.js` | map/filter/reduce on product dataset, chaining, find/findIndex |
| `spread_destruct.js` | Reference trap, spread copy/merge, destructuring with skip/defaults/rest, swap |
| `grade_analyzer.js` | Integration using all array methods on student dataset |
| Lab08-Part1.png | Console — array basics including wrong sort demo |
| Lab08-Part2.png | Console — map/filter/reduce all five sections |
| Lab08-Part3.png | Console — spread and destructuring including reference trap |
| Lab08-Part4.png | Console — grade analyzer complete output |

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In Part 1 Section 3, `splice` modified the original array but `slice` did not. Explain precisely what each method does and what it returns. Why does this distinction matter when you need to work with a copy of array data?

2. In Part 2 Section 3, you used `reduce` to count products by category. Trace through the first three iterations manually: what is `acc` before each call, what does the callback do, and what does it return? Write out the three rows of the accumulator table.

3. In Part 3 Section 1, mutating `sameRef` also mutated `original`. Explain why. What is the difference between assigning `const copy = original` and `const copy = [...original]` at the memory level?

4. The reading guide says that chaining `map` and `filter` is common but `reduce` is typically last in a chain. Looking at your code in Part 2 Section 3 (the in-stock total value), explain why `reduce` must come after `filter` and not before it in that particular chain.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `sort` without comparator gives wrong numeric order | Default sort converts to strings | Always use `(a, b) => a - b` for numbers |
| Original array mutated after `slice` | `splice` used instead of `slice` | Check method name — `slice` never mutates |
| `reduce` accumulator becomes `undefined` on iteration 2 | Multi-line callback missing `return acc` | Add `return acc` at end of callback |
| `map` returns `[undefined, undefined, ...]` | Callback missing return or using `{}` without `return` | Check implicit return rule — add braces + explicit `return` |
| Spread copy still shares nested objects | Shallow copy — nested objects are references | For nested objects use `JSON.parse(JSON.stringify(arr))` or structured clone |
| `find` returns `undefined` unexpectedly | Condition never true, or wrong property name | Log the element inside the callback to debug |
