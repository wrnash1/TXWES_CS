# Video Script: Module 13 — Terraform Security Best Practices

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Segment 1: Introduction (Lines 1–18)

Welcome back to CIS-4337. This is Module 13: Terraform Security Best Practices.

In the previous module we covered how to automate Terraform with CI/CD pipelines. But a pipeline is only as secure as the credentials it uses, the state files it writes, and the IAM policies it operates under. Security is not a layer you add after the pipeline works — it is a design constraint from the beginning.

In this module we will cover:

- Secrets management: why you must never hardcode secrets in Terraform
- Integrating HashiCorp Vault for dynamic secret retrieval
- Using environment variables as the baseline secrets approach
- Sensitive variable handling in Terraform
- State file security and encryption
- Least-privilege IAM design for Terraform execution
- CIS Benchmarks for Infrastructure as Code

Let us start with the most common mistake engineers make with Terraform and secrets.

---

## Segment 2: Never Hardcode Secrets (Lines 19–40)

I want to start with something that happens more often than it should: secrets committed to source control inside Terraform configurations.

This happens in several ways. An engineer puts an RDS password in a `variable "db_password"` default value. Another puts an API key directly in a `locals` block. Another passes a database connection string as a resource argument without marking it sensitive.

Once a secret is in version control history, it is effectively compromised. Git history does not automatically expire. Even if you delete the file, the secret remains in every clone of the repository. Services like GitHub scan for known secret patterns and alert you, but the window between commit and discovery is often hours or days.

The rule is absolute: no credentials, passwords, API keys, certificates, or tokens ever appear in Terraform source files. Every secret must come from an external source at runtime.

There are three external sources we will cover: environment variables, which are the simplest approach; CI/CD platform secret stores like GitHub Actions secrets or GitLab CI variables; and HashiCorp Vault, which is the enterprise-grade solution.

---

## Segment 3: Environment Variables (Lines 41–60)

Environment variables are the baseline approach to passing secrets to Terraform. They work for any provider and require no additional tooling.

Terraform reads environment variables that follow the `TF_VAR_` prefix convention. If you declare `variable "db_password"` in your configuration, you can set its value by exporting `TF_VAR_db_password=your-secret` in your shell or CI environment.

Most CI platforms let you define environment variables in their secrets store that are injected into the pipeline runner's environment. GitHub Actions calls these repository secrets. GitLab CI calls them CI/CD variables with the protected and masked flags. These secrets are never logged and are masked if they appear accidentally in output.

