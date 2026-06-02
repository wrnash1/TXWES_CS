# Video Script: CIS-1320 — Introduction to JavaScript

## Module 08 — Arrays and Array Methods

**Estimated Duration:** 18–21 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - This module was listed as "Midterm Prep & Arrays" in the skeleton — treat it as the full Arrays module. The midterm review material is embedded in the lab's reflection section.
> - The `map`, `filter`, and `reduce` trio is the highest-value exam content — spend equal time on all three and emphasize that they do NOT mutate the original array.
> - For `reduce`, show the accumulator table step-by-step on screen — this is the part students find hardest.
> - Spread operator demo: show both the copy-without-reference case and the merge case side by side.
> - Array destructuring appears on the JSE exam — show the positional nature clearly.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 08 | Arrays and Array Methods | CIS-1320"]**

"Module 08 is about arrays. You have already seen arrays used as property values in objects and as the return type of `Object.keys()`. Now we go deep. Arrays are ordered, indexed collections — the most common data structure in JavaScript programs. Nearly every real application processes arrays: lists of users, search results, shopping cart items, chart data points.

JavaScript arrays come with a rich set of built-in methods. We will cover the core set: `push`, `pop`, `shift`, `unshift`, `splice`, `slice`, `indexOf`, `includes`, and then the three most powerful higher-order methods — `map`, `filter`, and `reduce`. We will also cover the spread operator and array destructuring. Let us start with the fundamentals."

---

## [01:00 – 05:00] Part 1 — Array Basics

**[SHOW SLIDE: "Array Fundamentals"]**

"An array is created with square brackets and contains comma-separated values:

```javascript
const fruits = ['apple', 'banana', 'cherry'];
```

Arrays are **zero-indexed** — the first element is at index `0`:

```javascript
console.log(fruits[0]);   // 'apple'
console.log(fruits[1]);   // 'banana'
console.log(fruits[2]);   // 'cherry'
console.log(fruits[3]);   // undefined — out of bounds, no error
```

**[DEMO]**

```javascript
const nums = [10, 20, 30, 40, 50];

console.log('Length:', nums.length);   // 5
console.log('Last element:', nums[nums.length - 1]);   // 50
```

`nums.length - 1` is the standard idiom for the last index. It adapts automatically when the array changes.

[PAUSE]

**Mutating methods — these change the original array:**

```javascript
const stack = [];

stack.push('a');        // add to end → ['a']
stack.push('b', 'c');  // add multiple → ['a', 'b', 'c']
console.log(stack);

const last = stack.pop();   // remove from end → 'c'
console.log(last, stack);   // 'c' ['a', 'b']

stack.unshift('z');     // add to beginning → ['z', 'a', 'b']
const first = stack.shift(); // remove from beginning → 'z'
console.log(first, stack);   // 'z' ['a', 'b']
```

`push`/`pop` work at the end — think of a stack. `unshift`/`shift` work at the beginning — they are slower on large arrays because every element must be re-indexed.

[PAUSE]

**`splice` — insert, remove, or replace at any position:**

```javascript
const letters = ['a', 'b', 'c', 'd', 'e'];

// Remove 2 elements starting at index 1
const removed = letters.splice(1, 2);
console.log(removed);   // ['b', 'c']
console.log(letters);   // ['a', 'd', 'e']

// Insert elements at index 1 (delete 0, insert 'X', 'Y')
letters.splice(1, 0, 'X', 'Y');
console.log(letters);   // ['a', 'X', 'Y', 'd', 'e']
```

`splice(start, deleteCount, ...itemsToInsert)` — it modifies the array in-place and returns the removed elements.

**`slice` — copy a portion without modifying the original:**

```javascript
const arr = [1, 2, 3, 4, 5];
const portion = arr.slice(1, 4);   // from index 1 up to (not including) index 4
console.log(portion);   // [2, 3, 4]
console.log(arr);       // [1, 2, 3, 4, 5] — unchanged
```

