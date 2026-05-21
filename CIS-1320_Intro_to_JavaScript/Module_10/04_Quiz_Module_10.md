# Quiz: Module 10 - Document Object Model (DOM) Basics
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
Which DOM query method returns a static NodeList of all elements matching a specified CSS selector group?
*   A) getElementById()
*   B) querySelector()
*   C) querySelectorAll()
*   D) getElementsByClassName()
*   **Correct Answer:** C) The `querySelectorAll()` method targets all elements matching a CSS selector and returns them in a NodeList.
*   **Distractor Analysis:**
    *   *Why correct:* The `querySelectorAll()` method targets all elements matching a CSS selector and returns them in a NodeList.
    *   getElementById returns a single element. querySelector returns only the first matching element. getElementsByClassName returns an HTMLCollection.

---

**Question 2**
Which of the following most accurately describes the **`document` object** in JavaScript?
*   A) An array containing all HTML elements on the page, ordered by their position in the source code
*   B) The global JavaScript object representing the entire HTML document, providing methods to access and create DOM elements
*   C) A browser-specific API available only in Chrome for debugging page structure
*   D) An object that stores CSS styles and applies them dynamically to elements when called
*   **Correct Answer:** B) The global JavaScript object representing the entire HTML document, providing methods to access and create DOM elements.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `document` is not an array; it is a complex object with methods and properties for interacting with the DOM tree.
    *   *Why B is correct:* `document` is the top-level entry point to the DOM, exposing `getElementById`, `querySelector`, `createElement`, and many other methods.
    *   *Why C is incorrect:* `document` is part of the standard Web API available in all modern browsers, not a Chrome-specific debug tool.
    *   *Why D is incorrect:* CSS style management is handled through `element.style` and CSS stylesheets; the `document` object covers structure, not just styling.

---

**Question 3**
A developer has the HTML `<h1 id="title">Hello</h1>` and wants to change its visible text to "Welcome" using JavaScript. Which code is correct and safest?
*   A) `document.getElementById("title").innerHTML = "<b>Welcome</b>";`
*   B) `document.getElementById("title").textContent = "Welcome";`
*   C) `document.querySelector("h1").id = "Welcome";`
*   D) `document.getElementByTagName("h1").text = "Welcome";`
*   **Correct Answer:** B) `document.getElementById("title").textContent = "Welcome";`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using `innerHTML` works here, but it parses the value as HTML and is a security risk if the value comes from user input; `textContent` is safer for plain text.
    *   *Why B is correct:* `textContent` sets the text without parsing HTML, making it the safe and correct choice for plain text replacement.
    *   *Why C is incorrect:* Setting `.id` changes the element's ID attribute, not its visible text content.
    *   *Why D is incorrect:* The correct method name is `getElementsByTagName` (plural, with an "s"); also, `.text` is not a standard DOM property for general elements.

---

**Question 4**
While working on **DOM Basics**, a developer writes `document.querySelector(".card")`. The page has five elements with class `card`. How many elements does this call return?
*   A) All five elements as an array
*   B) All five elements as a NodeList
*   C) Only the first matching element
*   D) `null`, because `querySelector` only works with ID selectors
*   **Correct Answer:** C) Only the first matching element.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `querySelector` never returns an array; to get multiple elements, use `querySelectorAll`.
    *   *Why B is incorrect:* A NodeList is returned by `querySelectorAll`, not `querySelector`.
    *   *Why C is correct:* `querySelector` always returns the **first** matching element in document order, even when many elements match the selector.
    *   *Why D is incorrect:* `querySelector` accepts any valid CSS selector including class selectors (`.card`), attribute selectors, tag names, and more.

---

**Question 5**
What is the key difference between `textContent` and `innerHTML` when setting the content of a DOM element?
*   A) `textContent` only works on `<p>` elements; `innerHTML` works on all elements
*   B) `innerHTML` treats the value as plain text; `textContent` parses it as HTML markup
*   C) `textContent` treats the value as plain text (safe for user input); `innerHTML` parses the value as HTML markup (risk of injection)
*   D) There is no difference; both properties produce identical results for all input values
*   **Correct Answer:** C) `textContent` treats the value as plain text (safe for user input); `innerHTML` parses the value as HTML markup (risk of injection).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Both properties are available on all element types, not just `<p>`.
    *   *Why B is incorrect:* The descriptions are reversed; `innerHTML` parses HTML, `textContent` does not.
    *   *Why C is correct:* Setting `textContent` to a string containing `<script>` renders it as visible text; setting `innerHTML` to the same string can execute the script.
    *   *Why D is incorrect:* They produce different results when the value contains HTML tags — `textContent` escapes them, `innerHTML` renders them.
