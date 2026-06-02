# Reading Guide: Module 01 - HTML5 Semantics & SEO

**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers the foundational building blocks of every web application: structured HTML5 markup and the on-page practices that make pages discoverable, accessible, and maintainable. You will learn how semantic elements communicate page meaning to browsers, assistive technologies, and search engine crawlers. Mastering clean HTML structure is a prerequisite skill before applying CSS layout in Module 02, JavaScript interactivity in Module 04, and cloud deployment in Module 14.

---

## 1. The HTML5 Document Skeleton

Every HTML5 document begins with a required set of declarations and metadata elements in the `<head>` block. These elements control browser behavior and search engine indexing before any visible content is rendered.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="A 150-160 character description of this page's content.">
  <title>Page Title - Site Name</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- visible page content here -->
</body>
</html>
```

Key points about each required element:

- `<!DOCTYPE html>` triggers standards mode rendering. Omitting it causes browsers to enter quirks mode, which changes how CSS is calculated and can break layouts unpredictably.
- `<html lang="en">` specifies the primary language of the document. Screen readers use this attribute to select the correct language voice engine. WCAG 3.1.1 (Level A) requires a programmatic language declaration on every page.
- `<meta charset="UTF-8">` declares the character encoding. UTF-8 supports all Unicode characters including international alphabets, emoji, and special symbols. Always place this as the first element inside `<head>`.
- `<meta name="viewport">` is critical for mobile rendering. Without it, mobile browsers simulate a 980px desktop layout and scale it down — producing tiny unreadable text. The value `width=device-width, initial-scale=1.0` instructs the browser to render at the device's actual pixel width.
- `<meta name="description">` is the text snippet search engines display below your page title in results pages. Aim for 150 to 160 characters of plain-language description of the page's unique content.
- `<title>` is the highest-weight on-page SEO signal. Keep it under 60 characters, place the most important keyword near the beginning, and make it unique per page across your site.

---

## 2. Semantic HTML5 Reference Table

Semantic elements describe the meaning of their content to machines, not just their visual appearance. Use this table as a quick reference.

| Element | Role | When to Use |
|---|---|---|
| `<header>` | Introductory content | Site or section header; typically holds logo and `<h1>` |
| `<nav>` | Navigation landmark | Major navigation link groups; add `aria-label` if multiple navs exist |
| `<main>` | Primary content | One per page; holds content unique to this document |
| `<article>` | Self-contained content | Blog posts, news stories, product listings, forum replies |
| `<section>` | Thematic grouping | Named content group; always pair with a heading |
| `<aside>` | Tangential content | Sidebars, related links, callout boxes, advertisements |
| `<footer>` | Closing content | Copyright, legal links, contact info at page or section level |
| `<figure>` | Media with caption | Images, code samples, or diagrams with an optional `<figcaption>` |
| `<figcaption>` | Figure caption | Visible description of the parent `<figure>` element |
| `<time>` | Date or time | Machine-readable dates; use the `datetime` attribute |
| `<address>` | Contact info | Author or organization contact details |
| `<mark>` | Highlighted text | Relevant or important text within a larger passage |

---

## 3. Non-Semantic vs. Semantic Markup

Non-semantic markup uses generic containers that communicate nothing about content meaning:

```html
<!-- Non-semantic — browsers and crawlers see only boxes -->
<div id="header">
  <div id="logo">My Site</div>
  <div id="nav">
    <div class="nav-item"><a href="/">Home</a></div>
    <div class="nav-item"><a href="/about">About</a></div>
  </div>
</div>
<div id="content">
  <div class="post">
    <div class="post-title">Article Title</div>
    <div class="post-body">Content here...</div>
  </div>
</div>
```

Semantic markup replaces each generic container with an element whose name matches its purpose:

```html
<!-- Semantic — machines understand page structure -->
<header>
  <h1>My Site</h1>
  <nav aria-label="Primary navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h2>Article Title</h2>
    <p>Content here...</p>
  </article>
</main>
```

---

## 4. Heading Hierarchy

Headings serve two purposes: visual size hierarchy (which CSS handles) and document outline (which semantics handle). Always use headings for their structural meaning, not their default visual size.

Rules for correct heading hierarchy:

- One `<h1>` per page — it names the primary topic of the document
- Never skip heading levels (for example, jumping from `<h2>` to `<h4>`)
- Subsections under an `<h2>` use `<h3>`; subsections under those use `<h4>`
- Use CSS to change the visual size of headings independently of their semantic level

```html
<!-- Correct heading hierarchy -->
<h1>Department of Computer Science</h1>
  <h2>Undergraduate Programs</h2>
    <h3>BS Computer Science</h3>
    <h3>BS Information Systems</h3>
  <h2>Graduate Programs</h2>
    <h3>MS Data Science</h3>

<!-- Incorrect — skips h2 entirely -->
<h1>Department of Computer Science</h1>
  <h3>Undergraduate Programs</h3>   <!-- violation: skipped h2 -->
```

---

## 5. Images, Alt Text, and Accessibility

The `alt` attribute on `<img>` elements has three possible states — each appropriate in different situations.

```html
<!-- Informational image — write descriptive alt text -->
<img src="campus.jpg"
     alt="Students walking across the Texas Wesleyan campus quad in autumn"
     width="1200"
     height="600">

