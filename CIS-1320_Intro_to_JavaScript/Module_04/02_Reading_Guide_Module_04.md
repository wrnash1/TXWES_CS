# Reading Guide: Module 04 — Control Flow and Conditionals

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Control flow is what transforms a list of instructions into a program that responds to conditions. Every useful JavaScript program makes decisions: is the user authenticated? Is the score high enough? Did the network request succeed? The structures in this module — `if/else`, `switch`, and the ternary operator — are the tools that implement those decisions. Logical operators let you combine conditions. The truthy/falsy rules from Module 03 are what make every condition evaluate correctly.

---

## 1. The `if / else if / else` Statement

### Basic Syntax

```javascript
if (condition) {
  // executes when condition is truthy
} else if (anotherCondition) {
  // executes when condition is falsy AND anotherCondition is truthy
} else {
  // executes when all conditions above are falsy
}
```

Only the **first matching branch** executes. Once a truthy condition is found, its block runs and the engine skips all remaining `else if` and `else` clauses.

### Grade Calculator Example

```javascript
const score = 85;

if (score >= 90) {
  console.log('A');
} else if (score >= 80) {
  console.log('B');       // prints this — 85 >= 80 is true
} else if (score >= 70) {
  console.log('C');       // skipped
} else if (score >= 60) {
  console.log('D');       // skipped
} else {
  console.log('F');       // skipped
}
```

### Ordering Matters

When using `>=` comparisons, order from most specific (highest threshold) to least specific (lowest threshold). Reversing the order causes all scores to match the first branch:

```javascript
// BUG: wrong order — every score >= 60 prints 'D or above' and stops
if (score >= 60) {
  console.log('D or above');   // score 95 matches here — never reaches 'A'
} else if (score >= 80) {
  console.log('B or above');   // unreachable for scores 60–79
} else if (score >= 90) {
  console.log('A');            // unreachable entirely
}
```

### The Assignment-in-Condition Trap

Using `=` (assignment) instead of `===` (comparison) in a condition is a classic bug:

```javascript
let x = 10;

if (x = 5) {           // assignment: x becomes 5, evaluates to 5 (truthy)
  console.log('ran');  // always runs because 5 is truthy
}

console.log(x);        // 5 — x was unintentionally overwritten
```

The assignment `x = 5` evaluates to `5`, which is truthy, so the block always executes regardless of `x`'s original value. This is why ESLint warns on assignments inside conditions. Always use `===` for comparisons.

### Single-Statement Shorthand (Avoid)

JavaScript allows omitting braces for single-statement if blocks:

```javascript
if (score >= 90) console.log('A');   // valid syntax
```

This is error-prone when the code is later modified. Always use braces `{}`.

---

## 2. The `switch` Statement

### Syntax

```javascript
switch (expression) {
  case value1:
    // code for value1
    break;
  case value2:
    // code for value2
    break;
  default:
    // code when no case matches
}
```

`switch` evaluates `expression` once, then compares the result against each `case` label using **strict equality (`===`)**. The first matching case executes.

### `switch` with Strict Equality

Because `switch` uses `===`, types must match:

```javascript
const n = '3';   // string

switch (n) {
  case 3:
    console.log('number 3');    // does NOT match — type mismatch
    break;
  case '3':
    console.log('string 3');    // matches — same type and value
    break;
}
```

### Fall-Through — The Most Tested `switch` Trap

Without `break`, execution **falls through** to the next case regardless of whether it matches:

```javascript
const day = 3;

switch (day) {
  case 1:
    console.log('Monday');
  case 2:
    console.log('Tuesday');
  case 3:
    console.log('Wednesday');   // matches here
  case 4:
    console.log('Thursday');    // falls through — no break
  case 5:
    console.log('Friday');      // falls through — no break
  default:
    console.log('Weekend');     // falls through — no break
}

// Output: Wednesday, Thursday, Friday, Weekend
```

With `break` after each case, only the matching case runs:

```javascript
switch (day) {
  case 3:
    console.log('Wednesday');
    break;               // exits switch
  case 4:
    console.log('Thursday');
    break;
}
// Output: Wednesday
```

### Intentional Fall-Through

Fall-through is occasionally useful when multiple values share the same handler:

```javascript
const month = 6;

switch (month) {
  case 4:
  case 6:
  case 9:
  case 11:
    console.log('30 days');   // months 4, 6, 9, 11 all fall through here
    break;
  case 2:
    console.log('28 or 29 days');
    break;
  default:
    console.log('31 days');
}
```

### The `default` Case

`default` runs when no `case` label matches. It is optional but should always be included to handle unexpected input. It can appear anywhere in the switch, but convention places it last.

```javascript
const status = 'unknown';

switch (status) {
  case 'active':
    console.log('User is active');
    break;
  case 'inactive':
    console.log('User is inactive');
    break;
  default:
    console.log('Unknown status:', status);
}
```

---

## 3. The Ternary Operator

### Ternary Syntax

```text
condition ? valueIfTrue : valueIfFalse
```

The ternary operator is the only JavaScript operator with three operands. It is an **expression** (produces a value), unlike `if` which is a statement (performs an action). Because it is an expression, it can appear on the right side of an assignment or inside a template literal.

### Basic Usage

```javascript
const age = 20;
const status = age >= 18 ? 'adult' : 'minor';
console.log(status);   // 'adult'
```

Equivalent `if/else`:

```javascript
let status;
if (age >= 18) {
  status = 'adult';
} else {
  status = 'minor';
}
```

Both produce the same result. Use the ternary when the branches are simple values — it communicates "this is a value-producing decision."

