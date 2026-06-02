# CIS-4337 Infrastructure Automation

## Quiz — Module 02: Terraform Workflow

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

Which command downloads and installs the provider plugins defined in your Terraform configuration files?

- A) `terraform apply`
- B) `terraform init`
- C) `terraform plan`
- D) `terraform get`

Correct Answer: B

Distractor Analysis:

- Why B is correct: `terraform init` is always the first command run in a new or cloned project. It resolves and downloads all provider and module dependencies declared in `required_providers` and `module` blocks into the `.terraform/` directory.
- Why A is incorrect: `terraform apply` executes planned infrastructure changes. It requires provider plugins to already be installed by a previous `init` run.
- Why C is incorrect: `terraform plan` generates an execution plan. It requires providers to be installed before it can run.
- Why D is incorrect: `terraform get` downloads only module dependencies and is rarely called directly because `terraform init` handles both providers and modules.

---

### Question 2

Which of the following most accurately defines HCL (HashiCorp Configuration Language)?

- A) A proprietary binary compilation format that Terraform uses to cache provider API responses for faster re-runs.
- B) A human-readable, declarative language used to write Terraform configuration files that describe desired infrastructure state using blocks and attribute-value pairs.
- C) A runtime scripting language embedded in Terraform that executes imperative shell commands against cloud provider APIs.
- D) A JSON schema specification that validates the structure of `terraform.tfstate` files before each apply operation.

Correct Answer: B

Distractor Analysis:

- Why B is correct: HCL is the language of `.tf` files. It is declarative, human-readable, and expresses desired infrastructure state using block types such as `resource`, `provider`, `variable`, and `output`.
- Why A is incorrect: HCL is a text-based configuration language, not a binary cache format.
- Why C is incorrect: HCL is declarative. While `local-exec` provisioners can run shell commands, HCL itself is not a runtime scripting language.
- Why D is incorrect: HCL is used for writing configurations, not for validating state files.

---

### Question 3

You run `terraform plan` and see a resource annotated with `-/+` in the output. What does this symbol mean?

- A) The resource will be updated in place with no interruption to service.
- B) The resource will be destroyed and then recreated because one of its attributes cannot be changed after creation.
- C) The resource is being imported from existing infrastructure outside of Terraform.
- D) The resource has no changes and will be left in its current state.

Correct Answer: B

Distractor Analysis:

- Why B is correct: The `-/+` symbol indicates forced replacement. When an attribute that is immutable after resource creation needs a new value (such as an EC2 instance's AMI ID), Terraform must destroy the existing resource and create a new one. The new resource will have a different ID.
- Why A is incorrect: In-place updates are indicated by `~` (tilde), not `-/+`.
- Why C is incorrect: Import operations use `terraform import` and do not surface as `-/+` in a plan.
- Why D is incorrect: Resources with no planned changes show no action symbol and are not listed in the changes section of the plan.

---

### Question 4

In a project using a remote backend, a team member adds a new provider to `main.tf` and runs `terraform init` again. What happens?

- A) The new provider is automatically installed without any explicit command needed.
- B) `terraform init` downloads the new provider plugin and updates the `.terraform.lock.hcl` dependency lock file.
- C) Terraform deletes the existing state file and starts fresh with the new provider.
- D) `terraform init` replaces the backend configuration and migrates all existing state to the new provider.

Correct Answer: B

Distractor Analysis:

- Why B is correct: `terraform init` is designed to be re-run whenever the configuration changes. It downloads any missing providers and updates the lock file with new version hashes while leaving existing state and backend configuration untouched.
- Why A is incorrect: New providers are never automatically installed. You must explicitly run `terraform init` to fetch them.
- Why C is incorrect: `terraform init` never modifies or deletes the state file.
- Why D is incorrect: Backend configuration changes require explicit user confirmation via the `-migrate-state` or `-reconfigure` flag; `init` alone does not replace backends.

---

### Question 5

Which workflow sequence ensures that the exact plan reviewed by an engineer is the one applied in a CI/CD pipeline?

- A) Run `terraform apply -auto-approve` directly, skipping the plan step to reduce pipeline execution time.
- B) Run `terraform validate` only; if it passes, the pipeline automatically applies all changes.
- C) Run `terraform plan -out=tfplan`, have the plan reviewed and approved, then run `terraform apply tfplan` to execute the saved plan.
- D) Run `terraform destroy` followed immediately by `terraform apply` to guarantee a clean environment on every deployment.

Correct Answer: C

Distractor Analysis:

- Why C is correct: Saving the plan with `-out=tfplan` and then applying the binary plan file guarantees that no configuration changes can slip in between the review step and the execution step. This is the HashiCorp-recommended CI/CD pattern.
- Why A is incorrect: Skipping the plan review removes human oversight of what changes will reach production, which is a significant operational risk.
- Why B is incorrect: `terraform validate` only checks HCL syntax and internal references. It does not verify what infrastructure changes will be made against live infrastructure.
- Why D is incorrect: Destroying and re-applying on every deployment causes unnecessary downtime and creates data-loss risk for stateful resources such as databases.

