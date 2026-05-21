# Reading Guide: Module 07 - Objects & Properties
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 07 - Objects & Properties**! This week you will learn how JavaScript objects store and organize data as key-value pairs, how to access and modify properties, and how to attach methods. Objects are the fundamental building block of JavaScript programs and are heavily tested across many JSE exam domains.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Object literal**: A syntax for creating an object directly using curly braces with a comma-separated list of `key: value` pairs (e.g., `const car = { make: "Toyota", year: 2020 }`). Object literals are the most common way to create objects in JavaScript without a class or constructor.
*   **Dot notation**: The syntax `object.propertyName` used to access or set a property when the property name is a valid identifier known at write time (e.g., `car.make`). It is the preferred, more readable access style.
*   **Bracket notation**: The syntax `object["propertyName"]` or `object[variable]` used to access properties dynamically — when the key is stored in a variable, computed at runtime, or contains characters that are not valid identifier names (e.g., spaces or hyphens).
*   **Methods**: Functions stored as values on an object's properties. When called as `object.method()`, the function body can use `this` to refer to the object that owns the method. Methods add behavior to data structures.
*   **this keyword**: Inside a regular function method, `this` refers to the object on which the method was called. Its value is determined at call time (dynamic binding). In strict mode or arrow functions, `this` behaves differently — arrow functions inherit `this` from their enclosing scope instead.
*   **Key-value pairs**: The fundamental structure of a JavaScript object — each entry associates a property name (key, always a string or symbol) with a value (which can be any type, including another object or a function). Objects can be iterated using `for...in` or `Object.keys()`.

---

### 2. Certification Exam Tips
*   **Focus Area:** Know when to use dot notation vs bracket notation. The JSE exam presents scenarios where a property name is stored in a variable (requiring bracket notation) or has spaces (requiring bracket notation). Using dot notation in those cases returns `undefined`, not the expected value.
*   **Scenario Trap:** A common trap question shows `this` inside an arrow function method. Because arrow functions capture `this` lexically, `this` inside an arrow method does not refer to the object — it refers to the outer scope (often `undefined` in strict mode or the global object). Choose a regular function for object methods that need `this`.
*   **Study Resource:** [MDN – Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects) is the comprehensive guide for object creation, property access, and methods. Read the "Creating new objects" and "Defining methods" sections before the lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 4 – Data Structures: Objects and Arrays** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). The first half of the chapter covers object creation, property access, and `Object` methods.
*   **Required Video:** Watch the video lecture on **Objects & Properties** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on the objects, dot/bracket notation, and methods segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a user object literal**: Define a `user` object with properties `firstName`, `lastName`, `age`, and `email`.
*   **Access properties using dot and bracket notation**: Retrieve `user.firstName` using dot notation, then retrieve the same property using `user["firstName"]`; store a property name in a variable and use bracket notation to access it dynamically.
*   **Define a method that references this.username**: Add a `fullName()` method to `user` that returns `this.firstName + " " + this.lastName` using a regular function, and call it.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 4 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the objects and properties segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
