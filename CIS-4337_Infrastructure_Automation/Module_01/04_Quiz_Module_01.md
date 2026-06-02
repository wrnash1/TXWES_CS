# CIS-4337 Infrastructure Automation

## Quiz — Module 01: IaC Concepts and Benefits

### Course Alignment: HashiCorp Terraform Associate 003

---

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

What is the primary advantage of the declarative IaC model over imperative scripting?

- A) Declarative configurations require you to detail every deployment command step by step.
- B) Declarative configurations define the desired end state and let the tool determine how to achieve it.
- C) Declarative configurations always execute faster than imperative scripts.
- D) Declarative configurations do not require any files to be stored on disk.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Terraform's declarative model means you write HCL describing what you want to exist. Terraform computes the required API calls, dependency order, and error handling automatically. You specify the destination, not the route.
- Why A is incorrect: Describing every step is the defining characteristic of imperative scripting, not declarative IaC.
- Why C is incorrect: Execution speed is not what distinguishes the declarative model. The defining benefit is idempotency and automatic dependency resolution, not raw speed.
- Why D is incorrect: Declarative IaC absolutely requires configuration files. In Terraform, those are `.tf` files written in HCL.

---

### Question 2

Which of the following most accurately defines configuration drift in a Terraform-managed environment?

- A) The automatic horizontal scaling of cloud resources in response to increased CPU utilization.
- B) The migration of a Terraform state file from a local directory to a remote backend.
- C) The divergence between the actual deployed state of infrastructure and the desired state declared in Terraform code, typically caused by out-of-band manual changes.
- D) The incremental version history of `.tf` files accumulated in a Git repository over time.

Correct Answer: C

Distractor Analysis:

- Why C is correct: Drift occurs when someone makes a change to live infrastructure — for example, editing a security group rule in the AWS console — without updating the corresponding Terraform configuration. The real state and the declared state no longer agree.
- Why A is incorrect: Auto-scaling is a cloud platform feature that adjusts resource capacity. It has no relation to the concept of configuration drift.
- Why B is incorrect: Moving state to a remote backend is a backend migration operation, not drift.
- Why D is incorrect: Git history records code changes over time. Drift is about the gap between code and live infrastructure, not about version history.

---

### Question 3

A developer manually changes an S3 bucket's ACL setting through the AWS console without updating the Terraform configuration. What will `terraform plan` report on the next run?

- A) No changes — Terraform ignores out-of-band changes to managed resources.
- B) A proposed change to revert the ACL setting to the value declared in the HCL configuration.
- C) An immediate automatic rollback is triggered without requiring an apply.
- D) The state file becomes permanently corrupted and must be rebuilt from scratch.

Correct Answer: B

Distractor Analysis:

- Why B is correct: During `terraform plan`, Terraform refreshes its knowledge of live resource attributes by querying provider APIs. When it detects that the actual ACL differs from what HCL declares, it proposes a change to reconcile the difference.
- Why A is incorrect: Ignoring out-of-band changes would defeat the core purpose of IaC. Terraform detects and surfaces drift as a planned change.
- Why C is incorrect: Terraform never automatically applies changes. The plan phase is always a read-only preview; changes require an explicit `terraform apply`.
- Why D is incorrect: A manual console change does not touch the state file at all. The state file remains intact; it simply no longer reflects the current live state until the next plan refreshes it.

---

### Question 4

Which of the following best describes the role of the `terraform.tfstate` file?

- A) A compiled binary that Terraform executes when provisioning infrastructure resources.
- B) A log file that records every CLI command ever run in the working directory.
- C) A JSON record that maps Terraform resource declarations to the real-world IDs and current attributes of provisioned resources.
- D) A template file that auto-generates HCL configurations from cloud resource metadata.

Correct Answer: C

Distractor Analysis:

- Why C is correct: The state file is Terraform's source of truth about what it manages. It stores real resource IDs, current attribute values, and resource dependencies so Terraform can compute accurate diffs on subsequent runs.
- Why A is incorrect: Terraform is not compiled and does not produce executables. The `.tfstate` file is a plain JSON text file.
- Why B is incorrect: CLI command history is maintained by the shell, not by Terraform. The state file records resource state, not command history.
- Why D is incorrect: Terraform does not auto-generate HCL from resource metadata. You write HCL manually, and `terraform import` can bring existing resources into state management, but it still requires hand-written resource blocks.

---

### Question 5

An organization wants to prevent configuration drift caused by team members making ad-hoc changes through the AWS console. Which practice best addresses this problem?

- A) Enforce an IaC-only policy requiring all infrastructure changes to flow through reviewed Terraform code, and restrict direct console access using IAM permission boundaries.
- B) Schedule nightly `terraform destroy` runs to reset all infrastructure to a known clean state.
- C) Store the `terraform.tfstate` file on a shared network drive accessible to all team members simultaneously without file locking.
- D) Run `terraform taint` on every resource before each deployment to force recreation of all resources.

Correct Answer: A

Distractor Analysis:

- Why A is correct: Combining an IaC-only change policy with IAM restrictions eliminates the source of drift. If team members cannot make manual console changes, they cannot create drift. Code review catches unintended changes before apply.
- Why B is incorrect: Nightly destroys would delete production workloads. This is not a drift prevention strategy; it is a data-loss strategy.
- Why C is incorrect: Sharing a state file without locking leads to concurrent write conflicts and state corruption. This is a well-documented anti-pattern.
- Why D is incorrect: Tainting forces resource recreation on the next apply but does nothing to prevent team members from making manual changes. It does not address the root cause of drift.

---

### Question 6

