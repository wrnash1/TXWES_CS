# Reading Guide: Module 10 — Document Object Model (DOM) Basics

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-1320 &BULL; INTRODUCTION TO JAVASCRIPT PROGRAMMING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Introduction

Every interactive web page — a button that shows a menu, a form that validates before submitting, a live search that updates as you type — is JavaScript reading from and writing to the DOM. The Document Object Model is the in-memory tree of objects the browser builds when it parses HTML. JavaScript does not modify the HTML source file; it modifies the DOM, and the browser re-renders whatever the DOM contains.

This module covers the essentials: what the DOM is, how to select elements, how to read and write content, how to manage CSS classes, and how to traverse the tree. These skills are foundational for everything in Modules 11, 12, and beyond.

---

## 1. The DOM: A Tree of Objects

When the browser loads an HTML document, it parses the text and creates a **tree of node objects** in memory. The root of the tree is the `document` object. Every HTML element becomes an **element node**; the text inside an element becomes a **text node**. JavaScript interacts with these nodes through properties and methods.

```html
<body>
  <h1 id="title">Hello</h1>
  <p class="intro">Welcome.</p>
</body>
```

The DOM tree for this fragment:

```text
document
  └── body
        ├── h1#title  (text: "Hello")
        └── p.intro   (text: "Welcome.")
```

Each node is a full JavaScript object. You can read its properties, change them, add children, or remove it entirely — and the browser updates what is displayed immediately.

**The critical mental model:**

- HTML source → parser → DOM tree (in memory)
- JavaScript modifies the DOM tree
- Browser re-renders from the current DOM state
- The HTML source file never changes

---

## 2. Selecting Elements

All DOM selection begins from the `document` object (or from any element, to search within it).

### `getElementById`

```javascript
const heading = document.getElementById('title');
// Returns the element with id="title", or null if not found
```

Pass the ID string without `#`. Returns exactly one element (IDs must be unique) or `null`.

### `querySelector`

```javascript
const intro = document.querySelector('.intro');       // first element with class "intro"
const heading = document.querySelector('#title');     // by ID
const firstLi = document.querySelector('ul li');      // CSS descendant selector
```

`querySelector` accepts any valid CSS selector. Returns the **first** matching element or `null`. This is the modern, preferred method — one tool for all selection tasks.

### `querySelectorAll`

```javascript
const allItems = document.querySelectorAll('li');
// Returns a static NodeList of all matching elements
```

Returns all matches as a `NodeList`. A `NodeList` is array-like: it has `.length` and supports index access (`items[0]`), but it is not a true `Array`. To use full array methods, convert it:

```javascript
const itemArray = Array.from(document.querySelectorAll('li'));
itemArray.forEach(li => console.log(li.textContent));
```

### Older Methods (You Will See These in Legacy Code)

```javascript
document.getElementsByClassName('intro')   // HTMLCollection — live
document.getElementsByTagName('p')         // HTMLCollection — live
```

`HTMLCollection` updates automatically when the DOM changes. `querySelectorAll` returns a static snapshot. For new code, use `querySelector` and `querySelectorAll`.

### Null Checks

`getElementById` and `querySelector` return `null` when no match is found. Accessing properties of `null` throws a `TypeError`:

```javascript
const missing = document.getElementById('nonexistent');
missing.textContent = 'test';   // TypeError: Cannot set properties of null
```

Guard when the element may not exist:

```javascript
const el = document.getElementById('tooltip');
if (el) {
  el.textContent = 'Updated';
}
```

---

## 3. Reading and Writing Content

### `textContent`

`textContent` reads or writes the **plain text** inside an element. It ignores HTML tags in the existing content and treats any value you assign as literal text.

```javascript
const heading = document.querySelector('h1');

// Read
console.log(heading.textContent);   // 'Hello'

// Write — all text inside the element is replaced
heading.textContent = 'Welcome, JavaScript!';
```

When writing, `textContent` is safe with user-provided data — it never parses HTML, so `<script>` tags in the value are displayed as text, not executed.

### `innerHTML`

`innerHTML` reads or writes the **HTML markup** inside an element. The browser parses any HTML string you assign and creates the corresponding nodes.

```javascript
const container = document.querySelector('.intro');

// Read — returns the inner HTML as a string
console.log(container.innerHTML);   // 'Welcome.'

// Write — string is parsed as HTML
container.innerHTML = 'This is <strong>bold</strong> text.';
// Creates: "This is " + <strong> element + " text."
```

