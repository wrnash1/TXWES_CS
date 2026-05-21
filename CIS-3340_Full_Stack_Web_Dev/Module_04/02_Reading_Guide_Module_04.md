# Reading Guide: Module 04 - JavaScript DOM Manipulation
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 04 - JavaScript DOM Manipulation**! This module introduces the Document Object Model (DOM) — the browser's in-memory tree representation of an HTML document — and the JavaScript APIs that read, modify, create, and delete its nodes at runtime. You will learn how to select elements with query selectors, attach event listeners for user interactions, and update page content dynamically without a full page reload. DOM manipulation is the foundation of every interactive web interface, and understanding it deeply will help you write more efficient React components later in the course.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Document Object Model (DOM)**: A programming interface that represents an HTML (or XML) document as a hierarchical tree of node objects — including element nodes, text nodes, and attribute nodes. Browsers parse HTML into the DOM on page load, and JavaScript can traverse, modify, add, and remove nodes in this tree to dynamically change what the user sees without fetching a new page from the server.
*   **Query selectors**: JavaScript methods that search the DOM tree and return matching element nodes using CSS selector syntax. `document.querySelector(selector)` returns the first matching element; `document.querySelectorAll(selector)` returns a static `NodeList` of all matches. These methods replaced older approaches like `getElementById` and `getElementsByClassName` for most use cases because they accept any valid CSS selector string.
*   **Event listeners**: Functions registered on DOM elements via `element.addEventListener(type, handler)` that execute in response to user or browser events — such as `'click'`, `'keydown'`, `'submit'`, `'mouseover'`, or `'DOMContentLoaded'`. Event listeners decouple the UI interaction logic from the HTML markup and allow multiple handlers to be registered on the same element without overwriting each other.
*   **Bubbling and capturing**: The two phases of DOM event propagation. During the **capturing phase**, an event travels down the DOM tree from the `window` to the target element. During the **bubbling phase**, it travels back up from the target to the `window`. By default, `addEventListener` registers handlers in the bubbling phase; passing `true` as the third argument enables capturing. `event.stopPropagation()` halts further propagation in either phase.
*   **Dynamic DOM trees**: The ability to programmatically create, insert, modify, and remove DOM nodes at runtime using methods like `document.createElement()`, `element.appendChild()`, `element.insertBefore()`, `element.remove()`, and `element.innerHTML`. Dynamic DOM updates enable Single Page Application behavior — new content appears without navigating to a new URL or triggering a full page reload.

---

### 2. Certification Exam Tips
*   **DOM Knowledge Supports AWS Lambda Front-End Integration:** The DVA-C02 exam includes scenarios where a front-end application fetches data from an AWS Lambda-backed API Gateway endpoint using `fetch()` and updates the UI. The fetch call returns a Promise, and the resolved data is rendered by manipulating the DOM — this is exactly the DOM + async pattern you are building here.
*   **Event Delegation Reduces Memory Overhead:** When rendering large dynamic lists (e.g., a table of 500 API results), attaching individual click listeners to each row is inefficient. Event delegation — attaching a single listener to the parent container and checking `event.target` — is the scalable pattern. Know this for both front-end performance questions and full-stack architecture scenarios.
*   **Study Resource:** The MDN JavaScript DOM guide is the authoritative reference. [MDN — Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) explains the node tree structure, traversal methods, and manipulation APIs with interactive examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **JavaScript DOM Manipulation** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/) — the primary free textbook for this course.
*   **Required Video:** Watch the JavaScript DOM section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — an open-access walkthrough covering query selectors, events, and dynamic element creation.

---

### Lab & Command Integration
In this week's hands-on lab, you will apply DOM manipulation concepts directly:
*   **Implement DOM selector query loops**: Use `document.querySelectorAll()` to select a collection of list items, iterate over the resulting `NodeList` with `forEach()`, and log or transform each element's text content.
*   **Add keydown/click event listeners to forms**: Attach `addEventListener('submit', handler)` to a form element and `addEventListener('keydown', handler)` to a text input — calling `event.preventDefault()` to stop the default form submission and instead handle the input data in JavaScript.
*   **Dynamically append list elements using JavaScript**: Use `document.createElement('li')`, set its `textContent`, and call `parentElement.appendChild()` to add new items to an unordered list at runtime based on user input.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read the section covering **JavaScript DOM Manipulation** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/).
- [ ] Watch the JavaScript DOM section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Open the browser Console (F12) and practice running DOM queries on a live webpage before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
