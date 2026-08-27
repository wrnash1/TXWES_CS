# Reading Guide: Module 05 — Loops and Iteration

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Loops give a program the ability to repeat an action. Without loops, every shopping cart item, every form field, every row in a table would require its own line of code. JavaScript provides five loop constructs: `for`, `while`, `do-while`, `for...of`, and `for...in`. Each solves a specific class of repetition problem. Choosing the right one — and writing its condition correctly — is what separates working code from code that either skips an iteration or runs forever.

---

## 1. The `for` Loop

### Syntax

```javascript
for (initialization; condition; update) {
  // body — executes on each iteration
}
```

The three header expressions are separated by semicolons:

- **Initialization** — runs once before the loop begins. Typically declares and sets the counter variable.
- **Condition** — evaluated before each iteration. If truthy, the body runs. If falsy, the loop ends.
- **Update** — runs after each iteration. Typically increments or decrements the counter.

### Step-by-Step Execution

```javascript
for (let i = 0; i < 3; i++) {
  console.log(i);
}
// Output: 0, 1, 2
```

The engine executes this sequence:

1. `let i = 0` — initialization (once)
2. `0 < 3` → `true` — run body (prints `0`), then `i++` → `i = 1`
3. `1 < 3` → `true` — run body (prints `1`), then `i++` → `i = 2`
4. `2 < 3` → `true` — run body (prints `2`), then `i++` → `i = 3`
5. `3 < 3` → `false` — loop ends

### `<` vs `<=` — Off-by-One Errors

The most common `for` loop mistake is choosing the wrong comparison operator. Before writing a loop, decide: where does the counter start, and do I want to include the last value?

| Loop | Runs | Values of `i` |
|---|---|---|
| `for (let i = 0; i < 5; i++)` | 5 times | 0, 1, 2, 3, 4 |
| `for (let i = 0; i <= 5; i++)` | 6 times | 0, 1, 2, 3, 4, 5 |
| `for (let i = 1; i <= 5; i++)` | 5 times | 1, 2, 3, 4, 5 |
| `for (let i = 1; i < 5; i++)` | 4 times | 1, 2, 3, 4 |

Array indices start at `0` and end at `length - 1`. The standard pattern for iterating an array is `i < array.length` (not `<=`):

```javascript
const fruits = ['apple', 'banana', 'cherry'];

for (let i = 0; i < fruits.length; i++) {
  console.log(i, fruits[i]);
}
// Output: 0 apple, 1 banana, 2 cherry
```

Using `i <= fruits.length` would access index `3`, which is `undefined` — a subtle off-by-one bug. Always use `.length` instead of a hardcoded number so the loop adapts automatically when the array changes.

### Counting Down

The `for` loop can count in any direction. Countdown loops use a high starting value and `i--`:

```javascript
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
console.log('Done');
// Output: 5, 4, 3, 2, 1, Done
```

The condition `i >= 1` keeps the loop running while `i` is positive. When `i` reaches `0`, the condition is false and the loop exits.

---

## 2. The `while` Loop

### `while` Syntax

```javascript
while (condition) {
  // body — executes while condition is truthy
}
```

The `while` loop checks its condition **before** each iteration. If the condition is false on the first check, the body never runs.

### When to Use `while`

Use `while` when you do not know in advance how many iterations are needed:

```javascript
let attempts = 0;
const MAX = 3;

while (attempts < MAX) {
  console.log('Attempt', attempts + 1);
  attempts++;
}
console.log('Done after', attempts, 'attempts');
// Output: Attempt 1, Attempt 2, Attempt 3, Done after 3 attempts
```

### The Infinite Loop Trap

The critical mistake with `while` is forgetting to modify the variable the condition depends on:

```javascript
let x = 0;
while (x < 5) {
  console.log(x);
  // missing x++ — x never changes, condition never becomes false
}
// This freezes the browser tab
```

Every `while` loop must eventually make its condition false. Always verify: does the loop body change the variable in the condition?

### The `while` Loop Can Run Zero Times

If the condition is initially false, the body is never executed:

```javascript
let n = 10;
while (n < 5) {
  console.log('This will never print');
}
console.log('n is', n);   // n is 10 — loop was skipped entirely
```

This is intentional behavior — `while` makes no guarantee of running at all.

---

## 3. The `do-while` Loop

### `do-while` Syntax

```javascript
do {
  // body — always runs at least once
} while (condition);
```

The `do-while` loop executes the body **first**, then checks the condition. Even if the condition is initially false, the body runs once before the check occurs.

### The One Guaranteed Execution

