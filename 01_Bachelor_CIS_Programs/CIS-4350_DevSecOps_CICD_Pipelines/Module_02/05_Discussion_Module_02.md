# Discussion Forum: Module 02 — Version Control Security and Git Best Practices

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Overview

Post your original response to one scenario below (minimum 175 words). Then reply substantively to at least two classmates' posts (minimum 75 words each). Original posts due Sunday 11:59 PM; peer replies due Tuesday 11:59 PM.

Professor Nash note: Focus on the real-world trade-offs. Pre-commit hooks, branch protection, and secrets scanning all have failure modes and organizational costs. I want to see that you understand not just what a control does, but when it might fail and what compensating controls exist.

---

## Scenario 1 — The Secrets Sprawl Audit

Your company conducts an audit and discovers that over the past two years, 47 different API keys, database passwords, and OAuth tokens have been committed to internal Git repositories. Most were in feature branches that were eventually merged to main. Some secrets appear in repositories that multiple contractors had access to during their engagement. The security team wants to know: (1) how did this happen, (2) what do you do right now about the exposed secrets, and (3) what controls do you implement going forward to prevent recurrence?

Address all three questions. For question 2, describe the remediation order of operations — what do you do first, second, and third? For question 3, describe at least two specific technical controls from this module and explain why their combination is stronger than either alone. Consider the limitations of pre-commit hooks and explain what server-side or CI-based control complements them.

### Scenario 1 — Peer Response Prompt

Your classmate proposed a remediation order. Is their ordering correct? Is there a step they missed? Consider what happens if a secret was used maliciously before it was discovered — does their plan account for that?

---

## Scenario 2 — Branching Strategy for a Regulated Industry

You work at a fintech company that must comply with PCI-DSS. The compliance officer insists on a formal change management process: every code change must be reviewed by two qualified individuals, traced to an approved change ticket, and have documented test evidence before reaching production. Your development team currently uses trunk-based development and deploys to production 15 times per day.

The compliance officer proposes switching to GitFlow with a two-week release cycle to enable proper review. Your tech lead argues that GitFlow's long-lived branches actually increase security risk through branch drift and that the compliance requirements can be met with trunk-based development using strict branch protection rules, mandatory signed commits, and CI audit logs.

Take a position. Is the compliance officer or the tech lead correct, or is the truth somewhere in between? How would you configure branch protection rules and CI pipeline requirements to meet PCI-DSS change management requirements while preserving developer velocity? Be specific about which branch protection settings you would enable and what the CI audit trail would look like.

### Scenario 2 — Peer Response Prompt

Your classmate took a position on GitFlow vs. trunk-based development for PCI-DSS compliance. Do you agree? What specific PCI-DSS requirement (if you can identify one) is most difficult to satisfy with either approach?

---

## Scenario 3 — The Insider Threat and Commit Signing

A disgruntled employee with a developer's workstation access makes several commits to a critical payment processing repository impersonating a senior engineer before being detected. The commits introduce subtle logic errors that cause transaction amounts to be rounded down — a classic "salami attack." The commits were not signed, and the repository did not require signed commits.

Analyze this scenario through the lens of the version control security controls covered in this module. Which specific controls, if implemented, would have prevented or detected this attack? Acknowledge the limits of signed commits — what do they prove and what do they not prove? If the attacker had also stolen the engineer's GPG private key along with their workstation access, what additional controls would have provided detection or prevention? Consider branch protection rules and code review requirements in your answer.

### Scenario 3 — Peer Response Prompt

Your classmate identified controls that would have prevented this attack. Are those controls sufficient, or does this scenario point to a defense-in-depth gap that no single version control security control can close?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Original post addresses all parts of the chosen scenario | 3 |
| Specific technical controls, tools, or configurations cited | 2 |
| Trade-offs and control limitations acknowledged | 2 |
| Peer reply 1 — adds new perspective, challenge, or missing element | 1.5 |
| Peer reply 2 — adds new perspective, challenge, or missing element | 1.5 |
| Total | 10 |

---

Discussion — Module 02 | CIS-4350 | Texas Wesleyan University | Professor Nash
