# Quiz: Module 07 - Node.js & Express Server

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which code snippet correctly initializes a basic Express application instance?

- A) `const app = express()`
- B) `const app = new express.App()`
- C) `const app = require('express').start()`
- D) `const app = Express.init()`

**Correct Answer:** A

**Explanation:** The `express` module exports a factory function. Calling it with `express()` creates and returns a new application instance. The full pattern is `const express = require('express'); const app = express();`.

**Distractor Analysis:**

- Why A is correct: `express` is a factory function — invoking it returns the application object.
- Why B is incorrect: `express.App` is not a class. Express does not use `new` for instantiation.
- Why C is incorrect: The Express module does not expose a `.start()` method.
- Why D is incorrect: `Express.init()` is not valid. `express` is lowercase and called as a function.

---

## Question 2

Which of the following is the most accurate definition of server setup in an Express application?

- A) The process of provisioning an AWS EC2 instance, attaching an Elastic IP, and configuring SSH key pairs.
- B) Initializing an Express application, configuring global middleware, defining route handlers, and calling `app.listen()` to bind the server to a network port.
- C) Containerizing a Node.js application with Docker, building an image, and pushing it to Amazon ECR for ECS deployment.
- D) The configuration of IAM roles and security groups that control which AWS services an EC2 instance can access.

**Correct Answer:** B

**Explanation:** Server setup in Express refers to the code-level steps: creating the app with `express()`, registering middleware with `app.use()`, defining routes, and calling `app.listen()` to start accepting connections.

**Distractor Analysis:**

- Why A is incorrect: This describes EC2 provisioning — an infrastructure task, not Express application setup.
- Why B is correct: These are the four code-level steps required to stand up an Express server.
- Why C is incorrect: This describes Docker containerization and ECR — a CI/CD and container concept.
- Why D is incorrect: This describes AWS IAM and security group configuration — cloud access control, not application setup.

---

## Question 3

A developer needs an Express server that automatically restarts whenever a source file is saved during development. Which command enables this behavior?

- A) `node index.js`
- B) `nodemon index.js`
- C) `npm start --watch`
- D) `pm2 start index.js`

**Correct Answer:** B

**Explanation:** `nodemon` monitors the project directory for file changes and automatically restarts the Node.js process. It is installed as a dev dependency and invoked via the `npm run dev` script defined in `package.json`.

**Distractor Analysis:**

- Why A is incorrect: `node index.js` starts once and does not watch for changes — manual restart required.
- Why B is correct: `nodemon` is the standard development-time auto-restart tool for Node.js.
- Why C is incorrect: `npm start --watch` is not a standard npm CLI flag — behavior depends on `package.json` scripts.
- Why D is incorrect: `pm2` is a production process manager for clustering and persistence, not development-time file watching.

---

## Question 4

An Express server running on an EC2 instance is unreachable from the internet even though the application is listening on port 3000. What is the most likely cause?

- A) Node.js cannot listen on ports above 1024 without superuser privileges.
- B) The EC2 instance's security group does not have an inbound rule allowing TCP traffic on port 3000.
- C) Express requires a valid SSL certificate before it will accept inbound connections.
- D) `app.listen()` must be called with `'0.0.0.0'` as the host to accept external connections.

**Correct Answer:** B

**Explanation:** AWS security groups act as instance-level firewalls. A new EC2 instance blocks all inbound traffic by default. Port 3000 must be explicitly added as an inbound rule in the security group associated with the instance.

**Distractor Analysis:**

- Why A is incorrect: Node.js can listen on any port above 1024 without elevated privileges on Linux.
- Why B is correct: Missing security group inbound rule is the most common cause of an EC2-hosted server being unreachable.
- Why C is incorrect: Express does not require SSL to accept connections — HTTPS is optional and configured separately.
- Why D is incorrect: `app.listen(3000)` without a host argument binds to all interfaces (`0.0.0.0`) by default.

---

## Question 5

A Node.js/Express API processes POST requests but `req.body` is always `undefined`. What is the most likely fix?

- A) Add `Content-Type: text/plain` as a request header instead of `application/json`.
- B) Register `express.json()` middleware before the route handlers.
- C) Change the route from `app.post()` to `app.get()` since `req.body` is only populated on GET requests.
- D) Set `app.enable('body-parser')` in the Express configuration.

**Correct Answer:** B

**Explanation:** `app.use(express.json())` registers the built-in JSON body parser as global middleware. Without it, Express does not parse the incoming request body and `req.body` remains `undefined` for all routes.

**Distractor Analysis:**

- Why A is incorrect: Changing to `text/plain` would make the body a raw string, and `req.body` would still be undefined without body-parsing middleware.
- Why B is correct: `express.json()` must be registered before any route that reads `req.body`.
- Why C is incorrect: `req.body` is populated for POST, PUT, and PATCH — not GET requests, which have no body.
- Why D is incorrect: `app.enable('body-parser')` is not a valid Express configuration option.

---

## Question 6

A developer writes a DELETE route handler but adds `return res.status(204).json({})` instead of `return res.status(204).send()`. What problem does this cause?

- A) No problem — `204` with an empty JSON object `{}` is semantically equivalent to `204` with no body.
- B) Express throws an unhandled exception because `json()` requires a non-empty object.
- C) The HTTP `204 No Content` status code means the response body must be empty. Sending a body with `204` violates the HTTP specification and may cause parsing errors in some clients.
- D) Thunder Client and Postman block all `204` responses regardless of body content.

