# Reading Guide: Module 02 - Modern CSS Layouts
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 02 - Modern CSS Layouts**! This module covers the two dominant CSS layout systems — Flexbox and CSS Grid — along with the foundational box model that governs how every element is sized and spaced. You will learn how to build one-dimensional and two-dimensional layouts that adapt to varying content and viewport sizes. These skills directly underpin the React component styling and AWS-hosted front-end deployments you will work with later in the course.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Flexbox**: The CSS Flexible Box Layout module; a one-dimensional layout model that distributes space and aligns items along a single axis (either row or column). Flex containers use properties like `justify-content`, `align-items`, `flex-wrap`, and `gap` to control child item placement without relying on floats or manual positioning.
*   **CSS Grid**: A two-dimensional layout system that allows developers to define explicit rows and columns using `grid-template-rows`, `grid-template-columns`, and `grid-area` assignments. CSS Grid is best suited for complex page-level layouts where both axes must be controlled simultaneously, such as dashboard interfaces and magazine-style content grids.
*   **Display attributes**: CSS `display` property values — including `block`, `inline`, `inline-block`, `flex`, and `grid` — that control the formatting context of an element and determine how it participates in document flow. Changing `display` to `flex` or `grid` converts an element into a layout container whose direct children become layout items.
*   **Box model**: The fundamental CSS layout concept describing how every HTML element is rendered as a rectangular box consisting of four layers: the content area (width/height), padding (inner space between content and border), border, and margin (outer space between the element and its neighbors). The `box-sizing: border-box` declaration makes width calculations include padding and border, simplifying responsive layout math.
*   **Sizing properties**: CSS properties such as `width`, `height`, `min-width`, `max-width`, `min-height`, and `max-height` that constrain element dimensions. Relative units like percentages, `em`, `rem`, and `vw`/`vh` allow elements to resize proportionally relative to their parent, root font size, or viewport dimensions, enabling fluid and responsive layouts.

---

### 2. Certification Exam Tips
*   **CSS Layouts and AWS Front-End Deployment:** The DVA-C02 exam tests your ability to deploy and serve front-end applications on AWS. A React or static HTML application that uses Flexbox and Grid layouts is built with `npm run build` and deployed to S3 + CloudFront. Understanding that the compiled CSS in the build artifact must be properly structured ensures your deployment produces a functional UI.
*   **Responsive Design is a Full-Stack Concern:** When building serverless APIs on AWS API Gateway + Lambda, your front-end client must consume and display data on any device. Responsive CSS layouts are the mechanism that makes this work — know how `@media` queries complement Flexbox and Grid for breakpoint-based design.
*   **Study Resource:** The MDN Flexbox guide is the definitive interactive reference for CSS layouts. [MDN — Basic Concepts of Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) explains axis alignment, flex-grow/shrink/basis, and wrapping behavior with live code examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Modern CSS Layouts** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/) — the primary free textbook for this course.
*   **Required Video:** Watch the CSS layouts section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — an open-access walkthrough of Flexbox, Grid, and responsive layout techniques.

---

### Lab & Command Integration
In this week's hands-on lab, you will apply modern CSS layout concepts directly:
*   **Configure a CSS Flexbox card container**: Build a responsive card grid using `display: flex`, `flex-wrap: wrap`, and `gap` — ensuring cards reflow to a single column on narrow viewports without a media query on the cards themselves.
*   **Configure a CSS Grid dashboard interface**: Define a two-column, three-row dashboard layout using `grid-template-columns` and `grid-template-areas` — placing sidebar, header, and content regions in named grid zones.
*   **Debug layout overlapping elements**: Use Chrome DevTools Layout panel to inspect computed box model values (margin, border, padding, width) and identify why elements overflow their containers or overlap siblings.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read the section covering **Modern CSS Layouts** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/).
- [ ] Watch the CSS layouts section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Experiment with Flexbox and Grid in a local HTML file before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
