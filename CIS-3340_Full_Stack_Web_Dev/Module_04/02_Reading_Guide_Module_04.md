# Reading Guide: Module 04 - JavaScript DOM Manipulation

**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers the Document Object Model API — the programming interface that lets JavaScript read and modify the HTML structure, content, and styles of a live page. You will learn query methods, property manipulation, event listeners, event propagation, creating and removing elements, event delegation, and the `DOMContentLoaded` event. These skills are prerequisites for Module 05 (async JavaScript and Fetch), Module 11 (React), and Module 15 (WebSockets).

---

## 1. The Document Object Model

When a browser loads an HTML document, it parses the markup and constructs an in-memory tree called the DOM. Each HTML element becomes a node object with properties and methods. JavaScript interacts with this tree through the `document` global object.

```text
document
 └── html
      ├── head
      │    ├── title
      │    └── meta
      └── body
           ├── header
           │    └── h1
           ├── main
           │    ├── article
           │    └── aside
           └── footer
```

Key node types:

| Type | Description | Example |
|---|---|---|
| Element node | Represents an HTML tag | `<div>`, `<p>`, `<button>` |
| Text node | Text content inside an element | `"Hello world"` |
| Attribute node | HTML attribute on an element | `href`, `class`, `id` |
| Document node | The root of the tree | `document` |

---

## 2. DOM Query Methods

```javascript
// getElementById — most performant for single ID lookups
const hero = document.getElementById('hero-section');

// querySelector — first match, any CSS selector
const btn      = document.querySelector('#submit-btn');
const firstNav = document.querySelector('nav a');
const active   = document.querySelector('.card.active');

// querySelectorAll — all matches, returns NodeList
const cards    = document.querySelectorAll('.card');
const inputs   = document.querySelectorAll('input[type="text"]');

// Iterating NodeList
cards.forEach(card => console.log(card.id));

// Convert NodeList to Array for full Array methods
const cardArray = Array.from(cards);
const titles    = cardArray.map(card => card.querySelector('h4').textContent);

// Query within an element (scoped query)
const article = document.querySelector('article');
const heading = article.querySelector('h2'); // only searches inside article
```

---

## 3. Reading and Writing DOM Properties

```javascript
const el = document.querySelector('.card');

// Text content — safe, treats all content as literal text
el.textContent = 'Updated text';              // write
const text = el.textContent;                  // read

// innerHTML — parses HTML markup; never use with unsanitized user input
el.innerHTML = '<strong>Bold</strong> text';  // write
const html = el.innerHTML;                    // read

// Attributes
el.getAttribute('data-id');                   // read any attribute
el.setAttribute('data-status', 'active');     // set any attribute
el.removeAttribute('data-status');            // remove
el.hasAttribute('hidden');                    // boolean check

// Dataset (data-* attributes via JS property names)
el.dataset.id       = '42';                   // sets data-id="42"
console.log(el.dataset.category);            // reads data-category

// classList API
el.classList.add('selected');
el.classList.remove('selected');
el.classList.toggle('selected');              // add if absent, remove if present
el.classList.contains('selected');           // returns boolean
el.classList.replace('old-class', 'new-class');

// Inline styles (camelCase property names)
el.style.backgroundColor = '#f0f4ff';
el.style.fontSize        = '1.125rem';
el.style.display         = 'none';
el.style.display         = '';               // restore default (remove inline style)
```

---

## 4. Creating and Modifying Elements

```javascript
// Create a new element
const newCard = document.createElement('div');
newCard.className = 'card';
newCard.dataset.id = '5';
newCard.innerHTML = `
  <h4>New Program</h4>
  <p>Description text here.</p>
