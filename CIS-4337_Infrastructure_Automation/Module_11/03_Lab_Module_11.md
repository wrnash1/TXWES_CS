# Lab: Module 11 — Terraform Cloud and Remote Backends

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will connect a Terraform configuration to a Terraform Cloud organization, configure a workspace, store variables securely, and execute plans and applies remotely. You will also explore VCS integration concepts and simulate Sentinel policy evaluation through workspace settings.

**Estimated time**: 90–120 minutes

**Prerequisites**:

- Terraform >= 1.1 installed
- A free Terraform Cloud account at `app.terraform.io`
- A GitHub account (for Part 5 VCS integration)
- A text editor

**Note**: This lab uses only Terraform Cloud's free tier features. No cloud provider credentials or paid tier features are required for Parts 1–4. Part 5 requires a GitHub account.

---

## Part 1: Terraform Cloud Setup (15 minutes)

### Step 1.1 — Create a Terraform Cloud Account

1. Navigate to `app.terraform.io`
2. Sign up for a free account using your `.edu` email address
3. Create an **organization** named `txwes-<yourname>` (e.g., `txwes-jsmith`)

### Step 1.2 — Create a Workspace

1. In the Terraform Cloud UI, click **New Workspace**
2. Choose **CLI-driven workflow** (not VCS — we will add VCS later)
3. Name the workspace `lab11-local`
4. Click **Create workspace**

### Step 1.3 — Generate an API Token

1. Click your user avatar → **User Settings** → **Tokens**
2. Click **Create an API token**
3. Name it `lab11-token`
4. Copy the token value — **you cannot retrieve it again after closing the dialog**

### Step 1.4 — Authenticate the CLI

```bash
terraform login
```

Follow the prompts. Terraform opens a browser window. Paste your token when prompted.

Alternatively, set the environment variable:

```bash
export TF_TOKEN_app_terraform_io="your-token-here"
```

---

## Part 2: Connect a Configuration to Terraform Cloud (20 minutes)

### Step 2.1 — Create Lab Directory

```bash
mkdir -p ~/tf-lab-11 && cd ~/tf-lab-11
mkdir -p output
```

### Step 2.2 — Create main.tf with cloud Block

```hcl
# main.tf

terraform {
  required_version = ">= 1.1"

  cloud {
    organization = "txwes-<yourname>"

    workspaces {
      name = "lab11-local"
    }
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

provider "local" {}
provider "random" {}

variable "app_name" {
  type        = string
  description = "Application name"
  default     = "lab11-app"
}

variable "environment" {
  type        = string
  description = "Deployment environment"
  default     = "dev"
}

resource "random_id" "app_id" {
  byte_length = 4
}

resource "local_file" "app_config" {
  filename = "${path.module}/output/config.json"
  content  = jsonencode({
    app_name    = var.app_name
    environment = var.environment
    app_id      = random_id.app_id.hex
  })
}

output "app_id" {
  value = random_id.app_id.hex
}

output "app_name" {
  value = var.app_name
}
```

### Step 2.3 — Initialize

```bash
terraform init
```

Observe the output — Terraform reports connecting to Terraform Cloud and configuring the `lab11-local` workspace.

### Step 2.4 — Run a Plan

```bash
terraform plan
```

Observe that the plan runs remotely. The terminal output streams from Terraform Cloud:

```
Running plan in Terraform Cloud. Output will stream here.
Waiting for the plan to start...

Terraform v1.x.y
on linux_amd64
...
```

Open the Terraform Cloud UI and navigate to the `lab11-local` workspace. You should see the run in the **Runs** tab.

---

## Part 3: Manage Variables in Terraform Cloud (20 minutes)

### Step 3.1 — Set a Variable in the Workspace UI

1. In Terraform Cloud, open the `lab11-local` workspace
2. Click **Variables** → **+ Add variable**
3. Category: **Terraform variable**
4. Key: `app_name`
5. Value: `my-cloud-app`
6. Check **HCL** if the value is HCL syntax (not needed for a simple string)
7. Leave **Sensitive** unchecked for this variable
8. Click **Save variable**

### Step 3.2 — Add a Sensitive Variable

Repeat Step 3.1 with:

- Key: `secret_token`
- Value: `super-secret-value-123`
- Check **Sensitive** — the value will be hidden after saving

Add a corresponding variable to `variables.tf`:

```hcl
variable "secret_token" {
  type      = string
  sensitive = true
}
```

Add an output that demonstrates the variable was received (showing only a hash, not the value):

```hcl
output "token_hash" {
  value = substr(sha256(var.secret_token), 0, 8)
}
```

