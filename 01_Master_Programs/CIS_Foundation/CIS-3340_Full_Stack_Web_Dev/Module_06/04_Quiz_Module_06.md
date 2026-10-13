# Quiz: Module 06 - RESTful API Principles

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which HTTP status code class indicates a server-side processing error occurred?

- A) 2xx
- B) 3xx
- C) 4xx
- D) 5xx

**Correct Answer:** D

**Explanation:** `5xx` status codes indicate that the server encountered an error while attempting to fulfill a valid request. Common examples: `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`.

**Distractor Analysis:**

- Why A is incorrect: `2xx` codes indicate success — the request was received, understood, and processed.
- Why B is incorrect: `3xx` codes indicate redirection — the client must take additional action to complete the request.
- Why C is incorrect: `4xx` codes indicate client-side errors — the request was malformed or unauthorized.
- Why D is correct: `5xx` codes are exclusively server-side failures — the client's request was valid but the server could not fulfill it.

---

## Question 2

Which of the following is the most accurate definition of endpoints in a REST API?

- A) The URL paths combined with HTTP methods that identify where a specific resource or operation is accessible — such as `GET /users` for listing users or `DELETE /users/:id` for removing a specific user.
- B) The encryption keys stored on the server that are used to sign and verify JSON Web Tokens for API authentication.
- C) The database index columns that allow the API server to perform fast lookups when querying records by primary key.
- D) The network firewall rules that restrict which IP addresses are allowed to make requests to the API server.

**Correct Answer:** A

**Explanation:** In REST API design, an endpoint is the combination of an HTTP method and a URL path — together they define a unique, addressable operation on a resource.

**Distractor Analysis:**

- Why A is correct: This accurately describes REST endpoints — method plus URL path defines a specific resource operation.
- Why B is incorrect: This describes JWT signing keys — an authentication concept, not an API endpoint.
- Why C is incorrect: This describes database index columns — a data storage optimization.
- Why D is incorrect: This describes network security group rules — an infrastructure concern.

---

## Question 3

A developer is designing a REST API for a bookstore application. Which URL structure best follows REST naming conventions for retrieving a single book by ID?

- A) `GET /getBook?id=42`
- B) `GET /books/42`
- C) `POST /retrieveBook/42`
- D) `GET /book-fetch/id/42`

**Correct Answer:** B

**Explanation:** REST convention uses plural nouns for resource collections (`/books`) and places the resource identifier in the URL path (`/42`), not in a query string or verb.

**Distractor Analysis:**

- Why A is incorrect: Using `?id=42` as a query parameter is acceptable for filtering collections but unconventional for identifying a specific resource — the ID belongs in the path.
- Why B is correct: `GET /books/42` is the standard REST pattern: GET retrieves, `/books` is the collection noun, and `/42` identifies the specific resource.
- Why C is incorrect: REST endpoints should not contain verbs — the HTTP method communicates the action.
- Why D is incorrect: `/book-fetch/id/42` is non-standard and verbose — it does not follow REST naming conventions.

---

## Question 4

An AWS Lambda function behind an API Gateway endpoint is called three times due to a network retry. The function creates a new database record on each invocation. What REST concept explains why this is a design problem?

- A) The `GET` method was used instead of `POST` — GET requests should be used for all database writes.
- B) `POST` is not idempotent — repeating it creates duplicate resources. The API should use an idempotency key or switch to `PUT` with a client-generated ID to make the operation safe to retry.
- C) Lambda functions automatically deduplicate all requests — the problem must be in the database, not the API design.
- D) HTTP status code `201 Created` should have been `200 OK` — returning the wrong status code causes API Gateway to retry the request automatically.

**Correct Answer:** B

**Explanation:** `POST` creates a new resource each time it is called, making it non-idempotent. Retries produce duplicates unless an idempotency key prevents repeated processing. This is directly relevant to Lambda retry behavior in distributed systems.

**Distractor Analysis:**

- Why A is incorrect: `GET` must never be used for write operations — it is semantically read-only and safe.
- Why B is correct: `POST` non-idempotency is the root cause. Idempotency keys or client-generated IDs with `PUT` are the standard solutions.
- Why C is incorrect: Lambda does not automatically deduplicate requests — the developer must implement idempotency logic.
- Why D is incorrect: `201 Created` is the correct status code for a successful resource creation — it does not trigger automatic retries.

