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

Module 03 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
