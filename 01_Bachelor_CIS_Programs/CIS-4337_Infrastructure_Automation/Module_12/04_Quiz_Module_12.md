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

### Question 11 — Answer: B

A pipeline runs `terraform plan -out=tfplan` on a pull request branch. The PR is merged two days later. During that time, a colleague applied a change to the same infrastructure through a different PR. What is the risk of running `terraform apply tfplan` now?

A. The apply will fail because the plan artifact has expired.

B. The apply may attempt to revert the colleague's changes, because the saved plan is based on the state at plan time, not the current state.

C. The apply will automatically re-plan before executing to reconcile any state differences.

D. The apply will succeed because Terraform always refreshes state before applying a saved plan.

Why the distractors are wrong: **A** is wrong because plan artifacts do not have an automatic expiration that causes apply failures — the stale risk is logical, not a timeout error. **C** is wrong because `terraform apply <planfile>` applies the exact saved plan without re-planning; it is the responsibility of the pipeline design to manage stale artifacts. **D** is wrong because `terraform apply <planfile>` does not refresh state; refresh occurs during `terraform plan` or with `terraform apply -refresh=true`, which generates a new plan.

---

### Question 12 — Answer: A

A GitHub Actions workflow runs the apply job on every push to main, even for commits that only change documentation files. Which GitHub Actions feature would prevent unnecessary apply runs?

A. `paths` filter on the `push` trigger to only run the workflow when `.tf` files change

B. `if: github.actor != 'docs-bot'` condition on the apply job

C. A separate workflow file for documentation changes that overrides the Terraform workflow

D. Setting `continue-on-error: true` on the apply step so documentation-only failures are ignored

Why the distractors are wrong: **B** is wrong because filtering by actor is not a reliable way to detect documentation changes; it depends on who makes the commit rather than what changed. **C** is wrong because having a separate workflow file does not prevent the existing Terraform workflow from also running on the same trigger. **D** is wrong because `continue-on-error` handles failures, not unnecessary runs; the apply would still execute.

---

### Question 13 — Answer: D

A Checkov scan finds check `CKV_AWS_18` (S3 bucket access logging not enabled) but your organization has decided centralized VPC flow logs make per-bucket logging redundant. How do you suppress this specific check without disabling it globally?

A. Delete the check definition file from the Checkov installation directory.

B. Add `--skip-check CKV_AWS_18` to every `checkov` command in every pipeline job.

C. Set `soft_fail: true` in the Checkov GitHub Actions step to downgrade all failures to warnings.

D. Add `#checkov:skip=CKV_AWS_18:Covered by VPC flow logs` as an inline comment in the affected `.tf` file.

Why the distractors are wrong: **A** is wrong because modifying the Checkov installation is not version-controlled and would affect all scans, not just the specific resource. **B** is wrong because adding `--skip-check` to every pipeline job is a global suppression that removes visibility for all future resources of that type. **C** is wrong because `soft_fail` downgrades all findings, not just the specific check, and removes blocking enforcement for legitimate issues.

---

### Question 14 — Answer: C

A `terraform plan -detailed-exitcode` command exits with code 1. What is the correct automated response in a CI pipeline?

A. Treat it as a successful plan with no changes and proceed to apply.

B. Treat it as a successful plan with changes present and upload the plan artifact.

C. Fail the pipeline job and alert the team, because exit code 1 indicates an error, not a successful plan.

D. Re-run the plan job up to three times automatically before failing.

Why the distractors are wrong: **A** is wrong because exit code 0 means no changes; exit code 1 means an error, not a successful no-change plan. **B** is wrong because exit code 2 means changes present; exit code 1 is an error condition. **D** is wrong because retrying a plan that errored without understanding the cause risks masking infrastructure or credential problems.

---

### Question 15 — Answer: B

Which of the following is a valid reason to run `terraform validate` with `-backend=false` in a CI pipeline's validate job?

A. `-backend=false` skips provider plugin downloads, making the job faster.

B. `-backend=false` allows validate to run without backend credentials, making it safe to run on untrusted branches such as forks.

C. `-backend=false` prevents Terraform from modifying the state file during validation.

D. `-backend=false` disables the `.terraform.lock.hcl` check so any provider version can be used.

Why the distractors are wrong: **A** is wrong because `-backend=false` skips backend initialization, not provider downloads; providers may still be downloaded unless `-get=false` is also used. **C** is wrong because `terraform validate` never modifies state regardless of backend flag; validate is always read-only with respect to state. **D** is wrong because `-backend=false` does not affect the lock file check; lock file enforcement is independent of backend initialization.

---

### Question 16 — Answer: A

