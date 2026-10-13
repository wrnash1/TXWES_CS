# Discussion: Module 10 — Terraform Workspaces and Environments

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be **175–225 words**. Reply to **two classmates** with substantive feedback (minimum 75 words each). All posts are due by Sunday at 11:59 PM CT.

---

## Scenario A: The Workspace Incident

A mid-level DevOps engineer at a healthcare company uses Terraform workspaces to manage three environments: `dev`, `staging`, and `prod`. All three share an S3 backend and an AWS account. On a Friday afternoon the engineer selects the `staging` workspace, runs `terraform apply`, and only realizes during the apply that the terminal was actually in the `prod` workspace.

The apply completes. Infrastructure in production has been modified to match the staging configuration — 70% fewer compute replicas and a smaller database instance. The application begins degrading under load within minutes.

Walk through the immediate response steps you would take. What Terraform commands could help you understand the exact scope of change? Can state or infrastructure be quickly restored, and what would that involve? What organizational, procedural, and tooling changes would you recommend to prevent this class of incident in the future? Does this incident make an argument for or against workspaces for this use case?

---

## Scenario B: The Environments Architecture Decision

Your team is starting a new product from scratch. You have four environments planned: `dev`, `qa`, `staging`, and `prod`. The team size is three engineers today but expected to grow to fifteen within a year. The company is a startup with a compliance roadmap but no formal compliance requirements yet.

Design the environment management architecture. Should you use workspaces, directory-based isolation, or a hybrid? Justify your choice by reasoning through the team's current and anticipated needs. What would make you reconsider your choice in 12 months? Describe how the CI/CD pipeline would interact with your chosen approach — specifically, how `terraform init`, `terraform plan`, and `terraform apply` would be invoked per environment. What safeguards would you build into the pipeline to prevent accidental production deployments?

---

## Scenario C: Workspaces for Per-PR Environments

Your team is evaluating using Terraform workspaces to create ephemeral per-pull-request environments. The idea: when a PR is opened, the CI pipeline creates a workspace named `pr-<number>`, runs `terraform apply`, deploys a complete test environment, runs integration tests, then destroys everything and deletes the workspace when the PR is merged or closed.

Evaluate this proposal technically. What are the specific steps the CI pipeline must execute? What could go wrong, and how would you handle cleanup failures (a PR is force-closed without triggering the cleanup step)? What resource costs and limits does this approach introduce? Are there alternatives — such as feature flags or container-based ephemeral environments — that might achieve the same goal with fewer Terraform-specific risks? What conditions would lead you to recommend or reject this proposal for your team?

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

**Professor Nash note**: The scenarios in this forum reflect real decisions you will face as infrastructure engineers. There is rarely a universally correct answer — the right choice depends on team size, risk tolerance, compliance requirements, and organizational maturity. What I am grading is the quality of your reasoning, not the conclusion you reach.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
