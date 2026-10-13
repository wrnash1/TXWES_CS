# CIS-4337 Infrastructure Automation

## Quiz — Module 04: Terraform State — Local and Remote Backends

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What is the default filename for Terraform's local state file?

- A) `.tf`
- B) `.tfvars`
- C) `terraform.tfstate`
- D) `terraform.hcl`

Correct Answer: C

Distractor Analysis:

- Why C is correct: Terraform writes state to `terraform.tfstate` in the working directory by default. A previous-state backup is stored in `terraform.tfstate.backup`. Both are JSON files.
- Why A is incorrect: `.tf` is the extension for HCL configuration files, not state files.
- Why B is incorrect: `.tfvars` files supply variable values to configurations and have no relation to state storage.
- Why D is incorrect: `.hcl` is the general HashiCorp Configuration Language extension. Terraform configuration files use `.tf`; state files use `.tfstate`.

---

### Question 2

Which of the following best describes a remote backend in Terraform?

- A) A plugin installed alongside Terraform Core that provides additional resource types not available in public providers.
- B) A configuration that stores the Terraform state file in a shared, external location enabling team collaboration, state locking, and encryption at rest.
- C) A secondary Terraform binary installed on a remote server that executes `apply` operations on behalf of the local CLI.
- D) A Git repository integration that automatically commits the state file after every `terraform apply` run.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Remote backends store state externally in systems like S3, Azure Blob Storage, or Terraform Cloud. They enable multiple team members to share state, provide locking to prevent concurrent writes, and support encryption at rest.
- Why A is incorrect: That describes a provider plugin. Backends only manage state storage and locking; they do not add resource types.
- Why C is incorrect: Remote execution (running plan and apply on a Terraform Cloud runner) is a feature of Terraform Cloud workspaces, not the definition of a remote backend.
- Why D is incorrect: Git integration for state commits is not a Terraform backend feature. Storing state in Git is an anti-pattern because state files contain plaintext secrets.

---

### Question 3

A cloud resource was manually deleted from the AWS console but still appears in the Terraform state file. A developer needs to remove it from state without attempting any API calls. Which command is correct?

- A) `terraform destroy -target=aws_instance.web`
- B) `terraform apply -replace=aws_instance.web`
- C) `terraform state rm aws_instance.web`
- D) `terraform import aws_instance.web`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform state rm` removes the resource record from the state file only. It makes no API calls and does not attempt to delete any cloud infrastructure. After removal, Terraform treats the resource as unknown.
- Why A is incorrect: `terraform destroy -target` would call the AWS API to delete the resource, which would fail with a not-found error since the instance no longer exists.
- Why B is incorrect: `terraform apply -replace` forces a destroy-and-recreate of the resource. This is wrong when the resource no longer exists at all.
- Why D is incorrect: `terraform import` brings an existing real-world resource into Terraform state — the opposite of what is needed here.

---

### Question 4

Which additional AWS service must be configured to enable state locking when using the S3 backend?

- A) AWS Lambda
- B) AWS IAM
- C) Amazon DynamoDB
- D) Amazon SQS

Correct Answer: C

Distractor Analysis:

- Why C is correct: The S3 backend uses a DynamoDB table for state locking. You specify the table name with the `dynamodb_table` argument. The table must have a single string partition key attribute named exactly `LockID`.
- Why A is incorrect: Lambda is a serverless compute service and plays no role in Terraform state locking.
- Why B is incorrect: IAM controls authentication and authorization for accessing the S3 bucket but does not provide atomic locking functionality.
- Why D is incorrect: SQS is a message queue service and is not part of the S3 backend locking mechanism.

---

### Question 5

Which statement about the Terraform state file and sensitive values is correct?

- A) Variables marked `sensitive = true` are encrypted in the state file, so the state file is safe to store in a public S3 bucket.
- B) The state file never contains credentials or secrets because providers handle authentication separately.
- C) Sensitive values are stored in plaintext in the state file regardless of `sensitive = true` on variables, so the state file must be encrypted at rest and access-controlled.
- D) Running `terraform state list` encrypts the state file automatically before displaying output.

Correct Answer: C

Distractor Analysis:

- Why C is correct: `sensitive = true` only masks values in CLI output. The state file is plain JSON and stores all resource attributes, including passwords, private keys, and API tokens, as readable text. Encrypt the backend at rest and restrict access.
- Why A is incorrect: `sensitive = true` has no effect on the state file contents. A public S3 bucket would expose all state data including credentials.
- Why B is incorrect: Many resources write secrets to state. For example, `aws_db_instance` writes the `password` attribute and `tls_private_key` writes the private key value directly into state.
- Why D is incorrect: `terraform state list` is a read-only query command. It has no effect on how the state file is stored or encrypted.

---

### Question 6

What happens to the local `terraform.tfstate` file after you run `terraform init -migrate-state` and confirm the migration to an S3 backend?

- A) The local file is deleted automatically by Terraform.
- B) The local file remains but Terraform no longer reads from or writes to it; the remote backend becomes the authoritative state source.
- C) The local file is renamed to `terraform.tfstate.backup` and continues to be updated on every apply.
- D) The local file is committed to Git automatically as a backup record.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Terraform migrates state to the remote backend but leaves the local file in place. The local file is no longer used. It is safe to delete it manually, but Terraform does not do so automatically.
- Why A is incorrect: Terraform does not delete the local state file. It only stops using it after migration.
- Why C is incorrect: The existing `terraform.tfstate.backup` is the backup from the previous apply, not a post-migration rename.
- Why D is incorrect: Terraform has no built-in Git integration and never auto-commits files.

---

### Question 7

A Terraform apply process was forcibly killed while holding a state lock. Subsequent runs fail with a lock error. What command releases the lock?

- A) `terraform unlock`
- B) `terraform state unlock`
- C) `terraform force-unlock <lock-id>`
- D) `terraform apply -no-lock`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform force-unlock <lock-id>` releases a stuck lock. The lock ID is shown in the error message. Use this only when you are certain no other process is running, as forcibly releasing an active lock can cause state corruption.
- Why A is incorrect: `terraform unlock` is not a valid Terraform command.
- Why B is incorrect: `terraform state unlock` is not a valid subcommand of `terraform state`.
- Why D is incorrect: `terraform apply -no-lock` is not a valid flag. Terraform does not support bypassing state locking via CLI flag.

