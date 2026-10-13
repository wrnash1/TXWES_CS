# Quiz: Module 07 — Objects and Properties

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the output of the following code?

```javascript
const car = { make: 'Toyota', model: 'Camry', year: 2022 };
car.color = 'silver';
console.log(car.color);
```

- A) `TypeError: Cannot add property 'color' to a constant`
- B) `undefined`
- C) `'silver'`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `const` prevents reassigning the variable `car` to a different object. It does not prevent modifying the object's properties. Adding a property to a `const` object is always allowed.
- *Why B is incorrect:* `undefined` would result if `car.color` were accessed before being assigned. Here, it is assigned `'silver'` before the `console.log`.
- *Why C is correct:* `car.color = 'silver'` successfully adds a new property to the object. `const` restricts reassignment of the binding (`car = something`), not mutation of the object's contents.
- *Why D is incorrect:* `null` is not assigned anywhere in this code. The property is assigned the string `'silver'`.

---

### Question 2

What is the output of the following code?

```javascript
const obj = { name: 'Alice', score: 95 };
const key = 'score';
console.log(obj[key]);
```

- A) `undefined`
- B) `'key'`
- C) `'score'`
- D) `95`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `obj['score']` accesses the `score` property, which exists and holds `95`. It does not return `undefined`.
- *Why B is incorrect:* `'key'` is the variable name as a string. Bracket notation evaluates the expression inside the brackets, which is the variable `key`, whose value is `'score'`.
- *Why C is incorrect:* `'score'` is the value of the variable `key`. `obj[key]` uses that string to look up the property — it returns the property's value, not the key name itself.
- *Why D is correct:* `key` holds the string `'score'`. `obj[key]` is equivalent to `obj['score']`, which returns `95`. This demonstrates why bracket notation is required when the property name is stored in a variable.

---

### Question 3

What is the output of the following code?

```javascript
const person = {
  name: 'Bob',
  greet: () => {
    console.log('Hello from', this?.name);
  }
};

person.greet();
```

- A) `'Hello from Bob'`
- B) `'Hello from undefined'`
- C) `TypeError: this is not defined`
- D) `'Hello from person'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Arrow functions do not have their own `this`. `this` inside an arrow function is inherited from the outer lexical scope where the object was defined, not from the object itself. `this.name` does not refer to `person.name`.
- *Why B is correct:* In a browser script running in non-strict mode, the outer `this` is the global object (`window`). `window.name` is typically an empty string or `undefined`. With `?.` the access is safe. In strict mode, `this` would be `undefined`, and `this?.name` returns `undefined`. The output is `'Hello from undefined'`.
- *Why C is incorrect:* `this` exists in JavaScript everywhere — it is never undefined as a keyword. The `?.` in `this?.name` also prevents any access error.
- *Why D is incorrect:* `this` does not refer to the object literal `person`. The arrow function captures the `this` of the enclosing scope at definition time.

---

### Question 4

What is the output of the following code?

```javascript
const person = { name: 'Carol', age: 28, city: 'Austin' };
const { name, city } = person;
console.log(name, city);
```

- A) `undefined undefined`
- B) `{ name: 'Carol', city: 'Austin' }`
- C) `'Carol' 'Austin'`
- D) `'name' 'city'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The property names `name` and `city` both exist in `person`. Destructuring successfully extracts their values.
- *Why B is incorrect:* Destructuring does not produce a new object. It creates individual variables: `name` and `city`. Each holds its respective string value.
- *Why C is correct:* `const { name, city } = person` creates two variables: `name` with value `'Carol'` and `city` with value `'Austin'`. `console.log(name, city)` prints them separated by a space.
- *Why D is incorrect:* `'name'` and `'city'` are the property key strings. Destructuring extracts the property values, not the key names.

---

### Question 5

What is the output of the following code?

```javascript
const data = { username: 'eve', role: null };
const { username, role = 'viewer' } = data;
console.log(role);
```

