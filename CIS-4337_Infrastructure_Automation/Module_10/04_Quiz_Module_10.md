# Quiz: Module 10 — Terraform Workspaces and Environments

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

**Instructions**: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What is the name of the workspace that exists in every Terraform configuration and cannot be deleted?

A. `main`
B. `root`
C. `default`
D. `primary`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `main` is not a workspace name; it is a common convention for the primary `.tf` file.
- B is incorrect — `root` refers to the root module concept, not a workspace name.
- D is incorrect — `primary` is not a Terraform concept; it is not a reserved workspace name.

---

### Question 2

A developer runs `terraform workspace new staging`. What is the state of the CLI immediately after this command completes successfully?

A. The `staging` workspace is created but the CLI remains in the previously active workspace.
B. The `staging` workspace is created and the CLI is now in the `staging` workspace.
C. The `staging` workspace is created, initialized, and an empty apply is run automatically.
D. The `staging` workspace is created and the user is prompted to run `terraform init`.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — `terraform workspace new` both creates and switches to the new workspace in a single command.
- C is incorrect — workspace creation does not trigger any apply; the user must run `terraform apply` separately.
- D is incorrect — `terraform init` is not required when switching between workspaces; the configuration is already initialized.

---

### Question 3

When using the local backend, where does Terraform store the state file for a workspace named `dev`?

A. `dev/terraform.tfstate`
B. `.terraform/workspaces/dev/terraform.tfstate`
C. `terraform.tfstate.d/dev/terraform.tfstate`
D. `terraform-dev.tfstate`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — Terraform does not create a top-level `dev/` directory for local workspace state.
- B is incorrect — `.terraform/` is where provider and module plugins are stored, not state files.
- D is incorrect — Terraform does not use a naming convention like `terraform-<workspace>.tfstate` for local state.

---

### Question 4

Which built-in Terraform value returns the name of the currently selected workspace?

A. `var.workspace`
B. `local.workspace`
C. `env.workspace`
D. `terraform.workspace`

**Correct Answer**: D

**Distractor Analysis**:

- A is incorrect — `var.workspace` would require a declared input variable named `workspace`; no such built-in exists.
- B is incorrect — `local.workspace` would require a declared local value named `workspace`; no such built-in exists.
- C is incorrect — `env.` is not a valid Terraform namespace; there is no built-in `env` object.

---

### Question 5

A company wants each of its three environments (dev, staging, prod) to be deployed into separate AWS accounts with separate IAM credentials. Which approach best meets this requirement?

A. Use three Terraform workspaces (dev, staging, prod) and configure the provider with `terraform.workspace`-based role ARNs.
B. Use a directory-based structure with a separate backend and provider configuration per environment directory.
C. Use the `default` workspace for prod, and create two additional workspaces for dev and staging.
D. Use a single workspace with a `count` expression to create three sets of resources simultaneously.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — while it is technically possible to use `terraform.workspace` in a provider `assume_role` ARN, workspaces share the same provider block; this approach is fragile and is explicitly not recommended by HashiCorp for environments requiring separate credentials.
- C is incorrect — using the `default` workspace for prod is an anti-pattern; it does not provide separate credentials or backend configurations.
- D is incorrect — `count` creates multiple resource instances within the same state, not separate environments with separate accounts.

---

### Question 6

You want to delete the `dev` workspace. You run `terraform workspace delete dev` but receive an error. What is the most likely cause?

A. The `dev` workspace contains a non-empty state (resources have been created and not yet destroyed).
B. Workspace deletion requires the `-force` flag in all cases.
C. You cannot delete a workspace if any other workspaces exist.
D. The `default` workspace must be active before deleting any other workspace.

**Correct Answer**: A

**Distractor Analysis**:

- B is incorrect — `-force` is not a standard flag for `terraform workspace delete`; there is no such flag in the current CLI.
- C is incorrect — there is no restriction based on the existence of other workspaces.
- D is incorrect — you must NOT be in the workspace you are trying to delete, but you do not need to be specifically in `default`; any other workspace will work.

---

### Question 7

An operator is about to run `terraform apply` but cannot remember which workspace is currently active. What command shows the active workspace?

A. `terraform workspace current`
B. `terraform workspace show`
C. `terraform state workspace`
D. `terraform env show`

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — `terraform workspace current` is not a valid subcommand; there is no `current` subcommand.
- C is incorrect — `terraform state` and `terraform workspace` are separate command trees; `terraform state workspace` is invalid.
- D is incorrect — `terraform env` was the original (deprecated) command for workspaces in older Terraform versions; `terraform workspace` is the current command, and `show` is the correct subcommand.

---

### Question 8

A team uses the `terraform.workspace` built-in in a `locals` block to look up environment-specific settings from a map. When the configuration is applied to the `prod` workspace, the value `local.workspace_config["prod"]` is accessed. What happens if a team member accidentally runs `terraform apply` in a workspace named `production` instead of `prod`?