---

### Question 8

Which `terraform state` subcommand allows you to rename a resource in state without destroying and recreating it?

- A) `terraform state rename`
- B) `terraform state mv`
- C) `terraform state push`
- D) `terraform state replace`

Correct Answer: B

Distractor Analysis:

- Why B is correct: `terraform state mv <source-address> <destination-address>` updates the resource's address in state. This is used when renaming a resource local name in HCL or moving a resource into a module. No cloud resources are created or destroyed.
- Why A is incorrect: `terraform state rename` is not a valid command.
- Why C is incorrect: `terraform state push` uploads a local state file to the remote backend. It does not move resources within state.
- Why D is incorrect: `terraform state replace` is not a valid subcommand.

---

### Question 9

A team configures an S3 backend but does not configure DynamoDB locking. Two engineers run `terraform apply` simultaneously. What is the most likely outcome?

- A) Terraform detects the conflict and queues the second apply to run after the first completes.
- B) The second apply fails immediately with an "incompatible state" error.
- C) Both applies run concurrently and one may silently overwrite the other's state changes, potentially causing state corruption.
- D) Terraform merges the two state files automatically and applies both changesets.

Correct Answer: C

Distractor Analysis:

- Why C is correct: Without locking, both processes read state before either writes. When both write back, one write overwrites the other. The result is a state file that does not accurately reflect what was deployed, which can cause subsequent plans to propose incorrect changes or fail entirely.
- Why A is incorrect: Without locking, Terraform has no queuing mechanism. Both applies proceed concurrently.
- Why B is incorrect: An incompatible state error occurs when the `serial` field is out of sync in a specific way, but without locking the more common outcome is silent overwrite.
- Why D is incorrect: Terraform has no automatic state merging capability.

---

### Question 10

A developer runs `terraform import aws_instance.legacy i-0abc12345`. What must exist before this command can succeed?

- A) A running `terraform apply` operation in another terminal.
- B) A `resource "aws_instance" "legacy" {}` block in the HCL configuration.
- C) A `terraform.tfstate` file with a pre-existing record for `aws_instance.legacy`.
- D) An IAM policy attached specifically for Terraform import operations.

Correct Answer: B

Distractor Analysis:

- Why B is correct: `terraform import` requires a matching resource block in the configuration. Terraform imports the real-world resource's attributes into state under the specified address. Without the resource block, Terraform cannot determine the schema for the resource.
- Why A is incorrect: Import is a standalone operation that does not require a concurrent apply.
- Why C is incorrect: If a state record for the address already existed, the import would fail with a conflict. Import creates a new state entry.
- Why D is incorrect: No special IAM policy for import exists. The credentials need only the standard read permissions for the resource type being imported.

---

---

### Question 11 (5 points)

What is the purpose of the `serial` field in the Terraform state file?

- A) It records the number of resources currently managed in the configuration.
- B) It is a counter that increments by one on every state write, used to detect concurrent modification and prevent state corruption.
- C) It identifies the version of the Terraform CLI binary that last wrote the state file.
- D) It is a checksum of the state file contents used for integrity verification on read.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `serial` field is Terraform's optimistic concurrency control mechanism. Each write increments the serial. If two clients try to write state simultaneously, the one with a lower serial than what is already in the backend is rejected, signaling a conflict.
  - Why A is incorrect: The number of managed resources is reflected by the length of the `resources` array, not the `serial` field.
  - Why C is incorrect: The Terraform CLI version is recorded in the `terraform_version` field, not `serial`.
  - Why D is incorrect: The `lineage` UUID and backend-level checksums handle integrity verification. The `serial` is a write counter, not a hash.

