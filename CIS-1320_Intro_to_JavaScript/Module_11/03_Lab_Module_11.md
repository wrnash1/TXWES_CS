# Lab Activity: Module 11 — DOM Manipulation and Styling

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Lab Overview

This lab moves from reading the DOM to building it. You will create elements, insert them at precise positions, remove and replace them, clone structures, and build a complete data-driven product grid. All work runs in the browser.

**Environment:** VS Code + Live Server extension + Chrome or Firefox DevTools

---

## Setup

Create a project folder called `module11_lab`. Inside it, create the following files:

**`index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 11 Lab</title>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
    h1, h2 { color: #333; }
    ul { padding-left: 1.5rem; }
    li { margin: 0.25rem 0; }
    .highlight { background-color: #fffbcc; }
    .hidden { display: none; }
    .notice { background: #e8f4fb; border: 1px solid #90cce8; padding: 0.75rem 1rem; border-radius: 4px; margin: 0.5rem 0; }
    .card { border: 1px solid #ccc; padding: 1rem; margin: 0.5rem 0; border-radius: 6px; }
    .card h3 { margin: 0 0 0.5rem; }
    .card p  { margin: 0 0 0.5rem; color: #555; }
    .badge { display: inline-block; padding: 0.2rem 0.5rem; border-radius: 3px; font-size: 0.85rem; }
    .badge-green { background: #d4edda; color: #155724; }
    .badge-red   { background: #f8d7da; color: #721c24; }
    #product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem; }
    #status { color: #555; font-style: italic; margin-top: 1rem; }
    button { padding: 0.4rem 0.8rem; margin: 0.25rem; cursor: pointer; }
  </style>
</head>
<body>
  <h1>Module 11: DOM Manipulation</h1>

  <h2>Part 1 — Creating and Inserting</h2>
  <ul id="fruit-list">
    <li>Banana</li>
    <li>Cherry</li>
    <li>Date</li>
  </ul>
  <div id="insert-target" class="notice">This is the insert target div.</div>

  <h2>Part 2 — Removing and Replacing</h2>
  <ul id="task-list">
    <li class="task">Buy groceries</li>
    <li class="task expired">Old task — expired</li>
    <li class="task">Call dentist</li>
    <li class="task expired">Another expired task</li>
    <li class="task">Walk the dog</li>
  </ul>
  <div id="replace-target" class="card">
    <h3>Original Card</h3>
    <p>This card will be replaced.</p>
  </div>

  <h2>Part 3 — Cloning</h2>
  <div id="card-template" class="card hidden">
    <h3 class="card-name">Template Name</h3>
    <p class="card-desc">Template description.</p>
  </div>
  <div id="clone-container"></div>

  <h2>Part 4 — Product Grid</h2>
  <div>
    <button id="btn-all">Show All</button>
    <button id="btn-in-stock">In Stock Only</button>
    <button id="btn-sort-price">Sort by Price</button>
  </div>
  <div id="product-grid"></div>

  <div id="status"></div>

  <script src="lab11.js"></script>
</body>
</html>
```

**`lab11.js`** — start empty. Add code section by section.

Open with Live Server. Confirm the page loads. Open DevTools Console.

---

## Part 1 — Creating and Inserting Elements

**Learning objectives:** Use `createElement`, `appendChild`, `prepend`, `insertBefore`, `insertAdjacentHTML`.

### Section 1.1 — `createElement` and `appendChild`

```javascript
// --- Part 1: Creating and Inserting ---

// 1.1 — createElement + configure + appendChild
const list = document.getElementById('fruit-list');

const newItem = document.createElement('li');
newItem.textContent = 'Elderberry';
newItem.classList.add('highlight');

list.appendChild(newItem);   // appended as last child
console.log('List item count after append:', list.children.length);   // 4
```

Save. Confirm 'Elderberry' appears at the bottom of the fruit list.

### Section 1.2 — `prepend`

```javascript
// 1.2 — prepend — inserts as first child
const apple = document.createElement('li');
apple.textContent = 'Apple';
list.prepend(apple);
console.log('First item:', list.firstElementChild.textContent);   // 'Apple'
```

Save. Confirm 'Apple' appears at the top.

### Section 1.3 — `insertBefore`

```javascript
// 1.3 — insertBefore — insert at a specific position
const fig = document.createElement('li');
fig.textContent = 'Fig';

// Insert before 'Cherry' (now at index 2 after prepend)
const cherry = list.children[2];   // 'Cherry' is the 3rd item now (Apple, Banana, Cherry...)
list.insertBefore(fig, cherry);
console.log('Item before Cherry:', cherry.previousElementSibling.textContent);   // 'Fig'
```

### Section 1.4 — Building Nested Structures

```javascript
// 1.4 — Build a nested structure before inserting
const section = document.createElement('section');

const heading = document.createElement('h3');
heading.textContent = 'Dynamic Section';

const para = document.createElement('p');
para.textContent = 'This entire section was built in JavaScript.';

section.appendChild(heading);
section.appendChild(para);

// Insert after the fruit list heading
document.querySelector('#fruit-list').before(section);
// .before() is modern shorthand — inserts as a previous sibling
```

