# Lab: Module 08 — Terraform State Management

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will work with Terraform state using the local backend and the `local` provider (no cloud credentials required). You will practice using all major `terraform state` subcommands, simulating the kinds of state manipulation tasks that arise during real infrastructure refactoring. You will also configure and observe state file structure, practice state move operations, and explore state security considerations.

**Estimated time**: 75–90 minutes

**Prerequisites**:

- Terraform >= 1.5 installed
- A text editor
- A Unix/Linux terminal or Git Bash on Windows

---

## Part 1: Initial Infrastructure Setup (15 minutes)

### Step 1.1 — Create Lab Directory

```bash
mkdir -p ~/tf-lab-08 && cd ~/tf-lab-08
mkdir -p output
```

### Step 1.2 — Create main.tf

```hcl
# main.tf

terraform {
  required_version = ">= 1.5"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "local" {}
provider "random" {}

resource "random_id" "app_id" {
  byte_length = 4
}

resource "random_id" "db_id" {
  byte_length = 4
}

resource "local_file" "app_config" {
  filename = "${path.module}/output/app-config.json"
  content  = jsonencode({
    app_id      = random_id.app_id.hex
    environment = "dev"
    port        = 8080
  })
}

resource "local_file" "db_config" {
  filename = "${path.module}/output/db-config.json"
  content  = jsonencode({
    db_id    = random_id.db_id.hex
    host     = "localhost"
    port     = 5432
    database = "appdb"
  })
}

resource "local_file" "readme" {
  filename = "${path.module}/output/README.txt"
  content  = "Infrastructure managed by Terraform. Do not edit manually."
}
```

### Step 1.3 — Initialize and Apply

```bash
terraform init
terraform apply -auto-approve
```

Verify the files were created:

```bash
ls output/
cat output/app-config.json
```

---

## Part 2: Inspect State (15 minutes)

### Step 2.1 — Examine the State File

```bash
# View the raw state file
cat terraform.tfstate
```

Note the `version`, `serial`, `lineage`, and `resources` fields. Identify where each resource's attributes are stored.

### Step 2.2 — Use terraform state list

```bash
terraform state list
```

Expected output:

```
local_file.app_config
local_file.db_config
local_file.readme
random_id.app_id
random_id.db_id
```

### Step 2.3 — Use terraform state show

```bash
terraform state show local_file.app_config
terraform state show random_id.app_id
```

Record the `id` attribute of `local_file.app_config`. Note that `random_id.app_id` has both `hex` and `b64_std` attributes populated by the provider.

---

## Part 3: Rename a Resource in State (15 minutes)

In this part you will rename `local_file.app_config` to `local_file.web_app_config` — a common refactoring task.

### Step 3.1 — Update main.tf

Change the resource label in `main.tf`:

```hcl
# Change this:
resource "local_file" "app_config" {
  ...
}

# To this:
resource "local_file" "web_app_config" {
  filename = "${path.module}/output/app-config.json"
  content  = jsonencode({
    app_id      = random_id.app_id.hex
    environment = "dev"
    port        = 8080
  })
}
```

### Step 3.2 — Run terraform plan Before State Move

```bash
terraform plan
```

Observe that Terraform proposes to **destroy** `local_file.app_config` and **create** `local_file.web_app_config`. This is because Terraform thinks these are two different resources.

### Step 3.3 — Move the Resource in State

```bash
terraform state mv local_file.app_config local_file.web_app_config
```

Expected output:

```
Move "local_file.app_config" to "local_file.web_app_config"
Successfully moved 1 object(s).
```

### Step 3.4 — Verify with terraform plan

```bash
terraform plan
```

The plan should now show **no changes** — Terraform recognizes the resource under its new name.

### Step 3.5 — Verify state list

```bash
terraform state list
```

Confirm `local_file.web_app_config` appears and `local_file.app_config` is gone.

---

## Part 4: Remove a Resource from State (10 minutes)

In this part you will remove `local_file.readme` from state tracking without deleting the file.

### Step 4.1 — Remove from State

```bash
terraform state rm local_file.readme
```

Expected output:

```
Removed local_file.readme
Successfully removed 1 resource instance(s).
```

### Step 4.2 — Verify the File Still Exists

```bash
cat output/README.txt
```

The file is still on disk — `state rm` only removes Terraform's tracking record.

### Step 4.3 — Run terraform plan

```bash
terraform plan
```

Observe that Terraform proposes to **create** `local_file.readme` again, because it no longer knows the file exists.

### Step 4.4 — Remove the Resource from main.tf

To prevent Terraform from recreating it, also remove the `local_file.readme` block from `main.tf`. Then confirm the plan shows no changes.

---

## Part 5: State Backup and Pull (10 minutes)

### Step 5.1 — Pull State to a Backup File

```bash
terraform state pull > state_backup.json
```

### Step 5.2 — Inspect the Backup

```bash
cat state_backup.json | python3 -m json.tool | head -40
```

Confirm the backup contains all current resources. Note the `serial` number.

### Step 5.3 — Simulate the Backup

Compare `state_backup.json` with `terraform.tfstate`:

```bash
diff terraform.tfstate state_backup.json
```

They should be identical (or differ only in whitespace formatting).

---

## Part 6: Configure a Local Backend Explicitly (10 minutes)

### Step 6.1 — Add an Explicit Backend Block

Add the following to the `terraform` block in `main.tf`:

```hcl
terraform {
  required_version = ">= 1.5"

  backend "local" {
    path = "terraform.tfstate"
  }

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}
```

### Step 6.2 — Re-initialize

```bash
terraform init
```

Terraform detects the backend configuration and confirms the state path. This demonstrates that the local backend can be made explicit and that `terraform init` handles backend initialization.

---

## Part 7: Security Exercise (5 minutes)

### Step 7.1 — Inspect State for Sensitive Data

Look at the current state file:

```bash
cat terraform.tfstate
```

Observe that all resource attribute values are stored in plain text, including generated IDs. In a real environment, this would include passwords, connection strings, and private keys.

### Step 7.2 — Create a .gitignore

```bash
cat > .gitignore <<'EOF'
# Terraform state files
terraform.tfstate
terraform.tfstate.backup
*.tfstate
*.tfstate.*
state_backup.json

# Terraform directory
.terraform/
.terraform.lock.hcl

# Crash logs
crash.log
crash.*.log

# Variable files containing secrets
*.tfvars
!example.tfvars
EOF
```

Verify the .gitignore:

```bash
cat .gitignore
```

---

## Cleanup

```bash
terraform destroy -auto-approve
rm -rf output/ .terraform/ terraform.tfstate terraform.tfstate.backup state_backup.json
```

---

## Deliverables

Submit the following to the course LMS:

1. A screenshot of `terraform state list` after initial apply (Part 2)
2. A screenshot of the plan BEFORE `state mv` showing destroy + create
3. A screenshot of the plan AFTER `state mv` showing no changes
4. A screenshot of `terraform state show random_id.app_id` output
5. Your completed `.gitignore` file content

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial apply succeeds with all 5 resources | 15 |
| `state list` and `state show` outputs captured | 15 |
| `state mv` completed; plan shows no changes after | 25 |
| `state rm` completed; file persists on disk | 20 |
| State pull backup created correctly | 10 |
| `.gitignore` correctly excludes state files | 15 |
| **Total** | **100** |

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
