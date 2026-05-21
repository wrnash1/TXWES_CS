# Quiz: Module 12 - Event Handling & Listeners
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which method on the event object is used to stop the default browser action, such as navigating a link or submitting a form?
*   A) stopPropagation()
*   B) preventDefault()
*   C) stopImmediatePropagation()
*   D) cancelEvent()
*   **Correct Answer:** B) The `preventDefault()` method tells the user agent that if the event goes unhandled, its default action should not be taken.
*   **Distractor Analysis:**
    *   *Why correct:* The `preventDefault()` method tells the user agent that if the event goes unhandled, its default action should not be taken.
    *   stopPropagation prevents event bubbling. cancelEvent is not a valid method name.

---

**Question 2**
Which of the following most accurately describes **`addEventListener`** in JavaScript?
*   A) A method that replaces all existing event handlers on an element with the new handler function provided
*   B) A DOM method called on an element to register a callback that fires whenever a specified event type occurs, supporting multiple handlers per event
*   C) A global function that listens for events anywhere on the page without needing a specific target element
*   D) An event property that stores the name of the most recently fired event on any element in the document
*   **Correct Answer:** B) A DOM method called on an element to register a callback that fires whenever a specified event type occurs, supporting multiple handlers per event.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Unlike setting `element.onclick = fn` (which replaces), `addEventListener` stacks multiple handlers on the same element and event without overwriting.
    *   *Why B is correct:* `addEventListener(type, callback, options)` attaches a listener to a specific element; multiple calls for the same event type accumulate rather than replace.
    *   *Why C is incorrect:* `addEventListener` must be called on a specific target (element, `document`, or `window`); there is no parameter-less global version.
    *   *Why D is incorrect:* That describes a property like `event.type`, which identifies the current event's name; it is a property of the event object, not a method.

---

**Question 3**
A developer has a `<ul>` list with many `<li>` items added dynamically. They want a single click handler that works for all current and future `<li>` items. Which approach correctly uses event delegation?
*   A) Add a separate `addEventListener("click", ...)` to every `<li>` element as it is created.
*   B) Add one `addEventListener("click", ...)` to the parent `<ul>` and use `event.target` inside the handler to detect which `<li>` was clicked.
*   C) Add `addEventListener("click", ...)` to `document.body` and check `event.currentTarget` to find the clicked `<li>`.
*   D) Use `addEventListener("bubble", ...)` on the `<ul>` to catch bubbled events from its children.
*   **Correct Answer:** B) Add one `addEventListener("click", ...)` to the parent `<ul>` and use `event.target` inside the handler to detect which `<li>` was clicked.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Adding individual handlers to every item is inefficient and fails for dynamically added elements unless the handler is reattached each time.
    *   *Why B is correct:* Event delegation exploits bubbling — clicks on `<li>` items bubble up to the `<ul>`, where a single handler checks `event.target` to identify the originating item.
    *   *Why C is incorrect:* `event.currentTarget` always refers to the element the listener is attached to (the `<body>` in this case), not the clicked `<li>`.
    *   *Why D is incorrect:* `"bubble"` is not a valid event type; the correct approach is to listen for the event name (e.g., `"click"`) on the ancestor, taking advantage of bubbling automatically.

---

**Question 4**
While working on **Event Handling**, a developer attaches a submit listener to a form but reports that the page reloads before their code runs. What is missing?
*   A) A `return true;` statement at the end of the handler function
*   B) A call to `event.preventDefault()` at the beginning of the handler to cancel the default form submission
*   C) The `async` keyword on the handler function to prevent synchronous page reload
*   D) A call to `event.stopPropagation()` to prevent the form event from reaching the server
*   **Correct Answer:** B) A call to `event.preventDefault()` at the beginning of the handler to cancel the default form submission.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `return true` does not prevent the default action; only `preventDefault()` does.
    *   *Why B is correct:* The browser's default behavior for a form `submit` event is to serialize the form and navigate to a new URL; `preventDefault()` suppresses this, keeping the page in place.
    *   *Why C is incorrect:* Making the handler `async` allows it to use `await`, but does not prevent the synchronous default submission behavior.
    *   *Why D is incorrect:* `stopPropagation()` stops the event from bubbling to ancestor elements; it has no effect on the browser's default submit action.

---

**Question 5**
What is the difference between `event.target` and `event.currentTarget`?
*   A) They always refer to the same element; the two properties are aliases.
*   B) `event.target` is the element that originally triggered the event; `event.currentTarget` is the element on which the currently-executing listener is registered.
*   C) `event.target` refers to the element the listener is attached to; `event.currentTarget` refers to the element that was actually clicked.
*   D) `event.target` is only available for mouse events; `event.currentTarget` is available for all event types.
*   **Correct Answer:** B) `event.target` is the element that originally triggered the event; `event.currentTarget` is the element on which the currently-executing listener is registered.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* They are the same only when the listener is on the element that was directly interacted with; when events bubble, they differ.
    *   *Why B is correct:* During bubbling, `target` stays fixed as the originating element while `currentTarget` changes to each ancestor that has a listener as the event travels up.
    *   *Why C is incorrect:* The descriptions are reversed.
    *   *Why D is incorrect:* Both properties are available on all event types in all phases, not restricted to mouse events.
