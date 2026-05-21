# Quiz: Module 13 – Cloud Deployment Manager and Terraform on GCP
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your team wants to provision a set of GCP resources (a VPC network, a Compute Engine VM, and a Cloud Storage bucket) in a repeatable way so that the exact same environment can be created in dev, staging, and production projects. Changes should be tracked in source control and peer-reviewed before being applied. Which approach best implements this requirement?

A) Document the `gcloud` commands in a runbook and have an administrator execute them manually for each environment.
B) Use Cloud Console to create the resources, then export the project configuration using `gcloud projects export`.
C) Write Infrastructure as Code configuration files (using Terraform or Deployment Manager), commit them to a Git repository, and apply them per environment using the appropriate project flags.
D) Create a Cloud Scheduler job that runs `gcloud` commands on a schedule to recreate the environment resources each week.

*   **Correct Answer:** C) Write Infrastructure as Code configuration files (using Terraform or Deployment Manager), commit them to a Git repository, and apply them per environment using the appropriate project flags.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A manual runbook is error-prone and cannot guarantee identical environments across dev, staging, and production. It also does not provide version control, change history, or peer review of infrastructure changes — the core benefits of IaC.
    *   *Why B is incorrect:* `gcloud projects export` does not exist as a single command that produces a complete IaC-compatible configuration. Cloud Console resource creation is manual and does not produce version-controlled, reusable configuration files.
    *   *Why D is incorrect:* Recreating resources on a schedule would cause data loss by deleting and replacing existing resources, and it would not track configuration changes over time. Scheduled recreation is not an IaC pattern.

---

**Question 2**
A Terraform engineer runs `terraform plan` and sees the following in the output for an existing Cloud Storage bucket:

```
~ resource "google_storage_bucket" "logs" {
    ~ storage_class = "STANDARD" -> "NEARLINE"
}
```

What does this output indicate, and what happens when `terraform apply` is executed?

A) The bucket will be destroyed and recreated in NEARLINE storage class, causing data loss.
B) Terraform has detected a drift between the desired state (NEARLINE) and the recorded state (STANDARD); applying will update the bucket's storage class in place without destroying it.
C) The plan output shows an error — Terraform cannot modify storage class on an existing bucket and the apply will fail.
D) The `~` symbol means Terraform will skip this resource because no action is required.

*   **Correct Answer:** B) Terraform has detected a drift between the desired state (NEARLINE) and the recorded state (STANDARD); applying will update the bucket's storage class in place without destroying it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The `~` symbol in Terraform plan output means the resource will be updated in place. Resources that must be destroyed and recreated are shown with `-/+` (destroy then create). Cloud Storage bucket storage class changes are applied in place without destroying the bucket or its data.
    *   *Why C is incorrect:* Cloud Storage bucket storage class is a mutable property — it can be changed without recreating the bucket. Terraform's GCP provider supports this in-place update, so the apply will succeed.
    *   *Why D is incorrect:* The `~` symbol means the resource will be modified. A `+` means create, `-` means destroy, and no symbol (or `=`) means no change. Skipped resources would show no entry at all in the plan output.

---

**Question 3**
Your team uses Terraform to manage GCP infrastructure. A team member manually deleted a Cloud SQL instance from the Cloud Console, but the Terraform configuration and state file still reference it. When another team member runs `terraform plan`, what output does Terraform show for the deleted instance, and what does `terraform apply` do?

A) Terraform detects no change because the state file is the source of truth and the manual deletion is ignored.
B) Terraform shows the instance as needing to be created (`+`) because it exists in the desired configuration but no longer exists in GCP; applying will recreate it.
C) Terraform shows the instance as needing to be destroyed (`-`) because the state file is out of sync; applying will remove it from the state file.
D) Terraform automatically updates the state file to reflect the manual deletion and shows no planned changes.

