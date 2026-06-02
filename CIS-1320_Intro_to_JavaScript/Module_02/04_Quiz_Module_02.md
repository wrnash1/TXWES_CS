# Quiz: Module 02 — Variables, Constants, and Scope

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
