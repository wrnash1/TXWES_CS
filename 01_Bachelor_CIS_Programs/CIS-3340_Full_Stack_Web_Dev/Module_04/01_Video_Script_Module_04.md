# Video Script: Module 04 - JavaScript DOM Manipulation

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 24 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with JavaScript file open; Chrome with DevTools Console panel visible
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for Chrome
- Keep DevTools Console panel open throughout all live coding demos
- Show `console.log()` output in real time as code executes

---

## Section 1: Introduction - JavaScript and the DOM [00:00 - 04:00]

Welcome to Module 04. I am Professor Nash. In the first three modules we built structured, styled, and responsive HTML pages. Starting today, we make those pages respond to user interactions with JavaScript.

This module focuses on DOM manipulation — the foundation of all client-side JavaScript. Before React, before Vue, before any framework, there is the DOM API. Every JavaScript framework is an abstraction on top of this API. Understanding the raw DOM makes you a better framework developer because you understand what is happening underneath.

DOM stands for Document Object Model. When a browser loads an HTML file, it parses the markup and builds an in-memory tree of node objects — one object per HTML element. JavaScript can read and modify this tree at runtime, changing what users see without reloading the page.

**AWS Exam Tip:** DVA-C02 questions about front-end behavior focus on the interaction patterns between client-side JavaScript and AWS backend services. The JavaScript that makes `fetch()` calls to API Gateway, processes the response, and updates the DOM is exactly what you are building this week. Understanding DOM update patterns helps you design better API response formats.

[SHOW BROWSER]

Let me open a blank HTML file in Chrome and demonstrate the DOM tree in DevTools.

---

## Section 2: Querying the DOM [04:00 - 09:00]

[SHOW CODE]

The four query methods you will use in every project:

```javascript
// Select by ID — returns one element or null
const title = document.getElementById('page-title');
console.log(title.textContent);

// Select by CSS selector — returns the FIRST match or null
const firstCard = document.querySelector('.card');
const submitBtn = document.querySelector('#submit-btn');
const navLink   = document.querySelector('nav a');

// Select ALL matches — returns a static NodeList
const allCards = document.querySelectorAll('.card');
const allLinks = document.querySelectorAll('nav a');

// Iterate with forEach
allCards.forEach(function(card) {
  console.log(card.textContent);
});

// Arrow function syntax (same result)
allCards.forEach(card => console.log(card.textContent));
```

[SHOW BROWSER]

In the DevTools Console, type `document.querySelectorAll('.card')`. The console shows the NodeList. Now iterate it with `forEach` and observe each card's text content logged.

[SHOW CODE]

Reading and writing DOM properties:

```javascript
const heading = document.querySelector('h1');

// Text content — safe, no HTML parsing
heading.textContent = 'Welcome to Full Stack Development';

// innerHTML — parses HTML; never use with raw user input
const card = document.querySelector('.card');
card.innerHTML = '<strong>Updated</strong> content';

// Attributes
const link = document.querySelector('a');
console.log(link.getAttribute('href'));
link.setAttribute('href', 'https://txwes.edu');
link.removeAttribute('target');

// classList API
heading.classList.add('highlight');
heading.classList.remove('highlight');
heading.classList.toggle('active');
const isActive = heading.classList.contains('active'); // true or false

// Inline styles
card.style.backgroundColor = '#f0f4ff';
card.style.borderRadius    = '8px';
```

---

## Section 3: Event Listeners [09:00 - 14:30]

[SHOW CODE]

Events are how users communicate with the page. `addEventListener` registers a callback that executes when the event fires:

```javascript
const btn = document.querySelector('#submit-btn');

btn.addEventListener('click', function(event) {
  console.log('Button clicked!');
  console.log('Target:', event.target);
  console.log('Type:',   event.type);
});

// Arrow function
btn.addEventListener('click', (event) => {
  event.preventDefault(); // stop default behavior
});

// Mouse events
const card = document.querySelector('.card');
card.addEventListener('mouseenter', () => card.classList.add('hovered'));
card.addEventListener('mouseleave', () => card.classList.remove('hovered'));

// Keyboard events
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeModal();
  if (event.ctrlKey && event.key === 's') {
    event.preventDefault();
    saveDocument();
  }
});

// Form submit — prevent default browser submission
const form = document.querySelector('#search-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();
  const query = document.querySelector('#search-input').value;
  console.log('Searching for:', query);
});
```

