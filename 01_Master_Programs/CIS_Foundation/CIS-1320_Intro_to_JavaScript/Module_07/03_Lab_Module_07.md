# Lab Activity: Module 07 — Objects and Properties

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will build scripts that create and manipulate JavaScript objects using every technique covered in Module 07: object literals, dot and bracket notation, methods, `this`, the arrow function `this` trap, object destructuring, shorthand property names, optional chaining, and `Object.entries()` iteration. You will deliberately trigger a `TypeError` from unsafe nested access, then fix it with `?.`.

By the end of this lab you will have:

- Created objects with multiple property types and accessed them with both dot and bracket notation
- Added, modified, and deleted properties on a `const` object
- Written object methods using regular functions and observed the arrow function `this` trap
- Used destructuring with renaming, defaults, and function parameter destructuring
- Used shorthand property names to build objects from variables
- Used optional chaining to safely access nested data that may be missing
- Iterated an object's properties with `for...in` and `Object.entries()`

---

## Prerequisites

- VS Code with Live Server installed
- Google Chrome or Firefox
- Module 07 reading guide completed

---

## Part 1 — Object Creation and Property Access

### Step 1.1 — Create the Project

Create folder `module07-lab`. Inside it create `objects.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Module 07 — Objects</title>
  <script src="objects.js" defer></script>
</head>
<body>
  <h1>Objects — check the console</h1>
</body>
</html>
```

Create `objects.js`:

```javascript
// Objects and Properties — Module 07 Lab

// --- SECTION 1: object literal with mixed value types ---
console.log('--- Section 1: object literals ---');

const book = {
  title: 'Eloquent JavaScript',
  author: 'Marijn Haverbeke',
  pages: 472,
  free: true,
  editions: [1, 2, 3],
  publisher: {
    name: 'No Starch Press',
    country: 'USA'
  }
};

console.log('book:', book);
console.log('title:', book.title);
console.log('pages:', book.pages);
console.log('free:', book.free);
console.log('editions[1]:', book.editions[1]);
console.log('publisher.name:', book.publisher.name);

// --- SECTION 2: dot vs bracket notation ---
console.log('\n--- Section 2: dot vs bracket notation ---');

// Bracket with string literal — same as dot
console.log(book['author']);   // 'Marijn Haverbeke'

// Bracket with variable key — dot cannot do this
const prop = 'pages';
console.log('Using variable key:', book[prop]);   // 472

// Key with hyphen — requires bracket notation
const config = {
  'max-connections': 10,
  'retry-delay': 500
};
console.log('max-connections:', config['max-connections']);
console.log('retry-delay:', config['retry-delay']);

// --- SECTION 3: add, modify, delete properties ---
console.log('\n--- Section 3: mutating a const object ---');

const user = { name: 'Bob', age: 28 };
console.log('Original:', user);

user.email = 'bob@example.com';    // add
user.age = 29;                     // modify
console.log('After add and modify:', user);

delete user.email;                 // delete
console.log('After delete:', user);

// --- SECTION 4: in operator and missing properties ---
console.log('\n--- Section 4: property existence ---');

console.log('"name" in user:', 'name' in user);     // true
console.log('"email" in user:', 'email' in user);   // false — deleted

// Accessing a non-existent property returns undefined (no error)
console.log('user.email:', user.email);   // undefined

// Accessing a property of undefined DOES throw
try {
  console.log(user.address.city);   // TypeError
} catch (e) {
  console.error('TypeError caught:', e.message);
}
```

### Step 1.2 — Open and Verify

Open `objects.html` in Live Server. Confirm:

- Section 3: the object has three properties after creation, four after the add, and two after the delete.
- Section 4: the `try/catch` catches a `TypeError` — `user.address` is `undefined`, and accessing `.city` on `undefined` throws.

### Screenshot 1

Take a screenshot of the full console output from `objects.js`. All four sections must be visible. Label this **Lab07-Part1**.

---

## Part 2 — Methods and `this`

### Step 2.1 — Create `methods.js`

Update your HTML `src` to `methods.js`:

