# Quiz: Module 06 — Functions and Arrow Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the output of the following code?

```javascript
console.log(greet('Alice'));

function greet(name) {
  return 'Hello, ' + name;
}
```

- A) `ReferenceError: greet is not defined`
- B) `ReferenceError: Cannot access 'greet' before initialization`
- C) `Hello, Alice`
- D) `undefined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `greet` is defined — the function declaration exists in the code. This error would occur if `greet` were never declared at all.
- *Why B is incorrect:* That error applies to `const`/`let` variables accessed before their initialization (Temporal Dead Zone). Function declarations are hoisted completely and do not have a TDZ.
- *Why C is correct:* Function declarations are fully hoisted. The engine moves the entire `greet` definition to the top of the scope before executing any code. Calling it before the written line works perfectly.
- *Why D is incorrect:* `undefined` would be returned if the function existed but had no `return` statement. This function has `return 'Hello, ' + name`, so it returns a string.

---

### Question 2

What is the output of the following code?

```javascript
console.log(double(4));

const double = function(n) {
  return n * 2;
};
```

- A) `8`
- B) `undefined`
- C) `ReferenceError: Cannot access 'double' before initialization`
- D) `TypeError: double is not a function`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `const` function expressions are not hoisted. The assignment `const double = function(...)` has not yet executed when `console.log(double(4))` runs.
- *Why B is incorrect:* `undefined` is what a `var` variable holds before its assignment (because `var` declarations are hoisted to `undefined`). `const` variables are in the TDZ — accessing them throws an error, they are not silently `undefined`.
- *Why C is correct:* `const double` is in the Temporal Dead Zone from the start of the block until the line `const double = function(...)` is reached. Accessing the variable before that point throws `ReferenceError: Cannot access 'double' before initialization`.
- *Why D is incorrect:* This error would occur if `double` existed and held a non-function value, and then was called as a function. Here, the error is thrown before any call attempt — the variable access itself fails.

---

### Question 3

What does the following function return?

```javascript
function printScore(score) {
  console.log('Score:', score);
}

const result = printScore(85);
console.log(result);
```

- A) `85`
- B) `'Score: 85'`
- C) `undefined`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `85` is passed as an argument but it is not returned. The function uses it internally in `console.log` but has no `return` statement.
- *Why B is incorrect:* The string `'Score: 85'` is printed to the console as a side effect, but it is not the return value of the function.
- *Why C is correct:* A function with no `return` statement automatically returns `undefined`. `result` is assigned the return value of `printScore(85)`, which is `undefined`.
- *Why D is incorrect:* `null` is an intentional "no value" value that must be explicitly returned. Functions without `return` return `undefined`, not `null`.

---

### Question 4

Which of the following arrow functions correctly uses an implicit return?

- A) `const f = x => { x * 2 };`
- B) `const f = x => { return x * 2; };`
- C) `const f = x => x * 2;`
- D) `const f = (x) => { x * 2 }`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The braces `{}` create a block body. With a block body, the expression `x * 2` is computed but not returned — the function returns `undefined`. An explicit `return` is required inside braces.
- *Why B is incorrect:* This is syntactically correct and does return `x * 2`, but it uses an explicit return inside a block body — not an implicit return. The question asks which uses an implicit return.
- *Why C is correct:* When an arrow function has no braces, the expression after `=>` is the implicit return value. `n => n * 2` evaluates `n * 2` and returns the result automatically.
- *Why D is incorrect:* Same issue as A — braces create a block body and require an explicit `return`. Missing the semicolon after `}` is also a style issue, though not a syntax error here.

---

### Question 5

What is the output of the following code?

```javascript
function greet(name = 'stranger') {
  return 'Hi, ' + name;
}

