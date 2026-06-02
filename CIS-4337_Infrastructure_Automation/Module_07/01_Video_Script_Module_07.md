# CIS-4337 Infrastructure Automation

## Module 07: Terraform Workspaces and Environments

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337. I am Professor Nash. In this module we cover Terraform workspaces — a feature that allows you to maintain multiple independent state files from a single configuration directory.

By the end of this video you will understand what a workspace is, when to use workspaces versus separate configuration directories, the four workspace CLI commands, how to reference the current workspace in HCL, and where workspace state is stored.

Workspaces appear in the Terraform Associate 003 exam's Domain 4 (Use the Terraform CLI) and Domain 7 (Implement and maintain state).

---

## Section 2: What Is a Workspace — 1:30–5:30

A Terraform workspace is a named instance of state within a backend. Every Terraform configuration starts in the `default` workspace. You can create additional named workspaces that each maintain their own state file while sharing the same configuration code.

The most common use case is lightweight environment management. You want to deploy the same infrastructure for development and production, but they should not share state — a `terraform destroy` in dev should never touch prod.

Here is the mental model: the configuration code is the same, but the state is different. Workspace isolation is state-only.

Let me walk through the workspace commands.

**[SHOW CODE]**

```bash
# List all workspaces; active workspace marked with *
terraform workspace list

# Show only the active workspace name
terraform workspace show

# Create a new workspace
terraform workspace new dev

# Switch to an existing workspace
terraform workspace select prod

# Delete a workspace (must not be active, must have empty state)
terraform workspace delete dev
```

When you create or select a workspace, Terraform switches which state file it reads and writes. Everything else — providers, resources, variables — remains identical.

---

## Section 3: Using terraform.workspace in HCL — 5:30–9:00

The built-in value `terraform.workspace` returns the name of the currently active workspace as a string. You can use it in resource names, tags, and conditional expressions to make deployments workspace-aware.

**[SHOW CODE]**

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"

  tags = {
    Name        = "web-${terraform.workspace}"
    Environment = terraform.workspace
  }
}
```

This single resource block creates differently-sized instances depending on the active workspace, and tags each with its environment name.

You can also use `terraform.workspace` in `locals`:

**[SHOW CODE]**

```hcl
locals {
  environment = terraform.workspace
  is_prod     = terraform.workspace == "prod"

  instance_config = {
    default = { type = "t3.micro",  count = 1 }
    dev     = { type = "t3.micro",  count = 1 }
    staging = { type = "t3.small",  count = 2 }
    prod    = { type = "t3.large",  count = 4 }
  }

  current_config = local.instance_config[terraform.workspace]
}

resource "aws_instance" "web" {
  count         = local.current_config.count
  ami           = data.aws_ami.amazon_linux.id
  instance_type = local.current_config.type

  tags = {
    Name = "web-${local.environment}-${count.index}"
  }
}
```

---

## Section 4: Where State Is Stored by Workspace — 9:00–11:30

With the **local backend**, workspace state is stored at these paths:

- Default workspace: `terraform.tfstate` (in the working directory)
- Named workspaces: `terraform.tfstate.d/<workspace_name>/terraform.tfstate`

**[SHOW CODE]**

```text
my-project/
├── terraform.tfstate              # default workspace
├── terraform.tfstate.d/
│   ├── dev/
│   │   └── terraform.tfstate     # dev workspace
│   └── staging/
│       └── terraform.tfstate     # staging workspace
└── main.tf
```

With **remote backends** (S3, Terraform Cloud), workspace state is stored at distinct paths within the backend. For the S3 backend:

- Default workspace: the `key` value you specified.
- Named workspaces: `env:/<workspace_name>/<key>`.

For Terraform Cloud, each workspace has its own independently managed state.

---

## Section 5: Workspace Limitations and When NOT to Use Them — 11:30–15:00

Workspaces are a powerful but limited tool. The Terraform documentation explicitly states: **workspaces are not recommended for managing environments with significantly different infrastructure, different credentials, or different compliance requirements.**

Here is why.

**No per-workspace variables.** CLI workspaces do not have their own variable files. If production needs a different AWS account, a different S3 bucket name, or a different VPN configuration, you cannot specify that per-workspace without complex conditional logic in the HCL.

**No credential isolation.** All workspaces in a directory share the same provider configuration, which means the same IAM role or access key. This is a serious security concern for prod vs. non-prod.

**State corruption risk.** A mistake running `terraform destroy` in the wrong workspace can delete the wrong environment's resources. With separate directories, you must explicitly navigate to the right directory — an extra safeguard.

**Complex conditional logic.** Using `terraform.workspace` for extensive conditional resource creation creates configurations that are hard to read, test, and maintain.

HashiCorp recommends workspaces for:

- Temporary experiments (spin up an isolated copy of your infra, test something, destroy it).
- Teams using Terraform Cloud, where each Terraform Cloud workspace corresponds to one environment with its own variables, credentials, and access controls.

For managing dev, staging, and prod as persistent environments, use **separate configuration directories** or **separate Terraform Cloud workspaces** with per-workspace variable sets.

---

## Section 6: Workspace Pattern — Root Module Per Environment — 15:00–18:30

The recommended pattern for managing multiple environments looks like this:

**[SHOW CODE]**

```text
infrastructure/
├── modules/
│   └── vpc/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── environments/
│   ├── dev/
│   │   ├── main.tf        # calls ../modules/vpc with dev-specific inputs
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       └── terraform.tfvars
```

Each environment directory calls the shared modules with environment-specific variable values. They have separate state files (since they are separate working directories), separate backends, and separate credentials. This is the pattern used in production by large engineering organizations.

---

## Section 7: Terraform Cloud Workspaces — 18:30–20:30

It is important to distinguish between CLI workspaces and Terraform Cloud workspaces.

**CLI workspaces** are named state instances within a local or remote backend. They share configuration code and provider configuration.

**Terraform Cloud workspaces** are first-class organizational units. Each TFC workspace has its own:

- Variable set (including sensitive variables).
- Credentials and authentication.
- Access control policies.
- Run history and audit log.
- State file.
- Optional VCS repository connection.

When you use Terraform Cloud, creating a new TFC workspace is the recommended way to create a new environment — not CLI workspaces.

---

## Section 8: Closing — 20:30–21:30

Workspaces maintain independent state files within a single configuration directory. The active workspace is referenced as `terraform.workspace` in HCL. The four workspace commands are `list`, `show`, `new`, `select`, and `delete`.

Local workspace state is at `terraform.tfstate.d/<name>/terraform.tfstate`. Remote workspace state paths depend on the backend.

Use workspaces for lightweight, similar deployments. Use separate directories or Terraform Cloud workspaces for environments with different infrastructure, credentials, or compliance requirements.

In Module 08 we cover provisioners and null resources. Complete the reading guide, lab, quiz, and discussion first.

See you in Module 08.

---

End of Script — Module 07
