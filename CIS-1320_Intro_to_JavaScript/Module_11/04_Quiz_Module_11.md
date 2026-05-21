# Quiz: Module 11 - DOM Manipulation & Styling
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
What is the recommended method to add a new CSS class to an element without overwriting existing classes?
*   A) element.className = 'new-class'
*   B) element.classList.add('new-class')
*   C) element.setAttribute('class', 'new-class')
*   D) element.style.class = 'new-class'
*   **Correct Answer:** B) The `classList.add()` method appends the new class, preserving existing classes.
*   **Distractor Analysis:**
    *   *Why correct:* The `classList.add()` method appends the new class, preserving existing classes.
    *   className assignment and setAttribute overwrite the entire class attribute. style.class is invalid syntax.

---

**Question 2**
Which of the following most accurately describes `createElement` in JavaScript?
*   A) A method that selects an existing element from the DOM by its tag name and returns the first match
*   B) A `document` method that creates a new HTML element node in memory, ready to be configured and inserted into the DOM
*   C) A CSS property that instructs the browser to generate a new element when a pseudo-element selector matches
*   D) A method that copies an existing element and all its children into a new, independent element
*   **Correct Answer:** B) A `document` method that creates a new HTML element node in memory, ready to be configured and inserted into the DOM.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes `document.querySelector()` or `getElementsByTagName()`, not `createElement`.
    *   *Why B is correct:* `document.createElement("div")` produces a detached element object; it must be appended to the document tree to become visible.
    *   *Why C is incorrect:* CSS pseudo-elements (`::before`, `::after`) are a styling concept unrelated to the JS `createElement` method.
    *   *Why D is incorrect:* That describes `cloneNode(true)`, which copies an existing element rather than creating a fresh one.

---

**Question 3**
A developer runs this code:
```javascript
const btn = document.querySelector("#toggle");
const box = document.querySelector("#box");
btn.addEventListener("click", () => {
  box.classList.toggle("hidden");
});
```
What happens each time the button is clicked?
*   A) The `hidden` class is permanently added to `box` after the first click and cannot be removed.
*   B) The `hidden` class is added to `box` if it is not present, or removed if it is present, on each click.
*   C) All classes on `box` are removed and replaced with `hidden` on every click.
*   D) The `box` element is deleted from the DOM each time the button is clicked.
*   **Correct Answer:** B) The `hidden` class is added to `box` if it is not present, or removed if it is present, on each click.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `toggle` is designed to flip the class on and off; calling it again removes a class that was just added.
    *   *Why B is correct:* `classList.toggle("hidden")` adds `"hidden"` if absent or removes it if present — toggling the state on every invocation.
    *   *Why C is incorrect:* `toggle` only affects the named class; all other classes on the element remain untouched.
    *   *Why D is incorrect:* `classList.toggle` modifies the element's classes; it does not remove the element from the page.

---

**Question 4**
While working on **DOM Manipulation**, a developer needs to insert a new `<li>` element as the last child of a `<ul>`. Which sequence of operations is correct?
*   A) `document.insertBefore(li, ul)` → `li.textContent = "Item"`
*   B) `const li = document.createElement("li")` → `li.textContent = "Item"` → `ul.appendChild(li)`
*   C) `ul.setAttribute("child", li)` → `li.textContent = "Item"`
*   D) `document.querySelectorAll("ul").push(li)`
*   **Correct Answer:** B) `const li = document.createElement("li")` → `li.textContent = "Item"` → `ul.appendChild(li)`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `insertBefore` takes `(newNode, referenceNode)` where `referenceNode` is a child of the parent, not the parent itself; this usage is incorrect.
    *   *Why B is correct:* The standard pattern is: create the element, configure its content, then append it to the parent container.
    *   *Why C is incorrect:* `setAttribute` sets HTML attributes (like `id`, `class`, `src`); it cannot attach a child node as a child element.
    *   *Why D is incorrect:* `querySelectorAll` returns a NodeList, not an actual array; NodeLists do not have a `push` method, and this would not insert the element into the DOM anyway.

---

**Question 5**
How do you set an element's background color to `"blue"` using the `style` property in JavaScript?
*   A) `element.style["background-color"] = "blue";`
*   B) `element.style.backgroundColor = "blue";`
*   C) `element.setAttribute("background-color", "blue");`
*   D) Both A and B are valid ways to set the background color
*   **Correct Answer:** D) Both A and B are valid ways to set the background color.
*   **Distractor Analysis:**
    *   *Why A alone is incorrect as the only answer:* Bracket notation with the CSS hyphenated name works (JS evaluates the string), but B (camelCase) is the more common and readable form.
    *   *Why B alone is incorrect as the only answer:* While `element.style.backgroundColor` is the standard camelCase approach, bracket notation `element.style["background-color"]` is also valid.
    *   *Why C is incorrect:* `setAttribute("background-color", "blue")` sets an HTML attribute named `background-color`, which is not a valid HTML attribute; it does not change the element's style.
    *   *Why D is correct:* JavaScript's `style` object supports both camelCase property names (`backgroundColor`) and bracket notation with hyphenated CSS names (`"background-color"`); both correctly set the inline style.
