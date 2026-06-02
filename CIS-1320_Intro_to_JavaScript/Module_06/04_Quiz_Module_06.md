# Quiz: Module 06 — Functions and Arrow Functions

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
