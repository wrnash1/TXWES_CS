# CIS-4337 Infrastructure Automation

## Quiz — Module 03: HCL Syntax — Providers, Resources, and Variables

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What block type in HCL is used to configure the plugins that interact with cloud platforms such as AWS and Azure?

- A) `resource`
- B) `variable`
- C) `provider`
- D) `output`

Correct Answer: C

Distractor Analysis:

- Why C is correct: The `provider` block configures the plugin that translates HCL resource declarations into API calls for a specific cloud platform. It supplies authentication credentials, regional settings, and other platform-specific options.
- Why A is incorrect: The `resource` block declares specific infrastructure objects managed by a provider. It does not configure how Terraform connects to the platform.
- Why B is incorrect: The `variable` block declares input parameters for the configuration. It has no role in provider plugin configuration.
- Why D is incorrect: The `output` block exposes computed values after apply for display or cross-module use. It does not configure plugins.

---

### Question 2

Which of the following correctly describes the arguments inside a `provider "aws" {}` block?

- A) Arguments that configure how Terraform connects to and authenticates with AWS, such as `region`, `alias`, and credential settings.
- B) The list of required input variables that must be supplied before `terraform apply` can execute.
- C) The set of output values published from a module to the calling root configuration.
- D) The version constraints declared in `required_providers` that prevent incompatible provider upgrades.

Correct Answer: A

Distractor Analysis:

- Why A is correct: Provider block arguments configure the connection to the platform. `region` sets the default region. `alias` allows multiple provider configurations. Credential settings (profile, access key) tell Terraform how to authenticate.
- Why B is incorrect: Required input variables are declared with `variable {}` blocks and supplied via `.tfvars` files or CLI flags.
- Why C is incorrect: Module output values are declared with `output {}` blocks inside a module and referenced via `module.<name>.<output_name>`.
- Why D is incorrect: Version constraints belong in the `required_providers` block inside the `terraform {}` block, not inside the `provider {}` block.

---

### Question 3

Resource B must be created only after resource A is fully created, but resource B does not reference any attribute of resource A. How should this dependency be expressed?

- A) Declare resource A inside the body of resource B's block.
- B) Use the `depends_on` meta-argument inside resource B, referencing resource A.
- C) Run `terraform apply` twice — once targeting resource A, then once targeting resource B.
- D) Place resource A before resource B in the `.tf` file. Terraform reads files in top-to-bottom order.

Correct Answer: B

Distractor Analysis:

- Why B is correct: `depends_on = [resource_type.name]` creates an explicit dependency when no attribute reference (implicit dependency) exists. Terraform will not begin creating resource B until resource A is fully provisioned.
- Why A is incorrect: Nesting resource declarations inside other resource blocks is not valid HCL syntax.
- Why C is incorrect: Terraform resolves dependencies automatically within a single apply. Splitting into multiple runs is unnecessary and introduces fragility.
- Why D is incorrect: Terraform builds a dependency graph from attribute references and `depends_on` declarations. The physical order of blocks in `.tf` files has no effect on execution order.

---

### Question 4

You need a variable that accepts a list of strings representing subnet IDs such as `["subnet-aaa", "subnet-bbb"]`. Which type declaration is correct?

- A) `type = string`
- B) `type = map(string)`
- C) `type = list(string)`
- D) `type = bool`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `list(string)` declares an ordered collection of string values. It accepts `["subnet-aaa", "subnet-bbb"]` and supports index access such as `var.subnet_ids[0]`.
- Why A is incorrect: `type = string` accepts only a single string value, not a collection. Assigning a list to a string variable causes a type error at plan time.
- Why B is incorrect: `map(string)` accepts key-value pairs like `{az1 = "subnet-aaa"}`, not an ordered list. The data structure is fundamentally different.
- Why D is incorrect: `type = bool` accepts only `true` or `false`. It cannot hold string values.

---

### Question 5

Which `lifecycle` argument prevents Terraform from destroying a resource even when `terraform destroy` is explicitly run?

- A) `ignore_changes = [all]`
- B) `create_before_destroy = true`
- C) `prevent_destroy = true`
- D) `depends_on = []`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `lifecycle { prevent_destroy = true }` causes Terraform to raise an error and abort rather than proceeding with deletion. This is the safeguard used for production databases and state buckets that must never be accidentally deleted.
- Why A is incorrect: `ignore_changes` tells Terraform to ignore drift on specified attribute values during plan. It does not prevent the resource from being destroyed.
- Why B is incorrect: `create_before_destroy = true` changes the replacement order so the new resource is created before the old one is deleted. It does not prevent destruction; it only reorders it.
- Why D is incorrect: `depends_on = []` manages execution order. An empty depends_on list has no practical effect and provides no lifecycle protection.

