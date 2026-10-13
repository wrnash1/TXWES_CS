# Quiz: Module 11 — DOM Manipulation and Styling

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What is the correct order of steps to add a new `<li>` element to an existing `<ul>` with `id="list"`?

- A) Select the `<ul>`, insert the `<li>`, then set its text content
- B) Create the `<li>`, set its text content, then append it to the `<ul>`
- C) Append the `<li>` to the `<ul>`, then create it with `createElement`
- D) Select the `<ul>`, create the `<li>` inside it, then it appears automatically

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* You cannot set text content on an element before creating it. You must create the element first with `document.createElement`, then configure it, then insert it.
- *Why B is correct:* The correct pipeline is: create with `document.createElement('li')`, configure with `textContent` (and any other properties), then insert with `ul.appendChild(li)`. Configure before inserting — the element exists in memory but is not visible until appended.
- *Why C is incorrect:* You cannot append an element that has not yet been created. `createElement` must come before any insertion call.
- *Why D is incorrect:* Elements created with `createElement` do not appear automatically. They exist in memory until explicitly inserted into the document with `appendChild`, `prepend`, or another insertion method.

---

### Question 2

What does `parent.appendChild(node)` do if `node` is already present elsewhere in the document?

- A) Creates a copy of `node` and appends it — the original remains in place
- B) Throws a `TypeError` because the node is already in the DOM
- C) Moves `node` from its current position and appends it to `parent`
- D) Appends a reference to `node` — the DOM now contains it in two places

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `appendChild` does not copy. If you want a copy, you must call `cloneNode` first. `appendChild` with an existing node moves it.
- *Why B is incorrect:* No error is thrown. Moving a node via `appendChild` is valid and expected behavior.
- *Why C is correct:* A DOM node can only exist in one location in the tree. When you `appendChild` a node that is already in the document, the browser removes it from its current position and re-inserts it at the new location. This is the defined behavior.
- *Why D is incorrect:* A node cannot appear in two places simultaneously. The DOM is a tree — each node has exactly one parent. Appending it elsewhere moves it.

---

### Question 3

Which `insertAdjacentHTML` position inserts content **inside** the element, **after** its last existing child?

- A) `'afterend'`
- B) `'beforebegin'`
- C) `'afterbegin'`
- D) `'beforeend'`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `'afterend'` inserts content after the element itself — as a following sibling, outside the element entirely.
- *Why B is incorrect:* `'beforebegin'` inserts content before the element itself — as a preceding sibling, also outside the element.
- *Why C is incorrect:* `'afterbegin'` inserts content inside the element, but before its first child — the opposite end from `'beforeend'`.
- *Why D is correct:* `'beforeend'` inserts content inside the element, after its last child. It is equivalent to `appendChild` in positioning but accepts an HTML string.

---

### Question 4

What is the difference between `element.remove()` and `parent.removeChild(element)`?

- A) `remove()` deletes the element permanently from memory; `removeChild` only detaches it
- B) `remove()` requires no parent reference; `removeChild` must be called on the parent
- C) `removeChild` is the modern API; `remove()` is deprecated
- D) They are identical — both require a parent reference

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Neither method deletes anything from memory. Both detach the node from the DOM. If you hold a reference to it in a variable, it still exists in memory and can be re-inserted.
- *Why B is correct:* `element.remove()` is the modern API introduced in ES5+. You call it directly on the element — no parent needed. `parent.removeChild(element)` is the older API that requires obtaining a reference to the parent first and calling `removeChild` on it.
- *Why C is incorrect:* `remove()` is the modern API; `removeChild` is the older one. Neither is deprecated, but `remove()` is the preferred approach in new code.
- *Why D is incorrect:* `remove()` does not require a parent reference — that is its key advantage over `removeChild`.

---

### Question 5

What does `element.cloneNode(false)` return?