A. Terraform automatically aliases `production` to `prod` based on prefix matching.
B. Terraform errors during plan because the workspace name is not in the map, and the lookup fails.
C. Terraform silently uses the `default` key if the workspace name is not found.
D. Terraform prompts the operator to select a valid workspace from the map.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — Terraform does not perform prefix matching or aliasing for workspace names.
- C is incorrect — map lookups in Terraform do not fall back to a default key; an undefined key causes an error.
- D is incorrect — Terraform does not interactively prompt for workspace selection during plan or apply; it processes the configuration as-is.

---

### Question 9

Which of the following is a legitimate use case where Terraform workspaces are the MOST appropriate solution?

A. Managing dev, staging, and prod environments for a regulated financial application with separate AWS accounts
B. Creating ephemeral test environments for each pull request in a CI/CD pipeline
C. Managing infrastructure across multiple cloud providers simultaneously
D. Storing different provider credentials for different team members

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — regulated applications with separate accounts require directory-based isolation to enforce credential separation, a goal workspaces cannot achieve.
- C is incorrect — multi-cloud configurations require multiple provider blocks, not workspaces; workspaces do not add multi-cloud capability.
- D is incorrect — workspaces share provider configuration; they cannot store different credentials per user.

---

### Question 10

A Terraform configuration uses `terraform.workspace` extensively to branch environment-specific logic. Over time, the `locals` block containing workspace conditionals has grown to 200 lines. A new team member struggles to understand how the configuration behaves in each environment. What is the most architecturally sound remedy?

A. Add more inline comments to the `locals` block explaining each conditional.
B. Refactor to a directory-based environment structure where each environment directory has its own explicit variable values, eliminating the need for `terraform.workspace` conditionals.
C. Move all workspace conditionals from `locals` to inline expressions within each resource block for better co-location.
D. Replace `terraform.workspace` with a new input variable `var.environment` that must be supplied on the command line for every apply.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — adding comments addresses the symptom (poor readability) but not the root cause (a shared configuration that is too complex to reason about per-environment).
- C is incorrect — moving conditionals from `locals` to resource blocks actually increases complexity and reduces maintainability.
- D is incorrect — replacing `terraform.workspace` with `var.environment` without also separating the state could still allow accidental cross-environment applies; it also requires operators to correctly supply the environment name on every command, which is error-prone.

---

---

### Question 11 (5 points)

A developer runs `terraform workspace select prod` and then immediately runs `terraform apply` without reviewing the plan. Which workspace-related risk does this scenario illustrate?

- A) Workspace state corruption because `select` and `apply` cannot be run without an intervening `plan`.
- B) The implicit selection risk — the active workspace is a CLI-level setting that is easy to forget, leading to unintended applies against the wrong environment.
- C) The shared provider risk — the prod workspace uses a different AWS account than the developer's credentials allow.
- D) State locking failure because the prod workspace was already locked by another process.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — Terraform does not require `plan` before `apply`; `-auto-approve` skips the plan review entirely, but `plan` is not mandatory.
  - C is incorrect — the scenario does not mention credential differences; the risk described is forgetting which workspace is active.
  - D is incorrect — state locking would produce an explicit error message; this scenario illustrates a silent operational risk, not a locking failure.

---

### Question 12 (5 points)

What does the `*` symbol indicate when you run `terraform workspace list`?

- A) The workspace has unsaved changes.
- B) The workspace is the `default` workspace.
- C) The workspace is currently selected (active).
- D) The workspace has the highest resource count.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — Terraform state is written atomically after apply; there is no concept of "unsaved changes" tracked by the workspace list command.
  - B is incorrect — `*` marks whichever workspace is currently active, which may or may not be `default`.
  - D is incorrect — `terraform workspace list` output contains no resource count information.

---

### Question 13 (5 points)

A team stores Terraform state in an S3 backend with `key = "app/terraform.tfstate"`. After running `terraform workspace new prod`, what is the S3 key where the `prod` workspace state is stored?

- A) `app/terraform.tfstate.prod`
- B) `prod/app/terraform.tfstate`
- C) `env:/prod/app/terraform.tfstate`
- D) `app/prod/terraform.tfstate`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — S3 does not append the workspace name as a file extension suffix.
  - B is incorrect — Terraform prefixes the path with `env:/`, not just the workspace name.
  - D is incorrect — the workspace name is not inserted between the key segments; the `env:/` prefix is prepended to the entire key.

---

### Question 14 (5 points)

You need to destroy all resources in the `staging` workspace. Which sequence of commands is correct?

- A) `terraform workspace delete staging` then `terraform destroy`
- B) `terraform workspace select staging` then `terraform destroy -auto-approve` then `terraform workspace select default` then `terraform workspace delete staging`
- C) `terraform destroy -workspace=staging -auto-approve`
- D) `terraform workspace select staging` then `terraform workspace delete staging`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — you cannot delete a workspace that still has managed resources (non-empty state); you must destroy first.
  - C is incorrect — `-workspace=` is not a valid flag for `terraform destroy`; you must switch workspaces using `terraform workspace select`.
  - D is incorrect — you cannot delete the currently selected workspace; you must switch to a different workspace before deleting.

---

### Question 15 (5 points)

