# Quiz: Module 11 — Infrastructure as Code on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A team wants to deploy a set of GCP resources defined in a YAML file and manage them as
a single unit. They want GCP to handle state management without maintaining a local state
file. Which GCP-native service supports this workflow?

- A) Terraform with GCS backend
- B) Cloud Deployment Manager
- C) Cloud Build with gcloud scripts
- D) Config Connector on GKE

Correct answer: B — Cloud Deployment Manager is GCP's native IaC service that accepts
YAML configuration files and manages the state of deployments within GCP itself. No local
state file is required. Terraform requires a state file (local or remote). Cloud Build
can run gcloud commands but is not an IaC framework. Config Connector manages GCP
resources via Kubernetes but is GKE-specific.

---

### Question 2

In a Cloud Deployment Manager configuration, one resource references another using
`$(ref.my-network.selfLink)`. What is the effect of this reference?

- A) It creates a DNS alias between the two resources
- B) It creates an implicit dependency so Deployment Manager creates the referenced
   resource first
- C) It copies the network configuration into the referencing resource
- D) It exports the value as a deployment output

Correct answer: B — The `$(ref.RESOURCE.PROPERTY)` syntax creates an implicit dependency
in Deployment Manager. Before creating the resource that contains the reference, GCP
first ensures the referenced resource is successfully created and retrieves its property
value. This guarantees correct resource creation order without explicit dependency
declarations.

---

### Question 3

You want to preview what changes a Deployment Manager update will make before applying
them to production. Which command accomplishes this?

- A) `gcloud deployment-manager deployments describe MY_DEPLOY`
- B) `gcloud deployment-manager deployments update MY_DEPLOY --config=config.yaml --preview`
- C) `gcloud deployment-manager deployments validate MY_DEPLOY --config=config.yaml`
- D) `gcloud deployment-manager deployments plan MY_DEPLOY --config=config.yaml`

Correct answer: B — The `--preview` flag on the `deployments update` command creates a
preview deployment that shows what will change without applying the changes. After
reviewing, you run `deployments update` again (without `--preview`) to apply, or run
`deployments cancel-preview` to revert. `--validate` and `--plan` are not valid flags
for this command.

---

### Question 4

A developer runs `terraform apply` and it completes successfully. Another team member
then manually deletes the GCE VM that Terraform created using the Cloud Console. What
will happen the next time the first developer runs `terraform plan`?

- A) Terraform will show no changes because it does not detect out-of-band deletions
- B) Terraform will show an error because the state file is corrupted
- C) Terraform will show that it plans to recreate the deleted VM to match the desired
   state
- D) Terraform will automatically recreate the VM without requiring an apply

Correct answer: C — Terraform's state file still shows the VM as existing, but the next
`terraform plan` refreshes the state by querying GCP and detects that the VM no longer
exists. Terraform then shows it as needing to be created. The actual recreation happens
on the next `terraform apply`. Terraform detects drift — it does not silently ignore
out-of-band changes.

---

### Question 5

A team stores Terraform state locally on developers' workstations. Two developers both
run `terraform apply` on the same production infrastructure at the same time. What is
the risk?

- A) Terraform will automatically merge the two plans
- B) The second apply will be rejected because the state file is read-only
- C) Both applies may succeed but produce corrupted or inconsistent state, causing
   infrastructure drift
- D) Terraform will create duplicate resources to satisfy both applies

Correct answer: C — Concurrent local applies with no state locking can result in state
file corruption or resource inconsistency if both developers are modifying overlapping
resources. The correct solution is remote state in Cloud Storage with state locking
enabled. Remote backends prevent concurrent applies by locking the state file during
an operation.

---

### Question 6

Where should Terraform remote state be stored for a GCP project, and what additional
configuration should be applied to the storage location to support state rollback?

- A) In a BigQuery table; enable BigQuery table snapshots
- B) In a Cloud Storage bucket; enable object versioning on the bucket
- C) In Cloud Firestore; enable point-in-time recovery
- D) In a Cloud SQL database; enable automated backups

Correct answer: B — The recommended remote backend for Terraform on GCP is Cloud Storage
(GCS). Object versioning on the bucket allows rolling back to a previous version of the
state file if the current state becomes corrupted. The Terraform GCS backend also supports
state locking to prevent concurrent applies.

---

### Question 7

A team has an existing GCE VM that was created manually before they adopted Terraform.
They want to bring this VM under Terraform management without destroying and recreating
it. Which Terraform command should they use?

- A) `terraform refresh`
- B) `terraform plan --import`
- C) `terraform import google_compute_instance.NAME projects/P/zones/Z/instances/VM`
- D) `terraform state add google_compute_instance.NAME`

Correct answer: C — `terraform import` imports an existing resource into the Terraform
state file. The resource block must already be written in the `.tf` configuration files
before importing. After import, `terraform plan` will show the current resource state
vs. the configuration and indicate any differences. `terraform refresh` updates state
from the real world but does not import new resources.

---

### Question 8

Which statement best describes the key difference between Cloud Deployment Manager and
Terraform regarding multi-cloud support?

- A) Deployment Manager supports AWS and Azure resources via plugins
- B) Terraform is GCP-only and requires separate tools for AWS and Azure
- C) Deployment Manager manages GCP resources only; Terraform supports multiple cloud
   providers through provider plugins
- D) Both tools support multi-cloud deployments equally

Correct answer: C — Deployment Manager is a GCP-native service that only manages GCP
resources. Terraform uses a provider model that supports hundreds of cloud platforms and
services. A single Terraform configuration can provision resources across GCP, AWS,
Azure, and third-party services simultaneously. This makes Terraform the preferred choice
for multi-cloud or hybrid cloud organizations.

---

### Question 9

A Jinja2 template for Deployment Manager uses `{{ properties["zone"] }}` in its resource
definition. How is this value provided when the template is used?

- A) Terraform passes it via the `.tfvars` file
- B) The template reads it from an environment variable at runtime
- C) The configuration file that imports the template passes it in the `properties` block
   of the resource using that template
- D) The value is defined inside the Jinja2 template itself and cannot be overridden

Correct answer: C — When a Deployment Manager configuration imports a Jinja2 template,
it passes parameters via the `properties` block in the resource definition. The template
accesses these via `{{ properties["key"] }}`. This allows the same template to create
resources with different configurations (different zones, machine types, names) from a
single reusable template file.

---

### Question 10

An organization wants infrastructure changes to require peer review before being applied
to production. Which practice supports this requirement?

- A) Using `terraform apply -auto-approve` in a CI/CD pipeline
- B) Storing all Terraform or Deployment Manager configurations in a Git repository and
   requiring pull request approval before merging to the main branch
- C) Running `terraform plan` locally before each apply
- D) Using separate GCP projects for development and production

Correct answer: B — Storing IaC configurations in Git and requiring pull request
approval before merging to the main branch implements a peer review gate for all
infrastructure changes. The CI/CD pipeline can run `terraform plan` on the PR to show
reviewers exactly what will change. This is the standard GitOps practice for infrastructure
change management. The other options do not enforce review before production changes.
