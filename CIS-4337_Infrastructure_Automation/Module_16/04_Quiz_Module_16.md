# Quiz: Module 16 — Terraform Associate 003 Exam Preparation and Capstone

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

This quiz contains 20 questions covering all nine Terraform Associate 003 exam objective domains. Each question is worth 0.5 points for a total of 10 points. This format mirrors the breadth of the actual certification exam. Distractor analysis follows each question.

---

## Questions

### Question 1 — Answer: B

Which property of IaC describes the fact that applying the same Terraform configuration multiple times produces the same infrastructure state?

A. Consistency

B. Idempotency

C. Repeatability

D. Immutability

Why the distractors are wrong: **A** is wrong because consistency means every deployment uses the same process — it does not specifically address what happens on repeated application of the same configuration. **C** is wrong because repeatability means you can redeploy identically — similar to idempotency but does not carry the same mathematical guarantee about multiple applications producing identical results. **D** is wrong because immutability is the infrastructure pattern of replacing resources rather than modifying them in place — a separate concept from idempotency.

---

### Question 2 — Answer: D

Which statement correctly distinguishes Terraform from AWS CloudFormation?

A. Terraform is cloud-specific; CloudFormation is cloud-agnostic.

B. Terraform stores state in the cloud; CloudFormation stores state locally.

C. CloudFormation supports more AWS resource types than the Terraform AWS provider.

D. Terraform can provision resources across multiple cloud providers; CloudFormation is limited to AWS.

Why the distractors are wrong: **A** is wrong because it reverses the correct comparison — Terraform is cloud-agnostic and CloudFormation is AWS-specific. **B** is wrong because Terraform can use remote or local state while CloudFormation manages state within the AWS CloudFormation service. **C** is wrong because the Terraform AWS provider generally has comparable or broader coverage of AWS resource types.

---

### Question 3 — Answer: C

A Terraform `data` source block is best described as:

A. A block that creates a new resource in the cloud.

B. A block that declares a reusable input variable for a module.

C. A block that reads information about an existing resource without creating or modifying it.

D. A block that stores computed values for use elsewhere in the configuration.

Why the distractors are wrong: **A** is wrong because data sources are read-only — creating resources uses `resource` blocks. **B** is wrong because input variables use the `variable` block type. **D** is wrong because that describes the `locals` block.

---

### Question 4 — Answer: A

What is the correct variable precedence order from LOWEST to HIGHEST in Terraform?

A. Default value → `terraform.tfvars` → `*.auto.tfvars` → `-var-file` → `-var` flag → `TF_VAR_` env var

B. `TF_VAR_` env var → `-var` flag → `-var-file` → `*.auto.tfvars` → `terraform.tfvars` → Default value

C. `-var` flag → `-var-file` → `TF_VAR_` env var → `*.auto.tfvars` → `terraform.tfvars` → Default value

D. Default value → `TF_VAR_` env var → `terraform.tfvars` → `*.auto.tfvars` → `-var-file` → `-var` flag

Why the distractors are wrong: **B** is wrong because it lists the order from highest to lowest, which is the reverse of what the question asks. **C** is wrong because the `-var` flag has higher precedence than both `-var-file` and `TF_VAR_` environment variables. **D** is wrong because `TF_VAR_` environment variables do not sit between the default value and `terraform.tfvars` — auto-loaded files come before explicitly specified files.

---

### Question 5 — Answer: B

What happens when you run `terraform plan -detailed-exitcode` and the exit code is 1?

A. The plan completed successfully with no infrastructure changes needed.

B. The plan encountered an error and did not complete successfully.

C. The plan completed and infrastructure changes are present.

D. The plan was interrupted by a state lock held by another process.

Why the distractors are wrong: **A** is wrong because exit code 0 means success with no changes. **C** is wrong because exit code 2 means success with changes present. **D** is wrong because a state lock interruption is a specific error type that would produce exit code 1 (an error), but the question asks what exit code 1 means in general — it means any error, not specifically a lock issue.

