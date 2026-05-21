# Quiz: Module 01 - HTML5 Semantics & SEO
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which HTML5 tag is considered a semantic element?
*   A) `<div>`
*   B) `<span>`
*   C) `<article>`
*   D) `<b>`
*   **Correct Answer:** C) `<article>` is a semantic element that tells browsers and search engines the enclosed content is a self-contained piece of independently distributable content.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `<div>` is a generic block-level container with no semantic meaning — it conveys nothing about the content it wraps.
    *   *Why B is incorrect:* `<span>` is a generic inline container with no semantic meaning, used only for styling hooks.
    *   *Why C is correct:* `<article>` has semantic meaning, signaling that the enclosed content could stand alone (e.g., a blog post, news article, or forum entry).
    *   *Why D is incorrect:* `<b>` only applies bold styling and carries no semantic weight; `<strong>` should be used when emphasis is meaningful.

---

**Question 2**
Which of the following is the most accurate definition of **accessibility guidelines (WCAG)**?
*   A) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities, covering screen reader compatibility, keyboard navigation, and color contrast.
*   B) CSS sizing rules (such as `width`, `height`, `max-width`, and `box-sizing`) that control how element dimensions are calculated and rendered by the browser.
*   C) A set of HTTP response codes (2xx, 3xx, 4xx, 5xx) used by web servers to communicate the outcome of a client request.
*   D) A browser security policy that blocks JavaScript in one origin from reading data returned by a different origin unless the server explicitly permits it.
*   **Correct Answer:** A) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities, covering screen reader compatibility, keyboard navigation, and color contrast.
*   **Distractor Analysis:**
    *   *Why A is correct:* This accurately describes WCAG — the W3C standard for making web content accessible to users with disabilities.
    *   *Why B is incorrect:* This describes CSS box model sizing properties, not accessibility guidelines.
    *   *Why C is incorrect:* This describes HTTP status code classes, which are unrelated to accessibility standards.
    *   *Why D is incorrect:* This describes the Same-Origin Policy / CORS security model, not WCAG.

---

**Question 3**
A developer needs to check that an HTML page's structure is valid and free of errors before deployment. Which tool is most appropriate?
*   A) The W3C Nu HTML Checker at validator.w3.org
*   B) `git commit -m 'validate html'`
*   C) `npm run build`
*   D) Chrome DevTools Network tab
*   **Correct Answer:** A) The W3C Nu HTML Checker is the standard tool for validating HTML documents — it parses the markup against the HTML5 specification and reports structural errors and warnings.
*   **Distractor Analysis:**
    *   *Why A is correct:* The W3C Nu HTML Checker is purpose-built for validating HTML structure against the specification.
    *   *Why B is incorrect:* `git commit` records changes to version control but does not validate HTML correctness.
    *   *Why C is incorrect:* `npm run build` compiles front-end assets but does not semantically validate HTML structure.
    *   *Why D is incorrect:* The Network tab shows HTTP request/response traffic, not markup validity.

---

**Question 4**
While building a product page, a developer replaces every layout `<div>` with a `<section>` tag. What is the most significant problem with this approach?
*   A) `<section>` is not a valid HTML5 element and will cause a browser parse error.
*   B) `<section>` carries semantic meaning — it represents a thematic grouping with a heading — and using it as a generic container misrepresents the document's structure to crawlers and assistive technologies.
*   C) `<section>` elements cannot contain child block elements like `<p>` or `<ul>`.
*   D) Replacing `<div>` with `<section>` will cause CSS Flexbox and Grid layouts to stop functioning.
*   **Correct Answer:** B) `<section>` carries semantic meaning — it represents a thematic grouping with a heading — and using it as a generic container misrepresents the document's structure to crawlers and assistive technologies.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `<section>` is a valid HTML5 element and will not cause a parse error.
    *   *Why B is correct:* Semantic elements should only be used when their meaning applies; indiscriminate use of `<section>` distorts the document outline and harms SEO and accessibility.
    *   *Why C is incorrect:* `<section>` is a block-level element and can contain any block or inline child elements.
    *   *Why D is incorrect:* CSS layout models (Flexbox, Grid) are applied via CSS properties and are not affected by which HTML tag is used as the container.

---

**Question 5**
When optimizing an HTML page for search engine indexing, which combination of practices is most effective?
*   A) Use a single `<h1>` tag for the primary topic, write a descriptive `<meta name="description">` tag, and add meaningful `alt` attributes to all images.
*   B) Repeat the target keyword in every `<div>` tag's `id` attribute to increase keyword density.
*   C) Add as many `<h1>` tags as possible to signal the page's main topics to search crawlers.
*   D) Remove all `<meta>` tags to reduce page load time, since crawlers only read visible body text.
*   **Correct Answer:** A) Use a single `<h1>` tag for the primary topic, write a descriptive `<meta name="description">` tag, and add meaningful `alt` attributes to all images.
*   **Distractor Analysis:**
    *   *Why A is correct:* A clear heading hierarchy, descriptive meta description, and image alt text are the three core on-page HTML SEO practices.
    *   *Why B is incorrect:* Keyword stuffing in `id` attributes has no SEO benefit and is flagged as spam by modern search algorithms.
    *   *Why C is incorrect:* Multiple `<h1>` tags dilute heading hierarchy; only one `<h1>` per page is the current best practice.
    *   *Why D is incorrect:* `<meta>` tags are lightweight and have negligible impact on load time; removing them harms crawlability and social sharing previews.