---

## Question 5

A React front-end sends a `DELETE /api/posts/7` request to an Express server. The post is successfully deleted, and the server should return a response with no body. Which HTTP status code is most appropriate?

- A) `200 OK`
- B) `201 Created`
- C) `204 No Content`
- D) `404 Not Found`

**Correct Answer:** C

**Explanation:** `204 No Content` indicates a successful request that intentionally returns no response body — the standard status code for a successful DELETE operation.

**Distractor Analysis:**

- Why A is incorrect: `200 OK` is correct for successful requests that return a response body — for a DELETE with no body, `204` is more semantically precise.
- Why B is incorrect: `201 Created` is used when a new resource has been created — not for deletion.
- Why C is correct: `204 No Content` is the REST convention for successful DELETE operations that do not return a response body.
- Why D is incorrect: `404 Not Found` would indicate the post to be deleted does not exist — not a successful deletion.

---

## Question 6

A developer needs to design an API endpoint that allows a client to update only the email address of an existing user record without replacing the entire user object. Which HTTP method is most appropriate?

- A) POST — because a new email is being "created" for the user.
- B) PUT — because it updates the user resource.
- C) PATCH — because it applies a partial modification to an existing resource.
- D) GET — because the client is requesting the server to "get" the new email.

**Correct Answer:** C

**Explanation:** PATCH applies a partial update to an existing resource — the client sends only the fields to change, not the complete resource representation. PUT replaces the entire resource; sending only the email with PUT would overwrite all other user fields with missing values.

**Distractor Analysis:**

- Why A is incorrect: POST is for creating new resources, not updating existing ones.
- Why B is incorrect: PUT is for full replacement — it requires the complete resource representation and overwrites all fields not included in the body.
- Why C is correct: PATCH sends a partial representation and applies only the specified changes.
- Why D is incorrect: GET is a safe, read-only method — it cannot modify server state.

---

## Question 7

An API returns a `403 Forbidden` status when a logged-in user tries to view another user's private messages. A different endpoint returns `401 Unauthorized` when a user accesses any protected endpoint without a valid token. What is the conceptual difference between these two status codes?

- A) Both `401` and `403` mean the same thing — the client is not allowed to access the resource. The choice between them is a matter of developer preference.
- B) `401` means the request lacks valid authentication credentials (who are you?). `403` means the server knows who the client is but refuses access because the client lacks the required permission (you are not allowed to do this).
- C) `401` is for API endpoints; `403` is for web page routes. They are used in different layers of the application stack.
- D) `401` indicates the JWT token has expired; `403` indicates the JWT token has an invalid signature.

**Correct Answer:** B

**Explanation:** `401 Unauthorized` (despite the misleading name) is about authentication — the request needs valid credentials. `403 Forbidden` is about authorization — the identity is established but the action is not permitted. A user logged in as a student seeing `403` when trying to access admin endpoints is the correct use of `403`.

**Distractor Analysis:**

- Why A is incorrect: These are semantically distinct status codes with different meaning for API clients — using them interchangeably would confuse clients trying to implement proper error handling.
- Why B is correct: `401` = not authenticated; `403` = not authorized. This distinction is directly tested in REST API design interviews and DVA-C02 scenarios.
- Why C is incorrect: Both status codes are used by APIs — they are not layer-specific.
- Why D is incorrect: Both token expiry and invalid signatures typically return `401` (invalid/missing auth) — `403` is about permissions, not token validity.

---

## Question 8

Which of the following URL designs violates REST conventions?

- A) `GET /api/v1/orders/55/items`
- B) `POST /api/v1/orders`
- C) `GET /api/v1/getActiveOrders`
- D) `DELETE /api/v1/orders/55`

**Correct Answer:** C

**Explanation:** `GET /api/v1/getActiveOrders` violates REST conventions by including a verb (`getActiveOrders`) in the URL path. The HTTP method (`GET`) already communicates the action. The correct REST design would be `GET /api/v1/orders?status=active`.

**Distractor Analysis:**

