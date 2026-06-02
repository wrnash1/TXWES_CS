# Video Script: CIS-1320 — Introduction to JavaScript

## Module 03 — Data Types and Operators

**Estimated Duration:** 15–18 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for all [DEMO] sections — run every example live.
> - [PAUSE] = 2 seconds of silence.
> - The type coercion and `==` vs `===` sections are the highest-value exam content — go slowly.
> - Run the `1 + 2 + '3'` vs `'1' + 2 + 3` demo and make students predict the output before showing it.
> - The `typeof null` quirk always generates questions — address it directly.

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 03 | Data Types and Operators | CIS-1320"]**

"Module 03 is about how JavaScript represents data. Every value in a JavaScript program has a type — a category that determines what operations are valid on it and how it behaves when you combine it with other values. JavaScript has seven primitive types plus objects, and it has a system called type coercion that converts between types automatically in certain situations.

Type coercion is where most of the surprising behavior in JavaScript comes from — and it is one of the most tested areas on the JSE exam. By the end of today you will understand all the primitive types, the operators used to work with them, and the coercion rules that produce results that catch developers off guard. Let us get started."

---

## [01:00 – 04:00] Part 1 — The Seven Primitive Types

**[SHOW SLIDE: "JavaScript's Seven Primitive Types"]**

"JavaScript has seven primitive types. Let me go through each one.

**Number** — represents all numeric values, both integers and decimals. JavaScript has only one number type — there is no separate int or float. `42`, `3.14`, `-7`, and `0.001` are all numbers.

**String** — a sequence of characters enclosed in single quotes, double quotes, or backticks. `'hello'`, `\"world\"`, and `` `template` `` are all strings.

**Boolean** — `true` or `false`. Used for conditional logic.

**Null** — represents an intentional absence of value. A developer explicitly assigns `null` to a variable to say 'this currently has no value.'

**Undefined** — means a variable was declared but never assigned a value, or a function parameter was not provided.

**Symbol** — a unique identifier, introduced in ES6. Not heavily tested in this course, but you should know it exists.

**BigInt** — for integers too large for the standard Number type. You write it with an `n` suffix: `9007199254740993n`.

[PAUSE]

**[DEMO — DevTools Console]**

```javascript
typeof 42           // 'number'
typeof 3.14         // 'number'
typeof 'hello'      // 'string'
typeof true         // 'boolean'
typeof undefined    // 'undefined'
typeof null         // 'object'  ← historical bug
typeof Symbol()     // 'symbol'
typeof 42n          // 'bigint'
```

Let me run these live. Notice the result for `typeof null` — it returns `'object'`. This is a well-known bug in JavaScript that has existed since the language was created. It was never fixed because fixing it would break millions of existing websites that depend on this behavior. So you need to know it: `typeof null` is `'object'`, not `'null'`. This appears on the JSE exam.

[PAUSE]

The other result worth noting: `typeof undefined` returns the string `'undefined'`. So `typeof` on an undefined variable is safe — it returns a string rather than throwing an error. This is useful for feature detection:

```javascript
if (typeof someVariable === 'undefined') {
  // variable doesn't exist or was never assigned
}
```"

---

## [04:00 – 07:00] Part 2 — Arithmetic and String Operators

**[SHOW SLIDE: "Operators: Math and String Operations"]**

"JavaScript has the standard arithmetic operators: `+` for addition, `-` for subtraction, `*` for multiplication, `/` for division, `%` for the modulo remainder, and `**` for exponentiation.

**[DEMO]**

```javascript
10 + 3     // 13
10 - 3     // 7
10 * 3     // 30
10 / 3     // 3.3333...
10 % 3     // 1 — remainder when 10 is divided by 3
2 ** 8     // 256 — 2 to the power of 8
```

The `%` operator returns the remainder of division. `10 % 3` is `1` because 10 divided by 3 is 3 with remainder 1. This is useful for things like checking whether a number is even or odd — `n % 2 === 0` is true for even numbers.

