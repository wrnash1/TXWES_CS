# Video Script: Module 02 - Modern CSS Layouts

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 23 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with CSS file open; Chrome with DevTools layout overlay visible
- Use [SHOW CODE] cue to switch to full-screen VS Code
- Use [SHOW BROWSER] cue to switch to full-screen Chrome with Flexbox or Grid overlay enabled
- Enable the CSS Grid overlay in Chrome DevTools during grid demonstrations
- Keep a second browser tab with the unstyled HTML from Module 01 for before/after comparison

---

## Section 1: Introduction - Why CSS Layout Matters [00:00 - 03:30]

Welcome back. I am Professor Nash. In Module 01 we built a semantically correct HTML5 page — a clean, well-structured document that machines can read and understand. Today in Module 02 we make it look like a real application.

CSS layout is one of the most tested practical skills in any web developer interview. Interviewers ask you to center a div. They ask you to build a sidebar layout. They give you a Figma mockup and ask how you would implement it. The two tools that handle all of these are Flexbox and CSS Grid, and by the end of this module you will know exactly when to reach for each one.

This module connects to the AWS Developer Associate exam because the front-end assets you deploy to S3 and distribute through CloudFront include your CSS files alongside your HTML. A production build that breaks on a 768px tablet means a broken user experience in production. Understanding layout models makes you a better debugger when something looks wrong on a device you did not test.

[SHOW BROWSER]

Here is the semantic HTML page we built in Module 01 with no CSS applied. Let me show you what we will have by the end of this module — the same HTML, styled with Flexbox navigation, a two-column Grid layout, and a proper footer.

[SHOW CODE]

Let us open `styles.css` and start from scratch.

---

## Section 2: The Box Model Foundation [03:30 - 08:30]

[SHOW CODE]

Every CSS layout starts with the box model. Understanding the box model is the difference between layouts that just work and layouts where you constantly fight mysterious spacing.

```css
/* Apply border-box sizing globally — the standard for all modern projects */
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

By default, CSS uses `content-box` sizing: when you set `width: 300px`, that is only the content area. Padding and border are added on top of it. So a box with `width: 300px; padding: 20px; border: 2px solid` is actually 344px wide — guaranteed to break your grid math.

`border-box` changes the calculation: `width: 300px` means the total rendered width including padding and border. Content area shrinks to accommodate them. This is what every front-end developer adds to their stylesheet first, every time.

[SHOW BROWSER]

Watch the DevTools computed panel. I will click the element, expand the box model diagram, and show you the difference between content-box and border-box calculations in real time.

Now let us talk about `display`. This is the single most important CSS property for layout.

```css
/* Block elements stack vertically and fill available width */
div { display: block; }

/* Inline elements flow horizontally and only take up their content width */
span { display: inline; }

/* inline-block: flows inline but respects width/height settings */
img { display: inline-block; }

/* flex and grid activate layout contexts for children */
.container { display: flex; }
.grid-wrapper { display: grid; }
```

The key insight: `display` affects how the element participates in its parent's formatting context AND how its children are laid out.

---

## Section 3: Flexbox — One-Dimensional Layout [08:30 - 14:00]

[SHOW CODE]

Flexbox is a one-dimensional layout model. It manages items in either a row or a column — but not both simultaneously. Use Flexbox when you are arranging items in a line.

Let us style the navigation from our HTML:

```css
/* Flexbox navigation */
nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 1.5rem;
}

nav a {
  text-decoration: none;
  color: #1a1a2e;
  font-weight: 600;
  padding: 0.5rem 0.75rem;
}

nav a:hover {
  background-color: #e8f0fe;
  border-radius: 4px;
}
```

[SHOW BROWSER]

The navigation links are now in a horizontal row with consistent spacing. Notice the `gap` property — this is the modern replacement for margin hacks. It adds space between flex items without adding space at the edges.

[SHOW CODE]

The core Flexbox container properties:

```css
.flex-demo {
  display: flex;

  /* Direction: row (default) or column */
  flex-direction: row;

  /* Allow items to wrap to the next line if they overflow */
  flex-wrap: wrap;

  /* Alignment on the main axis (horizontal when row) */
  justify-content: space-between;

  /* Alignment on the cross axis (vertical when row) */
  align-items: center;

  /* Spacing between items */
  gap: 1rem;
}
```

The mental model: imagine a number line. `justify-content` positions items along that line. `align-items` positions items perpendicular to that line.

Flex item properties control how individual items grow and shrink:

```css
.flex-item {
  /* flex: grow shrink basis */
  flex: 1 1 200px;
  /* grow: can this item grow to fill available space? */
  /* shrink: can it shrink when space is tight? */
  /* basis: the starting size before growing/shrinking */
}

