# Quiz: Module 04 - JavaScript DOM Manipulation

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which DOM query method retrieves all page elements matching a CSS class selector?

- A) `document.getElementById()`
- B) `document.querySelector()`
- C) `document.querySelectorAll()`
- D) `document.classList()`

**Correct Answer:** C

**Explanation:** `document.querySelectorAll()` returns a static `NodeList` containing every element in the document that matches the provided CSS selector string, including class selectors like `.card`.

**Distractor Analysis:**

- Why A is incorrect: `getElementById()` returns a single element by its unique `id` attribute value — it cannot match by class name.
- Why B is incorrect: `querySelector()` returns only the first element matching the selector — not all matches.
- Why C is correct: `querySelectorAll('.classname')` returns all matching elements as a `NodeList` that can be iterated with `forEach()`.
- Why D is incorrect: `classList` is a property on an individual element object that provides methods to add, remove, and toggle CSS classes — it is not a document-level query method.

---

## Question 2

Which of the following is the most accurate definition of the Document Object Model?

- A) A browser security policy that prevents JavaScript loaded from one origin from reading DOM content rendered by a different origin's HTML.
- B) A JavaScript module system that allows one script file to import functions and variables exported by another file.
- C) A programming interface that represents an HTML document as a hierarchical tree of node objects, allowing JavaScript to read and modify page content, structure, and style at runtime.
- D) A CSS rendering engine feature that pre-computes layout geometry for all page elements before the first paint.

**Correct Answer:** C

**Explanation:** The DOM is the in-memory tree representation of an HTML document. JavaScript interacts with this tree through browser APIs on the `document` and individual element objects.

**Distractor Analysis:**

- Why A is incorrect: This describes the Same-Origin Policy — a browser security model unrelated to the DOM.
- Why B is incorrect: This describes the ES Module system (`import`/`export`) — not the DOM.
- Why C is correct: The DOM is the in-memory tree representation of an HTML document that JavaScript interacts with via browser APIs.
- Why D is incorrect: This describes the browser's layout engine behavior — not the DOM.

---

## Question 3

A developer wants to prevent a form from submitting to the server and instead handle the data with JavaScript. Which code correctly intercepts the form submission?

- A) `form.addEventListener('submit', function(event) { event.preventDefault(); });`
- B) `form.addEventListener('submit', function() { return false; });`
- C) `form.setAttribute('action', 'javascript:void(0)');`
- D) `form.removeEventListener('click', submitHandler);`

**Correct Answer:** A

**Explanation:** `event.preventDefault()` cancels the default behavior of any DOM event, including the default form submission behavior that sends a POST request to the server.

**Distractor Analysis:**

- Why A is correct: `event.preventDefault()` is the standard method to cancel the default action of any DOM event.
- Why B is incorrect: `return false` only cancels default behavior when used in an inline HTML `onsubmit` attribute handler — it has no effect inside `addEventListener` callbacks.
- Why C is incorrect: Setting `action="javascript:void(0)"` is an outdated, non-semantic approach that does not reliably prevent submission in all browsers.
- Why D is incorrect: `removeEventListener` removes a previously registered listener but does nothing to intercept the submit event itself.

---

## Question 4

During DOM event propagation, a click on a child `<button>` inside a `<div>` triggers handlers on both elements. What is the correct description of the default event propagation behavior?

- A) The event fires simultaneously on all elements that contain the target, with no defined order.
- B) The event fires on the `<button>` first (target phase) and then propagates upward through the `<div>` and subsequent ancestors (bubbling phase).
- C) The event fires on the outermost ancestor first and travels downward to the `<button>` — this is called the bubbling phase.
- D) Events only fire on the exact element clicked and never propagate to parent elements unless `addEventListener` is called with `{ capture: false }`.

**Correct Answer:** B

**Explanation:** By default, DOM events bubble upward from the target element through its ancestor chain. A click on the `<button>` fires on the button first, then bubbles to the `<div>`, then to `<body>`, then to the `<html>` element, then to `document`.

**Distractor Analysis:**

- Why A is incorrect: Event propagation has a defined order — it is not simultaneous.
- Why B is correct: Events bubble upward from the target element through its ancestor chain by default.
- Why C is incorrect: The downward phase is called the capturing phase — bubbling is the upward phase.
- Why D is incorrect: Events do bubble by default — propagation must be explicitly stopped with `event.stopPropagation()`.

