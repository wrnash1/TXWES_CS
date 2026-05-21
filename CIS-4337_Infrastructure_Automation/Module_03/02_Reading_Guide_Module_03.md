# Reading Guide: Module 03 - HCL Syntax – Providers, Resources, and Variables
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 03 - HCL Syntax**! This week's study material focuses on the fundamental building blocks of Terraform configuration files: **providers, resources, and variables** — as aligned with the **HashiCorp Certified: Terraform Associate** certification framework. Understanding HCL syntax precisely is critical for both the certification exam and for writing Terraform configurations that work reliably in production.

As a student, you will learn the syntax and required arguments for `provider`, `resource`, and `variable` blocks, understand how Terraform resolves resource dependencies, and practice writing configurations that are both syntactically valid and semantically correct. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Terraform Blocks**: The fundamental structural unit of HCL. A block has a *type* (e.g., `resource`, `provider`, `variable`), optional *labels*, and a *body* enclosed in `{}`. For example: `resource "aws_instance" "web" { ... }` has type `resource`, two labels (`aws_instance` and `web`), and a body containing attribute assignments. The exam tests correct block syntax and which block types require labels.
*   **Provider Block Parameters**: The `provider` block configures a provider plugin (e.g., AWS, Azure). Key parameters include `region`, `alias` (for multiple configurations of the same provider), `version` (deprecated in favor of `required_providers`), and authentication credentials. Provider configuration is separate from resource declarations, and a single provider block can serve multiple resource blocks. The exam tests how `alias` enables multi-region deployments.
*   **Resource Block Parameters**: The `resource` block declares a piece of infrastructure. Its syntax is `resource "<TYPE>" "<NAME>" { ... }` where TYPE is the provider-prefixed resource type (e.g., `aws_s3_bucket`) and NAME is the local identifier used to reference the resource elsewhere. Required vs. optional arguments vary by resource type and are documented in the provider's registry page.
*   **Dependency Resolution**: Terraform automatically builds a dependency graph from resource references. When resource B references `resource.A.id`, Terraform knows to create A before B. This is *implicit* dependency. The `depends_on` meta-argument creates *explicit* dependencies when no attribute reference exists. The exam tests the difference between implicit and explicit dependencies.

---

### 2. Certification Exam Tips
*   **Exam Domain — Write Terraform Configurations (Domain 3):** The Terraform Associate 003 exam tests HCL syntax directly. Know that the `required_providers` block inside a `terraform {}` block is the correct modern way to pin provider versions — not a `version` argument inside the `provider {}` block.
*   **`provider` Block vs. `required_providers` Trap:** The `version` argument inside a `provider` block is deprecated. The correct approach is: declare the provider source and version in `terraform { required_providers { ... } }`, then configure credentials/region in the `provider` block. The exam distinguishes between these two locations.
*   **Resource Meta-Arguments:** Know the four meta-arguments that apply to any resource block: `depends_on`, `count`, `for_each`, and `lifecycle`. The `lifecycle` block contains `create_before_destroy`, `prevent_destroy`, and `ignore_changes`. These are heavily tested. For example, `prevent_destroy = true` causes `terraform destroy` to error rather than delete the resource.
*   **Variable Types:** Terraform variable types include `string`, `number`, `bool`, `list(type)`, `map(type)`, `set(type)`, `object({})`, and `tuple([])`. The exam asks which type to use for a given scenario (e.g., a list of subnet IDs = `list(string)`).
*   **Study Resource:** The official provider and resource documentation on the Terraform Registry is the canonical reference for all provider-specific arguments: [Terraform Registry](https://registry.terraform.io). Browse the AWS or HashiCorp local provider documentation to see real resource block schemas.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the HCL language documentation covering blocks, providers, and resources at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language). The "Resources", "Providers", and "Input Variables" sections are directly exam-relevant.
*   **Required Video:** Watch the video lecture on **HCL Syntax** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the section demonstrating `provider`, `resource`, and `variable` block syntax with live examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a `provider` block and `required_providers`**: Write a `terraform {}` block with `required_providers` specifying a provider source and version constraint. Confirm `terraform init` downloads the correct version.
*   **Declare a `resource` block creating a file or cloud instance**: Write a resource block with at least two attribute assignments. Use `terraform validate` to check syntax, then `terraform apply` to create the resource.
*   **Add an `output` block referencing the resource**: Use `output "example" { value = resource_type.name.attribute }` and observe the value printed after `terraform apply`.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the HCL language documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language).
*   [ ] Watch the video lecture on **HCL Syntax** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