- A) A deep copy of the element and all its descendants
- B) A copy of the element with no children
- C) `null` — `false` means do not clone
- D) A copy of the element and its event listeners only

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That is the behavior of `cloneNode(true)`. `true` produces a deep clone including all descendants.
- *Why B is correct:* `cloneNode(false)` creates a shallow clone — the element itself is copied (with its attributes), but none of its child nodes are included. The result is an empty copy of the outer element.
- *Why C is incorrect:* `false` does not mean "do not clone." It means "clone shallowly." The method still returns a new element node.
- *Why D is incorrect:* `cloneNode` does not copy event listeners at all, regardless of the argument. Neither `cloneNode(true)` nor `cloneNode(false)` copies listeners attached via `addEventListener`.

---

### Question 6

A developer writes:

```javascript
const card = document.querySelector('.card');
card.addEventListener('click', () => console.log('clicked'));

const copy = card.cloneNode(true);
document.body.appendChild(copy);
```

When the user clicks the cloned card, what happens?

- A) `'clicked'` is logged — the event listener was cloned with the node
- B) Nothing is logged — event listeners are not copied by `cloneNode`
- C) A `TypeError` is thrown because the clone has no event listener
- D) Both the original and the clone log `'clicked'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `cloneNode` copies the element structure and attributes, but not event listeners. The clone has no click handler.
- *Why B is correct:* Event listeners attached via `addEventListener` are stored internally by the browser, not as node attributes. `cloneNode` only copies the DOM structure and attributes — listeners are not transferred. Clicking the clone does nothing unless you separately call `addEventListener` on the clone.
- *Why C is incorrect:* No error is thrown. Clicking an element that has no listener for that event is perfectly valid — the event fires and nothing handles it.
- *Why D is incorrect:* Event listeners do not propagate between a node and its clone. The original still fires; the clone does not.

---

### Question 7

What is the safest way to insert a string from a text input field (`input.value`) into the DOM?

- A) `div.innerHTML = input.value`
- B) `div.insertAdjacentHTML('beforeend', input.value)`
- C) `div.textContent = input.value`
- D) `div.outerHTML = input.value`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `innerHTML` parses the assigned string as HTML. If `input.value` contains `<script>` tags or event handler attributes, they will be executed — this is an XSS vulnerability.
- *Why B is incorrect:* `insertAdjacentHTML` also parses the string as HTML. It has the same XSS risk as `innerHTML` when given user-provided content.
- *Why C is correct:* `textContent` always treats the assigned value as plain text. HTML markup characters (`<`, `>`, `&`) are escaped and displayed as literal characters — they are never parsed as HTML. This is always safe for user input.
- *Why D is incorrect:* `outerHTML` replaces the element itself (not just its content) with parsed HTML — even more dangerous than `innerHTML` for user data.

---

### Question 8

What does `container.innerHTML = ''` do?

- A) Sets the text content of `container` to an empty string
- B) Removes `container` from the DOM
- C) Removes all child nodes from `container`, leaving it empty
- D) Throws a `SyntaxError` because `''` is not valid HTML

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `innerHTML = ''` operates on the children of `container`, not on `container`'s own text. It removes all child nodes.
- *Why B is incorrect:* `innerHTML = ''` does not remove `container` itself. `container` remains in the DOM — it simply has no children after the assignment.
- *Why C is correct:* Assigning an empty string to `innerHTML` instructs the browser to parse the empty string as HTML, producing no nodes. All existing child nodes of `container` are removed. `container` itself stays in place, now empty. This is the standard idiom for clearing a container before re-rendering.
- *Why D is incorrect:* An empty string is valid HTML content — it simply has no elements. No error is thrown.

---

### Question 9

A developer wants to render a list of names from an array. Which approach is safe if the names come from user-submitted form data?

```javascript
const names = getUserNames();   // could contain '<script>' etc.
const ul = document.getElementById('name-list');
```

- A) `ul.innerHTML = names.map(n => '<li>' + n + '</li>').join('')`
- B) `names.forEach(n => { const li = document.createElement('li'); li.textContent = n; ul.appendChild(li); })`
- C) `ul.insertAdjacentHTML('beforeend', names.map(n => '<li>' + n + '</li>').join(''))`
- D) `ul.outerHTML = '<ul>' + names.join('') + '</ul>'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Concatenating user data into an HTML string and assigning to `innerHTML` parses the result as HTML. If any name contains `<script>alert('xss')</script>`, it executes. This is an XSS vulnerability.
- *Why B is correct:* Creating each `<li>` with `createElement` and setting its content with `textContent` treats every name as plain text. No HTML parsing occurs. Even if a name contains `<script>` tags, they display as visible characters — they never execute.
- *Why C is incorrect:* Same XSS risk as A — string concatenation with user data inside `insertAdjacentHTML` is just as dangerous as `innerHTML`.
- *Why D is incorrect:* `outerHTML` replaces the element itself with parsed HTML — the most dangerous option. User data is still injected into an HTML string.

