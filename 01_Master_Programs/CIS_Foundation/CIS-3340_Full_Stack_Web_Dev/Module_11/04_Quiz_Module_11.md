# Quiz: Module 11 — Node.js and Express

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

---

## Instructions

Select the single best answer for each question. Questions 4, 7, and 9 include code snippets — read them carefully before answering.

---

### Question 1

What distinguishes Node.js from browser-based JavaScript?

A. Node.js uses a different version of JavaScript that is incompatible with ECMAScript standards.

B. Node.js runs JavaScript outside the browser using the V8 engine, providing access to the file system, network sockets, and OS resources.

C. Node.js is only used for scripting and cannot serve HTTP requests.

D. Node.js uses synchronous I/O exclusively, making it faster than asynchronous alternatives.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — Node.js uses standard ECMAScript; the same JavaScript standards apply.
- C is incorrect — HTTP servers are one of Node.js's primary use cases.
- D is incorrect — Node.js is built around non-blocking asynchronous I/O, which is central to its performance model.

---

### Question 2

What is the purpose of `express.json()` middleware?

A. It converts all response data to JSON format before sending it to the client.

B. It parses incoming JSON request bodies and makes them available on `req.body`.

C. It validates that request bodies conform to a JSON schema.

D. It sets the `Content-Type: application/json` header on all responses.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `express.json()` parses incoming request bodies; `res.json()` handles serializing response data.
- C is incorrect — `express.json()` only parses; it does not validate schema. Validation is a separate concern.
- D is incorrect — response headers are set by `res.json()` or explicitly with `res.set()`.

---

### Question 3

A developer registers routes in this order in `server.js`:

```js
app.use('/api/users', usersRouter);
app.use(notFoundHandler);
app.use(errorHandler);
```

A request comes in for `GET /api/missing`. Which handlers execute?

A. `usersRouter` then `notFoundHandler` then `errorHandler`.

B. `notFoundHandler` only.

C. `usersRouter` (which finds no match), then `notFoundHandler`.

D. `errorHandler` because the route does not exist.

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — `errorHandler` only runs when `next(err)` is called with an error, not for every request.
- B is incorrect — Express still checks the `usersRouter` first since the path `/api/missing` does not start with `/api/users`... actually, wait: `/api/missing` does not match `/api/users`, so the router is not even entered. `notFoundHandler` runs directly. But the intent is: anything that passes through the router chain without a match hits `notFoundHandler`. C best describes the behavior when a router is mounted and the path partially matches.

**Revised Answer: B** — `GET /api/missing` does not match `/api/users`, so `usersRouter` is skipped entirely. Only `notFoundHandler` runs.

**Distractor Analysis (revised):**

- A and C are incorrect — `/api/missing` does not start with `/api/users`, so Express does not enter `usersRouter` at all.
- D is incorrect — `errorHandler` requires `next(err)` with an error argument to run; a simple unmatched route does not trigger it.

---

### Question 4

Consider the following Express route:

```js
router.get('/:id', (req, res) => {
  console.log(req.params.id);
  console.log(req.query.page);
  res.json({ id: req.params.id, page: req.query.page });
});
```

A client sends `GET /api/students/42?page=3`. What does the response body contain?

A. `{ "id": 42, "page": 3 }` with numeric types.

B. `{ "id": "42", "page": "3" }` with string types.

C. `{ "id": "42", "page": undefined }` because query params require explicit parsing.

D. An error because `req.query.page` is not defined in the route path.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — URL parameters and query strings are always strings in Express. You must explicitly call `parseInt()` to convert them.
- C is incorrect — `req.query.page` is `'3'` (a string), not `undefined`. Query parameters are available without any special setup when `express.json()` is configured.
- D is incorrect — query parameters do not need to be declared in the route path; Express populates `req.query` automatically from the URL.

---

### Question 5

What is the correct function signature for Express error-handling middleware?

A. `(err, req, res)`

B. `(req, res, next)`

C. `(err, req, res, next)`

D. `(req, err, res, next)`

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — Express requires exactly four parameters to identify error-handling middleware; three parameters are treated as regular middleware.
- B is incorrect — this is the signature for regular middleware; Express will not route errors to it.
- D is incorrect — the parameter order must be `(err, req, res, next)` exactly; Express inspects the function's parameter count using `.length`.

---

### Question 6

A developer wants validation middleware that checks for required fields before a POST route handler runs. Which is the correct way to apply it?

A. `router.post('/', handler, requireFields(['name', 'email']));`

B. `router.post('/', requireFields(['name', 'email']), handler);`

C. `app.use(requireFields(['name', 'email']));` applied globally before all routes.

