# CIS-4337 Infrastructure Automation

## Lab — Module 02: Terraform Workflow

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Write a `null_resource` configuration and execute the full `init → validate → plan → apply → destroy` sequence.
- Interpret all symbols in a `terraform plan` output.
- Save a plan to a file with `-out` and apply it with `terraform apply <planfile>`.
- Explain the contents of `.terraform/`, `.terraform.lock.hcl`, and `terraform.tfstate`.
- Use `terraform fmt` and explain what it changes.

---

## Prerequisites

- Terraform CLI version 1.6.0 or later installed and on your PATH.
- A terminal (bash, zsh, or PowerShell on Windows).
- VS Code or another text editor.
- No cloud provider credentials are needed. This lab uses only the `null` provider.

Verify Terraform is installed:

```bash
terraform version
```

Expected output:

```text
Terraform v1.8.0
on linux_amd64
```

---

## Part 1: Initialize and Examine the Working Directory

### Step 1.1 — Create the working directory

```bash
mkdir ~/tf-lab-02
cd ~/tf-lab-02
```

### Step 1.2 — Create main.tf

Create `main.tf` with the following content:

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

resource "null_resource" "server_a" {
  triggers = {
    server_name = "web-01"
    environment = "dev"
  }
}

resource "null_resource" "server_b" {
  triggers = {
    server_name = "web-02"
    environment = "dev"
  }
}
```

### Step 1.3 — Run terraform init

```bash
terraform init
```

Record the following in `lab_notes.txt`:

1. What directory did Terraform create in your working directory?
2. What file did Terraform create to record provider version selections?
3. Which provider was downloaded, and what version was installed?

### Step 1.4 — List the directory contents

```bash
ls -la
```

Identify and describe each item Terraform created. Note the `.terraform/` directory and `.terraform.lock.hcl` file.

### Step 1.5 — Inspect the lock file

Open `.terraform.lock.hcl` in your editor. Record:

1. What is the `source` value for the null provider?
2. What constraints are listed?
3. What are `hashes` used for?

---

## Part 2: Validate and Generate the Plan

### Step 2.1 — Run terraform validate

```bash
terraform validate
```

Expected output:

```text
Success! The configuration is valid.
```

Now introduce a deliberate syntax error. In `main.tf`, remove the closing `}` from the `server_a` resource block. Run `terraform validate` again and record the error message in `lab_notes.txt`. Then restore the closing brace.

### Step 2.2 — Run terraform plan and interpret output

```bash
terraform plan
```

Read the output carefully. Answer the following questions in `lab_notes.txt`:

1. How many resources does Terraform plan to create?
2. What symbol appears next to each resource? What does it mean?
3. What is the value shown for `id` in both resources? Why is it not known yet?
4. What is the summary line at the bottom of the plan output?

### Step 2.3 — Save the plan to a file

```bash
terraform plan -out=tfplan
```

This creates a binary file named `tfplan`.

```bash
ls -lh tfplan
```

Record the file size. Now inspect the saved plan in human-readable form:

```bash
terraform show tfplan
```

Record in `lab_notes.txt`: Is the output of `terraform show tfplan` identical to the output of `terraform plan`? Why does the saved plan exist as a binary rather than as a plain text file?

---

## Part 3: Apply the Saved Plan and Inspect State

### Step 3.1 — Apply the saved plan

```bash
terraform apply tfplan
```

Note: because you are applying a saved plan, Terraform does not ask for confirmation. Record the apply output in `lab_notes.txt`.

### Step 3.2 — Inspect the state file

```bash
cat terraform.tfstate
```

Locate and record:

1. The `terraform_version` value.
2. The `type` and `name` for both resources.
3. The `id` value for each resource. Compare to the plan output — what changed?
4. The `triggers` attribute values for each resource.

### Step 3.3 — Run plan again on unchanged infrastructure

```bash
terraform plan
```

Expected output:

```text
No changes. Your infrastructure matches the configuration.
```

Record: This demonstrates which property of Terraform's declarative model?

---

## Part 4: Modify a Resource and Observe Plan Symbols

### Step 4.1 — Update a trigger value

In `main.tf`, change `server_b`'s `environment` trigger from `"dev"` to `"staging"`:

```hcl
resource "null_resource" "server_b" {
  triggers = {
    server_name = "web-02"
    environment = "staging"
  }
}
```

### Step 4.2 — Run plan and identify the symbol

```bash
terraform plan
```

Record the symbol that appears next to `null_resource.server_b`. For the `null_resource` type, any trigger change forces replacement. You should see `-/+`. Explain in `lab_notes.txt` what `-/+` means and why this differs from a `~` (in-place update).

### Step 4.3 — Apply the change

```bash
terraform apply -auto-approve
```

Record: Did `null_resource.server_a` change? Why or why not?

---

## Part 5: Format and Destroy

### Step 5.1 — Introduce a formatting issue

In `main.tf`, change the indentation of one attribute so it is misaligned — for example, add extra spaces before `server_name`. Then run:

```bash
terraform fmt
```

Open `main.tf` and confirm the indentation was corrected automatically. Record: Does `terraform fmt` change the behavior of the configuration?

### Step 5.2 — Destroy all resources

```bash
terraform destroy
```

Review the destroy plan. Type `yes` to confirm. Record the destroy output.

### Step 5.3 — Inspect the state file after destroy

```bash
cat terraform.tfstate
```

Record: What does the `resources` array contain now?

---

## Deliverables

Submit the following to the Canvas assignment portal:

1. Screenshot of `terraform init` output showing provider download.
2. Screenshot of `terraform plan` output showing both `+` resources before first apply.
3. Screenshot of the `-/+` plan output from Part 4.
4. Screenshot of `terraform destroy` confirmation and completion.
5. Your completed `lab_notes.txt` with all recorded answers.
6. Final `main.tf` file (after `terraform fmt` has been applied).

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| `terraform init` output captured; lock file contents described | 10 |
| `terraform validate` error demonstrated and explained | 10 |
| Plan output interpreted: symbols, id values, summary line | 20 |
| Saved plan applied with `terraform apply tfplan`; state file inspected | 15 |
| Idempotency demonstrated with second plan showing "No changes" | 10 |
| `-/+` plan symbol identified and explained correctly | 20 |
| `terraform fmt` applied and effect described | 5 |
| `terraform destroy` completed; empty resources array shown | 10 |

---

## Troubleshooting

**Error: no configuration files**
You must be in the directory containing your `.tf` files when running Terraform commands. Use `cd ~/tf-lab-02` to navigate to the correct directory.

**The saved plan file `tfplan` is not recognized**
Ensure you pass the filename without quotes: `terraform apply tfplan`, not `terraform apply "tfplan"`.

**terraform fmt made no changes**
Your formatting was already correct. This is expected behavior. `terraform fmt` is idempotent.

---

Module 02 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
