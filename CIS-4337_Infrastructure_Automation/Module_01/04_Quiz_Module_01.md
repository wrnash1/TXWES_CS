# CIS-4337 Infrastructure Automation

## Quiz — Module 01: IaC Concepts and Benefits

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What is the primary advantage of the declarative IaC model over imperative scripting?

- A) Declarative configurations require you to detail every deployment command step by step.
- B) Declarative configurations define the desired end state and let the tool determine how to achieve it.
- C) Declarative configurations always execute faster than imperative scripts.
- D) Declarative configurations do not require any files to be stored on disk.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Terraform's declarative model means you write HCL describing what you want to exist. Terraform computes the required API calls, dependency order, and error handling automatically. You specify the destination, not the route.
- Why A is incorrect: Describing every step is the defining characteristic of imperative scripting, not declarative IaC.
- Why C is incorrect: Execution speed is not what distinguishes the declarative model. The defining benefit is idempotency and automatic dependency resolution, not raw speed.
- Why D is incorrect: Declarative IaC absolutely requires configuration files. In Terraform, those are `.tf` files written in HCL.

---

### Question 2

Which of the following most accurately defines configuration drift in a Terraform-managed environment?

- A) The automatic horizontal scaling of cloud resources in response to increased CPU utilization.
- B) The migration of a Terraform state file from a local directory to a remote backend.
- C) The divergence between the actual deployed state of infrastructure and the desired state declared in Terraform code, typically caused by out-of-band manual changes.
- D) The incremental version history of `.tf` files accumulated in a Git repository over time.

Correct Answer: C

Distractor Analysis:

- Why C is correct: Drift occurs when someone makes a change to live infrastructure — for example, editing a security group rule in the AWS console — without updating the corresponding Terraform configuration. The real state and the declared state no longer agree.
- Why A is incorrect: Auto-scaling is a cloud platform feature that adjusts resource capacity. It has no relation to the concept of configuration drift.
- Why B is incorrect: Moving state to a remote backend is a backend migration operation, not drift.
- Why D is incorrect: Git history records code changes over time. Drift is about the gap between code and live infrastructure, not about version history.

---

### Question 3

A developer manually changes an S3 bucket's ACL setting through the AWS console without updating the Terraform configuration. What will `terraform plan` report on the next run?

- A) No changes — Terraform ignores out-of-band changes to managed resources.
- B) A proposed change to revert the ACL setting to the value declared in the HCL configuration.
- C) An immediate automatic rollback is triggered without requiring an apply.
- D) The state file becomes permanently corrupted and must be rebuilt from scratch.

Correct Answer: B

Distractor Analysis:

- Why B is correct: During `terraform plan`, Terraform refreshes its knowledge of live resource attributes by querying provider APIs. When it detects that the actual ACL differs from what HCL declares, it proposes a change to reconcile the difference.
- Why A is incorrect: Ignoring out-of-band changes would defeat the core purpose of IaC. Terraform detects and surfaces drift as a planned change.
- Why C is incorrect: Terraform never automatically applies changes. The plan phase is always a read-only preview; changes require an explicit `terraform apply`.
- Why D is incorrect: A manual console change does not touch the state file at all. The state file remains intact; it simply no longer reflects the current live state until the next plan refreshes it.

---

### Question 4

Which of the following best describes the role of the `terraform.tfstate` file?

- A) A compiled binary that Terraform executes when provisioning infrastructure resources.
- B) A log file that records every CLI command ever run in the working directory.
- C) A JSON record that maps Terraform resource declarations to the real-world IDs and current attributes of provisioned resources.
- D) A template file that auto-generates HCL configurations from cloud resource metadata.

Correct Answer: C

Distractor Analysis:

- Why C is correct: The state file is Terraform's source of truth about what it manages. It stores real resource IDs, current attribute values, and resource dependencies so Terraform can compute accurate diffs on subsequent runs.
- Why A is incorrect: Terraform is not compiled and does not produce executables. The `.tfstate` file is a plain JSON text file.
- Why B is incorrect: CLI command history is maintained by the shell, not by Terraform. The state file records resource state, not command history.
- Why D is incorrect: Terraform does not auto-generate HCL from resource metadata. You write HCL manually, and `terraform import` can bring existing resources into state management, but it still requires hand-written resource blocks.

