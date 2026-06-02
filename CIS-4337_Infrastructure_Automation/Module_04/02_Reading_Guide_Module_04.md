# CIS-4337 Infrastructure Automation

## Reading Guide — Module 04: Terraform State — Local and Remote Backends

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This module covers Terraform state: what it is, why it exists, how it is structured, and how to manage it safely. State management is one of the most heavily tested topics on the Terraform Associate 003 exam. Read every section before the lab.

---

## 1. Core Vocabulary

**State File**
A JSON file (`terraform.tfstate`) that maps each HCL resource declaration to the real-world resource ID and current attribute values of the corresponding cloud object. Terraform reads state on every `plan` and writes it after every `apply`.

**Local Backend**
The default backend. Stores `terraform.tfstate` in the working directory. Suitable for individual learning but not for team use due to lack of sharing and locking.

**Remote Backend**
A backend configuration that stores state outside the local filesystem in a shared, access-controlled location. Examples: S3, Azure Blob Storage, Google Cloud Storage, Terraform Cloud.

**State Locking**
A mechanism that prevents two processes from modifying state simultaneously. When Terraform runs `plan` or `apply`, it acquires a lock. Other processes that attempt to acquire the lock while it is held receive an error.

**LockID**
The string primary key attribute required on a DynamoDB table used for S3 backend locking. The table attribute must be named exactly `LockID`.

**State Workspace**
A named instance of state within a backend. Each workspace stores its own independent state file. The default workspace is always named `default`.

**terraform state rm**
Removes a resource record from the state file without destroying the real infrastructure. Used when a resource was deleted outside of Terraform.

**terraform state mv**
Moves a resource to a new address in state without destroying and recreating it. Used when renaming resources or refactoring configurations.

**terraform import**
Brings an existing real-world resource under Terraform management by creating a state record for it. Requires a corresponding resource block in the configuration.

**Sensitive State**
The state file stores all resource attributes in plaintext JSON, including passwords, private keys, and API tokens written to resources. The `sensitive = true` flag only masks CLI output; it does not encrypt state.

---

## 2. State File Structure

A simplified `terraform.tfstate` looks like this:

```json
{
  "version": 4,
  "terraform_version": "1.6.0",
  "serial": 3,
  "lineage": "a1b2c3d4-e5f6-...",
  "outputs": {
    "web_public_ip": {
      "value": "54.23.45.67",
      "type": "string"
    }
  },
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "id": "i-0abc12345",
            "ami": "ami-0c55b159cbfafe1f0",
            "instance_type": "t3.micro",
            "public_ip": "54.23.45.67",
            "tags": {
              "Name": "web-server"
            }
          }
        }
      ]
    }
  ]
}
```

Key fields:

- `version`: State file format version (currently 4).
- `serial`: Increments by 1 on every write. Used to detect concurrent modification.
- `lineage`: A UUID assigned when the state file is first created. Prevents mixing state from different environments.
- `resources`: The list of all managed resources with their real-world attributes.

---

## 3. Remote Backend Configuration

### S3 Backend with DynamoDB Locking

```hcl
terraform {
  backend "s3" {
    bucket         = "my-company-tfstate"
    key            = "prod/webapp/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

The DynamoDB table must exist before `terraform init` is run. Create it with a single string attribute named `LockID` as the partition key. There is no sort key.

### Terraform Cloud Backend

```hcl
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      name = "webapp-prod"
    }
  }
}
```

Terraform Cloud manages locking and encryption automatically. No additional services are needed.

### Azure Blob Storage Backend

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstate12345"
    container_name       = "tfstate"
    key                  = "prod/webapp.tfstate"
  }
}
```

### Backend Configuration Rules

- Only one `backend` block may exist in a configuration.
- Backend blocks cannot use variable references. Values must be literals (or use partial configuration).
- Changing the backend requires re-running `terraform init` with the `-migrate-state` flag.

---

## 4. State Commands Reference

| Command | Purpose |
|---|---|
| `terraform state list` | List all resources in state |
| `terraform state show <addr>` | Show all attributes of a resource |
| `terraform state mv <src> <dst>` | Rename or move a resource in state |
| `terraform state rm <addr>` | Remove a resource from state (no cloud destruction) |
| `terraform state pull` | Download and print remote state to stdout |
| `terraform state push` | Upload a local state file to the remote backend |
| `terraform force-unlock <id>` | Release a stuck lock |
| `terraform refresh` | Update state to match live infrastructure (deprecated; use `plan -refresh-only`) |

