# Quiz: Module 03 - Responsive Design

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

What media query rule targets screen sizes that are 768px wide or smaller?

- A) `@media (min-width: 768px)`
- B) `@media (max-width: 768px)`
- C) `@media screen 768`
- D) `@breakpoint 768px`

**Correct Answer:** B

**Explanation:** `@media (max-width: 768px)` matches any viewport up to and including 768px wide, making it the correct rule for targeting tablets and mobile devices at that specific breakpoint.

**Distractor Analysis:**

- Why A is incorrect: `min-width: 768px` matches screens that are at least 768px wide — the opposite of the requirement.
- Why B is correct: `max-width: 768px` is the standard syntax for applying styles to viewports up to the specified threshold.
- Why C is incorrect: `@media screen 768` is not valid CSS syntax — media queries require a feature condition in parentheses.
- Why D is incorrect: `@breakpoint` is not a CSS at-rule — breakpoints are implemented using `@media` rules.

---

## Question 2

Which of the following is the most accurate definition of media queries?

- A) CSS `@media` rule blocks that apply style declarations only when specific viewport or device conditions are met — such as screen width, orientation, or color scheme preference.
- B) JavaScript functions that listen for browser resize events and dynamically change DOM element class names in response to viewport width changes.
- C) HTTP request headers sent by the browser to inform the web server about the client device's screen resolution and preferred content format.
- D) SQL query statements used to retrieve responsive layout configuration data from a relational database at page load time.

**Correct Answer:** A

**Explanation:** CSS `@media` rules apply a block of CSS declarations only when a specified condition (width, orientation, color scheme, etc.) evaluates to true for the current viewing environment.

**Distractor Analysis:**

- Why A is correct: This is the accurate CSS definition of media queries — conditional blocks within a stylesheet.
- Why B is incorrect: This describes a JavaScript resize event handler, which is a different and less performant technique for responsive behavior.
- Why C is incorrect: HTTP request headers exist but are separate from CSS media queries and do not directly control styling.
- Why D is incorrect: SQL queries retrieve data from databases — they have no relationship to CSS layout or responsive design.

---

## Question 3

A developer is building a responsive site and wants the layout to start simple on mobile and progressively add complexity for larger screens. Which approach best describes this strategy?

- A) Desktop-first: write full desktop styles first, then use `max-width` media queries to simplify the layout for smaller screens.
- B) Mobile-first: write base styles for small screens first, then use `min-width` media queries to enhance the layout for progressively larger screens.
- C) Fixed-width: define a single 960px centered container and use `overflow: hidden` to clip content on smaller screens.
- D) Fluid-only: use percentage widths on all elements and avoid media queries entirely, relying solely on proportional scaling.

**Correct Answer:** B

**Explanation:** Mobile-first strategy writes lean base styles for the smallest screen and uses `min-width` breakpoints to add layout complexity for larger screens. This is the industry standard aligned with Google's mobile-first indexing.

**Distractor Analysis:**

- Why A is incorrect: Desktop-first is the older approach — less performant on mobile because phones must parse and override more CSS.
- Why B is correct: Mobile-first produces leaner default CSS and aligns with how Google evaluates page performance for SEO.
- Why C is incorrect: A fixed-width container clips or causes horizontal scrolling on small screens.
- Why D is incorrect: Pure fluid layouts without breakpoints produce poor UX at extreme viewport sizes.

---

## Question 4

A developer deploys a web application to AWS but mobile users report the page looks like a zoomed-out desktop version. What HTML fix resolves this?

- A) Add a `Content-Type: text/html; charset=UTF-8` header to the S3 bucket CORS configuration.
- B) Add `<meta name="viewport" content="width=device-width, initial-scale=1">` to the `<head>` of the HTML document.
- C) Set `body { zoom: 0.5; }` in the stylesheet to scale down the page for mobile devices.
- D) Configure AWS CloudFront to deliver a separate mobile-only HTML file using device detection headers.

**Correct Answer:** B

**Explanation:** Without the viewport meta tag, mobile browsers simulate a ~980px desktop layout and scale it down. The viewport tag instructs the browser to render at the device's actual pixel width.

**Distractor Analysis:**

- Why A is incorrect: CORS headers control cross-origin resource access, not mobile rendering behavior.
- Why B is correct: The viewport meta tag is the standard fix for the zoomed-out desktop rendering issue on mobile.
- Why C is incorrect: The CSS `zoom` property scales visual rendering without changing the layout viewport used for media queries.
- Why D is incorrect: Maintaining separate HTML files for mobile and desktop is an outdated approach that duplicates content and increases maintenance burden.