---

### Question 5

An organization wants to prevent configuration drift caused by team members making ad-hoc changes through the AWS console. Which practice best addresses this problem?

- A) Enforce an IaC-only policy requiring all infrastructure changes to flow through reviewed Terraform code, and restrict direct console access using IAM permission boundaries.
- B) Schedule nightly `terraform destroy` runs to reset all infrastructure to a known clean state.
- C) Store the `terraform.tfstate` file on a shared network drive accessible to all team members simultaneously without file locking.
- D) Run `terraform taint` on every resource before each deployment to force recreation of all resources.

Correct Answer: A

Distractor Analysis:

- Why A is correct: Combining an IaC-only change policy with IAM restrictions eliminates the source of drift. If team members cannot make manual console changes, they cannot create drift. Code review catches unintended changes before apply.
- Why B is incorrect: Nightly destroys would delete production workloads. This is not a drift prevention strategy; it is a data-loss strategy.
- Why C is incorrect: Sharing a state file without locking leads to concurrent write conflicts and state corruption. This is a well-documented anti-pattern.
- Why D is incorrect: Tainting forces resource recreation on the next apply but does nothing to prevent team members from making manual changes. It does not address the root cause of drift.

---

### Question 6

Which of the following characteristics distinguishes Terraform from AWS CloudFormation?

- A) Terraform uses an imperative model while CloudFormation uses a declarative model.
- B) Terraform requires manual state management while CloudFormation manages state automatically.
- C) Terraform can manage resources across multiple cloud providers and SaaS platforms while CloudFormation is limited to AWS resources.
- D) Terraform is a commercial product that requires a paid license while CloudFormation is free.

Correct Answer: C

Distractor Analysis:

- Why C is correct: Terraform's provider model enables a single configuration to manage AWS, Azure, Google Cloud, GitHub, Datadog, and hundreds of other platforms simultaneously. CloudFormation only manages AWS resources.
- Why A is incorrect: Both Terraform and CloudFormation use the declarative model. You describe desired state in both tools.
- Why B is incorrect: Both tools maintain state. Terraform uses `.tfstate` files or remote backends. CloudFormation maintains stack state internally within the AWS service.
- Why D is incorrect: The open-source Terraform CLI is free. CloudFormation is also free. Paid tiers exist for Terraform Cloud and Terraform Enterprise, but the CLI itself does not require a license.

---

### Question 7

What does the term "idempotent" mean in the context of Terraform?

- A) Terraform can only be run once per infrastructure environment before requiring a full reinstall.
- B) Running `terraform apply` multiple times with the same configuration produces the same result — no additional changes are made if infrastructure already matches the declared state.
- C) Terraform automatically scales resources up and down based on current workload demand.
- D) Terraform generates a unique random identifier for every resource on each run to ensure freshness.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Idempotency is a core property of Terraform's declarative model. If the live infrastructure already matches the HCL configuration, `terraform apply` makes zero changes. You can run it safely any number of times.
- Why A is incorrect: Terraform can be run any number of times. There is no one-run limit.
- Why C is incorrect: Auto-scaling is a cloud platform feature configured through resource attributes. It is not what idempotent means.
- Why D is incorrect: Terraform does not generate new random identifiers on every run. Resource IDs are assigned once at creation and remain stable across subsequent applies.

---

### Question 8

In the Terraform Write-Plan-Apply workflow, what is the specific purpose of the `terraform plan` command?

