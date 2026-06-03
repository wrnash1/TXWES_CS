# Quiz: Module 13 — Terraform Security Best Practices

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Select the best answer for each question. Each question is worth 1 point. Distractor analysis follows each question to explain why incorrect options are wrong.

---

## Questions

### Question 1 — Answer: B

A developer sets `default = "MyPassword123"` in a Terraform variable declaration and commits the file. What is the primary security risk?

A. Terraform will refuse to run because default values for password variables are not allowed.

B. The password is now in git history and must be treated as compromised even if the file is later deleted.

C. The password will appear in `terraform plan` output but not in the state file.

D. The variable cannot be overridden with `TF_VAR_` because a default is already defined.

Why the distractors are wrong: **A** is wrong because Terraform imposes no restrictions on default values by type — any variable can have a default. **C** is wrong because the password will appear in plan output and also in the state file as a resource attribute. **D** is wrong because environment variables and `.tfvars` files always override defaults regardless of whether a default is set.

---

### Question 2 — Answer: D

Which of the following correctly passes the value `"s3cr3tKey"` to a Terraform variable named `api_key` without writing the value to any file?

A. Add `api_key = "s3cr3tKey"` to `terraform.tfvars`.

B. Add `default = "s3cr3tKey"` to the variable declaration in `variables.tf`.

C. Pass `-var="api_key=s3cr3tKey"` on the command line.

D. Export `TF_VAR_api_key=s3cr3tKey` in the shell environment before running Terraform.

Why the distractors are wrong: **A** is wrong because `.tfvars` files are written to disk and may be committed to source control. **B** is wrong because the default is in the source file and committed to git. **C** is wrong because command-line arguments appear in shell history files (`.bash_history`), which can expose the secret. **D** is the only approach that avoids writing the secret to any persistent artifact.

---

### Question 3 — Answer: A

What does declaring `sensitive = true` on a Terraform output value actually do?

A. It suppresses the value from appearing in `terraform output` and `terraform plan` terminal output.

B. It encrypts the value before writing it to the state file.

C. It prevents the value from being read by users with state file access.

D. It removes the value from all Terraform logs permanently.

Why the distractors are wrong: **B** is wrong because `sensitive = true` has no effect on state file storage — values are always written to state in plaintext unless the backend provides encryption. **C** is wrong because anyone who can read the state file can read the value regardless of the sensitive flag. **D** is wrong because the value remains in state and is accessible via `terraform output -raw` when explicitly requested.

---

### Question 4 — Answer: C

Your CI pipeline uses the Vault AppRole authentication method. What two pieces of information are combined to authenticate?

A. A username and a time-based one-time password (TOTP)

B. A Vault token and a certificate

C. A Role ID and a Secret ID

D. An AWS access key and a Vault policy name

Why the distractors are wrong: **A** is wrong because AppRole does not use usernames or TOTP — those are features of the `userpass` and `totp` auth methods respectively. **B** is wrong because a Vault token is the result of authentication, not an input to it. **D** is wrong because AppRole is a Vault-native authentication method that does not require AWS credentials.

---

### Question 5 — Answer: B

You configure an S3 backend with `encrypt = true` but without specifying a `kms_key_id`. What encryption is applied to the state file?

A. No encryption — the `encrypt = true` flag is ignored without a KMS key.

B. Server-side encryption with Amazon S3-managed keys (SSE-S3).

C. Client-side encryption using the local Terraform process.

D. Server-side encryption with the AWS account's default CMK.

Why the distractors are wrong: **A** is wrong because `encrypt = true` activates SSE-S3 even without a KMS key specified. **C** is wrong because Terraform's S3 backend performs server-side encryption, not client-side encryption. **D** is wrong because SSE-KMS with the AWS-managed key (not account default CMK) would require specifying `kms_key_id = "aws/s3"` explicitly.

---

### Question 6 — Answer: D

