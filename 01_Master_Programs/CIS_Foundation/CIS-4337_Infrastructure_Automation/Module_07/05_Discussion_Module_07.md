# Discussion: Module 07 — Terraform Variables, Outputs, and Locals

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be **175–225 words**. Reply to **two classmates** with substantive feedback (minimum 75 words each). All posts are due by Sunday at 11:59 PM CT.

---

## Scenario A: The Sensitive Variable Misconception

A junior engineer on your team declares all database credentials as Terraform variables and marks them `sensitive = true`. She tells the security team, "Don't worry — these are encrypted because I used the sensitive flag." The security team accepts her explanation and closes the ticket.

Discuss the technical accuracy of her statement. What does `sensitive = true` actually protect against? What does it not protect against? What additional controls should the team implement to genuinely protect the credentials at rest? Reference specific Terraform features or external tools that address the gap she has left open. Consider both the state file storage problem and the risk of credentials appearing in CI/CD logs. What would you tell this engineer to ensure she understands the complete picture without undermining her confidence?

---

## Scenario B: Variable Precedence Debugging

A DevOps engineer is troubleshooting a deployment to the wrong AWS region. The configuration has a `terraform.tfvars` file setting `region = "us-east-1"`, but the resources are being created in `eu-west-1`. The engineer has checked the code twice and cannot find the problem.

Walk through the complete variable precedence order that Terraform uses. Identify all the sources that could be overriding the `.tfvars` file to produce `eu-west-1`. How would you systematically diagnose which source is winning? What command or technique would you use to reveal the effective variable values before apply? Discuss how teams can avoid this class of confusion in the future through documentation or tooling conventions. What would your debugging checklist look like for a variable that is not resolving to its expected value?

---

## Scenario C: Locals vs. Variables Design Decision

You are designing a Terraform module for a startup that plans to deploy the same application stack across five environments: `dev`, `qa`, `staging`, `uat`, and `prod`. The team is debating whether to use a single large `locals` block to define all environment-specific values, or whether to use input variables for everything and pass in separate `.tfvars` files per environment.

Argue for the approach you believe is architecturally superior. Consider maintainability, reusability, the risk of misconfiguration, and how the module interface should be designed for callers who may not understand the internals. Is there a hybrid approach that combines both? How would you structure the `.tfvars` files and locals together to get the benefits of both? Reference the concept of module interface design and what it means for a module to be self-documenting.

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

**Professor Nash note**: There are no universally right answers in these scenarios — the goal is rigorous technical reasoning. A well-argued case for a less common approach earns full credit if the reasoning is sound. I look for evidence that you have internalized the mechanics, not just recalled the definitions.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