console.log(greet(null));
```

- A) `'Hi, stranger'`
- B) `'Hi, null'`
- C) `'Hi, undefined'`
- D) `TypeError: null is not a valid argument`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Default parameter values are triggered only when the argument is `undefined`. `null` is not `undefined` — it is a distinct value that passes through to the parameter unchanged.
- *Why B is correct:* `null` is passed explicitly. Default parameters do not replace `null`. `name` receives `null`, and `'Hi, ' + null` evaluates to `'Hi, null'` (JavaScript coerces `null` to the string `'null'`).
- *Why C is incorrect:* `undefined` would produce this output if `name` had no default. With the default present, `undefined` would trigger `'Hi, stranger'` — but `null` is not `undefined`.
- *Why D is incorrect:* JavaScript does not throw a `TypeError` for passing `null` as a function argument. `null` is a valid value in JavaScript.

---

### Question 6

What is the output of the following code?

```javascript
function greet(name = 'stranger') {
  return 'Hi, ' + name;
}

console.log(greet(undefined));
```

- A) `'Hi, undefined'`
- B) `'Hi, stranger'`
- C) `ReferenceError`
- D) `'Hi, '`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Passing `undefined` explicitly is treated the same as omitting the argument — both trigger the default parameter value.
- *Why B is correct:* Default parameters are used when the argument is `undefined` — whether omitted entirely or explicitly passed as `undefined`. `name` receives the default value `'stranger'`.
- *Why C is incorrect:* Passing `undefined` to a function is not an error. It is a valid argument value that simply triggers any applicable default.
- *Why D is incorrect:* `'Hi, '` would result if `name` received an empty string `''`. Default parameters do not trigger for empty strings.

---

### Question 7

What is the output of the following code?

```javascript
function buildList(first, second, ...rest) {
  console.log(first);
  console.log(second);
  console.log(rest);
}

buildList('a', 'b', 'c', 'd', 'e');
```

- A) `'a'`, `'b'`, `'c'`
- B) `'a'`, `'b'`, `['c', 'd', 'e']`
- C) `['a', 'b', 'c', 'd', 'e']`, `undefined`, `[]`
- D) `'a'`, `'b'`, `'c', 'd', 'e'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `rest` collects the remaining arguments into an array — it is not a single string `'c'`. The output for `rest` is `['c', 'd', 'e']`.
- *Why B is correct:* `first` receives `'a'`, `second` receives `'b'`, and `...rest` collects all remaining arguments `'c'`, `'d'`, `'e'` into the array `['c', 'd', 'e']`.
- *Why C is incorrect:* `first` receives the first argument `'a'`, not all arguments. The rest parameter collects whatever is left after the named parameters are filled.
- *Why D is incorrect:* The rest parameter produces an array, not a sequence of separate values. `console.log(rest)` prints `['c', 'd', 'e']` — an array — not three separate values on one line.

---

### Question 8

Which of the following is a valid arrow function with no parameters?

- A) `const fn = => 'hello';`
- B) `const fn = _ => 'hello';`
- C) `const fn = () => 'hello';`
- D) `const fn = function => 'hello';`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `=>` cannot follow `=` directly. A parameter list — at minimum empty parentheses `()` — is required between `=` and `=>`. This is a syntax error.
- *Why B is incorrect:* `_ => 'hello'` is valid syntax but it declares one parameter named `_` (a common convention for an intentionally unused parameter). It is not a no-parameter function.
- *Why C is correct:* `()` is the required syntax for an arrow function with no parameters. The empty parentheses signal that no arguments are expected.
- *Why D is incorrect:* `function` is a keyword — it cannot be used as a parameter name. This is a syntax error.

---

### Question 9

What is the output of the following code?

```javascript
const add = (a, b) => {
  a + b;
};

console.log(add(3, 5));
```

