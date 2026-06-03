# Quiz: Module 06 — Infrastructure as Code Security

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Submit answers through the Canvas quiz interface.

---

## Question 1

Which statement best describes the primary reason IaC misconfigurations are so prevalent despite engineers using infrastructure code review processes?

- A) IaC files are too large to review effectively
- B) Engineers frequently copy public examples that prioritize functionality over security, and cloud APIs add new security parameters that legacy configs do not use
- C) IaC scanners are too slow to run in CI pipelines
- D) Cloud providers do not provide documentation about secure defaults

### Q1 — Correct Answer: B

### Q1 — Distractor Analysis

- A) File size is not a meaningful barrier to reviewing IaC — most Terraform files are small.
- C) IaC scanners like tfsec and checkov complete in seconds — speed is not the cause of misconfigurations.
- D) Cloud providers publish extensive security documentation; the problem is adoption and training, not availability.

---

## Question 2

tfsec is designed primarily to scan which type of infrastructure code?

- A) Kubernetes YAML manifests
- B) Terraform `.tf` files
- C) AWS CloudFormation templates
- D) Dockerfile configurations

### Q2 — Correct Answer: B

### Q2 — Distractor Analysis

- A) Kubernetes manifest scanning is supported by checkov and Trivy config mode — tfsec focuses on Terraform.
- C) CloudFormation scanning is supported by checkov and cfn-lint — not tfsec's primary focus.
- D) Dockerfile scanning is handled by hadolint or checkov — not tfsec.

---

## Question 3

A checkov inline suppression comment is written as `# checkov:skip=CKV_AWS_25: Public HTTP required for ALB`. What security benefit does including the justification text after the colon provide?

- A) The justification text is automatically validated against an approved exception database
- B) The justification creates an auditable record of accepted risk tracked in Git history
- C) Including a justification causes checkov to score the finding as lower severity
- D) The justification text triggers automatic ticket creation in Jira

### Q3 — Correct Answer: B

### Q3 — Distractor Analysis

- A) There is no automated validation of suppression justification — it is a human-readable comment.
- C) Justification text does not affect severity scoring — the finding is simply skipped.
- D) Checkov has no built-in integration with Jira ticket creation from suppression comments.

---

## Question 4

In HashiCorp Sentinel, which enforcement level blocks a Terraform plan and cannot be overridden by any user, including administrators?

- A) Advisory
- B) Soft Mandatory
- C) Hard Mandatory
- D) Strict

### Q4 — Correct Answer: C

### Q4 — Distractor Analysis

- A) Advisory logs the violation but allows the plan to proceed — it is the least-restrictive level.
- B) Soft Mandatory blocks but can be overridden by users with the appropriate override permission.
- D) "Strict" is not a Sentinel enforcement level — only Advisory, Soft Mandatory, and Hard Mandatory exist.

---

## Question 5

A developer runs `terraform plan -refresh-only` and sees that an AWS security group now allows `0.0.0.0/0` on port 22, but the Terraform code does not have that rule. What most likely caused this discrepancy?

- A) A bug in the Terraform AWS provider
- B) Configuration drift caused by a manual change made in the AWS console
- C) The `.tfstate` file is corrupted
- D) The developer ran the plan with the wrong AWS credentials

### Q5 — Correct Answer: B

### Q5 — Distractor Analysis

- A) Provider bugs that silently add security group rules are extremely rare — manual changes are far more common.
- C) State file corruption typically causes Terraform to fail entirely, not produce unexpected resource diffs.
- D) Wrong credentials would cause permission errors, not phantom security group rules.

---

## Question 6

What is the primary security risk of storing the Terraform state file (`.tfstate`) in a public or unencrypted location?

- A) It allows anyone to see which Terraform modules are being used
- B) State files frequently contain plaintext secrets such as database passwords and API keys
- C) It enables unauthorized users to run `terraform destroy` on the infrastructure
- D) It exposes the Terraform version being used, enabling version-specific attacks

### Q6 — Correct Answer: B

### Q6 — Distractor Analysis

- A) Module names are not sensitive security information.
- C) Running `terraform destroy` requires Terraform CLI credentials, not just access to the state file.
- D) Terraform version disclosure is a minimal risk compared to plaintext secret exposure.

---

## Question 7

Which command generates a JSON representation of a Terraform execution plan that can be tested with Conftest?

- A) `terraform show --json`
- B) `terraform plan -out=tfplan.binary && terraform show -json tfplan.binary`
- C) `terraform output -json`
- D) `terraform state pull`

### Q7 — Correct Answer: B

### Q7 — Distractor Analysis

- A) `terraform show --json` without a plan file shows the current state, not the planned changes.
- C) `terraform output -json` shows output values from the current state — not the planned changes to resources.
- D) `terraform state pull` downloads the raw state file — it does not show planned changes.

---

## Question 8

The immutable infrastructure principle improves security compared to traditional server patching primarily because:

- A) Immutable servers are automatically encrypted at rest
- B) Replacing servers eliminates configuration drift, ensuring production always matches the IaC-defined state
- C) Immutable infrastructure does not require network access after initial deployment
- D) Replacement builds are faster than patching, reducing the window of exposure

### Q8 — Correct Answer: B

### Q8 — Distractor Analysis

- A) Encryption at rest is a separate configuration — immutability does not automatically enable it.
- C) Servers still require network access for communication — immutability refers to configuration management, not network isolation.
- D) Speed is a secondary benefit; eliminating drift is the primary security rationale.

---

## Question 9

checkov's ability to scan multiple frameworks in a single tool provides which DevSecOps pipeline advantage over tfsec?

- A) checkov scans faster than tfsec because it uses a compiled binary
- B) A single checkov job can enforce security standards across Terraform, Kubernetes, Dockerfiles, and CloudFormation simultaneously
- C) checkov automatically creates pull requests with remediation suggestions
- D) checkov integrates with HashiCorp Vault for secret scanning inside IaC files

### Q9 — Correct Answer: B

### Q9 — Distractor Analysis

- A) Performance is not the differentiator — both tools are fast enough for CI use.
- C) Neither checkov nor tfsec automatically creates PRs with fixes — Bridgecrew's platform does, but the open-source CLI does not.
- D) Vault integration is not a checkov feature — secret detection in IaC is handled by tfsec's `general-secrets` rules or by gitleaks.

---

## Question 10

OPA Conftest uses the `deny` rule pattern in Rego policies. What happens when a Conftest policy has zero `deny` violations?

- A) Conftest exits with a non-zero code to indicate no policy was evaluated
- B) Conftest exits with code 0 (success), indicating all policies passed
- C) Conftest exits with a warning code and continues to the next policy file
- D) Conftest requires explicit `allow` rules to be defined for a pass result

### Q10 — Correct Answer: B

### Q10 — Distractor Analysis

- A) Zero violations means all checks passed — Conftest exits 0, not with an error.
- C) Conftest uses standard Unix exit codes — 0 for success, non-zero for failure — there is no "warning" exit code.
- D) Rego in Conftest defaults to deny-unless-explicitly-denied — `allow` rules are not required for the policy to pass.

---

Quiz — Module 06 | CIS-4350 | Texas Wesleyan University | Professor Nash