- A) `'viewer'`
- B) `null`
- C) `undefined`
- D) `'null'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Destructuring defaults — like function parameter defaults — only trigger when the value is `undefined`. The `role` property exists in `data` and holds `null`, which is not `undefined`.
- *Why B is correct:* `data.role` is `null`. `null` is not `undefined`, so the default `'viewer'` is not used. The destructured variable `role` receives the value `null`.
- *Why C is incorrect:* `undefined` would result if the `role` property did not exist in `data` at all, and there were no default. Here, the property exists (as `null`), so `undefined` is never involved.
- *Why D is incorrect:* `null` is not coerced to the string `'null'` by destructuring. The variable receives the actual `null` value.

---

### Question 6

What is the output of the following code?

```javascript
const { name: fullName, age = 25 } = { name: 'Frank' };
console.log(fullName);
console.log(age);
```

- A) `undefined` then `25`
- B) `'Frank'` then `undefined`
- C) `'Frank'` then `25`
- D) `'name'` then `25`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `fullName` successfully receives the value of the `name` property (`'Frank'`). Renaming syntax `name: fullName` assigns the value of `name` to a new variable called `fullName`.
- *Why B is incorrect:* The `age` property does not exist in the object, so the default `25` is used. `age` receives `25`, not `undefined`.
- *Why C is correct:* `{ name: fullName }` renames — it reads `obj.name` and stores it in `fullName`. `{ age = 25 }` provides a default — since `age` is absent from the object, `age` receives `25`.
- *Why D is incorrect:* `'name'` is the property key string. After renaming with `name: fullName`, the variable holding the value is `fullName`, not `name`. And `fullName` holds `'Frank'`, not the string `'name'`.

---

### Question 7

What is the output of the following code?

```javascript
const user = null;
console.log(user?.profile?.email ?? 'no email');
```

- A) `TypeError: Cannot read properties of null`
- B) `undefined`
- C) `'no email'`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Optional chaining `?.` short-circuits when it encounters `null` or `undefined`. `user?.profile` does not throw — it evaluates to `undefined` because `user` is `null`.
- *Why B is incorrect:* The full chain `user?.profile?.email` evaluates to `undefined`, but `??` then provides the fallback. The final result is `'no email'`, not `undefined`.
- *Why C is correct:* `user` is `null`. `user?.profile` short-circuits and returns `undefined`. `undefined?.email` also returns `undefined`. Then `undefined ?? 'no email'` returns `'no email'`.
- *Why D is incorrect:* `null` is the value of `user`, but `?.` prevents it from propagating. The chain resolves to `undefined`, and `??` replaces `undefined` with `'no email'`.

---

### Question 8

What does the following code print?

```javascript
const x = 'hello';
const y = 42;
const obj = { x, y };
console.log(obj);
```

- A) `{ x: 'x', y: 'y' }`
- B) `{ 'hello': 42 }`
- C) `{ x: 'hello', y: 42 }`
- D) `{ hello: 42 }`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Shorthand property syntax uses the variable name as the property key and the variable value as the property value. It does not produce the string `'x'` or `'y'` as values.
- *Why B is incorrect:* The property keys in the resulting object are the variable names (`x` and `y`), not the variable values (`'hello'` and `42`).
- *Why C is correct:* `{ x, y }` is shorthand for `{ x: x, y: y }`. The keys are `x` and `y` (the variable names), and the values are `'hello'` and `42` (the variable values).
- *Why D is incorrect:* `'hello'` is the value of `x`, not the key. The key in the resulting object is `x` (the variable name), not its value.

---

### Question 9

What is the output of the following code?

```javascript
const product = { title: 'Phone', price: 599 };
console.log('discount' in product);
console.log(product.discount);
```

- A) `true` then `0`
- B) `false` then `undefined`
- C) `false` then `null`
- D) `true` then `undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'discount' in product` is `false` — the property does not exist. `0` would only appear if `discount` existed with value `0`.
- *Why B is correct:* The `in` operator tests for property existence — `'discount'` is not a property of `product`, so `false` is logged. Accessing a non-existent property returns `undefined` (not an error), so the second log prints `undefined`.
- *Why C is incorrect:* Accessing a non-existent property returns `undefined`, not `null`. `null` must be explicitly assigned.
- *Why D is incorrect:* `'discount' in product` is `false`, not `true`. The property was never added.

---

### Question 10

What is the output of the following code?

```javascript
const scores = { alice: 90, bob: 85, carol: 92 };

