# Quiz: Module 04 — Control Flow and Conditionals

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the output of the following code?

```javascript
const score = 85;

if (score >= 90) {
  console.log('A');
} else if (score >= 80) {
  console.log('B');
} else if (score >= 70) {
  console.log('C');
} else {
  console.log('F');
}
```

- A) `A`
- B) `B`
- C) `B` then `C`
- D) `B` then `C` then `F`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `85 >= 90` is `false`, so the first branch is skipped.
- *Why B is correct:* The engine checks conditions in order. `85 >= 90` is `false` (skip). `85 >= 80` is `true` — the `B` block runs and the entire `if/else if/else` chain ends. No further conditions are evaluated.
- *Why C is incorrect:* In an `if/else if/else` chain, only the first matching branch executes. Once `score >= 80` is satisfied, the remaining `else if` and `else` blocks are skipped entirely.
- *Why D is incorrect:* Same reason — only one branch runs in a single `if/else if/else` chain.

---

### Question 2

What is the output of the following code?

```javascript
const day = 2;

switch (day) {
  case 1:
    console.log('Monday');
  case 2:
    console.log('Tuesday');
  case 3:
    console.log('Wednesday');
  default:
    console.log('Unknown');
}
```

- A) `Tuesday`
- B) `Tuesday` then `Wednesday`
- C) `Tuesday` then `Wednesday` then `Unknown`
- D) `Unknown`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* There are no `break` statements in any case. After `case 2` matches and runs, execution falls through to `case 3` and then `default`.
- *Why B is incorrect:* Fall-through continues past `case 3` into `default` because neither `case 3` nor `default` have `break` statements either.
- *Why C is correct:* `day === 2` matches `case 2`, printing `'Tuesday'`. Without a `break`, execution falls through to `case 3` (prints `'Wednesday'`) and then to `default` (prints `'Unknown'`). All three execute.
- *Why D is incorrect:* `default` does not run first. The switch engine matches `case 2` first, then falls through to subsequent cases including `default`.

---

### Question 3

What is the output of the following code?

```javascript
let x = 10;

if (x = 5) {
  console.log('block ran');
}

console.log(x);
```

- A) Nothing prints — the condition is false
- B) `block ran` then `10`
- C) `block ran` then `5`
- D) `SyntaxError: invalid assignment in condition`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `x = 5` is an assignment expression, not a comparison. It assigns `5` to `x` and evaluates to `5`. Since `5` is truthy, the block runs.
- *Why B is incorrect:* The assignment `x = 5` permanently changes `x` from `10` to `5`. After the `if` block, `x` is `5`, not `10`.
- *Why C is correct:* `if (x = 5)` performs an assignment — `x` becomes `5` and the expression evaluates to `5` (truthy). The block runs and prints `'block ran'`. Then `console.log(x)` prints `5` because `x` was overwritten.
- *Why D is incorrect:* JavaScript allows assignments inside conditions — it is not a syntax error. ESLint warns on this pattern, but the language itself executes it silently.

---

### Question 4

What does the following expression evaluate to?

```javascript
const age = 20;
const result = age >= 18 ? 'adult' : 'minor';
```

- A) `true`
- B) `false`
- C) `'adult'`
- D) `'minor'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The ternary operator does not return the boolean result of the condition. It returns one of its two value operands — the one selected by whether the condition is truthy.
- *Why B is incorrect:* Same reason — `false` is not one of the value operands.
- *Why C is correct:* `age >= 18` evaluates to `true` (20 >= 18), so the ternary returns the value after `?`, which is `'adult'`.
- *Why D is incorrect:* `'minor'` is returned when the condition is `false`. Since `20 >= 18` is `true`, `'minor'` is not returned.

---

### Question 5

Which `switch` case matches the following expression?

```javascript
const val = '5';

switch (val) {
  case 5:
    console.log('number five');
    break;
  case '5':
    console.log('string five');
    break;
  default:
    console.log('no match');
}
```

- A) `case 5` — `switch` coerces types like `==`
- B) `case '5'` — `switch` uses strict equality
- C) Both `case 5` and `case '5'` run
- D) `default` — `switch` does not match string values

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Unlike the `==` operator, `switch` uses **strict equality (`===`)** for case comparisons. The string `'5'` does not strictly equal the number `5`.
- *Why B is correct:* `switch` compares using `===`. `val` is the string `'5'`. `case 5` (number) fails — different type. `case '5'` (string) passes — same type and value. `'string five'` is printed.
- *Why C is incorrect:* Only one case can match. After `case '5'` runs and hits `break`, the switch exits.
- *Why D is incorrect:* `switch` can match strings. The `default` only runs when no case matches — here `case '5'` matches.

---

### Question 6

What is the output of the following code?

```javascript
const count = 0;
console.log(count || 'empty');
console.log(count ?? 'empty');
```

- A) `'empty'` then `'empty'`
- B) `0` then `0`
- C) `'empty'` then `0`
- D) `0` then `'empty'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `??` operator only provides the fallback when the left operand is `null` or `undefined`. `0` is neither, so `??` returns `0`.
- *Why B is incorrect:* `||` treats `0` as falsy and returns the right operand `'empty'`.
- *Why C is correct:* `count || 'empty'` — `0` is falsy, so `||` returns `'empty'`. `count ?? 'empty'` — `0` is not `null` or `undefined`, so `??` returns `0`.
- *Why D is incorrect:* This reverses the results. `||` returns `'empty'` (not `0`), and `??` returns `0` (not `'empty'`).

