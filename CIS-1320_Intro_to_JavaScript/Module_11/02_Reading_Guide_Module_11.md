# Reading Guide: Module 11 - DOM Manipulation & Styling
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 11 - DOM Manipulation & Styling**! This week you will go beyond reading the DOM to actively modifying it: creating new elements, inserting them into the page, changing CSS classes, and setting attributes. These techniques are the core of interactive web development and are tested on the JSE exam in both conceptual and code-reading questions.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **createElement**: A `document` method that creates a new HTML element node in memory but does not yet insert it into the page (e.g., `const li = document.createElement("li")`). The element must be appended to an existing node with `appendChild` or `append` before it becomes visible.
*   **appendChild**: A method on any DOM node that inserts a child node as the **last child** of the parent element (e.g., `ul.appendChild(li)`). If the node being appended already exists in the DOM, it is moved from its current position.
*   **classList**: A read-only property that returns a `DOMTokenList` representing the space-separated CSS classes of an element. Its methods — `add()`, `remove()`, `toggle()`, and `contains()` — let you manage classes without overwriting the full `className` string.
*   **setAttribute**: A method that adds or updates an HTML attribute on an element (e.g., `img.setAttribute("alt", "A sunset")`). It can set standard attributes like `src`, `href`, `disabled`, and custom `data-*` attributes. Use `getAttribute` to read a value back.
*   **Inline styles**: CSS rules applied directly to an element through its `style` property in JavaScript (e.g., `element.style.backgroundColor = "red"`). Inline styles have the highest specificity and override stylesheet rules. Property names use camelCase in JS (e.g., `fontSize`, not `font-size`).
*   **DOM hierarchy**: The parent-child-sibling structure of nodes in the DOM tree. Key traversal properties include `parentElement`, `children`, `firstElementChild`, `lastElementChild`, `nextElementSibling`, and `previousElementSibling`. Understanding hierarchy is essential for inserting nodes at the correct position.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam presents DOM manipulation scenarios and asks which methods to chain together. Know the typical pattern: `createElement` → set properties/text → `appendChild` to a container. Also know `insertBefore(newNode, referenceNode)` as an alternative to appending at the end.
*   **Scenario Trap:** `classList.add("active")` adds a class without disturbing others; `element.className = "active"` **replaces** all existing classes. The exam often tests whether a student knows which approach to use to preserve other classes on the element.
*   **Study Resource:** [MDN – Document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement) and [MDN – Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) are the key references for this module. The `classList` page shows all available methods with live examples — study the `toggle` method in particular.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 14 – The Document Object Model** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). Focus on the "Building the DOM" sections covering `createElement`, `appendChild`, and attribute manipulation.
*   **Required Video:** Watch the video lecture on **DOM Manipulation & Styling** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on creating/appending elements and managing classes with `classList`).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a new list item element dynamically**: Use `document.createElement("li")` and set its `textContent` to a string.
*   **Append elements to a list container**: Select an existing `<ul>` with `querySelector` and call `appendChild` to add the new `<li>` to the end.
*   **Toggle classes using classList.toggle**: Select a button and a content panel; inside a click handler, call `panel.classList.toggle("hidden")` to show/hide the panel on each click.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the "Building the DOM" sections of Chapter 14 in [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the createElement, appendChild, and classList segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
