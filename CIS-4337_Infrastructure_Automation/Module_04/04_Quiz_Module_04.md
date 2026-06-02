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

Module 04 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