---

### Question 7

What is the output of the following code?

```javascript
const user = null;
const name = user && user.name;
console.log(name);
```

- A) `undefined`
- B) `null`
- C) `TypeError: Cannot read properties of null`
- D) `''`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `undefined` would result if `user` were an object without a `name` property. Here `user` is `null`, so the `&&` short-circuits before accessing `.name`.
- *Why B is correct:* `&&` evaluates left-to-right. `user` is `null` (falsy), so `&&` short-circuits immediately and returns `null` — the first falsy operand. `user.name` is never evaluated, so no `TypeError` occurs.
- *Why C is incorrect:* The short-circuit behavior of `&&` prevents the property access. If `user` were `null` and `&&` were not used (`null.name` directly), that would throw a `TypeError`. The guard pattern prevents it.
- *Why D is incorrect:* `&&` returns one of its operands, not an empty string. The returned value here is `null`.

---

### Question 8

A developer wants to display a default message when `username` is an empty string. Which approach correctly uses `??` for this purpose?

```javascript
const username = '';
```

- A) `const display = username ?? 'Guest';` — displays `'Guest'`
- B) `const display = username || 'Guest';` — displays `'Guest'`
- C) `const display = username ?? 'Guest';` — displays `''`
- D) Both A and B display `'Guest'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `??` only triggers when the left operand is `null` or `undefined`. An empty string `''` is neither — it is a valid string value. So `'' ?? 'Guest'` returns `''`, not `'Guest'`.
- *Why B is correct:* `||` treats `''` as falsy and returns `'Guest'`. If the intent is to replace any empty/falsy username with a default, `||` is the correct operator.
- *Why C is correct as a statement but wrong as the answer:* Option C correctly describes what `??` does with an empty string (returns `''`). However, if the goal is to display `'Guest'` for an empty username, `??` is the wrong tool. The question asks for the approach that displays `'Guest'`.
- *Why D is incorrect:* Only `||` displays `'Guest'` for an empty string. `??` returns `''` because `''` is not `null` or `undefined`.

---

### Question 9

What is the output of the following code?

```javascript
const hour = 14;

if (hour < 12) {
  console.log('morning');
} else if (hour < 18) {
  console.log('afternoon');
} else {
  console.log('evening');
}
```

- A) `morning`
- B) `afternoon`
- C) `evening`
- D) `morning` then `afternoon`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `14 < 12` is `false`, so the `morning` branch is skipped.
- *Why B is correct:* `14 < 12` is `false` (skip). `14 < 18` is `true` — `'afternoon'` is printed and the chain ends.
- *Why C is incorrect:* `evening` runs only when `hour >= 18`. Since `14 < 18` is true, the `afternoon` branch fires first.
- *Why D is incorrect:* Only one branch runs. After `hour < 18` matches, the remaining `else` block is never evaluated.

---

### Question 10

Which of the following is the most appropriate use of the ternary operator?

- A) Assigning one of two values to a variable based on a single condition
- B) Implementing a multi-branch grade scale with five possible outcomes
- C) Executing a block of code with multiple statements when a condition is true
- D) Iterating over an array and processing each element

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The ternary operator is an expression — it produces a value. It is ideal for simple two-branch decisions that assign a value: `const label = count === 1 ? 'item' : 'items'`. This is concise and readable.
- *Why B is incorrect:* Multi-branch logic with five outcomes requires `if/else if/else` or `switch`. Nested ternaries for five branches are technically valid but nearly impossible to read and are considered poor practice.
- *Why C is incorrect:* The ternary operator is for value-producing expressions, not for executing multi-statement blocks. When you need to run multiple statements, use `if/else`.
- *Why D is incorrect:* That describes a loop (`for`, `forEach`), not a conditional operator.

---

### Question 11

What is the output of the following code?

```javascript
const x = 15;

