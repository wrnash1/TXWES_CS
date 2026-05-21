# Reading Guide: Module 09 - Terraform Cloud and Terraform Enterprise
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 09 - Terraform Cloud and Terraform Enterprise**! This week's study material covers **Terraform Cloud (TFC)**, HashiCorp's hosted SaaS platform for remote Terraform execution, state management, and team collaboration, and **Terraform Enterprise (TFE)**, the self-hosted version of the same platform for organizations with private network or compliance requirements. Both are heavily tested on the **HashiCorp Certified: Terraform Associate** exam as part of understanding the full Terraform ecosystem beyond the CLI.

As a student, you will learn how Terraform Cloud workspaces differ from CLI workspaces, how the `cloud` and `remote` backend blocks connect a local configuration to Terraform Cloud, how VCS-driven workflows automate plan and apply operations, and when Terraform Enterprise is the appropriate choice. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Terraform Cloud (TFC)**: HashiCorp's hosted SaaS platform that provides remote Terraform execution (runs), centralized state storage with locking, team access controls, cost estimation, policy enforcement (Sentinel/OPA), and a private module registry. TFC is free for small teams and scales to paid tiers for advanced features. The exam tests what TFC provides and when it is preferred over CLI-only usage.
*   **Terraform Enterprise (TFE)**: The self-hosted, on-premises version of Terraform Cloud for organizations that require air-gapped environments, private network execution, or stricter data residency controls. TFE provides all TFC features plus operator-managed installation. The exam distinguishes TFE from TFC by deployment model (self-hosted vs. SaaS).
*   **Terraform Cloud workspace**: In Terraform Cloud, a workspace is a fully isolated environment with its own state file, variables, run history, and access controls. Unlike CLI workspaces (which share configuration code), TFC workspaces can have entirely different configurations, providers, and credentials. The exam explicitly tests this distinction.
*   **`cloud` backend block**: The HCL block used to connect a Terraform configuration to Terraform Cloud. It replaces the older `remote` backend for TFC integrations. Example: `cloud { organization = "my-org" workspaces { name = "prod" } }`. After adding this block, `terraform init` establishes the connection and subsequent runs execute remotely on TFC.
*   **Remote execution vs. local execution**: In remote execution mode (the default for TFC), `terraform plan` and `terraform apply` run on TFC's infrastructure, not on the local machine. In local execution mode, the CLI runs locally but state is still stored on TFC. The exam tests which operations run remotely and that sensitive variable values set on TFC are never exposed to the local runner.

---

### 2. Certification Exam Tips
*   **Exam Domain — Understand Terraform Cloud Capabilities (Domain 5):** Terraform Cloud and Enterprise have their own dedicated exam domain. Know what TFC provides out of the box: remote state, remote execution, team permissions, VCS integration, cost estimation, and the private module registry.
*   **TFC workspace vs. CLI workspace distinction:** The exam commonly presents this as a trap. CLI workspaces share the same `.tf` code in one directory and isolate only state. TFC workspaces are fully independent environments — each can have different code, different providers, and different credentials. When environments differ significantly, TFC workspaces are the recommended pattern.
*   **Sentinel and OPA policy enforcement:** Terraform Cloud supports policy-as-code enforcement through Sentinel (HashiCorp's policy framework) and OPA (Open Policy Agent). Policies can be set to `advisory` (warn only) or `hard-mandatory` (block apply on failure). The exam tests that policy enforcement is a TFC/TFE feature, not a CLI feature.
*   **Private module registry:** TFC includes a private module registry where organizations can publish and version internal Terraform modules. Teams call these modules using the registry address format `<HOSTNAME>/<NAMESPACE>/<MODULE>/<PROVIDER>`. This is the TFC-specific variant of the public registry address format tested in Module 05.
*   **Study Resource:** The official Terraform Cloud documentation covers workspace configuration, the `cloud` block, VCS integration, and policy enforcement: [HashiCorp Terraform Documentation — Terraform Cloud](https://developer.hashicorp.com/terraform/cloud-docs). Review the "Getting Started" section and the workspace overview to understand the features the exam tests most frequently.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the Terraform Cloud overview and workspace documentation at [HashiCorp Terraform Documentation — Terraform Cloud](https://developer.hashicorp.com/terraform/cloud-docs). Focus on the `cloud` backend block configuration, the difference between remote and local execution modes, and the Sentinel policy enforcement overview.
*   **Required Video:** Watch the video lecture on **Terraform Cloud and Terraform Enterprise** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the sections demonstrating TFC workspace creation, VCS integration setup, and the comparison of TFC workspaces to CLI workspaces.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure the `cloud` backend block**: Add a `cloud` block to your Terraform configuration pointing to your TFC organization and workspace. Run `terraform init` and confirm the connection is established. Observe that subsequent `plan` and `apply` operations execute remotely.
*   **Set workspace variables in TFC**: In the TFC UI, set an environment variable and a Terraform variable for your workspace. Run `terraform plan` and verify that the remote run picks up the variables without them being present on the local machine.
*   **Explore the TFC run history**: After a successful `terraform apply`, review the run history in the TFC UI. Observe the plan output, apply log, and state version stored by TFC.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the Terraform Cloud documentation at [HashiCorp Terraform Documentation — Terraform Cloud](https://developer.hashicorp.com/terraform/cloud-docs).
*   [ ] Watch the video lecture on **Terraform Cloud and Terraform Enterprise** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
