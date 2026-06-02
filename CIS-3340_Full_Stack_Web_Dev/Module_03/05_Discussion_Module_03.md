# Discussion Forum: Module 03 - Responsive Design

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects responsive design principles to real product, performance, and accessibility decisions. Choose one of the three scenarios below and write an initial post addressing all three sub-questions.

---

## Scenario A: Mobile-First Refactor for a Government Agency

A state government agency is rebuilding its benefits application portal. The current site was built desktop-first three years ago. A new accessibility audit reveals three failures: the mobile viewport renders a zoomed-out desktop layout, the navigation is not keyboard-operable on mobile, and users with low vision who have set their browser font size to 24px see text that is still rendered at 14px because of `font-size: 14px` on the `<html>` element.

Address all three of the following in your post:

1. Explain why the CSS architecture choice (desktop-first vs. mobile-first) affects the performance experienced by mobile users, not just the visual appearance. Consider how browsers parse and apply CSS when explaining your answer.
2. The navigation failure says it is not keyboard-operable on mobile. The hamburger menu currently uses `<div class="hamburger">` with a JavaScript `click` listener. Identify two specific accessibility problems with this implementation and propose the correct HTML element and ARIA attributes to fix each one.
3. Explain why `font-size: 14px` on the `<html>` element violates WCAG 1.4.4 (Resize Text), and propose the correct CSS value to replace it. What happens to a user who has set their browser's default font size to 24px when the HTML element's font size is set in `px`?

Your initial post should be 175 to 225 words.

---

## Scenario B: Responsive Images and Core Web Vitals

A media company runs a photo news site built in React. The site is deployed to AWS S3 with CloudFront as the CDN. A Google Lighthouse audit reports a Largest Contentful Paint (LCP) score of 7.2 seconds on mobile — far above the "Good" threshold of 2.5 seconds. Investigation reveals that the hero image is a 4000x2667px JPEG at 8MB, delivered identically to desktop and mobile devices. The image element in HTML has no `width` or `height` attributes, contributing to a Cumulative Layout Shift (CLS) score of 0.42.

Address all three of the following in your post:

1. Explain the Largest Contentful Paint metric and why a large, unoptimized hero image is the primary cause of a poor LCP score. What is the relationship between file size, network transfer time, and LCP on a mobile connection?
2. Propose a complete HTML solution using the `<picture>` element and `srcset` that delivers appropriately sized images to mobile, tablet, and desktop users. Include approximate target dimensions for each breakpoint.
3. Explain how adding `width` and `height` attributes to the `<img>` element fixes the CLS score of 0.42. What does the browser do differently when these attributes are present before the image has loaded?

Your initial post should be 175 to 225 words.

---

## Scenario C: Breakpoint Strategy for a SaaS Dashboard

A startup is building a project management SaaS product in React. The design team delivers three mockups: mobile (375px), tablet (768px), and desktop (1440px). A senior engineer opens a team discussion about breakpoint strategy — specifically arguing that the team should not hard-code breakpoints at those exact pixel values, but should instead add breakpoints "where the layout breaks."

Address all three of the following in your post:

1. Explain the senior engineer's argument in your own words. Why is defining breakpoints at common device pixel widths (375, 768, 1440) potentially harmful compared to adding breakpoints where the layout actually breaks during testing?
2. The design shows a data table that becomes unreadable at 600px because columns overlap. The table is not in the designer's three mockup widths. Explain how you would discover this breakpoint and what CSS change would you make to handle the table at that width.
3. The team wants to support the `prefers-color-scheme: dark` media query for a dark mode without writing a separate stylesheet. Sketch the CSS architecture using custom properties (CSS variables) that would allow a single color change in the `:root` dark query to update the entire page's color scheme. Provide at least four variable examples.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add a concrete AWS or browser-behavior detail that strengthens the answer, or
- Present an alternative approach with a comparison of trade-offs

---

## Due Dates

- Initial post: Wednesday by 11:59 PM
- Peer responses (at least two): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Initial post uses correct CSS and/or WCAG terminology from the module | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

Responsive design is where front-end development intersects with business outcomes. A non-responsive site is not just aesthetically poor — it actively loses customers, fails legal accessibility requirements, and ranks lower in Google search because of mobile-first indexing. When you are deploying applications to AWS, assume your users are on mobile first, desktop second. Build accordingly, and you will spend far less time in production firefights.
