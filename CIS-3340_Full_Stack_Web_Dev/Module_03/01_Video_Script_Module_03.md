# Video Script: Module 03 - Responsive Design

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 21 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with CSS file and Chrome side by side
- Use [SHOW CODE] to switch to VS Code; use [SHOW BROWSER] to switch to Chrome
- Use Chrome DevTools Device Toolbar (Ctrl+Shift+M) to demonstrate viewport sizes
- Show presets: iPhone SE (375px), iPad (768px), desktop (1440px)
- Keep DevTools open with device simulation active throughout browser demos

---

## Section 1: Introduction - Responsive Design as a Production Requirement [00:00 - 03:30]

Welcome to Module 03. I am Professor Nash. Today we complete the front-end trilogy — HTML structure in Module 01, CSS layout in Module 02, and now in Module 03 we make everything responsive across every device.

Responsive design is not optional. As of 2024, over 60 percent of global web traffic originates from mobile devices. Google uses mobile-first indexing — it crawls and ranks the mobile version of your site, not the desktop version. When you deploy to AWS and serve traffic through CloudFront, your users arrive on phones, tablets, laptops, and ultrawide monitors. Your layout needs to work on all of them with a single codebase.

This module introduces three interconnected tools: the viewport meta tag (which we set up in Module 01), CSS media queries, and mobile-first design strategy. Together they give you complete control over how your layouts transform across screen sizes.

**AWS Exam Tip:** When a DVA-C02 scenario describes deploying a public-facing React app to S3 and CloudFront, "the app looks broken on mobile" is a symptom that maps to two possible root causes: missing viewport meta tag, or CSS media queries not firing correctly because the viewport meta tag is absent. Know both.

[SHOW BROWSER]

Let me start by opening the page we built in Lab 02 and simulating a mobile device.

---

## Section 2: The Viewport and Mobile-First Strategy [03:30 - 08:00]

[SHOW BROWSER]

Here is our two-column layout at full desktop width. Now let me open DevTools, press Ctrl+Shift+M to enter device simulation, and select iPhone SE at 375 pixels.

The sidebar is squished against the content. The navigation items overflow. The cards are too narrow to read. This is what a desktop-first layout looks like when viewed on mobile without media queries.

[SHOW CODE]

There are two strategies for writing responsive CSS:

Desktop-first: Write styles for the largest screen first, then use `max-width` media queries to override them for smaller screens.

Mobile-first: Write base styles for the smallest screen, then use `min-width` media queries to progressively enhance the layout for larger screens.

Mobile-first is the industry standard. Here is why: mobile browsers parse CSS from top to bottom. With mobile-first, the base styles are lean and simple — the phone does minimal work. Desktop enhancements are added only when the viewport is large enough to need them.

```css
/* Mobile-first: base styles apply to all sizes */
.main-layout {
  display: block;   /* single column on mobile */
  padding: 1rem;
}

/* Tablet and up: add the sidebar */
@media (min-width: 768px) {
  .main-layout {
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: 2rem;
    padding: 2rem;
  }
}

/* Desktop: wider padding */
@media (min-width: 1200px) {
  .main-layout {
    padding: 2rem 4rem;
  }
}
```

Read this as: by default, `.main-layout` is a single-column block layout. At 768px and above, it becomes a two-column grid. At 1200px and above, it gets wider padding.

---

## Section 3: Media Query Syntax and Breakpoints [08:00 - 13:30]

[SHOW CODE]

The `@media` rule syntax:

```css
/* Width conditions */
@media (max-width: 767px)  { /* applies up to 767px  — mobile only  */ }
@media (min-width: 768px)  { /* applies from 768px up — tablet+     */ }
@media (min-width: 1024px) { /* applies from 1024px up — laptop+    */ }
@media (min-width: 1440px) { /* applies from 1440px up — wide       */ }

/* Combining conditions */
@media (min-width: 768px) and (max-width: 1023px) {
  /* tablet only — 768px to 1023px */
}

/* Orientation */
@media (orientation: landscape) {
  /* applies in landscape mode on any device */
}

/* Dark mode preference */
@media (prefers-color-scheme: dark) {
  body { background: #1a1a2e; color: white; }
}

/* Reduced motion — important for animations and transitions */
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; animation: none !important; }
}
```

