# Lab Activity: Module 06 — Functions and Arrow Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will write functions using every syntax covered in Module 06: function declarations, function expressions, and arrow functions in all their forms. You will deliberately trigger the hoisting `ReferenceError`, observe functions that return `undefined`, and test how default parameters respond to `undefined` vs `null`. A final integration exercise combines all concepts into a working grade-report generator.

By the end of this lab you will have:

- Written function declarations with parameters and return values
- Observed hoisting: called a declaration before its definition and a `const` expression before its definition
- Progressively converted a function declaration to the shortest valid arrow function form
- Used default parameters and verified which argument values trigger the default
- Used rest parameters to build a variadic function
- Built an integrated grade-report generator using all function forms together

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 06 reading guide completed

---

## Part 1 — Function Declarations

### Step 1.1 — Create the Project

Create folder `module06-lab`. Inside it create `declarations.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 06 — Function Declarations</title>
  <script src="declarations.js" defer></script>
</head>
<body>
  <h1>Function Declarations — check the console</h1>
</body>
</html>
```

Create `declarations.js`:

```javascript
// Function Declarations — Module 06 Lab

// --- SECTION 1: basic declaration, parameters, return ---
console.log('--- Section 1: basic function declaration ---');

function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

function greet(name) {
  return 'Hello, ' + name + '!';
}

console.log('add(3, 4):', add(3, 4));
console.log('multiply(6, 7):', multiply(6, 7));
console.log('greet("Alice"):', greet('Alice'));

// --- SECTION 2: return undefined ---
console.log('\n--- Section 2: missing return → undefined ---');

function logSquare(n) {
  console.log('  Square of', n, 'is', n * n);
  // no return
}

const result = logSquare(5);
console.log('Return value of logSquare(5):', result);
// result is undefined — the function produced output but returned nothing

// --- SECTION 3: early return ---
console.log('\n--- Section 3: early return ---');

function classifyScore(score) {
  if (score < 0 || score > 100) {
    return 'Invalid score';
  }
  if (score >= 90) return 'A';
  if (score >= 80) return 'B';
  if (score >= 70) return 'C';
  if (score >= 60) return 'D';
  return 'F';
}

const testScores = [-5, 0, 59, 60, 75, 85, 95, 100, 105];
for (const s of testScores) {
  console.log(`classifyScore(${s}): ${classifyScore(s)}`);
}

// --- SECTION 4: hoisting — call BEFORE the declaration ---
console.log('\n--- Section 4: hoisting ---');

// Call square before it is defined in the source — works because of hoisting
console.log('square(8) called before definition:', square(8));

function square(n) {
  return n * n;
}

console.log('square(8) called after definition:', square(8));

// --- SECTION 5: hoisting trap — const function expression ---
console.log('\n--- Section 5: const expression hoisting trap ---');

try {
  console.log('cube(3) before const assignment:', cube(3));
} catch (e) {
  console.error('Error:', e.message);
  // Expected: ReferenceError: Cannot access 'cube' before initialization
}

const cube = function(n) {
  return n * n * n;
};

console.log('cube(3) after const assignment:', cube(3));
```

### Step 1.2 — Open and Verify

Open `declarations.html` in Live Server. Confirm:

- Section 4: `square(8)` before the definition prints `64` — hoisting works.
- Section 5: the `try/catch` catches a `ReferenceError` with the message `Cannot access 'cube' before initialization`.

### Screenshot 1

Take a screenshot showing the full console output from `declarations.js`. All five sections must be visible. Label this **Lab06-Part1**.

---

## Part 2 — Arrow Functions

### Step 2.1 — Create `arrow_functions.js`

Update your HTML `src` to `arrow_functions.js`:

```javascript
// Arrow Functions — Module 06 Lab

// --- SECTION 1: progressive shortening ---
console.log('--- Section 1: arrow function forms ---');

// Full function expression
const doubleV1 = function(n) {
  return n * 2;
};

// Arrow — full form with braces and return
const doubleV2 = (n) => {
  return n * 2;
};

// Arrow — single parameter, braces and return still explicit
const doubleV3 = n => {
  return n * 2;
};

// Arrow — implicit return (no braces, no return keyword)
const doubleV4 = n => n * 2;

// All four produce identical results
console.log('doubleV1(6):', doubleV1(6));
console.log('doubleV2(6):', doubleV2(6));
console.log('doubleV3(6):', doubleV3(6));
console.log('doubleV4(6):', doubleV4(6));
// All print 12

// --- SECTION 2: multiple parameters and no parameters ---
console.log('\n--- Section 2: parameter count variations ---');

const addArrow = (a, b) => a + b;
const multiplyArrow = (a, b) => a * b;
const getCurrentYear = () => 2026;
const sayHi = () => 'Hi there!';

console.log('addArrow(10, 5):', addArrow(10, 5));
console.log('multiplyArrow(3, 7):', multiplyArrow(3, 7));
console.log('getCurrentYear():', getCurrentYear());
console.log('sayHi():', sayHi());

// --- SECTION 3: multi-statement arrow (braces required, explicit return) ---
console.log('\n--- Section 3: multi-statement arrow ---');

const clamp = (value, min, max) => {
  if (value < min) return min;
  if (value > max) return max;
  return value;
};

console.log('clamp(5, 0, 10):', clamp(5, 0, 10));    // 5
console.log('clamp(-3, 0, 10):', clamp(-3, 0, 10));  // 0
console.log('clamp(15, 0, 10):', clamp(15, 0, 10));  // 10

// --- SECTION 4: implicit return trap ---
console.log('\n--- Section 4: implicit return trap ---');

// CORRECT — implicit return (no braces)
const squareCorrect = n => n * n;

// BUG — braces added but return forgotten
const squareBug = n => {
  n * n;   // computes value but does NOT return it
};

console.log('squareCorrect(5):', squareCorrect(5));   // 25
console.log('squareBug(5):', squareBug(5));            // undefined — missing return

// FIXED
const squareFixed = n => {
  return n * n;
};
console.log('squareFixed(5):', squareFixed(5));   // 25

// --- SECTION 5: arrow functions as callbacks ---
console.log('\n--- Section 5: arrow functions as callbacks ---');

const numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3];

// Array.sort with an arrow comparator
const sorted = [...numbers].sort((a, b) => a - b);
console.log('sorted ascending:', sorted);

// Array.filter with an arrow predicate
const evens = numbers.filter(n => n % 2 === 0);
console.log('even numbers:', evens);

// Array.map with an arrow transform
const doubled = numbers.map(n => n * 2);
console.log('doubled:', doubled);
```

### Step 2.2 — Verify the Implicit Return Trap

In Section 4, confirm that `squareBug(5)` prints `undefined`. The braces converted it from an implicit-return arrow to a body-statement arrow — without `return`, the function returns nothing.

### Screenshot 2

Take a screenshot of the full console output from `arrow_functions.js`. All five sections must be visible. Label this **Lab06-Part2**.

---

## Part 3 — Default and Rest Parameters

### Step 3.1 — Create `parameters.js`

Update your HTML `src` to `parameters.js`:

```javascript
// Default and Rest Parameters — Module 06 Lab

// --- SECTION 1: default parameters ---
console.log('--- Section 1: default parameters ---');

function createUser(username = 'anonymous', role = 'viewer', active = true) {
  return { username, role, active };
}

// All arguments provided
console.log(createUser('alice', 'admin', false));

// Some omitted — defaults kick in
console.log(createUser('bob'));
console.log(createUser());

// undefined triggers the default — null does NOT
console.log('With undefined:', createUser(undefined, undefined, undefined));
console.log('With null:', createUser(null, null, null));
// null produces { username: null, role: null, active: null }

// --- SECTION 2: default triggers comparison ---
console.log('\n--- Section 2: what triggers a default? ---');

function showDefault(x = 'DEFAULT') {
  console.log('x is:', x);
}

showDefault('hello');     // 'hello' — no default
showDefault();            // 'DEFAULT' — omitted
showDefault(undefined);   // 'DEFAULT' — undefined triggers default
showDefault(null);        // null — null does NOT trigger default
showDefault(0);           // 0 — 0 does NOT trigger default
showDefault('');          // '' — empty string does NOT trigger default
showDefault(false);       // false — false does NOT trigger default

// --- SECTION 3: default parameter referencing a previous parameter ---
console.log('\n--- Section 3: default expression ---');

function makeRectangle(width, height = width) {
  return { width, height, area: width * height };
}

console.log('makeRectangle(4, 6):', makeRectangle(4, 6));   // explicit height
console.log('makeRectangle(5):', makeRectangle(5));          // square — height = width

// --- SECTION 4: rest parameters ---
console.log('\n--- Section 4: rest parameters ---');

function sum(...numbers) {
  let total = 0;
  for (const n of numbers) {
    total += n;
  }
  return total;
}

console.log('sum():', sum());
console.log('sum(1, 2, 3):', sum(1, 2, 3));
console.log('sum(10, 20, 30, 40, 50):', sum(10, 20, 30, 40, 50));

// --- SECTION 5: rest with leading fixed parameters ---
console.log('\n--- Section 5: fixed + rest ---');

function logWithLabel(label, separator, ...items) {
  const joined = items.join(separator);
  console.log(`${label}: ${joined}`);
}

logWithLabel('Fruits', ', ', 'apple', 'banana', 'cherry');
logWithLabel('Scores', ' | ', 85, 92, 78, 96, 88);
logWithLabel('Empty', '-');   // rest receives empty array

// --- SECTION 6: rest parameter is a real array ---
console.log('\n--- Section 6: rest is a real Array ---');

function analyzeArgs(...args) {
  console.log('typeof args:', typeof args);
  console.log('Array.isArray(args):', Array.isArray(args));
  console.log('args.length:', args.length);
  console.log('args:', args);
}

analyzeArgs(10, 'hello', true, null);
// args is a genuine Array — can use .length, forEach, map, etc.
```

### Step 3.2 — Verify Key Outputs

Confirm:

- Section 2: `showDefault(undefined)` prints `DEFAULT` but `showDefault(null)` prints `null` — the critical distinction.
- Section 6: `Array.isArray(args)` is `true` — rest parameters produce real arrays.

### Screenshot 3

Take a screenshot of the full console output from `parameters.js`. All six sections must be visible. Label this **Lab06-Part3**.

---

## Part 4 — Integration: Grade Report Generator

### Step 4.1 — Create `grade_report.js`

Update your HTML `src` to `grade_report.js`. This exercise uses function declarations, arrow functions, default parameters, and rest parameters together in a single program:

```javascript
// Grade Report Generator — Module 06 Lab Integration

// --- Helper functions (declarations — hoistable) ---

function letterGrade(score) {
  if (score >= 90) return 'A';
  if (score >= 80) return 'B';
  if (score >= 70) return 'C';
  if (score >= 60) return 'D';
  return 'F';
}

function average(...scores) {
  if (scores.length === 0) return 0;
  const total = scores.reduce((sum, s) => sum + s, 0);
  return total / scores.length;
}

// --- Arrow utility functions ---

const isPassing = score => score >= 60;
const formatScore = (name, score) => `  ${name}: ${score} (${letterGrade(score)})`;

// --- Report builder (uses default parameter) ---

function buildReport(studentName = 'Unknown Student', ...scores) {
  const avg = average(...scores);
  const passing = scores.filter(isPassing).length;
  const failing = scores.length - passing;
  const grade = letterGrade(avg);

  console.log(`\n=== Grade Report: ${studentName} ===`);
  console.log(`Scores submitted: ${scores.length}`);
  console.log(`Average: ${avg.toFixed(1)} → ${grade}`);
  console.log(`Passing: ${passing} | Failing: ${failing}`);
  console.log(`Status: ${isPassing(avg) ? 'PASS' : 'FAIL'}`);
}

// --- Generate reports ---

buildReport('Alice Johnson', 92, 87, 95, 88, 91);
buildReport('Bob Martinez', 72, 65, 58, 80, 70);
buildReport('Carol White');             // no scores — uses default name, avg = 0
buildReport(undefined, 85, 90, 78);    // undefined name → default used

// --- Individual score breakdown ---
console.log('\n--- Individual Score Detail ---');

const aliceScores = [92, 87, 95, 88, 91];
const aliceReport = aliceScores.map((score, index) =>
  formatScore(`Quiz ${index + 1}`, score)
);
console.log('Alice:');
aliceReport.forEach(line => console.log(line));

// --- Summary stats using arrow functions ---
const allScores = [92, 87, 95, 88, 91, 72, 65, 58, 80, 70];
const highest = allScores.reduce((max, s) => s > max ? s : max, 0);
const lowest = allScores.reduce((min, s) => s < min ? s : min, 100);
const classAvg = average(...allScores);

console.log('\n--- Class Summary ---');
console.log(`Class average: ${classAvg.toFixed(1)}`);
console.log(`Highest score: ${highest}`);
console.log(`Lowest score: ${lowest}`);
console.log(`Class grade: ${letterGrade(classAvg)}`);
```

