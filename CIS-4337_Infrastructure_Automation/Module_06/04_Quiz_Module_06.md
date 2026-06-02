# CIS-4337 Infrastructure Automation

## Quiz — Module 06: Data Sources and Terraform Functions

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What is the primary characteristic that distinguishes a `data` block from a `resource` block in Terraform?

- A) A `data` block creates and manages the full lifecycle of a cloud resource, while a `resource` block only reads attributes.
- B) A `data` block performs a read-only query against a provider API to fetch attributes of existing infrastructure without creating or destroying anything, while a `resource` block declares objects Terraform creates and manages.
- C) A `data` block is used to declare output values, while a `resource` block declares input variables.
- D) A `data` block requires `terraform init` to be re-run on every change, while a `resource` block does not.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Data sources are read-only. They query existing infrastructure and make the result available for reference. Deleting a `data` block has no effect on real infrastructure. Resource blocks declare objects Terraform owns and manages through full create, update, and destroy lifecycle operations.
- Why A is incorrect: The roles are reversed. A `resource` block manages lifecycle; a `data` block reads.
- Why C is incorrect: `output` blocks declare displayed values. `variable` blocks declare inputs. Neither `data` nor `resource` serves these functions.
- Why D is incorrect: Both `data` and `resource` blocks require `terraform init` only when a new provider is added, not on every change.

---

### Question 2

Which of the following correctly retrieves the value for key `"dev"` from the map `var.sizes = { dev = "t3.micro", prod = "t3.large" }`, returning `"t3.micro"` as a fallback if the key is missing?

- A) `var.sizes[var.env]`
- B) `element(var.sizes, var.env)`
- C) `lookup(var.sizes, var.env, "t3.micro")`
- D) `find(var.sizes, var.env)`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `lookup(map, key, default)` retrieves a value from a map by key. If the key does not exist, it returns the default value. This is the safe pattern for dynamic map lookups.
- Why A is incorrect: Direct bracket notation `var.sizes[var.env]` raises an error if the key does not exist in the map. There is no fallback.
- Why B is incorrect: `element()` operates on ordered lists indexed by integers. It does not accept maps or string keys.
- Why D is incorrect: `find()` is not a built-in Terraform function. Using it produces a configuration error.

---

### Question 3

A `data "aws_vpc" "main"` block queries a VPC by tag. A `resource "aws_subnet" "app"` block uses `data.aws_vpc.main.id`. During plan, Terraform reports the data source cannot be read because the VPC does not yet exist. What is the correct fix?

- A) Move the `data` block into the same `.tf` file as the `resource` block.
- B) Add `depends_on = [aws_vpc.main]` inside the `data` block.
- C) Replace the `data` block with the hardcoded VPC ID.
- D) Run `terraform refresh` before `terraform plan`.

Correct Answer: B

Distractor Analysis:

- Why B is correct: `depends_on` is valid inside `data` blocks. It instructs Terraform to defer reading the data source until the referenced resource is fully created. This resolves sequencing issues when a data source queries infrastructure being created in the same run.
- Why A is incorrect: File organization has no effect on execution order. Terraform builds a dependency graph from references and `depends_on`, not from file position.
- Why C is incorrect: Hardcoding IDs eliminates the flexibility of data sources and creates maintenance burden. It is an anti-pattern.
- Why D is incorrect: `terraform refresh` updates state from live API calls but cannot query a resource that does not yet exist.

---

### Question 4

Which Terraform command opens an interactive environment where you can evaluate HCL expressions and test functions before using them in configurations?

