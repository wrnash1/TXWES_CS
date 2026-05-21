# Reading Guide: Module 05 - Modules – Creating and Using Reusable Modules
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 05 - Terraform Modules**! This week's study material focuses on how **modules** enable reusable, composable infrastructure code in Terraform — a core concept in the **HashiCorp Certified: Terraform Associate** certification exam. Modules are Terraform's primary mechanism for DRY (Don't Repeat Yourself) infrastructure patterns and for sharing standardized configurations across teams and projects.

As a student, you will learn the difference between root and child modules, how to pass inputs and receive outputs between modules, and how to source modules from local paths, Git repositories, and the Terraform Public Registry. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Root module**: Every Terraform configuration has exactly one root module — it is the set of `.tf` files in the directory where you run `terraform init` and `terraform apply`. The root module may call child modules. It is responsible for providing input variable values to all called modules and consuming their outputs.
*   **Child modules**: Reusable units of Terraform configuration called from a root module (or another module) using a `module` block. A child module lives in its own directory and defines its own `variable`, `resource`, and `output` blocks. Child modules do not inherit the calling module's provider configuration unless explicitly passed via the `providers` argument. The exam tests this isolation.
*   **Module `source` argument**: The only required argument in a `module` block. It specifies where the module code is located: a local relative path (`./modules/vpc`), a Git URL (`git::https://...`), or a Terraform Registry address (`hashicorp/consul/aws`). After adding or changing a `source`, you must re-run `terraform init` to download the module.
*   **Input variables and outputs in modules**: Child modules expose an interface through `variable` blocks (inputs) and `output` blocks (outputs). The calling module passes values to the child's variables as arguments in the `module` block. The caller accesses the child's outputs via `module.<name>.<output_name>`. This is the primary way data flows between modules.
*   **Module versioning**: When sourcing modules from the Terraform Registry or a Git tag, a `version` argument pins the module to a specific release. This is critical for stability — without pinning, updates to a registry module could break your configuration silently. The exam tests the `version` argument in the `module` block.

---

### 2. Certification Exam Tips
*   **Exam Domain — Use the Core Terraform Workflow / Interact with Modules (Domain 5):** Module interaction is a major exam domain. Know the required argument (`source`), the optional arguments (`version`, `providers`, `depends_on`, `count`, `for_each`), and how to reference module outputs.
*   **`terraform get` vs. `terraform init`:** Both download modules, but `terraform init` also downloads providers and sets up the backend. `terraform get` only downloads modules. In practice, always use `init`. The exam may ask which command downloads modules.
*   **Public Registry Module Address Format:** Registry module addresses follow the format `<NAMESPACE>/<MODULE>/<PROVIDER>` (e.g., `hashicorp/consul/aws`). The exam tests this three-part format. Registry modules also require a `version` argument; without it, `init` fetches the latest version, which may change unexpectedly.
*   **Module isolation trap:** Child modules do not automatically inherit provider configurations from the caller. If a child module needs a provider, it must either define its own `required_providers` or receive a provider via the `providers` map argument. The exam presents scenarios where a module needs a provider in a different region and tests whether you use `alias` and pass it explicitly.
*   **Study Resource:** The Terraform Public Registry hosts thousands of community and official modules with usage documentation: [Terraform Registry](https://registry.terraform.io/browse/modules). Browse the AWS VPC module to see a real-world example of module inputs, outputs, and source addresses.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the modules documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/modules). The "Module Blocks", "Calling a Child Module", and "Module Sources" pages are directly exam-relevant and free to access.
*   **Required Video:** Watch the video lecture on **Terraform Modules** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the section showing how to structure a child module directory and call it from root.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a reusable child module under `modules/`**: Create a subdirectory with its own `main.tf`, `variables.tf`, and `outputs.tf`. Define at least one input variable and one output value.
*   **Call the child module from the root configuration**: Write a `module` block in the root `main.tf` specifying `source = "./modules/<name>"` and pass the required input values. Run `terraform init` and `terraform apply`.
*   **Reference the module's output in a root output block**: Use `output "result" { value = module.<name>.<output_name> }` and verify the value appears after apply.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the modules documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/modules).
*   [ ] Watch the video lecture on **Terraform Modules** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
