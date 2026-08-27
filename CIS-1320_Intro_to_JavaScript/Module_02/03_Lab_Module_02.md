# Lab Activity: Module 02 — Variables, Constants, and Scope

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will explore every behavioral difference between `var`, `let`, and `const` by running code experiments in the browser DevTools Console and in script files. You will trigger and observe the exact error messages that appear on the JSE exam, confirm the block-scope rules, and demonstrate hoisting behavior.

By the end of this lab you will have:

- Declared variables with all three keywords and observed their behaviors
- Confirmed block scope containment for `let` and `const`
- Confirmed that `var` leaks out of blocks
- Triggered and identified `ReferenceError` and `TypeError` from scope and const violations
- Observed hoisting with `var` returning `undefined` vs. `let` throwing `ReferenceError`
- Verified that `const` allows object property mutation

---

## Prerequisites

- VS Code with Live Server extension installed
- Google Chrome or Firefox
- Module 02 reading guide completed

---

## Part 1 — `let`, `const`, and `var` Basics

This part uses the DevTools Console directly. Open Chrome, press F12, and click the Console tab.

### Step 1.1 — Declaring with `let`

Type each line one at a time, pressing Enter after each:

```text
> let playerScore = 0
> playerScore
> playerScore = 150
> playerScore
```

Confirm: the variable holds `0` initially and `150` after reassignment.

### Step 1.2 — Declaring with `const`

```text
> const GRAVITY = 9.81
> GRAVITY
> GRAVITY = 10
```

The last line should throw: `TypeError: Assignment to constant variable.`

Write down the exact error message — you will need to recognize it on the quiz.

### Step 1.3 — Declaring with `var`

```text
> var legacyVar = 'first'
> legacyVar
> var legacyVar = 'second'
> legacyVar
```

Notice that re-declaring `var legacyVar` a second time produces no error. The value is simply updated. This is the re-declaration permissiveness of `var`.

Now try re-declaring `let`:

```text
> let myLet = 1
> let myLet = 2
```

You should see: `SyntaxError: Identifier 'myLet' has already been declared`

### Step 1.4 — `const` Requires Initialization

```text
> const x
```

You should see: `SyntaxError: Missing initializer in const declaration`

`const` must be given a value at the time of declaration. You cannot declare it empty and assign it later.

### Screenshot 1

Take a screenshot showing the console output from all of Part 1, including the `TypeError`, `SyntaxError` from re-declaring `let`, and `SyntaxError` from declaring `const` without a value. Label this **Lab02-Part1**.

---

## Part 2 — Block Scope: `let` vs. `var`

### Step 2.1 — Create the Script File

Create a folder named `module02-lab`. Inside it, create `scope_demo.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 02 — Scope Demo</title>
  <script src="scope_demo.js" defer></script>
</head>
<body>
  <h1>Scope Demo — check the console</h1>
</body>
</html>
```

Create `scope_demo.js` with the following content:

```javascript
// --- SECTION 1: let inside an if block ---

console.log('--- Section 1: let inside if ---');

if (true) {
  let blockMessage = 'I was declared inside the if block';
  console.log('Inside block:', blockMessage);   // works
}

try {
  console.log('Outside block:', blockMessage);   // should throw
} catch (e) {
  console.error('Error accessing blockMessage outside:', e.message);
}

// --- SECTION 2: var inside an if block ---

console.log('--- Section 2: var inside if ---');

if (true) {
  var leakyMessage = 'I was declared inside the if block with var';
  console.log('Inside block:', leakyMessage);
}

console.log('Outside block:', leakyMessage);   // var leaks — accessible here

// --- SECTION 3: let in a for loop ---

console.log('--- Section 3: let in for loop ---');

for (let i = 0; i < 3; i++) {
  console.log('Loop iteration i =', i);
}

try {
  console.log('After loop, i =', i);   // should throw
} catch (e) {
  console.error('Error accessing i after loop:', e.message);
}

// --- SECTION 4: var in a for loop ---

console.log('--- Section 4: var in for loop ---');

for (var j = 0; j < 3; j++) {
  console.log('Loop iteration j =', j);
}

console.log('After loop, j =', j);   // var j is 3 — leaked into outer scope
```

### Step 2.2 — Open in Browser

Open `scope_demo.html` with Live Server. Open DevTools → Console tab.

Observe the output for all four sections. Specifically note:

- Section 1: the `ReferenceError` for `blockMessage` accessed outside its block
- Section 2: `leakyMessage` prints successfully outside the block
- Section 3: the `ReferenceError` for `i` accessed after the loop
- Section 4: `j` is `3` after the loop

### Screenshot 2

Take a screenshot of the full console output from `scope_demo.js`. All four sections should be visible, including the two error messages. Label this **Lab02-Part2**.

