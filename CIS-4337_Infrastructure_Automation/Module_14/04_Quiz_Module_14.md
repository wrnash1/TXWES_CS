# Quiz: Module 14 - Terraform in CI/CD Pipelines

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which flag must be appended to `terraform apply` in an automated CI/CD pipeline to prevent the command from blocking indefinitely waiting for user confirmation?

* A) `--force`
* B) `-auto-approve`
* C) `--yes`
* D) `-non-interactive`
* **Correct Answer:** B) The `-auto-approve` flag instructs `terraform apply` to skip the interactive confirmation prompt and execute the apply immediately, which is required in pipeline environments where no human is present to type `yes`.
* **Distractor Analysis:**
  * *Why B is correct:* `-auto-approve` is the only documented Terraform flag that suppresses the apply confirmation prompt. Without it, `terraform apply` waits indefinitely for `yes` input that a CI runner cannot provide, causing the pipeline job to hang until it times out.
  * *Why A is incorrect:* `--force` is not a valid `terraform apply` flag. It does not exist in the Terraform CLI. Providing an unrecognized flag causes Terraform to exit with an error.
  * *Why C is incorrect:* `--yes` is not a valid Terraform CLI flag. It is used by some other CLIs (e.g., certain package managers) but is not recognized by Terraform.
  * *Why D is incorrect:* `-non-interactive` is not a valid Terraform CLI flag. The correct flag for suppressing the apply confirmation is exclusively `-auto-approve`.

---

**Question 2**
Which of the following most accurately describes the purpose of the `TF_VAR_` environment variable prefix in a CI/CD pipeline?

* A) A prefix used to mark environment variables as sensitive so that Terraform automatically redacts them from all log output and state files
* B) A convention that tells Terraform to map the environment variable's value to an input variable of the same name, enabling secret injection without `.tfvars` files
* C) A prefix required by cloud providers to identify Terraform-specific credentials and distinguish them from other environment variables in the pipeline runner
* D) A flag that enables Terraform's variable validation rules, requiring the value to match the `validation` block conditions before a plan can proceed
* **Correct Answer:** B) Terraform automatically reads environment variables prefixed with `TF_VAR_` and maps them to input variables. For example, `TF_VAR_db_password=secret` sets the `db_password` input variable without requiring it to appear in any `.tfvars` file.
* **Distractor Analysis:**
  * *Why B is correct:* This is the documented, exam-tested mechanism for passing variable values into Terraform from CI/CD environments. It allows pipeline secrets to flow into Terraform configurations cleanly, keeping credentials out of source-controlled files. The variable must still be declared in the configuration with a `variable` block.
  * *Why A is incorrect:* `TF_VAR_` does not control log redaction. Sensitive value masking in Terraform output is controlled by the `sensitive = true` attribute on `variable` and `output` blocks — not by the environment variable name prefix.
  * *Why C is incorrect:* Cloud provider SDKs have their own environment variable conventions (e.g., `AWS_ACCESS_KEY_ID`, `GOOGLE_CREDENTIALS`). `TF_VAR_` is a Terraform-internal convention for input variable injection and is not recognized by provider SDKs as credential identifiers.
  * *Why D is incorrect:* Variable validation rules are defined with `validation` blocks inside `variable` declarations in HCL. They are evaluated during `terraform plan` regardless of how the variable value was supplied. `TF_VAR_` does not enable or disable validation.

---

**Question 3**
A CI/CD pipeline runs `terraform plan` on every pull request and `terraform apply` on every merge to `main`. During code review, a reviewer wants to see the exact changes Terraform will make. Which approach ensures the apply step executes exactly the plan that was reviewed?

* A) Run `terraform plan` and `terraform apply` as separate pipeline steps with no plan file; Terraform will produce the same result because the configuration has not changed
* B) Run `terraform plan -out=tfplan` to save the plan to a file, store `tfplan` as a pipeline artifact, then run `terraform apply tfplan` in the apply step to execute exactly that saved plan
* C) Run `terraform apply -refresh=false` in the apply step to prevent Terraform from re-evaluating state, ensuring the result matches what was planned
* D) Run `terraform apply -lock=false` to skip state locking, which allows the apply to use the cached plan from the previous `terraform plan` run
* **Correct Answer:** B) Saving the plan with `-out=tfplan` serializes the complete execution plan including state snapshot and proposed changes. Passing that file to `terraform apply` executes only that plan without re-evaluation, guaranteeing the apply matches exactly what was reviewed.
* **Distractor Analysis:**
  * *Why B is correct:* This is the HashiCorp-recommended pipeline pattern. Running plan and apply as separate steps without a plan file means apply re-evaluates state at apply time, which can diverge from the plan if infrastructure changed between the two steps. The saved plan file eliminates this race condition.
  * *Why A is incorrect:* Even if configuration has not changed, state can change between plan and apply due to out-of-band infrastructure modifications. A second plan evaluation is not guaranteed to produce the same diff as the reviewed plan, making this approach unsafe for production pipelines.
  * *Why C is incorrect:* `-refresh=false` skips the state refresh step, meaning Terraform uses potentially stale state data. This can cause applies to miss real-world changes or incorrectly assume resources are in their last-known state. It does not replay a previously computed plan.
  * *Why D is incorrect:* `-lock=false` disables state locking for that operation, creating a concurrency risk. It has nothing to do with using a cached plan. Terraform does not cache plans between invocations unless the `-out` flag was used.