- A) `8`
- B) `undefined`
- C) `0`
- D) `SyntaxError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The expression `a + b` is computed inside the braces but never returned. The braces create a block body that requires an explicit `return`. Without it, the function returns `undefined`.
- *Why B is correct:* Arrow functions with block bodies `{}` require an explicit `return` statement. `a + b` is evaluated but discarded. The function falls off the end and returns `undefined`.
- *Why C is incorrect:* `0` is not produced by this code. The function does not return `0` and there is no mechanism that would produce it.
- *Why D is incorrect:* The code is syntactically valid JavaScript. There is no syntax error — the bug is a missing `return`, which is a logic error, not a syntax error.

---

### Question 10

Which statement about arrow functions and the `this` keyword is correct?

- A) Arrow functions have their own `this` that refers to the function itself
- B) Arrow functions inherit `this` from the enclosing lexical scope
- C) Arrow functions always have `this` set to the global object
- D) Arrow functions cannot use `this` at all — it throws a `ReferenceError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Regular functions have their own `this` determined by how they are called. Arrow functions do not — they have no `this` binding of their own.
- *Why B is correct:* Arrow functions use **lexical `this`** — they inherit `this` from the surrounding context where they were defined, not from how they are called. This is the defining behavioral difference between arrow functions and regular functions.
- *Why C is incorrect:* In non-strict mode, a regular function called without an explicit context does have `this` set to the global object. But arrow functions never set their own `this` — they always look up the scope chain to find the enclosing `this`.
- *Why D is incorrect:* Using `this` inside an arrow function does not throw an error. It resolves `this` from the enclosing lexical scope. If no meaningful `this` is in the enclosing scope, it may be `undefined` (strict mode) or the global object — but it does not throw.

---

### Question 11

What is the output of the following code?

```javascript
function outer() {
  let count = 0;
  function increment() {
    count++;
    return count;
  }
  return increment;
}

const counter = outer();
console.log(counter());
console.log(counter());
console.log(counter());
```

- A) `1`, `1`, `1`
- B) `undefined`, `undefined`, `undefined`
- C) `1`, `2`, `3`
- D) `ReferenceError: count is not defined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Each call to `counter()` does not create a fresh `count = 0`. The closure captures the variable `count` from `outer`'s scope — and that same variable persists across calls.
- *Why B is incorrect:* `increment` always returns `count` after incrementing it. The return value is a number, not `undefined`.
- *Why C is correct:* `outer()` returns the `increment` function. This inner function forms a **closure** over the `count` variable in `outer`'s scope. Each call to `counter()` increments the shared `count`: first call → `1`, second → `2`, third → `3`. The variable persists because the closure keeps `outer`'s scope alive.
- *Why D is incorrect:* `count` is accessible inside `increment` via the closure. The closure extends `increment`'s reach into `outer`'s scope even after `outer` has returned.

---

### Question 12

What does the following code output?

```javascript
const multiply = (a, b = a * 2) => a * b;
console.log(multiply(3));
console.log(multiply(3, 4));
```

- A) `18` then `12`
- B) `3` then `12`
- C) `18` then `12`
- D) `NaN` then `12`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `multiply(3)` — `a = 3`, `b` is omitted so it defaults to `a * 2 = 6`. Result: `3 * 6 = 18`. `multiply(3, 4)` — `a = 3`, `b = 4` (explicit). Result: `3 * 4 = 12`. Note that options A and C are identical (both `18` then `12`) — the correct answer is `18` then `12`.
- *Why B is incorrect:* `multiply(3)` uses the default `b = a * 2 = 6`, so `3 * 6 = 18`, not `3`.
- *Why D is incorrect:* `a * 2` is `3 * 2 = 6`. Both `a` and the default `b` are valid numbers, so no `NaN` results.

---

### Question 13

What is the output of the following code?

```javascript
function greet(name = 'stranger') {
  return 'Hi, ' + name;
}

console.log(greet());
console.log(greet(''));
console.log(greet(0));
```

- A) `'Hi, stranger'`, `'Hi, stranger'`, `'Hi, stranger'`
- B) `'Hi, stranger'`, `'Hi, '`, `'Hi, 0'`
- C) `'Hi, stranger'`, `'Hi, stranger'`, `'Hi, 0'`
- D) `'Hi, stranger'`, `'Hi, '`, `'Hi, stranger'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Only `undefined` (or omitting the argument) triggers the default. `''` and `0` are valid argument values that are passed through directly.
- *Why B is correct:* `greet()` — no argument, `name` gets default `'stranger'`. `greet('')` — `''` is not `undefined`, so it is used as-is: `'Hi, '`. `greet(0)` — `0` is not `undefined`, so it is used: `'Hi, 0'` (JavaScript coerces `0` to `'0'` via string concatenation).
- *Why C is incorrect:* `greet('')` passes `''` which is not `undefined`, so the default does not apply. The empty string is passed to `name`.
- *Why D is incorrect:* `greet(0)` passes `0`, not `undefined`. The default does not trigger. `'Hi, ' + 0` = `'Hi, 0'`.

