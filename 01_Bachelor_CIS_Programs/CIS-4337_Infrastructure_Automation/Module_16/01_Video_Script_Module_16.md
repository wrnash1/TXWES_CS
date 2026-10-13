# Video Script: Module 16 — Terraform Associate 003 Exam Preparation and Capstone

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Segment 1: Introduction (Lines 1–18)

Welcome to Module 16, the final module of CIS-4337 Infrastructure Automation. I am Professor Nash.

This module serves two purposes. First, it is a complete review of every Terraform Associate 003 exam objective. Second, it is your capstone — the integration point where everything you have learned across 15 modules comes together.

The Terraform Associate 003 exam covers nine objective domains:

- IaC concepts
- Terraform's purpose in the IaC landscape
- Terraform basics
- Using Terraform outside of core workflow
- Terraform modules
- Core Terraform workflow
- Implementing and maintaining state
- Reading and using the Terraform documentation
- Understanding Terraform Cloud capabilities

We will move through each domain, covering the key concepts and the types of questions the exam asks. Then I will walk you through exam strategy: how to manage time, how to approach tricky questions, and what to study in the final week before your exam date.

Let us begin.

---

## Segment 2: IaC Concepts (Lines 19–40)

Infrastructure as Code is the practice of managing infrastructure through machine-readable configuration files rather than through manual processes. The exam tests your understanding of why IaC matters and what it enables.

The core benefits of IaC are: consistency (every deployment follows the same process), repeatability (you can redeploy the same infrastructure identically as many times as needed), version control (infrastructure history is tracked in git), and collaboration (infrastructure changes go through code review like application code).

The exam distinguishes between declarative and imperative IaC approaches. Terraform is declarative — you describe the desired end state and the tool determines how to achieve it. Ansible in its procedural form is imperative — you write step-by-step instructions. Declarative tools are generally better for infrastructure because you express intent rather than procedure.

Idempotency is a key IaC concept: applying the same configuration multiple times produces the same result. Running `terraform apply` when nothing has changed produces no changes. This is fundamentally different from a shell script that creates a resource unconditionally — running it twice creates two resources.

The exam also tests understanding of IaC benefits versus manual provisioning, and when IaC adoption is appropriate. Know that IaC is not appropriate for ephemeral one-off resources where the overhead of codifying them exceeds the benefit.

---

## Segment 3: Terraform's Purpose (Lines 41–60)

Terraform is an open-source infrastructure provisioning tool created by HashiCorp. It is not a configuration management tool — it does not manage software on running servers. It is a provisioning tool — it creates, modifies, and destroys infrastructure.

The key Terraform differentiators the exam tests are:

Provider ecosystem: Terraform has thousands of providers covering cloud platforms, SaaS services, networking equipment, and security tools. This makes it a single tool for heterogeneous infrastructure.

State management: Terraform maintains a state file that tracks which resources it manages. This is what enables Terraform to calculate the difference between current state and desired configuration.

Execution plans: `terraform plan` shows what will change before any changes are made. This preview-before-change capability is a safety mechanism that manual processes lack.

