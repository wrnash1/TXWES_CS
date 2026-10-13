# Reading Guide: Module 03 - Responsive Design

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3340 &BULL; FULL STACK WEB DEVELOPMENT</text>
    
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


**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

Responsive design is the practice of building web layouts that adapt to any screen size from a single codebase. This module covers the viewport meta tag, CSS media queries, mobile-first strategy, responsive typography, fluid images, and the standard breakpoint system used throughout the rest of this course. Responsive skills are applied in every remaining module and are assumed in all React component labs.

---

## 1. The Viewport Meta Tag

The viewport meta tag is the bridge between HTML and CSS responsive behavior. Without it, mobile browsers use a virtual viewport of approximately 980px and scale the rendered page down to the physical screen width — producing a miniaturized desktop view.

```html
<!-- Required in every HTML file — place in <head> -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Attribute breakdown:

- `width=device-width` sets the viewport width to the device's actual screen width in CSS pixels
- `initial-scale=1.0` sets the initial zoom level to 100%
- Optional: `user-scalable=no` disables pinch-to-zoom — avoid this, as it violates WCAG 1.4.4

---

## 2. Media Query Syntax

Media queries are conditional CSS blocks that apply styles only when a defined condition is true. The primary condition is viewport width.

```css
/* Applies when viewport is at most 767px */
@media (max-width: 767px) {
  .sidebar { display: none; }
}

/* Applies when viewport is at least 768px */
@media (min-width: 768px) {
  .sidebar { display: block; }
}

/* Applies between 768px and 1023px */
@media (min-width: 768px) and (max-width: 1023px) {
  .sidebar { width: 200px; }
}

/* Device orientation */
@media (orientation: landscape) {
  .hero { min-height: 60vh; }
}

/* User color scheme preference */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a2e;
    --text: #e0e0e0;
  }
}

/* Reduced motion — disable animations for vestibular disorder users */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    transition: none !important;
    animation: none !important;
  }
}
```

---

## 3. Mobile-First vs. Desktop-First Strategy

### Mobile-First (recommended)

Write base styles for the smallest screen. Use `min-width` media queries to progressively add complexity for larger screens.

```css
/* Base: single column on all screens */
.main-layout {
  display: block;
  padding: 1rem;
}

/* Tablet: add sidebar */
@media (min-width: 768px) {
  .main-layout {
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: 2rem;
  }
}

/* Desktop: wider spacing */
@media (min-width: 1200px) {
  .main-layout {
    padding: 2rem 4rem;
  }
}
```

### Desktop-First (legacy)

Write styles for large screens first. Use `max-width` media queries to simplify for smaller screens.

```css
/* Base: two-column layout on all screens */
.main-layout {
  display: grid;
  grid-template-columns: 1fr 280px;
}

/* Mobile: collapse to single column */
@media (max-width: 767px) {
  .main-layout {
    display: block;
  }
}
```

Mobile-first is preferred because:

- Mobile browsers parse less CSS by default (better performance)
- Google uses mobile-first indexing for search ranking
- Progressive enhancement is a safer strategy than progressive reduction

---

## 4. Standard Breakpoints

| Breakpoint | Min-Width | Target Devices |
|---|---|---|
| Mobile | 0px | Phones (portrait) |
| Large mobile | 480px | Phones (landscape), small tablets |
| Tablet | 768px | Tablets (portrait), iPad |
| Laptop | 1024px | Laptops, tablets (landscape) |
| Desktop | 1200px | Desktop monitors |
| Wide | 1440px | Large monitors, ultrawide |

Do not add breakpoints for specific device models. Add breakpoints where the layout breaks — open DevTools, slowly drag the viewport wider, and add a breakpoint at the pixel value where the layout stops looking correct.

---

## 5. Responsive Navigation Patterns

### Flexbox Navigation (tablet and desktop)

```css
nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 0.25rem;
}

nav a {
  display: block;
  padding: 0.5rem 0.75rem;
  text-decoration: none;
  color: white;
  border-radius: 4px;
}

nav a:hover,
nav a[aria-current="page"] {
  background-color: rgba(255, 255, 255, 0.15);
}
```

### Hamburger Menu (mobile)

```css
/* Mobile base: hide nav links, show toggle button */
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
}

.nav-links.open {
  display: flex;
}

.nav-toggle {
  display: block;
  background: none;
  border: 2px solid rgba(255, 255, 255, 0.5);
  color: white;
  padding: 0.4rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.25rem;
}

/* Tablet and up: show inline nav, hide toggle */
@media (min-width: 768px) {
  .nav-links {
    display: flex !important;
    flex-direction: row;
    position: static;
    background: none;
    padding: 0;
  }

  .nav-toggle {
    display: none;
  }
}
```

---

## 6. Responsive Typography

### Relative Units

| Unit | Relative to | Best Use |
|---|---|---|
| `rem` | Root element `font-size` | Body text, headings — respects user's browser font preferences |
| `em` | Parent element `font-size` | Component-scoped spacing (padding, margin) |
| `vw` | Viewport width | Large hero text, full-bleed elements |
| `vh` | Viewport height | Full-screen sections, hero areas |
| `%` | Parent element dimension | Fluid widths and heights |
| `px` | Fixed pixel | Borders, icons, minimum sizes |

### Fluid Typography with clamp()

```css
/* clamp(minimum, preferred, maximum) */
h1 {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
}
/* At 375px: 4vw = 15px — below minimum (24px), so clamps to 1.5rem */
/* At 768px: 4vw = 30.72px — within range */
/* At 1440px: 4vw = 57.6px — above maximum (40px), so clamps to 2.5rem */

