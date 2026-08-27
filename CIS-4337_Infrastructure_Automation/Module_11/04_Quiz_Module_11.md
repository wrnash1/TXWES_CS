# Quiz: Module 11 — Terraform Cloud and Remote Backends

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

**Instructions**: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A team configures a Terraform Cloud workspace with a Sentinel policy at the **hard mandatory** enforcement level. The policy fails during a plan check. What is the outcome?

A. The apply is blocked, but an organization owner can override the policy and proceed.
B. The apply is blocked with no override option, and the run is permanently failed.
C. The apply proceeds with a warning logged in the run output.
D. The plan is retried automatically after a 60-second delay.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — override capability is a feature of the **soft mandatory** enforcement level, not hard mandatory.
- C is incorrect — the **advisory** enforcement level allows the apply to proceed with a warning; hard mandatory does not.
- D is incorrect — Terraform Cloud does not retry runs due to policy failures; policy violations require code changes to resolve.

---

### Question 2

Which command authenticates the Terraform CLI with Terraform Cloud and stores the resulting token on the local machine?

A. `terraform auth login`
B. `terraform cloud authenticate`
C. `terraform login`
D. `terraform init --cloud`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `terraform auth login` is not a valid Terraform command.
- B is incorrect — `terraform cloud` is not a top-level Terraform subcommand; `terraform login` is the correct command.
- D is incorrect — `terraform init` initializes a configuration but does not authenticate; authentication is a prerequisite handled by `terraform login`.

---

### Question 3

What is a speculative plan in Terraform Cloud?

A. A plan that includes estimated cost information for resources to be created.
B. A read-only plan triggered on pull requests that cannot be applied and does not lock state.
C. A plan that runs on a schedule at a specified time interval.
D. A plan with a reduced scope that only evaluates resources in a single module.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — cost estimation is a separate Terraform Cloud feature; speculative plans refer to the PR-triggered read-only plans.
- C is incorrect — Terraform Cloud does support scheduled runs, but that is not what a speculative plan is.
- D is incorrect — speculative plans apply to the full configuration, not a reduced scope.

---

### Question 4

A company needs to share AWS credentials across 20 Terraform Cloud workspaces without duplicating the credential variables in each workspace. What Terraform Cloud feature enables this?

A. Workspace tags — tag all 20 workspaces and set a single variable per tag
B. Organization-level workspace defaults — set variables once at the organization level
C. Variable sets — create a set containing the AWS credentials and apply it to the relevant workspaces
D. Terraform modules — define the AWS provider credentials in a shared module

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — workspace tags are for organization and filtering; they do not provide variable sharing.
- B is incorrect — Terraform Cloud does not have an "organization-level workspace defaults" feature for variables; the correct feature is variable sets.
- D is incorrect — provider credentials should not be defined in module code; modules do not have access to the calling workspace's secrets, and embedding credentials in module code is a security anti-pattern.

---

### Question 5

A Terraform Cloud workspace is configured with **auto-apply enabled**. A developer pushes a commit that accidentally introduces a `terraform destroy` of a production database. What happens?

A. The plan is queued, a speculative check runs, and a human must confirm the destructive change.
B. The plan is queued and the apply runs automatically without any human confirmation.
C. Terraform Cloud detects the destructive change and pauses the run for review regardless of the auto-apply setting.
D. The push is rejected by Terraform Cloud's VCS integration webhook before the plan is queued.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — with auto-apply enabled, Terraform Cloud does not require human confirmation after a successful plan; it applies automatically.
- C is incorrect — Terraform Cloud does not automatically detect and pause destructive changes when auto-apply is enabled (though some organizations use Sentinel policies to enforce this behavior).
- D is incorrect — Terraform Cloud does not inspect commit content before queuing a plan; it queues a run for every push to the configured branch.

---

### Question 6

Which Terraform Cloud execution mode should a team choose when the infrastructure being managed is inside a private network that Terraform Cloud's managed workers cannot reach?