```javascript
// Methods and this — Module 07 Lab

// --- SECTION 1: method shorthand ---
console.log('--- Section 1: method shorthand ---');

const counter = {
  count: 0,
  increment() {
    this.count++;
  },
  decrement() {
    this.count--;
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
counter.decrement();
console.log('After 3 increments and 1 decrement:', counter.getCount());   // 2

counter.reset();
console.log('After reset:', counter.getCount());   // 0

// --- SECTION 2: this refers to the calling object ---
console.log('\n--- Section 2: this in methods ---');

const account = {
  owner: 'Alice',
  balance: 1000,
  deposit(amount) {
    this.balance += amount;
    console.log(`${this.owner} deposited $${amount}. Balance: $${this.balance}`);
  },
  withdraw(amount) {
    if (amount > this.balance) {
      console.log(`Insufficient funds. Balance: $${this.balance}`);
      return;
    }
    this.balance -= amount;
    console.log(`${this.owner} withdrew $${amount}. Balance: $${this.balance}`);
  },
  getBalance() {
    return this.balance;
  }
};

account.deposit(500);
account.withdraw(200);
account.withdraw(2000);   // should show insufficient funds
console.log('Final balance:', account.getBalance());

// --- SECTION 3: arrow function this trap ---
console.log('\n--- Section 3: arrow function this trap ---');

// BROKEN — arrow function as method
const brokenGreeter = {
  name: 'BrokenGreeter',
  greet: () => {
    // 'this' here is NOT brokenGreeter — it is the outer scope's this
    console.log('Arrow method this.name:', this?.name ?? '(undefined)');
  }
};

brokenGreeter.greet();   // this.name will be undefined

// FIXED — regular function / method shorthand
const workingGreeter = {
  name: 'WorkingGreeter',
  greet() {
    console.log('Method shorthand this.name:', this.name);
  }
};

workingGreeter.greet();   // 'WorkingGreeter'

// --- SECTION 4: multiple objects sharing the same method structure ---
console.log('\n--- Section 4: multiple objects ---');

function createPerson(name, age) {
  return {
    name,
    age,
    introduce() {
      console.log(`Hi, I'm ${this.name} and I'm ${this.age} years old.`);
    },
    isAdult() {
      return this.age >= 18;
    }
  };
}

const alice = createPerson('Alice', 30);
const bob = createPerson('Bob', 16);
const carol = createPerson('Carol', 22);

alice.introduce();
bob.introduce();
carol.introduce();

console.log('Alice is adult:', alice.isAdult());   // true
console.log('Bob is adult:', bob.isAdult());       // false
```

### Step 2.2 — Verify the `this` Trap

In Section 3, confirm that `brokenGreeter.greet()` does NOT print `'BrokenGreeter'` — it shows `undefined` or empty. `workingGreeter.greet()` correctly prints `'WorkingGreeter'`.

### Screenshot 2

Take a screenshot of the full console output from `methods.js`. All four sections must be visible. Label this **Lab07-Part2**.

---

## Part 3 — Destructuring and Shorthand

### Step 3.1 — Create `destructuring.js`

Update your HTML `src` to `destructuring.js`:

```javascript
// Destructuring and Shorthand — Module 07 Lab

// --- SECTION 1: basic destructuring ---
console.log('--- Section 1: basic destructuring ---');

const movie = {
  title: 'Interstellar',
  director: 'Christopher Nolan',
  year: 2014,
  rating: 8.6
};

// Without destructuring
const title1 = movie.title;
const director1 = movie.director;
console.log('Without destructuring:', title1, director1);

// With destructuring
const { title, director, year, rating } = movie;
console.log('With destructuring:', title, director, year, rating);

// --- SECTION 2: renaming during destructuring ---
console.log('\n--- Section 2: renaming ---');

const { title: movieTitle, director: filmDirector, year: releaseYear } = movie;
console.log('movieTitle:', movieTitle);
console.log('filmDirector:', filmDirector);
console.log('releaseYear:', releaseYear);
// Note: variables 'title', 'director', 'year' are NOT available here after renaming

// --- SECTION 3: default values in destructuring ---
console.log('\n--- Section 3: defaults in destructuring ---');

const partialUser = { name: 'Dave', email: 'dave@example.com' };

const { name, email, role = 'viewer', active = true } = partialUser;
console.log('name:', name);
console.log('email:', email);
console.log('role:', role);       // 'viewer' — used default
console.log('active:', active);   // true — used default

// null does NOT trigger the default
const { role: role2 = 'viewer' } = { role: null };
console.log('role with null:', role2);   // null — default not triggered

// --- SECTION 4: destructuring in function parameters ---
console.log('\n--- Section 4: parameter destructuring ---');

function renderProfile({ name, role = 'member', verified = false }) {
  const badge = verified ? '✓' : '○';
  console.log(`[${badge}] ${name} (${role})`);
}

renderProfile({ name: 'Alice', role: 'admin', verified: true });
renderProfile({ name: 'Bob', role: 'editor' });
renderProfile({ name: 'Carol' });   // all defaults

// --- SECTION 5: shorthand property names ---
console.log('\n--- Section 5: shorthand property names ---');

const firstName = 'Eve';
const lastName = 'Smith';
const age = 34;
const department = 'Engineering';

// Verbose form
const employeeVerbose = {
  firstName: firstName,
  lastName: lastName,
  age: age,
  department: department
};

// Shorthand form
const employee = { firstName, lastName, age, department };

console.log('verbose:', employeeVerbose);
console.log('shorthand:', employee);
// Both produce identical objects

// --- SECTION 6: computed property names ---
console.log('\n--- Section 6: computed property names ---');

const fieldName = 'score';
const fieldValue = 95;

const record = {
  id: 101,
  [fieldName]: fieldValue,
  [`${fieldName}Label`]: 'Excellent'
};

console.log('record:', record);
console.log('record.score:', record.score);
console.log('record.scoreLabel:', record.scoreLabel);
```

