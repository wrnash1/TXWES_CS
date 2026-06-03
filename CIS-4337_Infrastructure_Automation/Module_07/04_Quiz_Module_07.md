# Quiz: Module 07 — Terraform Variables, Outputs, and Locals

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

**Instructions**: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A Terraform variable is declared with `sensitive = true`. What is the effect of this setting?

A. The value is encrypted in the `terraform.tfstate` file.
B. The value is excluded from the state file entirely.
C. The value is redacted from console and plan output but is still stored in plain text in state.
D. Terraform refuses to accept the value unless it is passed via a `TF_VAR_` environment variable.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `sensitive = true` only affects display; it does not encrypt the state file.
- B is incorrect — sensitive values are always written to state; they must be stored to allow planning and apply.
- D is incorrect — sensitive variables can be passed by any valid mechanism; there is no restriction on how they are supplied.

---

### Question 2

You have the following sources all setting the same Terraform variable `region`. Which value does Terraform use?

- `terraform.tfvars` contains `region = "us-west-2"`
- Environment variable `TF_VAR_region=eu-west-1`
- CLI flag `-var="region=ap-southeast-1"`

A. `us-west-2` from `terraform.tfvars`
B. `eu-west-1` from the environment variable
C. `ap-southeast-1` from the CLI flag
D. Terraform errors because the variable is set in multiple sources

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `terraform.tfvars` has the lowest precedence of the three sources listed.
- B is incorrect — `TF_VAR_` has high precedence but the `-var` CLI flag is higher still.
- D is incorrect — Terraform does not error; it resolves conflicts using the defined precedence order.

---

### Question 3

Which of the following file names does Terraform auto-load without any explicit flags? (Choose all that apply — select the answer that lists ALL correct options.)

A. `variables.tfvars` and `terraform.tfvars`
B. `terraform.tfvars` and `production.auto.tfvars`
C. `terraform.tfvars`, `terraform.tfvars.json`, and `my-vars.tfvars`
D. Only `terraform.tfvars`

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — `variables.tfvars` is not auto-loaded; only `terraform.tfvars` and `*.auto.tfvars` patterns are.
- C is incorrect — `my-vars.tfvars` does not match the auto-load pattern (it does not end in `.auto.tfvars`).
- D is incorrect — `terraform.tfvars.json` and `*.auto.tfvars` files are also auto-loaded.

---

### Question 4

What is the correct syntax to reference a local value named `name_prefix` inside a resource block?

A. `var.name_prefix`
B. `locals.name_prefix`
C. `local.name_prefix`
D. `${name_prefix}`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `var.` is the prefix for input variables, not local values.
- B is incorrect — `locals` (plural) is used in the block declaration; the reference syntax uses the singular `local.`.
- D is incorrect — bare expressions without a namespace prefix are invalid in Terraform outside of string template interpolation, and even there you must include the prefix.

---

### Question 5

A developer wants to ensure that a variable named `instance_type` only accepts `t3.micro`, `t3.small`, or `t3.medium`. Which approach correctly enforces this constraint?

A. Use `type = set(string)` with `default = ["t3.micro", "t3.small", "t3.medium"]`
B. Add a `validation` block with `condition = contains(["t3.micro", "t3.small", "t3.medium"], var.instance_type)`
C. Set `type = enum("t3.micro", "t3.small", "t3.medium")` — Terraform supports enum types
D. Use a `precondition` block inside the variable declaration

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — setting a default to a set of values does not restrict what the caller can pass in.
- C is incorrect — Terraform does not have an `enum` type; this syntax would cause a parse error.
- D is incorrect — `precondition` blocks belong to `resource` and `output` lifecycle blocks, not `variable` declarations.

---

### Question 6

You run `terraform output -raw website_url`. What is the difference between this command and `terraform output website_url`?

A. `-raw` forces a refresh of the state before displaying the output.
B. `-raw` prints the string value without surrounding quotation marks, suitable for shell script consumption.
C. `-raw` shows the output even if it is marked sensitive.
D. `-raw` outputs the value in JSON format.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — `-raw` does not trigger a state refresh; use `terraform refresh` or `terraform apply -refresh-only` for that.
- C is incorrect — `-raw` does not bypass the sensitive flag; sensitive outputs still require `-json` with `jq` to extract, and even then the sensitivity warning is shown.
- D is incorrect — `-json` produces JSON output, not `-raw`.

---

### Question 7

Which of the following statements accurately describes the difference between input variables and local values?

A. Local values can be overridden by the caller; input variables cannot.
B. Input variables accept values from the caller; local values are computed internally and cannot be overridden by the caller.
C. Local values support `sensitive = true`; input variables do not.
D. Input variables are evaluated before local values, but both can reference each other freely.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — this reverses the relationship; input variables are overridden by the caller, and locals are not.
- C is incorrect — `sensitive = true` is a valid argument on input variables; local values do not have a `sensitive` argument (though they inherit sensitivity from the values they reference).
- D is incorrect — local values can reference variables, but there is no free circular reference; Terraform evaluates the dependency graph and detects cycles.

---

### Question 8

What happens if a required variable (no `default`) is not provided by any source when running `terraform plan`?

A. Terraform uses an empty string for string variables and zero for number variables.
B. Terraform prints a warning but proceeds with the plan.
C. Terraform interactively prompts the user to enter the value in the terminal.
D. Terraform immediately errors out without prompting.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — Terraform does not assume a zero-value; it requires explicit input.
- B is incorrect — Terraform does not silently continue; a missing required variable is a blocking issue.
- D is incorrect — when running interactively (not in CI), Terraform prompts the user for the missing value rather than immediately erroring. When stdin is not a TTY (CI mode), it does error.

---

### Question 9

A team stores all resource tags in a `locals` block so that every resource gets consistent tagging. The tag set references `var.environment` and `var.project`. A new team member wants to add a custom tag for their resources only. What is the correct approach?

A. Override the `locals` block in a new `.tf` file with a different `common_tags` local.
B. Use `merge(local.common_tags, { Owner = "alice" })` directly in the resource's `tags` argument.
C. Set a new environment variable to override the local value.
D. Create a new variable named `common_tags` to replace the local value.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — Terraform does not allow two `locals` blocks to define the same name; it would throw a duplicate error.
- C is incorrect — environment variables map only to `variable` declarations (`TF_VAR_` prefix), not to `locals`.
- D is incorrect — creating a variable named `common_tags` would be a different reference path (`var.common_tags`) and would not replace the local; it would also require callers to always supply it.

---

### Question 10

A CI/CD pipeline needs to pass a database password to Terraform without storing it in any file. Which method achieves this most securely?

A. Add the password to `terraform.tfvars` and add that file to `.gitignore`.
B. Hardcode the password in a `locals` block.
C. Export `TF_VAR_db_password` from the pipeline's secrets manager before running Terraform.
D. Pass the password using `-var="db_password=..."` in the pipeline script stored in version control.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — even with `.gitignore`, the file exists on disk and may be captured in build artifacts or logs; it is less secure than an in-memory environment variable.
- B is incorrect — hardcoding secrets in any Terraform file is a critical security violation; locals are evaluated and stored in state.
- D is incorrect — if the pipeline script containing the literal password is stored in version control, the secret is exposed to anyone with repository access.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
