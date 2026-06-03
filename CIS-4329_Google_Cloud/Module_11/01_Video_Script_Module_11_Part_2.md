# Video Script: Module 11 — Infrastructure as Code on GCP (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction to Part 2

Welcome back. In Part 1 we covered Cloud Deployment Manager. In Part 2 we cover
Terraform — the industry-standard IaC tool — with the GCP provider. We also compare
Deployment Manager to Terraform and discuss infrastructure versioning patterns.

---

### Section 1: Terraform Overview

Terraform is an open-source IaC tool created by HashiCorp. It uses its own
declarative configuration language called HCL (HashiCorp Configuration Language). Unlike
Deployment Manager (which is GCP-specific), Terraform supports hundreds of providers
including AWS, Azure, and GCP — making it the standard choice for multi-cloud teams.

Key concepts:

- **Provider** — a plugin that knows how to create resources on a platform (e.g.,
  `google` provider for GCP)
- **Resource** — a block defining one GCP resource to create
- **State file** — a JSON file (`terraform.tfstate`) tracking what Terraform has created;
  the source of truth for the current deployed state
- **Module** — a reusable collection of resource definitions; supports parameterization
- **Plan** — a preview of what changes Terraform will make
- **Apply** — executes the plan and creates/updates/destroys resources

---

### Section 2: Terraform with the GCP Provider

#### Provider Configuration

```hcl
# main.tf — provider block
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}
```

#### Variables

```hcl
# variables.tf
variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "Default GCP region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "Default GCP zone"
  type        = string
  default     = "us-central1-a"
}
```

#### Resource Definitions

```hcl
# compute.tf — create a VPC, subnet, and VM
resource "google_compute_network" "vpc" {
  name                    = "my-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "my-subnet"
  ip_cidr_range = "10.0.0.0/24"
  region        = var.region
  network       = google_compute_network.vpc.id
}

resource "google_compute_instance" "web_vm" {
  name         = "web-vm"
  machine_type = "e2-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet.id
    access_config {}
  }

  tags = ["http-server"]
}

resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server"]
}
```

#### Outputs

```hcl
# outputs.tf
output "vm_external_ip" {
  description = "External IP of the web VM"
  value       = google_compute_instance.web_vm.network_interface[0].access_config[0].nat_ip
}

output "vpc_id" {
  description = "VPC network ID"
  value       = google_compute_network.vpc.id
}
```

---

### Section 3: The Terraform Workflow

Terraform follows a four-step workflow:

```bash
# Step 1: Initialize — download provider plugins
terraform init

# Step 2: Plan — preview changes (no resources modified)
terraform plan -var="project_id=MY_PROJECT_ID"

# Step 3: Apply — create/update resources
terraform apply -var="project_id=MY_PROJECT_ID"
# Type "yes" when prompted, or use -auto-approve for automation

# Step 4: Destroy — tear down all resources in the configuration
terraform destroy -var="project_id=MY_PROJECT_ID"
```

#### State Management

The state file tracks every resource Terraform manages. For team environments, store
state remotely to avoid conflicts:

```hcl
# backend.tf — remote state in Cloud Storage
terraform {
  backend "gcs" {
    bucket  = "my-terraform-state-bucket"
    prefix  = "prod/terraform.tfstate"
  }
}
```

```bash
# Create the GCS bucket for state before initializing
gsutil mb gs://my-terraform-state-bucket/
gsutil versioning set on gs://my-terraform-state-bucket/

# Initialize with remote backend
terraform init
```

Enabling versioning on the state bucket allows rollback if a state file is corrupted.

---

### Section 4: Terraform Import and Drift Detection

If existing GCP resources were created manually, you can import them into Terraform state:

```bash
# Import an existing GCE instance into Terraform state
terraform import google_compute_instance.web_vm \
  projects/MY_PROJECT/zones/us-central1-a/instances/existing-vm
```

After importing, you must write the matching `resource` block in your `.tf` files. The
state now tracks the resource and future `terraform plan` will show any drift between
the configuration and the actual resource state.

---

### Section 5: Deployment Manager vs Terraform

Both tools accomplish Infrastructure as Code on GCP. Here is how they compare:

| Factor | Deployment Manager | Terraform |
|---|---|---|
| Scope | GCP only | Multi-cloud (GCP, AWS, Azure, others) |
| Language | YAML + Jinja2/Python | HCL |
| State management | GCP-managed (no state file) | Local or remote state file required |
| Ecosystem | GCP native | Massive open-source module registry |
| ACE exam coverage | Tested | Tested |
| Industry adoption | Declining | Very high |

For the ACE exam, know both tools. In real-world projects, Terraform is the dominant
choice for new IaC initiatives.

---

### Section 6: Infrastructure Versioning Patterns

IaC without version control misses the key benefit of treating infrastructure like code.
Best practices:

- **Git repository** — all `.tf` or `.yaml` files in version control; never apply from
  uncommitted changes
- **Branch per environment** — or separate state backends per environment
  (`dev/terraform.tfstate`, `staging/terraform.tfstate`, `prod/terraform.tfstate`)
- **Pull request review** — require PR approval before merging infrastructure changes
  to the main branch
- **Terraform plan in CI** — run `terraform plan` automatically on every PR to show
  reviewers what will change
- **Tag releases** — tag your infrastructure repo at each production deployment for
  traceability
- **State locking** — Cloud Storage backend with Terraform supports state locking via
  a Cloud Firestore or Cloud Storage lock mechanism to prevent concurrent applies

---

### Module 11 Summary

Module 11 covered Infrastructure as Code on GCP:

- **Cloud Deployment Manager** — GCP-native IaC using YAML and Jinja2; deployments,
  templates, outputs, cross-resource references; fully managed state
- **Terraform** — multi-cloud IaC with HCL; providers, resources, variables, outputs;
  init/plan/apply/destroy workflow; remote state in Cloud Storage
- **Infrastructure versioning** — Git for IaC, PR review, branch-per-environment,
  `terraform plan` in CI/CD

For the ACE exam: know the Deployment Manager CLI commands (`create`, `update`,
`delete`, `describe`) and understand Terraform's state-based model and remote state
configuration in GCS.

Complete the lab, take the quiz, and join the discussion. Module 12 covers BigQuery
and data analytics on GCP.
