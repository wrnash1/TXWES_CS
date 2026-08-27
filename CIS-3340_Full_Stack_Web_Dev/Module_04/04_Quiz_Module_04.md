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

---

### Question 11 (5 points)

What does `element.closest('.card')` return when called on an element that has no ancestor matching `.card`?

- A) It returns the `document` object as the root fallback.
- B) It returns `undefined`.
- C) It returns `null`.
- D) It throws a `TypeError` because no match was found.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `closest()` does not fall back to `document` — it returns `null` when no matching ancestor is found.
  - Why B is incorrect: `closest()` returns `null`, not `undefined`, when no match is found. This distinction matters when writing guard clauses.
  - Why C is correct: `Element.closest()` returns `null` when no ancestor (including the element itself) matches the selector. Guard clauses should check `if (!result) return;`.
  - Why D is incorrect: `closest()` does not throw — it returns `null` gracefully.

---

### Question 12 (5 points)

A developer writes `element.style.display = ''` (empty string). What is the effect?

- A) It hides the element by removing it from the layout, equivalent to `display: none`.
- B) It removes the inline `display` style from the element, restoring the value defined in the stylesheet or the browser's default.
- C) It throws a syntax error because `style.display` cannot be set to an empty string.
- D) It sets the element to `display: inline`, overriding any stylesheet rule.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: An empty string does not mean "none" — it means "remove the inline style entirely."
  - Why B is correct: Setting a style property to an empty string removes that inline style declaration, allowing the cascade to fall through to the stylesheet or browser default value.
  - Why C is incorrect: This is valid JavaScript that executes without error.
  - Why D is incorrect: An empty string does not impose any specific value — it defers the value to the CSS cascade.

---

### Question 13 (5 points)

Which event fires when the user types into a text `<input>` field, providing real-time updates on every keystroke?

- A) `change`
- B) `keypress`
- C) `input`
- D) `blur`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The `change` event fires when the input loses focus after the value has been modified — it does not fire on every keystroke.
  - Why B is incorrect: `keypress` is deprecated and fires on some keystrokes but not all (it does not fire for non-printable keys like Backspace).
  - Why C is correct: The `input` event fires synchronously on every change to the element's value, including typing, pasting, cutting, and autofill — making it the correct choice for real-time filtering.
  - Why D is incorrect: `blur` fires when the element loses focus — it fires once when the user tabs away, not on each keystroke.

---

### Question 14 (5 points)

What is the security risk of writing `element.innerHTML = userInput` where `userInput` is data entered by a website visitor?

- A) It may cause layout reflow because innerHTML triggers a full DOM repaint.
- B) If the user input contains HTML with `<script>` tags or event handler attributes like `onerror`, the browser may execute that code, resulting in a Cross-Site Scripting (XSS) attack.
- C) innerHTML cannot accept strings with angle brackets and will silently strip them.
- D) innerHTML synchronously blocks the JavaScript event loop, causing the page to freeze.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Layout reflow is a performance consideration, not a security risk.
  - Why B is correct: `innerHTML` parses its string argument as HTML markup. Unsanitized user input containing script tags or inline event handlers creates an XSS vulnerability — one of the OWASP Top 10 web application security risks.
  - Why C is incorrect: `innerHTML` does not strip angle brackets — it parses them as HTML, which is the source of the risk.
  - Why D is incorrect: DOM manipulation is synchronous but does not block the event loop in a harmful way under normal use.

---

### Question 15 (5 points)

A developer calls `element.removeEventListener('click', handler)` but the listener is still firing. What is the most likely cause?

- A) `removeEventListener` is not supported for click events — only for custom events.
- B) The handler passed to `removeEventListener` is a different function reference than the one passed to `addEventListener` — anonymous functions or re-declared functions cannot be removed this way.
- C) The listener is attached in the capture phase, so removing it from the bubble phase has no effect.
- D) `removeEventListener` only works if called within the event handler itself.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `removeEventListener` works for all event types including `click`.
  - Why B is correct: `removeEventListener` requires the exact same function reference that was passed to `addEventListener`. If the handler was defined as an anonymous function inline or re-declared, the references do not match and the listener is not removed.
  - Why C is incorrect: If the listener was registered with `{ capture: true }`, then yes, the capture phase must match — but the question implies the default (bubble) phase was used for both calls.
  - Why D is incorrect: `removeEventListener` can be called from anywhere — it is not restricted to use inside the handler.

---

### Question 16 (5 points)

What is the difference between `window.load` and `DOMContentLoaded`?

