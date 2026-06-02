# Video Script: CIS-1320 — Introduction to JavaScript

## Module 11 — DOM Manipulation and Styling

**Estimated Duration:** 18–22 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Live Server + Chrome DevTools for all [DEMO] sections. Keep the Elements panel visible while running code so students see the DOM update live.
> - [PAUSE] = 2 seconds of silence.
> - Module 10 covered selecting and reading. Module 11 covers creating, inserting, removing, and cloning — plus building from templates. The key progression: students can now build entire UI structures from data.
> - `createElement` + `appendChild` vs `insertAdjacentHTML` — both demonstrated; discuss when each is appropriate (safety vs convenience).
> - `removeChild` vs `remove()` — both shown; `remove()` is modern and simpler.
> - The `<template>` element is not JSE-required but is practical — keep the demo brief.
> - `document.createTextNode` — mention but prefer `textContent` for setting text.
> - The list builder demo (Part 4) ties together all concepts — spend time here to give students a model they can adapt.
> - `innerHTML` for building structures from static strings is acceptable in controlled code (no user data), but call out the distinction.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 11 | DOM Manipulation and Styling | CIS-1320"]**

"Module 10 taught you how to find elements and change their content. Module 11 goes further: you will learn to create brand-new elements from scratch, insert them into the page, remove them, and clone them. You will also learn to build page structures from data — taking an array of objects and generating the corresponding HTML entirely in JavaScript.

These skills are the foundation of every dynamic web application. A to-do list that adds items when you click a button, a product grid that renders from JSON fetched from a server, a comment section that appends new posts — all of these use exactly what you will learn today.

Let us start with the fundamental operation: creating a new element."

---

## [01:30 – 06:00] Part 1 — Creating and Inserting Elements

**[SHOW SLIDE: "createElement and appendChild"]**

"**[DEMO]**

```javascript
// Step 1: Create a new element
const newPara = document.createElement('p');

// Step 2: Set its content
newPara.textContent = 'This paragraph was created by JavaScript.';

// Step 3: Style it or add classes
newPara.classList.add('intro');

// Step 4: Insert it into the DOM
document.body.appendChild(newPara);
```

`document.createElement('p')` creates a new `<p>` element in memory — it exists as a JavaScript object but is not yet on the page. You set properties on it just like any existing element: `textContent`, `className`, `setAttribute`, `style`. Then `appendChild` inserts it as the last child of the target element.

[PAUSE]

Notice the four steps: **create → configure → insert**. Create and configure first, insert last. Once inserted, the browser renders it.

**[DEMO — Targeting the insertion point]**

```javascript
// Append to a specific container, not just body
const list = document.getElementById('item-list');
const newItem = document.createElement('li');
newItem.textContent = 'New Item';
list.appendChild(newItem);   // appended as the last <li>
```

[PAUSE]

**Other insertion methods — `insertBefore` and `prepend`:**

```javascript
// insertBefore(newNode, referenceNode) — inserts before the reference
const ul = document.getElementById('item-list');
const firstItem = ul.firstElementChild;
const prepended = document.createElement('li');
prepended.textContent = 'First!';
ul.insertBefore(prepended, firstItem);   // now the first <li>

// prepend — shortcut to insert as first child
ul.prepend(prepended);   // same result, simpler syntax

// append — can accept multiple nodes or strings
ul.append(newItem, 'trailing text');   // modern, flexible
```

[PAUSE]

**`insertAdjacentHTML` — insert HTML strings at specific positions:**

```javascript
const container = document.getElementById('output');

// beforebegin — before the element itself
container.insertAdjacentHTML('beforebegin', '<p>Before the container</p>');

// afterbegin — inside the element, before its first child
container.insertAdjacentHTML('afterbegin', '<p>First inside</p>');

// beforeend — inside the element, after its last child
container.insertAdjacentHTML('beforeend', '<p>Last inside</p>');

// afterend — after the element itself
container.insertAdjacentHTML('afterend', '<p>After the container</p>');
```

