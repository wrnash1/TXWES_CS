# Lab Activity: Module 04 — Control Flow and Conditionals

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will build scripts that use every conditional structure covered in Module 04: `if/else if/else`, `switch` (with and without `break`), ternary expressions, and logical operators including `??`. You will deliberately introduce the assignment-in-condition bug and the switch fall-through so you can observe both first-hand.

By the end of this lab you will have:

- Built a grade calculator with `if/else if/else`
- Observed the assignment-in-condition trap and explained it
- Implemented a `switch` with correct `break` statements
- Demonstrated switch fall-through and explained the output
- Converted `if/else` logic to ternary expressions
- Used `&&`, `||`, `!`, and `??` to build a user access controller

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 04 reading guide completed

---

## Part 1 — Grade Calculator with `if/else if/else`

### Step 1.1 — Create the Project

Create folder `module04-lab`. Inside it create `grade.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 04 — Grade Calculator</title>
  <script src="grade.js" defer></script>
</head>
<body>
  <h1>Grade Calculator — check the console</h1>
</body>
</html>
```

Create `grade.js`:

```javascript
// Grade Calculator — Module 04 Lab

function getLetterGrade(score) {
  if (score >= 90) {
    return 'A';
  } else if (score >= 80) {
    return 'B';
  } else if (score >= 70) {
    return 'C';
  } else if (score >= 60) {
    return 'D';
  } else {
    return 'F';
  }
}

const testScores = [95, 83, 71, 65, 52, 100, 0, 89, 90, 59];

console.log('--- Grade Results ---');
for (const score of testScores) {
  console.log(`Score ${score}: ${getLetterGrade(score)}`);
}

// --- BOUNDARY TESTING ---
console.log('\n--- Boundary Cases ---');
console.log('Score 90 (exact A boundary):', getLetterGrade(90));
console.log('Score 89 (just below A):', getLetterGrade(89));
console.log('Score 80 (exact B boundary):', getLetterGrade(80));
console.log('Score 60 (exact D boundary):', getLetterGrade(60));
console.log('Score 59 (just below D → F):', getLetterGrade(59));
```

### Step 1.2 — Open and Verify

Open `grade.html` in Live Server. Confirm each score maps to the expected letter grade. Pay attention to the boundary cases — 90 should be A, 89 should be B.

### Step 1.3 — Demonstrate the Assignment Trap

Add the following block to the **bottom** of `grade.js`:

```javascript
// --- ASSIGNMENT IN CONDITION TRAP ---
console.log('\n--- Assignment Trap Demo ---');

let threshold = 70;

// BUG: single = is assignment, not comparison
if (threshold = 50) {
  console.log('Condition ran — threshold is now:', threshold);
}
// threshold was silently changed from 70 to 50
console.log('threshold after if:', threshold);

// CORRECT: use === for comparison
threshold = 70;   // reset
if (threshold === 50) {
  console.log('This should not print');
} else {
  console.log('Correct comparison — threshold is still:', threshold);
}
```

Observe: the first `if (threshold = 50)` always runs because the assignment evaluates to `50` (truthy), and `threshold` is permanently overwritten to `50`.

### Screenshot 1

Take a screenshot showing the console output from `grade.js` including both the grade results and the assignment trap demo. Label this **Lab04-Part1**.

---

## Part 2 — `switch` Statement and Fall-Through

### Step 2.1 — Create `switch_demo.js`

Update your HTML `src` to `switch_demo.js`:

```javascript
// switch Demo — Module 04 Lab

// --- SECTION 1: switch with break (correct) ---
console.log('--- Section 1: switch with break ---');

function getDayName(dayNumber) {
  switch (dayNumber) {
    case 1:
      return 'Monday';
    case 2:
      return 'Tuesday';
    case 3:
      return 'Wednesday';
    case 4:
      return 'Thursday';
    case 5:
      return 'Friday';
    case 6:
      return 'Saturday';
    case 7:
      return 'Sunday';
    default:
      return 'Invalid day number';
  }
}

for (let i = 1; i <= 8; i++) {
  console.log(`Day ${i}: ${getDayName(i)}`);
}

// --- SECTION 2: fall-through (no break) ---
console.log('\n--- Section 2: fall-through WITHOUT break ---');

const code = 2;

switch (code) {
  case 1:
    console.log('case 1 ran');
  case 2:
    console.log('case 2 ran');   // matches here — then falls through
  case 3:
    console.log('case 3 ran');   // also runs
  case 4:
    console.log('case 4 ran');   // also runs
  default:
    console.log('default ran');  // also runs
}

// --- SECTION 3: intentional fall-through (shared handler) ---
console.log('\n--- Section 3: intentional fall-through ---');

function getDaysInMonth(month) {
  switch (month) {
    case 4:
    case 6:
    case 9:
    case 11:
      return 30;
    case 2:
      return 28;   // simplified — ignores leap year
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      return 31;
    default:
      return 'Invalid month';
  }
}

for (let m = 1; m <= 12; m++) {
  console.log(`Month ${m}: ${getDaysInMonth(m)} days`);
}

// --- SECTION 4: switch uses strict equality ---
console.log('\n--- Section 4: switch uses strict equality ---');

const val = '3';   // string

switch (val) {
  case 3:
    console.log('Matched number 3');     // will NOT match
    break;
  case '3':
    console.log('Matched string "3"');   // WILL match
    break;
  default:
    console.log('No match');
}
```

### Step 2.2 — Observe the Fall-Through

Focus on Section 2. `code` is `2`, matching `case 2`. Without `break`, execution falls through to `case 3`, `case 4`, and `default`. Confirm all four lines print.

### Screenshot 2

Take a screenshot of the full console output from `switch_demo.js`. All four sections must be visible. Label this **Lab04-Part2**.

---

## Part 3 — Ternary Operator

### Step 3.1 — Create `ternary.js`

Update your HTML `src` to `ternary.js`:

```javascript
// Ternary Operator Demo — Module 04 Lab

// --- SECTION 1: basic ternary ---
console.log('--- Section 1: basic ternary ---');

const age = 20;
const status = age >= 18 ? 'adult' : 'minor';
console.log('Status:', status);

const score = 78;
const result = score >= 60 ? 'Pass' : 'Fail';
console.log('Result:', result);

// --- SECTION 2: ternary in template literals ---
console.log('\n--- Section 2: ternary in template literals ---');

const items = 3;
console.log(`You have ${items} item${items !== 1 ? 's' : ''} in your cart.`);

const items2 = 1;
console.log(`You have ${items2} item${items2 !== 1 ? 's' : ''} in your cart.`);

const hour = 14;
const greeting = `Good ${hour < 12 ? 'morning' : hour < 18 ? 'afternoon' : 'evening'}!`;
console.log(greeting);

// --- SECTION 3: ternary vs if/else equivalence ---
console.log('\n--- Section 3: ternary vs if/else ---');

const temperature = 32;

// if/else version
let weatherDescription;
if (temperature < 0) {
  weatherDescription = 'freezing';
} else if (temperature < 10) {
  weatherDescription = 'cold';
} else if (temperature < 20) {
  weatherDescription = 'cool';
} else {
  weatherDescription = 'warm';
}
console.log('if/else result:', weatherDescription);

// Ternary is only appropriate for two branches
const tempLabel = temperature < 20 ? 'cold' : 'warm';
console.log('ternary (two branches) result:', tempLabel);

// --- SECTION 4: nested ternary — hard to read, avoid ---
console.log('\n--- Section 4: nested ternary (for awareness only) ---');

const s = 85;
// This is valid but unreadable — use if/else if instead
const g = s >= 90 ? 'A' : s >= 80 ? 'B' : s >= 70 ? 'C' : 'F';
console.log('Nested ternary grade for', s, ':', g);
console.log('(Prefer if/else if for multi-branch logic)');
```

### Screenshot 3

Take a screenshot of the console output from `ternary.js`. Label this **Lab04-Part3**.

---

## Part 4 — Logical Operators and `??`

### Step 4.1 — Create `logical.js`

Update your HTML `src` to `logical.js`:

```javascript
// Logical Operators and ?? — Module 04 Lab

// --- SECTION 1: && and || in conditions ---
console.log('--- Section 1: && and || ---');

const age2 = 22;
const hasTicket = true;
const isVIP = false;

if (age2 >= 18 && hasTicket) {
  console.log('Admission granted');
}

if (isVIP || age2 >= 21) {
  console.log('VIP lounge access');
}

if (!isVIP) {
  console.log('Standard access only');
}

// --- SECTION 2: short-circuit patterns ---
console.log('\n--- Section 2: short-circuit patterns ---');

// Guard pattern
const user1 = null;
const user2 = { name: 'Alice', role: 'admin' };

const name1 = user1 && user1.name;
const name2 = user2 && user2.name;
console.log('user1 name:', name1);   // null
console.log('user2 name:', name2);   // 'Alice'

// Default value pattern with ||
const input1 = '';
const input2 = 'Jordan';

const display1 = input1 || 'Anonymous';
const display2 = input2 || 'Anonymous';
console.log('display1:', display1);   // 'Anonymous'
console.log('display2:', display2);   // 'Jordan'

// --- SECTION 3: ?? vs || with 0 and '' ---
console.log('\n--- Section 3: ?? vs || ---');

const count = 0;
const label = '';
const missing = null;
const notSet = undefined;

console.log('count || 10:', count || 10);       // 10 — 0 is falsy
console.log('count ?? 10:', count ?? 10);       // 0 — ?? ignores falsy (only null/undefined)

console.log('label || "none":', label || 'none');   // 'none' — '' is falsy
console.log('label ?? "none":', label ?? 'none');   // '' — ?? ignores falsy

console.log('missing || "fallback":', missing || 'fallback');   // 'fallback'
console.log('missing ?? "fallback":', missing ?? 'fallback');   // 'fallback'

console.log('notSet || "fallback":', notSet || 'fallback');     // 'fallback'
console.log('notSet ?? "fallback":', notSet ?? 'fallback');     // 'fallback'

// --- SECTION 4: access controller combining all operators ---
console.log('\n--- Section 4: access controller ---');

function checkAccess(user) {
  const isLoggedIn = user !== null && user !== undefined;
  const username = user?.name ?? 'Guest';
  const role = user?.role ?? 'viewer';
  const isAdmin = role === 'admin';
  const canEdit = isLoggedIn && (isAdmin || role === 'editor');

  console.log(`User: ${username} | Role: ${role} | Admin: ${isAdmin} | Can edit: ${canEdit}`);
}

checkAccess(null);
checkAccess({ name: 'Bob', role: 'viewer' });
checkAccess({ name: 'Carol', role: 'editor' });
checkAccess({ name: 'Dave', role: 'admin' });
```

### Step 4.2 — Verify Key Outputs

Confirm:

- `count ?? 10` prints `0` (not `10`) — `??` does not treat `0` as needing a fallback
- `label ?? 'none'` prints `''` (not `'none'`) — `??` does not treat `''` as needing a fallback
- `missing ?? 'fallback'` prints `'fallback'` — `null` does trigger `??`

### Screenshot 4

Take a screenshot of the full console output from `logical.js`. All four sections must be visible. Label this **Lab04-Part4**.

---

## Deliverables

Submit the following to the Module 04 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `grade.js` | Grade calculator with assignment trap demo |
| `switch_demo.js` | switch with/without break, intentional fall-through, strict equality |
| `ternary.js` | Ternary expressions and if/else equivalence |
| `logical.js` | Logical operators, short-circuit, `??` vs `\|\|`, access controller |
| Lab04-Part1.png | Console — grade results and assignment trap |
| Lab04-Part2.png | Console — switch demo including fall-through output |
| Lab04-Part3.png | Console — ternary demo |
| Lab04-Part4.png | Console — logical operators and `??` |

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In Section 2 of Part 2 you observed switch fall-through. In your own words, describe what "fall-through" means and explain one scenario where intentional fall-through is useful rather than a bug.

2. You built a ternary expression that produces singular/plural labels (`item` vs `items`). Explain why a ternary is a better choice than an `if/else` statement for this specific use case. When should you choose `if/else` instead?

3. The `??` operator and the `||` operator both provide fallback values. After Part 4, describe a concrete scenario where using `||` instead of `??` would produce the wrong result. What is the correct operator for that case?

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Fall-through output missing from Part 2 | Used `return` in `getDayName` (returns exit switch) | The fall-through code uses a standalone switch, not the function |
| Assignment trap runs unexpectedly | Working correctly | `if (x = 5)` is always truthy — document this in your reflection |
| `count ?? 10` showing `10` instead of `0` | Possible browser without ES2020 | Use an up-to-date Chrome or Firefox |
| Ternary syntax error | Missing `:` part | Both `?` and `:` are required: `cond ? a : b` |
| `user?.name` syntax unfamiliar | Optional chaining — covered in reading guide section 4 | `?.` accesses property only if object is not null/undefined |
