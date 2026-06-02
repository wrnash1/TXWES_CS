# CIS-4337 Infrastructure Automation

## Lab — Module 07: Terraform Workspaces and Environments

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Create and switch between Terraform workspaces.
- Use `terraform.workspace` to create environment-aware resource names and tags.
- Verify that each workspace maintains independent state.
- Inspect workspace state storage paths on the local filesystem.
- Apply the recommended multi-environment directory pattern.

---

## Prerequisites

- Terraform CLI 1.6.0 or later.
- No cloud provider credentials required for Parts 1–3 (uses null provider).
- AWS credentials required for Part 4 (optional extension).

---

## Part 1: Create and Explore Workspaces

### Step 1.1 — Create the working directory and configuration

```bash
mkdir ~/tf-lab-07
cd ~/tf-lab-07
```

Create `main.tf`:

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

resource "null_resource" "env_marker" {
  triggers = {
    workspace   = terraform.workspace
    deployed_at = "2024-01-01"
  }
}
```

```bash
terraform init
```

### Step 1.2 — Inspect the default workspace

```bash
terraform workspace list
terraform workspace show
```

Record in `lab_notes.txt`:

1. What is the name of the active workspace?
2. What symbol indicates the active workspace in `workspace list` output?

### Step 1.3 — Apply in the default workspace

```bash
terraform apply -auto-approve
```

Confirm the state file location:

```bash
ls -la terraform.tfstate
cat terraform.tfstate | grep workspace
```

Record: Does the default workspace state file contain a workspace name in its contents? (Hint: the state file does not store a workspace name — it is implicit from the file location.)

---

## Part 2: Create Named Workspaces and Verify State Isolation

### Step 2.1 — Create a dev workspace

```bash
terraform workspace new dev
terraform workspace show
```

Confirm you are now in the `dev` workspace.

### Step 2.2 — Apply in dev workspace

```bash
terraform apply -auto-approve
```

### Step 2.3 — Inspect the workspace state storage structure

```bash
ls -la terraform.tfstate.d/
ls -la terraform.tfstate.d/dev/
cat terraform.tfstate.d/dev/terraform.tfstate
```

Record in `lab_notes.txt`:

1. What is the full path to the dev workspace state file?
2. What is the `triggers.workspace` value in the dev state file?

### Step 2.4 — Create a staging workspace

```bash
terraform workspace new staging
terraform apply -auto-approve
```

### Step 2.5 — List all workspaces

```bash
terraform workspace list
```

Record: How many workspaces exist? Which is active?

### Step 2.6 — Verify state isolation

Switch back to default and verify its state still shows the default workspace value:

```bash
terraform workspace select default
cat terraform.tfstate | python3 -m json.tool | grep -A2 triggers
```

Then check the staging state:

```bash
cat terraform.tfstate.d/staging/terraform.tfstate | python3 -m json.tool | grep -A2 triggers
```

Record: Do the two state files contain different values for `triggers.workspace`? What does this demonstrate about state isolation?

---

## Part 3: Workspace-Aware Configuration

### Step 3.1 — Update main.tf to use terraform.workspace

Replace the content of `main.tf` with:

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

locals {
  environment = terraform.workspace

  instance_config = {
    default = { replicas = 1, tier = "small"  }
    dev     = { replicas = 1, tier = "small"  }
    staging = { replicas = 2, tier = "medium" }
    prod    = { replicas = 4, tier = "large"  }
  }

  config = lookup(local.instance_config, local.environment, local.instance_config["default"])
}

resource "null_resource" "app_server" {
  count = local.config.replicas

  triggers = {
    name      = "app-${local.environment}-${count.index}"
    tier      = local.config.tier
    workspace = terraform.workspace
  }
}

output "environment_name" {
  value = local.environment
}

output "replica_count" {
  value = local.config.replicas
}

output "server_names" {
  value = [for r in null_resource.app_server : r.triggers.name]
}
```

### Step 3.2 — Apply in each workspace and compare outputs

```bash
terraform workspace select dev
terraform apply -auto-approve
terraform output
```

Record the output values for dev. Then repeat for staging and a new `prod` workspace:

```bash
terraform workspace new prod
terraform apply -auto-approve
terraform output
```

Record in `lab_notes.txt`:

1. How many `null_resource.app_server` instances were created in dev? In prod?
2. What are the server names in each workspace?
3. Could you achieve this behavior without `terraform.workspace`? If yes, how?

---

## Part 4: Clean Up All Workspaces

Destroy resources and delete workspaces one at a time:

```bash
terraform workspace select prod
terraform destroy -auto-approve
terraform workspace select default
terraform workspace delete prod

terraform workspace select staging
terraform destroy -auto-approve
terraform workspace select default
terraform workspace delete staging

terraform workspace select dev
terraform destroy -auto-approve
terraform workspace select default
terraform workspace delete dev

terraform destroy -auto-approve
```

Confirm all workspace directories are removed:

```bash
ls -la terraform.tfstate.d/
```

---

## Deliverables

Submit to Canvas:

1. Screenshot of `terraform workspace list` showing all four workspaces (default, dev, staging, prod).
2. Screenshot of the `terraform.tfstate.d/` directory structure.
3. Screenshot of `terraform output` from the dev workspace.
4. Screenshot of `terraform output` from the prod workspace showing 4 replicas.
5. Completed `lab_notes.txt` with all recorded answers.

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| Workspaces created and listed correctly; active workspace identified | 15 |
| State isolation verified: different workspace names in separate state files | 20 |
| Local state storage paths identified correctly | 15 |
| Workspace-aware configuration: `terraform.workspace` used in locals and resources | 20 |
| Different replica counts confirmed across dev and prod workspaces | 20 |
| All workspaces cleaned up; `terraform.tfstate.d/` empty | 10 |

---

## Troubleshooting

**Error: workspace already exists**
If `terraform workspace new dev` fails, the workspace may already exist. Use `terraform workspace select dev` to switch to it.

**The prod workspace shows 1 replica instead of 4**
Ensure the `local.instance_config` map in your `main.tf` contains a `prod` key. The `lookup` function uses the `"default"` key as a fallback if the current workspace name is not in the map.

**Error: terraform.tfstate.d: No such file or directory**
You must create at least one named workspace before the `terraform.tfstate.d/` directory is created. The default workspace uses only the root `terraform.tfstate` file.

---

Module 07 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
