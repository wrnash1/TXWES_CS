# Quiz: Module 13 - Terraform Cloud & the Public Registry

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Where do plan and apply operations execute when a Terraform configuration is connected to a VCS-backed Terraform Cloud workspace?

* A) On the developer's local machine, with results uploaded to Terraform Cloud
* B) In Terraform Cloud's remote execution environment, with state stored securely in Terraform Cloud
* C) On a GitHub Actions runner hosted by the repository owner
* D) On the target cloud provider's compute instances directly
* **Correct Answer:** B) Terraform Cloud acts as a remote execution environment. When a VCS push triggers a run, Terraform Cloud clones the repository, downloads providers, runs `terraform plan` and (after approval) `terraform apply` on its own managed runners, and stores state securely.
* **Distractor Analysis:**
  * *Why B is correct:* This is the fundamental operational model of VCS-connected Terraform Cloud workspaces. Remote execution frees developers from needing local credentials or CLI access for routine deployments and centralizes audit history in Terraform Cloud.
  * *Why A is incorrect:* In a VCS-connected Terraform Cloud workspace, local execution is not involved. The developer pushes code; Terraform Cloud handles all execution. Local execution is only used in the `local` operations mode, which is a separate, opt-in configuration.
  * *Why C is incorrect:* GitHub Actions runners are part of GitHub's CI/CD system. While Terraform can be run inside GitHub Actions workflows, that is a separate pattern from Terraform Cloud's native VCS integration, which uses Terraform Cloud's own runners.
  * *Why D is incorrect:* Cloud provider compute instances (e.g., EC2) are the target of Terraform provisioning, not the execution environment. Terraform Cloud's runners interact with provider APIs to provision resources on those platforms.

---

**Question 2**
Which of the following most accurately describes a **Terraform Cloud workspace**?

* A) A named state-isolation container within a single root module that shares the same backend configuration as all other workspaces in that module
* B) An independent managed environment in Terraform Cloud with its own state file, run history, variable set, and optional VCS connection — typically corresponding to one root module or environment
* C) A Git branch within a connected VCS repository that Terraform Cloud monitors for changes to trigger automated deployments
* D) A reusable HCL module stored in the private registry that can be sourced by multiple Terraform configurations across an organization
* **Correct Answer:** B) A Terraform Cloud workspace is a fully independent unit of infrastructure management — it has its own state, variables, run history, and access controls, and can be connected to a specific directory and branch in a VCS repository.
* **Distractor Analysis:**
  * *Why B is correct:* This is the exam-critical distinction between Terraform Cloud workspaces and CLI workspaces. Terraform Cloud workspaces are independent projects, not just state partitions of a shared configuration. Each can have completely different providers, configurations, and credentials.
  * *Why A is incorrect:* This describes a CLI workspace (`terraform workspace new`), not a Terraform Cloud workspace. CLI workspaces share the same root module directory and backend configuration; Terraform Cloud workspaces do not.
  * *Why C is incorrect:* A Git branch is a VCS concept. While a Terraform Cloud workspace can be configured to track a specific branch, the workspace itself is not the branch — it is the Terraform Cloud environment that monitors the branch.
  * *Why D is incorrect:* This describes a module in the private registry. A workspace and a module are distinct concepts — workspaces run infrastructure deployments; modules are reusable configuration components sourced by workspaces.

---

**Question 3**
A team opens a pull request in a GitHub repository connected to a Terraform Cloud workspace. What type of run does Terraform Cloud automatically trigger?

