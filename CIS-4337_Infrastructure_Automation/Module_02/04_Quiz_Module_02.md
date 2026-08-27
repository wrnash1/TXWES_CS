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

---

### Question 11 (5 points)

What is the effect of running `terraform init -upgrade` compared to plain `terraform init`?

- A) It destroys all managed resources and recreates them from scratch using the latest provider versions.
- B) It forces re-download of provider plugins to the latest versions allowed by the declared version constraints, even if a cached version already exists.
- C) It migrates the state file from a local backend to a remote backend automatically.
- D) It upgrades the Terraform CLI binary to the latest stable release.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `-upgrade` flag tells `terraform init` to check for newer provider versions within the declared constraints and update the lock file. Plain `terraform init` reuses cached providers when they already satisfy the constraints.
  - Why A is incorrect: `terraform init -upgrade` only affects provider plugin downloads. It does not touch infrastructure resources or the state file.
  - Why C is incorrect: Backend migration requires the `-migrate-state` or `-reconfigure` flag; `-upgrade` has no effect on backend configuration.
  - Why D is incorrect: `terraform init` does not upgrade the Terraform CLI itself. The CLI is updated by downloading a new binary from HashiCorp or using a version manager like `tfenv`.

---

### Question 12 (5 points)

A CI/CD pipeline runs `terraform plan -out=tfplan` and stores the result as a pipeline artifact. A human reviewer approves the artifact. The pipeline then runs `terraform apply tfplan`. Why is this pattern preferred over running `terraform apply -auto-approve` directly?

- A) The saved plan file compresses the configuration to reduce network transfer time during apply.
- B) Applying a saved plan ensures the exact changes reviewed and approved are the ones executed, with no possibility of a re-plan introducing new changes between review and apply.
- C) `terraform apply tfplan` bypasses provider API calls, making the apply phase faster.
- D) The saved plan file contains credentials embedded at plan time, so the apply phase does not require environment variables.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Between a `terraform plan` run and a subsequent `terraform apply` (without a saved plan), cloud state can change — someone else may have applied a different change. A saved plan file locks the exact diff, guaranteeing the apply executes only what was reviewed.
  - Why A is incorrect: The saved plan is a binary file for correctness and security, not for compression purposes. It does not reduce network transfer during apply.
  - Why C is incorrect: `terraform apply tfplan` still makes provider API calls to execute the changes. It skips only the re-plan phase, not the actual API interactions.
  - Why D is incorrect: Saved plan files do not embed credentials. Credentials must still be provided at apply time via environment variables or the provider configuration.

---

### Question 13 (5 points)

Which of the following files should be added to `.gitignore` in a Terraform project?

- A) `main.tf` and `variables.tf`
- B) `.terraform.lock.hcl`
- C) `.terraform/` directory and `terraform.tfstate`
- D) `outputs.tf` and `versions.tf`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The `.terraform/` directory contains downloaded provider binaries (large, platform-specific, reproducible via `init`) and should not be committed. `terraform.tfstate` may contain sensitive values and should not be in version control; use a remote backend instead.
  - Why A is incorrect: `.tf` files are the source code of your configuration and must be committed to version control. They are the entire point of treating infrastructure as code.
  - Why B is incorrect: `.terraform.lock.hcl` should be committed. It pins provider versions for reproducible installs across the team and CI/CD.
  - Why D is incorrect: `outputs.tf` and `versions.tf` are source files that belong in version control just like `main.tf`.

---

### Question 14 (5 points)

In a `terraform plan` output, the `<=` symbol appears next to a block. What does this indicate?

- A) A resource will be destroyed and a new one created with the same configuration.
- B) A data source will be read from the provider during the apply phase.
- C) A resource attribute will decrease in value compared to its current state.
- D) The resource is being moved to a different module address in the state file.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `<=` symbol indicates a data source read. Data sources in Terraform retrieve information from provider APIs without creating or modifying resources. They are read during the plan or apply phase.
  - Why A is incorrect: Destroy-and-recreate is shown with `-/+`. The `<=` symbol has nothing to do with replacement operations.
  - Why C is incorrect: Terraform plan symbols represent resource lifecycle actions, not numerical comparisons of attribute values.
  - Why D is incorrect: Module address moves are handled with `moved` blocks and show differently in plan output. `<=` specifically denotes data source reads.

---

### Question 15 (5 points)

What happens to the `.terraform.lock.hcl` file when you add a new provider to `required_providers` and run `terraform init`?

