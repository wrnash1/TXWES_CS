# Quiz: Module 02 — Variables, Constants, and Scope

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the output of the following code?

```javascript
if (true) {
  let message = 'inside';
}
console.log(message);
```

- A) `inside`
- B) `undefined`
- C) `null`
- D) `ReferenceError: message is not defined`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `message` is declared with `let` inside the `if` block. `let` is block-scoped — it is destroyed when the `}` closes. It is not accessible outside the block.
- *Why B is incorrect:* `undefined` would result if `message` were declared with `var` (hoisting) or if it were an accessible but uninitialized variable. `let` does not return `undefined` when accessed outside its scope — it throws `ReferenceError`.
- *Why C is incorrect:* `null` is an explicit assigned value, not a default for out-of-scope variables.
- *Why D is correct:* `let` is block-scoped. The block closes at `}` and `message` no longer exists. `console.log(message)` outside the block throws `ReferenceError`.

---

### Question 2

What is the output of the following code?

```javascript
console.log(counter);
var counter = 10;
console.log(counter);
```

- A) `ReferenceError` then `10`
- B) `10` then `10`
- C) `undefined` then `10`
- D) `null` then `10`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A `ReferenceError` would occur with `let` or `const`. `var` declarations are hoisted and initialized to `undefined`, so reading `counter` before its line is not an error.
- *Why B is incorrect:* The value `10` is not available until after the assignment executes. The hoisted `var counter` holds `undefined` until `counter = 10` runs.
- *Why C is correct:* `var counter` is hoisted to the top of its scope and initialized to `undefined`. The first `console.log` prints `undefined`. The assignment then executes and the second `console.log` prints `10`.
- *Why D is incorrect:* Hoisted `var` variables are initialized to `undefined`, not `null`. These are distinct values.

---

### Question 3

What is the output of the following code?

```javascript
if (true) {
  var leaky = 'escaped';
}
console.log(leaky);
```

- A) `ReferenceError: leaky is not defined`
- B) `undefined`
- C) `escaped`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A `ReferenceError` would occur with `let` or `const`. `var` ignores block boundaries — it is scoped to the enclosing function (or global scope), not the `if` block.
- *Why B is incorrect:* `undefined` would appear if the variable were accessible but unassigned. `leaky` was assigned `'escaped'` and `var` does not restrict it to the block.
- *Why C is correct:* `var` is function-scoped. The `if (true) {}` block does not create a new scope for `var`. `leaky` is accessible outside the block and prints `'escaped'`.
- *Why D is incorrect:* `null` is not a default value for variables. The assigned string `'escaped'` is accessible.

---

### Question 4

Which statement about `const` is correct?

- A) A `const` variable can be reassigned as long as the new value is the same type
- B) A `const` variable cannot be reassigned, and its value can never be changed in any way
- C) A `const` variable cannot be reassigned, but if it holds an object, that object's properties can be modified
- D) A `const` variable must be declared in the global scope

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `const` prevents reassignment entirely regardless of type. Any assignment to a `const` variable throws `TypeError`.
- *Why B is incorrect:* This is a common misconception. `const` prevents reassigning the binding — the variable cannot point to a different value. However, if the value is an object or array, its contents can be mutated: `obj.x = 1` or `arr.push(5)` are both valid.
- *Why C is correct:* `const` locks the binding only. The variable always refers to the same object, but that object's properties can be freely modified.
- *Why D is incorrect:* `const` works in any scope — global, function, or block.

---

### Question 5

What is the output of the following code?

```javascript
console.log(myVal);
let myVal = 42;
```

- A) `undefined`
- B) `42`
- C) `null`
- D) `ReferenceError: Cannot access 'myVal' before initialization`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `undefined` is the result when `var` is accessed before its declaration. `let` variables are in the Temporal Dead Zone from the start of their scope to their declaration line.
- *Why B is incorrect:* The value `42` is not available before the declaration line. The TDZ prevents access.
- *Why C is incorrect:* Variables are not set to `null` before their declaration.
- *Why D is correct:* `let` is hoisted but uninitialized (Temporal Dead Zone). Accessing it before the declaration line throws `ReferenceError: Cannot access 'myVal' before initialization`.

---

### Question 6

What is the output of the following code?

```javascript
for (var i = 0; i < 3; i++) {
  // loop body
}
console.log(i);
```

