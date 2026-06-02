# Reading Guide: Module 03 — Data Types and Operators

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Every value in a JavaScript program has a type. The type determines what operations are valid on the value, how it behaves when combined with other values, and what the engine does when it needs to convert between types. Understanding JavaScript's type system — especially the coercion rules and the `==` vs `===` distinction — is essential for writing correct comparisons and is one of the most heavily tested areas on the JSE certification exam.

---

## 1. The Seven Primitive Types

JavaScript has seven **primitive** types. Primitives are immutable — a primitive value itself cannot be changed. When you reassign a variable, you replace the value; you do not modify the original.

| Type | Description | Examples |
|---|---|---|
| `number` | All numeric values — integers and decimals | `42`, `3.14`, `-7`, `0`, `Infinity` |
| `string` | Sequence of characters | `'hello'`, `"world"`, `` `template` `` |
| `boolean` | Logical true or false | `true`, `false` |
| `null` | Intentional absence of a value | `null` |
| `undefined` | Declared but not yet assigned | `undefined` |
| `symbol` | Unique identifier (ES6) | `Symbol('id')` |
| `bigint` | Integer beyond Number precision (ES2020) | `9007199254740993n` |

Everything else in JavaScript — arrays, functions, dates, regular expressions — is an **object**.

### Checking Types with `typeof`

The `typeof` operator returns a string describing the type of its operand:

```javascript
typeof 42            // 'number'
typeof 3.14          // 'number'
typeof 'hello'       // 'string'
typeof true          // 'boolean'
typeof undefined     // 'undefined'
typeof null          // 'object'   ← historical bug — not 'null'
typeof Symbol()      // 'symbol'
typeof 42n           // 'bigint'
typeof {}            // 'object'
typeof []            // 'object'   ← arrays are objects
typeof function(){}  // 'function'
```

**Critical exam trap:** `typeof null` returns `'object'`, not `'null'`. This is a bug from JavaScript's first version that was never fixed because correcting it would break existing websites. You must know this.

`typeof` on an undeclared variable returns `'undefined'` rather than throwing a `ReferenceError` — making it safe for feature detection:

```javascript
if (typeof someFeature === 'undefined') {
  // someFeature is not available in this environment
}
```

---

## 2. The `number` Type in Depth

### Integers and Decimals

JavaScript has a single `number` type that represents both integers and floating-point numbers, using 64-bit IEEE 754 double-precision format.

```javascript
const a = 42;        // integer
const b = 3.14;      // decimal
const c = -7;        // negative
const d = 1e6;       // scientific notation — 1,000,000
const e = Infinity;  // special value
const f = -Infinity; // special value
```

### `NaN` — Not a Number

`NaN` is a special numeric value representing the result of an invalid or undefined numeric operation:

```javascript
'hello' - 5     // NaN
0 / 0           // NaN
Math.sqrt(-1)   // NaN
parseInt('abc') // NaN
```

`NaN` has two unusual properties:

1. `typeof NaN === 'number'` — it is of type number, despite the name
2. `NaN !== NaN` — NaN is the only value not equal to itself

To check whether a value is `NaN`, use `Number.isNaN()`:

```javascript
Number.isNaN(NaN)          // true
Number.isNaN(42)           // false
Number.isNaN('hello')      // false — the string is not NaN; it is a string
Number.isNaN(0 / 0)        // true
```

Do not use the global `isNaN()` function — it coerces its argument first, leading to surprising results (`isNaN('hello')` returns `true`). Prefer `Number.isNaN()`.

### Number Precision Limit

JavaScript numbers have a precision limit: `Number.MAX_SAFE_INTEGER` is `9007199254740991` (2^53 − 1). Operations on integers beyond this value may lose precision. Use `BigInt` for very large integers.

---

## 3. Strings

Strings can be delimited by single quotes, double quotes, or backtick template literals. The style is interchangeable for basic strings, but template literals enable embedded expressions:

```javascript
const name = 'Alice';
const greeting1 = 'Hello, ' + name + '!';         // concatenation
const greeting2 = `Hello, ${name}!`;               // template literal
console.log(greeting1);   // Hello, Alice!
console.log(greeting2);   // Hello, Alice!
```

Template literals (backtick strings) are covered more thoroughly in the strings module. For now, know that `${}` inside a template literal evaluates the expression inside the braces and inserts the result.

### String Properties

Strings have a `length` property and many methods:

```javascript
'hello'.length          // 5
'hello'.toUpperCase()   // 'HELLO'
'  hello  '.trim()      // 'hello'
'hello world'.split(' ') // ['hello', 'world']
```

---

## 4. Arithmetic Operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition / Concatenation | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `10 / 4` | `2.5` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 10` | `1024` |

### The `+` Operator: Addition vs. Concatenation

The `+` operator performs numeric addition when both operands are numbers. When at least one operand is a string, it performs string concatenation. This is **implicit type coercion**.

```javascript
5 + 3          // 8 — numeric addition
'5' + 3        // '53' — string concatenation ('5' + '3' → '53')
5 + '3'        // '53' — string concatenation
5 + 3 + '1'    // '81' — left-to-right: (5+3)=8, then 8+'1'='81'
'1' + 5 + 3    // '153' — left-to-right: '1'+5='15', then '15'+3='153'
```

This left-to-right evaluation rule is frequently tested. The order of operands changes the result.

### Non-`+` Operators Always Coerce to Number

The `-`, `*`, `/`, and `%` operators always attempt to convert their operands to numbers:

```javascript
'10' - 5       // 5 — '10' coerced to 10
'4' * '3'      // 12 — both coerced to numbers
'hello' - 5    // NaN — 'hello' cannot be converted to a number
true + 1       // 2 — true coerces to 1
false + 1      // 1 — false coerces to 0
null + 1       // 1 — null coerces to 0
undefined + 1  // NaN — undefined coerces to NaN
```

---

## 5. Assignment Operators

| Operator | Meaning | Example |
|---|---|---|
| `=` | Assign | `x = 5` |
| `+=` | Add and assign | `x += 3` → `x = x + 3` |
| `-=` | Subtract and assign | `x -= 2` → `x = x - 2` |
| `*=` | Multiply and assign | `x *= 4` → `x = x * 4` |
| `/=` | Divide and assign | `x /= 2` → `x = x / 2` |
| `%=` | Modulo and assign | `x %= 3` → `x = x % 3` |
| `**=` | Exponentiate and assign | `x **= 2` → `x = x ** 2` |
| `++` | Increment by 1 | `x++` or `++x` |
| `--` | Decrement by 1 | `x--` or `--x` |

### Pre-increment vs Post-increment

`x++` (post-increment) uses the current value first, then increments. `++x` (pre-increment) increments first, then uses the new value.

```javascript
let a = 5;
let b = a++;   // b = 5 (used before increment), a = 6
let c = ++a;   // a = 7 (incremented first), c = 7
```

In most contexts — especially `for` loops — the difference does not matter. `i++` is the standard convention.

---

## 6. Comparison Operators

| Operator | Description |
|---|---|
| `===` | Strict equality — same value AND same type |
| `!==` | Strict inequality — different value OR different type |
| `==` | Loose equality — same value after coercion |
| `!=` | Loose inequality — different value after coercion |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

### Strict Equality (`===`) — Always Prefer This

`===` compares value and type without any conversion. If the types differ, the result is `false`:

```javascript
5 === 5       // true — same value, same type
5 === '5'     // false — number vs string
0 === false   // false — number vs boolean
null === undefined  // false — null vs undefined
```

### Loose Equality (`==`) — Know It for the Exam, Avoid It in Code

`==` performs type coercion before comparing. The coercion rules are complex. The most important cases to memorize:

```javascript
0 == false          // true — false coerces to 0
'' == false         // true — '' coerces to 0, false coerces to 0
0 == ''             // true — both coerce to 0
null == undefined   // true — these two are loosely equal to each other only
null == 0           // false — null does not loosely equal 0
null == false       // false — null only loosely equals undefined
NaN == NaN          // false — NaN is not equal to anything
'5' == 5            // true — '5' coerced to 5
```

**Rule:** Always use `===` and `!==` in your own code. Understand `==` for the exam and for reading legacy code.

---

## 7. Logical Operators

| Operator | Name | Description |
|---|---|---|
| `&&` | AND | `true` if both operands are truthy |
| `\|\|` | OR | `true` if at least one operand is truthy |
| `!` | NOT | Inverts the boolean value |

### Short-Circuit Evaluation

`&&` and `||` do not always evaluate both operands — they use **short-circuit evaluation**:

- `&&` stops and returns the first **falsy** operand. If all operands are truthy, returns the last one.
- `||` stops and returns the first **truthy** operand. If all operands are falsy, returns the last one.