---

### Question 12 (5 points)

Which command prints the current remote state to standard output without modifying it?

- A) `terraform state show`
- B) `terraform state push`
- C) `terraform state pull`
- D) `terraform state list`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `terraform state pull` downloads the remote state and prints it as JSON to stdout. It is read-only and makes no changes. Useful for inspecting or backing up remote state.
  - Why A is incorrect: `terraform state show <addr>` displays the attributes of a single specific resource, not the entire state.
  - Why B is incorrect: `terraform state push` uploads a local state file to the remote backend, overwriting whatever is there. It is a write operation, not a read.
  - Why D is incorrect: `terraform state list` shows only the resource addresses (names), not the full state contents.

---

### Question 13 (5 points)

You need to refactor a Terraform configuration by moving `aws_instance.web` into a module called `app`. Which command updates the state to reflect the new address without destroying and recreating the resource?

- A) `terraform state rm aws_instance.web`
- B) `terraform state mv aws_instance.web module.app.aws_instance.web`
- C) `terraform import module.app.aws_instance.web <instance-id>`
- D) `terraform apply -replace=aws_instance.web`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform state mv` renames or relocates a resource address in state. Moving from `aws_instance.web` to `module.app.aws_instance.web` updates the state entry to match the new module path, allowing a subsequent `terraform plan` to show no changes.
  - Why A is incorrect: `terraform state rm` removes the resource from state entirely. The resource would then appear as new in the next plan and Terraform would try to create a duplicate.
  - Why C is incorrect: `terraform import` is for bringing untracked real-world resources into state. The resource is already in state; it just needs its address updated, not imported from scratch.
  - Why D is incorrect: `terraform apply -replace` forces destruction and recreation of the resource. This is the opposite of what a refactor should do — the goal is zero resource changes.

---

### Question 14 (5 points)

Why should backend blocks in Terraform not use variable references (e.g., `bucket = var.state_bucket`)?

- A) Backend blocks are evaluated before provider plugins are downloaded, so variable types are not yet known.
- B) Backend configuration is resolved at `terraform init` time, before the normal variable evaluation cycle, so variable values are not available.
- C) Using variables in backend blocks causes the state file to be stored under a different path on every run.
- D) HCL forbids variable references inside any block that starts with `terraform`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The backend is initialized during `terraform init`, which runs before variables are populated from `.tfvars` files, environment variables, or CLI flags. Because variables are not yet resolved at that stage, Terraform rejects references to them in backend blocks.
  - Why A is incorrect: Provider plugin downloads happen during init, but the reason variable references are rejected is about evaluation order during init, not about type checking.
  - Why C is incorrect: Variables in backend blocks are rejected at parse time with a clear error, not silently causing path changes.
  - Why D is incorrect: The `terraform {}` block does accept variable references in some arguments (like `required_version` expressions), but the backend sub-block specifically cannot use them due to init-time evaluation constraints.

---

### Question 15 (5 points)

A team accidentally deleted the `terraform.tfstate` file from their local working directory before migrating to a remote backend. The cloud resources still exist. What is the correct recovery procedure?

- A) Run `terraform apply` immediately to recreate all resources from scratch.
- B) Run `terraform destroy` to clean up and start over from a known state.
- C) Write resource blocks for all existing resources and run `terraform import` for each one to rebuild the state file.
- D) The state file cannot be recovered; all resources must be deleted and redeployed using Terraform.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: With the state file gone, Terraform treats all declared resources as new and would try to create duplicates. The correct approach is to use `terraform import` (or `import` blocks in Terraform 1.5+) to rebuild the state file by mapping each existing resource's real-world ID to its HCL resource block.
  - Why A is incorrect: Running `terraform apply` without state would attempt to create all resources again, resulting in duplicate resources or errors when names conflict.
  - Why B is incorrect: Running `terraform destroy` without state would do nothing, as Terraform has nothing to destroy from its perspective.
  - Why D is incorrect: Resources are recoverable through the import process. Declaring them lost and redeploying would cause unnecessary downtime and may be impossible for stateful resources like databases.

---

### Question 16 (5 points)

What does enabling S3 bucket versioning provide in the context of Terraform state management?

- A) It allows multiple teams to write to the same state file simultaneously without locking.
- B) It stores previous versions of the state file, enabling recovery if the current state becomes corrupted or an unintended apply destroys resources.
- C) It encrypts the state file using S3 server-side encryption keys.
- D) It automatically syncs state changes to a DynamoDB table for redundancy.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: S3 versioning preserves every version of the state file as it changes. If a bad `terraform apply` causes unintended destruction, a previous good state version can be retrieved, allowing operators to understand what changed and potentially restore resources.
  - Why A is incorrect: Versioning does not provide concurrent write safety. Locking (via DynamoDB) prevents concurrent writes; versioning provides recovery capability.
  - Why C is incorrect: Encryption is configured via S3 bucket policies, KMS keys, and the `encrypt = true` argument in the backend block. Versioning is a separate feature that manages object history.
  - Why D is incorrect: DynamoDB is used for locking, not for state replication. Versioning and DynamoDB locking are independent S3 backend features.

---

### Question 17 (5 points)

Which of the following is a valid use case for `terraform workspace`?

- A) Storing provider credentials separately for each team member within a shared configuration.
- B) Maintaining isolated state files for different environments (dev, staging, prod) within the same backend and configuration.
- C) Splitting a large configuration into smaller modules for better maintainability.
- D) Running `terraform apply` in a separate OS process to avoid memory limits.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: Terraform workspaces allow the same configuration to manage separate, isolated infrastructure environments by using separate state files. The `terraform.workspace` variable is available to differentiate resource names or configurations by workspace.
  - Why A is incorrect: Provider credentials are managed through environment variables, IAM roles, or provider block arguments, not workspaces.
  - Why C is incorrect: Splitting configurations into smaller units is the purpose of modules, not workspaces.
  - Why D is incorrect: Workspaces are a state isolation feature, not a process management tool.

---

### Question 18 (5 points)

After running `terraform state rm aws_instance.orphan`, what is the status of the corresponding EC2 instance in AWS?

- A) The instance is terminated immediately by Terraform.
- B) The instance is stopped but not terminated.
- C) The instance continues to run in AWS, but Terraform no longer tracks or manages it.
- D) The instance is tagged with `managed_by = "none"` to indicate it is unmanaged.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `terraform state rm` is purely a state manipulation command. It removes the record from the state file only. The cloud resource is completely unaffected and continues to run.
  - Why A is incorrect: `terraform state rm` makes no API calls and cannot terminate instances. Only `terraform destroy` (or `terraform apply -destroy`) terminates resources.
  - Why B is incorrect: `terraform state rm` cannot stop instances. It has no interaction with the AWS API whatsoever.
  - Why D is incorrect: Terraform does not modify any tags when a resource is removed from state. The resource's metadata in AWS is untouched.

---

### Question 19 (5 points)

What is the `lineage` field in the Terraform state file used for?

- A) It records the list of all Terraform users who have ever applied changes to this state.
- B) It is a UUID assigned when the state file is first created that prevents accidentally merging state files from different configurations or environments.
- C) It stores the Git commit hash of the last code change that triggered a Terraform apply.
- D) It is the encryption key identifier used when `encrypt = true` is set on the S3 backend.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `lineage` is a UUID generated once when the state file is created. Terraform uses it to detect if a remote backend has been overwritten with state from a different environment. If a push would change the lineage, Terraform warns the operator.
  - Why A is incorrect: Terraform does not track user history in the state file. Audit trails for who applied changes come from VCS commit history, CI/CD logs, or Terraform Cloud audit logs.
  - Why C is incorrect: Terraform has no built-in Git integration that would store commit hashes in the state file.
  - Why D is incorrect: Encryption keys are managed by KMS or S3 bucket settings, not stored inside the state file itself.

---

### Question 20 (5 points)

A team uses partial backend configuration, passing only `bucket` and `key` arguments in the `backend "s3"` block. How do they supply the remaining required arguments (`region`, `dynamodb_table`) without hardcoding them?

- A) By setting `TF_BACKEND_REGION` and `TF_BACKEND_DYNAMODB` environment variables.
- B) By declaring them as Terraform input variables and referencing them in the backend block.
- C) By passing a `-backend-config="region=us-east-1"` flag or a `-backend-config=backend.hcl` file when running `terraform init`.
- D) By creating a `backend_override.tf` file that Terraform automatically reads during init.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: Partial backend configuration allows the backend block to contain only some arguments. Missing arguments are supplied at `terraform init` time via `-backend-config="key=value"` flags or a separate HCL file passed with `-backend-config=filename.hcl`. This separates sensitive backend details from version-controlled configuration.
  - Why A is incorrect: There are no `TF_BACKEND_*` environment variables for backend configuration. Some backends read provider-level variables (like `AWS_REGION`), but the backend configuration mechanism is the `-backend-config` flag.
  - Why B is incorrect: Backend blocks cannot reference Terraform variables. This restriction is what makes partial backend configuration necessary.
  - Why D is incorrect: Terraform does have an `override` file mechanism for some block types, but there is no `backend_override.tf` special file that auto-supplies backend arguments.

---

Module 04 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