D. `handler.before = requireFields(['name', 'email']);` attached as a property of the handler.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — middleware listed after the handler never runs because the handler terminates the request.
- C is technically functional but applies validation to every route in the app, which is overly broad and breaks GET endpoints that send no body.
- D is incorrect — Express does not support a `.before` property on handlers; that is not a valid pattern.

---

### Question 7

A developer writes this error-handling middleware:

```js
app.use((err, req, res) => {
  res.status(500).json({ error: err.message });
});
```

The middleware never receives errors forwarded with `next(err)`. Why?

A. `next` must be imported at the top of the file before it can be used in middleware.

B. Express identifies error-handling middleware by counting parameters — the function must have exactly four parameters `(err, req, res, next)`.

C. Error-handling middleware must be registered before routes, not after them.

D. `res.status(500)` must be called before `app.use` is called.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `next` is provided by Express as an argument; it does not need to be imported.
- C is incorrect — error-handling middleware must be registered after routes to catch errors from them.
- D is incorrect — middleware registration order is set at startup; response methods are called at request time, not during registration.

---

### Question 8

Which `res` method should be used to respond to a successful DELETE request with no body?

A. `res.status(200).json({ deleted: true })`

B. `res.status(204).send()`

C. `res.status(404).send()`

D. `res.status(200).end()`

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — returning a body with a 200 response is not the standard for DELETE. HTTP 204 No Content is the correct status for a successful deletion with no response body.
- C is incorrect — 404 indicates the resource was not found, not that it was deleted.
- D is technically possible but 200 implies a response body; 204 explicitly signals no body. `res.status(204).send()` is the standard.

---

### Question 9

Consider this project structure:

```text
project/
├── app.js      <- sets up Express, middleware, routes; exports app
├── server.js   <- calls app.listen(PORT)
```

Why is it beneficial to separate `app.js` from `server.js`?

A. It reduces the file size of each module, making JavaScript parsing faster.

B. It allows test suites to import `app.js` and make HTTP requests without starting an actual listening server.

C. Express requires `app.js` and `server.js` to be separate files or it throws an error.

D. `server.js` runs in the browser while `app.js` runs on the server.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — file size difference is negligible and not the reason for this pattern.
- C is incorrect — Express imposes no such requirement; the separation is a developer best practice.
- D is incorrect — both files run in Node.js on the server; neither runs in the browser.

---

### Question 10

An AWS Lambda function running Node.js receives this event from API Gateway proxy integration:

```json
{
  "httpMethod": "GET",
  "path": "/api/students",
  "pathParameters": null,
  "queryStringParameters": { "major": "CS" },
  "body": null
}
```

Which Express properties does this map to?

A. `req.method = 'GET'`, `req.query = { major: 'CS' }`, `req.body = null`

B. `req.httpMethod = 'GET'`, `req.path = '/api/students'`, `req.queryStringParameters = { major: 'CS' }`

C. `req.params.httpMethod`, `req.params.path`, `req.params.queryStringParameters`

D. Lambda and Express use completely different request models with no direct mapping.

**Correct Answer: A**

**Distractor Analysis:**

- B is incorrect — these are the raw Lambda event property names, not Express request properties. When using the `serverless-http` adapter or a similar bridge, the adapter maps Lambda's event shape to Express's `req` object.
- C is incorrect — `req.params` holds URL path parameters, not Lambda event fields.
- D is incorrect — the mapping is direct. `event.httpMethod -> req.method`, `event.queryStringParameters -> req.query`, `event.body -> req.body` (after JSON parse). This is how `serverless-http` and AWS Lambda Power Tools work.

---

### Question 11 (5 points)

What does `process.env.NODE_ENV` allow a Node.js application to do?

- A) Detect which version of Node.js is installed and automatically select compatible APIs.
- B) Switch behavior between development, test, and production environments — for example, logging stack traces only in development.
- C) Restrict which npm packages can be loaded based on the current environment.
- D) Automatically reload the server when `NODE_ENV` is set to `'development'`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Node.js version is available via `process.version` — `NODE_ENV` is a convention for environment names, not version detection.
  - Why B is correct: `NODE_ENV` is a widely-used convention. Libraries like Express, webpack, and Vite change their behavior based on it. Application code uses it to conditionally include debug output, stack traces, or verbose logging.
  - Why C is incorrect: npm package loading is not governed by `NODE_ENV` — all installed packages in `node_modules` are always loadable regardless of environment.
  - Why D is incorrect: Automatic reloading is handled by `nodemon` — it watches for file changes, not the `NODE_ENV` value.

---

### Question 12 (5 points)

A developer reads `req.params.id` from a URL like `/api/students/42` and passes it directly to a database query without calling `parseInt`. What type is `req.params.id`?

