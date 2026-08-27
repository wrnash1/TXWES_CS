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

### Question 11 — Answer: C

A developer uses `terraform output -raw db_password` and the terminal displays the plaintext database password. The variable `db_password` was declared with `sensitive = true`. What does this demonstrate?

A. A bug in Terraform — `sensitive = true` should prevent `-raw` from displaying the value.

B. The `sensitive = true` flag was not applied correctly because the output is visible.

C. `sensitive = true` is a display-control flag, not an access-control mechanism; `-raw` explicitly requests the raw value and bypasses display suppression.

D. The variable declaration must also include `nullable = false` to enforce sensitive protection.

Why the distractors are wrong: **A** is wrong because this is designed behavior — `-raw` is an explicit request for the unquoted value and is intended for shell script consumption. **B** is wrong because `sensitive = true` was applied correctly; the behavior is working as designed. **D** is wrong because `nullable = false` prevents null assignment; it has no effect on sensitive value visibility.

---

### Question 12 — Answer: D

Your team stores Terraform state in an S3 bucket with `encrypt = true` but without `kms_key_id`. A security auditor requires that your team be able to revoke access to all state data if the encryption key is compromised. What change satisfies this requirement?

A. Enable S3 bucket versioning and set a 1-day retention period.

B. Change the backend to use Azure Blob Storage instead.

C. Add `restrict_public_buckets = true` to the S3 bucket's public access block.

D. Specify a customer-managed KMS key with `kms_key_id` so that revoking or disabling the key immediately makes all encrypted state inaccessible.

Why the distractors are wrong: **A** is wrong because bucket versioning controls data retention history, not encryption key revocation. **B** is wrong because switching backends does not solve the key revocation problem — Azure also uses platform-managed keys by default. **C** is wrong because blocking public access is a network-level control; it does not enable key revocation for already-encrypted data.

---

### Question 13 — Answer: A

A developer accidentally commits an `.env` file containing `TF_VAR_api_key=prod-secret-key-123` to the GitHub repository. The `.env` file was immediately deleted in the next commit. Which statement is accurate?

A. The secret must be treated as compromised and rotated immediately, because the value exists in git history and any clone made before deletion still contains it.

B. The secret is safe because the deletion commit removed it from the repository.

C. The secret is safe because `TF_VAR_` prefixed variables are encrypted by Terraform before being written to git.

D. The repository owner should mark the commit as private and restrict access to prevent exposure.

Why the distractors are wrong: **B** is wrong because deleting a file removes it from the working tree but not from git history; anyone who cloned before the deletion or who accesses the history can still read it. **C** is wrong because Terraform does not perform any git-level encryption; `TF_VAR_` is just a naming convention for shell environment variables. **D** is wrong because GitHub repositories are cloned and distributed — restricting visibility after exposure does not protect copies that were already cloned.

---

### Question 14 — Answer: B

In the Vault AppRole authentication flow for CI pipelines, what property of the Secret ID makes it more secure than storing a static Vault token?

A. Secret IDs are base64-encoded, making them harder to read in logs.

B. Secret IDs are typically single-use and short-lived — they expire after one authentication or after a configured TTL, eliminating long-lived credentials.

C. Secret IDs are encrypted in transit using TLS certificate pinning.

D. Secret IDs are randomly generated by the CI runner and never touch the Vault server.

Why the distractors are wrong: **A** is wrong because base64 encoding is not encryption and provides no security benefit. **C** is wrong because standard TLS protects all Vault API communication including static tokens; certificate pinning is not what differentiates Secret IDs. **D** is wrong because Secret IDs are issued by Vault to an authorized system and then provided to the pipeline — they originate from Vault, not from the runner.

---

### Question 15 — Answer: C

A Terraform configuration for an AWS Lambda function requires `lambda:CreateFunction`, `lambda:UpdateFunctionCode`, and `lambda:DeleteFunction`. Following least privilege, which resource scope is most appropriate for these permissions?

A. `"Resource": "*"` — wildcard because the function name is generated at runtime.

B. `"Resource": "arn:aws:lambda:*:*:function:*"` — all Lambda functions in all regions.

C. `"Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-app-*"` — scoped to the specific account, region, and name prefix.

D. `"Resource": "arn:aws:lambda:us-east-2:*:function:*"` — all functions in the correct region.

Why the distractors are wrong: **A** is wrong because even if the function name is generated at runtime, `random_id` produces predictable length and format — and scope can still be limited to account, region, and prefix. **B** is wrong because it grants permissions across all AWS accounts and all regions — far broader than needed. **D** is wrong because scoping to a region is better than a wildcard, but omitting the account ID (`*`) grants permissions on any account the role can access.

---

### Question 16 — Answer: A

Which `.gitignore` entries are essential for preventing Terraform state files and sensitive variable files from being committed to version control?

