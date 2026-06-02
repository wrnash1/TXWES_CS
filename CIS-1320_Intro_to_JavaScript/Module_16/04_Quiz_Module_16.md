# Quiz: Module 16 — Final Exam Prep & JSE Certification Review

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. This quiz covers all 15 modules and mirrors the style of JSE certification exam questions.

---

### Question 1

What does the following code log?

```javascript
var x = 1;

function test() {
  console.log(x);
  var x = 2;
}

test();
```

- A) `1`
- B) `2`
- C) `undefined`
- D) `ReferenceError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `x` inside the function shadows the outer `x`. The inner `var x` is hoisted to the top of `test()`, so the function's `x` exists at the time of `console.log` — but only its declaration is hoisted, not the assignment. Reading it before the assignment returns `undefined`.
- *Why B is incorrect:* The value `2` is assigned after the `console.log` line. Hoisting moves the declaration up, not the assignment.
- *Why C is correct:* `var` hoisting: inside `test()`, the declaration `var x` is hoisted to the top of the function scope. The function behaves as if it were written `var x; console.log(x); x = 2;`. At the time of `console.log`, `x` has been declared but not yet assigned — its value is `undefined`.
- *Why D is incorrect:* `ReferenceError` would occur if `x` had not been declared at all. Because `var x = 2` is inside the function, the declaration is hoisted and `x` exists in scope — it just has not been assigned yet.

---

### Question 2

What is the output of this code?

```javascript
const result = [1, 2, 3].forEach(n => n * 2);
console.log(result);
```

- A) `[2, 4, 6]`
- B) `[1, 2, 3]`
- C) `undefined`
- D) `6`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `[2, 4, 6]` would be the result of `map`, not `forEach`. `map` returns a new array of transformed values.
- *Why B is incorrect:* `forEach` does not return the original array. It returns `undefined` regardless of what the callback does.
- *Why C is correct:* `forEach` always returns `undefined`. The callback `n => n * 2` computes a value but that value is discarded — `forEach` does not collect callback return values. `result` receives the return value of `forEach`, which is `undefined`.
- *Why D is incorrect:* `6` would imply `reduce` with no initial value, or some other accumulation — not `forEach`. No accumulation happens here.

---

### Question 3

Which value is falsy in JavaScript?

- A) `'false'`
- B) `[]`
- C) `0`
- D) `{}`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `'false'` is a non-empty string. All non-empty strings are truthy, even if the string spells out the word "false".
- *Why B is incorrect:* `[]` is an empty array. Arrays are objects — all objects (including empty ones) are truthy in JavaScript.
- *Why C is correct:* The six falsy values in JavaScript are: `false`, `0`, `''` (empty string), `null`, `undefined`, and `NaN`. `0` is on this list. `-0` and `0n` (BigInt zero) are also falsy. Any numeric zero evaluates to `false` in a boolean context.
- *Why D is incorrect:* `{}` is an empty object. Like all objects, it is truthy — even an object with no properties.

---

### Question 4

What is the output of this code?

```javascript
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound.`; }
}

class Dog extends Animal {
  speak() { return `${this.name} barks.`; }
}

const d = new Dog('Rex');
console.log(d instanceof Animal);
console.log(d.speak());
```

- A) `false` and `'Rex makes a sound.'`
- B) `true` and `'Rex barks.'`
- C) `true` and `'Rex makes a sound.'`
- D) `false` and `'Rex barks.'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `d instanceof Animal` is `true` because `Dog extends Animal` — the prototype chain includes `Animal.prototype`. And `Dog` overrides `speak()`, so `d.speak()` calls the `Dog` version.
- *Why B is correct:* `instanceof` checks the prototype chain. `new Dog()` creates an instance that inherits from both `Dog.prototype` and `Animal.prototype`, so `d instanceof Animal` is `true`. `Dog` overrides `speak()` with its own version, so `d.speak()` returns `'Rex barks.'` — the subclass method, not the parent's.
- *Why C is incorrect:* `d.speak()` calls the overridden `Dog.speak()`, not `Animal.speak()`. JavaScript's method resolution always starts at the most-specific class in the prototype chain.
- *Why D is incorrect:* `d instanceof Animal` is `true`, not `false`. Inheritance means every `Dog` is also an `Animal`.

---

### Question 5

A developer writes:

```javascript
const btn = document.querySelector('#submit');

btn.addEventListener('click', () => {
  console.log('clicked');
});