switch (true) {
  case x < 10:
    console.log('small');
    break;
  case x < 20:
    console.log('medium');
    break;
  default:
    console.log('large');
}
```

- A) `small`
- B) `medium`
- C) `large`
- D) `SyntaxError — switch cannot use boolean expressions`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `x < 10` is `15 < 10` which is `false`. `switch (true)` compares `true` against each case using `===`. `false === true` does not match.
- *Why B is correct:* `switch (true)` is a valid pattern. The switch expression is `true`. `case x < 10` evaluates to `false === true` (no match). `case x < 20` evaluates to `true === true` (match) — `'medium'` prints and `break` exits.
- *Why C is incorrect:* `case x < 20` matches before reaching `default`, so `default` is never executed.
- *Why D is incorrect:* `switch (true)` is perfectly valid JavaScript. The switch expression can be any expression that evaluates to a value.

---

### Question 12

What is the output of the following code?

```javascript
const grade = 'B';

switch (grade) {
  case 'A':
  case 'B':
    console.log('Honor roll');
    break;
  case 'C':
    console.log('Satisfactory');
    break;
  default:
    console.log('See advisor');
}
```

- A) `Honor roll` then `Satisfactory`
- B) `See advisor`
- C) `Honor roll`
- D) `Satisfactory`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `break` after `'Honor roll'` exits the switch. `'Satisfactory'` is never reached.
- *Why B is incorrect:* `grade` is `'B'`, which falls into the `case 'A': case 'B':` group. `'See advisor'` is the `default` branch and is not reached.
- *Why C is correct:* `case 'A'` has no code and no `break` — it falls through to `case 'B'`. This is intentional fall-through used to group multiple matching values. `grade === 'B'` matches `case 'B'`, so execution reaches `console.log('Honor roll')` then hits `break`.
- *Why D is incorrect:* `case 'C'` does not match `'B'`.

---

### Question 13

What is the output of the following code?

```javascript
let result = '';

if (false) {
  result = 'A';
} else if (false) {
  result = 'B';
} else if (true) {
  result = 'C';
} else {
  result = 'D';
}

console.log(result);
```

- A) `'A'`
- B) `'D'`
- C) `'C'`
- D) `'B'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The first condition is `false`, so that branch is skipped.
- *Why B is incorrect:* `'D'` is the `else` fallback that only runs when all prior conditions are false. The third condition `true` matches first.
- *Why C is correct:* The engine evaluates each condition in order. The first two are `false` (skipped). The third is `true` — `result = 'C'` runs and the chain ends.
- *Why D is incorrect:* The second condition is `false`, so `result = 'B'` is skipped.

---

### Question 14

A developer writes the following conditional. What potential bug does it contain?

```javascript
const score = 72;
if (score >= 70);
  console.log('Passing');
```

- A) `SyntaxError` — a semicolon cannot follow a condition
- B) `console.log('Passing')` always runs regardless of the condition
- C) `console.log('Passing')` never runs because the condition has no body
- D) The code works correctly and only prints when `score >= 70`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A semicolon after an `if` condition is not a syntax error. It creates an `if` statement with an empty body (the semicolon is the body).
- *Why B is correct:* `if (score >= 70);` creates an `if` statement whose body is the empty statement `;`. The `console.log` on the next line is not part of the `if` block — it is a separate statement that always executes unconditionally, regardless of the score.
- *Why C is incorrect:* `console.log('Passing')` does run — always — because it is outside the (empty) `if` body.
- *Why D is incorrect:* The code does not behave correctly. `console.log` runs for every score, including scores below 70.

---

### Question 15

What is the output of the following code?

```javascript
const a = 5;
const b = 10;
const c = a > 3 ? (b > 8 ? 'both' : 'only a') : 'neither';
console.log(c);
```

- A) `'only a'`
- B) `'neither'`
- C) `'both'`
- D) `SyntaxError — ternary operators cannot be nested`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The inner condition `b > 8` is `10 > 8` which is `true`. The inner ternary returns `'both'`, not `'only a'`.
- *Why B is incorrect:* `a > 3` is `5 > 3` which is `true`. The outer `else` branch (`'neither'`) is not reached.
- *Why C is correct:* `a > 3` is `true`, so the outer ternary evaluates the nested ternary. `b > 8` is `true`, so the inner ternary returns `'both'`. `c` is `'both'`.
- *Why D is incorrect:* Nested ternary operators are valid JavaScript syntax. They are generally discouraged for readability but are syntactically correct and commonly tested.

---

### Question 16

What is the output of the following code?

```javascript
const user = { name: 'Alice', age: null };
const displayAge = user.age ?? 'Not provided';
console.log(displayAge);
```

