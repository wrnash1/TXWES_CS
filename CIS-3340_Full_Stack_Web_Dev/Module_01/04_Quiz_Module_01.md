# Quiz: Module 01 - HTML5 Semantics & SEO

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which HTML5 tag is considered a semantic element?

- A) `<div>`
- B) `<span>`
- C) `<article>`
- D) `<b>`

**Correct Answer:** C

**Explanation:** `<article>` is a semantic element that tells browsers, search engines, and assistive technologies that the enclosed content is a self-contained, independently distributable piece of content such as a blog post, news article, or forum entry.

**Distractor Analysis:**

- Why A is incorrect: `<div>` is a generic block-level container with no semantic meaning — it conveys nothing about the content it wraps.
- Why B is incorrect: `<span>` is a generic inline container with no semantic meaning, used only as a styling or scripting hook.
- Why C is correct: `<article>` carries inherent meaning — the content it wraps could stand alone and still make sense when redistributed.
- Why D is incorrect: `<b>` applies bold styling and carries no semantic weight; `<strong>` should be used when the bold emphasis is meaningful.

---

## Question 2

Which of the following is the most accurate definition of accessibility guidelines (WCAG)?

- A) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities, covering screen reader compatibility, keyboard navigation, and color contrast.
- B) CSS sizing rules such as `width`, `height`, `max-width`, and `box-sizing` that control how element dimensions are calculated and rendered by the browser.
- C) A set of HTTP response codes (2xx, 3xx, 4xx, 5xx) used by web servers to communicate the outcome of a client request.
- D) A browser security policy that blocks JavaScript in one origin from reading data returned by a different origin unless the server explicitly permits it.

**Correct Answer:** A

**Explanation:** WCAG is the W3C standard for making web content accessible to users with disabilities. It is organized around four principles (Perceivable, Operable, Understandable, Robust) and three conformance levels (A, AA, AAA).

**Distractor Analysis:**

- Why A is correct: This accurately describes WCAG — the international web accessibility standard published by the W3C.
- Why B is incorrect: This describes CSS box model sizing properties, not accessibility guidelines.
- Why C is incorrect: This describes HTTP status code classes, which are unrelated to accessibility standards.
- Why D is incorrect: This describes the Same-Origin Policy and CORS security model, not WCAG.

---

## Question 3

A developer needs to check that an HTML page's structure is valid and free of errors before deployment. Which tool is most appropriate?

- A) The W3C Nu HTML Checker at validator.w3.org
- B) `git commit -m 'validate html'`
- C) `npm run build`
- D) Chrome DevTools Network tab

**Correct Answer:** A

**Explanation:** The W3C Nu HTML Checker parses your markup against the HTML5 specification and reports structural errors and warnings. It is the standard tool for verifying HTML validity before deployment.

**Distractor Analysis:**

- Why A is correct: The W3C Nu HTML Checker is purpose-built for validating HTML structure against the HTML5 specification.
- Why B is incorrect: `git commit` records changes to version control but does not validate HTML correctness.
- Why C is incorrect: `npm run build` compiles front-end assets but does not semantically validate HTML structure.
- Why D is incorrect: The Network tab shows HTTP request and response traffic, not markup validity.

---

## Question 4

While building a product page, a developer replaces every layout `<div>` with a `<section>` tag. What is the most significant problem with this approach?

- A) `<section>` is not a valid HTML5 element and will cause a browser parse error.
- B) `<section>` carries semantic meaning — it represents a thematic grouping with a heading — and using it as a generic container misrepresents the document's structure to crawlers and assistive technologies.
- C) `<section>` elements cannot contain child block elements like `<p>` or `<ul>`.
- D) Replacing `<div>` with `<section>` will cause CSS Flexbox and Grid layouts to stop functioning.

**Correct Answer:** B

**Explanation:** Semantic elements should only be used when their meaning applies to the content they wrap. Indiscriminate use of `<section>` as a generic layout container distorts the document outline that search crawlers and screen reader users depend on.

**Distractor Analysis:**

- Why A is incorrect: `<section>` is a fully valid HTML5 element and will not cause a parse error.
- Why B is correct: Using semantic elements incorrectly is worse than using `<div>`, because it creates a misleading machine-readable document outline.
- Why C is incorrect: `<section>` is a block-level element and can contain any block or inline child elements.
- Why D is incorrect: CSS layout models (Flexbox, Grid) are applied via CSS properties and are not affected by which HTML element is used as the container.