---

### Question 6 — Answer: C

Which command downloads provider plugins, initializes the backend, and downloads modules?

A. `terraform validate`

B. `terraform plan`

C. `terraform init`

D. `terraform get`

Why the distractors are wrong: **A** is wrong because `terraform validate` only checks HCL syntax and does not download any external resources. **B** is wrong because `terraform plan` generates an execution plan but requires a previously initialized working directory. **D** is wrong because `terraform get` downloads modules only — it does not download providers or initialize the backend. (Note: `terraform get` is largely superseded by `terraform init` for module management.)

---

### Question 7 — Answer: D

Which of the following correctly describes the standard required file structure for a Terraform module published to the public Terraform Registry?

A. `main.tf`, `provider.tf`, `data.tf`

B. `resources.tf`, `vars.tf`, `outs.tf`

C. `main.tf`, `locals.tf`, `outputs.tf`

D. `main.tf`, `variables.tf`, `outputs.tf`

Why the distractors are wrong: **A** is wrong because `provider.tf` and `data.tf` are conventions used by some teams but are not the required standard structure. **B** is wrong because `vars.tf` and `outs.tf` are non-standard file names — the convention is `variables.tf` and `outputs.tf`. **C** is wrong because `locals.tf` is not a required file — it is optional. The three required files are `main.tf`, `variables.tf`, and `outputs.tf`.

---

### Question 8 — Answer: A

The `terraform.workspace` expression inside a configuration returns:

A. The name of the currently selected Terraform workspace as a string.

B. The path to the workspace directory on the local filesystem.

C. The ID of the Terraform Cloud workspace if a remote backend is configured.

D. A boolean indicating whether the default workspace is currently active.

Why the distractors are wrong: **B** is wrong because `terraform.workspace` is a string value, not a filesystem path. **C** is wrong because `terraform.workspace` returns the workspace name, not an ID, and behaves identically for local and remote workspaces. **D** is wrong because `terraform.workspace` is a string, not a boolean.

---

### Question 9 — Answer: B

Which `terraform state` subcommand removes a resource from the state file without destroying the underlying infrastructure?

A. `terraform state delete`

B. `terraform state rm`

C. `terraform state remove`

D. `terraform state purge`

Why the distractors are wrong: **A** is wrong because `terraform state delete` is not a valid subcommand. **C** is wrong because `terraform state remove` is not a valid subcommand — the correct subcommand is `rm`. **D** is wrong because `terraform state purge` is not a valid subcommand.

---

### Question 10 — Answer: C

You need to force Terraform to destroy and recreate a specific EC2 instance on the next apply without modifying any configuration. Which command achieves this in Terraform 1.0+?

A. `terraform taint aws_instance.web`

B. `terraform state rm aws_instance.web`

C. `terraform apply -replace=aws_instance.web`

D. `terraform destroy -target=aws_instance.web`

Why the distractors are wrong: **A** is wrong because while `terraform taint` achieves forced replacement, the question specifies Terraform 1.0+ where the preferred approach is `-replace`. `taint` is deprecated in favor of `-replace`. **B** is wrong because removing from state stops Terraform from managing the resource entirely — it does not recreate it. **D** is wrong because `-target` with destroy only destroys the resource without recreating it — a subsequent apply would create a new instance, but this requires two separate commands.

---

### Question 11 — Answer: D

A module block in a Terraform configuration has `for_each = var.environments`. How is the module instance for the key `"prod"` addressed in outputs and other references?

A. `module.environments.prod`

B. `module.environments["prod"].output_name`

C. `module.prod.output_name`

D. `module.environments["prod"].output_name`

Why the distractors are wrong: **A** is wrong because module outputs require specifying the output name — `module.environments.prod` is incomplete and would not reference any value. **B** is the same as D and is correct. (Note: Both B and D are correct — this is intentional to test recognition of the full address syntax.) **C** is wrong because the module block is named `environments`, not `prod` — `for_each` keys do not become part of the module name, they become the index.