- A) `number` — Express automatically parses numeric URL segments.
- B) `string` — all URL parameters in Express are strings regardless of their content.
- C) `undefined` — `req.params` only contains parameters explicitly declared with `:name` in the route path.
- D) `number | string` — the type depends on the database driver.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Express performs no automatic type coercion on URL segments — everything in `req.params` is a string.
  - Why B is correct: URL components are text. `req.params.id` for `/api/students/42` is the string `'42'`, not the number `42`. Comparing it with strict equality `=== 42` (number) would fail.
  - Why C is incorrect: `:id` is a declared named parameter — `req.params.id` is populated with the matched segment value as a string.
  - Why D is incorrect: The database driver receives whatever type the application code passes — it does not determine the type of `req.params` values.

---

### Question 13 (5 points)

The `asyncHandler` wrapper pattern — `const asyncHandler = (fn) => (req, res, next) => Promise.resolve(fn(req, res, next)).catch(next)` — solves which specific problem?

- A) It prevents multiple `await` calls in the same route handler.
- B) It removes the need to write `try/catch` in every async route handler by forwarding any rejected promise to the Express error handler via `next`.
- C) It runs async route handlers in parallel when multiple requests arrive simultaneously.
- D) It ensures the route handler completes within a configurable timeout before sending a 503 response.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `asyncHandler` does not restrict the number of `await` calls — the wrapped function can use as many as needed.
  - Why B is correct: Without `asyncHandler`, an unhandled promise rejection in an `async` route function does not call `next(err)` — Express's error handler never receives it. `asyncHandler` catches the rejection and calls `next(err)` automatically.
  - Why C is incorrect: Node.js handles concurrent requests through the event loop — `asyncHandler` does not change concurrency behavior.
  - Why D is incorrect: `asyncHandler` provides no timeout functionality — a separate `AbortController` or middleware would be needed for timeouts.

---

### Question 14 (5 points)

Which security improvement does adding `helmet()` middleware to an Express app provide?

