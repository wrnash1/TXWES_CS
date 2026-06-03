# Lab: Module 11 — Infrastructure as Code on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will use both Cloud Deployment Manager and Terraform to deploy GCP
infrastructure. You will create a VPC, subnet, firewall rule, and Compute Engine VM
using each tool, then compare the experience.

**Estimated time**: 75–90 minutes

**Cost estimate**: Under $1.00 USD if completed and cleaned up within the session

---

### Prerequisites

- A GCP project with billing enabled
- Cloud Shell (Terraform is pre-installed in Cloud Shell)
- Deployment Manager API and Compute Engine API enabled

```bash
gcloud services enable deploymentmanager.googleapis.com compute.googleapis.com
```

---

### Part 1: Cloud Deployment Manager

#### Task 1.1: Create the Configuration File

In Cloud Shell, create a new directory and configuration file:

```bash
mkdir ~/lab11-dm && cd ~/lab11-dm
```

Create `config.yaml` with the following content:

```yaml
resources:
  - name: lab11-network
    type: compute.v1.network
    properties:
      autoCreateSubnetworks: false

  - name: lab11-subnet
    type: compute.v1.subnetwork
    properties:
      region: us-central1
      ipCidrRange: 10.10.0.0/24
      network: $(ref.lab11-network.selfLink)

  - name: lab11-allow-ssh
    type: compute.v1.firewall
    properties:
      network: $(ref.lab11-network.selfLink)
      allowed:
        - IPProtocol: tcp
          ports:
            - "22"
      sourceRanges:
        - 35.235.240.0/20

  - name: lab11-vm
    type: compute.v1.instance
    properties:
      zone: us-central1-a
      machineType: zones/us-central1-a/machineTypes/e2-micro
      disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-11
      networkInterfaces:
        - subnetwork: $(ref.lab11-subnet.selfLink)
          accessConfigs:
            - name: External NAT
              type: ONE_TO_ONE_NAT

outputs:
  - name: vmSelfLink
    value: $(ref.lab11-vm.selfLink)
```

#### Task 1.2: Preview and Deploy

```bash
# Preview the deployment (no resources created yet)
gcloud deployment-manager deployments create lab11-dm-deploy \
  --config=config.yaml \
  --preview

# Inspect the preview
gcloud deployment-manager deployments describe lab11-dm-deploy

# Apply the deployment
gcloud deployment-manager deployments update lab11-dm-deploy

# Verify all resources were created
gcloud deployment-manager deployments describe lab11-dm-deploy
```

#### Task 1.3: Verify Resources

```bash
# Verify the VM was created
gcloud compute instances list --filter="name=lab11-vm"

# Verify the network was created
gcloud compute networks list --filter="name=lab11-network"

# View the deployment outputs
gcloud deployment-manager deployments describe lab11-dm-deploy \
  --format="value(outputs)"
```

#### Task 1.4: Update the Deployment

Modify `config.yaml` to change the VM machine type to `e2-small`:

Change the machineType line from:

```text
machineType: zones/us-central1-a/machineTypes/e2-micro
```

to:

```text
machineType: zones/us-central1-a/machineTypes/e2-small
```

Then preview and apply the update:

```bash
gcloud deployment-manager deployments update lab11-dm-deploy \
  --config=config.yaml \
  --preview

gcloud deployment-manager deployments update lab11-dm-deploy
```

---

### Part 2: Terraform

#### Task 2.1: Initialize a Terraform Project

```bash
mkdir ~/lab11-tf && cd ~/lab11-tf
```

Create `main.tf`:

```hcl
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
  region  = "us-central1"
}

variable "project_id" {
  description = "GCP project ID"
  type        = string
}

resource "google_compute_network" "tf_vpc" {
  name                    = "lab11-tf-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "tf_subnet" {
  name          = "lab11-tf-subnet"
  ip_cidr_range = "10.20.0.0/24"
  region        = "us-central1"
  network       = google_compute_network.tf_vpc.id
}

resource "google_compute_firewall" "tf_allow_ssh" {
  name    = "lab11-tf-allow-ssh"
  network = google_compute_network.tf_vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["35.235.240.0/20"]
}

resource "google_compute_instance" "tf_vm" {
  name         = "lab11-tf-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.tf_subnet.id
    access_config {}
  }
}

output "vm_name" {
  value = google_compute_instance.tf_vm.name
}

output "vm_external_ip" {
  value = google_compute_instance.tf_vm.network_interface[0].access_config[0].nat_ip
}
```

#### Task 2.2: Run the Terraform Workflow

```bash
# Initialize Terraform and download GCP provider
terraform init

# Validate configuration syntax
terraform validate

# Preview changes
terraform plan -var="project_id=YOUR_PROJECT_ID"

# Apply (creates all resources)
terraform apply -var="project_id=YOUR_PROJECT_ID"
# Type 'yes' when prompted

# View outputs
terraform output
```

#### Task 2.3: Modify and Re-Apply

Edit `main.tf` to add a label to the VM resource:

```hcl
resource "google_compute_instance" "tf_vm" {
  name         = "lab11-tf-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  labels = {
    environment = "lab"
    module      = "11"
  }

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.tf_subnet.id
    access_config {}
  }
}
```

Run plan and apply again to see how Terraform handles an in-place update:

```bash
terraform plan -var="project_id=YOUR_PROJECT_ID"
terraform apply -var="project_id=YOUR_PROJECT_ID"
```

Note whether Terraform recreated the VM or updated it in-place.

---

### Part 3: Reflection Questions

1. In the Deployment Manager configuration, you used `$(ref.lab11-subnet.selfLink)` to
   reference the subnet in the VM definition. What does this reference accomplish beyond
   providing the correct value?
2. Compare the Deployment Manager update experience to Terraform's. What information
   does `terraform plan` provide that `gcloud deployment-manager deployments update
   --preview` also provides?
3. After running `terraform apply`, a state file (`terraform.tfstate`) was created. What
   would happen if you deleted this file and ran `terraform apply` again?
4. Terraform showed whether the VM label change was an in-place update or required
   recreation. Why does this matter in a production environment?
5. Which tool would you choose for a new GCP-only project and why? Would your answer
   change if the project also used AWS resources?

---

### Part 4: Cleanup

```bash
# Terraform destroy
cd ~/lab11-tf
terraform destroy -var="project_id=YOUR_PROJECT_ID"
# Type 'yes' when prompted

# Deployment Manager delete
gcloud deployment-manager deployments delete lab11-dm-deploy --quiet
```

---

### Submission Checklist

- Deployment Manager config.yaml created with 4 resources
- Deployment previewed before applying
- All DM resources verified in the Console or CLI
- DM deployment updated with changed machine type
- Terraform project initialized and validated
- Terraform plan reviewed and apply completed
- Terraform label modification applied
- All 5 reflection questions answered
- Both deployments cleaned up

---

### Grading Rubric

| Task | Points |
|---|---|
| DM config created and deployed successfully | 20 |
| DM preview used before apply | 10 |
| DM update applied | 10 |
| Terraform init, plan, apply completed | 25 |
| Terraform modification applied | 10 |
| Reflection questions answered | 20 |
| Resources cleaned up | 5 |
| **Total** | **100** |