---

## Question 5

A developer needs to add 200 click event listeners to a dynamically generated table with 200 rows. Which approach is most performant?

- A) Attach a separate `addEventListener('click', handler)` to each of the 200 `<tr>` elements after they are appended to the DOM.
- B) Use event delegation: attach a single `addEventListener('click', handler)` to the parent `<tbody>` and use `event.target` inside the handler to identify which row was clicked.
- C) Use `setInterval()` to poll `document.querySelectorAll('tr')` every 100ms and check which row has focus.
- D) Add an inline `onclick` attribute to each `<tr>` tag in the HTML string passed to `innerHTML`.

**Correct Answer:** B

**Explanation:** Event delegation leverages event bubbling. One listener on the parent handles all child clicks, and `event.target` identifies the exact clicked row. This is the industry-standard pattern for dynamic lists and uses significantly less memory than individual per-element listeners.

**Distractor Analysis:**

- Why A is incorrect: Attaching 200 individual listeners consumes more memory and requires re-registration every time rows are added or removed dynamically.
- Why B is correct: One listener on the parent handles all child clicks via bubbling and works correctly for dynamically added rows without any re-registration.
- Why C is incorrect: Polling with `setInterval` is an anti-pattern that wastes CPU cycles and does not accurately detect click events.
- Why D is incorrect: Inline `onclick` attributes mix behavior with structure, are harder to maintain, and do not benefit from event delegation.

---

## Question 6

A developer writes this code to update a card when a user clicks it:

```javascript
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('selected');
  });
});
```

Later, a new card is added to the DOM dynamically. The new card does not respond to clicks. What is the root cause and the correct fix?

- A) `querySelectorAll` returns a live NodeList — new elements added after the initial query are never included. Fix: use `getElementsByClassName` instead, which returns a live HTMLCollection.
- B) The event listeners were attached to the specific card elements that existed at query time. New cards added after the query have no listeners. Fix: use event delegation by attaching a single listener to the parent container.
- C) The `toggle` method only works once per element — after the first click it stops working. Fix: use `add` and `remove` with a boolean flag instead.
- D) Arrow functions inside `forEach` create a new scope that loses the `card` reference. Fix: use a regular `function` instead of an arrow function.

**Correct Answer:** B

**Explanation:** `querySelectorAll` returns a static snapshot of the DOM at query time. Event listeners attached to those elements do not apply to elements added to the DOM later. Event delegation (one listener on the parent) is the correct pattern because it handles existing and future child elements.

**Distractor Analysis:**

- Why A is incorrect: `querySelectorAll` does return a static NodeList (not live), but switching to `getElementsByClassName` would give a live HTMLCollection of current elements — it still would not add listeners to new elements automatically.
- Why B is correct: Listeners are attached to specific elements at a point in time. New elements have no listeners. Event delegation on the parent solves this.
- Why C is incorrect: `classList.toggle` works correctly on repeated calls — it adds the class if absent and removes it if present.
- Why D is incorrect: Arrow functions and regular functions in `forEach` both correctly capture the `card` variable in their closure — this is not the issue.

---

## Question 7

A developer uses `event.target.closest('.card')` inside a delegated event handler on a `.card-grid` element. When the user clicks on the `<h4>` text inside a card, what does `closest('.card')` return?

- A) It returns the `<h4>` element because that is the element the user directly clicked.
- B) It traverses up the DOM from the `<h4>` and returns the nearest ancestor element that matches `.card`.
- C) It returns `null` because the `<h4>` is inside `.card`, not `.card` itself.
- D) It returns the `.card-grid` container because that is the element the listener is attached to.

**Correct Answer:** B

**Explanation:** `element.closest(selector)` starts at the element itself and walks up the ancestor chain, returning the first element that matches the selector. Starting from `<h4>`, it traverses to the parent `.card` div and returns it. This is exactly why `closest()` is used in event delegation — it finds the intended target regardless of which child element triggered the event.

**Distractor Analysis:**

- Why A is incorrect: `event.target` is the `<h4>` element, but `closest()` walks up from there — it does not return the target itself unless the target matches the selector.
- Why B is correct: `closest()` walks up the ancestor chain from the current element and returns the first ancestor matching `.card`.
- Why C is incorrect: `closest()` returns the ancestor, not null — it successfully finds `.card` as a parent of `<h4>`.
- Why D is incorrect: `closest()` stops at the first matching ancestor — it does not continue up to `.card-grid`.

