# Quiz: Module 11 - Frontend Frameworks (React)
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
How does React's Virtual DOM improve application rendering performance?
*   A) It pre-renders all components on the server and sends fully formed HTML to the browser, eliminating the need for client-side JavaScript execution.
*   B) It compiles JSX directly to machine code during the build step, bypassing the JavaScript engine's JIT compilation.
*   C) It computes a diff between the previous and new in-memory component trees (reconciliation) and updates only the changed elements in the real DOM — avoiding expensive full-page repaints.
*   D) It caches all DOM elements in localStorage so they do not need to be re-queried on subsequent renders.
*   **Correct Answer:** C) It computes a diff between the previous and new in-memory component trees (reconciliation) and updates only the changed elements in the real DOM — avoiding expensive full-page repaints.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Server-Side Rendering (SSR) — a separate technique. Standard React renders on the client side.
    *   *Why B is incorrect:* JSX is compiled to `React.createElement()` calls by Babel — not to machine code. The JavaScript engine handles execution.
    *   *Why C is correct:* React's reconciliation algorithm compares Virtual DOM snapshots and batches the minimal real DOM mutations needed, reducing browser reflow and repaint costs.
    *   *Why D is incorrect:* React does not store DOM elements in localStorage — caching DOM queries in local variables is a JavaScript optimization technique unrelated to React's Virtual DOM.

---

**Question 2**
Which of the following is the most accurate definition of **React components**?
*   A) HTML `<section>` and `<article>` semantic elements that define reusable page regions without JavaScript functionality.
*   B) Self-contained JavaScript functions (or classes) that accept input data via `props` and return JSX describing a portion of the user interface — composable into a complete application tree.
*   C) CSS class definitions that apply visual styles to groups of related HTML elements across multiple pages of an application.
*   D) SQL stored procedures that components invoke to fetch data from a relational database without writing explicit query strings.
*   **Correct Answer:** B) Self-contained JavaScript functions (or classes) that accept input data via `props` and return JSX describing a portion of the user interface — composable into a complete application tree.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* HTML semantic elements are markup constructs — they do not contain JavaScript logic, state, or composable behavior.
    *   *Why B is correct:* React components are the fundamental unit of a React application — reusable, isolated functions that render UI based on their input (`props`) and internal state.
    *   *Why C is incorrect:* CSS classes style HTML elements but are not JavaScript components — they have no behavior, props, or lifecycle.
    *   *Why D is incorrect:* SQL stored procedures run on a database server — React components are client-side JavaScript UI primitives.

---

**Question 3**
A developer writes valid HTML and pastes it into a React component's return statement, but the build fails. What is the most likely cause?
*   A) React does not support standard HTML elements — all markup must use React's proprietary element library.
*   B) The HTML uses `class` and `for` attributes, which are reserved JavaScript keywords — JSX requires `className` and `htmlFor` instead.
*   C) The component is missing a default export — React requires every component file to use `module.exports`.
*   D) The HTML contains inline styles with hyphenated property names (`font-size`) — JSX only supports camelCase style properties (`fontSize`).
*   **Correct Answer:** B) The HTML uses `class` and `for` attributes, which are reserved JavaScript keywords — JSX requires `className` and `htmlFor` instead.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* React components can render any standard HTML element — JSX just uses slightly different attribute names for a handful of reserved-word conflicts.
    *   *Why B is correct:* `class` is a reserved JavaScript keyword (used for ES6 class definitions) and `for` is used in `for` loops — JSX uses `className` and `htmlFor` to avoid the conflict.
    *   *Why C is incorrect:* React components use ES Module syntax (`export default` or named exports) — `module.exports` is CommonJS syntax and would not cause a JSX compilation failure.
    *   *Why D is incorrect:* Both hyphenated attribute values in HTML and camelCase style properties in JSX refer to different things — inline `style` objects in JSX do use camelCase, but this is a runtime warning, not a build failure.

---

**Question 4**
A developer deploys a React SPA to AWS S3 static website hosting. The root URL (`/`) loads correctly, but directly navigating to any other route (e.g., `/dashboard`) returns a 403 error. What is the cause?
*   A) S3 static website hosting does not support HTTPS — the application must be moved to EC2.
*   B) The React Router routes are defined on the client side — S3 does not know about them and returns a 403 (or 404) for any path that does not correspond to a real file. The fix is to configure the S3 error document to redirect to `index.html`, or use CloudFront with a custom error response for 403/404 that serves `index.html`.
*   C) React SPAs cannot use S3 for hosting — they require an Express server to serve the `index.html` file for all routes.
*   D) The IAM bucket policy is missing `s3:GetObject` permission for the specific `/dashboard` path — adding a separate policy statement for each route resolves the issue.
*   **Correct Answer:** B) The React Router routes are defined on the client side — S3 does not know about them and returns a 403 (or 404) for any path that does not correspond to a real file. The fix is to configure the S3 error document to redirect to `index.html`, or use CloudFront with a custom error response.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* S3 static website hosting supports HTTPS when combined with CloudFront — HTTPS is not the cause of the routing error.
    *   *Why B is correct:* In a React SPA, all routes are handled by React Router in `index.html` — the server must serve `index.html` for every path, not just `/`.
    *   *Why C is incorrect:* React SPAs work perfectly with S3 static hosting when properly configured — no server-side rendering is required.
    *   *Why D is incorrect:* A single `s3:GetObject` on `/*` covers all objects in the bucket — separate route-level policies are neither necessary nor effective.

---

**Question 5**
Which command produces an optimized production build of a React application created with Vite or Create React App?
*   A) `npm run dev`
*   B) `npm run build`
*   C) `npm start`
*   D) `npx react-compile --prod`
*   **Correct Answer:** B) `npm run build` compiles the React application with minification, tree-shaking, and code splitting — producing a `build/` or `dist/` directory of static assets ready for deployment to S3, CloudFront, or any static web server.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `npm run dev` starts the local development server with hot module replacement — it does not produce a production build.
    *   *Why B is correct:* `npm run build` is the standard command in both Create React App and Vite projects to produce optimized production assets.
    *   *Why C is incorrect:* `npm start` in Create React App also starts the development server (equivalent to `npm run dev`) — not a production build.
    *   *Why D is incorrect:* `npx react-compile --prod` is not a real command — production builds are managed through the project's own `package.json` build script.
