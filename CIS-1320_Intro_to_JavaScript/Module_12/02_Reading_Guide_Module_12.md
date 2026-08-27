# Reading Guide: Module 12 — Event Handling and Listeners

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Events are the mechanism by which web pages become interactive. Clicks, keystrokes, form input, mouse movement, page load — all are events that JavaScript can observe and respond to. Module 12 covers the complete event model: registering listeners, the event object, default browser behaviors, event bubbling and propagation, and the delegation pattern. These concepts underpin every interactive feature in every web application.

---

## 1. `addEventListener`

`addEventListener(type, handler)` registers a callback to be called when the specified event occurs on the element:

```javascript
const btn = document.getElementById('submit-btn');

btn.addEventListener('click', function(event) {
  console.log('Clicked!');
});
```

The handler (callback) is invoked by the browser when the event fires. It receives one argument: the event object.

### Multiple Listeners

Unlike assigning to `.onclick`, `addEventListener` supports multiple independent listeners on the same element for the same event:

```javascript
btn.addEventListener('click', () => console.log('first'));
btn.addEventListener('click', () => console.log('second'));
// Both fire on every click — neither overwrites the other
```

### `removeEventListener`

To remove a listener, pass the same function reference:

```javascript
function handleClick(e) {
  console.log('clicked');
}

btn.addEventListener('click', handleClick);
btn.removeEventListener('click', handleClick);   // removes it
```

**Critical:** `removeEventListener` matches by function reference. Inline arrow functions create a new function object each time — there is no reference to pass back, so they cannot be removed:

```javascript
btn.addEventListener('click', () => console.log('cannot remove'));
// No way to remove this listener — the arrow function is anonymous
```

Store the handler in a named variable or function declaration when removal is needed.

### `addEventListener` vs `onclick`

| Approach | Multiple listeners? | Removable? | Recommended? |
|---|---|---|---|
| `element.addEventListener('click', fn)` | Yes | Yes (with reference) | Yes |
| `element.onclick = fn` | No — overwrites | Yes | No |
| `<button onclick="fn()">` | No | No | No |

---

## 2. The Event Object

Every listener receives an **event object** as its first argument. It describes what happened.

### Universal Properties

| Property | Description |
|---|---|
| `event.type` | String: the event type (`'click'`, `'keydown'`, `'submit'`) |
| `event.target` | The element where the event originated |
| `event.currentTarget` | The element the listener is attached to |
| `event.timeStamp` | Milliseconds since page load when the event fired |

### Mouse Event Properties

```javascript
element.addEventListener('click', (e) => {
  console.log(e.clientX, e.clientY);   // position relative to viewport
  console.log(e.pageX, e.pageY);       // position relative to document
  console.log(e.button);               // 0=left, 1=middle, 2=right
});
```

### Keyboard Event Properties

```javascript
document.addEventListener('keydown', (e) => {
  console.log(e.key);       // 'a', 'Enter', 'ArrowUp', ' ' (space), etc.
  console.log(e.code);      // 'KeyA', 'Enter', 'ArrowUp', 'Space'
  console.log(e.shiftKey);  // boolean — true if Shift was held
  console.log(e.ctrlKey);   // boolean — true if Ctrl was held
  console.log(e.altKey);    // boolean — true if Alt was held
});
```

Use `event.key` for most keyboard handling. Use `event.code` when you need the physical key position (e.g., game controls where WASD should work regardless of keyboard layout).

### Form Event Properties

```javascript
input.addEventListener('input', (e) => {
  console.log(e.target.value);   // current value of the input
});
```

For `<select>` and `<checkbox>`:

- `event.target.value` — the selected value
- `event.target.checked` — boolean for checkboxes

---

## 3. Common Event Types

| Category | Event | When it fires |
|---|---|---|
| Mouse | `click` | Left-button click and release |
| Mouse | `dblclick` | Double-click |
| Mouse | `mouseenter` | Mouse enters element (does not bubble) |
| Mouse | `mouseleave` | Mouse leaves element (does not bubble) |
| Mouse | `mouseover` | Mouse enters element or any descendant (bubbles) |
| Mouse | `mousemove` | Mouse moves while over element |
| Keyboard | `keydown` | Key is pressed |
| Keyboard | `keyup` | Key is released |
| Form | `submit` | Form is submitted |
| Form | `input` | Value changes (fires on every keystroke) |
| Form | `change` | Value changes and element loses focus |
| Form | `focus` | Element gains focus (does not bubble) |
| Form | `blur` | Element loses focus (does not bubble) |
| Document | `DOMContentLoaded` | HTML parsed, DOM ready |
| Window | `load` | Page fully loaded including images |

