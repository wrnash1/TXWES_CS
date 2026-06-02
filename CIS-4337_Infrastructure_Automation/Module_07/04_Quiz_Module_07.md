# CIS-4337 Infrastructure Automation

## Quiz — Module 07: Terraform Workspaces and Environments

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

Which built-in Terraform reference returns the name of the currently active workspace?

- A) `var.workspace`
- B) `terraform.workspace`
- C) `local.workspace`
- D) `env.workspace`

Correct Answer: B

Distractor Analysis:

- Why B is correct: `terraform.workspace` is a built-in Terraform value that returns the current workspace name as a string. It is available without any declaration.
- Why A is incorrect: `var.workspace` would reference an input variable named `workspace` that you declared explicitly. It is not automatically created.
- Why C is incorrect: `local.workspace` references a locally defined value named `workspace`. Like `var.workspace`, you would need to declare it.
- Why D is incorrect: `env.workspace` is not valid HCL syntax. Terraform does not have an `env` object for workspace access.

---

### Question 2

Which statement most accurately describes Terraform workspace state isolation?

- A) Each workspace uses a separate set of `.tf` configuration files in different directories.
- B) Each workspace maintains an independent state file while all workspaces share the same configuration code and provider settings.
- C) Each workspace runs with a separate provider plugin binary enabling different provider versions per environment.
- D) Each workspace has its own `terraform.tfvars` file that is automatically loaded based on the workspace name.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Workspace isolation is state-only. All workspaces in a working directory share the same `.tf` files, provider configuration, and provider plugins. Only the state file is independent per workspace.
- Why A is incorrect: Workspaces do not use different configuration directories. All workspaces share the same working directory and `.tf` files by design.
- Why C is incorrect: Provider plugins are shared across all workspaces. Workspaces do not enable per-workspace provider versioning.
- Why D is incorrect: Terraform does not automatically load workspace-named `.tfvars` files. You must pass `-var-file=<env>.tfvars` explicitly.

---

### Question 3

A team manages dev, staging, and prod environments. Prod requires a different AWS account, different IAM permissions, and additional compliance controls. Which approach does HashiCorp recommend?

- A) Use one configuration directory with three workspaces and conditional `count` logic per workspace.
- B) Store all three environments in one workspace using a single large variable file.
- C) Use separate Terraform configuration directories or separate Terraform Cloud workspaces with dedicated credentials and state per environment.
- D) Create one `.tf` file with three copies of every resource block suffixed with `_dev`, `_staging`, and `_prod`.

Correct Answer: C

Distractor Analysis:

- Why C is correct: The Terraform documentation explicitly states that CLI workspaces are not recommended when environments have different infrastructure requirements, credentials, or compliance controls. Separate directories or Terraform Cloud workspaces provide proper isolation.
- Why A is incorrect: Complex per-workspace conditional `count` logic in one configuration is hard to maintain and cannot provide credential isolation between accounts.
- Why B is incorrect: A single workspace means all three environments share one state file, creating risk of accidental cross-environment destruction.
- Why D is incorrect: Duplicating resource blocks per environment creates a maintenance nightmare and violates the DRY principle.

---

### Question 4

Where does Terraform store workspace state files when using the local backend for a workspace named `staging`?

- A) `.terraform/workspaces/staging/terraform.tfstate`
- B) `terraform.tfstate` with a `workspace = "staging"` key inside the file
- C) `terraform.tfstate.d/staging/terraform.tfstate`
- D) `workspaces.json` in the current working directory

Correct Answer: C

Distractor Analysis:

- Why C is correct: With the local backend, named workspace state is stored at `terraform.tfstate.d/<workspace_name>/terraform.tfstate`. The `default` workspace continues to use the root `terraform.tfstate` file.
- Why A is incorrect: `.terraform/` contains provider binaries and module downloads, not state files.
- Why B is incorrect: Workspace state files are separate files at separate paths, not multiplexed with a workspace key inside one file.
- Why D is incorrect: There is no `workspaces.json` file in the local backend implementation.

---

### Question 5

Which command displays only the name of the currently active Terraform workspace?

