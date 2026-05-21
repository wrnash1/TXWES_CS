# Reading Guide: Module 11 - Workspaces & Multi-Environment Management

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction

Welcome to **Module 11 - Workspaces & Multi-Environment Management**! This week's study material focuses on Terraform's built-in workspace feature, which allows a single configuration to manage multiple isolated state files — one per environment (e.g., dev, staging, prod). Understanding workspaces is essential for passing the Terraform Associate exam and for managing real-world infrastructure across multiple deployment targets from a single codebase.

As a student, you will learn how workspaces are created and selected, how they isolate state, how to reference the active workspace inside HCL configurations, and the limitations of workspaces compared to directory-based environment separation. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Terraform workspaces**: Named state-isolation containers within a single Terraform configuration. Each workspace maintains its own `terraform.tfstate` file, allowing the same HCL code to provision separate instances of infrastructure (e.g., dev vs. prod) without state conflicts.
* **default workspace**: The workspace Terraform uses automatically when no other workspace has been created or selected. It cannot be deleted; its state is stored as `terraform.tfstate` at the backend root. All named workspaces store state under `terraform.tfstate.d/<name>/` when using the local backend.
* **workspace directories**: The file-system paths under which Terraform stores per-workspace state files when using a local backend. The `default` workspace uses the root working directory, while named workspaces use `terraform.tfstate.d/<workspace-name>/terraform.tfstate`.
* **workspace isolation**: The guarantee that resources provisioned in one workspace have no shared state with resources in another workspace under the same configuration, preventing accidental modification of production resources when running plans or applies against a development workspace.

---

### 2. Certification Exam Tips

* **`terraform.workspace` interpolation:** The exam tests whether you know to reference `terraform.workspace` (not `var.workspace` or `local.workspace`) inside HCL to dynamically name resources per environment. Practice writing expressions like `name = "app-${terraform.workspace}"` and know that this evaluates to the string `"default"` when in the default workspace.
* **Workspaces vs. separate root modules:** The exam presents scenarios asking which approach provides stronger environment isolation. Workspaces share the same backend configuration and provider credentials — for strict security boundaries (e.g., separate AWS accounts per environment), separate root module directories with independent state backends are recommended over workspaces.
* **Key workspace commands:** Know `terraform workspace list`, `terraform workspace new <name>`, `terraform workspace select <name>`, and `terraform workspace show`. The exam may ask what each command returns or what preconditions are required.
* **Study Resource:** The HashiCorp documentation page on workspaces covers state storage paths, the `terraform.workspace` reference, and when workspaces are and are not appropriate: [Terraform Workspaces — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/state/workspaces).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the **Workspaces** section of the official HashiCorp documentation, which covers workspace commands, state paths, and when to use workspaces versus directory-based separation: [Terraform Workspaces — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/state/workspaces).
* **Required Video:** Watch the video lecture on **Workspaces & Multi-Environment Management** in the official course playlist, which demonstrates live workspace creation, selection, and the `terraform.workspace` interpolation pattern: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **List workspaces (`terraform workspace list`)**: Run this command to display all existing workspaces for the current configuration. The active workspace is marked with an asterisk (`*`). Confirm the `default` workspace exists before creating additional ones.
* **Create a development workspace (`terraform workspace new dev`)**: Execute this command to create and automatically switch to a new workspace named `dev`. Terraform will create a new, empty state under `terraform.tfstate.d/dev/`. Verify the switch by running `terraform workspace show`.
* **Deploy resources dynamically named after the workspace**: Update a resource's `name` attribute to `"app-${terraform.workspace}"`, then run `terraform plan` to confirm the workspace name is interpolated into the resource name. This pattern allows the same code to deploy distinctly named resources per environment without modifying any `.tf` files.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
* [ ] Read the **Workspaces** section in [Terraform Workspaces — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/state/workspaces).
* [ ] Watch the video lecture on **Workspaces & Multi-Environment Management** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
