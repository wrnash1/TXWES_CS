# Quiz: Module 03 — Data Types and Operators

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What does `typeof null` return in JavaScript?

- A) `'null'`
- B) `'undefined'`
- C) `'object'`
- D) `'boolean'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* One might expect `'null'` as the most logical return value, but JavaScript has never returned this. This is a known limitation of the language.
- *Why B is incorrect:* `typeof undefined` returns `'undefined'`. `null` and `undefined` are different values with different `typeof` results.
- *Why C is correct:* `typeof null === 'object'` is a historical bug from JavaScript's first implementation. It was never corrected because fixing it would break existing code that depends on this behavior. You must know it for the JSE exam.
- *Why D is incorrect:* `typeof true` and `typeof false` return `'boolean'`. `null` is not a boolean.

---

### Question 2

What is the output of the following code?

```javascript
console.log('1' + 2 + 3);
console.log(1 + 2 + '3');
```

- A) `'123'` then `'33'`
- B) `6` then `6`
- C) `'123'` then `6`
- D) `6` then `'33'`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* JavaScript evaluates `+` left-to-right. In `'1' + 2 + 3`: `'1' + 2` is string concatenation (`'12'`), then `'12' + 3` is string concatenation (`'123'`). In `1 + 2 + '3'`: `1 + 2` is numeric addition (`3`), then `3 + '3'` is string concatenation (`'33'`).
- *Why B is incorrect:* The presence of a string operand causes concatenation, not numeric addition, for all subsequent `+` operations to the right.
- *Why C is incorrect:* `1 + 2 + '3'` does not produce `6`. The first two operands (`1` and `2`) add to `3`, but then `3 + '3'` is string concatenation, producing `'33'`, not `6`.
- *Why D is incorrect:* `'1' + 2 + 3` does not produce `6`. The first operand is a string, making all subsequent `+` operations concatenations — producing `'123'`.

---

### Question 3

What is the result of `'5' - 3` in JavaScript?

- A) `'53'` — string concatenation
- B) `'2'` — string subtraction
- C) `2` — numeric subtraction with coercion
- D) `NaN` — cannot subtract from a string

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* String concatenation only occurs with the `+` operator when one operand is a string. The `-` operator does not concatenate strings.
- *Why B is incorrect:* The result is the number `2`, not the string `'2'`. The subtraction operator coerces the string `'5'` to the number `5` and performs numeric subtraction.
- *Why C is correct:* The `-`, `*`, `/`, and `%` operators always attempt to convert their operands to numbers. `'5'` is successfully coerced to `5`, and `5 - 3 = 2`.
- *Why D is incorrect:* `NaN` would result if the string could not be converted to a number (e.g., `'hello' - 3`). The string `'5'` is a valid numeric string and coerces successfully.

---

### Question 4

What is the output of the following code?

```javascript
console.log(0 == false);
console.log(0 === false);
```

- A) `true` then `true`
- B) `false` then `false`
- C) `true` then `false`
- D) `false` then `true`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `0 === false` is `false` because strict equality does not perform type coercion. `0` is a number and `false` is a boolean — different types, so `===` returns `false`.
- *Why B is incorrect:* `0 == false` is `true` because loose equality coerces both operands — `false` is converted to `0`, and `0 == 0` is `true`.
- *Why C is correct:* `0 == false` is `true` (loose equality coerces `false` to `0`). `0 === false` is `false` (strict equality — different types: number vs boolean).
- *Why D is incorrect:* This reverses the actual results. `==` produces `true` for `0 == false`, and `===` produces `false`.

---

### Question 5

Which of the following is NOT a falsy value in JavaScript?

- A) `0`
- B) `''`
- C) `'0'`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `0` is falsy. `Boolean(0)` returns `false`.
- *Why B is incorrect:* `''` (empty string) is falsy. `Boolean('')` returns `false`.
- *Why C is correct:* `'0'` is a non-empty string. Any non-empty string is truthy in JavaScript. `Boolean('0')` returns `true`. This is one of the most common exam traps — the string `'0'` looks like zero but it is truthy.
- *Why D is incorrect:* `null` is falsy. `Boolean(null)` returns `false`.

---

### Question 6

What is the output of the following code?

```javascript
console.log(null == undefined);
console.log(null === undefined);
```

- A) `false` then `false`
- B) `true` then `true`
- C) `false` then `true`
- D) `true` then `false`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `null == undefined` is `true` — these two values are loosely equal to each other by a special rule in the language specification.
- *Why B is incorrect:* `null === undefined` is `false` — `null` and `undefined` are different types, and strict equality requires matching types.
- *Why C is incorrect:* This reverses the actual results.
- *Why D is correct:* `null == undefined` is `true` (special loose equality rule — they loosely equal only each other). `null === undefined` is `false` (different types: `'null'` vs `'undefined'`).

---

### Question 7

What does `NaN === NaN` evaluate to?

- A) `true`
- B) `false`
- C) `undefined`
- D) `TypeError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `NaN` is specifically defined as not equal to anything — including itself. This is the one value in JavaScript that violates reflexive equality.
- *Why B is correct:* `NaN !== NaN` is one of JavaScript's deliberate design decisions. NaN represents an undefined numeric result, and two undefined results are not necessarily the same undefined result. To check for NaN, use `Number.isNaN()`.
- *Why C is incorrect:* The comparison evaluates to a boolean `false`, not `undefined`.
- *Why D is incorrect:* The comparison is syntactically valid and executes without error. It simply returns `false`.

