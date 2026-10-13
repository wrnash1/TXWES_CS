# Discussion Forum: Module 13 — Web Security: JWT Authentication & CORS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects JWT authentication and CORS to real security decisions: how tokens are structured and trusted, where authentication state lives in a full-stack application, and how the AWS Lambda Authorizer pattern applies these concepts at scale. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: JWT Payload Design and Token Security

A team is building a healthcare appointment scheduling API. A developer proposes the following JWT payload:

```json
{
  "userId": 42,
  "email": "patient@example.com",
  "role": "patient",
  "ssn": "123-45-6789",
  "dateOfBirth": "1985-03-14",
  "exp": 1699900000
}
```

A security reviewer flags the design as dangerous.

Address all three of the following in your post:

1. Explain exactly why including `ssn` and `dateOfBirth` in the JWT payload is a security vulnerability. What is the encoding used in the JWT payload, and what can anyone who intercepts the token do with that data? How does this differ from a token stored in a database session?
2. Redesign the JWT payload to contain only what is necessary for authorization decisions, and explain what data should remain exclusively in the database and be fetched on demand when needed.
3. The team also debates token expiration. Developer A sets `expiresIn: '30d'` for convenience — users stay logged in for a month. Developer B argues for `expiresIn: '15m'` with a refresh token mechanism. Evaluate both approaches: what is the security consequence of a long-lived token if it is stolen, and what problem does the refresh token pattern solve?

Your initial post should be 175 to 225 words.

---

## Scenario B: Authentication Middleware Ordering and 401 vs 403

A developer builds an Express API for a student records system. The API has three categories of endpoints: public endpoints (course catalog), endpoints requiring a valid student login (view own grades), and endpoints requiring admin role (view all students' grades, modify records). The developer applies `authenticate` middleware globally with `app.use(authenticate)` at the top of `index.js`.

Address all three of the following in your post:

1. Identify the immediate consequence of applying `authenticate` globally before all routes. Which specific endpoint fails first, and why does it fail in a way that makes the problem difficult to diagnose?
2. Propose a route organization strategy that correctly applies authentication only to the routes that need it. Your answer should describe at least two different Express patterns for scoping middleware — one using router-level middleware and one using route-level middleware on individual routes.
3. The admin endpoints return `403 Forbidden` when a valid student token is used (the user is authenticated but not an admin). A developer argues that `401` should be returned instead because "the user is not authorized." Explain the precise distinction between `401 Unauthorized` and `403 Forbidden`, using the student/admin scenario to illustrate when each is the correct response.

Your initial post should be 175 to 225 words.

---

## Scenario C: CORS, Preflight, and AWS Lambda Authorizer

A React SPA hosted on CloudFront (`https://app.example.com`) calls an API Gateway endpoint (`https://api.example.com`). The API is backed by Lambda and protected by a Lambda Authorizer that verifies a JWT. A developer reports that all API calls fail after adding the `Authorization` header to the fetch requests — the browser shows a CORS preflight failure.

Address all three of the following in your post:

1. Explain why adding the `Authorization` header triggered a CORS preflight failure that did not exist before. What condition causes the browser to send an `OPTIONS` request, and what must both the Lambda Authorizer response and the API Gateway CORS configuration include for the preflight to succeed?
2. The Lambda Authorizer verifies the JWT and returns an IAM policy document. Describe the structure of this policy document — what does an `Allow` response look like, and what happens to the original API request after API Gateway receives an `Allow` policy? Also explain what API Gateway's authorizer caching does and why it matters for performance.
3. After fixing the preflight, a logged-in user's token expires mid-session. The Lambda Authorizer returns a `Deny` policy. The React app receives a `403` from API Gateway. Describe how the React application should handle this response — specifically, what state should be cleared, what the user should see, and how this differs from a `401` response from a non-AWS Express API.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context or a security principle that strengthens the answer, or
- Present an alternative approach with trade-off analysis

---

## Due Dates

- Initial post: Wednesday by 11:59 PM
- Peer responses (at least two): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Initial post uses correct JWT, Express, CORS, and/or AWS terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

The distinction between 401 and 403 seems trivial until you are debugging a production system at 2 AM and every endpoint is returning 403 even though no user is logged in. If your middleware returns 403 for a missing token instead of 401, every client — mobile app, web app, automated test — has to guess whether the problem is "no token" or "wrong permissions." 401 means "please authenticate." 403 means "you are authenticated but not allowed here." Get those right and your API tells the truth about what went wrong.
