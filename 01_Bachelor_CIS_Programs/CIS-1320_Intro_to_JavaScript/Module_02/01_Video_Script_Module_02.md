# Video Script: CIS-1320 — Introduction to JavaScript

## Module 02 — Variables, Constants, and Scope

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp &bull; JavaScript Programming Full Course &bull; Module 02</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=jS4aFq5-91M" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/jS4aFq5-91M" title="freeCodeCamp &bull; JavaScript Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp &bull; JavaScript Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 14–17 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 02 | Variables, Constants, and Scope | CIS-1320"]**

"Welcome back. Module 02 is about how JavaScript stores data. That sounds simple — declare a variable, give it a value. And it is simple in most cases. But JavaScript has three different ways to declare variables, and they behave differently in ways that trip up developers every day. Understanding those differences is also one of the most-tested topic areas on the JSE certification exam.

By the end of this module you will understand exactly what `var`, `let`, and `const` do, how scope determines where a variable is visible, and what hoisting means and why it matters. Let us get into it."

---

## [01:00 – 04:00] Part 1 — `let` and `const`: The Modern Keywords

**[SHOW SLIDE: "ES6 Variables: `let` and `const`"]**

"JavaScript was created in 1995 and the original keyword for declaring variables was `var`. In 2015, ECMAScript 6 — ES6 — introduced two new keywords: `let` and `const`. They were designed to fix real problems with `var`. In this course, we use `let` and `const` for everything. We will cover `var` in detail because the exam tests it, but you should not write new code with `var`.

**`let`** declares a variable that can be reassigned. Use `let` when you know the value will change.

**`const`** declares a binding that cannot be reassigned. Use `const` when the value is fixed after initialization.

**[DEMO — open DevTools Console]**

```javascript
let score = 0;
score = 100;
console.log(score);   // 100

const PI = 3.14159;
PI = 3;               // TypeError: Assignment to constant variable
```

[PAUSE]

Let me run that. Notice `score` changes from 0 to 100 — that is a reassignment with `let`. Then `PI = 3` throws a `TypeError` immediately. You cannot reassign a `const` binding.

**The practical rule:** start with `const` for everything. If you later discover you need to reassign it, change it to `let`. You will use `const` about 80 percent of the time.

[PAUSE]

One thing that surprises students: `const` does not make an object immutable. It only prevents you from reassigning the binding itself. The properties of an object declared with `const` can still be modified.

```javascript
const user = { name: 'Alice', score: 95 };
user.score = 100;          // OK — modifying a property
console.log(user.score);   // 100

user = { name: 'Bob' };    // TypeError — cannot reassign the binding
```

`const` locks the variable so it always points to the same object. It does not lock what is inside that object. We will explore this more in the Objects module."

---

## [04:00 – 07:00] Part 2 — Block Scope

**[SHOW SLIDE: "Block Scope: `let` and `const` Stay Inside `{}`"]**

"Scope is the concept that determines where a variable is visible and accessible in your code. `let` and `const` are **block-scoped** — they are only accessible inside the pair of curly braces where they were declared.

**[DEMO]**

```javascript
{
  let inside = 'I am inside the block';
  console.log(inside);   // I am inside the block
}

console.log(inside);     // ReferenceError: inside is not defined
```

The curly braces create a block. `inside` lives only in that block. Once you step outside, it is gone.

This applies in real code with if statements and loops:

```javascript
if (true) {
  let message = 'In the if block';
  const MAX = 10;
  console.log(message);   // In the if block
}

console.log(message);   // ReferenceError
console.log(MAX);       // ReferenceError
```

[PAUSE]

The JSE exam frequently tests this. A common question shows a variable declared with `let` inside an `if` block and then accessed outside it. You need to recognize that `let` and `const` do not escape blocks — they throw `ReferenceError` if accessed outside their block.

Loop variables work the same way:

```javascript
for (let i = 0; i < 3; i++) {
  console.log(i);   // 0, 1, 2
}

console.log(i);   // ReferenceError — i does not exist here
```

This is actually a good thing. It prevents accidental access to loop counters after the loop ends."

---

## [07:00 – 10:30] Part 3 — `var` and Function Scope

**[SHOW SLIDE: "`var` — Function Scope, Not Block Scope"]**

"Now let us look at `var`. `var` is function-scoped, not block-scoped. This means a `var` variable declared inside an if block or a for loop is visible to the entire function that contains it.

**[DEMO — paste both in console]**

```javascript
if (true) {
  var leaky = 'I escaped the block!';
}
console.log(leaky);   // I escaped the block!
```

That variable leaks out of the if block because `var` ignores block boundaries. It is only bounded by the nearest function.

[PAUSE]

Here is the classic loop trap. Compare these two:

```javascript
for (var i = 0; i < 3; i++) {}
console.log(i);   // 3 — var i leaked into the outer scope

for (let j = 0; j < 3; j++) {}
console.log(j);   // ReferenceError — let j did not leak
```