---

### Question 8

What is the output of the following code?

```javascript
const result = 0 || 'default';
console.log(result);
```

- A) `0`
- B) `false`
- C) `'default'`
- D) `true`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `||` operator returns the first truthy operand. `0` is falsy, so `||` continues evaluating and returns the next operand.
- *Why B is incorrect:* `false` is not one of the operands. `||` returns one of its actual operands — not a converted boolean.
- *Why C is correct:* `||` evaluates left-to-right and returns the first truthy operand. `0` is falsy, so it is skipped. `'default'` is a non-empty string (truthy), so it is returned. The result is the string `'default'`, not the boolean `true`.
- *Why D is incorrect:* `||` returns one of its operands as-is — it does not convert the result to a boolean.

---

### Question 9

What is the result of `typeof NaN`?

- A) `'NaN'`
- B) `'undefined'`
- C) `'number'`
- D) `'string'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* There is no `typeof` result of `'NaN'`. `NaN` is a value of the `number` type.
- *Why B is incorrect:* `typeof undefined` returns `'undefined'`. `NaN` is a number type, not undefined.
- *Why C is correct:* `NaN` stands for "Not a Number" but it is technically of the `number` type. `typeof NaN === 'number'` is `true`. This is a deliberate quirk that frequently appears on the JSE exam.
- *Why D is incorrect:* `NaN` is not a string. `typeof 'hello'` returns `'string'`; `typeof NaN` returns `'number'`.

---

### Question 10

What is the output of the following code?

```javascript
console.log(Boolean([]));
console.log(Boolean({}));
console.log(Boolean(''));
console.log(Boolean('false'));
```

- A) `false`, `false`, `false`, `false`
- B) `false`, `false`, `false`, `true`
- C) `true`, `true`, `false`, `true`
- D) `true`, `false`, `false`, `true`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Empty arrays `[]` and empty objects `{}` are truthy in JavaScript. They are objects (non-primitive references), and any object reference is truthy regardless of its contents.
- *Why B is incorrect:* Same issue with `[]` and `{}` — both are truthy.
- *Why C is correct:* `Boolean([])` is `true` — an empty array is still an object reference, which is truthy. `Boolean({})` is `true` — same reason. `Boolean('')` is `false` — an empty string is the only falsy string. `Boolean('false')` is `true` — `'false'` is a non-empty string, so it is truthy.
- *Why D is incorrect:* `Boolean({})` is `true`, not `false`. An empty object is truthy.

---

### Question 11

What is the output of the following code?

```javascript
console.log(5 ** 3);
console.log(10 % 3);
```

- A) `15` then `1`
- B) `125` then `1`
- C) `125` then `3`
- D) `15` then `3`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `5 ** 3` is the exponentiation operator (ES2016): `5` raised to the power of `3` = `125`. `5 * 3 = 15`, which would be multiplication — a different operator.
- *Why B is correct:* `5 ** 3` evaluates to `125` (5³). `10 % 3` is the remainder/modulo operator: `10 ÷ 3 = 3` remainder `1`, so the result is `1`.
- *Why C is incorrect:* `10 % 3` is `1`, not `3`. The modulo operator returns the remainder, not the quotient.
- *Why D is incorrect:* Both values are wrong. `5 ** 3` is `125`, not `15`, and `10 % 3` is `1`, not `3`.

---

### Question 12

What is the value of `x` after the following code executes?

```javascript
let x = 10;
x += 5;
x *= 2;
x -= 3;
```

- A) `27`
- B) `30`
- C) `17`
- D) `22`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Step by step: `x = 10`, then `x += 5` → `x = 15`, then `x *= 2` → `x = 30`, then `x -= 3` → `x = 27`.
- *Why B is incorrect:* `30` is the value after `x *= 2`, but the final operation `x -= 3` reduces it to `27`.
- *Why C is incorrect:* This would result if only the last two operations were performed: `10 * 2 - 3 = 17`. But `x += 5` executes first, changing `x` to `15` before the multiplication.
- *Why D is incorrect:* This does not match any step in the sequence.

---

### Question 13

What is the output of the following code?

```javascript
console.log(Number(''));
console.log(Number(false));
console.log(Number(null));
console.log(Number(undefined));
```

- A) `0`, `0`, `0`, `0`
- B) `0`, `0`, `0`, `NaN`
- C) `NaN`, `0`, `0`, `0`
- D) `NaN`, `NaN`, `NaN`, `NaN`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Number(undefined)` returns `NaN`, not `0`. `undefined` cannot be meaningfully coerced to a number.
- *Why B is correct:* `Number('')` converts an empty string to `0`. `Number(false)` converts `false` to `0` (booleans: `false → 0`, `true → 1`). `Number(null)` converts `null` to `0`. `Number(undefined)` converts `undefined` to `NaN` — the only one of these four that returns `NaN`.
- *Why C is incorrect:* `Number('')` is `0`, not `NaN`. An empty string represents zero numerically.
- *Why D is incorrect:* Three of the four conversions succeed and return `0`.

