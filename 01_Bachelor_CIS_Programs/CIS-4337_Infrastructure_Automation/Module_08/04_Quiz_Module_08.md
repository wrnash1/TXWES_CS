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

---

### Question 11 (5 points)

A developer runs `terraform state mv module.old_name module.new_name` after renaming a `module` block label in the configuration. What is the purpose of this operation?

A. It destroys all resources in `module.old_name` and recreates them under `module.new_name`.
B. It updates the state file so that resource addresses match the new module label, preventing unnecessary destroy-and-recreate during the next plan.
C. It moves the module's source code directory from one path to another on the filesystem.
D. It copies the state entry so that the same resources are tracked under both the old and new module names simultaneously.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform state mv` updates resource addresses in the state file without touching real infrastructure. Renaming a module block label changes all resource addresses from `module.old_name.*` to `module.new_name.*`, and running `state mv` ahead of the plan prevents Terraform from proposing destructive destroy-and-recreate operations.
  - Why A is incorrect: `state mv` makes no provider API calls. It only edits the state file. Infrastructure is not touched.
  - Why C is incorrect: `state mv` is purely a state file operation. It has no interaction with the filesystem or module source paths.
  - Why D is incorrect: `state mv` is a move, not a copy. The old address is removed and the new one is created. There is no dual-tracking.

---

### Question 12 (5 points)

Which of the following is the correct DynamoDB table partition key attribute name required by the Terraform S3 backend for state locking?

A. `StateID`
B. `TerraformLock`
C. `LockID`
D. `lock_key`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: The Terraform S3 backend expects the DynamoDB table to have a single string partition key attribute named exactly `LockID`. This exact name is hardcoded in the S3 backend implementation and is a frequently tested detail on the Terraform Associate exam.
  - Why A is incorrect: `StateID` is not the expected attribute name. Using it will prevent locking from functioning correctly.
  - Why B is incorrect: `TerraformLock` is not the expected attribute name. The value must be exactly `LockID`.
  - Why D is incorrect: `lock_key` uses snake_case rather than the required CamelCase `LockID`. The backend code performs a case-sensitive string match.

---

### Question 13 (5 points)

What does `terraform state pull` return, and when is it useful?

A. It downloads provider plugins from the registry and prints the version list.
B. It downloads the current state from the configured backend and prints it as JSON to stdout, useful for inspection, backup, or offline processing.
C. It pulls the latest code changes from the module's Git source repository.
D. It refreshes the state by querying all provider APIs and immediately applies the updates.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform state pull` retrieves the raw state JSON from the backend (whether local or remote) and writes it to stdout. This is useful before risky operations as a manual backup, and for scripted processing of state contents.
  - Why A is incorrect: Provider plugin downloads are performed by `terraform init`. `state pull` has no involvement with provider management.
  - Why C is incorrect: Module source code is managed by `terraform init` and the `.terraform/modules/` directory. `state pull` only operates on state data.
  - Why D is incorrect: Refreshing state from provider APIs is the job of `terraform apply -refresh-only` or the deprecated `terraform refresh`. `state pull` is a read-only state download with no API calls to cloud providers.

---

### Question 14 (5 points)

You run `terraform state rm module.database` (referring to the entire module, not a single resource). What is the effect?