`splice` modifies; `slice` does not. Know this distinction."

---

## [05:00 – 08:00] Part 2 — Searching and Checking

**[SHOW SLIDE: "Searching Arrays"]**

"**`indexOf`** returns the index of the first occurrence of a value, or `-1` if not found:

**[DEMO]**

```javascript
const colors = ['red', 'green', 'blue', 'green'];

console.log(colors.indexOf('green'));    // 1 — first occurrence
console.log(colors.indexOf('purple'));  // -1 — not found
console.log(colors.indexOf('blue'));    // 2
```

`indexOf` uses strict equality (`===`). It finds the first match only.

**`includes`** returns a boolean — `true` if the value exists, `false` otherwise:

```javascript
console.log(colors.includes('blue'));    // true
console.log(colors.includes('purple')); // false
```

Use `includes` when you need a yes/no answer. Use `indexOf` when you need the position.

[PAUSE]

**`find` and `findIndex`** — search by condition (covered more in Module 09, but introduced here):

```javascript
const scores = [72, 85, 91, 68, 55];

const firstPassing = scores.find(score => score >= 90);
console.log(firstPassing);   // 91

const firstPassingIndex = scores.findIndex(score => score >= 90);
console.log(firstPassingIndex);   // 2
```

`find` returns the first element that satisfies the callback. `findIndex` returns its index. Both return `undefined` / `-1` if nothing matches.

[PAUSE]

**`join`** — convert array to string:

```javascript
const words = ['Hello', 'world', 'from', 'JavaScript'];
console.log(words.join(' '));    // 'Hello world from JavaScript'
console.log(words.join(', '));   // 'Hello, world, from, JavaScript'
console.log(words.join(''));     // 'HelloworldfromJavaScript'
```

**`reverse` and `sort`** — both mutate the original array:

```javascript
const nums = [3, 1, 4, 1, 5, 9, 2, 6];
nums.sort((a, b) => a - b);   // ascending numeric sort
console.log(nums);             // [1, 1, 2, 3, 4, 5, 6, 9]
```

The comparator `(a, b) => a - b` returns negative when `a` should come first, positive when `b` should come first. Without a comparator, `sort` converts elements to strings and sorts lexicographically — `[10, 9, 2]` would sort as `[10, 2, 9]` because `'10'` comes before `'2'` in Unicode."

---

## [08:00 – 14:00] Part 3 — `map`, `filter`, and `reduce`

**[SHOW SLIDE: "Higher-Order Array Methods"]**

"These three methods are the heart of functional-style JavaScript. They all accept a callback function and return a new array or value — they do not modify the original.

**`map`** transforms every element and returns a new array of the same length:

**[DEMO]**

```javascript
const prices = [10, 25, 50, 75];

const discounted = prices.map(price => price * 0.9);
console.log(discounted);   // [9, 22.5, 45, 67.5]
console.log(prices);       // [10, 25, 50, 75] — unchanged
```

Every element goes through the callback and the result is collected into a new array. The original is untouched.

```javascript
const names = ['alice', 'bob', 'carol'];
const capitalized = names.map(name => name[0].toUpperCase() + name.slice(1));
console.log(capitalized);   // ['Alice', 'Bob', 'Carol']
```

[PAUSE]

**`filter`** tests every element with a predicate and returns a new array containing only the elements that pass:

```javascript
const scores = [72, 85, 91, 68, 55, 99, 44, 78];

const passing = scores.filter(score => score >= 60);
console.log(passing);   // [72, 85, 91, 68, 99, 78]
console.log(scores);    // unchanged
```

The callback must return a truthy value to include the element. Elements where the callback returns falsy are excluded.

```javascript
const users = [
  { name: 'Alice', active: true },
  { name: 'Bob', active: false },
  { name: 'Carol', active: true }
];

const activeUsers = users.filter(user => user.active);
console.log(activeUsers.map(u => u.name));   // ['Alice', 'Carol']
```

[PAUSE]