`;

// Append to a parent
const grid = document.querySelector('.card-grid');
grid.appendChild(newCard);     // adds at the end
grid.prepend(newCard);         // adds at the beginning

// Insert adjacent to a reference element
const ref = document.querySelector('.card:nth-child(2)');
ref.insertAdjacentElement('beforebegin', newCard); // before ref
ref.insertAdjacentElement('afterend', newCard);    // after ref

// insertAdjacentHTML — insert HTML string at a position
grid.insertAdjacentHTML('beforeend', '<div class="card"><h4>Quick Add</h4></div>');

// Clone an existing element
const clone = newCard.cloneNode(true); // deep clone (true = include children)

// Remove an element
newCard.remove();

// Replace an element
const old = document.querySelector('.card.outdated');
grid.replaceChild(newCard, old);
```

---

## 5. Event Listeners and the Event Object

```javascript
const btn = document.querySelector('#action-btn');

// addEventListener signature: (eventType, handler, options)
btn.addEventListener('click', handleClick);
btn.removeEventListener('click', handleClick); // must pass same reference

function handleClick(event) {
  event.preventDefault();     // cancel default browser action
  event.stopPropagation();    // stop bubbling to parent elements

  console.log(event.type);         // 'click'
  console.log(event.target);       // element that was clicked
  console.log(event.currentTarget);// element the listener is on
  console.log(event.clientX, event.clientY); // mouse coordinates
}

// once option — fires once then automatically removes itself
btn.addEventListener('click', handleClick, { once: true });

// capture option — handle event during capture phase (before bubbling)
document.addEventListener('click', handler, { capture: true });
```

Common event types:

| Category | Events |
|---|---|
| Mouse | `click`, `dblclick`, `mouseenter`, `mouseleave`, `mousemove` |
| Keyboard | `keydown`, `keyup`, `keypress` (deprecated) |
| Form | `submit`, `input`, `change`, `focus`, `blur`, `reset` |
| Document | `DOMContentLoaded`, `load`, `resize`, `scroll` |
| Drag | `dragstart`, `dragend`, `dragover`, `drop` |

---

## 6. Event Propagation and Event Delegation

### Propagation Phases

When an event fires on an element, it travels through three phases:

1. Capture phase — event travels from `document` down to the target
2. Target phase — event fires on the target element
3. Bubble phase — event travels back up from the target through ancestors

By default, `addEventListener` registers handlers in the bubble phase.

```javascript
// This logs in order: button → div → body → html → document
document.addEventListener('click', e => console.log('document'));
document.body.addEventListener('click', e => console.log('body'));
document.querySelector('div').addEventListener('click', e => console.log('div'));
document.querySelector('button').addEventListener('click', e => console.log('button'));
// Click the button: logs button, div, body, document
```

### Event Delegation

Attach one listener to a parent instead of many listeners to each child. Uses event bubbling.

```javascript
// INEFFICIENT: 200 listeners for 200 rows
document.querySelectorAll('tr').forEach(row => {
  row.addEventListener('click', handleRowClick);
});

// EFFICIENT: one listener on the table, check target
const table = document.querySelector('tbody');
table.addEventListener('click', function(event) {
  const row = event.target.closest('tr');
  if (row) handleRowClick(row);
});
```

Event delegation benefits:

- One listener in memory instead of N listeners
- Automatically handles dynamically added rows (no re-registration)
- Easier to remove — remove one listener, not N

---

## 7. DOMContentLoaded and Script Placement

```javascript
// Safe pattern: wait for DOM to be fully parsed before querying
document.addEventListener('DOMContentLoaded', function() {
  const btn = document.querySelector('#my-btn');
  btn.addEventListener('click', handleClick);
});
```

Script placement alternatives:

```html
<!-- Option 1: Place script at end of <body> — DOM parsed before script runs -->
<body>
  <!-- content -->
  <script src="app.js"></script>
</body>

<!-- Option 2: defer — downloads in parallel, executes after DOM parsing -->
<head>
  <script src="app.js" defer></script>
</head>

<!-- Option 3: async — downloads in parallel, executes immediately when ready -->
<!-- async does not guarantee execution order for multiple scripts -->
<head>
  <script src="app.js" async></script>
</head>
```

---

## 8. localStorage — Persisting State Between Sessions

