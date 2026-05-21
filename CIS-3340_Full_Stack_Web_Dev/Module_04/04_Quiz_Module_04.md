# Quiz: Module 04 - JavaScript DOM Manipulation
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which DOM query method retrieves all page elements matching a CSS class selector?
*   A) `document.getElementById()`
*   B) `document.querySelector()`
*   C) `document.querySelectorAll()`
*   D) `document.classList()`
*   **Correct Answer:** C) `document.querySelectorAll()` returns a static `NodeList` containing every element in the document that matches the provided CSS selector string.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `getElementById()` returns a single element by its unique `id` attribute value — it cannot match by class name.
    *   *Why B is incorrect:* `querySelector()` returns only the *first* element matching the selector — not all matches.
    *   *Why C is correct:* `querySelectorAll('.classname')` returns all matching elements as a `NodeList` that can be iterated with `forEach()`.
    *   *Why D is incorrect:* `classList` is a property on an element object that provides methods to add, remove, and toggle CSS classes — it is not a document-level query method.

---

**Question 2**
Which of the following is the most accurate definition of the **Document Object Model (DOM)**?
*   A) A browser security policy that prevents JavaScript loaded from one origin from reading DOM content rendered by a different origin's HTML.
*   B) A JavaScript module system that allows one script file to import functions and variables exported by another file using `import` / `export` syntax.
*   C) A programming interface that represents an HTML document as a hierarchical tree of node objects, allowing JavaScript to read and modify page content, structure, and style at runtime.
*   D) A CSS rendering engine feature that pre-computes layout geometry for all page elements before the first paint, reducing cumulative layout shift.
*   **Correct Answer:** C) A programming interface that represents an HTML document as a hierarchical tree of node objects, allowing JavaScript to read and modify page content, structure, and style at runtime.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes the Same-Origin Policy, a browser security model — not the DOM.
    *   *Why B is incorrect:* This describes the ES Module system (`import`/`export`) — not the DOM.
    *   *Why C is correct:* The DOM is the in-memory tree representation of an HTML document that JavaScript interacts with via browser APIs.
    *   *Why D is incorrect:* This describes the browser's layout engine behavior related to Cumulative Layout Shift (CLS) — not the DOM.

---

**Question 3**
A developer wants to prevent a form from submitting to the server and instead handle the data with JavaScript. Which code correctly intercepts the form submission?
*   A) `form.addEventListener('submit', function(event) { event.preventDefault(); });`
*   B) `form.addEventListener('submit', function() { return false; });`
*   C) `form.setAttribute('action', 'javascript:void(0)');`
*   D) `form.removeEventListener('click', submitHandler);`
*   **Correct Answer:** A) `form.addEventListener('submit', function(event) { event.preventDefault(); });` — calling `event.preventDefault()` inside the submit handler stops the browser's default form submission behavior.
*   **Distractor Analysis:**
    *   *Why A is correct:* `event.preventDefault()` is the standard method to cancel the default action of any DOM event, including form submission.
    *   *Why B is incorrect:* `return false` only cancels default behavior when used in an inline HTML `onsubmit` attribute handler — it has no effect inside `addEventListener` callbacks.
    *   *Why C is incorrect:* Setting `action="javascript:void(0)"` is an outdated, non-semantic approach that does not reliably prevent submission in all browsers.
    *   *Why D is incorrect:* `removeEventListener` removes a previously registered listener but does nothing to intercept the submit event itself.

---

**Question 4**
During DOM event propagation, a click on a child `<button>` inside a `<div>` triggers handlers on both elements. What is the correct description of the default event propagation behavior?
*   A) The event fires simultaneously on all elements that contain the target, with no defined order.
*   B) The event fires on the `<button>` first (target phase) and then propagates upward through the `<div>` and subsequent ancestors (bubbling phase).
*   C) The event fires on the outermost ancestor first and travels downward to the `<button>` — this is called the bubbling phase.
*   D) Events only fire on the exact element clicked and never propagate to parent elements unless `addEventListener` is called with `{ capture: false }`.
*   **Correct Answer:** B) The event fires on the `<button>` first (target phase) and then propagates upward through the `<div>` and subsequent ancestors (bubbling phase).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Event propagation has a defined order — it is not simultaneous.
    *   *Why B is correct:* By default, DOM events bubble upward from the target element through its ancestor chain — this is why a click on a child triggers listeners attached to parent elements.
    *   *Why C is incorrect:* The downward phase is called the *capturing* phase — bubbling is the upward phase.
    *   *Why D is incorrect:* Events do bubble by default even without any explicit `addEventListener` options — propagation must be explicitly stopped with `event.stopPropagation()`.

---

**Question 5**
A developer needs to add 200 click event listeners to a dynamically generated table with 200 rows. Which approach is most performant?
*   A) Attach a separate `addEventListener('click', handler)` to each of the 200 `<tr>` elements after they are appended to the DOM.
*   B) Use event delegation: attach a single `addEventListener('click', handler)` to the parent `<tbody>` and use `event.target` inside the handler to identify which row was clicked.
*   C) Use `setInterval()` to poll `document.querySelectorAll('tr')` every 100ms and check which row has focus.
*   D) Add an inline `onclick` attribute to each `<tr>` tag in the HTML string passed to `innerHTML`.
*   **Correct Answer:** B) Use event delegation: attach a single `addEventListener('click', handler)` to the parent `<tbody>` and use `event.target` inside the handler to identify which row was clicked.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Attaching 200 individual listeners consumes more memory and requires re-registration every time rows are added or removed dynamically.
    *   *Why B is correct:* Event delegation leverages event bubbling — one listener on the parent handles all child clicks, and `event.target` identifies the exact clicked row. This is the industry-standard pattern for dynamic lists.
    *   *Why C is incorrect:* Polling with `setInterval` is an anti-pattern — it wastes CPU cycles and does not accurately detect click events.
    *   *Why D is incorrect:* Inline `onclick` attributes mix behavior with structure, are harder to maintain, and do not benefit from event delegation.
