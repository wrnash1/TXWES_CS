# CIS-4337 Infrastructure Automation

## Reading Guide — Module 01: IaC Concepts and Benefits

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This reading guide supports Module 01 of CIS-4337 Infrastructure Automation at Texas Wesleyan University. The material in this module maps directly to Domain 1 of the Terraform Associate 003 exam: Understand Infrastructure as Code (IaC) Concepts. Work through every section before attempting the lab or quiz.

---

## 1. Core Vocabulary

Mastery of the following terms is required for both the course exams and the Terraform certification.

**Infrastructure as Code (IaC)**
The practice of managing and provisioning infrastructure resources — servers, networks, databases, load balancers, DNS records — through machine-readable configuration files rather than manual processes or graphical interfaces. IaC enables version control, repeatability, and automated deployment across multiple environments. The Terraform Associate exam tests whether you understand IaC as a declarative model in which you specify desired end state.

**Declarative Model**
An IaC approach in which you describe what the final infrastructure should look like. The automation tool determines the sequence of steps needed to reach that state. Terraform uses the declarative model. You write HCL that says "I want this resource to exist with these properties," and Terraform computes the required API calls.

**Imperative Model**
An IaC approach in which you write step-by-step instructions telling the tool exactly which actions to perform. Shell scripts, Python scripts using Boto3, and step-by-step Ansible tasks are examples of imperative automation. The model is powerful but can produce unintended results when run multiple times against infrastructure that has already been partially configured.

**Idempotency**
A property of an operation meaning it can be applied multiple times without producing a different result after the first application. Terraform's declarative model is idempotent: running `terraform apply` on infrastructure that already matches your configuration produces zero changes. Imperative scripts are frequently not idempotent.

**Configuration Drift**
The gradual divergence between the actual state of deployed infrastructure and the desired state declared in your IaC code. Drift is typically caused by manual out-of-band changes made through a cloud console or directly on a server without updating the corresponding configuration files. Terraform detects drift by comparing live resource state (queried through provider APIs) to the state file during `terraform plan`.

**Terraform State**
A JSON record, stored by default in a file named `terraform.tfstate`, that maps every resource declared in your HCL configuration to the real-world identifier and current attributes of the corresponding cloud resource. State is essential: without it, Terraform cannot determine what already exists, compute accurate diffs, or safely destroy resources. The state file must never be manually edited; use `terraform state` subcommands to manipulate it.

**Provider**
A plugin that enables Terraform to communicate with a specific API or platform. Providers exist for AWS, Azure, Google Cloud, Kubernetes, GitHub, Datadog, and hundreds of other services. Each provider is distributed independently and declared in your configuration with a `required_providers` block.

**HCL (HashiCorp Configuration Language)**
The domain-specific language used to write Terraform configurations. HCL is human-readable, supports comments, and uses a block-based syntax. Files with a `.tf` extension are HCL configuration files. Files with a `.tf.json` extension use JSON syntax as an alternative encoding.

**ClickOps**
An informal term describing the manual practice of provisioning and configuring infrastructure by clicking through web consoles. ClickOps is slow, error-prone, and leaves no reproducible audit trail. IaC replaces ClickOps with code-reviewed, version-controlled automation.

**Execution Plan**
The output of `terraform plan`, which shows a preview of every resource Terraform intends to create, modify, or destroy before any changes are made. The execution plan is one of Terraform's most important safety features because it allows operators to review the scope of a change before committing to it.

---

## 2. HCL Syntax Reference

The following examples demonstrate the core HCL block types used throughout this course. Study these patterns now; you will use them in every lab.

### Terraform Settings Block

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

The `terraform` block declares the minimum Terraform version and the providers the configuration requires.

### Provider Block

```hcl
provider "aws" {
  region = "us-east-1"
}
```

The `provider` block configures a specific provider. Every resource managed by that provider uses this configuration unless overridden.

### Resource Block

```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-bucket-name"

  tags = {
    Environment = "dev"
    ManagedBy   = "terraform"
  }
}
```

The `resource` block is the fundamental building block of a Terraform configuration. The first label (`aws_s3_bucket`) is the resource type. The second label (`example`) is the local name used to reference this resource within the configuration.

### Variable Block

```hcl
variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}
```

Variables parameterize configurations. They accept a `description`, a `type` constraint, an optional `default`, and optional `validation` blocks.

### Output Block

```hcl
output "bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.example.arn
}
```

Output blocks expose values from a configuration for display after `terraform apply` or for consumption by other configurations.

---

## 3. Terraform Workflow Commands

The following commands constitute the core Terraform workflow. Memorize their purpose and sequence.

| Command | Purpose |
|---|---|
| `terraform init` | Downloads provider plugins, initializes the backend, and prepares the working directory. Always run first. |
| `terraform validate` | Checks HCL syntax and internal consistency without contacting any provider APIs. |
| `terraform plan` | Computes an execution plan showing what changes will be made. Refreshes state from live infrastructure. |
| `terraform apply` | Executes the plan. Creates, updates, or destroys resources. Updates the state file. |
| `terraform destroy` | Destroys all resources managed by the current configuration. |
| `terraform fmt` | Formats `.tf` files to the canonical HCL style. |
| `terraform show` | Displays the current state or a saved plan file in human-readable form. |
| `terraform state list` | Lists all resources tracked in the state file. |

