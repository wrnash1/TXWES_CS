# Quiz: Module 04 - Terraform State – Local and Remote Backends
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which file extension is used by default for the file that stores Terraform state locally?
*   A) .tf
*   B) .tfvars
*   C) .tfstate
*   D) .hcl
*   **Correct Answer:** C) The default local state file is named `terraform.tfstate` and uses the `.tfstate` extension. It is a JSON file in the working directory.
*   **Distractor Analysis:**
    *   *Why C is correct:* Terraform writes state to `terraform.tfstate` by default. A backup of the previous state is kept in `terraform.tfstate.backup`. The exam tests this filename.
    *   *Why A is incorrect:* `.tf` files contain HCL configuration declarations, not state data.
    *   *Why B is incorrect:* `.tfvars` files supply variable values to a configuration; they have nothing to do with state storage.
    *   *Why D is incorrect:* `.hcl` is the general HashiCorp Configuration Language extension; Terraform configuration files specifically use `.tf`, and state files use `.tfstate`.

---

**Question 2**
Which of the following is the most accurate description of a **remote backend** in Terraform?
*   A) A plugin installed alongside Terraform Core that provides additional resource types not available in public providers
*   B) A configuration that stores the Terraform state file in a shared, external location (such as S3, GCS, or Terraform Cloud) enabling team collaboration, state locking, and encryption at rest
*   C) A secondary Terraform binary installed on a remote server that executes `apply` operations on behalf of the local CLI
*   D) A Git repository integration that automatically commits the state file after every `terraform apply` run
*   **Correct Answer:** B) A remote backend stores state outside the local machine, enabling multiple team members to share the same state, with locking to prevent concurrent modification and encryption for security.
*   **Distractor Analysis:**
    *   *Why B is correct:* Remote backends are the standard for team use. The exam tests which backends (S3+DynamoDB, Terraform Cloud, GCS, Azure Blob) support locking and which require additional services for it.
    *   *Why A is incorrect:* That describes a provider plugin, not a backend. Backends only manage state storage and locking; they do not add resource types.
    *   *Why C is incorrect:* Terraform Cloud remote execution does run operations remotely, but that is a feature of Terraform Cloud workspaces, not what "remote backend" means in general.
    *   *Why D is incorrect:* Terraform has no built-in Git integration for state. Storing state in Git is an anti-pattern because state files often contain sensitive plaintext secrets.

---

**Question 3**
A cloud resource was manually deleted from the AWS console, but it still appears in the Terraform state file. A developer needs to remove it from state without attempting to destroy anything. Which command should they run?
*   A) terraform destroy -target=aws_instance.web
*   B) terraform apply -replace=aws_instance.web
*   C) terraform state rm aws_instance.web
*   D) terraform import aws_instance.web
*   **Correct Answer:** C) `terraform state rm` removes the resource record from the state file only, without touching any real infrastructure. This is the correct approach when a resource no longer exists outside of Terraform.
*   **Distractor Analysis:**
    *   *Why C is correct:* After `terraform state rm`, Terraform no longer tracks the resource. Running `plan` afterward will show it as a new resource to create (if still in config) or show no changes (if also removed from config).
    *   *Why A is incorrect:* `terraform destroy -target` would attempt to call the provider API to delete the resource — which would fail with an error since it no longer exists in AWS.
    *   *Why B is incorrect:* `terraform apply -replace` forces recreation of a resource (destroy + create), which is wrong if the resource no longer exists at all.
    *   *Why D is incorrect:* `terraform import` adds an existing real-world resource into state — the opposite of what is needed here.

---

**Question 4**
You are configuring an S3 remote backend with state locking. Which additional AWS service must be configured to enable locking for the S3 backend?
*   A) AWS Lambda
*   B) AWS IAM
*   C) Amazon DynamoDB
*   D) Amazon SQS
*   **Correct Answer:** C) The S3 backend uses a DynamoDB table for state locking. You specify the table name in the `backend "s3"` block with the `dynamodb_table` argument.
*   **Distractor Analysis:**
    *   *Why C is correct:* S3 itself has no native locking mechanism. The S3 backend offloads locking to a DynamoDB table with a `LockID` string primary key. This is a classic exam question.
    *   *Why A is incorrect:* Lambda is a serverless compute service; it plays no role in Terraform state locking.
    *   *Why B is incorrect:* IAM controls authentication and authorization for accessing the S3 bucket, but does not provide locking functionality itself.
    *   *Why D is incorrect:* SQS is a message queuing service and is not involved in the S3 backend state locking mechanism.

---

**Question 5**
Which statement about Terraform state file security is correct and directly relevant to the Terraform Associate exam?
*   A) Variables marked `sensitive = true` are encrypted in the state file, so the state file is safe to store in a public S3 bucket
*   B) The state file never contains credentials or secrets because providers handle authentication separately
*   C) The state file stores sensitive values in plaintext regardless of `sensitive = true` on variables, so state must be encrypted at rest and access-controlled
*   D) Running `terraform state list` automatically encrypts the state file with AES-256 before displaying output
*   **Correct Answer:** C) `sensitive = true` only masks values in CLI output — it does not encrypt them in the state file. The state file always stores resource attributes, including secrets, as plaintext JSON, requiring proper backend encryption and access controls.
*   **Distractor Analysis:**
    *   *Why C is correct:* This is an explicit exam topic. HashiCorp documentation warns that state may contain secrets and recommends using a remote backend with encryption at rest (e.g., S3 with SSE, or Terraform Cloud which encrypts state automatically).
    *   *Why A is incorrect:* `sensitive = true` has no effect on state file contents — secrets are still in plaintext. A public S3 bucket would expose all state data including credentials.
    *   *Why B is incorrect:* Many resources write secrets to state (e.g., `aws_db_instance` writes the `password` attribute, `tls_private_key` writes the private key value).
    *   *Why D is incorrect:* `terraform state list` is a read-only query command and has no effect on how the state file is stored or encrypted.