```javascript
let count = 10;

do {
  console.log('count is', count);
  count++;
} while (count < 5);

// Output: count is 10
// (10 < 5 is false — loop ends after the first run)
```

Compare with the equivalent `while` loop:

```javascript
let count = 10;

while (count < 5) {
  console.log('count is', count);   // never runs
  count++;
}
// No output — condition was false before the first check
```

### When to Use `do-while`

Use `do-while` when you need to perform an action at least once and then repeat based on a condition — for example, showing a form validation message before checking whether to resubmit, or running a menu and asking whether to continue.

---

## 4. `break` and `continue`

### `break` — Exit the Loop Immediately

`break` terminates the enclosing loop and transfers control to the statement after the loop:

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
// Output: 0, 1, 2, 3, 4
// (loop exits when i reaches 5 — 5 is never printed)
```

`break` is commonly used for search patterns: iterate until the target is found, then stop.

### `continue` — Skip One Iteration

`continue` skips the rest of the current iteration's body and jumps to the update expression (in a `for` loop) or back to the condition check (in `while`/`do-while`):

```javascript
for (let i = 0; i < 10; i++) {
  if (i % 2 !== 0) {
    continue;
  }
  console.log(i);
}
// Output: 0, 2, 4, 6, 8
// (odd numbers: continue skips console.log and goes to i++)
```

### `break` vs `continue` — Comparison

| Keyword | Effect | What runs next |
|---|---|---|
| `break` | Exits the loop entirely | First statement after the loop |
| `continue` | Skips the rest of this iteration | Update expression (`for`) or condition check (`while`) |

### Nested Loops — `break` Only Exits the Innermost Loop

`break` and `continue` only affect the loop they are directly inside. In nested loops, `break` exits the inner loop but the outer loop continues:

```javascript
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) {
      break;   // exits inner loop only
    }
    console.log(i, j);
  }
}
// Output: 0 0, 1 0, 2 0
// (inner loop always stops when j === 1; outer loop runs 3 times)
```

If you need to break out of an outer loop, a common pattern is to use a boolean flag variable that the outer loop checks.

---

## 5. `for...of` — Iterate Values of an Iterable

### `for...of` Syntax

```javascript
for (const element of iterable) {
  // element takes each value in turn
}
```

`for...of` works on any **iterable** — objects that can produce a sequence of values. Arrays and strings are the most common iterables in introductory JavaScript.

### `for...of` on Arrays

```javascript
const colors = ['red', 'green', 'blue'];

for (const color of colors) {
  console.log(color);
}
// Output: red, green, blue
```

No index variable is needed. `color` takes the value of each element directly. Use `const` when you do not need to reassign the variable inside the loop.

### `for...of` on Strings

`for...of` iterates each character of a string individually:

```javascript
const word = 'hello';

for (const char of word) {
  console.log(char);
}
// Output: h, e, l, l, o
```

### `for...of` vs Traditional `for` on Arrays

Both of these produce the same values:

```javascript
const nums = [10, 20, 30];

// Traditional for — gives access to index i
for (let i = 0; i < nums.length; i++) {
  console.log(i, nums[i]);   // 0 10, 1 20, 2 30
}

// for...of — gives value directly, no index available
for (const n of nums) {
  console.log(n);            // 10, 20, 30
}
```

Choose `for...of` when you only need the values. Choose the traditional `for` loop when you also need the index.

---

## 6. `for...in` — Iterate Keys of an Object

### `for...in` Syntax

```javascript
for (const key in object) {
  // key takes each property name as a string
}
```

`for...in` iterates the **enumerable property names** (keys) of an object:

```javascript
const person = { name: 'Alice', age: 25, role: 'student' };

for (const key in person) {
  console.log(key, ':', person[key]);
}
// Output:
// name : Alice
// age : 25
// role : student
```

`key` holds each property name as a string. Use bracket notation `person[key]` to access the corresponding value.

### The Critical Trap: Do Not Use `for...in` on Arrays

Using `for...in` on an array gives you the **array indices as strings**, not the values:

```javascript
const arr = [10, 20, 30];

