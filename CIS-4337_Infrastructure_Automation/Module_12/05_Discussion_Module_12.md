# Discussion Forum: Module 12 — Terraform and CI/CD Pipelines

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Choose one of the three scenarios below. Write an initial post of 175–225 words responding to the scenario prompt. Then write two peer responses of 75–100 words each that add substantive new information, ask a clarifying question, or respectfully challenge an assumption in the original post. Use the 10-point rubric at the bottom of this page to self-assess before submitting.

---

## Scenario A: The Hotfix Dilemma

Your company runs a production Kubernetes cluster provisioned with Terraform. At 2:00 AM, a misconfigured security group blocks traffic to the cluster. The on-call engineer fixes the security group manually through the AWS console to restore service. By morning, `terraform plan` shows drift — the state no longer matches the live configuration.

Discuss: What is the correct process for resolving this drift? Should the team accept the manual change into Terraform state, revert it, or do something else? What policy changes would prevent this situation in the future without sacrificing the ability to respond to incidents quickly?

---

## Scenario B: Security Scanning Gate Design

Your team is adding tfsec and Checkov to an existing GitHub Actions pipeline that already has validate and plan jobs. A senior engineer suggests running both security scanners in the plan job to keep the pipeline simple. A junior engineer argues they should run in a separate, earlier job that blocks plan from starting.

Discuss: Which approach do you recommend and why? Consider pipeline speed, feedback quality, and the blast radius of a missed security finding. What severity threshold would you set for hard-failing the pipeline versus reporting-only?

---

## Scenario C: OIDC Migration

Your organization currently stores AWS IAM access keys as GitHub Actions secrets for all Terraform pipelines. A security audit flags these as long-lived credentials that violate the principle of least privilege and increase breach impact. The security team asks you to migrate all pipelines to OIDC-based authentication within 30 days.

Discuss: What are the technical steps required to complete this migration? What are the risks of the transition period when some pipelines use OIDC and others still use static keys? How would you prioritize which pipelines to migrate first?

---

## Sample Peer Response Starters

- "You raised an important point about drift resolution. I would add that..."
- "I chose the same scenario and reached a different conclusion about the severity threshold because..."
- "Your OIDC migration plan is solid. One risk you may not have considered is..."

---

## Discussion Rubric — 10 Points Total

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario accuracy | 2 | Initial post correctly identifies and addresses the core technical problem in the scenario |
| Depth of analysis | 2 | Post goes beyond surface-level description and explains trade-offs or consequences |
| Use of module concepts | 2 | Post accurately applies vocabulary and concepts from Module 12 (drift, OIDC, security scanning, etc.) |
| Peer response 1 | 2 | First peer response adds new information, asks a clarifying question, or substantively engages with the original post |
| Peer response 2 | 2 | Second peer response meets the same standard as peer response 1 and is not a simple agreement |

---

End of Module 12 Discussion
