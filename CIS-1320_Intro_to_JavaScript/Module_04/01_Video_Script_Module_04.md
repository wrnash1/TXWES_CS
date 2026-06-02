# Video Script: CIS-1320 — Introduction to JavaScript

## Module 04 — Control Flow and Conditionals

**Estimated Duration:** 14–17 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for short demos; use VS Code + browser for the switch fall-through demo.
> - [PAUSE] = 2 seconds of silence.
> - The `switch` fall-through demo is high-value — show it with and without `break` explicitly.
> - The assignment-in-condition trap (`if (x = 5)`) always surprises students — run it live.
> - Spend real time on the ternary operator. Students find it intimidating until they see it as just an if/else that returns a value.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 04 | Control Flow and Conditionals | CIS-1320"]**

"Module 04 is about decision-making in code. Every real program needs to take different paths based on conditions — if a user is logged in, show the dashboard; if not, show the login page. If a score is 90 or above, the grade is A; if it is 80 to 89, it is a B. These decisions are controlled by JavaScript's conditional structures: `if/else`, `switch`, the ternary operator, and logical operators.

You already know the truthy and falsy values from Module 03. Module 04 is where they actually get used — every `if` statement and `while` loop evaluates its condition using those rules. Let us go through each structure."

---

## [01:00 – 05:00] Part 1 — `if`, `else if`, and `else`

**[SHOW SLIDE: "if / else if / else"]**

"The `if` statement is the foundation of conditional logic. The syntax is straightforward:

```javascript
if (condition) {
  // runs when condition is truthy
}
```

The condition can be any expression. JavaScript converts it to a boolean using the truthy/falsy rules you learned in Module 03.

**[DEMO]**

```javascript
const score = 85;

if (score >= 90) {
  console.log('A');
} else if (score >= 80) {
  console.log('B');
} else if (score >= 70) {
  console.log('C');
} else if (score >= 60) {
  console.log('D');
} else {
  console.log('F');
}
```

With `score` at `85`, the engine checks the conditions in order. `85 >= 90` is `false` — skip. `85 >= 80` is `true` — run the `B` block and stop. It never even reaches the `C`, `D`, or `F` conditions. This is important: only the **first matching branch** runs in an `if/else if/else` chain.

[PAUSE]

A common mistake is to write overlapping conditions in the wrong order:

```javascript
// Wrong order — if score is 95, this prints 'C or above' not 'A'
if (score >= 60) {
  console.log('C or above');    // always matches first for scores 60+
} else if (score >= 80) {
  console.log('B or above');    // never reached for 60-79 range
} else if (score >= 90) {
  console.log('A');             // never reached at all
}
```

Always order your `else if` conditions from most specific to least specific when using `>=`.

[PAUSE]

The critical exam trap: **assignment instead of comparison in a condition.**

```javascript
let x = 10;

if (x = 5) {              // single = is assignment, not comparison
  console.log('ran');     // this always runs — 5 is truthy
}

console.log(x);           // 5 — x was reassigned!
```

`x = 5` assigns `5` to `x` and evaluates to `5`. Since `5` is truthy, the if block always runs. This is a real bug that static analysis tools like ESLint will catch. Always use `===` in conditions."

---

## [05:00 – 08:30] Part 2 — `switch` Statement

**[SHOW SLIDE: "switch: Match One Value Against Multiple Cases"]**

"The `switch` statement evaluates one expression and compares it against a series of `case` labels using strict equality. It is an alternative to a long chain of `if/else if` when you are testing the same variable against many specific values.

**[DEMO — VS Code + browser]**

```javascript
const day = 3;

switch (day) {
  case 1:
    console.log('Monday');
    break;
  case 2:
    console.log('Tuesday');
    break;
  case 3:
    console.log('Wednesday');
    break;
  case 4:
    console.log('Thursday');
    break;
  case 5:
    console.log('Friday');
    break;
  default:
    console.log('Weekend');
}
```

`day` is `3`, so the engine matches `case 3`, prints `'Wednesday'`, hits `break`, and exits the switch. The `break` statement is essential — it tells the engine to exit the switch block after the matched case.

[PAUSE]

**What happens without `break`?**

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
    console.log('Thursday');    // also runs — no break!
  case 5:
    console.log('Friday');      // also runs — no break!
  default:
    console.log('Weekend');     // also runs — no break!
}
```

Without `break`, execution **falls through** to every subsequent case. `day = 3` matches `case 3` and prints `'Wednesday'`, then continues into `case 4`, `case 5`, and `default` — printing them all. This fall-through behavior is one of the most tested JSE exam topics. Know it cold.

[PAUSE]

The `default` case runs when no `case` label matches. It is optional, but you should include it to handle unexpected values. It can go anywhere in the switch, but convention places it last.

[PAUSE]

One legitimate use of intentional fall-through: when multiple cases should execute the same code:

```javascript
const month = 4;