### Section 1.5 — `insertAdjacentHTML`

```javascript
// 1.5 — insertAdjacentHTML with four positions
const target = document.getElementById('insert-target');

target.insertAdjacentHTML('beforebegin', '<p><em>beforebegin: just before the div</em></p>');
target.insertAdjacentHTML('afterbegin',  '<strong>afterbegin: first inside the div. </strong>');
target.insertAdjacentHTML('beforeend',   ' <strong>beforeend: last inside the div.</strong>');
target.insertAdjacentHTML('afterend',    '<p><em>afterend: just after the div</em></p>');

console.log('Insert target innerHTML:', target.innerHTML);
```

Save. Inspect the insert target area and confirm the four pieces of content appear in the correct positions relative to the div.

---

## Part 2 — Removing and Replacing Elements

**Learning objectives:** Use `element.remove()`, `removeChild`, conditional removal, `innerHTML = ''` to clear, `replaceWith`.

### Section 2.1 — `element.remove()`

```javascript
// --- Part 2: Removing and Replacing ---

// 2.1 — remove() — modern API, no parent needed
const taskList = document.getElementById('task-list');
const firstTask = taskList.firstElementChild;

console.log('Removing:', firstTask.textContent);   // 'Buy groceries'
firstTask.remove();
console.log('First task after remove:', taskList.firstElementChild.textContent);
```

### Section 2.2 — `removeChild`

```javascript
// 2.2 — removeChild — older API, requires parent reference
const lastTask = taskList.lastElementChild;
const removed = taskList.removeChild(lastTask);
console.log('Removed via removeChild:', removed.textContent);   // 'Walk the dog'
// Note: removeChild returns the removed node
```

### Section 2.3 — Remove by Condition

```javascript
// 2.3 — Remove all elements matching a condition
// Remove all tasks with class 'expired'
const expiredTasks = taskList.querySelectorAll('.expired');
console.log('Expired tasks to remove:', expiredTasks.length);

expiredTasks.forEach(task => task.remove());

console.log('Tasks remaining:', taskList.children.length);
```

Save. Confirm the two expired tasks are removed. Verify the remaining task ('Call dentist') is still present.

### Section 2.4 — Emptying a Container

```javascript
// 2.4 — Clear all children from a container
console.log('Task list children before clear:', taskList.children.length);

taskList.innerHTML = '';

console.log('Task list children after clear:', taskList.children.length);   // 0
```

### Section 2.5 — `replaceWith`

```javascript
// 2.5 — replaceWith — replace an element with a new one
const oldCard = document.getElementById('replace-target');

const newCard = document.createElement('div');
newCard.classList.add('card');
newCard.innerHTML = '<h3>Replacement Card</h3><p>The original card has been replaced.</p>';
// Safe here because no user data — markup is hardcoded by us

oldCard.replaceWith(newCard);
console.log('Replace-target card text:', newCard.querySelector('h3').textContent);
```

---

## Part 3 — Cloning Nodes

**Learning objectives:** Use `cloneNode(true)` to generate repeated UI from a template; observe that event listeners do not clone.

### Section 3.1 — `cloneNode` Basics

```javascript
// --- Part 3: Cloning ---

// 3.1 — cloneNode(false) — shallow: element only, no children
const template = document.getElementById('card-template');
const shallow = template.cloneNode(false);
console.log('Shallow clone children:', shallow.children.length);   // 0

// 3.2 — cloneNode(true) — deep: full subtree
const deep = template.cloneNode(true);
console.log('Deep clone children:', deep.children.length);   // 2 (h3 and p)
console.log('Deep clone name text:', deep.querySelector('.card-name').textContent);
// 'Template Name'
```

### Section 3.2 — Event Listeners Are Not Cloned

```javascript
// 3.3 — Prove event listeners don't clone
template.addEventListener('click', () => {
  console.log('Template clicked');
});

const cloneForTest = template.cloneNode(true);
cloneForTest.id = 'clone-test';
cloneForTest.classList.remove('hidden');
cloneForTest.querySelector('.card-name').textContent = 'Click Test Card';
document.getElementById('clone-container').appendChild(cloneForTest);

// Click the visible "Click Test Card" card in the browser.
// The console will NOT log 'Template clicked' — the listener did not clone.
```

### Section 3.3 — Rendering Cards from Data Using `cloneNode`

```javascript
// 3.4 — Render multiple cards from an array using the template
const teamMembers = [
  { name: 'Alice',   desc: 'Frontend Developer' },
  { name: 'Bob',     desc: 'Backend Developer' },
  { name: 'Carol',   desc: 'UX Designer' }
];

const container = document.getElementById('clone-container');

teamMembers.forEach(member => {
  const card = template.cloneNode(true);
  card.removeAttribute('id');                                    // remove template id
  card.querySelector('.card-name').textContent = member.name;
  card.querySelector('.card-desc').textContent = member.desc;
  card.classList.remove('hidden');
  container.appendChild(card);
});

console.log('Cards rendered:', container.children.length);   // 4 (3 members + the click test card)
```

