# Discussion Forum: Module 09 — Web Application Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Professor Nash's Note on Professional Ethics

Web application penetration testing is the area where I see the most well-intentioned mistakes from new security professionals. The tools are easy to use, the vulnerabilities are often obvious, and it is tempting to go further than the scope allows — just to see what is there. That impulse must be disciplined.

Every test has a boundary. A vulnerability in the application's payment processor may be out of scope if the payment processor is a third-party vendor. An IDOR that exposes other users' data must be documented and immediately reported — not explored to see how much data can be accessed. An XSS that could steal admin cookies must be demonstrated with a safe, non-destructive payload, not actually used to take over accounts.

The discussions below focus on the judgment calls that distinguish a professional web application tester from someone who simply runs Burp Suite without thinking. Bring your full reasoning to these scenarios — technical, ethical, and legal.

---

## Discussion Scenario 1 — The Scope Boundary

A penetration tester is engaged to assess a retail company's customer-facing e-commerce web application. The scope document lists `shop.retailer.com` as the only authorized target. During testing, the tester discovers an IDOR vulnerability in the order history API:

```text
GET /api/orders?customer_id=10045
```

Changing `customer_id` to `10046` returns a different customer's full order history, shipping address, and the last four digits of their payment card. The tester confirms the vulnerability with a single request.

The tester notices that the response also includes an internal service URL pointing to `internal-api.retailer.com/admin/orders`. This domain is not in scope.

**Discussion Prompt:**

In 175–225 words, address the following:

- What should the tester do with the IDOR finding — how is it documented and reported without excessively accessing other customers' data?
- The internal API URL surfaced as a side effect of authorized testing. Does the tester have authorization to probe `internal-api.retailer.com`? What is the professional response?
- What does this scenario illustrate about the tension between thorough testing and scope discipline?
- What remediation should be recommended for the IDOR vulnerability?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 2 — XSS in a Healthcare Portal

A penetration tester is assessing a patient portal for a healthcare organization. The scope explicitly includes the patient-facing web application and identifies stored XSS as a test category. During testing, the tester discovers a stored XSS vulnerability in the "patient notes" field — a field that physicians enter clinical notes into, which is then displayed in the patient's portal view.

The tester confirms the vulnerability by injecting:

```html
<script>alert(document.domain)</script>
```

The alert fires, confirming stored XSS. The tester then considers whether to demonstrate session cookie theft by submitting a cookie-stealing payload that would fire for any physician who views a patient note containing the XSS.

**Discussion Prompt:**

In 175–225 words, address the following:

- Should the tester proceed with a cookie-stealing payload demonstration against real physician sessions, or is the `alert()` proof sufficient? Justify your reasoning.
- What are the HIPAA and patient safety implications if this XSS were exploited by a real attacker? Who would be harmed and how?
- How should the tester demonstrate maximum impact in the report without actually stealing any real user's session token?
- What is the OWASP Top 10 classification for this finding, and what does the remediation look like?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 3 — The API Discovery Problem

A security team at a financial technology company conducts an internal penetration test of their new mobile banking API. During the test, the tester uses Burp Suite to proxy all mobile app traffic and discovers that the API has numerous undocumented endpoints not listed in the official API specification provided by the development team. One of these endpoints, `/api/internal/admin/users`, returns a complete list of all user accounts including email addresses, phone numbers, and account balances when called with a standard user authentication token.

The development team's response when notified: "That endpoint is internal — it's not supposed to be accessible from outside. It must be a deployment mistake."

**Discussion Prompt:**

In 175–225 words, address the following:

- Does the fact that the endpoint was "not supposed to be accessible" mitigate the security risk? Explain using OWASP API Security concepts.
- What does this scenario illustrate about the gap between what developers build and what gets deployed — and how penetration testing bridges that gap?
- What is the appropriate CVSS severity for an unauthenticated (or low-privileged) endpoint that returns full user account data, and what factors drive that score?
- Beyond fixing this specific endpoint, what systemic process changes should the organization implement to prevent similar exposures in future deployments?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|---------|
| Initial Post — Technical Accuracy | 3 | Demonstrates accurate understanding of web application security concepts from Module 09 |
| Initial Post — Ethical Reasoning | 2 | Addresses scope, authorization, data protection, and professional obligations with specificity |
| Initial Post — Word Count and Format | 1 | 175–225 words, organized response, professional tone |
| Peer Response 1 | 2 | Minimum 75 words, adds substantive analysis or challenges a point with reasoning |
| Peer Response 2 | 2 | Minimum 75 words, introduces a new consideration or connects to course concepts |

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