switch (month) {
  case 4:
  case 6:
  case 9:
  case 11:
    console.log('30 days');
    break;
  case 2:
    console.log('28 or 29 days');
    break;
  default:
    console.log('31 days');
}
```

Cases 4, 6, 9, and 11 all fall through to the same code. This is intentional and readable.

[PAUSE]

One more thing: `switch` uses strict equality (`===`) for case matching. This means `switch ('3')` will not match `case 3`. The types must match."

---

## [08:30 – 11:00] Part 3 — Ternary Operator

**[SHOW SLIDE: "Ternary Operator: if/else in an Expression"]**

"The ternary operator is the only three-operand operator in JavaScript. Its syntax is:

```text
condition ? valueIfTrue : valueIfFalse
```

Think of it as an if/else that returns a value instead of executing statements. It is an **expression**, which means it produces a value that can be assigned to a variable or passed as an argument.

**[DEMO]**

```javascript
const score = 85;

// if/else version
let grade;
if (score >= 90) {
  grade = 'A';
} else {
  grade = 'B or below';
}

// ternary version — same logic, one line
const gradeT = score >= 90 ? 'A' : 'B or below';

console.log(grade);    // 'B or below'
console.log(gradeT);   // 'B or below'
```

Both produce the same result. The ternary version is concise and readable when the branches are simple values.

[PAUSE]

You can also use the ternary directly in a `console.log` or a template literal:

```javascript
const age = 20;
console.log(`You are ${age >= 18 ? 'an adult' : 'a minor'}.`);

const price = 150;
const label = price > 100 ? 'Premium' : 'Standard';
console.log(label);   // 'Premium'
```

[PAUSE]

Avoid **nested ternaries** — ternaries inside other ternaries. They are valid syntax but nearly impossible to read:

```javascript
// Avoid this
const result = score >= 90 ? 'A' : score >= 80 ? 'B' : score >= 70 ? 'C' : 'F';
```

For multi-branch logic like a grade scale, use `if/else if/else`. The ternary shines for simple two-outcome decisions."

---

## [11:00 – 13:30] Part 4 — Logical Operators in Conditions

**[SHOW SLIDE: "Combining Conditions with && and ||"]**

"You often need to check multiple conditions at once. Logical operators let you combine conditions into a single expression.

```javascript
const age = 25;
const hasID = true;

if (age >= 21 && hasID) {
  console.log('Entry allowed');
}

const isWeekend = false;
const isHoliday = true;

if (isWeekend || isHoliday) {
  console.log('Day off!');
}
```

`&&` requires both conditions to be truthy. `||` requires at least one.

[PAUSE]

Remember from Module 03: `&&` and `||` do not always return booleans — they return one of the operands. This enables the **guard pattern** and the **default value pattern**:

```javascript
// Guard — only access .name if user exists
const user = null;
const name = user && user.name;
console.log(name);   // null — user is falsy, short-circuit

// Default value
const input = '';
const display = input || 'Enter your name';
console.log(display);   // 'Enter your name' — input is falsy
```

[PAUSE]

ES2020 introduced the **nullish coalescing operator** `??`. It is similar to `||` but only treats `null` and `undefined` as falsy — not `0`, `''`, or `false`:

```javascript
const count = 0;

console.log(count || 'no count');   // 'no count' — 0 is falsy with ||
console.log(count ?? 'no count');   // 0 — ?? only triggers on null/undefined
```

`??` is useful when `0` or `''` are valid values you do not want to replace with a default. The exam may test this — know the distinction from `||`."

---

## [13:30 – 15:30] Closing — Lab Preview

**[SHOW SLIDE: "Module 04 Lab Preview"]**

"The Module 04 lab has four parts.

Part 1 builds a grade calculator using `if/else if/else`. You will evaluate numeric scores and output letter grades, then intentionally introduce and observe the assignment-in-condition trap.

Part 2 implements a day-of-week switch with and without `break`, so you can observe fall-through first-hand.

Part 3 rewrites if/else logic as ternary expressions and tests nested ternaries to see why they should be avoided.

Part 4 builds a user access checker combining `&&`, `||`, `!`, and `??` to control what content is displayed.

Read the reading guide before the lab — especially the fall-through and assignment-trap sections. Those appear on the quiz. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 04 — Control Flow and Conditionals]**

---

## Additional Resources

- [MDN — if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) — full reference with truthy/falsy behavior
- [MDN — switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch) — fall-through examples and best practices
- [MDN — Conditional (ternary) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)
- [MDN — Nullish coalescing operator (??)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
- [Eloquent JavaScript — Chapter 2: Program Structure](https://eloquentjavascript.net/02_program_structure.html)