---

## Question 5

When optimizing an HTML page for search engine indexing, which combination of practices is most effective?

- A) Use a single `<h1>` tag for the primary topic, write a descriptive `<meta name="description">` tag, and add meaningful `alt` attributes to all images.
- B) Repeat the target keyword in every `<div>` tag's `id` attribute to increase keyword density.
- C) Add as many `<h1>` tags as possible to signal the page's main topics to search crawlers.
- D) Remove all `<meta>` tags to reduce page load time, since crawlers only read visible body text.

**Correct Answer:** A

**Explanation:** A clear heading hierarchy, descriptive meta description, and image alt text are the three core on-page HTML SEO practices. Each addresses a different channel through which search crawlers understand page content.

**Distractor Analysis:**

- Why A is correct: These three practices form the foundation of technical on-page SEO for HTML documents.
- Why B is incorrect: Keyword stuffing in `id` attributes has no SEO benefit and is flagged as spam by modern search algorithms.
- Why C is incorrect: Multiple `<h1>` tags dilute heading hierarchy; only one `<h1>` per page is current best practice.
- Why D is incorrect: `<meta>` tags are lightweight and have negligible impact on load time; removing them harms crawlability and social sharing previews.

---

## Question 6

A developer omits the `<meta name="viewport">` tag from a page that is otherwise correctly built with responsive CSS. What will mobile users experience?

- A) The page will not load at all on mobile devices that do not support the viewport meta tag.
- B) Mobile browsers will simulate a roughly 980px desktop layout and scale it down to fit the screen, making text and buttons appear tiny and unreadable without pinching to zoom.
- C) The page will automatically render at the device's native pixel width because modern browsers default to mobile-first rendering.
- D) CSS media queries will still fire correctly at the right breakpoints because media queries do not depend on the viewport meta tag.

**Correct Answer:** B

**Explanation:** Without the viewport meta tag, mobile browsers use a virtual viewport of approximately 980px and then scale the entire rendered page down to the physical screen width. This produces a zoomed-out desktop view where text is unreadably small and touch targets are too small to tap accurately.

**Distractor Analysis:**

- Why A is incorrect: The page loads fine without the viewport tag — the problem is how it is rendered, not whether it loads.
- Why B is correct: This is the exact behavior described in the HTML specification and observed across all major mobile browsers when the viewport tag is absent.
- Why C is incorrect: Browsers do not default to mobile-first rendering without explicit viewport meta tag instructions.
- Why D is incorrect: CSS media queries use the visual viewport width for their conditions. Without the viewport tag, the virtual 980px viewport causes most mobile media queries to never match.

---

## Question 7

Which `<meta>` tag tells social media platforms and messaging apps what image to show when a page URL is shared?

- A) `<meta name="thumbnail" content="image.jpg">`
- B) `<meta property="og:image" content="https://example.com/image.jpg">`
- C) `<meta name="image" src="https://example.com/image.jpg">`
- D) `<link rel="preview-image" href="https://example.com/image.jpg">`

**Correct Answer:** B

**Explanation:** The Open Graph `og:image` property tells social media scrapers (LinkedIn, Slack, Microsoft Teams, and others) which image to display when the page URL is shared. The value must be an absolute URL pointing to an image at least 1200px wide for best display quality.

**Distractor Analysis:**

- Why A is incorrect: `meta name="thumbnail"` is not a recognized standard for social sharing previews — it is not parsed by major social platforms.
- Why B is correct: Open Graph Protocol `og:image` is the universally supported standard for controlling link-preview images across social media and messaging platforms.
- Why C is incorrect: The `<meta>` tag uses `content` as its value attribute, not `src`. `meta name="image"` is also not a recognized social sharing standard.
- Why D is incorrect: `<link rel="preview-image">` is not a valid or recognized link relation type.

---

## Question 8

A screen reader user navigates a page that has two `<nav>` elements: one for primary site navigation and one for breadcrumb navigation. Without any additional markup, both are announced as "navigation." What attribute distinguishes them?