### Step 4.2 — Verify the Integration

Confirm:

- `buildReport('Carol White')` shows `Scores submitted: 0` and `Average: 0.0`.
- `buildReport(undefined, 85, 90, 78)` shows `Unknown Student` — `undefined` triggered the default.
- Alice's individual breakdown shows five lines with `Quiz 1` through `Quiz 5`.
- Bob Martinez's report shows `Status: PASS` if his average is ≥ 60 — calculate manually to verify.

### Screenshot 4

Take a screenshot of the full console output from `grade_report.js`. The complete report for all students and the class summary must be visible. Label this **Lab06-Part4**.

---

## Deliverables

Submit the following to the Module 06 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `declarations.js` | Function declarations, return values, `undefined` return, early return, hoisting demo |
| `arrow_functions.js` | Four arrow forms, parameter variations, implicit return trap, callbacks |
| `parameters.js` | Default parameter triggers (`undefined` vs `null`), default expressions, rest parameters |
| `grade_report.js` | Integration exercise using all function forms together |
| Lab06-Part1.png | Console — declarations including hoisting `ReferenceError` |
| Lab06-Part2.png | Console — arrow functions including `undefined` from missing return |
| Lab06-Part3.png | Console — default and rest parameters |
| Lab06-Part4.png | Console — complete grade report output |

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In Part 1 Section 4, calling `square(8)` before its definition worked because of hoisting. In Section 5, calling `cube(3)` before its definition threw a `ReferenceError`. Explain precisely why the two behaviors differ. What does the JavaScript engine do differently with a function declaration versus a `const` function expression before execution begins?

2. In Part 2 Section 4, adding braces to an arrow function silently broke it — `squareBug(5)` returned `undefined` instead of `25`. Describe the rule in your own words: when does an arrow function use an implicit return, and when does it require an explicit `return`?

3. In Part 3 Section 2, `showDefault(null)` printed `null` instead of `'DEFAULT'`, but `showDefault(undefined)` printed `'DEFAULT'`. Explain why. What does this tell you about the relationship between default parameters and the `??` operator from Module 04?

4. In the integration exercise, the `buildReport` function used both default parameters and rest parameters in the same signature: `function buildReport(studentName = 'Unknown Student', ...scores)`. Why must `...scores` be the last parameter? What would happen if you tried to write `function buildReport(...scores, studentName = 'Unknown Student')`?

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Hoisting `ReferenceError` not thrown | `let` instead of `const` (TDZ behavior is the same) or function declaration used | Ensure you used `const cube = function(...)` |
| `squareBug(5)` returns `25` instead of `undefined` | Return was accidentally added inside braces | Remove `return` — the bug demo needs to be missing it |
| `showDefault(null)` prints `'DEFAULT'` | Default parameter was written as `x ?? 'DEFAULT'` not `x = 'DEFAULT'` | Use function default syntax `x = 'DEFAULT'` — they behave differently for `null` |
| Rest parameter receives wrong values | Rest is not the last parameter | Ensure `...rest` is always the final parameter in the list |
| `average()` returns `NaN` instead of `0` | Division by zero when `scores.length === 0` | The `if (scores.length === 0) return 0;` guard handles this |
