# Reading Guide: Module 10 - Infrastructure as Code Security – Terraform Security Scanning

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 10 - Infrastructure as Code Security – Terraform Security Scanning**! This module covers IaC security scanning as the pipeline gate that prevents misconfigured cloud infrastructure from being provisioned. As organizations define their AWS, Azure, and GCP infrastructure in Terraform HCL files, those files become security artifacts that must be scanned for misconfigurations before `terraform apply` runs. You will learn how IaC scanning tools (Checkov, tfsec, tflint) detect security violations in Terraform code, how they integrate into CI/CD pipelines, and how IaC security connects to the broader DevSecOps shift-left principle. These are core CDP exam topics.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **IaC validation**: The process of automatically checking Infrastructure as Code files (Terraform `.tf`, CloudFormation YAML, Ansible playbooks) for syntax errors, policy violations, and security misconfigurations before the infrastructure is provisioned. IaC validation is the shift-left equivalent for infrastructure — catching a misconfigured S3 bucket in a Terraform file before `terraform apply` is vastly cheaper than remediating a publicly exposed bucket after deployment.

* **Linter checks (tflint)**: Static analysis of Terraform configuration files for syntax errors, deprecated syntax, invalid resource configurations, and provider-specific rule violations. Tflint runs before IaC security scanning and ensures the Terraform code is valid and correctly structured — a prerequisite for meaningful security analysis.

* **Security scanning (Checkov, tfsec)**: Analysis of Terraform and other IaC files against a library of cloud security best-practice rules. Checkov (by Bridgecrew/Prisma Cloud) and tfsec both detect misconfigurations such as S3 buckets with public access enabled, security groups with overly permissive ingress rules (0.0.0.0/0), unencrypted EBS volumes, and missing CloudTrail logging. These tools map findings to CIS Benchmarks, SOC 2, and PCI-DSS control frameworks.

* **Pipeline execution**: The automated sequence of IaC security steps in a CI/CD workflow: checkout → `terraform init` → `tflint` → `checkov -d .` → (if all pass) → `terraform plan` → `terraform apply`. Each step's exit code gates the next; a CRITICAL Checkov finding blocks the plan and apply steps, preventing misconfigured infrastructure from being provisioned.

---

### 2. Certification Exam Tips

* **Shift-Left for Infrastructure**: IaC security scanning applies the same shift-left principle to infrastructure that SAST applies to application code. The CDP exam tests whether you understand that scanning Terraform files at the pull request stage (before `apply`) is the correct pipeline placement, not after provisioning.
* **Checkov vs. tfsec**: Both tools scan Terraform for misconfigurations but differ in approach. Checkov is broader (supports Terraform, CloudFormation, Kubernetes, Dockerfile) and maps findings to compliance frameworks. tfsec is Terraform-focused with deeper HCL parsing. The CDP exam may ask you to identify which tool supports a specific platform or compliance framework.
* **Common IaC Misconfigs**: Know the most common Terraform misconfigurations tested on CDP: public S3 buckets, security groups with `0.0.0.0/0` ingress on sensitive ports, unencrypted RDS instances, IAM roles with `*` actions, missing MFA delete on S3 versioning.
* **Study Resource**: The [Checkov documentation](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) covers all supported checks, CLI usage, CI/CD integration (GitHub Actions, Jenkins), and custom policy writing — essential reference for CDP IaC security scanning questions.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [Checkov documentation and getting started guide](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — covers how Checkov scans Terraform, CloudFormation, and Kubernetes files, the `--check` and `--skip-check` CLI options, SARIF report output, and GitHub Actions integration. Focus on Terraform scanning and CI/CD pipeline integration examples.
* **Required Video**: Watch the IaC security scanning segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — demonstrates writing Terraform code, running Checkov against it, interpreting failing checks, and integrating the scan into a GitHub Actions pipeline that gates `terraform apply`.

---

### Lab & Command Integration

In this week's hands-on lab, you will integrate IaC security scanning into a Terraform pipeline by:

* **Write checkov scanning script for terraform files**: Add a `checkov -d . --framework terraform --output sarif` step to a GitHub Actions workflow that runs on pull requests to the Terraform configuration repository, configured to fail on HIGH and CRITICAL severity findings.
* **Integrate tfsec scanner in pipeline**: Add a `tfsec . --format json` step that runs in parallel with Checkov, providing a second opinion on Terraform misconfigurations and producing a JSON report uploaded as a pipeline artifact.
* **Analyze security failures in outputs**: Review the SARIF and JSON reports — identify at least two failing security checks, note the affected resource, the violated rule (e.g., `CKV_AWS_18`: Ensure the S3 bucket has access logging enabled), and the Terraform configuration change needed to pass the check.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how IaC security scanning applies the shift-left principle to infrastructure provisioning.
* [ ] Read the Checkov documentation at [https://www.checkov.io/1.Welcome/What%20is%20Checkov.html](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html).
* [ ] Watch the IaC security scanning segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the Checkov and tfsec pipeline integration and report analysis in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
