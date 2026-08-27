# Lab Activity: Module 03 — Data Types and Operators

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will explore JavaScript's type system and operators through hands-on experiments in the browser console and in script files. You will confirm the `typeof` results for all primitive types (including the `null` quirk), observe type coercion in action, compare `==` vs `===`, and build a utility script that demonstrates operator precedence.

By the end of this lab you will have:

- Used `typeof` on all seven primitive types and objects
- Triggered and explained coercion with the `+` operator
- Confirmed the six falsy values
- Mapped the surprising `==` results tested on the JSE exam
- Built a script using arithmetic, comparison, and logical operators

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 03 reading guide completed

---

## Part 1 — `typeof` Experiments

This part uses the DevTools Console. Open Chrome, press F12, click Console.

### Step 1.1 — Type Each Expression

Type each of the following and record the result. Do not guess — run each one and write down what the console shows:

```text
> typeof 42
> typeof 3.14
> typeof 'hello'
> typeof "JavaScript"
> typeof true
> typeof false
> typeof undefined
> typeof null
> typeof Symbol('id')
> typeof 42n
> typeof {}
> typeof []
> typeof function() {}
> typeof NaN
```

### Step 1.2 — The `null` Trap

You should see that `typeof null` returns `'object'`. Now confirm that `null` is not actually an object:

```text
> null === null
> null instanceof Object
> typeof null === 'object'
> null == undefined
> null === undefined
```

Record all five results. These are frequently tested exam combinations.

### Step 1.3 — `NaN` Behavior

```text
> typeof NaN
> NaN === NaN
> NaN == NaN
> Number.isNaN(NaN)
> Number.isNaN(42)
> Number.isNaN('hello')
> 0 / 0
> 'hello' - 5
> Math.sqrt(-1)
```

Record each result. Specifically confirm that `typeof NaN === 'number'` is `true` and `NaN === NaN` is `false`.

### Screenshot 1

Take a screenshot of the console showing all the `typeof` results and the `NaN` experiments from Steps 1.1 through 1.3. Label this **Lab03-Part1**.

---

## Part 2 — Type Coercion with the `+` Operator

### Step 2.1 — Predict Before Running

Before typing each expression, write down what you think the result will be on paper. Then type it and check. This prediction-then-verify method is the best way to build intuition.

```text
> 5 + 3
> '5' + 3
> 5 + '3'
> 5 + 3 + '1'
> '1' + 5 + 3
> '1' + (5 + 3)
> 'Score: ' + 100
> 'Year: ' + 2025
```

### Step 2.2 — Other Arithmetic Operators (No Concatenation)

```text
> '10' - 5
> '4' * '3'
> '20' / '4'
> '10' % 3
> '5' ** 2
> 'hello' - 5
> 'hello' * 2
> true + 1
> false + 1
> null + 1
> undefined + 1
> true + true
> false + false
```

Record each result. Notice which values coerce to numbers (true→1, false→0, null→0) and which produce NaN (undefined, non-numeric strings).

### Step 2.3 — Create `coercion_demo.js`

Create a folder `module03-lab`. Inside it, create `coercion_demo.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 03 — Coercion Demo</title>
  <script src="coercion_demo.js" defer></script>
</head>
<body>
  <h1>Coercion Demo — check the console</h1>
</body>
</html>
```

Create `coercion_demo.js`:

```javascript
// Type Coercion Demo — Module 03 Lab

console.log('--- String + Number Coercion ---');
console.log('5' + 3);           // '53'
console.log(5 + '3');           // '53'
console.log(5 + 3 + '1');       // '81'
console.log('1' + 5 + 3);       // '153'
console.log('1' + (5 + 3));     // '18' — parentheses force numeric addition first

console.log('--- Subtraction Forces Number ---');
console.log('10' - 5);          // 5
console.log('4' * '3');         // 12
console.log('hello' - 5);       // NaN

console.log('--- Boolean and null Coercion ---');
console.log(true + 1);          // 2
console.log(false + 1);         // 1
console.log(null + 1);          // 1
console.log(undefined + 1);     // NaN

console.log('--- Numeric Conversion with Number() ---');
console.log(Number('42'));       // 42
console.log(Number('3.14'));     // 3.14
console.log(Number(''));         // 0
console.log(Number('hello'));    // NaN
console.log(Number(true));       // 1
console.log(Number(false));      // 0
console.log(Number(null));       // 0
console.log(Number(undefined));  // NaN
```

Open `coercion_demo.html` in Live Server and verify the console output.

### Screenshot 2

Take a screenshot of the full console output from `coercion_demo.js`. Label this **Lab03-Part2**.

---

## Part 3 — `==` vs `===`

### Step 3.1 — Console Experiments

Type each comparison in the console. Record both the result and your explanation of why:

```text
> 5 === 5
> 5 === '5'
> 0 === false
> '' === false
> null === undefined
> 5 == 5
> 5 == '5'
> 0 == false
> '' == false
> 0 == ''
> null == undefined
> null == 0
> null == false
> undefined == false
> NaN == NaN
> NaN === NaN
```