### Step 3.3 — Apply with Workspace Variables

```bash
terraform apply
```

When prompted to confirm in the UI (if auto-apply is off), navigate to the run in Terraform Cloud and click **Confirm & Apply**.

Verify in the output that `app_name` uses `my-cloud-app` (the workspace variable) rather than the default `lab11-app`.

---

## Part 4: Explore Run History and State Versions (15 minutes)

### Step 4.1 — Review Run History

In the Terraform Cloud UI, navigate to **Runs**. You should see all plans and applies with:

- Run ID
- Trigger (CLI run)
- Status (planned, applied)
- Timestamp
- Initiated by (your username)

Click on a run to see the full plan and apply output.

### Step 4.2 — Review State Versions

Navigate to **States** in the workspace. You should see:

- State version number
- Timestamp
- Run that created this version
- Serial number

Click on a state version to inspect the raw state file. Notice that sensitive variable values appear only as attribute references in the state (e.g., `(sensitive value)`) — though the underlying value is stored encrypted.

### Step 4.3 — Create a Second Workspace

1. In the Terraform Cloud UI, create a second workspace named `lab11-prod`
2. Update the `cloud` block in `main.tf` to target `lab11-prod`

```hcl
workspaces {
  name = "lab11-prod"
}
```

3. Run `terraform init` and `terraform apply`

Observe that `lab11-prod` has completely separate state from `lab11-local`. The `app_id` will be a different value because the state is independent.

4. Switch back to `lab11-local`:

```hcl
workspaces {
  name = "lab11-local"
}
```

Run `terraform init -reconfigure` to switch back.

---

## Part 5: VCS Integration (20 minutes)

### Step 5.1 — Create a GitHub Repository

1. Create a new public GitHub repository named `tf-lab-11`
2. Push your current `~/tf-lab-11` directory to the repository

```bash
cd ~/tf-lab-11
git init
git add main.tf variables.tf outputs.tf
echo "output/" >> .gitignore
echo ".terraform/" >> .gitignore
echo ".terraform.lock.hcl" >> .gitignore
git add .gitignore
git commit -m "Initial Terraform Cloud lab configuration"
git remote add origin https://github.com/<your-username>/tf-lab-11.git
git push -u origin main
```

### Step 5.2 — Connect Workspace to GitHub

1. In Terraform Cloud, create a new workspace named `lab11-vcs`
2. Choose **Version control workflow**
3. Connect to GitHub and authorize Terraform Cloud
4. Select your `tf-lab-11` repository
5. Set the Terraform working directory to `/` (root of the repository)
6. Leave other settings at defaults

### Step 5.3 — Trigger a Plan via Git Push

Make a minor change to `main.tf` — for example, add a description to the `app_name` variable:

```hcl
variable "app_name" {
  type        = string
  description = "Application name — updated via VCS integration"
  default     = "lab11-vcs-app"
}
```

Commit and push:

```bash
git add main.tf
git commit -m "Update app_name description"
git push
```

Navigate to the `lab11-vcs` workspace in Terraform Cloud. Observe that a plan was triggered automatically by the push. Review the plan output in the UI.

### Step 5.4 — Observe the Run Trigger

In the workspace **Runs** view, observe:

- The trigger shows "VCS" rather than "CLI"
- The commit SHA is linked to the GitHub commit
- The plan output matches what you would see locally

---

## Reflection Questions

Answer these in a text file named `reflection.txt` and submit with your deliverables:

1. What are three advantages of storing variables in Terraform Cloud rather than in local `.tfvars` files?

2. When would you choose **manual confirmation** over **auto-apply** for a workspace?

3. Explain in one paragraph why speculative plans on pull requests improve the infrastructure change review process.

---

## Deliverables

1. Screenshot of the Terraform Cloud workspace **Runs** tab showing at least two completed runs
2. Screenshot of the **Variables** tab showing `app_name` and `secret_token` (value of sensitive variable should be hidden)
3. Screenshot of the **States** tab showing multiple state versions
4. Screenshot of a VCS-triggered run in `lab11-vcs` workspace
5. `reflection.txt` with answers to the three questions

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Terraform Cloud organization and workspace created | 10 |
| `cloud` block configured correctly; `terraform init` succeeds | 15 |
| Remote plan and apply completed successfully | 20 |
| Workspace variables set (including sensitive) | 15 |
| Run history and state versions explored | 10 |
| VCS integration configured and plan triggered by git push | 20 |
| Reflection questions answered thoughtfully | 10 |
| **Total** | **100** |

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