A team of six engineers works on the same Terraform configuration. Each engineer creates their own workspace named after their username to test changes. What risk does this practice introduce?

- A) Workspace names must be globally unique across all Terraform Registry accounts.
- B) All workspaces share the same backend, so the S3 bucket (or equivalent) accumulates many state files, increasing storage costs and management overhead.
- C) Terraform automatically merges all workspace states during the next `terraform apply`.
- D) Workspaces named after usernames are rejected by Terraform's naming validation.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — workspace names are scoped to a single configuration's backend; there is no global registry of workspace names.
  - C is incorrect — Terraform never merges state across workspaces; each workspace's state is completely isolated.
  - D is incorrect — Terraform workspace names accept any alphanumeric string with underscores and hyphens; username-based names are fully valid.

---

### Question 16 (5 points)

In the directory-based environment isolation pattern, each environment directory has its own `backend.tf` file. What is the primary benefit of this over a single backend configuration shared by all environments?

- A) Separate backend files allow each environment to use a different Terraform version.
- B) Each environment can store its state in a completely separate location (e.g., different S3 bucket, storage account, or GCS bucket), enabling separate access controls and preventing accidental cross-environment state operations.
- C) Separate backend files are required by the Terraform Registry for module publication.
- D) Backend files in subdirectories are encrypted by default, whereas a root-level `backend.tf` is stored in plaintext.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — Terraform version constraints are set in `required_version`, not in the backend configuration.
  - C is incorrect — module publication requirements concern repository naming and module structure, not backend configuration.
  - D is incorrect — backend configuration files are plain HCL text in all cases; encryption applies to the state data stored in the backend, not to the configuration files.

---

### Question 17 (5 points)

Which of the following expressions correctly reads the current workspace name inside a `locals` block?

- A) `local.workspace = terraform.workspace`
- B) `environment = var.workspace`
- C) `env = terraform.workspace`
- D) `workspace_name = terraform.workspace`

- **Correct Answer:** D
- **Distractor Analysis:**
  - A is incorrect — `local.workspace = ...` is not valid HCL; local values are declared as `name = expression` inside a `locals {}` block, not using dot notation.
  - B is incorrect — `var.workspace` references an input variable named `workspace`, which must be explicitly declared; it is not the built-in workspace value.
  - C is incorrect — while `env = terraform.workspace` is syntactically valid as a local assignment, option D is the clearest and most semantically precise expression of reading the workspace name. More importantly, option C uses `env` which is not valid — this is a distractor that could be confused with `env.` namespace which doesn't exist.

---

### Question 18 (5 points)

A Terraform configuration uses a `lookup()` call: `lookup(local.workspace_config, terraform.workspace, local.workspace_config["default"])`. What does the third argument provide?

- A) A validation rule that rejects unknown workspace names.
- B) A fallback value returned when the workspace name is not a key in `local.workspace_config`.
- C) The default workspace's configuration, which is always used regardless of the current workspace.
- D) A required second map argument for the `lookup()` function signature.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — `lookup()` does not perform validation; it performs a safe map key access and returns the fallback instead of erroring on a missing key.
  - C is incorrect — the fallback is only used when the key is absent; if the workspace name exists in the map, the map's value is returned, not the default.
  - D is incorrect — `lookup(map, key, default)` is a three-argument function; the third argument is the default, not a second map. Two-argument `lookup(map, key)` also exists but throws an error on missing keys.

---

### Question 19 (5 points)

A CI/CD pipeline creates a workspace named after each pull request (e.g., `pr-123`) to deploy ephemeral test environments. After the pull request is merged, the pipeline should clean up. What is the correct cleanup sequence?

- A) Delete the workspace directory from version control, then run `terraform init`.
- B) Switch to the `pr-123` workspace, run `terraform destroy`, switch to another workspace, then delete the `pr-123` workspace.
- C) Run `terraform workspace delete pr-123 -force` without destroying resources first.
- D) Run `terraform state rm module.app` and then delete the workspace.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — workspaces are backend-level state constructs, not version-controlled directories; deleting a file from git does not affect backend state.
  - C is incorrect — while a `-force` flag analogue does not officially exist for workspace deletion in the standard CLI, destroying infrastructure first is the correct operational practice to avoid orphaned cloud resources.
  - D is incorrect — `terraform state rm` removes resources from state tracking without destroying the actual infrastructure, leaving orphaned cloud resources.

---

### Question 20 (5 points)

Which statement best describes the relationship between Terraform workspaces and the `terraform.workspace` built-in value when the `default` workspace is active?

- A) `terraform.workspace` returns `null` in the default workspace.
- B) `terraform.workspace` returns the empty string `""` in the default workspace.
- C) `terraform.workspace` returns the string `"default"` in the default workspace.
- D) `terraform.workspace` is only available when a non-default workspace is active.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — `terraform.workspace` is always a non-null string value; it never returns `null`.
  - B is incorrect — the default workspace has an actual name: `"default"`; the built-in returns that string, not an empty string.
  - D is incorrect — `terraform.workspace` is always available regardless of which workspace is active; there is no conditional availability.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