A. Remote execution with a VPN connection to the private network
B. Local execution mode
C. Agent execution mode with a self-hosted agent inside the private network
D. Speculative execution mode with network bridging

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — Terraform Cloud does not support configuring a VPN connection from its managed workers to customer networks.
- B is incorrect — local execution mode runs Terraform on the developer's local machine; while this can reach private networks, it removes the benefits of centralized execution and audit logging.
- D is incorrect — "speculative execution mode" is not a real Terraform Cloud execution mode.

---

### Question 7

How does the `cloud` block differ from `backend "remote"` for connecting to Terraform Cloud?

A. The `cloud` block requires a paid Terraform Cloud tier; `backend "remote"` is available on the free tier.
B. The `cloud` block is the newer, preferred syntax that supports additional Terraform Cloud features; `backend "remote"` is the legacy syntax.
C. The `cloud` block stores state locally and syncs to Terraform Cloud; `backend "remote"` stores state exclusively in Terraform Cloud.
D. The `cloud` block uses SSH for communication; `backend "remote"` uses HTTPS.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — both `cloud` and `backend "remote"` are available on all tiers, including the free tier.
- C is incorrect — both blocks store state in Terraform Cloud; neither uses a local-and-sync model.
- D is incorrect — both use HTTPS/TLS for communication with the Terraform Cloud API; SSH is not involved.

---

### Question 8

A Sentinel policy checks that all `aws_instance` resources have the tag `CostCenter` set. The policy is set to **soft mandatory**. A run fails the policy check. Which user can override the policy and allow the apply to proceed?

A. Any authenticated Terraform Cloud user in the organization
B. Only the user who triggered the run
C. A user with the appropriate override permission assigned to their team for that workspace
D. No user can override a soft mandatory policy; the code must be fixed

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — not all authenticated users have override permissions; overrides require specific team-level permissions configured by an organization owner.
- B is incorrect — the user who triggered the run does not automatically have override permissions unless they are also a member of a team with override capability.
- D is incorrect — soft mandatory policies CAN be overridden; this is the defining difference between soft mandatory and hard mandatory.

---

### Question 9

A team wants every infrastructure change to go through a pull request review before being applied. Which Terraform Cloud configuration achieves this goal?

A. Set the workspace execution mode to **local** to prevent remote applies.
B. Enable VCS integration with the main branch as the apply trigger and require manual confirmation on all runs.
C. Use Sentinel policies to block all applies until a PR is merged.
D. Configure workspace notifications to alert the team on every plan, then apply manually.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — local execution mode prevents Terraform Cloud from running applies but does not enforce a PR review; it just moves execution to the developer's laptop.
- C is incorrect — Sentinel cannot inspect VCS pull request status; it evaluates infrastructure plan content, not VCS workflow state.
- D is incorrect — notifications alone do not prevent an apply from happening; without manual confirmation configured, auto-applies would proceed regardless of whether the team reviewed the notification.

---

### Question 10

Where does the Terraform CLI store the API token after a successful `terraform login` command?

A. In the `terraform.tfstate` file in the current working directory
B. In the `.terraform/` directory inside the current working directory
C. In `~/.terraform.d/credentials.tfrc.json`
D. In an environment variable that persists across shell sessions

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `terraform.tfstate` stores infrastructure state, not authentication credentials.
- B is incorrect — `.terraform/` contains provider plugins and module downloads for the current project; credentials are stored globally, not per-project.
- D is incorrect — `terraform login` stores the token in a file, not an environment variable. Environment variables (`TF_TOKEN_`) are an alternative that the user sets manually.

---

---

### Question 11 (5 points)

A Terraform Cloud workspace has a VCS integration configured to trigger runs on pushes to the `main` branch. A developer pushes a commit that modifies only a `README.md` file. What happens?

