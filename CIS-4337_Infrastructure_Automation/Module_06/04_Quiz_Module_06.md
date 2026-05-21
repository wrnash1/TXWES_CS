# Quiz: Module 06 - Data Sources and Terraform Functions
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Why is state locking critical in enterprise team environments?
*   A) To encrypt the contents of variable files before they are written to disk
*   B) To prevent concurrent `terraform apply` runs from simultaneously modifying the state file and causing corruption
*   C) To automatically speed up provider API calls during large deployments
*   D) To ensure that `terraform plan` output is cached between runs
*   **Correct Answer:** B) State locking ensures that if two operators run `apply` simultaneously, one operation is blocked until the other completes, preventing race conditions that could corrupt or overwrite state.
*   **Distractor Analysis:**
    *   *Why B is correct:* Without locking, two simultaneous `apply` operations could both read the current state, compute diffs, and write conflicting updates — leaving the state file in an inconsistent or corrupt state.
    *   *Why A is incorrect:* Variable file encryption is not a function of state locking. Sensitive variable values are protected through `sensitive = true` and secure backend storage.
    *   *Why C is incorrect:* State locking has no effect on provider API call speed. It is purely a concurrency control mechanism.
    *   *Why D is incorrect:* Terraform does not cache plan output via state locking. Saved plans are produced with `terraform plan -out=<file>` and stored as separate binary files.

---

**Question 2**
Which of the following most accurately describes **how a Terraform `data` block differs from a `resource` block**?
*   A) A `data` block creates and manages the full lifecycle of a cloud resource, while a `resource` block only reads existing infrastructure attributes
*   B) A `data` block performs a read-only query against a provider to fetch attributes of existing infrastructure without creating or destroying anything, while a `resource` block declares objects that Terraform creates and manages
*   C) A `data` block is used to declare output values that are displayed after `terraform apply`, while a `resource` block declares input variables
*   D) A `data` block requires `terraform init` to be run after every change, while a `resource` block does not
*   **Correct Answer:** B) `data` blocks are read-only — they query existing infrastructure (like finding an AMI ID or reading a VPC) and make the result available for reference. `resource` blocks declare infrastructure that Terraform owns and manages through create/update/destroy lifecycle operations.
*   **Distractor Analysis:**
    *   *Why B is correct:* This distinction is tested directly on the Terraform Associate exam. Removing a `data` block never destroys real infrastructure; removing a `resource` block causes Terraform to plan destroying the managed object.
    *   *Why A is incorrect:* The roles are reversed — `resource` manages lifecycle; `data` is read-only.
    *   *Why C is incorrect:* `output` blocks declare displayed values; `variable` blocks declare inputs. Neither `data` nor `resource` performs those functions.
    *   *Why D is incorrect:* Both `data` and `resource` blocks require `terraform init` only when a new provider is added, not on every change.

---

**Question 3**
You have a map variable `var.instance_sizes = { dev = "t3.micro", prod = "t3.large" }`. Which HCL expression correctly retrieves the instance size for the current environment, falling back to `"t3.small"` if the key is not found?
*   A) `var.instance_sizes[var.env]`
*   B) `element(var.instance_sizes, var.env)`
*   C) `lookup(var.instance_sizes, var.env, "t3.small")`
*   D) `find(var.instance_sizes, var.env)`
*   **Correct Answer:** C) `lookup(map, key, default)` is the correct function for retrieving a value from a map with a safe fallback default when the key may not exist.
*   **Distractor Analysis:**
    *   *Why C is correct:* `lookup(var.instance_sizes, var.env, "t3.small")` returns the value for `var.env` if it exists in the map, otherwise returns `"t3.small"`. This is the exam-canonical pattern.
    *   *Why A is incorrect:* Direct bracket notation `var.instance_sizes[var.env]` throws an error if the key does not exist; there is no fallback. It is valid only when the key is guaranteed to be present.
    *   *Why B is incorrect:* `element()` works on ordered lists indexed by integer position, not on maps indexed by string keys.
    *   *Why D is incorrect:* `find()` is not a built-in Terraform function. Using it would cause a configuration error.

---

**Question 4**
A Terraform configuration uses a `data "aws_vpc" "main"` block to look up an existing VPC by tag. A separate `resource "aws_subnet" "app"` block uses the VPC ID from that data source. During `terraform plan`, Terraform reports that the data source cannot be read because the VPC does not yet exist. What is the correct fix?
*   A) Move the `data` block into the same `.tf` file as the `resource` block
*   B) Add `depends_on = [aws_vpc.main]` inside the `data` block to ensure the VPC is created before the data source is queried
*   C) Replace the `data` block with a hard-coded VPC ID string
*   D) Run `terraform refresh` before `terraform plan` to pre-populate the data source
*   **Correct Answer:** B) Adding `depends_on` inside the `data` block instructs Terraform to defer reading the data source until after the referenced resource is created, resolving the sequencing issue.
*   **Distractor Analysis:**
    *   *Why B is correct:* `depends_on` is valid inside `data` blocks and is the correct mechanism for handling cases where a data source depends on a resource that Terraform itself is creating in the same configuration.
    *   *Why A is incorrect:* File organization has no effect on execution order. Terraform builds a dependency graph regardless of which `.tf` file a block is in.
    *   *Why C is incorrect:* Hard-coding IDs eliminates the flexibility of the data source and is an anti-pattern. It also creates maintenance burden if the VPC ID ever changes.
    *   *Why D is incorrect:* `terraform refresh` updates state from real-world API calls but cannot query a resource that does not yet exist.

---

**Question 5**
Which Terraform command provides an interactive REPL environment where you can evaluate HCL expressions and test built-in functions before using them in configuration files?
*   A) terraform validate
*   B) terraform fmt
*   C) terraform console
*   D) terraform debug
*   **Correct Answer:** C) `terraform console` opens an interactive shell that evaluates HCL expressions, including function calls and variable references, against the current state and configuration.
*   **Distractor Analysis:**
    *   *Why C is correct:* The exam tests that `terraform console` is the right tool for interactively testing functions like `lookup()`, `element()`, and `join()` without running a full plan or apply. You can type expressions and see their outputs immediately.
    *   *Why A is incorrect:* `terraform validate` checks configuration syntax and internal consistency but does not evaluate expressions interactively.
    *   *Why B is incorrect:* `terraform fmt` reformats `.tf` files to canonical HCL style; it does not evaluate expressions.
    *   *Why D is incorrect:* `terraform debug` is not a standard Terraform CLI command. Debug logging is enabled via the `TF_LOG` environment variable.
