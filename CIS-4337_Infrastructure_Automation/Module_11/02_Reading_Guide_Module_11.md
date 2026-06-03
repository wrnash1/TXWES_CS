# Reading Guide: Module 11 — Terraform Cloud and Remote Backends

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Learning Objectives

After completing this reading guide you will be able to:

- Configure a Terraform configuration to use Terraform Cloud via the `cloud` block
- Explain the full feature set of Terraform Cloud workspaces
- Describe how VCS integration enables GitOps workflows
- Write basic Sentinel policies and explain enforcement levels
- Distinguish between remote, local, and agent execution modes
- Apply team-based access control concepts to a real deployment workflow

---

## 1. Terraform Cloud Overview

Terraform Cloud (TFC) is HashiCorp's hosted platform for managing Terraform at team and enterprise scale. It is distinct from the open-source Terraform CLI in several important ways:

| Capability | CLI (Open Source) | Terraform Cloud |
|---|---|---|
| State storage | Local filesystem or self-managed backend | Managed, versioned, encrypted |
| Execution | Developer's local machine | Managed or self-hosted agents |
| Secrets management | Environment variables or external vaults | Workspace-level encrypted variable store |
| Team access control | File system permissions | RBAC with team roles |
| Policy enforcement | None | Sentinel (Team+ tier) |
| VCS integration | None | GitHub, GitLab, Bitbucket, Azure DevOps |
| Run history and audit | None (local logs only) | Full run history with logs and status |

### 1.1 Terraform Cloud vs. Terraform Enterprise

Terraform Enterprise (TFE) is the self-hosted version of Terraform Cloud. It offers the same features as Terraform Cloud Business tier but runs in your own data center or cloud account. For the exam, treat them as functionally equivalent unless a question specifically asks about hosting model.

---

## 2. Connecting to Terraform Cloud

### 2.1 The cloud Block

The `cloud` block is the modern way to connect a configuration to Terraform Cloud. It replaces the older `backend "remote"` syntax.

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

| Argument | Required | Description |
|---|---|---|
| `organization` | Yes | The Terraform Cloud organization name |
| `workspaces.name` | Conditionally | Target a specific workspace by name |
| `workspaces.tags` | Conditionally | Target workspaces matching all given tags |
| `hostname` | No | Defaults to `app.terraform.io`; use for TFE |
| `token` | No | API token; prefer `TF_TOKEN_` env vars instead |

You must specify either `workspaces.name` or `workspaces.tags`, not both.

### 2.2 Authentication

```bash
# Authenticate with Terraform Cloud
terraform login

# Terraform opens a browser to generate a token
# Token is stored in ~/.terraform.d/credentials.tfrc.json
```

For CI/CD pipelines, use environment variables instead of `terraform login`:

```bash
export TF_TOKEN_app_terraform_io="your-api-token"
```

### 2.3 Initialization

After adding the `cloud` block:

```bash
terraform init
```

Terraform detects the cloud backend, prompts for state migration if local state exists, and configures the workspace connection.

### 2.4 The Older backend "remote" Syntax

For reference, the legacy syntax is:

```hcl
terraform {
  backend "remote" {
    organization = "acme-corp"

    workspaces {
      name = "my-app-prod"
    }
  }
}
```

The `cloud` block is preferred for new configurations. The `backend "remote"` syntax still works but does not support all newer Terraform Cloud features.

---

## 3. Terraform Cloud Workspaces

### 3.1 What a TFC Workspace Contains

A Terraform Cloud workspace is a self-contained execution environment:

- **State**: Versioned state file with full history; each apply creates a new state version
- **Variables**: Terraform variables and environment variables, stored encrypted
- **Run history**: Log of every plan and apply, with streaming output
- **Access controls**: Team-level permissions (read, plan, write, admin)
- **VCS connection**: Link to a repository and branch (if configured)
- **Settings**: Execution mode, Terraform version, auto-apply flag, run triggers