- A) Terraform Cloud triggers a full plan and apply because any push to the configured branch triggers a run.
- B) Terraform Cloud skips the run because no `.tf` files were modified.
- C) Terraform Cloud triggers a speculative plan only, not a full apply.
- D) Terraform Cloud triggers a plan but cancels it automatically when it detects no infrastructure changes.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B is incorrect — Terraform Cloud does not inspect file types before queuing a run; any push to the configured branch triggers a run regardless of which files changed.
  - C is incorrect — speculative plans are triggered by pull requests, not pushes to the configured apply branch; a push to `main` triggers a full plan-and-apply workflow.
  - D is incorrect — Terraform Cloud queues and runs the plan; the plan may show "No changes" but it is not automatically cancelled before running.

---

### Question 12 (5 points)

Which environment variable is used to authenticate the Terraform CLI with Terraform Cloud in a CI/CD pipeline where `terraform login` cannot be run interactively?

- A) `TF_CLOUD_TOKEN`
- B) `TF_API_TOKEN`
- C) `TF_TOKEN_app_terraform_io`
- D) `TERRAFORM_CLOUD_CREDENTIALS`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — `TF_CLOUD_TOKEN` is not a recognized Terraform environment variable.
  - B is incorrect — `TF_API_TOKEN` is not the standard environment variable format; Terraform uses `TF_TOKEN_` followed by the hostname with dots replaced by underscores.
  - D is incorrect — `TERRAFORM_CLOUD_CREDENTIALS` is not a valid Terraform environment variable.

---

### Question 13 (5 points)

A team uses Terraform Cloud with the free tier. They want to write a policy that blocks any apply unless all `aws_instance` resources have a `CostCenter` tag. Which Terraform Cloud feature would they use, and is it available on the free tier?

- A) Run triggers — available on the free tier
- B) Sentinel policies — requires the Team tier or above; not available on the free tier
- C) Variable sets — available on the free tier
- D) Workspace notifications — available on the free tier

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — run triggers control when one workspace triggers another workspace's run; they do not enforce infrastructure policies.
  - C is incorrect — variable sets share variable values across workspaces; they do not enforce policy rules on infrastructure content.
  - D is incorrect — workspace notifications send alerts on run events; they do not block applies or evaluate resource attributes.

---

### Question 14 (5 points)

A Terraform Cloud workspace is set to **remote** execution mode. A developer runs `terraform apply` from their local machine. Where does the actual Terraform execution occur?

- A) On the developer's local machine, with state saved to Terraform Cloud
- B) On Terraform Cloud's managed infrastructure, with output streamed to the developer's terminal
- C) Partly on the developer's machine (plan phase) and partly in Terraform Cloud (apply phase)
- D) On the developer's machine only; remote execution mode refers to the state backend, not execution

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — in remote execution mode, Terraform uploads the configuration and executes entirely in Terraform Cloud; local machine runs only the CLI wrapper.
  - C is incorrect — both plan and apply phases execute in Terraform Cloud; the local CLI only streams the output.
  - D is incorrect — remote execution mode means execution happens in Terraform Cloud, not on the local machine. Local execution mode is when only state is remote.

---

### Question 15 (5 points)

An organization has 50 Terraform Cloud workspaces spread across three teams (network, compute, security). They want each team to have Write access to their own workspaces and Read access to all other workspaces. What is the most maintainable way to configure this in Terraform Cloud?

- A) Manually add each engineer to each workspace with the appropriate permission level.
- B) Create three teams in Terraform Cloud, assign workspaces to each team with the appropriate permissions, and add engineers to their team.
- C) Use variable sets to define team membership and permission levels.
- D) Create a Sentinel policy that enforces team-based access by evaluating the username of the person triggering the run.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — manually managing 50 workspaces per-person is error-prone and does not scale; team-based access is the designed mechanism.
  - C is incorrect — variable sets manage configuration values, not access permissions.
  - D is incorrect — Sentinel policies evaluate infrastructure plan content; they cannot enforce or grant team-level workspace access permissions.

---

### Question 16 (5 points)

