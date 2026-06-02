# Video Script: Module 06 - RESTful API Principles

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 22 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code, Postman or Thunder Client (VS Code REST client extension)
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for Postman/browser
- Demonstrate each HTTP method using Postman against a live mock API
- Show request headers, body, and response status codes

---

## Section 1: Introduction - What is REST? [00:00 - 04:00]

Welcome to Module 06. I am Professor Nash. This is where we shift from front-end development to back-end design. For the last five modules we have been consumers of APIs — fetching data with `fetch()` and displaying it in the DOM. Starting today, we learn to design and build the APIs that those fetch calls talk to.

REST stands for Representational State Transfer. It is an architectural style — not a protocol — defined by Roy Fielding in his 2000 doctoral dissertation. REST describes how distributed systems should be structured to be scalable, maintainable, and interoperable. When developers talk about a "REST API" or a "RESTful endpoint," they mean a web API that follows these principles.

This module covers REST from the API design perspective: resource naming, HTTP methods and their semantics, status codes, and the six architectural constraints that make an API truly RESTful.

**AWS Exam Tip:** API Gateway on AWS is the managed service for building REST APIs at scale. DVA-C02 questions about API Gateway consistently test HTTP method semantics (especially idempotency of PUT vs. POST), status codes, and the difference between REST and HTTP APIs in API Gateway. Understanding the principles in this module makes those questions straightforward.

[SHOW BROWSER]

Let me open Postman and show you what a well-designed REST API looks like from the client's perspective before we dive into the design principles.

---

## Section 2: Resources and URL Design [04:00 - 09:00]

[SHOW CODE]

The fundamental concept in REST is the resource. A resource is any named concept the API exposes: users, products, orders, articles, comments. Resources are represented as nouns in URL paths.

Good REST URL design:

```
# Collections (plural nouns)
GET    /api/users           # list all users
POST   /api/users           # create a new user

# Individual resources (identified by ID in path)
GET    /api/users/42        # get user with ID 42
PUT    /api/users/42        # replace user 42 completely
PATCH  /api/users/42        # partially update user 42
DELETE /api/users/42        # delete user 42

# Nested resources (related sub-resources)
GET    /api/users/42/orders        # all orders belonging to user 42
GET    /api/users/42/orders/7      # specific order 7 for user 42

# Filtering and pagination with query parameters
GET    /api/products?category=electronics&page=2&limit=20

# Search
GET    /api/products?q=laptop
```

Bad REST URL design (anti-patterns to avoid):

```
GET    /api/getUsers        # verb in URL — HTTP method is the verb
POST   /api/deleteUser/42   # wrong method for deletion
GET    /api/user            # inconsistent singular vs. plural
POST   /api/users/create    # redundant — POST to /users already means create
```

[SHOW BROWSER]

Let me demonstrate the difference in Postman. I will call `GET /users` (returns a list) and `GET /users/1` (returns one user) against the JSONPlaceholder mock API.

---

## Section 3: HTTP Methods and Their Semantics [09:00 - 14:30]

[SHOW CODE]

Each HTTP method has a defined semantic meaning. Understanding these semantics is critical for API design.

The five primary HTTP methods and their properties:

| Method | Operation | Safe | Idempotent | Has Body |
|---|---|---|---|---|
| GET | Read resource | Yes | Yes | No |
| POST | Create resource | No | No | Yes |
| PUT | Replace resource | No | Yes | Yes |
| PATCH | Partial update | No | No | Yes |
| DELETE | Remove resource | No | Yes | No |

Safe means the request does not modify server state. Idempotent means calling it N times has the same effect as calling it once.

The idempotency distinction matters for AWS:

```
POST /api/orders          → creates a new order each time → NOT idempotent
PUT  /api/orders/42       → replaces order 42 with this data → idempotent
DELETE /api/orders/42     → deletes order 42 → idempotent (deleting twice = same state)
GET  /api/orders          → reads without changing → safe AND idempotent
```

When a Lambda function behind API Gateway is called three times due to network retries, a `POST` endpoint creates three orders. A `PUT` or `DELETE` endpoint produces the same final state regardless of retries. This is why idempotency matters for reliability in distributed systems.

**AWS Exam Tip:** This is directly tested on DVA-C02. Know that POST is non-idempotent. API Gateway and Lambda retry logic make idempotency a real design concern, not just a theoretical concept. Idempotency keys (a client-generated UUID sent with the request) are the standard solution for making POST endpoints safe to retry.

---

## Section 4: HTTP Status Codes [14:30 - 18:30]

[SHOW CODE]

Status codes communicate the outcome of every HTTP request. A well-designed API uses the right code every time.

```
2xx — Success
200 OK           — successful read (GET, PUT, PATCH)
201 Created      — new resource created (POST); include Location header
204 No Content   — successful write with no response body (DELETE, PUT)

3xx — Redirection
301 Moved Permanently    — URL has changed; update your bookmarks
304 Not Modified         — cached version is still current

4xx — Client Error (the request is wrong)
400 Bad Request          — malformed request body or invalid parameters
401 Unauthorized         — authentication required or token invalid
403 Forbidden            — authenticated but not authorized
404 Not Found            — resource does not exist
405 Method Not Allowed   — wrong HTTP method for this endpoint
409 Conflict             — state conflict (e.g., duplicate resource)
422 Unprocessable Entity — request is well-formed but semantically invalid
429 Too Many Requests    — rate limit exceeded

5xx — Server Error (the server failed to handle a valid request)
500 Internal Server Error — unhandled exception
502 Bad Gateway           — upstream server returned invalid response
503 Service Unavailable   — server overloaded or in maintenance
504 Gateway Timeout       — upstream server did not respond in time
```

[SHOW BROWSER]

Let me demonstrate in Postman. I will make a `GET /api/users/9999` request to a test API. A well-designed API returns `404 Not Found`. I will also demonstrate a `POST` with a missing required field to show `400 Bad Request` vs. `422 Unprocessable Entity`.

---

## Section 5: REST Constraints and Lab Preview [18:30 - 22:00]

[SHOW CODE]

The six architectural constraints that define REST (Fielding, 2000):

1. Client-Server: the client and server are separate concerns. The client does not know about data storage; the server does not know about UI rendering.

2. Stateless: each request contains all information needed to process it. The server holds no session state between requests. Authentication via JWT (Module 13) is the stateless approach.

3. Cacheable: responses must declare whether they are cacheable. `Cache-Control` headers tell clients and CDNs how long to cache responses.

4. Uniform Interface: all resources are accessed through a consistent URL + HTTP method convention. This is what the URL design and method semantics sections implement.

5. Layered System: the client does not know whether it is talking to the origin server or a load balancer, CDN, or cache layer. CloudFront as a CDN in front of API Gateway is an example of this constraint.

6. Code on Demand (optional): servers can send executable code to clients (JavaScript, for example).

In the lab this week you will design the complete URL and method structure for a university course registration API. You will specify each endpoint, its method, its request body format, its success response, and its error responses.

Thank you for watching. See you in Module 07 where we implement these API designs in Node.js and Express.

---

## Additional Resources

- developer.mozilla.org — search "HTTP methods" and "HTTP status codes" for the complete reference
- aws.amazon.com/certification — review API Gateway documentation for REST vs. HTTP API comparison