[PAUSE]

Now, the `+` operator has a dual role. It performs numeric addition when both operands are numbers. But when at least one operand is a string, it performs **string concatenation** — it joins the strings together.

**[DEMO — predict before running]**

```javascript
5 + 3          // 8 — both numbers, addition
'5' + 3        // '53' — one string, concatenation
5 + '3'        // '53' — one string, concatenation
5 + 3 + '1'    // '81' — left to right: 5+3=8, then 8+'1'='81'
'1' + 5 + 3    // '153' — left to right: '1'+5='15', then '15'+3='153'
```

[PAUSE]

This left-to-right evaluation is critical. `5 + 3 + '1'` gives `'81'` because the engine evaluates `5 + 3` first, getting `8`, then concatenates `8` with `'1'` to get `'81'`. But `'1' + 5 + 3` gives `'153'` because the first operation is string concatenation — `'1' + 5 = '15'` — and once you are in string mode, `'15' + 3 = '153'`.

The `-`, `*`, `/`, and `%` operators do not concatenate — they always attempt numeric conversion.

```javascript
'10' - 5    // 5 — string '10' coerced to number
'10' * 2    // 20 — string '10' coerced to number
'10' / '2'  // 5 — both coerced to numbers
'hello' - 1 // NaN — 'hello' cannot be converted to a number
```

`NaN` stands for Not-a-Number. It is the result of an invalid numeric operation. Importantly, `NaN` is of type `number` — `typeof NaN === 'number'` is `true`."

---

## [07:00 – 10:30] Part 3 — Comparison Operators and Type Coercion

**[SHOW SLIDE: "`==` vs `===`: The Most Important Distinction"]**

"This is the most important section of Module 03. JavaScript has two equality operators — loose equality `==` and strict equality `===`. They look similar but behave very differently.

**Strict equality `===`** compares both the value and the type. No coercion is performed. If the types are different, the result is `false`.

**Loose equality `==`** compares values after performing type coercion. JavaScript attempts to convert the operands to the same type before comparing.

**[DEMO]**

```javascript
5 === 5        // true — same value, same type
5 === '5'      // false — same value, different types (no coercion with ===)

5 == 5         // true
5 == '5'       // true — '5' is coerced to 5, then compared
0 == false     // true — false is coerced to 0
'' == false    // true — '' coerces to 0, false coerces to 0
0 == ''        // true — both coerce to 0
```

[PAUSE]

These `==` results are surprising. `0 == false` is `true`? `'' == false` is `true`? `0 == ''` is `true`? These pass through a coercion table that is complicated and non-obvious. This is exactly why modern JavaScript best practice is to **always use `===`** and never use `==`. Strict equality has no surprises.

[PAUSE]

Two special cases with `null` and `undefined`:

```javascript
null == undefined    // true — they loosely equal each other
null === undefined   // false — different types
null == 0           // false — null only loosely equals undefined, not 0
null == false       // false — same: null only equals undefined with ==
```

And `NaN` — the only value in JavaScript that is not equal to itself:

```javascript
NaN === NaN    // false — NaN is not equal to anything, including itself
NaN == NaN     // false — even loose equality fails
```

To check for NaN, use the built-in function `Number.isNaN()`:

```javascript
Number.isNaN(NaN)         // true
Number.isNaN(42)          // false
Number.isNaN('hello')     // false — 'hello' is not NaN, it is a string
```

[PAUSE]

The inequality operators `!=` and `!==` follow the same rule: `!==` is strict, `!=` is loose. Always prefer `!==`."

---

## [10:30 – 13:00] Part 4 — Logical Operators and Falsy Values

**[SHOW SLIDE: "Logical Operators and Truthiness"]**

"JavaScript has three logical operators: `&&` (AND), `||` (OR), and `!` (NOT).

`&&` returns `true` if both operands are truthy. `||` returns `true` if at least one operand is truthy. `!` inverts a boolean.