---

## 5. State Security Best Practices

The state file is a sensitive artifact. Apply all of the following:

- Enable server-side encryption on S3 buckets used for state (`encrypt = true`).
- Restrict S3 bucket access with IAM policies. No public access.
- Enable S3 bucket versioning to allow state recovery.
- Never store state files in Git. Add `*.tfstate` and `*.tfstate.backup` to `.gitignore`.
- Use Terraform Cloud, which encrypts state at rest automatically.
- Rotate IAM credentials used to access the state backend regularly.

---

## 6. Importing Existing Resources

When resources were created manually before Terraform adoption, use `terraform import` to bring them under management.

Step 1: Write the resource block in HCL.

```hcl
resource "aws_instance" "legacy" {
  # attributes will be populated after import
}
```

Step 2: Run the import command, providing the resource address and the real-world ID:

```bash
terraform import aws_instance.legacy i-0abc12345
```

Step 3: Run `terraform plan` to see what attributes differ between the imported state and your HCL block.

Step 4: Update the HCL block to match the imported state until the plan shows no changes.

Note: As of Terraform 1.5, `import` blocks in HCL are also supported, enabling declarative import:

```hcl
import {
  to = aws_instance.legacy
  id = "i-0abc12345"
}
```

---

## 7. Backend Locking Capability Reference

| Backend | Native Locking |
|---|---|
| Local | No |
| S3 | Yes (requires DynamoDB) |
| Azure Blob | Yes (native) |
| Google Cloud Storage | Yes (native) |
| Terraform Cloud | Yes (automatic) |
| HTTP | No (optional) |
| Consul | Yes (native) |

---

## 8. Required Reading

- Read the state overview at developer.hashicorp.com/terraform/language/state
- Read the S3 backend reference at developer.hashicorp.com/terraform/language/settings/backends/s3
- Read the `terraform state` command reference at developer.hashicorp.com/terraform/cli/commands/state
- Read the import guide at developer.hashicorp.com/terraform/cli/import

---

## 9. Terraform Associate 003 Exam Tips

**Tip 1.** The DynamoDB table for S3 locking must have a partition key attribute named exactly `LockID`. The attribute type is String. This exact detail appears on the exam.

**Tip 2.** `sensitive = true` suppresses CLI output only. Sensitive values are always stored as plaintext in the state file. Know this distinction — the exam tests it directly.

**Tip 3.** `terraform state rm` removes a resource from Terraform management without deleting the real cloud resource. `terraform destroy -target` deletes the real resource. These are opposites.

**Tip 4.** The `serial` field in state increments on every write. If two processes write state concurrently, the one with the lower serial is rejected. This is the mechanism that locking prevents.

**Tip 5.** Backend blocks cannot reference variables. This means environment, project name, and bucket name must be hardcoded in the backend block or supplied via partial configuration (`-backend-config` flag on init).

**Tip 6.** `terraform workspace new <name>` creates a new workspace. State for named workspaces is stored at a different key path within the backend (e.g., `env:/staging/key`).

**Tip 7.** Terraform Cloud workspaces and CLI workspaces are conceptually similar but functionally different. Terraform Cloud workspaces also manage variables, run policies, and team access.

**Tip 8.** `terraform refresh` is deprecated. Use `terraform apply -refresh-only` to update state without making infrastructure changes.

---

## 10. Study Checklist

- [ ] Explain why Terraform needs a state file in your own words.
- [ ] List the four problems with local state for team use.
- [ ] Write the `backend "s3"` configuration block from memory with all required arguments.
- [ ] Explain what the `LockID` DynamoDB attribute is and why it is needed.
- [ ] List all seven `terraform state` subcommands and their purpose.
- [ ] Explain what `terraform state rm` does versus `terraform destroy -target`.
- [ ] Describe the correct way to import an existing resource.
- [ ] List which backends support native locking without additional services.
- [ ] Complete the Module 04 lab, quiz, and discussion post.

---

Module 04 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
