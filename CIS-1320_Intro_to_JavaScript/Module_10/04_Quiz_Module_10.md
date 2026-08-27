# Quiz: Module 10 — Document Object Model (DOM) Basics

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

What does `document.getElementById('header')` return if no element with `id="header"` exists on the page?

- A) `undefined`
- B) An empty HTMLCollection
- C) `null`
- D) A `ReferenceError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `getElementById` returns `null` when no match is found — not `undefined`. `undefined` would be returned for an unset variable or missing object property, but DOM query methods return `null` for no match.
- *Why B is incorrect:* `getElementById` returns a single element or `null`. It never returns a collection — that is the behavior of `getElementsByClassName` or `querySelectorAll`.
- *Why C is correct:* When `getElementById` finds no matching element, it returns `null`. This is the specified behavior. Attempting to access a property of the returned `null` (such as `.textContent`) will throw a `TypeError`.
- *Why D is incorrect:* No error is thrown by the selection call itself. A `ReferenceError` would occur if you tried to use an undeclared variable — not if a DOM query finds no match.

---

### Question 2

Consider this HTML:

```html
<ul id="list">
  <li class="item">One</li>
  <li class="item">Two</li>
  <li class="item">Three</li>
</ul>
```

What is the value of `result` after this code runs?

```javascript
const result = document.querySelector('.item');
console.log(result.textContent);
```

- A) `'One'`
- B) A NodeList of three elements
- C) `null`
- D) `'One Two Three'`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `querySelector` returns the **first** element matching the selector. The first `.item` element contains the text `'One'`, so `result.textContent` is `'One'`.
- *Why B is incorrect:* `querySelector` returns a single element, not a NodeList. `querySelectorAll` returns a NodeList.
- *Why C is incorrect:* `.item` elements do exist on the page. `null` is only returned when no element matches the selector.
- *Why D is incorrect:* `textContent` returns the text of a single element. `'One Two Three'` would not come from a single `<li>`.

---

### Question 3

What type of value does `document.querySelectorAll('p')` return?

- A) An Array
- B) A NodeList
- C) An HTMLCollection
- D) A single Element

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `querySelectorAll` returns a `NodeList`, not a native `Array`. A `NodeList` has `length` and supports index access, but lacks `map`, `filter`, and `reduce`. You must use `Array.from()` to convert it.
- *Why B is correct:* `querySelectorAll` always returns a static `NodeList` containing all matching elements. Static means it is a snapshot at the time of the call — it does not update if the DOM changes later.
- *Why C is incorrect:* `HTMLCollection` is returned by older methods like `getElementsByClassName` and `getElementsByTagName`. It is live (updates when the DOM changes), unlike the static NodeList from `querySelectorAll`.
- *Why D is incorrect:* `querySelectorAll` returns a collection — it is designed to match multiple elements. `querySelector` returns a single element.

---

### Question 4

What is the difference in behavior between these two statements?

```javascript
element.textContent = '<strong>Hello</strong>';
element.innerHTML   = '<strong>Hello</strong>';
```

- A) Both display bold text
- B) Both display the literal angle bracket characters
- C) `textContent` displays the literal tags; `innerHTML` renders bold text
- D) `innerHTML` displays the literal tags; `textContent` renders bold text

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Only `innerHTML` causes the browser to parse and render the HTML. `textContent` treats the string as plain text.
- *Why B is incorrect:* `innerHTML` does not display literal angle brackets — it parses and renders the HTML it receives.
- *Why C is correct:* `textContent` treats the assigned string as literal text — `<strong>` and `</strong>` appear as visible characters on the page. `innerHTML` parses the string as HTML — `<strong>Hello</strong>` is rendered as bold text.
- *Why D is incorrect:* This reverses the actual behavior. `innerHTML` renders HTML; `textContent` escapes it.

---

### Question 5

A developer writes this code:

```javascript
const userInput = getUserComment();   // returns a string from a form field
postDiv.innerHTML = userInput;
```

What security risk does this introduce?

- A) The text may not display correctly on mobile devices
- B) `innerHTML` does not accept strings — a `TypeError` is thrown
- C) The user input could contain malicious HTML or script tags (XSS)
- D) `innerHTML` only works with numbers, not strings

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Mobile rendering is unrelated to this code. The issue is a security vulnerability, not a display concern.
- *Why B is incorrect:* `innerHTML` absolutely accepts strings — assigning a string to it is its normal usage. No error is thrown.
- *Why C is correct:* This is a **Cross-Site Scripting (XSS)** vulnerability. If `userInput` contains `<script>` tags or HTML with event handlers like `<img onerror="...">`, the browser will execute that code. Never assign user-provided content to `innerHTML`. Use `textContent` instead.
- *Why D is incorrect:* `innerHTML` works with strings. It parses the string as HTML — that is exactly the mechanism that makes it dangerous here.

---

### Question 6

What is the output of the following code?

```javascript
const el = document.querySelector('h1');
el.classList.add('active');
el.classList.add('highlight');
el.className = 'primary';
console.log(el.className);
```

- A) `'active highlight primary'`
- B) `'primary active highlight'`
- C) `'primary'`
- D) `'active highlight'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Assigning to `className` replaces the entire class string. It does not append to existing classes.
- *Why B is incorrect:* Same issue — `className =` is a full replacement, not an append. Order of the original classes is irrelevant because they are gone.
- *Why C is correct:* `classList.add` adds classes without disturbing others. But `className = 'primary'` assigns a new string to `className`, replacing all existing class values. Only `'primary'` remains.
- *Why D is incorrect:* The `className =` assignment does overwrite. `'active'` and `'highlight'` are removed when `'primary'` is assigned.

