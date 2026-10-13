# Lab 02: Styling a Page with Flexbox and CSS Grid

**Course:** CIS-3340 Full Stack Web Development
**Module:** 02 - Modern CSS Layouts
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will create a `styles.css` file and apply it to the semantic HTML page you built in Lab 01. You will implement Flexbox for the header and navigation, CSS Grid for the two-column main layout, a responsive card gallery, and a Grid-based footer. You will use Chrome DevTools to inspect and verify your layout.

---

## Prerequisites

- Completed `index.html` from Lab 01 (or use the starter file provided below)
- VS Code or any text editor
- Google Chrome with DevTools

---

## Starter HTML (use this if Lab 01 is incomplete)

Create a file called `index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Ramsey College of Technology department homepage.">
  <title>Ramsey College of Technology</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <div class="header-brand">
      <h1>Ramsey College of Technology</h1>
    </div>
    <nav aria-label="Primary navigation">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/programs">Programs</a></li>
        <li><a href="/faculty">Faculty</a></li>
        <li><a href="/admissions">Admissions</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article class="main-content">
      <h2>Welcome to Ramsey College</h2>
      <p>We offer programs in computer science, cybersecurity, and data analytics.</p>
      <section class="programs-section">
        <h3>Featured Programs</h3>
        <div class="card-grid">
          <div class="card">
            <h4>BS Computer Science</h4>
            <p>Four-year program covering software engineering and cloud computing.</p>
          </div>
          <div class="card">
            <h4>BS Cybersecurity</h4>
            <p>Hands-on training in network defense and security operations.</p>
          </div>
          <div class="card">
            <h4>MS Data Analytics</h4>
            <p>Advanced coursework in machine learning and data visualization.</p>
          </div>
          <div class="card">
            <h4>Certificate: AWS Cloud</h4>
            <p>Eight-week intensive program aligned to AWS certifications.</p>
          </div>
        </div>
      </section>
    </article>

    <aside class="sidebar">
      <h2>Quick Resources</h2>
      <ul>
        <li><a href="/schedule">Class Schedule</a></li>
        <li><a href="/advising">Academic Advising</a></li>
        <li><a href="/tutoring">Tutoring Center</a></li>
        <li><a href="/labs">Computer Labs</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <div class="footer-col">
      <h3>Contact</h3>
      <address>1234 University Blvd, Fort Worth, TX 76105</address>
    </div>
    <div class="footer-col">
      <h3>Programs</h3>
      <ul>
        <li><a href="/programs/cs">Computer Science</a></li>
        <li><a href="/programs/cyber">Cybersecurity</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h3>Resources</h3>
      <ul>
        <li><a href="/library">Library</a></li>
        <li><a href="/career">Career Services</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <p>&copy; 2025 Ramsey College of Technology</p>
    </div>
  </footer>
</body>
</html>
```

---

## Part 1: Build the Stylesheet

Create a new file called `styles.css` in the same directory as `index.html`.

### Step 1: Global reset and base styles

Add the following at the top of `styles.css`. Do not skip these lines — every professional stylesheet starts here.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  font-family: system-ui, -apple-system, Segoe UI, sans-serif;
  margin: 0;
  padding: 0;
  color: #1a1a2e;
  background-color: #f8f9fa;
  line-height: 1.6;
}

a {
  color: inherit;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

h1, h2, h3, h4 {
  margin-top: 0;
}
```

### Step 2: Flexbox header

Style the `<header>` as a Flexbox container that places the brand on the left and the navigation on the right.

```css
header {
  background-color: #1a1a2e;
  color: white;
  padding: 0 2rem;
  /* TODO: Add display: flex */
  /* TODO: Add justify-content to push nav to the right */
  /* TODO: Add align-items to vertically center both children */
  /* TODO: Set min-height to 64px */
}

header h1 {
  font-size: 1.25rem;
  color: white;
  margin: 0;
}
```

Fill in the four TODO comments with the correct CSS declarations.

### Step 3: Flexbox navigation

Style the navigation links in a horizontal row with spacing.

```css
nav ul {
  /* TODO: Add display: flex */
  /* TODO: Add gap of 0.25rem */
}

nav a {
  display: block;
  padding: 0.5rem 0.75rem;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.85);
  border-radius: 4px;
  font-size: 0.9rem;
}

