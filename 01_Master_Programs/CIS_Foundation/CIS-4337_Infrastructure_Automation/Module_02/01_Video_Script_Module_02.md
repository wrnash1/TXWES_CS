# CIS-4337 Infrastructure Automation

## Module 02: Terraform Workflow

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337 Infrastructure Automation. I am Professor Nash. In Module 01 we established why Infrastructure as Code exists and what problems it solves. In this module we go hands-on with the Terraform CLI and walk through every stage of the core workflow in detail.

By the end of this video you will be able to execute the full Terraform workflow from a blank directory to deployed resources and back to destroyed infrastructure. You will understand what each CLI command does, how to read an execution plan, what plan output symbols mean, and how to use saved plan files in a CI/CD pipeline context.

These skills are tested directly on the Terraform Associate 003 exam, and they are the foundation for every lab in this course from this point forward.

---

## Section 2: The Terraform Core Architecture — 1:30–5:30

Before we run any commands, let me describe the components that make Terraform work. Understanding the architecture helps you reason about what each CLI command is actually doing under the hood.

Terraform has three major components.

The first is **Terraform Core**, sometimes called the Terraform CLI. This is the binary you download and install. It is responsible for reading your HCL configuration files, loading the state file, computing execution plans, and orchestrating the application of changes. The Core does not know how to talk to AWS, Azure, or any other platform directly.

The second component is **providers**. Providers are plugins — separate binaries distributed by HashiCorp, cloud vendors, or the community — that know how to authenticate with and make API calls to a specific platform. When you run `terraform init`, Terraform Core downloads the providers your configuration requires. The provider for AWS is named `hashicorp/aws`. The provider for Azure is `hashicorp/azurerm`. There are over 3,000 providers in the public Terraform Registry.

The third component is **the state file**. We covered this in Module 01. It is the JSON record that maps your HCL resource declarations to real-world resource IDs and attributes. Terraform Core reads this file to determine what already exists and writes to it after every apply.

The workflow we are about to walk through coordinates all three of these components.

---

## Section 3: Setting Up a Working Directory — 5:30–7:30

Every Terraform project lives in a working directory — a folder on your filesystem that contains your `.tf` configuration files. Let me show you the minimal structure of a working directory.

**[SHOW CODE]**

```text
my-project/
├── main.tf
├── variables.tf
├── outputs.tf
└── terraform.tfvars
```

This is a common convention. `main.tf` contains provider and resource blocks. `variables.tf` contains variable declarations. `outputs.tf` contains output blocks. `terraform.tfvars` supplies variable values. Terraform processes all `.tf` files in a directory as a single configuration, so the split across multiple files is purely organizational.

Here is the minimal `main.tf` we will use to demonstrate the workflow:

**[SHOW CODE]**

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

resource "null_resource" "workflow_demo" {
  triggers = {
    step = "module-02"
  }
}
```

The `null` provider creates resources that have no real infrastructure backing. We use it here because it requires no cloud credentials, making the workflow demonstration clean and accessible.

---

## Section 4: terraform init — 7:30–11:00

`terraform init` is always the first command you run in a new or cloned Terraform working directory. It performs three jobs.

**Job 1: Initialize the backend.** If your configuration specifies a remote backend (we cover those in Module 04), `init` connects to and configures that backend. If no backend is specified, Terraform uses the local backend and stores state in the working directory.

**Job 2: Download and install provider plugins.** Terraform reads your `required_providers` block and downloads the specified provider binaries from the Terraform Registry into a `.terraform/providers/` subdirectory. This is why `terraform plan` and `apply` can work without an internet connection after `init` has run.

**Job 3: Download modules.** If your configuration references external modules, `init` downloads those as well.

Let me walk through the output you will see when you run `terraform init`:

**[SHOW CODE]**

```text
Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/null versions matching "~> 3.0"...
- Installing hashicorp/null v3.2.2...
- Installed hashicorp/null v3.2.2 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record
the provider selections made above. Include this file in your
version control repository so that Terraform can guarantee to
make the same selections by default when you run
"terraform init" in the future.

