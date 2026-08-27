# Quiz: Module 02 - Modern CSS Layouts

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which CSS property converts an element into a grid container?

- A) `display: grid`
- B) `layout: grid`
- C) `grid-template: true`
- D) `position: relative`

**Correct Answer:** A

**Explanation:** Setting `display: grid` on an element activates the CSS Grid formatting context, making all direct children become grid items that can be placed across defined rows and columns.

**Distractor Analysis:**

- Why A is correct: `display` is the core CSS property that establishes a formatting context — `display: grid` creates a block-level grid container.
- Why B is incorrect: `layout` is not a valid CSS property.
- Why C is incorrect: `grid-template` is used to define row and column tracks on an existing grid container — it does not activate grid layout on its own.
- Why D is incorrect: `position: relative` offsets an element from its normal flow position but does not create a grid context.

---

## Question 2

Which of the following is the most accurate definition of CSS sizing properties?

- A) CSS properties such as `width`, `height`, `min-width`, and `max-width` that constrain element dimensions; using relative units like `%`, `em`, or `vw` allows elements to scale proportionally with their parent or viewport.
- B) The CSS box model layers — margin, border, padding, and content — that determine the total rendered size and spacing of every page element.
- C) CSS `display` property values such as `block`, `inline`, `flex`, and `grid` that control how an element participates in document flow.
- D) A browser security model that prevents JavaScript on one origin from reading responses from a different origin unless the server sends permissive CORS headers.

**Correct Answer:** A

**Explanation:** CSS sizing properties (`width`, `height`, `min-width`, `max-width`) constrain element dimensions. Relative units (`%`, `em`, `vw`, `fr`) allow these values to scale proportionally.

**Distractor Analysis:**

- Why A is correct: This accurately describes CSS sizing properties and the role of relative units in responsive design.
- Why B is incorrect: This describes the CSS box model, which is a related but distinct concept.
- Why C is incorrect: This describes CSS display attributes, not sizing properties.
- Why D is incorrect: This describes CORS policy — a browser security mechanism unrelated to CSS sizing.

---

## Question 3

A developer wants to center a single flex item both horizontally and vertically inside its flex container. Which CSS declarations achieve this?

- A) `justify-content: center; align-items: center;` on the container
- B) `margin: auto;` on the container
- C) `text-align: center; vertical-align: middle;` on the container
- D) `position: center;` on the flex item

**Correct Answer:** A

**Explanation:** `justify-content: center` centers items along the main axis, and `align-items: center` centers them along the cross axis. Together they produce perfect horizontal and vertical centering inside a flex container.

**Distractor Analysis:**

- Why A is correct: These two flex container properties together center all child items on both axes.
- Why B is incorrect: `margin: auto` on the container centers the container itself within its parent — it does not center children inside the container.
- Why C is incorrect: `text-align` and `vertical-align` apply to inline or table-cell contexts, not flex containers.
- Why D is incorrect: `position: center` is not a valid CSS declaration.

---

## Question 4

While debugging a CSS Grid layout, a developer notices that grid items overflow their column boundaries and overlap adjacent cells. Which is the most likely root cause?

- A) The developer forgot to set `display: flex` before defining grid tracks.
- B) Explicit `width` values set on the items in pixels exceed the computed column track width, causing overflow that is not automatically clipped.
- C) CSS Grid automatically ignores `padding` values, causing items to expand beyond their boundaries.
- D) The `position: absolute` property is not required on all grid items to keep them inside their grid area.

**Correct Answer:** B

**Explanation:** Hard-coded pixel widths on grid items frequently exceed fractional or percentage-based column tracks, especially as the viewport narrows. The fix is to remove explicit pixel widths and let the grid algorithm size items.

**Distractor Analysis:**

- Why A is incorrect: `display: flex` and `display: grid` are separate layout models — setting `display: flex` on a grid container would override the grid context entirely.
- Why B is correct: Explicit pixel widths on grid items are the most common cause of overflow in Grid layouts.
- Why C is incorrect: CSS Grid does account for `padding` in size calculations — this is not a Grid limitation.
- Why D is incorrect: Grid items should not be positioned with `position: absolute` unless intentionally removed from grid flow.

