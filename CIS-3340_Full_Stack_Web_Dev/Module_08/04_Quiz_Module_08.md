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

---

### Question 11 (5 points)

A developer defines `router.route('/books/:id').get(getOne).put(replaceOne).delete(removeOne)`. What is the primary benefit of chaining handlers with `router.route()` compared to three separate `router.get()`, `router.put()`, `router.delete()` calls?

- A) `router.route()` runs all three handlers in sequence for every request to that path.
- B) `router.route()` eliminates duplication of the path string and makes it clear that all three methods operate on the same resource.
- C) `router.route()` is required when a path has more than one HTTP method — Express throws an error otherwise.
- D) `router.route()` automatically generates a 405 response for unsupported methods with no additional configuration.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Each HTTP method handler runs independently for its respective request method — they do not execute in sequence.
  - Why B is correct: `router.route()` groups all method handlers for a single path, reducing repetition and co-locating related logic.
  - Why C is incorrect: Multiple `router.get()` / `router.put()` calls on the same path are perfectly valid — `router.route()` is a convenience, not a requirement.
  - Why D is incorrect: Express does not automatically return 405 for unregistered methods — unmatched requests fall through to the next middleware or the 404 catch-all.

---

### Question 12 (5 points)

Which Express middleware is required to parse URL-encoded form data submitted by an HTML `<form>` with `method="POST"` and `enctype="application/x-www-form-urlencoded"`?

- A) `express.json()`
- B) `express.urlencoded({ extended: false })`
- C) `express.text()`
- D) `express.multipart()`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `express.json()` parses `application/json` bodies — it does not handle URL-encoded form data.
  - Why B is correct: `express.urlencoded()` parses `application/x-www-form-urlencoded` bodies and populates `req.body`.
  - Why C is incorrect: `express.text()` parses plain-text bodies (`text/plain`) — not form-encoded data.
  - Why D is incorrect: `express.multipart()` does not exist in Express — multipart form data (file uploads) requires a third-party package such as `multer`.

---

### Question 13 (5 points)

A router file exports `router` and is mounted at `/api/v1/authors` in `index.js`. Inside the router, `router.get('/', listAll)` is defined. A developer also tries `router.get('/api/v1/authors', listAll)` thinking the full path is required. What happens when a client sends `GET /api/v1/authors`?

- A) Both routes match and `listAll` executes twice, sending two responses.
- B) Only `router.get('/', listAll)` matches. The path `/api/v1/authors` inside the router would only match `GET /api/v1/authors/api/v1/authors`.
- C) Only `router.get('/api/v1/authors', listAll)` matches — Express ignores paths that are just `/`.
- D) Neither route matches because the router must be mounted at the root path `/` to handle `/api/v1/authors`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Express matches the first route that fits and does not re-invoke handlers unless `next('route')` or `next()` is called.
  - Why B is correct: The mount prefix is stripped, so `/api/v1/authors` → `/` inside the router. The full-path route `/api/v1/authors` inside the router would require the request URL to be `/api/v1/authors/api/v1/authors`.
  - Why C is incorrect: `/` inside a router correctly matches requests to the mount point — it is the collection endpoint.
  - Why D is incorrect: Routers can be mounted at any path — the mount path determines the URL prefix that is stripped.

---

### Question 14 (5 points)

`res.locals` is an object attached to every response object in Express. What is its primary purpose?

- A) Storing response headers before they are sent to the client.
- B) Passing data from one middleware function to downstream middleware and route handlers within a single request-response cycle.
- C) Persisting user session data between requests.
- D) Configuring Express application settings such as the view engine.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Response headers are managed via `res.set()` or `res.setHeader()` — not `res.locals`.
  - Why B is correct: `res.locals` provides a request-scoped object for sharing data (e.g., authenticated user info) between middleware and route handlers without modifying `req`.
  - Why C is incorrect: `res.locals` is cleared at the end of each request — it does not persist across requests. Session data requires a session store.
  - Why D is incorrect: Application settings are configured with `app.set()` — not `res.locals`.

---

### Question 15 (5 points)

A middleware function calls `res.status(401).json({ error: 'Unauthorized' })` but does NOT call `next()`. A route handler is registered for the same path after this middleware. What happens?

- A) Both the middleware response and the route handler response are sent — the client receives two responses.
- B) Express throws an `ERR_HTTP_HEADERS_SENT` error because two handlers attempt to respond.
- C) The route handler never executes. Once a middleware sends a response without calling `next()`, the pipeline stops for that request.
- D) The middleware response is ignored and the route handler response is used.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: HTTP does not support multiple responses per request — only one response is sent.
  - Why B is incorrect: `ERR_HTTP_HEADERS_SENT` only occurs if code attempts to send a second response after the first is already sent. Here the pipeline stops, so the route handler never runs.
  - Why C is correct: Not calling `next()` terminates request processing at that middleware. Subsequent handlers in the pipeline are skipped.
  - Why D is incorrect: The first response sent wins — there is no mechanism to discard a sent response in favor of a later one.