A Terraform Cloud workspace stores an AWS secret access key as a sensitive environment variable (`AWS_SECRET_ACCESS_KEY`). After the variable is saved, what can a workspace administrator do with the stored value?

- A) Read the value back from the Terraform Cloud UI at any time by clicking the variable row.
- B) Read the value via the Terraform Cloud API using an admin token.
- C) Neither read nor retrieve the value — sensitive variables can only be overwritten or deleted, never read back.
- D) Read the value only during an active run by inspecting run logs.

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — the Terraform Cloud UI hides sensitive variable values after saving; they cannot be revealed through the UI.
  - B is incorrect — the Terraform Cloud API also prevents retrieval of sensitive variable values; the API returns a masked placeholder.
  - D is incorrect — sensitive variable values are intentionally excluded from run logs; Terraform Cloud ensures they do not appear in streamed output.

---

### Question 17 (5 points)

What is the difference between a **Terraform Cloud workspace** and a **Terraform CLI workspace**?

- A) They are identical; CLI workspaces and Cloud workspaces are the same concept at different abstraction levels.
- B) Terraform Cloud workspaces are full environments with state, variables, access controls, run history, and VCS integration; CLI workspaces only provide state isolation within a single backend configuration.
- C) Terraform Cloud workspaces are for production only; CLI workspaces are for development.
- D) CLI workspaces support variable sets; Terraform Cloud workspaces do not.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — the two workspace concepts are different in scope and capability; equating them leads to misconfiguration.
  - C is incorrect — both types can be used in any environment; production vs. development is not what distinguishes them.
  - D is incorrect — variable sets are a Terraform Cloud feature; CLI workspaces have no equivalent variable set mechanism.

---

### Question 18 (5 points)

A run in Terraform Cloud passes all Sentinel policy checks but a team member rejects the apply during the manual confirmation step. What is the state of the infrastructure?

- A) The infrastructure was partially applied up to the point where the team member intervened.
- B) The infrastructure is unchanged; the rejection prevents the apply from executing.
- C) The resources are created in a "pending" state and must be manually cleaned up.
- D) The plan is automatically re-queued after a 30-minute delay.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — Terraform Cloud applies atomically at the run level; if the apply is not confirmed, no changes are made.
  - C is incorrect — Terraform Cloud does not create "pending" resources; the apply either executes fully or not at all.
  - D is incorrect — Terraform Cloud does not automatically re-queue rejected runs; the developer must trigger a new run.

---

### Question 19 (5 points)

A team configures a **global variable set** in their Terraform Cloud organization. Which workspaces receive the variables defined in this set?

- A) Only workspaces explicitly listed in the variable set's workspace assignments
- B) Only workspaces belonging to the team that owns the variable set
- C) All workspaces in the organization automatically
- D) All workspaces tagged with `global = true`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — a globally applied variable set is automatically applied to all workspaces; no explicit assignment per workspace is needed.
  - B is incorrect — variable sets are an organization-level feature; there is no concept of a team "owning" a variable set in the way described.
  - D is incorrect — global application does not require workspace tags; the scope is configured on the variable set itself.

---

### Question 20 (5 points)

A Terraform Cloud workspace has `terraform_version = "1.4.6"` set in workspace settings. A developer's local Terraform CLI is version `1.6.0`. The developer runs `terraform plan`. Which version of Terraform executes the plan?

- A) `1.6.0` — the developer's local version, because the CLI initiates the run
- B) `1.4.6` — the workspace-configured version runs on Terraform Cloud's managed agent
- C) The latest available version in Terraform Cloud's agent fleet, regardless of workspace settings
- D) Both versions run in parallel; the workspace setting only applies to the apply phase

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — in remote execution mode, the CLI only streams output; the plan runs on Terraform Cloud using the workspace-specified version.
  - C is incorrect — Terraform Cloud honors the workspace-configured version; it does not default to latest unless no version is specified.
  - D is incorrect — there is no parallel execution; a single version is used for the entire run lifecycle as determined by the workspace setting.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
