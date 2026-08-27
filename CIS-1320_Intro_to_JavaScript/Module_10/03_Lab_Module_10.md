# Lab Activity: Module 10 — Document Object Model (DOM) Basics

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Lab Overview

This lab introduces hands-on DOM manipulation. Unlike previous labs that ran in Node.js, this lab runs in the browser. You will write JavaScript that reads from and writes to a live web page, selecting elements, modifying content, toggling classes, and traversing the tree.

**Environment:** VS Code + Live Server extension + Chrome or Firefox DevTools

---

## Setup

Create a project folder called `module10_lab`. Inside it, create the following two files:

**`index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 10 Lab</title>
  <style>
    body { font-family: sans-serif; max-width: 700px; margin: 2rem auto; padding: 0 1rem; }
    h1 { color: #333; }
    .highlight { background-color: #fffbcc; border-left: 4px solid #f0c400; padding: 0.5rem 1rem; }
    .hidden { display: none; }
    .active { color: #0057b8; font-weight: bold; }
    .dark-mode { background-color: #1a1a1a; color: #f0f0f0; }
    .dark-mode h1 { color: #f0f0f0; }
    .card { border: 1px solid #ccc; padding: 1rem; margin: 0.5rem 0; border-radius: 4px; }
    .card.selected { border-color: #0057b8; background-color: #e8f0fb; }
    #status { padding: 0.5rem; margin-top: 1rem; font-style: italic; color: #666; }
  </style>
</head>
<body>
  <h1 id="main-heading">Module 10: DOM Basics</h1>

  <p id="intro-text">This paragraph can be changed by JavaScript.</p>

  <ul id="item-list">
    <li class="item">Apple</li>
    <li class="item">Banana</li>
    <li class="item">Cherry</li>
    <li class="item">Date</li>
  </ul>

  <div id="card-container">
    <div class="card" data-id="1">Card One</div>
    <div class="card" data-id="2">Card Two</div>
    <div class="card" data-id="3">Card Three</div>
  </div>

  <a id="main-link" href="https://txwes.edu">Texas Wesleyan University</a>

  <div id="status"></div>

  <script src="lab10.js"></script>
</body>
</html>
```

**`lab10.js`** — start with this file empty. You will add code section by section.

Open `index.html` with Live Server. The page should display. Open the browser's DevTools Console (`F12` → Console tab) where you can see output as you work.

---

## Part 1 — Selecting Elements

**File:** `lab10.js`

**Learning objectives:** Use `getElementById`, `querySelector`, `querySelectorAll`; observe the types of values returned; practice null checking.

### Section 1.1 — Single-Element Selectors

Add the following to `lab10.js`:

```javascript
// --- Part 1: Selecting Elements ---

// 1.1 — getElementById
const heading = document.getElementById('main-heading');
console.log('getElementById result:', heading);
console.log('Tag name:', heading.tagName);       // 'H1'
console.log('Text content:', heading.textContent); // 'Module 10: DOM Basics'

// 1.2 — querySelector by ID (note the # prefix)
const headingQ = document.querySelector('#main-heading');
console.log('querySelector by ID:', headingQ);

// Are they the same element?
console.log('Same element?', heading === headingQ);   // true

// 1.3 — querySelector by class
const intro = document.querySelector('.item');   // first match only
console.log('First .item:', intro.textContent);   // 'Apple'

// 1.4 — querySelector by tag
const firstLi = document.querySelector('li');
console.log('First li:', firstLi.textContent);   // 'Apple'
```

Save, check the console. Confirm the outputs. Note that `getElementById` and `querySelector('#main-heading')` return the same object.

### Section 1.2 — `querySelectorAll`

```javascript
// 1.5 — querySelectorAll returns a NodeList
const items = document.querySelectorAll('.item');
console.log('NodeList:', items);
console.log('Length:', items.length);   // 4
console.log('First:', items[0].textContent);
console.log('Last:', items[items.length - 1].textContent);

// 1.6 — NodeList has forEach but NOT map, filter, reduce
items.forEach((item, i) => {
  console.log(`  items[${i}] = ${item.textContent}`);
});

// 1.7 — Convert to Array to use full array methods
const itemArray = Array.from(items);
const texts = itemArray.map(li => li.textContent);
console.log('Texts array:', texts);   // ['Apple', 'Banana', 'Cherry', 'Date']
```

Save and confirm the NodeList contains 4 items and that `Array.from` lets you use `map`.

### Section 1.3 — Null Checks

```javascript
// 1.8 — When no element matches, null is returned
const missing = document.getElementById('does-not-exist');
console.log('Missing element:', missing);   // null

// 1.9 — Accessing a property of null throws TypeError
// Uncomment the next line to observe the error, then re-comment it
// console.log(missing.textContent);   // TypeError!

// 1.10 — Safe pattern: check before using
if (missing) {
  console.log(missing.textContent);
} else {
  console.log('Element not found — skipping');   // This logs
}

// 1.11 — Optional chaining also works
console.log(missing?.textContent);   // undefined (no error)
```