For cloud provider authentication, the providers themselves follow this pattern. AWS reads `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Azure reads `ARM_CLIENT_ID` and `ARM_CLIENT_SECRET`. GCP reads `GOOGLE_CREDENTIALS` containing a service account JSON key.

Environment variables are sufficient for most teams, but they have limitations. There is no automatic rotation. The secret is visible to anyone with access to the CI platform's secrets UI. There is no audit trail of which pipeline job read which secret. These limitations are why larger organizations adopt Vault.

---

## Segment 4: HashiCorp Vault Integration (Lines 61–90)

HashiCorp Vault is a secrets management platform that provides centralized secret storage, dynamic secret generation, fine-grained access control, and audit logging for every secret read.

The most powerful Vault feature for infrastructure teams is dynamic secrets. Instead of storing a static database password, Vault generates a unique, time-limited credential on demand. The Terraform pipeline requests a credential, Vault creates a new IAM user or database user with the minimum required permissions, and the credential expires automatically after a TTL you define. If the credential is compromised, it expires on its own schedule. There are no shared, long-lived passwords.

Terraform integrates with Vault through the `hashicorp/vault` provider. You configure it with the Vault server address and an authentication method. The most common method in CI pipelines is the AppRole method: a role ID and a short-lived secret ID are combined to authenticate. Kubernetes and AWS IAM authentication methods are also widely used.

Once authenticated, you use `vault_generic_secret` data sources or dedicated data sources like `vault_aws_secret_backend_creds` to retrieve secrets at plan and apply time.

For example, to retrieve a database password from Vault's KV store, you write a data source that reads from a specific Vault path. The retrieved value flows into your RDS resource as the master password. This value will be marked sensitive automatically because it comes from a Vault data source.

Vault also supports the `vault_kv_secret_v2` data source for KV version 2 mounts, which is the current standard. The data source returns a map of all key-value pairs at the specified path, and you reference individual keys with map notation.

One important consideration: when Terraform reads a Vault secret, the value appears in the state file. The state file must therefore also be encrypted — we will cover that shortly.

---

## Segment 5: Sensitive Variable Handling (Lines 91–118)

Terraform has a built-in mechanism for protecting sensitive values: the `sensitive = true` attribute.

When you declare a variable with `sensitive = true`, Terraform will redact that value from all plan and apply output. Instead of showing the actual value, it shows `(sensitive value)`. This prevents passwords and API keys from appearing in log files or PR comments.

You apply the sensitive marker in the variable declaration:

```hcl
variable "db_password" {
  description = "RDS master password"
  type        = string
  sensitive   = true
}
```

You can also mark output values as sensitive:

```hcl
output "db_connection_string" {
  value     = "postgresql://admin:${var.db_password}@${aws_db_instance.main.endpoint}/mydb"
  sensitive = true
}
```

Sensitive outputs are redacted from `terraform output` unless you use `terraform output -json` or `terraform output db_connection_string` explicitly. This means they will not appear in PR plan comments.

There is an important nuance here: marking a variable as sensitive does not encrypt it in the state file. The value is stored in plaintext in `terraform.tfstate` unless you configure state encryption. Sensitive just controls what appears in terminal output.

For Terraform 1.4 and later, state encryption is available as a feature. For earlier versions, you rely on the backend to provide encryption — S3 with SSE enabled, Azure Blob Storage with encryption, and GCP Cloud Storage with CMEK all provide server-side encryption for state files.

---

## Segment 6: State File Security (Lines 119–148)

The Terraform state file is a high-value security target. It contains the complete inventory of your infrastructure including resource IDs, IP addresses, and in some cases sensitive attribute values that providers write to state.

There are three principles for state file security.

The first principle is remote storage. Never store state files on local disks or in version control. Use a remote backend: S3, Azure Blob Storage, GCP Cloud Storage, Terraform Cloud, or the GitLab managed backend. Local state files are invisible to your team, cannot be locked for concurrency, and are lost if the engineer's machine fails.

The second principle is encryption at rest. Your remote backend must encrypt state files. For S3, enable server-side encryption with either S3-managed keys (SSE-S3) or customer-managed KMS keys (SSE-KMS). SSE-KMS is preferred because you control the key. For Azure, enable storage account encryption with a customer-managed key. For GCP, use Cloud Storage with CMEK.

The third principle is access control. The IAM role or service account that runs Terraform should have the minimum permissions needed to read and write the state file. No human should have direct read access to production state files — all state interactions should go through Terraform commands or the Terraform Cloud UI with audit logging enabled.

In Terraform 1.4, HCP Vault-based state encryption was introduced as an experimental feature. In production, using Terraform Cloud or Terraform Enterprise provides state encryption, access control, and audit logs out of the box.

---

## Segment 7: Least-Privilege IAM Design (Lines 149–178)

The Terraform execution role — the IAM role or service account that your CI pipeline assumes — should have the minimum permissions required to provision the specific resources in your configuration.

Many teams start with `AdministratorAccess` in AWS or `Owner` role in Azure because it makes everything work. This is a critical security mistake. If that role is compromised, an attacker has complete control of your cloud account.

The correct approach is to create a purpose-built Terraform execution role for each workspace or environment. That role should have only the permissions needed to create, read, update, and delete the specific resource types in that Terraform configuration.

For an EKS cluster deployment workspace, the execution role might need permissions for EC2 (VPCs, subnets, security groups), EKS (cluster and node group management), IAM (creating node instance roles), and ECR (container registry). It should not have permissions for RDS, DynamoDB, Lambda, or any service not used by that workspace.

AWS IAM provides permission boundaries — a maximum permission set that cannot be exceeded regardless of what policies are attached. Setting a permission boundary on the Terraform execution role prevents privilege escalation even if an attacker manages to attach additional policies.

Regular access reviews using AWS IAM Access Analyzer or Azure's Access Review feature should verify that the execution role permissions match what is actually used. Any permissions not seen in the access logs for 90 days should be removed.

---

## Segment 8: CIS Benchmarks for IaC (Lines 179–210)

The Center for Internet Security publishes benchmark documents that define security configuration standards for major cloud platforms. The CIS AWS Foundations Benchmark, CIS Azure Security Benchmark, and CIS Google Cloud Platform Foundation Benchmark all map directly to Terraform configuration practices.

Key CIS controls that apply directly to Terraform configurations include:

Logging and monitoring: CIS requires CloudTrail enabled in all regions, CloudWatch log metric filters for root account usage, and VPC flow logs enabled. These map to `aws_cloudtrail`, `aws_cloudwatch_log_metric_filter`, and `aws_flow_log` resources.

Networking: CIS prohibits unrestricted inbound access on sensitive ports. Security groups should not allow 0.0.0.0/0 on port 22 (SSH) or 3389 (RDP). These map to `aws_security_group_rule` constraints.

Identity and access management: CIS requires MFA for the root account, password policies with minimum complexity requirements, and no access keys for the root account. These are enforced via `aws_iam_account_password_policy`.

Storage: CIS requires S3 buckets to have public access blocked, versioning enabled, and encryption at rest configured. These map directly to the S3 resources we have already discussed.

Checkov's check library maps its check IDs directly to CIS control numbers. When Checkov runs in your pipeline and reports `CKV_AWS_18`, it is telling you that the check aligns with a specific CIS control. You can generate a Checkov compliance report sorted by CIS control for your auditors.

This alignment between your Terraform code, your CI/CD security scanning, and your compliance framework is what makes IaC auditing dramatically more efficient than manual cloud configuration review.

In the next module we will expand our scope from single-cloud to multi-cloud architectures.

See you there.

---

End of Module 13 Video Script