- A) It downloads and installs all required provider plugins into the working directory.
- B) It applies configuration changes immediately without showing a preview.
- C) It computes and displays an execution plan showing what changes Terraform will make, without actually making any changes.
- D) It permanently deletes all resources managed by the current configuration.

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform plan` is a read-only operation. It refreshes state, computes the diff between desired and current state, and displays a detailed preview of every planned action. No resources are created, modified, or destroyed.
- Why A is incorrect: Downloading and installing provider plugins is the job of `terraform init`.
- Why B is incorrect: Applying changes without a preview describes `terraform apply -auto-approve`, not `terraform plan`. Even `terraform apply` without flags shows the plan and requires confirmation.
- Why D is incorrect: Destroying all managed resources is the job of `terraform destroy`.

---

### Question 9

Which of the following is a correct statement about the `.terraform.lock.hcl` file created by `terraform init`?

- A) It prevents any other user from running Terraform commands in the same directory simultaneously.
- B) It records the exact versions of provider plugins selected during initialization so that subsequent runs use the same versions.
- C) It encrypts the state file to prevent unauthorized access to sensitive resource attributes.
- D) It stores the Terraform execution plan from the most recent `terraform plan` run.

Correct Answer: B

Distractor Analysis:

- Why B is correct: The dependency lock file records the exact provider version selected during `terraform init`, along with checksums. This ensures that all team members and CI/CD pipelines use identical provider versions, preventing "works on my machine" problems.
- Why A is incorrect: File-level locking to prevent concurrent CLI runs is not what `.terraform.lock.hcl` does. State locking (preventing concurrent applies) is handled by backends, not by this file.
- Why C is incorrect: The lock file does not encrypt the state file. State encryption is handled separately through backend configuration or Terraform Cloud.
- Why D is incorrect: Execution plans are not stored in the lock file. A plan can be saved to a binary file using `terraform plan -out=tfplan`, but that is a separate artifact.

---

### Question 10

A team is deciding whether to use Terraform or Ansible for provisioning new cloud infrastructure. Based on the IaC principles covered in this module, which statement best justifies choosing Terraform for this task?

- A) Ansible is declarative and therefore better suited to describing desired infrastructure state.
- B) Terraform's declarative model and state management make it purpose-built for provisioning infrastructure and tracking resource lifecycle, while Ansible is better suited to configuring software on existing servers.
- C) Terraform and Ansible are functionally identical; the choice depends only on personal preference.
- D) Ansible should always be chosen over Terraform because it supports more cloud providers.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Terraform is designed for infrastructure provisioning — creating, modifying, and destroying cloud resources. Its state file tracks resource lifecycle. Ansible excels at configuration management: installing packages, managing files, and configuring services on existing servers. The two tools are complementary, not interchangeable.
- Why A is incorrect: Ansible can be used in a declarative style, but it is primarily an imperative task-execution engine. Terraform is the more consistently declarative tool for infrastructure provisioning.
- Why C is incorrect: The two tools have distinct design philosophies, strengths, and use cases. The choice is not arbitrary.
- Why D is incorrect: Ansible does not support more cloud providers than Terraform in the infrastructure provisioning context. Terraform's provider ecosystem is among the largest in the industry.

---

---

### Question 11 (5 points)

Which Terraform CLI command should always be run first when working in a new or cloned configuration directory?

- A) `terraform plan`
- B) `terraform validate`
- C) `terraform init`
- D) `terraform apply`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `terraform init` downloads provider plugins, initializes the backend, and prepares the working directory. Without it, no other command can succeed because the required plugins are absent.
  - Why A is incorrect: `terraform plan` will fail if `terraform init` has not been run, because there are no provider plugins available to contact APIs or validate resource types.
  - Why B is incorrect: `terraform validate` checks HCL syntax but also requires that `terraform init` has been run so the provider schemas are available for type checking.
  - Why D is incorrect: `terraform apply` requires both initialized plugins and a valid plan. Running it first in an uninitialized directory will produce an error.

---

### Question 12 (5 points)

A team stores their `terraform.tfstate` file in a public GitHub repository alongside their `.tf` files. What is the primary security risk of this practice?

- A) The state file will cause merge conflicts that corrupt the HCL configuration files.
- B) GitHub will automatically delete state files larger than 1 MB.
- C) Sensitive values such as database passwords and private keys written to state by providers may be exposed to anyone with repository access.
- D) Terraform will refuse to read a state file that originated from a Git repository.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Many providers store sensitive resource attributes — RDS master passwords, IAM access keys, TLS private keys — in plain text within the state file. Committing it to a public (or even private) repository creates an unacceptable credential exposure risk.
  - Why A is incorrect: The state file is a separate JSON artifact from HCL files. Merge conflicts are a workflow concern, not a security risk, and do not corrupt configuration files.
  - Why B is incorrect: GitHub has no special behavior that deletes state files based on size. This is a fabricated constraint.
  - Why D is incorrect: Terraform reads state files from wherever the backend is configured to store them. It does not inspect file origin or reject files based on source location.

---

### Question 13 (5 points)

What is the purpose of the `terraform fmt` command?

- A) It formats and reformats cloud resource names to comply with provider naming conventions.
- B) It applies canonical HCL indentation and style to `.tf` files without changing their logic.
- C) It compresses the state file to reduce storage size on the backend.
- D) It validates that all provider API calls will succeed before running `terraform apply`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform fmt` is a code formatting tool. It rewrites `.tf` files to use consistent indentation, alignment, and spacing according to the canonical HCL style guide. It makes no logical changes to resource declarations.
  - Why A is incorrect: `terraform fmt` does not modify resource names or interact with provider naming conventions. Resource names are defined by the author and cannot be automatically changed without altering semantics.
  - Why C is incorrect: `terraform fmt` operates only on `.tf` source files, not on the state file. State file management is handled by backend configuration.
  - Why D is incorrect: Pre-flight API validation is not a function of `terraform fmt`. `terraform validate` checks configuration syntax, and `terraform plan` contacts provider APIs to compute diffs.