---

### Question 10

What is the output of the following code (assume the HTML has `<ul id="list"><li>A</li><li>B</li></ul>`)?

```javascript
const ul = document.getElementById('list');
const newLi = document.createElement('li');
newLi.textContent = 'C';
ul.prepend(newLi);
console.log(ul.firstElementChild.textContent);
```

- A) `'A'`
- B) `'B'`
- C) `'C'`
- D) `undefined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `prepend` inserts the new element **before** all existing children. After `prepend(newLi)`, the original first child `'A'` is now the second child.
- *Why B is incorrect:* `'B'` was the second child before the `prepend`. After it, `'B'` is now the third child.
- *Why C is correct:* `element.prepend(node)` inserts `node` as the **first** child of `element`. After the call, the `<ul>` contains `[C, A, B]` in order. `firstElementChild` returns the `<li>` containing `'C'`.
- *Why D is incorrect:* `firstElementChild` always returns an element node (or `null` for an empty parent). Since the `<ul>` has children, it returns the first `<li>`, which has `textContent` of `'C'`.

---

### Question 11

Which of the following correctly creates a `<div>` element with the class `'alert'` and the text `'Warning!'`, then appends it to `document.body`?

- A) `document.body.appendChild('<div class="alert">Warning!</div>')`
- B) `const d = document.createElement('div'); d.className = 'alert'; d.textContent = 'Warning!'; document.body.appendChild(d);`
- C) `document.body.innerHTML += '<div class="alert">Warning!</div>';`
- D) Both B and C are equivalent and correct

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `appendChild` requires a node object, not an HTML string. Passing a string throws a `TypeError`. Use `insertAdjacentHTML` or `innerHTML` if you want to insert an HTML string.
- *Why B is correct:* This is the standard safe pattern: create with `createElement`, configure with `className` and `textContent`, insert with `appendChild`. The element is created in memory, configured, and inserted in one clean sequence.
- *Why C is incorrect:* `innerHTML +=` re-parses the entire `innerHTML` of `document.body`, destroys all existing DOM nodes and their event listeners, and rebuilds them. It works in simple cases but is destructive and should be avoided.
- *Why D is incorrect:* B and C are not equivalent. C has significant side effects (destroying event listeners on existing children). Only B is the clean, recommended approach.

---

### Question 12

What does `parent.insertBefore(newNode, null)` do?

- A) Throws a `TypeError` because `null` is not a valid reference node
- B) Inserts `newNode` before the first child of `parent`
- C) Inserts `newNode` as the last child of `parent`
- D) Does nothing — `null` is ignored

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `null` is explicitly valid as the second argument to `insertBefore`. The specification defines this case — it is not an error.
- *Why B is incorrect:* Inserting before the first child would require passing `parent.firstChild` as the reference node, not `null`.
- *Why C is correct:* When the second argument to `insertBefore` is `null`, the method inserts `newNode` as the last child of `parent` — equivalent to `appendChild(newNode)`. This is part of the DOM specification.
- *Why D is incorrect:* `null` is not ignored — it has a defined meaning. The insertion happens; it places the node at the end of the parent.

---

### Question 13

What is the difference between `element.append('Hello')` and `element.appendChild(document.createTextNode('Hello'))`?

- A) `append` creates an element; `appendChild` creates a text node
- B) Both produce the same result — a text node containing `'Hello'` is added as the last child
- C) `append` only works in Internet Explorer; `appendChild` is modern
- D) `append` throws an error when passed a string; only nodes are accepted

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `element.append('Hello')` automatically converts the string to a text node before inserting it. Both calls result in the same DOM structure.
- *Why B is correct:* `append` accepts strings and converts them to text nodes internally. `document.createTextNode` explicitly creates a text node. Both produce the same result: a text node with content `'Hello'` appended as the last child of `element`.
- *Why C is incorrect:* `append` is a modern API; `appendChild` is the older one. Neither is Internet Explorer-specific. `append` has broad modern browser support.
- *Why D is incorrect:* `append` specifically supports strings as arguments. From MDN: "The Element.append() method inserts a set of Node objects or string objects after the last child of the Element."

---

### Question 14

A developer writes a function to render a list of user objects:

```javascript
function render(users) {
  const list = document.getElementById('list');
  list.innerHTML = '';
  users.forEach(u => {
    const li = document.createElement('li');
    li.innerHTML = `<span class="name">${u.name}</span>`;
    list.appendChild(li);
  });
}
```

What security risk does this introduce?

- A) None — only `u.name` is inserted, and object properties are safe
- B) `innerHTML` on `li` is an XSS risk if `u.name` contains HTML or script content
- C) `createElement` cannot create `<li>` elements — it is limited to `<div>`
- D) The function throws a `TypeError` because you cannot call `innerHTML` on a newly created element

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Object properties can contain any string, including `<script>alert('xss')</script>`. If `u.name` comes from user input or an external source, injecting it into `innerHTML` is an XSS vulnerability.
- *Why B is correct:* Assigning `` `<span class="name">${u.name}</span>` `` to `innerHTML` parses the interpolated string as HTML. If `u.name` contains malicious markup (e.g., `<img onerror="...">`) it will execute. The fix is `span.textContent = u.name` instead.
- *Why C is incorrect:* `document.createElement` creates any valid HTML element — `'li'`, `'div'`, `'span'`, `'input'`, etc.
- *Why D is incorrect:* `innerHTML` is available on all element nodes, including newly created ones. Setting it before inserting the element into the document is perfectly valid.

---

### Question 15

What does `element.replaceWith(newElement)` do if `element` is a child of some parent?

- A) Removes `element` from the DOM and returns it; `newElement` must be inserted separately
- B) Inserts `newElement` after `element` in the parent, then removes `element`
- C) Replaces `element` in its parent with `newElement` in a single operation
- D) Throws an error if `newElement` is already in the document

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `replaceWith` handles both the removal of `element` and the insertion of `newElement` in one call. No separate insertion step is needed.
- *Why B is incorrect:* `replaceWith` does not insert then remove — it replaces directly. `newElement` takes exactly the position `element` occupied.
- *Why C is correct:* `element.replaceWith(newElement)` removes `element` from its parent and inserts `newElement` in the same position in a single atomic operation. This is the modern replacement for `parent.replaceChild(newElement, element)`.
- *Why D is incorrect:* If `newElement` is already in the DOM, it is moved — just as with `appendChild`. No error is thrown.

---

### Question 16

How many child nodes does the following code create inside `ul`?

```javascript
const ul = document.createElement('ul');
ul.innerHTML = '<li>A</li><li>B</li><li>C</li>';
```

- A) 1
- B) 3
- C) 6
- D) 7

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `innerHTML` parses the string as HTML, producing three `<li>` elements — not a single text node or element.
- *Why B is correct:* The HTML string contains three `<li>` elements. After parsing, `ul` has exactly three child element nodes — `<li>A</li>`, `<li>B</li>`, and `<li>C</li>`.
- *Why C is incorrect:* 6 would result from counting each `<li>` element plus its text node child. But `childNodes` would give 6 in some cases; `children` (element nodes only) gives 3. The question asks about child nodes from `innerHTML`, which places 3 elements.
- *Why D is incorrect:* 7 would imply text nodes for whitespace between the `<li>` elements. Since the string has no whitespace between tags, there are no inter-element text nodes. Only 3 `<li>` element nodes are created.

---

### Question 17

What is the value of `copy.children.length` after this code runs?

```javascript
const original = document.createElement('ul');
original.innerHTML = '<li>One</li><li>Two</li><li>Three</li>';
const copy = original.cloneNode(false);
```

- A) `3`
- B) `1`
- C) `0`
- D) `undefined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `cloneNode(false)` is a shallow clone — it copies the element itself but none of its children. The `<li>` elements are not included in `copy`.
- *Why B is incorrect:* No partial cloning occurs. Either all children are cloned (`cloneNode(true)`) or none (`cloneNode(false)`).
- *Why C is correct:* `cloneNode(false)` creates an empty `<ul>` element with no children. `copy.children.length` is `0` because the three `<li>` nodes were not copied.
- *Why D is incorrect:* `children` is a defined property on all element nodes. It returns an empty `HTMLCollection` (not `undefined`) for elements with no children.

