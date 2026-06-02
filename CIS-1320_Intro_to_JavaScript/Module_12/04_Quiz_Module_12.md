# Quiz: Module 12 — Event Handling and Listeners

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

A developer writes the following code. How many times does `'clicked'` appear in the console when the button is clicked once?

```javascript
const btn = document.getElementById('btn');
btn.addEventListener('click', () => console.log('clicked'));
btn.addEventListener('click', () => console.log('clicked'));
btn.onclick = () => console.log('clicked');
```

- A) 1
- B) 2
- C) 3
- D) 0

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `addEventListener` does not overwrite previous listeners. Each call registers a new independent listener. And `onclick` adds a third handler.
- *Why B is incorrect:* Both `addEventListener` calls register separate listeners that both fire. The `onclick` assignment adds a third.
- *Why C is correct:* The two `addEventListener` calls each register an independent listener — both fire. The `onclick` assignment registers a third listener. All three fire on a single click, printing `'clicked'` three times.
- *Why D is incorrect:* All three handlers are valid. The click event fires all of them.

---

### Question 2

A developer adds a click listener using an inline arrow function and later tries to remove it. What is the result?

```javascript
btn.addEventListener('click', () => console.log('hello'));
btn.removeEventListener('click', () => console.log('hello'));
```

- A) The listener is successfully removed — both lines use the same arrow syntax
- B) The listener is not removed — each arrow expression creates a new function object
- C) A `TypeError` is thrown because arrow functions cannot be used with `removeEventListener`
- D) The listener fires once after the `removeEventListener` call, then stops

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Even though both arrows look identical, they are separate function objects created at different points in code execution. They do not share the same reference.
- *Why B is correct:* `removeEventListener` matches by function reference, not by source code text. Each arrow function expression `() => ...` creates a new, unique function object. The two arrows in this code are different objects — `removeEventListener` finds no match and the listener remains active.
- *Why C is incorrect:* Arrow functions work fine with `removeEventListener`. The problem is the missing reference, not the function type.
- *Why D is incorrect:* The listener is never removed — it fires on every click indefinitely.

---

### Question 3

What does `event.target` refer to inside an event listener?

- A) The element the listener was attached to
- B) The element where the event originated
- C) The parent element of the clicked element
- D) The `document` object

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That is `event.currentTarget`. During bubbling, `currentTarget` is the element the listener is attached to. `target` is different — it is the element where the event actually started.
- *Why B is correct:* `event.target` always refers to the element where the event originally fired — the innermost element the user interacted with. It stays the same as the event bubbles up through ancestors.
- *Why C is incorrect:* `event.target` is not the parent. The parent would be `event.target.parentElement`.
- *Why D is incorrect:* `event.target` is a specific DOM element, not the document root. `document` would only be the target if the event was dispatched directly on `document`.

---

### Question 4

The following HTML has nested elements with click listeners:

```html
<div id="outer">
  <div id="inner">
    <button id="btn">Click</button>
  </div>
</div>
```

```javascript
document.getElementById('btn').addEventListener('click', () => console.log('btn'));
document.getElementById('inner').addEventListener('click', () => console.log('inner'));
document.getElementById('outer').addEventListener('click', () => console.log('outer'));
```

When the button is clicked, what appears in the console and in what order?

- A) `outer`, `inner`, `btn`
- B) `btn`, `inner`, `outer`
- C) `btn` only
- D) `outer` only

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That would be the capture phase order. The default phase for `addEventListener` (without a third argument of `true`) is the bubble phase — events travel from the innermost element outward.
- *Why B is correct:* Events bubble from the origin outward. The click originates on `btn`, so `btn` fires first. The event then bubbles to `inner` (fires second) and then to `outer` (fires third). All three listeners execute in this order.
- *Why C is incorrect:* `stopPropagation` was not called, so the event bubbles normally through all ancestors that have listeners.
- *Why D is incorrect:* The outermost listener fires last, not first, in the default bubble phase.

---

### Question 5

What is the purpose of `event.preventDefault()` on a form's `submit` event?

- A) It stops the event from bubbling to ancestor elements
- B) It prevents other `submit` listeners from firing
- C) It cancels the browser's default behavior of reloading the page on submission
- D) It removes the form element from the DOM

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `preventDefault` does not affect event propagation. To stop bubbling, use `event.stopPropagation()`. These are independent operations.
- *Why B is incorrect:* `preventDefault` does not affect other listeners. `stopImmediatePropagation` would stop other listeners on the same element.
- *Why C is correct:* When a form is submitted, the browser's default behavior is to serialize the form data and reload the page (or navigate to the action URL). `event.preventDefault()` cancels this default, allowing JavaScript to process the form data without a page reload.
- *Why D is incorrect:* `preventDefault` has no effect on the DOM structure. The form element remains.

---

### Question 6

A developer wants to handle clicks on 50 list items efficiently. Which approach is best?

