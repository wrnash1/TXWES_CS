# Video Script: CIS-1320 — Introduction to JavaScript

## Module 12 — Event Handling and Listeners

**Estimated Duration:** 18–22 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Live Server + Chrome DevTools for all [DEMO] sections. The Elements panel and Event Listeners tab in DevTools are useful for confirming listeners are registered.
> - [PAUSE] = 2 seconds of silence.
> - The event object is the conceptual core — every listener receives it, and `event.target` is how you identify what was clicked. Spend time here.
> - Event bubbling is JSE-tested. The visual: event fires on innermost element and bubbles up through ancestors. `event.stopPropagation()` is the escape hatch.
> - Event delegation is the key practical pattern — one listener on the parent instead of one per child. The `event.target.closest()` technique makes this clean.
> - `removeEventListener` requires the exact same function reference — cannot use inline arrows. This is a common mistake.
> - `DOMContentLoaded` — brief mention: scripts in `<head>` that reference DOM elements must wait for the DOM to be ready. Scripts at the end of `<body>` (as used in the labs) do not have this problem.
> - `input` vs `change` event distinction: `input` fires on every keystroke; `change` fires on blur. Worth demonstrating on a text field.
> - Do not cover `this` inside event handlers deeply — Module 09 established that arrow functions capture lexical `this`. Keep focus on `event.target`.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 12 | Event Handling and Listeners | CIS-1320"]**

"A web page that cannot respond to user actions is just a document. Events — clicks, keystrokes, form submissions, mouse movements — are how JavaScript makes pages interactive. Module 12 covers the complete event handling model: how to register listeners, what the event object contains, how events travel through the DOM, and how to handle many elements efficiently with a single listener.

By the end of this module, you will understand not just how to write a click handler but why events work the way they do — and that understanding will save you hours of debugging."

---

## [01:30 – 06:00] Part 1 — `addEventListener`

**[SHOW SLIDE: "addEventListener"]**

"`addEventListener` is the standard way to respond to events in modern JavaScript.

**[DEMO]**

```javascript
const btn = document.getElementById('my-btn');

btn.addEventListener('click', function(event) {
  console.log('Button clicked!');
  console.log('Event object:', event);
});
```

The three pieces:

1. The **element** to listen on: `btn`
2. The **event type** as a string: `'click'`
3. The **handler function** (the callback): receives the event object

[PAUSE]

**Why `addEventListener` instead of `onclick`?**

You may see older code using `element.onclick = function() {...}` or HTML attributes like `<button onclick='doSomething()'>`. These work, but they have a critical limitation: you can only assign one handler. `addEventListener` allows multiple listeners on the same element for the same event:

```javascript
btn.addEventListener('click', () => console.log('First listener'));
btn.addEventListener('click', () => console.log('Second listener'));
// Both fire — neither overwrites the other
```

Always use `addEventListener` in new code.

[PAUSE]

**Removing a listener — `removeEventListener`:**

```javascript
function handleClick(event) {
  console.log('clicked');
}

btn.addEventListener('click', handleClick);

// Later — remove it
btn.removeEventListener('click', handleClick);
```

`removeEventListener` requires the **exact same function reference** that was passed to `addEventListener`. This is why inline arrow functions cannot be removed — each arrow creates a new function object, so there is no reference to pass back:

```javascript
// Cannot remove this:
btn.addEventListener('click', () => console.log('inline'));
// btn.removeEventListener('click', () => console.log('inline'));
// This does nothing — a different function object
```

Store the handler in a named variable or function declaration if you need to remove it later."

---

## [06:00 – 11:00] Part 2 — The Event Object

**[SHOW SLIDE: "The Event Object"]**

"Every event handler receives an **event object** as its first argument. This object contains information about what happened: what element was interacted with, where the mouse was, what key was pressed, and more.

**[DEMO — `event.target` and `event.type`]**

```javascript
document.addEventListener('click', (event) => {
  console.log('Event type:', event.type);     // 'click'
  console.log('Target:', event.target);       // the element that was clicked
  console.log('Target tag:', event.target.tagName);
});
```

