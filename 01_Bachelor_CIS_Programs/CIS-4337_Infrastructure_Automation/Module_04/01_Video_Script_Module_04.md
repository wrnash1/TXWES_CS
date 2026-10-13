# CIS-4337 Infrastructure Automation

## Module 04: Terraform State — Local and Remote Backends

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337. I am Professor Nash. In Module 03 we wrote complete HCL configurations with providers, resources, and variables. In this module we focus on one of the most important and most misunderstood concepts in Terraform: state.

By the end of this video you will understand what the state file is, why it exists, how it is structured, the risks of poor state management, how remote backends solve those risks, how to configure the S3 backend with DynamoDB locking, and how to use the `terraform state` subcommands to manage state safely.

State concepts appear throughout the Terraform Associate 003 exam. Domain 4 — Use the Terraform CLI — and Domain 7 — Implement and maintain state — are both heavily weighted on state knowledge.

---

## Section 2: Why State Exists — 1:30–5:00

Terraform needs to know three things to do its job:

1. What infrastructure you declared (the HCL configuration).
2. What infrastructure actually exists (queried from provider APIs).
3. The mapping between declared resources and real resource IDs.

The third item is what the state file provides. Without state, Terraform cannot answer the question: "Is this HCL `aws_instance.web` resource the same thing as EC2 instance `i-0abc12345` that already exists in my AWS account?" State is the link.

Here is a concrete example. You write an HCL resource block for an EC2 instance and run `terraform apply`. AWS assigns the instance an ID: `i-0abc12345`. Terraform records this ID in the state file alongside all the attributes of the resource. On the next `terraform plan`, Terraform looks up `i-0abc12345` in the AWS API to get its current attributes, compares them to your HCL, and reports any differences.

Without the state file, Terraform would have to create a new instance on every apply because it would have no way to know that `i-0abc12345` corresponds to your declared resource.

State also tracks resource dependencies. When you destroy infrastructure, Terraform uses the dependency graph stored in state to determine the correct deletion order.

---

## Section 3: Local State — 5:00–8:00

By default, Terraform stores state in a file named `terraform.tfstate` in the working directory. A backup of the previous state is stored in `terraform.tfstate.backup`. Both are JSON files.

Local state is fine for individual work and learning, but it has serious limitations for teams.

**Problem 1: No locking.** If two team members run `terraform apply` simultaneously against the same local state file, both may read the state before either writes, and then both write — causing one write to silently overwrite the other. The result is state corruption.

**Problem 2: No sharing.** Local state files cannot be accessed by other team members or by CI/CD pipelines unless everyone shares the same machine, which is not practical.

**Problem 3: Security.** State files contain sensitive values in plaintext — database passwords, private keys, API tokens. A local state file sitting in a repository or on a developer's laptop is a security risk.

**Problem 4: No audit trail.** Local state files are not versioned separately from code. If state is accidentally deleted or corrupted, recovery is difficult.

Remote backends solve all four of these problems.

---

## Section 4: Remote Backends — 8:00–13:00

A remote backend stores Terraform state in a shared, external location rather than the local filesystem. The most common remote backends are:

- S3 with DynamoDB locking (AWS)
- Azure Blob Storage
- Google Cloud Storage
- Terraform Cloud / Terraform Enterprise
- HashiCorp Consul

Remote backends provide three critical features: shared storage so teams can collaborate, state locking to prevent concurrent writes, and encryption at rest for security.

Let me show you how to configure the S3 backend.

**[SHOW CODE]**

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "my-company-tfstate"
    key            = "prod/webapp/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

The `bucket` is the S3 bucket that stores the state file. The `key` is the path within the bucket — using a structured path like `env/project/terraform.tfstate` keeps states organized when multiple projects share a bucket. `encrypt = true` enables server-side encryption. `dynamodb_table` names the DynamoDB table used for locking.

The DynamoDB table must exist before `terraform init` is run. It needs a single attribute: a string primary key named `LockID`. This is a classic exam detail — know the key name.

When you run `terraform init` after adding a backend configuration, Terraform prompts you to migrate existing state to the new backend if local state exists.

---

## Section 5: State Locking — 13:00–15:30

State locking prevents two operations from modifying state at the same time. When you run `terraform apply`, Terraform acquires a lock on the state. If another process tries to run apply while the lock is held, it sees an error like:

**[SHOW CODE]**

```text
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: The conditional request failed
Lock Info:
  ID:        abc123
  Path:      prod/webapp/terraform.tfstate
  Operation: OperationTypeApply
  Who:       alice@workstation
  Version:   1.6.0
  Created:   2024-01-15 14:32:00
```

If a Terraform process is forcibly killed while holding a lock, the lock remains in place. Use `terraform force-unlock <lock-id>` to release it manually. Use this only when you are certain no other process is running.

Not all backends support locking. Local, HTTP, and some legacy backends do not. The exam tests which backends support locking natively.

---

## Section 6: terraform state Subcommands — 15:30–19:30

The `terraform state` command provides subcommands for inspecting and manipulating state without directly editing the JSON file. Never manually edit `terraform.tfstate`.

**`terraform state list`** — Lists all resources in state:

**[SHOW CODE]**

```bash
terraform state list
```

Output:

```text
aws_instance.web
aws_s3_bucket.data
aws_vpc.main
module.networking.aws_subnet.public[0]
```

**`terraform state show <address>`** — Shows all attributes of a specific resource:

**[SHOW CODE]**

```bash
terraform state show aws_instance.web
```

**`terraform state mv <source> <destination>`** — Moves a resource to a new address in state. Used when renaming resources or moving them into modules:

**[SHOW CODE]**

```bash
terraform state mv aws_instance.web aws_instance.web_server
```

**`terraform state rm <address>`** — Removes a resource from state without destroying it. Used when a resource was deleted outside of Terraform:

**[SHOW CODE]**

```bash
terraform state rm aws_instance.web
```

**`terraform state pull`** — Downloads and prints remote state to stdout. Useful for inspection or backup.

**`terraform state push`** — Uploads a local state file to the remote backend. Use with extreme caution.

---

## Section 7: State Workspaces (Brief Preview) — 19:30–21:00

Terraform supports named workspaces within a backend. Each workspace has its own state file, enabling multiple environments (dev, staging, prod) to share the same configuration and backend without sharing state.

**[SHOW CODE]**

```bash
terraform workspace new staging
terraform workspace select staging
terraform workspace list
```

We cover workspaces in depth in Module 07 and Module 11. For now, understand that the default workspace is named `default`, and each additional workspace stores state at a distinct path within the backend.

---

## Section 8: Closing — 21:00–22:00

State is Terraform's memory. It maps declared resources to real infrastructure, tracks dependencies, and enables accurate drift detection.

Local state works for learning but creates collaboration, security, and reliability problems for teams. Remote backends solve these with shared storage, locking, and encryption.

The S3 backend requires a DynamoDB table named with a `LockID` string primary key for locking. Terraform Cloud provides locking and encryption automatically.

The `terraform state` subcommands — `list`, `show`, `mv`, `rm` — let you inspect and manage state safely without editing JSON directly.

In Module 05 we cover Terraform modules: how to create reusable infrastructure components and use the public Terraform Registry. Complete the reading guide, lab, quiz, and discussion first.

See you in Module 05.

---

End of Script — Module 04
