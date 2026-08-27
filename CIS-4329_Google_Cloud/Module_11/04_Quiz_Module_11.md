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

---

### Question 11 (5 points)

A Terraform configuration references a module hosted in a Cloud Storage bucket at
`gs://my-tf-modules/network-module.zip`. After running `terraform init`, the module
is not downloaded. What is the most likely cause?

- A) Terraform does not support GCS as a module source
- B) The GCS backend is not configured before using module sources
- C) The user account running `terraform init` does not have Storage Object Viewer
   access on the bucket
- D) Module sources must be hosted in the Terraform Registry, not GCS

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Terraform supports GCS as a module source using the `gcs::` source prefix; this is a documented and supported pattern.
  - B) The GCS backend for remote state is a separate configuration from module sources; backend configuration does not need to be present for module downloads to work.
  - D) The Terraform Registry is one source option, but Terraform also supports GCS, GitHub, Bitbucket, and other HTTP sources; GCS is a valid module source.

---

### Question 12 (5 points)

You run `terraform destroy` on a production environment. After confirming, Terraform
reports that 3 resources were destroyed but 1 resource failed with a dependency error.
What is the correct next step?

- A) Run `terraform apply` to recreate the resources and then retry destroy
- B) Manually delete the failed resource in the GCP Console and then run `terraform
   state rm` for that resource
- C) Resolve the dependency that blocked deletion (e.g., detach or delete the
   dependent resource first), then re-run `terraform destroy`
- D) Run `terraform refresh` to sync state, which will automatically remove the
   failed resource

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Running `terraform apply` would attempt to recreate the three already-destroyed resources, expanding the problem rather than resolving the stuck deletion.
  - B) Manually deleting in the Console and running `terraform state rm` is a last resort workaround; the dependency error should be resolved through proper IaC means first, as manual deletion bypasses Terraform's lifecycle hooks.
  - D) `terraform refresh` updates the state file to reflect the current real-world state but does not delete resources or resolve dependency ordering issues.

---

### Question 13 (5 points)

In a Deployment Manager template, which file format allows the use of Python logic
(loops, conditionals) to generate resource configurations dynamically?

- A) YAML only — Deployment Manager does not support dynamic generation
- B) Jinja2 template (.jinja)
- C) Python template (.py)
- D) Both Jinja2 and Python templates support programmatic generation

- **Correct Answer:** D
- **Distractor Analysis:**
  - A) Deployment Manager supports both Jinja2 and Python templates precisely to enable dynamic, programmatic resource generation; pure YAML does not support logic but is the base configuration format.
  - B) Jinja2 templates support basic templating logic (loops, conditionals, variable substitution) but Python templates provide full Python scripting capability.
  - C) Python templates offer the most flexibility with full Python language support, but Jinja2 templates also support loops and conditionals — so Python is not the only dynamic option.

---

### Question 14 (5 points)

What does the `terraform state mv` command do?

- A) Moves the state file from local storage to a GCS remote backend
- B) Renames or moves a resource within the Terraform state file without
   destroying and recreating the infrastructure
- C) Migrates all resources from one GCP project to another
- D) Moves a Terraform module from one directory to another

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Moving state to a remote backend is accomplished by configuring a `backend` block in the Terraform configuration and running `terraform init -migrate-state`; `terraform state mv` is not the command for this.
  - C) Terraform does not have a built-in command to migrate deployed resources between GCP projects; that would require destroying in one project and applying in another.
  - D) Moving module directories is a filesystem operation unrelated to `terraform state mv`; after moving files, you would update the `source` path in the configuration.

---

### Question 15 (5 points)

A Deployment Manager deployment has 5 resources. You delete one resource from
the config.yaml and run `gcloud deployment-manager deployments update`. What
happens to the deleted resource?

- A) It remains in GCP because Deployment Manager only adds resources on update
- B) It is deleted from GCP because Deployment Manager reconciles the actual
   state with the declared configuration
- C) The update fails because you cannot remove resources from a running deployment
- D) The resource is moved to a pending deletion queue and deleted after 24 hours

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Deployment Manager is a declarative tool; it reconciles the actual deployment to match the configuration, which means resources removed from the config are deleted from GCP on the next update.
  - C) Removing resources from a Deployment Manager configuration is fully supported on update; the update will delete the removed resources.
  - D) Deployment Manager does not have a pending deletion queue; resource deletion happens synchronously during the update operation.

