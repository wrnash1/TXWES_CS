# Quiz: Module 15 - Terraform Security & Secrets Management

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which HCL attribute, when added to a `variable` or `output` block, prevents the value from being printed to the console during `terraform plan` and `terraform apply`?

* A) `write = false`
* B) `sensitive = true`
* C) `hidden = true`
* D) `redact = true`
* **Correct Answer:** B) Declaring `sensitive = true` on a `variable` or `output` block instructs Terraform to mask the value as `(sensitive value)` in all plan, apply, and output console displays.
* **Distractor Analysis:**
  * *Why B is correct:* `sensitive = true` is the documented Terraform attribute for controlling console output masking. It is set inside `variable` or `output` blocks and causes Terraform to suppress the actual value in CLI output. Note that the value is still stored in plaintext in `terraform.tfstate`.
  * *Why A is incorrect:* `write = false` is not a valid attribute on Terraform `variable` or `output` blocks. No such attribute exists in the Terraform language specification.
  * *Why C is incorrect:* `hidden = true` is not a valid Terraform attribute. This option is a plausible-sounding distractor but does not correspond to any real Terraform language feature.
  * *Why D is incorrect:* `redact = true` is not a valid Terraform attribute. The correct attribute name is `sensitive`, not `redact`.

---

**Question 2**
Which of the following most accurately describes **sensitive outputs** in Terraform?

* A) Output values that are automatically encrypted using AES-256 before being written to the state file, ensuring they cannot be read without the encryption key
* B) Output values declared with `sensitive = true` that are masked in CLI display but are still written to the state file in plaintext, requiring secure backend access controls as the primary protection mechanism
* C) Output values that are never written to the state file and exist only in memory during the `terraform apply` run, disappearing after the process exits
* D) Output values that trigger a Terraform error if referenced by any downstream module, enforcing that sensitive data never propagates through module composition
* **Correct Answer:** B) Sensitive outputs are masked in console output but are not encrypted in state. The `sensitive = true` declaration is a display control, not a cryptographic protection. The state backend must be independently secured with encryption and access controls.
* **Distractor Analysis:**
  * *Why B is correct:* This is the precise, exam-tested behavior of sensitive outputs. The most critical point is that `sensitive = true` only affects what is shown in the terminal — the actual value is always persisted to state in plaintext. This is why the exam emphasizes encrypting state backends (e.g., S3 with `encrypt = true`, Terraform Cloud's built-in encryption).
  * *Why A is incorrect:* Terraform does not encrypt individual output values before writing them to state. State file encryption (if any) is handled at the backend level (e.g., S3 server-side encryption) and applies to the entire file, not to individual sensitive values.
  * *Why C is incorrect:* All output values — sensitive or not — are written to the state file. Sensitive outputs are not held only in memory; they persist to state just like non-sensitive outputs.
  * *Why D is incorrect:* Sensitive outputs can be referenced by downstream configurations, but when a sensitive output is referenced in a non-sensitive context, Terraform raises an error requiring explicit acknowledgment. This is a referencing guard, not a blanket prohibition on propagation.

---

**Question 3**
A practitioner runs `terraform output db_password` and the terminal displays `(sensitive value)`. Where can the actual plaintext value of `db_password` be found?

* A) It cannot be retrieved; marking an output as sensitive permanently destroys the underlying value after apply completes
* B) In the `terraform.tfstate` file, where all output values including sensitive ones are stored in plaintext
* C) In a Vault secret automatically created by Terraform when a sensitive output is declared
* D) Only in Terraform Cloud's encrypted secrets store, which requires an API token to access
* **Correct Answer:** B) Sensitive outputs are masked only in CLI display. The actual value is stored without encryption in the `terraform.tfstate` file under the `outputs` section and can be read by anyone with file-system access to state.
* **Distractor Analysis:**
  * *Why B is correct:* This is the key security implication that the exam tests repeatedly. The `(sensitive value)` display is purely cosmetic protection. Direct state file inspection — `cat terraform.tfstate` or `terraform state pull` — reveals the plaintext value. This is why backend security is critical.
  * *Why A is incorrect:* `sensitive = true` does not destroy or discard the value. It only controls display output. The value is preserved in state to support future plan/apply operations that need to compare current and desired state.
  * *Why C is incorrect:* Terraform does not automatically create Vault secrets when sensitive outputs are declared. Vault integration requires explicit configuration of the Vault provider and resource blocks. Sensitive outputs have no relationship to Vault unless the practitioner explicitly wires them together.
  * *Why D is incorrect:* Terraform Cloud's secrets store holds workspace variables, not Terraform output values. Output values are stored in the workspace's state, which Terraform Cloud does encrypt — but this is a backend-level protection, not a separate secrets store that requires an API token to read outputs.