---

## Question 5

Which CSS unit is most appropriate for setting font-size values in a way that respects a user's browser accessibility settings for base font size?

- A) `px` — because pixel values are precise and consistent across all browsers.
- B) `rem` — because it scales relative to the root element's font size, which honors the user's browser font-size preference.
- C) `vw` — because font size should always scale with the viewport.
- D) `pt` — because point units were designed specifically for web typography.

**Correct Answer:** B

**Explanation:** `rem` multiplies against the root element's font size. If a user sets their browser's base font to 20px for accessibility, all `rem`-based text scales accordingly. This is the accessibility-preferred approach.

**Distractor Analysis:**

- Why A is incorrect: Pixel values are fixed — if a user enlarges their browser's default font, `px`-based font sizes ignore that preference.
- Why B is correct: `rem` scales with the root font size, which honors browser-level accessibility settings.
- Why C is incorrect: `vw` makes text very large on wide monitors and tiny in narrow windows when used alone — unsuitable as a standalone font-size unit.
- Why D is incorrect: Point units (`pt`) are a print measurement equivalent to 1/72 inch — they have no responsive behavior and are not recommended for screen typography.

---

## Question 6

What does `font-size: clamp(1rem, 3vw, 2rem)` produce on a screen that is exactly 800px wide?

- A) The font size is always 1rem regardless of viewport width, because `clamp()` ignores the middle value.
- B) The font size is 24px (3% of 800px), which falls between the 16px minimum and 32px maximum, so the preferred value is used.
- C) The font size is 2rem (32px) because 800px is considered a large screen.
- D) `clamp()` is not valid CSS and will cause the rule to be silently ignored by the browser.

**Correct Answer:** B

**Explanation:** `clamp(1rem, 3vw, 2rem)` evaluates as: minimum 16px, preferred 3% of 800px = 24px, maximum 32px. Since 24px is between the minimum (16px) and maximum (32px), the preferred value of 24px is used.

**Distractor Analysis:**

- Why A is incorrect: `clamp()` uses the minimum value only when the preferred value falls below it — at 800px, 3vw = 24px which is above 16px.
- Why B is correct: At 800px, 3vw = 24px. This falls within the clamp range of 16px to 32px, so 24px is used.
- Why C is incorrect: The maximum (2rem = 32px) is used only when 3vw exceeds 32px — which requires a viewport wider than 1067px.
- Why D is incorrect: `clamp()` is a fully supported CSS function in all modern browsers.

---

## Question 7

A developer wants to hide the hamburger menu button on screens wider than 768px and hide the full navigation links on screens narrower than 768px. Which CSS approach is correct?

- A) Apply `visibility: hidden` to both elements and use JavaScript to show/hide them on resize events.
- B) Apply `display: none` to `.nav-toggle` and `display: flex` to `.nav-links` in the base styles, then in a `max-width: 767px` media query reverse both rules.
- C) In the mobile base styles, set `.nav-toggle { display: block }` and `.nav-links { display: none }`. In a `min-width: 768px` media query, set `.nav-toggle { display: none }` and `.nav-links { display: flex }`.
- D) Use CSS `@keyframes` animations to slide the nav links off-screen on mobile and back into view on desktop.

**Correct Answer:** C

**Explanation:** The mobile-first approach shows the toggle button and hides the nav links in base styles. The `min-width: 768px` media query then reverses these rules for larger screens — showing the inline navigation and hiding the toggle button.

**Distractor Analysis:**

- Why A is incorrect: Using JavaScript resize events for this is a performance anti-pattern — CSS media queries are the correct tool and require no JavaScript.
- Why B is incorrect: This is a desktop-first approach, not mobile-first. It also applies `display: flex` to nav links by default, which would show them on all screens unless overridden.
- Why C is correct: Mobile-first base styles hide the nav links, and the `min-width` media query adds the desktop nav behavior.
- Why D is incorrect: CSS `@keyframes` animate property values over time — they do not replace the show/hide toggle logic needed here.

---

## Question 8

A Google Lighthouse audit on a deployed AWS application flags "Does not have a `<meta name=viewport>` tag with width or initial-scale" as a failing audit. Why is this audit failure significant for SEO?

