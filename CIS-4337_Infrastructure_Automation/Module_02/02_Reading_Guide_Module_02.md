# CIS-4337 Infrastructure Automation

## Reading Guide — Module 02: Terraform Workflow

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This reading guide covers the complete Terraform CLI workflow: init, validate, plan, apply, and destroy. These commands are tested on every section of the Terraform Associate 003 exam and are used in every lab activity for the remainder of the course. Work through this guide carefully before beginning the lab.

---

## 1. Core Vocabulary

**Working Directory**
The filesystem directory containing your Terraform configuration files. All `.tf` files in a working directory are processed together as a single configuration unit. Terraform also creates a `.terraform/` subdirectory here during initialization to store provider plugins and module downloads.

**Terraform Core**
The main Terraform CLI binary. It reads HCL configuration, loads state, computes execution plans, and orchestrates provider calls. It does not know how to communicate with any cloud platform directly — that is the job of providers.

**Provider Plugin**
A separate binary that Terraform Core downloads and invokes to communicate with a specific platform API. Providers translate HCL resource declarations into API calls. Each provider is versioned independently and declared in the `required_providers` block.

**Execution Plan**
The output of `terraform plan`. A detailed description of every resource action (create, update, destroy, replace) that Terraform will take to reconcile the current state with the desired state. No changes are made when generating a plan.

**Saved Plan File**
A binary artifact produced by `terraform plan -out=<filename>`. Contains the exact planned changes. When passed to `terraform apply <filename>`, Terraform executes those changes without re-planning. Used in CI/CD pipelines to ensure the reviewed plan is exactly what gets applied.

**Dependency Lock File**
The `.terraform.lock.hcl` file created by `terraform init`. Records the exact provider versions and checksums selected during initialization. Should be committed to version control to ensure reproducible provider installs.

**Forced Replacement**
A situation where an attribute that cannot be changed on an existing resource needs a new value. Terraform must destroy the old resource and create a new one. Indicated by `-/+` in plan output.

**In-Place Update**
A resource change that can be applied without destroying and recreating the resource. Indicated by `~` in plan output.

**Backend**
The storage location for Terraform state. The local backend (default) stores state in `terraform.tfstate` in the working directory. Remote backends (S3, Terraform Cloud, Azure Blob) store state externally and support team collaboration and state locking.

---

## 2. The Terraform Workflow — Step by Step

### Step 1: Write

Create or modify `.tf` configuration files in your working directory. The standard file organization is:

```text
project/
├── main.tf          # provider and resource blocks
├── variables.tf     # variable declarations
├── outputs.tf       # output blocks
├── terraform.tfvars # variable value assignments
└── versions.tf      # terraform block with required_version
```

All files in the directory are merged at runtime. The split is for human readability, not technical necessity.

### Step 2: terraform init

```bash
terraform init
```

Always run first. Performs three jobs:

1. Initializes the configured backend (or local backend if none specified).
2. Downloads provider plugins declared in `required_providers` into `.terraform/providers/`.
3. Downloads modules referenced in `module` blocks into `.terraform/modules/`.

Safe to re-run: if everything is already initialized, `init` does nothing harmful. Re-run whenever you add a new provider or change the backend configuration.

Key flag: `terraform init -upgrade` forces re-download of all providers to their latest versions within the declared version constraints.

### Step 3: terraform validate

```bash
terraform validate
```

Checks HCL syntax and internal configuration consistency. Does not query provider APIs. Useful as a fast pre-check before running plan. Catches problems like missing required attributes, incorrect argument names, and invalid references.

### Step 4: terraform plan

```bash
terraform plan
terraform plan -out=tfplan
```

The most important workflow command. Refreshes state, computes the diff, and displays the execution plan. No changes are applied.

Use `-out=tfplan` to save the plan for use in CI/CD pipelines. The saved file is binary; inspect it with `terraform show tfplan`.

### Step 5: terraform apply

```bash
terraform apply           # re-plans and prompts for confirmation
terraform apply tfplan    # executes saved plan, no confirmation needed
terraform apply -auto-approve  # skips confirmation, use only in pipelines
```

Executes planned changes. Creates, modifies, or destroys resources. Updates the state file after each resource operation.

### Step 6: terraform destroy

```bash
terraform destroy
terraform destroy -auto-approve
```

Destroys all resources managed by the current configuration and state file. Equivalent to `terraform apply -destroy`. Review the destroy plan before confirming in production environments.

---

## 3. HCL Syntax Reference