### Step 3.2 — Create `equality_demo.js`

Create `equality_demo.js` and update the HTML `src` attribute:

```javascript
// Equality Demo — Module 03 Lab

console.log('--- Strict Equality (===) ---');
console.log(5 === 5);           // true
console.log(5 === '5');         // false — different types
console.log(0 === false);       // false — different types
console.log('' === false);      // false — different types
console.log(null === undefined); // false — different types
console.log(null === null);     // true

console.log('--- Loose Equality (==) ---');
console.log(5 == 5);            // true
console.log(5 == '5');          // true — '5' coerced to 5
console.log(0 == false);        // true — false coerced to 0
console.log('' == false);       // true — both coerce to 0
console.log(0 == '');           // true — both coerce to 0
console.log(null == undefined); // true — special rule
console.log(null == 0);         // false — null only equals undefined loosely
console.log(null == false);     // false — null only equals undefined loosely
console.log(NaN == NaN);        // false — NaN equals nothing
console.log(NaN === NaN);       // false — NaN equals nothing

console.log('--- Comparison Operators ---');
console.log(5 > 3);             // true
console.log('b' > 'a');         // true — string comparison by char code
console.log('10' > 9);          // true — '10' coerced to 10
console.log(10 > '9');          // true — '9' coerced to 9
console.log('10' > '9');        // false — string comparison: '1' < '9'

console.log('--- !== vs != ---');
console.log(5 !== '5');         // true — different types (strict)
console.log(5 != '5');          // false — '5' coerced to 5 (loose)
```

Verify the output matches the comments.

### Screenshot 3

Take a screenshot showing the full console output from `equality_demo.js`. Label this **Lab03-Part3**.

---

## Part 4 — Falsy and Truthy Values

### Step 4.1 — Console Experiments

```text
> Boolean(false)
> Boolean(0)
> Boolean('')
> Boolean(null)
> Boolean(undefined)
> Boolean(NaN)
> Boolean('0')
> Boolean([])
> Boolean({})
> Boolean(1)
> Boolean(-1)
> Boolean('false')
> Boolean(' ')
```

Record each result. The key surprises: `Boolean('0')`, `Boolean([])`, and `Boolean({})` are all `true`.

### Step 4.2 — Create `falsy_demo.js`

Create `falsy_demo.js`:

```javascript
// Falsy and Truthy Demo — Module 03 Lab

const values = [
  false, 0, -0, '', null, undefined, NaN,   // all falsy
  true, 1, -1, '0', 'false', ' ', [], {}    // all truthy
];

console.log('--- Falsy/Truthy Classification ---');
for (const val of values) {
  const label = val === null ? 'null'
    : val !== val ? 'NaN'      // NaN check — only value !== itself
    : typeof val === 'string' ? `'${val}'`
    : String(val);
  console.log(`Boolean(${label}) =`, Boolean(val));
}

console.log('--- Short-Circuit Evaluation ---');
console.log('hello' && 42);          // 42
console.log(0 && 'hello');           // 0
console.log('hello' || 42);          // 'hello'
console.log(0 || 'default');         // 'default'
console.log(false || null || '');    // ''
console.log(false || null || 'ok');  // 'ok'

console.log('--- Default Value Pattern ---');
const userInput = '';
const displayName = userInput || 'Anonymous';
console.log('Display name:', displayName);   // 'Anonymous'

const userInput2 = 'Jordan';
const displayName2 = userInput2 || 'Anonymous';
console.log('Display name:', displayName2);  // 'Jordan'
```

### Screenshot 4

Take a screenshot of the full console output from `falsy_demo.js`. Label this **Lab03-Part4**.

---

## Part 5 — Operators in Practice

### Step 5.1 — Create `operators_practice.js`

Create `operators_practice.js`. This script builds a simple score calculator that uses all the operator types from this module:

```javascript
// Operators Practice — Module 03 Lab
// Simple game score calculator

const playerName = 'Alex';
const baseScore = 150;
const bonusMultiplier = 2;
const penaltyPoints = 30;
const ROUND_COUNT = 5;

// Arithmetic
const bonusScore = baseScore * bonusMultiplier;
const finalScore = bonusScore - penaltyPoints;
const averagePerRound = finalScore / ROUND_COUNT;
const remainder = finalScore % 10;

console.log('--- Score Calculation ---');
console.log('Player:', playerName);
console.log('Base Score:', baseScore);
console.log('Bonus Score (x' + bonusMultiplier + '):', bonusScore);
console.log('Final Score (after -' + penaltyPoints + ' penalty):', finalScore);
console.log('Average per round:', averagePerRound);
console.log('Score mod 10:', remainder);

// Comparison
const WINNING_SCORE = 200;
console.log('\n--- Comparisons ---');
console.log('Final score >= winning threshold:', finalScore >= WINNING_SCORE);
console.log('Final score === 270:', finalScore === 270);
console.log('typeof finalScore === "number":', typeof finalScore === 'number');

// Logical operators
const isHighScore = finalScore > 250;
const isPositive = finalScore > 0;
const isValid = typeof finalScore === 'number' && !Number.isNaN(finalScore);

console.log('\n--- Logical Checks ---');
console.log('Is high score:', isHighScore);
console.log('Is positive:', isPositive);
console.log('Is valid number:', isValid);
console.log('Is high score AND valid:', isHighScore && isValid);
console.log('Is high score OR positive:', isHighScore || isPositive);

// Assignment operators
let runningTotal = 0;
console.log('\n--- Accumulating Scores ---');
const roundScores = [42, 38, 55, 61, 50];
for (const score of roundScores) {
  runningTotal += score;
  console.log('After adding', score, ':', runningTotal);
}
console.log('Total across all rounds:', runningTotal);
console.log('Average:', (runningTotal / roundScores.length).toFixed(1));
```