---

## Question 5

Which CSS approach correctly implements a responsive two-column layout that collapses to a single column on screens narrower than 600px?

- A) Define a Flexbox container with `flex-wrap: wrap`, set each item to `flex: 1 1 300px`, and allow natural wrapping — no media query needed for this specific breakpoint.
- B) Use `display: block` on the container and `float: left; width: 50%` on each item, which automatically collapses at all screen sizes.
- C) Set `width: 200%` on each column and rely on the browser to auto-fit within the viewport.
- D) Use `position: fixed` on both columns so they remain side-by-side regardless of viewport width.

**Correct Answer:** A

**Explanation:** `flex: 1 1 300px` means each item starts at 300px and can grow or shrink. When the container is narrower than 600px (two 300px items cannot fit), they wrap to separate rows, producing a single-column layout automatically.

**Distractor Analysis:**

- Why A is correct: `flex-wrap: wrap` combined with `flex: 1 1 300px` creates automatic responsive wrapping without media queries.
- Why B is incorrect: Float-based layouts do not automatically collapse and require explicit media queries; floats are a legacy technique.
- Why C is incorrect: `width: 200%` would make each column twice the viewport width, causing severe overflow.
- Why D is incorrect: `position: fixed` removes elements from normal document flow and pins them to the viewport — not a layout technique for content columns.

---

## Question 6

A developer defines `grid-template-columns: 200px 1fr 2fr` on a container that is 800px wide. What are the computed widths of the three columns?

- A) 200px, 200px, 400px
- B) 200px, 300px, 300px
- C) 266px, 266px, 266px
- D) 200px, 400px, 200px

**Correct Answer:** A

**Explanation:** The fixed 200px column is allocated first, leaving 600px of available space. The remaining space is divided into three fractions (1fr + 2fr = 3 total parts): 1fr = 200px, 2fr = 400px. Final widths: 200px, 200px, 400px.

**Distractor Analysis:**

- Why A is correct: The fr unit divides remaining space proportionally after fixed columns are subtracted. 600px / 3 parts = 200px per fr.
- Why B is incorrect: This would result from dividing 600px into two equal halves (300px each), which would be `1fr 1fr` — not `1fr 2fr`.
- Why C is incorrect: This would result from dividing 800px into three equal parts with no fixed column — but 200px is a fixed size.
- Why D is incorrect: The 2fr column receives twice the space of the 1fr column — 400px, not 200px.

---

## Question 7

Which CSS property controls whether flex items wrap to new lines when they run out of space in the flex container?

- A) `overflow: wrap`
- B) `flex-wrap: wrap`
- C) `justify-content: wrap`
- D) `word-wrap: break-word`

**Correct Answer:** B

**Explanation:** `flex-wrap: wrap` on a Flexbox container allows items to wrap onto new rows (or columns in `flex-direction: column`) when they exceed the container's available space. The default value is `nowrap`, which causes overflow.

**Distractor Analysis:**

- Why A is incorrect: `overflow: wrap` is not a valid CSS declaration — `overflow` accepts values like `hidden`, `scroll`, and `auto`.
- Why B is correct: `flex-wrap` is the Flexbox property that controls wrapping behavior.
- Why C is incorrect: `justify-content` controls item distribution along the main axis — it does not control wrapping.
- Why D is incorrect: `word-wrap: break-word` (now `overflow-wrap: break-word`) controls how long words break within their containing box — it is a text-layout property unrelated to Flexbox wrapping.

---

## Question 8

A developer uses `grid-template-areas` to define a page layout. One grid area is named `"sidebar"`. How does a grid item claim that named area?

- A) Add `class="sidebar"` to the element — Grid automatically places classed elements into matching named areas.
- B) Add `grid-area: sidebar;` to the element's CSS rule.
- C) Add `position: sidebar;` to the element's CSS rule.
- D) Add `data-grid-area="sidebar"` as an HTML attribute to the element.

**Correct Answer:** B

**Explanation:** The `grid-area` property assigns a grid item to a named area defined in the container's `grid-template-areas` declaration. The name in `grid-area` must exactly match the name used in `grid-template-areas`.

