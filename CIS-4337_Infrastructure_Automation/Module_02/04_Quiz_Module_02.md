# Quiz: Module 02 - Terraform Workflow
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which command downloads and installs the provider plugins defined in your Terraform configuration files?
*   A) terraform apply
*   B) terraform init
*   C) terraform plan
*   D) terraform get
*   **Correct Answer:** B) `terraform init` initializes the working directory, downloads required provider plugins into `.terraform/providers/`, and sets up the backend.
*   **Distractor Analysis:**
    *   *Why B is correct:* `terraform init` is always the first command run in a new or cloned Terraform project; it resolves and downloads all provider and module dependencies.
    *   *Why A is incorrect:* `terraform apply` executes the planned changes to create or modify infrastructure; it does not download providers.
    *   *Why C is incorrect:* `terraform plan` generates an execution plan showing proposed changes; it requires providers to already be downloaded by `init`.
    *   *Why D is incorrect:* `terraform get` downloads only modules, not providers, and is rarely used directly since `init` handles both.

---

**Question 2**
Which of the following is the most accurate definition of **HCL (HashiCorp Configuration Language)** in the context of Terraform?
*   A) A proprietary binary compilation format that Terraform uses to cache provider API responses for faster re-runs
*   B) A human-readable, declarative language used to write Terraform configuration files that describe desired infrastructure state using blocks and attribute-value pairs
*   C) A runtime scripting language embedded in Terraform that executes imperative shell commands against cloud provider APIs
*   D) A JSON schema specification that validates the structure of `terraform.tfstate` files before each apply operation
*   **Correct Answer:** B) HCL is the language of `.tf` files — it is declarative, human-readable, and expresses the desired end-state of infrastructure rather than procedural steps.
*   **Distractor Analysis:**
    *   *Why B is correct:* HCL is the defining syntax of Terraform configurations. Understanding its block types (`resource`, `provider`, `variable`, `output`) is heavily tested on the Associate exam.
    *   *Why A is incorrect:* HCL is a text-based configuration language, not a binary cache format.
    *   *Why C is incorrect:* HCL is declarative, not a runtime scripting language. `local-exec` provisioners can run shell commands, but that is not what HCL itself is.
    *   *Why D is incorrect:* HCL is not a JSON schema and does not validate state files; it is the language for writing configuration, not validating state.

---

**Question 3**
You run `terraform plan` and see a resource annotated with `-/+` in the output. What does this symbol mean?
*   A) The resource will be updated in-place with no downtime
*   B) The resource will be destroyed and then recreated (forced replacement)
*   C) The resource is being imported from existing infrastructure
*   D) The resource has no changes and will be left untouched
*   **Correct Answer:** B) The `-/+` symbol means the resource must be destroyed and recreated because one of its attributes cannot be updated in-place — it forces replacement.
*   **Distractor Analysis:**
    *   *Why B is correct:* Many cloud resource attributes are immutable after creation (e.g., an EC2 instance's AMI). When such an attribute changes, Terraform must destroy the old resource and create a new one. This is a critical distinction for the exam.
    *   *Why A is incorrect:* In-place updates are shown with `~` (tilde), not `-/+`.
    *   *Why C is incorrect:* Import operations use `terraform import` and do not appear as `-/+` in a plan.
    *   *Why D is incorrect:* Resources with no changes are shown as no symbol or listed as "No changes" in the plan summary.

---

**Question 4**
In a Terraform project using a remote backend, what happens when `terraform init` is run again after a team member adds a new provider to `main.tf`?
*   A) The new provider is automatically installed without any re-initialization needed
*   B) `terraform init` downloads the new provider plugin and updates the `.terraform.lock.hcl` dependency lock file
*   C) Terraform deletes the existing state file and starts fresh
*   D) `terraform init` replaces the backend configuration and migrates all existing state to the new provider
*   **Correct Answer:** B) Re-running `terraform init` after adding a new provider downloads the missing plugin and updates the lock file with the new provider's version hash.
*   **Distractor Analysis:**
    *   *Why B is correct:* `init` is designed to be run whenever the configuration changes. It is safe and idempotent — it only adds what is missing. The `.terraform.lock.hcl` file records provider version hashes for reproducible installs.
    *   *Why A is incorrect:* New providers are NOT automatically downloaded; you must explicitly run `terraform init` to fetch them.
    *   *Why C is incorrect:* `terraform init` never modifies or deletes the state file under any circumstances.
    *   *Why D is incorrect:* `init` does not replace backend configurations or migrate state automatically; backend migration requires explicit confirmation via the `-migrate-state` flag.

---

**Question 5**
When designing an automated CI/CD pipeline for Terraform deployments, which workflow sequence ensures the exact plan reviewed by an engineer is the one applied in production?
*   A) Run `terraform apply -auto-approve` directly, skipping the plan step to save pipeline execution time
*   B) Run `terraform validate` only; if it passes, the pipeline automatically applies all changes
*   C) Run `terraform plan -out=tfplan`, have the plan reviewed and approved, then run `terraform apply tfplan` to execute the saved plan exactly
*   D) Run `terraform destroy` followed immediately by `terraform apply` to ensure a clean environment on every deployment
*   **Correct Answer:** C) Saving the plan with `-out=tfplan` and then applying the saved file ensures no configuration changes can slip in between the review and execution steps.
*   **Distractor Analysis:**
    *   *Why C is correct:* This is the HashiCorp-recommended pipeline pattern. The saved plan file is a binary artifact that captures the exact changes; `apply tfplan` executes those changes without re-planning, preventing race conditions.
    *   *Why A is incorrect:* Skipping the plan review removes human oversight over what changes will be applied to production, which is a significant risk.
    *   *Why B is incorrect:* `terraform validate` only checks HCL syntax and configuration structure; it does not verify what infrastructure changes will be made.
    *   *Why D is incorrect:* Destroying and re-applying on every deployment causes unnecessary downtime and data loss risks for stateful resources.