Terraform has been successfully initialized!
```

The `.terraform.lock.hcl` file records the exact provider version selected and its checksum. Commit this file to Git. This is how you ensure every team member and every CI/CD pipeline uses the same provider version.

The `.terraform/` directory itself should be added to `.gitignore` because it contains downloaded binaries that are large and platform-specific.

---

## Section 5: terraform validate — 11:00–12:30

After `init`, it is good practice to run `terraform validate` before generating a plan. This command checks your HCL files for syntax errors and internal consistency problems without making any network calls.

**[SHOW CODE]**

```bash
terraform validate
```

If everything is correct, you see:

```text
Success! The configuration is valid.
```

If there is an error, such as a missing required attribute, validate will tell you the file name, line number, and a description of the problem. Fix these before proceeding to plan.

---

## Section 6: terraform plan — 12:30–16:30

`terraform plan` is the most important diagnostic tool in the Terraform workflow. When you run it, Terraform does four things in sequence.

First, it reads all `.tf` files in the working directory.

Second, it refreshes state by querying the provider APIs to get the current attributes of all resources tracked in the state file. This is how drift is detected.

Third, it computes the diff between the desired state (your HCL) and the current state (what the APIs report).

Fourth, it outputs an execution plan describing every proposed action.

Let me walk through reading a plan output.

**[SHOW CODE]**

```text
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # null_resource.workflow_demo will be created
  + resource "null_resource" "workflow_demo" {
      + id       = (known after apply)
      + triggers = {
          + "step" = "module-02"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.
```

The symbols in the plan output tell you the action that will be taken:

- `+` means the resource will be created.
- `-` means the resource will be destroyed.
- `~` means the resource will be updated in place.
- `-/+` means the resource will be destroyed and recreated (forced replacement). This happens when an attribute that cannot be changed after creation needs a new value — for example, changing an EC2 instance's AMI ID.
- `<=` means a data source will be read.

The summary line at the bottom — `Plan: 1 to add, 0 to change, 0 to destroy` — gives you a quick count of each action type. Get in the habit of reading this line before approving any apply.

You can save a plan to a file for later execution:

**[SHOW CODE]**

```bash
terraform plan -out=tfplan
```

This produces a binary plan file named `tfplan`. When you apply this saved file, Terraform executes exactly the changes captured in it, with no re-planning. This is the recommended pattern for CI/CD pipelines.

---

## Section 7: terraform apply — 16:30–19:30

`terraform apply` executes the changes described in the plan. When called without arguments, it re-generates the plan and asks for confirmation.

**[SHOW CODE]**

```bash
terraform apply
```

You will see the plan output followed by a confirmation prompt:

```text
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

Type `yes` and press Enter. Terraform creates the resources in dependency order, printing progress as it goes:

```text
null_resource.workflow_demo: Creating...
null_resource.workflow_demo: Creation complete after 0s [id=5678901234567890]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

To apply a saved plan file:

**[SHOW CODE]**

```bash
terraform apply tfplan
```

This skips the confirmation prompt because the plan was already reviewed. Do not use `-auto-approve` in production unless you have an established review process for the saved plan file.

---

## Section 8: terraform destroy — 19:30–21:30

`terraform destroy` is the reverse of apply. It destroys all resources managed by the current configuration.

**[SHOW CODE]**

```bash
terraform destroy
```

Like apply, it shows a plan first — this time all resources marked with `-` — and asks for confirmation. This is a destructive and irreversible operation for stateful resources. Always review the destroy plan carefully.

For test environments and CI/CD pipelines, `terraform destroy -auto-approve` is acceptable. For production, require manual confirmation.

---

## Section 9: Closing — 21:30–22:30

Let me recap the complete Terraform workflow:

1. Write your HCL configuration files.
2. Run `terraform init` to download providers and initialize the backend.
3. Run `terraform validate` to catch syntax errors early.
4. Run `terraform plan` to preview changes. Use `-out=tfplan` to save the plan.
5. Run `terraform apply` to execute changes. Use `terraform apply tfplan` in pipelines.
6. Run `terraform destroy` when you need to remove all managed resources.

Know the plan output symbols: `+` create, `-` destroy, `~` update, `-/+` forced replacement, `<=` read data source. The exam tests all of them.

In Module 03 we go deep into HCL syntax — providers, resources, variables, and outputs. Complete the reading guide, lab, quiz, and discussion before then.

All official documentation is at developer.hashicorp.com.

See you in Module 03.

---

End of Script — Module 02