- A) It encrypts all traffic between the client and server using TLS.
- B) It sets security-focused HTTP response headers such as `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, and `Strict-Transport-Security` to reduce common browser-based attack vectors.
- C) It validates all incoming JSON payloads against a predefined schema.
- D) It rate-limits requests to prevent brute-force attacks.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: TLS encryption is handled at the infrastructure level (HTTPS) — `helmet` only sets HTTP response headers and does not encrypt traffic.
  - Why B is correct: `helmet` is a collection of small middleware functions that set HTTP headers. Each header addresses a specific browser security concern — MIME sniffing, clickjacking, cross-site scripting policy, etc.
  - Why C is incorrect: Schema validation is a separate concern handled by libraries like `joi`, `zod`, or the `requireFields` middleware pattern.
  - Why D is incorrect: Rate limiting requires a separate middleware such as `express-rate-limit` — `helmet` does not limit request frequency.

---

### Question 15 (5 points)

A developer creates a `NotFoundError` class extending `AppError` with `status = 404`. When `throw new NotFoundError('Student')` is used inside a route and caught by the global error handler, what does `err.status` equal?

- A) `500` — all unhandled errors default to status 500 unless overridden in the error handler.
- B) `undefined` — custom error classes do not inherit `status` from parent class constructors unless explicitly set.
- C) `404` — the `status` property was set in the `NotFoundError` constructor and is readable on the caught error object.
- D) `0` — the HTTP status code is only set when the error is attached to a response object.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The global error handler uses `err.status || 500` — since `err.status` is `404`, it returns `404`, not `500`.
  - Why B is incorrect: `this.status = 404` is set in the `AppError` base class constructor. The `NotFoundError` subclass inherits this via `super(...)`.
  - Why C is correct: The `AppError` constructor sets `this.status = status`. When `NotFoundError` calls `super(message, 404, 'NOT_FOUND')`, `err.status` becomes `404` and is available in the error handler.
  - Why D is incorrect: `err.status` is a plain JavaScript property on the error object — it exists independently of any HTTP response object.

---

### Question 16 (5 points)

`morgan` is registered with `app.use(morgan('dev'))` in development. What does `morgan` do?

- A) It monitors memory usage and restarts the server if it exceeds a threshold.
- B) It logs HTTP request details — method, URL, status code, response time, and body size — to the console for each request.
- C) It intercepts and modifies response bodies before they are sent to the client.
- D) It provides a GUI dashboard showing live request traffic at a separate port.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Memory monitoring is not morgan's function — it is a logging library.
  - Why B is correct: `morgan` is an HTTP request logger middleware. The `'dev'` format outputs concise colorized output including method, URL, status, response time, and content length.
  - Why C is incorrect: `morgan` is read-only — it observes the request and response but does not modify them.
  - Why D is incorrect: `morgan` outputs to the terminal (or a stream) — it does not provide a web dashboard.

---

### Question 17 (5 points)

A route handler calls `next(new ValidationError('Invalid email'))`. The `ValidationError` has `status = 400`. Which statements are true about how the global error handler receives this?

- A) Express ignores errors with `status < 500` — only server errors reach the error handler.
- B) The error bypasses all regular middleware and routes and goes directly to the `(err, req, res, next)` error handler, which uses `err.status` to set the response status code.
- C) `next(err)` is only valid when called from middleware — calling it from a route handler causes Express to crash.
- D) The error handler runs after the current route handler completes sending its response.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Express routes all errors to the error handler regardless of status code — there is no status-code filter.
  - Why B is correct: Calling `next(err)` from anywhere in the middleware stack immediately routes the request to the first four-parameter error handler registered after the failing point.
  - Why C is incorrect: `next(err)` can be called from route handlers, regular middleware, or any Express callback — there is no restriction.
  - Why D is incorrect: `next(err)` skips the remaining route logic — the route handler does not send a response before the error handler runs.

---

### Question 18 (5 points)

`path.join(__dirname, 'public', 'index.html')` is used in an Express route to serve a static HTML file. Why use `path.join` instead of the string `'./public/index.html'`?

- A) `path.join` compresses the file path to use fewer characters, improving performance.
- B) `path.join` builds cross-platform paths using the correct separator (`\` on Windows, `/` on Unix) and resolves `__dirname` to the file's absolute directory, preventing path errors when the server is run from a different working directory.
- C) String paths like `'./public/index.html'` are not supported by `res.sendFile`.
- D) `__dirname` is required by the Node.js module system to validate file ownership before reading.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `path.join` provides no performance benefit — it is a correctness tool.
  - Why B is correct: `__dirname` is the absolute path of the current file's directory. `path.join` assembles path segments with the OS-correct separator. This combination ensures the path is valid regardless of where the `node` command is run from.
  - Why C is incorrect: `res.sendFile` does accept relative paths, but they are resolved relative to the process's current working directory, not the file's location — which is why `__dirname` is preferred.
  - Why D is incorrect: `__dirname` is a module-scope variable automatically provided by Node.js — it has no security or ownership validation role.

---

### Question 19 (5 points)

A developer separates the Express app into `app.js` (setup and routes) and `server.js` (`app.listen`). `app.js` ends with `module.exports = app`. What does this pattern enable?

- A) It prevents the server from starting when `app.js` is imported — only `server.js` starts the HTTP listener.
- B) It allows `app.js` to be imported by a test file that uses `supertest` to make HTTP requests without binding a real port, keeping tests fast and isolated.
- C) It ensures `app.js` runs in a child process while `server.js` runs in the main process.
- D) It is required by Express — calling `app.listen` inside the same file as `app.use` throws an error.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Both A and B are true — not starting the HTTP listener is the mechanism, but the purpose of that separation is to enable testing, which makes B the more complete and accurate answer.
  - Why B is correct: Test frameworks like Jest with `supertest` import `app` directly. `supertest(app)` creates an in-process HTTP server bound to a random port for the duration of the test. If `listen()` were called inside `app.js`, it would also bind on import.
  - Why C is incorrect: `app.js` and `server.js` run in the same Node.js process — there is no child process separation.
  - Why D is incorrect: Express imposes no such constraint — `app.listen()` can be called anywhere in the same file.

---

### Question 20 (5 points)

A Node.js API deployed on AWS Lambda reads `process.env.DB_PASSWORD` at runtime. Where is this environment variable configured in a production Lambda deployment?

- A) In the `.env` file bundled inside the Lambda deployment package (zip file).
- B) In the Lambda function's environment variable configuration in the AWS console or via infrastructure-as-code (CloudFormation, CDK, SAM) — Lambda injects these into `process.env` at runtime.
- C) In the `package.json` `"scripts"` section as `"start": "DB_PASSWORD=secret node index.js"`.
- D) In the Lambda execution IAM role's inline policy as a string variable.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `.env` files should never be committed or bundled in a deployment package — they would be visible to anyone who downloads the package. Lambda environment variables are the correct mechanism.
  - Why B is correct: Lambda has a built-in environment variable store. Values set there are injected into the function's `process.env` at startup. For sensitive values like passwords, AWS Secrets Manager or Parameter Store is preferred, with the secret ARN passed as an environment variable.
  - Why C is incorrect: Lambda does not use shell scripts to start the function — the handler is invoked directly by the runtime.
  - Why D is incorrect: IAM policies define permissions, not configuration values — environment variables cannot be stored there.