Save and observe. The optional chaining `?.` prevents the TypeError and returns `undefined` instead of crashing.

---

## Part 2 — Reading and Modifying Content

**Learning objectives:** Use `textContent` and `innerHTML`; understand the safety difference; read and write attributes.

### Section 2.1 — `textContent`

```javascript
// --- Part 2: Content ---

// 2.1 — Read textContent
const introText = document.getElementById('intro-text');
console.log('Original text:', introText.textContent);

// 2.2 — Write textContent
introText.textContent = 'Updated by JavaScript using textContent.';
console.log('After update:', introText.textContent);

// 2.3 — textContent with HTML tags — tags are treated as literal text, not parsed
introText.textContent = 'This is <strong>NOT bold</strong> — it is literal text.';
// The page shows the angle brackets as visible characters
```

Save. Observe on the page — the `<strong>` tags are visible as text, not rendered as HTML.

### Section 2.2 — `innerHTML`

```javascript
// 2.4 — Write innerHTML — the string is parsed as HTML
introText.innerHTML = 'This is <strong>bold</strong> via innerHTML.';
// 'bold' appears bold on the page

// 2.5 — Read innerHTML — returns the inner HTML string
console.log('innerHTML:', introText.innerHTML);
// 'This is <strong>bold</strong> via innerHTML.'

// 2.6 — textContent after innerHTML — strips tags, returns text only
console.log('textContent after innerHTML:', introText.textContent);
// 'This is bold via innerHTML.'
```

Save. Confirm that `innerHTML` renders the `<strong>` tag visually. Note that reading `textContent` after `innerHTML` strips the tags.

### Section 2.3 — Safe vs Unsafe Use

```javascript
// 2.7 — Safe: textContent for any user-provided data
const simulatedUserInput = '<img src=x onerror="alert(\'XSS attack\')">';

// SAFE: displays the text literally
introText.textContent = simulatedUserInput;
// You see the angle brackets as text — no alert fires

// UNSAFE (do not uncomment in a real app with real user data):
// introText.innerHTML = simulatedUserInput;
// In a real app this would execute the onerror script!

// Reset to normal text after the demo
introText.textContent = 'Content reset.';
```

### Section 2.4 — Attributes

```javascript
// 2.8 — getAttribute
const link = document.getElementById('main-link');
console.log('href:', link.getAttribute('href'));   // 'https://txwes.edu'
console.log('id:', link.getAttribute('id'));        // 'main-link'

// 2.9 — setAttribute
link.setAttribute('href', 'https://www.txwes.edu/academics');
link.setAttribute('target', '_blank');
console.log('Updated href:', link.getAttribute('href'));

// 2.10 — hasAttribute / removeAttribute
console.log('Has target?', link.hasAttribute('target'));   // true
link.removeAttribute('target');
console.log('Has target after remove?', link.hasAttribute('target'));   // false

// 2.11 — Direct property shortcut (equivalent to setAttribute)
link.href = 'https://txwes.edu';   // restores original
```

### Section 2.5 — Custom Data Attributes

```javascript
// 2.12 — data-* attributes via dataset
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
  // data-id="1" is accessed as card.dataset.id
  console.log('Card data-id:', card.dataset.id);
});
// Logs: '1', '2', '3'
```

---

## Part 3 — `classList` and CSS Classes

**Learning objectives:** Add, remove, toggle, and check classes using `classList`; build a working toggle feature; compare `classList` to `className`.

### Section 3.1 — Basic `classList` Methods

```javascript
// --- Part 3: classList ---

const heading3 = document.getElementById('main-heading');

// 3.1 — add
heading3.classList.add('highlight');
console.log('After add:', heading3.className);   // 'highlight'

// 3.2 — contains
console.log('Has highlight?', heading3.classList.contains('highlight'));   // true
console.log('Has active?', heading3.classList.contains('active'));         // false

// 3.3 — remove
heading3.classList.remove('highlight');
console.log('After remove:', heading3.className);   // ''

// 3.4 — toggle — adds if absent, removes if present
heading3.classList.toggle('active');
console.log('After first toggle:', heading3.classList.contains('active'));   // true
heading3.classList.toggle('active');
console.log('After second toggle:', heading3.classList.contains('active'));  // false

// 3.5 — toggle return value
const wasAdded = heading3.classList.toggle('active');
console.log('Toggle return value:', wasAdded);   // true (class was added)
```

### Section 3.2 — `classList` vs `className`

