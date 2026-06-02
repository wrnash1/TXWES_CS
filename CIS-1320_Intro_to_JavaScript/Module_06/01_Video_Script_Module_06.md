# Video Script: CIS-1320 — Introduction to JavaScript

## Module 06 — Functions and Arrow Functions

**Estimated Duration:** 16–19 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use DevTools Console for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - The hoisting demo (function declaration vs expression) is the highest-value exam content — show both errors side by side.
> - For the arrow function demos, write the full-form first and then progressively shorten to the concise form so students see the transformation.
> - The `this` keyword behavior difference between regular and arrow functions is a common interview trap — mention it briefly but note it is covered more deeply in the Objects module.
> - Parameters vs arguments: use the analogy "parameter is the label on the box; argument is what you put in the box."

---

## [00:00 – 01:00] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 06 | Functions and Arrow Functions | CIS-1320"]**

"Module 06 is about functions — the single most important concept in JavaScript, and in programming generally. A function is a named, reusable block of code. Instead of writing the same logic in ten places, you write it once as a function and call it whenever you need it.

JavaScript has three ways to define a function: function declarations, function expressions, and arrow functions. Each has different behavior around hoisting and the `this` keyword. We will cover all three, plus parameters, return values, default parameters, and rest parameters. Let us start with the most traditional form."

---

## [01:00 – 05:00] Part 1 — Function Declarations and Calls

**[SHOW SLIDE: "Function Declaration"]**

"A function declaration uses the `function` keyword followed by a name, a parameter list, and a body:

```javascript
function greet(name) {
  return 'Hello, ' + name + '!';
}
```

You call a function by writing its name followed by parentheses with any arguments:

```javascript
const message = greet('Alice');
console.log(message);   // 'Hello, Alice!'
```

Three terms to know precisely:

- **Parameter** — the variable listed in the function definition (`name` here). It is a placeholder.
- **Argument** — the actual value passed when the function is called (`'Alice'` here).
- **Return value** — the value the function sends back to its caller via `return`.

Think of it this way: the parameter is the label on the box, the argument is what you put inside.

[PAUSE]

**[DEMO]**

```javascript
function add(a, b) {
  return a + b;
}

console.log(add(3, 4));    // 7
console.log(add(10, -2)); // 8
console.log(add(1.5, 2.5)); // 4
```

The function receives two numbers and returns their sum. Every time you call `add`, the parameters `a` and `b` receive new values.

[PAUSE]

**What happens when a function has no `return` statement?**

```javascript
function sayHello(name) {
  console.log('Hi,', name);
  // no return
}

const result = sayHello('Bob');
console.log(result);   // undefined
```

Without an explicit `return` statement, a function returns `undefined` automatically. If you try to use the result of a void function — one that produces output as a side effect but returns nothing — you will get `undefined`. This is a common source of bugs.

[PAUSE]

**[DEMO — multiple parameters and return]**

```javascript
function calculateArea(width, height) {
  const area = width * height;
  return area;
}

console.log(calculateArea(5, 3));    // 15
console.log(calculateArea(10, 4));   // 40
```

`return` exits the function immediately. Any code after `return` in the same block does not execute:

```javascript
function earlyReturn(x) {
  if (x < 0) {
    return 'negative';
  }
  return 'non-negative';
}

console.log(earlyReturn(-5));   // 'negative' — second return never reached
console.log(earlyReturn(3));    // 'non-negative'
```

Early returns like this are a common and intentional pattern — they handle edge cases at the top and let the main logic flow without nesting."

---

## [05:00 – 08:00] Part 2 — Function Expressions and Hoisting

**[SHOW SLIDE: "Function Expressions and Hoisting"]**

"A function expression assigns a function to a variable:

```javascript
const multiply = function(a, b) {
  return a * b;
};

console.log(multiply(3, 4));   // 12
```

The function itself has no name — it is an **anonymous function** assigned to the variable `multiply`. The behavior is the same, but the hoisting behavior is different.

[PAUSE]

**Hoisting — the most-tested difference between declarations and expressions.**

Function declarations are hoisted completely — the engine moves the entire function to the top of its scope before execution. This means you can call a function declaration before the line where it appears:

**[DEMO]**

```javascript
console.log(square(5));   // 25 — works even before the declaration

function square(n) {
  return n * n;
}
```

Function expressions assigned to `const` or `let` are NOT hoisted. The variable is hoisted to the Temporal Dead Zone, but the function value is not assigned until the line is reached. Calling it before the line throws a `ReferenceError`:

```javascript
console.log(cube(3));   // ReferenceError: Cannot access 'cube' before initialization

const cube = function(n) {
  return n * n * n;
};
```

**[SHOW SIDE-BY-SIDE on screen]**

| | Declared before definition? | Error if called early? |
|---|---|---|
| Function declaration | Yes — hoisted completely | No |
| Function expression (`const`) | No — TDZ applies | Yes — ReferenceError |

The practical recommendation: define functions before you call them, regardless of hoisting. Relying on hoisting makes code harder to read."

