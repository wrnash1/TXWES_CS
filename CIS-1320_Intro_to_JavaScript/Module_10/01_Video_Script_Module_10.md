# Video Script: CIS-1320 — Introduction to JavaScript

## Module 10 — Document Object Model (DOM) Basics

**Estimated Duration:** 18–22 minutes
**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use a simple HTML file in VS Code + Live Server for all [DEMO] sections. Chrome DevTools Elements panel is essential — show the live DOM tree updating as JavaScript runs.
> - [PAUSE] = 2 seconds of silence.
> - The tree metaphor is the conceptual core — spend time on it before any code.
> - `getElementById` vs `querySelector` distinction: both select by ID but `querySelector` is more versatile and is the modern choice. Explain why both are taught.
> - Emphasize: `innerHTML` can execute injected scripts (XSS risk) — introduce this awareness now, not later.
> - The distinction between `textContent` and `innerHTML` is exam-tested. Show both with a concrete `<strong>` tag example.
> - `classList` API is preferred over directly assigning `element.className`. Show both so students understand older code they will encounter.
> - `style` property: direct inline style setting. Briefly introduce — CSS classes via `classList` are the preferred pattern.
> - End with a clear mental model: HTML is parsed → DOM tree is built → JavaScript reads and writes that tree → browser re-renders.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 10 | Document Object Model (DOM) Basics | CIS-1320"]**

"Up to this point, every program we have written runs in the console — numbers in, output out. That changes today. Module 10 introduces the Document Object Model, the bridge between JavaScript and the web page you see in the browser. Once you understand the DOM, you can read content from a page, change what is displayed, add and remove elements, and respond to user actions.

The DOM is the reason JavaScript became the language of the web. Every interactive web application — every button that changes a color, every form that validates input, every live search result — is JavaScript manipulating the DOM.

Let us start with what the DOM actually is before we write a single line of code."

---

## [01:30 – 04:30] Part 1 — What Is the DOM?

**[SHOW SLIDE: "The Document Object Model"]**

"When the browser loads an HTML page, it parses the HTML text and builds a **tree of objects** in memory. This tree is the Document Object Model — the DOM. Each HTML element becomes a **node** in that tree. Each node is a JavaScript object with properties and methods you can read and modify.

**[SHOW DIAGRAM: HTML → DOM Tree]**

Here is a simple HTML document:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1 id="title">Hello</h1>
    <p class="intro">Welcome to the DOM.</p>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </body>
</html>
```

The browser turns this into a tree:

```text
document
  └── html
        ├── head
        │     └── title ('My Page')
        └── body
              ├── h1#title ('Hello')
              ├── p.intro ('Welcome to the DOM.')
              └── ul
                    ├── li ('Item 1')
                    └── li ('Item 2')
```

Every box in that diagram is a node object. The `document` object is the root — the entry point to the entire tree. Everything you do with the DOM starts from `document`.

[PAUSE]

**[DEMO — DevTools Elements panel]**

Open a page in Chrome, right-click any element, and choose 'Inspect'. The Elements panel shows you the DOM tree. This is the live DOM — when JavaScript modifies it, this panel updates in real time. Watch this as we run code in the next sections.

The key mental model:

- HTML is **text** — the source file
- The DOM is **objects in memory** — what the browser builds from the text
- JavaScript reads and writes the DOM — the browser re-renders whatever the DOM says"

---

## [04:30 – 09:00] Part 2 — Selecting Elements

**[SHOW SLIDE: "Selecting DOM Elements"]**

"Before you can change anything on the page, you need to select the element you want to work with. JavaScript gives you several methods for this.

**[DEMO]**

```javascript
// Select by ID — returns one element or null
const title = document.getElementById('title');
console.log(title);   // <h1 id="title">Hello</h1>

// Select by CSS selector — returns first match or null
const intro = document.querySelector('.intro');
console.log(intro);   // <p class="intro">Welcome to the DOM.</p>

// Select all matches — returns a NodeList (not a real Array)
const items = document.querySelectorAll('li');
console.log(items);          // NodeList(2) [li, li]
console.log(items.length);   // 2
```

[PAUSE]

Let me walk through each method.

`getElementById('id')` — takes an ID string, no `#` prefix. Returns the matching element, or `null` if not found. Fast and simple for single elements you have already assigned an ID.