---

### Question 6

What is the correct syntax to reference a local value named `common_tags` inside a resource block?

- A) `var.common_tags`
- B) `self.common_tags`
- C) `local.common_tags`
- D) `module.common_tags`

Correct Answer: C

Distractor Analysis:

- Why C is correct: Local values defined in a `locals {}` block are referenced using the `local.<name>` syntax. They are internal computed values, not module inputs or outputs.
- Why A is incorrect: `var.<name>` references input variables declared with `variable {}` blocks, not local values.
- Why B is incorrect: `self.<attribute>` is available only inside `connection` and `provisioner` blocks to reference the containing resource's own attributes.
- Why D is incorrect: `module.<name>.<output>` references output values from a child module. Local values are not modules.

---

### Question 7

A team uses `count = 3` to create three identical EC2 instances. They later reorder the list so that the former third instance becomes the first. What does Terraform plan to do on the next run?

- A) Nothing — Terraform recognizes the instances are functionally identical and makes no changes.
- B) Update instance tags in place to reflect the new order.
- C) Destroy all three instances and recreate them in the new order.
- D) Destroy the instances at the old indices and recreate resources to fill the new indices, potentially replacing most instances.

Correct Answer: D

Distractor Analysis:

- Why D is correct: `count`-based resources are indexed numerically. When the list is reordered, the mapping between index and resource intent changes, causing Terraform to destroy and recreate resources to match the new index assignments. This is why `for_each` is preferred when resources have meaningful identities.
- Why A is incorrect: Terraform evaluates the configuration against the state. If the desired attributes at each index differ from what is currently deployed at that index, Terraform will plan changes.
- Why B is incorrect: A reordering does not affect only tags. The entire resource at each index is compared to the new desired state at that index.
- Why C is incorrect: Terraform does not necessarily destroy all three. It destroys and recreates the resources whose index mappings changed, which depends on the specific reordering.

---

### Question 8

Which of the following demonstrates the correct way to pass a variable value to Terraform from the command line?

- A) `terraform apply --variable="env=prod"`
- B) `terraform apply -var="environment=prod"`
- C) `terraform apply /var environment=prod`
- D) `terraform apply --set environment=prod`

Correct Answer: B

Distractor Analysis:

- Why B is correct: The `-var="name=value"` flag is the correct CLI syntax for supplying a single variable value. The flag uses a single dash, and the assignment uses `=` inside quotes.
- Why A is incorrect: `--variable` is not a valid Terraform flag. The correct flag is `-var`.
- Why C is incorrect: `/var` is a filesystem path, not a Terraform CLI syntax. This is not a valid flag format.
- Why D is incorrect: `--set` is used in Helm (Kubernetes package manager) syntax, not in Terraform.

---

### Question 9

What does `sensitive = true` do when applied to an `output` block?

- A) It encrypts the value in the Terraform state file using AES-256.
- B) It prevents the value from being displayed in `terraform plan` and `apply` CLI output, but the value is still stored in the state file.
- C) It permanently deletes the value from state after each apply so it cannot be retrieved.
- D) It requires multi-factor authentication before the output value can be read.

Correct Answer: B

Distractor Analysis:

- Why B is correct: `sensitive = true` suppresses display in CLI output, showing `(sensitive value)` instead. The actual value remains in the state file in plain text unless the backend provides encryption at rest. State encryption is a separate concern from the sensitive flag.
- Why A is incorrect: `sensitive = true` does not encrypt the state file. State file encryption is a backend configuration responsibility.
- Why C is incorrect: Sensitive outputs are retained in state across runs. They are not deleted.
- Why D is incorrect: Terraform does not integrate with MFA systems for reading output values.

---

### Question 10

A resource uses `for_each = var.server_names` where `server_names` is a `set(string)`. After apply, how is the second resource instance addressed in Terraform state and in references?

- A) `aws_instance.servers[1]` (zero-indexed, second element)
- B) `aws_instance.servers["<name>"]` where `<name>` is the specific string value from the set
- C) `aws_instance.servers.second`
- D) `aws_instance.servers.1`

Correct Answer: B

Distractor Analysis:

- Why B is correct: Resources created with `for_each` are addressed by their key. When iterating over a `set(string)`, the key for each instance is the string value itself. So an instance for the value `"web-01"` is addressed as `aws_instance.servers["web-01"]`.
- Why A is incorrect: Numeric index addressing applies to `count`-based resources, not `for_each` resources.
- Why C is incorrect: `.second` is not a valid Terraform addressing syntax for any resource type.
- Why D is incorrect: Dot-notation with a number is not valid HCL addressing syntax.

---

---

### Question 11 (5 points)

What is the correct syntax to reference the `id` attribute of the data source `data "aws_ami" "latest" {}` within the same configuration?