- Why A is incorrect: `GET /orders/55/items` is a valid nested resource pattern — items belonging to order 55.
- Why B is incorrect: `POST /orders` is the correct pattern for creating a new order.
- Why C is correct: The verb `getActiveOrders` belongs in the HTTP method, not the URL. Status filtering belongs in a query parameter.
- Why D is incorrect: `DELETE /orders/55` correctly identifies the method (DELETE), the resource (orders), and the ID (55).

---

## Question 9

A developer is designing an endpoint for creating a user account. Which combination of elements produces the most complete and correct REST response for a successful creation?

- A) Status code `200 OK` with the new user object in the response body.
- B) Status code `201 Created` with the new user object in the response body and a `Location: /api/users/42` header.
- C) Status code `200 OK` with a response body of `{ "success": true }`.
- D) Status code `204 No Content` because the resource was created and no additional data is needed.

**Correct Answer:** B

**Explanation:** `201 Created` is the correct status for a successful resource creation. The `Location` header pointing to the new resource URL is the standard REST pattern that allows the client to immediately know where to find the created resource. Including the new object in the response body saves the client an extra GET request.

**Distractor Analysis:**

- Why A is incorrect: `200 OK` is technically acceptable but `201 Created` is more semantically precise for resource creation. More importantly, the `Location` header is missing.
- Why B is correct: `201` + `Location` header is the canonical REST response for successful POST creation.
- Why C is incorrect: `{ "success": true }` is not RESTful — the response body should represent the created resource, not a generic success flag.
- Why D is incorrect: `204 No Content` is appropriate for DELETE or PUT operations with no response body — not for POST creation where the client needs the new resource's ID.

---

## Question 10

An API Gateway REST API on AWS is configured to forward requests to a Lambda function. A developer tests the endpoint with Postman and receives a `502 Bad Gateway` error. Which of the following is the most likely cause?

- A) The client sent a request with an invalid `Content-Type` header — this causes API Gateway to reject the request before forwarding it.
- B) The Lambda function's response object is missing the required `statusCode` field — API Gateway cannot parse an incomplete Lambda integration response and returns 502.
- C) The API Gateway resource does not have a `GET` method enabled — all methods are disabled by default.
- D) The 502 error indicates a CORS misconfiguration — adding the `Access-Control-Allow-Origin` header to the Lambda response will fix it.

**Correct Answer:** B

**Explanation:** API Gateway Lambda integrations require the Lambda function to return a specific response object format: `{ statusCode, headers, body }`. If the Lambda function returns `undefined`, throws an unhandled exception, or omits the `statusCode` field, API Gateway cannot construct a valid HTTP response and returns `502 Bad Gateway`.

**Distractor Analysis:**

- Why A is incorrect: Invalid `Content-Type` headers would typically produce a `400 Bad Request` from API Gateway before the Lambda function is invoked.
- Why B is correct: The `502` in API Gateway integrations is the standard error for a Lambda response that API Gateway cannot interpret — always the first thing to check in the Lambda return value.
- Why C is incorrect: API Gateway returns `403 Missing Authentication Token` or `405 Method Not Allowed` for unrecognized routes — not `502`.
- Why D is incorrect: CORS misconfiguration causes browser-side blocking with a specific CORS error — not a `502` status code from the server.

---

### Question 11 (5 points)

A developer designs `GET /api/users/42/orders?status=pending`. What does the query parameter `status=pending` represent in REST conventions?

- A) It identifies a specific resource called "pending" within the orders collection.
- B) It is a filter applied to the collection of orders for user 42, returning only orders with a pending status.
- C) It triggers a different handler function than `GET /api/users/42/orders` without the parameter.
- D) It specifies the HTTP response status code the client expects to receive.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Resource identifiers belong in the path segment, not the query string — `status=pending` is a filter, not an identifier.
  - Why B is correct: Query parameters are the REST convention for filtering, sorting, and pagination of collections — they narrow a collection result without identifying a specific resource.
  - Why C is incorrect: REST convention suggests the same handler processes the route regardless of query parameters; the handler reads the parameters to filter results.
  - Why D is incorrect: The expected response status code is a concern of HTTP protocol, not a query parameter in the URL.

---

### Question 12 (5 points)

Which HTTP status code should a server return when a client sends a `POST /api/users` request with a valid JSON body but an email address that already exists in the database?

