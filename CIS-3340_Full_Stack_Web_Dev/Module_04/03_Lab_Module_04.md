# Lab 04: JavaScript DOM Manipulation

**Course:** CIS-3340 Full Stack Web Development
**Module:** 04 - JavaScript DOM Manipulation
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will add three interactive JavaScript features to the Ramsey College of Technology page: a live card search filter, a dark mode toggle that persists to `localStorage`, and an accordion FAQ section. All functionality is implemented using vanilla JavaScript DOM APIs — no libraries or frameworks.

---

## Prerequisites

- Completed `index.html` and `styles.css` from Lab 03 (or use the provided starter files)
- Google Chrome with DevTools
- A text editor (VS Code recommended)

---

## Starter HTML Additions

Add the following sections to your `index.html` before the `<footer>`:

```html
<!-- Search bar above the card grid -->
<div class="search-bar">
  <label for="search-input" class="sr-only">Search programs</label>
  <input type="text"
         id="search-input"
         placeholder="Search programs..."
         autocomplete="off">
  <span id="result-count" aria-live="polite"></span>
</div>

<!-- Theme toggle button in the header -->
<!-- Add this inside <header>, after the nav -->
<button id="theme-toggle" aria-label="Toggle dark mode">
  Dark Mode
</button>

<!-- FAQ accordion section — add inside <main>, below the article -->
<section class="faq-section">
  <h2>Frequently Asked Questions</h2>

  <div class="accordion">
    <button class="accordion-btn" aria-expanded="false">
      What programming languages are taught?
    </button>
    <div class="accordion-panel" hidden>
      <p>Our programs teach Python, JavaScript, Java, and SQL. Advanced
         electives cover Rust, Go, and TypeScript.</p>
    </div>
  </div>

  <div class="accordion">
    <button class="accordion-btn" aria-expanded="false">
      Is financial aid available?
    </button>
    <div class="accordion-panel" hidden>
      <p>Yes. All students are eligible for federal financial aid through FAFSA.
         Merit scholarships are available for students with a 3.5 GPA or higher.</p>
    </div>
  </div>

  <div class="accordion">
    <button class="accordion-btn" aria-expanded="false">
      Are courses available online?
    </button>
    <div class="accordion-panel" hidden>
      <p>We offer hybrid and fully online formats for most programs.
         Lab-intensive courses require at least one on-campus session per week.</p>
    </div>
  </div>
</section>
```

Add this CSS to `styles.css`:

```css
/* Screen-reader-only utility class */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Search bar */
.search-bar {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

#search-input {
  flex: 1;
  padding: 0.6rem 1rem;
  border: 2px solid #dee2e6;
  border-radius: 6px;
  font-size: 1rem;
  font-family: inherit;
  max-width: 400px;
}

#search-input:focus {
  outline: none;
  border-color: #4361ee;
}

#result-count {
  font-size: 0.875rem;
  color: #666;
}

/* Dark mode */
body.dark-mode {
  background: #1a1a2e;
  color: #e0e0e0;
}

body.dark-mode .card,
body.dark-mode .main-content,
body.dark-mode .sidebar {
  background: #2d2d44;
  border-color: #444;
  color: #e0e0e0;
}

body.dark-mode header,
body.dark-mode footer {
  background: #0f0f1a;
}

/* Accordion */
.faq-section {
  margin-top: 2rem;
}

.accordion {
  border: 1px solid #dee2e6;
  border-radius: 6px;
  margin-bottom: 0.5rem;
  overflow: hidden;
}

.accordion-btn {
  width: 100%;
  text-align: left;
  padding: 1rem 1.25rem;
  background: #f8f9fa;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-family: inherit;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.accordion-btn::after {
  content: '+';
  font-size: 1.25rem;
  font-weight: 300;
  transition: transform 0.2s;
}

.accordion-btn[aria-expanded="true"]::after {
  transform: rotate(45deg);
}

.accordion-panel {
  padding: 0 1.25rem;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.25s ease, padding 0.25s ease;
}

.accordion-panel:not([hidden]) {
  max-height: 300px;
  padding: 1rem 1.25rem;
}
```

---

## Part 1: Card Search Filter

Create a new file called `app.js` in the same directory as `index.html`. Add a `<script src="app.js" defer></script>` tag in the `<head>` of `index.html`.

### Step 1: Write the filterCards function

In `app.js`, implement the `filterCards` function. The function should:

- Accept a `query` string parameter
- Iterate over all `.card` elements using `querySelectorAll`
- For each card, check whether the query string appears in the card's `<h4>` text or `<p>` text (case-insensitive)
- Show matching cards and hide non-matching cards by setting `card.style.display`
- Update the `#result-count` span with the count of visible cards

Starter code — fill in the TODO sections:

```javascript
document.addEventListener('DOMContentLoaded', function () {

  const searchInput = document.querySelector('#search-input');
  const counter     = document.querySelector('#result-count');

  function filterCards(query) {
    const cards = document.querySelectorAll('.card');
    let visibleCount = 0;

    // TODO: normalize query to lowercase and trim whitespace

    cards.forEach(function (card) {
      // TODO: get the h4 text and p text from each card (lowercase)
      const titleText = '';  // replace with correct code
      const bodyText  = '';  // replace with correct code

      // TODO: determine if the card matches the query
      const isMatch = false; // replace with correct boolean expression

      // TODO: show or hide the card based on isMatch
      // Hint: set card.style.display to '' (empty string) to show,
      //       or 'none' to hide

      if (isMatch) visibleCount++;
    });

    // TODO: update counter.textContent with visibleCount
    // Use a ternary to pluralize "program" vs "programs"
  }

  // TODO: add 'input' event listener on searchInput that calls filterCards
  //       with the current input value

  // TODO: add 'keydown' event listener on searchInput that clears the field
  //       and calls filterCards('') when the Escape key is pressed

  // TODO: call filterCards('') once to initialize the count display

```

### Step 2: Test the search filter

Open `index.html` in Chrome. In the search box, type "security." Verify that only the cybersecurity card is visible and the counter shows "1 program found." Press Escape — all cards return and the counter updates.

---

## Part 2: Dark Mode Toggle

### Step 3: Implement the theme toggle

Continue in `app.js`. After the search code, implement the dark mode toggle.

```javascript
  // --- Dark Mode Toggle ---
  const themeToggle = document.querySelector('#theme-toggle');

  // TODO: add 'click' event listener to themeToggle that:
  //   1. Toggles the 'dark-mode' class on document.body
  //   2. Reads whether the class is now present (classList.contains)
  //   3. Stores 'dark' or 'light' in localStorage under the key 'theme'
  //   4. Updates themeToggle.textContent to 'Light Mode' or 'Dark Mode'

  // TODO: on DOMContentLoaded, read localStorage.getItem('theme')
  //       If the value is 'dark', add 'dark-mode' to document.body
  //       and set themeToggle.textContent to 'Light Mode'

```

### Step 4: Test dark mode persistence

Click "Dark Mode" — the page background should change. Reload the page — the dark mode should still be active (loaded from localStorage). Click "Light Mode" — the background returns to light. Reload — light mode is preserved.

---

## Part 3: Accordion FAQ

### Step 5: Implement the accordion

Implement the accordion using event delegation on the `.faq-section` element.

```javascript
  // --- Accordion ---
  const faqSection = document.querySelector('.faq-section');

  faqSection.addEventListener('click', function (event) {
    const btn = event.target.closest('.accordion-btn');
    if (!btn) return;

    const panel = btn.nextElementSibling;

    // TODO: Check if the panel is currently open
    //       (hint: check btn.getAttribute('aria-expanded') === 'true')
    const isOpen = false; // replace with correct code

    // TODO: If the panel is open, close it:
    //   - set btn.setAttribute('aria-expanded', 'false')
    //   - set panel.hidden = true

    // TODO: If the panel is closed, open it:
    //   - set btn.setAttribute('aria-expanded', 'true')
    //   - set panel.hidden = false
  });

```

Close the enclosing `DOMContentLoaded` callback with a `});` after the accordion code.

### Step 6: Test the accordion

Click the first accordion question — the panel opens and the `+` rotates to `×`. Click it again — the panel closes. Click a different question — it opens independently. Verify in DevTools that `aria-expanded` changes on the button when toggled.

---

## Part 4: Verify with DevTools

### Step 7: Console verification

Open DevTools Console. Paste the following and verify each statement returns the expected result:

```javascript
// Should return a non-null element
document.querySelector('#search-input');

// Should return the aria-expanded value 'false'
document.querySelector('.accordion-btn').getAttribute('aria-expanded');

// After clicking first accordion: should return 'true'
document.querySelector('.accordion-btn').getAttribute('aria-expanded');
```

---

## Deliverables

Submit the following to Canvas:

1. `app.js` with all three features implemented
2. `index.html` with starter HTML additions and `<script src="app.js" defer>`
3. `styles.css` with dark mode and accordion styles added
4. Screenshot: search input showing "security" with only one card visible
5. Screenshot: dark mode active (dark background)
6. Screenshot: one accordion panel open with `aria-expanded="true"` visible in DevTools Elements panel

---

## Grading Rubric

| Criterion | Points |
|---|---|
| `filterCards` correctly shows and hides cards based on query | 20 |
| Counter updates with correct count and pluralization | 10 |
| Escape key clears search and resets cards | 10 |
| Dark mode toggle adds/removes `dark-mode` class | 15 |
| Dark mode preference persists across page reloads via `localStorage` | 10 |
| Accordion opens and closes with correct `aria-expanded` attribute | 20 |
| Event delegation used for accordion (one listener on `.faq-section`) | 10 |
| Required screenshots submitted | 5 |
| **Total** | **100** |
