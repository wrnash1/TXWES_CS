# Reading Guide: Module 08 - Server-Side Routing & Middleware
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 08 - Server-Side Routing & Middleware**! This module deepens your Express.js knowledge by focusing on middleware — the functions that sit between an incoming HTTP request and the final route handler — and on advanced routing patterns including parameterized routes, nested routers, and error handling middleware. Understanding Express middleware is essential for building production-ready APIs with authentication, logging, input validation, and CORS support. These patterns also appear in AWS API Gateway authorizers and Lambda middleware layers.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Middleware pipeline**: The ordered sequence of functions in an Express application that process an incoming HTTP request before the final route handler sends a response. Each middleware function receives the `req` (request), `res` (response), and `next` objects. Middleware can read and modify `req`/`res`, end the response cycle, or pass control to the next function by calling `next()`. The pipeline executes in the order middleware is registered with `app.use()`.
*   **Request parsing**: The process of extracting structured data from incoming HTTP request bodies and headers. Express provides `express.json()` (parses `application/json` bodies into `req.body`), `express.urlencoded()` (parses form-encoded bodies), and `express.static()` (serves static files). Without request parsing middleware, `req.body` is `undefined` and raw request data is inaccessible to route handlers.
*   **Routing parameters**: Named URL path segments preceded by a colon (`:`) that capture variable values from the URL into `req.params`. For example, defining a route as `app.get('/users/:id', handler)` captures the value after `/users/` into `req.params.id`. Multiple parameters can appear in a single route (`/users/:userId/orders/:orderId`), and `req.query` captures URL query string parameters (`?status=active`).
*   **CORS handling**: Cross-Origin Resource Sharing configuration that allows (or restricts) browsers from making requests to an API from a different origin. In Express, the `cors` npm package provides a `cors()` middleware that sets the `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and `Access-Control-Allow-Headers` response headers. Without CORS headers, browsers block responses from cross-origin API requests as a security measure.
*   **next() function**: The third argument passed to every Express middleware function. Calling `next()` passes control to the next middleware or route handler in the pipeline. Calling `next(error)` with an argument skips all remaining non-error middleware and passes control to the error-handling middleware (which has the signature `(err, req, res, next)`). Forgetting to call `next()` when not sending a response will cause the request to hang indefinitely.

---

### 2. Certification Exam Tips
*   **AWS API Gateway Authorizers Mirror Middleware:** AWS API Gateway Lambda Authorizers function like authentication middleware — they receive the request, validate a token, and either allow or deny the request before it reaches the backend Lambda. Understanding how Express authentication middleware works (`req.user`, JWT verification, `next()` vs. `res.status(401)`) directly maps to how you design and troubleshoot API Gateway authorizers on the DVA-C02 exam.
*   **CORS Must Be Configured on API Gateway:** The DVA-C02 exam includes scenarios where a React front-end cannot reach an API Gateway endpoint due to missing CORS headers. API Gateway has a built-in CORS configuration panel — know that `OPTIONS` preflight requests must be handled and that `Access-Control-Allow-Origin` must match the front-end origin.
*   **Study Resource:** The Express.js documentation on routing and middleware is the most concise reference. [Express.js — Writing Middleware](https://expressjs.com/en/guide/writing-middleware.html) and [Express.js — Router](https://expressjs.com/en/guide/routing.html) cover the complete API for middleware registration and route parameterization.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Server-Side Routing & Middleware** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3) — Part 3 covers middleware, parameterized routes, and error handling in Express.
*   **Required Video:** Watch the Express middleware and routing section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering `app.use()`, `next()`, and parameterized route patterns.

---

### Lab & Command Integration
In this week's hands-on lab, you will build and test Express middleware and parameterized routes:
*   **Implement logging middleware printing timestamp data**: Write a custom `app.use()` middleware that logs `[timestamp] METHOD /path` to the console for every incoming request, then calls `next()` to pass control to the route handler.
*   **Create parameterized routes (e.g., /users/:id)**: Define a `GET /api/users/:id` route, extract `req.params.id`, and return a JSON response with the matching user data (or `404` if not found).
*   **Configure JSON request body parsing**: Register `app.use(express.json())` globally and verify that `POST /api/users` correctly populates `req.body` by logging it inside the handler and testing with a JSON Postman request.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 3 covering **Server-Side Routing & Middleware** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3).
- [ ] Watch the Express middleware section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Install the `cors` and `morgan` npm packages and experiment with them before starting the lab: `npm install cors morgan`.
- [ ] Proceed to the weekly hands-on lab activity.
