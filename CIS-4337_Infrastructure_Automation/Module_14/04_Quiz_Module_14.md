# Quiz: Module 14 — Multi-Cloud Provisioning with Terraform

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Select the best answer for each question. Each question is worth 1 point. Distractor analysis follows each question to explain why incorrect options are wrong.

---

## Questions

### Question 1 — Answer: B

A Terraform configuration has two `provider "aws"` blocks. The first has no `alias` attribute. The second has `alias = "west"`. How does Terraform determine which provider to use for a given resource?

A. Terraform uses the second provider block for all resources because it is more specific.

B. Resources without a `provider` meta-argument use the default (no alias) provider; resources with `provider = aws.west` use the aliased provider.

C. Terraform alternates between providers for each resource in declaration order.

D. Both providers are used for every resource to ensure cross-region redundancy.

Why the distractors are wrong: **A** is wrong because a provider block with an alias is not "more specific" — it is simply an additional instance. The default (no alias) provider is used unless explicitly overridden. **C** is wrong because Terraform never alternates providers automatically — the provider meta-argument is always explicit. **D** is wrong because Terraform creates each resource with exactly one provider instance, not both.

---

### Question 2 — Answer: C

You want to pass an aliased provider to a child module so the module deploys resources in a different AWS region than the default. Which configuration achieves this?

A. Set the `region` variable in the module block to the target region.

B. Declare a second `provider` block inside the child module with the target region.

C. Use the `providers` map in the module block to pass the aliased provider instance.

D. Set the `AWS_DEFAULT_REGION` environment variable before calling the module.

Why the distractors are wrong: **A** is wrong because the `region` variable in the module would be an input variable, not a provider configuration — the module would still use whatever provider it is configured with. **B** is wrong because declaring a provider inside a child module creates a new independent provider instance, not the aliased one from the parent — and mixing provider declarations between parent and child is a pattern Terraform discourages. **D** is wrong because the environment variable affects the default provider but does not control which aliased provider instance a module receives.

---

### Question 3 — Answer: D

What does the `.terraform.lock.hcl` file record, and why must it be committed to version control?

A. It records the Terraform CLI version required and prevents version mismatches.

B. It records the backend configuration so engineers do not need to re-run `terraform init`.

C. It records the names and addresses of all resources in the configuration for documentation.

D. It records resolved provider versions and content hashes, ensuring all team members and CI runners use identical provider binaries.

Why the distractors are wrong: **A** is wrong because the required Terraform CLI version is specified in `required_version` in the `terraform` block, not in the lock file. **B** is wrong because backend configuration is in the `backend` block and the `.terraform` directory — not in the lock file. **C** is wrong because resource state is in `terraform.tfstate` — the lock file contains only provider version and hash information.

---

### Question 4 — Answer: A

A provider is currently installed at version 5.8.2 and the lock file records this version. The `required_providers` constraint is `~> 5.0`. You run `terraform init` without any flags. What happens?

A. Terraform uses version 5.8.2 as recorded in the lock file without downloading anything new.

B. Terraform downloads the newest 5.x version available and updates the lock file automatically.

C. Terraform fails because the installed version does not match the constraint exactly.

D. Terraform prompts you to choose between the lock file version and the latest available version.

Why the distractors are wrong: **B** is wrong because `terraform init` without `-upgrade` respects the lock file and does not automatically update to newer versions. **C** is wrong because `~> 5.0` allows any 5.x version; 5.8.2 satisfies the constraint and there is no conflict. **D** is wrong because `terraform init` does not prompt for version choices — it either uses the lock file or, with `-upgrade`, downloads the newest satisfying version.

---

### Question 5 — Answer: B

An AWS provider block includes `assume_role { role_arn = "arn:aws:iam::123456789:role/TerraformExecutor" }`. What does this configuration do?

A. It grants the TerraformExecutor role permissions to read from the Terraform state file.

B. It causes Terraform to call AWS STS AssumeRole and use the resulting temporary credentials for all API calls made by that provider instance.

C. It restricts Terraform to only creating resources with the ARN prefix of the specified role.

D. It configures AWS IAM to automatically rotate the credentials used by this provider block.

Why the distractors are wrong: **A** is wrong because state file access is a backend concern, not related to the assume_role configuration in the provider block. **C** is wrong because assume_role controls authentication, not resource ARN filtering. **D** is wrong because assume_role performs a one-time role assumption — it does not configure IAM credential rotation.