`querySelector(selector)` — takes any CSS selector: `'#title'`, `'.intro'`, `'li'`, `'div > p'`, anything. Returns the **first** matching element, or `null`. This is the modern, versatile choice — one method handles all your selection needs.

`querySelectorAll(selector)` — same CSS selector syntax, returns **all** matches as a `NodeList`. A NodeList is array-like — it has a `length` and you can index into it — but it is not a real `Array`. You can convert it if needed:

```javascript
const itemArray = Array.from(document.querySelectorAll('li'));
itemArray.forEach(li => console.log(li.textContent));
```

[PAUSE]

**Checking for null:**

If no element matches, `getElementById` and `querySelector` return `null`. Trying to read a property of `null` throws a `TypeError`:

```javascript
const missing = document.getElementById('doesNotExist');
console.log(missing);              // null
console.log(missing.textContent);  // TypeError: Cannot read properties of null
```

Always guard when the element might not exist, especially if the ID or selector could change:

```javascript
const el = document.getElementById('myElement');
if (el) {
  el.textContent = 'Found it';
}
```

[PAUSE]

**Two additional selection methods (less common but you will see them in older code):**

```javascript
// By class name — returns HTMLCollection (live, array-like)
const intros = document.getElementsByClassName('intro');

// By tag name — returns HTMLCollection
const paragraphs = document.getElementsByTagName('p');
```

These return `HTMLCollection` objects, which are live (they update if the DOM changes). `querySelectorAll` returns a static `NodeList` (snapshot at time of call). In modern code, prefer `querySelector` and `querySelectorAll`."

---

## [09:00 – 14:00] Part 3 — Reading and Modifying Content

**[SHOW SLIDE: "textContent and innerHTML"]**

"Once you have an element, you can read and write its content.

**[DEMO — `textContent`]**

```javascript
const h1 = document.querySelector('h1');

// Read text content
console.log(h1.textContent);   // 'Hello'

// Write text content — replaces everything inside the element
h1.textContent = 'Welcome, JavaScript!';
// The page heading now reads: Welcome, JavaScript!
```

`textContent` reads or writes the **raw text** inside an element. It ignores any HTML tags inside the element, and when writing, it treats the new value as plain text — any `<` characters are treated as literal text, not HTML.

[PAUSE]

**[DEMO — `innerHTML`]**

```javascript
const intro = document.querySelector('.intro');

// Read innerHTML — includes any nested HTML tags as a string
console.log(intro.innerHTML);   // 'Welcome to the DOM.'

// Write innerHTML — parsed as HTML, can include tags
intro.innerHTML = 'This is <strong>important</strong>.';
// The browser parses the string and creates a <strong> child element
```

`innerHTML` reads or writes the **HTML content** inside an element. Writing to `innerHTML` causes the browser to parse the string and build new child nodes.

[PAUSE]

**The security warning — XSS:**

`innerHTML` is powerful but dangerous if the string contains user-provided content:

```javascript
// NEVER do this with user input:
const userInput = '<img src=x onerror="alert(\'hacked\')">';
element.innerHTML = userInput;   // Executes the onerror script!
```

This is a **Cross-Site Scripting (XSS)** vulnerability. The rule: never set `innerHTML` using data from user input, URL parameters, or any external source. Use `textContent` for plain text, or use safe DOM construction methods (which we cover in Module 11).

[PAUSE]

**[DEMO — Attributes]**

```javascript
const link = document.querySelector('a');

// Read an attribute
console.log(link.getAttribute('href'));   // 'https://example.com'

// Write an attribute
link.setAttribute('href', 'https://txwes.edu');

// Check existence
console.log(link.hasAttribute('target'));   // false

// Remove an attribute
link.removeAttribute('target');
```

Direct property shortcut — many common attributes have direct element properties:

```javascript
link.href = 'https://txwes.edu';    // same as setAttribute('href', ...)
link.id = 'mainLink';
link.title = 'Go to TXWES';
```

[PAUSE]

**[DEMO — `style` property]**

```javascript
const h1 = document.querySelector('h1');

// Set inline styles directly
h1.style.color = 'navy';
h1.style.fontSize = '2rem';
h1.style.backgroundColor = 'lightyellow';
```

