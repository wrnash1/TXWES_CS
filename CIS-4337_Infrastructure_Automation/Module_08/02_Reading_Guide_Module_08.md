# Reading Guide: Module 08 — Terraform State Management

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Learning Objectives

After completing this reading guide you will be able to:

- Explain the purpose and structure of `terraform.tfstate`
- Configure S3, Azure Blob, and GCS remote backends
- Describe how state locking works and how to recover from a stuck lock
- Execute all major `terraform state` subcommands correctly
- Apply security best practices to protect state files in production

---

## 1. What Is Terraform State

Terraform state is a persistent record that maps the resources defined in your configuration to the real-world objects that were created. Without state, Terraform cannot determine whether a resource already exists, what its current attributes are, or whether a change to your configuration requires an update or a destroy-and-recreate.

### 1.1 State File Format

The state file is a JSON document stored by default as `terraform.tfstate` in the working directory. The format is versioned and managed by Terraform — you should never manually edit it except in carefully controlled recovery scenarios.

Key fields in a state file:

```json
{
  "version": 4,
  "terraform_version": "1.5.7",
  "serial": 12,
  "lineage": "a1b2c3d4-...",
  "outputs": {},
  "resources": []
}
```

| Field | Purpose |
|---|---|
| `version` | State format version (currently 4) |
| `terraform_version` | Terraform version that wrote this state |
| `serial` | Monotonically increasing counter; detects conflicts |
| `lineage` | Unique ID for this state; prevents mixing unrelated states |
| `outputs` | Persisted output values from the last apply |
| `resources` | Array of all tracked resources and their attributes |

### 1.2 State and the Dependency Graph

Terraform builds a dependency graph from both your configuration and your state. This graph determines the order of operations during plan and apply. State stores resource IDs that providers need to read current status — for example, an AWS instance ID is needed to call the `DescribeInstances` API.

### 1.3 terraform.tfstate.backup

Each time Terraform updates the state, it first writes a backup to `terraform.tfstate.backup`. This is your last resort recovery option when local state is corrupted.

---

## 2. Remote Backends

A backend defines where Terraform stores state and how operations are performed. The built-in local backend stores state on the local filesystem. Remote backends store state in a shared, durable location.

### 2.1 Configuring a Backend

Backend configuration belongs inside the `terraform` block:

```hcl
terraform {
  required_version = ">= 1.5"

  backend "s3" {
    bucket = "my-tf-state-bucket"
    key    = "prod/api/terraform.tfstate"
    region = "us-east-1"
  }
}
```

**Important**: Backend configuration cannot use variables or references. All values must be literals. If you need to vary the backend configuration per environment, use partial configuration with `-backend-config` flags on `terraform init`.

### 2.2 Partial Backend Configuration

```hcl
# backend.tf (committed to git — no secrets)
terraform {
  backend "s3" {}
}
```

```bash
# Run at init time (values come from CI secrets or a config file)
terraform init \
  -backend-config="bucket=my-tf-state-bucket" \
  -backend-config="key=prod/api/terraform.tfstate" \
  -backend-config="region=us-east-1"
```

This pattern keeps the configuration portable while keeping the actual bucket name and key outside of version control if needed.

### 2.3 S3 Backend

```hcl
terraform {
  backend "s3" {
    bucket         = "acme-tfstate"
    key            = "prod/vpc/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
    kms_key_id     = "arn:aws:kms:us-east-1:123456789:key/abc123"
  }
}
```

| Argument | Required | Purpose |
|---|---|---|
| `bucket` | Yes | Name of the S3 bucket |
| `key` | Yes | Path within the bucket to store the state file |
| `region` | Yes | AWS region of the bucket |
| `encrypt` | No | Enable server-side encryption (strongly recommended) |
| `dynamodb_table` | No | DynamoDB table name for state locking |
| `kms_key_id` | No | KMS key ARN for additional encryption |

### 2.4 Azure Blob Backend

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-terraform-state"
    storage_account_name = "acmetfstate001"
    container_name       = "tfstate"
    key                  = "prod/app/terraform.tfstate"
  }
}
```

Azure Blob Storage provides native locking via blob leases. No additional locking resource is required.

### 2.5 GCS Backend

```hcl
terraform {
  backend "gcs" {
    bucket = "acme-tfstate-bucket"
    prefix = "prod/app"
  }
}
```

GCS provides native locking. When using the GCS backend, the state file path is `<prefix>/default.tfstate`.

### 2.6 Backend Comparison

| Feature | S3 | Azure Blob | GCS |
|---|---|---|---|
| Locking mechanism | DynamoDB (separate resource) | Native blob lease | Native object lock |
| Encryption at rest | Optional (`encrypt = true`) | Default (Azure manages) | Default (Google manages) |
| Versioning | Bucket-level setting | Blob versioning | Object versioning |
| CLI auth | AWS credentials / IAM | `az login` / SP | `gcloud auth` / SA |

---

## 3. State Locking

State locking prevents two Terraform processes from reading and writing state simultaneously. Without locking, concurrent `terraform apply` operations can result in state corruption — a situation that may require manual recovery.

### 3.1 How Locking Works

When an operation begins, Terraform writes a lock record to the locking mechanism. The record includes:

- A randomly generated Lock ID
- The operation type (plan or apply)
- The user or process identity
- A timestamp

If Terraform cannot acquire the lock within a timeout period, it displays an error containing the Lock ID.

### 3.2 Force Unlock

If a Terraform process is forcibly killed during an operation, the lock record may remain. Use `force-unlock` to release it:

```bash
terraform force-unlock <LOCK-ID>
```

The Lock ID is displayed in the error message when Terraform fails to acquire the lock. Use `-force` to skip the confirmation prompt in automation:

```bash
terraform force-unlock -force <LOCK-ID>
```

**Warning**: Only use `force-unlock` when you are certain no other process is actively running. Forcibly releasing a lock while an apply is in progress can corrupt state.

---

## 4. Terraform State Commands

### 4.1 Command Reference

| Command | Description |
|---|---|
| `terraform state list` | List all tracked resources |
| `terraform state show <resource>` | Display attributes of a specific resource |
| `terraform state mv <src> <dst>` | Move or rename a resource in state |
| `terraform state rm <resource>` | Remove a resource from state (does not destroy) |
| `terraform state pull` | Download state to stdout |
| `terraform state push <file>` | Upload a state file to the backend |
| `terraform force-unlock <id>` | Release a stuck state lock |

### 4.2 terraform state list

```bash
# List all resources
terraform state list

