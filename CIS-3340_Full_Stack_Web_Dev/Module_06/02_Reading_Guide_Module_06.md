# Reading Guide: Module 06 - RESTful API Principles
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 06 - RESTful API Principles**! This module covers the architectural style that underlies nearly every web API — Representational State Transfer (REST). You will learn the six REST constraints, how HTTP verbs map to CRUD operations, how to design clean resource URLs, and how to use HTTP status codes to communicate outcomes. RESTful API design is directly testable on the AWS Certified Developer – Associate exam: API Gateway, Lambda, and DynamoDB are commonly combined to build serverless REST APIs, and the exam tests your understanding of endpoint design, request/response structure, and status code semantics.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Representational State Transfer (REST)**: An architectural style for distributed hypermedia systems defined by Roy Fielding (2000). REST APIs are stateless (each request carries all necessary context), client-server separated, cacheable, and expose resources via uniform interfaces. In practice, a RESTful API communicates over HTTP, identifies resources with URIs, and transfers representations (typically JSON) of resource state.
*   **Endpoints**: The specific URLs (combined with an HTTP method) at which an API makes a resource available. Well-designed REST endpoints use plural nouns for resource collections (`/users`, `/orders`) and path parameters for individual resources (`/users/:id`). Endpoints should not contain verbs — the HTTP method communicates the action.
*   **Resource identifiers**: The URI (Uniform Resource Identifier) path strings that uniquely identify a resource in a REST API. A resource identifier follows a hierarchical pattern: `/users` identifies the users collection, `/users/42` identifies user 42, and `/users/42/orders` identifies the orders belonging to user 42. Path parameters (`:id`) and query strings (`?status=active`) extend the base resource identifier.
*   **HTTP verbs**: The standardized request methods that indicate the intended action in a REST API. `GET` retrieves a resource (safe, idempotent). `POST` creates a new resource (not idempotent). `PUT` replaces an existing resource completely (idempotent). `PATCH` partially updates a resource. `DELETE` removes a resource (idempotent). The DVA-C02 exam tests both the semantic meaning of each verb and their idempotency properties.
*   **Status codes**: Three-digit numeric codes in HTTP responses that communicate the outcome of a request. `2xx` = success (`200 OK`, `201 Created`, `204 No Content`). `3xx` = redirection (`301 Moved Permanently`, `304 Not Modified`). `4xx` = client error (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`). `5xx` = server error (`500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`).

---

### 2. Certification Exam Tips
*   **DVA-C02 Directly Tests REST and API Gateway:** The exam includes scenario questions about designing AWS API Gateway routes — knowing that `GET /items` retrieves a collection, `POST /items` creates one, and `GET /items/{id}` retrieves a single item by ID is required. Know the HTTP verb for each CRUD operation and the corresponding status codes.
*   **Idempotency in AWS Contexts:** The exam tests idempotency in the context of retrying failed API calls. `GET`, `PUT`, and `DELETE` are idempotent (repeating them produces the same result). `POST` is not — retrying a `POST` may create duplicate records. AWS SQS and API Gateway support idempotency keys for this reason.
*   **Study Resource:** The RESTful API Design Guide from Zalando is one of the most comprehensive free references for REST best practices. [Full Stack Open — Part 3: Node.js and Express](https://fullstackopen.com/en/part3) covers building a REST API with Express step-by-step and is directly relevant to this module's lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 3 covering **RESTful API Principles** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3) — this section builds a REST API from scratch and is the primary reading for this module.
*   **Required Video:** Watch the REST API and Node.js section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering endpoint design, HTTP verbs, and status codes with practical examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will apply RESTful API design concepts directly:
*   **Map HTTP endpoints using standard RESTful naming conventions**: Design a routes table for a `products` resource — documenting the HTTP method, URL path, operation, and expected status code for GET (collection), GET (single), POST, PUT, and DELETE.
*   **Test endpoints using mock client payloads**: Use Postman or the `curl` command to send `POST` requests with JSON bodies (`Content-Type: application/json`) and verify that the server returns `201 Created` on success and `400 Bad Request` for missing required fields.
*   **Inspect API headers**: Examine the response headers in Postman or DevTools Network tab — specifically `Content-Type`, `Cache-Control`, and any `Access-Control-Allow-Origin` CORS headers to understand how the server describes its response to clients.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 3 covering **RESTful API Principles** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3).
- [ ] Watch the REST API section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Install [Postman](https://www.postman.com/downloads/) or use the VS Code REST Client extension to practice sending HTTP requests before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
