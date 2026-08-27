# Reading Guide: Module 11 — DOM Manipulation and Styling

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Module 10 covered reading from the DOM and modifying existing elements. Module 11 covers writing to the DOM: creating new elements, inserting them at precise positions, removing and replacing elements, and cloning structures. These operations are the engine of all dynamic web UI. A search result list that re-renders on each keystroke, a shopping cart that adds items when a button is clicked, a comment feed that appends new posts — each uses the techniques in this module.

---

## 1. Creating Elements: `document.createElement`

New elements are created in memory with `document.createElement`:

```javascript
const p = document.createElement('p');
```

The argument is the tag name as a string — `'p'`, `'div'`, `'li'`, `'span'`, `'input'`, etc. The result is a full element object with all the properties and methods you already know: `textContent`, `innerHTML`, `classList`, `setAttribute`, `style`, `dataset`.

The new element exists only in memory until you insert it into the document. It is not visible on the page until that insertion step.

### Configuring Before Inserting

Configure the element fully before inserting it. This avoids triggering multiple browser reflows:

```javascript
const card = document.createElement('div');
card.classList.add('card', 'featured');
card.dataset.id = '42';
card.textContent = 'My Card';

document.getElementById('container').appendChild(card);
```

Create and configure first. Insert once. The browser renders once.

### Building Nested Structures

Build the entire tree before inserting any of it:

```javascript
const article = document.createElement('article');

const heading = document.createElement('h2');
heading.textContent = 'Title';

const body = document.createElement('p');
body.textContent = 'Body text.';

article.appendChild(heading);   // heading is now a child of article
article.appendChild(body);      // body is now a child of article

document.body.appendChild(article);   // insert the whole tree at once
```

---

## 2. Inserting Elements

### `appendChild`

`parent.appendChild(node)` adds `node` as the **last child** of `parent`.

```javascript
const ul = document.getElementById('list');
const li = document.createElement('li');
li.textContent = 'New item';
ul.appendChild(li);   // appended at the end
```

If `node` is already in the document, `appendChild` **moves** it rather than copying it. A node can only appear once in the DOM.

### `prepend` and `append`

Modern alternatives to `appendChild`:

```javascript
ul.prepend(li);           // insert as first child
ul.append(li);            // insert as last child (same as appendChild)
ul.append(li, 'text');    // accepts multiple arguments including strings
```

### `insertBefore`

`parent.insertBefore(newNode, referenceNode)` inserts `newNode` before `referenceNode` inside `parent`:

```javascript
const ul = document.getElementById('list');
const first = ul.firstElementChild;
const newFirst = document.createElement('li');
newFirst.textContent = 'Inserted at top';
ul.insertBefore(newFirst, first);
```

To insert at the end, pass `null` as the reference node: `ul.insertBefore(node, null)` — equivalent to `appendChild`.

### `insertAdjacentHTML`

`element.insertAdjacentHTML(position, htmlString)` inserts a parsed HTML string at a specific position relative to the element:

| Position | Location |
|---|---|
| `'beforebegin'` | Before the element itself (as a previous sibling) |
| `'afterbegin'` | Inside the element, before its first child |
| `'beforeend'` | Inside the element, after its last child |
| `'afterend'` | After the element itself (as a next sibling) |

```javascript
const section = document.querySelector('section');
section.insertAdjacentHTML('beforeend', '<p>Added inside at end.</p>');
```

**Safety note:** `insertAdjacentHTML` parses the string as HTML. Never use it with user-provided content — use `insertAdjacentText` or `createElement` + `textContent` instead.

### `insertAdjacentElement` and `insertAdjacentText`

```javascript
// Insert an element node (not an HTML string)
section.insertAdjacentElement('afterend', newNode);

// Insert literal text safely (no HTML parsing)
section.insertAdjacentText('beforeend', '<script>not executed</script>');
```

---

## 3. Removing Elements

### `element.remove()`

The modern approach: call `remove()` on the element you want to delete:

```javascript
const notice = document.getElementById('notice');
notice.remove();   // removes itself from the DOM
```