.flex-item-fixed {
  flex: 0 0 250px; /* fixed — does not grow or shrink */
}

.flex-item-greedy {
  flex: 2 1 0; /* grows twice as fast as flex:1 siblings */
}
```

**AWS Exam Tip:** The DVA-C02 exam does not test CSS directly, but exam scenarios that describe responsive front-end applications assume you know how static assets built with these tools are structured. When Elastic Beanstalk or Amplify deploys a build artifact, the CSS file that produces your layout is included in that artifact.

---

## Section 4: CSS Grid — Two-Dimensional Layout [14:00 - 19:30]

[SHOW CODE]

CSS Grid is a two-dimensional layout model. It manages items in rows and columns simultaneously. Use Grid when you are building a page layout with both horizontal and vertical structure.

Let us apply Grid to the page's main content area:

```css
/* Two-column layout: main content + sidebar */
main {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
```

[SHOW BROWSER]

Enable the CSS Grid overlay in DevTools. You can now see the column tracks, row tracks, and gap areas highlighted over the rendered page.

[SHOW CODE]

The `fr` unit is unique to Grid. It stands for "fraction" — `1fr` means "one share of the remaining available space." In `1fr 300px`, the second column is fixed at 300px, and the first column gets all the remaining space.

Grid placement properties:

```css
/* Explicit placement by line number */
.featured-article {
  grid-column: 1 / 3; /* spans from line 1 to line 3 — full width */
  grid-row: 1 / 2;
}

/* Named areas — the most readable Grid approach for page layouts */
.page-layout {
  display: grid;
  grid-template-areas:
    "header header"
    "nav    main  "
    "footer footer";
  grid-template-rows: auto 1fr auto;
  grid-template-columns: 220px 1fr;
}

header { grid-area: header; }
nav    { grid-area: nav; }
main   { grid-area: main; }
footer { grid-area: footer; }
```

Named template areas are the clearest way to build a full page layout. The ASCII-art structure in `grid-template-areas` directly mirrors what the user will see on screen.

`repeat()` and `auto-fill`:

```css
/* Responsive card grid — as many columns as fit */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}
```

`repeat(auto-fill, minmax(250px, 1fr))` creates as many columns as will fit, where each column is at least 250px wide. When the container narrows, columns drop automatically — no media query needed. This is the most powerful responsive pattern in CSS Grid.

[SHOW BROWSER]

Watch me resize the browser window. The card grid reflows from four columns to three to two to one seamlessly as the viewport narrows.

---

## Section 5: Flexbox vs. Grid and Lab Preview [19:30 - 23:00]

[SHOW CODE]

The practical decision rule:

- Use Flexbox when laying out items in one direction — navigation bars, button groups, vertically centered content, card rows.
- Use Grid when building the overall page structure — the relationship between header, sidebar, main content, and footer. Also use Grid for card grids where you want precise two-dimensional control.
- Use Grid's `repeat(auto-fill, minmax())` pattern for responsive card galleries that need to reflow without media queries.
- Use them together: a Grid-based page layout with Flexbox components inside each grid area.

Here is the complete stylesheet we built today as a reference:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  margin: 0;
  color: #1a1a2e;
  background-color: #f8f9fa;
}

header {
  background-color: #1a1a2e;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 1.5rem;
}

main {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

footer {
  background-color: #1a1a2e;
  color: white;
  padding: 2rem;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}
```

In the lab this week you are going to apply Flexbox and Grid to style the semantic HTML page you built in Lab 01. You will implement navigation Flexbox, a two-column main layout, and a responsive card section.

Thank you for watching. I will see you in Module 03, where we add media queries and make this layout fully responsive across all screen sizes.

---

## Additional Resources

- developer.mozilla.org — search "CSS Flexbox" and "CSS Grid Layout" for interactive guides with live examples
- aws.amazon.com/certification — review Domain 1 (Development with AWS Services) for front-end deployment context
