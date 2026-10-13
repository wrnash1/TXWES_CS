# Video Script: Module 08 — Terraform State Management

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Introduction (0:00 – 1:30)

Welcome back. I'm Professor Nash and this is Module 08 of CIS-4337, Infrastructure Automation.

In Module 07 you learned to parameterize Terraform with variables and outputs. Now we need to answer a foundational question: how does Terraform remember what it has already built?

The answer is **state**. Terraform state is the mechanism that maps your configuration to real-world infrastructure. Without it, every `terraform plan` would look at your `.tf` files and assume nothing has been created yet.

By the end of this module you will be able to:

- Explain what `terraform.tfstate` is and why it exists
- Configure remote state backends including S3, Azure Blob, and GCS
- Implement state locking to prevent concurrent modifications
- Use all major `terraform state` subcommands
- Apply security best practices to protect state files

Let's get into it.

[PAUSE]

---

## Section 1: What Is Terraform State (1:30 – 4:30)

When you run `terraform apply`, Terraform creates or modifies real infrastructure and then records what it created in a file called `terraform.tfstate`. This JSON file is the single source of truth for Terraform about the current state of your managed resources.

[SHOW TERMINAL]

Let's look at a simplified excerpt from a state file:

```json
{
  "version": 4,
  "terraform_version": "1.5.7",
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "attributes": {
            "id": "i-0abc123def456789",
            "instance_type": "t3.micro",
            "public_ip": "54.234.12.45",
            "ami": "ami-0c55b159cbfafe1f0"
          }
        }
      ]
    }
  ]
}
```

Terraform uses this file to:

- Know which resources exist and their current attribute values
- Compute a diff between desired state (your `.tf` files) and actual state
- Track resource dependencies for safe ordering
- Store sensitive output values and resource metadata

[PAUSE]

### What Happens Without State

Without state, Terraform has no memory. Every plan would compare your configuration against nothing — resulting in a proposal to create every resource again. That would be catastrophic in production.

State is also why `terraform plan` is fast — Terraform does not call every cloud API to check current resource status on every run. It reads the state file and uses it as a cached snapshot.

[PAUSE]

---

## Section 2: Local State and Its Limitations (4:30 – 6:30)

By default, Terraform writes state to a file named `terraform.tfstate` in your working directory. This is **local state** — it lives on the machine running Terraform.

Local state works fine when you are the only person working on an infrastructure project and always running from the same machine. But in a team, local state causes immediate problems:

- **Concurrent modifications**: Two engineers running `terraform apply` at the same time will corrupt state
- **Lost state**: If the state file is deleted or the machine is lost, Terraform loses track of all resources
- **No history**: You cannot see who changed what or roll back to a previous state
- **Secret exposure**: State files often contain sensitive values; local files are hard to audit

These problems are why remote backends exist.

[PAUSE]

---

## Section 3: Remote State Backends (6:30 – 11:00)

A backend is where Terraform stores its state file. When you configure a remote backend, the state is stored in a shared, durable location instead of your local filesystem.

### The backend Block

