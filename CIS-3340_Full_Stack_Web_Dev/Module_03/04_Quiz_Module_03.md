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

---

### Question 11 (5 points)

A developer wants to apply different styles when the user's operating system is set to dark mode. Which CSS feature enables this without JavaScript?

- A) `@media (color-scheme: dark)`
- B) `@media (prefers-color-scheme: dark)`
- C) `@supports (dark-mode: enabled)`
- D) `:root[data-theme="dark"]`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `color-scheme` is a CSS property (not a media feature) that hints to the browser which color scheme an element supports — it does not query the user's OS preference.
  - Why B is correct: `@media (prefers-color-scheme: dark)` is the standard media query that detects the user's OS-level color scheme preference and applies the enclosed styles when dark mode is active.
  - Why C is incorrect: `@supports` tests for CSS property support, not user preferences; `dark-mode: enabled` is not valid syntax.
  - Why D is incorrect: `:root[data-theme="dark"]` is a valid CSS selector for a JavaScript-driven theme toggle, but it does not respond to the OS color preference automatically without JavaScript setting the attribute.

---

### Question 12 (5 points)

Which CSS property prevents images from overflowing their containers on small screens?

- A) `width: 100%`
- B) `max-width: 100%`
- C) `overflow: hidden` on the container
- D) `object-fit: contain`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `width: 100%` forces the image to always fill its container's width, which can cause upscaling and quality loss on large screens.
  - Why B is correct: `max-width: 100%` allows the image to be its natural size up to the container width, then scales it down if the container is narrower — preventing overflow without forcing upscaling.
  - Why C is incorrect: `overflow: hidden` clips content that overflows rather than preventing the image from overflowing.
  - Why D is incorrect: `object-fit: contain` controls how image content fills its declared box dimensions — it does not prevent the box itself from overflowing the container.

---

### Question 13 (5 points)

What does `@media (prefers-reduced-motion: reduce)` target, and why is it important?

- A) It targets users on low-bandwidth connections and disables high-resolution images to reduce data transfer.
- B) It targets users who have enabled a system-level setting to minimize motion and animation, often required by users with vestibular disorders or motion sensitivity to prevent discomfort.
- C) It targets older browsers that do not support CSS transitions and falls back to static styles automatically.
- D) It targets mobile devices with reduced CPU power and applies lighter rendering effects to improve performance.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Bandwidth reduction is addressed by the `prefers-reduced-data` media feature (experimental), not `prefers-reduced-motion`.
  - Why B is correct: The `prefers-reduced-motion` setting reflects the user's OS accessibility preference to minimize animation. Users with vestibular disorders, epilepsy, or motion sensitivity may experience nausea or disorientation from excessive animation.
  - Why C is incorrect: `@media (prefers-reduced-motion)` is a preference query, not a browser capability detection — `@supports` is the feature used to test CSS support.
  - Why D is incorrect: CPU performance is not reported by `prefers-reduced-motion`; this preference is set by the user in OS accessibility settings regardless of device performance.

---

### Question 14 (5 points)

A developer writes base styles for a 1200px desktop layout and adds `@media (max-width: 768px)` rules to adjust for mobile. Which responsive strategy does this represent, and what is its primary drawback?

- A) Mobile-first; the drawback is that `max-width` media queries require more CSS declarations than `min-width`.
- B) Desktop-first; mobile browsers must parse and then override the full desktop CSS before applying the mobile rules, which adds unnecessary parsing work on constrained devices.
- C) Container queries; the drawback is that container queries are not yet supported in all modern browsers.
- D) Fluid-only; the drawback is that percentage widths break at extreme viewport sizes.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Writing base styles for 1200px and overriding with `max-width` is desktop-first, not mobile-first.
  - Why B is correct: Desktop-first strategy requires mobile browsers to load and parse the full desktop stylesheet before applying override rules, adding unnecessary work on lower-powered devices.
  - Why C is incorrect: Container queries use `@container`, not `@media` — this code uses `@media (max-width)` which is a standard viewport media query.
  - Why D is incorrect: The described approach uses `max-width` breakpoints, not percentage-only fluid layout.

---

### Question 15 (5 points)

Which attribute on a hamburger toggle button is required to communicate its open/closed state to screen reader users?

- A) `data-open="true"`
- B) `aria-expanded="true"` or `aria-expanded="false"` updated dynamically with JavaScript
- C) `role="toggle"` on the button element
- D) `aria-hidden="false"` on the navigation list

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `data-*` attributes are custom data hooks for JavaScript — they are not exposed in the accessibility tree and are not announced by screen readers.
  - Why B is correct: `aria-expanded` is the ARIA state attribute that communicates whether a control's associated panel is expanded or collapsed. Screen readers announce the current state when the button receives focus.
  - Why C is incorrect: `role="toggle"` is not a valid ARIA role; interactive toggle state is communicated through `aria-expanded`, not a custom role.
  - Why D is incorrect: `aria-hidden="false"` is the default state and redundant; it does not communicate the toggle state of the controlling button.

---

