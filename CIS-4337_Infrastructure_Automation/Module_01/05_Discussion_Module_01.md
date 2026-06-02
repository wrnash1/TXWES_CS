# CIS-4337 Infrastructure Automation

## Discussion — Module 01: IaC Concepts and Benefits

### Course Alignment: HashiCorp Terraform Associate 003

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two classmates by Sunday at 11:59 PM. All posts must reflect your own analysis and use correct technical terminology from the module readings.

---

## Scenario A: The Overnight Outage

A mid-sized e-commerce company runs its entire web platform on AWS. Late one Friday evening, a senior engineer manually adjusts a security group rule through the AWS console to troubleshoot a customer-reported connectivity issue. The change resolves the issue temporarily, but the engineer forgets to update the Terraform configuration or document the change. Two weeks later, the on-call engineer runs a routine `terraform apply` as part of a scheduled maintenance window. The security group rule is reverted to the state declared in HCL — and the connectivity issue returns. The incident takes four hours to diagnose because no one knows a drift event occurred.

For your initial post (175–225 words), address all three of the following points:

1. Identify the specific IaC concept that failed in this scenario and explain why the incident occurred in technical terms.
2. Propose two concrete practices the team should adopt to prevent this class of incident in the future. Be specific about tooling and process.
3. Explain how the benefits of IaC that we discussed in Module 01 apply to this scenario — specifically, which benefits were absent and what their presence would have prevented.

---

## Scenario B: The Multi-Environment Problem

A startup is preparing to launch a SaaS application. The development team has been provisioning AWS resources manually through the console for the past six months. As the launch date approaches, the engineering manager realizes that the development, staging, and production environments have drifted significantly from each other: different instance types, different security group configurations, different S3 bucket policies. A production deployment fails because staging was missing a required IAM role that was added to development but never replicated to staging.

For your initial post (175–225 words), address all three of the following points:

1. Explain how IaC would have prevented this multi-environment drift from occurring in the first place.
2. Describe how Terraform variables and modules (introduced briefly in Module 01 and covered in depth in later modules) could be used to maintain consistent environments.
3. Identify the specific IaC benefit that is most relevant here and explain why it is the most important in this context.

---

## Scenario C: The New Team Member

A cloud infrastructure team has relied on a single senior engineer, who is the only person who knows how all of the company's AWS infrastructure was provisioned and why specific configuration choices were made. That engineer accepts a position at another company and leaves within two weeks. The remaining team must now maintain, scale, and troubleshoot hundreds of EC2 instances, RDS databases, VPCs, and load balancers — none of which was ever defined in code.

For your initial post (175–225 words), address all three of the following points:

1. Identify which IaC benefits are most directly relevant to the knowledge-transfer problem described in this scenario.
2. Propose a phased plan for adopting Terraform in this environment. Your plan should account for the risk of importing existing resources into Terraform management without disrupting production.
3. Reflect on how this scenario illustrates the true cost of ClickOps at organizational scale.

---

## Peer Response Guidelines

When responding to classmates, do not simply agree with their post. Add technical value in at least one of the following ways:

- Identify a risk or edge case they did not address.
- Offer an alternative technical approach with a brief justification.
- Connect their scenario to a concept from the reading guide that they did not mention.
- Ask a specific follow-up question that would deepen the discussion.

Each peer response must be at least 75 words and contain at least one specific technical reference to Terraform concepts from Module 01.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all three prompt points with technical accuracy. Uses correct terminology (drift, declarative, state, idempotency, etc.). Meets the 175–225 word count. Demonstrates understanding beyond surface-level definitions.
- 3–4 pts: Addresses most prompt points but lacks technical depth or precision in at least one area. Minor terminology errors.
- 1–2 pts: Addresses fewer than two prompt points or contains significant technical inaccuracies.
- 0 pts: No initial post submitted.

Peer Responses — 4 Points:

- 4 pts: Responds to at least two classmates with substantive technical contributions. Each response is at least 75 words and references specific Module 01 concepts.
- 2 pts: Responds to only one classmate, or both responses are superficial without technical substance.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Your discussion grade reflects the quality of your technical reasoning, not just your word count. A concise, precise post that correctly applies Terraform concepts will score higher than a long post that restates definitions without applying them to the scenario. Write as a practitioner explaining a real problem to a colleague.

---

Module 01 Discussion — CIS-4337 Infrastructure Automation — Texas Wesleyan University