- A) `ReferenceError: i is not defined`
- B) `2`
- C) `undefined`
- D) `3`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* A `ReferenceError` would result from using `let i`. `var i` is not block-scoped — it leaks into the surrounding scope.
- *Why B is incorrect:* The last value of `i` during the loop body is `2`, but the loop continues — `i` is incremented to `3`, the condition `i < 3` fails, and the loop exits with `i` equal to `3`.
- *Why C is incorrect:* `i` has a value of `3` after the loop. There is no reason for it to be `undefined`.
- *Why D is correct:* `var i` leaks out of the for block. The loop increments `i` to `3` before the condition fails. After the loop, `console.log(i)` prints `3`.

---

### Question 7

What happens when the following code executes?

```javascript
let count = 0;
let count = 1;
console.log(count);
```

- A) Prints `0`
- B) Prints `1`
- C) `SyntaxError: Identifier 'count' has already been declared`
- D) `TypeError: Assignment to constant variable`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The engine throws a `SyntaxError` before any code runs. The `console.log` is never reached.
- *Why B is incorrect:* Same reason — the `SyntaxError` occurs at parse time.
- *Why C is correct:* `let` does not allow re-declaration in the same scope. The second `let count = 1` triggers `SyntaxError: Identifier 'count' has already been declared` during parsing, before execution begins.
- *Why D is incorrect:* `TypeError: Assignment to constant variable` occurs when you try to reassign a `const` binding. This code uses `let`, and the issue is re-declaration (a second `let` keyword), not reassignment.

---

### Question 8

Which variable declaration follows modern JavaScript best practice for a value that will never be reassigned?

- A) `var MAX_SIZE = 100;`
- B) `let MAX_SIZE = 100;`
- C) `const MAX_SIZE = 100;`
- D) `MAX_SIZE = 100;`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `var` has function scope, hoists to `undefined`, and allows re-declaration — behaviors that can introduce bugs. It is not recommended for new code.
- *Why B is incorrect:* `let` is appropriate when you need to reassign. For a value that will never change, `const` is the correct choice — it signals intent and is enforced by the engine.
- *Why C is correct:* `const` explicitly communicates that `MAX_SIZE` will not be reassigned. `UPPER_SNAKE_CASE` is the conventional style for module-level constants.
- *Why D is incorrect:* Assigning without a keyword creates an implicit global in non-strict mode, which pollutes the global scope. In strict mode it throws `ReferenceError`. Never assign variables without a declaration keyword.

---

### Question 9

What is the output of the following code?

```javascript
const config = { debug: false, version: '1.0' };
config.debug = true;
config.author = 'Nash';
console.log(config.debug, config.version, config.author);
```

- A) `TypeError: Cannot assign to read only property 'debug'`
- B) `false 1.0 undefined`
- C) `true 1.0 Nash`
- D) `TypeError: Assignment to constant variable`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* JavaScript does not make object properties read-only simply because the object is declared with `const`. Only the binding is constant. To make properties read-only you would need `Object.freeze()`.
- *Why B is incorrect:* `config.debug` is successfully mutated to `true`. The original `false` value is replaced.
- *Why C is correct:* `const config` prevents `config = something_new`, but property assignments on the existing object are valid mutations. The output is `true 1.0 Nash`.
- *Why D is incorrect:* `TypeError: Assignment to constant variable` occurs when you try to reassign the binding (`config = {}`). Property mutations on the existing object do not trigger this error.

---

### Question 10

A developer wants to declare a variable `total` that starts at `0` and will be incremented inside a loop. Which declaration is most appropriate?

- A) `const total = 0;`
- B) `var total = 0;`
- C) `let total = 0;`
- D) `total = 0;`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `total` needs to be incremented (`total += price`), which is a reassignment. `const` prevents reassignment — the first `total += price` would throw `TypeError`.
- *Why B is incorrect:* `var` would work mechanically, but it is not modern best practice. `var` is function-scoped and allows re-declaration. `let` is the correct keyword for a variable that needs to be reassigned.
- *Why C is correct:* `let` is block-scoped and reassignable — exactly what is needed for an accumulator variable. This is the standard modern JavaScript pattern.
- *Why D is incorrect:* Assigning without a keyword creates an implicit global variable in non-strict mode, polluting the global scope. This is never correct.

---

### Question 11

What is the output of the following code?

```javascript
function outer() {
  let x = 10;
  function inner() {
    console.log(x);
  }
  inner();
}
outer();
```

