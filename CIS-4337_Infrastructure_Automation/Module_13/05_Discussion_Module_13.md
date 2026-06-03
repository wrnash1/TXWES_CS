# Discussion Forum: Module 13 — Terraform Security Best Practices

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Choose one of the three scenarios below. Write an initial post of 175–225 words responding to the scenario prompt. Then write two peer responses of 75–100 words each that add substantive new information, ask a clarifying question, or respectfully challenge an assumption in the original post. Use the 10-point rubric at the bottom of this page to self-assess before submitting.

---

## Scenario A: The Exposed State File

During a security audit, the auditor discovers that your team's production Terraform state file is stored in an S3 bucket with no encryption, no bucket policy restricting access, and versioning disabled. The bucket is private, but any IAM user in the AWS account can list and download the file. The state file contains RDS master passwords and an IAM access key that a provider stored as a resource attribute.

Discuss: What are the immediate remediation steps in order of priority? What would a fully hardened remote backend configuration look like? How would you handle the already-exposed credentials in the existing state file?

---

## Scenario B: Vault vs. Environment Variables

Your startup has five engineers and uses GitHub Actions with repository secrets for all Terraform credentials. A security-focused engineer is proposing that the team deploy HashiCorp Vault to replace environment variables entirely. The engineering manager questions whether the added complexity is worth it at this scale.

Discuss: At what point does the operational overhead of Vault become justified compared to CI platform secrets? What specific capabilities does Vault provide that environment variables cannot? Are there intermediate options that provide some of Vault's benefits without the full operational cost?

---

## Scenario C: The Least-Privilege Migration

Your team is inheriting a Terraform codebase from another team. All CI pipelines run with the AWS `AdministratorAccess` managed policy. There are 47 Terraform workspaces across 12 AWS accounts. The security team has given you 90 days to implement least-privilege IAM for all pipelines.

Discuss: How would you approach this migration systematically? What tooling would you use to determine what permissions each workspace actually requires? How would you handle the transition period where some workspaces are migrated and others are not?

---

## Sample Peer Response Starters

- "Your remediation priority order makes sense. I would also add that..."
- "I agree that Vault's dynamic secrets are valuable, but I think the threshold for adoption is actually lower because..."
- "Your migration plan is thorough. One risk in the 90-day window is..."

---

## Discussion Rubric — 10 Points Total

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario accuracy | 2 | Initial post correctly identifies and addresses the core technical problem in the scenario |
| Depth of analysis | 2 | Post goes beyond surface-level description and explains trade-offs or consequences |
| Use of module concepts | 2 | Post accurately applies vocabulary and concepts from Module 13 (Vault, sensitive, least privilege, state encryption, etc.) |
| Peer response 1 | 2 | First peer response adds new information, asks a clarifying question, or substantively engages with the original post |
| Peer response 2 | 2 | Second peer response meets the same standard and is not a simple agreement |

---

End of Module 13 Discussion