### `input` vs `change`

```javascript
const field = document.getElementById('search');

field.addEventListener('input', e => {
  // Fires on every keystroke — good for live search
  console.log('Typing:', e.target.value);
});

field.addEventListener('change', e => {
  // Fires only when field loses focus with a new value — good for validation
  console.log('Committed:', e.target.value);
});
```

---

## 4. `preventDefault`

Browsers have default behaviors for many events — form submission reloads the page, clicking a link navigates, right-clicking opens a context menu. `event.preventDefault()` cancels the browser's default response:

```javascript
// Prevent form reload
form.addEventListener('submit', (e) => {
  e.preventDefault();
  // Handle form data with JavaScript instead
});

// Prevent link navigation
link.addEventListener('click', (e) => {
  e.preventDefault();
  console.log('Link click intercepted');
});
```

`preventDefault` does **not** stop the event from bubbling. It only cancels the browser's built-in response. To stop bubbling, use `stopPropagation` (see next section).

---

## 5. Event Bubbling and Propagation

When an event fires on an element, it **bubbles** — it propagates upward through all ancestors to `document`. Every ancestor with a listener for the same event type will also receive it.

### Bubbling Example

```html
<div id="outer">
  <div id="inner">
    <button id="btn">Click</button>
  </div>
</div>
```

```javascript
document.getElementById('btn').addEventListener('click',   () => console.log('btn'));
document.getElementById('inner').addEventListener('click', () => console.log('inner'));
document.getElementById('outer').addEventListener('click', () => console.log('outer'));
document.addEventListener('click',                         () => console.log('document'));
```

Clicking the button logs: `btn`, `inner`, `outer`, `document` — in that order. The event starts at the deepest element and travels up.

### `event.target` vs `event.currentTarget`

| Property | Value during bubbling |
|---|---|
| `event.target` | Always the element where the event originated (the button) |
| `event.currentTarget` | The element whose listener is currently executing (changes as event bubbles) |

```javascript
document.getElementById('outer').addEventListener('click', (e) => {
  console.log(e.target.id);          // 'btn' — where click happened
  console.log(e.currentTarget.id);   // 'outer' — where this listener is
});
```

### `stopPropagation`

Stops the event from traveling further up the tree:

```javascript
document.getElementById('btn').addEventListener('click', (e) => {
  e.stopPropagation();
  console.log('btn only — no bubbling');
});
```

After `stopPropagation`, the `inner`, `outer`, and `document` listeners do not fire for this event.

### `stopImmediatePropagation`

Stops bubbling AND prevents any other listeners on the same element from firing:

```javascript
btn.addEventListener('click', (e) => {
  e.stopImmediatePropagation();
  console.log('only this listener fires');
});
btn.addEventListener('click', () => {
  console.log('this never fires');
});
```

### Events That Do Not Bubble

`focus`, `blur`, `mouseenter`, `mouseleave`, and `scroll` do not bubble. Their bubbling equivalents (`focusin`, `focusout`, `mouseover`, `mouseout`) do bubble and can be used with delegation.

---

## 6. Event Delegation

Event delegation adds a single listener to a **parent** element and uses `event.target` to determine which child was interacted with. It relies on bubbling.

### Why Delegation?

- **Performance:** One listener instead of one per child
- **Dynamic elements:** Handles children added after the listener was registered

### Basic Delegation

```javascript
const ul = document.getElementById('task-list');

ul.addEventListener('click', (e) => {
  if (e.target.tagName === 'LI') {
    e.target.classList.toggle('done');
  }
});
```

### Delegation with `closest`

When list items contain child elements (icons, badges, buttons), `event.target` may be one of those children, not the `<li>` itself. `closest(selector)` walks up from `event.target` to find the nearest ancestor matching the selector:

```javascript
ul.addEventListener('click', (e) => {
  const li = e.target.closest('li');
  if (!li) return;   // click was outside any li
  li.classList.toggle('done');
});
```

`closest` starts at `e.target` itself, checks it, then walks up. If `e.target` is the `<li>`, it returns the `<li>`. If `e.target` is a `<span>` inside the `<li>`, it returns the `<li>`. If the click was outside any `<li>`, it returns `null`.

### Filtering by Data Attribute