# Filter by resource type prefix
terraform state list aws_instance

# List resources in a module
terraform state list module.network
```

### 4.3 terraform state show

```bash
terraform state show aws_instance.web
```

Output includes all attributes known to Terraform — both those in your configuration and those that the provider populated after creation (such as IDs, ARNs, and dynamically assigned IPs).

### 4.4 terraform state mv

Used during configuration refactoring to tell Terraform that an existing resource is now tracked under a different address — without destroying and recreating it.

```bash
# Rename resource
terraform state mv aws_instance.web aws_instance.app

# Move resource into a module
terraform state mv aws_instance.app module.compute.aws_instance.app

# Move resource between state files
terraform state mv \
  -state=old.tfstate \
  -state-out=new.tfstate \
  aws_instance.web aws_instance.web
```

### 4.5 terraform state rm

```bash
# Remove a single resource from tracking
terraform state rm aws_instance.web

# Remove all resources in a module
terraform state rm module.network
```

After `rm`, the resource is no longer managed by this Terraform configuration. The real infrastructure is unaffected. A subsequent `terraform plan` will propose to create the resource again.

---

## 5. State File Security

### 5.1 What State Files Contain

State files contain sensitive information including:

- All resource attribute values (including passwords, tokens, private keys)
- Output values, including sensitive outputs
- Provider credentials that were cached during initialization
- Database connection strings with credentials

### 5.2 Security Best Practices

**Version control exclusion**:

```gitignore
# Add to .gitignore
terraform.tfstate
terraform.tfstate.backup
*.tfstate
*.tfstate.*
.terraform/
crash.log
```

**Encryption at rest**: Use `encrypt = true` with the S3 backend, optionally specifying a KMS key. Azure and GCS encrypt by default.

**Access control**: Use the principle of least privilege.

- S3: IAM policies allowing `s3:GetObject`, `s3:PutObject`, `s3:DeleteObject` only to authorized principals
- DynamoDB: `dynamodb:GetItem`, `dynamodb:PutItem`, `dynamodb:DeleteItem` on the lock table
- Azure: RBAC `Storage Blob Data Contributor` role on the container
- GCS: `storage.objects.create`, `storage.objects.get`, `storage.objects.delete` via IAM

**Enable versioning**: S3 bucket versioning, GCS object versioning, or Azure blob versioning allows recovery of previous state.

**Audit logging**: Enable S3 access logs, GCS audit logs, or Azure Monitor to detect unauthorized state access.

---

## 6. Remote State Data Source

You can read outputs from another Terraform configuration's state using the `terraform_remote_state` data source:

```hcl
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "acme-tfstate"
    key    = "prod/network/terraform.tfstate"
    region = "us-east-1"
  }
}

resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_id
}
```

This is one of the primary patterns for cross-stack communication in large Terraform codebases.

---

## 7. Exam Tips — Terraform Associate 003

1. **S3 locking requires DynamoDB**: The S3 backend does not provide native locking; you must create and configure a DynamoDB table separately.

2. **`state rm` does not destroy**: Removing from state leaves the real resource running; it just removes Terraform's tracking.

3. **`state mv` prevents destroy/recreate**: This is the correct approach when renaming a resource in your `.tf` files.

4. **Backend config cannot use variables**: All values in a `backend` block must be literals. Use `-backend-config` flags for dynamic values.

5. **`terraform init` migrates state**: When you change backends, `terraform init` detects the change and prompts you to migrate the existing state.

6. **Serial number conflicts**: If two processes write conflicting state, the lower serial is rejected. This is a safety mechanism, not an automatic resolution.

7. **`terraform state pull`**: Downloads the current state to stdout; useful for inspection and backup before risky operations.

8. **Sensitive outputs in state**: Even outputs marked `sensitive = true` are stored in plain text in state — encryption must be at the backend level.

---

## 8. Summary

Terraform state is the bridge between your configuration and real infrastructure. Managing state correctly — using remote backends with locking, encryption, versioning, and access control — is one of the most important operational skills for any Terraform practitioner.

The `terraform state` subcommands give you surgical control over state content, enabling refactoring without infrastructure disruption.

---

## 9. Supplemental Resources

**1. Terraform State Documentation**
<https://developer.hashicorp.com/terraform/language/state>
The official overview of Terraform state: why it exists, what it contains, the risks of sensitive data in state, and the case for remote backends. Maps directly to the exam's state management domain.

**2. Terraform S3 Backend Reference**
<https://developer.hashicorp.com/terraform/language/settings/backends/s3>
Complete reference for the S3 backend including all arguments, the DynamoDB locking table requirements (exact `LockID` attribute), partial configuration via `-backend-config`, and KMS encryption setup.

**3. Terraform `state` Command Reference**
<https://developer.hashicorp.com/terraform/cli/commands/state>
Documents all `terraform state` subcommands: `list`, `show`, `mv`, `rm`, `pull`, `push`. Each subcommand page includes flags, examples, and guidance on when to use each command safely.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