p {
  font-size: clamp(0.9rem, 1.5vw, 1.125rem);
}
```

### Accessible Font Sizing

```css
html {
  font-size: 100%; /* equals 16px by default; respects browser font size setting */
}

/* Never set font-size on html to px — this overrides the user's accessibility preference */
/* This is wrong: */
html { font-size: 14px; } /* blocks browser zoom-based font scaling */
```

---

## 7. Fluid Images and the picture Element

```css
/* Make all images responsive by default */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Responsive container with aspect ratio */
.video-wrapper {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

```html
<!-- Art-directed responsive images with <picture> -->
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.jpg" width="1440" height="600">
  <source media="(min-width: 768px)"  srcset="hero-tablet.jpg"  width="768"  height="400">
  <img src="hero-mobile.jpg"
       alt="Students collaborating in the Ramsey College computer lab"
       width="375" height="300">
</picture>
```

---

## 8. CSS Custom Properties (Variables) for Responsive Theming

```css
:root {
  /* Default (mobile) spacing scale */
  --space-sm: 0.75rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;

  /* Layout */
  --content-max: 1200px;
  --sidebar-width: 280px;
  --nav-height: 64px;
}

@media (min-width: 768px) {
  :root {
    --space-md: 1.5rem;
    --space-lg: 2rem;
    --space-xl: 3rem;
  }
}
```

Using variables for spacing means a single media query change propagates throughout the entire design system automatically.

---

## 9. Exam and Interview Tips

1. The `@media (max-width)` pattern is desktop-first. The `@media (min-width)` pattern is mobile-first. Interviewers ask this question directly — know the difference.

2. The viewport meta tag must be present for CSS media queries to fire correctly on mobile devices. Without it, the virtual 980px viewport prevents mobile breakpoints from matching.

3. `rem` is the preferred unit for font sizes because it honors the user's browser font-size preference. `px` overrides this preference and violates WCAG 1.4.4.

4. The `prefers-reduced-motion` media query is not just about aesthetics — it is a legal accessibility requirement for enterprise and government applications deployed on AWS.

5. `clamp(min, preferred, max)` creates fluid values that scale between a minimum and maximum without any media queries. Use it for font sizes and spacing in design systems.

6. In a DVA-C02 deployment question: after uploading responsive CSS to S3, a CloudFront cache invalidation is needed for the CSS files. The HTML `<meta name="viewport">` tag does not require a CDN change — it is part of the HTML file which may itself be separately invalidated.

7. `@media (prefers-color-scheme: dark)` allows you to implement dark mode without JavaScript by using CSS custom properties that change their values in the dark media query block.

8. Never add a breakpoint at every common device width. Add breakpoints at the specific pixel values where your layout breaks during testing.

---

## 10. Study Checklist

- [ ] Understand what the viewport meta tag does and why it is required for responsive design
- [ ] Know the difference between mobile-first (`min-width`) and desktop-first (`max-width`) strategies
- [ ] Memorize the five standard breakpoints (480, 768, 1024, 1200, 1440)
- [ ] Be able to write a hamburger navigation with CSS-only toggle behavior
- [ ] Understand when to use `rem`, `em`, `vw`, `vh`, `%`, and `px`
- [ ] Know the `clamp(min, preferred, max)` function and write an example
- [ ] Apply `max-width: 100%; height: auto` to make images responsive
- [ ] Understand `prefers-reduced-motion` and its accessibility importance
- [ ] Complete Lab 03 with DevTools device simulation verification
- [ ] Complete Quiz 03 and Discussion 03 before the module deadline

---

## 11. Supplemental Resources

The following free, open-access resources go deeper on Module 03 topics:

**1. MDN Web Docs — Using media queries**
[https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries)
Comprehensive reference covering media query syntax, all available media features (width, orientation, prefers-color-scheme, prefers-reduced-motion, hover, pointer), and combining conditions with `and`, `or`, and `not`.

**2. MDN Web Docs — clamp()**
[https://developer.mozilla.org/en-US/docs/Web/CSS/clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)
Full documentation for the `clamp(min, preferred, max)` function with interactive examples. Covers usage for fluid typography, spacing, and container sizing without media queries.

**3. web.dev — Responsive design (Google)**
[https://web.dev/learn/design](https://web.dev/learn/design)
Google's free responsive design course covering the viewport, media queries, typography, images, the picture element, and CSS Grid — directly aligned to this module's content and the DVA-C02 deployment context.

**4. The Odin Project — Responsive Design**
[https://www.theodinproject.com/lessons/node-path-advanced-html-and-css-introduction-to-responsive-design](https://www.theodinproject.com/lessons/node-path-advanced-html-and-css-introduction-to-responsive-design)
A free, project-based lesson covering mobile-first methodology, natural responsiveness, and responsive images with hands-on exercises that complement the Lab 03 hamburger navigation work.