- A) Add a `click` listener to each `<li>` element individually in a loop
- B) Add a single `click` listener to the parent `<ul>` and use `event.target` to identify the clicked item
- C) Add a `click` listener to `document` and check `event.target.tagName`
- D) Use `onclick` attributes in the HTML for each `<li>`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Adding 50 separate listeners uses more memory and does not handle list items added dynamically after the listeners are registered.
- *Why B is correct:* Event delegation — one listener on the parent `<ul>` — is the efficient solution. Click events from any `<li>` bubble up to the `<ul>` listener. `event.target` identifies which item was clicked. This handles both current and future items with no additional code.
- *Why C is incorrect:* Listening on `document` works, but it is too broad — every click on the entire page reaches this listener, requiring more defensive checks. Listening on the nearest common ancestor (`<ul>`) is the correct scope.
- *Why D is incorrect:* `onclick` HTML attributes are the oldest, least maintainable approach. They mix HTML and JavaScript, support only one handler, and are not configurable from external scripts.

---

### Question 7

Inside a delegated click listener on a `<ul>`, a developer uses `event.target.closest('li')`. What does `closest('li')` do?

- A) Returns the parent `<ul>` of the clicked element
- B) Searches downward from `event.target` to find the nearest `<li>` descendant
- C) Starts at `event.target` and walks up the DOM to find the nearest ancestor matching `'li'`
- D) Returns all `<li>` elements in the document

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `closest` does not return the parent `<ul>`. It searches upward for a match to the given CSS selector — in this case, `'li'`.
- *Why B is incorrect:* `closest` searches **upward** (toward ancestors), not downward toward descendants. For downward searching, `querySelector` would be used.
- *Why C is correct:* `element.closest(selector)` starts at the element itself, checks if it matches the selector, then checks its parent, then its grandparent, and so on, until a match is found or the document root is reached. It returns the first match or `null`. This is useful in delegation when `event.target` may be a child element (like a `<span>` inside an `<li>`).
- *Why D is incorrect:* `closest` operates on a single element and returns at most one element. `document.querySelectorAll('li')` would return all `<li>` elements.

---

### Question 8

What is the difference between `event.stopPropagation()` and `event.preventDefault()`?

- A) They are identical — both stop the event completely
- B) `stopPropagation` stops bubbling through the DOM; `preventDefault` cancels the browser's default action
- C) `preventDefault` stops bubbling; `stopPropagation` cancels the browser's default action
- D) `stopPropagation` removes the event listener; `preventDefault` pauses the event

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* They do different things. Using one does not replace the other. You can call both on the same event.
- *Why B is correct:* `event.stopPropagation()` prevents the event from traveling to ancestor elements — it stays at the current element in the bubbling chain. `event.preventDefault()` cancels the browser's built-in response to the event (page reload for form submit, navigation for link click, etc.). They are completely independent.
- *Why C is incorrect:* This reverses the two behaviors. `stopPropagation` handles bubbling; `preventDefault` handles default browser actions.
- *Why D is incorrect:* Neither method removes listeners or pauses events. `removeEventListener` removes a listener; there is no way to "pause" an event.

---

### Question 9

Which event fires on a text input on **every keystroke**, as opposed to only when the field loses focus?

- A) `change`
- B) `blur`
- C) `input`
- D) `keyup`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `change` fires when the input's value has changed **and** the field loses focus (blur). It does not fire on every keystroke.
- *Why B is incorrect:* `blur` fires when the element loses focus — once, when the user clicks away or tabs out. It does not track what the user types.
- *Why C is correct:* The `input` event fires synchronously whenever the value of an `<input>`, `<textarea>`, or `<select>` element is changed — on every keystroke, paste, cut, and autocomplete. It is the right event for live search, character counters, and real-time validation.
- *Why D is incorrect:* `keyup` fires on every key release, but it misses value changes from mouse paste, drag-and-drop, and browser autocomplete. `input` is more reliable for tracking value changes.

---

### Question 10

A task list uses event delegation. The `<ul>` has a click listener. A new `<li>` is added dynamically after the listener was registered. When the new `<li>` is clicked, what happens?

- A) Nothing — the listener was registered before the `<li>` existed
- B) A `TypeError` is thrown because the element is not registered
- C) The delegated listener fires, because the click bubbles up to the `<ul>`
- D) The click is silently ignored

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Event delegation is specifically designed to handle this case. The listener is on the `<ul>`, not on any individual `<li>`. Since any `<li>` click bubbles up to the `<ul>`, it does not matter when the `<li>` was created.
- *Why B is incorrect:* No error is thrown. Events do not require registration on the specific target element. The `<ul>` listener receives all click events that bubble up to it, regardless of which child element they originate from.
- *Why C is correct:* When the user clicks the new `<li>`, the click event fires on it and bubbles upward through the DOM. It reaches the `<ul>`, where the delegated listener is registered, and the listener fires. `event.target` is the new `<li>`. This is the defining advantage of delegation over per-element listeners.
- *Why D is incorrect:* Events are never silently ignored due to listener registration timing. Bubbling is a fundamental behavior of the DOM event model.