```javascript
// 3.6 — classList.add preserves existing classes
heading3.classList.add('active');
heading3.classList.add('highlight');
console.log('classList after two adds:', heading3.className);
// 'active highlight' — both classes present

// 3.7 — className = replaces ALL classes
heading3.className = 'new-class';
console.log('className after assign:', heading3.className);
// 'new-class' — 'active' and 'highlight' are GONE

// Reset
heading3.className = '';
```

### Section 3.3 — Working Toggle Feature

Add this code to implement a dark mode toggle. Note that the button does not exist in the HTML yet — add a button to the `<body>` in `index.html` first:

In `index.html`, add this line just before `<div id="status">`:

```html
<button id="dark-btn">Toggle Dark Mode</button>
```

Then in `lab10.js`:

```javascript
// 3.8 — Dark mode toggle
const darkBtn = document.getElementById('dark-btn');

darkBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');

  const isNowDark = document.body.classList.contains('dark-mode');
  darkBtn.textContent = isNowDark ? 'Switch to Light Mode' : 'Toggle Dark Mode';

  const status = document.getElementById('status');
  status.textContent = isNowDark ? 'Dark mode is ON' : 'Dark mode is OFF';
});
```

Save both files. Click the button and confirm the page background toggles between dark and light, and the button text updates.

### Section 3.4 — Card Selection

```javascript
// 3.9 — Clicking a card selects it; clicking again deselects it
const allCards = document.querySelectorAll('.card');

allCards.forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('selected');

    const status = document.getElementById('status');
    const selectedCards = document.querySelectorAll('.card.selected');
    status.textContent = `${selectedCards.length} card(s) selected`;
  });
});
```

Save. Click cards to observe the selection style toggling. The status line counts how many are selected.

---

## Part 4 — DOM Traversal and Integration

**Learning objectives:** Navigate the DOM tree from a selected element; combine selection, content modification, and traversal; build a small working feature.

### Section 4.1 — Traversal Properties

```javascript
// --- Part 4: Traversal ---

const list = document.getElementById('item-list');

// 4.1 — Parent
console.log('Parent of ul:', list.parentElement.tagName);   // 'BODY'

// 4.2 — Children
console.log('Children count:', list.children.length);   // 4
console.log('First child:', list.firstElementChild.textContent);    // 'Apple'
console.log('Last child:', list.lastElementChild.textContent);      // 'Date'

// 4.3 — Iterate children
Array.from(list.children).forEach((child, i) => {
  console.log(`  child[${i}]: ${child.textContent}`);
});

// 4.4 — Siblings
const firstItem = list.firstElementChild;
console.log('Next sibling:', firstItem.nextElementSibling.textContent);    // 'Banana'
console.log('Prev sibling:', firstItem.previousElementSibling);            // null
```

### Section 4.2 — Scoped Selection

```javascript
// 4.5 — querySelector on an element searches only its descendants
const cardContainer = document.getElementById('card-container');

// Only finds .card elements inside #card-container
const firstCard = cardContainer.querySelector('.card');
console.log('First card text:', firstCard.textContent);   // 'Card One'

// querySelectorAll scoped to container
const containerCards = cardContainer.querySelectorAll('.card');
console.log('Cards in container:', containerCards.length);   // 3
```

### Section 4.3 — Integration Exercise

Build a list highlighter: clicking a list item highlights it and logs its position information. Add this to `lab10.js`:

```javascript
// 4.6 — Integration: list item inspector
const listItems = document.querySelectorAll('#item-list .item');

listItems.forEach((item, index) => {
  item.addEventListener('click', () => {
    // Clear previous highlights
    listItems.forEach(li => li.classList.remove('highlight'));

    // Highlight clicked item
    item.classList.add('highlight');

    // Report position using traversal
    const parent = item.parentElement;
    const siblings = Array.from(parent.children);
    const position = siblings.indexOf(item);
    const total = siblings.length;

    const prev = item.previousElementSibling;
    const next = item.nextElementSibling;

    const status = document.getElementById('status');
    status.innerHTML = `
      <strong>${item.textContent}</strong> —
      position ${position + 1} of ${total} |
      prev: ${prev ? prev.textContent : 'none'} |
      next: ${next ? next.textContent : 'none'}
    `;
  });
});
```

Save. Click each list item in sequence. The status div should update with the item's position and its neighbors. Verify all four items report correct siblings (Apple has no prev; Date has no next).

### Section 4.4 — Reflection Questions

Answer these questions in a comment block at the bottom of `lab10.js`:

```javascript
/*
  Reflection:

  1. What is the difference between querySelectorAll and getElementsByClassName?
     (Hint: static vs live, return type)

  2. What happens if you call innerHTML with a string that contains <script> tags?
     Why is textContent safer for user-provided content?

  3. Why does classList.add not destroy existing classes, but className = does?

  4. What does previousElementSibling return for the first child of a parent?

  5. When would you use querySelector on an element (not document)?
*/
```

