# CIS-4337 Infrastructure Automation

## Lab — Module 01: IaC Concepts and Benefits

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Install Terraform and verify the installation from the command line.
- Write a minimal valid Terraform configuration using a `null_resource`.
- Execute the full `terraform init → plan → apply → destroy` workflow.
- Observe how `terraform plan` reports configuration drift caused by a manual state edit.
- Explain the contents and purpose of the `terraform.tfstate` file.

---

## Prerequisites

- Terraform CLI version 1.6.0 or later installed and available on your PATH.
- A terminal (bash, zsh, or PowerShell).
- A text editor (VS Code is recommended).
- No cloud provider credentials are required for this lab. All resources use the `null_resource` type, which makes no external API calls.

Install Terraform by following the instructions at developer.hashicorp.com/terraform/downloads. Verify the installation:

```bash
terraform version
```

Expected output (version number may differ):

```text
Terraform v1.8.0
on linux_amd64
```

---

## Part 1: Observe the ClickOps vs. IaC Contrast

Before writing any Terraform code, take 5 minutes to complete the following observation exercise. This activity anchors the conceptual material from the reading guide to a practical experience.

### Step 1.1 — Log in to the AWS Free Tier console (console.aws.amazon.com)

If you do not have an AWS account, you may use the AWS Free Tier or the provided course sandbox. Navigate to the EC2 console and note how many manual steps are required simply to reach the instance launch wizard. Count the clicks.

### Step 1.2 — Record your observations

In a text file named `clickops_notes.txt`, answer the following questions in two to three sentences each:

1. How many distinct screens or decision points did you encounter before you could even see a launch button?
2. If you needed to reproduce this exact configuration in a second region, what would you have to do?
3. If a colleague needed to audit what settings were chosen, where would they look?

You will reference these answers in your discussion post.

---

## Part 2: Write and Execute a Minimal Terraform Configuration

### Step 2.1 — Create a working directory

```bash
mkdir ~/tf-lab-01
cd ~/tf-lab-01
```

### Step 2.2 — Create main.tf

Create a file named `main.tf` with the following content exactly as shown:

```hcl
terraform {
  required_version = ">= 1.6.0"
}

resource "null_resource" "iac_demo" {
  triggers = {
    demo_value = "module-01"
  }
}
```

This configuration requires no provider credentials. The `null_resource` type is built into Terraform's null provider and performs no real infrastructure action. It exists purely to demonstrate the Terraform lifecycle.

### Step 2.3 — Initialize the working directory

```bash
terraform init
```

Expected output (abbreviated):

```text
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/null...
- Installing hashicorp/null v3.x.x...

Terraform has been successfully initialized!
```

Note what `terraform init` created in your directory:

```bash
ls -la
```

You should see a `.terraform/` directory (containing the downloaded provider plugin) and a `.terraform.lock.hcl` file (which locks provider versions for reproducibility).

### Step 2.4 — Validate the configuration

```bash
terraform validate
```

Expected output:

```text
Success! The configuration is valid.
```

### Step 2.5 — Generate an execution plan

```bash
terraform plan
```

Examine the output carefully. You should see:

```text
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # null_resource.iac_demo will be created
  + resource "null_resource" "iac_demo" {
      + id       = (known after apply)
      + triggers = {
          + "demo_value" = "module-01"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.
```

Record your answers to these questions in `lab_notes.txt`:

1. What symbol precedes `null_resource.iac_demo` in the plan output, and what does it mean?
2. Why does `id` show `(known after apply)` rather than a real value?
3. Has any infrastructure been changed at this point? How do you know?

### Step 2.6 — Apply the configuration

```bash
terraform apply
```

Terraform will display the plan again and prompt for confirmation:

```text
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

Type `yes` and press Enter.

Expected output:

```text
null_resource.iac_demo: Creating...
null_resource.iac_demo: Creation complete after 0s [id=1234567890123456789]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

### Step 2.7 — Inspect the state file

```bash
cat terraform.tfstate
```

Examine the JSON contents. Locate the following fields and record them in `lab_notes.txt`:

- `terraform_version`
- `resources[0].type`
- `resources[0].name`
- `resources[0].instances[0].attributes.id`
- `resources[0].instances[0].attributes.triggers`

### Step 2.8 — Run plan again on unchanged infrastructure

```bash
terraform plan
```

Expected output:

```text
No changes. Your infrastructure matches the configuration.
```

This demonstrates idempotency: the same configuration applied to already-correct infrastructure produces no changes.

---

## Part 3: Simulate and Detect Configuration Drift

In this part you will manually modify the state file to simulate what happens when infrastructure diverges from its declared configuration. You will then observe how `terraform plan` detects the drift.

### Step 3.1 — Open the state file in your editor