- A) `DOMContentLoaded` fires after all CSS and images load; `window.load` fires after only the HTML is parsed.
- B) `DOMContentLoaded` fires when the HTML has been fully parsed and the DOM is ready; `window.load` fires after all dependent resources (images, stylesheets, iframes) have finished loading.
- C) Both events fire at the same time — they are aliases for the same browser event.
- D) `DOMContentLoaded` is only available in Chrome; `window.load` is the cross-browser standard.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This reverses the two events' descriptions.
  - Why B is correct: `DOMContentLoaded` fires as soon as the HTML document is fully parsed and the DOM tree is built — before images and stylesheets have loaded. `window.load` fires after every resource the page depends on has finished loading.
  - Why C is incorrect: They fire at different times and serve different purposes.
  - Why D is incorrect: Both events are cross-browser standards supported by all modern browsers.

---

### Question 17 (5 points)

A developer needs to create 50 `<li>` elements from an array and add them to a `<ul>`. Which approach is most performant?

- A) Append each `<li>` to the `<ul>` individually inside a loop using `appendChild`.
- B) Build all 50 elements inside a `DocumentFragment`, then append the fragment to the `<ul>` in a single operation.
- C) Use `innerHTML` to set the full HTML string at once.
- D) Use `setTimeout` with 0ms delay to defer each `appendChild` call off the main thread.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Each `appendChild` call in a loop triggers a reflow/repaint cycle — 50 individual appends cause 50 layout recalculations.
  - Why B is correct: A `DocumentFragment` is a lightweight in-memory container. Appending elements to a fragment does not trigger layout. A single `appendChild(fragment)` inserts all 50 elements in one DOM operation, causing one reflow.
  - Why C is incorrect: Setting `innerHTML` is also a single DOM operation and is acceptable, but it destroys existing child nodes, re-parses the string as HTML, and has security implications with user data.
  - Why D is incorrect: `setTimeout` with 0ms does not move execution off the main thread — JavaScript is single-threaded. This creates 50 queued callbacks with no performance benefit.

---

### Question 18 (5 points)

Which method is used to read a `data-user-id` attribute from a DOM element using the dataset API?

- A) `element.getAttribute('data-user-id')`
- B) `element.dataset['data-user-id']`
- C) `element.dataset.userId`
- D) `element.data.userId`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `getAttribute` works but does not use the dataset API — the question specifically asks about the dataset API.
  - Why B is incorrect: The dataset API converts hyphenated attribute names to camelCase property names — `data-user-id` becomes `dataset.userId`, not `dataset['data-user-id']`.
  - Why C is correct: The dataset API converts `data-user-id` to the camelCase property `userId`. Hyphens indicate the start of each new word in the camelCase conversion.
  - Why D is incorrect: `element.data` is not a valid DOM property — the correct API property is `element.dataset`.

---

### Question 19 (5 points)

A developer uses `sessionStorage` instead of `localStorage` to store a user's current filter selections. What is the key behavioral difference?

- A) `sessionStorage` can store larger amounts of data than `localStorage`.
- B) `sessionStorage` data is cleared when the browser tab or window is closed; `localStorage` data persists until explicitly deleted by code or the user clearing browser data.
- C) `sessionStorage` is shared across all tabs on the same origin; `localStorage` is scoped to a single tab.
- D) `sessionStorage` stores data server-side in a session cookie; `localStorage` stores data in the browser.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Both storage APIs have similar per-origin capacity limits (typically 5–10MB). `sessionStorage` does not have a larger quota.
  - Why B is correct: `sessionStorage` is scoped to the page session — data is cleared when the tab is closed. `localStorage` persists across sessions until programmatically cleared.
  - Why C is incorrect: This is the opposite — `localStorage` is shared across all tabs on the same origin; `sessionStorage` is isolated to its specific tab.
  - Why D is incorrect: Both `localStorage` and `sessionStorage` are entirely client-side browser storage APIs. Neither communicates with the server or uses cookies.

---

### Question 20 (5 points)

What does the `defer` attribute on a `<script>` tag in the `<head>` do?

- A) It prevents the script from executing until the user scrolls the script's parent element into view.
- B) It downloads the script file in parallel with HTML parsing and executes it after the HTML document has been fully parsed, in the order the scripts appear.
- C) It delays script execution by exactly 100ms to give the CSS paint a head start.
- D) It marks the script as optional — the browser will skip it if the network is slow.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `defer` is not related to scroll position or Intersection Observer behavior.
  - Why B is correct: `defer` instructs the browser to download the script in parallel without blocking HTML parsing, then execute it after parsing is complete and in document order — making it safe to query DOM elements without `DOMContentLoaded`.
  - Why C is incorrect: `defer` does not introduce a fixed millisecond delay — execution happens as soon as parsing completes.
  - Why D is incorrect: `defer` does not make a script optional or skippable — the browser always downloads and executes deferred scripts.
