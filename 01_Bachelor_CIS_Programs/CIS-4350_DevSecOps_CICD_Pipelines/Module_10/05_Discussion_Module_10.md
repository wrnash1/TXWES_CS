# Discussion Forum: Module 10 — Cloud Security Posture Management (CSPM)

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Overview

This week's discussion focuses on Cloud Security Posture Management — the automated discipline of continuously detecting and remediating cloud misconfigurations. You will engage with three real-world scenarios drawn from actual breach cases and governance challenges that practitioners face. Initial posts are due Wednesday at 11:59 PM Central. Peer responses are due Sunday at 11:59 PM Central.

---

### Scenario 1 — The Public S3 Bucket

A financial services company discovers that a customer data S3 bucket has been publicly accessible for 14 months. The misconfiguration was introduced when a developer manually set `acl = "public-read"` through the AWS console during a late-night debugging session and forgot to revert it. The company had Checkov running in its Terraform CI/CD pipeline, but this bucket was not managed by Terraform — it was created through the console.

**Discussion Prompt:**

In 175–225 words, analyze this incident from a CSPM perspective. Your response must address:

- Why the Checkov pipeline gate failed to catch this misconfiguration, and what that reveals about the limits of IaC scanning as a sole CSPM control
- Which additional CSPM control layer — preventive, detective, or reactive — would have caught or prevented this specific misconfiguration, and name the specific AWS tool or service that implements it
- What organizational process change would prevent console-based provisioning that bypasses the IaC pipeline in the future

---

### Scenario 2 — Auto-Remediation in Production

A retail company's security team implements AWS Config auto-remediation for the `rds-storage-encrypted` rule. The SSM Automation document automatically enables encryption on any unencrypted RDS instance. During a peak shopping weekend, the auto-remediation fires on a production database that was provisioned outside Terraform three years ago. Enabling encryption at rest requires recreating the database instance, causing a four-hour outage. The engineering team is furious.

**Discussion Prompt:**

In 175–225 words, evaluate this auto-remediation failure. Your response must address:

- Which step in the auto-remediation implementation process was skipped that would have prevented the production outage
- How the team should restructure their auto-remediation governance to prevent this type of incident while still achieving automated remediation at scale
- Identify one category of CSPM finding where auto-remediation is safe to enable without extensive testing, and one category where human approval should always be required before remediation

---

### Scenario 3 — The CSPM Exception Creep Problem

A SaaS company begins its SOC 2 Type II audit preparation. The auditors review the CSPM exceptions register and find 847 active exceptions — 312 of which have expiry dates more than 24 months in the future, and 115 of which have no named risk owner. The original DevSecOps team that created most exceptions has been through significant turnover and many exception justifications reference architectural decisions that are no longer accurate.

**Discussion Prompt:**

In 175–225 words, design a remediation plan for this exceptions register problem. Your response must address:

- The immediate action the team should take before the audit to address exceptions without named risk owners
- A policy change to prevent exception creep going forward, specifying the maximum allowed expiry duration, required fields in each exception entry, and the review cadence
- How this exceptions register problem reflects a broader organizational maturity issue with the company's security culture and what DevSecOps practices would have prevented it

---

### Peer Response Requirements

After your initial post, write substantive replies to at least two classmates (minimum 60 words each). Your peer responses should:

- Extend the analysis with a detail your classmate did not mention
- Offer a constructive alternative approach to the scenario
- Connect the scenario to a concept from a previous module (SAST, SCA, container security, etc.)

Responses that only agree or restate the original post do not meet the substantive requirement.

---

### Discussion Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all three required elements of the chosen scenario with technical accuracy | 4 |
| Initial post uses precise CSPM and DevSecOps terminology (names specific tools, services, and control types) | 2 |
| Initial post meets the 175–225 word count requirement | 1 |
| First peer response is substantive — extends analysis or offers an alternative approach | 1.5 |
| Second peer response is substantive — extends analysis or offers an alternative approach | 1.5 |
| **Total** | **10** |

---

### Grading Notes

- Posts that say "I agree" or "Great point" without substantive technical addition receive 0 points for that peer response.
- Initial posts that address all required elements but use vague language ("use better security" or "implement proper controls") without naming specific tools, services, or control types receive partial credit (2–3 points).
- Late initial posts submitted after Wednesday at 11:59 PM receive a 20% deduction per day up to a maximum of 60%.