for (const [name, score] of Object.entries(scores)) {
  if (score > 89) {
    console.log(name);
  }
}
```

- A) `alice` then `carol`
- B) `alice` then `bob` then `carol`
- C) `90` then `92`
- D) `carol` only

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `Object.entries(scores)` produces `[['alice', 90], ['bob', 85], ['carol', 92]]`. The destructuring `[name, score]` unpacks each pair. The condition `score > 89` is true for `alice` (90) and `carol` (92), but false for `bob` (85). Only `'alice'` and `'carol'` are logged.
- *Why B is incorrect:* `bob`'s score is `85`, which is not greater than `89`. The condition filters `bob` out.
- *Why C is incorrect:* `name` holds the key string (e.g., `'alice'`), not the score. Logging `name` prints the student's name, not their score.
- *Why D is incorrect:* Both `alice` (90 > 89) and `carol` (92 > 89) satisfy the condition. The loop checks all entries and prints both names.

---

### Question 11

What is the output of the following code?

```javascript
const obj = { a: 1, b: 2, c: 3 };
delete obj.b;
console.log(Object.keys(obj));
console.log('b' in obj);
```

- A) `['a', 'b', 'c']` then `true`
- B) `['a', 'c']` then `false`
- C) `['a', 'c']` then `true`
- D) `TypeError: Cannot delete property 'b'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `delete obj.b` successfully removes the `b` property from the object. After deletion, `Object.keys(obj)` returns only the remaining keys.
- *Why B is correct:* `delete obj.b` removes the `b` property. `Object.keys(obj)` returns `['a', 'c']`. `'b' in obj` returns `false` because the property no longer exists.
- *Why C is incorrect:* After `delete obj.b`, `'b' in obj` is `false`. The property has been removed.
- *Why D is incorrect:* `delete` on a regular object property does not throw a `TypeError`. It returns `true` (indicating success) and removes the property. `TypeError` would occur only when trying to delete a non-configurable property.

---

### Question 12

What is the output of the following code?

```javascript
const obj = {};
obj['first name'] = 'Alice';
console.log(obj['first name']);
console.log(obj.first name);
```

- A) `'Alice'` then `'Alice'`
- B) `'Alice'` then `undefined`
- C) `'Alice'` then `SyntaxError`
- D) `undefined` then `SyntaxError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `obj.first name` is not valid syntax. `first name` contains a space and cannot be used with dot notation. The engine cannot parse it as a valid property name.
- *Why B is incorrect:* Dot notation with a space is not valid syntax — it produces a `SyntaxError` at parse time, not `undefined`.
- *Why C is correct:* `obj['first name']` correctly accesses the property using bracket notation (which accepts any string). `obj.first name` is a syntax error because dot notation requires a valid identifier — and identifiers cannot contain spaces.
- *Why D is incorrect:* `obj['first name']` successfully returns `'Alice'` because the property was assigned.

---

### Question 13

What is the output of the following code?

```javascript
const a = { x: 1 };
const b = a;
b.x = 99;
console.log(a.x);
```

- A) `1`
- B) `undefined`
- C) `99`
- D) `TypeError: Cannot modify const object`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `b = a` does not copy the object. Both variables point to the same object in memory. Modifying `b.x` also modifies `a.x` because they reference the same object.
- *Why B is incorrect:* `a.x` is not `undefined`. Both `a` and `b` refer to the same object, and `x` was set to `99`.
- *Why C is correct:* Objects are assigned by reference. `const b = a` makes `b` point to the same object as `a`. `b.x = 99` modifies the shared object. `a.x` reflects the change: `99`.
- *Why D is incorrect:* `const` prevents reassigning `a` or `b` to a different value. It does not prevent mutating the object's properties. No error is thrown.

---

### Question 14

What is the output of the following code?

```javascript
const person = {
  name: 'Alice',
  greet() {
    return `My name is ${this.name}`;
  }
};

const fn = person.greet;
console.log(fn());
```

- A) `'My name is Alice'`
- B) `'My name is undefined'`
- C) `TypeError: this is not defined`
- D) `'My name is '`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* When `fn` is assigned `person.greet` and called as `fn()` (not `person.greet()`), the function is invoked without a calling object. In non-strict mode, `this` inside `fn` becomes the global object, which has no `name` property. In strict mode, `this` is `undefined`.
- *Why B is correct:* Extracting a method from an object loses its binding context. `fn()` is called without an explicit receiver. In non-strict mode `this` is the global object and `this.name` is `undefined`. The template literal produces `'My name is undefined'`.
- *Why C is incorrect:* `this` is always defined (it is `undefined` in strict mode or the global object in sloppy mode — but it is never a `ReferenceError`).
- *Why D is incorrect:* `this.name` is `undefined`, not an empty string. `undefined` converts to the string `'undefined'` in template literals.

---

### Question 15

What does `Object.assign({}, source)` do?

- A) Freezes the `source` object so it cannot be mutated
- B) Creates a shallow copy of `source` into a new empty object
- C) Deep-clones all nested objects inside `source`
- D) Merges `source` into the global object

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Object.assign` does not freeze anything. `Object.freeze()` is the method that makes an object immutable.
- *Why B is correct:* `Object.assign({}, source)` copies all enumerable own properties of `source` into the first argument (an empty object `{}`). The result is a new object with the same top-level properties. Note that nested objects are still copied by reference (shallow copy).
- *Why C is incorrect:* `Object.assign` performs a shallow copy. Nested objects inside `source` are copied by reference, not cloned. Modifying a nested object in the copy also modifies the original.
- *Why D is incorrect:* The first argument is the target object (`{}`). `Object.assign` copies into that target — not into the global object.