- A) `400 Bad Request`
- B) `404 Not Found`
- C) `409 Conflict`
- D) `422 Unprocessable Entity`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `400 Bad Request` is appropriate for malformed or missing fields — the email format may be valid; the problem is a state conflict with existing data.
  - Why B is incorrect: `404 Not Found` means a resource does not exist — it is not used for duplicate creation attempts.
  - Why C is correct: `409 Conflict` indicates the request could not be completed because it conflicts with the current state of the resource — a duplicate email is a classic 409 scenario.
  - Why D is incorrect: `422 Unprocessable Entity` is used when the request is syntactically valid but semantically invalid (e.g., `age: -5`) — a duplicate email is a state conflict, not a semantic validation failure.

---

### Question 13 (5 points)

A REST API returns the following response body for every error. Which property is most important for programmatic error handling by client code?

```json
{ "error": "User not found", "code": "USER_NOT_FOUND", "details": [] }
```

- A) `error` — because human-readable strings are easiest for client code to parse.
- B) `code` — because machine-readable error codes allow client code to branch on specific error types without parsing natural-language strings.
- C) `details` — because the details array contains the full error context.
- D) The HTTP status code — the JSON body is informational only; clients should branch on the status code alone.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Human-readable strings change between API versions and cannot be reliably parsed — they are for developer logs, not programmatic branching.
  - Why B is correct: Machine-readable error codes like `USER_NOT_FOUND` are stable identifiers that client code can `switch` on without fragile string matching.
  - Why C is incorrect: `details` supplements the error with field-level context — it is not the primary branching key.
  - Why D is incorrect: HTTP status codes provide coarse-grained categories (404, 409, 422) but do not distinguish between specific error causes within the same status class — error codes fill that gap.

---

### Question 14 (5 points)

A client sends `PUT /api/products/15` with only a `{ "price": 29.99 }` body, intending to update just the price. The server applies the body as a full replacement. What is the result?

- A) The server merges the incoming price with the existing fields — PUT always performs a merge.
- B) All fields not included in the PUT body (name, description, stock, etc.) are set to `null` or removed, because PUT replaces the entire resource representation.
- C) The server returns `422 Unprocessable Entity` because PUT bodies must include all fields.
- D) The server automatically uses PATCH semantics when only one field is provided.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: PUT is defined as a full replacement — it does not merge with existing values.
  - Why B is correct: PUT semantics require the client to send the complete resource representation. Fields omitted from the body are overwritten with missing/null values, destroying existing data.
  - Why C is incorrect: Many APIs accept partial PUT bodies without returning 422 — but the side effect is data loss, not an error response.
  - Why D is incorrect: Servers do not automatically switch between PUT and PATCH based on body completeness — the HTTP method is explicit.

---

### Question 15 (5 points)

What is the purpose of the `Location` header in a `201 Created` response?

- A) It tells the browser to redirect to the new resource URL, loading it automatically.
- B) It provides the URL of the newly created resource so the client can immediately access or reference it without making a separate discovery request.
- C) It specifies the geographic region where the server stored the new resource.
- D) It is required by the HTTP specification for all 2xx responses — omitting it causes clients to retry the request.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A `201 Created` response does not trigger an automatic browser redirect — that behavior is associated with `301`, `302`, and `303` status codes.
  - Why B is correct: The `Location` header in a 201 response gives the client the canonical URL of the created resource, following the REST HATEOAS principle of linking clients to the next logical state.
  - Why C is incorrect: `Location` contains a URL path, not geographic information.
  - Why D is incorrect: `Location` is required for 201 and 3xx responses — it is not required for all 2xx responses.

---

### Question 16 (5 points)

An API endpoint is called `GET /api/v1/users/search?q=alice`. A colleague suggests renaming it to `GET /api/v1/users?name=alice`. Why is the colleague's suggestion more RESTful?

- A) The colleague's URL uses a shorter path, which improves performance.
- B) `search` is a verb — REST URLs should use nouns. Moving the search term to a query parameter on the collection endpoint removes the verb while achieving the same behavior.
- C) `GET /api/v1/users/search` would conflict with `GET /api/v1/users/:id` if a user has the ID "search".
- D) Query parameters are processed faster by API Gateway than URL path segments.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: URL length has negligible performance impact — REST conventions are about semantics, not performance.
  - Why B is correct: REST naming rules forbid verbs in URL paths. "search" is a verb — the correct pattern uses query parameters to filter the collection resource.
  - Why C is incorrect: While `search` could theoretically conflict with a string ID, this is a secondary concern — the primary reason is the REST convention against verbs in paths.
  - Why D is incorrect: API Gateway routing is based on path pattern matching — query parameters and path segments have equivalent processing overhead.

