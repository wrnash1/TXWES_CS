# Quiz: Module 02 - Modern CSS Layouts
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which CSS property converts an element into a grid container?
*   A) `display: grid`
*   B) `layout: grid`
*   C) `grid-template: true`
*   D) `position: relative`
*   **Correct Answer:** A) Setting `display: grid` on an element activates the CSS Grid formatting context, making all direct children become grid items that can be placed across defined rows and columns.
*   **Distractor Analysis:**
    *   *Why A is correct:* `display` is the core CSS property that establishes a formatting context — `display: grid` creates a block-level grid container.
    *   *Why B is incorrect:* `layout` is not a valid CSS property.
    *   *Why C is incorrect:* `grid-template` is used to define row/column tracks on an existing grid container — it does not activate grid layout on its own.
    *   *Why D is incorrect:* `position: relative` offsets an element from its normal flow position but does not create a grid context.

---

**Question 2**
Which of the following is the most accurate definition of **sizing properties** in CSS?
*   A) CSS properties such as `width`, `height`, `min-width`, and `max-width` that constrain element dimensions; using relative units like `%`, `em`, or `vw` allows elements to scale proportionally with their parent or viewport.
*   B) The CSS box model layers — margin, border, padding, and content — that determine the total rendered size and spacing of every page element.
*   C) CSS `display` property values (`block`, `inline`, `flex`, `grid`) that control how an element participates in document flow and establishes a formatting context for its children.
*   D) A browser security model that prevents JavaScript on one origin from reading responses from a different origin unless the server sends permissive CORS headers.
*   **Correct Answer:** A) CSS properties such as `width`, `height`, `min-width`, and `max-width` that constrain element dimensions; using relative units like `%`, `em`, or `vw` allows elements to scale proportionally with their parent or viewport.
*   **Distractor Analysis:**
    *   *Why A is correct:* This accurately describes CSS sizing properties and the role of relative units in responsive design.
    *   *Why B is incorrect:* This describes the CSS box model, which is a related but distinct concept.
    *   *Why C is incorrect:* This describes CSS display attributes, not sizing properties.
    *   *Why D is incorrect:* This describes the Cross-Origin Resource Sharing (CORS) policy — a browser security mechanism unrelated to CSS sizing.

---

**Question 3**
A developer wants to center a single flex item both horizontally and vertically inside its flex container. Which CSS declarations achieve this?
*   A) `justify-content: center; align-items: center;` on the container
*   B) `margin: auto;` on the container
*   C) `text-align: center; vertical-align: middle;` on the container
*   D) `position: center;` on the flex item
*   **Correct Answer:** A) `justify-content: center` centers items along the main axis, and `align-items: center` centers them along the cross axis — together they produce perfect horizontal and vertical centering inside a flex container.
*   **Distractor Analysis:**
    *   *Why A is correct:* These two flex container properties together center all child items on both axes.
    *   *Why B is incorrect:* `margin: auto` on the container centers the container itself within its parent — it does not center children inside the container.
    *   *Why C is incorrect:* `text-align` and `vertical-align` apply to inline or table-cell contexts, not flex containers.
    *   *Why D is incorrect:* `position: center` is not a valid CSS declaration.

---

**Question 4**
While debugging a CSS Grid layout, a developer notices that grid items overflow their column boundaries and overlap adjacent cells. Which is the most likely root cause?
*   A) The developer forgot to set `display: flex` before defining grid tracks.
*   B) Explicit `width` values set on the items in pixels exceed the computed column track width, causing overflow that is not automatically clipped.
*   C) CSS Grid automatically ignores `padding` values, causing items to expand beyond their boundaries.
*   D) The `position: absolute` property is not required on all grid items to keep them inside their grid area.
*   **Correct Answer:** B) Explicit `width` values set on the items in pixels exceed the computed column track width, causing overflow that is not automatically clipped.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `display: flex` and `display: grid` are separate layout models — setting `display: flex` on a grid container would override the grid context entirely.
    *   *Why B is correct:* Hard-coded pixel widths on grid items frequently exceed fractional (`fr`) or percentage-based column tracks, especially as viewport narrows.
    *   *Why C is incorrect:* CSS Grid does account for `padding` in size calculations; this is not a Grid limitation.
    *   *Why D is incorrect:* Grid items should not be positioned with `position: absolute` unless intentionally removed from grid flow; doing so removes them from the layout algorithm.

---

**Question 5**
Which CSS approach correctly implements a responsive two-column layout that collapses to a single column on screens narrower than 600px?
*   A) Define a Flexbox container with `flex-wrap: wrap`, set each item to `flex: 1 1 300px`, and allow natural wrapping — no media query needed for this specific breakpoint.
*   B) Use `display: block` on the container and `float: left; width: 50%` on each item, which automatically collapses at all screen sizes.
*   C) Set `width: 200%` on each column and rely on the browser to auto-fit within the viewport.
*   D) Use `position: fixed` on both columns so they remain side-by-side regardless of viewport width.
*   **Correct Answer:** A) Define a Flexbox container with `flex-wrap: wrap`, set each item to `flex: 1 1 300px`, and allow natural wrapping — no media query needed for this specific breakpoint.
*   **Distractor Analysis:**
    *   *Why A is correct:* `flex: 1 1 300px` means each item starts at 300px and can grow or shrink. When the container is narrower than 600px (two 300px items), they wrap to separate rows, producing a single-column layout automatically.
    *   *Why B is incorrect:* `float`-based layouts do not automatically collapse and require explicit media queries; floats are a legacy technique discouraged in modern CSS.
    *   *Why C is incorrect:* `width: 200%` would make each column twice the width of the viewport, causing severe overflow.
    *   *Why D is incorrect:* `position: fixed` removes elements from normal document flow and pins them to the viewport — not a layout technique for content columns.
