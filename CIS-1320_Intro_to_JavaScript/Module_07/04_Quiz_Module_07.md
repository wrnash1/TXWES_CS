# Quiz: Module 07 - Objects & Properties
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which syntax is required to access an object property dynamically using a variable containing the property name?
*   A) dot notation (object.variableName)
*   B) bracket notation (object[variableName])
*   C) parenthetical notation (object(variableName))
*   D) arrow notation (object->variableName)
*   **Correct Answer:** B) Bracket notation allows variable-based dynamic key lookup (e.g. `obj[key]`), whereas dot notation expects a literal identifier name.
*   **Distractor Analysis:**
    *   *Why correct:* Bracket notation allows variable-based dynamic key lookup (e.g. `obj[key]`), whereas dot notation expects a literal identifier name.
    *   A will lookup a property literally named 'variableName'. C and D are syntactically invalid for property access in JavaScript.

---

**Question 2**
Which of the following most accurately describes the **`this` keyword** inside a regular function method of an object?
*   A) `this` always refers to the global `window` object, regardless of how the method is called
*   B) `this` refers to the object on which the method was called at runtime (dynamic binding)
*   C) `this` is undefined inside any function that is a property of an object
*   D) `this` refers to the function itself, allowing the function to call itself recursively
*   **Correct Answer:** B) `this` refers to the object on which the method was called at runtime (dynamic binding).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `this` in a regular method refers to the calling object, not the global object; it only falls back to global (or `undefined` in strict mode) if the function is called without an object context.
    *   *Why B is correct:* In a regular function, `this` is bound dynamically — `obj.method()` causes `this` inside `method` to be `obj`.
    *   *Why C is incorrect:* `this` is not automatically `undefined` inside object methods; it is `undefined` inside arrow functions in strict mode when there is no outer `this`.
    *   *Why D is incorrect:* `this` does not refer to the function itself; that would require `arguments.callee` (deprecated) or a named function reference.

---

**Question 3**
A developer has an object `config` and a string variable `key = "timeout"`. Which expression correctly reads the `timeout` property?
*   A) `config.key`
*   B) `config[key]`
*   C) `config.timeout(key)`
*   D) `config->key`
*   **Correct Answer:** B) `config[key]`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `config.key` looks for a property literally named `"key"`, not the value stored in the variable `key`.
    *   *Why B is correct:* Bracket notation evaluates the expression inside the brackets, so `config["timeout"]` is accessed via the variable `key`.
    *   *Why C is incorrect:* `config.timeout(key)` attempts to call `timeout` as a function, which would throw a `TypeError` if it is not callable.
    *   *Why D is incorrect:* `->` is not valid JavaScript property access syntax; it is used in some other languages (like PHP or C).

---

**Question 4**
While working on **Objects & Properties**, a developer defines the following:
```javascript
const user = {
  name: "Alice",
  greet: () => {
    return "Hello, " + this.name;
  }
};
console.log(user.greet());
```
What is logged?
*   A) `"Hello, Alice"` because `this` refers to the `user` object
*   B) `"Hello, undefined"` because arrow functions do not bind `this` to the calling object
*   C) A `TypeError` because arrow functions cannot be used as object properties
*   D) `"Hello, "` because strings require template literals inside methods
*   **Correct Answer:** B) `"Hello, undefined"` because arrow functions do not bind `this` to the calling object.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Arrow functions capture `this` from the surrounding lexical scope (here, the module/global scope), not from the object — so `this.name` is `undefined`.
    *   *Why B is correct:* This is the classic arrow function `this` trap: `this` inside the arrow refers to whatever `this` was where the object literal was written, not to `user`.
    *   *Why C is incorrect:* Arrow functions can be object properties; they just do not bind `this` to the object.
    *   *Why D is incorrect:* String concatenation with `+` works fine; the issue is `this.name` being `undefined`.

---

**Question 5**
What does `Object.keys(obj)` return?
*   A) An array of the object's own enumerable property values
*   B) An array of the object's own enumerable property names (keys)
*   C) A boolean indicating whether the object has any properties
*   D) A copy of the object with all keys converted to lowercase
*   **Correct Answer:** B) An array of the object's own enumerable property names (keys).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes `Object.values(obj)`, which returns an array of values.
    *   *Why B is correct:* `Object.keys(obj)` returns an array of strings representing the names of the object's own enumerable properties.
    *   *Why C is incorrect:* `Object.keys()` always returns an array; you would check `Object.keys(obj).length > 0` for emptiness.
    *   *Why D is incorrect:* `Object.keys()` does not modify the keys or return a copy of the object.