---

**Question 4**
A team discovers that a Terraform configuration file contains a hardcoded database password: `password = "Sup3rS3cr3t!"`. Which remediation correctly removes the secret from the configuration while keeping the Terraform workflow functional?

* A) Wrap the password in a `nonsensitive()` function call: `password = nonsensitive("Sup3rS3cr3t!")` — this encrypts the value before storing it in state
* B) Declare a `variable "db_password" { sensitive = true }` block, replace the hardcoded value with `var.db_password`, and supply the value via the `TF_VAR_db_password` environment variable at runtime
* C) Move the password to a `locals` block: `locals { db_password = "Sup3rS3cr3t!" }` and reference it as `local.db_password` — locals are not written to state
* D) Store the password in `terraform.tfvars` and add `terraform.tfvars` to `.gitignore` so it is not committed to version control
* **Correct Answer:** B) Declaring the variable with `sensitive = true`, replacing the hardcoded value with a variable reference, and injecting the value via `TF_VAR_db_password` removes the secret from all source files and provides it only at runtime in a controlled way.
* **Distractor Analysis:**
  * *Why B is correct:* This is the complete, correct remediation. The secret no longer appears in any `.tf` file. The `TF_VAR_` environment variable is set in the pipeline's secrets store or the operator's shell and is never written to disk. The `sensitive = true` declaration ensures the value is masked in all CLI output.
  * *Why A is incorrect:* `nonsensitive()` is a Terraform function that removes the sensitive marking from a value so it can be used in non-sensitive contexts. It does not encrypt anything. Using it on a hardcoded string still leaves the plaintext credential in the source file.
  * *Why C is incorrect:* Local values are evaluated during plan and apply and their resolved values — including secrets — are written to the state file. Moving a secret to a `locals` block does not protect it; it remains in source code and state.
  * *Why D is incorrect:* While `.gitignore` prevents future commits of `terraform.tfvars`, it does not remove the file from the working directory or protect it on developer machines. It also does not solve the root problem if the file has already been committed historically. Environment variable injection is the more robust solution.

---

**Question 5**
Which of the following best describes the security advantage of using HashiCorp Vault's dynamic secrets feature over injecting static credentials via environment variables in a Terraform pipeline?

* A) Vault dynamic secrets are automatically added to the Terraform state file with `sensitive = true`, preventing them from appearing in plan output
* B) Vault generates short-lived, automatically expiring credentials for each Terraform run, reducing the window of exposure if credentials are leaked compared to long-lived static keys
* C) Vault encrypts the Terraform state file at the block level, ensuring each resource's attributes are independently encrypted with separate keys
* D) Vault dynamic secrets bypass the need to declare `variable` blocks in Terraform configuration, simplifying the credential injection process
* **Correct Answer:** B) Vault's dynamic secrets engine generates credentials on demand with a configurable TTL (e.g., 15 minutes). Even if these credentials are captured from logs or state, they expire quickly and cannot be reused after their TTL, drastically reducing the blast radius of a credential leak compared to long-lived static access keys.
* **Distractor Analysis:**
  * *Why B is correct:* This is the primary security advantage of dynamic secrets over static injection. Exam questions on Vault focus on the concept of short-lived, just-in-time credentials that are revoked automatically. A static AWS access key may remain valid for months or years if not manually rotated; a Vault-issued credential expires in minutes.
  * *Why A is incorrect:* Vault does not automatically add `sensitive = true` to state values. Whether a Vault-sourced credential appears as sensitive in state depends entirely on how the Terraform configuration declares the relevant `variable` or `output` blocks — it is not automatic.
  * *Why C is incorrect:* Vault does not encrypt the Terraform state file. State encryption is a backend responsibility (S3 server-side encryption, Terraform Cloud's built-in encryption). Vault manages secrets access and dynamic credential issuance; it does not touch state files.
  * *Why D is incorrect:* The Vault provider still requires `variable` or `data` blocks in Terraform configuration to receive and use Vault-sourced values. Dynamic secrets do not eliminate the need for standard HCL declarations; they change where the secret value originates, not how it is consumed by Terraform.