A scheduled drift detection pipeline has been running for six months and has never triggered. A new engineer removes the `aws_s3_bucket_public_access_block` resource from the Terraform configuration and merges the PR without any reviewer noticing. The apply removes the public access block from the production bucket. What control would have prevented this?

A. A required PR reviewer approval with Terraform plan output posted as a PR comment, so reviewers see the `destroy` action on the public access block before merging.

B. A tfsec scan, which would have flagged the removal as a security regression.

C. The drift detection pipeline, which would have detected the configuration change before apply.

D. A Terratest test, which would have asserted the public access block exists after apply.

Why the distractors are wrong: **B** is wrong because tfsec scans the remaining configuration for insecure patterns; removing a resource from configuration does not necessarily trigger a tfsec finding. **C** is wrong because drift detection compares live infrastructure to state; it detects changes made outside Terraform, not changes made through Terraform. **D** is wrong because Terratest runs after apply; it would detect the problem only after the destructive change already occurred.

---

### Question 17 — Answer: C

In a GitHub Actions workflow, what is the purpose of the `needs` keyword in a job definition?

A. It specifies which GitHub Actions marketplace actions the job requires to be installed.

B. It declares which environment variables the job needs from the repository secrets.

C. It creates an explicit dependency between jobs, ensuring the listed jobs complete successfully before the current job starts.

D. It sets the minimum runner size needed for the job to execute.

Why the distractors are wrong: **A** is wrong because marketplace action references are handled by `uses:` in individual steps, not by `needs`. **B** is wrong because environment variable references from secrets are handled by `env:` with `${{ secrets.NAME }}` syntax. **D** is wrong because runner configuration is set with `runs-on`, not `needs`.

---

### Question 18 — Answer: D

A Terratest test file calls `terraform.InitAndApply(t, terraformOptions)` without `defer terraform.Destroy(t, terraformOptions)`. What is the risk?

A. The test will fail because `InitAndApply` requires a corresponding `Destroy` call in the same function.

B. The test will run faster because skipping destroy avoids the teardown latency.

C. Terratest will automatically destroy resources after the test function returns if no defer is present.

D. If a test assertion fails and panics, the test exits without cleaning up cloud resources, leaving orphaned infrastructure that incurs ongoing costs.

Why the distractors are wrong: **A** is wrong because there is no language-level requirement to pair `InitAndApply` with `Destroy`; the code compiles and runs without it. **B** is incorrect as a risk — while the test is faster, the risk is exactly the missing cleanup. **C** is wrong because Terratest does not implement any automatic resource cleanup; cleanup is entirely the test author's responsibility via `defer`.

---

### Question 19 — Answer: B

Which statement correctly describes the relationship between `terraform fmt` and `terraform validate` in a CI pipeline?

A. `terraform fmt -check` modifies files in place; `terraform validate` checks those modified files for syntax errors.

B. `terraform fmt -check` fails if any files are not formatted to Terraform's canonical style without modifying them; `terraform validate` checks configuration syntax and type correctness without formatting.

C. Both commands contact the cloud provider API to verify that the specified resources exist.

D. `terraform validate` must be run before `terraform fmt -check` because validate generates the type information that fmt uses.

Why the distractors are wrong: **A** is wrong because `terraform fmt -check` does NOT modify files; `-check` causes it to exit with a non-zero code if files are unformatted, without making changes. **C** is wrong because neither command contacts cloud provider APIs; both are entirely local operations. **D** is wrong because `terraform fmt` operates on HCL syntax only and has no dependency on type information from validate.

---

### Question 20 — Answer: A

A team wants to implement OIDC authentication between GitHub Actions and AWS instead of storing long-lived access keys. Which AWS resource must be created in the AWS account to enable this trust relationship?

A. An IAM OIDC identity provider configured with GitHub's OIDC token endpoint URL, and an IAM role with a trust policy that allows GitHub Actions to assume it.

B. An AWS Secrets Manager secret containing the GitHub Actions runner's public key.

C. An IAM user with programmatic access and a permissions boundary limiting its capabilities.

D. An AWS STS endpoint configured to accept tokens from GitHub's IP address ranges.

Why the distractors are wrong: **B** is wrong because OIDC authentication does not use Secrets Manager or key-based secrets; the trust is established through the identity provider and role trust policy. **C** is wrong because OIDC eliminates the need for IAM users entirely; creating an IAM user defeats the purpose of OIDC. **D** is wrong because STS endpoints do not need IP-based configuration for OIDC; the trust is validated cryptographically through the OIDC token, not by network origin.

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
| 11 | B |
| 12 | A |
| 13 | D |
| 14 | C |
| 15 | B |
| 16 | A |
| 17 | C |
| 18 | D |
| 19 | B |
| 20 | A |

---

End of Module 12 Quiz