<!-- Decorative image — empty alt tells screen readers to skip it -->
<img src="separator.png" alt="" role="presentation">

<!-- Linked image — alt describes the link destination, not the image -->
<a href="/programs">
  <img src="programs-icon.svg" alt="View academic programs">
</a>
```

Always include `width` and `height` attributes on images. Before the image file loads, the browser uses these values to reserve the correct space in the layout, preventing Cumulative Layout Shift — a Core Web Vitals metric that affects Google search ranking.

---

## 6. SEO Head Tag Patterns

Search engine optimization starts with correct `<head>` metadata. Here is a complete production-quality `<head>` block:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Primary SEO tags -->
  <title>Full Stack Web Development | CIS-3340 | TXWES</title>
  <meta name="description"
        content="Learn full-stack development with HTML, CSS, JavaScript,
                 Node.js, React, and AWS at Texas Wesleyan University.">
  <meta name="author" content="Professor Nash">

  <!-- Open Graph: controls link previews on Slack, LinkedIn, Teams -->
  <meta property="og:title" content="Full Stack Web Development | CIS-3340">
  <meta property="og:description"
        content="Industry-aligned full-stack curriculum with AWS certification prep.">
  <meta property="og:image" content="https://txwes.edu/images/cis-3340-og.jpg">
  <meta property="og:url" content="https://txwes.edu/courses/cis-3340">
  <meta property="og:type" content="website">

  <!-- Canonical URL prevents duplicate content penalties -->
  <link rel="canonical" href="https://txwes.edu/courses/cis-3340">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
```

---

## 7. WCAG Accessibility Principles

The Web Content Accessibility Guidelines (WCAG) are organized around four principles known as POUR:

| Principle | Meaning | HTML Examples |
|---|---|---|
| Perceivable | Content can be perceived through multiple senses | `alt` text on images, captions on video, sufficient color contrast |
| Operable | UI components are operable by keyboard and assistive tools | Focusable links and buttons, no keyboard traps, skip-navigation links |
| Understandable | Content and interface behavior is understandable | `lang` attribute, clear error messages, consistent navigation |
| Robust | Content is interpreted correctly by assistive technologies | Valid semantic HTML, ARIA roles where needed, tested with screen readers |

WCAG has three conformance levels:

- Level A — minimum requirements; failure causes some users to be completely blocked
- Level AA — the legally required standard in most enterprise, government, and education contexts
- Level AAA — enhanced accessibility; typically aspirational for public-facing content

---

## 8. ARIA Roles and Landmarks

When semantic HTML elements are not sufficient, ARIA (Accessible Rich Internet Applications) attributes supplement them. However, the first rule of ARIA is: use native HTML elements before adding ARIA.

```html
<!-- Prefer native elements -->
<nav>...</nav>          <!-- role="navigation" is implicit -->
<main>...</main>        <!-- role="main" is implicit -->
<button>Submit</button> <!-- role="button" is implicit -->

<!-- ARIA for non-native interactive elements -->
<div role="tablist" aria-label="Module navigation">
  <div role="tab" aria-selected="true" tabindex="0">Module 01</div>
  <div role="tab" aria-selected="false" tabindex="-1">Module 02</div>
</div>

<!-- aria-label adds an accessible name when visible text is absent -->
<button aria-label="Close dialog">
  <span aria-hidden="true">&times;</span>
</button>
```

---

## 9. Exam and Interview Tips

1. A page should have exactly one `<h1>` that describes the page's primary topic — multiple `<h1>` elements weaken the heading hierarchy and dilute SEO signals.

2. `<div>` and `<span>` are still valid — use them when no semantic element matches the content's meaning. Do not force semantic elements onto generic containers.

3. `<section>` is not a generic container — it represents a named thematic grouping and should always contain a heading. If a grouping has no natural heading, use `<div>` instead.

4. The `viewport` meta tag is the most common reason a correctly coded responsive site breaks on mobile when first deployed.

5. WCAG 1.4.3 requires a minimum contrast ratio of 4.5:1 between text and background at Level AA. This is often tested in accessibility audit questions.

6. In the DVA-C02 exam, static website hosting on S3 routes all requests to the `index.html` object by default — understanding what that file contains is foundational to the Module 14 deployment questions.

7. Open Graph `og:image` values must be absolute URLs. Relative paths do not work when the page is shared on social media or messaging platforms.

8. The `<link rel="canonical">` tag tells search engines which URL is the authoritative version of a page — important when the same content is accessible at multiple URLs (for example, with and without trailing slashes).

---

## 10. Study Checklist

- [ ] Memorize the six primary landmark elements: `header`, `nav`, `main`, article`, `aside`, `footer`
- [ ] Understand when to use `<article>` vs. `<section>` vs. `<div>`
- [ ] Know the required `<head>` elements and what each one does
- [ ] Be able to write correct heading hierarchy without skipping levels
- [ ] Understand the three `alt` text states: descriptive, empty, and link-destination
- [ ] Know the four WCAG POUR principles and their HTML implications
- [ ] Be able to explain why the viewport meta tag is required for mobile rendering
- [ ] Understand why Open Graph image URLs must be absolute paths
- [ ] Complete Lab 01 and pass W3C Nu HTML Checker with zero errors
- [ ] Complete Quiz 01 and Discussion 01 before the module deadline