- A) `null`
- B) `'Not provided'`
- C) `undefined`
- D) `0`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `user.age` is `null`, which triggers the `??` operator to return the right-hand fallback.
- *Why B is correct:* `user.age` is `null`. The nullish coalescing operator `??` returns the right-hand operand when the left is `null` or `undefined`. So `displayAge` is `'Not provided'`.
- *Why C is incorrect:* `undefined` would be the result if `user.age` were not a property at all (undeclared property returns `undefined`). Here it is explicitly set to `null`.
- *Why D is incorrect:* `0` is not involved anywhere in this code.

---

### Question 17

What is the output of the following code?

```javascript
const isAdmin = true;
const isLoggedIn = false;

if (isAdmin && isLoggedIn) {
  console.log('Admin access');
} else if (isAdmin || isLoggedIn) {
  console.log('Partial access');
} else {
  console.log('No access');
}
```

- A) `'Admin access'`
- B) `'No access'`
- C) `'Partial access'`
- D) `'Admin access'` then `'Partial access'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `isAdmin && isLoggedIn` is `true && false` which is `false`. The first branch is skipped.
- *Why B is incorrect:* `isAdmin || isLoggedIn` is `true || false` which is `true`. The `else if` branch fires before reaching `else`.
- *Why C is correct:* `true && false` is `false` (skip first branch). `true || false` is `true` (match second branch) → prints `'Partial access'` and exits.
- *Why D is incorrect:* Only one branch runs in an `if/else if/else` chain.

---

### Question 18

Which of the following correctly describes the optional chaining operator `?.`?

- A) It converts `null` or `undefined` to `0` before accessing a property
- B) It accesses a property and returns `undefined` (instead of throwing `TypeError`) if the left side is `null` or `undefined`
- C) It is equivalent to `??` and only triggers when the left side is null or undefined
- D) It checks whether a property exists on an object and returns `true` or `false`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `?.` does not convert values. It short-circuits — if the left side is `null` or `undefined`, the whole expression returns `undefined` without attempting the property access.
- *Why B is correct:* `obj?.prop` safely accesses `prop` on `obj`. If `obj` is `null` or `undefined`, the expression evaluates to `undefined` instead of throwing `TypeError: Cannot read properties of null`. This is called optional chaining.
- *Why C is incorrect:* `?.` and `??` are different operators. `?.` is for safe property access. `??` is for providing a fallback value. They are often used together: `obj?.prop ?? 'default'`.
- *Why D is incorrect:* That describes the `in` operator (`'prop' in obj`). `?.` does not return a boolean.

---

### Question 19

What is the output of the following code?

```javascript
const items = [];

if (items) {
  console.log('has items');
} else {
  console.log('no items');
}

if (items.length) {
  console.log('array has content');
} else {
  console.log('array is empty');
}
```

- A) `'no items'` then `'array is empty'`
- B) `'has items'` then `'array has content'`
- C) `'has items'` then `'array is empty'`
- D) `'no items'` then `'array has content'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An empty array `[]` is truthy. `if (items)` evaluates to `true`, so `'has items'` prints.
- *Why B is incorrect:* `items.length` is `0` for an empty array. `0` is falsy, so the `else` branch prints `'array is empty'`.
- *Why C is correct:* `items` is an empty array — a truthy object reference. `if (items)` is `true` → `'has items'`. `items.length` is `0` — falsy. `if (items.length)` is `false` → `'array is empty'`. This is the correct pattern for checking if an array actually contains elements.
- *Why D is incorrect:* `items` is truthy, so `'no items'` never prints.

---

### Question 20

What is the output of the following code?

```javascript
function getDiscount(isMember, totalSpend) {
  if (isMember && totalSpend > 100) return 20;
  if (isMember || totalSpend > 200) return 10;
  return 0;
}

console.log(getDiscount(true, 150));
console.log(getDiscount(false, 250));
console.log(getDiscount(false, 50));
```

- A) `20`, `10`, `0`
- B) `10`, `10`, `0`
- C) `20`, `20`, `0`
- D) `20`, `0`, `0`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* First call: `isMember=true, totalSpend=150` — `true && 150>100` is `true` → return `20`. Second call: `isMember=false, totalSpend=250` — first condition `false && ...` is `false` (skip). Second condition `false || 250>200` is `false || true` = `true` → return `10`. Third call: `isMember=false, totalSpend=50` — both conditions are `false` → return `0`.
- *Why B is incorrect:* The first call satisfies `isMember && totalSpend > 100` and returns `20`, not `10`.
- *Why C is incorrect:* The second call does not satisfy `isMember && totalSpend > 100` (`false && true` = `false`). It falls to the second condition and returns `10`, not `20`.
- *Why D is incorrect:* The second call returns `10` because `totalSpend > 200` satisfies the `||` condition.
