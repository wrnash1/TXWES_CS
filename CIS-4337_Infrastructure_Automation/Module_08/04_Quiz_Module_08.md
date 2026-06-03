# Quiz: Module 08 — Terraform State Management

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

**Instructions**: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What is the primary purpose of the `terraform.tfstate` file?

A. It stores the Terraform configuration in a compiled binary format for faster execution.
B. It maps the resources defined in your configuration to the real-world objects that were created, including their current attribute values.
C. It records the history of all `terraform apply` commands run against the configuration.
D. It stores provider plugin binaries and their version checksums.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — state is a JSON document, not a compiled binary, and does not store configuration.
- C is incorrect — state records current infrastructure state, not a history of operations. A history is maintained via state versioning in the backend, not in the file itself.
- D is incorrect — provider binaries are stored in `.terraform/providers/`; the lock file `.terraform.lock.hcl` records version checksums.

---

### Question 2

You are configuring an S3 backend for a team environment. You want to prevent two engineers from running `terraform apply` simultaneously. What additional resource must you create?

A. An S3 bucket policy that denies concurrent PutObject operations
B. An AWS Lambda function that monitors the S3 bucket for concurrent writes
C. A DynamoDB table with a `LockID` primary key, referenced in the backend configuration
D. An IAM role with a session condition that limits one active session per user

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — S3 bucket policies cannot enforce sequential writes in the way Terraform requires; this is not a supported locking mechanism.
- B is incorrect — Lambda monitoring would not provide the atomic lock-acquire semantics that Terraform needs.
- D is incorrect — IAM session conditions do not provide the mutex (mutual exclusion) behavior needed for state locking.

---

### Question 3

A Terraform apply operation was forcibly killed mid-run, and now all subsequent `terraform plan` commands fail with a state lock error. What is the correct recovery action?

A. Delete the `terraform.tfstate` file and re-run `terraform init`.
B. Run `terraform state push` with a backup state file to overwrite the current state.
C. Run `terraform force-unlock <LOCK-ID>` using the Lock ID displayed in the error message.
D. Run `terraform destroy` to release the lock automatically.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — deleting the state file would cause Terraform to lose all knowledge of existing infrastructure, leading to duplicate resource creation.
- B is incorrect — `state push` is for uploading an alternative state file; it does not address a stuck lock and bypasses locking protections.
- D is incorrect — `terraform destroy` also tries to acquire the lock; it will fail with the same lock error.

---

### Question 4

A developer runs `terraform state rm aws_instance.web`. What is the result?

A. The EC2 instance is terminated in AWS and removed from state.
B. The EC2 instance continues running in AWS but is removed from Terraform's state tracking.
C. The state file entry is marked as "tainted" and the instance will be replaced on the next apply.
D. Terraform creates a plan to import the instance back into state automatically.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — `state rm` only modifies the state file; it does not call the provider to destroy the resource.
- C is incorrect — tainting is a different operation (`terraform taint`) that marks a resource for recreation; `state rm` completely removes the tracking entry.
- D is incorrect — Terraform has no automatic re-import mechanism; you would need to manually run `terraform import` to re-track the resource.

---

### Question 5

You are refactoring a Terraform configuration and rename a resource from `aws_instance.app` to `aws_instance.web_server` in your `.tf` files. Without any other action, what will `terraform plan` propose?

A. No changes — Terraform automatically detects the rename.
B. Update the resource with a new name tag.
C. Destroy `aws_instance.app` and create a new `aws_instance.web_server`.
D. An error — Terraform does not allow resource addresses to change.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — Terraform tracks resources by their address in state; it has no way to infer that a renamed address is the same resource.
- B is incorrect — instance renaming in code results in destroy/create, not an update, because the state no longer has a matching address.
- D is incorrect — renaming is valid HCL; Terraform processes it but treats the new name as a new resource and the old name as a deleted one.

---

### Question 6

Which backend configuration argument is NOT valid in an S3 backend block?

A. `bucket`
B. `dynamodb_table`
C. `encrypt`
D. `lock_timeout`

**Correct Answer**: D

**Distractor Analysis**:

- A is incorrect — `bucket` is a required argument for the S3 backend.
- B is incorrect — `dynamodb_table` is a valid optional argument that enables state locking.
- C is incorrect — `encrypt` is a valid optional argument that enables server-side encryption.
- D is correct — `lock_timeout` is not a valid S3 backend argument. The timeout for lock acquisition is a global Terraform behavior, not a per-backend setting.

---

### Question 7

You need to share an output value (specifically a VPC ID) from one Terraform configuration with another. Which approach is correct?

A. Copy and paste the VPC ID value directly into the second configuration's variables file.
B. Use the `terraform_remote_state` data source in the second configuration, pointing to the first configuration's backend.
C. Export the VPC ID as a Terraform variable and reference it with `var.vpc_id` in the second configuration.
D. Use a `module` block with `source` pointing to the first configuration's directory.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — hardcoding values defeats the purpose of infrastructure as code and breaks when the VPC ID changes.
- C is incorrect — Terraform variables require a value to be supplied; they do not automatically read from another configuration's outputs.
- D is incorrect — `module` blocks compose configurations at authoring time; they do not read live state from a separately-applied configuration.

---

### Question 8

What is the effect of adding `terraform.tfstate` to a `.gitignore` file?

A. Terraform will automatically store state in the cloud backend instead of locally.
B. The state file will be encrypted before Git can track it.
C. Git will not track the state file, preventing accidental commits of sensitive infrastructure data.
D. Terraform will refuse to create a local state file and will require a remote backend.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `.gitignore` is a Git configuration file; it has no effect on Terraform's backend selection.
- B is incorrect — `.gitignore` prevents tracking entirely; it does not apply encryption.
- D is incorrect — Terraform's backend selection is entirely independent of `.gitignore`; Terraform will still create a local state file if the local backend is configured.

---

### Question 9

Which command downloads the current state file from the configured backend and prints it to stdout?

A. `terraform state show`
B. `terraform state list`
C. `terraform state pull`
D. `terraform show -state`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `terraform state show <resource>` displays attributes of a specific resource, not the entire state file.
- B is incorrect — `terraform state list` lists resource addresses, not the full state file content.
- D is incorrect — `terraform show -state` is not a valid command syntax; `terraform show` displays the current plan or state in a human-readable format but does not output raw JSON.

---

### Question 10

A team is moving from storing Terraform state locally to using an S3 backend. They run `terraform init` after adding the backend block. What does `terraform init` do with the existing local state?

A. Deletes the local state file after verifying the S3 bucket is accessible.
B. Prompts the user to migrate the existing state to the new backend and copies it if confirmed.
C. Errors out because you cannot change backends after initial initialization.
D. Ignores the local state and starts with an empty state in S3.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — Terraform does not automatically delete the local state; it preserves it as a backup after migration.
- C is incorrect — backend changes are fully supported; `terraform init` is the mechanism for performing them.
- D is incorrect — starting with empty state in S3 would cause Terraform to propose creating all resources again, which is dangerous; the migration prompt prevents this.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
