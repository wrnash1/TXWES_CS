# Lab 03: Making the Layout Responsive

**Course:** CIS-3340 Full Stack Web Development
**Module:** 03 - Responsive Design
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will extend the stylesheet from Lab 02 with mobile-first media queries, a collapsible hamburger navigation, responsive typography using `clamp()`, and fluid images. You will test your implementation across three simulated device widths using Chrome DevTools.

---

## Prerequisites

- Completed `index.html` and `styles.css` from Lab 02
- Google Chrome with DevTools
- Basic familiarity with Chrome's Device Toolbar (Ctrl+Shift+M)

---

## Part 1: Refactor to Mobile-First

### Step 1: Audit and reorganize the stylesheet

Open `styles.css`. Currently, the main layout grid is applied unconditionally. We need to wrap it in a `min-width` media query and add a mobile base style.

Find the `main` CSS rule. Replace it with the following mobile-first version:

```css
/* Mobile base: single column */
main {
  display: block;
  padding: 1rem;
}

/* Tablet and up: two-column grid */
@media (min-width: 768px) {
  main {
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: 2rem;
    padding: 1.5rem 2rem;
    max-width: 1200px;
    margin: 1.5rem auto;
  }
}

/* Desktop: wider padding */
@media (min-width: 1200px) {
  main {
    padding: 2rem 4rem;
    margin: 2rem auto;
  }
}
```

### Step 2: Refactor card grid for mobile

The card grid currently uses `repeat(auto-fill, minmax(200px, 1fr))`. On a 375px phone with 1rem padding on each side, the available width is roughly 343px — just enough for one 200px card. Verify this looks clean at mobile size.

Add an explicit minimum column count for mobile:

```css
.card-grid {
  display: grid;
  grid-template-columns: 1fr;   /* single column on mobile */
  gap: 1rem;
  margin-top: 1.5rem;
}

@media (min-width: 480px) {
  .card-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}
```

### Step 3: Refactor footer for mobile

The footer currently has four fixed columns. Stack them on mobile:

```css
footer {
  background-color: #1a1a2e;
  color: rgba(255, 255, 255, 0.8);
  padding: 2rem 1rem;
  display: grid;
  grid-template-columns: 1fr;   /* stacked on mobile */
  gap: 2rem;
  margin-top: 2rem;
}

@media (min-width: 768px) {
  footer {
    grid-template-columns: repeat(2, 1fr);
    padding: 3rem 2rem;
  }
}

@media (min-width: 1024px) {
  footer {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

---

## Part 2: Hamburger Navigation

### Step 4: Add the toggle button to HTML

Open `index.html`. Inside the `<header>`, add a toggle button before the `<nav>` element:

```html
<header>
  <div class="header-brand">
    <h1>Ramsey College of Technology</h1>
  </div>

  <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
    &#9776;
  </button>

  <nav aria-label="Primary navigation">
    <ul class="nav-links">
      <li><a href="/">Home</a></li>
      <li><a href="/programs">Programs</a></li>
      <li><a href="/faculty">Faculty</a></li>
      <li><a href="/admissions">Admissions</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>
</header>
```

### Step 5: Add hamburger CSS

Add the following rules to `styles.css`. The mobile styles hide the nav links and show the toggle button. The tablet-and-up styles reverse this behavior.

```css
/* Mobile: hide nav links */
.nav-links {
  display: none;
  flex-direction: column;
  position: absolute;
  top: 64px;
  left: 0;
  right: 0;
  background: #1a1a2e;
  padding: 1rem;
  z-index: 100;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Open state — toggled by JavaScript */
.nav-links.open {
  display: flex;
}

/* Mobile: show toggle button */
.nav-toggle {
  display: block;
  background: none;
  border: 1px solid rgba(255, 255, 255, 0.4);
  color: white;
  padding: 0.4rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.25rem;
  line-height: 1;
}

/* Tablet and up: show inline nav, hide toggle */
@media (min-width: 768px) {
  .nav-links {
    display: flex !important;
    flex-direction: row;
    position: static;
    background: none;
    padding: 0;
    border: none;
    gap: 0.25rem;
  }

  .nav-toggle {
    display: none;
  }
}
```

### Step 6: Add the toggle JavaScript

At the bottom of `index.html`, just before `</body>`, add the toggle script:

```html
<script>
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  toggle.addEventListener('click', function () {
    const isOpen = navLinks.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen.toString());
  });
</script>
```

Note that `aria-expanded` updates to match the open state — this is the accessible toggle pattern required by WCAG 4.1.2.

---

## Part 3: Responsive Typography

### Step 7: Add fluid typography

Replace or supplement your heading font sizes with `clamp()` declarations:

```css
html {
  font-size: 100%;   /* 16px base — respects browser accessibility settings */
}

