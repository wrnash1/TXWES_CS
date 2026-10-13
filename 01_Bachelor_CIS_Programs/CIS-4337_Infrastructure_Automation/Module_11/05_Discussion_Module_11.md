# Discussion: Module 11 — Terraform Cloud and Remote Backends

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be **175–225 words**. Reply to **two classmates** with substantive feedback (minimum 75 words each). All posts are due by Sunday at 11:59 PM CT.

---

## Scenario A: Sentinel Policy Design

Your organization has just purchased Terraform Cloud with the Team tier, giving you access to Sentinel policies. The CTO wants you to design a Sentinel policy framework for three goals: (1) all resources must have `Owner`, `Environment`, and `CostCenter` tags; (2) no S3 buckets should be publicly accessible; (3) EC2 instances in dev environments must use only t3.micro or t3.small.

Design the policy set architecture. How many policies do you create? How do you organize them into policy sets? What enforcement level is appropriate for each policy, and why? How do you roll out the policies to an organization that has existing non-compliant infrastructure — do you start with hard mandatory, or do you phase in enforcement? What process do you put in place for handling legitimate exceptions to policy (e.g., a specific team that needs larger instances for a valid reason)?

---

## Scenario B: VCS Workflow Design

Your platform team is migrating 15 Terraform configurations to Terraform Cloud with VCS integration. The organization uses GitHub. Each configuration manages infrastructure for a different microservice team.

Design the end-to-end VCS workflow. What branching strategy do you recommend for infrastructure changes? How do speculative plans fit into the PR review process? Who should have permission to merge to the production branch? How do you handle the scenario where a plan succeeds on a feature branch but fails when it hits the main branch (due to a concurrent infrastructure change by another team)? What notifications would you configure, and who would receive them?

---

## Scenario C: Terraform Cloud vs. Self-Managed Backends

Your company is evaluating whether to use Terraform Cloud (free or paid tier) or to continue self-managing a state backend (S3 + DynamoDB + KMS). The team of 8 infrastructure engineers currently spends about 4 hours per month maintaining the backend infrastructure, access policies, and rotation procedures.

Make the case for one option. Consider total cost of ownership (including engineering time), security posture, feature set, vendor lock-in risk, compliance requirements, and the team's current pain points. If you recommend Terraform Cloud, which tier, and what justifies the cost? If you recommend self-managed, what improvements would you make to the current setup to reduce maintenance burden? Is there a hybrid approach that captures the best of both?

---

## Peer Response Guidelines

When responding to classmates:

- Engage with the specific technical points they made
- Add a detail, counterexample, or real-world context they may not have considered
- Respectfully correct any technical inaccuracies with supporting reasoning
- Ask a follow-up question that extends the discussion

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses the scenario directly and accurately | 3 |
| Technical content is correct and demonstrates module knowledge | 3 |
| Post is 175–225 words (not including code snippets if used) | 1 |
| First peer response is substantive and adds value | 1.5 |
| Second peer response is substantive and adds value | 1.5 |
| **Total** | **10** |

---

**Professor Nash note**: Terraform Cloud sits at the intersection of tooling, process, and organizational design. The best answers in this forum will connect the technical capabilities we studied to real team dynamics — how engineers work, how trust is established, and how governance scales. I am looking for that connection, not just a feature list.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
