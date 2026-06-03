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

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
