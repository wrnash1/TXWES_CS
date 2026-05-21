# Quiz: Module 08 - Server-Side Routing & Middleware
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
What function must be invoked at the end of a custom Express middleware handler to pass control to the next function in line?
*   A) `end()`
*   B) `send()`
*   C) `next()`
*   D) `forward()`
*   **Correct Answer:** C) Calling `next()` tells Express to advance to the subsequent middleware or route handler in the pipeline. Failing to call `next()` or send a response will cause the request to hang.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `res.end()` terminates the response and sends it to the client — it does not advance the middleware pipeline.
    *   *Why B is incorrect:* `res.send()` sends a response body and ends the request — it does not pass control forward.
    *   *Why C is correct:* `next()` is the third parameter in every middleware function signature `(req, res, next)` — invoking it progresses to the next registered handler.
    *   *Why D is incorrect:* `forward()` is not an Express API method.

---

**Question 2**
Which of the following is the most accurate definition of the **middleware pipeline** in Express?
*   A) The sequence of `package.json` scripts that npm executes when running `npm run build` to compile and bundle a front-end application.
*   B) The ordered chain of functions registered with `app.use()` that process an HTTP request in sequence — each function can modify `req`/`res` or pass control to the next function by calling `next()`.
*   C) The AWS CodePipeline stages (Source → Build → Deploy) that automate the CI/CD workflow for deploying application updates to production.
*   D) The list of database migration scripts that run in order when initializing a new application schema in PostgreSQL.
*   **Correct Answer:** B) The ordered chain of functions registered with `app.use()` that process an HTTP request in sequence — each function can modify `req`/`res` or pass control to the next function by calling `next()`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes an npm build pipeline — not Express middleware.
    *   *Why B is correct:* The Express middleware pipeline is the request-processing chain where each registered function receives the request, optionally transforms it, and either responds or calls `next()`.
    *   *Why C is incorrect:* This describes AWS CodePipeline — a CI/CD service, not an Express middleware concept.
    *   *Why D is incorrect:* This describes database migration scripts — a data management concept unrelated to Express middleware.

---

**Question 3**
An Express route is defined as `app.get('/products/:category/:id', handler)`. A client requests `GET /products/electronics/42`. What values are available in `req.params`?
*   A) `{ category: 'electronics', id: '42' }`
*   B) `{ 0: 'electronics', 1: '42' }`
*   C) `{ path: '/products/electronics/42' }`
*   D) `{ query: 'category=electronics&id=42' }`
*   **Correct Answer:** A) `{ category: 'electronics', id: '42' }` — Express maps each named path parameter (`:category`, `:id`) to its corresponding URL segment and exposes them as string properties on `req.params`.
*   **Distractor Analysis:**
    *   *Why A is correct:* Named route parameters are accessible by their declared names as string values on `req.params`.
    *   *Why B is incorrect:* `req.params` uses the parameter names as keys, not numeric indices.
    *   *Why C is incorrect:* The full URL path is available on `req.path` or `req.url` — not inside `req.params`.
    *   *Why D is incorrect:* Query string parameters (`?key=value`) are parsed into `req.query` — not `req.params`. Path segments and query strings are separate in Express.

---

**Question 4**
A React front-end running on `http://localhost:3000` sends a `fetch()` request to an Express API on `http://localhost:5000`. The browser logs a CORS error. Which Express configuration resolves this?
*   A) Change the React app's port to 5000 so both apps share the same origin.
*   B) Add `app.use(cors())` using the `cors` npm package on the Express server to send `Access-Control-Allow-Origin` headers in responses.
*   C) Add `mode: 'no-cors'` to the `fetch()` options — this disables the Same-Origin Policy for the request.
*   D) Move both applications behind an HTTPS proxy — the CORS error only occurs on HTTP origins.
*   **Correct Answer:** B) Add `app.use(cors())` using the `cors` npm package on the Express server to send `Access-Control-Allow-Origin` headers in responses.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running both on the same port is not possible since each server needs a unique port on the same machine; additionally, this is not a scalable solution for production cross-origin APIs.
    *   *Why B is correct:* CORS errors are resolved on the server side by adding the appropriate `Access-Control-Allow-Origin` response header. The `cors` npm middleware sets this automatically.
    *   *Why C is incorrect:* `mode: 'no-cors'` makes the response opaque — the browser receives it but JavaScript cannot read the response body, making it useless for API calls.
    *   *Why D is incorrect:* CORS is origin-based (scheme + host + port) — switching from HTTP to HTTPS changes the scheme portion of the origin but does not resolve cross-origin issues if the origins remain different.

---

**Question 5**
An Express error-handling middleware must have which specific function signature to be recognized by Express as an error handler?
*   A) `(req, res, next) => { }` — standard three-argument middleware
*   B) `(err, req, res, next) => { }` — four arguments with error as the first parameter
*   C) `(error) => { }` — a single-argument handler that only receives the error object
*   D) `try { } catch(err) { }` — a try/catch block wrapped around the route definition
*   **Correct Answer:** B) `(err, req, res, next) => { }` — Express specifically identifies error-handling middleware by the presence of four parameters; the error object is passed as the first argument when `next(error)` is called.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Three-argument middleware `(req, res, next)` is standard middleware — Express does not treat it as an error handler.
    *   *Why B is correct:* Express recognizes a four-argument middleware function as an error handler — it is only invoked when `next(error)` is called upstream.
    *   *Why C is incorrect:* A single-argument function is not a recognized Express middleware or error handler signature.
    *   *Why D is incorrect:* `try/catch` handles synchronous errors within a function — it does not register an error handler in the Express middleware pipeline.