### Screenshot 5

Take a screenshot of the full console output from `operators_practice.js`. Label this **Lab03-Part5**.

---

## Deliverables

Submit the following to the Module 03 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `coercion_demo.js` | Type coercion experiments |
| `equality_demo.js` | `==` vs `===` comparison demo |
| `falsy_demo.js` | Falsy/truthy classification and short-circuit |
| `operators_practice.js` | Score calculator using all operator types |
| Lab03-Part1.png | Console — `typeof` and `NaN` experiments |
| Lab03-Part2.png | Console — coercion demo output |
| Lab03-Part3.png | Console — equality demo output |
| Lab03-Part4.png | Console — falsy/truthy demo output |
| Lab03-Part5.png | Console — operators practice output |

---

## Part 9 — Challenge Exercise

**This section is optional but strongly recommended.** These steps deepen your understanding of type coercion edge cases that frequently appear on the JSE exam and in technical interviews.

### Challenge Step 9.1 — Build a Full Coercion Truth Table

Create `coercion_table.js`. Use `console.table()` to output a structured table showing how JavaScript coerces each of the six falsy values when operated on by `+`, `-`, `*`, and `/` with the number `1`. Structure it as an array of objects:

```javascript
const falsyValues = [false, 0, '', null, undefined, NaN];
const rows = falsyValues.map(val => ({
  value: String(val === '' ? '""' : val),
  'val + 1': val + 1,
  'val - 1': val - 1,
  'val * 1': val * 1,
  'val / 1': val / 1
}));
console.table(rows);
```

Observe which falsy values produce `NaN` under arithmetic and which coerce to `0`. Write a comment explaining the pattern.

### Challenge Step 9.2 — Nullish Coalescing vs. Logical OR

The nullish coalescing operator `??` (ES2020) is stricter than `||`. It only falls back to the right-hand side when the left side is `null` or `undefined` — not for other falsy values like `0` or `''`. Create `nullish_demo.js` and compare the two:

```javascript
const score = 0;
const displayScore1 = score || 'No score';   // '||' treats 0 as falsy
const displayScore2 = score ?? 'No score';   // '??' treats 0 as a valid value

console.log('Using ||:', displayScore1);   // 'No score' — bug!
console.log('Using ??:', displayScore2);   // 0 — correct

const name = null;
console.log('null || "Guest":', name || 'Guest');   // 'Guest'
console.log('null ?? "Guest":', name ?? 'Guest');   // 'Guest'
```

Write a comment describing when you would prefer `??` over `||`.

### Challenge Step 9.3 — Explore `Object.is()` for Edge Cases

`Object.is()` is more precise than `===` in two edge cases: `NaN` and `-0`. Create `object_is_demo.js` and test:

```javascript
console.log(NaN === NaN);          // false
console.log(Object.is(NaN, NaN));  // true

console.log(0 === -0);             // true
console.log(Object.is(0, -0));     // false
```

Explain in comments why `Object.is()` was introduced and in what real-world scenario distinguishing `0` from `-0` could matter.

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. You observed that `'1' + 5 + 3` produces `'153'` while `1 + 5 + '3'` produces `'63'`. Explain in your own words why the position of the string operand changes the result. What rule governs this behavior?

2. The reading guide says to always use `===` instead of `==`. After working through Part 3, identify one specific `==` comparison from the lab where the result would surprise a developer who assumed `==` behaves like `===`. Explain what mental model they would need to have to predict the correct result.

3. Before this lab, you may have assumed that empty arrays `[]` and empty objects `{}` are falsy. After Part 4, explain why they are truthy and describe a real-world scenario where this distinction could cause a bug.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `'153'` result surprising in Part 2 | Expected numeric addition | Left-to-right: `'1'+5='15'`, then `'15'+3='153'` |
| `NaN` appears in arithmetic | String that cannot convert to number | Check operands — `'hello' - 5 = NaN` |
| `typeof null` showing `'object'` seems wrong | JavaScript historical bug | It IS wrong but it is the specified behavior |
| `null == 0` returning `false` is confusing | `null` only loosely equals `undefined` | Special case — `null == undefined` is true but `null == 0` is not |
| Script output is empty | HTML `src` still points to old file | Update `<script src="...">` in HTML |