* A) A full apply run that immediately provisions any infrastructure changes in the pull request
* B) A speculative plan — a read-only plan whose output is posted as a pull request status check, which cannot be applied
* C) A destroy run that removes all resources to prepare a clean environment for the pull request changes
* D) A `terraform validate` run that checks HCL syntax but does not evaluate provider APIs or compute a resource diff
* **Correct Answer:** B) Pull requests trigger a speculative plan in Terraform Cloud. The plan output is posted as a status check on the pull request so reviewers can see the infrastructure impact before merging. Speculative plans are read-only and cannot be applied.
* **Distractor Analysis:**
  * *Why B is correct:* Speculative plans are a core Terraform Cloud feature designed for code review workflows. They give reviewers infrastructure change visibility at the PR stage without risking accidental applies. The exam tests that speculative plans are non-applicable and do not lock state.
  * *Why A is incorrect:* Terraform Cloud does not apply infrastructure changes automatically on pull requests. An apply only occurs after a merge to the tracked branch and, by default, after a human operator approves the plan in the Terraform Cloud UI.
  * *Why C is incorrect:* Terraform Cloud never runs a destroy operation automatically on a pull request. Destroy runs must be manually triggered and confirmed by a workspace administrator.
  * *Why D is incorrect:* While `terraform validate` checks configuration syntax, Terraform Cloud's PR integration runs a full speculative plan — which includes provider API calls to refresh state and compute a resource diff — not just a syntax check.

---

**Question 4**
An organization wants to share a set of internal Terraform modules across multiple teams without publishing them to the public Terraform Registry. Which Terraform Cloud feature supports this requirement?

* A) Run triggers — link workspaces so that modules in one workspace are automatically available to downstream workspaces
* B) The private registry — publish internal modules to an organization-scoped registry accessible only to authenticated members
* C) Sentinel policies — write policy-as-code rules that enforce module usage standards across all workspaces in the organization
* D) Variable sets — define module source paths as organization-wide variables that all workspace configurations can reference
* **Correct Answer:** B) The Terraform Cloud private registry allows organizations to publish versioned modules internally. Modules are sourced using the `<hostname>/<organization>/<module>/<provider>` format and are only accessible to members of that Terraform Cloud organization.
* **Distractor Analysis:**
  * *Why B is correct:* This is precisely the purpose of the private registry. It mirrors the public registry's versioning and documentation interface but gates access to the organization. Teams source private registry modules the same way they source public ones — with a `source` argument in the `module` block.
  * *Why A is incorrect:* Run triggers connect workspace execution chains; they have nothing to do with module sharing. A run trigger causes one workspace's completed apply to queue a run in another workspace — it does not make module code available between workspaces.
  * *Why C is incorrect:* Sentinel policies enforce compliance rules (e.g., "all resources must have a cost estimate below $X") but do not provide a mechanism for publishing or sharing module source code across teams.
  * *Why D is incorrect:* Variable sets distribute Terraform input variables and environment variables to workspaces. They cannot distribute HCL module source code or make a module's resource blocks available to other configurations.

---

**Question 5**
Which block syntax, introduced in Terraform 1.1, is the recommended way to configure Terraform Cloud as the backend instead of the legacy `backend "remote"` block?

* A) The `remote` block nested inside the `terraform {}` block, specifying `organization` and `workspaces` arguments
* B) The `cloud` block nested inside the `terraform {}` block, specifying `organization` and `workspaces` arguments
* C) The `terraform_cloud` block at the root level of the configuration, referencing the organization token and workspace name
* D) The `backend "cloud"` block inside the `terraform {}` block, using the same syntax as other backend types
* **Correct Answer:** B) The `cloud` block nested inside `terraform {}` is the recommended Terraform Cloud integration method introduced in Terraform 1.1. It supports tag-based workspace filtering and provides a cleaner experience than the legacy `backend "remote"` block.
* **Distractor Analysis:**
  * *Why B is correct:* The `cloud` block is documented as the preferred replacement for `backend "remote"` for Terraform Cloud configurations. It accepts `organization`, `hostname` (optional, defaults to `app.terraform.io`), and a `workspaces` block with either a `name` or `tags` argument for workspace targeting.
  * *Why A is incorrect:* There is no standalone `remote` block in Terraform configuration. The legacy approach used `backend "remote"` inside `terraform {}`, not a `remote` block.
  * *Why C is incorrect:* `terraform_cloud` is not a valid Terraform block type. Terraform configuration blocks are `terraform`, `provider`, `resource`, `data`, `variable`, `output`, `locals`, and `module` — there is no `terraform_cloud` block.
  * *Why D is incorrect:* There is no `backend "cloud"` type. The Terraform Cloud integration uses either the `cloud` block (recommended) or `backend "remote"` (legacy) — neither uses `backend "cloud"` as its type name.
