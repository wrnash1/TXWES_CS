# Reading Guide: Module 06 - RESTful API Principles

**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers the design principles of RESTful APIs — the architectural style used by virtually all modern web services. You will learn resource naming, HTTP method semantics, status codes, idempotency, the six REST constraints, and API versioning. These principles are directly applied in Module 07 (Express server), Module 08 (routing), and Module 14 (AWS API Gateway deployment).

---

## 1. What is REST?

REST (Representational State Transfer) is an architectural style for distributed hypermedia systems defined by Roy Fielding in 2000. It is not a protocol or a standard — it is a set of constraints that, when applied, produce scalable, stateless, and maintainable web services.

A web API is called "RESTful" when it follows the REST constraints:

- Resources are identified by URLs
- Resources are manipulated through standard HTTP methods
- Representations (typically JSON) transfer state between client and server
- The server is stateless — each request is self-contained

---

## 2. Resource Naming and URL Design

### Resource URL Patterns

| Pattern | Example | Meaning |
|---|---|---|
| Collection | `GET /api/products` | List all products |
| Collection create | `POST /api/products` | Create a new product |
| Single resource | `GET /api/products/42` | Get product with ID 42 |
| Single resource replace | `PUT /api/products/42` | Replace product 42 entirely |
| Single resource update | `PATCH /api/products/42` | Partially update product 42 |
| Single resource delete | `DELETE /api/products/42` | Remove product 42 |
| Nested resource | `GET /api/users/7/orders` | Orders belonging to user 7 |
| Nested single | `GET /api/users/7/orders/3` | Specific order 3 for user 7 |

### URL Design Rules

```text
# GOOD: plural nouns, hierarchical, clean
GET  /api/users
POST /api/users
GET  /api/users/42
GET  /api/users/42/posts

# BAD: verbs in URLs
GET  /api/getUsers
POST /api/createUser
POST /api/deleteUser/42

# BAD: inconsistent plurality
GET  /api/user       (should be /users)
GET  /api/user/42    (should be /users/42)

# Filtering and pagination -- use query parameters, not new paths
GET  /api/products?category=electronics&sort=price&order=asc
GET  /api/posts?page=3&limit=25&author=42
GET  /api/orders?status=pending&from=2025-01-01
```

---

## 3. HTTP Methods Reference

| Method | Semantic | Safe | Idempotent | Request Body | Typical Response |
|---|---|---|---|---|---|
| GET | Read resource | Yes | Yes | No | 200 OK + body |
| POST | Create resource | No | No | Yes | 201 Created + Location header |
| PUT | Replace resource | No | Yes | Yes | 200 OK or 204 No Content |
| PATCH | Partial update | No | No | Yes | 200 OK + updated body |
| DELETE | Remove resource | No | Yes | No | 204 No Content |
| HEAD | Read headers only | Yes | Yes | No | Same as GET, no body |
| OPTIONS | List supported methods | Yes | Yes | No | 200 OK + Allow header |

### Safe and Idempotent Explained

A method is safe if it does not modify server state. A method is idempotent if calling it N times produces the same server state as calling it once.

```text
POST /api/orders -- creates a new order each call -> NOT idempotent
                   calling twice creates two orders

PUT /api/orders/42 -- replaces order 42 with the request body
                     calling twice produces the same final state -> IDEMPOTENT

DELETE /api/users/7 -- removes user 7
                      first call removes the user; subsequent calls find nothing
                      the final state (user 7 is gone) is the same -> IDEMPOTENT

GET /api/users -- reads data without changing it -> SAFE AND IDEMPOTENT
```

---

## 4. HTTP Status Codes Reference

### 2xx — Success

| Code | Text | When to Use |
|---|---|---|
| 200 | OK | Successful GET, PUT, PATCH with response body |
| 201 | Created | Successful POST that created a resource; include `Location` header |
| 204 | No Content | Successful DELETE, PUT, or PATCH with no response body |

### 4xx — Client Errors

| Code | Text | When to Use |
|---|---|---|
| 400 | Bad Request | Malformed JSON, missing required field, invalid type |
| 401 | Unauthorized | No credentials or token is invalid/expired |
| 403 | Forbidden | Authenticated but lacks permission for this action |
| 404 | Not Found | Resource does not exist |
| 405 | Method Not Allowed | HTTP method not supported on this endpoint |
| 409 | Conflict | State conflict — duplicate record, version mismatch |
| 422 | Unprocessable Entity | Request is syntactically valid but semantically invalid |
| 429 | Too Many Requests | Rate limit exceeded |

### 5xx — Server Errors

| Code | Text | When to Use |
|---|---|---|
| 500 | Internal Server Error | Unhandled exception in application code |
| 502 | Bad Gateway | Upstream server (Lambda, EC2) returned invalid response |
| 503 | Service Unavailable | Server overloaded or in maintenance mode |
| 504 | Gateway Timeout | Upstream server did not respond within the timeout |

---

## 5. Request and Response Structure

### Request Headers

```http
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

### Request Body (JSON)

```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "role": "student"
}
```

### Response Headers

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/42
```

### Response Body (JSON)

```json
{
  "id": 42,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "role": "student",
  "createdAt": "2025-09-01T12:00:00Z"
}
```

### Error Response Structure

```json
{
  "error": "Validation failed",
  "code": "INVALID_EMAIL",
  "details": [
    { "field": "email", "message": "Must be a valid email address" }
  ]
}
```

---

## 6. Idempotency Keys for Safe POST Requests

