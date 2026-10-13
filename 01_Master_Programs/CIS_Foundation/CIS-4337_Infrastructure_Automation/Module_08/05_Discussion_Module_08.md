# Discussion: Module 08 — Terraform State Management

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be **175–225 words**. Reply to **two classmates** with substantive feedback (minimum 75 words each). All posts are due by Sunday at 11:59 PM CT.

---

## Scenario A: The Corrupted State Crisis

A DevOps engineer at a mid-sized company ran two `terraform apply` operations simultaneously on the same state file stored in S3 — without a DynamoDB lock table configured. Both operations completed, but the resulting state file is partially corrupted: some resources are listed twice, others are missing. The infrastructure itself appears to be running normally.

Describe the full recovery plan you would execute. What is the first thing you check before doing anything else? How do you determine the true current state of the infrastructure? What role does `terraform state pull`, `terraform state show`, and `terraform import` play in the recovery? Going forward, what architectural changes do you implement to prevent this class of incident? Discuss the role of state locking specifically and why the S3 backend's locking behavior differs from Azure Blob or GCS.

---

## Scenario B: State File Secrets Audit

Your company's security team conducts an audit and discovers that Terraform state files for the production environment are stored in an S3 bucket without encryption, without versioning, and without IAM-restricted access. The audit flag notes that the state files contain plaintext database passwords and API keys.

Outline your remediation plan. Which issues are highest priority and why? Describe each security control you would implement, the specific AWS/Terraform configuration required to implement it, and how you would migrate to the new secure configuration with minimal disruption to the team's ongoing work. Address both the at-rest and in-transit security dimensions. What organizational processes (beyond technical controls) would you put in place to prevent this situation from recurring?

---

## Scenario C: The Great Refactor

A platform engineering team needs to refactor a large Terraform configuration. Currently, all 45 resources are defined in a single root configuration. The team wants to reorganize them into four modules: `network`, `compute`, `database`, and `storage`. The infrastructure is in production and cannot be destroyed.

Explain the approach you would use to perform this refactoring safely using `terraform state mv`. What is the order of operations? How do you verify that each step was performed correctly before proceeding to the next? What does the `terraform plan` output tell you at each stage? Are there risks in this process that cannot be fully mitigated through tooling, and if so, how would you address them procedurally? What would your rollback plan be if a step goes wrong partway through?

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

**Professor Nash note**: State management is where Terraform theory meets operational reality. The scenarios in this forum represent situations that happen in real production environments — sometimes with significant consequences. I am looking for responses that demonstrate you can reason under pressure and think about both the immediate fix and the systemic improvements.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
