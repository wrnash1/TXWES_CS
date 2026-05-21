# Quiz: Module 06 - Functions & Arrow Functions
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
How does an arrow function handle the binding of the 'this' keyword?
*   A) It binds 'this' dynamically at runtime
*   B) It has no 'this' of its own; it inherits 'this' from the lexical context
*   C) It binds 'this' to the global window object always
*   D) It forces 'this' to be undefined
*   **Correct Answer:** B) Arrow functions do not define their own `this` context; they inherit it from the surrounding lexical scope.
*   **Distractor Analysis:**
    *   *Why correct:* Arrow functions do not define their own `this` context; they inherit it from the surrounding lexical scope.
    *   Standard functions bind `this` dynamically based on execution context.

---

**Question 2**
Which of the following most accurately describes **parameters** in a JavaScript function?
*   A) The actual values passed to the function when it is called (e.g., `add(3, 5)` — 3 and 5 are the arguments)
*   B) Named local variables listed in the function definition that receive the values passed by the caller
*   C) Variables declared inside the function body using `let` or `const`
*   D) The value that a function sends back to the caller using the `return` keyword
*   **Correct Answer:** B) Named local variables listed in the function definition that receive the values passed by the caller.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes *arguments* (the values supplied at call time), not parameters (the names in the definition).
    *   *Why B is correct:* Parameters are the named placeholders in the function signature (e.g., `function add(a, b)` — `a` and `b` are parameters).
    *   *Why C is incorrect:* Those are local variables declared inside the body, not parameters listed in the parentheses.
    *   *Why D is incorrect:* That describes the return value, not parameters.

---

**Question 3**
What is the key difference between a function declaration and a function expression?
*   A) Function declarations can only accept one parameter; function expressions accept unlimited parameters.
*   B) Function declarations are hoisted fully and can be called before their definition; function expressions stored in `const`/`let` cannot be called before initialization.
*   C) Function expressions can use the `return` statement; function declarations cannot.
*   D) Function declarations always return `undefined`; function expressions can return any value.
*   **Correct Answer:** B) Function declarations are hoisted fully and can be called before their definition; function expressions stored in `const`/`let` cannot be called before initialization.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Both declarations and expressions accept any number of parameters.
    *   *Why B is correct:* Hoisting is the key distinction — `function foo() {}` is fully hoisted; `const foo = function() {}` is in the temporal dead zone until its line executes.
    *   *Why C is incorrect:* Both declarations and expressions can include a `return` statement.
    *   *Why D is incorrect:* Both can return any value; the return behavior is identical.

---

**Question 4**
While working on **Functions & Arrow Functions**, a developer wants to define a method inside an object that references the object's own properties via `this`. Which function type is most appropriate?
*   A) Arrow function, because it always binds `this` to the calling object
*   B) Regular function declaration or expression, because `this` is bound dynamically to the object that called the method
*   C) Arrow function, because it provides a shorter syntax and `this` behaves the same as in regular functions
*   D) An immediately invoked function expression (IIFE), because `this` must be invoked immediately to work correctly
*   **Correct Answer:** B) Regular function declaration or expression, because `this` is bound dynamically to the object that called the method.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Arrow functions do NOT bind `this` to the calling object; they inherit `this` from the surrounding lexical scope, which is often the wrong context for object methods.
    *   *Why B is correct:* Regular functions bind `this` dynamically — when called as `obj.method()`, `this` inside the function refers to `obj`.
    *   *Why C is incorrect:* `this` in arrow functions does NOT behave the same as in regular functions; that is the entire point of the distinction.
    *   *Why D is incorrect:* IIFEs are for immediately-executed code, not for defining reusable object methods.

---

**Question 5**
What is returned by the following function call?
```javascript
function multiply(a, b = 2) {
  return a * b;
}
console.log(multiply(5));
```
*   A) `NaN` because `b` is `undefined` when only one argument is passed
*   B) `5` because JavaScript ignores the second parameter when it is not provided
*   C) `10` because the default value `b = 2` is used when no second argument is supplied
*   D) A `TypeError` because the function requires two arguments
*   **Correct Answer:** C) `10` because the default value `b = 2` is used when no second argument is supplied.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Default parameters prevent `undefined` from being used; `b` receives `2` when no argument is passed.
    *   *Why B is incorrect:* JavaScript does not ignore the parameter; it applies the default value `2`, making the computation `5 * 2 = 10`.
    *   *Why C is correct:* ES6 default parameters substitute the default value when the caller passes `undefined` or no argument at all.
    *   *Why D is incorrect:* JavaScript does not throw errors for missing arguments; missing parameters receive `undefined` or their default value.
