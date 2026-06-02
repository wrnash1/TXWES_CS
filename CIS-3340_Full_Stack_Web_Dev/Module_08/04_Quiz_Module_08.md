# Quiz: Module 08 - Server-Side Routing & Middleware

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

What function must be invoked at the end of a custom Express middleware handler to pass control to the next function in the pipeline?

- A) `end()`
- B) `send()`
- C) `next()`
- D) `forward()`

**Correct Answer:** C

**Explanation:** `next()` is the third parameter in every middleware function signature `(req, res, next)`. Calling it tells Express to advance to the next registered middleware or route handler. Failing to call `next()` and not sending a response causes the request to hang indefinitely.

**Distractor Analysis:**

- Why A is incorrect: `res.end()` terminates the response and sends it to the client — it does not advance the middleware pipeline.
- Why B is incorrect: `res.send()` sends a response body and ends the request — it does not pass control forward.
- Why C is correct: `next()` progresses to the next handler in the middleware stack.
- Why D is incorrect: `forward()` is not an Express API method.

---

## Question 2

Which of the following is the most accurate definition of the middleware pipeline in Express?

- A) The sequence of `package.json` scripts that npm executes when running `npm run build`.
- B) The ordered chain of functions registered with `app.use()` that process an HTTP request in sequence — each function can modify `req` or `res` or pass control forward by calling `next()`.
- C) The AWS CodePipeline stages (Source, Build, Deploy) that automate CI/CD deployments.
- D) The list of database migration scripts that run in order when initializing a new application schema.

**Correct Answer:** B

**Explanation:** The Express middleware pipeline is the request-processing chain. Each function registered with `app.use()` receives the request, optionally modifies it, and either sends a response or calls `next()` to pass control to the next function.

**Distractor Analysis:**

- Why A is incorrect: This describes an npm build pipeline — not Express middleware.
- Why B is correct: The middleware pipeline processes every request through an ordered sequence of functions.
- Why C is incorrect: This describes AWS CodePipeline — a CI/CD service unrelated to Express.
- Why D is incorrect: This describes database migration scripts — a data management concept.

---

## Question 3

An Express route is defined as `app.get('/products/:category/:id', handler)`. A client requests `GET /products/electronics/42`. What values are available in `req.params`?

- A) `{ category: 'electronics', id: '42' }`
- B) `{ 0: 'electronics', 1: '42' }`
- C) `{ path: '/products/electronics/42' }`
- D) `{ query: 'category=electronics&id=42' }`

**Correct Answer:** A

**Explanation:** Express maps each named path parameter (`:category`, `:id`) to its corresponding URL segment and exposes them as string properties on `req.params`. Note that all values are strings — `'42'` not `42`.

**Distractor Analysis:**

- Why A is correct: Named route parameters are accessible by name as string values on `req.params`.
- Why B is incorrect: `req.params` uses parameter names as keys, not numeric indices.
- Why C is incorrect: The full URL path is available on `req.path` — not inside `req.params`.
- Why D is incorrect: Query string parameters are on `req.query` — not `req.params`.

---

## Question 4

A React front-end running on `http://localhost:3000` sends a `fetch()` request to an Express API on `http://localhost:5000`. The browser logs a CORS error. Which Express configuration resolves this?

- A) Change the React app's port to 5000 so both apps share the same origin.
- B) Add `app.use(cors())` using the `cors` npm package on the Express server to send `Access-Control-Allow-Origin` headers in responses.
- C) Add `mode: 'no-cors'` to the `fetch()` options — this disables the Same-Origin Policy for the request.
- D) Move both applications behind an HTTPS proxy — the CORS error only occurs on HTTP origins.

**Correct Answer:** B

**Explanation:** CORS errors are resolved on the server side by adding `Access-Control-Allow-Origin` response headers. The `cors` npm middleware sets these headers automatically. The browser blocks cross-origin responses that lack the appropriate CORS headers.

**Distractor Analysis:**

