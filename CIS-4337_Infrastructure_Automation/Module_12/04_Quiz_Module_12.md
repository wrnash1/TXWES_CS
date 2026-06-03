# Quiz: Module 12 — Terraform and CI/CD Pipelines

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Select the best answer for each question. Each question is worth 1 point. Distractor analysis follows each question to explain why incorrect options are wrong.

---

## Questions

### Question 1 — Answer: C

A CI pipeline runs `terraform plan -detailed-exitcode`. The pipeline script checks the exit code and the job exits with code 2. What does this indicate?

A. The plan encountered a fatal error and no plan was generated.

B. The plan completed successfully and no infrastructure changes are needed.

C. The plan completed successfully and infrastructure changes are present.

D. The pipeline was cancelled before the plan could finish.

Why the distractors are wrong: **A** is wrong because exit code 1 indicates an error — exit code 2 specifically signals that the plan succeeded and changes are present. **B** is wrong because exit code 0 means no changes; exit code 2 means changes were detected. **D** is wrong because a cancelled pipeline reports its own cancellation status, not a predictable Terraform exit code.

---

### Question 2 — Answer: C

Your team wants to ensure that the exact plan reviewed in a pull request is the one that gets applied after merge. Which approach achieves this?

A. Run `terraform plan` again at apply time using the same commit SHA.

B. Save the plan output as a text file in the repository and read it during apply.

C. Save the binary plan file as a CI artifact and apply it with `terraform apply tfplan`.

D. Use `terraform refresh` before apply to ensure state is current.

Why the distractors are wrong: **A** is wrong because a new plan at apply time can differ if cloud resources changed or provider versions differ. **B** is wrong because the human-readable plan text cannot be consumed by `terraform apply` — only the binary `.tfplan` file produced by `-out=tfplan` can. **D** is wrong because `terraform refresh` updates state but does not produce a plan and does not guarantee the apply matches the reviewed output.

---

### Question 3 — Answer: B

Which authentication method eliminates the need to store long-lived cloud provider credentials as CI/CD secrets?

A. IAM user access keys stored in environment variables

B. OpenID Connect (OIDC) federated identity

C. Encrypted credentials committed to a private repository

D. SSH key pairs uploaded to the CI platform

Why the distractors are wrong: **A** is wrong because IAM access keys are long-lived — if the CI secrets store is compromised the attack window is large. **C** is wrong because committing credentials to any repository is a security anti-pattern regardless of encryption. **D** is wrong because SSH key pairs are for repository and server authentication, not cloud provider API authentication.

---

### Question 4 — Answer: C

In a GitLab CI pipeline, a job is configured with `when: manual`. What is the behavior of this job?

A. The job runs automatically when the previous stage succeeds.

B. The job is skipped unless a specific environment variable is set.

C. The job pauses the pipeline and requires a human to click play in the GitLab UI.

D. The job runs only on scheduled pipelines, not on push events.

Why the distractors are wrong: **A** is wrong because that describes the default `when: on_success` behavior. **B** is wrong because conditional execution on environment variables uses `rules:` with `if:` conditions. **D** is wrong because `when: manual` is not tied to scheduled pipelines; it creates a pause point on any trigger type.

---

### Question 5 — Answer: C

A developer manually enables a public access setting on an S3 bucket through the AWS console. The Terraform configuration has `block_public_acls = true`. What term describes this situation, and what command detects it?

A. Configuration conflict; detected with `terraform validate`

B. State corruption; detected with `terraform show`

C. Infrastructure drift; detected with `terraform plan`

D. Provider error; detected with `terraform providers`

Why the distractors are wrong: **A** is wrong because `terraform validate` checks HCL syntax only and does not contact cloud providers. **B** is wrong because state corruption means a damaged state file, not a resource changed outside Terraform; `terraform show` displays state but does not compare it to live infrastructure. **D** is wrong because `terraform providers` lists provider requirements and does not inspect resource state.

---

### Question 6 — Answer: C

Which tfsec command-line flag causes the tool to report findings but exit with code 0 even when issues are found?

A. `--ignore-warnings`

B. `--no-color`

C. `--soft-fail`

D. `--format=json`

Why the distractors are wrong: **A** is wrong because `--ignore-warnings` is not a valid tfsec flag; tfsec uses severity levels rather than a separate warnings category. **B** is wrong because `--no-color` disables ANSI color codes and does not affect exit codes. **D** is wrong because `--format=json` changes output format to JSON and does not affect exit codes.

---

### Question 7 — Answer: B

Your organization requires that all S3 buckets use a specific KMS key ARN. This rule is not in the default tfsec or Checkov check libraries. How do you enforce it?

A. Add a comment to every Terraform file reminding engineers to use the key.

B. Write a custom Checkov policy or tfsec YAML rule and include it in the pipeline.

C. Use `terraform validate` with a custom schema to enforce the KMS ARN.

D. Manually review every plan output for the correct KMS ARN before approving.

Why the distractors are wrong: **A** is wrong because comments are not enforceable and the pipeline will not catch violations. **C** is wrong because `terraform validate` checks HCL structure and type correctness, not specific attribute values. **D** is wrong because manual review is error-prone and does not scale to a team environment.

---

### Question 8 — Answer: B

Why are Terratest integration tests typically excluded from pull request pipelines and run only on a schedule or manually?

A. Terratest is incompatible with GitHub Actions and can only run locally.

B. Terratest tests deploy real cloud resources, making them slow and costly to run on every commit.

C. Terratest requires a special Terraform Enterprise license.

D. Terratest tests can only validate AWS resources.

Why the distractors are wrong: **A** is wrong because Terratest runs in any environment with Go installed, including GitHub Actions runners. **C** is wrong because Terratest is open-source with no dependency on Terraform Enterprise. **D** is wrong because Terratest supports AWS, Azure, GCP, Kubernetes, and more through its provider-specific modules.

---

### Question 9 — Answer: C

A team is designing their GitOps Terraform workflow. Which of the following configurations violates the GitOps principle?

A. All infrastructure changes are submitted as pull requests and reviewed before merge.

B. The CI pipeline posts `terraform plan` output as a comment on every pull request.

C. An on-call engineer runs `terraform apply` manually from their laptop during an incident.

D. The main branch is protected and requires at least one approval before merge.

Why the distractors are wrong: **A** is wrong because submitting all changes as PRs is a core GitOps practice. **B** is wrong because surfacing plan output in PRs supports the GitOps review process. **D** is wrong because branch protection with required approvals is a GitOps best practice.

---

### Question 10 — Answer: C

In a GitHub Actions workflow, an apply job has `needs: [validate, security-scan]` but no dependency on the plan job. What is the primary risk?

A. The apply job will always fail because it cannot find the tfplan artifact.

B. The apply job will run without waiting for security scan results.

C. The apply job may apply changes that were never reviewed in a PR plan comment.

D. The apply job will run `terraform plan` again automatically before applying, duplicating work.

Why the distractors are wrong: **A** is wrong because the apply job generates a new plan at apply time and would not automatically fail from a missing artifact. **B** is wrong because `needs: [validate, security-scan]` ensures security scan results are awaited. **D** is wrong because `terraform apply` without `-out` applies current state rather than running a new plan automatically.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | C |
| 2 | C |
| 3 | B |
| 4 | C |
| 5 | C |
| 6 | C |
| 7 | B |
| 8 | B |
| 9 | C |
| 10 | C |

---

End of Module 12 Quiz
