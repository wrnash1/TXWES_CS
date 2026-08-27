# Quiz: Module 15 — Advanced Terraform Patterns

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Select the best answer for each question. Each question is worth 1 point. Distractor analysis follows each question to explain why incorrect options are wrong.

---

## Questions

### Question 1 — Answer: D

A `dynamic "ingress"` block has `for_each = var.ingress_rules` and no `iterator` argument. Inside the `content` block, how do you reference the current element's `from_port` field?

A. `var.ingress_rules.from_port`

B. `each.value.from_port`

C. `content.from_port`

D. `ingress.value.from_port`

Why the distractors are wrong: **A** is wrong because `var.ingress_rules` is the full collection — inside the dynamic block you reference the current element through the iterator, not the original variable. **B** is wrong because `each.value` is the syntax used inside `for_each` on a resource block, not inside a `dynamic` block's content. **C** is wrong because `content` is the keyword that wraps the block definition — it is not an iterator variable.

---

### Question 2 — Answer: C

You have four EC2 instances created with `count = 4`. You remove the second element from the list used to drive the count. What does Terraform plan?

A. Terraform plans no changes because the count is still 3 instances.

B. Terraform plans to destroy only the second instance (index 1).

C. Terraform plans to destroy the fourth instance and modify the third instance because their indices shift down by one.

D. Terraform plans to destroy all four instances and recreate three of them.

Why the distractors are wrong: **A** is wrong because removing an element changes the values at each index, which Terraform detects as changes. **B** is wrong because count-indexed resources are identified by position — removing position 1 renumbers subsequent resources, not just deletes the specific one. **D** is wrong because only the affected instances (those whose index content changed) are impacted — the first instance at index 0 is unchanged if the first element was not modified.

---

### Question 3 — Answer: B

Which of the following collections can be passed to `for_each` on a resource block? Select all that apply.

A. A list of strings

B. A map of objects

C. A set of strings

D. A list of numbers

The question asks you to identify the valid options. Which answer correctly identifies both valid choices?

A. Only option A (list of strings)

B. Options B and C (map of objects and set of strings)

C. Options A, B, and C (lists, maps, and sets)

D. Options A and D (lists only)

Why the distractors are wrong: **A** is wrong because lists are not valid for_each inputs — `for_each` requires a map or a set. **C** is wrong because lists (A and D) are not directly supported — they must be converted with `toset()` first. **D** is wrong for the same reason — lists of numbers cannot be used directly with for_each.

---

### Question 4 — Answer: A

A resource uses `for_each = var.environments` where `var.environments` is a map. How is the instance for the key `"production"` addressed in Terraform state and in references from other resources?

A. `aws_instance.app["production"]`

B. `aws_instance.app.production`

C. `aws_instance.app[production]`

D. `aws_instance.app.for_each.production`

Why the distractors are wrong: **B** is wrong because Terraform uses bracket notation with a quoted string key for for_each instances, not dot notation. **C** is wrong because the key must be quoted inside the brackets — unquoted `production` is not valid HCL. **D** is wrong because `for_each` is a meta-argument keyword, not part of the resource address.

---

### Question 5 — Answer: C

What is the correct Terraform syntax for a conditional expression that sets `instance_type` to `"t3.large"` when `var.is_production` is true and `"t3.micro"` when false?

A. `instance_type = if var.is_production then "t3.large" else "t3.micro"`

B. `instance_type = var.is_production == true { "t3.large" } else { "t3.micro" }`

C. `instance_type = var.is_production ? "t3.large" : "t3.micro"`

D. `instance_type = switch(var.is_production, true, "t3.large", "t3.micro")`

Why the distractors are wrong: **A** is wrong because Terraform does not support `if/then/else` keyword syntax — it uses the ternary operator. **B** is wrong because this syntax is not valid HCL. **D** is wrong because Terraform has no `switch()` function — conditional logic uses the ternary operator or `lookup()` for map-based dispatch.

---

### Question 6 — Answer: B

What does the `moved` block do when you run `terraform apply`?

A. It destroys the resource at the `from` address and creates a new resource at the `to` address.

B. It updates the state file to record the resource at the new `to` address without modifying the underlying infrastructure.

C. It copies the resource configuration to the new address and keeps both the old and new resources active.

D. It marks the resource at the `from` address as tainted so it is replaced on the next apply.

Why the distractors are wrong: **A** is wrong because this describes what Terraform would do without a `moved` block — the whole purpose of `moved` is to avoid this destroy/create cycle. **C** is wrong because `moved` does not duplicate resources — it updates the state reference. **D** is wrong because tainting is a separate concept (marking a resource for forced replacement) and has nothing to do with `moved` blocks.