- Why A is incorrect: Two Node.js servers cannot share the same port on the same machine — and this is not a scalable production solution.
- Why B is correct: `app.use(cors())` adds the required CORS response headers.
- Why C is incorrect: `mode: 'no-cors'` makes the response opaque — JavaScript cannot read the response body, making it useless for API calls.
- Why D is incorrect: CORS is origin-based (scheme + host + port) — switching to HTTPS does not resolve cross-origin issues if the origins differ.

---

## Question 5

An Express error-handling middleware must have which specific function signature to be recognized by Express as an error handler?

- A) `(req, res, next) => { }` — standard three-argument middleware
- B) `(err, req, res, next) => { }` — four arguments with error as the first parameter
- C) `(error) => { }` — a single-argument handler that only receives the error object
- D) A `try { } catch(err) { }` block wrapped around the route definition

**Correct Answer:** B

**Explanation:** Express identifies error-handling middleware by the presence of exactly four parameters. The error object is the first parameter. This function is invoked when any upstream route or middleware calls `next(err)`. With three or fewer parameters, Express treats the function as regular middleware.

**Distractor Analysis:**

- Why A is incorrect: Three-argument middleware is standard middleware — Express does not treat it as an error handler.
- Why B is correct: The four-parameter signature `(err, req, res, next)` is the contract for an Express error handler.
- Why C is incorrect: A single-argument function is not a recognized Express middleware signature.
- Why D is incorrect: `try/catch` handles synchronous errors locally — it does not register a handler in the Express middleware pipeline.

---

## Question 6

A developer mounts an Express router at `/api/users` with `app.use('/api/users', usersRouter)`. Inside the router, a route is defined as `router.get('/:id', handler)`. Which URL does a GET request to `/api/users/42` match?

- A) The route does not match because the router's internal path must include the full prefix `/api/users/:id`.
- B) The route matches `/:id` and `req.params.id` equals `'42'` — Express strips the mount prefix before matching against router-internal paths.
- C) The route matches but `req.params.id` equals `'/api/users/42'` — the full path is stored in params.
- D) The request matches only if the router is also registered with `app.get('/api/users/:id', ...)` directly on the app object.

**Correct Answer:** B

**Explanation:** When a router is mounted at `/api/users`, Express strips that prefix before comparing the remaining URL segment against the router's internal routes. A request to `/api/users/42` is presented to the router as `/42`, which matches the `/:id` pattern. `req.params.id` is `'42'`.

**Distractor Analysis:**

- Why A is incorrect: Router-internal routes use paths relative to the mount point — not the full URL path.
- Why B is correct: Express removes the mount prefix during router dispatch.
- Why C is incorrect: `req.params.id` contains only the captured segment value, not the full URL.
- Why D is incorrect: Direct `app.get()` registration is not required when using `app.use()` with a router.

---

## Question 7

A validation middleware factory `requireFields(['title', 'author'])` is applied to a POST route. A client sends a request body `{ "title": "Dune", "genre": "sci-fi" }`. What does the middleware return?

- A) Status `200` — the `title` field is present, so validation passes.
- B) Status `400` with a `details` array listing `author` as missing.
- C) Status `422` — the body is syntactically valid but missing a field.
- D) The middleware calls `next()` and the route handler receives `req.body.author` as `undefined`.

**Correct Answer:** B

**Explanation:** The `requireFields` factory checks that all listed fields are present and non-empty in `req.body`. Since `author` is not in the request body, the middleware responds with `400 Bad Request` and a `details` array identifying the missing field. The route handler never executes.

**Distractor Analysis:**

- Why A is incorrect: All required fields must be present — not just one. The `author` field is missing.
- Why B is correct: `400` with a field-level `details` array is the correct validation error response.
- Why C is incorrect: `422 Unprocessable Entity` is used when the body is semantically invalid (e.g., a value fails business-logic constraints) — missing required fields are typically `400`.
- Why D is incorrect: The middleware is designed to block the request — it does not call `next()` when required fields are absent.

---

## Question 8

A developer adds CORS middleware after the route definitions in `index.js`. A React app sending a POST request receives a CORS error even though the route executes successfully. What is the root cause?