This is a major source of bugs in older JavaScript code. With `var`, the loop counter stays alive after the loop ends and has the value it had when the loop stopped. With `let`, it vanishes.

[PAUSE]

`var` also allows re-declaration in the same scope — no error:

```javascript
var x = 1;
var x = 2;   // No error — x is just reassigned
console.log(x);   // 2
```

With `let`, re-declaration in the same scope is a `SyntaxError`:

```javascript
let y = 1;
let y = 2;   // SyntaxError: Identifier 'y' has already been declared
```

The `let` version gives you an explicit error message so you know immediately that something is wrong. The `var` version silently succeeds, which is harder to debug."

---

## [10:30 – 13:30] Part 4 — Hoisting

**[SHOW SLIDE: "Hoisting: What Happens Before Your Code Runs"]**

"Hoisting is one of the most important concepts to understand for the JSE exam. It describes a behavior that happens before your code actually executes.

When the JavaScript engine processes a script, it scans for all variable and function declarations before running any code. It 'hoists' those declarations to the top of their scope. The key difference is what gets hoisted and what does not.

**`var` hoisting — declaration is hoisted AND initialized to `undefined`:**

**[DEMO]**

```javascript
console.log(myVar);   // undefined — not an error
var myVar = 5;
console.log(myVar);   // 5
```

Why does the first `console.log` print `undefined` instead of throwing an error? Because `var myVar` was hoisted to the top of the scope during the compilation phase. It is as if the engine rewrote your code like this:

```javascript
var myVar;            // declaration hoisted — value is undefined
console.log(myVar);   // undefined
myVar = 5;            // assignment stays in place
console.log(myVar);   // 5
```

[PAUSE]

**`let` and `const` hoisting — declaration is hoisted but NOT initialized:**

```javascript
console.log(myLet);   // ReferenceError: Cannot access 'myLet' before initialization
let myLet = 5;
```

`let` is technically hoisted — the engine knows it exists — but it is placed in what is called the **Temporal Dead Zone** (TDZ). The TDZ is the period from the start of the scope to the declaration line. Any access during the TDZ throws a `ReferenceError`.

The practical difference is important:

| Keyword | Accessed before declaration |
|---|---|
| `var` | Returns `undefined` — no error |
| `let` | `ReferenceError: Cannot access before initialization` |
| `const` | `ReferenceError: Cannot access before initialization` |

[PAUSE]

For the JSE exam, recognize this pattern immediately: code that reads a variable before its declaration line. If the variable is `var`, you see `undefined`. If it is `let` or `const`, you see a `ReferenceError`. The word 'Temporal Dead Zone' appears in documentation but the exam focuses on the practical behavior."

---

## [13:30 – 15:30] Part 5 — Naming Rules and Best Practices

**[SHOW SLIDE: "Variable Naming Rules"]**

"A few quick rules on naming. Variable names in JavaScript are called **identifiers**. Identifiers must follow these rules:

- Must start with a letter, underscore `_`, or dollar sign `$` — not a digit
- Can contain letters, digits, underscores, and dollar signs
- Are case-sensitive: `score`, `Score`, and `SCORE` are three different variables
- Cannot be a reserved keyword like `let`, `const`, `if`, `return`

Valid identifiers: `score`, `playerName`, `_total`, `$price`, `MAX_SIZE`
Invalid: `1stPlace` (starts with digit), `my-variable` (hyphen not allowed)

[PAUSE]

The JavaScript convention for multi-word variable names is **camelCase**: the first word is lowercase, each subsequent word starts with a capital letter. `playerScore`, `totalAmount`, `isGameOver`, `firstName`. This is the near-universal convention in JavaScript code.

For constants that represent fixed configuration values, many teams use `UPPER_SNAKE_CASE`: `MAX_RETRIES`, `API_TIMEOUT_MS`. This signals 'this value never changes' to anyone reading the code.

[PAUSE]

Here is the style guide I want you to follow in this course:

1. Use `const` by default
2. Use `let` only when you know you need to reassign the value
3. Never use `var` in new code
4. Use descriptive names — `playerScore` is better than `ps` or `x`
5. Follow camelCase for variables, UPPER_SNAKE_CASE for module-level constants

That is Module 02. The lab will have you experimenting with all of these behaviors directly in the console and in script files. The quiz covers the `var`/`let`/`const` behavioral differences, hoisting, and scope rules. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 02 — Variables, Constants, and Scope]**

---

## Additional Resources

- [MDN Web Docs — `let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) — block scope and temporal dead zone documentation
- [MDN Web Docs — `const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) — const binding rules and the object mutation nuance
- [MDN Web Docs — `var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var) — function scope and hoisting behavior
- [Eloquent JavaScript — Chapter 2: Program Structure](https://eloquentjavascript.net/02_program_structure.html) — free textbook coverage of bindings and scope