**`reduce`** accumulates all elements into a single value:

```javascript
const nums = [1, 2, 3, 4, 5];

const total = nums.reduce((accumulator, current) => accumulator + current, 0);
console.log(total);   // 15
```

`reduce` takes two arguments: a callback and an initial value. The callback receives the accumulator (running result) and the current element. Let me trace through this step by step:

**[WRITE ACCUMULATOR TABLE ON SCREEN]**

| Step | Accumulator | Current | Return |
|---|---|---|---|
| Start | 0 (initial) | — | — |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 6 | 4 | 10 |
| 5 | 10 | 5 | 15 |

The final accumulator value is `15` — the sum of all elements.

```javascript
// Find the maximum value
const max = nums.reduce((acc, cur) => cur > acc ? cur : acc, nums[0]);
console.log(max);   // 5

// Count occurrences
const letters = ['a', 'b', 'a', 'c', 'b', 'a'];
const counts = letters.reduce((acc, letter) => {
  acc[letter] = (acc[letter] ?? 0) + 1;
  return acc;
}, {});
console.log(counts);   // { a: 3, b: 2, c: 1 }
```

`reduce` is the most general — it can implement `map` and `filter`, but `map` and `filter` are more readable for their specific cases."

---

## [14:00 – 17:00] Part 4 — Spread Operator and Array Destructuring

**[SHOW SLIDE: "Spread and Destructuring"]**

"**The spread operator `...`** expands an array into individual elements:

**[DEMO]**

```javascript
const a = [1, 2, 3];
const b = [4, 5, 6];

// Merge arrays
const merged = [...a, ...b];
console.log(merged);   // [1, 2, 3, 4, 5, 6]

// Copy an array
const copy = [...a];
copy.push(99);
console.log(a);      // [1, 2, 3] — original unaffected
console.log(copy);   // [1, 2, 3, 99]
```

`[...a]` creates a **shallow copy** — a new array with the same elements. Modifying the copy does not affect the original.

```javascript
// Spread into a function call
const nums = [3, 1, 4, 1, 5];
console.log(Math.max(...nums));   // 5 — spreads array as individual arguments
```

[PAUSE]

**Array destructuring** extracts elements by position:

```javascript
const rgb = [255, 128, 0];

const [red, green, blue] = rgb;
console.log(red);    // 255
console.log(green);  // 128
console.log(blue);   // 0
```

Position determines the assignment — the first variable gets index 0, the second gets index 1, and so on.

**Skipping elements:**

```javascript
const [first, , third] = [10, 20, 30];
console.log(first, third);   // 10, 30 — second element skipped
```

**Default values:**

```javascript
const [x = 0, y = 0, z = 0] = [5, 10];
console.log(x, y, z);   // 5, 10, 0 — z used the default
```

**Swapping variables — a classic use case:**

```javascript
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b);   // 2, 1 — swapped without a temp variable
```"

---

## [17:00 – 18:30] Closing — Lab Preview

**[SHOW SLIDE: "Module 08 Lab Preview"]**

"The Module 08 lab has four parts.

Part 1 covers the mutating methods — `push`, `pop`, `shift`, `unshift`, `splice` — and the non-mutating `slice`. You will verify which methods change the original and which do not.

Part 2 covers searching and utility methods — `indexOf`, `includes`, `find`, `findIndex`, `join`, `sort`.

Part 3 is the core of the module — `map`, `filter`, and `reduce`. You will implement each on the same dataset and verify that the original array is never modified.

Part 4 covers the spread operator and array destructuring, including the swap pattern.

The quiz focuses heavily on `map`/`filter`/`reduce` return values and on `splice` vs `slice`. Read the reading guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 08 — Arrays and Array Methods]**

---

## Additional Resources

- [MDN — Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [MDN — Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
- [MDN — Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- [MDN — Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
- [MDN — Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
- [Eloquent JavaScript — Chapter 4: Data Structures](https://eloquentjavascript.net/04_data.html)