---

## Question 8

What is the difference between `element.textContent = userInput` and `element.innerHTML = userInput` when `userInput` is a string submitted by a website visitor?

- A) There is no practical difference — both insert the string into the element identically.
- B) `textContent` treats the string as literal text, escaping any HTML characters. `innerHTML` parses the string as HTML — if `userInput` contains `<script>` tags or event handler attributes, they will execute in the browser, creating a Cross-Site Scripting (XSS) vulnerability.
- C) `innerHTML` is safer than `textContent` because it validates the HTML before inserting it.
- D) `textContent` can only set text on leaf nodes; `innerHTML` must be used on container elements like `<div>` and `<section>`.

**Correct Answer:** B

**Explanation:** `textContent` always inserts literal characters — angle brackets are treated as plain text, not markup. `innerHTML` parses the string as HTML and executes any embedded JavaScript. Setting `innerHTML` with unsanitized user input is the classic stored XSS attack vector.

**Distractor Analysis:**

- Why A is incorrect: The difference is significant and security-critical — `innerHTML` parses HTML, `textContent` does not.
- Why B is correct: This accurately describes the security implication. In AWS applications, stored XSS via `innerHTML` is a OWASP Top 10 vulnerability.
- Why C is incorrect: `innerHTML` does not validate or sanitize HTML — it executes it.
- Why D is incorrect: Both `textContent` and `innerHTML` can be used on any element type, including containers.

---

## Question 9

A developer registers two event listeners on the same button:

```javascript
btn.addEventListener('click', listenerA);
btn.addEventListener('click', listenerB);
```

In what order do the listeners execute when the button is clicked?

- A) `listenerB` always executes first because later registrations have higher priority.
- B) The execution order is undefined — the browser decides at runtime which listener fires first.
- C) `listenerA` executes first because event listeners registered on the same element and event type fire in registration order.
- D) Both listeners execute simultaneously on separate threads.

**Correct Answer:** C

**Explanation:** The DOM specification guarantees that multiple event listeners registered on the same element and event type fire in the order they were registered. `listenerA` was registered first and therefore fires first.

**Distractor Analysis:**

- Why A is incorrect: Later registrations do not have higher priority — registration order is the deterministic rule.
- Why B is incorrect: The execution order is not undefined — the specification defines registration order as the execution order.
- Why C is correct: The Event specification requires listeners to be dispatched in registration order.
- Why D is incorrect: JavaScript is single-threaded — event listeners cannot execute simultaneously.

---

## Question 10

A developer uses `localStorage` to persist a user's dark mode preference. After deploying the React application to AWS S3 and CloudFront, users report that their dark mode preference resets after navigating to a different page in the app. What is the most likely cause?

- A) CloudFront does not forward `localStorage` values between edge locations — the preference is lost at each CDN node.
- B) S3 static hosting resets `localStorage` on every file request because static servers do not maintain client state.
- C) The developer is reading `localStorage.getItem('theme')` inside a `useEffect` with a dependency that re-runs on every navigation, which clears the stored value.
- D) `localStorage` is scoped to the origin (protocol + domain + port) and persists across page navigations within the same origin. If preferences reset on navigation, the code that reads or applies the preference is likely not running on the new page, or a `localStorage.clear()` call is being made somewhere.

**Correct Answer:** D

**Explanation:** `localStorage` persists data per origin across all pages, tabs, and sessions. If preferences reset on navigation within a React SPA, the cause is a code-level issue: the initialization code that reads and applies the preference is not running on the new rendered page, or something in the app is calling `localStorage.clear()` or `localStorage.removeItem('theme')`.

**Distractor Analysis:**

- Why A is incorrect: CloudFront is a CDN that delivers static files — it has no knowledge of or access to browser `localStorage`. `localStorage` is entirely client-side.
- Why B is incorrect: S3 is a static file server — it delivers files to the browser. Client-side `localStorage` is managed entirely by the browser and is unaffected by S3.
- Why C is incorrect: A `useEffect` dependency issue could cause incorrect behavior, but it would not "clear" the stored value — it would fail to apply it on certain renders.
- Why D is correct: `localStorage` is an origin-scoped persistent browser storage. Navigation within the same origin does not reset it. The bug is in the application code.
