# Reading Guide: Module 02 - Modern CSS Layouts

**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers the two modern CSS layout systems that power every professional web application: Flexbox and CSS Grid. You will learn the box model, the `display` property, Flexbox container and item properties, Grid track definitions, named template areas, and responsive column patterns. These skills are directly applied in Module 03 (Responsive Design), Module 11 (React), and throughout the remaining front-end modules.

---

## 1. The CSS Box Model

Every HTML element is a rectangular box. The box model defines how that box's dimensions are calculated.

```css
/* Content-box sizing (browser default — avoid in production) */
.content-box {
  box-sizing: content-box;
  width: 300px;
  padding: 20px;
  border: 2px solid black;
  /* Actual rendered width: 300 + 20 + 20 + 2 + 2 = 344px */
}

/* Border-box sizing (use this in all production stylesheets) */
.border-box {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 2px solid black;
  /* Actual rendered width: 300px — padding and border fit inside */
}

/* Standard reset applied at the top of every stylesheet */
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

The box model consists of four layers from innermost to outermost:

| Layer | Property | Description |
|---|---|---|
| Content | `width`, `height` | The area that contains text, images, or child elements |
| Padding | `padding` | Space between content and the border; inherits background color |
| Border | `border` | The visible outline surrounding padding and content |
| Margin | `margin` | Space outside the border; transparent; collapses between siblings |

---

## 2. The Display Property

The `display` property determines two things: how an element participates in its parent's layout, and what layout model it applies to its own children.

| Value | Element behavior | Children layout |
|---|---|---|
| `block` | Takes full available width, stacks vertically | Normal flow |
| `inline` | Flows with text, ignores width/height | Inline formatting context |
| `inline-block` | Flows with text, respects width/height | Normal flow |
| `flex` | Block-level container | Flexbox layout |
| `inline-flex` | Inline-level container | Flexbox layout |
| `grid` | Block-level container | Grid layout |
| `none` | Element is removed from layout and accessibility tree | N/A |

---

## 3. Flexbox — One-Dimensional Layout

### Container Properties

```css
.flex-container {
  display: flex;

  /* Primary axis direction */
  flex-direction: row;            /* row | row-reverse | column | column-reverse */

  /* Whether items wrap to new lines */
  flex-wrap: wrap;                /* nowrap | wrap | wrap-reverse */

  /* Main axis alignment */
  justify-content: space-between; /* flex-start | flex-end | center |
                                     space-between | space-around | space-evenly */

  /* Cross axis alignment */
  align-items: center;            /* flex-start | flex-end | center |
                                     stretch | baseline */

  /* Gap between items */
  gap: 1rem;
}
```

### Item Properties

```css
.flex-item {
  /* Shorthand: flex: grow shrink basis */
  flex: 1 1 200px;   /* can grow, can shrink, starts at 200px */
  flex: 0 0 300px;   /* fixed size: no grow, no shrink */
  flex: 1;           /* grow:1 shrink:1 basis:0 */

  /* Override alignment for a single item */
  align-self: flex-end;

  /* Control visual order */
  order: 2;
}
```

### Common Flexbox Patterns

```css
/* Center an element horizontally and vertically */
.centered-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* Navigation bar with logo on left, links on right */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
}

/* Responsive card row that wraps below 250px per card */
.card-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.card-row .card {
  flex: 1 1 250px;
}
```

---

## 4. CSS Grid — Two-Dimensional Layout

### Defining Grid Tracks

```css
.grid-container {
  display: grid;

  /* Column definitions */
  grid-template-columns: 200px 1fr 1fr;
  grid-template-columns: repeat(3, 1fr);
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));

  /* Row definitions */
  grid-template-rows: auto 1fr auto;

  /* Spacing */
  gap: 1.5rem;
  column-gap: 2rem;
  row-gap: 1rem;
}
```

### Placing Items by Grid Lines

```css
.grid-item {
  grid-column: 1 / 3;   /* spans columns 1 and 2 */
  grid-column: 1 / -1;  /* spans full width */
  grid-row: 2 / 4;      /* spans rows 2 and 3 */
  grid-column: span 2;  /* spans 2 tracks from current position */
}
```

### Named Template Areas

```css
.page {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header "
    "sidebar content"
    "footer  footer ";
  min-height: 100vh;
}

header   { grid-area: header; }
.sidebar { grid-area: sidebar; }
main     { grid-area: content; }
footer   { grid-area: footer; }
```

### Responsive Grid Patterns

```css
/* Auto-fill: creates as many columns as fit at minimum 200px */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

