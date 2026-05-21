# Quiz: Module 09 - Terraform Cloud and Terraform Enterprise
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which HCL block is used to connect a Terraform configuration to Terraform Cloud for remote execution and state storage?
*   A) backend "remote"
*   B) cloud
*   C) provider "tfe"
*   D) workspace
*   **Correct Answer:** B) The `cloud` block is the current, recommended way to configure a Terraform Cloud integration. It is placed inside the `terraform {}` block and specifies the organization and workspace. It replaces the older `remote` backend for TFC integrations.
*   **Distractor Analysis:**
    *   *Why B is correct:* The `cloud` block was introduced as the purpose-built TFC integration block. After adding it and running `terraform init`, all subsequent plan and apply operations execute remotely on Terraform Cloud. The exam tests this block name and its placement inside the `terraform {}` configuration block.
    *   *Why A is incorrect:* `backend "remote"` is the legacy way to configure a Terraform Cloud backend. It still works but HashiCorp now recommends the `cloud` block for all new TFC integrations. The exam distinguishes between the two.
    *   *Why C is incorrect:* There is no `provider "tfe"` for connecting to TFC's execution backend. The `tfe` provider exists for managing TFC resources (workspaces, teams, policies) via the TFC API, but it is not used to route plan/apply operations to TFC.
    *   *Why D is incorrect:* `workspace` is not a top-level HCL block. Workspace configuration for TFC is specified as a nested argument inside the `cloud` block, not as a standalone block.

---

**Question 2**
Which of the following most accurately describes how **Terraform Cloud workspaces** differ from **Terraform CLI workspaces**?
*   A) Terraform Cloud workspaces and CLI workspaces are identical in behavior — both share the same configuration code and differ only in state file location
*   B) Terraform Cloud workspaces are fully isolated environments, each with its own configuration code, variables, credentials, and state, while CLI workspaces share one configuration directory and differ only in state
*   C) CLI workspaces are the preferred approach for enterprise teams because they provide stronger access control than Terraform Cloud workspaces
*   D) Terraform Cloud workspaces can only be created through the TFC API and cannot be managed from the Terraform CLI
*   **Correct Answer:** B) TFC workspaces are fully independent environments — each can have completely different configuration code, provider credentials, team access, and variable sets. CLI workspaces share all `.tf` files in a single directory and isolate only the state file. This is a key distinction tested on the exam.
*   **Distractor Analysis:**
    *   *Why B is correct:* The official Terraform documentation explicitly distinguishes these two workspace types. The exam frequently uses a scenario where environments have different configurations or credentials and asks which approach is appropriate — the answer is TFC workspaces (or separate configuration directories), not CLI workspaces.
    *   *Why A is incorrect:* CLI workspaces do share configuration code, but TFC workspaces do not. Saying they are identical misses the fundamental architectural difference.
    *   *Why C is incorrect:* CLI workspaces have no built-in team access control. TFC workspaces provide granular RBAC (read, plan, apply, admin) per team. TFC is the enterprise-preferred approach for access control.
    *   *Why D is incorrect:* TFC workspaces can be created and managed through the TFC UI, TFC API, and also via the `tfe` Terraform provider. They are not restricted to API-only creation.

---