---

### Question 14

What is the output of the following code?

```javascript
const x = 5;
console.log(x > 3 ? 'big' : 'small');
console.log(x < 3 ? 'big' : 'small');
```

- A) `'big'` then `'big'`
- B) `'small'` then `'small'`
- C) `'big'` then `'small'`
- D) `'small'` then `'big'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `x < 3` is `5 < 3`, which is `false`. The ternary returns the `else` branch `'small'` when the condition is false.
- *Why B is incorrect:* `x > 3` is `5 > 3`, which is `true`. The ternary returns the `then` branch `'big'` when the condition is true.
- *Why C is correct:* `5 > 3` is `true` → ternary returns `'big'`. `5 < 3` is `false` → ternary returns `'small'`.
- *Why D is incorrect:* This reverses the results. The ternary operator follows `condition ? valueIfTrue : valueIfFalse`.

---

### Question 15

What is the output of the following code?

```javascript
console.log(null == 0);
console.log(null == '');
console.log(null == false);
console.log(null == undefined);
```

- A) `true`, `true`, `true`, `true`
- B) `false`, `false`, `false`, `false`
- C) `false`, `false`, `false`, `true`
- D) `true`, `false`, `false`, `true`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `null` does not loosely equal `0`, `''`, or `false`. The ECMAScript spec defines a special case: `null` is only loosely equal to `undefined`, and to nothing else.
- *Why B is incorrect:* `null == undefined` is `true` by special rule.
- *Why C is correct:* According to the ECMAScript abstract equality algorithm, `null` is only loosely equal to `undefined`. All three comparisons with `0`, `''`, and `false` return `false` because no type coercion applies between `null` and non-null/undefined values.
- *Why D is incorrect:* `null == 0` is `false`. The special null/undefined rule does not extend to other falsy values.

---

### Question 16

What is the output of the following code?

```javascript
const a = 10;
const b = '10';
console.log(a == b);
console.log(a === b);
console.log(a !== b);
```

- A) `true`, `true`, `false`
- B) `true`, `false`, `true`
- C) `false`, `false`, `true`
- D) `false`, `true`, `false`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `a === b` is `false` because `a` is a number and `b` is a string — strict equality requires matching types.
- *Why B is correct:* `a == b` is `true` because `==` coerces `'10'` to `10` and `10 == 10` is `true`. `a === b` is `false` because strict equality requires same type (number vs string). `a !== b` is `true` because `a` and `b` are not strictly equal.
- *Why C is incorrect:* `a == b` is `true`, not `false`. Loose equality coerces `'10'` to a number.
- *Why D is incorrect:* `a === b` is `false`, and `a !== b` is `true` (the opposite of this answer).

---

### Question 17

Which expression correctly checks whether the variable `x` is `NaN`?

- A) `x === NaN`
- B) `x == NaN`
- C) `x !== x`
- D) Both C and the built-in `Number.isNaN(x)` are correct

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `NaN === NaN` is `false`. Strict equality with `NaN` always returns `false`. This check never identifies `NaN`.
- *Why B is incorrect:* `NaN == NaN` is also `false`. Neither loose nor strict equality identifies `NaN`.
- *Why C is incorrect:* While `x !== x` is a valid technique (NaN is the only value not equal to itself), it is not the only correct method. D includes C as part of its answer.
- *Why D is correct:* There are two reliable ways to test for NaN: `Number.isNaN(x)` (the modern, explicit built-in) and the self-inequality trick `x !== x`. Both are valid. Note that the older `isNaN()` function (without `Number.`) is unreliable because it coerces the argument first.

---

### Question 18

What is the result of `'hello'.length + 1`?

- A) `'hello1'`
- B) `6`
- C) `NaN`
- D) `TypeError: Cannot read properties of a string`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'hello'.length` returns the number `5`. `5 + 1` is numeric addition (both operands are numbers), so the result is `6`, not the string `'hello1'`.
- *Why B is correct:* `'hello'.length` is the number `5`. `5 + 1 = 6`. The `+` operator performs numeric addition because both operands are numbers.
- *Why C is incorrect:* There is no invalid numeric operation here. `NaN` only results from invalid numeric coercions (e.g., `'hello' - 1`), not from accessing `.length`.
- *Why D is incorrect:* JavaScript primitives can access properties via auto-boxing — the engine temporarily wraps the string in a `String` object to access `.length`. This is valid and produces a number.

