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

```
project/
├── app.js      ← sets up Express, middleware, routes; exports app
├── server.js   ← calls app.listen(PORT)
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
- D is incorrect — the mapping is direct. `event.httpMethod → req.method`, `event.queryStringParameters → req.query`, `event.body → req.body` (after JSON parse). This is how `serverless-http` and AWS Lambda Power Tools work.