---

## Part 3 — Hoisting

### Step 3.1 — Create `hoisting_demo.js`

Create `hoisting_demo.js` inside `module02-lab`. Update your HTML file's `src` attribute to `hoisting_demo.js`:

```javascript
// --- SECTION 1: var hoisting ---

console.log('--- Section 1: var hoisting ---');

console.log('Before declaration, varX =', varX);   // undefined — hoisted
var varX = 42;
console.log('After assignment, varX =', varX);      // 42

// --- SECTION 2: let Temporal Dead Zone ---

console.log('--- Section 2: let TDZ ---');

try {
  console.log('Before declaration, letY =', letY);   // ReferenceError
} catch (e) {
  console.error('TDZ error for letY:', e.message);
}

let letY = 100;
console.log('After declaration, letY =', letY);   // 100

// --- SECTION 3: const Temporal Dead Zone ---

console.log('--- Section 3: const TDZ ---');

try {
  console.log('Before declaration, constZ =', constZ);   // ReferenceError
} catch (e) {
  console.error('TDZ error for constZ:', e.message);
}

const constZ = 'hello';
console.log('After declaration, constZ =', constZ);   // hello

// --- SECTION 4: var hoisting in a function ---

console.log('--- Section 4: var hoisting inside function ---');

function demoFunction() {
  console.log('Inside function, before declaration:', localVar);   // undefined
  var localVar = 'I was hoisted within the function';
  console.log('Inside function, after declaration:', localVar);
}

demoFunction();

try {
  console.log('Outside function, localVar:', localVar);   // ReferenceError
} catch (e) {
  console.error('localVar not accessible outside function:', e.message);
}
```

### Step 3.2 — Observe the Output

Open the page and confirm all four sections appear:

- Section 1: `varX` prints `undefined` before its line — hoisting in action
- Section 2: `letY` throws `ReferenceError` — Temporal Dead Zone
- Section 3: `constZ` throws `ReferenceError` — same TDZ behavior
- Section 4: `localVar` is `undefined` inside the function before its assignment, and throws `ReferenceError` outside the function

### Screenshot 3

Take a screenshot of the full console output from `hoisting_demo.js`. All four sections should be visible. Label this **Lab02-Part3**.

---

## Part 4 — `const` with Objects and Arrays

### Step 4.1 — Create `const_objects.js`

Update your HTML `src` to `const_objects.js` and create the file:

```javascript
// --- SECTION 1: const object properties can be mutated ---

console.log('--- Section 1: const object mutation ---');

const student = {
  name: 'Maria',
  grade: 'A',
  score: 95
};

console.log('Original student:', student);

student.score = 100;              // modify existing property — OK
student.course = 'CIS-1320';      // add new property — OK
console.log('After mutation:', student);

try {
  student = { name: 'New Student' };   // reassign the binding — TypeError
} catch (e) {
  console.error('Cannot reassign const student:', e.message);
}

// --- SECTION 2: const array elements can be mutated ---

console.log('--- Section 2: const array mutation ---');

const grades = [90, 85, 92, 88];
console.log('Original grades:', grades);

grades.push(95);         // add element — OK
grades[0] = 99;          // modify element — OK
console.log('After mutation:', grades);

try {
  grades = [100, 100];   // reassign the binding — TypeError
} catch (e) {
  console.error('Cannot reassign const grades:', e.message);
}

// --- SECTION 3: summary comparison ---

console.log('--- Section 3: summary comparison ---');

var varName = 'Alice';
let letAge = 20;
const constCourse = 'CIS-1320';

console.log('var:', varName, '| let:', letAge, '| const:', constCourse);

varName = 'Bob';
letAge = 21;
// constCourse = 'Different'; // would throw TypeError if uncommented

console.log('After reassignment: var:', varName, '| let:', letAge, '| const:', constCourse);
```

### Step 4.2 — Verify the Output

Open the page and confirm:

- `student.score` changes to `100` after mutation
- `student.course` is added successfully
- Attempting to reassign `student` throws `TypeError`
- `grades` array is modified by `push` and index assignment
- Attempting to reassign `grades` throws `TypeError`

### Screenshot 4

Take a screenshot of the full console output from Part 4. Both `TypeError` messages from the attempted reassignments should be visible. Label this **Lab02-Part4**.

---

## Part 5 — Naming Conventions Practice

### Step 5.1 — Create `naming.js`

Update your HTML `src` to `naming.js` and create the file:

```javascript
// JavaScript Naming Conventions — Module 02 Lab

// camelCase for regular variables
const firstName = 'Jordan';
const lastName = 'Rivera';
const totalScore = 287;
const isLoggedIn = true;
const currentLevel = 3;

// UPPER_SNAKE_CASE for module-level constants
const MAX_PLAYERS = 4;
const DEFAULT_LIVES = 3;
const GAME_TITLE = 'Asteroid Defender';

// Computed values
const fullName = firstName + ' ' + lastName;
const averageScorePerLevel = totalScore / currentLevel;

console.log('Player:', fullName);
console.log('Total Score:', totalScore);
console.log('Average per level:', averageScorePerLevel.toFixed(2));
console.log('Max players:', MAX_PLAYERS);
console.log('Game:', GAME_TITLE);
console.log('Logged in:', isLoggedIn);

// --- Invalid identifiers (DO NOT uncomment — these would be syntax errors) ---
// let 1stPlayer = 'Alice';     // starts with a digit
// let my-score = 100;          // hyphen not allowed
// const let = 'reserved';      // 'let' is a reserved keyword
// var class = 'CIS-1320';      // 'class' is a reserved keyword
// let first name = 'Jordan';   // spaces not allowed
```

### Screenshot 5

Take a screenshot of the console output from `naming.js`. Label this **Lab02-Part5**.

---

## Deliverables

Submit the following to the Module 02 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `scope_demo.js` | Block scope demo with all four sections |
| `hoisting_demo.js` | Hoisting demo with var/let/const TDZ |
| `const_objects.js` | const mutation demo with objects and arrays |
| `naming.js` | Naming convention practice file |
| Lab02-Part1.png | Console — basic declarations and errors |
| Lab02-Part2.png | Console — block scope comparison |
| Lab02-Part3.png | Console — hoisting and TDZ |
| Lab02-Part4.png | Console — const with objects/arrays |
| Lab02-Part5.png | Console — naming conventions output |

---

## Part 9 — Challenge Exercise

**This section is optional but strongly recommended.** No screenshot submission is required, but completing these steps significantly deepens your understanding of scope and closures ahead of Module 06.

### Challenge Step 9.1 — Demonstrate Classic `var` Loop Closure Bug

In your `module02-lab` folder, create `closure_bug.js` and link it in your HTML. Add the following code:

```javascript
// Classic var closure bug
const funcs = [];
for (var i = 0; i < 3; i++) {
  funcs.push(function() { console.log('var loop i =', i); });
}
funcs[0]();   // What do you expect?
funcs[1]();
funcs[2]();

// Fix with let
const funcs2 = [];
for (let j = 0; j < 3; j++) {
  funcs2.push(function() { console.log('let loop j =', j); });
}
funcs2[0]();
funcs2[1]();
funcs2[2]();
```

Run this and observe the output. The `var` version prints `3` three times (all functions share the same `i`). The `let` version prints `0`, `1`, `2` correctly (each iteration gets its own `j`). Write a comment in the file explaining why the behaviors differ.

### Challenge Step 9.2 — Freeze a `const` Object with `Object.freeze()`

Add the following to a new file `freeze_demo.js`:

```javascript
const config = Object.freeze({
  maxRetries: 3,
  timeout: 5000,
  debug: false
});

config.debug = true;        // silently ignored in non-strict mode
config.newProp = 'test';    // silently ignored

console.log(config.debug);    // false — freeze prevented mutation
console.log(config.newProp);  // undefined — property was not added
```

Observe how `Object.freeze()` makes the object's properties truly immutable — mutations are silently ignored in non-strict mode, or throw `TypeError` in strict mode. Add `'use strict';` to the top of the file and observe the difference.

### Challenge Step 9.3 — Build a Scope Chain Visualization

Write a function `scopeChain()` that creates three levels of nested functions, each logging a variable from a different scope level. The innermost function should be able to access all three variables. Add `console.log` calls to demonstrate which scope each variable comes from. Annotate the code with comments identifying each scope level: global, outer function, inner function, and innermost function.

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In your own words, explain the Temporal Dead Zone. What is the practical benefit of `let` throwing a `ReferenceError` instead of silently returning `undefined` like `var` does?

2. You observed that a `const` object's properties can be changed even though `const` cannot be reassigned. How would you explain this distinction to a classmate who expected `const` to make data completely unchangeable?

3. Why do most modern JavaScript style guides recommend using `const` by default and only switching to `let` when necessary? What problem does this habit prevent?

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| No output in console | HTML `src` attribute still points to old file | Update `<script src="...">` in HTML |
| `ReferenceError: blockMessage is not defined` is confusing | Working correctly | This IS the expected output — `let` is block-scoped |
| `undefined` before `varX` declaration looks wrong | Working correctly | This is `var` hoisting — document it in your reflection |
| TypeError messages scroll off screen | Console output exceeds visible area | Scroll up in console, or filter for Errors only |
| `Cannot access before initialization` error message | Correct TDZ error | Write down this exact wording — it appears on the JSE exam |