---

## Part 9 — Challenge Exercise

This section is **optional**. It extends the lab with advanced problems that apply DOM selection, traversal, and class management in more demanding scenarios.

### Step 9.1 — Build a DOM Query Utility

Add a `<script>` section to `lab10.html` (or create `dom_utils.js`) and implement two utility functions that wrap the built-in DOM selection methods:

```javascript
// Returns the first matching element or throws a descriptive error
function $$(selector, context = document) {
  const el = context.querySelector(selector);
  if (!el) throw new Error(`No element found for selector: "${selector}"`);
  return el;
}

// Returns a true Array of all matching elements
function $$all(selector, context = document) {
  return Array.from(context.querySelectorAll(selector));
}
```

Verify both utilities:

```javascript
// Should work
const heading = $$('h1');
console.log(heading.textContent);

// Should throw — catch and log the error message
try {
  $$('#does-not-exist');
} catch (e) {
  console.error(e.message);
}

// Should return an array with map available
const texts = $$all('li').map(li => li.textContent);
console.log(texts);
```

Extend `$$all` to accept an optional `transform` callback: if provided, it should apply the callback to every matched element and return the mapped results (equivalent to `$$all(sel).map(transform)`).

### Step 9.2 — Breadcrumb Trail from DOM Traversal

Add an element `<div id="breadcrumb"></div>` to your HTML. Write a function `buildBreadcrumb(element)` that walks from `element` up to the `<body>` using `parentElement`, collecting each ancestor's tag name and `id` (if present), then renders the trail into `#breadcrumb`:

```javascript
function buildBreadcrumb(element) {
  const trail = [];
  let current = element;

  while (current && current !== document.body.parentElement) {
    const label = current.id
      ? `${current.tagName.toLowerCase()}#${current.id}`
      : current.tagName.toLowerCase();
    trail.unshift(label);
    current = current.parentElement;
  }

  const breadcrumb = document.getElementById('breadcrumb');
  breadcrumb.textContent = trail.join(' > ');
}
```

Call `buildBreadcrumb` on several deeply nested elements (click handlers on your existing elements work well). Observe the path update in `#breadcrumb`. Confirm the output for an `<li>` inside a `<ul id="list">` inside a `<section id="main">` produces something like `html > body > section#main > ul#list > li`.

### Step 9.3 — Class-Based State Machine

Create a small state machine for a UI component that cycles through three visual states: `default` → `loading` → `success` → `default`. Each state should be represented entirely by CSS classes (no inline styles).

Add these CSS rules to your `<style>` tag:

```css
.state-default  { background: #eee; color: #333; }
.state-loading  { background: #ffd700; color: #333; }
.state-success  { background: #28a745; color: #fff; }
```

Write a `StateMachine` factory function:

```javascript
function StateMachine(element, states) {
  let currentIndex = 0;

  function applyState() {
    // Remove all state classes, then add the current one
    states.forEach(s => element.classList.remove(s));
    element.classList.add(states[currentIndex]);
  }

  applyState();

  return {
    next() {
      currentIndex = (currentIndex + 1) % states.length;
      applyState();
    },
    current() {
      return states[currentIndex];
    }
  };
}
```

Attach it to a `<button id="stateBtn">` in your HTML:

```javascript
const btn = document.getElementById('stateBtn');
const machine = StateMachine(btn, ['state-default', 'state-loading', 'state-success']);

btn.addEventListener('click', () => {
  machine.next();
  console.log('Current state:', machine.current());
});
```

Click the button three times and confirm the button cycles through all three visual states and returns to `state-default` on the fourth click.

---

## Lab Completion Checklist

- [ ] `getElementById` and `querySelector('#id')` return the same element object
- [ ] `querySelectorAll` returns a NodeList; `Array.from()` converts it
- [ ] Accessing a property of `null` throws a TypeError — null check confirmed
- [ ] `textContent` displays HTML tags as visible characters (not parsed)
- [ ] `innerHTML` renders HTML tags — `<strong>` appears bold
- [ ] `textContent` does not execute injected scripts; `innerHTML` could
- [ ] `setAttribute` / `getAttribute` / `hasAttribute` / `removeAttribute` all tested
- [ ] `data-*` attributes accessed via `.dataset`
- [ ] `classList.add` does not overwrite other classes; `className =` does
- [ ] Dark mode toggle works with `classList.toggle`
- [ ] Card selection works with `classList.toggle` and `querySelectorAll('.card.selected')`
- [ ] `firstElementChild`, `lastElementChild`, `nextElementSibling`, `previousElementSibling` tested
- [ ] Scoped `querySelector` on an element (not `document`) tested
- [ ] List item inspector works for all four items with correct sibling values
- [ ] Reflection questions answered