A. `terraform.tfstate`, `terraform.tfstate.backup`, `*.tfstate`, `*.tfvars`, `.terraform/`

B. `*.tf`, `*.json`, `.terraform.lock.hcl`

C. `terraform.tfstate`, `main.tf`, `variables.tf`

D. `.env`, `*.pem`, `*.key` (general secrets only — Terraform files are not sensitive)

Why the distractors are wrong: **B** is wrong because excluding all `.tf` and `.json` files would exclude the Terraform configuration itself, making the repository non-functional. **C** is wrong because excluding `main.tf` and `variables.tf` removes the infrastructure code from version control, defeating the GitOps purpose. **D** is wrong because Terraform state files ARE sensitive — they contain resource attributes including passwords, tokens, and connection strings.

---

### Question 17 — Answer: D

An IAM permission boundary is attached to the Terraform execution role, allowing only `s3:*` and `rds:*` actions. The role also has an attached policy allowing `ec2:*` and `s3:*`. What EC2 and S3 operations can the role perform?

A. All EC2 and S3 operations because the attached policy takes precedence over the boundary.

B. Only EC2 operations because the boundary allows both `s3:*` and `rds:*`.

C. No operations because the boundary and attached policy have conflicting statements.

D. Only S3 operations — `s3:*` is in both the boundary and the attached policy (intersection), while `ec2:*` is in the attached policy but not the boundary (blocked by intersection).

Why the distractors are wrong: **A** is wrong because permission boundaries are a hard ceiling — attached policies cannot grant permissions beyond them. **B** is wrong because the boundary allows `s3:*` and `rds:*`, not `ec2:*`; EC2 operations are blocked by the boundary. **C** is wrong because there is no conflict — the intersection model simply limits permissions to the overlap of both sets.

---

### Question 18 — Answer: B

A Checkov finding reports `CKV_AWS_111` on an `aws_iam_policy_document`. The inline comment `#checkov:skip=CKV_AWS_111:Wildcard required for service discovery` is added to the Terraform file. What is the effect?

A. Checkov ignores all findings in that file permanently.

B. Checkov skips CKV_AWS_111 for that specific resource, records the skip with the justification text, and continues evaluating all other checks normally.

C. Checkov converts the finding from a failure to a warning for that resource.

D. The comment only takes effect if Checkov is run with the `--skip-check` CLI flag.

Why the distractors are wrong: **A** is wrong because inline skips are resource-scoped, not file-scoped; other checks in the same file still run. **C** is wrong because Checkov inline skips suppress the finding entirely for that resource, not downgrade it to a warning. **D** is wrong because inline `#checkov:skip=` comments are processed by default without any additional CLI flags.

---

### Question 19 — Answer: A

Which Terraform state backend feature is specifically designed to prevent two engineers from running `terraform apply` at the same time and corrupting the state file?

A. State locking — the backend writes a lock record when an operation begins and releases it when the operation ends.

B. State versioning — the backend retains previous state versions so a corrupted state can be restored.

C. State encryption — the backend encrypts the state file so only authorized users can read it.

D. Backend authentication — the backend verifies user identity before allowing any operation.

Why the distractors are wrong: **B** is wrong because versioning allows recovery after corruption but does not prevent two concurrent writes from occurring. **C** is wrong because encryption protects data confidentiality but does not prevent concurrent write operations. **D** is wrong because authentication controls who can access the backend but does not prevent two authenticated users from simultaneously initiating applies.

---

### Question 20 — Answer: C

A team separates their CI pipeline into a plan role and an apply role. The plan role has `ec2:Describe*` and `rds:Describe*` permissions. The apply role has full `ec2:*` and `rds:*` permissions. A pull request pipeline is compromised via a malicious dependency. What is the maximum damage the attacker can cause using the plan role?

A. Full access to all EC2 and RDS resources in the account because plan operations reveal resource IDs.

B. Deletion of all EC2 instances because Describe permissions include implicit delete access.

C. The attacker can read resource metadata and enumerate infrastructure details but cannot create, modify, or delete any resources.

D. No damage because the plan role has no permissions on any resources.

Why the distractors are wrong: **A** is wrong because knowing resource IDs does not grant modification permissions; the plan role lacks write actions. **B** is wrong because `Describe` permissions are strictly read-only in IAM — they grant no create, modify, or delete capability. **D** is wrong because `Describe` permissions do allow reading resource metadata, IP addresses, and configuration details, which may still expose sensitive information useful for reconnaissance.

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
| 11 | C |
| 12 | D |
| 13 | A |
| 14 | B |
| 15 | C |
| 16 | A |
| 17 | D |
| 18 | B |
| 19 | A |
| 20 | C |

---

End of Module 13 Quiz
