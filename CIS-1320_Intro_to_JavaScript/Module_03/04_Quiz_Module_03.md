# Quiz: Module 03 — Data Types and Operators

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
