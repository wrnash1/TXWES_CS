# Reading Guide: Module 12 - Drift Management & Importing Existing Resources

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction

Welcome to **Module 12 - Drift Management & Importing Existing Resources**! This week's study material covers two closely related challenges: detecting when real infrastructure has diverged from Terraform's recorded state (drift), and bringing pre-existing infrastructure under Terraform management via `terraform import`. These topics are tested directly on the Terraform Associate exam and arise constantly in real-world IaC adoption.

As a student, you will learn how Terraform detects drift during `terraform plan`, the difference between drift in state versus drift in configuration, how `terraform import` populates state without generating HCL, and the workflow required to fully reconcile imported resources with written code. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Infrastructure drift**: The condition where real-world infrastructure resources have been modified outside of Terraform — through the cloud console, CLI, or another tool — so that the actual resource configuration no longer matches what is recorded in the Terraform state file. Drift is surfaced as a diff in `terraform plan` output showing changes Terraform would make to restore the desired state.
* **`terraform import`**: A CLI command that reads a real cloud resource identified by its provider-specific ID and writes its attributes into the Terraform state file. Critically, `terraform import` does not generate HCL configuration — the practitioner must manually write a matching `resource` block before import, and the two must align or subsequent `terraform plan` runs will show unwanted diffs.
* **drift reconciliation**: The process of resolving the gap between actual infrastructure state and the Terraform-managed desired state. Reconciliation options include running `terraform apply` to force infrastructure back to the desired state, updating the HCL configuration to accept the out-of-band change, or using `terraform state rm` to remove the drifted resource from state management entirely.

---

### 2. Certification Exam Tips

* **`terraform refresh` vs. `terraform plan`:** The exam tests the difference between these commands. `terraform refresh` updates the state file to match real infrastructure without producing a plan or making changes. `terraform plan` implicitly refreshes state and then computes the diff. In Terraform 0.15.4+, `terraform plan -refresh-only` is the preferred replacement for the standalone `terraform refresh` command.
* **`terraform import` does not write HCL:** This is the most common exam trap for this topic. After running `terraform import`, state is populated but no `.tf` file is created. You must write the `resource` block manually. If you run `terraform plan` before writing the HCL, Terraform will show a plan to destroy the imported resource.
* **`terraform state` subcommands:** Know `terraform state list`, `terraform state show <address>`, `terraform state mv`, and `terraform state rm`. These commands are used for manual drift reconciliation and are tested in scenario questions.
* **Study Resource:** The HashiCorp documentation on importing infrastructure covers both the CLI command and the newer config-driven `import` block introduced in Terraform 1.5: [Import Existing Resources — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/import).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the **Import** section of the official HashiCorp documentation, which covers both the CLI `terraform import` command and the newer `import` block syntax introduced in Terraform 1.5: [Import Existing Resources — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/import).
* **Required Video:** Watch the video lecture on **Drift Management & Importing Existing Resources** in the official course playlist, which demonstrates detecting drift with `terraform plan` and the full import workflow from resource discovery to HCL reconciliation: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Manually modify a resource outside Terraform to simulate drift**: Use the cloud console or CLI to change an attribute (e.g., a resource tag or instance type) on a resource that Terraform manages. This simulates an out-of-band change — the most common real-world source of drift.
* **Run `terraform plan` to detect the drift**: Execute `terraform plan` and observe the diff output. Terraform will show the attribute change as something it wants to revert. Review which attributes are shown as changing and confirm they match the manual modification you made.
* **Import a pre-existing resource into Terraform state**: Write a `resource` block for an existing cloud resource, then run `terraform import <resource_address> <provider_id>` to populate state. Run `terraform plan` afterward and iteratively update the HCL until the plan shows no changes, confirming full reconciliation.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
* [ ] Read the **Import** section in [Import Existing Resources — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/language/import).
* [ ] Watch the video lecture on **Drift Management & Importing Existing Resources** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
