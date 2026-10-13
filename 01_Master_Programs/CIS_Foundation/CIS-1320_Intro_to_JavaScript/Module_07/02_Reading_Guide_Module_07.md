# Reading Guide: Module 07 — Objects and Properties

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-1320 &BULL; INTRODUCTION TO JAVASCRIPT PROGRAMMING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

An object is a collection of named values — properties — that represent a single entity. A user has a name, an email, and a role. A product has a title, a price, and a quantity. Objects group these related values together so you can pass one thing instead of many. JavaScript objects are mutable, dynamic collections: properties can be added, changed, or removed at any time. Understanding how to create, access, and manipulate objects — including methods, `this`, destructuring, and optional chaining — is foundational to every real JavaScript program.

---

## 1. Object Literals

### Creating an Object

The **object literal** syntax creates an object directly with curly braces:

```javascript
const person = {
  name: 'Alice',
  age: 30,
  role: 'engineer'
};
```

Each entry is a **property** consisting of a key (always a string or Symbol) and a value (any type). Keys are written without quotes in a literal unless they contain spaces or special characters.

### Property Values Can Be Any Type

```javascript
const product = {
  title: 'Laptop',
  price: 999.99,
  inStock: true,
  tags: ['electronics', 'computers'],
  dimensions: { width: 35, height: 25 }   // nested object
};
```

---

## 2. Accessing Properties

### Dot Notation

```javascript
console.log(person.name);   // 'Alice'
console.log(person.age);    // 30
```

Dot notation is the most common form. Use it when the property name is known and is a valid identifier (no spaces, no special characters, does not start with a digit).

### Bracket Notation

```javascript
console.log(person['name']);   // 'Alice'
console.log(person['age']);    // 30
```

Bracket notation is required in two situations:

**1. The key is stored in a variable:**

```javascript
const key = 'role';
console.log(person[key]);   // 'engineer' — dot notation cannot use a variable
```

**2. The key contains a space or special character:**

```javascript
const config = { 'max-retries': 5 };
console.log(config['max-retries']);   // 5
// config.max-retries would parse as config.max minus retries — a bug
```

### Accessing a Non-Existent Property

Accessing a property that does not exist returns `undefined` — it does not throw an error:

```javascript
console.log(person.email);   // undefined — property does not exist
```

---

## 3. Modifying Objects

### Adding and Updating Properties

Objects declared with `const` are still mutable — `const` prevents reassigning the variable, not modifying the object's contents:

```javascript
const user = { name: 'Bob' };

user.email = 'bob@example.com';   // add new property
user.name = 'Robert';             // update existing property

console.log(user);   // { name: 'Robert', email: 'bob@example.com' }
```

### Deleting Properties

The `delete` operator removes a property from an object:

```javascript
delete user.email;
console.log(user);          // { name: 'Robert' }
console.log(user.email);    // undefined
```

### Checking Property Existence

The `in` operator tests whether a key exists on an object (including its prototype chain):

```javascript
console.log('name' in user);    // true
console.log('email' in user);   // false
```

Use `in` rather than checking `obj.key !== undefined` — a property could exist and hold the value `undefined`.

---

## 4. Methods and `this`

### Methods

A property whose value is a function is called a **method**:

```javascript
const calculator = {
  value: 0,
  add(n) {
    this.value += n;
  },
  getResult() {
    return this.value;
  }
};

calculator.add(5);
calculator.add(3);
console.log(calculator.getResult());   // 8
```

The `methodName() {}` syntax is the **ES6 method shorthand** — equivalent to `methodName: function() {}`.

### `this` in Methods

Inside a method, `this` refers to the **object the method was called on** — the object to the left of the dot at call time:

```javascript
const dog = {
  name: 'Rex',
  bark() {
    console.log(this.name, 'says: Woof!');
  }
};

dog.bark();   // 'Rex says: Woof!' — this === dog
```

### The Arrow Function `this` Trap

Arrow functions have **no `this` of their own**. They inherit `this` from the enclosing lexical scope. Using an arrow function as an object method means `this` inside the function is not the object:

```javascript
const broken = {
  name: 'MyObject',
  greet: () => {
    console.log('Hello from', this.name);   // this is the outer scope's this
  }
};

broken.greet();   // 'Hello from undefined' (strict mode) or global name
```

The fix is to use a regular function or method shorthand:

```javascript
const working = {
  name: 'MyObject',
  greet() {
    console.log('Hello from', this.name);   // this === working
  }
};

working.greet();   // 'Hello from MyObject'
```

### `this` Rule for Object Methods

| Method form | `this` refers to |
|---|---|
| Regular function: `greet: function() {}` | The object the method is called on |
| Method shorthand: `greet() {}` | The object the method is called on |
| Arrow function: `greet: () => {}` | Outer lexical scope — NOT the object |

Use regular functions or method shorthand for object methods. Use arrow functions for callbacks.

---

## 5. Object Destructuring

Destructuring extracts properties from an object into named variables:

```javascript
const person = { name: 'Alice', age: 30, city: 'Dallas' };

// Without destructuring
const name = person.name;
const age = person.age;

// With destructuring
const { name, age, city } = person;
```

The variable names in the braces must match the property names.

### Renaming During Destructuring

Use `:` to assign to a differently-named variable:

```javascript
const { name: fullName, age: years } = person;
console.log(fullName);   // 'Alice'
console.log(years);      // 30
// Note: variables 'name' and 'age' do NOT exist here
```

### Default Values in Destructuring

Provide a default for properties that may not exist:

```javascript
const { name, role = 'viewer' } = person;
console.log(role);   // 'viewer' — 'role' was not in person
```

### Destructuring in Function Parameters

A function can destructure its argument directly in the parameter list:

```javascript
function showUser({ name, role = 'viewer', active = true }) {
  console.log(`${name} | ${role} | active: ${active}`);
}

showUser({ name: 'Bob', role: 'admin' });     // 'Bob | admin | active: true'
showUser({ name: 'Carol' });                  // 'Carol | viewer | active: true'
```

This is a widely used modern pattern — it makes function signatures self-documenting and provides defaults inline.

---

## 6. Shorthand Property Names

When a variable name matches the intended property name, you can use shorthand:

```javascript
const name = 'Dave';
const age = 25;
const role = 'editor';

// Verbose form
const user = { name: name, age: age, role: role };

// Shorthand
const user = { name, age, role };
```

Both produce the same object. Shorthand is the preferred modern style.

---

## 7. Computed Property Names

Property names can be computed dynamically using bracket syntax inside an object literal:

```javascript
const field = 'email';
const value = 'alice@example.com';

const record = {
  id: 1,
  [field]: value   // property name is the value of the variable 'field'
};

console.log(record.email);   // 'alice@example.com'
```

Computed names are useful when building objects from dynamic keys — for example, grouping form field names and values from user input.

---

## 8. Optional Chaining (`?.`)

Optional chaining safely accesses nested properties without throwing a `TypeError` when an intermediate value is `null` or `undefined`:

### The Problem Without Optional Chaining

```javascript
const user = { name: 'Bob' };   // no 'address' property

console.log(user.address.city);   // TypeError: Cannot read properties of undefined
```

### The Solution: `?.`

```javascript
console.log(user?.address?.city);   // undefined — no error
```

`?.` short-circuits at the first `null` or `undefined` and returns `undefined` for the entire expression.

### Three Forms of Optional Chaining

```javascript
const user = null;

user?.name               // property access — undefined
user?.getName?.()        // method call — undefined
user?.tags?.[0]          // array element — undefined
```

### Combining `?.` with `??`

```javascript
const city = user?.address?.city ?? 'Unknown';
console.log(city);   // 'Unknown' — the chain returned undefined, ?? provides fallback
```

### When to Use `?.`

Use `?.` when accessing data from external sources (API responses, user input, database results) where properties may be absent. Do not overuse it on internal data where you control the shape — it can hide bugs by silently returning `undefined` instead of alerting you to a missing property.

---

## 9. Object Iteration

### `for...in` — Iterating Keys

```javascript
const scores = { alice: 92, bob: 85, carol: 78 };

for (const name in scores) {
  console.log(name, ':', scores[name]);
}
// alice : 92, bob : 85, carol : 78
```