---

### Question 18

A developer wants to insert a new `<h2>` before the `<p>` inside a `<section>`. The HTML is:

```html
<section id="intro">
  <p id="body-text">Content here.</p>
</section>
```

Which code correctly inserts `<h2>New Heading</h2>` before the `<p>`?

- A) `document.getElementById('body-text').insertAdjacentHTML('beforebegin', '<h2>New Heading</h2>')`
- B) `document.getElementById('intro').insertAdjacentHTML('afterbegin', '<h2>New Heading</h2>')`
- C) Both A and B produce the same result
- D) Neither — you must use `insertBefore` for this operation

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect on its own:* `'beforebegin'` inserts before the `#body-text` element itself — as a sibling immediately before it inside the `<section>`. This places the `<h2>` before the `<p>`. This is correct.
- *Why B is incorrect on its own:* `'afterbegin'` inserts inside `#intro`, before its first child — which is the `<p>`. This also places the `<h2>` before the `<p>`. This is correct too.
- *Why C is correct:* Both A and B achieve the same result — inserting `<h2>New Heading</h2>` immediately before the `<p>` within `<section>`. `'beforebegin'` on the `<p>` and `'afterbegin'` on the `<section>` are equivalent positions when the `<p>` is the first child.
- *Why D is incorrect:* `insertAdjacentHTML` is a perfectly valid tool for this operation. `insertBefore` would also work but is not the only option.