A. All cloud resources created by `module.database` are destroyed.
B. All state entries for resources inside `module.database` are removed; the actual cloud resources continue to run.
C. Only the module's outputs are removed from state; resource entries are preserved.
D. Terraform raises an error because `state rm` only accepts individual resource addresses, not module addresses.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform state rm` accepts both individual resource addresses and module addresses. When given a module address, it removes all state entries for every resource in that module. The actual cloud resources are completely unaffected.
  - Why A is incorrect: `state rm` never destroys cloud resources. It only edits the state file.
  - Why C is incorrect: `state rm` removes the full resource entries, not just outputs. Module outputs are stored separately in state and would also be removed.
  - Why D is incorrect: `terraform state rm` does accept module addresses. Running `terraform state rm module.database` is valid and removes all resource entries under that module prefix.

---

### Question 15 (5 points)

A `terraform_remote_state` data source references another configuration's S3 backend. What must the consumer configuration's AWS credentials include to use this data source?

A. Write access to the S3 bucket to cache the remote state locally.
B. The ability to create DynamoDB lock entries in the source configuration's lock table.
C. Read access to the S3 object at the configured `key` path in the configured `bucket`.
D. Full administrative access to the source configuration's state bucket.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why C is correct: `terraform_remote_state` performs a read-only operation. The consuming configuration needs only `s3:GetObject` permission on the specific state file path. No write access or DynamoDB access is required for a read.
  - Why A is incorrect: `terraform_remote_state` reads state from S3 directly. There is no local caching that requires write access.
  - Why B is incorrect: DynamoDB locking is used only when writing state. Reading state via `terraform_remote_state` does not acquire or need a lock.
  - Why D is incorrect: Least privilege is the correct security posture. Full administrative access is never required for a read-only data source operation.

---

### Question 16 (5 points)

The `serial` field in a Terraform state file is `14`. After a successful `terraform apply` that modifies two resources, what is the new `serial` value?

A. `14` — the serial only changes during `terraform destroy`.
B. `15` — the serial increments by one per apply, regardless of how many resources changed.
C. `16` — the serial increments by one per modified resource.
D. `28` — the serial doubles each time state is written.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `serial` field increments by exactly one each time the state file is written, regardless of the number of resources changed. After one successful apply that updates two resources, the serial advances from `14` to `15`.
  - Why A is incorrect: The serial increments on every state write, including plans that refresh state, applies, and destroys.
  - Why C is incorrect: The serial is not resource-count-aware. It tracks the number of state writes, not the number of resources changed per write.
  - Why D is incorrect: The serial uses a simple linear increment, not exponential growth.

---

### Question 17 (5 points)

Which of the following is a valid reason to use `terraform state push` with caution?

A. It permanently deletes the remote state and cannot be undone.
B. It uploads a local state file to the remote backend, potentially overwriting the current remote state with an older version and causing state corruption.
C. It triggers an immediate `terraform apply` against the pushed state without showing a plan.
D. It permanently locks the state backend, preventing any future `terraform apply` operations.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: `terraform state push` overwrites the remote backend's state with whatever is in the local file. If the local file is outdated or incorrect, the push can replace a more current or accurate state with corrupted or stale data. Always create a backup with `terraform state pull` before using `state push`.
  - Why A is incorrect: The overwritten state can be recovered from S3 versioning, GCS object versioning, or Azure blob versioning if those features are enabled. The operation is not necessarily permanent.
  - Why C is incorrect: `terraform state push` only updates the state file. It does not trigger any apply operation or resource changes.
  - Why D is incorrect: `state push` does not lock the backend. It writes the state and releases any hold it acquired during the operation.

---

### Question 18 (5 points)

Why is the `lineage` field important in Terraform state?

A. It records the Git branch from which the last `terraform apply` was run.
B. It is a UUID generated when state is first created that prevents accidentally mixing state from different environments or configurations.
C. It stores the ARN or resource ID of the first resource ever created in this configuration.
D. It is the encryption key reference used when `encrypt = true` is configured on the backend.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: The `lineage` UUID is assigned once when a new state file is created. Terraform checks it when pushing state to a backend — if the lineage in the local file does not match the remote, Terraform warns that you may be mixing state from different configurations or environments.
  - Why A is incorrect: Terraform has no built-in Git integration in the state file. Git branch tracking requires external tooling or CI/CD metadata.
  - Why C is incorrect: The `lineage` is a UUID generated at state creation time, not derived from any resource's attributes.
  - Why D is incorrect: Encryption key references are configured in the backend block arguments (e.g., `kms_key_id` for S3). They are not stored in the state `lineage` field.

---

### Question 19 (5 points)

After enabling S3 bucket versioning for a Terraform state backend, what recovery scenario does versioning support that it would not without versioning?

A. Concurrent write conflicts are automatically resolved by selecting the most recent version.
B. If a `terraform apply` produces an unintended result, a previous version of the state file can be retrieved and restored to roll back to the pre-apply configuration knowledge.
C. Versioning automatically triggers a `terraform destroy` for resources removed from the latest state version.
D. Versioning allows multiple teams to maintain separate state histories in the same S3 key path.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: S3 versioning preserves every previous version of the state file as a separate object. If an apply destroys resources unintentionally or corrupts state, an operator can download the previous state version and push it back to restore Terraform's knowledge of the pre-apply infrastructure state.
  - Why A is incorrect: S3 versioning does not provide concurrent write conflict resolution. State locking via DynamoDB prevents conflicts; versioning provides point-in-time recovery.
  - Why C is incorrect: S3 versioning is a passive storage feature. It does not trigger any Terraform operations.
  - Why D is incorrect: Multiple teams use separate key paths (or workspaces) to isolate state — not separate version histories within the same key.

---

### Question 20 (5 points)

A team's `terraform plan` command fails with the message: "Error acquiring the state lock: ... Lock Info: ID: abc123-xyz". The last `terraform apply` completed successfully 30 minutes ago. What is the most likely explanation?

A. The DynamoDB table has reached its storage limit and cannot accept new lock entries.
B. A previous Terraform process was killed during an operation, leaving a stale lock record in DynamoDB.
C. The S3 bucket policy has been changed to deny write access since the last successful apply.
D. Terraform automatically locked the state after 30 minutes to protect against unauthorized changes.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why B is correct: A stale lock is the most common cause of this error after a prior successful operation. When a Terraform process is killed (e.g., by a CI/CD timeout, signal, or network loss) while holding the lock, the DynamoDB lock record is not cleaned up. Subsequent runs encounter the orphaned record and cannot proceed.
  - Why A is incorrect: DynamoDB lock tables store only one record per state file (a single `LockID` entry). Storage capacity is not a practical concern.
  - Why C is incorrect: If the bucket policy denied writes, the error message would reference S3 access denial, not a state lock conflict.
  - Why D is incorrect: Terraform does not implement automatic time-based locking. Locks are acquired at operation start and released at completion. There is no 30-minute idle lock timer.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