### `Object.keys()`, `Object.values()`, `Object.entries()`

These three methods return arrays you can iterate with `for...of`:

```javascript
const person = { name: 'Alice', age: 30, role: 'engineer' };

console.log(Object.keys(person));     // ['name', 'age', 'role']
console.log(Object.values(person));   // ['Alice', 30, 'engineer']
console.log(Object.entries(person));  // [['name','Alice'], ['age',30], ['role','engineer']]

for (const [key, value] of Object.entries(person)) {
  console.log(`${key}: ${value}`);
}
```

`Object.entries()` with destructuring in the loop produces the cleanest syntax for iterating both keys and values simultaneously.

---

## 10. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 4: Data Structures: Objects and Arrays](https://eloquentjavascript.net/04_data.html)**
  The primary OER textbook. Covers object literals, properties, methods, arrays, and the relationships between them with extensive worked examples.

- **[MDN Web Docs — Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)**
  Comprehensive guide covering object creation, property access, property enumeration, object methods (`Object.keys`, `Object.values`, `Object.entries`, `Object.assign`, `Object.freeze`), and getter/setter syntax.

- **[MDN Web Docs — Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)**
  Full reference for object and array destructuring including renaming, default values, nested destructuring, and rest patterns in destructuring.

- **[MDN Web Docs — Optional chaining (`?.`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)**
  Full reference with examples for `?.` on properties, method calls, and array indexes. Includes browser compatibility and the combined `?.` + `??` pattern.

- **[javascript.info — Objects: the basics](https://javascript.info/object)**
  Beginner-friendly introduction to object literals, properties, computed property names, shorthand properties, and property existence checks with interactive exercises.

---

## 11. JSE Certification Exam Tips

1. **Dot vs bracket notation** — dot notation requires a valid identifier. Bracket notation works with any string, including keys stored in variables. Know which situations require brackets.

2. **`const` objects are still mutable** — `const` prevents reassignment of the variable, not modification of the object. Adding, changing, or deleting properties is always allowed.

3. **Accessing missing properties returns `undefined`** — not an error. Accessing a property of `undefined` (e.g., `user.address.city` when `address` is `undefined`) throws a `TypeError`.

4. **`this` in methods** — inside a regular function or method shorthand, `this` is the object to the left of the dot. Inside an arrow function method, `this` is the outer scope's `this`, not the object.

5. **Arrow functions as methods** — a common trap. Arrow function methods fail to reference the object via `this`. Always use regular functions or method shorthand for object methods.

6. **Destructuring variable names** — the names inside `{}` must match the object's property names unless renaming with `key: newName`. A mismatch silently produces `undefined`.

7. **Renaming in destructuring** — `const { name: fullName } = obj` creates the variable `fullName`, not `name`. The original key name is not a variable after this point.

8. **Default values in destructuring** — `{ role = 'viewer' }` provides a default when the property is absent or `undefined`. It does not trigger for `null`.

9. **`?.` short-circuits** — the entire chain returns `undefined` as soon as `?.` encounters `null` or `undefined`. No `TypeError` is thrown.

10. **`Object.keys()` / `Object.values()` / `Object.entries()`** — return arrays. `Object.entries()` returns an array of `[key, value]` pairs, which can be destructured in a `for...of` loop.

---

## 12. Study Checklist

- [ ] Watch the Module 07 video lecture by Professor Nash.
- [ ] Read Chapter 4 (Data Structures) of [Eloquent JavaScript](https://eloquentjavascript.net/04_data.html).
- [ ] Read [MDN — Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects).
- [ ] Read [MDN — Optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining).
- [ ] Open the console and demonstrate the `TypeError` from accessing a nested property on `undefined`.
- [ ] Replace the failing access with `?.` and confirm it returns `undefined` instead.
- [ ] Write an arrow function method — observe that `this.name` is `undefined`. Fix it with a regular function.
- [ ] Destructure an object with renaming and a default value.
- [ ] Iterate an object with `Object.entries()` and destructuring in the loop header.
- [ ] Complete the Module 07 Lab.
- [ ] Complete the Module 07 Quiz.