- A) `var.aws_ami.latest.id`
- B) `aws_ami.latest.id`
- C) `data.aws_ami.latest.id`
- D) `local.aws_ami.latest.id`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Data sources are referenced with the prefix `data.<type>.<name>.<attribute>`. For a block declared as `data "aws_ami" "latest"`, the `id` attribute is `data.aws_ami.latest.id`.
  - Why A is incorrect: The `var.` prefix is for input variables. Data sources use the `data.` prefix.
  - Why B is incorrect: `aws_ami.latest.id` without the `data.` prefix would imply a managed resource named `latest` of type `aws_ami`. Omitting `data.` causes a reference error.
  - Why D is incorrect: `local.` is used for values defined in a `locals {}` block. Data source references always begin with `data.`.

---

### Question 12 (5 points)

A configuration declares `variable "server_count"` with `type = number` and no `default`. What happens when you run `terraform plan` without supplying a value for this variable?

- A) Terraform uses `0` as the default value for all numeric variables.
- B) Terraform prompts you interactively to enter a value before the plan can proceed.
- C) Terraform skips the plan and writes an empty state file.
- D) Terraform automatically infers the value from the existing state file.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: When a required variable (one with no default) is not supplied via CLI flags, environment variables, or `.tfvars` files, Terraform prompts the user interactively during `plan` or `apply`. In non-interactive CI/CD runs this causes a timeout or error.
  - Why A is incorrect: Terraform does not assign implicit defaults to any type. If no default is declared and no value is supplied, the variable is required and must be provided.
  - Why C is incorrect: Terraform does not skip the plan or write an empty state file for missing variables. It stops execution until the value is provided.
  - Why D is incorrect: Variable values are never inferred from state. The state file records resource attributes, not input variable values.

---

### Question 13 (5 points)

Which meta-argument changes the replacement order so that the new resource is created before the old one is deleted?

- A) `depends_on = []`
- B) `ignore_changes = [all]`
- C) `prevent_destroy = true`
- D) `create_before_destroy = true`

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why D is correct: `lifecycle { create_before_destroy = true }` instructs Terraform to provision the replacement resource first and only destroy the original after the new one is ready. This minimizes downtime for resources that require replacement.
  - Why A is incorrect: `depends_on` manages execution ordering between different resources, not the creation/destruction order of a single resource being replaced.
  - Why B is incorrect: `ignore_changes` suppresses drift detection on listed attributes. It does not affect the order of create/destroy operations.
  - Why C is incorrect: `prevent_destroy = true` blocks deletion entirely; it does not change the order of operations.

---

### Question 14 (5 points)

You define a variable with `type = map(string)` and supply the value `{ region_a = "us-east-1", region_b = "us-west-2" }`. How do you access the value for `region_b` inside a resource block?

- A) `var.regions[1]`
- B) `var.regions.region_b`
- C) `var.regions["region_b"]`
- D) `lookup(region_b, var.regions)`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Map values in Terraform are accessed using bracket notation with the key as a string: `var.<name>["<key>"]`. This is the standard HCL syntax for map lookups.
  - Why A is incorrect: Numeric index access applies to list and tuple types, not maps. Maps use string keys.
  - Why B is incorrect: Dot notation for map key access is not valid in Terraform HCL. Only the bracket notation `["key"]` works for map lookups.
  - Why D is incorrect: The `lookup` function signature is `lookup(map, key, default)`. The argument order is reversed in this option, making it incorrect.

---

### Question 15 (5 points)

What is the purpose of the `validation` block inside a `variable` declaration?

- A) It automatically corrects invalid values to the nearest valid value before running the plan.
- B) It enforces a condition that the supplied value must satisfy, causing an error with a custom message if the condition fails.
- C) It validates that all provider API calls referencing this variable will succeed.
- D) It encrypts the variable value before storing it in the state file.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `validation` block contains a `condition` expression and an `error_message`. If the condition evaluates to `false` for the supplied value, Terraform produces an error with the specified message before any plan or apply proceeds.
  - Why A is incorrect: Terraform never silently modifies or corrects supplied variable values. If a value fails validation, the run aborts with an error.
  - Why C is incorrect: Validation blocks run entirely locally before any provider API calls. They cannot verify that a value is valid against a remote provider's constraints.
  - Why D is incorrect: Variable validation has no encryption function. Sensitive values are protected using `sensitive = true`, not through validation blocks.

---

### Question 16 (5 points)

A `locals` block defines `env_prefix = "${var.environment}-${var.region}"`. How is this local value referenced in a resource tag attribute?