- A) `terraform validate`
- B) `terraform fmt`
- C) `terraform console`
- D) `terraform debug`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform console` opens an interactive REPL that evaluates HCL expressions against the current state and configuration. Type any expression — `upper("hello")`, `cidrsubnet("10.0.0.0/16", 8, 3)` — and see the result immediately.
- Why A is incorrect: `terraform validate` checks configuration syntax and internal consistency. It does not evaluate expressions interactively.
- Why B is incorrect: `terraform fmt` reformats `.tf` files to canonical style. It does not evaluate expressions.
- Why D is incorrect: `terraform debug` is not a valid Terraform command. Debug logging is enabled via the `TF_LOG` environment variable.

---

### Question 5

What does `cidrsubnet("10.0.0.0/16", 8, 3)` return?

- A) `"10.0.0.0/8"`
- B) `"10.0.3.0/24"`
- C) `"10.3.0.0/24"`
- D) `"10.0.0.3/16"`

Correct Answer: B

Distractor Analysis:

- Why B is correct: `cidrsubnet(prefix, newbits, netnum)` extends the prefix by `newbits` bits and selects the subnet numbered `netnum`. `10.0.0.0/16` extended by 8 bits becomes `/24`. Subnet number 3 gives `10.0.3.0/24`.
- Why A is incorrect: Extending a `/16` by 8 bits yields `/24`, not `/8`.
- Why C is incorrect: The subnet number 3 selects the third octet offset, producing `10.0.3.0/24`, not `10.3.0.0/24`.
- Why D is incorrect: The subnet number does not become a host bit in the original prefix. The function calculates a new CIDR block.

---

### Question 6

Which function correctly converts an HCL object to a JSON string for use as an IAM policy argument?

- A) `tojson(policy_object)`
- B) `stringify(policy_object)`
- C) `jsonencode(policy_object)`
- D) `base64encode(policy_object)`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `jsonencode(val)` converts any HCL value (object, map, list, string) to a JSON-encoded string. It is the standard way to pass structured data to AWS arguments that expect JSON strings such as IAM policies and S3 bucket policies.
- Why A is incorrect: `tojson()` is not a Terraform built-in function.
- Why B is incorrect: `stringify()` is not a Terraform built-in function.
- Why D is incorrect: `base64encode()` encodes a string as Base64. It does not convert objects to JSON.

---

### Question 7

A `dynamic "ingress"` block inside an `aws_security_group` resource has `for_each = var.allowed_ports` where `var.allowed_ports = [80, 443, 8080]`. How many `ingress` nested blocks will the plan show?

- A) One block containing all three port values.
- B) Three separate `ingress` blocks, one for each port.
- C) Zero blocks because `dynamic` requires a `map`, not a list.
- D) The number of blocks is determined at apply time and cannot be previewed in a plan.

Correct Answer: B

Distractor Analysis:

- Why B is correct: The `dynamic` block generates one nested block per element in the `for_each` collection. With three elements in `var.allowed_ports`, three separate `ingress` blocks are generated and shown in the plan.
- Why A is incorrect: A `dynamic` block does not aggregate values into one block. It produces one block per element.
- Why C is incorrect: `for_each` in a `dynamic` block accepts both lists and maps. When a list is used, the iterator value is the list element.
- Why D is incorrect: Terraform evaluates `for_each` during plan. The number and content of generated blocks are fully visible in the plan output.

---

### Question 8

You need to get the names of all IAM users in your AWS account without creating any resources. Which block type is correct?

- A) `resource "aws_iam_users" "all" {}`
- B) `data "aws_iam_users" "all" {}`
- C) `variable "aws_iam_users" "all" {}`
- D) `module "iam_users" { source = "aws_iam_users" }`

Correct Answer: B

Distractor Analysis:

- Why B is correct: `data` blocks perform read-only queries. `data "aws_iam_users"` queries the AWS API to retrieve IAM user information without creating any resources. The result is referenced as `data.aws_iam_users.all.names`.
- Why A is incorrect: A `resource` block would declare IAM users Terraform manages. It would attempt to create new users, not read existing ones.
- Why C is incorrect: `variable` blocks declare input parameters. They do not perform API queries.
- Why D is incorrect: `aws_iam_users` is not a module source. This is not a valid module call syntax.

---

### Question 9

What does the following for expression produce?

```hcl
[for s in ["web", "api", "db"] : "${s}-server"]
```

- A) `{"web" = "web-server", "api" = "api-server", "db" = "db-server"}`
- B) `["web-server", "api-server", "db-server"]`
- C) `"web-server,api-server,db-server"`
- D) `3`

Correct Answer: B

Distractor Analysis:

- Why B is correct: The `[for s in list : expression]` syntax produces a new list. Each element `s` is transformed by the expression `"${s}-server"`, yielding a list of three strings.
- Why A is incorrect: A `{for k, v in map : key => value}` expression with curly braces produces a map. Square brackets produce a list.
- Why C is incorrect: For expressions do not automatically join results with commas. To produce a joined string, use `join(",", [for s in ... : ...])`.
- Why D is incorrect: `3` is what `length([...])` would return for a list of three elements. The for expression returns the transformed list, not its count.

---

### Question 10

A data source `data "aws_availability_zones" "available"` is referenced as `data.aws_availability_zones.available.names[0]`. What does this reference return?

- A) The total count of available availability zones.
- B) The first availability zone name in the list returned by the data source.
- C) A Boolean value indicating whether the first AZ is available.
- D) The ID of the first availability zone.

Correct Answer: B

Distractor Analysis:

- Why B is correct: `data.aws_availability_zones.available.names` is a list of availability zone name strings. Index `[0]` accesses the first element, which is a string like `"us-east-1a"`.
- Why A is incorrect: The total count would be obtained with `length(data.aws_availability_zones.available.names)`.
- Why C is incorrect: The `names` attribute returns strings, not Boolean values. Boolean availability filtering is done by the `state = "available"` argument in the data source block.
- Why D is incorrect: AZ IDs are different from AZ names. The `zone_ids` attribute returns IDs. `names` returns human-readable names like `"us-east-1a"`.

---

Module 06 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