- A) `id` — setting unique `id` values on each `<nav>` element makes screen readers announce the ID as the name.
- B) `aria-label` — setting a unique accessible name on each `<nav>` element allows screen readers to announce "Primary navigation" and "Breadcrumb navigation" respectively.
- C) `class` — CSS class names are read by screen readers as landmark names when no other label is present.
- D) `name` — the HTML `name` attribute on a `<nav>` element provides the accessible label.

**Correct Answer:** B

**Explanation:** When a page contains multiple landmarks of the same type (multiple `<nav>` elements, multiple `<section>` elements), WCAG 2.4.1 requires that each be distinguishable. Adding `aria-label="Primary navigation"` and `aria-label="Breadcrumb navigation"` gives each a unique accessible name that screen readers announce before reading the landmark's contents.

**Distractor Analysis:**

- Why A is incorrect: Screen readers use `aria-labelledby` to reference an element's `id` as a label, but the `id` attribute itself is not announced as a landmark name.
- Why B is correct: `aria-label` directly assigns an accessible name to a landmark element, allowing screen reader users to distinguish between multiple landmarks of the same type.
- Why C is incorrect: CSS class names are styling hooks — they are not exposed in the accessibility tree and are not announced by screen readers.
- Why D is incorrect: The `name` attribute is not valid on `<nav>` elements and has no effect on accessibility.

---

## Question 9

Which HTML element is most appropriate for wrapping an image together with a text caption that visually describes that image?

- A) `<div class="image-wrapper">` with a `<p class="caption">` below it
- B) `<figure>` with a `<figcaption>` child element
- C) `<section>` with an `<h3>` heading used as the caption
- D) `<aside>` with a `<blockquote>` used as the caption text

**Correct Answer:** B

**Explanation:** The `<figure>` element is designed for self-contained media (images, code samples, diagrams, charts) that is referenced from the main content but could appear elsewhere without breaking the flow. The optional `<figcaption>` child element provides a visible caption that is programmatically associated with the figure.

**Distractor Analysis:**

- Why A is incorrect: A generic `<div>` with a `<p>` caption works visually but provides no semantic association between the image and its caption — a screen reader cannot determine that the paragraph describes the image.
- Why B is correct: `<figure>` and `<figcaption>` are the HTML5 elements specifically designed for this purpose and create an explicit programmatic relationship between the media and its caption.
- Why C is incorrect: `<section>` implies a thematic grouping with a heading — using it to wrap a single image and caption misrepresents the document structure.
- Why D is incorrect: `<aside>` marks tangential content; `<blockquote>` marks quoted text from an external source — neither is semantically appropriate for an image caption.

---

## Question 10

A developer deploys a React application to S3 with static website hosting enabled. The S3 bucket's index document is set to `index.html`. When a search engine crawler requests the page, it receives the `index.html` file. Which `<head>` element most directly determines what title the search engine displays for this page in its results?

- A) `<meta name="description">`
- B) `<meta property="og:title">`
- C) `<title>`
- D) `<h1>` inside the `<body>`

**Correct Answer:** C

**Explanation:** The `<title>` element is the primary signal search engines use to determine the clickable headline displayed in search results. It appears in the browser tab, bookmarks, and search result titles. The `<meta name="description">` controls the descriptive snippet below the title in search results, not the title itself.

**Distractor Analysis:**

- Why A is incorrect: `<meta name="description">` controls the description snippet shown below the title in search results — not the title itself.
- Why B is incorrect: `<meta property="og:title">` controls the title shown in social media link previews — search engines use the `<title>` element, not the Open Graph title.
- Why C is correct: The `<title>` element is the highest-weight on-page SEO signal and directly controls the headline displayed in organic search results.
- Why D is incorrect: Search engines read the `<h1>` as a content signal, but it does not control the search result title — that is determined by `<title>`.

---

### Question 11 (5 points)

Which HTML5 element should be used to mark up a standalone piece of content, such as a blog post, that could be syndicated or redistributed independently?

- A) `<section>`
- B) `<div>`
- C) `<article>`
- D) `<main>`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `<section>` represents a thematic grouping within a larger document and is not designed for independently distributable content.
  - Why B is incorrect: `<div>` is a non-semantic generic container that conveys no meaning about the content it wraps.
  - Why C is correct: `<article>` is the semantic element for self-contained content that could stand alone when removed from its surrounding context, such as a blog post or news article.
  - Why D is incorrect: `<main>` marks the primary content area of the page — there is only one per page and it wraps everything unique to that document, not individual posts.