body {
  font-size: 1rem;
  line-height: 1.6;
}

h1 {
  font-size: clamp(1.25rem, 3.5vw, 2rem);
  margin: 0;
}

h2 {
  font-size: clamp(1.1rem, 2.5vw, 1.5rem);
}

h3 {
  font-size: clamp(1rem, 2vw, 1.25rem);
}

p {
  font-size: clamp(0.9rem, 1.5vw, 1rem);
}
```

### Step 8: Add fluid images

Add the following rule after your global reset:

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

---

## Part 4: Verify Across Breakpoints

### Step 9: Chrome DevTools device simulation

Open `index.html` in Chrome. Press F12 to open DevTools, then press Ctrl+Shift+M to activate the Device Toolbar.

Test at each of the following widths and verify the expected behavior:

| Width | Expected Behavior |
|---|---|
| 375px (iPhone SE) | Single-column layout; hamburger button visible; nav links hidden |
| 480px | Cards showing 2 columns; still single-column main layout |
| 768px (iPad) | Two-column main layout; inline navigation visible; hamburger hidden |
| 1024px | Full layout; footer shows 4 columns |
| 1440px | Wide desktop layout with maximum padding |

### Step 10: Test hamburger toggle

At 375px, click the hamburger button. Verify:

- The nav links slide open as a vertical menu
- The `aria-expanded` attribute on the button changes from `false` to `true` (check in Elements panel)
- Clicking the button again closes the menu

---

## Deliverables

Submit the following to the Canvas assignment portal:

1. Your completed `index.html` with the hamburger toggle button and JavaScript
2. Your completed `styles.css` with all mobile-first media queries
3. Screenshot at 375px showing single-column layout and hamburger button
4. Screenshot at 375px with the hamburger menu open showing vertical nav links
5. Screenshot at 768px showing the two-column grid layout with inline navigation
6. Screenshot at 1024px showing the four-column footer

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Mobile-first base styles (single-column block layout) | 15 |
| Tablet breakpoint media query adds two-column grid | 15 |
| Hamburger button with `aria-expanded` attribute present | 15 |
| Toggle JavaScript opens and closes the nav links | 15 |
| `clamp()` applied to at least two heading levels | 15 |
| `max-width: 100%; height: auto` on images | 5 |
| Footer stacks on mobile and expands to 4 columns at 1024px | 10 |
| Screenshots at all required breakpoints submitted | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Dark Mode with prefers-color-scheme

Implement an automatic dark mode using CSS custom properties and the `prefers-color-scheme` media query — no JavaScript required.

1. Add a `:root` block at the top of `styles.css` declaring light-mode custom properties for background, surface, text, and accent colors:

```css
:root {
  --color-bg: #f8f9fa;
  --color-surface: #ffffff;
  --color-text: #1a1a2e;
  --color-muted: #555555;
  --color-accent: #4361ee;
  --color-nav-bg: #1a1a2e;
}
```

1. Add a `@media (prefers-color-scheme: dark)` block that overrides the same properties with dark values:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0d1117;
    --color-surface: #161b22;
    --color-text: #c9d1d9;
    --color-muted: #8b949e;
    --color-accent: #58a6ff;
    --color-nav-bg: #010409;
  }
}
```

1. Replace all hard-coded color values in your existing CSS rules with the corresponding `var()` references.
1. In Chrome DevTools, open the Rendering tab (three-dot menu → More tools → Rendering), scroll to "Emulate CSS media feature prefers-color-scheme," and toggle between `light` and `dark`. Verify the page colors switch without a reload.

### Challenge 2: Container Query for the Card Component

Refactor the `.card` component to respond to its container's width rather than the viewport width, using a CSS container query.

1. Add `container-type: inline-size` to `.card-grid` to establish it as a query container:

```css
.card-grid {
  container-type: inline-size;
  container-name: card-grid;
}
```

1. Replace the `.card-grid` `@media` breakpoint rule with a `@container` rule so the cards reflow based on the grid container's own width, not the viewport:

```css
@container card-grid (min-width: 400px) {
  .card-grid {
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  }
}
```

1. Drag the browser window and observe that the card layout responds to the container width rather than the full viewport, allowing the cards to reflow even if the container is embedded inside a narrow sidebar.

### Reflection Questions

1. The dark mode implementation using `prefers-color-scheme` required no JavaScript. What advantage does this CSS-only approach have over a JavaScript toggle for users who visit the page for the first time?
2. Container queries respond to the element's own width rather than the viewport width. Describe a real-world scenario where a component should reflow based on its container size rather than the screen size.