---

### Question 16 (5 points)

Which Terraform command validates the syntax and internal consistency of `.tf`
configuration files without connecting to any provider API?

- A) `terraform plan`
- B) `terraform validate`
- C) `terraform fmt`
- D) `terraform check`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `terraform plan` validates configuration syntax but also connects to the provider API to compare the desired state against actual infrastructure; it requires provider credentials and API access.
  - C) `terraform fmt` reformats `.tf` files to canonical style but does not validate configuration logic or resource attribute correctness.
  - D) `terraform check` is not a standard Terraform CLI command; there is a `check` block feature in Terraform 1.5+ for custom condition assertions, but the CLI command is `validate`.

---

### Question 17 (5 points)

A team wants to reuse the same Terraform configuration to deploy identical
infrastructure in both `us-central1` and `us-east1` without duplicating code.
Which Terraform feature enables this?

- A) `terraform workspace` to create separate state workspaces per region
- B) Input variables for the region combined with calling the root module twice
   with different variable values
- C) Terraform modules — define the infrastructure once in a module and call it
   twice with different region variables
- D) Terraform providers — configure two Google providers with different regions

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Workspaces create isolated state environments but do not eliminate code duplication on their own; you still need parameterization to deploy to different regions from the same code.
  - B) You cannot call the root module twice within itself; modules are the mechanism for reusable infrastructure components.
  - D) Configuring two provider aliases is part of the implementation, but the module pattern is the primary code-reuse mechanism; provider aliases alone do not eliminate the need to duplicate resource definitions.

---

### Question 18 (5 points)

What happens to existing GCP resources if you run `terraform import` for a resource
that already has a matching block in your `.tf` configuration?

- A) Terraform overwrites the resource with the values in the configuration file
- B) The resource's current real-world state is added to the Terraform state file;
   the configuration is not applied or changed
- C) Terraform deletes the resource and recreates it from the configuration
- D) The import fails because the resource block already exists in the configuration

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `terraform import` only adds the resource to the state file; it does not modify the real GCP resource to match the configuration. Any configuration drift is visible on the next `terraform plan`.
  - C) `terraform import` never destroys or recreates resources; it is a read operation that records existing infrastructure in Terraform state.
  - D) A matching resource block in the configuration is required for `terraform import` to work; the import fails if there is NO block for the resource, not if there is one.

---

### Question 19 (5 points)

A Deployment Manager configuration uses a template to create a firewall rule.
The template needs to reference the network name from another resource in the
same deployment. What is the correct syntax to reference the `selfLink` property
of a resource named `my-vpc`?

- A) `{{ my-vpc.selfLink }}`
- B) `$(ref.my-vpc.selfLink)`
- C) `${google_compute_network.my-vpc.self_link}`
- D) `$(my-vpc.selfLink)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `{{ ... }}` is Jinja2 template variable syntax for accessing `properties` values; it does not resolve runtime resource references like `selfLink` from deployed resources.
  - C) `${google_compute_network.my-vpc.self_link}` is Terraform HCL interpolation syntax, not Deployment Manager syntax.
  - D) `$(my-vpc.selfLink)` is missing the `ref.` keyword; the full syntax requires `ref.RESOURCE_NAME.PROPERTY` inside the `$()` reference notation.

---

### Question 20 (5 points)

Your team uses Terraform for GCP infrastructure. After a Terraform apply, a junior
engineer changes a firewall rule manually in the Console. The next day, another
team member runs `terraform apply` with no configuration changes. What will Terraform
do?

- A) Terraform will do nothing because the configuration has not changed
- B) Terraform will detect the manual change and revert the firewall rule to match
   the configuration
- C) Terraform will fail with an error because the state and real-world are out of sync
- D) Terraform will prompt the user to choose between keeping the manual change or
   reverting to the configuration

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Terraform runs a refresh during `terraform apply` to compare the real-world state against both the state file and the configuration; it detects the drift and plans a corrective change.
  - C) Terraform handles state drift gracefully; it does not fail with an error. It shows the drift in the plan and applies a correction.
  - D) Terraform does not interactively prompt the user to choose between the manual change and the configuration; it always converges toward the declared configuration, treating the configuration as the source of truth.
