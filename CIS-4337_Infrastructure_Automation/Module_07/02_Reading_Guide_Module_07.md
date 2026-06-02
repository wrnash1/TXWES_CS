# CIS-4337 Infrastructure Automation

## Reading Guide — Module 07: Terraform Workspaces and Environments

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This module covers Terraform workspaces — named state instances within a backend — and the recommended patterns for managing multiple environments. Workspace behavior, limitations, and state storage paths are tested on the Associate 003 exam.

---

## 1. Core Vocabulary

**Workspace**
A named instance of state within a Terraform backend. Each workspace maintains an independent state file. All workspaces in a directory share the same configuration code and provider configuration.

**default Workspace**
The initial workspace present in every Terraform configuration. Its state is stored directly in `terraform.tfstate` with the local backend. The name `default` cannot be deleted.

**terraform.workspace**
A built-in string value that returns the name of the currently active workspace. Can be used in resource arguments, tags, and local expressions.

**State Isolation**
The property of workspaces where resources created in one workspace do not appear in or affect another workspace's state.

**Separate Configuration Directories**
The recommended pattern for managing distinct environments (dev/staging/prod) with different infrastructure requirements, credentials, or compliance controls. Each environment directory has its own backend and state file.

**Terraform Cloud Workspace**
A first-class organizational unit in Terraform Cloud that includes its own variables, credentials, access control, run history, and state. Distinct from CLI workspaces.

---

## 2. Workspace CLI Commands

| Command | Description |
|---|---|
| `terraform workspace list` | List all workspaces; active workspace marked with `*` |
| `terraform workspace show` | Print the name of the active workspace |
| `terraform workspace new <name>` | Create and switch to a new workspace |
| `terraform workspace select <name>` | Switch to an existing workspace |
| `terraform workspace delete <name>` | Delete a workspace (must not be active; state must be empty) |

---

## 3. Workspace State Storage Paths

### Local Backend

```text
terraform.tfstate                           # default workspace
terraform.tfstate.d/
├── dev/
│   └── terraform.tfstate                   # dev workspace
├── staging/
│   └── terraform.tfstate                   # staging workspace
└── prod/
    └── terraform.tfstate                   # prod workspace
```

### S3 Backend

- Default workspace: the `key` you configured.
- Named workspaces: `env:/<workspace_name>/<key>`.

### Terraform Cloud

Each TFC workspace maintains its own state automatically. No additional path configuration is needed.

---

## 4. Using terraform.workspace in HCL

### Resource Naming

```hcl
resource "aws_s3_bucket" "app_data" {
  bucket = "myapp-${terraform.workspace}-data"

  tags = {
    Environment = terraform.workspace
    ManagedBy   = "terraform"
  }
}
```

### Conditional Instance Sizing

```hcl
locals {
  instance_types = {
    default = "t3.micro"
    dev     = "t3.micro"
    staging = "t3.small"
    prod    = "t3.large"
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = lookup(local.instance_types, terraform.workspace, "t3.micro")
}
```

### Workspace-Based Count

```hcl
resource "aws_instance" "worker" {
  count         = terraform.workspace == "prod" ? 3 : 1
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  tags = {
    Name = "worker-${terraform.workspace}-${count.index}"
  }
}
```

---

## 5. Workspace Limitations

Workspaces are **not** recommended for:

- Environments with different provider credentials (different AWS accounts, IAM roles).
- Environments with significantly different infrastructure (different resource types, counts).
- Environments with different compliance or security requirements.
- Cases where strong isolation between environments is required.

Workspaces **are** appropriate for:

- Temporary isolated copies of the same infrastructure for testing.
- Lightweight identical deployments that share the same credentials.
- Terraform Cloud deployments where each workspace has full per-workspace variable and credential isolation.

---

## 6. Recommended Multi-Environment Pattern

```text
infrastructure/
├── modules/
│   ├── vpc/
│   └── compute/
└── environments/
    ├── dev/
    │   ├── main.tf
    │   ├── backend.tf
    │   ├── variables.tf
    │   └── terraform.tfvars
    ├── staging/
    │   ├── main.tf
    │   ├── backend.tf
    │   ├── variables.tf
    │   └── terraform.tfvars
    └── prod/
        ├── main.tf
        ├── backend.tf
        ├── variables.tf
        └── terraform.tfvars
```

Each environment directory:

- Has its own backend configuration and state file.
- Uses its own credentials via environment variables or IAM roles.
- Calls shared modules from the `modules/` directory.
- Has environment-specific values in `terraform.tfvars`.

---

## 7. Complete Workspace Workflow Example

```bash
# Start in the default workspace
terraform workspace list
# * default

# Create a dev workspace
terraform workspace new dev
# Switched to workspace "dev".

# Deploy infrastructure in dev
terraform apply -var-file=dev.tfvars

# Create a staging workspace
terraform workspace new staging
# Switched to workspace "staging".

# Deploy infrastructure in staging
terraform apply -var-file=staging.tfvars

# View all workspaces
terraform workspace list
#   default
#   dev
# * staging

# Switch back to dev
terraform workspace select dev

# Show active workspace
terraform workspace show
# dev
```

---

## 8. Required Reading

- Read the workspaces overview at developer.hashicorp.com/terraform/language/state/workspaces
- Read the CLI workspace commands at developer.hashicorp.com/terraform/cli/commands/workspace
- Read the workspaces when to use guide at developer.hashicorp.com/terraform/cli/workspaces

---

## 9. Terraform Associate 003 Exam Tips

**Tip 1.** The built-in workspace reference is `terraform.workspace` — not `var.workspace`, `local.workspace`, or `env.workspace`. Only one prefix is correct.

**Tip 2.** Workspace isolation is state-only. Configuration code, provider configuration, and provider plugins are shared. This is the most tested workspace concept.

**Tip 3.** The four workspace subcommands to know: `list`, `show`, `new`, `select`. There is also `delete`. `terraform workspace status` is a common wrong-answer distractor — it does not exist.

**Tip 4.** Local workspace state for named workspaces is stored at `terraform.tfstate.d/<name>/terraform.tfstate`. The `default` workspace state is in root `terraform.tfstate`.

**Tip 5.** HashiCorp explicitly recommends against using CLI workspaces for managing environments with different credentials or significantly different infrastructure. Know this limitation for scenario questions.

**Tip 6.** The `default` workspace cannot be deleted. You can delete any other workspace that is not currently active and has empty state.

**Tip 7.** `terraform workspace delete <name>` requires the workspace to have no resources in state. Run `terraform destroy` in the workspace before deleting it.

**Tip 8.** Terraform Cloud workspaces provide per-workspace variables, credentials, and access controls. CLI workspaces do not. The exam distinguishes between these two concepts.

---

## 10. Study Checklist

- [ ] List all five workspace subcommands from memory.
- [ ] Explain the difference between workspace state isolation and configuration isolation.
- [ ] Write a `resource` block that uses `terraform.workspace` in its name and tags.
- [ ] Write a `locals` block that maps workspace names to instance types using `lookup`.
- [ ] Draw the local filesystem path for workspace state files for three workspaces.
- [ ] Explain when workspaces are appropriate and when separate directories are better.
- [ ] Explain the difference between CLI workspaces and Terraform Cloud workspaces.
- [ ] Read all three required documentation pages.
- [ ] Complete the Module 07 lab, quiz, and discussion post.

---

Module 07 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