Which of the following characteristics distinguishes Terraform from AWS CloudFormation?

- A) Terraform uses an imperative model while CloudFormation uses a declarative model.
- B) Terraform requires manual state management while CloudFormation manages state automatically.
- C) Terraform can manage resources across multiple cloud providers and SaaS platforms while CloudFormation is limited to AWS resources.
- D) Terraform is a commercial product that requires a paid license while CloudFormation is free.

Correct Answer: C

Distractor Analysis:

- Why C is correct: Terraform's provider model enables a single configuration to manage AWS, Azure, Google Cloud, GitHub, Datadog, and hundreds of other platforms simultaneously. CloudFormation only manages AWS resources.
- Why A is incorrect: Both Terraform and CloudFormation use the declarative model. You describe desired state in both tools.
- Why B is incorrect: Both tools maintain state. Terraform uses `.tfstate` files or remote backends. CloudFormation maintains stack state internally within the AWS service.
- Why D is incorrect: The open-source Terraform CLI is free. CloudFormation is also free. Paid tiers exist for Terraform Cloud and Terraform Enterprise, but the CLI itself does not require a license.

---

### Question 7

What does the term "idempotent" mean in the context of Terraform?

- A) Terraform can only be run once per infrastructure environment before requiring a full reinstall.
- B) Running `terraform apply` multiple times with the same configuration produces the same result — no additional changes are made if infrastructure already matches the declared state.
- C) Terraform automatically scales resources up and down based on current workload demand.
- D) Terraform generates a unique random identifier for every resource on each run to ensure freshness.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Idempotency is a core property of Terraform's declarative model. If the live infrastructure already matches the HCL configuration, `terraform apply` makes zero changes. You can run it safely any number of times.
- Why A is incorrect: Terraform can be run any number of times. There is no one-run limit.
- Why C is incorrect: Auto-scaling is a cloud platform feature configured through resource attributes. It is not what idempotent means.
- Why D is incorrect: Terraform does not generate new random identifiers on every run. Resource IDs are assigned once at creation and remain stable across subsequent applies.

---

### Question 8

In the Terraform Write-Plan-Apply workflow, what is the specific purpose of the `terraform plan` command?

- A) It downloads and installs all required provider plugins into the working directory.
- B) It applies configuration changes immediately without showing a preview.
- C) It computes and displays an execution plan showing what changes Terraform will make, without actually making any changes.
- D) It permanently deletes all resources managed by the current configuration.

Correct Answer: C

Distractor Analysis:

- Why C is correct: `terraform plan` is a read-only operation. It refreshes state, computes the diff between desired and current state, and displays a detailed preview of every planned action. No resources are created, modified, or destroyed.
- Why A is incorrect: Downloading and installing provider plugins is the job of `terraform init`.
- Why B is incorrect: Applying changes without a preview describes `terraform apply -auto-approve`, not `terraform plan`. Even `terraform apply` without flags shows the plan and requires confirmation.
- Why D is incorrect: Destroying all managed resources is the job of `terraform destroy`.

---

### Question 9

Which of the following is a correct statement about the `.terraform.lock.hcl` file created by `terraform init`?

- A) It prevents any other user from running Terraform commands in the same directory simultaneously.
- B) It records the exact versions of provider plugins selected during initialization so that subsequent runs use the same versions.
- C) It encrypts the state file to prevent unauthorized access to sensitive resource attributes.
- D) It stores the Terraform execution plan from the most recent `terraform plan` run.

Correct Answer: B

Distractor Analysis:

- Why B is correct: The dependency lock file records the exact provider version selected during `terraform init`, along with checksums. This ensures that all team members and CI/CD pipelines use identical provider versions, preventing "works on my machine" problems.
- Why A is incorrect: File-level locking to prevent concurrent CLI runs is not what `.terraform.lock.hcl` does. State locking (preventing concurrent applies) is handled by backends, not by this file.
- Why C is incorrect: The lock file does not encrypt the state file. State encryption is handled separately through backend configuration or Terraform Cloud.
- Why D is incorrect: Execution plans are not stored in the lock file. A plan can be saved to a binary file using `terraform plan -out=tfplan`, but that is a separate artifact.

---

### Question 10

A team is deciding whether to use Terraform or Ansible for provisioning new cloud infrastructure. Based on the IaC principles covered in this module, which statement best justifies choosing Terraform for this task?

- A) Ansible is declarative and therefore better suited to describing desired infrastructure state.
- B) Terraform's declarative model and state management make it purpose-built for provisioning infrastructure and tracking resource lifecycle, while Ansible is better suited to configuring software on existing servers.
- C) Terraform and Ansible are functionally identical; the choice depends only on personal preference.
- D) Ansible should always be chosen over Terraform because it supports more cloud providers.

Correct Answer: B

Distractor Analysis:

- Why B is correct: Terraform is designed for infrastructure provisioning — creating, modifying, and destroying cloud resources. Its state file tracks resource lifecycle. Ansible excels at configuration management: installing packages, managing files, and configuring services on existing servers. The two tools are complementary, not interchangeable.
- Why A is incorrect: Ansible can be used in a declarative style, but it is primarily an imperative task-execution engine. Terraform is the more consistently declarative tool for infrastructure provisioning.
- Why C is incorrect: The two tools have distinct design philosophies, strengths, and use cases. The choice is not arbitrary.
- Why D is incorrect: Ansible does not support more cloud providers than Terraform in the infrastructure provisioning context. Terraform's provider ecosystem is among the largest in the industry.

---

Module 01 Quiz — CIS-4337 Infrastructure Automation — Texas Wesleyan University
