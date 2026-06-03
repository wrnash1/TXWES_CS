# Discussion Forum: Module 14 — Multi-Cloud Provisioning with Terraform

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Choose one of the three scenarios below. Write an initial post of 175–225 words responding to the scenario prompt. Then write two peer responses of 75–100 words each that add substantive new information, ask a clarifying question, or respectfully challenge an assumption in the original post. Use the 10-point rubric at the bottom of this page to self-assess before submitting.

---

## Scenario A: The Acquisition Integration

Your company has acquired a startup that runs entirely on GCP. Your company's existing infrastructure runs on AWS. The CTO wants both environments integrated so engineers can deploy applications to either cloud from a single Terraform configuration. You have 60 days to propose an integration architecture.

Discuss: What are the technical steps required to configure Terraform for cross-cloud integration? What authentication challenges arise when a single CI pipeline runner needs to provision in both AWS and GCP? What would the provider configuration look like, and what constraints would you place on the provider versions?

---

## Scenario B: Provider Version Drift Incident

Your team has 8 engineers. Three months ago, no one committed the `.terraform.lock.hcl` file to the repository. When a new engineer joined and ran `terraform init`, they got AWS provider version 5.15.0 while the rest of the team is on 5.8.2. The new engineer's `terraform plan` output shows resource changes that no one else can reproduce. This causes confusion in code review and nearly results in an unintended apply.

Discuss: How does this situation arise mechanically? What is the correct remediation? What processes or repository rules would prevent this from happening again? What are the risks of running `terraform init -upgrade` to align everyone to the latest version?

---

## Scenario C: Multi-Cloud Cost Analysis

Your company's architecture team is evaluating whether to implement active-active multi-cloud for a high-traffic application that processes 10 TB of data per day. The primary data flows between an AWS compute tier and a GCP analytics tier. The team is excited about the resilience benefits but has not fully modeled the costs.

Discuss: What cost factors must be included in a multi-cloud cost analysis that would not exist in a single-cloud architecture? How would you quantify egress costs at 10 TB/day? What architectural changes could reduce inter-cloud data transfer while preserving the analytics capability in GCP?

---

## Sample Peer Response Starters

- "Your acquisition integration plan is practical. One additional complexity you may face is..."
- "I agree the lock file incident is a process failure. I would add that the risk of `-upgrade` is..."
- "Your egress cost estimate is on target. Another cost factor that is often overlooked is..."

---

## Discussion Rubric — 10 Points Total

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario accuracy | 2 | Initial post correctly identifies and addresses the core technical problem in the scenario |
| Depth of analysis | 2 | Post goes beyond surface-level description and explains trade-offs or consequences |
| Use of module concepts | 2 | Post accurately applies vocabulary and concepts from Module 14 (provider aliasing, lock file, version constraints, multi-cloud patterns, etc.) |
| Peer response 1 | 2 | First peer response adds new information, asks a clarifying question, or substantively engages with the original post |
| Peer response 2 | 2 | Second peer response meets the same standard and is not a simple agreement |

---

End of Module 14 Discussion
