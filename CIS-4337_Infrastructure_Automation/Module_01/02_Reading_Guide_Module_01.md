# Reading Guide: Module 01 - IaC Concepts & Benefits
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 01 - IaC Concepts & Benefits**! This week's study material focuses on the core foundations of **Infrastructure as Code** as aligned with the **HashiCorp Certified: Terraform Associate** certification framework. Understanding these topics is essential not only for passing the certification exam but also for managing infrastructure reliably in real-world environments.

As a student, you will learn what IaC is, why it matters, and how the declarative model differs from traditional scripting. You will examine the concept of infrastructure drift, understand how state connects configurations to real resources, and explore the automation benefits that IaC tools like Terraform deliver at scale. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Infrastructure as Code (IaC)**: The practice of defining and provisioning infrastructure resources (servers, networks, databases) through machine-readable configuration files rather than manual processes or GUIs. IaC enables version control, repeatability, and automated deployments across environments. The Terraform Associate exam tests whether you understand IaC as a *declarative* model where you specify the desired end-state.
*   **Declarative vs. Imperative**: Declarative IaC (used by Terraform) describes *what* the final infrastructure should look like; the tool determines the steps to reach that state. Imperative scripting (e.g., shell scripts, Ansible tasks) describes *how* to reach a state step-by-step. The exam frequently asks you to identify which approach Terraform uses and why declarative is preferred for idempotency.
*   **Drift**: Configuration drift occurs when the actual state of deployed infrastructure diverges from the desired state defined in your IaC code — typically caused by manual out-of-band changes. Terraform detects drift by comparing the live resource state to the state file during `terraform plan`. The exam tests your ability to recognize drift scenarios and describe how Terraform reconciles them.
*   **State**: Terraform state is a JSON record (stored in `terraform.tfstate`) that maps your HCL resource declarations to real-world infrastructure IDs. State is essential for tracking what Terraform manages, computing diffs during plan, and enabling resource updates and destruction. Never delete or manually edit the state file; use `terraform state` subcommands instead.
*   **Automation**: In the IaC context, automation means that infrastructure provisioning, changes, and teardown are triggered programmatically (via CLI or CI/CD pipeline) without manual intervention. Terraform achieves automation through its workflow (`init → plan → apply`) and supports non-interactive runs with `-auto-approve` in pipelines.

---

### 2. Certification Exam Tips
*   **Exam Domain — Understand IaC Concepts (Domain 1):** The Terraform Associate 003 exam explicitly tests IaC benefits: consistency, repeatability, versioning, and self-documentation. Know that Terraform uses a *declarative* model, not imperative, and understand what makes this advantageous.
*   **Declarative vs. Imperative Trap:** The exam presents scenarios asking which approach Terraform follows. Always answer *declarative*. Do not confuse `local-exec` provisioners (which run imperative shell commands) with Terraform's overall declarative model — Terraform itself is declarative even when calling shell scripts.
*   **Drift Detection:** Know that `terraform plan` is the command that reveals drift. When a plan shows unexpected changes you did not make in code, that is drift from an out-of-band manual change. The exam may ask what causes drift (manual console changes, other tools) and how to fix it (re-apply or update code to match reality).
*   **Study Resource:** The official HashiCorp documentation on IaC concepts provides the authoritative definitions tested on the exam: [HashiCorp Terraform Documentation — What is Terraform?](https://developer.hashicorp.com/terraform/intro). Review the "Use Cases" and "How Terraform Works" sections carefully.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the IaC introduction and core concepts section in the official HashiCorp documentation: [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/intro). This is the primary OER resource for this course and is free to access.
*   **Required Video:** Watch the video lecture on **IaC Concepts & Benefits** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Pay close attention to the sections distinguishing declarative from imperative approaches.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Compare manual server provisioning vs. automated IaC configuration**: Manually create a resource via a cloud console, then observe what `terraform plan` reports when the same resource is declared in HCL. Note the difference in repeatability and auditability.
*   **Review declarative IaC configurations**: Examine a sample `main.tf` file and identify each declarative block. Confirm that the file describes desired state, not procedural steps.
*   **Examine infrastructure drift symptoms**: Make a manual change to a provisioned resource (e.g., change a tag or file content), then run `terraform plan` to observe how drift is surfaced as a planned change.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
- [ ] Read the IaC introduction in [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/intro).
- [ ] Watch the video lecture on **IaC Concepts & Benefits** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