---

### Question 14 (5 points)

In Terraform HCL, what is the correct way to reference the `arn` attribute of a resource named `main_bucket` of type `aws_s3_bucket` within the same configuration?

- A) `var.main_bucket.arn`
- B) `aws_s3_bucket.main_bucket.arn`
- C) `output.main_bucket.arn`
- D) `data.aws_s3_bucket.main_bucket.arn`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Terraform resource references follow the pattern `<resource_type>.<local_name>.<attribute>`. For a resource declared as `resource "aws_s3_bucket" "main_bucket"`, the ARN is referenced as `aws_s3_bucket.main_bucket.arn`.
  - Why A is incorrect: The `var.` prefix is used to reference input variables declared with a `variable` block, not managed resource attributes.
  - Why C is incorrect: The `output.` prefix does not exist as a first-class reference type within configurations. Outputs from child modules are accessed via `module.<name>.<output_name>`.
  - Why D is incorrect: The `data.` prefix is used for data source blocks, which read existing infrastructure. A `resource` block is not a data source.

---

### Question 15 (5 points)

Which of the following best describes a Terraform provider?

- A) A cloud region setting that determines where resources are deployed.
- B) A plugin that translates Terraform resource declarations into API calls for a specific platform or service.
- C) A reusable group of resource blocks that can be instantiated multiple times.
- D) An encrypted vault that stores provider credentials securely within the state file.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: A provider is a plugin distributed by HashiCorp or third parties that knows how to communicate with a specific API (AWS, Azure, GitHub, etc.). It exposes resource types and data sources, and translates Terraform operations into the appropriate API calls.
  - Why A is incorrect: The deployment region is an attribute configured within the provider block, not the definition of a provider itself.
  - Why C is incorrect: A reusable group of resource blocks is called a module, not a provider.
  - Why D is incorrect: Providers do not serve as credential vaults. Credentials are supplied to providers through environment variables, provider block arguments, or secrets managers — but that is the configuration of a provider, not the definition of what a provider is.

---

### Question 16 (5 points)

A `terraform apply` completes successfully and provisions five resources. A team member then deletes two of those resources directly in the cloud console. What happens on the next `terraform apply` without any changes to the `.tf` files?

- A) Terraform ignores the deletion because no `.tf` files changed.
- B) Terraform detects the missing resources during the plan phase and recreates them to match the declared configuration.
- C) Terraform automatically removes the deleted resources from the state file and reports success.
- D) Terraform aborts with a fatal error and requires `terraform destroy` before any further applies can proceed.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: During `terraform plan`, Terraform queries provider APIs to refresh the current state of all managed resources. When it finds that two resources no longer exist, it plans to recreate them so that the live infrastructure matches the `.tf` configuration.
  - Why A is incorrect: Terraform does not condition its behavior solely on whether `.tf` files changed. It compares declared state to live infrastructure state on every run.
  - Why C is incorrect: Terraform does not silently remove managed resources from state because they were deleted externally. That would cause it to lose track of those resources entirely. It plans to recreate them instead.
  - Why D is incorrect: Missing resources are a recoverable drift condition that Terraform handles by planning recreations. It does not abort or require a destroy.

---

### Question 17 (5 points)

Which of the following is the correct definition of a Terraform module?