---

### Question 7

What does `classList.toggle('open')` do?

- A) Adds `'open'` to the class list regardless of its current state
- B) Removes `'open'` from the class list regardless of its current state
- C) Adds `'open'` if it is absent; removes it if it is present
- D) Throws an error if `'open'` is not already in the class list

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* That is the behavior of `classList.add`. `toggle` does not always add — it adds only when the class is absent.
- *Why B is incorrect:* That is the behavior of `classList.remove`. `toggle` does not always remove — it removes only when the class is present.
- *Why C is correct:* `classList.toggle` is a conditional add/remove. If the element does not have the class, it adds it and returns `true`. If the element already has the class, it removes it and returns `false`. This is the standard toggle pattern for interactive UI states.
- *Why D is incorrect:* `classList.toggle` never throws an error. If the class is not present, it simply adds it — that is part of its designed behavior.

---

### Question 8

Given this HTML:

```html
<ul id="nav">
  <li>Home</li>
  <li id="about">About</li>
  <li>Contact</li>
</ul>
```

What does the following code log?

```javascript
const about = document.getElementById('about');
console.log(about.nextElementSibling.textContent);
```

- A) `'About'`
- B) `'Home'`
- C) `'Contact'`
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `'About'` is the text content of the `about` element itself, not its sibling.
- *Why B is incorrect:* `'Home'` is the text of the element **before** `about`. That would be `previousElementSibling`, not `nextElementSibling`.
- *Why C is correct:* The `about` element (`<li id="about">About</li>`) is the second `<li>`. Its `nextElementSibling` is the third `<li>`, which contains `'Contact'`.
- *Why D is incorrect:* `null` would be logged if the element had no next sibling. Since `about` is the middle item, it does have a next sibling.

---

### Question 9

What is the correct CSS property name to use when setting `background-color` via the JavaScript `style` property?

- A) `element.style['background-color'] = 'blue'`
- B) `element.style.background-color = 'blue'`
- C) `element.style.backgroundColor = 'blue'`
- D) `element.style.BgColor = 'blue'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* While `element.style['background-color']` does work (bracket notation with the hyphenated string), it is not the standard pattern. C is the standard camelCase property access.
- *Why B is incorrect:* `background-color` with a hyphen is not a valid JavaScript identifier for dot notation. The hyphen would be interpreted as a subtraction operator and cause a `SyntaxError`.
- *Why C is correct:* CSS property names in JavaScript use camelCase. Hyphens are removed and the following letter is capitalized: `background-color` → `backgroundColor`, `font-size` → `fontSize`. `element.style.backgroundColor = 'blue'` is correct.
- *Why D is incorrect:* `BgColor` is not a valid JavaScript or CSS property name. It is an artifact of old HTML attributes.

---

### Question 10

What does `element.parentElement` return?

- A) The first child element of `element`
- B) The document root
- C) The element directly containing `element` in the DOM tree
- D) A NodeList of all ancestor elements

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The first child element is accessed via `element.firstElementChild`. `parentElement` navigates upward, not downward.
- *Why B is incorrect:* `parentElement` returns the immediate parent — the single element one level above in the tree. The document root (`document.documentElement`) is only returned when `parentElement` is called on the `<html>` element itself.
- *Why C is correct:* `parentElement` returns the direct parent element — the element that contains `element` as a child. For a `<li>` inside a `<ul>`, `li.parentElement` returns the `<ul>`.
- *Why D is incorrect:* `parentElement` returns one element, not a list. Traversing all ancestors would require a loop calling `parentElement` repeatedly.

---

### Question 11

What is the output of the following code given this HTML: `<p id="msg">Hello</p>`?

```javascript
const p = document.getElementById('msg');
p.textContent = '<strong>Hi</strong>';
console.log(p.textContent);
```

- A) `'Hi'` (bold)
- B) `'<strong>Hi</strong>'`
- C) `'Hello'`
- D) `TypeError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `textContent` never parses HTML. Assigning `'<strong>Hi</strong>'` stores that string as literal text — the tags are not interpreted as markup.
- *Why B is correct:* `textContent` writes the value as plain text. When read back with `p.textContent`, the full string `'<strong>Hi</strong>'` is returned, including angle brackets. The tags appear as visible characters on the page.
- *Why C is incorrect:* The assignment `p.textContent = '<strong>Hi</strong>'` replaces the original `'Hello'`. Reading `textContent` after an assignment returns the new value.
- *Why D is incorrect:* No error is thrown. `textContent` is a valid property on any element node.