**Distractor Analysis:**

- Why A is incorrect: CSS class names and grid area names are independent. The Grid algorithm does not inspect class names to place items.
- Why B is correct: `grid-area: sidebar` is the CSS property that maps a grid item to the `"sidebar"` named area defined on the container.
- Why C is incorrect: `position` accepts values like `static`, `relative`, `absolute`, and `fixed` — not area names.
- Why D is incorrect: `data-*` attributes are custom HTML attributes for JavaScript use — the CSS Grid engine does not read them for placement.

---

## Question 9

A developer needs the sidebar in a two-column grid to stick to the top of its grid cell rather than stretching to match the main content column's height. Which CSS declaration achieves this?

- A) `height: auto;` on the sidebar
- B) `align-self: start;` on the sidebar grid item
- C) `justify-self: flex-start;` on the sidebar grid item
- D) `vertical-align: top;` on the parent grid container

**Correct Answer:** B

**Explanation:** In a Grid layout, items stretch to fill their grid area by default (`align-self: stretch`). Setting `align-self: start` on the sidebar item aligns it to the top (start) of its grid cell rather than stretching to the full cell height.

**Distractor Analysis:**

- Why A is incorrect: `height: auto` allows the element to shrink to its content height, but without `align-self: start`, the Grid algorithm may still stretch it.
- Why B is correct: `align-self: start` overrides the default `stretch` alignment for an individual grid item, positioning it at the top of its cell.
- Why C is incorrect: `justify-self` controls horizontal placement within a grid cell — not vertical alignment. Also, `flex-start` is a Flexbox value; Grid uses `start`.
- Why D is incorrect: `vertical-align` applies to inline or table-cell elements — it has no effect on Grid item alignment.

---

## Question 10

After deploying updated CSS files to an AWS S3 bucket that is served through CloudFront, users report they still see the old styles. What is the correct procedure to serve the updated files?

- A) Delete the CloudFront distribution and recreate it pointing to the same S3 origin.
- B) Run `aws cloudfront create-invalidation --distribution-id DIST_ID --paths "/*"` to purge cached files from all edge locations.
- C) Change the S3 bucket's public-access settings to "Block all public access" and then re-enable it.
- D) Re-upload the CSS files with a different file name — CloudFront caches by URL, so renaming the file bypasses the cache automatically.

**Correct Answer:** B

**Explanation:** CloudFront caches objects at edge locations according to the Cache-Control headers. After deploying updated CSS to S3, a cache invalidation forces CloudFront edge locations to discard their cached copies and fetch fresh versions from S3 on the next request.

**Distractor Analysis:**

- Why A is incorrect: Recreating the CloudFront distribution is destructive, unnecessary, and causes downtime — cache invalidation is the correct tool.
- Why B is correct: `create-invalidation` with the path `"/*"` invalidates all cached objects. For production, invalidating only changed paths (for example, `"/styles.css"`) is more cost-efficient, as AWS charges per invalidation path above the free tier.
- Why C is incorrect: Toggling S3 public-access settings affects object permissions, not CloudFront's edge cache.
- Why D is incorrect: While cache-busting via filename changes (for example, `styles.abc123.css`) is a valid continuous deployment pattern, it requires updating all HTML references to the new filename — simply renaming in S3 without updating HTML references breaks the site.

---

### Question 11 (5 points)

A developer sets `display: none` on a sidebar to hide it on mobile. What is the accessibility consequence of this approach?

- A) The sidebar remains visible to screen readers because `display: none` only affects visual rendering.
- B) The sidebar is removed from both the visual layout and the accessibility tree, so screen reader users cannot access its content.
- C) The sidebar is hidden visually but remains keyboard-focusable, causing a confusing tab order.
- D) `display: none` is not valid CSS and has no effect on the element's rendering.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `display: none` removes the element from the accessibility tree entirely — screen readers cannot perceive or navigate to it.
  - Why B is correct: `display: none` removes the element from both the visual render tree and the accessibility tree, making it completely inaccessible to all users including screen reader users.
  - Why C is incorrect: Elements with `display: none` are also removed from the tab order — they cannot receive keyboard focus.
  - Why D is incorrect: `display: none` is a fully valid and widely supported CSS declaration.

