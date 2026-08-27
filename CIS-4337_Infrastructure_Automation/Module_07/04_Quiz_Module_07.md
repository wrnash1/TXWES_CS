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

---

### Question 11 (5 points)

Which of the following is a valid `validation` block condition for a variable `var.cidr_block` that must be a /16, /24, or /28 prefix?

A. `var.cidr_block == "/16" || var.cidr_block == "/24" || var.cidr_block == "/28"`
B. `contains(["/16", "/24", "/28"], regex("/(\\d+)$", var.cidr_block)[0])`
C. `can(regex("^10\\.\\d+\\.\\d+\\.\\d+/(16|24|28)$", var.cidr_block))`
D. `type(var.cidr_block) == "cidr"`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `can(regex(...))` returns `true` if the regex matches and `false` if it fails — making it safe to use in a validation condition. The pattern anchors the string and allows only the specified prefix lengths.
  - Why A is incorrect: Comparing the variable to bare strings like `"/16"` would never match because `var.cidr_block` is a full CIDR string like `"10.0.0.0/16"`, not just the prefix length.
  - Why B is incorrect: The `regex()` function returns a string, not a list, when using a single capture group. This syntax is incorrect and would produce an error.
  - Why D is incorrect: Terraform does not have a `cidr` type. The type system only includes `string`, `number`, `bool`, and collection types.

---

### Question 12 (5 points)

A `variable "tags"` is declared with `type = map(string)`. A caller supplies `tags = { Name = "web", Env = "prod" }`. Which expression correctly adds a third tag `ManagedBy = "terraform"` to the merged set without modifying the input variable?

A. `var.tags["ManagedBy"] = "terraform"`
B. `var.tags + { ManagedBy = "terraform" }`
C. `merge(var.tags, { ManagedBy = "terraform" })`
D. `concat(var.tags, { ManagedBy = "terraform" })`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `merge()` combines two or more maps, with later arguments taking precedence for duplicate keys. This is the standard pattern for adding default tags to a caller-supplied tag map.
  - Why A is incorrect: HCL does not support mutable assignment of map values. Variable values are immutable once set. This is also not valid HCL syntax.
  - Why B is incorrect: The `+` operator is not supported for maps in Terraform. It is used for numeric addition.
  - Why D is incorrect: `concat()` operates on lists, not maps. Passing a map to `concat()` produces a type error.

---

### Question 13 (5 points)

What is the correct output command to extract just the raw value of an output named `db_endpoint` so it can be captured into a shell variable without surrounding quotes?

A. `terraform output db_endpoint`
B. `terraform output -json db_endpoint`
C. `terraform output -raw db_endpoint`
D. `terraform output --plain db_endpoint`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `terraform output -raw <name>` prints the value with no surrounding quotation marks, making it suitable for direct capture by shell command substitution: `ENDPOINT=$(terraform output -raw db_endpoint)`.
  - Why A is incorrect: `terraform output db_endpoint` prints the value with surrounding quotes for string types, which would include the quotes in the shell variable.
  - Why B is incorrect: `-json` outputs a JSON structure, which includes the value type and quotes. It requires further parsing (e.g., with `jq`) to extract a raw string.
  - Why D is incorrect: `--plain` is not a valid `terraform output` flag.

---

### Question 14 (5 points)

A variable is declared with `nullable = false`. What happens if a caller explicitly passes `null` for this variable?

A. Terraform silently converts `null` to the variable's `default` value.
B. Terraform ignores the `null` and uses an empty string.
C. Terraform produces an error because `null` is not allowed when `nullable = false`.
D. Terraform accepts `null` and treats it as `false` for boolean variables or `0` for numeric variables.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `nullable = false` prevents a variable from being set to `null`. If a caller attempts to pass `null`, Terraform produces a validation error. This is used when a module requires a non-null value to function correctly.
  - Why A is incorrect: Terraform does not automatically substitute the `default` value when `nullable = false` is violated. It raises an error instead.
  - Why B is incorrect: Terraform does not silently coerce `null` to an empty string. Type coercion in Terraform is explicit, and `null` is never treated as an empty string.
  - Why D is incorrect: Terraform does not perform type-specific coercions for `null`. The `nullable = false` constraint simply rejects any `null` value.

---

### Question 15 (5 points)

A `locals` block defines `is_prod = var.environment == "prod"`. Which conditional expression correctly selects `"t3.large"` for production and `"t3.micro"` for all other environments?

A. `if local.is_prod then "t3.large" else "t3.micro"`
B. `local.is_prod == true ? "t3.large" : "t3.micro"`
C. `local.is_prod ? "t3.large" : "t3.micro"`
D. `select(local.is_prod, "t3.large", "t3.micro")`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The HCL ternary operator `condition ? true_value : false_value` is the correct syntax. `local.is_prod` evaluates to a boolean, so it can be used directly as the condition.
  - Why A is incorrect: `if/then/else` is not valid HCL expression syntax. HCL uses the ternary operator for conditional expressions.
  - Why B is incorrect: While `local.is_prod == true` is technically valid (it evaluates to the same boolean), the explicit `== true` comparison is redundant and unnecessarily verbose. Answer C is more correct and canonical.
  - Why D is incorrect: `select()` is not a Terraform built-in function. The ternary operator handles conditional selection.

---

### Question 16 (5 points)