- A) A single `.tf` file that contains one `resource` block and one `variable` block.
- B) Any directory containing Terraform configuration files, which can be called from another configuration to encapsulate and reuse infrastructure patterns.
- C) The compiled binary artifact that Terraform produces after running `terraform init`.
- D) A cloud-provider-specific API wrapper that replaces the need for a provider plugin.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: In Terraform, any directory with `.tf` files is a module. The root module is the directory where you run Terraform commands. Child modules are directories called using `module` blocks. Modules encapsulate and enable reuse of infrastructure patterns.
  - Why A is incorrect: A module is not restricted to a single file or a specific combination of block types. It is defined by directory structure, not file content limits.
  - Why C is incorrect: Terraform does not produce compiled binary artifacts. `terraform init` downloads provider plugins, but the configuration itself remains as human-readable HCL files.
  - Why D is incorrect: Modules do not replace providers. Providers handle API communication; modules organize and reuse resource configurations that use those providers.

---

### Question 18 (5 points)

What is the significance of the `required_version` constraint in a Terraform settings block?

- A) It specifies the minimum version of the cloud provider CLI that must be installed on the workstation.
- B) It restricts which versions of the Terraform CLI are permitted to execute the configuration, ensuring consistency across teams and CI/CD pipelines.
- C) It defines the maximum number of resources that can be created in a single `terraform apply`.
- D) It sets the expiration date after which the configuration must be reviewed and re-approved.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `required_version` specifies a version constraint (e.g., `">= 1.6.0"`) for the Terraform CLI binary itself. If a team member or CI/CD runner uses a Terraform version that does not satisfy the constraint, the run is rejected. This prevents behavior differences caused by CLI version mismatches.
  - Why A is incorrect: `required_version` applies to the Terraform CLI, not to any cloud provider's own CLI tool (such as `aws` or `az`).
  - Why C is incorrect: There is no built-in resource count limit in Terraform. `required_version` has nothing to do with resource quantities.
  - Why D is incorrect: Terraform has no concept of configuration expiration dates. `required_version` is strictly a version compatibility constraint.

---

### Question 19 (5 points)

Which of the following actions correctly removes a resource from Terraform state management without destroying the actual cloud resource?

- A) Delete the resource block from the `.tf` file and run `terraform apply`.
- B) Run `terraform state rm <resource_address>`.
- C) Run `terraform destroy -target=<resource_address>`.
- D) Delete the `terraform.tfstate` file and run `terraform init`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform state rm` removes a resource from the state file while leaving the actual cloud resource intact. This is useful when you want to stop managing a resource with Terraform (e.g., handing it off to another configuration) without deleting it.
  - Why A is incorrect: Deleting a resource block from `.tf` files and running `terraform apply` will cause Terraform to destroy the corresponding cloud resource, because it concludes the resource should no longer exist.
  - Why C is incorrect: `terraform destroy -target` destroys the actual cloud resource. It does not simply untrack it; it deletes it.
  - Why D is incorrect: Deleting the entire state file causes Terraform to lose track of all managed resources and will attempt to recreate everything on the next apply, potentially creating duplicate resources.

---

### Question 20 (5 points)

In the context of IaC and GitOps, why is it important to treat infrastructure changes with the same code-review process as application source code?

- A) Cloud providers require a Git commit hash before processing any infrastructure API requests.
- B) Code review enables peer validation of infrastructure changes, creating an audit trail, catching misconfigurations before deployment, and enforcing organizational policies.
- C) Terraform will not execute a plan unless the `.tf` files have been reviewed and approved in a pull request.
- D) Application source code and infrastructure code use identical syntax, making them interchangeable in the same review pipeline.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Applying a GitOps workflow to infrastructure code creates multiple benefits: peer review catches logic errors and security misconfigurations before they reach production; the Git log provides a complete audit trail of who changed what and why; branch protection rules enforce approval policies; and automated CI/CD can run `terraform plan` on pull requests so reviewers see exactly what will change.
  - Why A is incorrect: Cloud provider APIs do not require or validate Git commit hashes. Terraform communicates directly with provider APIs without any Git integration at the API level.
  - Why C is incorrect: Terraform has no built-in awareness of Git or pull request approval status. It executes plans based on configuration files and credentials, not on repository workflow state.
  - Why D is incorrect: Application code and HCL have entirely different syntax and semantics. The rationale for unified code review is process consistency and governance, not syntactic similarity.

---

Module 01 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
