# Reading Guide: Module 02 - Terraform Workflow
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 02 - Terraform Workflow**! This week's study material focuses on the core operational commands of the **Terraform CLI workflow — Init, Plan, Apply, and Destroy** — as aligned with the **HashiCorp Certified: Terraform Associate** certification framework. Understanding these topics is essential not only for passing the certification exam but also for operating Terraform confidently in real-world environments.

As a student, you will learn the precise purpose and sequence of each Terraform CLI command, understand what happens inside the `.terraform/` directory after initialization, and practice reading plan output to predict infrastructure changes before they are applied. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Terraform Core**: The open-source binary (`terraform`) that reads HCL configuration files, communicates with provider plugins via RPC, and manages the state file. Terraform Core is distinct from provider plugins — it orchestrates the workflow but does not itself understand any specific cloud API. The exam tests whether you know Core is separate from providers.
*   **Plugins / Providers**: Provider plugins are separate executables (e.g., `terraform-provider-aws`) downloaded into `.terraform/providers/` during `terraform init`. They translate HCL resource declarations into the correct API calls for a specific platform (AWS, Azure, GCP, etc.). The Terraform Registry at [registry.terraform.io](https://registry.terraform.io) is the default source for providers. Exam tip: providers are NOT part of Terraform Core.
*   **HCL (HashiCorp Configuration Language)**: The human-readable, declarative language used to write Terraform configuration files (`.tf`). HCL uses blocks (`resource`, `provider`, `variable`, `output`, `locals`, `terraform`) with attribute-value pairs. It supports expressions, functions, and references between resources. The exam tests basic HCL syntax and block types extensively.
*   **`terraform init`**: The first command run in any Terraform project directory. It downloads provider plugins, sets up the `.terraform/` directory, initializes the backend (local or remote), and fetches any referenced modules. You must re-run `init` after adding new providers or modules. This command is safe to run multiple times — it is idempotent.
*   **`terraform plan`**: Generates an execution plan by comparing the current state to the desired configuration. It shows what will be created (`+`), updated (`~`), or destroyed (`-`). Plan does not make any changes to real infrastructure; it is a dry-run. The `-out` flag saves the plan to a file that can be passed to `apply` for deterministic deployments.

---

### 2. Certification Exam Tips
*   **Exam Domain — Understand Terraform's Purpose and Workflow (Domain 1 & 2):** The Terraform Associate 003 exam tests the four core workflow commands in detail. Know the exact sequence: `init` → `plan` → `apply` → `destroy`. Know what each command does and what it does NOT do (e.g., `plan` never modifies resources).
*   **`terraform init` Traps:** The exam frequently asks what `init` does: it downloads providers AND modules AND sets up backends. It does NOT apply configuration or create resources. If a new provider is added to a config that was already initialized, you must re-run `init` to download it.
*   **Reading Plan Output:** Know how to interpret plan symbols: `+` (create), `-` (destroy), `~` (update in-place), `-/+` (destroy then recreate). The exam presents plan output snippets and asks what will happen. Pay special attention to `-/+` — it means forced replacement, not just an update.
*   **`terraform apply` vs `terraform plan -out`:** `apply` without a saved plan does a fresh plan first; `apply <planfile>` executes the exact saved plan with no additional prompt. In automated pipelines, use `plan -out=tfplan` followed by `apply tfplan` to guarantee what runs matches what was reviewed.
*   **Study Resource:** The official HashiCorp documentation covers the CLI workflow in detail: [HashiCorp Terraform Documentation — The Core Terraform Workflow](https://developer.hashicorp.com/terraform/intro/core-workflow). This page is the authoritative reference for workflow-related exam questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the core workflow documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/intro/core-workflow). This free OER resource explains the Write → Plan → Apply workflow with diagrams.
*   **Required Video:** Watch the video lecture on **Terraform Workflow** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the section demonstrating each CLI command and its terminal output.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Install Terraform CLI and verify the binary**: Run `terraform version` after installation to confirm the binary is accessible on your PATH and note the version number. The exam may reference CLI version compatibility.
*   **Create a minimal `main.tf` and run `terraform init`**: Observe the `.terraform/` directory created, the `.terraform.lock.hcl` file generated, and the provider plugin downloaded. Note which registry URL the provider was fetched from.
*   **Run `terraform plan` and interpret the output**: Read each line of the plan carefully. Identify `+`, `~`, and `-` symbols. Then run `terraform apply` to execute the plan and observe real resource creation.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the core workflow documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/intro/core-workflow).
*   [ ] Watch the video lecture on **Terraform Workflow** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