```javascript
// Store a value
localStorage.setItem('theme', 'dark');
localStorage.setItem('searchQuery', JSON.stringify({ term: 'security', date: Date.now() }));

// Read a value
const theme = localStorage.getItem('theme');                 // 'dark'
const query = JSON.parse(localStorage.getItem('searchQuery'));

// Remove a value
localStorage.removeItem('theme');

// Clear all values
localStorage.clear();

// Persist dark mode preference
const toggleBtn = document.querySelector('#theme-toggle');
toggleBtn.addEventListener('click', function() {
  document.body.classList.toggle('dark-mode');
  const isDark = document.body.classList.contains('dark-mode');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

// Restore on page load
document.addEventListener('DOMContentLoaded', function() {
  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
  }
});
```

---

## 9. Exam and Interview Tips

1. `querySelector` returns the first match or `null`. `querySelectorAll` returns all matches as a NodeList. Never confuse them — calling `.forEach()` on the `null` return of `querySelector` throws a TypeError.

2. `event.preventDefault()` stops the browser's default behavior (form submission, link navigation). `event.stopPropagation()` stops the event from bubbling to parent elements. They are independent — calling one does not imply the other.

3. `textContent` is always safe to write user-supplied data to — it treats all input as literal text and does not parse HTML. `innerHTML` parses HTML — never use it with user-supplied content without sanitization.

4. Event delegation is the standard pattern for dynamic lists. One listener on the parent handles all children, including dynamically added ones. Use `event.target.closest('.selector')` to identify which child was clicked.

5. `DOMContentLoaded` fires when HTML is fully parsed. `window.load` fires after all resources (images, stylesheets) have loaded. Use `DOMContentLoaded` for initialization code.

6. In the DVA-C02 exam: when a question asks how a React app deployed on S3 updates the page after fetching data from API Gateway, the answer involves the Virtual DOM (React's abstraction over the raw DOM API) — but understanding the raw DOM makes this concept clear.

7. `localStorage` stores strings only. Always use `JSON.stringify()` before storing objects and `JSON.parse()` after reading them.

8. The `closest()` method traverses up the DOM tree from the target element, returning the first ancestor that matches a given CSS selector. It is the correct tool in event delegation handlers.

---

## 10. Study Checklist

- [ ] Know all four DOM query methods and when to use each
- [ ] Be able to read and write `textContent`, `innerHTML`, attributes, `classList`, and inline styles
- [ ] Write an `addEventListener` for click, input, keydown, and submit events
- [ ] Understand the difference between `event.target` and `event.currentTarget`
- [ ] Understand `event.preventDefault()` vs. `event.stopPropagation()`
- [ ] Explain event bubbling and draw the propagation order for a nested click
- [ ] Implement event delegation for a dynamic list
- [ ] Build a DOM element with `createElement` and `innerHTML` from a data object
- [ ] Persist user preferences with `localStorage`
- [ ] Complete Lab 04 and Discussion 04 before the module deadline

---

## 11. Supplemental Resources

The following free, open-access resources go deeper on Module 04 topics:

**1. MDN Web Docs — Introduction to the DOM**
[https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
The authoritative reference for the DOM API, covering the node tree, query methods, event interfaces, and the relationship between HTML markup and the in-memory object model.

**2. MDN Web Docs — EventTarget.addEventListener()**
[https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
Full documentation for `addEventListener` including the options object (`once`, `capture`, `passive`), event bubbling and capturing phases, and the complete list of event types.

**3. javascript.info — Document and events**
[https://javascript.info/document](https://javascript.info/document)
A free, interactive course section covering DOM navigation, element manipulation, event delegation, and bubbling with live code examples and exercises — directly complementing the Lab 04 accordion and search filter tasks.

**4. web.dev — Storage for the web**
[https://web.dev/articles/storage-for-the-web](https://web.dev/articles/storage-for-the-web)
Google's guide comparing `localStorage`, `sessionStorage`, IndexedDB, and Cache API — including storage limits, eviction policies, and best practices relevant to the dark mode persistence feature in Lab 04.