- A) `ReferenceError: x is not defined`
- B) `undefined`
- C) `10`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `x` is declared in `outer`'s scope. Through the scope chain, `inner` can look up to its enclosing scope and find `x`. This is called **lexical scoping** (or closure). No error is thrown.
- *Why B is incorrect:* `x` has been assigned the value `10` before `inner` is called. There is no TDZ issue because `inner` is called after `x`'s declaration.
- *Why C is correct:* `inner` does not declare its own `x`, so the engine searches the scope chain and finds `x = 10` in `outer`'s scope. Lexical scoping allows inner functions to access variables from enclosing scopes.
- *Why D is incorrect:* `null` is not a default value for variables. `x` holds the number `10`.

---

### Question 12

Which of the following variable names is **syntactically invalid** in JavaScript?

- A) `_privateValue`
- B) `$element`
- C) `2ndAttempt`
- D) `isActive`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Leading underscores are valid in JavaScript identifiers. `_privateValue` is commonly used to signal a "private" variable by convention.
- *Why B is incorrect:* The dollar sign `$` is a valid identifier start character. `$element` is widely used in jQuery-based code.
- *Why C is correct:* Identifiers cannot start with a digit. `2ndAttempt` begins with `2`, making it a `SyntaxError`. It would need to be written as `secondAttempt` or `attempt2`.
- *Why D is incorrect:* `isActive` is a valid camelCase identifier — it starts with a letter and contains only alphanumeric characters.

---

### Question 13

What is the output of the following code?

```javascript
let a = 5;
{
  let a = 10;
  console.log(a);
}
console.log(a);
```

- A) `10` then `10`
- B) `5` then `5`
- C) `10` then `5`
- D) `SyntaxError: Identifier 'a' has already been declared`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `a` inside the inner block is a separate binding from the outer `a`. After the block closes, the inner `a` no longer exists and the outer `a` is restored to `5`.
- *Why B is incorrect:* Inside the block, the inner declaration of `let a = 10` shadows the outer `a`. The inner `console.log(a)` sees `10`, not `5`.
- *Why C is correct:* The inner block creates a new scope. `let a = 10` is a new binding that shadows the outer `a` within the block. Inside the block `a` is `10`; after the block closes, the outer `a = 5` is again in scope.
- *Why D is incorrect:* Re-declaring `let` in a **different** (nested) scope is valid. The `SyntaxError` for re-declaration only applies when using `let` twice in the **same** scope.

---

### Question 14

What does the following code output?

```javascript
const arr = [1, 2, 3];
arr.push(4);
console.log(arr.length);
```

- A) `3`
- B) `TypeError: Cannot read properties of undefined`
- C) `TypeError: Assignment to constant variable`
- D) `4`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `push(4)` adds a fourth element to the array, making its length `4`, not `3`.
- *Why B is incorrect:* `arr` is a valid array and `push` is a defined array method. No undefined-access error occurs.
- *Why C is incorrect:* `arr.push(4)` mutates the existing array — it does not reassign the `arr` binding. `const` only prevents `arr = [something_else]`. Calling methods on a `const` object or array is always permitted.
- *Why D is correct:* `push` adds an element to the end of the array. The array becomes `[1, 2, 3, 4]` with a length of `4`. `const` does not prevent this mutation.

---

### Question 15

A developer writes the following code at the top level of a browser script (not inside a function):

```javascript
var counter = 0;
```

Which additional statement is therefore `true`?

- A) `window.counter === 0`
- B) `window.counter === undefined`
- C) `counter` is block-scoped and not accessible outside this file
- D) `window.counter` throws `ReferenceError`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Global `var` declarations in a browser environment automatically become properties of the `window` object. After `var counter = 0` at the top level, `window.counter` evaluates to `0`.
- *Why B is incorrect:* `window.counter` is not `undefined` because the variable was declared and assigned to `0`. If it had not been declared at all, `window.counter` would be `undefined`.
- *Why C is incorrect:* `var` is function-scoped (or globally scoped), not block-scoped. There is no concept of "file scope" in browser JavaScript — global `var` declarations are accessible everywhere.
- *Why D is incorrect:* Accessing an undeclared property on an object like `window` returns `undefined`, not a `ReferenceError`. `ReferenceError` occurs when accessing an undeclared variable, not an undeclared object property.

---

### Question 16

What is the output of the following code?

```javascript
function test() {
  console.log(x);
  var x = 'hello';
  console.log(x);
}
test();
```

