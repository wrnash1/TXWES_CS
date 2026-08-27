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

---

### Question 11 (5 points)

What does the expression `flatten([["a", "b"], ["c"], ["d", "e"]])` return?

- A) `[["a", "b"], ["c"], ["d", "e"]]`
- B) `["a", "b", "c", "d", "e"]`
- C) `"a,b,c,d,e"`
- D) `5`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `flatten()` takes a list that may contain nested lists and produces a single flat list by removing one level of nesting. All elements from all inner lists are combined into one ordered list.
  - Why A is incorrect: That is the input, unchanged. `flatten()` specifically removes nesting.
  - Why C is incorrect: `flatten()` does not join elements into a string. Use `join(",", flatten(...))` to produce a comma-separated string.
  - Why D is incorrect: `5` is what `length(flatten(...))` would return. The function itself returns the flattened list, not its count.

---

### Question 12 (5 points)

A `data "aws_ami" "latest"` block includes `most_recent = true`. What does this argument do?

- A) It caches the AMI ID locally and skips the API call on subsequent plan runs.
- B) When multiple AMIs match the filter criteria, it selects the one with the most recent creation date.
- C) It forces Terraform to always re-query the AMI API, ignoring any cached state data.
- D) It restricts the lookup to AMIs created within the last 24 hours.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Without `most_recent = true`, the data source would error if multiple AMIs match. Setting it to `true` tells the provider to select the single most recently created matching AMI, which is the standard pattern for always using the latest version.
  - Why A is incorrect: Data source results are not locally cached between plan runs. The provider queries the API on every plan and apply.
  - Why C is incorrect: `most_recent` is a tie-breaking selection argument, not a cache-bypass flag.
  - Why D is incorrect: There is no time-window restriction implied by `most_recent`. It simply selects the newest from all matching AMIs regardless of age.

---

### Question 13 (5 points)

Which for expression correctly produces a map from the list `["web", "api", "db"]` where each key is the service name and each value is `"${name}-svc"`?

- A) `[for s in ["web", "api", "db"] : "${s}-svc"]`
- B) `{for s in ["web", "api", "db"] : s => "${s}-svc"}`
- C) `{for s in ["web", "api", "db"] : "${s}-svc"}`
- D) `(for s in ["web", "api", "db"] : s, "${s}-svc")`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Map-producing for expressions use curly braces `{}` and the `key => value` syntax. `{for s in list : s => "${s}-svc"}` produces `{"web"="web-svc", "api"="api-svc", "db"="db-svc"}`.
  - Why A is incorrect: Square brackets `[]` produce a list, not a map. This expression yields `["web-svc", "api-svc", "db-svc"]`.
  - Why C is incorrect: The curly braces are correct for a map, but the `=>` separator between key and value is missing. This is a syntax error.
  - Why D is incorrect: Parentheses are not used for for expressions in HCL. The comma syntax is also invalid.

---

### Question 14 (5 points)

In a `dynamic` block, what is the purpose of the `iterator` argument?

- A) It sets the number of nested blocks to generate by providing an integer count.
- B) It renames the object used to access each element's value inside the `content` block, overriding the default name (which is the dynamic block's label).
- C) It specifies which attribute of the parent resource the generated blocks belong to.
- D) It controls whether the dynamic block generates blocks before or after static nested blocks of the same type.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: By default, the iterator inside a `dynamic "ingress"` block is accessed as `ingress.value` and `ingress.key`. Setting `iterator = rule` changes it to `rule.value` and `rule.key`, which improves readability when the block label name is verbose or ambiguous.
  - Why A is incorrect: The number of generated blocks is determined by the size of the `for_each` collection, not by the `iterator` argument.
  - Why C is incorrect: The block label (e.g., `"ingress"`) identifies which nested block type is generated. The `iterator` only affects the variable name inside `content`.
  - Why D is incorrect: Terraform does not define an ordering between dynamic and static nested blocks of the same type based on any argument.

---

### Question 15 (5 points)

What does `jsonencode({Version = "2012-10-17", Statement = []})` produce?

- A) An HCL object literal with those key-value pairs.
- B) The Base64-encoded form of the JSON string.
- C) A JSON-formatted string: `"{\"Version\":\"2012-10-17\",\"Statement\":[]}"`.
- D) A Terraform-native policy document object that can be passed directly to IAM resource arguments.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `jsonencode()` converts an HCL value (object, map, list, string, number, bool) into a JSON-encoded string. AWS IAM policy arguments expect a JSON string, making `jsonencode` the standard way to construct them inline.
  - Why A is incorrect: `jsonencode` produces a string output, not an HCL object. The HCL object is the input to the function.
  - Why B is incorrect: `base64encode()` produces Base64 output. `jsonencode()` produces a JSON string without any encoding transformation.
  - Why D is incorrect: Terraform does not have a "native policy document object" type. IAM policy arguments accept JSON strings. The `aws_iam_policy_document` data source is an alternative approach, but `jsonencode` also produces a string.

