# Reading Guide: Module 13 – Cloud Deployment Manager and Terraform on GCP
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 13 – Cloud Deployment Manager and Terraform on GCP**! Infrastructure as Code (IaC) lets you define, version, and repeatedly deploy cloud resources using configuration files rather than manual Console clicks. This module covers Google Cloud Deployment Manager (GCP's native IaC tool) and HashiCorp Terraform (the most widely adopted multi-cloud IaC tool), including how each manages state, handles updates, and integrates with GCP. The ACE exam tests your ability to recognize IaC concepts, interpret basic configuration syntax, and understand when each tool is appropriate.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Infrastructure as Code (IaC)**: The practice of managing and provisioning cloud infrastructure through machine-readable configuration files rather than manual processes. IaC enables version control, repeatability, and peer review of infrastructure changes. Both Deployment Manager and Terraform implement IaC for GCP resources.

*   **Cloud Deployment Manager**: GCP's native IaC service. Configurations are written in YAML (with optional Python or Jinja2 templates). Deployment Manager manages a **deployment** — a collection of GCP resources defined in a configuration file. It tracks resource state internally and supports `create`, `update`, and `delete` operations on deployments.

*   **Terraform**: An open-source IaC tool by HashiCorp that uses HashiCorp Configuration Language (HCL). Terraform manages resources across multiple cloud providers. On GCP, Terraform uses the `google` provider. Key workflow: `terraform init` (downloads providers), `terraform plan` (previews changes), `terraform apply` (creates/updates resources), `terraform destroy` (deletes all managed resources).

*   **Terraform State**: A file (by default `terraform.tfstate`) that records the current state of all resources Terraform manages. Terraform compares the desired state (your `.tf` files) against the recorded state to determine what changes need to be made. For team environments, state should be stored remotely in a Cloud Storage bucket to prevent conflicts.

*   **Idempotency**: The property of an operation that produces the same result whether applied once or many times. Both Deployment Manager and Terraform are idempotent — re-running a deployment with no configuration changes results in no resource modifications.

*   **`gcloud deployment-manager` commands**: The CLI interface for Cloud Deployment Manager. Key subcommands: `deployments create`, `deployments update`, `deployments delete`, and `deployments describe`. The `--config` flag specifies the YAML configuration file to use.

---

### 2. Certification Exam Tips

*   **`terraform plan` before `terraform apply`**: The ACE exam tests the Terraform workflow. Always run `terraform plan` to preview changes before applying them. The plan output shows what resources will be created (`+`), modified (`~`), or destroyed (`-`). This prevents unintended infrastructure changes.

*   **Remote state storage in Cloud Storage**: For production Terraform usage with a team, store the state file in a Cloud Storage bucket with versioning enabled. This prevents two team members from running `terraform apply` simultaneously and corrupting the state. The exam may ask about the correct backend configuration for GCP.

*   **Deployment Manager vs. Terraform — when each is appropriate**: Deployment Manager is GCP-native and requires no additional tooling. Terraform supports multi-cloud deployments and has a larger ecosystem of modules. The ACE exam primarily tests Deployment Manager concepts but expects familiarity with Terraform commands and workflow.

*   **Import existing resources**: Both tools can import existing manually created resources into their management. In Terraform, `terraform import` brings an existing GCP resource under Terraform management by adding it to the state file. The exam may test that you know you cannot manage a resource with Terraform until it is imported or until the resource is recreated by Terraform.

*   **Study Resource**: The freeCodeCamp ACE course covers Deployment Manager configuration syntax and Terraform provider setup for GCP: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Infrastructure as Code chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Cloud Deployment Manager overview including configuration file structure, deployments, and the `gcloud deployment-manager` command reference: [Cloud Deployment Manager Overview](https://cloud.google.com/deployment-manager/docs/overview). The YAML configuration structure is directly exam-relevant.
*   **Required Reading**: Review the Terraform on GCP getting started guide, which covers provider configuration, resource blocks, and the init/plan/apply workflow: [Terraform on Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started). Focus on the core workflow commands.
*   **Required Video**: Watch the Infrastructure as Code segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Deployment Manager and Terraform chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a GCP resource using Cloud Deployment Manager and deploy a simple infrastructure using Terraform. Key commands to practice:

*   `gcloud deployment-manager deployments create my-deployment --config=config.yaml` — creates a new deployment from a YAML configuration file
*   `gcloud deployment-manager deployments update my-deployment --config=config.yaml` — applies changes to an existing deployment
*   `terraform init` — initializes the working directory, downloads the GCP provider plugin
*   `terraform plan -out=tfplan` — generates and saves an execution plan showing proposed changes
*   `terraform apply tfplan` — applies the saved execution plan to create or modify resources

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Deployment Manager Overview](https://cloud.google.com/deployment-manager/docs/overview) documentation page.
- [ ] Read the [Terraform on Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started) getting started guide.
- [ ] Watch the Infrastructure as Code segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: deploy a GCP resource using Deployment Manager and Terraform.
- [ ] Proceed to the weekly quiz.