- A) `var.env_prefix`
- B) `self.env_prefix`
- C) `local.env_prefix`
- D) `module.env_prefix`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Local values defined in a `locals {}` block are always referenced with the `local.<name>` syntax. This is distinct from input variables (`var.`), module outputs (`module.`), and the `self` reference available only inside provisioner blocks.
  - Why A is incorrect: `var.env_prefix` would look for an input variable named `env_prefix`. Local values and input variables are separate namespaces in HCL.
  - Why B is incorrect: `self` is only available inside `connection` and `provisioner` blocks to reference the containing resource's own computed attributes.
  - Why D is incorrect: `module.<name>.<output>` references output values exported from child modules, not locally computed expressions.

---

### Question 17 (5 points)

You have a `for_each` resource keyed on `set(string)` with values `{"api", "web", "db"}`. Which of the following correctly expresses the resource address for the `web` instance?

- A) `aws_instance.servers[1]`
- B) `aws_instance.servers.web`
- C) `aws_instance.servers["web"]`
- D) `aws_instance.servers.1`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `for_each` resources use the map or set key as their instance identifier. The resource address for the `web` instance is `aws_instance.servers["web"]` with the key in quotes inside square brackets.
  - Why A is incorrect: Numeric indexing applies to `count`-based resources. `for_each` uses string key addressing.
  - Why B is incorrect: Dot notation with a string (`.web`) is not valid HCL for `for_each` instance addressing. The bracket notation `["web"]` is required.
  - Why D is incorrect: `.1` is not valid addressing syntax for any Terraform resource type.

---

### Question 18 (5 points)

Which of the following is true about the `provider` block's `alias` argument?

- A) It renames the provider globally so all resources must use the new name.
- B) It creates an additional named provider configuration, allowing resources to select a non-default configuration using `provider = <type>.<alias>`.
- C) It sets the provider's authentication alias in the cloud platform's IAM system.
- D) It is required for every provider block; provider blocks without an alias are invalid.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: When a `provider` block includes `alias = "west"`, it creates a secondary named configuration. Resources that should use this configuration explicitly declare `provider = aws.west`. The unaliased provider block remains the default for all other resources.
  - Why A is incorrect: An alias does not rename the provider. It creates an additional configuration alongside the default one.
  - Why C is incorrect: The alias is a Terraform-internal label for selecting between multiple provider configurations. It has no effect on the cloud platform's IAM system.
  - Why D is incorrect: The `alias` argument is optional. Most configurations have a single unaliased provider block. Aliases are only needed for multi-region or multi-account configurations.

---

### Question 19 (5 points)

What is the difference between `type = list(string)` and `type = set(string)` in a variable declaration?

- A) Lists allow duplicate values and maintain insertion order; sets do not allow duplicates and do not guarantee order.
- B) Lists are key-value collections; sets are ordered indexed collections.
- C) Sets can contain mixed types; lists require all elements to be the same type.
- D) There is no functional difference — both accept the same inputs and produce identical outputs.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: A `list` preserves order and allows duplicate elements. A `set` automatically removes duplicates and does not guarantee a specific iteration order. This distinction matters when using `for_each`, which requires a set or map to ensure stable keys.
  - Why B is incorrect: Key-value collections are `map` types. Both lists and sets are simple value collections, not key-value structures.
  - Why C is incorrect: Both `list` and `set` can be parameterized with a type (e.g., `list(any)`), but the mixed-type capability is the same for both. The key difference is ordering and uniqueness, not type flexibility.
  - Why D is incorrect: The two types behave differently in terms of ordering, deduplication, and how Terraform uses them. For example, `for_each` accepts sets and maps but not lists directly.

---

### Question 20 (5 points)

When using the `ignore_changes` lifecycle argument, what does `ignore_changes = [tags]` tell Terraform?

- A) Delete the resource if its `tags` attribute changes and recreate it with the declared tags.
- B) Do not update the `tags` attribute during plan and apply even if the live resource's tags differ from what is declared in HCL.
- C) Permanently remove the `tags` attribute from the resource and the state file.
- D) Make the `tags` attribute read-only so users cannot modify it via CLI variables.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `ignore_changes = [tags]` tells Terraform to accept whatever the current value of `tags` is on the live resource and not plan any changes to bring it in line with the HCL declaration. This is commonly used when tags are managed by an external system or when tag drift should be tolerated.
  - Why A is incorrect: `ignore_changes` suppresses change detection; it does not trigger recreation. The destroy-and-recreate pattern is `create_before_destroy` or forced replacement, not `ignore_changes`.
  - Why C is incorrect: `ignore_changes` does not remove attributes from the resource or the state file. The attribute remains in state; Terraform simply ignores differences to it during plan.
  - Why D is incorrect: `ignore_changes` affects Terraform's reconciliation behavior, not the accessibility of variables or CLI flags.

---

Module 03 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