- A) The existing lock file is deleted and replaced with a new one containing only the new provider.
- B) The new provider's version and checksums are added to the existing lock file while existing entries are preserved.
- C) Terraform prompts you to manually edit the lock file to add the new provider entry.
- D) The lock file is unchanged; it only updates when you run `terraform init -upgrade`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform init` adds new provider entries to the lock file incrementally. Existing locked versions are preserved, and new providers are appended with their selected version and integrity checksums.
  - Why A is incorrect: Deleting existing lock entries would break reproducibility for already-locked providers. Terraform updates the file additively.
  - Why C is incorrect: The lock file is maintained automatically by Terraform. Users should not manually edit it.
  - Why D is incorrect: Plain `terraform init` does update the lock file when new providers are added. `-upgrade` is only needed to update versions for existing providers.

---

### Question 16 (5 points)

You run `terraform apply` without the `-auto-approve` flag. What does Terraform do before making any changes?

- A) It immediately begins creating resources in the order they appear in the configuration file.
- B) It displays the execution plan and requires you to type `yes` to confirm before proceeding.
- C) It sends an approval request email to the team's infrastructure administrator.
- D) It checks whether a saved plan file named `tfplan` exists and uses it automatically if found.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: When run interactively without `-auto-approve`, `terraform apply` re-runs the plan phase, displays the proposed changes, and requires explicit `yes` confirmation before executing any changes. This is a safety gate.
  - Why A is incorrect: Terraform always computes and displays the plan before acting, even in interactive mode. It does not begin changes immediately.
  - Why C is incorrect: Terraform has no built-in email approval workflow. External approval gates are implemented at the CI/CD pipeline level, not within Terraform itself.
  - Why D is incorrect: `terraform apply` does not automatically detect a `tfplan` file. You must explicitly pass the filename: `terraform apply tfplan`.

---

### Question 17 (5 points)

Which version constraint syntax means "any version in the 5.x range, but not 6.0 or higher"?

- A) `>= 5.0, < 5.9`
- B) `= 5.0`
- C) `~> 5.0`
- D) `> 5.0`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The pessimistic constraint operator `~>` with a version like `5.0` means `>= 5.0, < 6.0`. It allows any patch and minor release within the 5.x line but prevents upgrading to 6.0.
  - Why A is incorrect: `>= 5.0, < 5.9` would exclude versions 5.9.x and above within the 5.x range. This is more restrictive than the typical intent of allowing all 5.x versions.
  - Why B is incorrect: `= 5.0` pins to exactly version 5.0.0 and prevents any updates, including security patches in the 5.x line.
  - Why D is incorrect: `> 5.0` allows version 6.0 and beyond, which is wider than intended for a constraint meant to stay within the 5.x major line.

---

### Question 18 (5 points)

A colleague runs `terraform plan` and sees the message: `Error: No configuration files`. What is the most likely cause?

- A) The `terraform.tfstate` file has been deleted.
- B) The `.terraform/` directory is missing because `init` was not run.
- C) Terraform is being run from a directory that contains no `.tf` files.
- D) The provider version specified in `required_providers` does not exist in the registry.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: "No configuration files" means Terraform cannot find any `.tf` files in the current working directory. The most common cause is running the command from the wrong directory.
  - Why A is incorrect: A missing state file does not produce "No configuration files." Terraform would treat all declared resources as new and plan to create them.
  - Why B is incorrect: A missing `.terraform/` directory produces "Required plugins are not installed" or a similar provider initialization error, not "No configuration files."
  - Why D is incorrect: An invalid provider version in the registry produces an error during `terraform init`, not during `terraform plan`, and the message would reference the provider registry lookup failure.

---

### Question 19 (5 points)

What does `terraform show` display when run after a successful `terraform apply`?

- A) The raw JSON contents of the `.terraform.lock.hcl` file.
- B) The human-readable representation of the current state — all managed resources and their current attribute values.
- C) A diff between the previous state and the current state showing only what changed in the last apply.
- D) The list of all Terraform commands available in the current CLI version.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform show` reads `terraform.tfstate` and renders its contents in human-readable form, showing all managed resources and their current attributes. It can also be used to display a saved plan file: `terraform show tfplan`.
  - Why A is incorrect: The lock file is an HCL file, not JSON, and `terraform show` does not display it. The lock file is read directly in your editor.
  - Why C is incorrect: Terraform does not produce a changelog diff of consecutive applies. The state file reflects current state only. History tracking requires external tooling or Terraform Cloud's state versioning feature.
  - Why D is incorrect: Listing available CLI commands is the job of `terraform help` or `terraform -help`, not `terraform show`.

---

### Question 20 (5 points)

After running `terraform destroy`, what state does the `terraform.tfstate` file reflect?

- A) The file is automatically deleted by `terraform destroy`.
- B) The file retains the last-known resource attributes as a backup in case of accidental destruction.
- C) The file's `resources` array is empty, indicating that no resources are currently managed.
- D) The file is renamed to `terraform.tfstate.backup` and a new empty file is created in its place.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: After a successful `terraform destroy`, all resources are removed from cloud infrastructure and the state file is updated to reflect zero managed resources. The file itself remains; only its `resources` array becomes empty.
  - Why A is incorrect: `terraform destroy` does not delete the state file. The file is updated to show an empty resource set, which allows Terraform to be run again in the same directory without reinitializing.
  - Why B is incorrect: The state file is not kept as a backup after destroy; it is updated to reflect the current (empty) state. A `terraform.tfstate.backup` file is created before each apply or destroy to preserve the previous state, but the main file is updated.
  - Why D is incorrect: While Terraform does create a `.backup` file before applying changes, the main `terraform.tfstate` file is updated in place rather than being replaced by an empty new file.

---

Module 02 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