---

### Question 17 (5 points)

Which REST architectural constraint requires that each HTTP request contain all the information necessary to process it, with no server-side session state?

- A) Uniform Interface
- B) Cacheable
- C) Stateless
- D) Layered System

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Uniform Interface requires consistent URL, method, and representation conventions — not statelessness.
  - Why B is incorrect: Cacheable requires responses to declare whether they can be cached — not statelessness.
  - Why C is correct: The Stateless constraint means each request must carry all context the server needs (authentication, parameters, body) — the server stores no per-client session between requests.
  - Why D is incorrect: Layered System allows clients to be unaware of intermediaries like proxies and CDNs — not statelessness.

---

### Question 18 (5 points)

A developer adds a `PATCH /api/v1/users/:id/activate` endpoint to toggle a user's active status. A reviewer flags this as a REST violation. Why?

- A) PATCH is not supported by all HTTP clients and should be avoided.
- B) The endpoint contains a verb (`activate`) in the URL path — REST convention uses nouns; the correct design would be `PATCH /api/v1/users/:id` with `{ "active": true }` in the body.
- C) User activation requires a POST request, not PATCH.
- D) The `:id` path parameter should be a query string parameter for PATCH endpoints.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: PATCH is fully supported by all modern HTTP clients and servers — avoidance is not warranted.
  - Why B is correct: `activate` is a verb. REST encodes actions through HTTP methods — partial state changes belong in the request body sent to the resource's canonical URL.
  - Why C is incorrect: Whether to use POST or PATCH depends on whether you are creating a new resource or updating an existing one — toggling a field on an existing user is a PATCH operation.
  - Why D is incorrect: Path parameters for resource identifiers are the correct REST pattern — moving them to query strings would violate the resource-identification convention.

---

### Question 19 (5 points)

An API Gateway endpoint for `GET /api/products` returns a large JSON array. A developer wants CDN caching to serve this response directly from CloudFront without hitting the Lambda origin on every request. Which response header should the Lambda function include?

- A) `X-Cache-Enable: true`
- B) `Cache-Control: max-age=300`
- C) `ETag: "abc123"`
- D) `Vary: Accept-Encoding`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `X-Cache-Enable` is not a standard HTTP header — CloudFront does not recognize it.
  - Why B is correct: `Cache-Control: max-age=300` instructs CloudFront (and browsers) to cache the response for 300 seconds. CloudFront uses this header to determine how long to serve the cached response before re-validating with the origin.
  - Why C is incorrect: `ETag` is a cache validation header — it enables conditional requests but does not set a cache duration. Without `Cache-Control`, CloudFront will not cache the response.
  - Why D is incorrect: `Vary: Accept-Encoding` instructs caches to store separate versions by encoding type — it does not enable or control caching duration.

---

### Question 20 (5 points)

A developer receives a `429 Too Many Requests` response from an external API. What does this status code indicate and what is the standard client-side remedy?

- A) The client sent a request body that is too large — reduce the payload size.
- B) The client has exceeded the API's rate limit for the time window — implement exponential backoff and retry after the duration specified in the `Retry-After` response header.
- C) The server is temporarily unavailable — this is equivalent to `503 Service Unavailable`.
- D) The client's API key has been revoked due to abuse — contact the API provider to restore access.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Oversized request bodies produce `413 Payload Too Large`, not `429`.
  - Why B is correct: `429 Too Many Requests` specifically indicates rate limiting. The standard remedy is to honor the `Retry-After` header (if present) and implement exponential backoff to reduce request frequency.
  - Why C is incorrect: `503 Service Unavailable` indicates server-side capacity issues — `429` is a client-side rate-limit enforcement.
  - Why D is incorrect: A revoked API key typically produces `401 Unauthorized` or `403 Forbidden` — `429` is specifically about request frequency, not authentication status.
