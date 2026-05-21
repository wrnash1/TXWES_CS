# Reading Guide: Module 10 - Document Object Model (DOM) Basics
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 10 - Document Object Model (DOM) Basics**! This week you will learn how the browser represents an HTML page as a tree of objects that JavaScript can read and modify. Selecting elements and reading or writing their content are the most fundamental DOM skills, and they are heavily tested on the JSE exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **DOM tree**: The in-memory hierarchical representation of an HTML document that the browser builds when it parses the page. Every HTML element, text node, and attribute becomes a node in the tree. JavaScript can traverse this tree to read, add, remove, or modify content and structure.
*   **document object**: The global JavaScript object that serves as the entry point to the DOM. It represents the entire HTML document and provides methods like `getElementById`, `querySelector`, and `createElement` for accessing and creating elements.
*   **querySelector**: A `document` (or element) method that accepts a CSS selector string and returns the **first** matching element in the DOM, or `null` if no match is found. It uses the same selector syntax as CSS (e.g., `"#main"`, `".btn"`, `"p > span"`).
*   **querySelectorAll**: A `document` (or element) method that accepts a CSS selector string and returns a **static NodeList** of all matching elements. Unlike an HTMLCollection, a NodeList returned by `querySelectorAll` does not update automatically when the DOM changes.
*   **getElementById**: A `document` method that returns the single element with the specified `id` attribute, or `null` if none exists. It is faster than `querySelector("#id")` for ID lookups because the browser maintains an ID index.
*   **textContent**: A property of DOM nodes that gets or sets the text of an element and all its descendants as a plain string. Unlike `innerHTML`, `textContent` does not parse HTML — it treats the value as literal text, which prevents XSS injection.

---

### 2. Certification Exam Tips
*   **Focus Area:** Know the differences between `querySelector` (returns one element or null), `querySelectorAll` (returns all matches as a static NodeList), `getElementById` (single element by ID), and `getElementsByClassName` (live HTMLCollection). The JSE exam asks which to use in a given scenario and what each returns.
*   **Scenario Trap:** Do not confuse `textContent` and `innerHTML`. `textContent` is safe for inserting user-supplied strings because it does not parse HTML tags. `innerHTML` parses the string as HTML, which can execute injected scripts and cause security vulnerabilities — avoid setting `innerHTML` to untrusted input.
*   **Study Resource:** [MDN – Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) gives a clear visual and conceptual overview of the DOM tree. Read the "Important Data Types" and "DOM interfaces" sections to understand nodes, elements, and the `document` object.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 14 – The Document Object Model** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter covers the tree structure, element selection methods, and how to read and update content.
*   **Required Video:** Watch the video lecture on **Document Object Model (DOM) Basics** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on `document`, element selection methods, and `textContent`/`innerHTML`).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Access elements by ID and Class**: Use `document.getElementById("title")` and `document.getElementsByClassName("card")` to select elements; log the returned objects to inspect them in DevTools.
*   **Use querySelector to target elements**: Use `document.querySelector("p.intro")` to retrieve the first paragraph with class `intro`; use `querySelectorAll("li")` to get all list items.
*   **Change element text using textContent**: Select a heading and reassign its `textContent` property to a new string; verify the visible change in the browser.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 14 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the DOM selection and text content segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
