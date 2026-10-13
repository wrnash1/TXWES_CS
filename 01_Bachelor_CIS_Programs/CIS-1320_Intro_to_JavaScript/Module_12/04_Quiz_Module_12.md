# Quiz: Module 12 — Event Handling and Listeners

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

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

---

### Question 11

What is the value of `e.currentTarget.id` inside the `outer` listener when the button is clicked?

```html
<div id="outer"><button id="btn">Click</button></div>
```

```javascript
document.getElementById('outer').addEventListener('click', e => {
  console.log(e.currentTarget.id);
});
```

- A) `'btn'`
- B) `'outer'`
- C) `undefined`
- D) Changes depending on which element is clicked

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `e.target.id` would be `'btn'` — the element where the click originated. `currentTarget` refers to the element the listener is attached to, which is `outer`.
- *Why B is correct:* `event.currentTarget` is always the element whose listener is currently executing. The listener is attached to `#outer`, so `e.currentTarget.id` is `'outer'`, regardless of where in the subtree the click occurred.
- *Why C is incorrect:* `currentTarget` is a defined, non-null element reference while a listener is executing. It is only `null` outside of active event dispatch.
- *Why D is incorrect:* `currentTarget` does not change based on which child was clicked. It always refers to the element the listener is registered on — `#outer` in this case.

---

### Question 12

Which of the following correctly adds a one-time event listener that automatically removes itself after firing once?

- A) `btn.addEventListener('click', handler, { once: false })`
- B) `btn.addEventListener('click', handler, { once: true })`
- C) `btn.addEventListener('click', handler); btn.removeEventListener('click', handler);`
- D) `btn.addEventListener('click', () => { handler(); btn.removeEventListener('click', handler); })`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `{ once: false }` is the default behavior — the listener fires every time. `false` does not make it fire once.
- *Why B is correct:* The `addEventListener` options object accepts `{ once: true }`, which causes the listener to automatically remove itself after firing once. This is the cleanest built-in mechanism for one-time event handlers.
- *Why C is incorrect:* Calling `removeEventListener` immediately after `addEventListener` removes the listener before it ever fires. The handler would never execute.
- *Why D is incorrect:* This approach does work as a workaround, but it uses a different anonymous arrow function as the registered listener — meaning `handler` was never the registered function, so `removeEventListener('click', handler)` would not actually remove anything. The anonymous arrow would remain. The correct self-removal pattern inside a callback requires using the arrow's own reference or `arguments.callee` (deprecated).

---

### Question 13

What does `event.stopImmediatePropagation()` do that `event.stopPropagation()` does not?

- A) It also cancels the browser's default action
- B) It also prevents any remaining listeners on the same element from firing
- C) It stops the event before it reaches the target element
- D) It removes the event from the event queue permanently

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Neither `stopPropagation` nor `stopImmediatePropagation` cancels default browser behavior. That requires `preventDefault`. These are orthogonal operations.
- *Why B is correct:* `stopPropagation` prevents the event from bubbling to ancestor elements — but other listeners on the same element still fire. `stopImmediatePropagation` does both: it stops bubbling AND prevents any other listeners registered on the same element for the same event from executing.
- *Why C is incorrect:* Neither method prevents the event from reaching the target. Both are called from within a listener on the target (or an ancestor) — by definition, the event has already reached that element.
- *Why D is incorrect:* There is no mechanism to permanently remove events from the event queue. Both methods only affect the current event dispatch cycle.

---

### Question 14

A developer adds a click listener to a `<div>` that contains a `<span>`. The user clicks the `<span>`. Which statement is true?

```javascript
div.addEventListener('click', e => {
  console.log(e.target === div);
  console.log(e.currentTarget === div);
});
```

- A) Both log `true`
- B) Both log `false`
- C) First logs `false`, second logs `true`
- D) First logs `true`, second logs `false`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The user clicked the `<span>`, not the `<div>`. `e.target` is the `<span>` — `e.target === div` is `false`.
- *Why B is incorrect:* The listener is attached to `div`, so `e.currentTarget === div` is `true`. The second statement does not log `false`.
- *Why C is correct:* `e.target` is the `<span>` (the element clicked) — not the `div`, so `e.target === div` is `false`. `e.currentTarget` is the `<div>` (the element the listener is on) — so `e.currentTarget === div` is `true`.
- *Why D is incorrect:* This reverses the values. `target` is the origin element; `currentTarget` is the listener's element.

---

### Question 15

What event should be used to detect when the user presses the Escape key?

