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

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
