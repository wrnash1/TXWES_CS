# Quiz: Module 03 - Responsive Design
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
What media query rule targets screen sizes that are 768px wide or smaller?
*   A) `@media (min-width: 768px)`
*   B) `@media (max-width: 768px)`
*   C) `@media screen 768`
*   D) `@breakpoint 768px`
*   **Correct Answer:** B) `@media (max-width: 768px)` matches any viewport up to and including 768px wide, making it the correct rule for targeting tablets and mobile devices.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `min-width: 768px` matches screens that are *at least* 768px wide — the opposite of the requirement.
    *   *Why B is correct:* `max-width: 768px` is the standard syntax for applying styles to viewports up to the specified threshold.
    *   *Why C is incorrect:* `@media screen 768` is not valid CSS syntax — media queries require a feature condition in parentheses.
    *   *Why D is incorrect:* `@breakpoint` is not a CSS at-rule — breakpoints are implemented using `@media` rules.

---

**Question 2**
Which of the following is the most accurate definition of **media queries**?
*   A) CSS `@media` rule blocks that apply style declarations only when specific viewport or device conditions are met — such as screen width, orientation, or color scheme preference.
*   B) JavaScript functions that listen for browser resize events and dynamically change DOM element class names in response to viewport width changes.
*   C) HTTP request headers sent by the browser to inform the web server about the client device's screen resolution and preferred content format.
*   D) SQL query statements used to retrieve responsive layout configuration data from a relational database at page load time.
*   **Correct Answer:** A) CSS `@media` rule blocks that apply style declarations only when specific viewport or device conditions are met — such as screen width, orientation, or color scheme preference.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the accurate CSS definition of media queries — conditional blocks within a stylesheet.
    *   *Why B is incorrect:* This describes a JavaScript resize event handler, which is a different (and less performant) technique for responsive behavior.
    *   *Why C is incorrect:* HTTP request headers (`Accept`, `User-Agent`) exist but are separate from CSS media queries and do not directly control styling.
    *   *Why D is incorrect:* SQL queries retrieve data from databases — they have no relationship to CSS layout or responsive design.

---

**Question 3**
A developer is building a responsive site and wants the layout to start simple on mobile and progressively add complexity for larger screens. Which approach best describes this strategy?
*   A) Desktop-first: write full desktop styles first, then use `max-width` media queries to simplify the layout for smaller screens.
*   B) Mobile-first: write base styles for small screens first, then use `min-width` media queries to enhance the layout for progressively larger screens.
*   C) Fixed-width: define a single `960px` centered container and use `overflow: hidden` to clip content on smaller screens.
*   D) Fluid-only: use percentage widths on all elements and avoid media queries entirely, relying solely on proportional scaling.
*   **Correct Answer:** B) Mobile-first: write base styles for small screens first, then use `min-width` media queries to enhance the layout for progressively larger screens.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Desktop-first is the older approach; it is less performant for mobile devices because they must parse and override more CSS rules.
    *   *Why B is correct:* Mobile-first is the current industry standard — it produces leaner default CSS and aligns with how Google evaluates page performance for SEO.
    *   *Why C is incorrect:* A fixed-width container does not adapt to the viewport; content is clipped or requires horizontal scrolling on mobile.
    *   *Why D is incorrect:* Pure fluid layouts without breakpoints often produce poor UX at extreme viewport sizes — very narrow or very wide screens typically require structural layout changes, not just proportional scaling.

---

**Question 4**
A developer deploys a web application to AWS but mobile users report the page looks like a zoomed-out desktop version. What HTML fix resolves this?
*   A) Add a `Content-Type: text/html; charset=UTF-8` header to the S3 bucket CORS configuration.
*   B) Add `<meta name="viewport" content="width=device-width, initial-scale=1">` to the `<head>` of the HTML document.
*   C) Set `body { zoom: 0.5; }` in the stylesheet to scale down the page for mobile devices.
*   D) Configure AWS CloudFront to deliver a separate mobile-only HTML file using device detection headers.
*   **Correct Answer:** B) Add `<meta name="viewport" content="width=device-width, initial-scale=1">` to the `<head>` of the HTML document.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CORS headers control cross-origin resource access, not mobile rendering behavior.
    *   *Why B is correct:* Without the viewport meta tag, mobile browsers simulate a ~980px desktop layout and scale it down — this tag instructs them to render at the device's actual pixel width.
    *   *Why C is incorrect:* The CSS `zoom` property is non-standard and scales visual rendering without changing the layout width the browser uses for media queries.
    *   *Why D is incorrect:* CloudFront can route requests based on headers, but maintaining separate HTML files for mobile/desktop is an outdated approach that duplicates content and increases maintenance burden.

---

**Question 5**
Which CSS unit is most appropriate for setting `font-size` values in a way that respects a user's browser accessibility settings for base font size?
*   A) `px` (pixels) — because pixel values are precise and consistent across all browsers.
*   B) `rem` (root em) — because it scales relative to the root element's font size, which honors the user's browser font-size preference.
*   C) `vw` (viewport width) — because font size should always scale with the viewport.
*   D) `pt` (points) — because point units were designed specifically for web typography.
*   **Correct Answer:** B) `rem` (root em) — because it scales relative to the root element's font size, which honors the user's browser font-size preference.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Pixel values are fixed — if a user sets their browser base font size to 20px for accessibility, `px`-based font sizes ignore that preference.
    *   *Why B is correct:* `rem` multiplies against the root font size, so if a user enlarges their browser's default font, all `rem`-based text scales accordingly — this is the accessibility-preferred approach.
    *   *Why C is incorrect:* `vw` scales font sizes with the viewport width — text in a full-screen browser on a wide monitor becomes very large while text in a narrow window becomes tiny, making it unsuitable as a standalone font-size unit.
    *   *Why D is incorrect:* Point (`pt`) units are a print measurement equivalent to 1/72 inch — they have no responsive behavior and are not recommended for screen typography.
