# Discussion: Module 09 — Terraform Modules

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be **175–225 words**. Reply to **two classmates** with substantive feedback (minimum 75 words each). All posts are due by Sunday at 11:59 PM CT.

---

## Scenario A: The Shared Module Library Debate

Your company's platform team wants to build an internal Terraform module library — a Git repository containing modules for VPCs, EKS clusters, RDS databases, and S3 buckets. Two engineers have a strong disagreement about the approach:

**Engineer A** argues that every team should be able to modify the shared modules freely and merge changes directly. This keeps modules current with each team's needs.

**Engineer B** argues that shared modules should be versioned with Git tags, and consuming teams should pin to a specific version. Changes require going through a review process.

Which approach do you support, and why? What are the risks of the opposing approach in a real production environment? Reference specific Terraform mechanisms (version constraints, `?ref=` in Git sources, semantic versioning) in your argument. Is there a middle ground that captures the benefits of both positions? How would you structure the release process for a shared module to balance stability and velocity?

---

## Scenario B: Registry vs. Internal Module

Your team is starting a new AWS infrastructure project. A popular community module on the Terraform Registry (`terraform-aws-modules/vpc/aws`) would give you a production-ready VPC with subnets, routing tables, NAT gateways, and flow logs in about 30 lines of configuration. Alternatively, your senior engineer suggests writing your own VPC module from scratch to maintain full control.

Argue for one approach. Consider the trade-offs in terms of maintenance burden, security patch cadence, customization flexibility, onboarding new engineers, and organizational knowledge. How would you evaluate a community module's trustworthiness before using it in production? What criteria would tip the decision toward building internally? What criteria would tip it toward the public Registry?

---

## Scenario C: Module Abstraction Level

You are designing a Terraform module for your organization's standard Kubernetes application deployment on AWS (EKS). You must decide how coarse-grained or fine-grained to make the module. Two extreme options are presented:

**Option 1 — Coarse**: A single module called `aws_k8s_app` that takes `app_name`, `image`, and `replicas` as inputs and provisions everything — EKS cluster, node groups, load balancer, DNS records, monitoring, and TLS certificates.

**Option 2 — Fine**: Separate modules for each layer: `eks_cluster`, `node_group`, `alb_ingress`, `route53_record`, `acm_certificate`, `cloudwatch_dashboard`.

Discuss the trade-offs of each approach in terms of reusability, composability, blast radius (what breaks when one thing changes), and the cognitive load placed on operators. Is there a "right" answer, or does it depend on organizational context? What principles would guide your decision?

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

**Professor Nash note**: Module design is a discipline unto itself, and experienced Terraform engineers still debate these questions. There is no single answer — context matters enormously. I am looking for evidence that you can reason through trade-offs rather than simply pick a side.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
