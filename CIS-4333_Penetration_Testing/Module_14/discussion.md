# Discussion: Module 14 — Legal, Compliance, and Contractual Considerations

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Choose ONE of the three scenarios below. Write a primary response of 175–225 words addressing the scenario's questions. Then post substantive peer responses to TWO classmates who chose different scenarios. Peer responses must be 75–100 words and include a specific technical point of agreement, disagreement, or extension.

Initial post due: Thursday 11:59 PM. Peer responses due: Sunday 11:59 PM.

---

## Scenario A: The Scope Creep Temptation

A penetration tester is conducting an authorized external assessment. The authorized scope is 10.10.0.0/24. During reconnaissance, the tester notices that the client's website references an administrative backend at `admin.internal.client.com`, which resolves to 10.20.0.5 — outside the authorized scope. A quick check reveals the admin page has no authentication required and the interface is fully functional.

Address the following: Should the tester access the admin interface? What is the precise legal risk under the CFAA if they do? What is the correct professional action? How should this finding be documented and communicated to the client? Draft a one-paragraph email to the client's CISO explaining the discovery and requesting guidance.

---

## Scenario B: The Retroactive Authorization Request

A junior tester on your firm's team got excited during an engagement and tested several additional systems that were clearly outside the authorized scope. No systems were harmed and the tester found a critical vulnerability on one out-of-scope system. The client is now asking the firm to include the out-of-scope finding in the report and is willing to provide retroactive authorization.

Address the following: Does retroactive authorization resolve the legal issue created by the unauthorized testing? What is your firm's liability exposure from this incident, and what insurance coverage might apply? How should the out-of-scope finding be handled in the report — include it, exclude it, or note it in a specific way? What internal process change would prevent this situation in future engagements?

---

## Scenario C: The Bug Bounty Gray Zone

A security researcher participates in a company's public bug bounty program. The policy says "test *.app.example.com." While testing, the researcher discovers that a request to `beta.app.example.com` (in scope) causes the server to make outbound requests to internal infrastructure — a SSRF vulnerability. By manipulating the URL, the researcher can reach `admin.internal.example.com` — clearly not in the public scope. The internal admin panel has no authentication and contains user account data for 2 million customers.

Address the following: Is accessing admin.internal.example.com within the researcher's bug bounty authorization? What is the safe harbor status for this access? What is the correct action once the researcher can see that internal admin data is accessible? How should the vulnerability be reported — through the bug bounty program, through a separate security contact, or through CISA? What does this scenario illustrate about the limits of bug bounty scope definitions?

---

## Peer Response Guidance

A strong peer response does more than agree. Consider:

- Citing specific CFAA case law that bears on the scenario
- Offering an alternative interpretation of the authorization question
- Extending the analysis to the client's potential obligations (breach notification, regulatory disclosure)
- Challenging the proposed documentation approach with a specific professional standard

---

## Grading Rubric (10 points)

| Criterion | Points |
|-----------|--------|
| Primary response addresses all scenario questions | 3 |
| Demonstrates accurate understanding of CFAA authorization principles | 2 |
| Demonstrates professional judgment in handling authorization issues | 2 |
| Peer Response 1 — substantive legal or professional contribution | 1.5 |
| Peer Response 2 — substantive legal or professional contribution | 1.5 |
| **Total** | **10** |

**Note:** Responses that justify unauthorized access on any basis — scope ambiguity, client benefit, "just a test" — will receive zero points for the CFAA accuracy criterion.
