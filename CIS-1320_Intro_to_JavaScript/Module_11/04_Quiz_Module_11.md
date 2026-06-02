# Quiz: Module 11 — DOM Manipulation and Styling

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
