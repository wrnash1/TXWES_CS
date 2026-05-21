# Reading Guide: Module 07 - Terraform Workspaces and Environments
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 07 - Terraform Workspaces**! This week's study material covers **Terraform workspaces**, a feature that enables multiple independent state files to be managed within a single configuration directory. Workspaces are tested on the **HashiCorp Certified: Terraform Associate** exam as one approach to managing multiple environments (dev, staging, prod) with the same Terraform code.

As a student, you will learn how to create and switch between workspaces, understand their limitations, and compare them to alternative multi-environment patterns like separate directories or separate Terraform Cloud workspaces. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Terraform workspaces**: Named state isolation units within a single Terraform configuration directory. Each workspace maintains a completely separate state file, so resources in different workspaces do not interfere with each other. The CLI commands are `terraform workspace new <name>`, `terraform workspace select <name>`, `terraform workspace list`, and `terraform workspace show`. Workspaces are supported by most remote backends.
*   **`default` workspace**: Every Terraform configuration starts with a single workspace named `default`. You cannot delete the `default` workspace. When no workspace has been explicitly created or selected, all operations use the `default` workspace. The exam tests the fact that `default` always exists and cannot be removed.
*   **`terraform.workspace` reference**: A built-in string value available in any configuration that returns the name of the currently active workspace. It is commonly used in resource names and tags to differentiate resources per environment: `name = "app-${terraform.workspace}"`. The exam tests the correct reference path — it is `terraform.workspace`, not `var.workspace`.
*   **Workspace state file storage**: When using a local backend, workspace state files are stored in `terraform.tfstate.d/<workspace_name>/terraform.tfstate`. When using remote backends (S3, Terraform Cloud), workspaces are stored as separate state files or state versions within the backend. The exam tests the local storage path.
*   **Workspace limitations**: CLI workspaces share the same configuration code and the same provider credentials. They are best for simple environment separation with similar infrastructure. For significantly different infrastructure between environments (e.g., different modules, different providers), separate Terraform projects or Terraform Cloud workspaces are the recommended pattern. The exam tests when workspaces are and are not appropriate.

---

### 2. Certification Exam Tips
*   **Exam Domain — Navigate Terraform Workflow (Domain 2):** Workspace commands are directly tested. Know all four workspace subcommands: `list`, `new`, `select`, `show`. Know that `terraform workspace show` prints the name of the current workspace.
*   **`terraform.workspace` vs. `var.workspace` trap:** The exam commonly presents `var.workspace` as a distractor. The correct built-in reference is `terraform.workspace` (no `var.` prefix). There is no automatically created variable called `workspace`.
*   **Workspace isolation scope:** Workspaces isolate only state — they do not isolate provider credentials, variable files, or configuration code. All workspaces in a directory share the same `.tf` files and the same `terraform.tfvars`. If different environments need different variable values, you must use `-var-file` flags or environment-specific `.tfvars` files alongside workspace selection.
*   **When NOT to use workspaces:** The exam may present a scenario with significantly different infrastructure per environment and ask which approach is recommended. The answer is separate Terraform configurations (separate directories), not workspaces. Workspaces are for lightweight isolation of identical infrastructure.
*   **Study Resource:** The official workspace documentation explains the full workflow and limitations: [HashiCorp Terraform Documentation — Workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces). Read both the CLI workspace page and the "When to use Multiple Workspaces" guidance.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the workspaces documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/state/workspaces). The free page covers workspace commands, state isolation, and the recommended patterns for multi-environment management.
*   **Required Video:** Watch the video lecture on **Terraform Workspaces** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the section demonstrating workspace creation, switching, and use of `terraform.workspace` in resource naming.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **List and inspect workspaces**: Run `terraform workspace list` to see the `default` workspace. Note the `*` marking the active workspace.
*   **Create and switch to a `dev` workspace**: Run `terraform workspace new dev` and confirm the switch with `terraform workspace show`. Observe that state is now isolated from `default`.
*   **Use `terraform.workspace` in a resource name**: Add `name = "server-${terraform.workspace}"` to a resource and apply in both `default` and `dev` workspaces. Verify that two separate resources with distinct names are created and tracked in separate state files.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the workspaces documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/state/workspaces).
*   [ ] Watch the video lecture on **Terraform Workspaces** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