### Ternary in Template Literals

```javascript
const score = 78;
console.log(`Grade: ${score >= 60 ? 'Pass' : 'Fail'}`);   // Grade: Pass

const items = 1;
console.log(`${items} item${items !== 1 ? 's' : ''} in cart`);   // 1 item in cart
```

### Nested Ternaries — Avoid

Ternaries can be nested, but the result is very hard to read:

```javascript
// Avoid
const grade = score >= 90 ? 'A' : score >= 80 ? 'B' : score >= 70 ? 'C' : 'F';
```

For multi-branch logic use `if/else if/else`. The ternary is appropriate for two-branch decisions only.

---

## 4. Logical Operators in Conditions

### Combining Conditions

```javascript
const age = 25;
const hasID = true;

if (age >= 21 && hasID) {
  console.log('Entry allowed');    // both conditions truthy
}

const isWeekend = false;
const isHoliday = true;

if (isWeekend || isHoliday) {
  console.log('Day off!');         // at least one is truthy
}

const isLoggedIn = true;
if (!isLoggedIn) {
  console.log('Please log in');    // negation — runs when NOT logged in
}
```

### Short-Circuit Patterns

`&&` and `||` return operands, not just booleans. This enables concise patterns:

```javascript
// Guard pattern — safe property access
const user = null;
const name = user && user.name;    // null (short-circuits at user)

const user2 = { name: 'Alice' };
const name2 = user2 && user2.name; // 'Alice'

// Default value pattern
const input = '';
const display = input || 'Placeholder text';   // 'Placeholder text'

const input2 = 'Jordan';
const display2 = input2 || 'Placeholder text'; // 'Jordan'
```

### Nullish Coalescing Operator `??` (ES2020)

`??` returns the right operand only when the left operand is `null` or `undefined`. Unlike `||`, it does not treat `0`, `''`, or `false` as triggering the fallback:

```javascript
const count = 0;
console.log(count || 10);    // 10 — 0 is falsy with ||
console.log(count ?? 10);    // 0 — ?? only triggers on null/undefined

const label = '';
console.log(label || 'default');   // 'default' — '' is falsy with ||
console.log(label ?? 'default');   // '' — ?? only triggers on null/undefined

const value = null;
console.log(value ?? 'fallback');  // 'fallback' — null triggers ??

const value2 = undefined;
console.log(value2 ?? 'fallback'); // 'fallback' — undefined triggers ??
```

Use `??` when `0`, `''`, and `false` are meaningful values that should not be replaced by a default. Use `||` when any falsy value should trigger the fallback.

---

## 5. Truthy and Falsy in Conditions

Every `if` condition, `while` condition, and `switch` expression relies on JavaScript's truthiness rules. These were introduced in Module 03. Here they are applied directly:

```javascript
const username = '';

if (username) {
  console.log('Welcome,', username);
} else {
  console.log('Please enter a username');   // '' is falsy — runs this
}

const items = [];

if (items.length) {
  console.log('Cart has items');
} else {
  console.log('Cart is empty');             // items.length is 0 — falsy
}

const response = null;

if (response) {
  console.log('Got a response');
} else {
  console.log('No response yet');           // null is falsy — runs this
}
```

Note: `items` itself would be truthy (an empty array is truthy), but `items.length` is `0` which is falsy. Checking `.length` is the correct pattern for testing whether an array has any elements.

---

## 6. Choosing Between `if/else` and `switch`

| Situation | Prefer |
|---|---|
| Two branches (yes/no) | `if/else` or ternary |
| Three or more branches based on ranges (`>`, `<`, `>=`) | `if/else if/else` |
| Three or more branches based on exact values | `switch` |
| Assigning a value based on a condition | Ternary |
| Many values mapping to the same code | `switch` with intentional fall-through |

---

## 7. JSE Certification Exam Tips

1. **`switch` fall-through without `break`** — execution continues into subsequent cases. Without `break`, all cases from the match to the end (or the next `break`) run.

2. **`switch` uses `===` for matching** — `switch ('3')` does not match `case 3`. Types must match.

3. **Assignment in condition** — `if (x = 5)` always runs because the assignment evaluates to `5` (truthy). This is a bug pattern, not a comparison.

4. **`else if` is not a separate keyword** — it is an `else` followed by another `if`. The engine only evaluates conditions after a false one.

5. **Only the first matching branch runs** in `if/else if/else`. Once a true condition is found, all remaining branches are skipped.

6. **Ternary is an expression** — it produces a value and can appear inside assignments, function arguments, and template literals. `if` is a statement and cannot.

7. **`??` vs `||`** — `??` only triggers on `null`/`undefined`. `||` triggers on any falsy value (`0`, `''`, `false`, `null`, `undefined`, `NaN`).

8. **`default` in switch** — if no case matches and there is no `default`, nothing runs. The switch is silently skipped.

---

## 8. Study Checklist

- [ ] Watch the Module 04 video lecture by Professor Nash.
- [ ] Read Chapter 2 (Program Structure) of [Eloquent JavaScript](https://eloquentjavascript.net/02_program_structure.html).
- [ ] Read [MDN — switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch) — especially the fall-through section.
- [ ] Open the browser console and run the fall-through demo from Section 2 with and without `break`.
- [ ] Reproduce the assignment-in-condition bug from Section 1 and explain what happens.
- [ ] Write a ternary expression for three different two-branch decisions.
- [ ] Run the `??` vs `||` examples from Section 4 with `count = 0`.
- [ ] Complete the Module 04 Lab.
- [ ] Complete the Module 04 Quiz.