**Question 3**
A company's security policy requires that all Terraform runs execute within their private data center network and that no state data leaves the corporate perimeter. Which HashiCorp product meets this requirement?
*   A) Terraform Cloud (free tier), configured with a local backend override
*   B) Terraform CLI with the S3 remote backend and DynamoDB locking
*   C) Terraform Enterprise, deployed as a self-hosted installation within the company's private network
*   D) Terraform Cloud (plus tier), with IP allowlisting configured to restrict inbound connections
*   **Correct Answer:** C) Terraform Enterprise is the self-hosted version of Terraform Cloud, designed for organizations with air-gapped networks, strict data residency requirements, or private execution environments. All runs and state remain within the organization's infrastructure.
*   **Distractor Analysis:**
    *   *Why C is correct:* The exam tests the distinction between TFC (SaaS — runs and state on HashiCorp infrastructure) and TFE (self-hosted — runs and state on the organization's own infrastructure). When the requirement is private network execution or data residency, TFE is the correct answer.
    *   *Why A is incorrect:* Terraform Cloud is a SaaS product — plan and apply operations execute on HashiCorp's infrastructure. Even with a local backend override, the TFC control plane is still external. This does not satisfy a private data center requirement.
    *   *Why B is incorrect:* S3 + DynamoDB is a valid remote backend for state storage, but it does not provide the Terraform Cloud feature set (VCS integration, Sentinel policies, private registry, run history). More importantly, this approach does not satisfy the "runs within the private data center" requirement for the run execution itself.
    *   *Why D is incorrect:* IP allowlisting controls which IPs can reach TFC, but Terraform's plan and apply operations still execute on HashiCorp's cloud infrastructure. The state and run logs still exist on TFC servers, which does not satisfy a data residency requirement.

---

**Question 4**
Terraform Cloud supports policy-as-code enforcement through Sentinel. When a Sentinel policy is configured as `hard-mandatory`, what happens if an `apply` would violate the policy?
*   A) Terraform Cloud logs the policy violation as a warning in the run history but allows the apply to proceed
*   B) Terraform Cloud pauses the run and sends an email to the workspace owner, who must manually approve or override the policy within 24 hours
*   C) Terraform Cloud blocks the apply from completing — the run fails and the infrastructure change cannot be deployed until the policy is satisfied or the policy itself is changed
*   D) Terraform Cloud automatically modifies the plan to bring it into compliance with the policy before proceeding with the apply
*   **Correct Answer:** C) A `hard-mandatory` Sentinel policy cannot be overridden by any user, including organization owners. If the plan violates a hard-mandatory policy, the apply is blocked entirely. The code or configuration must be changed to pass the policy.
*   **Distractor Analysis:**
    *   *Why C is correct:* The exam tests all three Sentinel policy enforcement levels: `advisory` (warn, allow), `soft-mandatory` (block, but organization owners can override), and `hard-mandatory` (block, no override possible). `hard-mandatory` is the strictest level and completely prevents non-compliant deployments.
    *   *Why A is incorrect:* That behavior describes the `advisory` enforcement level, which logs a warning but does not block the apply.
    *   *Why B is incorrect:* Terraform Cloud does not have a timed approval window for policy overrides. Soft-mandatory policies can be overridden immediately by an organization owner with a single click, not after a 24-hour window.
    *   *Why D is incorrect:* Terraform Cloud does not automatically modify plans to satisfy policies. Policy enforcement is strictly a gate — it either passes or blocks. No automated remediation is applied.

---

**Question 5**
Which Terraform Cloud feature allows teams to publish and share internal, private Terraform modules across their organization, using the same registry address format as the public Terraform Registry?
*   A) VCS integration, which automatically detects and indexes module directories in connected Git repositories
*   B) The Terraform Cloud private module registry, which hosts organization-specific modules at an address in the format `<HOSTNAME>/<NAMESPACE>/<MODULE>/<PROVIDER>`
*   C) Sentinel policies, which enforce that all module calls reference approved source URLs
*   D) Workspace variable sets, which inject module source paths as environment variables at runtime
*   **Correct Answer:** B) The Terraform Cloud private module registry lets organizations publish, version, and share internal modules. Modules in the private registry are called using a four-part address that includes the TFC hostname, making them distinguishable from public registry modules.
*   **Distractor Analysis:**
    *   *Why B is correct:* The private module registry is a first-class TFC feature tested on the exam. The address format `<HOSTNAME>/<NAMESPACE>/<MODULE>/<PROVIDER>` (e.g., `app.terraform.io/my-org/vpc/aws`) is the TFC-specific variant of the three-part public registry format (`hashicorp/consul/aws`). Teams use this to enforce consistent, organization-approved module versions.
    *   *Why A is incorrect:* VCS integration connects workspaces to Git repositories for triggering runs — it does not index or publish modules to a registry. Module publishing to the private registry is a separate, explicit action.
    *   *Why C is incorrect:* Sentinel policies can enforce compliance rules (including requiring specific module sources), but they do not host or serve modules. The registry is the hosting mechanism; Sentinel is the enforcement mechanism.
    *   *Why D is incorrect:* Variable sets inject Terraform variables and environment variables into workspaces at runtime. They have no role in defining or serving module source addresses.
