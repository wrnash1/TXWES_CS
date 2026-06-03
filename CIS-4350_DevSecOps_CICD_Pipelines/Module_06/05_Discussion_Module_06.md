# Discussion Forum: Module 06 — Infrastructure as Code Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Overview

Post your original response to one scenario below (minimum 175 words). Then reply substantively to at least two classmates' posts (minimum 75 words each). Original posts due Sunday 11:59 PM; peer replies due Tuesday 11:59 PM.

Professor Nash note: IaC security is where cloud security theory meets cloud engineering practice. The best responses will engage with the real organizational challenges — why engineers use public examples, why scanning is hard to adopt in infrastructure teams, and why drift is so common in organizations that started without IaC discipline. I am looking for practical, realistic analysis.

---

## Scenario 1 — The Legacy Cloud Estate

Your organization has been using AWS for six years. The first four years were "ClickOps" — everything provisioned through the AWS console. Two years ago the team adopted Terraform and began managing new resources as IaC. Approximately 60% of your AWS resources are still managed manually (no Terraform state). A security audit identifies 47 critical misconfigurations across the estate, including 12 S3 buckets with public access and 8 security groups with port 22 open to 0.0.0.0/0.

Design a remediation and modernization plan. How do you prioritize the 47 critical findings — do you start with manual resources or Terraform-managed ones, and why? What is your strategy for bringing the 60% of manually managed resources under IaC without causing outages? How do tfsec and checkov fit into your plan, and when can you start enforcing IaC security gates? What is the risk of using Terraform import on production resources? Reference specific tools and concepts from this module.

### Scenario 1 — Peer Response Prompt

Your classmate proposed a prioritization framework for the 47 findings. Is "fix Terraform-managed first" or "fix manual resources first" the better strategy? What risk does their choice create?

---

## Scenario 2 — The Sentinel Hard Mandatory Debate

Your organization uses Terraform Enterprise. The security team wants to enforce the following as a Hard Mandatory Sentinel policy: all AWS RDS instances must have `deletion_protection = true`. The database team pushes back: "We have dozens of ephemeral testing databases that are intentionally short-lived. If we can't delete them, our testing workflows break." The security team's response: "If it's in Terraform, it's subject to the policy."

Evaluate both positions. Is a blanket Hard Mandatory policy the right tool for this requirement, or should it be Soft Mandatory with an exception workflow? How would you write a Sentinel policy that differentiates between production and non-production RDS instances — for example, using resource tags or workspace names? What is the broader principle about how enforcement level should be calibrated to the risk of the controlled configuration? Reference the three Sentinel enforcement levels from the reading guide and propose a specific policy design that satisfies both teams.

### Scenario 2 — Peer Response Prompt

Your classmate proposed a policy design to satisfy both teams. Does their approach scale to a 50-team enterprise? What happens when a team forgets to tag their test database correctly?

---

## Scenario 3 — The Drift Incident

A security incident is traced to a misconfigured AWS security group that allowed SSH access from a specific external IP — an IP address belonging to a former contractor. Investigation reveals the security group rule was added manually in the AWS console six months ago and persists in production today despite the contractor's access being revoked. The Terraform code for the security group does not include this rule. The rule survived six months because Terraform was run with `terraform apply -refresh=false` in the CI pipeline — disabling the drift detection that would have flagged the discrepancy.

Analyze this incident. What went wrong at each of three levels: process, tooling configuration, and governance? What specific Terraform pipeline configuration would have detected and potentially auto-remediated this drift? Why is `-refresh=false` used in some pipelines (there are legitimate reasons), and how do you get the security benefit of drift detection without the performance cost it adds to large Terraform plans? Reference Terraform plan flags and Terraform Cloud capabilities from the reading guide.

### Scenario 3 — Peer Response Prompt

Your classmate proposed a solution to the `-refresh=false` performance vs. security trade-off. Is their solution practical for a Terraform configuration managing 500+ resources? What additional compensating control would you recommend?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Original post addresses all parts of the chosen scenario | 3 |
| Specific IaC tools, policies, or pipeline configurations cited | 2 |
| Organizational realities and trade-offs acknowledged | 2 |
| Peer reply 1 — substantive challenge or extension | 1.5 |
| Peer reply 2 — substantive challenge or extension | 1.5 |
| Total | 10 |

---

Discussion — Module 06 | CIS-4350 | Texas Wesleyan University | Professor Nash