---

## [08:00 – 12:00] Part 3 — Arrow Functions

**[SHOW SLIDE: "Arrow Functions (ES6)"]**

"ES6 introduced arrow functions — a shorter syntax for function expressions. The arrow `=>` replaces the `function` keyword.

Let us transform a regular function expression into an arrow function step by step:

**[DEMO — progressive shortening]**

```javascript
// Step 1: regular function expression
const double = function(n) {
  return n * 2;
};

// Step 2: arrow function — full form
const double = (n) => {
  return n * 2;
};

// Step 3: single parameter — parentheses optional
const double = n => {
  return n * 2;
};

// Step 4: single expression body — braces and return optional (implicit return)
const double = n => n * 2;
```

All four forms produce identical behavior. Call them the same way:

```javascript
console.log(double(5));    // 10
console.log(double(12));   // 24
```

[PAUSE]

**Multiple parameters — parentheses required:**

```javascript
const add = (a, b) => a + b;
console.log(add(3, 7));   // 10
```

**No parameters — empty parentheses required:**

```javascript
const greetWorld = () => 'Hello, world!';
console.log(greetWorld());   // 'Hello, world!'
```

**Multi-statement body — braces and explicit `return` required:**

```javascript
const clamp = (value, min, max) => {
  if (value < min) return min;
  if (value > max) return max;
  return value;
};

console.log(clamp(5, 0, 10));   // 5
console.log(clamp(-3, 0, 10));  // 0
console.log(clamp(15, 0, 10));  // 10
```

When the body has braces, the implicit return is gone — you must write `return` explicitly, just like in a regular function.

[PAUSE]

**Arrow functions and `this`:**

Arrow functions do not have their own `this` — they inherit `this` from the surrounding context. This matters when working with objects and event handlers, which we cover in the Objects module. For now, just know: if you need `this` to refer to the function's own object context, use a regular function. Arrow functions are best for callbacks and short utility functions."

---

## [12:00 – 15:30] Part 4 — Default and Rest Parameters

**[SHOW SLIDE: "Default and Rest Parameters"]**

"ES6 also added two parameter features that appear on the JSE exam: default parameters and rest parameters.

**Default parameters** let you specify a fallback value for a parameter when the caller does not provide one:

**[DEMO]**

```javascript
function greet(name = 'stranger') {
  return 'Hello, ' + name + '!';
}

console.log(greet('Alice'));   // 'Hello, Alice!'
console.log(greet());          // 'Hello, stranger!' — default used
console.log(greet(undefined)); // 'Hello, stranger!' — undefined triggers default
console.log(greet(null));      // 'Hello, null!' — null does NOT trigger default
```

Three rules to know:

1. Default parameters are used when the argument is `undefined` — either omitted or explicitly passed as `undefined`.
2. Passing `null` does **not** trigger the default — `null` is a real value.
3. Default parameters can be expressions: `function multiply(a, b = a * 2)` is valid.

[PAUSE]

**Rest parameters** collect any number of remaining arguments into an array:

```javascript
function sum(...numbers) {
  let total = 0;
  for (const n of numbers) {
    total += n;
  }
  return total;
}

console.log(sum(1, 2, 3));         // 6
console.log(sum(10, 20, 30, 40));  // 100
console.log(sum());                // 0
```

The `...numbers` syntax collects all arguments passed to `sum` into the array `numbers`. The function works regardless of how many arguments are provided.

Rules for rest parameters:

- The rest parameter must be the **last** parameter.
- There can only be one rest parameter per function.
- `...rest` before the last position is a syntax error.

```javascript
function first(a, b, ...rest) {
  console.log('a:', a);
  console.log('b:', b);
  console.log('rest:', rest);
}

first(1, 2, 3, 4, 5);
// a: 1
// b: 2
// rest: [3, 4, 5]
```

The first two arguments are captured by `a` and `b`. Everything else goes into `rest` as an array."

---

## [15:30 – 17:30] Closing — Lab Preview

**[SHOW SLIDE: "Module 06 Lab Preview"]**

"The Module 06 lab has four parts.

Part 1 uses function declarations — you will write functions with parameters and return values, trigger both the `undefined`-return case and the early return pattern, and observe hoisting by calling a declaration before its definition.

Part 2 uses function expressions — you will write arrow functions and progressively convert a regular function to the shortest valid arrow form, observing each step.

Part 3 covers default and rest parameters — you will write functions that use `undefined` and `null` as arguments to see which triggers the default, and use rest parameters to build a variadic sum function.

Part 4 is a practical integration exercise — you will build a small grade-report generator that uses function declarations, arrow functions, default parameters, and rest parameters together in one program.

The quiz focuses heavily on hoisting behavior — which form can be called before its definition — and the arrow function implicit return rules. Read the reading guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 06 — Functions and Arrow Functions]**

---

## Additional Resources

- [MDN — Functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [MDN — Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [MDN — Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [MDN — Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Eloquent JavaScript — Chapter 3: Functions](https://eloquentjavascript.net/03_functions.html)