Open `terraform.tfstate` in VS Code or your preferred editor. Find the `triggers` object under `attributes` and change the value from `"module-01"` to `"manual-change"`.

Before edit:

```json
"triggers": {
  "demo_value": "module-01"
}
```

After edit:

```json
"triggers": {
  "demo_value": "manual-change"
}
```

Save the file.

### Step 3.2 — Run terraform plan to detect drift

```bash
terraform plan
```

Examine the output. You should see a proposed change to update or replace the resource because the live state (as recorded in `terraform.tfstate`) no longer matches the configuration in `main.tf`.

Record in `lab_notes.txt`:

1. What change does Terraform propose?
2. What symbol appears next to the resource, and what does it indicate?
3. In a real-world scenario, what would have caused this drift instead of your manual file edit?

### Step 3.3 — Restore correct state by applying

```bash
terraform apply -auto-approve
```

The `-auto-approve` flag skips the interactive confirmation prompt. Note: in production environments this flag should be used cautiously, typically only in CI/CD pipelines after a plan has been reviewed.

Run `terraform plan` one more time to confirm no changes remain.

---

## Part 4: Destroy All Resources

```bash
terraform destroy
```

Type `yes` when prompted. After completion, run:

```bash
cat terraform.tfstate
```

Observe that the `resources` array is now empty. The state file still exists but records that no resources are managed.

---

## Deliverables

Submit the following to the Canvas assignment portal.

1. A screenshot of your `terraform apply` output showing `1 added, 0 changed, 0 destroyed`.
2. A screenshot of your drift-detection `terraform plan` output showing the proposed change.
3. Your completed `lab_notes.txt` file with answers to all recorded questions.
4. Your final `main.tf` file.

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| `terraform init` executed successfully; screenshot shows provider download | 10 |
| `terraform plan` output captured before first apply; symbols identified correctly | 15 |
| `terraform apply` output captured; state file contents described accurately | 20 |
| Idempotency demonstrated with second plan showing "No changes" | 10 |
| Drift simulation completed; plan output captured showing proposed change | 25 |
| Drift explanation in lab notes is technically accurate | 10 |
| `terraform destroy` completed; empty resources array in state file shown | 10 |

---

## Troubleshooting

**Error: terraform: command not found**
Terraform is not on your PATH. Follow the installation guide at developer.hashicorp.com/terraform/downloads and ensure the binary directory is in your PATH environment variable.

**Error: Required plugins are not installed**
Run `terraform init` again. This error means the `.terraform/` directory is missing or incomplete.

**The state file drift simulation shows no change**
Ensure you saved the file after editing. Also confirm you edited the value inside `attributes.triggers`, not the `triggers` key inside the HCL-source-tracking section of the state file.

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Resource Configuration with Output References

Extend your `main.tf` to declare two `null_resource` blocks where the second resource depends on the first using an explicit `depends_on` meta-argument. Then add an `output` block that exposes the `id` of the second resource.

```hcl
resource "null_resource" "first" {
  triggers = {
    step = "one"
  }
}

resource "null_resource" "second" {
  depends_on = [null_resource.first]
  triggers = {
    step      = "two"
    first_id  = null_resource.first.id
  }
}

output "second_resource_id" {
  description = "ID of the second null resource"
  value       = null_resource.second.id
}
```

1. Run `terraform plan` and observe the dependency ordering in the output. Note which resource Terraform plans to create first.
2. Run `terraform apply -auto-approve` and confirm the output value is printed after apply completes.
3. Record in `lab_notes.txt`: what would happen if you removed `depends_on` — would the order change, and why or why not given that `first_id` already creates an implicit dependency?

### Challenge 2: Variable-Driven Configuration

Refactor your `main.tf` to accept an input variable `demo_label` of type `string` with a default of `"challenge"`. Use this variable as the `demo_value` trigger on the `null_resource`.

```hcl
variable "demo_label" {
  description = "Label used as the trigger value for the demo resource"
  type        = string
  default     = "challenge"
}

resource "null_resource" "variable_demo" {
  triggers = {
    demo_value = var.demo_label
  }
}
```

1. Run `terraform apply -auto-approve` with no extra flags to use the default value.
2. Run `terraform apply -auto-approve -var="demo_label=custom-value"` and observe whether Terraform detects a change and replaces the resource.
3. Run `terraform apply -auto-approve` a second time with no flags and confirm idempotency (no changes).

### Reflection Questions

1. When you changed `demo_label` via `-var` and Terraform replaced the resource, what does this tell you about how Terraform handles trigger value changes on `null_resource`? How does this behavior relate to the concept of immutable infrastructure?
2. In a real-world scenario where your organization currently uses manual AWS console workflows, identify two specific risks that IaC adoption would mitigate, and explain how the declarative model addresses each risk.

---

Module 01 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
