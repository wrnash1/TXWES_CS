# Lab Activity: Module 05 — Loops and Iteration

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will build scripts that use every loop construct covered in Module 05: `for`, `while`, `do-while`, `break`, `continue`, `for...of`, and `for...in`. You will deliberately trigger an infinite loop, observe it freeze the browser tab, then correct it. You will also demonstrate the `for...in` array trap so you can see first-hand why it produces string keys instead of values.

By the end of this lab you will have:

- Used a `for` loop to count up, count down, and iterate arrays by index
- Demonstrated the `<` vs `<=` off-by-one difference with a side-by-side table
- Used `while` and `do-while` including an intentional infinite loop you interrupt
- Applied `break` to implement a search and `continue` to implement a filter
- Demonstrated nested `break` behavior
- Used `for...of` to iterate array values and string characters
- Used `for...in` on an object and observed the trap when applied to an array

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 05 reading guide completed

---

## Part 1 — `for` Loop

### Step 1.1 — Create the Project

Create folder `module05-lab`. Inside it create `for_loop.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 05 — for Loop</title>
  <script src="for_loop.js" defer></script>
</head>
<body>
  <h1>for Loop — check the console</h1>
</body>
</html>
```

Create `for_loop.js`:

```javascript
// for Loop Demo — Module 05 Lab

// --- SECTION 1: basic counting ---
console.log('--- Section 1: counting up ---');

for (let i = 0; i < 5; i++) {
  console.log('i =', i);
}
// Expected: 0, 1, 2, 3, 4

// --- SECTION 2: < vs <= off-by-one comparison ---
console.log('\n--- Section 2: < vs <= ---');

console.log('i < 5 (starts at 0):');
for (let i = 0; i < 5; i++) {
  process.stdout ? process.stdout.write(i + ' ') : null;
  console.log('  i < 5 iteration:', i);
}

console.log('i <= 5 (starts at 0):');
for (let i = 0; i <= 5; i++) {
  console.log('  i <= 5 iteration:', i);
}

console.log('i <= 5 (starts at 1):');
for (let i = 1; i <= 5; i++) {
  console.log('  i<=5 from 1 iteration:', i);
}

console.log('i < 5 (starts at 1):');
for (let i = 1; i < 5; i++) {
  console.log('  i<5 from 1 iteration:', i);
}

// Summary table — count the lines in each group above and record them
console.log('\nSummary:');
console.log('i=0, i<5  → runs 5 times (values 0-4)');
console.log('i=0, i<=5 → runs 6 times (values 0-5)');
console.log('i=1, i<=5 → runs 5 times (values 1-5)');
console.log('i=1, i<5  → runs 4 times (values 1-4)');

// --- SECTION 3: counting down ---
console.log('\n--- Section 3: countdown ---');

for (let i = 10; i >= 1; i--) {
  console.log(i);
}
console.log('Liftoff!');

// --- SECTION 4: iterating an array by index ---
console.log('\n--- Section 4: array iteration by index ---');

const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter'];

for (let i = 0; i < planets.length; i++) {
  console.log(`Planet ${i + 1}: ${planets[i]}`);
}

// Demonstrate the off-by-one bug: i <= planets.length
console.log('\n--- Off-by-one bug: i <= planets.length ---');
for (let i = 0; i <= planets.length; i++) {
  console.log(`Index ${i}:`, planets[i]);   // last value will be undefined
}
// The last line prints: Index 5: undefined — accessing beyond the array
```

### Step 1.2 — Open and Verify

Open `for_loop.html` in Live Server. Confirm in the console:

- Section 1 prints `0` through `4` — five values.
- Section 2: `i < 5` from 0 runs 5 times; `i <= 5` from 0 runs 6 times.
- Section 3 counts from `10` down to `1`, then `Liftoff!`.
- Section 4: the last iteration of the off-by-one loop prints `undefined`.

### Screenshot 1

Take a screenshot showing the full console output from `for_loop.js`. All four sections must be visible. Label this **Lab05-Part1**.

---

## Part 2 — `while` and `do-while`

### Step 2.1 — Create `while_demo.js`

