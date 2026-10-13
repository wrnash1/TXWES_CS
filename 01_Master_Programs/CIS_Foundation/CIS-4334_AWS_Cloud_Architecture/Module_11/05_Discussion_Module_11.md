# Discussion Forum: Module 11 — AWS IAM and Security Architecture

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to the scenario. Then write a substantive reply (75–100 words) to at least one classmate who chose a different scenario. Use specific AWS service names and feature names in your response.

---

## Scenario A — The Credential Compromise Incident

A security team receives an alert from Amazon GuardDuty: `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` — an IAM user named `deploy-automation` has logged into the AWS console from an IP address in Eastern Europe. This user's access key was found in a public GitHub repository after a developer accidentally committed it two weeks ago. The security team must respond immediately.

Describe the complete incident response workflow. What are the first three immediate actions the team should take to contain the damage? How should the `deploy-automation` user's purpose (automation) have been implemented using IAM roles and STS instead of a long-term access key to prevent this entirely? Explain how CloudTrail can help determine what actions the attacker performed with the compromised credentials during the two-week exposure window. What AWS service would help detect if the attacker created any new IAM users, roles, or backdoors before credentials were revoked?

---

## Scenario B — The SCP Governance Gap

A large enterprise runs 50 AWS accounts across three Organizational Units: Production, Development, and Sandbox. The Security team wants to implement organizational guardrails. A junior cloud engineer suggests applying a single SCP to the organizational root that denies all actions not on an approved list. A senior architect pushes back and says this approach will cause immediate problems.

Explain why a "deny all by default, allow specific actions only" SCP at the organizational root is problematic for an organization already running workloads. What is the SCP model that AWS recommends for organizations with existing workloads? Describe at least three specific SCPs that would be appropriate to apply to the Production OU to enforce security governance without breaking existing applications. Explain why SCPs applied to the Production OU should be more restrictive than those applied to the Sandbox OU.

---

## Scenario C — Defense in Depth for a Healthcare Application

A healthcare company is building a patient portal on AWS that will store Protected Health Information (PHI) in compliance with HIPAA. The CTO asks you to design the security architecture. A colleague says "we just need a private VPC and HTTPS — that's enough for HIPAA."

Explain why HTTPS and a private VPC alone are insufficient for a HIPAA-compliant healthcare application on AWS. Describe the complete defense-in-depth security architecture, addressing at minimum: encryption at rest (which KMS key type and why), encryption in transit, access control (IAM principles for least privilege), threat detection (which AWS service and what it monitors), audit logging (what must be logged and for how long), and application-layer protection (WAF rules for a patient-facing web portal). Reference at least two AWS services from Module 11 that are specifically relevant to PHI protection.

---

## Peer Response Instructions

After posting your initial response, read your classmates' posts and reply to at least one person who chose a different scenario than you. Your reply should:

- Identify one point in their response you agree with and explain why
- Identify one consideration they may have missed or could strengthen
- Ask a follow-up question that extends the discussion

---

## 10-Point Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical Accuracy | 3 | AWS service names, IAM concepts, and security behaviors described correctly |
| Depth of Analysis | 2 | Response addresses the specific scenario with concrete recommendations |
| Word Count (Initial) | 1 | Initial post is between 175 and 225 words |
| Use of Module Concepts | 2 | Response explicitly references concepts from Module 11 video and reading guide |
| Peer Reply Quality | 2 | Reply is substantive (75–100 words), identifies a specific point, and asks a meaningful follow-up question |
| **Total** | **10** | |

---

**Professor Nash Note:** Scenario A is the one most students will encounter in their careers. Access key compromise via GitHub is not a hypothetical — it happens constantly, and there are automated scanners that find AWS credentials in public repositories within minutes of a commit. The architectural lesson is not just "rotate your keys" — it is "stop using long-term access keys for automation entirely." If you choose Scenario A, be specific about the timeline: what does the attacker have access to during the 14-day window, and why does using IAM roles with STS-issued temporary credentials eliminate this entire attack class?

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