/* Auto-fit: same as auto-fill but collapses empty trailing tracks */
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
}
```

---

## 5. CSS Layout Properties Reference

| Property | Context | Purpose |
|---|---|---|
| `display: flex` | Container | Activates Flexbox |
| `flex-direction` | Flex container | Sets main axis (row or column) |
| `justify-content` | Flex or Grid container | Distributes items on main or inline axis |
| `align-items` | Flex or Grid container | Aligns items on cross or block axis |
| `flex-wrap` | Flex container | Allows items to wrap to new lines |
| `gap` | Flex or Grid container | Spacing between items |
| `flex` | Flex item | Shorthand for grow, shrink, basis |
| `display: grid` | Container | Activates Grid |
| `grid-template-columns` | Grid container | Defines column track sizes |
| `grid-template-areas` | Grid container | Names regions for semantic placement |
| `grid-area` | Grid item | Places item in named area |
| `grid-column` | Grid item | Column placement by line numbers |
| `grid-row` | Grid item | Row placement by line numbers |

---

## 6. Spacing: Margin, Padding, and Gap

```css
/* Padding — internal space, inherits background */
.card {
  padding: 1.5rem;
  padding: 1rem 2rem;              /* top/bottom left/right */
  padding: 0.5rem 1rem 1.5rem 0;  /* top right bottom left */
}

/* Margin — external space, transparent */
.container {
  margin: 0 auto;   /* centers horizontally with explicit width */
}

/* Margin collapse: adjacent top/bottom margins merge */
/* p margin-bottom: 1rem + h2 margin-top: 2rem = 2rem gap (not 3rem) */

/* Gap in flex/grid: no collapse, cleaner than margin hacks */
.grid { gap: 1.5rem; }
```

---

## 7. Flexbox vs. Grid Decision Guide

| Situation | Recommended |
|---|---|
| Horizontal navigation bar | Flexbox |
| Centering one element in a container | Flexbox |
| Full-page layout with sidebar | CSS Grid |
| Responsive card gallery | CSS Grid with `auto-fill` |
| Form label-input pairs | Flexbox |
| Dashboard with multiple widget regions | CSS Grid |
| Stacked vertical components in a sidebar | Flexbox with `flex-direction: column` |

---

## 8. Exam and Interview Tips

1. The `box-sizing: border-box` global reset should be the first rule in every stylesheet. Layout math that "adds up wrong" is almost always a content-box issue.

2. `justify-content` aligns on the main axis. `align-items` aligns on the cross axis. Swapping these is the most common Flexbox mistake in interviews.

3. Use `gap` instead of `margin` on individual flex or grid items. Gap does not apply to the outer edges of the container, making spacing cleaner.

4. `repeat(auto-fill, minmax(250px, 1fr))` creates a responsive card grid with no media queries. Know this pattern — it appears in interviews and coding assessments regularly.

5. `display: none` removes an element from both the visual layout and the accessibility tree. Use `visibility: hidden` to preserve layout space while hiding an element visually.

6. In the DVA-C02 exam: CSS files deployed to S3 are static assets cached at CloudFront edge locations. After a deploy, run `aws cloudfront create-invalidation --paths "/*.css"` to flush the edge cache.

7. `margin: auto` centers a block element with an explicit `width` within its parent. This is still the most reliable horizontal centering pattern for block-level elements.

8. The `fr` unit divides available space after fixed-size tracks are subtracted. In `200px 1fr 2fr`, the 200px column is allocated first, then the remainder is split one-third to the middle and two-thirds to the last column.

---

## 9. Study Checklist

- [ ] Understand box model layers and why `border-box` is preferred
- [ ] Know the five main Flexbox container properties and their values
- [ ] Be able to write a `flex: grow shrink basis` declaration
- [ ] Understand when to use Flexbox vs. Grid
- [ ] Be able to write a named `grid-template-areas` page layout
- [ ] Know the `repeat(auto-fill, minmax())` responsive pattern
- [ ] Understand the difference between `auto-fill` and `auto-fit`
- [ ] Be able to center an element using both Flexbox and `margin: auto`
- [ ] Complete Lab 02 with DevTools Grid overlay verification
- [ ] Complete Quiz 02 and Discussion 02 before the module deadline

---

## 10. Supplemental Resources

The following free, open-access resources go deeper on Module 02 topics:

**1. MDN Web Docs — CSS Flexible Box Layout**
[https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout)
The authoritative reference for all Flexbox container and item properties, with interactive examples for `justify-content`, `align-items`, `flex-wrap`, and the `flex` shorthand.

**2. MDN Web Docs — CSS Grid Layout**
[https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
Comprehensive documentation covering grid tracks, named template areas, implicit vs. explicit grids, the `fr` unit, and the `repeat()` function with `auto-fill` and `auto-fit`.

**3. CSS-Tricks — A Complete Guide to Flexbox**
[https://css-tricks.com/snippets/css/a-guide-to-flexbox/](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
A widely-referenced visual guide illustrating every Flexbox property with diagrams. Particularly useful for understanding the main axis vs. cross axis distinction before exams.

**4. CSS-Tricks — A Complete Guide to CSS Grid**
[https://css-tricks.com/snippets/css/complete-guide-grid/](https://css-tricks.com/snippets/css/complete-guide-grid/)
The companion visual guide to CSS Grid, covering `grid-template-areas`, line-based placement, the `minmax()` function, and the difference between `auto-fill` and `auto-fit` with diagrams.
