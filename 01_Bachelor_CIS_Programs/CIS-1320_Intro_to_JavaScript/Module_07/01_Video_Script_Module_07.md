# Video Script: CIS-1320 — Introduction to JavaScript

## Module 07 — Objects and Properties

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp &bull; JavaScript Programming Full Course &bull; Module 07</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=jS4aFq5-91M" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/jS4aFq5-91M" title="freeCodeCamp &bull; JavaScript Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp &bull; JavaScript Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 17–20 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

Module 07 is about objects. If functions are the primary unit of behavior in JavaScript, objects are the primary unit of data. An object groups related values together under a single name. A person has a name, an age, and a role. A product has a title, a price, and a quantity. An object lets you represent all of those properties as one coherent thing rather than a collection of unrelated variables.

JavaScript objects are also more flexible than objects in languages like Java or C++ — you can add, modify, and remove properties at runtime. We will cover object creation, property access, methods, the `this` keyword, object destructuring, shorthand syntax, and optional chaining. Let us start with the basics.

---

## Part 1 — Creating Objects and Accessing Properties

The most common way to create an object in JavaScript is the **object literal** syntax — curly braces containing key-value pairs separated by commas:

```javascript
const person = {
  name: 'Alice',
  age: 30,
  role: 'engineer'
};
```

Each key-value pair is called a **property**. The key is a string (usually written without quotes in a literal), and the value can be any type — number, string, boolean, array, another object, or a function.

```javascript
const product = {
  title: 'Laptop',
  price: 999.99,
  inStock: true,
  tags: ['electronics', 'computers']
};

console.log(product);
```

You access properties using either **dot notation** or **bracket notation**:

```javascript
console.log(product.title);         // 'Laptop' — dot notation
console.log(product['price']);      // 999.99 — bracket notation
console.log(product.tags[0]);       // 'electronics' — dot then array index
```

Dot notation is shorter and more common. Bracket notation is required in two specific situations:

```javascript
// 1. Key stored in a variable
const key = 'price';
console.log(product[key]);   // 999.99 — dot notation cannot use a variable

// 2. Key contains a space or special character
const config = { 'max-retries': 3 };
console.log(config['max-retries']);   // 3 — dot notation would fail here
```

**Adding and modifying properties:**

Objects are mutable even when assigned to `const`. `const` prevents reassigning the variable — it does not freeze the object's content:

```javascript
const user = { name: 'Bob' };

user.email = 'bob@example.com';   // add new property
user.name = 'Robert';             // modify existing property

console.log(user);   // { name: 'Robert', email: 'bob@example.com' }
```

**Deleting a property:**

```javascript
delete user.email;
console.log(user);   // { name: 'Robert' }
```

**Checking if a property exists:**

```javascript
console.log('name' in user);    // true
console.log('email' in user);   // false — we deleted it
```"

---

## Part 2 — Methods and `this`

A property whose value is a function is called a **method**. Methods let an object carry behavior alongside its data:

```javascript
const calculator = {
  value: 0,
  add: function(n) {
    this.value += n;
  },
  subtract: function(n) {
    this.value -= n;
  },
  getResult: function() {
    return this.value;
  }
};

calculator.add(10);
calculator.add(5);
calculator.subtract(3);
console.log(calculator.getResult());   // 12
```

Inside a method, `this` refers to the object the method was called on. When you write `this.value` inside `add`, it refers to `calculator.value`.

**ES6 method shorthand:**

```javascript
const counter = {
  count: 0,
  increment() {
    this.count++;
  },
  reset() {
    this.count = 0;
  },
  getCount() {
    return this.count;
  }
};

counter.increment();
counter.increment();
counter.increment();
console.log(counter.getCount());   // 3
counter.reset();
console.log(counter.getCount());   // 0
```

The shorthand `methodName() {}` is equivalent to `methodName: function() {}` for regular methods.

**The `this` trap with arrow functions:**

Here is one of the most common JavaScript bugs. If you use an arrow function as an object method, `this` does not refer to the object — it inherits `this` from the surrounding scope:

```javascript
const broken = {
  name: 'BrokenObject',
  greet: () => {
    console.log('Hello from', this.name);   // this is NOT broken — it's the outer this
  }
};

broken.greet();   // 'Hello from undefined' — or the global name property
```

Arrow functions have no `this` of their own. They look outward to whatever `this` was in the enclosing scope when the object was defined — usually `undefined` in strict mode or the global object in non-strict mode.

The fix: use a regular function for methods that need `this`:

```javascript
const working = {
  name: 'WorkingObject',
  greet() {
    console.log('Hello from', this.name);   // this = working
  }
};

working.greet();   // 'Hello from WorkingObject'
```