### `parent.removeChild(child)`

The older approach, still common in legacy code:

```javascript
const ul = document.getElementById('list');
const lastItem = ul.lastElementChild;
ul.removeChild(lastItem);
```

`removeChild` returns the removed node — you can hold a reference to it and re-insert it elsewhere.

### Removing by Condition

```javascript
document.querySelectorAll('.item').forEach(item => {
  if (item.textContent.includes('expired')) {
    item.remove();
  }
});
```

### Emptying a Container

To clear all children before re-rendering:

```javascript
// Fastest and simplest
container.innerHTML = '';

// Alternative (useful when you need to preserve event listeners on the container)
while (container.firstChild) {
  container.removeChild(container.firstChild);
}
```

`innerHTML = ''` is the idiomatic choice for clearing a container.

---

## 4. Replacing Elements

### `element.replaceWith(...nodes)`

Modern: replaces `element` with one or more new nodes or strings:

```javascript
const old = document.querySelector('h1');
const fresh = document.createElement('h1');
fresh.textContent = 'New Heading';
old.replaceWith(fresh);
```

### `parent.replaceChild(newChild, oldChild)`

Older approach requiring a parent reference:

```javascript
const parent = document.getElementById('header');
parent.replaceChild(fresh, old);
```

---

## 5. Cloning Nodes: `cloneNode`

`element.cloneNode(deep)` creates a copy of the element:

| Argument | Effect |
|---|---|
| `cloneNode(false)` | Copies the element only — no children, no text content |
| `cloneNode(true)` | Deep clone — copies element, all descendants, all attributes, all text |

```javascript
const card = document.querySelector('.card');
const copy = card.cloneNode(true);   // deep clone

copy.id = 'card-2';   // IDs must be unique — update before inserting
document.getElementById('grid').appendChild(copy);
```

**Important:** `cloneNode` does **not** copy event listeners attached via `addEventListener`. If the original element has click listeners, the clone will not.

### Cloning as a Rendering Pattern

Clone a hidden template element to render repeated structures:

```html
<!-- A hidden template in the HTML -->
<div class="card hidden" id="card-template">
  <h3 class="card-title"></h3>
  <p class="card-body"></p>
</div>
```

```javascript
const template = document.getElementById('card-template');

const data = [
  { title: 'Alpha', body: 'First card.' },
  { title: 'Beta',  body: 'Second card.' }
];

data.forEach(item => {
  const card = template.cloneNode(true);
  card.removeAttribute('id');                           // remove template ID
  card.querySelector('.card-title').textContent = item.title;
  card.querySelector('.card-body').textContent  = item.body;
  card.classList.remove('hidden');
  document.getElementById('grid').appendChild(card);
});
```

---

## 6. Rendering Data as DOM Nodes

A common real-world task: given an array of objects, generate the corresponding DOM structure. Two approaches:

### Approach 1: `createElement` (Safe for Any Data)

```javascript
function renderList(items) {
  const ul = document.getElementById('output');
  ul.innerHTML = '';

  items.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item.name;     // textContent — never parses as HTML
    li.dataset.id = item.id;
    ul.appendChild(li);
  });
}
```

Safe regardless of what `item.name` contains. Recommended when data may include user-provided content.

### Approach 2: Template Literal + `innerHTML` (Controlled Data Only)

```javascript
function renderList(items) {
  document.getElementById('output').innerHTML = items.map(item => `
    <li data-id="${item.id}">${item.name}</li>
  `).join('');
}
```

Concise and readable. Only safe when `item.name` and `item.id` come from your own controlled data, not from user input.

### Comparison

| Approach | Safety | Verbosity | Use When |
|---|---|---|---|
| `createElement` + `textContent` | Always safe | More code | Data includes any user input |
| Template literal + `innerHTML` | Safe only for controlled data | Less code | Data is from your own code or a trusted API |

---

## 7. `document.createTextNode`

Creates a text node — the lowest-level safe way to insert text:

```javascript
const text = document.createTextNode('Hello, world!');
document.body.appendChild(text);
```