---

### Question 16 (5 points)

`router.param('id', callback)` is a special Express method. What does it do?

- A) It validates that the `id` parameter is present in the query string before any route handler runs.
- B) It registers a callback that runs automatically before any route handler whose path contains `:id`, receiving the parameter value as an argument.
- C) It replaces `req.params.id` with the result of a database lookup and blocks the route if no record is found.
- D) It restricts the `:id` route parameter to numeric values only and returns 400 for non-numeric IDs.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `router.param()` watches path parameters (`:id`), not query string parameters.
  - Why B is correct: `router.param('id', fn)` registers a pre-processing callback `(req, res, next, value)` that runs for any route on that router containing `:id`.
  - Why C is incorrect: The callback can perform a lookup and call `next()` or `next(err)`, but this behavior is user-written — `router.param()` itself does not enforce any database behavior.
  - Why D is incorrect: `router.param()` does not impose type restrictions — any validation logic must be written explicitly inside the callback.

---

### Question 17 (5 points)

The `helmet` package is installed and registered with `app.use(helmet())` in an Express application. What does `helmet` do?

- A) It encrypts the request body using AES-256 before storing it in `req.body`.
- B) It sets several security-related HTTP response headers such as `X-Content-Type-Options`, `X-Frame-Options`, and `Strict-Transport-Security` to reduce common web vulnerabilities.
- C) It validates JSON Web Tokens on every request and returns `401` if no valid token is present.
- D) It compresses response bodies with gzip to improve performance.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `helmet` does not encrypt request bodies — it only sets response headers.
  - Why B is correct: `helmet` is a collection of small middleware functions that set HTTP headers to mitigate cross-site scripting, clickjacking, MIME sniffing, and other browser-based attacks.
  - Why C is incorrect: JWT validation is the responsibility of a separate authentication middleware — `helmet` has no knowledge of tokens.
  - Why D is incorrect: Response compression is handled by the `compression` middleware package, not `helmet`.

---

### Question 18 (5 points)

A rate-limiting middleware is applied globally with `app.use(rateLimit({ windowMs: 60000, max: 100 }))`. After 100 requests within one minute from the same IP address, what HTTP status does the middleware return?

- A) `403 Forbidden` — the IP is permanently blocked.
- B) `429 Too Many Requests` — the limit has been exceeded and the client must wait before retrying.
- C) `503 Service Unavailable` — the server is overloaded.
- D) `401 Unauthorized` — the client must authenticate before making more requests.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Rate limiting produces a temporary `429` — it does not permanently block the IP with `403`.
  - Why B is correct: `429 Too Many Requests` is the standard status code for rate limit violations. The limit resets after the `windowMs` period.
  - Why C is incorrect: `503` indicates server-side overload or maintenance — not a client-side rate limit.
  - Why D is incorrect: `401` relates to authentication, not request frequency.

---

### Question 19 (5 points)

A developer accesses `req.app` inside a middleware function registered on a sub-router. What does `req.app` refer to?

- A) The `Router` instance the middleware is attached to.
- B) The top-level Express `app` object — the same object returned by `express()` in `index.js`.
- C) The `http.Server` instance created by `app.listen()`.
- D) The `package.json` metadata for the application.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `req.app` is not the router — it is the top-level application instance.
  - Why B is correct: Express sets `req.app` to the main application object, giving middleware and route handlers access to app-level settings and methods regardless of which router they are mounted in.
  - Why C is incorrect: The HTTP server created by `app.listen()` is a separate object — it is not accessible via `req.app`.
  - Why D is incorrect: `package.json` metadata is not attached to `req.app` — it would be accessed via `require('../package.json')`.

---

### Question 20 (5 points)

A CORS preflight request is an HTTP `OPTIONS` request sent by the browser before a cross-origin `POST` with a custom header. If the `cors()` middleware is registered but the Express app has no `app.options('*', ...)` handler, what happens to the preflight request?

- A) The preflight fails because Express requires an explicit `app.options()` handler for every protected route.
- B) The `cors()` middleware intercepts `OPTIONS` requests and responds automatically with the correct `Access-Control-Allow-*` headers — no separate `app.options()` handler is needed for basic CORS.
- C) The preflight succeeds but the actual POST request is still blocked because CORS only affects GET requests.
- D) Express returns `404` for all `OPTIONS` requests unless they are explicitly registered.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `cors()` handles preflight internally — explicit `app.options()` routes are only needed for fine-grained per-route control.
  - Why B is correct: When `cors()` is registered globally, it intercepts `OPTIONS` preflight requests and responds with the appropriate CORS headers, allowing the browser to proceed with the actual request.
  - Why C is incorrect: CORS applies to all cross-origin requests regardless of HTTP method — not only GET.
  - Why D is incorrect: `cors()` handles `OPTIONS` before the request reaches the route-matching stage — it does not fall through to a 404.
