# Discussion Forum: Module 02 - IAM: Users, Roles, Policies, and Best Practices

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Instructions

Read all three scenarios below and select one to address in your initial post. Your initial post must be 175-225 words, technically precise, and reference specific IAM concepts from the module. Respond to at least two classmates who chose different scenarios from yours.

Initial post due: Wednesday at 11:59 PM
Peer responses due: Sunday at 11:59 PM

---

## Scenario A - Credential Exposure Incident

A startup's backend application is running on Amazon EC2. A developer accidentally committed the application's AWS access keys to a public GitHub repository. Within four hours, an attacker used the keys to create new IAM users, launch EC2 instances in multiple Regions, and attempt to exfiltrate data from S3 buckets. The company is now cleaning up the incident and redesigning their IAM architecture. Describe the root cause of this incident from an IAM design perspective, explain what architectural change would have prevented the credential exposure, and outline at least three specific IAM remediation steps the team should take after the incident. Reference the IAM best practices from this module and explain how each recommendation directly addresses the conditions that made this breach possible.

---

## Scenario B - Over-Permissioned Application Role

A QA engineer is reviewing IAM roles for a new microservices application before it goes to production. She finds that the order-processing service's IAM role has the following policy attached: `Action: "*"` and `Resource: "*"` with Effect Allow. The engineering team defends this by saying "it is just temporary — we will restrict it later." Evaluate the risk of deploying this role to production even temporarily. Explain at least three specific harmful actions an attacker or compromised process could take with this permission set. Then propose a process the team could follow to quickly determine the minimum necessary permissions for the role before deployment — referencing any AWS tools that could assist in building a least-privilege policy.

---

## Scenario C - Multi-Account Access Design

A financial services company is migrating to a multi-account AWS Organizations structure with separate accounts for Production, Development, and Security. The security team in the Security account needs read-only access to CloudTrail logs and Config findings in both the Production and Development accounts. The CISO insists that no long-term credentials should exist in the Security account and that access must require MFA. Design the IAM architecture that satisfies these requirements. Identify all IAM components that must be created (roles, policies, trust relationships), explain which account each component lives in, and describe how the MFA requirement is enforced. Explain why this design is more secure than creating an IAM user in each account for the security team.

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — technical accuracy | 3 | Correctly applies IAM concepts (roles, policies, evaluation logic, best practices); no factual errors |
| Initial post — depth and completeness | 2 | Addresses all parts of the chosen scenario; 175-225 words; uses specific AWS service and IAM term names |
| Initial post — clarity | 1 | Well-organized, professional tone, correct IAM terminology |
| Peer response 1 — substantive engagement | 2 | Adds new technical detail, a different design approach, or a real-world extension; minimum 50 words |
| Peer response 2 — substantive engagement | 2 | Adds new technical detail, a different design approach, or a real-world extension; minimum 50 words |
| **Total** | **10** | |

---

## Professor Nash Note

IAM is where most real-world cloud security failures originate. Posts that engage with the specific IAM mechanisms — policy evaluation logic, role trust relationships, permission scoping — will earn full credit. Responses that only describe the problem without proposing a technically specific solution will not. When responding to peers, engage with the design they proposed: would it work? What edge cases does it miss? What would you do differently?