for (const i in arr) {
  console.log(i, typeof i);
}
// Output:
// 0 string
// 1 string
// 2 string
```

The indices `0`, `1`, `2` are returned as the strings `'0'`, `'1'`, `'2'`. Arithmetic with string indices may produce unexpected results, and the loop can also pick up non-index properties if any have been added to the array object.

### `for...of` vs `for...in` — Summary

| Loop form | Use with | Gives you |
|---|---|---|
| `for...of` | Arrays, strings, iterables | Values directly (`'red'`, `'green'`) |
| `for...in` | Plain objects | String property names (`'name'`, `'age'`) |
| `for...in` on array | Avoid | String index keys (`'0'`, `'1'`, `'2'`) |

Rule: use `for...of` for arrays and strings; use `for...in` for plain objects.

---

## 7. Choosing the Right Loop

| Situation | Best Loop |
|---|---|
| Known number of iterations, counter needed | `for` |
| Iterating an array by index (index value needed) | `for` |
| Unknown number of iterations, condition-driven | `while` |
| Must execute at least once before checking | `do-while` |
| Iterating values of an array or string | `for...of` |
| Iterating keys of a plain object | `for...in` |
| Search: stop when target is found | `for` or `for...of` with `break` |
| Filter: skip certain iterations | Any loop with `continue` |

---

## 8. Infinite Loops — Causes and Prevention

An infinite loop runs without end, freezing the browser tab. The three most common causes:

| Cause | Example | Fix |
|---|---|---|
| Missing update in `while` | `while (x < 5) { /* no x++ */ }` | Add `x++` inside the body |
| Condition never reaches `false` | `while (true) { }` without `break` | Ensure a `break` or exit condition exists |
| Off-direction update | `for (let i = 1; i > 0; i++)` | Match the update direction to the condition |

If your browser tab freezes during a loop exercise, close the tab immediately. Fix the loop, then reload.

---

## 9. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 2: Program Structure (Loops section)](https://eloquentjavascript.net/02_program_structure.html)**
  The primary OER textbook. The loop sections cover `for`, `while`, and `do-while` with practical examples including break and continue behavior.

- **[MDN Web Docs — Loops and iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)**
  Comprehensive guide covering all loop types (`for`, `while`, `do-while`, `for...in`, `for...of`, `labeled` statements, `break`, and `continue`) with runnable examples.

- **[javascript.info — Loops: while and for](https://javascript.info/while-for)**
  Detailed breakdown of loop mechanics with interactive tasks. Covers off-by-one analysis, `break`/`continue` behavior, and loop labels for breaking nested loops.

- **[MDN Web Docs — `for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)**
  Full reference for the `for...of` loop including iterable protocol, use with arrays, strings, Maps, Sets, and generators.

- **[MDN Web Docs — `for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)**
  Reference for `for...in` including the explicit warning about using it on arrays and why `for...of` or a traditional `for` loop is preferred for array iteration.

---

## 10. JSE Certification Exam Tips

1. **`<` vs `<=` off-by-one** — `i < 5` runs five times (0–4); `i <= 5` runs six times (0–5). Read the condition carefully and count.

2. **`while` zero-execution** — if the condition is false before the first check, a `while` loop body never runs. `do-while` always runs at least once regardless of the condition.

3. **Infinite loop from missing update** — `while` loops that never modify the condition variable run forever. "Browser freezes" or "runs forever" is the expected answer for such code on the exam.

4. **`break` exits the innermost loop only** — in nested loops, `break` inside the inner loop does not affect the outer loop.

5. **`continue` does not exit the loop** — it skips the current iteration and moves to the next one. The loop keeps running.

6. **`for...of` gives values; `for...in` gives keys** — this distinction is tested directly. `for...in` on an array gives string index keys (`'0'`, `'1'`, `'2'`), not the values.

7. **`typeof` the keys from `for...in`** — keys from `for...in` are always strings, even when used on an array whose indices look like numbers.

8. **`for...in` on arrays is unreliable** — it may include inherited properties. Always use `for...of` or a traditional `for` loop for arrays.

9. **Loop variable scope with `let`** — `for (let i = 0; ...)` makes `i` block-scoped and unavailable after the loop ends. Accessing `i` after the loop throws a `ReferenceError`.

10. **`do-while` semicolon** — the `do-while` loop requires a semicolon after the closing `while (condition);`. Missing the semicolon is a syntax error.

---

## 11. Study Checklist

- [ ] Watch the Module 05 video lecture by Professor Nash.
- [ ] Read Chapter 2 (Program Structure) of [Eloquent JavaScript](https://eloquentjavascript.net/02_program_structure.html) — loop sections.
- [ ] Read [MDN — for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for).
- [ ] Read [MDN — while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while).
- [ ] Read [MDN — for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of).
- [ ] Read [MDN — for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in).
- [ ] Open the console and trace the `<` vs `<=` comparison table manually — count each one.
- [ ] Write a `while` loop with a missing update — confirm the tab freezes — then close and fix it.
- [ ] Demonstrate `for...in` on an array and confirm the keys come back as strings.
- [ ] Complete the Module 05 Lab.
- [ ] Complete the Module 05 Quiz.
