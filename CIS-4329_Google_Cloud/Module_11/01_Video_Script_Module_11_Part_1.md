# Video Script: Module 11 — Infrastructure as Code on GCP (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 11. I am Professor Nash, and today we cover Infrastructure as Code
on GCP.

Infrastructure as Code, or IaC, is the practice of defining your cloud resources in
configuration files rather than creating them manually through the Console or CLI. IaC
enables repeatability, version control, peer review, and automated deployment of your
infrastructure — treating it the same way you treat application code.

GCP offers its own native IaC tool — Cloud Deployment Manager — and the industry-standard
third-party tool Terraform works fully with GCP. Both are tested on the ACE exam.

By the end of this two-part video you will understand both tools, write Deployment Manager
and Terraform configurations, deploy resources, and explain infrastructure versioning
patterns.

---

### Section 1: Why Infrastructure as Code

Without IaC, infrastructure is created manually and exists only as a running state. If a
VM is accidentally deleted or configuration drifts from the intended state, recreating it
requires remembering every setting.

With IaC:

- **Repeatability** — run the same configuration in dev, staging, and production and get
  identical infrastructure
- **Version control** — track every infrastructure change in Git with commit history
- **Code review** — require approval before applying changes to production
- **Disaster recovery** — recreate an entire environment from code in minutes
- **Documentation** — the configuration file IS the documentation

---

### Section 2: Cloud Deployment Manager

Cloud Deployment Manager is GCP's native IaC service. You define resources in YAML
(or Python/Jinja2 templates) and Deployment Manager creates and manages the resources
as a **deployment**.

Key concepts:

- **Deployment** — a named collection of GCP resources defined and managed together
- **Configuration file** — YAML file listing resource types and their properties
- **Template** — a reusable Jinja2 or Python module referenced by a configuration
- **Manifest** — a record of a specific deployed state; Deployment Manager maintains a
  history of manifests

#### Basic Configuration File Structure

```yaml
# config.yaml — deploys one VM and one firewall rule
resources:
  - name: my-vm
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
        - network: global/networks/default
          accessConfigs:
            - name: External NAT
              type: ONE_TO_ONE_NAT

  - name: allow-http
    type: compute.v1.firewall
    properties:
      network: global/networks/default
      targetTags:
        - http-server
      allowed:
        - IPProtocol: tcp
          ports:
            - "80"
```

#### Deployment Manager CLI Commands

```bash
# Create a new deployment
gcloud deployment-manager deployments create my-deployment \
  --config=config.yaml

# List all deployments
gcloud deployment-manager deployments list

# Describe a deployment (shows resources and their status)
gcloud deployment-manager deployments describe my-deployment

# Update an existing deployment (apply changes to config.yaml)
gcloud deployment-manager deployments update my-deployment \
  --config=config.yaml

# Preview changes before applying
gcloud deployment-manager deployments update my-deployment \
  --config=config.yaml \
  --preview

# Cancel a preview and revert to current state
gcloud deployment-manager deployments cancel-preview my-deployment

# Delete a deployment and all its resources
gcloud deployment-manager deployments delete my-deployment
```

---

### Section 3: Deployment Manager Templates

Templates enable reuse. A Jinja2 template accepts parameters and generates resource
definitions dynamically.

#### Jinja2 Template Example

```jinja2
{# vm_template.jinja #}
resources:
  - name: {{ properties["vmName"] }}
    type: compute.v1.instance
    properties:
      zone: {{ properties["zone"] }}
      machineType: zones/{{ properties["zone"] }}/machineTypes/{{ properties["machineType"] }}
      disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-11
      networkInterfaces:
        - network: global/networks/default
          accessConfigs:
            - name: External NAT
              type: ONE_TO_ONE_NAT
```

Referencing the template from a configuration:

```yaml
# config-with-template.yaml
imports:
  - path: vm_template.jinja

resources:
  - name: web-vm-1
    type: vm_template.jinja
    properties:
      vmName: web-vm-1
      zone: us-central1-a
      machineType: e2-micro

  - name: web-vm-2
    type: vm_template.jinja
    properties:
      vmName: web-vm-2
      zone: us-central1-b
      machineType: e2-micro
```

Templates allow you to create multiple similar resources without duplicating the full
resource definition — ideal for creating instance fleets with consistent configuration.

---

### Section 4: Deployment Manager Outputs and References

Deployment Manager supports cross-resource references and outputs.

```yaml
resources:
  - name: my-network
    type: compute.v1.network
    properties:
      autoCreateSubnetworks: false

  - name: my-subnet
    type: compute.v1.subnetwork
    properties:
      region: us-central1
      ipCidrRange: 10.0.0.0/24
      network: $(ref.my-network.selfLink)

outputs:
  - name: networkSelfLink
    value: $(ref.my-network.selfLink)
  - name: subnetSelfLink
    value: $(ref.my-subnet.selfLink)
```

The `$(ref.RESOURCE_NAME.PROPERTY)` syntax creates a dependency between resources.
Deployment Manager waits for `my-network` to be created before creating `my-subnet`.
Outputs can be retrieved after deployment:

```bash
gcloud deployment-manager deployments describe my-deployment \
  --format="value(outputs)"
```

---

### Closing — Part 1

In Part 1 we covered:

- The purpose and benefits of Infrastructure as Code
- Cloud Deployment Manager: configuration files, deployments, CLI commands
- Jinja2 templates for reusable resource definitions
- Cross-resource references and deployment outputs

In Part 2 we cover Terraform with the GCP provider, comparing it to Deployment Manager,
and walk through the Terraform workflow and infrastructure versioning patterns.

See you in Part 2.