nav a:hover {
  background-color: rgba(255, 255, 255, 0.15);
  color: white;
}
```

### Step 4: CSS Grid main layout

Apply a two-column Grid to `<main>` with the article taking the remaining space and the sidebar fixed at 280px.

```css
main {
  /* TODO: Add display: grid */
  /* TODO: Set grid-template-columns to "1fr 280px" */
  /* TODO: Add gap of 2rem */
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}
```

### Step 5: Article and sidebar styles

```css
.main-content {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.sidebar {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
  align-self: start; /* prevents sidebar from stretching to article height */
}

.sidebar h2 {
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #666;
  margin-bottom: 1rem;
}

.sidebar a {
  display: block;
  padding: 0.5rem 0;
  border-bottom: 1px solid #f0f0f0;
  text-decoration: none;
  color: #1a1a2e;
}

.sidebar a:hover {
  color: #4361ee;
}
```

### Step 6: Responsive card grid

Style the program cards as a responsive CSS Grid that reflows without media queries.

```css
.card-grid {
  /* TODO: Add display: grid */
  /* TODO: Set grid-template-columns to repeat(auto-fill, minmax(200px, 1fr)) */
  /* TODO: Add gap of 1.25rem */
  margin-top: 1.5rem;
}

.card {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.25rem;
}

.card h4 {
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: #4361ee;
}

.card p {
  font-size: 0.875rem;
  color: #555;
  margin: 0;
}
```

### Step 7: Grid footer

Style the footer as a CSS Grid that creates four equal columns.

```css
footer {
  background-color: #1a1a2e;
  color: rgba(255, 255, 255, 0.8);
  padding: 3rem 2rem;
  /* TODO: Add display: grid */
  /* TODO: Set grid-template-columns to repeat(4, 1fr) */
  /* TODO: Add gap of 2rem */
  margin-top: 3rem;
}

.footer-col h3 {
  color: white;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}

.footer-col a {
  display: block;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  padding: 0.25rem 0;
  font-size: 0.875rem;
}

.footer-col a:hover {
  color: white;
}

.footer-col address {
  font-style: normal;
  font-size: 0.875rem;
  line-height: 1.6;
}
```

---

## Part 2: Verify with Chrome DevTools

### Step 8: Inspect the Flexbox header

In Chrome, right-click on the `<header>` element and select "Inspect." In the Elements panel, find the `<header>` rule in the Styles panel. Click the small flex icon next to `display: flex` to open the Flexbox overlay. Verify:

- Both children (`.header-brand` and `<nav>`) are shown as flex items
- There is space between them (space-between behavior)
- They are vertically centered

### Step 9: Inspect the CSS Grid main layout

Click on the `<main>` element. In the Elements panel, look for the grid badge next to the element. Click "grid" to enable the grid overlay. Verify:

- Two column tracks are visible: a wide article column and a 280px sidebar column
- The 2rem gap between them is visible as a shaded region

### Step 10: Test card grid reflow

Drag the browser window to reduce its width to approximately 600px. Observe the `.card-grid` reflow from four columns to two columns to one column as the window narrows. No media queries were needed because of the `minmax()` declaration.

---

## Deliverables

Submit the following to the Canvas assignment portal:

1. Your completed `styles.css` file
2. Your `index.html` file (with the `<link rel="stylesheet">` tag pointing to `styles.css`)
3. A screenshot of the desktop layout (at full browser width) showing the Flexbox header and two-column Grid main layout
4. A screenshot of the card grid at approximately 600px width showing the reflow behavior
5. A screenshot of the Chrome DevTools Grid overlay on the `<main>` element

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Global reset with `box-sizing: border-box` applied | 10 |
| Header uses `display: flex` with `justify-content: space-between` and `align-items: center` | 15 |
| Navigation uses `display: flex` with `gap` | 10 |
| Main uses `display: grid` with `1fr 280px` columns and `gap` | 20 |
| Card grid uses `repeat(auto-fill, minmax(200px, 1fr))` | 15 |
| Footer uses `display: grid` with four columns | 10 |
| Desktop screenshot shows correct two-column layout | 10 |
| Card grid reflow screenshot at 600px | 5 |
| Grid overlay DevTools screenshot | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: CSS Custom Properties for a Theme System

Extend your stylesheet to use CSS custom properties (variables) for colors and spacing so the visual theme can be changed from a single location.

1. At the top of `styles.css`, before all other rules, add a `:root` block declaring at least four custom properties:

```css
:root {
  --color-primary: #1a1a2e;
  --color-accent: #4361ee;
  --color-bg: #f8f9fa;
  --color-surface: #ffffff;
  --space-sm: 0.75rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
}
```

1. Replace every hard-coded color and spacing value in your existing rules with the appropriate custom property using `var(--property-name)`.
1. Add a second theme by writing a `[data-theme="dark"]` selector block that overrides the same custom properties with dark-mode values (dark background, light text).
1. In your HTML, add a `<button id="themeToggle">Toggle Theme</button>` to the header and a small inline `<script>` at the bottom of `<body>` that toggles `document.documentElement.dataset.theme` between `""` and `"dark"` on click. Verify the theme switches without a page reload.

### Challenge 2: Sticky Sidebar with Scroll Behavior

Make the sidebar stick to the top of the viewport as the user scrolls past the header.

1. Add the following properties to your `.sidebar` rule:

```css
.sidebar {
  position: sticky;
  top: 1rem;
}
```

1. Ensure the `<main>` grid container has `align-items: start` so the sidebar's grid cell height does not constrain the sticky behavior.
1. Add enough placeholder paragraph content to the `.main-content` article to make the page scrollable (at least 2000px of content height).
1. Open the page in Chrome and scroll down — verify that the sidebar remains visible at the top of the viewport while the article content scrolls past it.

### Reflection Questions

1. When you replaced hard-coded values with CSS custom properties, how does this approach reduce the effort required to apply a new visual theme compared to editing individual rule declarations?
2. Why does `position: sticky` require the parent grid container to have `align-items: start` or the sidebar item to have `align-self: start` to work correctly in a CSS Grid layout?