- A) Google's search crawler requires the viewport meta tag as a syntactic validator — pages without it are de-indexed from all search results.
- B) Google uses mobile-first indexing, meaning it crawls and evaluates the mobile version of pages for ranking. Without the viewport tag, the mobile version renders as a zoomed-out desktop view, which degrades Core Web Vitals scores and may lower search ranking.
- C) The viewport meta tag controls whether the page appears in Google's AMP index — pages without it cannot be served as Accelerated Mobile Pages.
- D) Without the viewport meta tag, Google's crawler cannot identify which CSS breakpoints the page uses and refuses to index responsive pages.

**Correct Answer:** B

**Explanation:** Google's mobile-first indexing means the mobile rendering of a page determines how it is evaluated and ranked. Without the viewport tag, mobile rendering degrades Core Web Vitals metrics (particularly Cumulative Layout Shift and Largest Contentful Paint), which directly affect search ranking scores.

**Distractor Analysis:**

- Why A is incorrect: Pages without the viewport tag are not de-indexed — they receive a lower performance score, not removal.
- Why B is correct: Mobile-first indexing makes mobile Core Web Vitals the primary ranking factor. The viewport tag is necessary for mobile rendering to work correctly.
- Why C is incorrect: AMP (Accelerated Mobile Pages) is a separate framework — the standard viewport meta tag is not an AMP-specific requirement.
- Why D is incorrect: Google's crawler does not require it to parse CSS breakpoints — the viewport tag affects how the page renders, not how CSS is parsed.

---

## Question 9

Which CSS property and value prevents a user from pinching to zoom on a mobile device, and why should developers generally avoid it?

- A) `touch-action: none` on the `<body>` element — disables all touch interactions including tapping links, making the site unusable.
- B) `user-select: none` on all text elements — prevents text selection, which some users rely on to trigger zoom behaviors.
- C) Adding `user-scalable=no` to the viewport meta tag prevents pinch-to-zoom on mobile devices — this violates WCAG 1.4.4 (Resize Text), which requires that text can be resized up to 200 percent without loss of content or functionality.
- D) `overflow: hidden` on the `<html>` element — prevents viewport scrolling and zooming simultaneously.

**Correct Answer:** C

**Explanation:** `user-scalable=no` in the viewport meta tag disables pinch-to-zoom, which low-vision users depend on for reading. WCAG 1.4.4 (Level AA) requires that text can be resized up to 200% without assistive technology. Disabling zoom blocks this capability and can constitute an accessibility law violation.

**Distractor Analysis:**

- Why A is incorrect: `touch-action: none` disables pointer/touch gestures on specific elements — it does not globally prevent zooming.
- Why B is incorrect: `user-select: none` prevents text from being highlighted — it has no effect on zooming.
- Why C is correct: `user-scalable=no` is the setting that prevents zoom and violates WCAG 1.4.4 for users with low vision.
- Why D is incorrect: `overflow: hidden` on `<html>` prevents scrolling overflow — it does not prevent zooming.

---

## Question 10

An AWS CloudFront distribution serves a responsive website. A developer updates the viewport meta tag in `index.html` on S3 to fix mobile rendering. Users still report the old broken behavior on mobile. What is the most likely cause?

- A) The viewport meta tag change requires a CloudFront distribution settings update before it takes effect.
- B) CloudFront has cached the old `index.html` at its edge locations. The developer needs to create a cache invalidation for `"/index.html"` to force edge locations to fetch the updated file from S3.
- C) S3 does not support HTML file updates — the developer must delete and re-upload the file with a new object key.
- D) The viewport meta tag is parsed by the CDN, not the browser — CloudFront must be configured to forward the viewport setting to mobile clients.

**Correct Answer:** B

**Explanation:** CloudFront caches objects at edge locations according to their Cache-Control headers. Updating `index.html` in S3 does not automatically update cached copies at edge locations. A targeted cache invalidation for `"/index.html"` (or `"/*"`) is required to force CloudFront to serve the updated file.

**Distractor Analysis:**

- Why A is incorrect: The viewport meta tag is HTML content — it does not require CloudFront distribution settings changes, only a cache invalidation for the HTML file.
- Why B is correct: CloudFront caching is the most common reason users see stale content after an S3 update. Invalidating `"/index.html"` resolves this immediately.
- Why C is incorrect: S3 objects can be overwritten in place — deletion and re-upload is not required.
- Why D is incorrect: The viewport meta tag is a client-side HTML instruction parsed by the browser's rendering engine — CloudFront does not parse or forward meta tags.