Update your HTML `src` to `while_demo.js`:

```javascript
// while and do-while Demo — Module 05 Lab

// --- SECTION 1: basic while loop ---
console.log('--- Section 1: while loop ---');

let attempts = 0;
const MAX_ATTEMPTS = 3;

while (attempts < MAX_ATTEMPTS) {
  console.log('Attempt', attempts + 1, 'of', MAX_ATTEMPTS);
  attempts++;
}
console.log('Finished. Total attempts:', attempts);

// --- SECTION 2: while with a false initial condition ---
console.log('\n--- Section 2: while with false initial condition ---');

let n = 100;
while (n < 5) {
  console.log('This should never print');
}
console.log('n is', n, '— while loop body never ran');

// --- SECTION 3: do-while — runs at least once ---
console.log('\n--- Section 3: do-while ---');

let count = 100;   // starts above the condition threshold

do {
  console.log('do-while body ran — count is', count);
  count++;
} while (count < 5);

console.log('After do-while. count is', count);
// do-while ran once even though 100 < 5 was false immediately

// --- SECTION 4: do-while that repeats ---
console.log('\n--- Section 4: do-while that repeats ---');

let roll = 0;
let tries = 0;

do {
  roll = Math.floor(Math.random() * 6) + 1;   // simulate a die roll: 1–6
  tries++;
  console.log('Roll', tries, ':', roll);
} while (roll !== 6);

console.log('Rolled a 6 after', tries, 'tries');

// --- SECTION 5: infinite loop demo (CONTROLLED — read the comment first) ---
// WARNING: This loop IS infinite. After you confirm what it does,
// immediately close the browser tab to stop it.
// Then reload, comment it out, and observe the corrected version.

// STEP A: Uncomment this block, save, and watch the tab freeze:
/*
console.log('\n--- Section 5: INFINITE LOOP DEMO ---');
let x = 0;
while (x < 5) {
  console.log('x is', x);
  // missing x++ — x stays 0 forever
}
*/

// STEP B: After closing and reloading, uncomment the CORRECTED version:
/*
console.log('\n--- Section 5: CORRECTED loop ---');
let x = 0;
while (x < 5) {
  console.log('x is', x);
  x++;   // update ensures the condition eventually becomes false
}
console.log('Loop finished. x is', x);
*/
```

### Step 2.2 — Perform the Infinite Loop Exercise

**Step A:** In the `while_demo.js` file, uncomment the infinite loop block (Section 5, STEP A). Save the file and observe the browser tab freeze. Then **immediately close the tab**. Do not wait — close it.

**Step B:** Reopen `for_loop.html` in Live Server (or create a fresh `while_demo.html` pointing to `while_demo.js`). Re-comment the infinite loop block and uncomment the CORRECTED version. Confirm it prints `x is 0` through `x is 4` and exits cleanly.

> **What to observe:** The difference between the two versions is one line — `x++`. Without it, `x` stays at `0` and `x < 5` is always `true`. This is the most common `while` loop bug.

### Screenshot 2

Take a screenshot of the console output from `while_demo.js` with the infinite loop commented out and the corrected version active. All five sections (with Section 5 showing the corrected output) must be visible. Label this **Lab05-Part2**.

---

## Part 3 — `break` and `continue`

### Step 3.1 — Create `break_continue.js`

Update your HTML `src` to `break_continue.js`:

```javascript
// break and continue — Module 05 Lab

// --- SECTION 1: break — search and stop ---
console.log('--- Section 1: break ---');

const scores = [72, 85, 91, 68, 55, 99, 44, 78];
const TARGET = 91;
let foundIndex = -1;

for (let i = 0; i < scores.length; i++) {
  console.log('Checking index', i, ':', scores[i]);
  if (scores[i] === TARGET) {
    foundIndex = i;
    break;   // stop searching once found
  }
}

if (foundIndex !== -1) {
  console.log('Found', TARGET, 'at index', foundIndex);
} else {
  console.log(TARGET, 'not found');
}
// Only three iterations run — break stops after finding 91 at index 2

// --- SECTION 2: continue — filter odd numbers ---
console.log('\n--- Section 2: continue ---');

console.log('Even numbers from 0 to 9:');
for (let i = 0; i < 10; i++) {
  if (i % 2 !== 0) {
    continue;   // skip odd numbers
  }
  console.log(i);
}
// Output: 0, 2, 4, 6, 8 — continue skips console.log for odd i

// --- SECTION 3: continue — skip a specific value ---
console.log('\n--- Section 3: continue to skip a value ---');

const names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'];

for (const name of names) {
  if (name === 'Charlie') {
    console.log('Skipping Charlie');
    continue;
  }
  console.log('Hello,', name);
}

// --- SECTION 4: nested break — exits inner loop only ---
console.log('\n--- Section 4: nested break ---');

console.log('Multiplication table (break when product > 6):');
for (let i = 1; i <= 3; i++) {
  for (let j = 1; j <= 5; j++) {
    if (i * j > 6) {
      console.log(`  i=${i}, j=${j}: product ${i * j} > 6, breaking inner loop`);
      break;   // exits inner loop only — outer loop continues
    }
    console.log(`  ${i} × ${j} = ${i * j}`);
  }
}
// The outer loop still runs for i=1, i=2, i=3
// The inner loop breaks as soon as the product exceeds 6

// --- SECTION 5: break vs continue summary ---
console.log('\n--- Section 5: break vs continue summary ---');

console.log('break demo — loop stops at 5:');
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  console.log('break loop i =', i);
}

console.log('\ncontinue demo — 5 is skipped but loop continues:');
for (let i = 0; i < 10; i++) {
  if (i === 5) continue;
  console.log('continue loop i =', i);
}
// break: 0,1,2,3,4 — stops at 5
// continue: 0,1,2,3,4,6,7,8,9 — skips 5 but keeps going
```

### Step 3.2 — Verify Key Behaviors

Confirm:

- Section 1: the `Checking index` log only appears three times (indices 0, 1, 2) — `break` stops the loop after the match.
- Section 2: only even numbers print — `continue` prevents the `console.log` from running for odd `i`.
- Section 4: the outer `for (let i = ...)` loop runs three full times; only the inner loop breaks early.
- Section 5: `break` produces 5 values (0–4); `continue` produces 9 values (0–9 minus 5).

### Screenshot 3

Take a screenshot of the full console output from `break_continue.js`. All five sections must be visible. Label this **Lab05-Part3**.

---

## Part 4 — `for...of` and `for...in`

### Step 4.1 — Create `modern_loops.js`

Update your HTML `src` to `modern_loops.js`:

```javascript
// for...of and for...in — Module 05 Lab

// --- SECTION 1: for...of on arrays ---
console.log('--- Section 1: for...of on an array ---');

const languages = ['JavaScript', 'Python', 'Java', 'C', 'Ruby'];

for (const lang of languages) {
  console.log(lang);
}

// --- SECTION 2: for...of on a string ---
console.log('\n--- Section 2: for...of on a string ---');

const message = 'Hello';

for (const char of message) {
  console.log(char);
}
// Output: H, e, l, l, o — each character individually

// --- SECTION 3: for...in on a plain object ---
console.log('\n--- Section 3: for...in on an object ---');

const car = {
  make: 'Toyota',
  model: 'Camry',
  year: 2022,
  color: 'silver'
};

for (const key in car) {
  console.log(`${key}: ${car[key]}`);
}
// Output: make: Toyota, model: Camry, year: 2022, color: silver

// --- SECTION 4: for...in trap on arrays ---
console.log('\n--- Section 4: for...in trap on an array ---');

const scores = [95, 82, 71, 60, 45];

console.log('Using for...in on an array:');
for (const index in scores) {
  console.log(`index: ${index}  typeof: ${typeof index}  value: ${scores[index]}`);
}
// index is a STRING — typeof returns 'string', not 'number'

console.log('\nUsing for...of on the same array (correct):');
for (const score of scores) {
  console.log(`score: ${score}  typeof: ${typeof score}`);
}
// score is a NUMBER — for...of gives the actual values

// --- SECTION 5: comparing for...of vs traditional for ---
console.log('\n--- Section 5: for...of vs traditional for ---');

const temps = [98.6, 101.2, 99.4, 102.0, 97.8];

// Traditional for — useful when you need the index
console.log('Traditional for (with index):');
for (let i = 0; i < temps.length; i++) {
  const flag = temps[i] > 100 ? ' ← FEVER' : '';
  console.log(`Reading ${i + 1}: ${temps[i]}°F${flag}`);
}

// for...of — cleaner when only values are needed
console.log('\nfor...of (values only):');
let feverCount = 0;
for (const temp of temps) {
  if (temp > 100) feverCount++;
}
console.log('Fever readings:', feverCount);

// --- SECTION 6: iterating an object's entries ---
console.log('\n--- Section 6: full object iteration ---');

const inventory = {
  apples: 50,
  bananas: 30,
  cherries: 120,
  dates: 8
};

let total = 0;

for (const item in inventory) {
  const qty = inventory[item];
  total += qty;
  const status = qty < 10 ? ' ← LOW STOCK' : '';
  console.log(`${item}: ${qty} units${status}`);
}

console.log('Total units in inventory:', total);
```