Why is a DynamoDB table required when using the S3 Terraform backend in production?

A. DynamoDB stores the encrypted state file content for faster retrieval.

B. DynamoDB holds the Terraform provider plugin cache to avoid repeated downloads.

C. DynamoDB stores the list of all resources managed by Terraform for plan generation.

D. DynamoDB provides state locking, preventing concurrent `terraform apply` runs from corrupting the state file.

Why the distractors are wrong: **A** is wrong because state content is stored in S3 — DynamoDB only stores the lock record. **B** is wrong because provider plugins are cached locally, not in DynamoDB. **C** is wrong because resource state is in the S3-stored state file, not in DynamoDB.

---

### Question 7 — Answer: A

A Terraform execution role in AWS has `AdministratorAccess`. A security review requires reducing it to least privilege. What is the first step in building a least-privilege replacement policy?

A. Identify every `resource` and `data` block in the Terraform configuration to enumerate all resource types that need IAM permissions.

B. Attach `ReadOnlyAccess` as a starting point and add permissions until apply succeeds.

C. Use AWS IAM Access Analyzer to scan the entire account and generate a policy automatically.

D. Copy the existing administrator policy and remove the `*` wildcards one at a time.

Why the distractors are wrong: **B** is wrong because starting from read-only and adding permissions is trial-and-error and produces an incomplete policy until all errors are resolved. **C** is wrong because IAM Access Analyzer generates policies from access activity logs, which requires the current over-privileged role to have been in use — it does not generate policies from Terraform configuration. **D** is wrong because administrator policy is a managed policy that cannot be edited, and copying and stripping wildcards without understanding resource requirements will produce an incorrect policy.

---

### Question 8 — Answer: C

Which Vault secret type generates a unique, time-limited IAM credential on demand rather than returning a stored static secret?

A. KV (Key-Value) secrets engine with versioning enabled

B. PKI secrets engine with a short-lived certificate TTL

C. AWS secrets engine with a configured IAM role

D. Transit secrets engine with AES-256-GCM encryption

Why the distractors are wrong: **A** is wrong because the KV engine stores static key-value pairs — it does not generate credentials. **B** is wrong because the PKI engine generates TLS certificates, not IAM credentials. **D** is wrong because the Transit engine provides encryption-as-a-service for arbitrary data — it does not generate cloud credentials.

---

### Question 9 — Answer: B

A Checkov scan reports `CKV_AWS_17` on your `aws_db_instance` resource. What does this finding indicate?

A. The RDS instance does not have a deletion protection flag set.

B. The RDS instance is configured with `publicly_accessible = true`.

C. The RDS instance storage is not encrypted.

D. The RDS instance does not have automated backups enabled.

Why the distractors are wrong: **A** is wrong because deletion protection is a different check (CKV_AWS_293 in current Checkov). **C** is wrong because storage encryption is CKV_AWS_16. **D** is wrong because automated backup configuration has its own Checkov check distinct from CKV_AWS_17.

---

### Question 10 — Answer: D

An AWS IAM permission boundary is set on the Terraform execution role. The role's attached policies include `AdministratorAccess`. What is the effective permission level?

A. The role has administrator access because the attached policy takes precedence over the boundary.

B. The role has no permissions because the boundary and the policy conflict.

C. The role has the permissions defined in the boundary plus the administrator policy combined.

D. The role has only the permissions that are allowed by both the permission boundary and the attached policies.

Why the distractors are wrong: **A** is wrong because permission boundaries are enforced as a ceiling — attached policies cannot grant permissions beyond the boundary regardless of their content. **B** is wrong because there is no conflict — the boundary simply limits the maximum; permissions within both sets are allowed. **C** is wrong because permission boundaries are intersected with, not added to, the attached policies.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | C |
| 5 | B |
| 6 | D |
| 7 | A |
| 8 | C |
| 9 | B |
| 10 | D |

---

End of Module 13 Quiz