`insertAdjacentHTML` is convenient when you have a static HTML string to insert — for example, from a template literal. It parses the string as HTML. The same XSS warning applies: never use user-provided data in the HTML string."

---

## [06:00 – 10:00] Part 2 — Removing and Replacing Elements

**[SHOW SLIDE: "Removing and Replacing DOM Nodes"]**

"**Removing — `remove()` and `removeChild`:**

**[DEMO]**

```javascript
// Modern: element.remove() — removes the element itself
const outdatedNotice = document.getElementById('notice');
outdatedNotice.remove();   // gone from the DOM

// Older: parent.removeChild(child) — removes a child from its parent
const list = document.getElementById('item-list');
const lastItem = list.lastElementChild;
list.removeChild(lastItem);
```

`element.remove()` is the modern approach — clean and direct. `removeChild` requires a reference to the parent and the child. You will see `removeChild` in older code. Both work.

[PAUSE]

**Removing by condition — filtering elements out of the DOM:**

```javascript
const items = document.querySelectorAll('#item-list li');
items.forEach(item => {
  if (item.textContent.includes('Old')) {
    item.remove();
  }
});
```

[PAUSE]

**Replacing — `replaceWith` and `replaceChild`:**

```javascript
// Modern: element.replaceWith(newNode)
const oldHeading = document.querySelector('h2');
const newHeading = document.createElement('h2');
newHeading.textContent = 'Updated Heading';
newHeading.classList.add('active');
oldHeading.replaceWith(newHeading);

// Older: parent.replaceChild(newChild, oldChild)
const parent = document.getElementById('container');
parent.replaceChild(newHeading, oldHeading);
```

[PAUSE]

**Emptying a container:**

A common task is clearing all children from a container before re-rendering:

```javascript
// Option 1: innerHTML = '' — fast, simple
const container = document.getElementById('output');
container.innerHTML = '';

// Option 2: remove children one by one
while (container.firstChild) {
  container.removeChild(container.firstChild);
}
```

`innerHTML = ''` is the simplest and most common approach for clearing a container."

---

## [10:00 – 14:00] Part 3 — Cloning Nodes

**[SHOW SLIDE: "cloneNode"]**

"Sometimes you need to create multiple copies of an element structure. Instead of building each from scratch with `createElement`, you can clone an existing element.

**[DEMO]**

```javascript
const card = document.querySelector('.card');

// cloneNode(false) — clones the element only, not its children
const shallowClone = card.cloneNode(false);

// cloneNode(true) — deep clone: element AND all descendants
const deepClone = card.cloneNode(true);

// The clone is in memory — insert it to make it visible
deepClone.id = 'card-copy';   // IDs must be unique
document.getElementById('card-container').appendChild(deepClone);
```

`cloneNode(true)` copies the element, all its children, all their attributes, and all their text content. It does **not** copy event listeners attached via `addEventListener`.

[PAUSE]

**Practical use — rendering repeated structures from data:**

```javascript
const users = [
  { name: 'Alice', role: 'Admin' },
  { name: 'Bob',   role: 'Editor' }
];

const template = document.querySelector('.user-card');   // a hidden template element

users.forEach(user => {
  const card = template.cloneNode(true);
  card.querySelector('.user-name').textContent = user.name;
  card.querySelector('.user-role').textContent = user.role;
  card.classList.remove('hidden');
  document.getElementById('user-list').appendChild(card);
});
```

This pattern — clone, populate, insert — is the most common approach to rendering repeated UI from data without a framework."

---

## [14:00 – 18:00] Part 4 — Building Structures from Data

**[SHOW SLIDE: "Rendering Data as DOM Nodes"]**

"Let us build a complete working example. We have an array of products and we want to render them as cards on the page.

**[DEMO — the data]**

```javascript
const products = [
  { id: 1, name: 'Widget Pro', price: 29.99, inStock: true },
  { id: 2, name: 'Gadget Lite', price: 14.99, inStock: false },
  { id: 3, name: 'Super Tool',  price: 49.99, inStock: true }
];
```

**[DEMO — building with createElement]**

