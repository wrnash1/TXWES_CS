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

---

End of Module 15 Quiz