---

### Question 12 (5 points)

A developer writes `<img src="logo.svg">` without an `alt` attribute. What is the consequence for users accessing the page with a screen reader?

- A) The screen reader skips the image entirely because SVG files are ignored.
- B) The screen reader announces the full file path or filename, which is unhelpful and potentially confusing.
- C) The browser automatically generates a description using computer vision and inserts it as alt text.
- D) The image is hidden from the accessibility tree, producing the same result as `alt=""`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Screen readers do not skip all SVG images; they attempt to describe any image element that lacks an `alt` attribute.
  - Why B is correct: When `alt` is absent, most screen readers fall back to reading the filename or URL of the image, which provides no meaningful context to the user.
  - Why C is incorrect: Browsers do not generate alt text from computer vision; that is a feature of some third-party browser extensions, not native browser behavior.
  - Why D is incorrect: An empty `alt=""` explicitly marks the image as decorative and removes it from the accessibility tree. A missing `alt` attribute is different and triggers fallback behavior.

---

### Question 13 (5 points)

What is the purpose of the `<link rel="canonical">` element in an HTML `<head>` block?

- A) It loads an external CSS file and marks it as the canonical stylesheet for the page.
- B) It tells search engines which URL is the authoritative version of a page to prevent duplicate content penalties.
- C) It specifies the language of the linked resource for screen reader voice selection.
- D) It creates a browser-level redirect from the current URL to the canonical URL.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `<link rel="canonical">` is unrelated to stylesheets; CSS is linked with `<link rel="stylesheet">`.
  - Why B is correct: The canonical link element signals to search crawlers which version of a URL should be indexed when the same content is accessible at multiple addresses, preventing split ranking signals.
  - Why C is incorrect: Language is declared with the `lang` attribute on the `<html>` element or the `hreflang` attribute on alternate links, not `rel="canonical"`.
  - Why D is incorrect: Canonical links are hints for search crawlers, not HTTP redirects; they do not affect browser navigation behavior.

---

### Question 14 (5 points)

A developer wants to display a publication date on a blog post in a human-friendly format while also making it machine-readable. Which markup is most appropriate?

- A) `<p class="date">September 15, 2025</p>`
- B) `<span data-date="2025-09-15">September 15, 2025</span>`
- C) `<time datetime="2025-09-15">September 15, 2025</time>`
- D) `<meta name="date" content="2025-09-15">`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: A plain `<p>` with a CSS class provides no machine-readable date; the class name is a styling hook, not a semantic signal.
  - Why B is incorrect: `data-*` attributes are custom data slots for JavaScript; they are not read by search engines or assistive technologies as semantic date values.
  - Why C is correct: The `<time>` element is the HTML5 semantic element for dates and times; the `datetime` attribute provides the machine-readable ISO 8601 value while the element's text content remains human-readable.
  - Why D is incorrect: `<meta>` tags are invisible metadata; this would not render any visible date text on the page.

---

### Question 15 (5 points)

Which of the following best describes the difference between `<strong>` and `<b>` in HTML5?

- A) `<strong>` adds bold styling; `<b>` adds bold styling with an underline.
- B) `<strong>` conveys semantic importance and is announced by screen readers; `<b>` applies bold styling with no semantic meaning.
- C) `<strong>` is deprecated in HTML5 and should be replaced with `<b>`.
- D) Both elements are identical — HTML5 does not distinguish between them.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Neither `<strong>` nor `<b>` adds an underline. Both render text in bold by default, but their semantic meanings differ.
  - Why B is correct: `<strong>` indicates that the enclosed text has strong importance; screen readers may emphasize it with a different tone. `<b>` draws visual attention without implying importance.
  - Why C is incorrect: `<strong>` is a current, actively-used HTML5 element; it is not deprecated.
  - Why D is incorrect: HTML5 defines distinct semantics for `<strong>` (importance) and `<b>` (stylistic attention) even though both render as bold by default.

---

### Question 16 (5 points)

A page contains a sidebar with related articles that are tangentially related to the main content but not part of the primary editorial flow. Which element is most semantically appropriate for the sidebar?