```javascript
document.getElementById('toolbar').addEventListener('click', (e) => {
  const btn = e.target.closest('[data-action]');
  if (!btn) return;

  const action = btn.dataset.action;
  if (action === 'save')   saveDocument();
  if (action === 'delete') deleteDocument();
  if (action === 'print')  window.print();
});
```

---

## 7. `DOMContentLoaded`

Scripts placed in `<head>` run before the DOM is built. Querying elements at that point returns `null`.

**Solution 1 — Script at end of `<body>`** (used in the labs):

```html
<body>
  <!-- All HTML here -->
  <script src="lab.js"></script>
</body>
```

**Solution 2 — `DOMContentLoaded` listener**:

```javascript
document.addEventListener('DOMContentLoaded', () => {
  // DOM is ready — safe to query and attach listeners
  document.getElementById('btn').addEventListener('click', handler);
});
```

`DOMContentLoaded` fires when HTML parsing is complete. It fires before images and stylesheets finish loading. For most JavaScript initialization, `DOMContentLoaded` is the right moment.

---

## 8. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 15: Handling Events](https://eloquentjavascript.net/15_event.html)**
  The primary OER textbook chapter for this module. Covers event handlers, propagation, default actions, key events, mouse events, scroll events, focus/blur, and debouncing, with extensive worked examples.

- **[MDN Web Docs — Introduction to events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events)**
  Comprehensive guide covering event handlers, event objects, `addEventListener`, event bubbling and capture, event delegation, and removing listeners. Includes interactive examples and comparisons of all three handler registration approaches.

- **[MDN Web Docs — Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)**
  Complete reference for all standard DOM events organized by category (mouse, keyboard, form, document, window). Use this as a lookup for any event type's full specification.

- **[MDN Web Docs — Element.closest()](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest)**
  Full reference for `closest` including the selector syntax, traversal direction, return value, and examples using it with event delegation to handle nested element structures.

- **[javascript.info — Introduction to browser events](https://javascript.info/introduction-browser-events)**
  Clear, beginner-friendly coverage of event handlers, the event object, bubbling and capturing, `stopPropagation`, and `preventDefault`, with interactive diagrams showing event flow through the DOM tree.

---

## 9. JSE Certification Exam Tips

1. **`addEventListener` vs `onclick`** — `addEventListener` supports multiple listeners; `onclick` overwrites. In all new code, use `addEventListener`.

2. **`removeEventListener` requires the same reference** — inline arrows cannot be removed. Store the function in a variable if removal is needed.

3. **`event.target` is the origin; `event.currentTarget` is the listener's element** — during bubbling, `target` never changes; `currentTarget` changes as the event travels up.

4. **Events bubble by default** — `click`, `keydown`, `submit`, `input`, `change` all bubble. `focus`, `blur`, `mouseenter`, `mouseleave`, `scroll` do not.

5. **`stopPropagation` stops bubbling** — the event does not reach ancestor listeners. `preventDefault` stops the browser's default action — they are independent.

6. **Event delegation relies on bubbling** — one listener on a parent handles events from all descendants. Works for dynamically added elements.

7. **`event.target.closest(selector)`** — walks up from the event target and returns the nearest ancestor matching the selector (or `null`). Essential for delegation when child elements have their own structure.

8. **`input` fires on every change; `change` fires on blur** — use `input` for live feedback (search-as-you-type); use `change` for final validation.

9. **`event.key` for keyboard events** — `'Enter'`, `'Escape'`, `'ArrowUp'`, `' '` (space), `'a'`–`'z'`. Do not use `event.keyCode` — it is deprecated.

10. **`event.preventDefault()` on `submit`** — required to prevent the default form-reload behavior when handling forms with JavaScript.

---

## 10. Study Checklist

- [ ] Watch the Module 12 video lecture by Professor Nash.
- [ ] Read Chapter 15 (Handling Events) of [Eloquent JavaScript](https://eloquentjavascript.net/15_event.html).
- [ ] Read [MDN — Introduction to events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events).
- [ ] Read [MDN — Element.closest()](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest).
- [ ] Build a nested div structure and add `click` listeners to each level — observe the bubbling order in the console.
- [ ] Test `removeEventListener` with a named function — confirm the listener stops firing. Then try with an inline arrow — confirm it cannot be removed.
- [ ] Build a delegated list: one `click` listener on `<ul>` that toggles a class on clicked `<li>` elements.
- [ ] Add a new `<li>` to the list after the listener was registered — confirm the new item is also handled.
- [ ] Complete the Module 12 Lab.
- [ ] Complete the Module 12 Quiz.