The exam will ask questions that distinguish Terraform from Ansible, Chef, Puppet, and CloudFormation. Key distinctions: Terraform is cloud-agnostic (unlike CloudFormation which is AWS-only), Terraform is declarative (unlike Ansible's procedural default mode), and Terraform focuses on provisioning (unlike Chef/Puppet which focus on configuration management).

---

## Segment 4: Terraform Basics (Lines 61–85)

The exam covers core HCL concepts thoroughly. Let me review the most tested items.

Resource blocks are the fundamental unit. A resource has a type and a name that together form its address: `aws_instance.web`. The type corresponds to a provider resource. The name is arbitrary and local to the configuration.

Data sources read existing infrastructure without creating or modifying anything. They use the `data` block type and are addressed as `data.aws_ami.ubuntu`.

Variable types: string, number, bool, list, map, set, object, tuple. Know the difference between list (ordered, allows duplicates), set (unordered, no duplicates), and map (key-value pairs). The exam tests type conversion — `toset()`, `tolist()`, `tomap()`.

Output values expose information about your infrastructure. They are accessible via `terraform output` and can be consumed by parent modules or external systems.

Locals are intermediate values computed from other values. They reduce repetition and improve readability. They cannot be overridden from outside the module — they are internal.

Functions: the exam tests commonly used Terraform functions. Know `length()`, `toset()`, `tolist()`, `merge()`, `lookup()`, `contains()`, `flatten()`, `zipmap()`, `format()`, `join()`, `split()`, and `element()`. Know the difference between `coalesce()` and `coalescelist()`.

---

## Segment 5: Terraform Modules (Lines 86–110)

Modules are the primary mechanism for code reuse in Terraform. Every configuration is a module — the root module. Child modules are called from the root using module blocks.

The exam tests:

Module sources: local paths (`./modules/vpc`), Terraform Registry (`hashicorp/consul/aws`), GitHub URLs, and S3 archives. Know that the Terraform Registry URL format includes namespace, module name, and provider.

Module inputs: variables declared in the child module become inputs in the calling module block.

Module outputs: the child module must declare outputs for any values the parent needs. References use `module.module_name.output_name`.

Module versioning: when sourcing from the Terraform Registry, specify a version constraint. This is equivalent to provider version constraints.

Published module standards: a module published to the Terraform Registry must have `main.tf`, `variables.tf`, and `outputs.tf` files. The standard directory structure also includes `README.md` and optionally an `examples/` directory.

The exam distinguishes between the root module (the directory where you run Terraform commands) and child modules (called via module blocks). There is no functional difference in HCL capability — a child module can do anything a root module can do.

---

## Segment 6: Core Workflow (Lines 111–135)

The core Terraform workflow is: write, plan, apply.

The exam tests every CLI command and its purpose:

- `terraform init` — downloads providers, initializes backend, downloads modules. Must be run before any other command in a new directory. Re-run after adding providers or changing backend configuration.
- `terraform validate` — checks HCL syntax. Does not require cloud credentials. Does not contact providers.
- `terraform fmt` — formats configuration files to canonical style. `-check` returns exit code 1 if any file needs formatting.
- `terraform plan` — generates an execution plan showing what will change. Key flags: `-out=tfplan` saves the plan, `-var`, `-var-file`, `-target`, `-destroy`, `-refresh-only`, `-detailed-exitcode`.
- `terraform apply` — applies the plan. With `-auto-approve` skips confirmation. Can take a saved plan file as an argument.
- `terraform destroy` — destroys all managed resources. Equivalent to `terraform apply -destroy`.
- `terraform output` — displays output values. `-raw` strips formatting for scripting.
- `terraform show` — displays state or a saved plan file in human-readable form.
- `terraform state` — subcommands for state manipulation: `list`, `show`, `mv`, `rm`, `pull`, `push`.
- `terraform workspace` — subcommands for workspace management: `new`, `select`, `list`, `show`, `delete`.

The exam particularly tests the difference between `terraform plan -refresh-only` (updates state to match reality without changing infrastructure) and `terraform apply -refresh-only` (same, but also updates the state file).

---

## Segment 7: State Management (Lines 136–162)

State is the most critical concept for the Terraform Associate exam. Know every aspect.

The state file purpose: records the mapping between Terraform resource addresses and real-world resource IDs. Enables Terraform to calculate diffs between configuration and reality.

Remote backends: know the commonly used backends — S3, Azure Blob Storage, GCP Cloud Storage, Terraform Cloud, and the legacy HTTP backend. Each backend has different capabilities for locking, versioning, and encryption.

State locking: prevents concurrent operations that could corrupt state. S3 uses DynamoDB. Other backends have their own mechanisms. `terraform force-unlock` manually releases a stuck lock.

Workspaces: named state file instances within a single backend configuration. The default workspace is called `default`. Workspaces are useful for managing multiple environments (dev, staging, prod) with the same configuration. Inside the configuration, the current workspace name is available as `terraform.workspace`.

Sensitive state: the state file stores all resource attributes including sensitive ones in plaintext unless the backend provides encryption. This is why state access must be controlled.

State drift: `terraform plan` detects drift. `terraform apply -refresh-only` updates state to match reality without making infrastructure changes.

`terraform state mv` moves resources within or between state files. It is the manual counterpart to the `moved` block for situations where the `moved` block cannot be used (different backends).

`terraform state rm` removes a resource from state without destroying it. Used when you want Terraform to stop managing a resource.

---

## Segment 8: Terraform Cloud and Exam Strategy (Lines 163–200)

Terraform Cloud (now called HCP Terraform) provides remote state storage, remote execution, team access controls, Sentinel policy enforcement, and a private module registry.

The exam tests these Terraform Cloud concepts:

Remote runs: plan and apply run on Terraform Cloud infrastructure, not on the engineer's machine. The workspace configuration in the cloud stores all variables and credentials.

Organizations and workspaces: the two-tier structure of Terraform Cloud. An organization contains workspaces. A workspace contains one Terraform configuration, its state, and its run history.

Sentinel: the policy framework for Terraform Cloud. Sentinel policies are written in a DSL that evaluates Terraform plans and enforces organizational rules. A policy can be advisory (warns but allows) or mandatory (blocks apply if violated).

Private Registry: organizations can publish internal modules to a private Terraform Registry hosted by Terraform Cloud. Modules are versioned and accessible to workspaces in the same organization.

Variable sets: reusable collections of variables that can be shared across multiple workspaces. This avoids duplicating provider credentials in every workspace.

Now let me give you exam strategy for the day of the exam.

The Terraform Associate 003 exam is 57 questions in 60 minutes. That is slightly over one minute per question. Do not spend more than 90 seconds on any single question — flag it and move on. You can review flagged questions at the end.

The exam has multiple choice (one correct answer), multiple select (multiple correct answers — the question tells you how many), and true/false questions. Multiple select questions are harder — you must get all correct choices to receive full credit.

Focus your final study week on: state management, the core workflow CLI commands and their flags, module structure and sourcing, and the differences between Terraform, Terraform Cloud, and Terraform Enterprise.

Read the official Terraform documentation for every command. The exam is known to test specific flags and behaviors documented in the official docs that are easy to confuse.

Practice with the free HashiCorp study guide and the sample questions on the HashiCorp learning platform. Hands-on practice is the single most effective preparation method — the exam rewards engineers who have actually used Terraform, not just read about it.

Good luck on your exam. It has been a privilege teaching this course with you.

---

End of Module 16 Video Script