---

### Question 12

What is the return value of `document.querySelectorAll('div')`  when no `<div>` elements exist in the document?

- A) `null`
- B) `undefined`
- C) An empty NodeList
- D) An empty Array

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `null` is returned by `querySelector` and `getElementById` when no match is found. `querySelectorAll` always returns a NodeList — never `null`.
- *Why B is incorrect:* `querySelectorAll` always returns a NodeList object. `undefined` is not a possible return value for this method.
- *Why C is correct:* `querySelectorAll` always returns a `NodeList`. When no elements match, the NodeList is empty (`.length === 0`), but it is still a valid NodeList object — not `null` or `undefined`.
- *Why D is incorrect:* `querySelectorAll` returns a `NodeList`, not a native `Array`. You must use `Array.from()` to convert it to an array.

---

### Question 13

Which traversal property would you use to get only the element children of a `<ul>` (excluding text nodes)?

- A) `ul.childNodes`
- B) `ul.children`
- C) `ul.firstChild`
- D) `ul.nodeList`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `childNodes` returns a `NodeList` that includes text nodes — the whitespace between `<li>` tags becomes text nodes. This is rarely what you want for DOM traversal.
- *Why B is correct:* `children` returns an `HTMLCollection` containing only the element node children — `<li>` elements in this case. Text nodes created by whitespace are excluded.
- *Why C is incorrect:* `firstChild` returns the first node of any type — typically a text node (whitespace) before the first `<li>`. Use `firstElementChild` to get the first element child.
- *Why D is incorrect:* `nodeList` is not a DOM property. `NodeList` is a type, not a property name.

---

### Question 14

What does `element.setAttribute('data-user-id', '42')` do?

- A) Sets the `userId` property of the element to `42`
- B) Sets an HTML attribute named `data-user-id` on the element to the string `'42'`
- C) Creates a JavaScript variable `data-user-id` with value `42`
- D) Throws a `SyntaxError` because attribute names cannot contain hyphens

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `setAttribute` sets an HTML attribute, not a JavaScript property. The attribute is accessible via `getAttribute('data-user-id')` or `element.dataset.userId` — not as a direct property named `userId`.
- *Why B is correct:* `setAttribute(name, value)` sets an HTML attribute on the element. The first argument is the attribute name string and the second is the value string. `data-*` attributes are standard HTML5 custom data attributes.
- *Why C is incorrect:* `setAttribute` does not create JavaScript variables. It modifies the DOM element's attribute collection.
- *Why D is incorrect:* HTML attribute names may contain hyphens. `data-user-id` is a perfectly valid attribute name following the `data-*` convention.

---

### Question 15

What is logged by the following code?

```javascript
const el = document.querySelector('div');
el.style.display = 'none';
console.log(el.style.display);
```

- A) `''` (empty string)
- B) `null`
- C) `'none'`
- D) `undefined`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An empty string would be logged if no inline display style had been set (or after removing an inline style by assigning `''`). After explicitly setting `display = 'none'`, the property holds the assigned value.
- *Why B is incorrect:* `element.style.display` is a string property. It never returns `null`.
- *Why C is correct:* `element.style.display = 'none'` sets an inline style. Reading `el.style.display` immediately afterward returns `'none'` — the value just assigned.
- *Why D is incorrect:* `display` is a defined property on `CSSStyleDeclaration`. It returns an empty string when not set inline, not `undefined`.