---

### Question 6 — Answer: C

Which version constraint allows versions 5.12.0, 5.12.5, and 5.12.10, but NOT versions 5.13.0 or 6.0.0?

A. `>= 5.12.0, < 6.0.0`

B. `~> 5.0`

C. `~> 5.12.3`

D. `= 5.12`

Why the distractors are wrong: **A** is wrong because `>= 5.12.0, < 6.0.0` would allow 5.13.0, 5.14.0, etc. — not limited to 5.12.x. **B** is wrong because `~> 5.0` allows all 5.x versions including 5.13.0. **D** is wrong because `= 5.12` is not valid semantic versioning syntax — it would need to be `= 5.12.0` for an exact match, which would exclude 5.12.5 and 5.12.10.

---

### Question 7 — Answer: A

Your organization runs 20 different Terraform workspaces across 5 AWS accounts. Each workspace manages different resources. You need a single CI pipeline runner to apply changes to any workspace. What AWS authentication pattern enables this?

A. Configure provider blocks with `assume_role` pointing to a different execution role ARN in each account; the pipeline runner has permission to assume each of those roles.

B. Create a single IAM user with administrator access in each account and store all five sets of credentials as CI secrets.

C. Use AWS Organizations consolidated billing so one account's credentials grant access to all accounts.

D. Deploy the pipeline runner inside each AWS account so it uses the local instance profile.

Why the distractors are wrong: **B** is wrong because storing multiple sets of long-lived administrator credentials is a security anti-pattern — it creates multiple high-value targets. **C** is wrong because consolidated billing provides cost aggregation, not cross-account IAM access. **D** is wrong because this approach requires a separate pipeline runner per account, which defeats the goal of a single pipeline runner.

---

### Question 8 — Answer: B

What is the primary operational reason multi-cloud active-active architectures are expensive compared to multi-region single-cloud architectures?

A. Multi-cloud requires purchasing Terraform Enterprise licenses for each cloud provider.

B. Data transfer between cloud providers incurs egress fees from both providers, which accumulate rapidly with continuous replication or API traffic.

C. Multi-cloud active-active requires paying for twice as many Terraform state files.

D. Cloud providers charge extra fees for resources that are managed by Terraform rather than their own native tools.

Why the distractors are wrong: **A** is wrong because Terraform open-source supports all cloud providers without additional licensing. **C** is wrong because state files are small and state backend costs are negligible. **D** is wrong because cloud providers do not distinguish between Terraform-provisioned and console-provisioned resources in their pricing.

---

### Question 9 — Answer: D

A Terraform configuration manages an AWS VPC and uses the VPC's CIDR block as an input to an Azure Virtual Network peering resource. What does Terraform do when it encounters this cross-provider dependency?

A. Terraform refuses to plan across providers and requires the resources to be in separate workspaces.

B. Terraform creates both resources in parallel because it cannot determine dependencies across providers.

C. Terraform creates the Azure resource first because Azure provider blocks are processed before AWS blocks.

D. Terraform builds a unified dependency graph across all providers and creates the AWS VPC first, then passes its output to the Azure resource.

Why the distractors are wrong: **A** is wrong because Terraform fully supports cross-provider dependencies within a single workspace. **B** is wrong because Terraform resolves dependencies regardless of provider — it does not create resources in parallel when one depends on another. **C** is wrong because provider block order in the configuration does not determine resource creation order — the dependency graph does.

---

### Question 10 — Answer: C

Which multi-cloud pattern uses each cloud provider specifically for its strongest services rather than deploying the same application in multiple clouds?

A. Active-active multi-cloud

B. Primary-failover multi-cloud

C. Best-of-breed service selection

D. Cloud-agnostic abstraction

Why the distractors are wrong: **A** is wrong because active-active deploys the same application workload in both clouds simultaneously for resilience. **B** is wrong because primary-failover keeps one cloud as standby for the primary's workload. **D** is wrong because cloud-agnostic abstraction attempts to write infrastructure code that works identically on any cloud, which is a different strategy from selecting clouds for specific strengths.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | C |
| 3 | D |
| 4 | A |
| 5 | B |
| 6 | C |
| 7 | A |
| 8 | B |
| 9 | D |
| 10 | C |

---

End of Module 14 Quiz