Rule: **always use regular functions (or method shorthand) for object methods. Use arrow functions for callbacks and utilities.**

---

## Part 3 — Destructuring and Shorthand

ES6 introduced two syntax features that make working with objects much cleaner: **object destructuring** and **shorthand property names**.

**Object destructuring** extracts properties into variables in one line:

```javascript
const person = { name: 'Alice', age: 30, city: 'Dallas' };

// Old way — three separate assignments
const name = person.name;
const age = person.age;
const city = person.city;

// Destructuring — one line
const { name, age, city } = person;

console.log(name);   // 'Alice'
console.log(age);    // 30
console.log(city);   // 'Dallas'
```

The variable names in the braces must match the property names exactly. The engine looks up each key on the object and assigns its value to the matching variable.

**Renaming during destructuring:**

```javascript
const { name: fullName, age: years } = person;
console.log(fullName);   // 'Alice'
console.log(years);      // 30
// name and age variables do NOT exist here — only fullName and years
```

**Default values in destructuring:**

```javascript
const { name, role = 'user' } = person;
console.log(role);   // 'user' — property doesn't exist, default used
```

**Destructuring in function parameters:**

```javascript
function displayUser({ name, role = 'user' }) {
  console.log(`${name} — ${role}`);
}

displayUser({ name: 'Bob', role: 'admin' });   // 'Bob — admin'
displayUser({ name: 'Carol' });                // 'Carol — user' (default)
```

This is a very common pattern in modern JavaScript — functions receive an object and immediately destructure the properties they need from the parameter list.

**Shorthand property names:**

When a variable name and a property name are the same, you can use shorthand:

```javascript
const name = 'Dave';
const age = 25;
const role = 'editor';

// Old way
const user = { name: name, age: age, role: role };

// Shorthand
const user = { name, age, role };

console.log(user);   // { name: 'Dave', age: 25, role: 'editor' }
```

Both forms produce identical objects. The shorthand version is preferred in modern JavaScript.

---

## Part 4 — Optional Chaining and Computed Properties

Two more features that appear on the JSE exam: optional chaining and computed property names.

**Optional chaining (`?.`)** allows you to safely access nested properties without throwing an error if an intermediate value is `null` or `undefined`:

```javascript
const user1 = { name: 'Alice', address: { city: 'Dallas' } };
const user2 = { name: 'Bob' };   // no address property

// Without optional chaining — throws TypeError if address is undefined
console.log(user2.address.city);   // TypeError: Cannot read properties of undefined

// With optional chaining
console.log(user1?.address?.city);   // 'Dallas'
console.log(user2?.address?.city);   // undefined — no error
```

`?.` short-circuits at the first `null` or `undefined` it encounters and returns `undefined` for the entire chain instead of throwing. It works with:

```javascript
const result1 = user?.address?.city;         // property access
const result2 = user?.getAddress?.();        // method call
const result3 = user?.tags?.[0];             // array element
```

Combine `?.` with `??` to provide a fallback:

```javascript
const city = user2?.address?.city ?? 'Unknown';
console.log(city);   // 'Unknown' — the whole chain returned undefined
```

**Computed property names:**

Bracket notation works in object literals too, allowing dynamic property names:

```javascript
const fieldName = 'email';
const fieldValue = 'alice@example.com';

const record = {
  [fieldName]: fieldValue,   // property name computed from variable
  id: 42
};

console.log(record);        // { email: 'alice@example.com', id: 42 }
console.log(record.email);  // 'alice@example.com'
```

Computed property names are useful when building objects dynamically — for example, mapping user-chosen keys to values, or building objects in a loop.

---

## Closing — Lab Preview

The Module 07 lab has four parts.

Part 1 covers object creation, dot and bracket notation, property addition and deletion, and the `in` operator.

Part 2 covers methods and `this` — including the arrow function `this` trap. You will write the broken version, observe `undefined`, then fix it with a regular function method.

Part 3 covers destructuring — extracting properties, renaming, defaults, and destructuring in function parameters.

Part 4 covers optional chaining and shorthand property names. You will work through a realistic scenario where nested properties may be missing and observe the difference between accessing them safely and unsafely.

The quiz focuses on `this` in methods, destructuring syntax, and `?.` behavior. Read the reading guide before the lab. Good luck.

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 07 — Objects and Properties]**

---

## Additional Resources

- [MDN — Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
- [MDN — Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
- [MDN — Optional chaining (?.)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
- [MDN — Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
- [Eloquent JavaScript — Chapter 4: Data Structures](https://eloquentjavascript.net/04_data.html)