You need to pass a list of strings `["10.0.1.0/24", "10.0.2.0/24"]` as a variable value from the command line. Which syntax is correct?

A. `terraform plan -var="subnets=10.0.1.0/24,10.0.2.0/24"`
B. `terraform plan -var='subnets=["10.0.1.0/24","10.0.2.0/24"]'`
C. `terraform plan -var="subnets=[10.0.1.0/24, 10.0.2.0/24]"`
D. `terraform plan -var-list="subnets=10.0.1.0/24,10.0.2.0/24"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: When passing a list value using the `-var` flag, the value must be valid HCL or JSON. `'["10.0.1.0/24","10.0.2.0/24"]'` is a valid JSON array. Single quotes in the shell prevent the inner double quotes from being interpreted by the shell.
  - Why A is incorrect: A bare comma-separated string is not interpreted as a list — it would be treated as a single string value and would fail the `list(string)` type constraint.
  - Why C is incorrect: The strings in the list must be quoted. Without quotes around the CIDR values, Terraform cannot parse them as string values.
  - Why D is incorrect: `-var-list` is not a valid Terraform CLI flag.

---

### Question 17 (5 points)

What is the result of declaring two `locals` blocks in the same Terraform configuration, each defining a different local name?

A. Terraform errors because only one `locals` block is allowed per configuration.
B. Both blocks are valid. Terraform merges all `locals` blocks together into a single namespace.
C. The second `locals` block overrides all local values defined in the first block.
D. Each `locals` block creates a separate local namespace, accessed with different prefixes.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: A Terraform configuration can contain multiple `locals` blocks. All local values from all `locals` blocks are merged into one namespace and accessed uniformly with `local.<name>`. The only restriction is that the same name cannot be defined in two different `locals` blocks.
  - Why A is incorrect: Multiple `locals` blocks are explicitly supported. This is a common pattern for organizing groups of related local values across different files.
  - Why C is incorrect: The second block does not override the first. If the same name appears in two blocks, Terraform raises a duplicate definition error.
  - Why D is incorrect: All local values share a single `local.` namespace regardless of which `locals` block they are defined in.

---

### Question 18 (5 points)

Which statement about the `output` block's `depends_on` argument is correct?

A. `depends_on` in an output block causes the output value to be computed only after the listed resources are applied.
B. `depends_on` in an output block prevents the output from being shown until the entire apply completes.
C. `depends_on` is not a valid argument in `output` blocks — it is only valid in `resource` and `data` blocks.
D. `depends_on` in an output block forces the output to be re-evaluated on every plan regardless of state.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: The `depends_on` argument in an `output` block creates an explicit dependency, ensuring the listed resources are fully applied before the output value is computed and displayed. This is used when an output value does not directly reference a resource attribute but relies on side effects of that resource.
  - Why B is incorrect: All outputs are shown after apply completes. `depends_on` affects the ordering of evaluation, not the timing of display.
  - Why C is incorrect: `depends_on` is valid in `output` blocks as well as `resource` and `data` blocks. Terraform added this support to handle indirect output dependencies.
  - Why D is incorrect: `depends_on` has no effect on the plan frequency. Output re-evaluation is driven by changes to the values the output references.

---

### Question 19 (5 points)

A team has a variable `region` with default `"us-east-1"` in the `variable` block, `"us-west-2"` in `terraform.tfvars`, and `"eu-west-1"` in a `production.auto.tfvars` file. No CLI flags are used. Which value does Terraform use?

A. `"us-east-1"` from the default
B. `"us-west-2"` from `terraform.tfvars`
C. `"eu-west-1"` from `production.auto.tfvars`
D. Terraform errors because the variable is defined in multiple sources

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `*.auto.tfvars` files have higher precedence than `terraform.tfvars`. When both are present, the auto-loading `.auto.tfvars` value wins. The precedence order (low to high) is: default → `terraform.tfvars` → `*.auto.tfvars` → `-var-file` → `-var` → `TF_VAR_`.
  - Why A is incorrect: The default is the lowest-precedence source. Any external source overrides it.
  - Why B is incorrect: `terraform.tfvars` is overridden by `*.auto.tfvars` files.
  - Why D is incorrect: Terraform does not error when a variable is set in multiple sources. It resolves the conflict deterministically using the precedence order.

---

### Question 20 (5 points)

What is the purpose of the `can()` function when used inside a variable `validation` block condition?

A. It cancels the current apply if the condition is false.
B. It wraps an expression that might produce an error and returns `true` if it succeeds or `false` if it fails, preventing the condition from throwing an error.
C. It checks whether a variable has been declared in the current module scope.
D. It enables cancellation of long-running provider API calls during validation.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `can(expression)` evaluates the expression and returns `true` if it evaluates without error, or `false` if evaluation produces any error. This is essential in validation blocks where functions like `regex()` throw errors on non-matching input rather than returning a falsy value — wrapping them in `can()` makes them safe to use as boolean conditions.
  - Why A is incorrect: `can()` does not cancel or abort any operation. It is purely an error-trapping boolean expression evaluator.
  - Why C is incorrect: Checking whether a variable exists in scope is not a runtime function. `can()` evaluates arbitrary expressions for success or failure.
  - Why D is incorrect: `can()` has no interaction with provider API calls or I/O operations. It operates on pure HCL expression evaluation.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
