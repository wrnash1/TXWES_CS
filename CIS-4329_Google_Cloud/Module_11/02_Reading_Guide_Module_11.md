# Reading Guide: Module 11 — Infrastructure as Code on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This reading guide accompanies the Module 11 video lectures on Infrastructure as Code.
It covers Cloud Deployment Manager, Terraform with the GCP provider, state management,
and infrastructure versioning patterns.

**Estimated reading time**: 60–75 minutes

---

### Learning Objectives

After completing this module's readings you will be able to:

- Explain the purpose and benefits of Infrastructure as Code
- Write and deploy Cloud Deployment Manager configurations
- Use Deployment Manager Jinja2 templates for reusable resource definitions
- Initialize, plan, apply, and destroy infrastructure with Terraform
- Configure Terraform remote state in Cloud Storage
- Compare Deployment Manager and Terraform for GCP use cases
- Describe infrastructure versioning best practices using Git

---

### Required Reading 1: Cloud Deployment Manager

**Source**: Google Cloud Documentation — Deployment Manager Overview

**URL**: `https://cloud.google.com/deployment-manager/docs/fundamentals`

#### Deployment Manager Key Terms

- **Deployment**: A named collection of GCP resources defined and managed as a unit;
  creating, updating, and deleting a deployment affects all its resources together
- **Configuration file**: A YAML file listing resources with their types and properties;
  the primary input to Deployment Manager
- **Template**: A reusable Jinja2 or Python file that generates resource definitions;
  imported by configuration files and parameterized with `properties`
- **Type**: Specifies the GCP resource type, such as `compute.v1.instance` or
  `storage.v1.bucket`
- **Manifest**: An immutable record of a deployment at a specific point in time;
  Deployment Manager retains a manifest history for each deployment
- **Preview**: A dry-run mode that shows what changes will be made without applying them;
  enabled with `--preview` flag

#### Deployment Manager CLI Reference

| Command | Purpose |
|---|---|
| `gcloud deployment-manager deployments create NAME --config=FILE` | Create a new deployment |
| `gcloud deployment-manager deployments update NAME --config=FILE` | Update an existing deployment |
| `gcloud deployment-manager deployments update NAME --config=FILE --preview` | Preview changes before applying |
| `gcloud deployment-manager deployments cancel-preview NAME` | Revert a preview without applying |
| `gcloud deployment-manager deployments delete NAME` | Delete deployment and all its resources |
| `gcloud deployment-manager deployments describe NAME` | Show deployment status and resources |
| `gcloud deployment-manager deployments list` | List all deployments in the project |
| `gcloud deployment-manager manifests list --deployment=NAME` | List deployment history |

#### Deployment Manager ACE Exam Focus Points

- Deployment Manager manages resources as a unit — deleting a deployment deletes all
  its resources unless you explicitly exclude them
- The `$(ref.RESOURCE.PROPERTY)` syntax creates implicit dependencies; Deployment Manager
  creates referenced resources before dependents
- Jinja2 templates use `{{ properties["key"] }}` to access parameters passed from the
  configuration file
- Deployment Manager does not require a local state file — state is managed entirely
  by the GCP service
- Python templates are also supported but Jinja2 is more common in documentation

#### Deployment Manager Review Questions

1. What is the difference between a configuration file and a template in Deployment
   Manager?
2. What does the `--preview` flag do, and how do you apply or cancel a preview?
3. What happens to the resources in a deployment when you run `deployments delete`?

---

### Required Reading 2: Terraform with GCP Provider

**Source**: Terraform Documentation — Google Cloud Provider

**URL**: `https://registry.terraform.io/providers/hashicorp/google/latest/docs`

#### Terraform Key Terms

- **HCL (HashiCorp Configuration Language)**: The declarative language used to write
  Terraform configurations; human-readable JSON-compatible syntax
- **Provider**: A plugin that implements CRUD operations for a specific platform; the
  `google` provider manages GCP resources
- **Resource block**: The primary unit of a Terraform configuration; defines one GCP
  resource and its desired state
- **State file**: `terraform.tfstate` — a JSON file tracking every resource Terraform
  manages; must not be deleted or modified manually
- **Backend**: Configures where the state file is stored; local by default; GCS backend
  for team environments
- **Plan**: `terraform plan` output showing what will be created, updated, or destroyed;
  no changes are applied
- **Module**: A directory of `.tf` files that can be called from other configurations;
  supports parameterization via `variable` blocks

#### Terraform Workflow Steps

1. `terraform init` — downloads provider plugins and initializes the backend
2. `terraform validate` — checks configuration syntax without connecting to GCP
3. `terraform plan` — shows what changes will be made; compare to the state file
4. `terraform apply` — executes the plan; prompts for confirmation
5. `terraform destroy` — destroys all resources tracked in the state file

#### Terraform GCP Provider Authentication

Terraform authenticates to GCP using Application Default Credentials (ADC). In Cloud
Shell or on a GCE VM with the correct service account, ADC works automatically. For
local development:

```bash
# Authenticate using your user account
gcloud auth application-default login

# Or specify a service account key file
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

#### Terraform Remote State in GCS

```hcl
terraform {
  backend "gcs" {
    bucket  = "my-tf-state"
    prefix  = "env/prod"
  }
}
```

The GCS bucket must exist before running `terraform init`. Enable object versioning on
the bucket to allow state file rollback.

#### Terraform ACE Exam Focus Points

- Terraform state is the source of truth — if a resource is deleted outside of Terraform,
  the next `terraform plan` shows it as needing recreation
- `terraform import` brings existing resources under Terraform management; the resource
  block must be written manually after import
- The `google` provider version is pinned in the `terraform` block to prevent breaking
  changes from provider updates
- Remote state in GCS allows multiple team members to work with the same infrastructure
  without state conflicts
- `terraform plan` should always be reviewed before `terraform apply` in production

#### Terraform Review Questions

1. What is the purpose of the Terraform state file, and why should it never be deleted
   manually?
2. What are the five steps of the Terraform workflow in order?
3. What backend configuration stores Terraform state in Cloud Storage?

---

### Required Reading 3: Deployment Manager vs Terraform

**Source**: Google Cloud Blog — Choosing IaC Tools on GCP

#### Comparison Table

| Dimension | Cloud Deployment Manager | Terraform |
|---|---|---|
| Language | YAML + Jinja2 or Python | HCL |
| GCP scope | GCP only | Multi-cloud |
| State management | GCP-managed | Local or remote .tfstate file |
| Module ecosystem | Limited | Extensive (Terraform Registry) |
| Community size | Small | Very large |
| CI/CD integration | Via Cloud Build | Via Cloud Build, GitHub Actions, etc. |
| Drift detection | Via manifest comparison | Via `terraform plan` vs state |
| Exam coverage | ACE tested | ACE tested |

#### When to Use Each

Use Deployment Manager when:

- Your team is GCP-only and wants zero state file management
- You are working in an environment where third-party tools are restricted
- You need deep integration with GCP-specific APIs not yet in the Terraform provider

Use Terraform when:

- Your infrastructure spans multiple cloud providers
- You want access to the large Terraform module registry
- Your team prefers HCL over YAML
- You need advanced features like workspaces, moved blocks, and conditional resources

#### IaC Comparison ACE Exam Focus Points

- Both tools create GCP resources; the ACE exam tests whether you know the basic commands
  and concepts for each
- Deployment Manager is GCP-native and requires no state file management
- Terraform requires explicit state management; remote state is required for teams
- Neither tool locks you in — you can migrate between them if needed

---

### Required Reading 4: Infrastructure Versioning Patterns

**Source**: Google Cloud Architecture Center — Infrastructure as Code best practices

**URL**: `https://cloud.google.com/docs/terraform/best-practices-for-terraform`

#### Infrastructure Versioning Key Terms

- **GitOps**: The practice of using Git as the single source of truth for both
  application code and infrastructure; all changes go through pull requests
- **Branch protection**: Prevents direct commits to the main branch; all changes must
  go through reviewed pull requests
- **Environment isolation**: Separate state backends for dev, staging, and production
  to prevent accidental cross-environment changes
- **State locking**: Prevents two users or CI/CD pipelines from running `terraform apply`
  simultaneously; GCS backend supports locking via Cloud Storage object conditions

#### Infrastructure Versioning Best Practices

- Store all IaC configuration in a Git repository alongside application code or in a
  dedicated infrastructure repository
- Never apply Terraform from a local machine in production — always use CI/CD
- Run `terraform plan` as a required check on every pull request
- Tag the infrastructure repository at each production deployment (e.g., `prod-2024-01-15`)
- Use separate `.tfvars` files per environment rather than hardcoded values
- Enable state bucket versioning so corrupted state files can be rolled back

#### Infrastructure Versioning ACE Exam Focus Points

- The ACE exam does not test deep Git knowledge, but may ask about Deployment Manager
  update strategies (preview before apply) and Terraform state isolation patterns
- Multiple Terraform workspaces or separate state files per environment are both valid
  isolation patterns

---

### Pre-Lab Checklist

Before starting Lab 11, confirm you can answer yes to each item:

- I can write a Deployment Manager YAML configuration defining at least 2 resources
- I know the gcloud commands to create, update, describe, and delete a deployment
- I understand what `$(ref.RESOURCE.PROPERTY)` does in a Deployment Manager config
- I can describe the 5-step Terraform workflow
- I know how to configure a GCS backend for Terraform remote state

---

### Additional Resources

- Deployment Manager documentation:
  `https://cloud.google.com/deployment-manager/docs`
- Terraform GCP provider documentation:
  `https://registry.terraform.io/providers/hashicorp/google/latest/docs`
- Terraform best practices on GCP:
  `https://cloud.google.com/docs/terraform/best-practices-for-terraform`
- ACE exam guide:
  `https://cloud.google.com/certification/guides/cloud-engineer`