- A) `ReferenceError` then `hello`
- B) `hello` then `hello`
- C) `undefined` then `hello`
- D) `null` then `hello`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `var x` is hoisted inside `test`'s function scope and initialized to `undefined`. Accessing it before the assignment line returns `undefined`, not a `ReferenceError`.
- *Why B is incorrect:* The first `console.log(x)` runs before `x = 'hello'` executes. The declaration is hoisted but the assignment is not.
- *Why C is correct:* `var x` is hoisted to the top of `test`'s scope and initialized to `undefined`. The first `console.log` prints `undefined`. Then `x = 'hello'` runs and the second `console.log` prints `hello`.
- *Why D is incorrect:* Hoisted `var` variables are initialized to `undefined`, not `null`.

---

### Question 17

Which statement correctly describes a **global variable** declared with `let` at the top level of a browser script?

- A) It becomes a property of the `window` object, just like `var`
- B) It is accessible from any code in the same script but is not attached to `window`
- C) It is block-scoped to the `<script>` tag and inaccessible from other scripts on the same page
- D) It is garbage-collected after the script file finishes loading

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Only `var` declarations at the global level create `window` properties. `let` and `const` live in the global scope but are not attached to `window`. `window.myLetVar` would be `undefined` even if `let myLetVar = 5` exists globally.
- *Why B is correct:* Top-level `let` is in the global scope and is accessible from anywhere in the same script. It does not, however, become a property of `window`. This is an intentional design decision to prevent global namespace pollution.
- *Why C is incorrect:* While `let` is block-scoped, a top-level `let` declaration is not inside any block — it is in the global scope and is accessible to all code below it in the same execution context.
- *Why D is incorrect:* Variables in the global scope persist for the lifetime of the page. They are garbage-collected only when the page is unloaded.

---

### Question 18

What is the output of the following code?

```javascript
const PI = 3.14159;
const radius = 5;
const area = PI * radius * radius;
console.log(area.toFixed(2));
```

- A) `78.53975`
- B) `78.54`
- C) `TypeError: toFixed is not a function`
- D) `NaN`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `toFixed(2)` rounds the number to exactly 2 decimal places and returns a string. `3.14159 * 25 = 78.53975`, and `toFixed(2)` rounds to `78.54`.
- *Why B is correct:* `area` evaluates to `78.53975`. Calling `toFixed(2)` rounds to 2 decimal places, returning the string `"78.54"`. `console.log` prints it as `78.54`.
- *Why C is incorrect:* `area` is a number (the result of a multiplication), and all JavaScript numbers have access to `.toFixed()` through the `Number` prototype.
- *Why D is incorrect:* All operands are valid numbers. No `NaN` is produced.

---

### Question 19

Which of the following correctly describes the **Temporal Dead Zone (TDZ)**?

- A) The period after a `let` variable is declared and before it is reassigned
- B) The period from the start of a scope to the line where a `let` or `const` variable is declared
- C) The period after a `var` variable is declared but before the function containing it is called
- D) The period during which a `const` variable's object properties are immutable

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The TDZ ends at the declaration line, not at the reassignment line. After declaration, the variable is fully accessible.
- *Why B is correct:* The TDZ is the region from the beginning of the enclosing block (or global scope) up to — but not including — the `let` or `const` declaration statement. Accessing the variable in this zone throws `ReferenceError: Cannot access before initialization`.
- *Why C is incorrect:* The TDZ applies to `let` and `const`, not `var`. `var` has no TDZ — it is initialized to `undefined` and can be read (returning `undefined`) at any point after the scope is entered.
- *Why D is incorrect:* This describes nothing related to the TDZ. `const` object properties are not immutable by default — only the binding is constant.

---

### Question 20

What is the output of the following code?

```javascript
var x = 'global';

function showX() {
  var x = 'local';
  console.log(x);
}

showX();
console.log(x);
```

- A) `global` then `global`
- B) `local` then `local`
- C) `local` then `global`
- D) `global` then `local`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Inside `showX`, `var x = 'local'` creates a new function-scoped variable that shadows the global `x`. The function's `console.log` prints the local `x`, not the global one.
- *Why B is incorrect:* After `showX` returns, the local `x` is destroyed. The global `x` remains `'global'`.
- *Why C is correct:* Inside `showX`, the local `var x = 'local'` shadows the global `x`. The function prints `local`. After the function returns, only the global `x = 'global'` is in scope, so the second `console.log` prints `global`.
- *Why D is incorrect:* The inner function runs first (called on the second line), printing `local`. Then the outer `console.log(x)` runs, printing `global`. The order is local → global.