- A) `<section>`
- B) `<div>`
- C) `<aside>`
- D) `<nav>`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `<section>` groups thematically related content that is part of the main content flow; it is not designed for tangential supplementary content.
  - Why B is incorrect: `<div>` is non-semantic; it is a valid fallback but `<aside>` is more meaningful for this use case.
  - Why C is correct: `<aside>` is defined as content that is tangentially related to the content around it, such as a sidebar, pull quote, or related-articles panel.
  - Why D is incorrect: `<nav>` is reserved for landmark navigation link groups; using it for a list of related articles misrepresents the content's purpose.

---

### Question 17 (5 points)

What does the `lang` attribute on the `<html>` element tell assistive technologies?

- A) It sets the character encoding used to decode the document's bytes.
- B) It specifies the primary human language of the document so screen readers can select the correct voice engine and pronunciation rules.
- C) It declares the programming language used by inline `<script>` elements.
- D) It configures the browser's spell-check language for all text input fields on the page.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Character encoding is declared by `<meta charset="UTF-8">`, not the `lang` attribute.
  - Why B is correct: WCAG 3.1.1 (Level A) requires a `lang` attribute on the `<html>` element so that screen readers can apply correct language-specific pronunciation and voice profiles.
  - Why C is incorrect: Script type or language is declared with the `type` attribute on `<script>`, not the `lang` attribute on `<html>`.
  - Why D is incorrect: While some browsers use `lang` as a hint for spell-check, the primary and required purpose of `lang` on `<html>` is accessibility and language processing.

---

### Question 18 (5 points)

A team is auditing their page for WCAG 2.1 Level AA compliance. Which color contrast ratio must body text (18pt or smaller) meet to pass?

- A) 3:1
- B) 4.5:1
- C) 7:1
- D) 2:1

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A 3:1 ratio is the minimum for large text (18pt or 14pt bold) and for non-text UI components under WCAG 1.4.11 — it does not meet the requirement for standard body text.
  - Why B is correct: WCAG 1.4.3 (Level AA) requires a minimum contrast ratio of 4.5:1 between normal text and its background for text smaller than 18pt (or 14pt bold).
  - Why C is incorrect: 7:1 is the enhanced contrast ratio required for WCAG Level AAA under criterion 1.4.6, not Level AA.
  - Why D is incorrect: 2:1 falls below all WCAG conformance thresholds and would fail even the minimum Level A requirements.

---

### Question 19 (5 points)

Which `<head>` element should be placed first within the `<head>` block, before any other element?

- A) `<title>`
- B) `<meta name="viewport">`
- C) `<meta charset="UTF-8">`
- D) `<link rel="stylesheet">`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `<title>` must come after the charset declaration; placing it first can cause the title to be parsed with the wrong encoding if non-ASCII characters are present.
  - Why B is incorrect: `<meta name="viewport">` is important but must follow `<meta charset>` to ensure correct rendering context.
  - Why C is correct: The HTML specification recommends placing `<meta charset>` as the very first element inside `<head>` so the browser knows the encoding before parsing any other content, including the `<title>`.
  - Why D is incorrect: Stylesheets are typically the last items in `<head>` after metadata declarations; placing them first before charset risks encoding issues with any non-ASCII characters in the stylesheet path.

---

### Question 20 (5 points)

A developer adds `role="banner"` to a `<div>` at the top of the page. A colleague suggests replacing the `<div>` with `<header>`. Which statement best justifies the colleague's suggestion?

- A) `<div role="banner">` causes a browser rendering error; `<header>` must be used instead.
- B) The `<header>` element implicitly carries `role="banner"` when it is a direct child of `<body>`, making the explicit ARIA role redundant — using native HTML is preferred per the first rule of ARIA.
- C) `<div role="banner">` is ignored by all screen readers because ARIA roles are only valid on native semantic elements.
- D) Using `<header>` instead of `<div>` reduces the page's DOM node count, which improves Lighthouse performance scores.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `<div role="banner">` is valid markup and does not cause a rendering error; it is simply less elegant than using the native element.
  - Why B is correct: The first rule of ARIA states that you should use native HTML elements with built-in semantics before adding explicit ARIA roles. `<header>` already exposes `role="banner"` implicitly, so the ARIA attribute is unnecessary.
  - Why C is incorrect: ARIA roles on `<div>` elements are fully supported and recognized by modern screen readers; they are not ignored.
  - Why D is incorrect: Replacing a `<div>` with `<header>` does not change the DOM node count — it replaces one element with another of the same structural depth.