### Question 16 (5 points)

A developer wants a section's padding to scale smoothly with viewport width — 1rem at 375px, scaling up to 3rem at 1440px — without writing media queries. Which CSS function accomplishes this?

- A) `padding: min(1rem, 3rem);`
- B) `padding: clamp(1rem, 2vw, 3rem);`
- C) `padding: calc(1rem + 100vw);`
- D) `padding: fit-content(3rem);`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `min()` returns the smaller of its arguments — `min(1rem, 3rem)` always returns `1rem` regardless of viewport width.
  - Why B is correct: `clamp(1rem, 2vw, 3rem)` uses `2vw` as the fluid preferred value that scales with viewport width, clamped between a 1rem minimum and 3rem maximum.
  - Why C is incorrect: `calc(1rem + 100vw)` would produce an extremely large value (the full viewport width plus 16px) rather than a gently scaling padding.
  - Why D is incorrect: `fit-content()` is a sizing function for grid tracks and element widths — it is not valid for padding values.

---

### Question 17 (5 points)

Which media query feature detects that a user is interacting via a pointing device that lacks hover capability, such as a touchscreen?

- A) `@media (pointer: coarse)`
- B) `@media (hover: none)`
- C) `@media (touch-events: enabled)`
- D) `@media (input: touch)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `@media (pointer: coarse)` detects an imprecise pointing device (like a finger on a touchscreen) but does not directly test hover capability.
  - Why B is correct: `@media (hover: none)` matches devices where the primary input mechanism cannot hover, such as touchscreens. Developers use this to disable hover-only interactions that would not be accessible on touch devices.
  - Why C is incorrect: `touch-events` is not a valid CSS media feature.
  - Why D is incorrect: `input: touch` is not a valid CSS media feature.

---

### Question 18 (5 points)

A developer uses `em` units for padding inside a card component. If the card's `font-size` is `1.25rem` and the padding is set to `1em`, what is the computed padding in pixels (assuming the root font size is 16px)?

- A) 16px
- B) 20px
- C) 25px
- D) 12.5px

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: 16px would be the result if `em` computed against the root font size, but `em` is relative to the element's own `font-size`, not the root.
  - Why B is correct: The card's `font-size` is `1.25rem` = 1.25 × 16px = 20px. `1em` = the element's font-size = 20px.
  - Why C is incorrect: 25px would require a `font-size` of 25px (1.5625rem), not 1.25rem.
  - Why D is incorrect: 12.5px would result from `0.625rem` — not from `1em` at a 20px font-size context.

---

### Question 19 (5 points)

When writing mobile-first CSS, where should `@media (min-width: 768px)` rules be placed relative to the base styles they override?

- A) Before the base styles, so the browser applies desktop styles before the mobile defaults.
- B) After the base styles they modify, so the cascade applies the media query block over the base rules when the condition is met.
- C) In a separate CSS file linked with a `media` attribute on the `<link>` element.
- D) Inside the HTML `<style>` tag in the `<head>` rather than in the external stylesheet.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Placing media queries before their base styles would cause the base styles to override the media query styles due to cascade order — the opposite of the intended behavior.
  - Why B is correct: In the CSS cascade, later rules with the same or higher specificity win. Media query blocks must follow the base rules they augment so the browser applies them on top when the condition is true.
  - Why C is incorrect: While separate files linked with `media` attributes is a valid historical pattern, it adds extra HTTP requests and is not the standard modern approach — all breakpoints in a single file is preferred.
  - Why D is incorrect: Moving media queries to a `<style>` tag does not affect their cascade behavior and fragments the stylesheet across files and inline markup.

---

### Question 20 (5 points)

A responsive page works correctly in Chrome DevTools device simulation but breaks on a real iPhone. The developer verifies the viewport meta tag is present. What is the most likely additional cause?

- A) iPhones do not support CSS Grid — the layout must be rebuilt using Flexbox for iOS compatibility.
- B) The page is served over HTTP instead of HTTPS — iOS Safari applies different rendering rules for non-secure pages.
- C) The page uses device-pixel-ratio-specific assets that conflict with the iPhone's Retina display scaling, causing layout to calculate at 2x sizes.
- D) The DevTools simulation does not account for iOS Safari-specific behaviors such as the address bar affecting `100vh`, or CSS features not yet implemented in the WebKit engine.

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: iOS Safari fully supports CSS Grid — this is not the cause of layout differences between DevTools simulation and real device.
  - Why B is incorrect: HTTP vs HTTPS affects security features like service workers and mixed-content blocking, not basic layout rendering.
  - Why C is incorrect: Device pixel ratio affects image sharpness, not CSS layout dimensions — `px` in CSS refers to logical pixels, not physical pixels.
  - Why D is correct: Chrome DevTools simulates screen dimensions but does not replicate WebKit-specific rendering quirks. Common iOS-only issues include `100vh` being taller than the visible viewport (due to the Safari address bar), `-webkit-` prefixed properties needed for certain CSS features, and Safari's distinct handling of certain flexbox edge cases.