---

### Question 6

What does the `.terraform.lock.hcl` file record, and should it be committed to version control?

- A) It records the current state of all managed resources and must not be committed because it contains sensitive data.
- B) It records the exact provider versions and checksums selected during `terraform init` and should be committed to ensure reproducible installs across all team members.
- C) It records the saved execution plan from the most recent `terraform plan` run and is only needed locally.
- D) It locks the working directory so no other Terraform process can run concurrently and is deleted after apply completes.

Correct Answer: B

Distractor Analysis:

- Why B is correct: The lock file pins provider versions and their integrity checksums. Committing it ensures that every team member and every CI/CD pipeline run uses identical provider binaries, eliminating version-mismatch bugs.
- Why A is incorrect: The lock file contains provider version constraints and checksums, not resource state or sensitive data. The state file is what contains sensitive values.
- Why C is incorrect: Saved plan files are produced by `terraform plan -out=<file>`. They are separate from the lock file and are typically not committed to version control.
- Why D is incorrect: Concurrent operation locking is handled by state backends, not by the lock file. The lock file is not deleted after apply.

---

### Question 7

A `terraform plan` output shows `~ update in-place` next to `aws_instance.web`. What does the `~` symbol indicate?

- A) The instance will be destroyed and a brand-new instance will be created with a new ID.
- B) The instance's configuration will change but the resource will not be destroyed; changes are applied to the existing resource.
- C) The instance is being read from a data source and will not be modified.
- D) The instance is being imported from outside of Terraform management.

Correct Answer: B

Distractor Analysis:

- Why B is correct: The `~` symbol means in-place update. The resource exists and Terraform will modify its mutable attributes without destroying and recreating it. The resource retains the same ID.
- Why A is incorrect: Destroy-and-recreate is indicated by `-/+`, not `~`.
- Why C is incorrect: Data source reads are indicated by `<=`, not `~`.
- Why D is incorrect: Import operations are performed through `terraform import` and do not show as `~` in a plan.

---

### Question 8

Which command checks HCL syntax and internal configuration consistency without making any API calls to provider services?

- A) `terraform plan`
- B) `terraform apply -refresh-only`
- C) `terraform validate`
- D) `terraform show`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform validate` performs static analysis of the configuration. It checks block syntax, required arguments, valid references, and type consistency. It makes no network calls and requires no provider credentials.
- Why A is incorrect: `terraform plan` does query provider APIs to refresh live resource state. It also requires provider plugins to be installed.
- Why B is incorrect: `terraform apply -refresh-only` updates the state file to match live resource state without changing any resources. It does make API calls.
- Why D is incorrect: `terraform show` displays the current state or a saved plan file in human-readable form. It does not check configuration syntax.

---

### Question 9

After running `terraform apply`, you want to remove all resources managed by the current configuration. Which command accomplishes this?

- A) `terraform apply -destroy`
- B) `terraform reset`
- C) `terraform clean`
- D) `terraform state rm`

Correct Answer: A

Distractor Analysis:

- Why A is correct: `terraform apply -destroy` is equivalent to `terraform destroy`. It generates a plan to remove all managed resources, shows it for review, and deletes them after confirmation. Both `terraform destroy` and `terraform apply -destroy` are valid answers on the exam.
- Why B is incorrect: `terraform reset` is not a valid Terraform command.
- Why C is incorrect: `terraform clean` is not a valid Terraform command.
- Why D is incorrect: `terraform state rm` removes a resource from the state file without destroying the actual cloud resource. This is used when you want Terraform to stop managing a resource, not when you want to delete it.

---

### Question 10

You run `terraform plan` and the output ends with: `Plan: 0 to add, 0 to change, 0 to destroy.` What does this result indicate?

- A) The configuration files are empty and no resources have been declared.
- B) Terraform encountered an authentication error and could not read live resource state.
- C) The live infrastructure matches the declared configuration exactly; Terraform has nothing to change.
- D) The state file has been deleted and Terraform cannot determine what resources exist.

Correct Answer: C

Distractor Analysis:

- Why C is correct: A "0 to add, 0 to change, 0 to destroy" result means Terraform refreshed live state, compared it to the configuration, and found them to be identical. This is the expected result of running plan on infrastructure that has not drifted since the last apply — it demonstrates idempotency.
- Why A is incorrect: If configuration files were empty, Terraform would plan to destroy any resources currently tracked in state, not report zero changes.
- Why B is incorrect: An authentication error would produce an error message, not a clean plan with zero changes.
- Why D is incorrect: A missing state file would cause Terraform to treat all declared resources as new and plan to create them, not report zero changes.

---

Module 02 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