### Step 3.3 — Verify Key Outputs

Confirm:

- Section 3: `role` shows `'viewer'` (default used) but `role2` shows `null` (default not triggered by `null`).
- Section 4: `renderProfile({ name: 'Carol' })` uses both defaults and prints `○ Carol (member)`.
- Section 6: `record.score` is `95` and `record.scoreLabel` is `'Excellent'` — computed names work.

### Screenshot 3

Take a screenshot of the full console output from `destructuring.js`. All six sections must be visible. Label this **Lab07-Part3**.

---

## Part 4 — Optional Chaining and Object Iteration

### Step 4.1 — Create `optional_chaining.js`

Update your HTML `src` to `optional_chaining.js`:

```javascript
// Optional Chaining and Object Iteration — Module 07 Lab

// --- SECTION 1: the problem without optional chaining ---
console.log('--- Section 1: unsafe nested access ---');

const userA = { name: 'Alice', address: { city: 'Dallas', zip: '75201' } };
const userB = { name: 'Bob' };   // no address

console.log('userA city:', userA.address.city);   // 'Dallas' — works

try {
  console.log('userB city:', userB.address.city);   // TypeError
} catch (e) {
  console.error('TypeError on userB:', e.message);
}

// --- SECTION 2: safe access with optional chaining ---
console.log('\n--- Section 2: optional chaining ---');

console.log('userA?.address?.city:', userA?.address?.city);   // 'Dallas'
console.log('userB?.address?.city:', userB?.address?.city);   // undefined — no error

// Optional chaining on method calls
const userC = { name: 'Carol', getTitle() { return 'Dr.'; } };
const userD = { name: 'Dave' };   // no getTitle method

console.log('userC getTitle:', userC?.getTitle?.());   // 'Dr.'
console.log('userD getTitle:', userD?.getTitle?.());   // undefined — no error

// Optional chaining on array elements
const userE = { name: 'Eve', scores: [92, 85, 78] };
const userF = { name: 'Frank' };   // no scores

console.log('userE scores[0]:', userE?.scores?.[0]);   // 92
console.log('userF scores[0]:', userF?.scores?.[0]);   // undefined

// --- SECTION 3: optional chaining with nullish coalescing ---
console.log('\n--- Section 3: ?. combined with ?? ---');

const users = [
  { name: 'Alice', address: { city: 'Dallas' } },
  { name: 'Bob' },
  null,
  { name: 'Carol', address: null }
];

for (const u of users) {
  const city = u?.address?.city ?? 'Unknown';
  const name = u?.name ?? 'Anonymous';
  console.log(`${name}: ${city}`);
}

// --- SECTION 4: for...in iteration ---
console.log('\n--- Section 4: for...in on objects ---');

const inventory = {
  apples: 50,
  bananas: 12,
  cherries: 200,
  dates: 7
};

for (const item in inventory) {
  const flag = inventory[item] < 10 ? ' ← LOW' : '';
  console.log(`${item}: ${inventory[item]}${flag}`);
}

// --- SECTION 5: Object.keys, Object.values, Object.entries ---
console.log('\n--- Section 5: Object methods ---');

const scores = { alice: 92, bob: 78, carol: 85, dave: 91 };

console.log('Object.keys:', Object.keys(scores));
console.log('Object.values:', Object.values(scores));
console.log('Object.entries:', Object.entries(scores));

// Iterate with Object.entries and destructuring
console.log('\nDetailed breakdown:');
for (const [student, score] of Object.entries(scores)) {
  const grade = score >= 90 ? 'A' : score >= 80 ? 'B' : 'C';
  console.log(`  ${student}: ${score} (${grade})`);
}

// Compute average using Object.values
const total = Object.values(scores).reduce((sum, s) => sum + s, 0);
const average = total / Object.values(scores).length;
console.log(`\nClass average: ${average.toFixed(1)}`);
```

### Step 4.2 — Verify Key Outputs