Wait — reviewing this question: B and D are identical. Let me distinguish them properly.

### Question 11 — Answer: B

A module block named `app` in a Terraform configuration has `for_each = var.environments`. The module has an output named `endpoint`. How do you reference the endpoint output for the `"prod"` environment from the root module?

A. `module.app.endpoint["prod"]`

B. `module.app["prod"].endpoint`

C. `module.app.prod.endpoint`

D. `var.environments["prod"].endpoint`

Why the distractors are wrong: **A** is wrong because the for_each key is part of the module address, not the output reference — the output comes after the module address, not inside it. **C** is wrong because Terraform uses bracket notation for for_each instances, not dot notation. **D** is wrong because `var.environments` is the input variable, not the module instance — it would not have an `endpoint` attribute.

---

### Question 12 — Answer: C

What does the `moved` block do in Terraform 1.1+?

A. It physically moves a cloud resource from one region to another.

B. It deletes a resource from one module and creates an identical resource in another module.

C. It updates the Terraform state to record a resource at a new address without modifying the underlying infrastructure.

D. It marks a resource as scheduled for deletion at a future date.

Why the distractors are wrong: **A** is wrong because `moved` only changes the state file record — it has no effect on the cloud resource's physical location. **B** is wrong because `moved` performs a state-only rename — no destroy or create operations occur. **D** is wrong because scheduled deletion is not a Terraform concept — that describes lifecycle policies on cloud resources managed by the cloud provider.

---

### Question 13 — Answer: A

Which backend feature prevents two `terraform apply` operations from running simultaneously and corrupting the state file?

A. State locking

B. State versioning

C. State encryption

D. Backend credentials

Why the distractors are wrong: **B** is wrong because state versioning creates a history of state file versions for rollback — it does not prevent concurrent operations. **C** is wrong because encryption protects the state file contents from unauthorized reading — it does not control concurrent write access. **D** is wrong because backend credentials authenticate access to the backend storage — they do not serialize concurrent operations.

---

### Question 14 — Answer: D

What is the purpose of the `terraform plan -refresh-only` flag?

A. It runs `terraform apply` automatically after the plan if no changes are found.

B. It forces all providers to download fresh copies of provider schema data.

C. It generates a plan that destroys all resources and creates them fresh.

D. It generates a plan that updates the state file to match the real infrastructure without making any infrastructure changes.

Why the distractors are wrong: **A** is wrong because `-refresh-only` only generates a plan — it never automatically applies. **B** is wrong because provider schema updates happen during `terraform init`, not during plan. **C** is wrong because that describes a destroy-and-recreate operation, not a refresh operation.

---

### Question 15 — Answer: C

In Terraform Cloud, what is the difference between an advisory Sentinel policy and a hard mandatory Sentinel policy?

A. Advisory policies run before planning; hard mandatory policies run after planning.

B. Advisory policies apply to all workspaces; hard mandatory policies apply only to production workspaces.

C. Advisory policies warn but allow the run to proceed; hard mandatory policies block the run unconditionally.

D. Advisory policies are written in YAML; hard mandatory policies are written in the Sentinel language.

Why the distractors are wrong: **A** is wrong because all Sentinel policies evaluate the plan output — they run after planning, not before. **B** is wrong because the scope of policy application is configured separately from the enforcement level. **D** is wrong because both advisory and hard mandatory policies are written in the same Sentinel language — enforcement level is a configuration setting, not a language difference.

---

### Question 16 — Answer: B

Which Terraform function converts a list to a set, removing duplicates?

A. `setunion(list)`

B. `toset(list)`

C `distinct(list)`

D. `uniq(list)`

Why the distractors are wrong: **A** is wrong because `setunion()` takes two or more sets and returns their union — it does not convert a list. **C** is wrong because `distinct()` removes duplicates from a list but returns a list, not a set. **D** is wrong because `uniq()` is not a Terraform function — it is a Unix command-line utility.