**[DEMO]**

```javascript
true && true     // true
true && false    // false
false || true    // true
false || false   // false
!true            // false
!false           // true
```

[PAUSE]

Now the important nuance: JavaScript's logical operators do not always return booleans — they return one of the operands based on **short-circuit evaluation**.

```javascript
'hello' && 42      // 42 — both truthy, returns last evaluated operand
0 && 'hello'       // 0 — 0 is falsy, short-circuits, returns 0
'hello' || 42      // 'hello' — first operand is truthy, returns it
0 || 'default'     // 'default' — 0 is falsy, returns second operand
```

`||` is commonly used to provide a default value: `const name = userInput || 'Anonymous'`. If `userInput` is empty (falsy), you get `'Anonymous'`.

[PAUSE]

This connects to **falsy values** — values that JavaScript treats as `false` in a boolean context. There are exactly six falsy values in JavaScript:

- `false`
- `0` and `-0`
- `''` (empty string)
- `null`
- `undefined`
- `NaN`

Everything else is truthy — including `'0'` (the string zero), `[]` (empty array), `{}` (empty object), and `'false'` (the string false).

```javascript
Boolean(0)         // false
Boolean('')        // false
Boolean(null)      // false
Boolean('0')       // true — non-empty string
Boolean([])        // true — empty array is truthy
Boolean({})        // true — empty object is truthy
```

The `Boolean()` function explicitly converts a value to `true` or `false`. In practice you rarely need to call it — JavaScript does this conversion automatically in `if` conditions and logical operators."

---

## [13:00 – 15:30] Part 5 — `null` vs `undefined` and Assignment Operators

**[SHOW SLIDE: "null vs undefined — Two Different 'Nothings'"]**

"I want to spend a minute on the distinction between `null` and `undefined` because they confuse students and appear regularly on the exam.

**`undefined`** means a variable exists but has never been assigned. It is the default state. When you declare a variable with `var` and do not assign it, JavaScript sets it to `undefined`. When a function does not explicitly return a value, it returns `undefined`. When you access a property that does not exist on an object, you get `undefined`.

**`null`** is an intentional assignment. When a developer writes `let user = null`, they are saying 'I know this variable exists, and I am explicitly setting it to no value right now.' It is a deliberate placeholder.

```javascript
let x;
console.log(x);                  // undefined — declared, not assigned

let user = null;
console.log(user);               // null — explicitly set to nothing

const obj = { name: 'Alice' };
console.log(obj.age);            // undefined — property does not exist
```

[PAUSE]

**Assignment operators** — a quick summary:

```javascript
let n = 10;
n += 5;     // n = n + 5 → 15
n -= 3;     // n = n - 3 → 12
n *= 2;     // n = n * 2 → 24
n /= 4;     // n = n / 4 → 6
n %= 4;     // n = n % 4 → 2
n **= 3;    // n = n ** 3 → 8
```

And the increment/decrement operators:

```javascript
let count = 0;
count++;   // post-increment: use value (0), then increment to 1
count--;   // post-decrement: use value (1), then decrement to 0
++count;   // pre-increment: increment first, then use value
```

The difference between `count++` and `++count` matters when the expression's value is used in another expression — but in practice, `count++` is far more common and you will see it in every `for` loop.

[PAUSE]

That is Module 03. The lab will walk you through type coercion experiments, `==` vs `===` comparisons, and falsy value testing — all in the browser console. Make sure you complete the reading guide before the lab, specifically the coercion table and the falsy values list. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 03 — Data Types and Operators]**

---

## Additional Resources

- [MDN — JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures) — authoritative type reference
- [MDN — Equality comparisons and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) — full `==` coercion table
- [Eloquent JavaScript — Chapter 1: Values, Types, and Operators](https://eloquentjavascript.net/01_values.html) — free textbook coverage
- [JavaScript.info — Type Conversions](https://javascript.info/type-conversions) — clear explanation of implicit coercion rules