```hcl
terraform {
  backend "s3" {
    bucket         = "my-company-tfstate"
    key            = "prod/web-app/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

This configuration tells Terraform to store state in an S3 bucket and use a DynamoDB table for locking. We will cover locking in a moment.

[PAUSE]

### S3 Backend

S3 is the most common backend for AWS users. The bucket must exist before you run `terraform init`.

```hcl
terraform {
  backend "s3" {
    bucket  = "acme-terraform-state"
    key     = "environments/prod/app/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
```

Best practices for S3 backends:

- Enable versioning on the bucket so you can recover previous state
- Enable server-side encryption at the bucket level
- Restrict bucket access with IAM policies — only Terraform runners should write to it
- Never put the bucket in the same Terraform configuration you are using it to manage

[PAUSE]

### Azure Blob Backend

For Azure users, the equivalent is Azure Blob Storage:

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-terraform-state"
    storage_account_name = "acmetfstate"
    container_name       = "tfstate"
    key                  = "prod/app/terraform.tfstate"
  }
}
```

Azure provides built-in blob lease locking, so you do not need a separate locking resource like you do with S3/DynamoDB.

[PAUSE]

### GCS Backend

For Google Cloud users:

```hcl
terraform {
  backend "gcs" {
    bucket = "acme-terraform-state"
    prefix = "prod/app"
  }
}
```

GCS provides object versioning and native locking via object metadata. Enable versioning on the bucket as with S3.

[PAUSE]

---

## Section 4: State Locking (11:00 – 13:30)

State locking prevents two Terraform processes from modifying state simultaneously. Without locking, concurrent applies can corrupt the state file — a scenario that is extremely difficult to recover from.

[SHOW TERMINAL]

When Terraform acquires a lock, you will see this message at the start of an operation:

```
Acquiring state lock. This may take a few moments...
```

If another process holds the lock, Terraform waits. If it times out, it shows an error with the Lock ID.

### DynamoDB Locking for S3

For the S3 backend you must create a DynamoDB table separately:

```hcl
resource "aws_dynamodb_table" "tf_lock" {
  name         = "terraform-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

Then reference it in the backend:

```hcl
backend "s3" {
  bucket         = "acme-terraform-state"
  key            = "prod/app/terraform.tfstate"
  region         = "us-east-1"
  encrypt        = true
  dynamodb_table = "terraform-state-lock"
}
```

### Force-Unlock

If a Terraform process is killed mid-apply, the lock may be left in place. Use `terraform force-unlock` to release it:

```bash
terraform force-unlock LOCK-ID-FROM-ERROR-MESSAGE
```

Use this carefully — only when you are certain no other process is running.

[PAUSE]

---

## Section 5: Terraform State Commands (13:30 – 18:00)

Terraform provides several subcommands for inspecting and manipulating state directly. These are essential for operations work.

[SHOW TERMINAL]

### terraform state list

Lists all resources currently tracked in state:

```bash
terraform state list
```

Example output:

```
aws_instance.web
aws_security_group.web_sg
aws_s3_bucket.assets
data.aws_ami.ubuntu
```

### terraform state show

Shows all attributes of a specific resource:

```bash
terraform state show aws_instance.web
```

This outputs the full attribute map of the resource as Terraform knows it — extremely useful for debugging.

[PAUSE]

### terraform state mv

Renames or moves a resource in state without destroying and recreating it. This is essential when you refactor your configuration:

```bash
# Rename a resource
terraform state mv aws_instance.web aws_instance.app_server

# Move a resource into a module
terraform state mv aws_instance.web module.compute.aws_instance.web
```

**Important**: Always run `terraform plan` after a `state mv` to confirm the change has the effect you expect.

[PAUSE]

### terraform state rm

Removes a resource from Terraform's tracking without destroying the actual infrastructure. Use this when you want Terraform to "forget" about a resource — for example, when you are migrating a resource to a different state file.

```bash
terraform state rm aws_instance.web
```

After this command, running `terraform plan` will show a plan to create `aws_instance.web` because Terraform no longer knows it exists.

[PAUSE]

### terraform state pull and push

You can download or upload the entire state file manually:

```bash
# Download state to stdout
terraform state pull > backup.tfstate

# Upload a local state file to the configured backend
terraform state push backup.tfstate
```

Use `pull` to create backups. Use `push` only in emergency recovery situations — it bypasses locking.

[PAUSE]

---

## Section 6: State File Security (18:00 – 21:00)

The state file is one of the most sensitive artifacts in your infrastructure. It contains:

- Resource IDs and ARNs
- IP addresses and DNS names
- Database connection strings
- Passwords and API keys (even sensitive variables are stored in plain text)

[SHOW TERMINAL]

Best practices for state security:

1. **Never commit state to version control**: Add `terraform.tfstate` and `terraform.tfstate.backup` to `.gitignore`

2. **Encrypt state at rest**: Use S3 with `encrypt = true` and AWS KMS; Azure Blob and GCS encrypt by default

3. **Encrypt state in transit**: All major backends use TLS; never use HTTP-only backends

4. **Restrict access with IAM**: Only CI/CD pipelines and authorized operators should have write access to the state bucket

5. **Enable versioning**: S3 bucket versioning, GCS object versioning, or Azure soft-delete allows rollback

6. **Audit access**: Enable S3 access logging or GCS audit logs to track who reads the state file

```gitignore
# .gitignore
terraform.tfstate
terraform.tfstate.backup
*.tfstate
*.tfstate.*
.terraform/
```

[PAUSE]

---

## Summary and Exam Tips (21:00 – 23:00)

Here is what we covered in Module 08:

- `terraform.tfstate` is the JSON file mapping configuration to real infrastructure
- Local state is suitable only for solo, single-machine use
- Remote backends (S3, Azure Blob, GCS) enable team collaboration and durability
- State locking prevents concurrent modification; S3 uses DynamoDB; Azure and GCS have native locking
- `terraform state list`, `show`, `mv`, `rm`, `pull`, `push` are the core state manipulation commands
- State files contain sensitive data and must be encrypted, access-controlled, and never committed to Git

**For the Terraform Associate exam**, remember:

- The S3 backend requires a separate DynamoDB table for locking — it is NOT built in
- `terraform state rm` removes from tracking; it does NOT destroy the real resource
- `terraform state mv` is used for refactoring without destroy/recreate cycles
- `force-unlock` requires the Lock ID from the error message
- State is always in the backend you configure; the default is local (current directory)

[PAUSE]

---

## Closing (23:00 – 24:00)

State management is what separates Terraform beginners from practitioners. Once your infrastructure is in production, the state file is as important as the infrastructure itself. Treat it with the same care.

In Module 09 we dive into Terraform Modules — the mechanism for organizing, reusing, and sharing your infrastructure code. It is one of the most powerful features of Terraform.

See you there.

[END OF SCRIPT]