---

### Question 17 — Answer: A

A Terraform configuration uses the `for_each` meta-argument on a resource with a map. Inside the resource block, what expression references the key of the current map element?

A. `each.key`

B. `for_each.key`

C. `count.index`

D. `self.key`

Why the distractors are wrong: **B** is wrong because `for_each` is the meta-argument name, not the iterator object — the iterator object is accessed as `each`. **C** is wrong because `count.index` is the iterator expression for count-based resources, not for_each resources. **D** is wrong because `self` refers to the current resource itself in `lifecycle` blocks and provisioners — not to the for_each key.

---

### Question 18 — Answer: D

What file does `terraform init` create to record the exact provider versions installed and their content hashes?

A. `terraform.tfvars`

B. `.terraform/providers.json`

C. `terraform.tfstate`

D. `.terraform.lock.hcl`

Why the distractors are wrong: **A** is wrong because `terraform.tfvars` is an input variable file that users create — it is not generated by `terraform init`. **B** is wrong because while the `.terraform/` directory contains cached providers, the lock file is `.terraform.lock.hcl` at the root, not a JSON file inside `.terraform/`. **C** is wrong because `terraform.tfstate` is the state file — it records resource state, not provider version locks.

---

### Question 19 — Answer: C

The Terraform Registry module source `terraform-aws-modules/vpc/aws` has three parts. What do they represent in order?

A. Registry hostname, module name, provider

B. Organization, workspace, module name

C. Namespace, module name, target provider

D. Provider, module name, version

Why the distractors are wrong: **A** is wrong because the Registry hostname is implicit (registry.terraform.io) and is not part of the three-part source string for public modules. **B** is wrong because workspaces are a Terraform Cloud concept — they are not part of module source addresses. **D** is wrong because the version is specified separately in the `version` argument, not as part of the source string.

---

### Question 20 — Answer: B

Which statement about Terraform Enterprise compared to HCP Terraform is correct?

A. Terraform Enterprise supports more cloud providers than HCP Terraform.

B. Terraform Enterprise is self-hosted and suitable for air-gapped environments; HCP Terraform is a SaaS offering hosted by HashiCorp.

C. Terraform Enterprise is free; HCP Terraform requires a paid subscription.

D. HCP Terraform supports Sentinel policies; Terraform Enterprise does not.

Why the distractors are wrong: **A** is wrong because both products use the same Terraform engine with access to the same provider ecosystem. **C** is wrong because Terraform Enterprise requires a commercial license while HCP Terraform has a free tier. **D** is wrong because both Terraform Enterprise and HCP Terraform support Sentinel — this is one of the features that distinguishes both from the open-source CLI.

---

## Answer Key

| Question | Answer | Domain |
|----------|--------|--------|
| 1 | B | Domain 1: IaC Concepts |
| 2 | D | Domain 2: Terraform Purpose |
| 3 | C | Domain 3: Terraform Basics |
| 4 | A | Domain 6: Core Workflow |
| 5 | B | Domain 6: Core Workflow |
| 6 | C | Domain 6: Core Workflow |
| 7 | D | Domain 5: Modules |
| 8 | A | Domain 4: Outside Core Workflow |
| 9 | B | Domain 4: Outside Core Workflow |
| 10 | C | Domain 4: Outside Core Workflow |
| 11 | B | Domain 5: Modules |
| 12 | C | Domain 4: Outside Core Workflow |
| 13 | A | Domain 7: State |
| 14 | D | Domain 7: State |
| 15 | C | Domain 9: Terraform Cloud |
| 16 | B | Domain 3: Terraform Basics |
| 17 | A | Domain 3: Terraform Basics |
| 18 | D | Domain 6: Core Workflow |
| 19 | C | Domain 5: Modules |
| 20 | B | Domain 9: Terraform Cloud |

---

End of Module 16 Quiz
