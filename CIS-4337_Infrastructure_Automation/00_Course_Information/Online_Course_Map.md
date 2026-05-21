# Online Course Map: CIS-4337_Infrastructure_Automation

## Target Certification: HashiCorp Certified: Terraform Associate (003)

---

## 16-Week Module Breakdown

### Unit 1 — IaC Foundations & Core Terraform Concepts (Modules 1–4)

* **Module 01:** Introduction to Infrastructure as Code (IaC) — IaC principles, benefits over manual provisioning, declarative vs. imperative models, Terraform's role in the IaC ecosystem
* **Module 02:** Terraform Architecture & Core Workflow — `terraform init`, `terraform plan`, `terraform apply`, `terraform destroy`, provider plugins, the `.terraform` directory
* **Module 03:** HCL Language Fundamentals — resource blocks, variable blocks, output blocks, locals, data sources, expressions, type constraints
* **Module 04:** Terraform State — state file structure, purpose of state, local vs. remote backends, state locking, `terraform.tfstate` security implications

### Unit 2 — Configuration, Providers & Modules (Modules 5–8)

* **Module 05:** Input Variables, Outputs & Locals — variable types, validation blocks, `sensitive = true`, output dependencies, local value expressions
* **Module 06:** Terraform Modules — module blocks, source types (registry, local, Git), module versioning, input/output wiring, module composition patterns
* **Module 07:** Providers & the Terraform Registry — provider configuration, `required_providers`, version constraints, the public registry, provider authentication patterns
* **Module 08:** Remote Backends & State Management — backend types, S3 + DynamoDB locking, Terraform Cloud backend, `terraform init -migrate-state`, partial backend configuration

### Unit 3 — Advanced Operations & Cloud Providers (Modules 9–12)

* **Module 09:** Provisioners, Meta-Arguments & Lifecycle Rules — `depends_on`, `count`, `for_each`, `lifecycle` blocks, `create_before_destroy`, `prevent_destroy`, `ignore_changes`
* **Module 10:** Managing AWS Infrastructure with Terraform — AWS provider configuration, `aws_instance`, `aws_vpc`, `aws_s3_bucket`, IAM roles, S3 remote backend with DynamoDB locking
* **Module 11:** Workspaces & Multi-Environment Management — `terraform workspace` commands, `terraform.workspace` interpolation, workspace isolation, workspaces vs. separate root modules
* **Module 12:** Drift Management & Importing Existing Resources — infrastructure drift detection with `terraform plan`, `terraform import`, `terraform state` subcommands, drift reconciliation strategies

### Unit 4 — Terraform Cloud, CI/CD & Security (Modules 13–15)

* **Module 13:** Terraform Cloud & the Public Registry — Terraform Cloud workspaces, VCS connections, speculative plans, the private registry, run triggers, the `cloud` block
* **Module 14:** Terraform in CI/CD Pipelines — GitHub Actions and GitLab CI integration, `-auto-approve` flag, `TF_VAR_` credential injection, plan file workflows, `terraform validate` and `terraform fmt` in pipelines
* **Module 15:** Terraform Security & Secrets Management — `sensitive = true` on variables and outputs, state file security, hardcoded secret anti-patterns, `TF_VAR_` injection, HashiCorp Vault dynamic secrets

### Unit 5 — Certification Exam (Module 16)

* **Module 16:** Final Exam Prep & Terraform Associate 003 Certification — comprehensive review of all nine exam objective domains, timed practice exam, exam scheduling and logistics for the HashiCorp Certified: Terraform Associate (003) exam

---

## Exam Information

* **Exam:** HashiCorp Certified: Terraform Associate (003)
* **Format:** 57 questions, 60 minutes, multiple choice and true/false
* **Passing score:** Approximately 70% (HashiCorp does not publish the exact threshold)
* **Scheduling:** [HashiCorp Certifications — PSI Exams](https://www.hashicorp.com/certifications/terraform-associate)
* **Official study guide:** [Terraform Associate 003 Exam Review — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003)