### `textContent` vs `innerHTML`

| Property | Reads | Writes | Safe with user data? |
|---|---|---|---|
| `textContent` | Plain text (strips tags) | Plain text only | Yes |
| `innerHTML` | HTML markup as string | Parsed as HTML | No — XSS risk |

### XSS Warning

Never assign user-provided content to `innerHTML`:

```javascript
// UNSAFE — do not do this:
const userComment = getCommentFromUser();
div.innerHTML = userComment;   // If the comment contains <script>, it runs
```

This is a **Cross-Site Scripting (XSS)** vulnerability. Use `textContent` for plain text. For HTML construction from dynamic data, use DOM creation methods (covered in Module 11).

---

## 4. Attributes

HTML attributes (`id`, `class`, `href`, `src`, `disabled`, etc.) are readable and writable from JavaScript.

### `getAttribute` / `setAttribute` / `hasAttribute` / `removeAttribute`

```javascript
const link = document.querySelector('a');

link.getAttribute('href')              // 'https://example.com'
link.setAttribute('href', 'https://txwes.edu')
link.hasAttribute('target')            // false
link.removeAttribute('disabled')
```

### Direct Property Shortcuts

Many common attributes have matching element properties:

```javascript
link.href = 'https://txwes.edu';    // same as setAttribute('href', ...)
link.id = 'navLink';
img.src = 'logo.png';
input.value = 'default text';
input.disabled = true;
```

Use direct properties for common attributes — they are shorter and type-safe. Use `getAttribute`/`setAttribute` for custom attributes (e.g., `data-*`) or when working dynamically with attribute names as strings.

---

## 5. Inline Styles

The `style` property of an element corresponds to its inline `style` attribute. Setting a style here adds or overrides inline styles.

```javascript
const box = document.querySelector('.box');

box.style.color = 'navy';
box.style.backgroundColor = 'lightyellow';   // camelCase, not background-color
box.style.fontSize = '1.5rem';
box.style.display = 'none';    // hides the element
box.style.display = '';        // removes inline style, reverts to stylesheet
```

CSS property names in JavaScript are **camelCase** versions of their CSS names: `background-color` → `backgroundColor`, `font-size` → `fontSize`, `border-radius` → `borderRadius`.

Inline style manipulation is useful for dynamic values (e.g., setting a width based on a calculation). For toggling visual states, prefer `classList` (next section).

---

## 6. `classList` — Managing CSS Classes

The `classList` property provides methods to add, remove, toggle, and check CSS classes on an element without touching other classes.

```javascript
const card = document.querySelector('.card');

card.classList.add('selected');              // adds class
card.classList.remove('selected');           // removes class
card.classList.toggle('selected');           // adds if absent, removes if present
card.classList.contains('selected');         // returns true or false
card.classList.replace('old', 'new');        // replaces one class with another
```

### `classList` vs `className`

```javascript
// className — a string of all classes
element.className = 'card selected';   // REPLACES all existing classes

// classList.add — appends, does not replace
element.classList.add('selected');     // adds 'selected', keeps other classes
```

Use `classList` for all class manipulation. Only use `className` if you need to read or set the entire class string at once.

### Practical Pattern — CSS Class Toggling

Define your visual states in CSS:

```css
.hidden   { display: none; }
.active   { background-color: #0057b8; color: white; }
.dark-mode { background: #1a1a1a; color: #fff; }
```

Toggle them with JavaScript:

```javascript
document.getElementById('toggleBtn').addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});
```

JavaScript handles **when**; CSS handles **what**. This separation keeps styles maintainable.

---

## 7. DOM Traversal

From any element, you can navigate to related elements using traversal properties.

```javascript
const ul = document.querySelector('ul');

// Parent
ul.parentElement           // the element directly containing ul

// Children (element nodes only — no text nodes)
ul.children                // HTMLCollection of direct child elements
ul.firstElementChild       // first child element
ul.lastElementChild        // last child element

// Siblings
const li = ul.firstElementChild;
li.nextElementSibling      // the element immediately after li
li.previousElementSibling  // the element immediately before li (null if first)
```

### `children` vs `childNodes`

| Property | Returns | Includes text nodes? |
|---|---|---|
| `children` | HTMLCollection of element nodes | No |
| `childNodes` | NodeList of all node types | Yes |