btn.addEventListener('click', () => {
  console.log('also clicked');
});
```

How many times is `console.log` called when the button is clicked once?

- A) Once — the second `addEventListener` overwrites the first
- B) Twice — both listeners fire
- C) Zero — arrow functions cannot be used as event listeners
- D) Once — only the last listener registered fires

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `addEventListener` does not overwrite previous listeners. Each call registers an independent listener. Overwriting behavior belongs to the `onclick` property — `btn.onclick = fn` replaces any previously assigned `onclick` handler.
- *Why B is correct:* `addEventListener` appends a new listener each time it is called. Both handlers are registered on the same click event, and both fire when the button is clicked. The button has two independent listeners and both execute.
- *Why C is incorrect:* Arrow functions are fully valid as event listener callbacks. The restriction on arrow functions is that they do not have their own `this` — but they can be passed to `addEventListener` without issue.
- *Why D is incorrect:* All registered listeners fire, not just the last one. There is no "last one wins" behavior with `addEventListener`.

---

### Question 6

What does `Promise.allSettled([p1, p2, p3])` return when `p2` rejects?

- A) A rejected Promise with `p2`'s reason
- B) A fulfilled Promise with only the results of `p1` and `p3`
- C) A fulfilled Promise with an array containing the outcome of every Promise
- D) `undefined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.allSettled` never rejects. Unlike `Promise.all`, it does not fail fast. It waits for every Promise to settle and always resolves.
- *Why B is incorrect:* `allSettled` does not filter out failures. It returns results for all input Promises — both fulfilled and rejected — without filtering.
- *Why C is correct:* `Promise.allSettled` always fulfills with an array where each entry is either `{ status: 'fulfilled', value: ... }` or `{ status: 'rejected', reason: ... }`. The array contains exactly one entry per input Promise, regardless of outcomes. The caller inspects each entry's `status` to handle successes and failures individually.
- *Why D is incorrect:* `allSettled` returns a Promise — it is a combinator, and combinators always return Promises. The result is not `undefined`.

---

### Question 7

What is logged by this code?

```javascript
async function getValue() {
  return 42;
}

const result = getValue();
console.log(typeof result);
```

- A) `'number'`
- B) `'object'`
- C) `42`
- D) `'undefined'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `result` is not the number `42`. `getValue()` is an `async` function. All `async` functions return a Promise, regardless of what the `return` statement specifies. The number `42` is the resolved value of the Promise — not the direct return value.
- *Why B is correct:* `async` functions always return a Promise. `typeof result` is `'object'` because Promises are objects. To get `42`, you would need `await getValue()` inside another async function, or `.then(val => ...)`.
- *Why C is incorrect:* `console.log(typeof result)` logs the type string, not the value. Even if it logged `result`, it would log a Promise object, not `42`.
- *Why D is incorrect:* `typeof result` is `'object'`, not `'undefined'`. The function call returns a Promise, which is a defined value.

---

### Question 8

Which code pattern correctly handles the case where `step2` depends on the result of `step1`, but `step3` and `step4` are independent of each other and can run simultaneously?

- A) `await step1(); await step2(); await step3(); await step4();`
- B) `await Promise.all([step1(), step2(), step3(), step4()]);`
- C) `const r1 = await step1(); const r2 = await step2(r1); await Promise.all([step3(), step4()]);`
- D) `Promise.race([step1(), step2(), step3(), step4()]);`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Sequential `await` for all four steps forces step3 to wait for step2 and step4 to wait for step3, even though step3 and step4 are independent. This is unnecessarily slow.
- *Why B is incorrect:* `Promise.all([step1(), step2(), step3(), step4()])` starts all four simultaneously. But step2 needs step1's result — it cannot start until step1 completes. Running step2 before step1 finishes would pass no result to step2.
- *Why C is correct:* Await step1 (required first). Pass its result to step2 and await step2 (dependent). Then use `Promise.all` to run step3 and step4 concurrently (independent). This honors the dependency and exploits the independence for maximum performance.
- *Why D is incorrect:* `Promise.race` returns only the first result and discards all others. It does not collect all four results, and it does not respect the dependency between step1 and step2.

---

### Question 9

What is the output of this code?

```javascript
const obj = { a: 1 };
const copy = { ...obj, b: 2 };
obj.a = 99;
console.log(copy.a);
```

- A) `99`
- B) `1`
- C) `undefined`
- D) A `TypeError` is thrown

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Spread creates a shallow copy — it copies the current values, not references to the original properties. At the time of `{ ...obj, b: 2 }`, `obj.a` is `1`. That value `1` is copied into `copy`. Later changes to `obj.a` do not affect `copy.a`.
- *Why B is correct:* The spread operator copies the values of `obj`'s properties into the new object at the time of the spread. `copy.a` receives the value `1`. When `obj.a` is later changed to `99`, `copy` is unaffected — it holds an independent copy of the primitive value.
- *Why C is incorrect:* `copy.a` is `1`, not `undefined`. The property `a` was copied into `copy` during the spread.
- *Why D is incorrect:* Nothing throws here. Spreading an object and later modifying the original are both valid operations.

---

### Question 10

A developer writes this custom error class. What is the value of `err.name`?

```javascript
class NetworkError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    // no this.name assignment
  }
}

const err = new NetworkError('Not found', 404);
console.log(err.name);
```

- A) `'NetworkError'`
- B) `'Error'`
- C) `undefined`
- D) `404`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `err.name` would be `'NetworkError'` only if the constructor explicitly set `this.name = 'NetworkError'`. The class declaration name does not automatically set the `name` property — it must be assigned manually.
- *Why B is correct:* When a class extends `Error` without setting `this.name`, the `name` property is inherited from `Error.prototype.name`, which has the default value `'Error'`. The subclass name is not inferred from the class keyword. This is why every custom error constructor should include `this.name = 'NetworkError'` (or the appropriate class name) explicitly.
- *Why C is incorrect:* `name` is not `undefined`. The property exists on `Error.prototype` with the value `'Error'`, and it is inherited by all subclasses that do not override it.
- *Why D is incorrect:* `404` is the value of `this.statusCode`, a custom property set in the constructor. It has no relation to `this.name`.
