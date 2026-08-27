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

### Question 11 — Answer: C

A Terraform configuration has `required_providers` declaring the `aws` provider with `version = "~> 5.12.3"`. The current lock file records version `5.12.5`. A developer runs `terraform init`. What is the result?

A. Terraform downloads version 5.12.3 because the constraint specifies that exact patch starting point.

B. Terraform downloads the newest available 5.x version regardless of the lock file.

C. Terraform uses version 5.12.5 as recorded in the lock file because `~> 5.12.3` allows `5.12.5` and the lock file version satisfies the constraint.

D. Terraform fails because `5.12.5` is higher than `5.12.3` and does not exactly match.

Why the distractors are wrong: **A** is wrong because `~>` is a range operator, not an exact match — `5.12.5` satisfies `~> 5.12.3`. **B** is wrong because `terraform init` without `-upgrade` does not override the lock file. **D** is wrong because `~> 5.12.3` means >= 5.12.3, < 5.13.0; version 5.12.5 is within this range and is valid.

---

### Question 12 — Answer: D

A root module uses two aliased AWS providers: `aws` (default, us-east-1) and `aws.west` (us-west-2). A child module `module "app"` is called with `providers = { aws = aws.west }`. Inside the child module, all resource blocks reference only the default `aws` provider (no explicit `provider` meta-argument). What region do the child module's resources deploy to?

A. us-east-1, because child modules always use the root module's default provider.

B. Both us-east-1 and us-west-2, because the module inherits the parent's default and receives the aliased provider.

C. Neither — the configuration fails because the child module does not declare a `required_providers` block.

D. us-west-2, because the `providers` map remaps the child module's `aws` to `aws.west` from the parent, so all `aws` resources in the child use us-west-2.

Why the distractors are wrong: **A** is wrong because the `providers` map overrides which provider instance the child module uses; child modules do not automatically inherit the parent's default. **B** is wrong because each resource has exactly one provider; the `providers` map replaces the child's default with the specified alias. **C** is wrong because child modules do not need their own `required_providers` — they inherit provider requirements from the calling configuration.

---

### Question 13 — Answer: B

You have a Terraform configuration managing both AWS and Azure resources. The Azure `azurerm_virtual_network` resource needs to use a CIDR block that was determined as an output of an `aws_vpc` resource. Without any explicit `depends_on`, how does Terraform handle the ordering?

A. Terraform creates both resources simultaneously because they belong to different providers.

B. Terraform automatically creates the `aws_vpc` first because the `azurerm_virtual_network` references its output; the reference creates an implicit dependency.

C. Terraform creates the `azurerm_virtual_network` first because Azure resources are alphabetically before AWS.

D. Terraform requires an explicit `depends_on = [aws_vpc.main]` in the Azure resource because cross-provider dependencies are not tracked automatically.

Why the distractors are wrong: **A** is wrong because Terraform evaluates dependencies across all providers in the same configuration; a reference between resources of different providers creates an implicit dependency. **C** is wrong because alphabetical order plays no role in Terraform's resource creation ordering — the dependency graph determines order. **D** is wrong because implicit dependencies from attribute references work across providers; `depends_on` is only needed when the dependency cannot be expressed as a reference.

---

### Question 14 — Answer: A

`terraform init -upgrade` is run in a directory where `.terraform.lock.hcl` records `aws` version `5.8.0` and `required_providers` specifies `~> 5.0`. The newest available version satisfying `~> 5.0` is `5.15.2`. What does `-upgrade` do?

A. It downloads version 5.15.2 and updates the lock file to record this new version and its content hashes.

B. It downloads version 5.15.2 but does not change the lock file to preserve reproducibility.

C. It fails because the lock file version and the constraint conflict.

D. It upgrades the Terraform CLI to the latest version before downloading providers.

Why the distractors are wrong: **B** is wrong because the entire purpose of `-upgrade` is to update both the downloaded provider AND the lock file to the new version. **C** is wrong because there is no conflict — `5.8.0` satisfies `~> 5.0` and so does `5.15.2`; `-upgrade` simply selects the newer one. **D** is wrong because `terraform init -upgrade` operates on provider plugins, not the Terraform CLI binary.

---

### Question 15 — Answer: C

A team wants their Terraform configuration to use an exact provider version in CI to guarantee identical builds across all environments and prevent any automatic updates. Which constraint pattern achieves this?

A. `version = "~> 5.12"` — prevents major and minor updates

B. `version = ">= 5.12.0"` — allows any version 5.12.0 and above

C. `version = "= 5.12.3"` — pins to exactly one version

D. Committing `.terraform.lock.hcl` — the lock file guarantees the exact version without needing a pinned constraint

Why the distractors are wrong: **A** is wrong because `~> 5.12` still allows patch updates (5.12.1, 5.12.5, etc.) and could return different provider binaries in different environments if the lock file is absent. **B** is wrong because `>= 5.12.0` allows any future version including major versions with breaking changes. **D** is partially correct but incomplete — without a pinned constraint, `terraform init -upgrade` can still update the lock file to a newer version, breaking the guarantee.