---

### Question 14

What is the output of the following code?

```javascript
const add = (a, b) => a + b;
const double = n => n * 2;
const apply = (fn, value) => fn(value);

console.log(apply(double, 5));
console.log(apply(n => n ** 2, 4));
```

- A) `10` then `16`
- B) `5` then `4`
- C) `10` then `8`
- D) `TypeError: fn is not a function`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `apply(double, 5)` calls `double(5)` = `5 * 2 = 10`. `apply(n => n ** 2, 4)` calls the inline arrow function with `4`: `4 ** 2 = 16`.
- *Why B is incorrect:* The functions are called and their results are returned. `5` and `4` are the inputs, not the outputs.
- *Why C is incorrect:* `4 ** 2 = 16`, not `8`. `**` is the exponentiation operator (`4 × 4`), not `* 2`.
- *Why D is incorrect:* `double` and the anonymous arrow function are valid function values. Passing functions as arguments is valid JavaScript — this is a **higher-order function** pattern.

---

### Question 15

What does the spread operator do when used in a function call?

```javascript
const nums = [3, 1, 4, 1, 5, 9];
console.log(Math.max(...nums));
```

- A) It creates a new array from the function's arguments
- B) It expands the array into individual arguments passed to the function
- C) It merges the array into the first argument
- D) `TypeError — Math.max does not accept arrays`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The spread operator in a function call expands an iterable into individual arguments. Creating an array from function arguments is what the rest parameter `...` does in a function definition.
- *Why B is correct:* `...nums` in a function call expands the array `[3, 1, 4, 1, 5, 9]` into six separate arguments: `Math.max(3, 1, 4, 1, 5, 9)`. The result is `9`.
- *Why C is incorrect:* The spread operator does not merge values. It unpacks them into individual positional arguments.
- *Why D is incorrect:* `Math.max` accepts multiple numeric arguments. Without spread, `Math.max([3,1,4,1,5,9])` would return `NaN` because an array is not a number. With spread, each element becomes a separate argument.

---

### Question 16

What is the output of the following code?

```javascript
function outer(x) {
  return function inner(y) {
    return x + y;
  };
}

const add5 = outer(5);
console.log(add5(3));
console.log(add5(10));
```

- A) `8` then `15`
- B) `5` then `5`
- C) `3` then `10`
- D) `ReferenceError: x is not defined`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `outer(5)` returns the `inner` function with `x = 5` captured in its closure. `add5(3)` calls `inner(3)` → `5 + 3 = 8`. `add5(10)` calls `inner(10)` → `5 + 10 = 15`. This is the **currying/partial application** pattern.
- *Why B is incorrect:* `x` is `5` in both calls but `y` changes. The function returns `x + y`, not just `x`.
- *Why C is incorrect:* `y` changes each call (`3` then `10`), but `x + y` is what is returned, not just `y`.
- *Why D is incorrect:* `x` is captured in `inner`'s closure from `outer`'s scope. It is accessible via the closure even after `outer` has returned.

---

### Question 17

Which of the following is a correct IIFE (Immediately Invoked Function Expression)?

- A) `function() { console.log('run'); }()`
- B) `(function() { console.log('run'); })()`
- C) `function run() { console.log('run'); }()`
- D) `const fn = function() { console.log('run'); }; fn()`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A function declaration starting with `function` cannot be immediately invoked with `()`. The parser treats it as a declaration, not an expression. This is a `SyntaxError`.
- *Why B is correct:* Wrapping the function in parentheses forces the parser to treat it as a function expression, not a declaration. The trailing `()` then immediately invokes it. This is the standard IIFE pattern.
- *Why C is incorrect:* A named function declaration also cannot be immediately invoked. The `()` at the end is parsed as grouping parentheses for nothing, producing a `SyntaxError`.
- *Why D is incorrect:* This declares a function expression and then calls it in a separate statement. That is two statements — not an immediately invoked function expression. An IIFE executes in a single expression without naming the function.