- A) POST requests are not covered by the `cors()` middleware — a separate `app.options()` handler is required.
- B) CORS middleware registered after routes only applies to responses from the 404 catch-all, not from defined routes. The route response was sent before the CORS headers were added.
- C) CORS headers must be set at the AWS API Gateway level — Express cannot add CORS headers.
- D) The CORS middleware requires a second `app.use(cors())` call specifically for POST routes.

**Correct Answer:** B

**Explanation:** Middleware runs in the order it is registered. If CORS middleware is registered after route definitions, the route handler sends its response before the CORS middleware has a chance to add the `Access-Control-Allow-Origin` header. The browser receives a response without CORS headers and blocks it. CORS middleware must be registered before routes.

**Distractor Analysis:**

- Why A is incorrect: The `cors()` middleware handles all methods including POST and automatically responds to OPTIONS preflight requests.
- Why B is correct: Registration order determines execution order. CORS must come before routes.
- Why C is incorrect: Express can and should add CORS headers for local development — API Gateway handles CORS separately in production.
- Why D is incorrect: A single `app.use(cors())` applies to all routes when registered globally before route definitions.

---

## Question 9

A request logger middleware uses `res.on('finish', callback)` to log the status code. Why is this approach preferable to logging inside the middleware function before calling `next()`?

- A) `res.on('finish')` runs synchronously — it is faster than the alternative.
- B) The `finish` event fires after the response is sent, which allows the logger to record the actual HTTP status code and response duration — these values are not available before the route handler runs.
- C) `res.on('finish')` is required by the Express specification — other approaches are not supported.
- D) Logging before `next()` prevents the request from reaching the route handler.

**Correct Answer:** B

**Explanation:** When the logger middleware runs before calling `next()`, the route handler has not yet executed, so `res.statusCode` is still the default (`200`) and the response duration is not known. The `finish` event fires after the response is fully sent, providing access to the final status code and the elapsed time since the logger began.

**Distractor Analysis:**

- Why A is incorrect: `res.on('finish')` registers an asynchronous event listener — it does not run synchronously during middleware execution.
- Why B is correct: The `finish` event captures the actual status code and allows duration measurement.
- Why C is incorrect: This is a design choice, not an Express specification requirement.
- Why D is incorrect: Calling `next()` after attaching the event listener passes control forward without blocking — it does not prevent the route from running.

---

## Question 10

In AWS API Gateway, a Lambda Authorizer is configured on a protected endpoint. A client sends a request with an invalid JWT token. What response does the client receive?

- A) `500 Internal Server Error` — the Lambda function throws an unhandled exception when the token is invalid.
- B) `403 Forbidden` — the Lambda Authorizer returns a deny policy and API Gateway blocks the request before the main Lambda function is invoked.
- C) `401 Unauthorized` — API Gateway automatically inspects the JWT and returns `401` for invalid tokens.
- D) `404 Not Found` — API Gateway hides protected endpoints from clients that are not authenticated.

**Correct Answer:** B

**Explanation:** A Lambda Authorizer evaluates the request (typically inspecting an Authorization header) and returns an IAM policy document allowing or denying access. When it returns a deny policy, API Gateway returns `403 Forbidden` without invoking the main Lambda function. This is the AWS equivalent of Express route-level authentication middleware calling `res.status(403).json(...)` instead of `next()`.

**Distractor Analysis:**

- Why A is incorrect: The Authorizer function handles the invalid token and returns a policy — it does not throw an unhandled exception for an invalid token if coded correctly.
- Why B is correct: Lambda Authorizers that return a deny policy produce a `403` from API Gateway.
- Why C is incorrect: API Gateway does not automatically parse JWTs for Lambda Authorizers — that logic is in the Authorizer function code. (JWT Authorizers in HTTP API mode do parse tokens, but the question describes a Lambda Authorizer.)
- Why D is incorrect: API Gateway does not hide endpoints — protected endpoints return `403` when access is denied, not `404`.
