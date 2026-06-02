# Video Script: CIS-1320 — Introduction to JavaScript

## Module 05 — Loops and Iteration

**Estimated Duration:** 15–18 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - The `<` vs `<=` off-by-one demo is the highest-value exam content — write the iteration table on screen.
> - For the infinite loop demo, show it briefly in the console, then immediately close the tab to demonstrate the browser freeze — emphasize "this is why we check conditions carefully."
> - The `for...of` vs `for...in` distinction surprises students — emphasize that `for...in` gives string keys, not values.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 05 | Loops and Iteration | CIS-1320"]**

"Module 05 is about repetition. Real programs rarely execute each line of code exactly once — they process all items in a shopping cart, validate each field in a form, retry a failed request, count through a range of numbers. Loops are the tool for all of that.

JavaScript has three traditional loop constructs — `for`, `while`, and `do-while` — plus two modern iteration forms: `for...of` and `for...in`. Each is suited to different situations. We will cover all five, plus `break` and `continue` for controlling loop flow. Let us start with the most common one."

---

## [01:00 – 05:30] Part 1 — The `for` Loop

**[SHOW SLIDE: "The for Loop"]**

"The `for` loop is the most commonly used loop in JavaScript. Its header has three parts separated by semicolons:

```javascript
for (initialization; condition; update) {
  // body — runs on each iteration
}
```

The **initialization** runs once before the loop starts. The **condition** is checked before every iteration — if it is truthy, the body runs; if it is falsy, the loop ends. The **update** runs after every iteration.

**[DEMO]**

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

The engine executes this as:

1. `let i = 0` — initialize
2. `0 < 5` → `true` — run body, prints `0`, then `i++` → `i = 1`
3. `1 < 5` → `true` — run body, prints `1`, then `i++` → `i = 2`
4. `2 < 5` → `true` — run body, prints `2`, then `i++` → `i = 3`
5. `3 < 5` → `true` — run body, prints `3`, then `i++` → `i = 4`
6. `4 < 5` → `true` — run body, prints `4`, then `i++` → `i = 5`
7. `5 < 5` → `false` — loop ends

Output: `0`, `1`, `2`, `3`, `4` — five values.

[PAUSE]

**The most-tested JSE exam concept in this module: `<` vs `<=`.**

```javascript
for (let i = 0; i < 5; i++) {}   // runs 5 times: i = 0,1,2,3,4
for (let i = 0; i <= 5; i++) {}  // runs 6 times: i = 0,1,2,3,4,5
for (let i = 1; i <= 5; i++) {}  // runs 5 times: i = 1,2,3,4,5
for (let i = 1; i < 5; i++) {}   // runs 4 times: i = 1,2,3,4
```

Before you write a `for` loop, ask two questions: where does my counter start — at `0` or at `1`? And do I want to include the last value — `<` or `<=`? Getting this wrong produces off-by-one errors.

[PAUSE]

**[DEMO — counting down]**

```javascript
for (let i = 10; i >= 1; i--) {
  console.log(i);
}
console.log('Liftoff!');
```

You can count down by starting high and using `i--`. The condition `i >= 1` keeps the loop running until `i` reaches `0`.

[PAUSE]

**[DEMO — iterating an array]**

```javascript
const fruits = ['apple', 'banana', 'cherry'];

for (let i = 0; i < fruits.length; i++) {
  console.log(i, fruits[i]);
}
```

Using `i < fruits.length` is the standard idiom for iterating an array by index. Never hardcode the length — use `.length` so the loop adapts if the array changes."

---

## [05:30 – 08:30] Part 2 — `while` and `do-while`

**[SHOW SLIDE: "`while` and `do-while`"]**

"The `while` loop checks its condition before each iteration:

```javascript
while (condition) {
  // runs while condition is truthy
}
```

If the condition is initially false, the body never runs. Use `while` when you do not know in advance how many iterations you need.

**[DEMO]**

```javascript
let attempts = 0;
const MAX_ATTEMPTS = 3;

while (attempts < MAX_ATTEMPTS) {
  console.log('Attempt', attempts + 1);
  attempts++;
}
console.log('Done after', attempts, 'attempts');
```

[PAUSE]

The critical mistake with `while` is forgetting the update. Without `attempts++`, `attempts` stays at `0` forever and you get an infinite loop:

```javascript
let x = 0;
while (x < 5) {
  console.log(x);
  // missing x++ — infinite loop!
}
```

**[BRIEF DEMO — show in console, then immediately close or Ctrl+C]**