`event.target` is the element that the user actually interacted with — the element where the event originated. This is not necessarily the element you attached the listener to. More on that in the bubbling section.

[PAUSE]

**Mouse events:**

```javascript
const box = document.getElementById('hover-box');

box.addEventListener('mousemove', (event) => {
  console.log(`Mouse at: ${event.clientX}, ${event.clientY}`);
});

box.addEventListener('mouseenter', () => console.log('Mouse entered'));
box.addEventListener('mouseleave', () => console.log('Mouse left'));
```

[PAUSE]

**Keyboard events:**

```javascript
document.addEventListener('keydown', (event) => {
  console.log('Key pressed:', event.key);      // 'a', 'Enter', 'ArrowUp', etc.
  console.log('Code:', event.code);            // 'KeyA', 'Enter', 'ArrowUp'
  console.log('Shift held?', event.shiftKey);  // boolean
  console.log('Ctrl held?',  event.ctrlKey);
});
```

`event.key` is the logical key value — what the key produces. `event.code` is the physical key location. For most purposes, use `event.key`.

[PAUSE]

**Form events:**

```javascript
const input = document.getElementById('search-input');

// input fires on every keystroke
input.addEventListener('input', (event) => {
  console.log('Current value:', event.target.value);
});

// change fires when the field loses focus with a changed value
input.addEventListener('change', (event) => {
  console.log('Final value:', event.target.value);
});
```

[PAUSE]

**`preventDefault` — stopping default behavior:**

```javascript
const form = document.getElementById('signup-form');

form.addEventListener('submit', (event) => {
  event.preventDefault();   // stops the browser from reloading the page
  console.log('Form submitted — handling with JavaScript');
  // validate and process the form data here
});

const link = document.querySelector('a#no-navigate');
link.addEventListener('click', (event) => {
  event.preventDefault();   // stops navigation to href
  console.log('Link clicked but navigation prevented');
});
```

`preventDefault` tells the browser not to perform its built-in response to the event. It does not stop other JavaScript listeners."

---

## [11:00 – 15:30] Part 3 — Event Bubbling and `stopPropagation`

**[SHOW SLIDE: "Event Bubbling"]**

"When an event fires on an element, it does not just stay there. It **bubbles** up through the DOM — from the target element to its parent, to its grandparent, all the way to `document`. Every ancestor that has a listener for the same event type also receives it.

**[DEMO]**

```html
<div id="outer">
  <div id="inner">
    <button id="btn">Click me</button>
  </div>
</div>
```

```javascript
document.getElementById('btn').addEventListener('click',   () => console.log('button'));
document.getElementById('inner').addEventListener('click', () => console.log('inner'));
document.getElementById('outer').addEventListener('click', () => console.log('outer'));
```

Click the button — all three listeners fire. The console logs:

```text
button
inner
outer
```

The event starts at `button`, bubbles to `inner`, then to `outer`. This is bubbling.

[PAUSE]

**`event.stopPropagation()`** — stops the event from bubbling further:

```javascript
document.getElementById('btn').addEventListener('click', (event) => {
  event.stopPropagation();   // inner and outer listeners will NOT fire
  console.log('button only');
});
```

Use `stopPropagation` sparingly — it makes event behavior harder to reason about in complex UIs.

[PAUSE]

**`event.target` vs `event.currentTarget`:**

```javascript
document.getElementById('outer').addEventListener('click', (event) => {
  console.log('target:', event.target.id);          // the element clicked
  console.log('currentTarget:', event.currentTarget.id);  // 'outer' — where the listener is
});
```

`event.target` — where the event originated.
`event.currentTarget` — the element the listener is attached to.
When the event bubbles, `target` stays fixed at the origin; `currentTarget` changes as the event moves up."

---

## [15:30 – 19:00] Part 4 — Event Delegation

**[SHOW SLIDE: "Event Delegation"]**

"Bubbling enables one of the most important patterns in DOM event handling: **event delegation**.