When a POST endpoint must be safe to retry (e.g., payment creation, order submission), use an idempotency key — a client-generated UUID the server uses to detect and deduplicate repeated calls.

```http
POST /api/payments HTTP/1.1
Idempotency-Key: f47ac10b-58cc-4372-a567-0e02b2c3d479
Content-Type: application/json

{
  "amount": 99.99,
  "currency": "USD",
  "customerId": 42
}
```

On the server, the idempotency key is stored with the result. If the same key arrives again, the server returns the stored result without processing the payment twice. Stripe and PayPal both implement this pattern.

---

## 7. API Versioning

APIs change over time. Versioning allows clients to use a stable contract while new versions are developed.

```text
# URL versioning (most common)
GET /api/v1/users
GET /api/v2/users

# Header versioning
GET /api/users
Accept-Version: v2

# Query parameter versioning
GET /api/users?version=2
```

URL versioning is recommended for REST APIs because it is explicit, visible, and easy to cache at the CDN level.

---

## 8. The Six REST Constraints

| Constraint | Description | AWS Example |
|---|---|---|
| Client-Server | UI and data concerns are separated | React front-end separate from Lambda API |
| Stateless | Each request is self-contained; no server sessions | JWT tokens carry auth state in each request |
| Cacheable | Responses declare their cacheability | CloudFront caches GET responses by URL |
| Uniform Interface | Consistent URL + method + representation conventions | All resources follow the same URL naming rules |
| Layered System | Client cannot distinguish server from proxy | CloudFront CDN in front of API Gateway |
| Code on Demand | Server can deliver executable code (optional) | Lambda@Edge modifying responses |

---

## 9. REST API Design Checklist

```text
Resource naming:
  [ ] URLs use plural nouns (not verbs)
  [ ] IDs are in the path, not the query string
  [ ] Nested resources reflect genuine ownership relationships

HTTP methods:
  [ ] GET for reads (safe, idempotent)
  [ ] POST for creation (non-idempotent)
  [ ] PUT for full replacement (idempotent)
  [ ] PATCH for partial updates
  [ ] DELETE for removal (idempotent)

Status codes:
  [ ] 201 Created on POST with Location header
  [ ] 204 No Content on DELETE
  [ ] 400 for malformed requests, 404 for missing resources
  [ ] 401 vs. 403 distinction is correct

Versioning:
  [ ] API has a version prefix in the URL path

Error responses:
  [ ] Consistent JSON error format with error code and details
```

---

## 10. Exam and Interview Tips

1. The HTTP method is the verb. The URL path is the noun. Never put a verb in a REST URL path — `GET /api/getUser` is wrong; `GET /api/users/42` is correct.

2. `201 Created` should include a `Location` header pointing to the newly created resource URL. This is tested directly in REST API design interview questions.

3. `401 Unauthorized` means authentication is missing or invalid. `403 Forbidden` means authenticated but not authorized. Confusing these is a common interview mistake.

4. POST is not idempotent. PUT and DELETE are idempotent. In DVA-C02 exam questions about Lambda retries or SQS message processing, idempotency determines whether duplicate invocations cause data corruption.

5. `204 No Content` is the correct status code for a successful DELETE that returns no body. `200 OK` is also acceptable if the server returns the deleted resource in the body.

6. PATCH is for partial updates (send only the fields to change). PUT is for full replacement (send the complete resource representation).

7. Query parameters are for filtering, pagination, and sorting — not for identifying specific resources. Resource IDs belong in the URL path.

8. Idempotency keys solve the duplicate-request problem for non-idempotent operations. AWS API Gateway supports idempotency keys natively in some SDK integrations.

---

## 11. Study Checklist

- [ ] Know the five primary HTTP methods and their semantics
- [ ] Understand safe vs. idempotent and which methods are which
- [ ] Memorize the key 2xx, 4xx, and 5xx status codes and when to use each
- [ ] Know the difference between 401 and 403
- [ ] Be able to design a complete CRUD endpoint set for any resource
- [ ] Understand URL versioning and when it is needed
- [ ] Know the six REST architectural constraints
- [ ] Understand idempotency keys and when to use them
- [ ] Complete Lab 06 and Discussion 06 before the module deadline

---

## 12. Supplemental Resources

The following free, open-access resources go deeper on Module 06 topics:

**1. MDN Web Docs — HTTP response status codes**
[https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
The complete reference for every HTTP status code grouped by class (1xx–5xx), with descriptions of when each code should be used — essential for implementing correct status codes in Express (Module 07) and API Gateway (Module 14).

**2. REST API Tutorial — RESTful resource naming**
[https://restfulapi.net/resource-naming/](https://restfulapi.net/resource-naming/)
A concise guide covering noun-based URL design, plural vs. singular conventions, nested resource patterns, and the anti-patterns (verbs in URLs, RPC-style endpoints) that are tested in Lab 06 and REST design interviews.

**3. HTTP Methods — Roy Fielding's dissertation (Chapter 5)**
[https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
The original academic source defining the six REST architectural constraints. Reading Chapter 5 provides the authoritative context for the stateless, cacheable, and uniform interface constraints covered in this module.

**4. Stripe API Reference — Idempotency Keys**
[https://stripe.com/docs/api/idempotent_requests](https://stripe.com/docs/api/idempotent_requests)
Stripe's production documentation for idempotency keys — the real-world implementation of the POST idempotency pattern discussed in Section 6 of this reading guide, with code examples in multiple languages.