---

### Question 7 — Answer: D

You run `terraform import aws_s3_bucket.my_bucket my-existing-bucket`. What must be true before running this command?

A. The S3 bucket must be empty and have no bucket policy.

B. The `terraform.tfstate` file must not yet exist so import can create it fresh.

C. The Terraform workspace must have `TF_WORKSPACE=default` set in the environment.

D. A `resource "aws_s3_bucket" "my_bucket" {}` block must already exist in the configuration.

Why the distractors are wrong: **A** is wrong because import works on buckets with any content and any policy — it reads the current state and does not modify the resource. **B** is wrong because import adds to an existing state file or creates one if absent — an existing state file is fine. **C** is wrong because workspace selection is independent of the import command.

---

### Question 8 — Answer: A

The `terraform plan -generate-config-out=generated.tf` command is run after adding an `import` block. What does the generated file contain?

A. A resource block for the imported resource with its current attribute values populated from the live cloud resource.

B. A complete Terraform module with variables, outputs, and the resource block.

C. A `.tfvars` file with the current attribute values formatted as variable assignments.

D. A JSON representation of the current state of the imported resource.

Why the distractors are wrong: **B** is wrong because the generated output is only the resource block — not a full module with variables and outputs. **C** is wrong because the output is HCL resource block syntax, not tfvars format. **D** is wrong because the generated output is HCL configuration, not the JSON state format produced by `terraform show -json`.

---

### Question 9 — Answer: C

A Terraform configuration has `resource "aws_cloudwatch_log_group" "app" { count = var.enable_logging ? 1 : 0 }`. Another resource needs to reference the log group ARN only when logging is enabled. Which expression correctly handles this?

A. `aws_cloudwatch_log_group.app.arn`

B. `aws_cloudwatch_log_group.app[*].arn`

C. `var.enable_logging ? aws_cloudwatch_log_group.app[0].arn : ""`

D. `try(aws_cloudwatch_log_group.app.arn, "")`

Why the distractors are wrong: **A** is wrong because `aws_cloudwatch_log_group.app` without an index is ambiguous when count is used — Terraform requires an explicit index. **B** is wrong because the splat expression `[*]` returns a list, not a single string value — it cannot be used where a single string is required. **D** is wrong because `try()` catches type conversion errors, not missing count instances — Terraform would raise a plan-time error about the missing index before try could catch it.

---

### Question 10 — Answer: B

You want to change a resource created with `count` to use `for_each` without destroying and recreating the resources. You have two instances: `aws_subnet.public[0]` and `aws_subnet.public[1]`. You want them to become `aws_subnet.public["subnet-a"]` and `aws_subnet.public["subnet-b"]`. What is the correct approach?

A. Delete the resource from the state file with `terraform state rm` and re-import it using the new for_each keys.

B. Add two `moved` blocks mapping each count-indexed instance to its corresponding for_each key, then change the resource to use `for_each`.

C. Run `terraform taint aws_subnet.public[0]` and `terraform taint aws_subnet.public[1]` to force recreation with new addresses.

D. Change `count` to `for_each` directly in the configuration and run `terraform apply -refresh-only` to update the state.

Why the distractors are wrong: **A** is wrong because removing from state and re-importing is unnecessary — `moved` blocks handle this cleanly without risking data loss. **C** is wrong because tainting forces replacement (destroy and recreate), which is exactly what you are trying to avoid for production subnets. **D** is wrong because changing count to for_each without moved blocks would cause Terraform to plan destroying the count-indexed instances and creating the for_each-keyed instances.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | D |
| 2 | C |
| 3 | B |
| 4 | A |
| 5 | C |
| 6 | B |
| 7 | D |
| 8 | A |
| 9 | C |
| 10 | B |
| 11 | A |
| 12 | C |
| 13 | D |
| 14 | B |
| 15 | A |
| 16 | C |
| 17 | D |
| 18 | B |
| 19 | A |
| 20 | C |

---

### Question 11 — Answer: A

A dynamic block uses `for_each = var.security_group_rules` where `var.security_group_rules` is a list of objects. You run `terraform plan` and receive: `The given value is not suitable for for_each: must be a map or set of strings.` What is the minimal fix?

A. Change `for_each = var.security_group_rules` to `for_each = toset(var.security_group_rules)` if the objects are unique, or restructure the variable as a map keyed by a unique identifier.

B. Replace the dynamic block with a `count`-based resource and reference `var.security_group_rules[count.index]`.

C. Wrap the list in a `jsondecode()` call to convert it to a map before passing it to `for_each`.