```javascript
function renderProducts(data) {
  const container = document.getElementById('product-grid');
  container.innerHTML = '';   // clear before re-render

  data.forEach(product => {
    // Create the card wrapper
    const card = document.createElement('div');
    card.classList.add('product-card');
    card.dataset.id = product.id;

    // Create and append the name
    const name = document.createElement('h3');
    name.textContent = product.name;
    card.appendChild(name);

    // Create and append the price
    const price = document.createElement('p');
    price.textContent = `$${product.price.toFixed(2)}`;
    card.appendChild(price);

    // Create and append the stock badge
    const badge = document.createElement('span');
    badge.textContent = product.inStock ? 'In Stock' : 'Out of Stock';
    badge.classList.add(product.inStock ? 'badge-green' : 'badge-red');
    card.appendChild(badge);

    // Insert the finished card into the container
    container.appendChild(card);
  });
}

renderProducts(products);
```

[PAUSE]

Notice the structure: for each product, we create the card container first, build all the inner elements, then append the card to the page. The entire card is configured in memory before a single insertion — this is more efficient than inserting and re-querying.

**[DEMO — building with a template literal and insertAdjacentHTML]**

For simple structures with no user-provided data, a template literal is faster to write:

```javascript
function renderProductsHTML(data) {
  const container = document.getElementById('product-grid');
  container.innerHTML = data.map(p => `
    <div class="product-card" data-id="${p.id}">
      <h3>${p.name}</h3>
      <p>$${p.price.toFixed(2)}</p>
      <span class="${p.inStock ? 'badge-green' : 'badge-red'}">
        ${p.inStock ? 'In Stock' : 'Out of Stock'}
      </span>
    </div>
  `).join('');
}
```

This is clean and readable. The warning: only use this pattern when the data is controlled — from your own code, not from user input. If `p.name` came from a user, it could contain HTML that would be injected."

---

## [18:00 – 21:00] Part 5 — `document.createTextNode` and Safe Node Construction

**[SHOW SLIDE: "Safe DOM Construction"]**

"When you need to insert text into the DOM safely — especially text from user input — the safest approach is to create a text node directly:

**[DEMO]**

```javascript
const div = document.createElement('div');

// createTextNode — always safe, never parsed as HTML
const text = document.createTextNode('<script>alert(\"XSS\")</script>');
div.appendChild(text);
// The page displays the angle brackets as literal text — no script executes
```

In practice, assigning `element.textContent = userInput` has the same safe effect and is simpler:

```javascript
const div = document.createElement('div');
div.textContent = userInput;   // equivalent safety, simpler syntax
document.body.appendChild(div);
```

Both treat the content as text, not markup. Use whichever you find more readable — `textContent` is the modern convention."

---

## [21:00 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 11 Lab Preview"]**

"The Module 11 lab has four parts.

Part 1 covers creating and inserting — you will use `createElement`, `appendChild`, `prepend`, and `insertAdjacentHTML` to add elements at specific positions.

Part 2 covers removing and replacing — you will remove individual elements, remove by condition, empty a container, and use `replaceWith`.

Part 3 covers cloning — you will use `cloneNode(true)` to build a repeated card structure from an array of data.

Part 4 is the integration — a complete product grid renderer using both `createElement` and the template literal approach, with a sort and filter feature that re-renders the list.

The quiz focuses on the `createElement`/`appendChild` pipeline, insertion positions, `remove` vs `removeChild`, `cloneNode` depth parameter, and the safety distinction between `textContent` and `innerHTML` for user data. Read the reading guide before the lab. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 11 — DOM Manipulation and Styling]**

---

## Additional Resources

- [MDN — Document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
- [MDN — Node.appendChild()](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)
- [MDN — Element.insertAdjacentHTML()](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)
- [MDN — Node.cloneNode()](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)
- [MDN — ChildNode.remove()](https://developer.mozilla.org/en-US/docs/Web/API/ChildNode/remove)
- [Eloquent JavaScript — Chapter 14: The Document Object Model](https://eloquentjavascript.net/14_dom.html)