Standard breakpoints used in this course:

- 480px — large mobile
- 768px — tablet (iPad portrait)
- 1024px — laptop
- 1200px — desktop
- 1440px — wide desktop

You do not need to use all of them. Add a breakpoint only when the layout actually breaks at that size — not because a specific pixel value is "standard."

**AWS Exam Tip:** `prefers-reduced-motion` is a WCAG 2.3.3 AAA guideline. For enterprise applications deployed on AWS that serve users with vestibular disorders, disabling animations under this media query is a legal and accessibility best practice.

---

## Section 4: Responsive Navigation and Typography [13:30 - 18:00]

[SHOW CODE]

The navigation is the component that most frequently breaks on mobile. Let us implement a hamburger-style toggle navigation.

```css
/* Mobile: hide nav links by default */
.nav-links {
  display: none;
  flex-direction: column;
  gap: 0;
  position: absolute;
  top: 64px;
  left: 0;
  right: 0;
  background: #1a1a2e;
  padding: 1rem;
}

.nav-links.open {
  display: flex;
}

/* Mobile: show hamburger button */
.nav-toggle {
  display: block;
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
}

/* Tablet and up: show links, hide hamburger */
@media (min-width: 768px) {
  .nav-links {
    display: flex !important;
    flex-direction: row;
    position: static;
    background: none;
    padding: 0;
    gap: 0.25rem;
  }

  .nav-toggle {
    display: none;
  }
}
```

Responsive typography uses relative units that scale with device context:

```css
/* Base typography — rem scales with browser font size preference */
html {
  font-size: 16px;  /* establishes 1rem = 16px */
}

body {
  font-size: 1rem;     /* 16px */
  line-height: 1.6;
}

h1 { font-size: 1.75rem; }  /* 28px */
h2 { font-size: 1.4rem; }   /* 22.4px */
h3 { font-size: 1.15rem; }  /* 18.4px */

/* Fluid typography: scales between a minimum and maximum */
h1 {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  /* minimum: 1.5rem | preferred: 4% of viewport width | maximum: 2.5rem */
}
```

`clamp(min, preferred, max)` is one of the most powerful modern CSS functions. It produces fluid typography that scales with the viewport between defined limits — no media queries required for font sizing.

---

## Section 5: Fluid Images and Lab Preview [18:00 - 21:00]

[SHOW CODE]

Images need one rule to become responsive:

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

`max-width: 100%` prevents images from overflowing their container. `height: auto` preserves the aspect ratio as the width scales. `display: block` removes the small gap below inline images caused by baseline alignment.

For the `<picture>` element with art direction — different crops for different screens:

```css
/* The HTML handles the responsive source selection */
```

```html
<picture>
  <source media="(min-width: 768px)" srcset="hero-desktop.jpg">
  <source media="(min-width: 480px)" srcset="hero-tablet.jpg">
  <img src="hero-mobile.jpg"
       alt="Students in the Ramsey College computer lab"
       width="800" height="400">
</picture>
```

[SHOW BROWSER]

Let me demonstrate the complete responsive page in Chrome DevTools. Watch as I switch between iPhone SE (375px), iPad (768px), and desktop (1440px). The navigation collapses to a hamburger on mobile, the two-column layout stacks to single-column, and the card grid reflows automatically.

In this week's lab you will add media queries to the CSS you built in Lab 02. You will implement mobile-first breakpoints, a collapsible navigation, and responsive typography with `clamp()`.

Thank you for watching. See you in Module 04 where we add JavaScript to make these layouts interactive.

---

## Additional Resources

- developer.mozilla.org — search "CSS media queries" for the complete specification and browser compatibility tables
- aws.amazon.com/certification — review the DVA-C02 exam guide for static site deployment scenarios
