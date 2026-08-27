# Quiz: Module 16 — Final Exam Prep & JSE Certification Review

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. This quiz covers all 15 modules and mirrors the style of JSE certification exam questions. Each question is worth 5 points (20 questions × 5 points = 100 points).

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

---

### Question 11

What does this code log?

```javascript
function makeAdder(x) {
  return function(y) {
    return x + y;
  };
}

const add5 = makeAdder(5);
console.log(add5(3));
console.log(add5(10));
```

- A) `8` then `15`
- B) `8` then `8`
- C) `undefined` then `undefined`
- D) A `ReferenceError` is thrown on the second call

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `makeAdder(5)` returns an inner function that closes over `x = 5`. Each call to `add5` adds `5` to its argument using the closed-over `x`. `add5(3)` returns `5 + 3 = 8`. `add5(10)` returns `5 + 10 = 15`. The closure captures `x` by reference to the binding, but since `x` never changes after `makeAdder` returns, both calls produce the expected sums.
- *Why B is incorrect:* `add5(10)` returns `15`, not `8`. The closure captures `x = 5` permanently — the outer function's scope is retained, and `x` is `5` for every call to `add5`.
- *Why C is incorrect:* `x` is captured in the closure and remains accessible. Neither call returns `undefined`.
- *Why D is incorrect:* Closures persist as long as the inner function exists. `x` is accessible on every call to `add5` without error.

---

### Question 12

What is the output of this code?

```javascript
const arr = [1, 2, 3];
const result = arr.slice(1);
arr.push(4);
console.log(result);
```

- A) `[2, 3, 4]`
- B) `[2, 3]`
- C) `[1, 2, 3]`
- D) `[1, 2, 3, 4]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `slice` creates a new independent array at the time it is called. Adding `4` to `arr` afterward has no effect on `result`.
- *Why B is correct:* `arr.slice(1)` returns a new array containing elements from index 1 to the end: `[2, 3]`. This is a shallow copy — it is entirely independent of `arr`. Subsequent mutations of `arr` (like `push(4)`) do not affect `result`.
- *Why C is incorrect:* `slice(1)` starts at index 1, not index 0. The element `1` is not included.
- *Why D is incorrect:* `result` was created before `push(4)`. `slice` does not maintain a live reference to `arr`.

---

### Question 13

A `<ul id="list">` contains many `<li>` elements that are added dynamically. Which approach correctly handles clicks on any `<li>` — including ones added after the listener is registered?

- A) `document.querySelectorAll('li').forEach(li => li.addEventListener('click', handler));`
- B) `document.querySelector('#list').addEventListener('click', e => { if (e.target.closest('li')) handler(e); });`
- C) `document.addEventListener('click', handler);`
- D) `document.querySelector('#list').onclick = handler;`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `querySelectorAll` captures only the `<li>` elements that exist at the time of the call. Elements added later have no listener. This approach requires re-registering listeners every time new elements are added.
- *Why B is correct:* Attaching the listener to the `#list` parent exploits event bubbling — clicks on any child `<li>` bubble up to the list. `e.target.closest('li')` confirms the click originated inside an `<li>` (even if the actual target is a nested child). Because the listener is on the parent, all future `<li>` elements are covered automatically.
- *Why C is incorrect:* Attaching to `document` works but is too broad — every click anywhere on the page triggers the handler. Delegating to the closest relevant ancestor is the preferred pattern.
- *Why D is incorrect:* `onclick` is a property, not `addEventListener`. Assigning to it replaces any previous handler and only handles one listener. It also does not filter to `<li>` clicks — any click on the list fires `handler`.

---

### Question 14

What is the output of this code?

```javascript
const obj = { a: 1, b: { c: 2 } };
const copy = { ...obj };
copy.b.c = 99;
console.log(obj.b.c);
```

- A) `2`
- B) `99`
- C) `undefined`
- D) A `TypeError` is thrown

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The spread creates a shallow copy. `copy.b` and `obj.b` point to the same nested object in memory. Mutating `copy.b.c` also mutates `obj.b.c`.
- *Why B is correct:* Object spread (`{ ...obj }`) is a shallow copy. Primitive values are copied by value, but nested objects are copied by reference. Both `copy.b` and `obj.b` reference the same object `{ c: 2 }`. Setting `copy.b.c = 99` modifies that shared object, so `obj.b.c` also becomes `99`.
- *Why C is incorrect:* `obj.b.c` is defined. The property is not removed or set to `undefined`.
- *Why D is incorrect:* No operation here is invalid. Accessing and mutating nested properties is well-defined.

---

### Question 15

What does this code log?

```javascript
let x = 10;

function outer() {
  let x = 20;
  function inner() {
    console.log(x);
  }
  return inner;
}

const fn = outer();
fn();
```

