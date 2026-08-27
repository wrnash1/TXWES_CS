# Reading Guide: Module 13 — Terraform Security Best Practices

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Overview

This reading guide covers the security principles that govern how Terraform configurations handle credentials, sensitive data, state files, and cloud permissions. Security is not optional in production Terraform work — every team that manages real infrastructure must understand these concepts before their first production deployment.

**Estimated reading time:** 60–75 minutes

---

## Section 1: The Secrets Problem in Infrastructure as Code

### 1.1 Why Secrets Leak into Terraform

Secrets appear in Terraform code through several common paths. A developer migrating from manual configuration may copy database passwords directly into a `locals` block. A tutorial may show a provider configuration with hardcoded API credentials. An engineer may set a variable default to a real password for quick testing and forget to remove it before committing.

Once a secret is committed, git history preserves it forever. `git filter-repo` can remove secrets from history, but every clone made before the removal still contains the secret. The only safe response to a committed secret is to immediately rotate it and treat it as compromised.

### 1.2 The `git-secrets` Defense

`git-secrets` is a tool that scans staged changes for patterns that match known secret formats — AWS key IDs, private keys, passwords — before allowing a commit. Installing it as a pre-commit hook provides a last-resort check before secrets reach the repository. This is a complement to, not a replacement for, proper secrets management architecture.

### 1.3 Terraform-Specific Secret Exposure Patterns

Beyond committed secrets, Terraform has specific exposure patterns to understand:

- Provider credentials in the `provider` block: credentials must come from environment variables or instance role — never from literal values in the block.
- Variable default values: `default = "my-password"` in a variable declaration is committed to source control along with the code.
- `local` values: a `locals` block that assembles a connection string from a password variable stores that string in state.
- `output` values: an output that includes a password or key will display it in terminal output unless marked `sensitive = true`.

---

## Section 2: Environment Variables for Secrets

### 2.1 The TF_VAR_ Convention

Terraform reads input variable values from environment variables following the `TF_VAR_<variable_name>` pattern. Setting `TF_VAR_db_password=supersecret` in the shell is equivalent to setting `db_password = "supersecret"` in a `terraform.tfvars` file. The value is available to the configuration without appearing in any source file.

This works for any variable of any type. For complex types (lists, maps), you can use HCL syntax in the environment variable value.

### 2.2 Provider Authentication Environment Variables

Each Terraform provider defines its own environment variable conventions for authentication. These are the standard variables — all providers check for these before falling back to explicit configuration:

AWS provider:

- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for static credentials
- `AWS_PROFILE` to select a named profile from `~/.aws/credentials`
- No environment variable needed when running on an EC2 instance with an instance profile — the provider reads from the instance metadata service automatically

Azure provider:

- `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID` for service principal authentication
- `ARM_USE_MSI=true` to use managed identity on Azure VMs

GCP provider:

- `GOOGLE_CREDENTIALS` containing a service account key JSON string
- `GOOGLE_APPLICATION_CREDENTIALS` pointing to a service account key JSON file
- No variable needed when running on GCE with a service account attached

### 2.3 CI Platform Secret Stores

CI/CD platforms provide secure storage for environment variables that are injected into pipeline runners:

- GitHub Actions: repository secrets and environment secrets, accessible via `${{ secrets.SECRET_NAME }}`
- GitLab CI: CI/CD variables with the Protected flag (only available on protected branches) and Masked flag (value is masked in job logs)
- Jenkins: credentials store with the `withCredentials` pipeline step
- CircleCI: context variables scoped to an organization context

These stores encrypt secrets at rest and mask them in logs. They are appropriate for team-level credentials. They do not provide rotation, audit trails, or per-user access granularity — for those features, use Vault.

---

## Section 3: HashiCorp Vault Integration

### 3.1 Vault Architecture Overview

HashiCorp Vault is a secrets management platform with these core capabilities:

- **Secret storage**: encrypted key-value storage for static secrets
- **Dynamic secrets**: on-demand generation of time-limited credentials
- **Authentication**: multiple methods including AppRole, Kubernetes, AWS IAM, and OIDC
- **Access control policies**: fine-grained rules specifying which identities can read which paths
- **Audit logging**: every read, write, and authentication event is logged

The Vault server stores secrets encrypted with AES-256-GCM. The encryption keys themselves are protected by a root key that is split using Shamir's Secret Sharing — requiring multiple key holders to unseal the Vault after a restart.

### 3.2 Vault Provider Configuration

The Terraform Vault provider connects to a Vault server and reads secrets as data sources. Configuration requires the Vault server address and an authentication token or method:

```hcl
provider "vault" {
  address = "https://vault.example.com:8200"
}
```

In CI pipelines, the Vault token is passed via the `VAULT_TOKEN` environment variable or via AppRole authentication configured in the provider block.

### 3.3 Reading Static Secrets from Vault KV

Vault's KV (Key-Value) secrets engine stores arbitrary key-value pairs. To read a secret:

```hcl
data "vault_kv_secret_v2" "db_credentials" {
  mount = "secret"
  name  = "production/database"
}

resource "aws_db_instance" "main" {
  username = data.vault_kv_secret_v2.db_credentials.data["username"]
  password = data.vault_kv_secret_v2.db_credentials.data["password"]
}
```

The `data` attribute returns a map of all key-value pairs stored at that Vault path.

### 3.4 Dynamic AWS Credentials from Vault

Vault's AWS secrets engine generates temporary IAM credentials on demand:

```hcl
data "vault_aws_secret_backend_creds" "terraform_creds" {
  backend = "aws"
  role    = "terraform-deployer"
}

provider "aws" {
  access_key = data.vault_aws_secret_backend_creds.terraform_creds.access_key
  secret_key = data.vault_aws_secret_backend_creds.terraform_creds.secret_key
  token      = data.vault_aws_secret_backend_creds.terraform_creds.security_token
}
```

The IAM credentials expire automatically after the TTL configured in the Vault role. This eliminates long-lived access keys entirely.

### 3.5 AppRole Authentication in CI Pipelines

AppRole is the recommended Vault authentication method for CI pipelines. It uses two factors:

- A **Role ID** — semi-public, identifies the application role. Can be stored in CI configuration.
- A **Secret ID** — secret, time-limited, single-use. Retrieved from Vault just before pipeline execution.

The pipeline fetches a fresh Secret ID from Vault at job start, authenticates with the Role ID + Secret ID pair, receives a Vault token, and uses that token to read secrets. The Secret ID and token expire automatically. This eliminates long-lived Vault tokens.

---

## Section 4: Sensitive Variables and Outputs

### 4.1 The sensitive Attribute

Declaring a variable with `sensitive = true` instructs Terraform to redact its value from all console output, plan output, and error messages:

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}
```

When this variable flows into resource arguments, Terraform tracks the sensitivity and redacts the value wherever it would appear in output. If you reference a sensitive variable in a non-sensitive local or output, Terraform raises a warning and requires you to explicitly acknowledge the exposure.

### 4.2 Sensitive Outputs

```hcl
output "rds_endpoint" {
  value     = aws_db_instance.main.endpoint
  sensitive = false
}