D. Add `type = map(any)` to the variable declaration to automatically coerce the list to a map.

Why the distractors are wrong: **B** is wrong because this avoids the dynamic block entirely and reintroduces the index-shifting problem — the requirement is to fix the dynamic block, not replace it. **C** is wrong because `jsondecode()` parses a JSON string into an HCL value — it does not convert an already-decoded list into a map. **D** is wrong because changing the variable type declaration does not convert an existing list value into a map — values and types must be aligned before the dynamic block can use them.

---

### Question 12 — Answer: C

A `moved` block has `from = aws_security_group.legacy` and `to = module.networking.aws_security_group.main`. What does this indicate?

A. The security group resource is being moved from one AWS region to another.

B. The security group is being renamed within the same module.

C. The security group resource is being refactored from the root module into a child module named `networking` without destroying and recreating the resource.

D. The `networking` module will create a new security group and the legacy resource will be deleted at the end of the apply.

Why the distractors are wrong: **A** is wrong because `moved` blocks update state references only — they have no ability to move physical resources between AWS regions. **B** is wrong because a rename within the same module would have the same module prefix in both `from` and `to` — the presence of `module.networking` in `to` indicates a cross-module move. **D** is wrong because a `moved` block explicitly prevents the destroy/create cycle — the whole purpose is to preserve the existing infrastructure.

---

### Question 13 — Answer: D

Which statement about `terraform import` using an `import` block (Terraform 1.5+) is accurate compared to the legacy `terraform import` CLI command?

A. The `import` block requires the resource to already have all attribute values specified in the configuration before import.

B. The `import` block only works with resources that support the `generate-config-out` flag.

C. The `import` block runs the import silently during `terraform apply` without showing the import operation in the plan output.

D. The `import` block allows the import to be previewed with `terraform plan` and reviewed before any state changes occur, unlike the CLI command which immediately modifies state.

Why the distractors are wrong: **A** is wrong because the `import` block combined with `-generate-config-out` is specifically designed to work even without pre-written configuration — the command generates the configuration for you. **B** is wrong because `generate-config-out` is optional; you can write the resource block manually and use the `import` block without generation. **C** is wrong because `terraform plan` with an `import` block explicitly shows the import and any resulting configuration drift, making it fully visible.

---

### Question 14 — Answer: B

A Terraform configuration has `locals { names = [for n in var.raw_names : lower(trimspace(n)) if n != ""] }`. What does this expression produce?

A. A map of raw names to their lowercase trimmed equivalents.

B. A list of lowercase, whitespace-trimmed strings from `var.raw_names` with empty strings excluded.

C. A set of unique lowercase names with duplicates removed.

D. A tuple of exactly two values: the first name and the last name from the input.

Why the distractors are wrong: **A** is wrong because the `for` expression uses a list result syntax (no `=>` operator), which produces a list, not a map. **C** is wrong because a `for` expression with list syntax produces a list that preserves duplicates — to produce a set you would wrap it with `toset()`. **D** is wrong because a for expression without a length limit iterates over every element in `var.raw_names`, not just the first and last.

---

### Question 15 — Answer: A

You add a `precondition` block inside a resource's `lifecycle` block that checks `var.instance_count >= 1`. At what point does Terraform evaluate this check?

A. During `terraform plan`, before any infrastructure changes are made, failing the plan if the condition is false.

B. During `terraform apply`, after all resources are created, as a post-deployment verification.

C. During `terraform validate`, as a static syntax check before any provider initialization.

D. During `terraform init`, to verify that the variable default satisfies the constraint before downloading providers.

Why the distractors are wrong: **B** is wrong because `precondition` is evaluated before the resource is created or modified, not after — that is the purpose of `postcondition`. **C** is wrong because `terraform validate` checks configuration syntax and type correctness but does not evaluate expressions that depend on variable values — the variable may not yet have a value at validate time. **D** is wrong because `terraform init` downloads providers and modules — it does not evaluate lifecycle preconditions.

---

### Question 16 — Answer: C

A module author wants to ensure that a `variable "environment"` only accepts the values `"dev"`, `"staging"`, or `"prod"`. Which configuration correctly enforces this?

A. `type = enum("dev", "staging", "prod")`

B. `default = ["dev", "staging", "prod"]`

C. `validation { condition = contains(["dev", "staging", "prod"], var.environment); error_message = "Environment must be dev, staging, or prod." }`

D. `sensitive = true` with a comment documenting the allowed values