---

### Question 12 (5 points)

What does `flex: 0 0 300px` mean for a flex item?

- A) The item can grow up to 300px, cannot shrink, and has no base size.
- B) The item cannot grow, cannot shrink, and has a fixed base size of 300px — it will always be exactly 300px wide.
- C) The item can grow 300 times its base size, can shrink, and starts at 0px.
- D) The item takes up 300% of the flex container's available width.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The first value is `flex-grow` (0 = cannot grow), not a maximum size. The third value (300px) is the flex-basis.
  - Why B is correct: `flex: 0 0 300px` sets grow to 0 (no growth), shrink to 0 (no shrink), and basis to 300px — the item is rigidly 300px regardless of container size.
  - Why C is incorrect: `flex-grow: 0` means no growth, and `flex-basis: 300px` is an initial size, not a multiplier.
  - Why D is incorrect: `flex-basis` is an initial size, not a percentage of the container unless a percentage unit is specified.

---

### Question 13 (5 points)

A developer uses `grid-column: 1 / -1` on a grid item. What does `-1` refer to?

- A) The item spans one column to the left of the first explicit column line.
- B) `-1` refers to the last explicit grid line, so the item spans all defined columns from start to end.
- C) The item is removed from grid placement and positioned absolutely within the grid container.
- D) `-1` is invalid in `grid-column` shorthand and will be ignored by the browser.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Negative line numbers count backward from the end of the explicit grid, not from before the first line.
  - Why B is correct: In CSS Grid, `-1` is shorthand for the last explicit grid line. `grid-column: 1 / -1` spans from the first line to the last explicit line, filling the full grid width.
  - Why C is incorrect: `grid-column` controls placement within grid flow — it does not affect the `position` property.
  - Why D is incorrect: Negative line numbers are fully valid in CSS Grid and well-supported in all modern browsers.

---

### Question 14 (5 points)

Which CSS property and value prevents margin collapse between vertically adjacent block elements?

- A) `margin: 0` on both elements
- B) Wrapping the adjacent elements in a flex or grid container, which creates a new formatting context that prevents margin collapse
- C) `display: inline` on the parent container
- D) `overflow: scroll` on each individual element

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Setting margin to 0 removes spacing but does not demonstrate margin collapse prevention — if either element has a non-zero margin, they will still collapse.
  - Why B is correct: Flex and Grid containers create a new block formatting context for their children, which suppresses margin collapse between adjacent flex or grid items.
  - Why C is incorrect: `display: inline` on a parent container removes block-level formatting entirely but does not specifically address margin collapse in a useful way.
  - Why D is incorrect: `overflow: scroll` on each item creates scroll containers but does not prevent margin collapse between siblings in normal block flow.

---

### Question 15 (5 points)

What is the difference between `auto-fill` and `auto-fit` in `grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))`?

- A) `auto-fill` requires a fixed number of columns; `auto-fit` calculates columns automatically.
- B) `auto-fill` creates as many column tracks as fit, leaving empty tracks if there are fewer items; `auto-fit` collapses empty tracks so existing items stretch to fill the row.
- C) `auto-fill` only works with pixel units; `auto-fit` works with any unit type including `fr`.
- D) `auto-fill` and `auto-fit` are identical — the difference only matters in Flexbox, not Grid.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Both `auto-fill` and `auto-fit` automatically calculate the number of columns — neither requires a fixed number.
  - Why B is correct: When there are fewer items than possible columns, `auto-fill` preserves the empty column tracks (maintaining a fixed number of columns), while `auto-fit` collapses empty tracks so items expand to fill the available space.
  - Why C is incorrect: Both keywords work with any valid track size unit, including `fr`, `px`, `%`, and `minmax()`.
  - Why D is incorrect: The `auto-fill`/`auto-fit` distinction only applies to CSS Grid; Flexbox uses `flex-wrap` for similar behavior and does not have these keywords.

---

### Question 16 (5 points)

A developer applies `align-self: stretch` to a grid item. What is the visual result?

