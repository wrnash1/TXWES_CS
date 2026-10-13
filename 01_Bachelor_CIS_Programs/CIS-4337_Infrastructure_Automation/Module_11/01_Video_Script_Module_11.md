# Video Script: Module 11 — Terraform Cloud and Remote Backends

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Introduction (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 11 of CIS-4337, Infrastructure Automation.

In the previous module you learned how Terraform workspaces provide state isolation. Now we move to the platform that extends that concept into a full collaboration and governance system: **Terraform Cloud**.

Terraform Cloud is HashiCorp's hosted SaaS platform for managing Terraform at team scale. It brings together remote execution, shared state, secrets management, access controls, policy enforcement, and VCS integration — everything you need to operate Terraform professionally.

By the end of this module you will be able to:

- Describe the key features of Terraform Cloud and how they differ from the open-source CLI
- Configure the `cloud` block to connect a configuration to Terraform Cloud
- Understand workspaces in the Terraform Cloud context
- Explain how remote execution and VCS integration work
- Describe Sentinel policy as code and how it enforces governance
- Understand team workflows and role-based access

Let's get started.

[PAUSE]

---

## Section 1: What Is Terraform Cloud (1:30 – 4:30)

Terraform Cloud is a managed platform from HashiCorp that provides a centralized control plane for Terraform operations. There are three tiers:

- **Free tier** — up to 500 managed resources, remote state, and one team per organization
- **Plus/Team tier** — unlimited users, SSO, Sentinel policies, audit logging
- **Business tier** — self-managed agents, audit trails, and enterprise SLA features

The exam focuses on the features, not the pricing, so let's go through what each capability does.

[PAUSE]

### Remote State Storage

Terraform Cloud provides a managed state backend. State is stored, versioned, and locked automatically. You do not need to manage an S3 bucket, DynamoDB table, or Azure Blob container.

### Remote Execution

Instead of running `terraform plan` and `terraform apply` on your local machine, Terraform Cloud runs them on managed worker infrastructure. This means:

- Consistent, reproducible execution environment
- Secrets and provider credentials are stored in the workspace, not on developer laptops
- All plan and apply output is logged and retained for auditing
- No need to distribute cloud credentials to individual engineers

### Shared Variables and Secrets

Variables are stored per workspace in Terraform Cloud's encrypted secrets store. Team members trigger runs; Terraform Cloud injects the variables — no one needs to know the actual secret values.

[PAUSE]

---

## Section 2: The cloud Block (4:30 – 7:30)

To connect a Terraform configuration to Terraform Cloud, you use the `cloud` block inside the `terraform` block. This replaces a `backend` block.

```hcl
terraform {
  required_version = ">= 1.1"

  cloud {
    organization = "acme-corp"

    workspaces {
      name = "my-app-prod"
    }
  }
}
```

[SHOW TERMINAL]

After adding this block, run:

```bash
terraform login
terraform init
```

`terraform login` opens a browser window to generate an API token, which is stored in `~/.terraform.d/credentials.tfrc.json`. Subsequent `terraform plan` and `terraform apply` commands execute remotely in Terraform Cloud.

[PAUSE]

### Workspace Tags

Instead of pinning to a single workspace name, you can use tags to target multiple workspaces:

```hcl
terraform {
  cloud {
    organization = "acme-corp"

    workspaces {
      tags = ["production", "us-east"]
    }
  }
}
```

This is useful when you have multiple workspaces with the same configuration, tagged for identification.

[PAUSE]

---

## Section 3: Workspaces in Terraform Cloud (7:30 – 10:30)

**Important distinction**: In Terraform Cloud, a workspace is a richer concept than a CLI workspace. A Terraform Cloud workspace includes:

- Its own state file (with version history)
- Its own variable set (Terraform variables and environment variables)
- Its own run history (plan and apply logs)
- Its own access controls
- Its own VCS connection (if configured)
- Its own notification settings

CLI workspaces (`terraform workspace new`) are a simpler mechanism that only separates state. Terraform Cloud workspaces are complete isolated environments with full configuration, secrets, and execution context.

[SHOW TERMINAL]

When you connect to Terraform Cloud and target a workspace named `my-app-prod`, all plans and applies for that workspace run in Terraform Cloud's execution environment with the workspace's variables injected automatically.

[PAUSE]

### Variable Sets

Terraform Cloud allows you to define **variable sets** — collections of variables that can be shared across multiple workspaces. This is ideal for credentials or common tags that apply to all workspaces in an organization.

For example, a variable set named `AWS-Production-Creds` containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as environment variables can be applied to all production workspaces — without duplicating the secret in each workspace.

[PAUSE]

---

## Section 4: VCS Integration (10:30 – 13:30)

One of Terraform Cloud's most powerful features is **VCS integration** — connecting a workspace directly to a version control repository.

When VCS integration is configured:

1. You push code to a branch (e.g., `main`)
2. Terraform Cloud detects the push via a webhook
3. A speculative plan runs automatically
4. If the push is to the configured production branch, an apply can run automatically or wait for manual approval
5. Plan output is posted as a comment on the pull request

[SHOW TERMINAL]

This workflow looks like:

```
Developer → git push → GitHub → Terraform Cloud webhook
                                       ↓
                               Speculative plan runs
                                       ↓
                          PR comment with plan summary
                                       ↓
                        Merge to main → Auto or manual apply
```

This is **GitOps for infrastructure**: every infrastructure change is tracked in Git, reviewed in a PR, and applied through a controlled, auditable pipeline.

[PAUSE]

### Speculative Plans

A speculative plan is a Terraform plan that runs against a pull request but does not lock state or allow an apply. It shows what WOULD change if the PR were merged — surfacing any errors or unintended consequences before merge.

[PAUSE]

---

## Section 5: Sentinel — Policy as Code (13:30 – 17:30)

**Sentinel** is HashiCorp's policy as code framework. It is available in Terraform Cloud's Team tier and above. Sentinel policies run after the plan phase and before the apply phase, enforcing governance rules on infrastructure changes.

[SHOW TERMINAL]

Here are some examples of what Sentinel policies can enforce:

- All EC2 instances must be of type `t3.micro` or `t3.small` in non-production environments
- S3 buckets must have server-side encryption enabled
- All resources must have a `cost_center` tag
- Production applies must be approved by at least two team members
- Instances cannot have public IP addresses

A Sentinel policy is written in the Sentinel language:

```python
import "tfplan/v2" as tfplan

# Require all S3 buckets to have encryption enabled
all_buckets = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_s3_bucket" and
    (rc.change.actions contains "create" or rc.change.actions contains "update")
}

bucket_encryption_enabled = rule {
    all all_buckets as _, bucket {
        bucket.change.after.server_side_encryption_configuration is not null
    }
}

main = rule {
    bucket_encryption_enabled
}
```

[PAUSE]

### Policy Enforcement Levels

Sentinel policies have three enforcement levels:

- **Advisory** — Policy failures log a warning but the apply is allowed to proceed
- **Soft mandatory** — Policy failures block the apply, but authorized users can override
- **Hard mandatory** — Policy failures always block the apply; cannot be overridden

This graduated enforcement allows teams to introduce policies gradually — starting with advisory, promoting to soft mandatory as teams adapt, then locking down with hard mandatory for critical controls.

[PAUSE]

---

## Section 6: Remote Execution Modes (17:30 – 20:00)

Terraform Cloud workspaces support three execution modes:

### Remote Execution

Plans and applies run on Terraform Cloud's managed agents. All output streams back to the CLI in real time. This is the default and most common mode.

```bash
terraform apply
# Running apply in the remote backend. Output will stream here.
# Waiting for the plan to start...
#
# Terraform v1.5.7
# on linux_amd64
# ...
```

### Local Execution

Plans and applies run locally on your machine, but state is stored in Terraform Cloud. This is useful for development and debugging when you need local execution environment control.

### Agent Execution

Plans and applies run on self-hosted Terraform agents — useful when your infrastructure is in a private network that Terraform Cloud's managed agents cannot reach.

[PAUSE]

---

## Section 7: Team Workflows and Access Control (20:00 – 22:00)

Terraform Cloud provides role-based access control (RBAC) at both the organization and workspace level.

### Organization-Level Roles

- **Owner** — Full control over the organization, teams, and all workspaces
- **Member** — Can be added to teams with workspace-specific permissions

### Team-Level Workspace Permissions

- **Read** — View runs, state, and variables
- **Plan** — Trigger speculative plans
- **Write** — Queue and apply runs, manage variables
- **Admin** — Manage workspace settings and team access

[SHOW TERMINAL]

A typical team structure for a production deployment workflow:

- Developers: Plan permission — they can see what a change would do but cannot apply it
- SRE/Platform team: Write permission — they can apply changes
- Security team: Read + Sentinel policy management — they enforce policies but do not operate infrastructure
- Engineering manager: Admin on workspaces they own

### Run Approvals

In Terraform Cloud you can configure workspaces to require manual approval before applies run. This is the primary mechanism for enforcing a human-in-the-loop review before production changes.

[PAUSE]

---

## Summary and Exam Tips (22:00 – 23:30)

Here is what we covered in Module 11:

- Terraform Cloud provides managed state, remote execution, VCS integration, and governance
- The `cloud` block replaces the `backend` block for Terraform Cloud connections
- Terraform Cloud workspaces are richer than CLI workspaces — they include secrets, run history, and access controls
- Variable sets allow sharing credentials and config across multiple workspaces
- VCS integration enables GitOps — plans run on PR and applies run on merge
- Sentinel provides policy as code with advisory, soft mandatory, and hard mandatory enforcement levels
- Remote, local, and agent execution modes serve different use cases

**For the Terraform Associate exam**, remember:

- `terraform login` generates and stores the API token for Terraform Cloud
- The `cloud` block is preferred over `backend "remote"` for new configurations
- Speculative plans are non-destructive plans run against PRs
- Sentinel is a paid feature (Team tier and above)
- Remote execution uses Terraform Cloud's agents; agent execution uses self-hosted agents
- Variable sets can be applied globally (all workspaces) or to specific workspaces

[PAUSE]

---

## Closing (23:30 – 24:00)

Terraform Cloud is where Terraform grows from a personal tool into a team platform. If you go on to work in infrastructure engineering, you will almost certainly encounter Terraform Cloud or its self-hosted counterpart, Terraform Enterprise.

Congratulations on completing Module 11 and the Modules 07–11 series. You now have a comprehensive foundation in Terraform's advanced features. Keep practicing, take the sample exams, and you will be well-prepared for the Terraform Associate certification.

See you in the next module.

[END OF SCRIPT]