In almost all cases, use `children`, `firstElementChild`, `lastElementChild`, `nextElementSibling`, and `previousElementSibling`. The `childNodes` / `firstChild` / `lastChild` properties include text nodes created by whitespace in the HTML source — not useful for element traversal.

---

## 8. Selecting Within an Element

`querySelector` and `querySelectorAll` can be called on any element, not just `document`. This scopes the search to that element's descendants:

```javascript
const nav = document.querySelector('nav');

// Only searches inside the nav element
const links = nav.querySelectorAll('a');
```

This is useful when you have multiple similar structures on the page and want to work with only one section's descendants.

---

## 9. Supplemental Resources

The following free, openly available resources extend and reinforce the topics covered in this module.

- **[Eloquent JavaScript — Chapter 14: The Document Object Model](https://eloquentjavascript.net/14_dom.html)**
  The primary OER textbook chapter for this module. Covers the DOM tree structure, moving through the DOM, finding elements, changing the document, creating and removing nodes, and handling attributes with worked examples.

- **[MDN Web Docs — Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)**
  Comprehensive introduction to the DOM API including the document tree, node types, the `document` object, and how JavaScript interacts with HTML. A strong conceptual foundation for all DOM work.

- **[MDN Web Docs — Document.querySelector()](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)**
  Full reference for `querySelector` and `querySelectorAll` including accepted CSS selector syntax, return types, and the distinction between static NodeList and live HTMLCollection.

- **[MDN Web Docs — Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)**
  Complete reference for the `classList` API — `add`, `remove`, `toggle`, `contains`, `replace`, and the `DOMTokenList` type. Includes browser compatibility and runnable examples.

- **[javascript.info — Searching: getElement*, querySelector*](https://javascript.info/searching-elements-dom)**
  Beginner-friendly comparison of all DOM selection methods with interactive examples. Clearly explains the difference between `querySelector`, `getElementById`, `getElementsByClassName`, live vs static collections, and scoped queries.

---

## 10. JSE Certification Exam Tips

1. **`getElementById` vs `querySelector` syntax** — `getElementById('title')` takes just the string; `querySelector('#title')` uses the full CSS selector including the `#`. Both select by ID but with different argument formats.

2. **`querySelector` returns the first match** — if multiple elements match the selector, only the first is returned. Use `querySelectorAll` for all matches.

3. **`querySelectorAll` returns a NodeList, not an Array** — `NodeList` has `length` and supports `forEach` (in modern browsers), but lacks `map`, `filter`, `reduce`. Convert with `Array.from()`.

4. **`getElementById` and `querySelector` return `null` if not found** — not `undefined`, not an empty NodeList. Accessing `.textContent` on `null` throws a `TypeError`.

5. **`textContent` vs `innerHTML`** — `textContent` is plain text (safe, no HTML parsing); `innerHTML` is HTML markup (powerful, XSS risk). Know which to use and why.

6. **`innerHTML` XSS risk** — never assign user-provided content to `innerHTML`. This is a security vulnerability that the JSE exam and every code review will flag.

7. **CSS properties in JavaScript use camelCase** — `background-color` is `backgroundColor`, `font-size` is `fontSize`. The hyphen form is CSS syntax; camelCase is the JavaScript property.

8. **`classList.add` vs `className =`** — `classList.add` appends without disturbing other classes; `className =` replaces all classes. Know the difference.

9. **`classList.toggle`** — adds the class if absent, removes it if present. Returns `true` if the class was added, `false` if removed.

10. **Traversal properties use `ElementChild` / `ElementSibling` variants** — `firstElementChild` skips text nodes; `firstChild` does not. Prefer the `Element*` versions for DOM traversal.

---

## 11. Study Checklist

- [ ] Watch the Module 10 video lecture by Professor Nash.
- [ ] Read Chapter 14 (The Document Object Model) of [Eloquent JavaScript](https://eloquentjavascript.net/14_dom.html).
- [ ] Read [MDN — Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).
- [ ] Read [MDN — Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList).
- [ ] Open a page in Chrome, open DevTools Elements panel, and run `document.querySelector('h1').textContent = 'Changed'` in the Console — observe the page update live.
- [ ] Confirm that `querySelectorAll` returns a NodeList by calling `.map()` on it and observing the error.
- [ ] Write a toggle that uses `classList.toggle` to switch a class — define the class in a `<style>` tag and confirm it works.
- [ ] Complete the Module 10 Lab.
- [ ] Complete the Module 10 Quiz.