The browser tab freezes when you run this. Always make sure your while loop modifies the variable the condition depends on.

[PAUSE]

The `do-while` loop runs the body first, then checks the condition:

```javascript
do {
  // body runs at least once
} while (condition);
```

Even if the condition starts as `false`, the body runs once before the check:

```javascript
let count = 10;

do {
  console.log('count is', count);
  count++;
} while (count < 5);

// Output: 'count is 10' — runs once, then 10 < 5 is false, loop ends
```

`do-while` is useful when you need to perform an action at least once and then decide whether to repeat — like showing a dialog and asking the user to try again."

---

## [08:30 – 11:00] Part 3 — `break` and `continue`

**[SHOW SLIDE: "`break` and `continue`"]**

"`break` and `continue` control loop flow.

**`break`** immediately exits the entire loop:

**[DEMO]**

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
// Output: 0, 1, 2, 3, 4 — stops before printing 5
```

When `i === 5`, `break` exits the loop immediately. The loop never reaches `6`, `7`, `8`, or `9`. This is commonly used to search for a value — once found, stop searching.

[PAUSE]

**`continue`** skips the rest of the current iteration and jumps to the next one:

```javascript
for (let i = 0; i < 10; i++) {
  if (i % 2 !== 0) {
    continue;
  }
  console.log(i);
}
// Output: 0, 2, 4, 6, 8 — odd numbers are skipped
```

When `i` is odd, `continue` skips the `console.log` for that iteration and jumps back to `i++`, then the condition check. The loop continues — only that one iteration is skipped.

[PAUSE]

`break` exits the loop entirely. `continue` skips one iteration. Know this distinction for the exam.

**Important:** `break` and `continue` only affect the **innermost** loop they are in. In nested loops, `break` exits only the inner loop, not the outer one:

```javascript
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) break;           // exits inner loop only
    console.log(i, j);
  }
}
// Output: 0 0, 1 0, 2 0 — inner loop always stops at j=1
```"

---

## [11:00 – 14:00] Part 4 — `for...of` and `for...in`

**[SHOW SLIDE: "Modern Iteration: for...of and for...in"]**

"ES6 introduced two new loop forms that are more convenient for specific use cases.

**`for...of`** iterates over the **values** of any iterable — arrays, strings, and others:

**[DEMO]**

```javascript
const colors = ['red', 'green', 'blue'];

for (const color of colors) {
  console.log(color);
}
// Output: red, green, blue
```

No index variable needed. `color` takes the value of each element directly.

```javascript
const word = 'hello';

for (const char of word) {
  console.log(char);
}
// Output: h, e, l, l, o
```

`for...of` works on strings too — it iterates each character.

[PAUSE]

**`for...in`** iterates over the **keys** (property names) of an object:

```javascript
const person = { name: 'Alice', age: 25, role: 'student' };

for (const key in person) {
  console.log(key, ':', person[key]);
}
// Output: name : Alice, age : 25, role : student
```

`key` holds each property name as a string. Use `person[key]` to access the value.

[PAUSE]

**The critical trap:** do not use `for...in` on arrays. It gives you the **index as a string**, not the value, and it can include inherited properties:

```javascript
const arr = [10, 20, 30];

for (const i in arr) {
  console.log(i, typeof i);   // '0' string, '1' string, '2' string
}
```

The indexes `0`, `1`, `2` come back as strings `'0'`, `'1'`, `'2'`. Use `for...of` for arrays, `for...in` for objects. This distinction appears on the JSE exam."

---

## [14:00 – 16:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 05 Lab Preview"]**

"The Module 05 lab has four parts.

Part 1 uses `for` loops — counting up, counting down, iterating arrays by index, and demonstrating the `<` vs `<=` off-by-one difference with a comparison table.

Part 2 uses `while` and `do-while` — including an intentional infinite loop that you will interrupt, then correct.

Part 3 uses `break` and `continue` — searching for a value in an array, filtering odd numbers, and demonstrating `break` in nested loops.

Part 4 uses `for...of` and `for...in` — iterating array values, string characters, and object key-value pairs — and demonstrates why `for...in` on arrays produces string keys.

The quiz focuses heavily on off-by-one errors and the `break` vs `continue` distinction. Read the reading guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 05 — Loops and Iteration]**

---

## Additional Resources

- [MDN — for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
- [MDN — while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
- [MDN — do...while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
- [MDN — for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
- [MDN — for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
- [Eloquent JavaScript — Chapter 2: Program Structure](https://eloquentjavascript.net/02_program_structure.html)
