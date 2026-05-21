# Reading Guide: Module 13 - Web Security (JWT & CORS)
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 13 - Web Security (JWT & CORS)**! This module covers two critical security topics for full-stack web applications: JSON Web Tokens (JWT) for stateless authentication, and Cross-Origin Resource Sharing (CORS) for safely sharing resources across different origins. You will also learn password hashing with bcrypt — the industry standard for storing user credentials. These concepts are heavily tested on the AWS Certified Developer – Associate exam in the context of API Gateway authorizers, Cognito authentication, and secure API design.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Cross-Origin Resource Sharing (CORS)**: A browser security mechanism that enforces the Same-Origin Policy — blocking JavaScript in a page loaded from one origin (`scheme + host + port`) from reading responses from a different origin unless the response includes explicit permission headers (`Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`). CORS is enforced by the browser, not the server — the server always receives the request, but the browser blocks the response from reaching JavaScript if CORS headers are missing or insufficient.
*   **JSON Web Tokens (JWT)**: A compact, URL-safe token format used for stateless authentication and authorization. A JWT consists of three Base64URL-encoded parts separated by dots: a Header (algorithm and token type), a Payload (claims such as `sub`, `iat`, `exp`, and custom user data), and a Signature (HMAC-SHA256 or RSA signature computed over the header + payload using a secret key). The server verifies the signature on every request — no session storage is needed.
*   **Signing keys**: The secret strings or RSA key pairs used to generate and verify JWT signatures. For symmetric signing (HMAC-SHA256 / `HS256`), the same secret is used to sign and verify. For asymmetric signing (RSA / `RS256`), a private key signs the token and a public key verifies it — enabling third parties to verify tokens without access to the signing secret. Signing keys must be stored securely — never hard-code them in source code; use environment variables or AWS Secrets Manager.
*   **Payload structures**: The decoded middle section of a JWT containing the token's claims — standardized claims include `iss` (issuer), `sub` (subject/user ID), `aud` (audience), `exp` (expiration timestamp), and `iat` (issued-at timestamp). Custom claims carry application-specific data (e.g., `role: 'admin'`). Payloads are Base64URL-encoded but not encrypted — sensitive data must not be stored in the payload without encryption.
*   **bcrypt**: A password-hashing function that incorporates a salt (random data mixed with the password before hashing) and an adjustable cost factor (work factor) that controls how computationally expensive the hash is to compute. bcrypt's design intentionally slows brute-force attacks — increasing the cost factor by 1 doubles the computation time. The Node.js `bcrypt` or `bcryptjs` package provides `bcrypt.hash(password, saltRounds)` for hashing and `bcrypt.compare(password, hash)` for verification.

---

### 2. Certification Exam Tips
*   **DVA-C02 Tests Amazon Cognito and JWT:** The exam heavily tests Amazon Cognito — AWS's managed user authentication service that issues JWTs (ID tokens, access tokens, refresh tokens). Know the difference between Cognito User Pools (user directory + JWT issuance) and Identity Pools (temporary AWS credentials). API Gateway can use Cognito User Pool authorizers to validate JWTs automatically — no custom Lambda authorizer needed.
*   **CORS on API Gateway:** The exam presents scenarios where a React app cannot reach an API Gateway endpoint due to CORS. API Gateway has a dedicated CORS configuration panel where you set allowed origins, methods, and headers. For Lambda Proxy integrations, the Lambda function itself must return the CORS headers in its response — API Gateway does not add them automatically in this integration type.
*   **Study Resource:** JWT.io provides an interactive decoder and library directory for JWTs. [JWT.io — Introduction](https://jwt.io/introduction) explains the three-part structure with a live decoder. For CORS, [MDN — CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is the most complete browser-side explanation.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 4 covering **Authentication and JWT** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part4) — this section implements bcrypt password hashing and JWT authentication in the Express REST API built in earlier modules.
*   **Required Video:** Watch the web security and JWT section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering token-based authentication flow, bcrypt hashing, and CORS configuration.

---

### Lab & Command Integration
In this week's hands-on lab, you will implement JWT authentication and CORS in an Express API:
*   **Configure CORS origins in Express app**: Install the `cors` package (`npm install cors`), configure it with an options object restricting the allowed origin to your React dev server (`origin: 'http://localhost:3000'`), and verify that Postman requests from non-allowed origins are rejected with a CORS error.
*   **Hash passwords using bcrypt before saving**: Install `bcryptjs` (`npm install bcryptjs`), hash a test password with `bcrypt.hash('password123', 10)`, and verify the result with `bcrypt.compare('password123', hash)` — confirming that the original plaintext is never stored.
*   **Generate and verify signed JWT payloads**: Install `jsonwebtoken` (`npm install jsonwebtoken`), generate a token with `jwt.sign({ userId: 1, role: 'user' }, process.env.JWT_SECRET, { expiresIn: '1h' })`, and verify it with `jwt.verify(token, process.env.JWT_SECRET)` — inspecting the decoded payload claims.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 4 covering **Authentication and JWT** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part4).
- [ ] Watch the web security section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Use [JWT.io](https://jwt.io) to decode a sample JWT and inspect its header, payload, and signature sections before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
