# Discussion: Module 15 — Specialized Testing Environments

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Choose ONE of the three scenarios below. Write a primary response of 175–225 words addressing the scenario's questions. Then post substantive peer responses to TWO classmates who chose different scenarios. Peer responses must be 75–100 words and include a specific technical point of agreement, disagreement, or extension.

Initial post due: Thursday 11:59 PM. Peer responses due: Sunday 11:59 PM.

---

## Scenario A: The Cloud Credential Leak

During an authorized AWS penetration test, a tester uses Pacu to enumerate IAM policies and discovers that a developer has committed AWS access keys to a public GitHub repository three months ago. The keys have not been revoked. The tester assumes the role associated with those keys and finds that the role has `*:*` permissions on all S3 buckets, including one containing customer PII for 180,000 users.

Address the following: What is the tester's immediate obligation upon discovering the exposed credentials? Is the use of publicly available credentials to access the S3 bucket within the scope of an authorized AWS penetration test? Rate this finding: what CVSS score and qualitative rating would you assign, and what are the two most critical remediation steps? What does this scenario demonstrate about the relationship between code security and cloud security?

---

## Scenario B: The ICS Safety Dilemma

Your firm has been engaged to assess the OT network of a regional natural gas pipeline operator. The scope authorizes "network security assessment of the SCADA infrastructure." During passive analysis, you discover that the Modbus TCP control network is directly connected to the corporate IT network with no firewall. You can communicate with the PLCs from your standard penetration testing laptop. The client's OT engineer is not available during this phase of testing.

Address the following: Should you send any Modbus commands (read-only or otherwise) to the PLCs without the OT engineer present? What is the difference between passive and active testing in this OT context, and why does the distinction matter more here than in a typical IT assessment? What immediate actions do you take upon this discovery? How would you document the IT/OT flat network finding in your report without specifying how to exploit it in a way that could cause harm?

---

## Scenario C: The Mobile App Overreach

A client engages your firm to test their iOS banking application. The authorized scope is the mobile application and its backend API. During testing, you successfully bypass certificate pinning using Frida. Analyzing the captured traffic, you notice that the API server is responding to requests with database error messages that include partial SQL queries. You also observe that the API endpoint `/internal/admin/users` is reachable from the mobile app and returns a list of all 245,000 customer accounts with balances.

Address the following: Classify each of these two findings (SQL error disclosure and exposed admin endpoint) using OWASP API Top 10 categories and provide a CVSS score for each. For the admin endpoint, you have confirmed it returns customer data using only your own valid user token — no credentials were escalated. Does this constitute unauthorized access requiring immediate client notification? What is the most critical immediate remediation for the admin endpoint finding, and why is rate limiting alone insufficient?

---

## Peer Response Guidance

A strong peer response does more than agree. Consider:

- Offering an additional tool or technique specific to the environment discussed
- Extending the finding's remediation with a cloud/OT/mobile-specific security standard
- Challenging the risk rating with specific CVSS metric arguments
- Connecting the scenario to a documented real-world breach involving the same environment type

---

## Grading Rubric (10 points)

| Criterion | Points |
|-----------|--------|
| Primary response addresses all scenario questions | 3 |
| Demonstrates technical accuracy for the specific environment | 2 |
| Demonstrates understanding of authorization and safety limits | 2 |
| Peer Response 1 — substantive technical contribution | 1.5 |
| Peer Response 2 — substantive technical contribution | 1.5 |
| **Total** | **10** |

**Note:** Responses advocating for active OT exploitation in live operational environments will receive zero points regardless of other content quality.