---

### Question 19

What is the effect of calling `element.remove()` when `element` is stored in a JavaScript variable?

- A) The variable becomes `null`
- B) The variable becomes `undefined`
- C) A `ReferenceError` is thrown because the element no longer exists
- D) The variable still holds a reference to the detached element, which can be reinserted

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `element.remove()` does not change the value of the variable `element`. The variable still holds a reference to the node object; the node is simply no longer connected to the document.
- *Why B is incorrect:* Same reasoning — the variable is not set to `undefined`. It still references the element object.
- *Why C is incorrect:* No error is thrown. You can call properties and methods on detached nodes. The variable is valid; the node just has no parent.
- *Why D is correct:* `remove()` detaches the node from the DOM tree but does not destroy it. If you hold a reference in a variable, the node persists in memory and can be reinserted with `appendChild` or another insertion method.

---

### Question 20

A developer wants to render a list of 1,000 items from an array. Which approach is most performant?

- A) Loop through the array and call `document.body.appendChild(li)` for each item inside the loop
- B) Build all `<li>` elements, append them to a `DocumentFragment`, then append the fragment to the list once
- C) Use `innerHTML +=` inside the loop to add one item at a time
- D) Call `querySelectorAll` after each insertion to verify the item was added

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Calling `appendChild` directly on a live DOM element 1,000 times causes up to 1,000 reflows and repaints. Each insertion may trigger the browser to recalculate layout.
- *Why B is correct:* A `DocumentFragment` is a lightweight in-memory container that is not part of the live DOM. Appending nodes to a `DocumentFragment` causes no reflows. When the fragment is appended to the document in a single call, the browser performs one reflow for all 1,000 items — significantly faster.
- *Why C is incorrect:* `innerHTML +=` re-parses the entire innerHTML string on each iteration, destroys all existing child nodes and their listeners, and rebuilds them. Doing this 1,000 times is catastrophically slow.
- *Why D is incorrect:* Calling `querySelectorAll` after each insertion performs an unnecessary DOM search on every iteration and does nothing to improve performance — it actively makes things worse.
