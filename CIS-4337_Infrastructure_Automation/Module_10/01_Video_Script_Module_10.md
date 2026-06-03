# Video Script: Module 10 — Terraform Workspaces and Environments

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Introduction (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 10 of CIS-4337, Infrastructure Automation.

Across Modules 07 through 09 we covered variables, state, and modules — the fundamental building blocks of Terraform. Now we tackle one of the more nuanced topics: **managing multiple environments**.

Every team eventually faces this challenge. You need a dev environment for experimentation, a staging environment for testing, and a production environment for real users. How do you manage all three without duplicating your code or tangling your state?

Terraform provides two main approaches: **workspaces** and **directory-based environment isolation**. By the end of this module you will understand both, know when to use each, and be prepared for how the Terraform Associate exam tests this topic.

Let's get started.

[PAUSE]

---

## Section 1: What Are Terraform Workspaces (1:30 – 5:00)

A Terraform workspace is an isolated state environment within a single backend configuration. Each workspace has its own `terraform.tfstate` file, which means operations in one workspace do not affect the state of another.

[SHOW TERMINAL]

Think of it this way: workspaces are like Git branches for your state. The configuration code is shared; the state is separate.

When you first run `terraform init`, you are automatically in the `default` workspace. To see your current workspace:

```bash
terraform workspace show
```

Output: `default`

### Workspace Commands

Let me walk through all the workspace commands:

```bash
# List all workspaces (* marks current)
terraform workspace list

# Create a new workspace and switch to it
terraform workspace new dev

# Switch to an existing workspace
terraform workspace select staging

# Show the current workspace
terraform workspace show

# Delete a workspace (must be empty and not selected)
terraform workspace delete staging
```

[PAUSE]

[SHOW TERMINAL]

Let's run through a quick demonstration:

```bash
terraform workspace new dev
# Created and switched to workspace "dev"!

terraform workspace new staging
# Created and switched to workspace "staging"!

terraform workspace list
#   default
# * staging
#   dev

terraform workspace select dev
# Switched to workspace "dev".

terraform workspace show
# dev
```

[PAUSE]

### Where Workspaces Store State

When using local state, workspaces store their state in a `terraform.tfstate.d/` directory:

```
terraform.tfstate.d/
  dev/
    terraform.tfstate
  staging/
    terraform.tfstate
```

The `default` workspace still uses the root `terraform.tfstate` file.

When using a remote backend like S3, each workspace gets a separate key. For example:

- `default` workspace: `env:/default/my-app/terraform.tfstate`
- `dev` workspace: `env:/dev/my-app/terraform.tfstate`
- `staging` workspace: `env:/staging/my-app/terraform.tfstate`

[PAUSE]

---

## Section 2: Using terraform.workspace in Configuration (5:00 – 8:30)

The real value of workspaces comes from using `terraform.workspace` — a built-in value that returns the name of the currently selected workspace. You can use it to vary your configuration by environment.

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = terraform.workspace == "prod" ? "t3.medium" : "t3.micro"
  tags = {
    Name        = "web-${terraform.workspace}"
    Environment = terraform.workspace
  }
}
```

[SHOW TERMINAL]

Here is a more complete example using `terraform.workspace` with a lookup map for environment-specific sizing:

```hcl
locals {
  env_config = {
    default = {
      instance_type = "t3.micro"
      replicas      = 1
    }
    dev = {
      instance_type = "t3.micro"
      replicas      = 1
    }
    staging = {
      instance_type = "t3.small"
      replicas      = 2
    }
    prod = {
      instance_type = "t3.medium"
      replicas      = 3
    }
  }

  config = local.env_config[terraform.workspace]
}

resource "aws_instance" "web" {
  count         = local.config.replicas
  ami           = data.aws_ami.ubuntu.id
  instance_type = local.config.instance_type
}
```

This pattern is powerful: the same configuration, deployed to multiple workspaces, produces different infrastructure sizes based on the workspace name.

[PAUSE]

---

## Section 3: Limitations of Workspaces (8:30 – 11:30)

Workspaces are a convenient tool, but they have significant limitations that you need to understand — especially for the exam.

### Limitation 1: Shared Backend Configuration

All workspaces within a configuration share the same backend. If you use an S3 backend for `prod`, you also use it for `dev` and `staging`. You cannot have different backends per workspace natively.

### Limitation 2: Shared Provider Configuration

All workspaces share the same provider configuration. This means all environments are typically in the same AWS account, GCP project, or Azure subscription — which violates the security principle of strong environment isolation.

### Limitation 3: Configuration Code Is Shared

The same `.tf` files are used across all workspaces. This is convenient for small differences (instance sizes, replica counts) but becomes unwieldy when environments genuinely require different architectures.

### Limitation 4: Not Visible in Code

When someone reads your Terraform configuration, there is no way to see from the code which workspace is active. The active workspace is implicit, not explicit. This can lead to operators forgetting which workspace they are in and running apply against the wrong environment.

[SHOW TERMINAL]

HashiCorp's own documentation explicitly warns:

> "Workspaces alone are not a suitable mechanism for deployment pipelines targeting separate environments with separate credentials, separate state storage, or separate architectural requirements."

[PAUSE]

---

## Section 4: Directory-Based Environment Isolation (11:30 – 16:00)

The alternative to workspaces — and the approach recommended for production multi-environment setups — is the **directory structure pattern**. Each environment gets its own directory with its own backend configuration.

```
infrastructure/
  environments/
    dev/
      main.tf
      variables.tf
      backend.tf
      terraform.tfvars
    staging/
      main.tf
      variables.tf
      backend.tf
      terraform.tfvars
    prod/
      main.tf
      variables.tf
      backend.tf
      terraform.tfvars
  modules/
    network/
    compute/
    database/