CSS property names in JavaScript use **camelCase** — `background-color` becomes `backgroundColor`, `font-size` becomes `fontSize`.

Direct style manipulation works but is harder to maintain. Prefer toggling CSS classes instead (next section)."

---

## [14:00 – 18:00] Part 4 — `classList` and CSS Classes

**[SHOW SLIDE: "classList API"]**

"Changing inline styles from JavaScript tightly couples your JavaScript to your visual design. A better pattern: define your styles in CSS classes, then use JavaScript to add, remove, or toggle those classes.

**[DEMO — `classList`]**

```javascript
const box = document.querySelector('.box');

// Add a class
box.classList.add('highlight');

// Remove a class
box.classList.remove('highlight');

// Toggle — adds if absent, removes if present
box.classList.toggle('active');

// Check if a class is present
console.log(box.classList.contains('active'));   // true or false

// Replace one class with another
box.classList.replace('old-class', 'new-class');
```

[PAUSE]

**Why `classList` instead of `className`?**

```javascript
// Old approach — overwrites ALL classes
element.className = 'highlight';   // removes any other classes

// classList.add — adds to existing classes, preserves the rest
element.classList.add('highlight');
```

`className` is a string that holds all classes. Assigning to it replaces everything. `classList.add` surgically adds one class without disturbing the others.

**[DEMO — Practical toggle example]**

```html
<!-- HTML -->
<button id="modeBtn">Toggle Dark Mode</button>
<body id="page">...</body>
```

```javascript
// JavaScript
const btn = document.getElementById('modeBtn');
const page = document.getElementById('page');

btn.addEventListener('click', () => {
  page.classList.toggle('dark-mode');
});
```

```css
/* CSS */
.dark-mode {
  background-color: #1a1a1a;
  color: #ffffff;
}
```

Each click toggles the `dark-mode` class on the body. JavaScript controls **when** the class is applied; CSS controls **what** the class looks like. Clean separation."

---

## [18:00 – 21:00] Part 5 — Traversing the DOM

**[SHOW SLIDE: "DOM Traversal"]**

"Once you have an element, you can navigate to nearby elements using traversal properties. This lets you move up to the parent, down to children, or sideways to siblings — without re-querying the document.

**[DEMO]**

```javascript
const ul = document.querySelector('ul');

// Parent
console.log(ul.parentElement);     // the element containing ul (e.g., body or div)

// Children — HTMLCollection of direct child elements (no text nodes)
console.log(ul.children);          // HTMLCollection [li, li]
console.log(ul.children[0]);       // first <li>

// First and last child element
console.log(ul.firstElementChild);   // first <li>
console.log(ul.lastElementChild);    // last <li>

// Siblings
const firstLi = ul.firstElementChild;
console.log(firstLi.nextElementSibling);      // second <li>
console.log(firstLi.previousElementSibling);  // null — it's the first
```

[PAUSE]

**`children` vs `childNodes`:**

`children` returns only **element** nodes — ignores text nodes and comments. `childNodes` returns all node types including whitespace text nodes between tags, which is almost never what you want. Use `children`, `firstElementChild`, `lastElementChild`, `nextElementSibling`, and `previousElementSibling` in modern code."

---

## [21:00 – 22:00] Closing — Lab Preview

**[SHOW SLIDE: "Module 10 Lab Preview"]**

"The Module 10 lab has four parts.

Part 1 works with DOM selection — you will select elements by ID, class, tag, and CSS selector, compare the results, and practice null-checking.

Part 2 covers reading and writing content — you will use `textContent` and `innerHTML`, observe the difference, and practice safe vs unsafe use.

Part 3 covers `classList` — you will add, remove, toggle, and check classes on multiple elements and build a working style-toggle feature.

Part 4 puts it together — a page inspector exercise where you traverse the DOM tree, read content from parent/child/sibling nodes, and modify the page in response to those readings.

Read the reading guide before the lab — the DOM is a large topic and the guide covers several details the video did not have time for. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-1320 Introduction to JavaScript | Module 10 — Document Object Model (DOM) Basics]**

---

## Additional Resources

- [MDN — Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [MDN — Document.querySelector()](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [MDN — Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)
- [MDN — Element.textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent)
- [MDN — Element.innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
- [Eloquent JavaScript — Chapter 14: The Document Object Model](https://eloquentjavascript.net/14_dom.html)
