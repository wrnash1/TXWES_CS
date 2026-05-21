# Reading Guide: Module 15 - Terraform Security & Secrets Management

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction

Welcome to **Module 15 - Terraform Security & Secrets Management**! This week's study material focuses on protecting sensitive values throughout the Terraform lifecycle — from variable input, through plan and apply, to state storage. Secrets management is a critical operational discipline and a tested topic on the Terraform Associate exam. Mishandling credentials or sensitive outputs is one of the most common real-world Terraform security failures.

As a student, you will learn how to declare sensitive variables and outputs, why sensitive values still appear in state files, how to inject secrets via environment variables without hardcoding them, how to integrate HashiCorp Vault as a dynamic credentials provider, and how to protect state backends that contain sensitive data. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Secret management guidelines**: The set of practices governing how secrets (API keys, passwords, certificates, tokens) are stored, accessed, rotated, and audited in a Terraform workflow. HashiCorp's guidance emphasizes never hardcoding secrets in `.tf` files or `.tfvars` files committed to version control, using short-lived dynamic credentials where possible, and ensuring state backends are encrypted and access-controlled since state files contain sensitive resource attributes in plaintext.
* **Avoiding hardcoded secrets**: The practice of never embedding credentials, passwords, or tokens directly in Terraform configuration files. Hardcoded secrets are exposed to anyone with repository read access and remain permanently visible in Git history. The correct patterns are environment variable injection via `TF_VAR_` prefixes, CI/CD secret stores, or dynamic secret providers like HashiCorp Vault.
* **Environment variables for secret injection**: Using shell environment variables prefixed with `TF_VAR_` to supply sensitive input variable values at runtime without writing them to any file. For example, `export TF_VAR_db_password="s3cr3t"` sets the `db_password` Terraform variable in the current shell session. The variable must still be declared with `variable "db_password" { sensitive = true }` in the configuration.
* **Sensitive outputs**: Terraform `output` blocks declared with `sensitive = true` to prevent their values from being printed to the console during `terraform apply` or `terraform output` runs. Sensitive outputs are still written to the state file in plaintext, so backend access controls remain the critical last line of defense. Referencing a sensitive output in a non-sensitive context produces a Terraform error, enforcing explicit acknowledgment.

---

### 2. Certification Exam Tips

* **`sensitive = true` masks CLI output but not state:** The most commonly tested exam point in this module. Declaring `sensitive = true` on a variable or output causes Terraform to display `(sensitive value)` instead of the actual value in plan and apply output. However, the value is still written to `terraform.tfstate` in plaintext. Secure state storage (encrypted S3 bucket, Terraform Cloud) is essential.
* **State files contain all resource attributes:** Exam scenarios ask about which files may contain secrets. The answer is always `terraform.tfstate` and `terraform.tfstate.backup`. Any resource attribute Terraform manages — including database passwords, private keys, and connection strings — appears in state in plaintext. This is why state backends must be encrypted and access-restricted.
* **HashiCorp Vault provider:** The `vault` provider allows Terraform to read secrets from a running Vault instance at plan/apply time. Vault issues short-lived, dynamically generated credentials (e.g., AWS IAM credentials with a 15-minute TTL) rather than long-lived static secrets. Know the difference between static secret injection (environment variables) and dynamic secret injection (Vault provider).
* **Study Resource:** The HashiCorp documentation on sensitive data in state and the Vault provider covers all exam-relevant patterns: [Sensitive Data in State — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/state/sensitive-data).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the HashiCorp documentation on sensitive data in Terraform state, which explains what is stored in state files, how `sensitive = true` works, and best practices for state backend security: [Sensitive Data in State — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/state/sensitive-data).
* **Required Video:** Watch the video lecture on **Terraform Security & Secrets Management** in the official course playlist, which demonstrates declaring sensitive variables, verifying masked CLI output, and injecting secrets via `TF_VAR_` environment variables: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Mark a variable as sensitive (`sensitive = true`)**: Add `sensitive = true` to a `variable` block for a database password or API key. Run `terraform plan` and observe that the value is masked as `(sensitive value)` in the diff output, confirming the CLI masking behavior.
* **Verify that sensitive output values are not displayed in the CLI console**: Declare an `output` block for the sensitive variable with `sensitive = true`. Run `terraform apply` and confirm the output section shows `(sensitive value)`. Then run `terraform output <name>` and observe the masking. Finally, inspect `terraform.tfstate` directly to confirm the plaintext value is present in the state file.
* **Inject secrets using `TF_VAR_` environment variables**: Remove any default value from the sensitive variable declaration. Export the value as `export TF_VAR_<variable_name>="<value>"` in the terminal. Run `terraform plan` and confirm Terraform resolves the variable from the environment without requiring a `.tfvars` file or command-line `-var` flag.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
* [ ] Read the sensitive data documentation at [Sensitive Data in State — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/state/sensitive-data).
* [ ] Watch the video lecture on **Terraform Security & Secrets Management** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