Imagine a list with 100 items. You want each item to be clickable. Adding 100 separate listeners is wasteful. Instead, add one listener to the parent — events from the children bubble up to it:

**[DEMO]**

```javascript
const list = document.getElementById('item-list');

list.addEventListener('click', (event) => {
  // event.target is the actual element clicked
  if (event.target.tagName === 'LI') {
    console.log('Clicked item:', event.target.textContent);
    event.target.classList.toggle('selected');
  }
});
```

One listener handles all current and future list items — including items added to the list after the listener was registered. This is the key advantage of delegation over individual listeners.

[PAUSE]

**`event.target.closest(selector)`** — a cleaner check:

```javascript
list.addEventListener('click', (event) => {
  const item = event.target.closest('li');
  if (!item) return;   // clicked outside any li

  item.classList.toggle('selected');
  console.log('Selected:', item.textContent);
});
```

`closest(selector)` starts at `event.target` and walks up the DOM until it finds an ancestor matching the selector, or returns `null` if none is found. This handles clicks on child elements inside an `<li>` (like a `<strong>` or `<span>`) — `event.target` might be the inner element, but `closest('li')` still finds the `<li>` ancestor.

[PAUSE]

**When to use event delegation:**

- Lists of items where each needs the same handler
- Dynamically added elements (delegation handles future elements automatically)
- Large numbers of similar elements

**When not to use it:**

- Events that do not bubble (`focus`, `blur`, `scroll` — though `focusin`/`focusout` do bubble)
- When you need different behavior for each element that cannot be determined from the element itself"

---

## [19:00 – 21:00] Part 5 — `DOMContentLoaded`

**[SHOW SLIDE: "DOMContentLoaded"]**

"A brief but important concept: when does JavaScript run relative to the DOM?

If your `<script>` tag is in the `<head>`, the browser parses and executes the script before it has finished parsing the `<body>`. Any `document.getElementById` call in that script will return `null` — the element does not exist yet.

```html
<!-- Problem: script in head, DOM not ready yet -->
<head>
  <script>
    const btn = document.getElementById('my-btn');   // null!
  </script>
</head>
<body>
  <button id='my-btn'>Click me</button>
</body>
```

Two solutions:

**Solution 1 — Place `<script>` at the end of `<body>`** (what the labs do):

```html
<body>
  <button id='my-btn'>Click me</button>
  <script src='lab.js'></script>  <!-- DOM is fully parsed before this runs -->
</body>
```

**Solution 2 — Listen for `DOMContentLoaded`**:

```javascript
document.addEventListener('DOMContentLoaded', () => {
  // DOM is fully parsed — safe to query elements
  const btn = document.getElementById('my-btn');
  btn.addEventListener('click', () => console.log('clicked'));
});
```

`DOMContentLoaded` fires when the HTML is fully parsed and the DOM tree is built, before stylesheets and images finish loading. The labs place `<script>` at the end of `<body>`, so this is not required — but you will see it frequently in real codebases."

---

## [21:00 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 12 Lab Preview"]**

"The Module 12 lab has four parts.

Part 1 covers `addEventListener` and multiple listeners — you will add several event types to the same element and confirm they fire independently.

Part 2 covers the event object — you will log `event.target`, `event.key`, `event.clientX`, and use `preventDefault` on a form and a link.

Part 3 covers event bubbling — you will build a nested structure, observe the bubbling order in the console, and use `stopPropagation` to interrupt it.

Part 4 is the integration — a task list application using event delegation. Adding a new task, marking tasks complete, and removing tasks are all handled by delegated listeners on the container rather than individual listeners on each task.

Read the reading guide before the lab — `event.target` vs `event.currentTarget` and the `closest` technique are both covered in more depth there. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 12 — Event Handling and Listeners]**

---

## Additional Resources

- [MDN — EventTarget.addEventListener()](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [MDN — Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
- [MDN — Event bubbling](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling)
- [MDN — Element.closest()](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest)
- [MDN — Event.preventDefault()](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)
- [Eloquent JavaScript — Chapter 15: Handling Events](https://eloquentjavascript.net/15_event.html)
