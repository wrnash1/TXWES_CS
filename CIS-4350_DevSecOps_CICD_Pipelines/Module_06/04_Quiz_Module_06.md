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

---

### Question 11 (5 points)

A Terraform configuration uses a `locals` block to construct a security group name from a variable: `local.sg_name = "${var.env}-app-sg"`. An attacker injects `; rm -rf /` as the `env` variable value. Why does this NOT result in code execution in Terraform?

- A) Terraform sanitizes all variable inputs automatically before use
- B) Terraform's HCL interpolation is a configuration language, not a shell — string interpolation does not execute OS commands
- C) Terraform runs in a sandboxed environment that blocks all system calls
- D) The `locals` block has no network access so injected commands cannot exfiltrate data

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Terraform does not automatically sanitize inputs — but HCL is a declarative language where string values are treated as data, not as shell commands.
  - C) Terraform does not run in a formal sandbox — the language design prevents injection, not a sandbox.
  - D) Whether network access exists is irrelevant to whether the injected string executes as a command.

---

### Question 12 (5 points)

A checkov scan produces a `CKV_AWS_18` finding on an S3 bucket configuration. The finding indicates access logging is not enabled. The team decides to accept this risk for a scratch bucket. How should this exception be documented to satisfy audit requirements?

- A) Delete the S3 bucket resource from the Terraform file until the scan passes
- B) Add `# checkov:skip=CKV_AWS_18: Scratch bucket — no PII, logging accepted risk, reviewed YYYY-MM-DD` inline in the resource block
- C) Lower the checkov severity threshold so CKV_AWS_18 is no longer reported
- D) Add the bucket to a global `.checkov.yaml` exclusion file without a justification comment

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Deleting the resource defeats the purpose — the bucket needs to exist.
  - C) Lowering severity thresholds suppresses other findings and does not create an auditable exception record.
  - D) Global exclusion files are appropriate for false positives but require justification; an undocumented suppression cannot satisfy audit requirements.

---

### Question 13 (5 points)

A Terraform remote backend uses an S3 bucket for state storage. Which two additional configurations are required to meet security best practices for state management?

- A) Public ACL enabled + versioning disabled
- B) Server-side encryption (SSE) + DynamoDB table for state locking
- C) Bucket replication enabled + CloudFront distribution for global access
- D) Bucket policy allowing all IAM users + versioning enabled

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Public ACL should be disabled — state files contain sensitive data and must not be publicly accessible.
  - C) Replication and CloudFront are availability/performance features — they do not address the security requirements of encryption and concurrent-write protection.
  - D) Allowing all IAM users is a permissions anti-pattern — least-privilege access to state should be strictly controlled.

---

### Question 14 (5 points)

A tfsec finding reports `aws-ec2-no-public-ingress-sgr` on a security group rule allowing `0.0.0.0/0` on port 443. The team intentionally hosts a public HTTPS endpoint. What is the correct way to handle this?

- A) Disable tfsec entirely — it produces too many false positives for public-facing infrastructure
- B) Use tfsec's `#tfsec:ignore:aws-ec2-no-public-ingress-sgr` annotation on the resource with an explanatory comment
- C) Change the security group to block port 443 — public HTTPS is not allowed by the security policy
- D) Switch from tfsec to checkov — checkov does not flag port 443 public ingress rules

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Disabling tfsec entirely removes all IaC security checks — a targeted suppression is appropriate.
  - C) Public HTTPS on port 443 is a standard and legitimate requirement — blocking it defeats the purpose of the service.
  - D) checkov also flags public ingress — switching tools does not resolve the issue.

---

### Question 15 (5 points)

In a GitOps workflow using Flux or ArgoCD, which security control ensures that only IaC changes reviewed and merged to `main` can be applied to the production cluster?

- A) A pre-commit hook that validates YAML before the developer pushes
- B) The GitOps operator reconciles cluster state exclusively from the `main` branch, so only merged, reviewed changes are applied
- C) A `terraform apply -auto-approve` command in the CI pipeline triggered on every push
- D) Manual SSH access to the cluster to apply manifests after review

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Pre-commit hooks are client-side and run before push — they do not control which branch the cluster tracks.
  - C) Auto-approve on every push bypasses the review gate — the GitOps model requires changes to go through a pull request and merge to a protected branch first.
  - D) Manual SSH application defeats the automation and auditability benefits of GitOps.

