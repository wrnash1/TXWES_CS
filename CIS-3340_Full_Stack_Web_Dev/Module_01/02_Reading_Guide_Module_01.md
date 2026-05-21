# Reading Guide: Module 01 - HTML5 Semantics & SEO
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 01 - HTML5 Semantics & SEO**! This module covers the foundational building blocks of every web application: structured HTML5 markup and the principles that make pages discoverable and accessible. You will learn how semantic elements communicate page meaning to browsers, assistive technologies, and search engine crawlers. Mastering clean, well-structured HTML is a prerequisite skill before moving into CSS layout, JavaScript interactivity, and cloud deployment.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Semantic markup**: HTML elements that describe the *meaning* of their content — such as `<header>`, `<nav>`, `<article>`, `<section>`, `<aside>`, and `<footer>` — rather than just controlling visual presentation. Semantic markup helps browsers, screen readers, and search engine crawlers correctly interpret page structure and improves both SEO ranking and accessibility compliance.
*   **SEO (Search Engine Optimization)**: A set of practices for improving a page's visibility in organic search results. In HTML, this includes writing descriptive `<title>` tags, meaningful `<meta name="description">` content, proper heading hierarchy (`<h1>`–`<h6>`), and descriptive `alt` attributes on images so crawlers can index content accurately.
*   **Head tags**: Elements placed inside the `<head>` block of an HTML document that define document metadata — including `<meta charset>`, `<meta name="viewport">`, `<title>`, stylesheet `<link>` references, and `<script>` deferred loads. These elements are not rendered in the visible page body but control browser behavior and search engine indexing.
*   **Accessibility guidelines (WCAG)**: The Web Content Accessibility Guidelines published by the W3C; a set of international standards organized around four principles — Perceivable, Operable, Understandable, and Robust (POUR). Compliance ensures that users with visual, motor, or cognitive disabilities can navigate and consume web content, typically enforced by writing proper `alt` text, ARIA labels, sufficient color contrast, and keyboard-navigable focus management.
*   **Metadata**: Structured data embedded in the `<head>` of an HTML document — such as `<meta name="description">`, `<meta name="author">`, Open Graph tags, and `<meta name="viewport" content="width=device-width, initial-scale=1">` — that is consumed by browsers, crawlers, and social media parsers but is not displayed to end users on the page.

---

### 2. Certification Exam Tips
*   **HTML Foundations for AWS DVA-C02:** While the DVA-C02 exam does not directly test HTML syntax, understanding how front-end assets are structured is essential for deploying full-stack applications on AWS. Static HTML/CSS/JS builds are uploaded to S3 buckets and served through CloudFront — knowing what a "static site" means in practice is foundational.
*   **Accessibility and Compliance:** Know that WCAG compliance is a legal requirement for many enterprise applications. When AWS Amplify or Elastic Beanstalk is used to serve a front-end, the HTML the server returns is still your responsibility. Always use semantic elements to make pages screen-reader compatible.
*   **Study Resource:** The MDN Web Docs are the most authoritative reference for HTML semantics. [MDN HTML Reference — Semantic Elements](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantics_in_html) provides interactive examples and browser compatibility tables for every semantic tag covered in this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **HTML5 Semantics & Structure** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/) — this free, peer-reviewed resource is used throughout the course.
*   **Required Video:** Watch the HTML fundamentals section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — a comprehensive open-access video covering HTML, CSS, and JavaScript from scratch.

---

### Lab & Command Integration
In this week's hands-on lab, you will apply semantic HTML concepts directly:
*   **Draft a structured HTML page using semantic tags**: Build a complete page skeleton using `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, and `<footer>` — replacing all `<div>` containers with meaningful equivalents where appropriate.
*   **Verify tags against accessibility validator**: Run your HTML file through the [W3C Nu HTML Checker](https://validator.w3.org/nu/) to identify missing `alt` attributes, duplicate `<h1>` tags, or malformed structure.
*   **Write descriptive alt text**: Add meaningful `alt` attributes to all `<img>` elements — describing the image content for screen reader users rather than leaving the attribute empty or using filename strings.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read the section covering **HTML5 Semantics** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/).
- [ ] Watch the HTML fundamentals section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Review the semantic elements and accessibility requirements outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