Why the distractors are wrong: **A** is wrong because Terraform has no `enum` type — valid types are `string`, `number`, `bool`, `list`, `map`, `set`, `object`, and `tuple`. **B** is wrong because setting a `default` of a list does not constrain the accepted values — it only provides a fallback if no value is supplied. **D** is wrong because `sensitive = true` suppresses display of the value — it has no enforcement effect on which values are accepted.

---

### Question 17 — Answer: D

A resource block has both a `precondition` that checks an input variable and a `postcondition` that checks an output attribute. The `precondition` passes but the `postcondition` fails after apply. What is the result?

A. Terraform marks the resource as tainted and plans to replace it on the next run.

B. Terraform rolls back the apply and destroys the resource that was just created.

C. Terraform ignores the failed postcondition and marks the apply as successful.

D. Terraform raises an error, marks the apply as failed, and leaves the resource in state as-is for manual investigation.

Why the distractors are wrong: **A** is wrong because a failed postcondition does not automatically taint a resource — tainting is a manual operation or the result of a `replace_triggered_by` configuration. **B** is wrong because Terraform does not have automatic rollback — once a resource is created, a failed postcondition errors the run but does not destroy the resource. **C** is wrong because Terraform treats failed postconditions as errors that halt the run — it does not silently ignore them.

---

### Question 18 — Answer: B

What is the difference between `toset(["a", "b", "a"])` and `tolist(["a", "b", "a"])` when used in Terraform?

A. Both return the same three-element collection because sets and lists store identical data.

B. `toset()` returns a set containing `"a"` and `"b"` with the duplicate removed and without guaranteed ordering; `tolist()` returns a three-element list preserving order and duplicates.

C. `toset()` sorts the elements alphabetically; `tolist()` preserves the original insertion order.

D. `toset()` and `tolist()` are interchangeable — the difference is only cosmetic in plan output.

Why the distractors are wrong: **A** is wrong because sets deduplicate values, so the three-element input produces a two-element set. **C** is wrong because Terraform sets have no guaranteed ordering — they are not sorted, they simply eliminate duplicates. **D** is wrong because they are not interchangeable — `for_each` requires a set or map and rejects a list; passing a list where a set is expected produces a type error.

---

### Question 19 — Answer: A

A `for_each` resource has been applied with keys `["web", "api", "db"]`. A team member needs to remove the `"api"` instance without affecting `"web"` or `"db"`. What is the correct procedure?

A. Remove `"api"` from the collection passed to `for_each` and run `terraform apply` — Terraform will plan to destroy only the `"api"` instance.

B. Run `terraform destroy -target=aws_instance.app["api"]` and then remove `"api"` from the collection before the next plan.

C. Run `terraform state rm aws_instance.app["api"]` and then remove `"api"` from the collection — the resource will be orphaned in AWS.

D. Add a `lifecycle { prevent_destroy = false }` block to the `"api"` instance and then remove it from the collection.

Why the distractors are wrong: **B** is wrong because using `-target` for routine removal is discouraged — it bypasses dependency checking and can leave related resources in an inconsistent state. More importantly, the question asks for the correct procedure, and the standard `for_each` removal pattern requires only removing the key from the collection. **C** is wrong because `terraform state rm` removes the resource from state without destroying it, leaving an unmanaged resource in AWS — this is not the intended behavior for decommissioning. **D** is wrong because `prevent_destroy = false` is the default — it has no effect on whether the resource is destroyed when removed from the collection.

---

### Question 20 — Answer: C

A team uses the `moved` block to rename a resource. Six months later, a new engineer joins and asks why the `moved` block is still in the codebase — "the resource was already moved, why not delete it?" What is the correct answer?

A. The `moved` block must remain permanently because Terraform needs it to read the state file on every plan.

B. The `moved` block should be deleted immediately because leaving it causes Terraform to re-apply the state update on every plan, which is wasteful.

C. The `moved` block can be safely deleted once all team members and all CI environments have run `terraform apply` with the block present, because its only purpose was to update existing state files — once all state files are updated, the block is no longer needed.

D. The `moved` block cannot be deleted because older Terraform versions will error if the `from` address appears in the state file without a corresponding `moved` block.

Why the distractors are wrong: **A** is wrong because `moved` blocks are idempotent — once the state file has been updated, subsequent plans with the `moved` block present produce no additional state changes. **B** is wrong because the `moved` block is idempotent and does not re-apply changes on every plan once the state is already updated — it is safe to leave temporarily but not harmful. **D** is wrong because Terraform does not require `moved` blocks to interpret existing state entries — addresses in state that do not match configuration produce a "will be destroyed" plan, not an error referencing a missing moved block.

---

End of Module 15 Quiz