output "rds_password" {
  value     = var.db_password
  sensitive = true
}
```

Sensitive outputs are hidden from `terraform output` (shown as `(sensitive value)`) but are included in `terraform output -json` for programmatic consumption. They are always written to the state file.

### 4.3 What sensitive Does Not Do

Marking a variable or output as `sensitive = true` does not:

- Encrypt the value in the state file
- Prevent the value from being read by anyone with state file access
- Remove the value from Vault, AWS Secrets Manager, or any other backing store

It only suppresses display in Terraform's own output streams. State file encryption is a separate, required control.

---

## Section 5: State File Security

### 5.1 What State Files Contain

The Terraform state file (`terraform.tfstate`) is a JSON document that records:

- Every managed resource and its current attribute values
- Output values including sensitive ones
- Provider configuration including some authentication metadata
- Resource dependencies and meta-information

For an RDS instance, the state file contains the database endpoint, port, database name, username, and — in some providers — the master password. This makes the state file a high-value target for attackers.

### 5.2 Remote Backend Requirements

Remote backends solve the local state problem:

- **S3 backend**: requires an S3 bucket with versioning enabled, SSE-KMS encryption, and a DynamoDB table for state locking. All three components are required for a production-grade setup.
- **Azure Blob Storage backend**: built-in encryption; configure with a storage account, container, and access key or managed identity.
- **GCP Cloud Storage backend**: configure with a bucket name; enable CMEK for customer-managed encryption.
- **Terraform Cloud / HCP Terraform**: provides state storage, encryption, locking, access control, and audit logging in a managed service.

### 5.3 State Locking

State locking prevents concurrent `terraform apply` runs from corrupting the state file. Without locking, two engineers running apply simultaneously can interleave writes and produce a corrupted state.

- S3 backend uses DynamoDB for locking. The DynamoDB table must have a primary key named `LockID` of type String.
- Azure Blob Storage uses native blob leases for locking.
- GCP Cloud Storage uses object versioning and conditional writes.
- Terraform Cloud uses a built-in locking mechanism.

If a Terraform command is interrupted, the lock may not be released automatically. Use `terraform force-unlock <lock-id>` to manually release a stale lock after verifying no other operation is in progress.

### 5.4 Terraform 1.4+ State Encryption

Terraform 1.4 introduced an experimental `encryption` block for encrypting state data locally before writing to the backend. This provides an additional layer of protection where the state is encrypted client-side before leaving the Terraform process. Production use requires careful key management — losing the encryption key means losing access to the state.

---

## Section 6: Least-Privilege IAM Design

### 6.1 The Principle of Least Privilege

Least privilege means granting only the permissions required to perform a specific task and nothing more. For Terraform, this means the execution role has exactly the permissions needed to create, read, update, and delete the resources in that workspace — and no others.

### 6.2 Building a Least-Privilege Policy

The process for building a least-privilege Terraform execution policy:

1. Start with the resource types your configuration manages. List every `resource` and `data` block.
2. Map each resource type to its required IAM actions. AWS documentation lists required permissions for each API call under the "Actions, resources, and condition keys" section.
3. Build an IAM policy granting exactly those actions on the specific resource ARNs.
4. Test the policy by running `terraform plan` and `terraform apply` and fixing any access denied errors.
5. After 30–90 days, use IAM Access Analyzer to review which permissions were actually used and remove unused ones.

### 6.3 Permission Boundaries

AWS IAM permission boundaries define the maximum permissions an entity can have. Even if additional policies are attached later, the effective permissions cannot exceed the boundary. Setting a permission boundary on the Terraform execution role prevents privilege escalation attacks where an attacker uses the execution role to attach a more permissive policy.

### 6.4 Separating Plan and Apply Permissions

A mature security architecture separates the permissions for plan (read-only) and apply (read-write). The plan role has read permissions on all relevant resource types, allowing it to describe current state and generate accurate plans. The apply role has the full create/update/delete permissions.

In a CI pipeline, pull request jobs use the plan role. The apply job — triggered only after merge — uses the apply role. This limits the blast radius of a compromised PR pipeline.

---

## Section 7: CIS Benchmarks and Compliance Mapping

### 7.1 CIS Benchmark Overview

The CIS Benchmarks are consensus-based security configuration guides published by the Center for Internet Security. For cloud infrastructure, the most relevant are:

- CIS AWS Foundations Benchmark v3.0
- CIS Microsoft Azure Foundations Benchmark v2.0
- CIS Google Cloud Platform Foundation Benchmark v2.0

Each benchmark consists of numbered controls with descriptions, rationale, audit procedures, and remediation steps. Controls are categorized as Level 1 (basic, low impact) and Level 2 (advanced, may impact functionality).

### 7.2 Terraform Mappings for Key CIS Controls

Selected CIS AWS controls and their Terraform resource mappings:

- CIS 2.1.1 (S3 versioning): `aws_s3_bucket_versioning`
- CIS 2.1.2 (S3 public access block): `aws_s3_bucket_public_access_block`
- CIS 2.2.1 (EBS encryption at rest): `aws_ebs_volume` with `encrypted = true`
- CIS 3.1 (CloudTrail enabled): `aws_cloudtrail` with `is_multi_region_trail = true`
- CIS 4.1 (no unrestricted SSH): `aws_security_group` rules with no `0.0.0.0/0` on port 22
- CIS 1.8 (IAM password policy): `aws_iam_account_password_policy`

### 7.3 Automated Compliance Reporting

Checkov generates compliance reports mapped to CIS controls. The `--compliance` flag outputs results organized by framework and control number. This output can be archived as a CI artifact to serve as automated evidence for security audits.

Integrating Checkov SARIF output with GitHub's code scanning feature makes CIS compliance violations visible in the Security tab of the repository, creating a continuous compliance dashboard.

---

## Key Terms

- **sensitive = true**: Terraform attribute that suppresses a variable's value from appearing in output
- **TF_VAR_**: environment variable prefix for passing Terraform input variable values
- **Dynamic secrets**: credentials generated on demand by Vault with an automatic expiration TTL
- **AppRole**: Vault authentication method using a role ID and secret ID pair
- **SSE-KMS**: AWS server-side encryption using a customer-managed KMS key
- **Least privilege**: granting only the minimum permissions required for a specific task
- **Permission boundary**: AWS IAM construct defining the maximum permissions an entity can have
- **State locking**: mechanism preventing concurrent Terraform operations on the same state file
- **CIS Benchmark**: consensus security configuration standard published by the Center for Internet Security

---

## Review Questions

1. What is the `TF_VAR_` prefix convention and when would you use it over a `.tfvars` file?

2. What does marking a Terraform variable as `sensitive = true` actually protect, and what does it not protect?

3. Describe the AppRole authentication flow for a CI pipeline connecting to HashiCorp Vault.

4. Why must a DynamoDB table be configured alongside an S3 backend for production use?

5. What is the difference between a plan-only IAM role and an apply IAM role, and why would you separate them?

6. Name two CIS AWS Foundations Benchmark controls and the Terraform resource types that implement them.

---

## Supplemental Resources

**1. Terraform Security — Protect Sensitive Input Variables**
<https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variables>
An official HashiCorp tutorial demonstrating the `sensitive = true` variable attribute, how Terraform propagates sensitivity through expressions, and why the state file still requires encryption at the backend level. Includes hands-on examples showing the difference between display suppression and true data protection.

**2. HashiCorp Vault Provider for Terraform**
<https://registry.terraform.io/providers/hashicorp/vault/latest/docs>
The complete Terraform provider documentation for HashiCorp Vault, covering all supported data sources including `vault_kv_secret_v2` for static secrets, `vault_aws_secret_backend_creds` for dynamic IAM credentials, and the AppRole authentication configuration. Essential for understanding Vault-Terraform integration patterns used in secure CI/CD pipelines.

**3. AWS IAM Policy Generator for Terraform**
<https://developer.hashicorp.com/terraform/tutorials/aws/aws-iam-policy>
A HashiCorp tutorial on building least-privilege IAM policies using `aws_iam_policy_document` data sources. Covers the structured policy document syntax, condition keys for scoping resources to specific ARN patterns, and the workflow of iteratively building and testing policies against real `terraform plan` and `terraform apply` runs.

---

End of Module 13 Reading Guide