---

### Question 16 (5 points)

A Rego Conftest policy contains `deny[msg] { input.resource_changes[_].type == "aws_s3_bucket"; not input.resource_changes[_].change.after.versioning[_].enabled }`. What is the policy checking?

- A) That all S3 bucket names end with a versioning suffix
- B) That every S3 bucket in the Terraform plan has versioning enabled
- C) That no S3 buckets are being destroyed in the plan
- D) That S3 bucket objects are encrypted before upload

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The policy checks the `versioning.enabled` boolean field — not bucket name patterns.
  - C) Deletion checks would look at `change.actions` containing `"delete"` — not the `versioning` field.
  - D) Object encryption is a separate configuration (`server_side_encryption_configuration`) — not what this policy checks.

---

### Question 17 (5 points)

What is the primary risk of using `terraform apply` with static, long-lived AWS access keys stored as CI/CD environment variables?

- A) Long-lived keys increase Terraform plan execution time due to AWS API rate limiting
- B) Compromised CI/CD environment or pipeline logs can expose keys with full infrastructure modification access for an extended period
- C) AWS does not accept static access keys for Terraform — only IAM roles are supported
- D) Long-lived keys cause Terraform state drift because they use cached credentials

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Key longevity has no effect on Terraform execution time or API rate limits.
  - C) AWS fully supports static access keys for Terraform — IAM roles via OIDC are simply the more secure alternative.
  - D) State drift is caused by out-of-band infrastructure changes, not credential type.

---

### Question 18 (5 points)

A Terraform `resource "aws_db_instance"` block has `publicly_accessible = true`. Which IaC scanning tool and check would detect this misconfiguration?

- A) gitleaks with the `database-secret` rule
- B) checkov with `CKV_AWS_17` (Ensure that RDS database is not publicly accessible)
- C) Trivy with the `HIGH` severity container scan
- D) tfsec with the `general-secrets` check

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) gitleaks detects secrets in code — it does not analyze resource configuration attributes like `publicly_accessible`.
  - C) Trivy container scanning analyzes Docker images, not Terraform resource attributes.
  - D) tfsec's `general-secrets` check looks for hardcoded credentials — not resource accessibility flags.

---

### Question 19 (5 points)

The `terraform plan -out=tfplan.binary` command followed by `terraform show -json tfplan.binary > tfplan.json` produces JSON that Conftest can test. Why is testing the plan JSON preferred over testing the raw `.tf` source files?

- A) Plan JSON is smaller than `.tf` files, making Rego evaluation faster
- B) Plan JSON represents resolved values after variable substitution and module expansion, reflecting what will actually be applied to the cloud provider
- C) Testing `.tf` source files requires a running Terraform provider — plan JSON does not
- D) Conftest only supports JSON input — it cannot parse HCL `.tf` files directly

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) File size is not the reason — plan JSON is often larger than source `.tf` files.
  - C) Running a provider is required to generate the plan — this is not an advantage of plan JSON over source.
  - D) Conftest can parse `.tf` files with the `--parser` flag — the preference for plan JSON is about accuracy, not format limitation.

---

### Question 20 (5 points)

An organization uses Terraform Cloud with Sentinel policies at the `hard-mandatory` enforcement level. A developer attempts to apply a Terraform plan that creates an unencrypted RDS instance. What happens?

- A) Terraform Cloud logs the violation and sends an email but allows the apply to proceed
- B) The apply is blocked and cannot be overridden by any user, including workspace admins
- C) The apply is blocked but a workspace admin can override the policy and proceed
- D) The apply proceeds but the RDS instance is automatically remediated by Terraform Cloud to enable encryption

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Logging with email and allowing the apply is the behavior of `advisory` enforcement level, not `hard-mandatory`.
  - C) Override capability is the behavior of `soft-mandatory` — `hard-mandatory` cannot be overridden.
  - D) Terraform Cloud does not auto-remediate resources — it enforces policies at plan time, not after apply.