---

## 4. State File Fundamentals

The `terraform.tfstate` file is a JSON document. A simplified excerpt looks like this:

```json
{
  "version": 4,
  "terraform_version": "1.6.0",
  "resources": [
    {
      "type": "aws_s3_bucket",
      "name": "example",
      "instances": [
        {
          "attributes": {
            "bucket": "my-unique-bucket-name",
            "arn": "arn:aws:s3:::my-unique-bucket-name"
          }
        }
      ]
    }
  ]
}
```

Key facts about state:

- Terraform reads state on every `plan` and `apply` to determine what already exists.
- The state file may contain sensitive values such as passwords and private keys. Protect it accordingly.
- Local state (the default) stores `terraform.tfstate` in the working directory. Remote backends (covered in Module 04) store state in systems like S3, Terraform Cloud, or Azure Blob Storage.
- Never delete the state file unless you intentionally want Terraform to lose track of all managed resources.
- Use `terraform state rm` to remove a resource from state without destroying it.

---

## 5. IaC Approaches Compared

| Characteristic | Declarative (Terraform) | Imperative (Scripts) |
|---|---|---|
| You specify | Desired end state | Step-by-step actions |
| Idempotent by design | Yes | Rarely |
| Drift detection | Built in via `plan` | Manual or custom |
| Dependency resolution | Automatic | Manual ordering |
| Example tools | Terraform, CloudFormation | Bash, Python/Boto3 |

---

## 6. The IaC Benefits Summary

The Terraform Associate exam frequently asks you to identify IaC benefits. Know all eight:

1. **Speed** — Automated provisioning takes minutes instead of hours.
2. **Consistency** — Identical configurations produce identical environments.
3. **Version control** — All infrastructure changes are tracked in Git with author and timestamp.
4. **Self-documentation** — The configuration file is always accurate documentation.
5. **Reusability** — Modules can be shared across teams and projects.
6. **Cost management** — Ephemeral environments can be destroyed when not needed.
7. **Disaster recovery** — Rebuilding from code is faster and more reliable than manual reconstruction.
8. **Collaboration** — Infrastructure changes receive the same code-review treatment as application code.

---

## 7. Required Reading

Complete the following before the lab activity:

- Read the "What is Terraform?" introduction at developer.hashicorp.com/terraform/intro
- Read the "Use Cases" page at developer.hashicorp.com/terraform/intro/use-cases
- Read the "Terraform Language" overview at developer.hashicorp.com/terraform/language

These pages are free to access and are the same documentation referenced during the certification exam.

---

## 8. Terraform Associate 003 Exam Tips

The following tips address the most common mistakes students make on Domain 1 questions.

**Tip 1.** The exam always classifies Terraform as declarative. Do not be misled by the fact that `local-exec` and `remote-exec` provisioners run imperative shell commands. Terraform as a whole is declarative even when it invokes shell scripts for edge cases.

**Tip 2.** Drift is detected during `terraform plan`, not `terraform apply`. The plan phase refreshes state by querying live provider APIs, which is when divergence becomes visible.

**Tip 3.** The state file maps HCL resource declarations to real-world resource IDs. If you delete the state file, Terraform does not know what resources it manages, which causes it to attempt to create duplicates on the next apply.

**Tip 4.** Idempotency is a benefit of the declarative model, not a separate feature you configure. Running `terraform apply` on already-correct infrastructure produces a "No changes" result automatically.

**Tip 5.** The exam distinguishes between IaC and configuration management. Terraform provisions infrastructure. Tools like Ansible, Chef, and Puppet configure software on existing servers. The two categories are complementary.

**Tip 6.** Know all four Terraform workflow commands: `init`, `plan`, `apply`, `destroy`. The exam tests the correct sequence (init always before plan) and what each command does.

**Tip 7.** The `terraform.tfstate` file should never be stored in version control when it contains sensitive values. Remote backends solve this problem and also enable team collaboration.

**Tip 8.** Cloud-agnostic means one tool manages multiple providers simultaneously. A single Terraform configuration can provision AWS resources, Azure resources, and a GitHub repository in the same run.

---

## 9. Study Checklist

Work through each item before proceeding to the lab.

- [ ] Define Infrastructure as Code in your own words without referring to notes.
- [ ] Explain the difference between declarative and imperative IaC to a classmate.
- [ ] List all eight IaC benefits from memory.
- [ ] Describe what configuration drift is and how Terraform detects it.
- [ ] Explain the purpose of the `terraform.tfstate` file.
- [ ] State the four core Terraform CLI commands in correct sequence.
- [ ] Read all three required pages at developer.hashicorp.com.
- [ ] Complete the Module 01 lab activity.
- [ ] Complete the Module 01 quiz.
- [ ] Submit your initial discussion post by the Wednesday deadline.

---

Module 01 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