Save. Confirm three member cards appear below the click test card.

---

## Part 4 — Product Grid Integration

**Learning objectives:** Build a data-driven grid renderer; combine `createElement`, `textContent`, `classList`, `dataset`, and filtering/sorting with re-render.

### Section 4.1 — Product Data

```javascript
// --- Part 4: Product Grid ---

const products = [
  { id: 1, name: 'Widget Pro',    price: 29.99, inStock: true,  category: 'Tools' },
  { id: 2, name: 'Gadget Lite',   price: 14.99, inStock: false, category: 'Electronics' },
  { id: 3, name: 'Super Tool',    price: 49.99, inStock: true,  category: 'Tools' },
  { id: 4, name: 'Nano Device',   price: 79.99, inStock: true,  category: 'Electronics' },
  { id: 5, name: 'Mini Gadget',   price: 9.99,  inStock: false, category: 'Electronics' },
  { id: 6, name: 'Power Widget',  price: 34.99, inStock: true,  category: 'Tools' }
];
```

### Section 4.2 — Renderer Using `createElement`

```javascript
// 4.2 — Render function using createElement (safe for any data)
function renderProducts(data) {
  const grid = document.getElementById('product-grid');
  grid.innerHTML = '';   // clear before render

  if (data.length === 0) {
    const msg = document.createElement('p');
    msg.textContent = 'No products match the current filter.';
    grid.appendChild(msg);
    updateStatus(`0 products displayed`);
    return;
  }

  data.forEach(product => {
    // Card wrapper
    const card = document.createElement('div');
    card.classList.add('card');
    card.dataset.id = product.id;

    // Name heading
    const name = document.createElement('h3');
    name.textContent = product.name;

    // Price paragraph
    const price = document.createElement('p');
    price.textContent = `$${product.price.toFixed(2)}`;

    // Category
    const category = document.createElement('p');
    category.textContent = product.category;
    category.style.color = '#888';
    category.style.fontSize = '0.85rem';

    // Stock badge
    const badge = document.createElement('span');
    badge.classList.add('badge', product.inStock ? 'badge-green' : 'badge-red');
    badge.textContent = product.inStock ? 'In Stock' : 'Out of Stock';

    // Assemble card
    card.appendChild(name);
    card.appendChild(price);
    card.appendChild(category);
    card.appendChild(badge);

    grid.appendChild(card);
  });

  updateStatus(`${data.length} product(s) displayed`);
}

function updateStatus(message) {
  document.getElementById('status').textContent = message;
}

// Initial render
renderProducts(products);
```

Save. Confirm six product cards appear in the grid.

### Section 4.3 — Filter and Sort Controls

```javascript
// 4.3 — Filter and sort buttons
document.getElementById('btn-all').addEventListener('click', () => {
  renderProducts(products);
});

document.getElementById('btn-in-stock').addEventListener('click', () => {
  const inStock = products.filter(p => p.inStock);
  renderProducts(inStock);
});

document.getElementById('btn-sort-price').addEventListener('click', () => {
  const sorted = [...products].sort((a, b) => a.price - b.price);
  renderProducts(sorted);
});
```

Save. Test each button:

- "Show All" renders all 6 products
- "In Stock Only" renders 4 products (the two out-of-stock are filtered out)
- "Sort by Price" renders 6 products ordered lowest to highest price

### Section 4.4 — Clicking a Card Highlights It

```javascript
// 4.4 — Add click-to-highlight to the grid (event delegation — Module 12 preview)
document.getElementById('product-grid').addEventListener('click', (event) => {
  const card = event.target.closest('.card');
  if (!card) return;

  // Deselect all cards, select clicked card
  document.querySelectorAll('#product-grid .card').forEach(c => {
    c.classList.remove('highlight');
  });
  card.classList.add('highlight');

  const id = parseInt(card.dataset.id);
  const product = products.find(p => p.id === id);
  updateStatus(`Selected: ${product.name} — $${product.price.toFixed(2)}`);
});
```

Save. Click any product card. It should highlight and the status bar should display the product name and price.

---

## Lab Completion Checklist

- [ ] `createElement` + `textContent` + `classList` + `appendChild` pipeline confirmed
- [ ] `prepend` inserts before all existing children
- [ ] `insertBefore` inserts before a specific reference node
- [ ] All four `insertAdjacentHTML` positions produce content in the correct location
- [ ] `element.remove()` removes without needing a parent reference
- [ ] `removeChild` removes and returns the removed node
- [ ] Conditional removal (`.expired` items) works correctly
- [ ] `innerHTML = ''` clears all children
- [ ] `replaceWith` replaces the old card with the new one
- [ ] `cloneNode(false)` produces no children; `cloneNode(true)` includes the full subtree
- [ ] Event listeners confirmed as not cloned (click test card does not trigger template listener)
- [ ] Three team member cards rendered via `cloneNode` loop
- [ ] Product grid renders all 6 products on load using `createElement`
- [ ] "In Stock Only" filter correctly shows 4 products
- [ ] "Sort by Price" orders products from lowest to highest
- [ ] Clicking a card highlights it and shows product details in the status bar
