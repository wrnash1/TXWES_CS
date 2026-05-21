# Quiz: Module 03 - HCL Syntax – Providers, Resources, and Variables
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What block type in HCL is used to configure plugins that interact with cloud platforms (e.g., AWS, Azure)?
*   A) resource
*   B) variable
*   C) provider
*   D) output
*   **Correct Answer:** C) The `provider` block configures the plugin that translates HCL resource declarations into API calls for a specific cloud platform.
*   **Distractor Analysis:**
    *   *Why C is correct:* Each cloud platform requires a provider plugin; the `provider` block is where you supply authentication credentials, region, and other platform-specific settings.
    *   *Why A is incorrect:* The `resource` block declares specific infrastructure objects (like a VM or S3 bucket) managed by the provider — it does not configure the provider itself.
    *   *Why B is incorrect:* The `variable` block declares input parameters for the configuration; it has nothing to do with provider plugin setup.
    *   *Why D is incorrect:* The `output` block exposes values after apply for display or cross-module reference; it does not configure plugins.

---

**Question 2**
Which of the following is the most accurate definition of **provider block parameters** in Terraform?
*   A) The arguments declared inside a `provider {}` block that configure how Terraform connects to and authenticates with a specific cloud platform, such as `region`, `alias`, and credential settings
*   B) The list of required input variables that must be supplied before `terraform apply` can execute
*   C) The set of output values published from a module that can be consumed by the calling root configuration
*   D) The version constraints declared in the `required_providers` block that prevent incompatible provider upgrades
*   **Correct Answer:** A) Provider block parameters are the configuration arguments inside the `provider {}` block — they tell Terraform how to connect to and authenticate with the target platform.
*   **Distractor Analysis:**
    *   *Why A is correct:* Parameters like `region = "us-east-1"` inside `provider "aws" {}` are provider block parameters. The `alias` parameter enables multiple configurations of the same provider for multi-region deployments.
    *   *Why B is incorrect:* Required input variables are declared with `variable {}` blocks and supplied via `.tfvars` files or environment variables, not in the provider block.
    *   *Why C is incorrect:* Module outputs are declared with `output {}` blocks inside the module and referenced via `module.<name>.<output>` in the caller.
    *   *Why D is incorrect:* Version constraints live in the `required_providers` block inside `terraform {}`, not inside the `provider {}` block (that location is deprecated).

---

**Question 3**
A Terraform configuration creates resource B, which must exist only after resource A is fully created, but resource B does not reference any attribute of resource A. How should this dependency be expressed?
*   A) By declaring resource A inside the resource B block body
*   B) Using the `depends_on` meta-argument inside resource B's block, referencing resource A
*   C) By running `terraform apply` twice — once for A and once for B
*   D) By placing resource A before resource B in the `.tf` file; Terraform reads files top-to-bottom
*   **Correct Answer:** B) The `depends_on` meta-argument creates an explicit dependency when no implicit reference exists. Terraform will not create B until A is fully provisioned.
*   **Distractor Analysis:**
    *   *Why B is correct:* When resource B does not reference any attribute of resource A (no implicit dependency), `depends_on = [resource_type.name]` inside B's block explicitly instructs Terraform to serialize their creation.
    *   *Why A is incorrect:* Nesting resource declarations inside other resource blocks is not valid HCL syntax.
    *   *Why C is incorrect:* Terraform manages dependencies automatically within a single apply; splitting into multiple runs is unnecessary and fragile.
    *   *Why D is incorrect:* Terraform builds a dependency graph regardless of file order; the physical order of blocks in `.tf` files has no effect on execution order.

---

**Question 4**
You need a Terraform variable that accepts a list of strings representing subnet IDs (e.g., `["subnet-aaa", "subnet-bbb"]`). Which type declaration is correct?
*   A) `type = string`
*   B) `type = map(string)`
*   C) `type = list(string)`
*   D) `type = bool`
*   **Correct Answer:** C) `list(string)` declares an ordered collection of string values, which is the correct type for a set of subnet IDs that may be iterated with `for_each` or indexed.
*   **Distractor Analysis:**
    *   *Why C is correct:* `list(string)` accepts `["subnet-aaa", "subnet-bbb"]` and allows index-based access via `var.subnet_ids[0]`. This is a common exam pattern.
    *   *Why A is incorrect:* `type = string` accepts only a single string value, not a collection. Passing a list to a string variable causes a type error.
    *   *Why B is incorrect:* `map(string)` accepts key-value pairs like `{az1 = "subnet-aaa", az2 = "subnet-bbb"}`, not a plain list. The structure is different.
    *   *Why D is incorrect:* `type = bool` accepts only `true` or `false` and cannot hold subnet ID strings.

---

**Question 5**
Which resource meta-argument prevents Terraform from destroying a resource even when `terraform destroy` is explicitly run?
*   A) `ignore_changes = [all]`
*   B) `create_before_destroy = true`
*   C) `prevent_destroy = true`
*   D) `depends_on = []`
*   **Correct Answer:** C) The `lifecycle { prevent_destroy = true }` setting causes Terraform to raise an error and abort rather than proceed with destroying the protected resource.
*   **Distractor Analysis:**
    *   *Why C is correct:* `prevent_destroy = true` inside the `lifecycle {}` block is the explicit safeguard for production resources (databases, state buckets) that should never be accidentally deleted. The exam tests this distinction.
    *   *Why A is incorrect:* `ignore_changes` tells Terraform to ignore specific attribute changes during plan; it does not prevent destruction of the resource itself.
    *   *Why B is incorrect:* `create_before_destroy = true` changes the replacement order (create new before deleting old) but does not prevent destruction.
    *   *Why D is incorrect:* `depends_on = []` manages execution order, not lifecycle protection. An empty `depends_on` list has no practical effect.