---

### Question 18

What is the output of the following code?

```javascript
const greet = name => name ? `Hello, ${name}!` : 'Hello, stranger!';

console.log(greet('Bob'));
console.log(greet(''));
console.log(greet());
```

- A) `'Hello, Bob!'`, `'Hello, !'`, `'Hello, undefined!'`
- B) `'Hello, Bob!'`, `'Hello, stranger!'`, `'Hello, stranger!'`
- C) `'Hello, Bob!'`, `'Hello, stranger!'`, `'Hello, undefined!'`
- D) `'Hello, Bob!'`, `'Hello, '`, `'Hello, stranger!'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The ternary condition `name ?` checks truthiness. `''` is falsy and `undefined` (from no argument) is also falsy — both return the `else` branch `'Hello, stranger!'`.
- *Why B is correct:* `greet('Bob')` — `'Bob'` is truthy → `'Hello, Bob!'`. `greet('')` — `''` is falsy → `'Hello, stranger!'`. `greet()` — `name` is `undefined` (falsy) → `'Hello, stranger!'`.
- *Why C is incorrect:* When `name` is `undefined`, the ternary condition is `false` and the else branch `'Hello, stranger!'` is returned — not `'Hello, undefined!'`.
- *Why D is incorrect:* `''` is falsy, so the ternary returns `'Hello, stranger!'`, not `'Hello, '`.

---

### Question 19

What is the output of the following code?

```javascript
function sum(...numbers) {
  return numbers.reduce((acc, n) => acc + n, 0);
}

console.log(sum(1, 2, 3));
console.log(sum(10));
console.log(sum());
```

- A) `6`, `10`, `NaN`
- B) `6`, `10`, `0`
- C) `6`, `10`, `undefined`
- D) `TypeError: numbers.reduce is not a function`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `sum()` calls `reduce` on an empty array `[]` with an initial value of `0`. `reduce` with an initial value returns that initial value when the array is empty — so the result is `0`, not `NaN`.
- *Why B is correct:* `sum(1, 2, 3)` → rest `[1,2,3]`, reduce → `6`. `sum(10)` → rest `[10]`, reduce → `10`. `sum()` → rest `[]`, reduce with initial `0` → `0`.
- *Why C is incorrect:* `reduce` on an empty array with an initial value returns the initial value (`0`), not `undefined`.
- *Why D is incorrect:* The rest parameter `...numbers` always produces a real `Array`, even when no arguments are passed (it produces `[]`). `Array.prototype.reduce` is available on all arrays.

---

### Question 20

What is the output of the following code?

```javascript
const makeCounter = (start = 0, step = 1) => {
  let current = start;
  return {
    next: () => (current += step),
    reset: () => { current = start; }
  };
};

const counter = makeCounter(10, 5);
console.log(counter.next());
console.log(counter.next());
counter.reset();
console.log(counter.next());
```

- A) `15`, `20`, `15`
- B) `10`, `15`, `10`
- C) `15`, `20`, `10`
- D) `5`, `10`, `5`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `makeCounter(10, 5)` — `start = 10`, `step = 5`. `current = 10`. `next()` does `current += 5` and returns the new value: first call → `15`. Second call → `20`. `reset()` sets `current = start = 10`. Third `next()` call → `current += 5` → `15`.
- *Why B is incorrect:* `next()` increments and returns the new value. The first call adds `5` to the starting `10`, giving `15`, not `10`.
- *Why C is incorrect:* After `reset()`, `current = 10`. The next `next()` call does `10 + 5 = 15`, not `10`.
- *Why D is incorrect:* The counter starts at `10`, not `0`. `step` is `5`. The sequence is `15`, `20`, then after reset `15` — not `5`, `10`, `5`.