### 3.2 Workspace Variables

Variables in Terraform Cloud are set at the workspace level through the UI, API, or variable sets.

**Terraform variables** — equivalent to input variables (`var.region`):

```
Key:   region
Value: us-east-1
```

**Environment variables** — available as shell environment variables during execution:

```
Key:   AWS_ACCESS_KEY_ID
Value: AKIAIOSFODNN7EXAMPLE
```

Both types can be marked **Sensitive**, which hides the value in the UI and prevents it from being read back through the API.

### 3.3 Variable Sets

Variable sets are collections of variables that can be applied to multiple workspaces simultaneously.

Common use cases:

- **Global variable set**: Common tags (`Owner`, `CostCenter`) applied to all workspaces in the organization
- **Cloud credentials**: AWS, Azure, or GCP credentials applied to all production workspaces
- **Environment-specific configs**: Shared variables for all workspaces in a specific environment

Variable sets eliminate the need to duplicate variable definitions across dozens of workspaces.

---

## 4. Remote Execution

### 4.1 Execution Modes

| Mode | Where runs execute | Best for |
|---|---|---|
| Remote | Terraform Cloud's managed agents | Teams; standard use case |
| Local | Developer's local machine | Development and debugging |
| Agent | Self-hosted Terraform agents | Private network access |

### 4.2 Remote Execution Workflow

When using remote execution:

1. `terraform plan` or `terraform apply` is run on the local CLI
2. The CLI packages configuration files and uploads them to Terraform Cloud
3. Terraform Cloud queues the run in the workspace
4. A managed agent picks up the run, downloads providers, and executes
5. Output streams back to the local CLI in real time
6. State is saved to the workspace in Terraform Cloud

### 4.3 Self-Hosted Agents

Terraform Cloud agents are used when the target infrastructure is in a private network. An agent is a lightweight process running inside the private network that polls Terraform Cloud for work.

```bash
# Install and register a Terraform agent
terraform-agent \
  --token="<agent-pool-token>" \
  --address="https://app.terraform.io"
```

---

## 5. VCS Integration

### 5.1 Connecting a Workspace to VCS

Supported VCS providers:

- GitHub and GitHub Enterprise
- GitLab and GitLab Self-Managed
- Bitbucket Cloud and Bitbucket Server
- Azure DevOps

When a workspace is connected to a VCS repository:

- Pushes to the configured branch trigger plans
- Pull requests receive speculative plan results as comments
- Merges to the production branch can auto-apply or wait for confirmation

### 5.2 Speculative Plans

A speculative plan is a read-only plan run against the current state without locking it or allowing an apply. It is triggered automatically on pull requests.

Characteristics:

- Does not lock state
- Cannot be applied
- Posts results to the PR as a comment
- Shows what infrastructure changes the PR would produce

### 5.3 GitOps Workflow

```
1. Developer creates branch and modifies .tf files
2. Pull request opened
3. Terraform Cloud detects PR → runs speculative plan
4. Plan results appear as PR comment
5. Team reviews plan output alongside code changes
6. PR merged to main branch
7. Terraform Cloud detects merge → runs plan + apply
8. If manual approval configured: team member reviews and approves
9. Apply executes; state updated in workspace
```

---

## 6. Sentinel — Policy as Code

### 6.1 What Is Sentinel

Sentinel is HashiCorp's policy as code framework. It is available on Terraform Cloud's Team and Business tiers. Sentinel policies run in the **policy check** phase — after a plan completes but before an apply can be triggered.

### 6.2 Policy Enforcement Levels

| Level | Behavior |
|---|---|
| Advisory | Failure logs a warning; apply proceeds |
| Soft mandatory | Failure blocks apply; authorized users can override |
| Hard mandatory | Failure always blocks apply; cannot be overridden |

### 6.3 Sentinel Policy Examples

**Require instance type to be in an approved list**:

```python
import "tfplan/v2" as tfplan

allowed_types = ["t3.micro", "t3.small", "t3.medium"]

all_instances = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_instance" and
    (rc.change.actions contains "create" or rc.change.actions contains "update")
}

instance_types_valid = rule {
    all all_instances as _, instance {
        instance.change.after.instance_type in allowed_types
    }
}

main = rule {
    instance_types_valid
}
```

**Require all resources to have specific tags**:

```python
import "tfplan/v2" as tfplan

required_tags = ["Environment", "Owner", "CostCenter"]

all_resources = filter tfplan.resource_changes as _, rc {
    rc.change.actions contains "create"
}

tags_present = rule {
    all all_resources as _, resource {
        all required_tags as tag {
            resource.change.after.tags[tag] is not null
        }
    }
}

main = rule {
    tags_present
}
```

### 6.4 Policy Sets

Policies are organized into **policy sets**, which are then applied to specific workspaces or to all workspaces in an organization. A policy set is typically stored in a VCS repository for version control.

---

## 7. Team Workflows and Access Control

### 7.1 Organization Roles

- **Owner**: Full administrative control over the organization
- **Member**: Access to workspaces is controlled by team membership

### 7.2 Workspace Permission Levels

| Permission | Capabilities |
|---|---|
| Read | View runs, state, variables (non-sensitive), workspace settings |
| Plan | All of Read + trigger speculative plans |
| Write | All of Plan + queue and confirm applies, manage variables |
| Admin | All of Write + manage workspace settings and team access |

### 7.3 Run Confirmation

Workspaces can be configured to:

- **Auto-apply**: Apply runs automatically after a successful plan
- **Manual confirmation**: A team member with Write or Admin permission must confirm the apply

Manual confirmation is the recommended setting for production workspaces.

---

## 8. Command Reference

| Command | Description |
|---|---|
| `terraform login` | Authenticate with Terraform Cloud; stores token |
| `terraform logout` | Remove stored Terraform Cloud credentials |
| `terraform init` | Initialize and connect to Terraform Cloud workspace |
| `terraform plan` | Queue and stream a plan run in Terraform Cloud |
| `terraform apply` | Queue, stream, and confirm an apply run |
| `terraform workspace list` | List Terraform Cloud workspaces (cloud backend) |
| `terraform workspace select <name>` | Switch to a different Terraform Cloud workspace |

---

## 9. Exam Tips — Terraform Associate 003

1. **`cloud` block vs. `backend "remote"`**: Both connect to Terraform Cloud; `cloud` is preferred for new configurations and supports more features.

2. **`terraform login` stores a token**: The token goes to `~/.terraform.d/credentials.tfrc.json`. For CI/CD, use `TF_TOKEN_app_terraform_io`.

3. **TFC workspaces vs. CLI workspaces**: TFC workspaces are full environments with state, variables, and runs. CLI workspaces only isolate state within a local configuration.

4. **Speculative plans cannot be applied**: They are read-only plans triggered on PRs; they do not lock state.

5. **Sentinel is a paid feature**: It requires the Team tier or above; it is not available on the free tier.

6. **Hard mandatory cannot be overridden**: Only hard mandatory prevents an apply with no override path. Soft mandatory can be overridden by authorized users.

7. **Variable sets**: Shared across multiple workspaces; global variable sets apply to all workspaces in the organization.

8. **Agent execution**: For infrastructure in private networks; agents run inside the private network and poll Terraform Cloud for jobs.

9. **Auto-apply**: Can be enabled per workspace; typically off for production environments to require human confirmation.

---

## 10. Summary

Terraform Cloud transforms Terraform from a single-user CLI tool into a team-scale platform. Its key differentiators over the open-source CLI are managed remote execution, workspace-level secrets, VCS-triggered workflows, Sentinel policy enforcement, and role-based access control.

Understanding the architecture of Terraform Cloud — particularly how workspaces, runs, variables, and policies interact — is essential for both the Terraform Associate exam and for any team operating Terraform in production.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