- A) `element.addEventListener('escape', e => { ... })`
- B) `document.addEventListener('keydown', e => { if (e.key === 'Escape') { ... } })`
- C) `document.addEventListener('keypress', e => { if (e.keyCode === 27) { ... } })`
- D) `document.addEventListener('keydown', e => { if (e.code === 'escape') { ... } })`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'escape'` is not a valid DOM event type. Keyboard events are `'keydown'`, `'keyup'`, and (deprecated) `'keypress'`.
- *Why B is correct:* `'keydown'` fires as soon as the key is pressed. `e.key === 'Escape'` checks for the Escape key using the modern `key` property. This is the recommended modern approach.
- *Why C is incorrect:* `keypress` is deprecated and does not fire for all keys (notably Escape in some browsers). `keyCode` is also deprecated — use `e.key` instead.
- *Why D is incorrect:* `e.code` values are case-sensitive and use title case for named keys: `'Escape'` not `'escape'`. However, this option uses lowercase `'escape'` which would not match. Additionally, `e.key` is preferred over `e.code` for semantic key detection.

---

### Question 16

A form has a required text input and a submit button. The developer writes:

```javascript
form.addEventListener('submit', e => {
  e.preventDefault();
  if (!inputField.value.trim()) {
    errorDiv.textContent = 'Name is required.';
    return;
  }
  submitData(inputField.value);
});
```

What does `e.preventDefault()` accomplish here?

- A) It prevents the form from being rendered in the browser
- B) It stops the `submit` event from bubbling to ancestor elements
- C) It prevents the browser from reloading the page and submitting the form data to the server
- D) It clears all form field values

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `preventDefault` has no effect on rendering. The form continues to display normally.
- *Why B is incorrect:* The `submit` event does bubble, but that is not what `preventDefault` controls. `stopPropagation` would stop bubbling.
- *Why C is correct:* A form's default submit behavior is to serialize the input values and send an HTTP request, causing the page to reload (or navigate). `preventDefault` cancels this, allowing the JavaScript handler to process the data entirely client-side without a page reload.
- *Why D is incorrect:* `preventDefault` does not modify form field values. The fields retain their current values — the handler can read `inputField.value` normally after calling it.

---

### Question 17

A developer builds a toolbar using event delegation. Each button has a `data-action` attribute. What is wrong with this code?

```javascript
document.getElementById('toolbar').addEventListener('click', e => {
  const action = e.target.dataset.action;
  if (action === 'save') save();
  if (action === 'delete') deleteItem();
});
```

- A) `dataset` is not accessible inside event listeners
- B) If the button contains a child element (like an icon `<span>`), clicking the icon makes `e.target` the `<span>`, which has no `data-action` attribute — `action` will be `undefined`
- C) `e.target` always refers to the toolbar, not the clicked button
- D) The code will throw a `SyntaxError` because `data-action` contains a hyphen

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `dataset` is fully accessible anywhere in JavaScript, including inside event listeners. It is a standard DOM property.
- *Why B is correct:* If a `<button data-action="save"><span class="icon"></span>Save</button>` is clicked on the `<span>` icon, `e.target` is the `<span>`, which has no `data-action` attribute. `action` is `undefined` and neither `save()` nor `deleteItem()` fires. The fix is to use `e.target.closest('[data-action]')` to walk up to the button.
- *Why C is incorrect:* `e.target` is the element the click originated on — the button or one of its descendants, not the toolbar itself.
- *Why D is incorrect:* `dataset.action` correctly accesses `data-action` by converting the hyphenated attribute name to camelCase. No `SyntaxError` occurs.

---

### Question 18

What is the difference between the `mouseenter` and `mouseover` events?

- A) `mouseenter` fires repeatedly as the mouse moves; `mouseover` fires once on entry
- B) `mouseenter` does not bubble and fires only when the mouse enters the element itself; `mouseover` bubbles and fires when entering the element or any descendant
- C) `mouseenter` fires on touch devices; `mouseover` fires on desktop only
- D) They are identical — use either one

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Neither fires repeatedly while the mouse moves — `mousemove` does that. Both fire on entry; the distinction is bubbling and descendant behavior.
- *Why B is correct:* `mouseenter` does not bubble and triggers only when the pointer moves into the element from outside (not when moving between child elements). `mouseover` bubbles and fires each time the pointer enters the element or any of its descendants. For simple hover effects on a single element, `mouseenter`/`mouseleave` are preferred because they do not fire repeatedly on child entry.
- *Why C is incorrect:* Touch device support is unrelated to the bubbling distinction. Neither event is device-specific in the standard specification.
- *Why D is incorrect:* They have meaningfully different behavior. Using `mouseover` with a delegate on a parent with many descendants can cause the listener to fire many more times than intended.

---

### Question 19

Which event fires when the HTML is fully parsed and the DOM is ready, but before images and stylesheets have finished loading?

- A) `window.load`
- B) `document.DOMContentLoaded`
- C) `document.ready`
- D) `window.DOMReady`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `window.addEventListener('load', ...)` fires when the entire page is fully loaded — HTML, images, stylesheets, scripts, and all subresources. It fires after `DOMContentLoaded`.
- *Why B is correct:* `document.addEventListener('DOMContentLoaded', ...)` fires when the HTML has been parsed and the DOM tree is complete — but before images, stylesheets, and other resources finish loading. This is the right moment to query elements and attach event listeners.
- *Why C is incorrect:* `document.ready` is a jQuery concept, not a native DOM event. In vanilla JavaScript, use `DOMContentLoaded`.
- *Why D is incorrect:* `window.DOMReady` does not exist as a native browser event. It is not part of the DOM specification.

---

### Question 20

A `<button>` inside a `<form>` is clicked. Both have click listeners. The button's listener calls `e.stopPropagation()`. What happens to the form's default submit behavior?

```javascript
btn.addEventListener('click', e => {
  e.stopPropagation();
  console.log('button clicked');
});

form.addEventListener('click', e => {
  console.log('form click received');
});
```

- A) The form's click listener fires but the form does not submit (stopPropagation prevents submit)
- B) The form's default submit behavior is unaffected; the form click listener does not fire
- C) Both the button and form listeners fire, and the form submits
- D) Neither listener fires because `stopPropagation` cancels all event processing

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `stopPropagation` does not affect the browser's default submit behavior. It only stops the event from bubbling to ancestor listeners. To prevent the default submit, you need `preventDefault`.
- *Why B is correct:* `stopPropagation` on the button's click listener prevents the click event from bubbling to the `form` click listener — so `'form click received'` is not logged. However, the button is of type `submit` by default, and the browser's form submission behavior is separate from the click listener chain. The default submit still fires unless `preventDefault` is also called. The form click listener specifically does not fire because bubbling was stopped.
- *Why C is incorrect:* Bubbling was stopped — the `form` click listener does not receive the event. `stopPropagation` prevents this.
- *Why D is incorrect:* `stopPropagation` does not cancel all event processing. The target element's listeners still fire (the button's listener runs normally). Only propagation to ancestors is stopped.