**Correct Answer:** C

**Explanation:** The HTTP specification defines `204 No Content` as a response with no message body. Sending `{}` with a `204` violates this constraint. While most browsers tolerate it, strict clients and proxies may reject or misparse the response. The correct pattern is `res.status(204).send()`.

**Distractor Analysis:**

- Why A is incorrect: The HTTP specification explicitly defines `204` as having no response body — `{}` is not semantically equivalent to "no body."
- Why B is incorrect: Express does not throw when `json({})` is called — it sends the JSON body without error, but the resulting response violates the spec.
- Why C is correct: `204` must have no body per RFC 7231 — use `res.status(204).send()` for DELETE success responses.
- Why D is incorrect: Postman and Thunder Client do not block `204` responses — they display whatever the server returns.

---

## Question 7

Which of the following describes the correct order for registering middleware and routes in an Express application?

- A) Define all routes first, then register `express.json()` so it applies only to responses.
- B) Register `express.json()` and other global middleware before route definitions so `req.body` is populated when route handlers execute.
- C) Route registration order does not matter because Express processes all middleware after all routes are matched.
- D) `express.json()` only needs to be registered once per route, not globally with `app.use()`.

**Correct Answer:** B

**Explanation:** Express processes middleware and routes in the order they are registered. If `express.json()` is registered after a route definition, POST requests handled by that route will have `req.body === undefined` because the body parser has not yet run.

**Distractor Analysis:**

- Why A is incorrect: `express.json()` parses the request body before routes run — it is not applied to responses.
- Why B is correct: Middleware registered with `app.use()` before routes runs for every request before the route handler executes.
- Why C is incorrect: Express processes middleware in registration order, not after all routes are matched.
- Why D is incorrect: `express.json()` must be registered globally with `app.use()` to apply to all routes — registering it per-route is not standard practice.

---

## Question 8

A developer adds a fifth parameter `(err, req, res, next, extra)` to the global error handler function. What is the consequence?

- A) No change — Express ignores extra parameters in middleware functions.
- B) Express no longer recognizes the function as an error handler because error handlers must have exactly four parameters `(err, req, res, next)`. Errors will go unhandled.
- C) The function receives an additional `extra` object containing request metadata from API Gateway.
- D) Express throws a startup error and the server will not start.

**Correct Answer:** B

**Explanation:** Express identifies error-handling middleware by the presence of exactly four parameters. A function with five parameters is treated as regular middleware, not an error handler. Errors forwarded with `next(err)` will go unhandled, typically resulting in a hanging request or a default error response.

**Distractor Analysis:**

- Why A is incorrect: Express does not ignore the parameter count — the arity of the function determines how Express classifies it.
- Why B is correct: The four-parameter signature is the contract that tells Express the function is an error handler.
- Why C is incorrect: Express does not inject API Gateway metadata into middleware parameters — that is a Lambda-specific concern.
- Why D is incorrect: Express does not validate middleware function signatures at startup — the misconfiguration silently fails at runtime.

---

## Question 9

A developer wants to read a query parameter from the URL `GET /api/books?sort=title&page=2`. Which code correctly reads both values?

- A) `const sort = req.params.sort; const page = req.params.page;`
- B) `const sort = req.body.sort; const page = req.body.page;`
- C) `const { sort, page } = req.query;`
- D) `const sort = req.headers['sort']; const page = req.headers['page'];`

**Correct Answer:** C

**Explanation:** Query string parameters (`?key=value`) are available on the `req.query` object. Path parameters (`:id` in the URL pattern) are on `req.params`. Request body fields are on `req.body`. Headers are on `req.headers`. These four objects are distinct and not interchangeable.

**Distractor Analysis:**

- Why A is incorrect: `req.params` contains URL path parameters defined with `:name` in the route pattern — not query string parameters.
- Why B is incorrect: `req.body` contains the parsed JSON or form data request body — not query string parameters.
- Why C is correct: `req.query` is the correct object for query string parameters.
- Why D is incorrect: `req.headers` contains HTTP request headers — not URL query parameters.

---

## Question 10

An AWS Lambda function written in Node.js is deployed behind API Gateway. The function runs successfully but API Gateway returns a `502 Bad Gateway` error to the client. What is the most likely cause?

- A) The Lambda function exceeded the 29-second API Gateway integration timeout.
- B) The Lambda function returned a plain string instead of the required response object with `statusCode`, `headers`, and `body` fields.
- C) The IAM execution role does not have permission to invoke the Lambda function.
- D) The Lambda function used `console.log()` which causes a `502` when CloudWatch Logs is unavailable.

**Correct Answer:** B

**Explanation:** API Gateway Lambda proxy integrations require the function to return a specific object structure: `{ statusCode, headers, body }`. If the function returns a plain string, `undefined`, or an object missing `statusCode`, API Gateway cannot construct a valid HTTP response and returns `502 Bad Gateway`. This mirrors the Express pattern where every route must call `res.status().json()` — the Lambda equivalent is returning the structured response object.

**Distractor Analysis:**

- Why A is incorrect: A timeout produces a `504 Gateway Timeout`, not a `502 Bad Gateway`.
- Why B is correct: The `502` in API Gateway integrations is the standard symptom of a malformed Lambda response object — always the first thing to check.
- Why C is incorrect: An IAM permission error produces a `403 Forbidden` from API Gateway — not a `502`.
- Why D is incorrect: `console.log()` writes to CloudWatch Logs and does not affect the HTTP response — it never causes a `502`.