---

### Question 16 — Answer: B

A Terraform plan output shows the resource address `module.west_app.aws_s3_bucket.main`. What does this address indicate?

A. The resource was created with `count` and the index `west_app` references the second instance.

B. The resource `aws_s3_bucket.main` was created by the child module called `west_app` in the root configuration.

C. The resource is an aliased provider reference using the `west_app` alias.

D. The resource is managed by Terraform Cloud workspace `west_app`.

Why the distractors are wrong: **A** is wrong because count indices are numeric (e.g., `module.app[1]`), not string labels — `module.west_app` uses the module block name, not a count index. **C** is wrong because provider aliases appear in the provider block, not in resource addresses. **D** is wrong because Terraform Cloud workspace names do not appear in resource addresses.

---

### Question 17 — Answer: D

Your organization prohibits deploying cloud resources to any region other than `us-east-2` due to data residency requirements. You are building a new Terraform module used by 15 different teams. What is the best way to enforce this constraint in the module itself?

A. Add a comment in `variables.tf` warning engineers not to change the region.

B. Set `default = "us-east-2"` on the `region` variable so it defaults correctly.

C. Hard-code the region inside the provider block in the module.

D. Add a `validation` block to the region input variable that enforces `var.region == "us-east-2"`.

Why the distractors are wrong: **A** is wrong because comments are not enforced — they rely on engineers reading and following guidance. **B** is wrong because a default can be overridden with `-var` or `.tfvars` files; it does not prevent a different value from being passed. **C** is wrong because hard-coding provider configuration inside a module makes the module inflexible and couples it to a specific account credential model — provider configuration should be passed in from the calling configuration.

---

### Question 18 — Answer: A

A company is evaluating multi-cloud to achieve "cloud provider independence" and avoid vendor lock-in. Their primary workload uses AWS Lambda, AWS Aurora Serverless, and CloudFront. What is the most accurate assessment of this strategy?

A. The workloads are already deeply cloud-specific; achieving true portability would require replacing them with generic compute, open-source databases, and generic CDN services — which would sacrifice the features that make them valuable.

B. Terraform's cloud-agnostic HCL syntax means the code is already portable and can be applied to any cloud provider.

C. The multi-cloud strategy is unnecessary because AWS guarantees service availability.

D. Switching to Azure would achieve the same functionality with equivalent managed services at lower cost.

Why the distractors are wrong: **B** is wrong because HCL is syntactically portable but the resource types (`aws_lambda_function`, `aws_rds_cluster`) are cloud-specific; changing clouds requires rewriting the Terraform code and the application. **C** is wrong because provider availability concerns are a legitimate driver for multi-cloud consideration — this distractor avoids the real question of whether the strategy achieves portability. **D** is wrong because equivalent managed services exist but the migration cost is high and the result is still vendor lock-in, just on a different vendor.

---

### Question 19 — Answer: C

A Terraform configuration has three providers: `aws`, `azurerm`, and `google`. Running `terraform init` downloads provider plugins. Where are these plugins stored?

A. In the system-wide Terraform binary directory alongside the `terraform` executable.

B. In `~/.terraform.d/plugins/` in the user's home directory, shared across all configurations.

C. In `.terraform/providers/` within the current working directory, specific to this configuration.

D. In the operating system's package manager cache (e.g., `/usr/lib/terraform-providers/`).

Why the distractors are wrong: **A** is wrong because provider plugins are not stored alongside the CLI binary; they are downloaded per-project. **B** is wrong because `.terraform.d/plugins/` is a legacy caching location from older Terraform versions; current Terraform downloads providers to `.terraform/providers/` in the project directory. **D** is wrong because Terraform manages its own plugin downloads independently of the OS package manager.

---

### Question 20 — Answer: B

An enterprise Terraform configuration assumes different IAM roles for a networking account (111111111111) and a workloads account (222222222222). The pipeline runner's initial identity has permission to assume both roles. When Terraform provisions an `aws_vpc` that uses `provider = aws.networking` and an `aws_instance` that uses `provider = aws.workloads`, what AWS API calls happen at apply time?

A. A single STS AssumeRole call with both role ARNs combined into one request.

B. Two separate STS AssumeRole calls — one per provider instance — with each provider receiving its own temporary credentials scoped to its respective role.

C. No STS calls — `assume_role` in the provider block is evaluated during plan only and credentials are cached.

D. STS calls happen only for the first provider block defined in the configuration; subsequent provider blocks reuse the same credentials.

Why the distractors are wrong: **A** is wrong because AWS STS does not support multi-role assumption in a single API call; each `AssumeRole` call targets exactly one role ARN. **C** is wrong because temporary credentials from STS have a TTL; new credentials are obtained as needed during apply. **D** is wrong because each aliased provider instance maintains its own authentication state and independently assumes its configured role.

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
| 11 | C |
| 12 | D |
| 13 | B |
| 14 | A |
| 15 | C |
| 16 | B |
| 17 | D |
| 18 | A |
| 19 | C |
| 20 | B |

---

End of Module 14 Quiz
