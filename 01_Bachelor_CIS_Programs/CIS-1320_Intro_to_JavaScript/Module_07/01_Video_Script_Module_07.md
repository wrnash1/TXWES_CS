# Video Script: CIS-1320 — Introduction to JavaScript

## Module 07 — Objects and Properties

**Estimated Duration:** 17–20 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - The dot vs bracket notation demo should show a case where bracket notation is required (dynamic key lookup, key with a space) to motivate why both forms exist.
> - The `this` keyword demo is the most important new concept — show the broken version (arrow function method) before the working version (regular function method) so students understand why the rule exists.
> - Destructuring and shorthand are exam content — take time on both. Show the "old way" first so the shorthand feels like a simplification, not magic.
> - Optional chaining (`?.`) is ES2020 content that appears on the JSE exam — write the null-check version first, then replace it with `?.` to show the improvement.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 07 | Objects and Properties | CIS-1320"]**

"Module 07 is about objects. If functions are the primary unit of behavior in JavaScript, objects are the primary unit of data. An object groups related values together under a single name. A person has a name, an age, and a role. A product has a title, a price, and a quantity. An object lets you represent all of those properties as one coherent thing rather than a collection of unrelated variables.

JavaScript objects are also more flexible than objects in languages like Java or C++ — you can add, modify, and remove properties at runtime. We will cover object creation, property access, methods, the `this` keyword, object destructuring, shorthand syntax, and optional chaining. Let us start with the basics."

---

## [01:00 – 05:00] Part 1 — Creating Objects and Accessing Properties

**[SHOW SLIDE: "Object Literals"]**

"The most common way to create an object in JavaScript is the **object literal** syntax — curly braces containing key-value pairs separated by commas:

```javascript
const person = {
  name: 'Alice',
  age: 30,
  role: 'engineer'
};
```

Each key-value pair is called a **property**. The key is a string (usually written without quotes in a literal), and the value can be any type — number, string, boolean, array, another object, or a function.

**[DEMO]**

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

[PAUSE]

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

## [05:00 – 09:00] Part 2 — Methods and `this`

**[SHOW SLIDE: "Object Methods and `this`"]**

"A property whose value is a function is called a **method**. Methods let an object carry behavior alongside its data:

**[DEMO]**

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

[PAUSE]

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

[PAUSE]

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

Rule: **always use regular functions (or method shorthand) for object methods. Use arrow functions for callbacks and utilities.**"

---

## [09:00 – 13:00] Part 3 — Destructuring and Shorthand

**[SHOW SLIDE: "Destructuring and Shorthand Syntax"]**

"ES6 introduced two syntax features that make working with objects much cleaner: **object destructuring** and **shorthand property names**.

**Object destructuring** extracts properties into variables in one line:

**[DEMO]**

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

[PAUSE]

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

[PAUSE]

**Destructuring in function parameters:**

```javascript
function displayUser({ name, role = 'user' }) {
  console.log(`${name} — ${role}`);
}

displayUser({ name: 'Bob', role: 'admin' });   // 'Bob — admin'
displayUser({ name: 'Carol' });                // 'Carol — user' (default)
```

This is a very common pattern in modern JavaScript — functions receive an object and immediately destructure the properties they need from the parameter list.

[PAUSE]

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

Both forms produce identical objects. The shorthand version is preferred in modern JavaScript."

---

## [13:00 – 16:30] Part 4 — Optional Chaining and Computed Properties

**[SHOW SLIDE: "Optional Chaining and Computed Properties"]**

"Two more features that appear on the JSE exam: optional chaining and computed property names.

**Optional chaining (`?.`)** allows you to safely access nested properties without throwing an error if an intermediate value is `null` or `undefined`:

**[DEMO]**

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

[PAUSE]

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

Computed property names are useful when building objects dynamically — for example, mapping user-chosen keys to values, or building objects in a loop."

---

## [16:30 – 18:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 07 Lab Preview"]**

"The Module 07 lab has four parts.

Part 1 covers object creation, dot and bracket notation, property addition and deletion, and the `in` operator.

Part 2 covers methods and `this` — including the arrow function `this` trap. You will write the broken version, observe `undefined`, then fix it with a regular function method.

Part 3 covers destructuring — extracting properties, renaming, defaults, and destructuring in function parameters.

Part 4 covers optional chaining and shorthand property names. You will work through a realistic scenario where nested properties may be missing and observe the difference between accessing them safely and unsafely.

The quiz focuses on `this` in methods, destructuring syntax, and `?.` behavior. Read the reading guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 07 — Objects and Properties]**

---

## Additional Resources

- [MDN — Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
- [MDN — Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
- [MDN — Optional chaining (?.)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
- [MDN — Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
- [Eloquent JavaScript — Chapter 4: Data Structures](https://eloquentjavascript.net/04_data.html)