---

### Question 16

What is the output of the following code?

```javascript
const user = { name: 'Alice', age: 30, role: 'admin' };
const { role, ...rest } = user;
console.log(role);
console.log(rest);
```

- A) `'admin'` then `{ name: 'Alice', age: 30, role: 'admin' }`
- B) `'admin'` then `{ name: 'Alice', age: 30 }`
- C) `undefined` then `{ name: 'Alice', age: 30, role: 'admin' }`
- D) `'admin'` then `{}`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The rest element `...rest` collects all properties that were not explicitly destructured. Since `role` was extracted, it is excluded from `rest`.
- *Why B is correct:* `role` receives `'admin'`. The rest pattern `...rest` collects the remaining properties `{ name: 'Alice', age: 30 }` — everything except `role`.
- *Why C is incorrect:* `role` is explicitly destructured and receives `'admin'`.
- *Why D is incorrect:* `rest` contains all properties not already extracted — `name` and `age` — not an empty object.

---

### Question 17

What is the output of the following code?

```javascript
const config = Object.freeze({ host: 'localhost', port: 3000 });
config.port = 8080;
console.log(config.port);
```

- A) `8080`
- B) `3000`
- C) `TypeError: Cannot assign to read only property 'port'`
- D) `undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Object.freeze()` makes all existing properties read-only. The assignment `config.port = 8080` is silently ignored in non-strict mode.
- *Why B is correct:* `Object.freeze()` prevents any property additions, modifications, or deletions. In non-strict mode, the assignment silently fails and `config.port` remains `3000`.
- *Why C is incorrect:* In **strict mode**, attempting to modify a frozen object does throw `TypeError`. However, without `'use strict'` the assignment silently fails. The question does not specify strict mode, so the answer is `3000`.
- *Why D is incorrect:* The `port` property was initialized to `3000` and was not changed. It is not `undefined`.

---

### Question 18

What is the output of the following code?

```javascript
const source = { a: 1, b: { c: 2 } };
const copy = { ...source };
copy.b.c = 99;
console.log(source.b.c);
```

- A) `2`
- B) `99`
- C) `undefined`
- D) `TypeError: Cannot assign to read only property`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The spread operator `{ ...source }` creates a shallow copy. Top-level properties (`a`) are copied by value. Nested objects (`b`) are copied by reference — both `source.b` and `copy.b` point to the same object.
- *Why B is correct:* `copy.b` and `source.b` reference the same nested object. Modifying `copy.b.c = 99` mutates the shared object. `source.b.c` reflects the change: `99`. This demonstrates the shallow copy limitation.
- *Why C is incorrect:* `source.b.c` is `99` after the mutation through `copy.b.c`. It is not `undefined`.
- *Why D is incorrect:* The spread operator does not freeze objects. Mutation of nested objects is permitted.

---

### Question 19

Which method returns an array of a plain object's **enumerable own property values**?

- A) `Object.keys(obj)`
- B) `Object.entries(obj)`
- C) `Object.values(obj)`
- D) `Object.getOwnPropertyNames(obj)`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Object.keys(obj)` returns an array of property **names** (keys), not values.
- *Why B is incorrect:* `Object.entries(obj)` returns an array of `[key, value]` pairs — not just values.
- *Why C is correct:* `Object.values(obj)` returns an array containing only the values of the object's enumerable own properties, in the same order as `for...in`.
- *Why D is incorrect:* `Object.getOwnPropertyNames(obj)` returns all own property names including non-enumerable ones (like `length` on arrays) — and it returns names, not values.

---

### Question 20

What is the output of the following code?

```javascript
const team = {
  name: 'Alpha',
  members: ['Alice', 'Bob'],
  describe() {
    return `${this.name} has ${this.members.length} members`;
  }
};

console.log(team.describe());
console.log(team['describe']());
```

- A) `'Alpha has 2 members'` then `TypeError`
- B) `'Alpha has 2 members'` then `'Alpha has 2 members'`
- C) `'undefined has 2 members'` then `'Alpha has 2 members'`
- D) `'Alpha has 2 members'` then `undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `team['describe']()` is valid syntax. Bracket notation can access any property — including methods — and calling the result with `()` invokes it.
- *Why B is correct:* Both `team.describe()` and `team['describe']()` call the same method with the same calling context (`team`). Both produce `'Alpha has 2 members'`. Dot and bracket notation are functionally identical here.
- *Why C is incorrect:* Both calls have `team` as the calling object, so `this.name` is `'Alpha'` in both cases.
- *Why D is incorrect:* `team['describe']()` returns the string from the method, not `undefined`. `undefined` would result only if the method had no `return` statement.
