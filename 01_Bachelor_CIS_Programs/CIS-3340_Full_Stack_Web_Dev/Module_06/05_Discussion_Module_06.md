# Discussion Forum: Module 06 - RESTful API Principles

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects REST API design principles to real product decisions, security concerns, and AWS architectural patterns. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: API Design Review for a Healthcare Application

A healthcare startup is building a patient portal API. A senior developer reviews the draft API design and flags the following endpoint issues:

```
GET  /api/getPatientRecords?patientId=42
POST /api/updatePatient/42
GET  /api/deleteAppointment?appointmentId=7
POST /api/patient/42/prescriptions/add
```

Address all three of the following in your post:

1. Identify all REST convention violations in the four endpoint designs above. For each violation, name the principle being violated and provide the correct endpoint design.
2. The healthcare application handles Protected Health Information (PHI) under HIPAA. Explain why the stateless constraint of REST (no server-side sessions) is particularly valuable for this application's security architecture. How does JWT-based authentication (which you will implement in Module 13) satisfy the stateless constraint?
3. The API will be deployed to AWS API Gateway. A product manager asks why they cannot just use `GET` requests for all operations — "a GET is simpler, and we can put the action in the query parameter." Provide a technical argument against this proposal that covers at least two distinct reasons (consider HTTP caching, idempotency, and browser history in your answer).

Your initial post should be 175 to 225 words.

---

## Scenario B: Versioning Strategy for a Breaking API Change

A fintech company's public REST API (`/api/v1/`) currently returns transaction amounts as integer cents:

```json
{ "transactionId": "tx_001", "amount": 9999 }
```

A new regulatory requirement mandates returning amounts as decimal dollars with currency code:

```json
{ "transactionId": "tx_001", "amount": "99.99", "currency": "USD" }
```

Hundreds of third-party integrations rely on the current format. Changing the format without versioning would break them all.

Address all three of the following in your post:

1. Explain why this is considered a breaking change. What specific impact does changing `amount` from an integer to a string have on a consumer application that has not been updated?
2. Propose the URL versioning strategy for introducing the new format. Describe what the new endpoint URL looks like, how long you would maintain `/api/v1/` alongside `/api/v2/`, and what information you would include in the API deprecation notice sent to integration partners.
3. AWS API Gateway supports multiple stages (dev, staging, prod) and can be associated with custom domain names. Explain how you would use API Gateway stages and custom domain mappings to serve `/api/v1/` and `/api/v2/` simultaneously from the same domain while routing to different Lambda functions.

Your initial post should be 175 to 225 words.

---

## Scenario C: Idempotency in a Payment Processing System

A payment API receives requests from a mobile app. The mobile network is unreliable — the app has a built-in retry mechanism that resends failed payment requests up to three times. The endpoint is `POST /api/payments`. Without any special handling, network retries cause users to be charged multiple times for the same order.

Address all three of the following in your post:

1. Explain precisely why `POST /api/payments` without idempotency handling creates duplicate charges during network retries. Use the definition of idempotency to frame your explanation. Why is `PUT /api/payments/:paymentId` with a client-generated UUID more idempotent than POST in this context?
2. Describe the idempotency key pattern for making the POST endpoint safe to retry. Explain: how does the client generate and send the key, how does the server use the key to detect duplicates, where the key and result are stored, and for how long the key should be retained.
3. AWS API Gateway supports idempotency keys natively for certain SDK integrations (specifically for DynamoDB TransactWriteItems). Explain how you would implement idempotency in a Lambda + DynamoDB payment API without using a native SDK feature — describe the DynamoDB table design and the Lambda function logic for key checking.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context or a REST design principle that strengthens the answer, or
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
| Initial post uses correct REST and/or AWS terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

API design is the contract you make with every developer who will ever consume your service. A poorly named endpoint, a wrong status code, a missing `Location` header on a 201 response — these are bugs that cascade into bugs in every downstream application. In Module 14 when we deploy to AWS API Gateway, you will discover that API Gateway validates your method-path combinations and enforces many of these conventions automatically. The time you spend now understanding the "why" behind REST design saves you hours of debugging CloudWatch logs later.