---

### Question 19

What is the output of the following code?

```javascript
let count = 5;
console.log(count++);
console.log(count);
console.log(++count);
console.log(count);
```

- A) `5`, `6`, `7`, `7`
- B) `6`, `6`, `7`, `7`
- C) `5`, `5`, `7`, `7`
- D) `5`, `6`, `6`, `7`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `count++` (post-increment) returns the current value (`5`) and then increments `count` to `6`. The first `console.log` prints `5`. The second `console.log` prints `count`'s new value: `6`. `++count` (pre-increment) increments `count` to `7` first, then returns `7`. The third `console.log` prints `7`. The fourth `console.log` prints the unchanged `count`: `7`.
- *Why B is incorrect:* `count++` (post-increment) returns `5` before incrementing, not `6`.
- *Why C is incorrect:* After `count++`, `count` is `6`. The second `console.log` prints `6`, not `5`.
- *Why D is incorrect:* `++count` increments to `7` before returning, so the third `console.log` prints `7`, not `6`.

---

### Question 20

What is the output of the following code?

```javascript
const result = 10 > 5 && 3 < 7 && 'hello';
console.log(result);
```

- A) `true`
- B) `false`
- C) `'hello'`
- D) `1`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `&&` operator does not convert its result to a boolean. It returns the last evaluated operand when all conditions are truthy.
- *Why B is incorrect:* All three operands are truthy — `10 > 5` is `true`, `3 < 7` is `true`, and `'hello'` is a non-empty string (truthy). There is no falsy value to short-circuit to.
- *Why C is correct:* `&&` evaluates left-to-right and returns the first falsy value it encounters, or the last value if all are truthy. `10 > 5` is `true` (continues), `3 < 7` is `true` (continues), `'hello'` is truthy and is the last operand — so `&&` returns `'hello'`. The variable `result` holds the string `'hello'`.
- *Why D is incorrect:* `&&` does not return `1`. It returns the actual operand value — in this case, the string `'hello'`.