```javascript
'hello' && 42        // 42 — both truthy, returns last
0 && 'hello'         // 0 — 0 is falsy, short-circuits, returns 0
'hello' || 42        // 'hello' — first is truthy, returns it
0 || 'default'       // 'default' — 0 is falsy, returns second
false || null || ''  // '' — all falsy, returns last
```

This behavior enables common patterns:

```javascript
// Default value pattern
const name = userInput || 'Anonymous';

// Guard pattern — only calls method if obj exists
const len = obj && obj.name && obj.name.length;
```

---

## 8. Falsy and Truthy Values

JavaScript converts values to booleans automatically in conditions (`if`, `while`, `&&`, `||`). The result is always either `true` (truthy) or `false` (falsy).

### Falsy Values — Exactly Six

| Value | Type |
|---|---|
| `false` | boolean |
| `0` | number (also `-0` and `0n`) |
| `''` | string (empty string only) |
| `null` | null |
| `undefined` | undefined |
| `NaN` | number |

### Everything Else Is Truthy

Including:

| Value | Truthy? | Note |
|---|---|---|
| `'0'` | Yes | Non-empty string |
| `'false'` | Yes | Non-empty string |
| `[]` | Yes | Empty array |
| `{}` | Yes | Empty object |
| `1` | Yes | Non-zero number |
| `-1` | Yes | Non-zero number |

The most surprising truthy values are `'0'`, `[]`, and `{}`. Students frequently guess these are falsy. They are not.

```javascript
Boolean('0')    // true
Boolean([])     // true
Boolean({})     // true
Boolean(0)      // false
Boolean('')     // false
```

---

## 9. `null` vs `undefined`

Both represent "no value," but they have distinct meanings:

| | `null` | `undefined` |
|---|---|---|
| Meaning | Intentional absence — developer set it explicitly | Unintentional — not yet assigned |
| Set by | Developer | JavaScript engine (or developer) |
| `typeof` | `'object'` (historical bug) | `'undefined'` |
| Loosely equal to each other? | `null == undefined` → `true` | — |
| Strictly equal to each other? | `null === undefined` → `false` | — |
| Default return value of a function? | No | Yes |
| Default value of uninitialized `var`? | No | Yes — `undefined` |

```javascript
let declared;
console.log(declared);      // undefined — declared but not assigned

let intentional = null;
console.log(intentional);   // null — developer's intentional placeholder

function noReturn() {}
console.log(noReturn());    // undefined — no return statement
```

---

## 10. JSE Certification Exam Tips

1. **`typeof null === 'object'`** — not `'null'`. Historical bug. Know it.

2. **`typeof NaN === 'number'`** — NaN is a numeric value. Know it.

3. **`NaN !== NaN`** — NaN is not equal to anything, including itself. Use `Number.isNaN()` to check.

4. **String + number = string** — `'5' + 3 = '53'`. The `+` operator triggers string concatenation when either operand is a string.

5. **Left-to-right evaluation changes results** — `5 + 3 + '1'` is `'81'`, but `'1' + 5 + 3` is `'153'`.

6. **Non-`+` operators coerce to number** — `'5' - 3 = 2`, `'hello' - 3 = NaN`.

7. **Always use `===`** — `==` produces non-obvious results (`0 == false` is `true`, `'' == false` is `true`).

8. **`null == undefined` is `true`; `null === undefined` is `false`** — the only two values loosely equal to each other are null and undefined.

9. **`'0'`, `[]`, and `{}` are truthy** — despite looking like empty/zero values, they are all truthy.

10. **Falsy values are exactly six**: `false`, `0`, `''`, `null`, `undefined`, `NaN`.

---

## 11. Study Checklist

- [ ] Watch the Module 03 video lecture by Professor Nash.
- [ ] Read Chapter 1 (Values, Types, and Operators) of [Eloquent JavaScript](https://eloquentjavascript.net/01_values.html).
- [ ] Read the MDN article on [JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures).
- [ ] Open the browser console and run every example in Section 6 (loose equality) by hand.
- [ ] Write out the six falsy values from memory, then check against Section 8.
- [ ] Predict the output of `1 + 2 + '3'` and `'1' + 2 + 3` before running them, then verify.
- [ ] Complete the Module 03 Lab.
- [ ] Complete the Module 03 Quiz.