Event propagation — click on `<button>` inside `<div>`:

```javascript
const container = document.querySelector('.card-grid');
const btn       = document.querySelector('.card button');

// Bubbling: fires on button first, then bubbles up to container
container.addEventListener('click', e => console.log('Grid clicked'));
btn.addEventListener('click', e => {
  console.log('Button clicked');
  e.stopPropagation(); // prevents bubble to container
});
```

---

## Section 4: Creating, Updating, and Removing DOM Elements [14:30 - 19:30]

[SHOW CODE]

Dynamic content — building DOM nodes from data:

```javascript
// Create a card element from data
function createCard(program) {
  const card = document.createElement('div');
  card.className = 'card';
  card.dataset.id = program.id;  // data-id attribute
  card.innerHTML = `
    <h4>${program.title}</h4>
    <p>${program.description}</p>
    <button class="btn-details">Learn More</button>
  `;
  return card;
}

// Append to grid
const programs = [
  { id: 1, title: 'BS Computer Science', description: 'Four-year CS program.' },
  { id: 2, title: 'MS Data Analytics', description: 'Graduate analytics program.' }
];

const grid = document.querySelector('.card-grid');
programs.forEach(program => grid.appendChild(createCard(program)));

// Remove an element
const stale = document.querySelector('.card[data-id="1"]');
if (stale) stale.remove();
```

Event delegation — the performance-correct pattern for dynamic lists:

```javascript
// AVOID: attaching one listener per item
document.querySelectorAll('.card button').forEach(btn => {
  btn.addEventListener('click', handleDetails);
});

// PREFER: one listener on the parent, check event.target
const grid = document.querySelector('.card-grid');
grid.addEventListener('click', function(event) {
  const btn = event.target.closest('.btn-details');
  if (!btn) return;
  const card = btn.closest('.card');
  const id   = card.dataset.id;
  console.log('Details requested for card:', id);
});
```

**AWS Exam Tip:** In Lambda functions that generate HTML responses, you often build DOM-like string templates server-side. Understanding how `innerHTML` and `textContent` differ helps you write safer templates. Never concatenate unsanitized user input into `innerHTML` — this is the root cause of stored XSS vulnerabilities in applications deployed at any scale.

---

## Section 5: Lab Preview — Searchable Card List [19:30 - 24:00]

[SHOW CODE]

The complete interactive component we will build in the lab:

```javascript
document.addEventListener('DOMContentLoaded', function () {

  const searchInput = document.querySelector('#search-input');
  const cards       = document.querySelectorAll('.card');
  const counter     = document.querySelector('#result-count');

  function filterCards(query) {
    let visible = 0;
    query = query.toLowerCase().trim();

    cards.forEach(function (card) {
      const title = card.querySelector('h4').textContent.toLowerCase();
      const body  = card.querySelector('p').textContent.toLowerCase();
      const match = title.includes(query) || body.includes(query);

      card.style.display = match ? '' : 'none';
      if (match) visible++;
    });

    counter.textContent = `${visible} program${visible !== 1 ? 's' : ''} found`;
  }

  searchInput.addEventListener('input', function () {
    filterCards(this.value);
  });

  searchInput.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      this.value = '';
      filterCards('');
    }
  });

  filterCards(''); // initial count
});
```

[SHOW BROWSER]

Watch as I type "security" — only the cybersecurity card remains visible. Type "data" — the data analytics card appears. Press Escape — everything resets. This is pure DOM manipulation: no libraries, no network calls, no frameworks.

In the lab you will also implement a dark mode toggle that persists to `localStorage`, and an accordion component for the FAQ section. Both are built using the same `addEventListener` and `classList.toggle` patterns.

Thank you for watching. See you in Module 05 where we go asynchronous with Promises, async/await, and the Fetch API.

---

## Additional Resources

- developer.mozilla.org — search "DOM manipulation guide" and "EventTarget addEventListener" for comprehensive API reference
- aws.amazon.com/certification — review Lambda and API Gateway scenarios that involve client-side JavaScript consuming REST APIs