---

### Question 16 (5 points)

You run `terraform console` and enter `cidrsubnet("172.16.0.0/12", 4, 2)`. What does this return?

- A) `"172.16.2.0/12"`
- B) `"172.18.0.0/16"`
- C) `"172.16.0.0/16"`
- D) `"172.32.0.0/16"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `cidrsubnet("172.16.0.0/12", 4, 2)` extends the `/12` prefix by 4 bits to create a `/16` prefix. The 12-bit prefix covers `172.16.0.0` to `172.31.255.255`. Subnet number 2 gives the third `/16` in that range: `172.18.0.0/16`.
  - Why A is incorrect: Changing only the third octet to 2 while keeping `/12` misunderstands how `cidrsubnet` works. The new prefix length is `/16` (12+4), not `/12`.
  - Why C is incorrect: `172.16.0.0/16` would be subnet number 0 (the first subnet). Subnet number 2 is two positions later.
  - Why D is incorrect: `172.32.0.0` falls outside the original `172.16.0.0/12` range. `cidrsubnet` only generates subnets within the parent CIDR.

---

### Question 17 (5 points)

When you remove a `data` block from a Terraform configuration and run `terraform apply`, what is the result?

- A) Terraform destroys the cloud resource that the data source was querying.
- B) Terraform plans and applies no infrastructure changes; only the data source's read query is removed from the plan.
- C) Terraform errors because any resource referencing the data source will have an unresolvable reference.
- D) Terraform prompts you to confirm whether you want to delete the data source's query results from state.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Data sources are read-only. Removing a `data` block from the configuration means Terraform simply stops querying that information. No cloud resources are created or destroyed as a result.
  - Why A is incorrect: Data sources do not own or manage cloud resources. They only read existing ones. Removing a `data` block cannot destroy anything.
  - Why C is incorrect: If any resource currently references the removed data source, that would be a configuration error caught by `terraform validate`. In that case the fix is to remove the reference, not the data source. But the question implies a clean removal.
  - Why D is incorrect: Data source results are not stored in state as persistent entries requiring confirmation to delete. Data is re-queried on every plan/apply run.

---

### Question 18 (5 points)

Which function returns the maximum value from a set of numbers in Terraform?

- A) `greatest(1, 5, 3)`
- B) `max(1, 5, 3)`
- C) `top(1, 5, 3)`
- D) `sort([1, 5, 3])[2]`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `max(numbers...)` is a built-in Terraform function that returns the largest of any number of numeric arguments. `max(1, 5, 3)` returns `5`.
  - Why A is incorrect: `greatest()` is not a Terraform built-in function and produces a configuration error.
  - Why C is incorrect: `top()` is not a Terraform built-in function.
  - Why D is incorrect: While `sort([1, 5, 3])[2]` would technically return the largest value if the sort is ascending, `sort()` operates on lists of strings, not numbers. Numeric sorting requires type conversion and is an unnecessarily complex pattern compared to using `max()` directly.

---

### Question 19 (5 points)

What is the result of `length(toset(["a", "b", "a", "c", "b"]))` in Terraform?

- A) `5`
- B) `3`
- C) `2`
- D) An error because `toset` cannot be nested inside `length`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `toset()` converts a list to a set, removing duplicates. The list `["a", "b", "a", "c", "b"]` has three unique values: `"a"`, `"b"`, `"c"`. `length()` of the resulting set is `3`.
  - Why A is incorrect: `5` is the length of the original list before deduplication. `toset` removes duplicates before `length` counts the elements.
  - Why C is incorrect: `2` would be the count if only `"a"` and `"b"` were present. `"c"` is a third unique element.
  - Why D is incorrect: Nesting function calls is fully supported in Terraform HCL. The result of `toset()` is a valid argument to `length()`.

---

### Question 20 (5 points)

A data source `data "aws_subnets" "private"` filters subnets by tag. A resource needs to spread instances across all returned subnets. Which expression correctly references the nth subnet ID, where `n = count.index`?

- A) `data.aws_subnets.private[count.index].id`
- B) `data.aws_subnets.private.ids[count.index]`
- C) `element(data.aws_subnets.private, count.index)`
- D) `module.aws_subnets.private.ids[count.index]`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `aws_subnets` data source returns a list attribute `ids` containing all matching subnet IDs. Indexing with `[count.index]` selects the correct subnet for each resource instance.
  - Why A is incorrect: Data sources return a single object (not a list of objects), so you cannot index the data source itself with `[count.index]`. The `ids` list attribute is what you index into.
  - Why C is incorrect: `element()` expects a list as its first argument, but `data.aws_subnets.private` is the data source object, not a list. The correct list is `data.aws_subnets.private.ids`.
  - Why D is incorrect: `module.` is used to reference child module outputs. Data sources use the `data.` prefix.

---

Module 06 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
