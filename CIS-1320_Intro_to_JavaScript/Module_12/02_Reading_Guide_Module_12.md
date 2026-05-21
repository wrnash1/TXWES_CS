# Reading Guide: Module 12 - Event Handling & Listeners
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 12 - Event Handling & Listeners**! This week you will learn how to make web pages respond to user actions — clicks, keypresses, form submissions, and more — by registering event listeners. Understanding event flow (bubbling and capturing), the event object, and `preventDefault` is essential for the JSE exam and for building any interactive application.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **addEventListener**: A DOM method called on an element that registers a callback function to execute whenever a specified event occurs (e.g., `btn.addEventListener("click", handleClick)`). Multiple listeners can be added for the same event on the same element, unlike the older `onclick` property.
*   **click event**: A browser event that fires when a user clicks (or taps on mobile) an element. It is the most commonly used event type. The handler receives an event object containing information about the click (coordinates, target element, modifier keys held, etc.).
*   **event object**: The argument automatically passed to an event handler function when an event fires. It contains properties like `target` (the element that triggered the event), `type` (the event name), `key` (for keyboard events), and methods like `preventDefault()` and `stopPropagation()`.
*   **event target**: The `event.target` property that references the specific DOM element on which the event originally occurred. Useful in event delegation when a parent element listens for events that originate from any of its children.
*   **preventDefault**: A method on the event object (`event.preventDefault()`) that cancels the browser's default behavior for the event. For example, calling it on a form's `submit` event prevents the page from reloading, and calling it on a link's `click` event prevents navigation.
*   **Bubbling**: The default phase of event propagation where an event triggered on a child element travels upward through its ancestor elements in the DOM tree. A click on a `<button>` inside a `<div>` will first fire handlers on the button, then on the div, then on the body, and so on, unless `stopPropagation()` is called.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests the difference between `event.target` and `event.currentTarget`. `target` is the element that originally triggered the event; `currentTarget` is the element on which the listener is currently running. They differ when events bubble.
*   **Scenario Trap:** A common trap shows a form where `event.preventDefault()` is missing from the submit handler, causing the page to reload before any JavaScript logic runs. Recognize that any form submission validation or processing requires calling `preventDefault()` first.
*   **Study Resource:** [MDN – Introduction to events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events) is a well-structured beginner-to-intermediate guide that covers event listeners, event objects, bubbling, and `preventDefault` with practical examples. Read the entire article before the lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 15 – Handling Events** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). This chapter covers event listeners, propagation, default actions, and keyboard/mouse events.
*   **Required Video:** Watch the video lecture on **Event Handling & Listeners** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on addEventListener, the event object, bubbling, and preventDefault).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Attach a click handler to a button**: Select a `<button>` element and call `addEventListener("click", ...)` with an arrow function that logs a message to the console.
*   **Access event details using the event parameter**: Inside the handler, log `event.target`, `event.type`, and `event.clientX`/`event.clientY` to see the information available in the event object.
*   **Use preventDefault on a form submit event**: Add a listener for the form's `submit` event; call `event.preventDefault()` to stop the page reload, then log the form input values.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 15 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the event handling and event object segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