*   **Correct Answer:** B) Terraform shows the instance as needing to be created (`+`) because it exists in the desired configuration but no longer exists in GCP; applying will recreate it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Terraform compares the state file against the actual GCP resources (by calling the GCP API) during `terraform plan` — it does not blindly trust the state file. When the instance is found to be missing in GCP, Terraform marks it for recreation.
    *   *Why C is incorrect:* Terraform's goal is to make GCP match the desired configuration (the `.tf` files), not to match the current GCP state. Since the instance is in the `.tf` files, Terraform plans to create it — not remove it from state.
    *   *Why D is incorrect:* Terraform does not automatically rewrite the state file to reflect manual changes detected during `plan`. You must explicitly run `terraform refresh` or `terraform state rm` to update the state file for manually deleted resources.

---

**Question 4**
Your organization wants to enforce that all Terraform state files for GCP projects are stored in a shared Cloud Storage bucket so that the entire infrastructure team can collaborate without state file conflicts. Which Terraform configuration block implements remote state storage in Cloud Storage?

A) Add a `remote_state` block in `main.tf` pointing to the Cloud Storage bucket path.
B) Configure a `backend "gcs"` block in the Terraform configuration specifying the bucket name and prefix, then run `terraform init` to migrate state.
C) Set the `TF_STATE_BUCKET` environment variable to the Cloud Storage bucket name before running `terraform apply`.
D) Run `gcloud storage cp terraform.tfstate gs://my-state-bucket/` after each `terraform apply` to manually sync the state file.

*   **Correct Answer:** B) Configure a `backend "gcs"` block in the Terraform configuration specifying the bucket name and prefix, then run `terraform init` to migrate state.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* There is no `remote_state` configuration block in Terraform. The `terraform_remote_state` data source reads outputs from another state file — it does not configure where Terraform stores its own state. The `backend` block is the correct configuration for state storage location.
    *   *Why C is incorrect:* `TF_STATE_BUCKET` is not a recognized Terraform environment variable. Terraform backend configuration is done in the `terraform` block of the configuration files, not through environment variables (though `TF_BACKEND_*` variables exist for some backends, the correct pattern is the `backend` block).
    *   *Why D is incorrect:* Manually copying the state file after each apply creates a race condition in team environments — if two engineers run `apply` simultaneously, one overwrites the other's state changes. The `backend "gcs"` configuration provides native locking via Cloud Storage object versioning to prevent this.

---

**Question 5**
A Cloud Deployment Manager configuration deploys a Compute Engine VM. After the initial deployment, a team member updates the configuration YAML to change the machine type from `n1-standard-2` to `n1-standard-4`. They then run `gcloud deployment-manager deployments update my-deployment --config=config.yaml`. What is the expected behavior?

A) Deployment Manager rejects the update because machine type is an immutable property and requires a new deployment.
B) Deployment Manager compares the updated configuration against the existing deployment, stops the VM, changes its machine type to `n1-standard-4`, and restarts it — all within the same deployment.
C) Deployment Manager deletes the entire deployment and all its resources, then recreates everything from scratch with the new configuration.
C) Deployment Manager creates a second VM with the new machine type alongside the existing VM, then waits for manual confirmation before deleting the old one.

*   **Correct Answer:** B) Deployment Manager compares the updated configuration against the existing deployment, stops the VM, changes its machine type to `n1-standard-4`, and restarts it — all within the same deployment.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Machine type on a Compute Engine VM can be changed while the VM is stopped — it is not an immutable property. Deployment Manager supports in-place updates to many VM properties by stopping and restarting the instance as part of the update operation.
    *   *Why C (first) is incorrect:* Deployment Manager's `update` command performs an incremental update — it only modifies resources whose configuration has changed. It does not delete and recreate the entire deployment unless the changed property requires resource replacement.
    *   *Why C (second) is incorrect:* Deployment Manager does not perform blue/green VM swaps or require manual confirmation during updates. It directly updates the existing resource according to the new configuration in a single atomic operation.
