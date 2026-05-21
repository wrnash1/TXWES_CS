# Quiz: Module 11 - Workspaces & Multi-Environment Management

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which built-in Terraform expression returns the name of the currently active workspace?

* A) `var.workspace`
* B) `terraform.workspace`
* C) `local.workspace`
* D) `env.workspace`
* **Correct Answer:** B) `terraform.workspace` is a built-in string expression that evaluates to the name of the currently selected workspace (e.g., `"dev"`, `"prod"`, or `"default"`).
* **Distractor Analysis:**
  * *Why B is correct:* `terraform.workspace` is a reserved, built-in reference — not a variable, local, or custom attribute. It is the only supported way to dynamically reference the active workspace name inside HCL resource arguments.
  * *Why A is incorrect:* `var.workspace` would reference a user-defined input variable named `workspace`. No such variable exists automatically; it would not reflect the active workspace unless the user manually passed a matching value.
  * *Why C is incorrect:* `local.workspace` would reference a user-defined local value. Like `var.workspace`, it does not automatically track the active workspace.
  * *Why D is incorrect:* `env.workspace` is not a valid Terraform expression. Terraform does not have an `env` built-in object.

---

**Question 2**
Which of the following most accurately describes **workspace isolation** in Terraform?

* A) A mechanism that encrypts the state file so that only users with the correct KMS key can read resource attributes
* B) The guarantee that each named workspace maintains a completely separate state file, so resources provisioned in one workspace do not appear in or conflict with another workspace's state
* C) A policy that prevents Terraform from running `apply` commands until a peer-review approval is granted in Terraform Cloud
* D) A feature that automatically splits a single large state file into multiple smaller shards to improve performance on configurations with thousands of resources
* **Correct Answer:** B) Workspace isolation means each workspace has its own independent state, so a `terraform apply` in the `dev` workspace creates, updates, or destroys only resources tracked in the `dev` state file without touching `prod` state.
* **Distractor Analysis:**
  * *Why B is correct:* This is the core purpose of workspaces. Isolation is achieved by storing each workspace's state separately — under `terraform.tfstate.d/<name>/` for local backends. It is the defining characteristic that makes workspaces useful for multi-environment workflows.
  * *Why A is incorrect:* State encryption is a backend security feature (e.g., `encrypt = true` in the S3 backend) and is unrelated to workspace isolation. Encryption controls who can read state, not which resources belong to which environment.
  * *Why C is incorrect:* Peer-review approval gates are a Terraform Cloud run workflow feature, not a workspace isolation concept. They are independent of how state files are separated.
  * *Why D is incorrect:* Terraform does not shard state files. Large configurations are managed by organizing resources into smaller root modules, not by splitting a single state file.

---

**Question 3**
A Terraform engineer runs `terraform workspace new staging` and then `terraform apply`. Where does Terraform store the resulting state file when using the local backend?

* A) Overwrites the existing `terraform.tfstate` file in the working directory
* B) Creates `terraform.tfstate.d/staging/terraform.tfstate` relative to the working directory
* C) Creates `staging/terraform.tfstate` in the directory where `terraform init` was last run
* D) Uploads the state to a remote backend automatically, regardless of backend configuration
* **Correct Answer:** B) When using the local backend, named workspace state files are stored under `terraform.tfstate.d/<workspace-name>/terraform.tfstate`. The `default` workspace continues to use the root `terraform.tfstate` file.
* **Distractor Analysis:**
  * *Why B is correct:* This is the documented local backend workspace state path. Knowing the `terraform.tfstate.d/` directory structure is a testable exam detail that demonstrates understanding of how workspace isolation is implemented on disk.
  * *Why A is incorrect:* Overwriting the root `terraform.tfstate` would destroy the `default` workspace state. Terraform avoids this by using a separate subdirectory for named workspaces.
  * *Why C is incorrect:* `staging/terraform.tfstate` is not a path Terraform creates. The `terraform.tfstate.d/` prefix is required; a bare workspace-name directory is not used.
  * *Why D is incorrect:* Terraform only uses a remote backend if one is explicitly configured in the `terraform {}` block. Creating a workspace does not trigger automatic remote state upload.

---

**Question 4**
A team wants to deploy the same Terraform configuration to three different AWS accounts — one for dev, one for staging, and one for prod — each with different IAM credentials. Should they use Terraform workspaces or separate root module directories?

* A) Use workspaces — they can pass different `provider` blocks to each workspace using the `workspace` meta-argument
* B) Use workspaces — the `terraform.workspace` expression can switch AWS credentials automatically inside the provider block
* C) Use separate root module directories — workspaces share the same provider configuration and cannot natively target different AWS accounts or regions per workspace
* D) Use workspaces — Terraform Cloud automatically maps each workspace to a separate AWS account when the workspace name matches the account alias
* **Correct Answer:** C) Workspaces share a single provider configuration block. There is no built-in mechanism to point different workspaces at different AWS accounts without fragile workarounds. Separate root modules with independent backend and provider configurations are the recommended pattern for cross-account deployments.
* **Distractor Analysis:**
  * *Why C is correct:* The HashiCorp documentation explicitly states workspaces are not suitable when each environment requires different provider credentials or backend configurations. Separate directories with independent `provider` and `backend` blocks cleanly support different AWS accounts per environment.
  * *Why A is incorrect:* There is no `workspace` meta-argument on provider blocks. Provider configurations cannot be conditionally routed per workspace without complex variable injection.
  * *Why B is incorrect:* While `terraform.workspace` can be interpolated into string arguments, the AWS provider's credential arguments still come from a shared provider block. Injecting completely separate credentials per workspace requires external tooling, not native Terraform syntax.
  * *Why D is incorrect:* Terraform Cloud does not automatically map workspace names to AWS account aliases. Credentials in Terraform Cloud are configured per workspace as variable sets — a manual configuration, not an automatic workspace behavior.

---

**Question 5**
When designing a multi-environment Terraform workflow using workspaces, which of the following practices best prevents accidental destruction of production resources?

* A) Use `terraform plan -out=plan.tfplan` and review the plan file before running `terraform apply plan.tfplan` in the production workspace
* B) Delete the `prod` workspace after each deployment so it cannot be accidentally targeted
* C) Always run `terraform destroy` before `terraform apply` to ensure a clean state in the production workspace
* D) Store production state in the `default` workspace since the default workspace cannot be deleted
* **Correct Answer:** A) Saving the plan output with `-out` and reviewing it before applying is the standard safety practice for production workspaces. It ensures the operator sees exactly what will change before any infrastructure is modified.
* **Distractor Analysis:**
  * *Why A is correct:* `terraform plan -out=plan.tfplan` serializes the execution plan to a binary file. Running `terraform apply plan.tfplan` executes only that saved plan with no re-evaluation. This guarantees the apply matches the reviewed plan and is the HashiCorp-recommended practice for production automation.
  * *Why B is incorrect:* Deleting the workspace also deletes its state file, causing Terraform to lose track of all production resources. Those resources would still exist in AWS but be unmanaged — a far more dangerous situation.
  * *Why C is incorrect:* Running `terraform destroy` before `terraform apply` in production would first remove all existing resources and then recreate them, causing unnecessary downtime and risk. This is the opposite of a safe deployment strategy.
  * *Why D is incorrect:* The `default` workspace is not inherently safer than named workspaces. The inability to delete `default` prevents accidental state loss for that workspace but provides no protection against accidental `apply` or `destroy` operations.