---

**Question 4**
A Terraform pipeline fails at the `terraform validate` step with an error. Which of the following issues would `terraform validate` detect?

* A) An AWS IAM permission error that would prevent Terraform from creating an `aws_s3_bucket` resource at apply time
* B) A reference to an output value of a module that does not exist in that module's `outputs.tf` file
* C) A cost estimate that exceeds the organization's monthly budget threshold for cloud resources
* D) A provider version constraint in `required_providers` that is incompatible with the currently installed provider version
* **Correct Answer:** B) `terraform validate` checks that all references within the configuration are valid — including module output references. If a configuration references `module.networking.vpc_id` but the networking module does not declare a `vpc_id` output, `terraform validate` will report an error.
* **Distractor Analysis:**
  * *Why B is correct:* `terraform validate` performs static analysis of the HCL configuration graph — it checks that all resource, variable, output, and module references resolve to declared entities. It does not make provider API calls, so it catches structural errors like missing output declarations before any network request is made.
  * *Why A is incorrect:* IAM permission errors are runtime failures that occur when provider API calls are made during `terraform plan` or `terraform apply`. `terraform validate` does not make API calls and cannot detect permission issues.
  * *Why C is incorrect:* Cost estimation is not a function of `terraform validate`. Cost analysis requires provider API data and is performed by third-party tools (e.g., Infracost) or Terraform Cloud's cost estimation feature, not the built-in validate command.
  * *Why D is incorrect:* Provider version constraint conflicts are detected during `terraform init`, which resolves and downloads provider versions according to `required_providers` constraints. By the time `terraform validate` runs, providers are already installed and the version check has already passed or failed.

---

**Question 5**
A security engineer reviews a GitHub Actions workflow for Terraform and notices AWS credentials are exported directly in the workflow YAML as `env: AWS_ACCESS_KEY_ID: AKIAIOSFODNN7EXAMPLE`. Why is this a critical security risk, and what is the correct remediation?

* A) The credential format is wrong — AWS access key IDs must be base64-encoded before use in environment variables; encode the value and update the YAML
* B) The plaintext credential is committed to the repository and visible in version control history; store the value in GitHub Actions encrypted secrets and reference it as `${{ secrets.AWS_ACCESS_KEY_ID }}` instead
* C) GitHub Actions does not support the `env` key for setting environment variables; use the `with` key to pass credentials to the Terraform action
* D) The credential should be placed in a `terraform.tfvars` file and committed to the repository so the pipeline can load it with `terraform apply -var-file=terraform.tfvars`
* **Correct Answer:** B) Hardcoding credentials directly in a YAML workflow file commits them to the repository, exposing them to anyone with read access to the repo — including in perpetuity through Git history even if the file is later updated. The correct pattern is to store secrets in GitHub Actions encrypted secrets and reference them with the `${{ secrets.SECRET_NAME }}` syntax.
* **Distractor Analysis:**
  * *Why B is correct:* This is a foundational secrets management principle tested by the exam. GitHub Actions encrypted secrets are encrypted at rest, never appear in logs, and are only exposed to authorized workflow runs. The `${{ secrets.NAME }}` reference is the correct and documented injection pattern.
  * *Why A is incorrect:* AWS access key IDs do not need to be base64-encoded. The format `AKIAIOSFODNN7EXAMPLE` is the correct plaintext format used by all AWS SDKs. Base64-encoding a credential value would cause authentication failures.
  * *Why C is incorrect:* GitHub Actions fully supports the `env` key for setting environment variables on a step or job. The problem is the credential value being hardcoded in plaintext, not the use of the `env` key itself.
  * *Why D is incorrect:* Placing credentials in `terraform.tfvars` and committing it to version control is an equally serious (or worse) security violation. Committed secrets in version control are permanently exposed in repository history. This option describes the exact anti-pattern the question is warning against.