Confirm:

- Section 1: the `try/catch` catches the `TypeError`.
- Section 2: all `?.` accesses on the object missing the property return `undefined` without an error.
- Section 3: `Bob` and `null` both show `Unknown`, and the `null` entry shows `Anonymous`.
- Section 4: `dates: 7` shows the `← LOW` flag.

### Screenshot 4

Take a screenshot of the full console output from `optional_chaining.js`. All five sections must be visible. Label this **Lab07-Part4**.

---

## Deliverables

Submit the following to the Module 07 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `objects.js` | Object literals, dot/bracket notation, add/modify/delete, `in` operator, `TypeError` demo |
| `methods.js` | Method shorthand, `this` in methods, arrow function `this` trap, factory function |
| `destructuring.js` | Destructuring with renaming, defaults, parameter destructuring, shorthand, computed names |
| `optional_chaining.js` | Safe nested access, `?.` on methods and arrays, `?.` + `??`, `Object.entries` iteration |
| Lab07-Part1.png | Console — object operations and `TypeError` |
| Lab07-Part2.png | Console — methods and `this` including broken vs working greeter |
| Lab07-Part3.png | Console — destructuring and shorthand |
| Lab07-Part4.png | Console — optional chaining and object iteration |

---

## Part 9 — Challenge Exercise

**This section is optional but strongly recommended.** These exercises introduce advanced object patterns used daily in professional JavaScript.

### Challenge Step 9.1 — Deep Clone vs Shallow Clone

Create `clone_demo.js`. Demonstrate the difference between a shallow spread clone and a deep clone using `JSON.parse(JSON.stringify(obj))`. Create an object with a nested object and an array. Shallow-clone it with spread and show that mutating the nested object mutates the original. Then deep-clone it with `JSON.parse/stringify` and show the mutation is isolated. Add comments explaining when each approach is appropriate and what `JSON.parse/stringify` cannot handle (functions, `undefined` values, circular references).

### Challenge Step 9.2 — Build a Map-Like Object with Helper Functions

Create `object_map.js`. Implement three utility functions that operate on plain objects as if they were maps:

- `mapValues(obj, fn)` — returns a new object with each value transformed by `fn`
- `filterKeys(obj, predicate)` — returns a new object with only entries where `predicate(key, value)` is true
- `mergeDeep(target, source)` — merges two objects recursively (not just shallow)

Test each function with at least two examples and verify with `console.log`. This exercise reinforces `Object.entries()`, spread syntax, and recursive thinking.

### Challenge Step 9.3 — Implement a Simple Observable Object

Create `observable.js`. Write a `createObservable(initialData)` factory function that returns a proxy-like object where any property set triggers a console notification. Use a Proxy (or a getter/setter approach with `Object.defineProperty`) to intercept writes and log `Property 'X' changed from Y to Z`:

```javascript
const state = createObservable({ count: 0, name: 'App' });
state.count = 1;   // logs: Property 'count' changed from 0 to 1
state.name = 'My App';  // logs: Property 'name' changed from App to My App
```

This pattern is used in reactive frameworks like Vue.js.

---

## Reflection Questions

Answer in the Canvas text box (two to three sentences each):

1. In Part 1 Section 3, you added, modified, and deleted properties on a `const` object. Explain why this is allowed even though the object is declared with `const`. What exactly does `const` prevent?

2. In Part 2 Section 3, the arrow function method `greet` did not print the object's name. Explain in your own words why `this` inside an arrow function does not refer to the object. What is the rule for when to use arrow functions vs regular functions for methods?

3. In Part 3 Section 3, destructuring with `role: null` produced `null` instead of using the default value `'viewer'`. Explain why. How is this behavior the same as what you observed with default parameters in Module 06?

4. In Part 4, you used both `for...in` and `Object.entries()` to iterate an object's properties. Describe one situation where `Object.entries()` with a `for...of` loop is preferable to `for...in`, and explain why.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `TypeError` not caught in Part 1 | `try` block missing or malformed | Ensure `user.address.city` is inside the `try` block |
| `workingGreeter.greet()` still shows `undefined` | Method defined as arrow function accidentally | Ensure `greet()` uses method shorthand (no arrow `=>`) |
| Destructuring produces `undefined` for all variables | Property names in `{}` don't match object keys | Check spelling — destructuring matches by exact key name |
| `null` property triggers default in destructuring | Using `??` manually instead of destructuring default syntax | Use `{ role = 'viewer' }` syntax — `null` does not trigger it |
| `optional_chaining.js` Section 3 null entry throws | `u.name` accessed without `?.` on the null entry | Use `u?.name` — `u` itself can be `null` in the array |
