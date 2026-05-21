# Quiz: Module 01 - IaC Concepts & Benefits
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
What is a primary advantage of declarative IaC over imperative scripting?
*   A) Declarative requires detailing exact deployment commands
*   B) Declarative defines the target end-state; the tool handles deployment steps
*   C) Declarative executes faster than all imperative scripts
*   D) Declarative does not require any configuration files
*   **Correct Answer:** B) Declarative tools (like Terraform) allow you to specify *what* you want, rather than scripting the *how* step-by-step.
*   **Distractor Analysis:**
    *   *Why B is correct:* Terraform's declarative model means you describe the desired end-state in HCL and Terraform figures out the API calls needed to achieve it.
    *   *Why A is incorrect:* Detailing exact deployment commands is the characteristic of imperative scripting, not declarative IaC.
    *   *Why C is incorrect:* Execution speed is not a defining characteristic of the declarative model; the benefit is consistency and idempotency.
    *   *Why D is incorrect:* Declarative IaC requires configuration files (`.tf` files in HCL); they define the desired state.

---

**Question 2**
Which of the following is the most accurate definition of **infrastructure drift** in a Terraform context?
*   A) The automatic scaling of cloud resources based on CPU utilization metrics
*   B) The process of moving a Terraform state file from local storage to a remote backend
*   C) A divergence between the infrastructure's actual deployed state and the desired state defined in Terraform code, typically caused by out-of-band manual changes
*   D) The incremental version history of `.tf` configuration files stored in a Git repository
*   **Correct Answer:** C) Drift is the gap that forms when real-world resources are changed outside of Terraform — for example by a manual console edit — making them no longer match what the HCL code declares.
*   **Distractor Analysis:**
    *   *Why C is correct:* This precisely captures the meaning tested on the Terraform Associate exam: drift = real state diverges from declared state due to changes outside Terraform's control.
    *   *Why A is incorrect:* Auto-scaling is a cloud platform feature unrelated to configuration drift.
    *   *Why B is incorrect:* Moving state to a remote backend is a backend migration, not drift.
    *   *Why D is incorrect:* Git version history tracks code changes, not the divergence of live infrastructure from code.

---

**Question 3**
A team member manually updates a security group rule in the AWS console without updating the Terraform code. What will `terraform plan` report on the next run?
*   A) No changes detected — Terraform ignores out-of-band changes
*   B) A planned change to revert the security group rule back to the state declared in HCL
*   C) An immediate rollback is applied automatically
*   D) The state file is permanently corrupted
*   **Correct Answer:** B) `terraform plan` compares the current real-world state (read via provider APIs) to the desired state in HCL, and proposes changes to reconcile any differences, including reverting manual edits.
*   **Distractor Analysis:**
    *   *Why B is correct:* Terraform refreshes state on each plan and surfaces any drift as a proposed change, giving the operator a chance to review before applying.
    *   *Why A is incorrect:* Terraform does not ignore out-of-band changes; detecting and reconciling them is a core feature.
    *   *Why C is incorrect:* Terraform never applies changes automatically during `plan`; apply is a separate explicit step.
    *   *Why D is incorrect:* A manual cloud console change does not corrupt the state file; it simply causes the next plan to show a diff.

---

**Question 4**
Which of the following best describes the role of the `terraform.tfstate` file?
*   A) A compiled binary that Terraform executes when provisioning resources
*   B) A log file that records every CLI command run in the working directory
*   C) A JSON record that maps Terraform resource declarations to the real-world IDs and attributes of provisioned resources
*   D) A template file that generates HCL code automatically from cloud resource tags
*   **Correct Answer:** C) The state file is Terraform's database of what it manages — it stores the real resource IDs, attributes, and dependencies so Terraform can compute accurate diffs on subsequent runs.
*   **Distractor Analysis:**
    *   *Why C is correct:* The state file is fundamental to Terraform's operation: without it, Terraform cannot determine what already exists or what needs to change.
    *   *Why A is incorrect:* Terraform is not compiled; `.tfstate` is a JSON data file, not an executable.
    *   *Why B is incorrect:* CLI command history is not stored in the state file; that is a shell history function.
    *   *Why D is incorrect:* Terraform does not auto-generate HCL from the state file; `terraform import` adds resources to state but still requires manually written HCL.

---

**Question 5**
When designing infrastructure automation for a Terraform-managed environment, which practice best reduces the risk of configuration drift caused by team members making ad-hoc manual changes to cloud resources?
*   A) Enforce an IaC-only change policy: all infrastructure modifications must go through Terraform code review and `apply`, with IAM permissions restricting direct console access
*   B) Schedule nightly `terraform destroy` runs to reset infrastructure to a known state
*   C) Store the `terraform.tfstate` file in a shared network drive accessible to all team members simultaneously
*   D) Use `terraform taint` on every resource before each deployment to force recreation
*   **Correct Answer:** A) Restricting direct console access and requiring all changes to flow through reviewed Terraform code is the industry best practice for preventing drift in team environments.
*   **Distractor Analysis:**
    *   *Why A is correct:* Combining an IaC-only policy with least-privilege IAM permissions removes the ability to create drift at its source — unauthorized manual changes.
    *   *Why B is incorrect:* Nightly `destroy` runs would delete production infrastructure; this is not a valid drift-prevention strategy.
    *   *Why C is incorrect:* Sharing a state file on a network drive without locking causes state corruption from concurrent writes — the opposite of a best practice.
    *   *Why D is incorrect:* Tainting forces resource recreation on the next apply but does not prevent team members from making manual changes; it does not address the root cause of drift.