---

### Question 16

Which statement correctly adds the class `'active'` to an element without removing any existing classes?

- A) `el.className = 'active'`
- B) `el.classList.add('active')`
- C) `el.style.className = 'active'`
- D) `el.setAttribute('class', 'active')`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `el.className = 'active'` replaces the entire class string. If the element already had `'card selected'`, those classes would be lost.
- *Why B is correct:* `classList.add('active')` appends `'active'` to the element's existing class list without disturbing any other classes. This is the correct method for adding a single class.
- *Why C is incorrect:* `style.className` is not a valid property. `style` is the `CSSStyleDeclaration` for inline styles; `className` is a property on the element itself, not on `style`.
- *Why D is incorrect:* `setAttribute('class', 'active')` replaces the entire `class` attribute with the new value — equivalent to `className =`. It does not append.

---

### Question 17

Consider this HTML:

```html
<div id="outer">
  <p id="inner">Text</p>
</div>
```

What does `document.getElementById('inner').parentElement.id` return?

- A) `'inner'`
- B) `'outer'`
- C) `null`
- D) `undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'inner'` is the ID of the element itself. `parentElement` navigates one level up to the containing element.
- *Why B is correct:* `getElementById('inner')` returns the `<p>`. `.parentElement` returns the `<div id="outer">`. `.id` on that element returns `'outer'`.
- *Why C is incorrect:* `null` would be returned if `parentElement` was called on an element with no parent (the `<html>` element's `parentElement` is `null`). The `<p>` has a clear parent.
- *Why D is incorrect:* `id` is a defined property on element nodes. It returns an empty string `''` if no ID is set, not `undefined`.

---

### Question 18

What is the difference between `querySelector('#nav a')` called on `document` and the same selector called on `navElement`?

- A) There is no difference — both always search the entire document
- B) Called on `document`, it searches the whole document; called on `navElement`, it searches only within `navElement`'s descendants
- C) Called on `navElement`, it uses a different CSS syntax and will throw an error
- D) `querySelector` cannot be called on element nodes — only on `document`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `querySelector` scopes its search to the subtree of the object it is called on. Calling it on an element limits results to that element's descendants.
- *Why B is correct:* `document.querySelector(selector)` searches the entire document. `element.querySelector(selector)` searches only the element's descendants. This scoping behavior is useful for working with a specific section of the page.
- *Why C is incorrect:* The CSS selector syntax is identical regardless of whether `querySelector` is called on `document` or an element. No error is thrown.
- *Why D is incorrect:* `querySelector` and `querySelectorAll` are methods available on all element nodes (they are defined on `Element`), not exclusively on `document`.

---

### Question 19

What does `classList.contains('hidden')` return if the element has `class="card hidden active"`?

- A) `'hidden'`
- B) `false`
- C) `true`
- D) `1`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `classList.contains` returns a boolean, not the class name string. It answers whether the class is present, not what the class is.
- *Why B is incorrect:* `'hidden'` is present in the class list. The method returns `true` when the specified class exists on the element.
- *Why C is correct:* `classList.contains('hidden')` returns `true` because `'hidden'` is one of the element's classes. The element having other classes (`card`, `active`) does not affect the check.
- *Why D is incorrect:* `classList.contains` always returns a boolean (`true` or `false`), never a number.

---

### Question 20

A developer wants to hide an element by removing its `display` inline style so the stylesheet value takes effect again. Which code achieves this?

- A) `el.style.display = 'default'`
- B) `el.style.display = null`
- C) `el.style.display = ''`
- D) `delete el.style.display`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `'default'` is not a valid CSS `display` value. Setting it would apply an invalid style string that the browser ignores or treats as invalid.
- *Why B is incorrect:* Assigning `null` to a style property sets the property to the string `'null'` in some browsers or is silently ignored. The correct way to remove an inline style is to assign an empty string.
- *Why C is correct:* Assigning an empty string `''` to an inline style property removes that property from the inline style declaration. The element then falls back to whatever the stylesheet specifies for `display`.
- *Why D is incorrect:* `delete` does not work reliably on style properties because `CSSStyleDeclaration` properties are not normal object properties. The standard technique is to assign `''`.