### Terraform Settings Block

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}
```

### Provider Block

```hcl
provider "aws" {
  region  = "us-east-1"
  profile = "default"
}
```

### Resource Block

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

### Variable Block

```hcl
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"

  validation {
    condition     = contains(["t3.micro", "t3.small"], var.instance_type)
    error_message = "Instance type must be t3.micro or t3.small."
  }
}
```

### Output Block

```hcl
output "instance_public_ip" {
  description = "Public IP address of the web server"
  value       = aws_instance.web.public_ip
}
```

### Referencing Resources

Within a configuration, reference another resource's attribute using `<type>.<name>.<attribute>`:

```hcl
resource "aws_eip" "web" {
  instance = aws_instance.web.id
}
```

This reference creates an implicit dependency: Terraform creates `aws_instance.web` before `aws_eip.web`.

---

## 4. Plan Output Symbols Reference

| Symbol | Meaning |
|---|---|
| `+` | Resource will be created |
| `-` | Resource will be destroyed |
| `~` | Resource will be updated in place |
| `-/+` | Resource will be destroyed and recreated (forced replacement) |
| `<=` | Data source will be read |
| `+/-` | Resource will be recreated (create before destroy) |

---

## 5. Version Constraint Syntax

Provider version constraints use a specific syntax tested on the exam:

| Constraint | Meaning |
|---|---|
| `= 5.0.0` | Exactly version 5.0.0 |
| `>= 5.0.0` | Version 5.0.0 or higher |
| `~> 5.0` | Any version in the 5.x range (pessimistic constraint) |
| `~> 5.0.0` | Any version in the 5.0.x range |
| `>= 5.0, < 6.0` | Any version from 5.0 up to but not including 6.0 |

The `~>` operator (pessimistic constraint operator) is the most commonly used pattern in production configurations.

---

## 6. The .terraform Directory and .gitignore

After `terraform init`, your working directory contains:

```text
.terraform/
├── providers/
│   └── registry.terraform.io/hashicorp/null/3.2.2/linux_amd64/
│       └── terraform-provider-null_v3.2.2_x5
└── modules/
    (module downloads if any)
.terraform.lock.hcl
```

Add the following to `.gitignore`:

```text
.terraform/
terraform.tfstate
terraform.tfstate.backup
*.tfvars
tfplan
```

Do commit: `.terraform.lock.hcl`, all `.tf` files, and `terraform.tfvars` in environments where it contains no credentials.

---

## 7. Required Reading

- Read the CLI workflow overview at developer.hashicorp.com/terraform/intro/core-workflow
- Read the `terraform init` command reference at developer.hashicorp.com/terraform/cli/commands/init
- Read the `terraform plan` command reference at developer.hashicorp.com/terraform/cli/commands/plan
- Read the `terraform apply` command reference at developer.hashicorp.com/terraform/cli/commands/apply

---

## 8. Terraform Associate 003 Exam Tips

**Tip 1.** The correct workflow sequence is: `init` then `validate` then `plan` then `apply`. The exam tests that `init` must precede `plan`. Running `plan` before `init` fails because provider plugins are not installed.

**Tip 2.** Know all five plan output symbols. The exam presents a plan snippet and asks you to interpret what will happen to a specific resource.

**Tip 3.** `-/+` (forced replacement) is heavily tested. Understand that it means destroy-then-create, not in-place update, and that the resulting resource will have a new ID.

**Tip 4.** `terraform plan -out=tfplan` followed by `terraform apply tfplan` is the CI/CD-safe pattern. The saved plan guarantees that exactly the reviewed changes are applied.

**Tip 5.** `terraform validate` does not check whether resource configurations are valid against the provider's API. It only checks HCL syntax and internal references. A configuration can pass validate but fail during apply if, for example, an AMI ID does not exist.

**Tip 6.** The `.terraform.lock.hcl` file should be committed to version control. The `.terraform/` directory should not. The exam distinguishes between these two.

**Tip 7.** `terraform init -upgrade` updates provider versions to the latest within constraints. This is different from plain `terraform init`, which uses cached versions when possible.

**Tip 8.** `terraform fmt` formats `.tf` files to canonical HCL style. It does not affect functionality, only readability. The exam may ask about the purpose of this command.

---

## 9. Study Checklist

- [ ] List the six Terraform CLI commands in the workflow in correct order from memory.
- [ ] Explain what `terraform init` does to the working directory.
- [ ] Describe the difference between `terraform validate` and `terraform plan`.
- [ ] Identify all five plan output symbols and state what action each represents.
- [ ] Explain what a saved plan file is and why it is used in CI/CD pipelines.
- [ ] List the files that should and should not be committed to Git.
- [ ] Read all four required documentation pages.
- [ ] Complete the Module 02 lab.
- [ ] Complete the Module 02 quiz.
- [ ] Submit your initial discussion post.

---

## 9. Supplemental Resources

**1. Terraform CLI Core Workflow**
<https://developer.hashicorp.com/terraform/intro/core-workflow>
The official walkthrough of the Write-Plan-Apply workflow with explanations of each phase. Covers team collaboration considerations and when to use saved plan files.

**2. Terraform `terraform init` Command Reference**
<https://developer.hashicorp.com/terraform/cli/commands/init>
Complete reference for all `init` flags including `-upgrade`, `-migrate-state`, and `-reconfigure`. Essential for understanding backend initialization and provider plugin management.

**3. Dependency Lock File Documentation**
<https://developer.hashicorp.com/terraform/language/files/dependency-lock>
Explains the `.terraform.lock.hcl` format, what checksums are recorded, when to commit it, and how to update it with `init -upgrade`. Directly supports Module 02 quiz questions on lock file behavior.

---

Module 02 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