- A) `10`
- B) `20`
- C) `undefined`
- D) A `ReferenceError` is thrown

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `inner` closes over the `x` in `outer`'s scope, not the global `x`. When `inner` is defined inside `outer`, it captures `outer`'s `x = 20` because that is the closest enclosing binding.
- *Why B is correct:* Lexical scoping determines which `x` `inner` closes over. The lookup chain is: `inner`'s own scope (no `x`) → `outer`'s scope (found: `x = 20`). The global `x = 10` is shadowed. Even after `outer` returns, the closure keeps `outer`'s scope alive, so `fn()` logs `20`.
- *Why C is incorrect:* `x` is found in the closure — it is not `undefined`.
- *Why D is incorrect:* `x` is accessible through the closure chain. No reference error occurs.

---

### Question 16

What is the result of evaluating `typeof undefined === typeof null`?

- A) `true`
- B) `false`
- C) `'undefined'`
- D) `'object'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `typeof undefined` is `'undefined'`. `typeof null` is `'object'` (a historical JavaScript bug). `'undefined' === 'object'` is `false`.
- *Why B is correct:* `typeof undefined` returns the string `'undefined'`. `typeof null` returns the string `'object'` — a well-known language quirk present since the first JavaScript specification. These two strings are not equal under strict comparison, so the expression evaluates to `false`.
- *Why C is incorrect:* The expression is a boolean comparison, not a `typeof` call. The result is a boolean, not a type string.
- *Why D is incorrect:* `'object'` is the value of `typeof null` alone — it is not the result of comparing the two `typeof` results.

---

### Question 17

Which statement about `let` and the Temporal Dead Zone (TDZ) is correct?

- A) `let` variables are hoisted and initialized to `undefined`, like `var`
- B) `let` variables are not hoisted at all — the declaration is ignored until runtime
- C) Accessing a `let` variable before its declaration throws a `ReferenceError`
- D) `let` variables in the TDZ return `null` when accessed

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `var` is initialized to `undefined` during hoisting. `let` is hoisted (the engine knows the binding exists) but is NOT initialized — it remains in the TDZ until the declaration is reached.
- *Why B is incorrect:* `let` is hoisted in the sense that the binding is known to the scope from the beginning of the block. The engine will not create a separate variable with the same name; it just refuses access until the declaration line.
- *Why C is correct:* The Temporal Dead Zone spans from the start of the block to the `let` declaration line. Any access to the variable during this zone — read or write — throws a `ReferenceError`. This is intentional: it eliminates the class of bugs caused by `var`'s silent `undefined` behavior.
- *Why D is incorrect:* TDZ access throws an error — it does not return any value including `null`. `null` is a valid JavaScript value but is not related to TDZ behavior.

---

### Question 18

What does `Array.from('hello')` return?

- A) `['hello']`
- B) `['h', 'e', 'l', 'l', 'o']`
- C) `[104, 101, 108, 108, 111]`
- D) A `TypeError` — strings are not valid arguments for `Array.from`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `['hello']` would be the result of `['hello']` or `[].concat('hello')`. `Array.from` iterates over the iterable and collects each item — strings are iterable character by character.
- *Why B is correct:* Strings are iterable in JavaScript — they implement the iterable protocol and yield individual characters. `Array.from('hello')` iterates over the string and collects each character as an element: `['h', 'e', 'l', 'l', 'o']`.
- *Why C is incorrect:* `Array.from` produces the characters themselves, not their Unicode code points. `charCodeAt` or `codePointAt` would produce numeric codes.
- *Why D is incorrect:* Strings are valid iterables and accepted by `Array.from`. No error is thrown.

---

### Question 19

What is the output of this code?

```javascript
function process(items) {
  return items
    .filter(n => n > 2)
    .map(n => n * 10);
}

console.log(process([1, 2, 3, 4]));
```

- A) `[30, 40]`
- B) `[10, 20, 30, 40]`
- C) `[3, 4]`
- D) `[1, 2, 30, 40]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `filter(n => n > 2)` keeps only elements greater than `2`: `[3, 4]`. Then `map(n => n * 10)` transforms each: `[30, 40]`. Chaining non-mutating array methods applies each transformation to the result of the previous.
- *Why B is incorrect:* `[10, 20, 30, 40]` would result from applying `map` to all four elements without filtering first.
- *Why C is incorrect:* `[3, 4]` is the result after `filter` but before `map`. Both methods are chained, so `map` also runs.
- *Why D is incorrect:* `filter` removes elements — it does not leave the filtered-out values in place. Only `[3, 4]` survives the filter step.

---

### Question 20

Which statement correctly describes the difference between `splice` and `slice`?

- A) Both return a new array; `splice` preserves the original, `slice` mutates it
- B) `splice` mutates the original array and returns the removed elements; `slice` returns a copy and does not mutate
- C) `slice` can insert elements; `splice` can only remove them
- D) Both mutate the original array; `slice` returns the first element, `splice` returns the last

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This reverses the behavior. `splice` mutates the original; `slice` does not.
- *Why B is correct:* `splice(start, deleteCount, ...items)` modifies the array in place — it removes elements, optionally inserts new ones, and returns an array of the removed elements. `slice(start, end)` returns a new shallow-copy array of the selected range without touching the original.
- *Why C is incorrect:* `splice` can both remove AND insert elements. `slice` cannot insert — it is read-only.
- *Why D is incorrect:* Only `splice` mutates the original. `slice` returns a new array containing a portion of the original, not just one element.
