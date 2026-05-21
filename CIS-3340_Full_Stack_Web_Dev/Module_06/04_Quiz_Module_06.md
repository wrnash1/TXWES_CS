# Quiz: Module 06 - RESTful API Principles
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which HTTP status code class indicates a server-side processing error occurred?
*   A) 2xx
*   B) 3xx
*   C) 4xx
*   D) 5xx
*   **Correct Answer:** D) `5xx` status codes (e.g., `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`) indicate that the server encountered an error while attempting to fulfill a valid request.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `2xx` codes indicate success — the request was received, understood, and processed (e.g., `200 OK`, `201 Created`).
    *   *Why B is incorrect:* `3xx` codes indicate redirection — the client must take additional action to complete the request (e.g., `301 Moved Permanently`).
    *   *Why C is incorrect:* `4xx` codes indicate client-side errors — the request was malformed or unauthorized (e.g., `404 Not Found`, `401 Unauthorized`).
    *   *Why D is correct:* `5xx` codes are exclusively server-side failures — the client's request was valid but the server could not fulfill it.

---

**Question 2**
Which of the following is the most accurate definition of **endpoints** in a REST API?
*   A) The URL paths combined with HTTP methods that identify where a specific resource or operation is accessible — such as `GET /users` for listing users or `DELETE /users/:id` for removing a specific user.
*   B) The encryption keys stored on the server that are used to sign and verify JSON Web Tokens for API authentication.
*   C) The database index columns that allow the API server to perform fast lookups when querying records by primary key.
*   D) The network firewall rules that restrict which IP addresses are allowed to make requests to the API server.
*   **Correct Answer:** A) The URL paths combined with HTTP methods that identify where a specific resource or operation is accessible — such as `GET /users` for listing users or `DELETE /users/:id` for removing a specific user.
*   **Distractor Analysis:**
    *   *Why A is correct:* In REST API design, an endpoint is the combination of an HTTP method and a URL path — together they define a unique, addressable operation on a resource.
    *   *Why B is incorrect:* This describes JWT signing keys — an authentication concept, not an API endpoint.
    *   *Why C is incorrect:* This describes database index columns — a data storage optimization, not an API endpoint.
    *   *Why D is incorrect:* This describes network security group or firewall rules — an infrastructure concern, not an API endpoint.

---

**Question 3**
A developer is designing a REST API for a bookstore application. Which URL structure best follows REST naming conventions for retrieving a single book by ID?
*   A) `GET /getBook?id=42`
*   B) `GET /books/42`
*   C) `POST /retrieveBook/42`
*   D) `GET /book-fetch/id/42`
*   **Correct Answer:** B) `GET /books/42` — REST convention uses plural nouns for resource collections (`/books`) and places the resource identifier in the URL path (`/42`), not in a query string or verb.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using `?id=42` as a query parameter is acceptable for filtering collections but unconventional for identifying a specific resource — the ID belongs in the path.
    *   *Why B is correct:* `GET /books/42` is the standard REST pattern: `GET` retrieves, `/books` is the collection noun, and `/42` identifies the specific resource.
    *   *Why C is incorrect:* REST endpoints should not contain verbs (`retrieveBook`) — the HTTP method (`GET`) communicates the action.
    *   *Why D is incorrect:* `/book-fetch/id/42` is a non-standard, verbose path that does not follow REST naming conventions.

---

**Question 4**
An AWS Lambda function behind an API Gateway endpoint is called three times due to a network retry. The function creates a new database record on each invocation. What REST/HTTP concept explains why this is a design problem?
*   A) The `GET` method was used instead of `POST` — GET requests should be used for all database writes.
*   B) `POST` is not idempotent — repeating it creates duplicate resources. The API should use an idempotency key or switch to `PUT` with a client-generated ID to make the operation safe to retry.
*   C) Lambda functions automatically deduplicate all requests — the problem must be in the database, not the API design.
*   D) HTTP status code `201 Created` should have been `200 OK` — returning the wrong status code causes API Gateway to retry the request automatically.
*   **Correct Answer:** B) `POST` is not idempotent — repeating it creates duplicate resources. The API should use an idempotency key or switch to `PUT` with a client-generated ID to make the operation safe to retry.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `GET` must never be used for write operations — it is semantically read-only and safe.
    *   *Why B is correct:* `POST` creates a new resource each time it is called — making it non-idempotent. Retries produce duplicates unless an idempotency key prevents repeated processing.
    *   *Why C is incorrect:* Lambda does not automatically deduplicate requests — the developer must implement idempotency logic.
    *   *Why D is incorrect:* `201 Created` is the correct status code for a successful resource creation — it does not trigger automatic retries.

---

**Question 5**
A React front-end sends a `DELETE /api/posts/7` request to an Express server. The post is successfully deleted, and the server should return a response with no body. Which HTTP status code is most appropriate?
*   A) `200 OK`
*   B) `201 Created`
*   C) `204 No Content`
*   D) `404 Not Found`
*   **Correct Answer:** C) `204 No Content` indicates a successful request that intentionally returns no response body — the standard status code for a successful `DELETE` operation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `200 OK` is correct for successful requests that return a response body — for a DELETE with no body, `204` is more precise.
    *   *Why B is incorrect:* `201 Created` is used when a new resource has been created — not for deletion.
    *   *Why C is correct:* `204 No Content` is the REST convention for successful DELETE (and some PUT/PATCH) operations that do not return a response body.
    *   *Why D is incorrect:* `404 Not Found` would indicate the post to be deleted does not exist — not a successful deletion.