### Step 4.2 — Verify Key Outputs

Confirm:

- Section 2: each character of `'Hello'` prints on its own line — `for...of` works on strings.
- Section 4: `for...in` on the array shows `typeof index` as `'string'`, not `'number'`.
- Section 4: `for...of` on the same array shows `typeof score` as `'number'`.
- Section 6: the item with quantity `8` shows the `← LOW STOCK` flag.

### Screenshot 4

Take a screenshot of the full console output from `modern_loops.js`. All six sections must be visible. Label this **Lab05-Part4**.

---

## Deliverables

Submit the following to the Module 05 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `for_loop.js` | Counting up/down, `<` vs `<=` comparison, array iteration, off-by-one demo |
| `while_demo.js` | `while` with false initial condition, `do-while` runs-once, corrected infinite loop |
| `break_continue.js` | Search with `break`, filter with `continue`, nested `break` behavior |
| `modern_loops.js` | `for...of` on arrays/strings, `for...in` on objects, `for...in` array trap |
| Lab05-Part1.png | Console — `for` loop output including off-by-one `undefined` |
| Lab05-Part2.png | Console — `while`/`do-while` output with corrected infinite loop section |
| Lab05-Part3.png | Console — `break` and `continue` all five sections |
| Lab05-Part4.png | Console — `for...of` and `for...in` all six sections |

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In Section 2 of Part 1, you ran four different `for` loop variants side by side. Explain in your own words why `i < 5` starting at `0` produces five iterations but `i <= 5` starting at `0` produces six. Why does the starting value of `i` matter when choosing between `<` and `<=`?

2. In Part 2 Section 5, the infinite loop was caused by a missing `x++`. What specifically happens inside the engine on each iteration of that loop — what does it check, what does it do, and why does it never stop? What is the one-line fix?

3. In Part 3, `break` and `continue` both appear inside loops but behave very differently. After completing Part 3, describe in concrete terms what each keyword does to the execution sequence. Use the Section 5 output (the counts of iterations) to support your answer.

4. In Part 4 Section 4, `for...in` on an array returned string indices instead of values. Explain why this is a problem — give a specific scenario where treating `'0'` as a string instead of `0` as a number would produce a bug in real code.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Browser tab freezes | Ran the infinite loop in Section 5 of Part 2 | Close the tab immediately, re-comment the block, reload |
| Off-by-one `undefined` not showing | Using `i < planets.length` in the bug demo | Change to `i <= planets.length` for the bug demonstration only |
| `for...in` shows numbers not strings | Reading `typeof scores[index]` instead of `typeof index` | Log `typeof index`, not `typeof scores[index]` |
| `for...of` on object throws TypeError | Objects are not iterable with `for...of` | Use `for...in` for plain objects; use `Object.entries()` for `for...of` on objects |
| `continue` in `for...of` not working | Correct behavior — `continue` works in all loop types | Verify you are not confusing it with `break` |
| Nested `break` exits both loops | `break` labeled incorrectly | Plain `break` only exits the innermost loop — this is correct behavior |