In practice, `element.textContent = 'Hello, world!'` achieves the same result with less code. Use `createTextNode` when you need to insert a text node as a sibling (not the only child) inside an element.

---

## 8. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 14: The Document Object Model](https://eloquentjavascript.net/14_dom.html)**
  The primary OER textbook chapter for this module. Covers creating and inserting nodes with `createElement` and `appendChild`, modifying the tree, removing elements, and the `createTextNode` API with worked exercises.

- **[MDN Web Docs — Document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)**
  Full reference for `createElement` including the element name string, custom element support, and a complete example showing the create-configure-insert pipeline.

- **[MDN Web Docs — Element.insertAdjacentHTML()](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)**
  Complete reference for all four `insertAdjacentHTML` position values with diagrams and runnable examples. Also covers the safer alternatives `insertAdjacentText` and `insertAdjacentElement`.

- **[MDN Web Docs — Node.cloneNode()](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)**
  Full reference for `cloneNode` explaining the `deep` parameter, what is and is not copied (notably: event listeners are not copied), and common use cases such as template-based rendering.

- **[javascript.info — Modifying the document](https://javascript.info/modifying-document)**
  Comprehensive tutorial on creating, inserting, removing, and cloning DOM nodes. Includes comparison of all insertion methods (`append`, `prepend`, `before`, `after`, `replaceWith`), the `DocumentFragment` pattern for batch insertion, and the security implications of `innerHTML`.

---

## 9. JSE Certification Exam Tips

1. **The three steps of safe node creation** — create with `createElement`, configure with `textContent`/`classList`/`setAttribute`, insert with `appendChild`. Know the order.

2. **`appendChild` moves, not copies** — if you append a node that is already in the document, it is removed from its current position and inserted at the new one.

3. **`insertAdjacentHTML` position values** — `'beforebegin'`, `'afterbegin'`, `'beforeend'`, `'afterend'`. Know which are inside and which are outside the element.

4. **`cloneNode(false)` vs `cloneNode(true)`** — `false` is shallow (element only); `true` is deep (full subtree). The argument is required to get a deep clone.

5. **`cloneNode` does not copy event listeners** — only the node structure and attributes are copied. This is a common misconception.

6. **`element.remove()` is the modern API** — it requires no parent reference. `removeChild` is the older API that requires calling it on the parent.

7. **`innerHTML = ''` clears all children** — the fastest way to empty a container before re-rendering. All child nodes are removed.

8. **`textContent` is safe; `innerHTML` is not** — for any content derived from user input, use `createElement` + `textContent` or `insertAdjacentText`. Only use `innerHTML` for controlled, trusted markup.

9. **Inserting to the page once is efficient** — build the entire subtree in memory, then insert the root. Avoid inserting partially-built nodes and then adding children to them on the live DOM — each insertion can trigger a reflow.

10. **`prepend` / `append` accept strings** — unlike `appendChild`, `element.append('text', node)` accepts a mix of strings and nodes. Strings are converted to text nodes automatically.

---

## 10. Study Checklist

- [ ] Watch the Module 11 video lecture by Professor Nash.
- [ ] Read Chapter 14 (The Document Object Model) of [Eloquent JavaScript](https://eloquentjavascript.net/14_dom.html) — focus on the node creation section.
- [ ] Read [MDN — Document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement).
- [ ] Read [MDN — Element.insertAdjacentHTML()](https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML).
- [ ] Read [MDN — Node.cloneNode()](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode).
- [ ] In DevTools, run `document.createElement('p')` in the Console — observe the element object returned. Confirm it is not yet in the DOM.
- [ ] Build a small list renderer: given a `['Alice', 'Bob', 'Carol']` array, generate `<li>` elements with `createElement` and append them to a `<ul>`.
- [ ] Test `cloneNode(true)` on a card element — confirm text content is preserved. Then add a click listener to the original and confirm the clone does not fire it.
- [ ] Complete the Module 11 Lab.
- [ ] Complete the Module 11 Quiz.
