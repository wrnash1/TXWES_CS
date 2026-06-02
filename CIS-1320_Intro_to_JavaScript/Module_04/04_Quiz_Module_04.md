# Quiz: Module 04 — Control Flow and Conditionals

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
