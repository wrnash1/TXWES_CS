# Reading Guide: Module 14 - Terraform in CI/CD Pipelines

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction

Welcome to **Module 14 - Terraform in CI/CD Pipelines**! This week's study material focuses on automating Terraform workflows inside continuous integration and continuous delivery systems such as GitHub Actions and GitLab CI. Running Terraform in pipelines enables consistent, auditable, and repeatable infrastructure deployments triggered by code changes — a core pattern in modern DevOps and a topic tested on the Terraform Associate exam.

As a student, you will learn how to structure a CI/CD pipeline for Terraform, which flags and environment variables are required for non-interactive execution, how to gate applies behind plan review steps, how to validate and lint configurations automatically, and the security considerations for storing credentials in pipeline environments. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **GitHub Actions**: A CI/CD automation platform built into GitHub that executes workflows defined in YAML files stored under `.github/workflows/`. Each workflow consists of jobs containing steps that run shell commands or reusable actions. For Terraform, workflows typically include steps for `terraform init`, `terraform validate`, `terraform plan`, and (on merge) `terraform apply -auto-approve`.
* **GitLab CI**: GitLab's built-in CI/CD system configured via a `.gitlab-ci.yml` file at the repository root. Pipelines are divided into stages (e.g., validate, plan, apply), with each stage running one or more jobs in parallel or sequence. GitLab CI supports manual approval gates between stages, which is the standard pattern for gating Terraform applies.
* **non-interactive execution (`-auto-approve`)**: The `-auto-approve` flag passed to `terraform apply` that suppresses the interactive confirmation prompt, allowing the command to run to completion without waiting for user input. This flag is required in all automated CI/CD pipelines because pipeline runners have no interactive terminal to accept the confirmation.
* **linting and validation**: Automated checks run against Terraform configuration before planning or applying. `terraform validate` checks that all configuration files are syntactically correct and internally consistent. `terraform fmt -check` verifies that files conform to the canonical HCL formatting style. Third-party tools such as `tflint` and `checkov` add provider-specific rule checks and security scanning.

---

### 2. Certification Exam Tips

* **`-auto-approve` is required in pipelines:** The exam tests knowledge of why `terraform apply` must include `-auto-approve` in automated contexts. Without it, the command blocks indefinitely waiting for `yes` input that a pipeline runner cannot provide. Know that this flag bypasses the safety confirmation step and should be paired with a required plan-review gate earlier in the pipeline.
* **Credential injection via environment variables:** Pipelines must supply cloud provider credentials without hardcoding them in `.tf` files. The standard pattern is to store secrets in the CI platform's secret store (GitHub Actions secrets, GitLab CI variables) and inject them as environment variables (e.g., `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `TF_VAR_` prefixed variables) available to the Terraform process.
* **`TF_VAR_` prefix for variable injection:** Terraform reads environment variables prefixed with `TF_VAR_` and maps them to input variables of the same name. For example, `TF_VAR_region=us-east-1` sets the `region` input variable. This is the recommended way to pass secrets and environment-specific values into Terraform from CI pipelines without using `.tfvars` files.
* **Study Resource:** The HashiCorp documentation on automating Terraform covers the full recommended CI/CD workflow including plan files, approval gates, and credential patterns: [Automate Terraform — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the HashiCorp tutorial on automating Terraform in CI/CD systems, which covers the recommended pipeline structure, plan file usage, and credential injection patterns: [Automate Terraform — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform).
* **Required Video:** Watch the video lecture on **Terraform in CI/CD Pipelines** in the official course playlist, which demonstrates writing a GitHub Actions workflow YAML file that runs `terraform init`, `terraform validate`, `terraform plan`, and `terraform apply -auto-approve` as separate pipeline steps: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Write a GitHub Actions YAML workflow file**: Create `.github/workflows/terraform.yml` with jobs for `terraform init`, `terraform fmt -check`, `terraform validate`, `terraform plan -out=tfplan`, and `terraform apply tfplan`. Configure the workflow to trigger on `push` to the `main` branch and on `pull_request` events. Inject AWS credentials using `env:` variables sourced from GitHub Actions secrets.
* **Run `terraform validate` in the pipeline workflow**: Add a dedicated validation step that runs `terraform validate` after `terraform init`. Confirm the step exits with code 0 on valid configuration and non-zero on a syntax error. Introduce a deliberate error and observe the pipeline fail at the validate step before reaching plan.
* **Configure automated plan output on pull requests**: Add a step that runs `terraform plan -out=tfplan` and posts the plan summary as a pull request comment using the `actions/github-script` action or a community Terraform action. Verify the PR shows the plan diff before a reviewer approves the merge.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
* [ ] Read the automation tutorial at [Automate Terraform — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform).
* [ ] Watch the video lecture on **Terraform in CI/CD Pipelines** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
