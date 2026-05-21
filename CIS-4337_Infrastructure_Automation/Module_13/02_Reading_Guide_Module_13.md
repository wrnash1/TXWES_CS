# Reading Guide: Module 13 - Terraform Cloud & the Public Registry

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction

Welcome to **Module 13 - Terraform Cloud & the Public Registry**! This week's study material focuses on HashiCorp's managed service platform, Terraform Cloud, and the public Terraform Registry. Terraform Cloud provides remote state storage, remote plan/apply execution, policy enforcement, and VCS integration — all heavily tested on the Terraform Associate exam. The Terraform Registry is the canonical source for public provider and module discovery.

As a student, you will learn how Terraform Cloud workspaces differ from CLI workspaces, how to connect a workspace to a VCS repository, what triggers a run, how the private registry works, and how run triggers chain dependent workspaces. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Terraform Cloud workspaces**: Managed execution environments in Terraform Cloud that each hold their own state, variables, and run history. Unlike CLI workspaces (which share a single configuration directory and backend), Terraform Cloud workspaces are independent units — each typically corresponds to a separate root module or environment and can be connected to a different VCS branch or repository.
* **VCS connection**: An integration between a Terraform Cloud workspace and a version control system repository (GitHub, GitLab, Bitbucket, etc.). When a VCS connection is configured, Terraform Cloud automatically triggers a speculative plan on pull requests and a full run on merges to the tracked branch, enabling GitOps-style infrastructure workflows.
* **private registry**: A Terraform Cloud feature that allows organizations to publish and share internal Terraform modules and providers within their organization. It mirrors the public Terraform Registry's interface but restricts access to authenticated members of the organization, enabling module reuse without public exposure.
* **run triggers**: A Terraform Cloud feature that connects workspaces so that a completed apply in one workspace automatically queues a run in one or more downstream workspaces. This enables multi-workspace dependency chains — for example, a networking workspace completing triggers a compute workspace that depends on its outputs.

---

### 2. Certification Exam Tips

* **Terraform Cloud workspace vs. CLI workspace:** This distinction is heavily tested. CLI workspaces (`terraform workspace new`) are state-isolation containers within a single root module sharing one backend. Terraform Cloud workspaces are full independent projects with separate state, variables, runs, and optional VCS connections. They are fundamentally different concepts that happen to share the word "workspace."
* **Remote backend vs. cloud block:** Know that configuring Terraform Cloud as a backend can be done with either the legacy `backend "remote"` block or the newer `cloud` block (recommended in Terraform 1.1+). The `cloud` block supports tag-based workspace filtering; the `backend "remote"` block requires an explicit workspace name or prefix.
* **Speculative plans:** When a VCS-connected workspace receives a pull request, Terraform Cloud runs a speculative plan — a read-only plan that cannot be applied. Results are posted as a status check on the pull request. Know that speculative plans do not lock state and are not billable as full runs.
* **Study Resource:** The Terraform Cloud documentation covers workspace types, VCS connections, the private registry, and run triggers in detail: [Terraform Cloud Documentation — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/cloud-docs).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the Terraform Cloud overview and workspace documentation, focusing on workspace types, VCS-driven workflows, and the private module registry: [Terraform Cloud Documentation — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/cloud-docs).
* **Required Video:** Watch the video lecture on **Terraform Cloud & the Public Registry** in the official course playlist, which demonstrates creating a Terraform Cloud workspace, connecting it to a GitHub repository, and observing how a code push triggers a remote run: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Configure a Terraform Cloud workspace and connect it to a VCS repository**: Create a workspace in Terraform Cloud, connect it to a GitHub repository using the OAuth app integration, and set the working directory if the repository contains multiple root modules. Observe that pushing a commit triggers a new run automatically.
* **Examine VCS trigger behaviors on pull requests**: Open a pull request against the tracked branch and observe the speculative plan posted as a pull request status check. Confirm that the speculative plan is read-only and cannot be applied directly from the PR.
* **Map the run approval workflow**: Review the Terraform Cloud run queue for a workspace and step through the plan-then-apply workflow, noting where human approval is required before the apply stage proceeds. Understand how sentinel policies or OPA policies can add automated approval gates.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
* [ ] Read the Terraform Cloud workspace and VCS documentation at [Terraform Cloud Documentation — HashiCorp Developer Docs](https://developer.hashicorp.com/terraform/cloud-docs).
* [ ] Watch the video lecture on **Terraform Cloud & the Public Registry** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
