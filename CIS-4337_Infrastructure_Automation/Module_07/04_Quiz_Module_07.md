# Quiz: Module 07 - Terraform Workspaces and Environments
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which built-in Terraform reference returns the name of the currently active workspace?
*   A) var.workspace
*   B) terraform.workspace
*   C) local.workspace
*   D) env.workspace
*   **Correct Answer:** B) `terraform.workspace` is a built-in string value that returns the name of the currently selected workspace (e.g., `"default"`, `"dev"`, `"prod"`).
*   **Distractor Analysis:**
    *   *Why B is correct:* This is one of a small set of built-in Terraform values (along with `terraform.env`, which is deprecated). The exam specifically tests the correct path — it is `terraform.workspace`, not prefixed with `var.` or `local.`.
    *   *Why A is incorrect:* `var.workspace` would reference an input variable named `workspace`, which you would have to declare yourself. No such variable is automatically created by Terraform.
    *   *Why C is incorrect:* `local.workspace` would reference a local value named `workspace`. Like `var.workspace`, you would need to declare it explicitly.
    *   *Why D is incorrect:* `env.workspace` is not valid HCL syntax. Terraform has no `env` object for built-in workspace access.

---

**Question 2**
Which of the following most accurately describes **Terraform workspace state isolation**?
*   A) Each workspace uses a completely separate set of `.tf` configuration files stored in different directories on the filesystem
*   B) Each workspace maintains an independent state file, so resources created in one workspace do not appear in or affect another workspace's state, while all workspaces share the same configuration code
*   C) Each workspace runs with a separate provider plugin binary, enabling different provider versions per environment
*   D) Each workspace has its own `terraform.tfvars` file that is automatically loaded based on the workspace name
*   **Correct Answer:** B) Workspaces isolate state only — each has its own state file, so infrastructure deployed in `dev` is tracked separately from `prod`. However, all workspaces in a directory share identical `.tf` configuration files and provider configurations.
*   **Distractor Analysis:**
    *   *Why B is correct:* This is the core concept the exam tests. Workspace isolation is state-only. The same code runs against different state files. This is what makes `terraform.workspace` useful for naming resources differently per workspace.
    *   *Why A is incorrect:* Workspaces do not use different configuration directories. All workspaces share the same working directory and `.tf` files — that is by design.
    *   *Why C is incorrect:* Provider plugins are shared across all workspaces in a directory. Workspaces do not enable per-workspace provider versioning.
    *   *Why D is incorrect:* Terraform does not automatically load workspace-named `.tfvars` files. You must explicitly pass `-var-file=dev.tfvars` when running in the dev workspace if you want different values.

---

**Question 3**
A team is using Terraform to manage infrastructure for three environments: `dev`, `staging`, and `prod`. The `prod` environment requires a completely different module structure, different provider credentials, and different compliance controls than `dev`. Which approach does HashiCorp recommend?
*   A) Use a single configuration directory with three workspaces and conditional `count` logic to enable/disable resources per workspace
*   B) Store all three environments in one workspace and use variable files to differentiate them
*   C) Use separate Terraform configuration directories (or separate Terraform Cloud workspaces) for each environment, with dedicated credentials and state per environment
*   D) Create a single monolithic `.tf` file with three copies of each resource block named `_dev`, `_staging`, and `_prod`
*   **Correct Answer:** C) When environments have significantly different infrastructure, credentials, or compliance requirements, HashiCorp recommends separate configurations or separate Terraform Cloud workspaces — not CLI workspaces, which are designed for lightweight state isolation of similar infrastructure.
*   **Distractor Analysis:**
    *   *Why C is correct:* The official Terraform documentation explicitly states that CLI workspaces are not recommended for managing multiple environments when those environments have meaningfully different infrastructure or security boundaries.
    *   *Why A is incorrect:* Complex conditional `count` logic in a single config to simulate different environments becomes difficult to maintain and test. It also cannot provide credential isolation.
    *   *Why B is incorrect:* A single workspace means all three environments share one state file — a serious risk if a `destroy` is run or state is corrupted.
    *   *Why D is incorrect:* Duplicating resource blocks per environment violates the DRY principle and creates a maintenance nightmare as the number of resources grows.

---

**Question 4**
Where does Terraform store workspace state files when using the local backend?
*   A) In the `.terraform/` hidden directory alongside provider plugins
*   B) In the same `terraform.tfstate` file, using a `workspace` key to separate entries
*   C) In `terraform.tfstate.d/<workspace_name>/terraform.tfstate` subdirectories
*   D) In a `workspaces.json` file in the current working directory
*   **Correct Answer:** C) With a local backend, each non-default workspace's state is stored at `terraform.tfstate.d/<workspace_name>/terraform.tfstate`. The `default` workspace state stays in the root as `terraform.tfstate`.
*   **Distractor Analysis:**
    *   *Why C is correct:* This is the exact filesystem path the exam tests. Knowing where local workspace state is stored helps with backup strategies and understanding what to gitignore.
    *   *Why A is incorrect:* The `.terraform/` directory contains provider binaries and module downloads, not state files.
    *   *Why B is incorrect:* The state file is not multiplexed with workspace keys — each workspace has a completely separate file at a separate path.
    *   *Why D is incorrect:* There is no `workspaces.json` file in the local backend implementation.

---

**Question 5**
Which command displays the name of the currently active Terraform workspace?
*   A) terraform workspace list
*   B) terraform workspace status
*   C) terraform workspace show
*   D) terraform env show
*   **Correct Answer:** C) `terraform workspace show` prints the name of the currently selected workspace to stdout.
*   **Distractor Analysis:**
    *   *Why C is correct:* The four workspace subcommands are `list`, `new`, `select`, and `show`. `show` is specifically for displaying the active workspace name. The exam tests all four.
    *   *Why A is incorrect:* `terraform workspace list` shows all available workspaces and marks the active one with an asterisk (`*`), but its primary purpose is listing, not showing the single active name.
    *   *Why B is incorrect:* `terraform workspace status` is not a valid subcommand. This is a common distractor on the exam.
    *   *Why D is incorrect:* `terraform env` was the old command prefix for workspaces in Terraform 0.9. It was renamed to `terraform workspace` and `terraform env show` is no longer valid.