- A) `terraform workspace list`
- B) `terraform workspace status`
- C) `terraform workspace show`
- D) `terraform env show`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform workspace show` prints the active workspace name to stdout. The four valid workspace subcommands are `list`, `show`, `new`, `select`, and `delete`.
- Why A is incorrect: `terraform workspace list` shows all available workspaces and marks the active one with `*`, but its purpose is listing all workspaces, not printing just the active name.
- Why B is incorrect: `terraform workspace status` is not a valid subcommand. This is a common exam distractor.
- Why D is incorrect: `terraform env show` was the command in Terraform 0.9. It was replaced by `terraform workspace show` and is no longer valid.

---

### Question 6

You are in the `dev` workspace and run `terraform destroy`. What is the effect on the `prod` workspace?

- A) Both `dev` and `prod` infrastructure are destroyed because they share the same configuration.
- B) Only `dev` infrastructure is destroyed. The `prod` workspace state and infrastructure are not affected.
- C) The `prod` workspace state file is merged with the `dev` state file after destruction.
- D) Terraform prompts you to confirm destruction of all workspaces before proceeding.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Workspace state isolation means `terraform destroy` in `dev` reads and modifies only the `dev` state file. The `prod` state and its resources are completely unaffected.
- Why A is incorrect: Even though both environments use the same configuration code, they are tracked in separate state files. Destruction is scoped to the active workspace.
- Why C is incorrect: Terraform does not merge state files. Each workspace state remains independent.
- Why D is incorrect: Terraform prompts only for the current workspace's resources. It does not have awareness of resources in other workspaces during a destroy operation.

---

### Question 7

A configuration uses `terraform.workspace` in a `locals` block to select the number of EC2 instances: `replicas = terraform.workspace == "prod" ? 4 : 1`. You are currently in the `staging` workspace. How many instances will be created?

- A) 4 instances, because staging is similar to prod.
- B) 0 instances, because staging is not explicitly handled in the conditional.
- C) 1 instance, because the condition is false (staging is not "prod") and the false branch returns 1.
- D) An error, because `terraform.workspace` cannot be used in a ternary expression.

Correct Answer: C

Distractor Analysis:

- Why C is correct: The conditional `terraform.workspace == "prod"` evaluates to `false` when the active workspace is `staging`. The ternary expression returns the false-branch value of `1`.
- Why A is incorrect: The ternary expression only returns `4` when the workspace is exactly `"prod"`. Staging returns the false branch.
- Why B is incorrect: The false branch is `1`, not `0`. An explicit `0` would be required to produce no instances.
- Why D is incorrect: `terraform.workspace` is a string value and can be used in any expression that accepts a string, including comparisons and ternary expressions.

---

### Question 8

Which of the following is NOT a valid `terraform workspace` subcommand?

- A) `terraform workspace new`
- B) `terraform workspace select`
- C) `terraform workspace rename`
- D) `terraform workspace delete`

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform workspace rename` is not a valid subcommand. To rename a workspace, you must create a new one, migrate the state using `terraform state pull` and `terraform state push`, and delete the old workspace.
- Why A is incorrect: `terraform workspace new <name>` is a valid command that creates and switches to a new workspace.
- Why B is incorrect: `terraform workspace select <name>` is a valid command that switches to an existing workspace.
- Why D is incorrect: `terraform workspace delete <name>` is a valid command that deletes an empty, non-active workspace.

---

### Question 9

A Terraform configuration manages S3 buckets. The bucket name must be unique globally. The configuration is deployed in three workspaces: `dev`, `staging`, and `prod`. Which naming approach ensures global uniqueness across workspaces?

- A) `bucket = "my-app-data"` — the same name is used in all workspaces.
- B) `bucket = "my-app-${terraform.workspace}-data"` — workspace name is embedded in the bucket name.
- C) `bucket = var.bucket_name` — a separate variable value is supplied for each deployment manually.
- D) Both B and C are valid approaches.

Correct Answer: D

Distractor Analysis:

- Why D is correct: Both embedding `terraform.workspace` in the name and using a variable are valid techniques. Option B is automatic and convenient for workspace-based deployments. Option C requires explicit input but gives full control over naming. Both achieve global uniqueness when the values are distinct across workspaces.
- Why A is incorrect: Using the same bucket name in all workspaces would cause failures — S3 bucket names are globally unique across all AWS accounts. The second workspace to apply would receive an error that the bucket already exists.
- Why B is incorrect alone: This is a valid approach, but D is more complete.
- Why C is incorrect alone: This is also valid, but D is more complete.

---

### Question 10

What happens when you attempt to delete the `default` workspace?

- A) The default workspace is deleted and Terraform reverts to using no workspace.
- B) Terraform deletes the default state file and creates a new empty one.
- C) Terraform raises an error — the default workspace cannot be deleted.
- D) The default workspace is archived but not deleted.

Correct Answer: C

Distractor Analysis:

- Why C is correct: The `default` workspace is a permanent workspace. Running `terraform workspace delete default` produces an error. You can delete any other workspace that is not currently active and has empty state.
- Why A is incorrect: Terraform requires at least one workspace (`default`). You cannot operate without any workspace.
- Why B is incorrect: Terraform does not automatically recreate state files after deletion. The `default` workspace is simply protected from deletion.
- Why D is incorrect: There is no archive mechanism for workspaces.

---

Module 07 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