- A) The item stretches horizontally to span all columns in the grid.
- B) The item expands vertically to fill the full height of its grid row track.
- C) The item is removed from the grid and stretches to fill the full page height.
- D) The item text content is justified to fill the full width of the element.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Horizontal spanning is controlled by `grid-column`, not `align-self`. `align-self` controls alignment on the block (vertical) axis.
  - Why B is correct: `align-self: stretch` is the default value — it causes the grid item to expand its height to match the tallest content in the same row track.
  - Why C is incorrect: `align-self` only affects the item's placement within its grid area, not the entire page.
  - Why D is incorrect: Text justification is controlled by the `text-align` property, not `align-self`.

---

### Question 17 (5 points)

Which shorthand correctly sets `flex-direction` to `column` and `flex-wrap` to `wrap` in a single declaration?

- A) `flex: column wrap;`
- B) `flex-flow: column wrap;`
- C) `flex-direction-wrap: column wrap;`
- D) `flex-layout: column wrap;`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `flex` is a shorthand for `flex-grow`, `flex-shrink`, and `flex-basis` on items — not for container direction and wrap properties.
  - Why B is correct: `flex-flow` is the official shorthand property that combines `flex-direction` and `flex-wrap` in a single declaration.
  - Why C is incorrect: `flex-direction-wrap` is not a valid CSS property.
  - Why D is incorrect: `flex-layout` is not a valid CSS property.

---

### Question 18 (5 points)

A developer wants to place a grid item in the second row and third column without using named template areas. Which declaration achieves this?

- A) `grid-position: 2 / 3;`
- B) `grid-area: 2 / 3;`
- C) `grid-row: 2; grid-column: 3;`
- D) `place-item: row 2 col 3;`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `grid-position` is not a valid CSS property.
  - Why B is incorrect: When `grid-area` is used with four slash-separated values it acts as a shorthand for row-start, column-start, row-end, column-end — `2 / 3` provides only two values and would be interpreted as row-start / column-start, starting the item at row 2, column 3, but the syntax `grid-area: 2 / 3` is ambiguous and non-standard for this intent.
  - Why C is correct: `grid-row: 2` places the item starting at row line 2, and `grid-column: 3` places it starting at column line 3 — together they precisely position the item in the second row, third column.
  - Why D is incorrect: `place-item` is not a valid CSS property; `place-items` (plural) is a shorthand for `align-items` and `justify-items` on the container.

---

### Question 19 (5 points)

What does `margin: 0 auto` achieve when applied to a block element with an explicit width?

- A) It removes all margin from the element and makes it flow inline with surrounding elements.
- B) It sets the top and bottom margins to 0 and distributes the remaining horizontal space equally as left and right margins, centering the block within its parent.
- C) It sets the left margin to 0 and automatically calculates the right margin based on the viewport.
- D) `margin: auto` is only valid on flex and grid items — it has no effect on block-level elements.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `margin: 0 auto` sets margins — it does not change the element's display type.
  - Why B is correct: The shorthand `margin: 0 auto` sets top/bottom to 0 and left/right to `auto`. With an explicit width, the browser distributes the remaining space equally on both sides, horizontally centering the block.
  - Why C is incorrect: `margin: 0 auto` applies `auto` to both left and right equally — not just the right margin.
  - Why D is incorrect: `margin: auto` works on block-level elements and is one of the oldest horizontal centering techniques in CSS, predating Flexbox and Grid.

---

### Question 20 (5 points)

Which CSS Grid property on a container sets equal spacing between columns only, without adding space between rows?

- A) `gap: 0 1.5rem;`
- B) `column-gap: 1.5rem;`
- C) `padding: 0 1.5rem;`
- D) `justify-content: space-between;`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `gap: 0 1.5rem` is valid (row-gap 0, column-gap 1.5rem) and produces the same result, but `column-gap` is the more explicit and readable single-axis property.
  - Why B is correct: `column-gap` applies spacing exclusively between column tracks and has no effect on row spacing, making it the most direct answer.
  - Why C is incorrect: `padding` on the container adds space inside the container's border, not between column tracks.
  - Why D is incorrect: `justify-content: space-between` distributes extra space between grid areas along the inline axis — it does not add fixed gutter-style gaps between columns.
