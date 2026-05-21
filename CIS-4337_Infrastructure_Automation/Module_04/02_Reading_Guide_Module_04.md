# Reading Guide: Module 04 - Terraform State – Local and Remote Backends
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 04 - Terraform State**! This week's study material focuses on how Terraform tracks infrastructure through the **state file**, and how backends — both local and remote — determine where that state is stored and how it is accessed. These topics map directly to the **HashiCorp Certified: Terraform Associate** certification exam's state management domain, one of its most heavily tested areas.

As a student, you will learn what information the state file contains, why it must be protected, how remote backends enable team collaboration, and how to configure an S3 or Terraform Cloud backend. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Terraform state (`terraform.tfstate`)**: A JSON file that records the mapping between your HCL resource declarations and the real-world infrastructure objects Terraform manages. It stores resource IDs, attribute values, and dependency metadata. The state file is the source of truth Terraform uses to compute diffs on every `plan`. It must be treated as sensitive because it often contains secrets (passwords, private keys) in plaintext.
*   **Local backend**: The default backend — state is stored in a `terraform.tfstate` file in the current working directory. Local backend is fine for solo development but unsuitable for teams because there is no locking mechanism and the file is not shared. The exam tests when local vs. remote backends are appropriate.
*   **Remote backends**: Configurations that store state outside the local filesystem — on Amazon S3, Google Cloud Storage, Azure Blob Storage, or Terraform Cloud. Remote backends enable shared state, state locking to prevent concurrent modification, and encryption at rest. The `backend` block inside `terraform {}` configures this. Run `terraform init` after changing the backend.
*   **State locking**: A mechanism that prevents two Terraform operations from running simultaneously against the same state file. AWS S3 backend uses a DynamoDB table for locking; Terraform Cloud has built-in locking. Without locking, concurrent `apply` runs can corrupt the state. The exam tests which backends support locking natively.
*   **`terraform state` subcommands**: The CLI commands for inspecting and managing state without editing the file directly. Key subcommands: `terraform state list` (show all tracked resources), `terraform state show <resource>` (show attributes of one resource), `terraform state mv` (rename or move resources), `terraform state rm` (remove a resource from state without destroying it). The exam tests when to use `state rm` vs. `terraform destroy`.

---

### 2. Certification Exam Tips
*   **Exam Domain — Navigate Terraform Workflow / Manage State (Domain 4):** The Terraform Associate 003 exam has an entire domain on state management. Know the difference between `terraform state rm` (removes from state only, leaves real infrastructure intact) and `terraform destroy` (removes both state and real infrastructure).
*   **Remote Backend Configuration Trap:** The `backend` block goes inside the `terraform {}` block, not the `provider {}` block. A common exam distractor places it in the wrong location. Also: the `backend` block cannot use variable references — all values must be literal strings or use partial configuration with `-backend-config`.
*   **State File Security:** The exam expects you to know that even with `sensitive = true` on a variable, its value is stored in plaintext in the state file. This is why state files must be encrypted at rest and access-controlled. Terraform Cloud encrypts state automatically; S3 backend requires enabling server-side encryption explicitly.
*   **`terraform refresh` vs. `terraform plan`:** `terraform refresh` updates the state file to reflect real-world resource attributes without creating a plan. In newer Terraform versions, `refresh` behavior is incorporated into `plan` by default via the `-refresh=true` flag. The exam may ask about this difference.
*   **Study Resource:** The official backend documentation covers all supported backend types and their locking support: [HashiCorp Terraform Documentation — Backends](https://developer.hashicorp.com/terraform/language/settings/backends/configuration). Review the S3 and Terraform Cloud backend pages specifically.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the state and backends documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/state). The "Purpose of Terraform State" and "Remote State" pages are directly exam-relevant and free to access.
*   **Required Video:** Watch the video lecture on **Terraform State** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the section demonstrating remote backend configuration and `terraform state` subcommands.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Inspect the local `terraform.tfstate` file after an apply**: Open the JSON file and identify the `resources` array. Note the `id` and `attributes` fields and understand how they map to the HCL resource declarations.
*   **Run `terraform state list` and `terraform state show`**: Practice querying the state registry without editing files. Note the output format and identify which attributes are stored.
*   **Configure a remote backend (S3 or Terraform Cloud)**: Update the `terraform {}` block with a `backend` configuration, run `terraform init`, and observe the state migration prompt.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the state documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/state).
*   [ ] Watch the video lecture on **Terraform State** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