```

[SHOW TERMINAL]

Each environment's `main.tf` calls the shared modules:

```hcl
# environments/prod/main.tf

module "network" {
  source = "../../modules/network"

  environment = "prod"
  vpc_cidr    = "10.0.0.0/16"
}

module "compute" {
  source = "../../modules/compute"

  environment   = "prod"
  vpc_id        = module.network.vpc_id
  instance_type = "t3.medium"
}
```

And each environment has its own backend configuration:

```hcl
# environments/prod/backend.tf
terraform {
  backend "s3" {
    bucket = "acme-tfstate-prod"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

[PAUSE]

### Benefits of Directory Isolation

- **Separate state**: Each environment has completely separate state files — no cross-contamination possible
- **Separate credentials**: Each directory can be deployed with different AWS accounts, Azure subscriptions, or GCP projects
- **Separate approval workflows**: CI/CD pipelines can require manual approval for `prod` but auto-apply `dev`
- **Visible in code**: Reading the directory structure tells you immediately how many environments exist and how they differ
- **Safe blast radius**: An error in `dev` cannot affect `prod` state

[PAUSE]

---

## Section 5: When to Use Workspaces (16:00 – 19:00)

Given these limitations, when ARE workspaces appropriate?

### Good Use Cases

- **Feature branches**: A developer wants an isolated environment to test a specific feature without affecting the shared dev environment

```bash
terraform workspace new feature/new-vpc
terraform apply
# test the feature
terraform destroy
terraform workspace select default
terraform workspace delete feature/new-vpc
```

- **Ephemeral test environments**: CI/CD pipelines can create a workspace per pull request, run tests, then destroy it

- **Small, low-risk infrastructure**: Internal tooling or personal projects where strict environment isolation is not a security requirement

### Inappropriate Use Cases

- **Production-tier environments**: `prod` should always have its own backend, state, and credentials — never share these with lower environments
- **Architecturally different environments**: If `prod` needs a multi-region active-active setup and `dev` is single-region, workspaces cannot cleanly express this
- **Different cloud accounts per environment**: Workspaces share provider configuration; separate accounts require separate provider configurations

[PAUSE]

---

## Section 6: Hybrid Approach (19:00 – 21:30)

Many teams use a hybrid: directories for major environment tiers (dev, staging, prod) and workspaces within a tier for sub-environments or feature branches.

```
environments/
  dev/
    # workspaces used here for feature branches
  staging/
    # single workspace (default)
  prod/
    # single workspace (default)
```

This gives you strong isolation between tiers (directories + separate backends) while still allowing lightweight sub-environment creation within a tier (workspaces).

[SHOW TERMINAL]

A CI/CD workflow using this hybrid:

```bash
# For a feature branch PR:
cd environments/dev
terraform workspace new "pr-${PR_NUMBER}"
terraform apply -var-file="dev.tfvars"
# run integration tests
terraform destroy -var-file="dev.tfvars"
terraform workspace select default
terraform workspace delete "pr-${PR_NUMBER}"
```

[PAUSE]

---

## Summary and Exam Tips (21:30 – 23:30)

Here is what we covered in Module 10:

- Workspaces isolate state within a single configuration and backend
- Workspace commands: `new`, `select`, `list`, `show`, `delete`
- `terraform.workspace` returns the active workspace name and can drive conditional configuration
- State is stored in `terraform.tfstate.d/<workspace>/` for local backends
- Workspaces have significant limitations: shared backend, shared providers, shared code, implicit selection
- Directory-based isolation is better for production environments requiring separate credentials or architecture
- Workspaces are well-suited for ephemeral and feature-branch environments

**For the Terraform Associate exam**, remember:

- The `default` workspace always exists and cannot be deleted
- `terraform workspace new` creates AND switches to the new workspace
- `terraform workspace delete` requires the workspace to not be currently selected
- `terraform.workspace` is a built-in value, not a variable — no `var.` prefix
- HashiCorp recommends directory-based isolation for environments with different credentials

[PAUSE]

---

## Closing (23:30 – 24:00)

Understanding the trade-offs between workspaces and directory isolation is one of those topics that separates engineers who have read the docs from engineers who have been burned in production. Both approaches have valid use cases — the key is matching the tool to the requirement.

Module 11 moves us to Terraform Cloud, where workspaces take on a richer meaning and the collaboration features for teams become much more powerful.

See you there.

[END OF SCRIPT]
