# Quiz: Module 16 - Final Exam Prep & Terraform Associate 003 Certification

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which command downloads provider plugins, initializes the backend, and installs modules listed in a Terraform configuration — and must be run before any other Terraform workflow command?

* A) `terraform validate`
* B) `terraform init`
* C) `terraform get`
* D) `terraform providers`
* **Correct Answer:** B) `terraform init` is the first command in every Terraform workflow. It reads the configuration's `required_providers` and `backend` blocks, downloads the specified provider plugins into `.terraform/`, configures the state backend, and installs any referenced modules.
* **Distractor Analysis:**
  * *Why B is correct:* `terraform init` is the mandatory initialization step. Without it, no other Terraform command can run successfully because the provider plugins and backend configuration that all subsequent commands depend on have not been established.
  * *Why A is incorrect:* `terraform validate` checks that configuration files are syntactically valid and internally consistent, but it requires providers to already be initialized. Running `validate` before `init` on a fresh configuration will fail because the provider schemas needed for validation have not been downloaded.
  * *Why C is incorrect:* `terraform get` downloads and updates modules referenced in the configuration but does not initialize provider plugins or configure the backend. It is a subset of what `terraform init` does, and `terraform init` is always preferred because it handles all initialization tasks in one command.
  * *Why D is incorrect:* `terraform providers` prints a tree of provider requirements for the current configuration but does not download anything or configure the backend. It is an informational command, not an initialization command.

---

**Question 2**
Which of the following most accurately describes the role of `terraform.tfstate` in the Terraform workflow?

* A) A configuration file that declares the desired end state of infrastructure, which Terraform reads to determine what resources to create
* B) A JSON file maintained by Terraform that maps each resource block in the configuration to the real-world infrastructure object it manages, serving as the source of truth for computing diffs during `terraform plan`
* C) A lock file that prevents concurrent `terraform apply` operations by recording the identity of the process currently modifying infrastructure
* D) A backup file automatically created by Terraform before every `terraform apply` that stores the previous infrastructure configuration for rollback purposes
* **Correct Answer:** B) `terraform.tfstate` is Terraform's state file — a JSON record of which real-world resources are managed by the current configuration, their current attribute values, and their resource addresses. Terraform compares this file against both the configuration and the live provider API during `terraform plan` to compute a diff.
* **Distractor Analysis:**
  * *Why B is correct:* The state file is the central data structure in Terraform's operational model. Every exam domain touches state in some way. Understanding that state records the current known condition of managed resources (not desired state, which is the configuration) is fundamental to answering drift, import, and refactoring questions correctly.
  * *Why A is incorrect:* This describes the HCL configuration files (`.tf` files), not the state file. Configuration expresses desired state. The state file records current known state. The difference between these two concepts — and how `terraform plan` reconciles them — is a core exam topic.
  * *Why C is incorrect:* State locking is implemented through a separate mechanism: a lock record in DynamoDB (for S3 backends), a lock file on disk (for local backends), or Terraform Cloud's built-in locking. The `terraform.tfstate` file itself is not the lock mechanism.
  * *Why D is incorrect:* `terraform.tfstate.backup` is a file Terraform automatically creates before writing a new state (containing the previous state version). It is not the state file itself, and it is not a configuration backup — it is a previous state snapshot, not a configuration rollback point.

---

**Question 3**
A Terraform configuration references a module with `source = "terraform-aws-modules/vpc/aws"`. Where does Terraform download this module from when `terraform init` is run?

* A) From the GitHub repository at `github.com/terraform-aws-modules/vpc/aws` using the Git protocol
* B) From the public Terraform Registry at `registry.terraform.io`, which hosts community and verified modules indexed by `<namespace>/<module>/<provider>`
* C) From a private S3 bucket specified in the `backend "s3"` block, where all external modules must be pre-staged before use
* D) From the HashiCorp official documentation site, which serves module archives alongside provider documentation
* **Correct Answer:** B) A `source` string in the format `<namespace>/<module>/<provider>` without a hostname prefix is resolved against the public Terraform Registry at `registry.terraform.io`. Terraform downloads the specified module version during `terraform init`.
* **Distractor Analysis:**
  * *Why B is correct:* The public Terraform Registry is the default source for modules specified with the `<namespace>/<module>/<provider>` three-part format. This is a directly exam-tested fact. The full implicit source address is `registry.terraform.io/<namespace>/<module>/<provider>`. An explicit hostname prefix is required for private registries or GitHub-sourced modules.
  * *Why A is incorrect:* Sourcing from a GitHub repository requires an explicit `source = "github.com/<org>/<repo>"` or `"git::https://github.com/<org>/<repo>.git"` format. The three-part format without a hostname is registry-specific, not Git-specific.
  * *Why C is incorrect:* The S3 backend stores Terraform state, not module archives. Modules are not sourced from state backends. S3-hosted modules require an explicit `s3::https://` source URL format, not the three-part registry format.
  * *Why D is incorrect:* `developer.hashicorp.com` is a documentation and tutorial site. It does not serve Terraform module archives. Module distribution is handled exclusively by the Terraform Registry, private registries, version control systems, or direct archive URLs.

---

**Question 4**
A practitioner wants to force Terraform to replace a specific resource on the next `terraform apply` without destroying and recreating the entire configuration. Which current best-practice command achieves this?

* A) `terraform taint aws_instance.web` followed by `terraform apply`
* B) `terraform apply -replace="aws_instance.web"`
* C) `terraform state rm aws_instance.web` followed by `terraform apply`
* D) `terraform destroy -target=aws_instance.web` followed by `terraform apply`
* **Correct Answer:** B) `terraform apply -replace="aws_instance.web"` marks the specified resource for replacement in a single command, showing the replacement in the plan before applying. This is the recommended approach introduced in Terraform 0.15.2 as a replacement for the deprecated `terraform taint` command.
* **Distractor Analysis:**
  * *Why B is correct:* The `-replace` flag combines the taint and apply steps into one command with a visible plan step. It is the current HashiCorp-recommended practice and is explicitly tested as the successor to `terraform taint`. It destroys and recreates only the targeted resource while leaving all other resources untouched.
  * *Why A is incorrect:* `terraform taint` was deprecated in Terraform 0.15.2. While it may still function in some Terraform versions, the exam tests current best practices, and the recommended approach is `-replace`. Using deprecated commands is flagged as incorrect on the exam.
  * *Why C is incorrect:* `terraform state rm` removes the resource from state without destroying the real infrastructure, then `terraform apply` creates a new resource alongside the orphaned original. This results in duplicate infrastructure, not a controlled replacement.
  * *Why D is incorrect:* `terraform destroy -target` destroys the resource immediately without a create step. A subsequent `terraform apply` would then recreate it. This two-command approach works but creates a gap where the resource does not exist, causing service disruption. The `-replace` flag does an atomic destroy-and-recreate that minimizes downtime.

---

**Question 5**
At the end of a complete Terraform Associate 003 exam preparation, which of the following study resources is the most authoritative source for confirming which topics will be tested and how they are weighted?

* A) Community blog posts and third-party practice exam providers, which aggregate real exam questions reported by past test-takers
* B) The official HashiCorp Terraform Associate 003 exam review guide and study guide published on the HashiCorp Developer documentation site
* C) The Terraform GitHub repository's CHANGELOG file, which documents every feature added in each release and indicates which features are exam-relevant
* D) The AWS, Azure, and GCP provider documentation pages, which contain all the resource arguments that appear in exam scenario questions
* **Correct Answer:** B) The official HashiCorp exam review guide at `developer.hashicorp.com` is the canonical, authoritative source for exam objectives. It lists every tested topic, maps each to official documentation, and is updated by HashiCorp when the exam blueprint changes.
* **Distractor Analysis:**
  * *Why B is correct:* For any vendor certification, the exam owner's official study guide is always the authoritative source. HashiCorp publishes the Terraform Associate 003 review guide and study guide with explicit objective mappings. Preparing directly from this guide ensures coverage of every tested topic without relying on second-hand reports.
  * *Why A is incorrect:* Community blog posts and brain-dump practice exams may contain inaccurate, outdated, or misremembered questions. Using them as the primary study source risks studying for a different exam version or learning incorrect explanations. They can supplement study but should never be the primary reference.
  * *Why C is incorrect:* The CHANGELOG documents code changes for Terraform developers and operators, not exam objectives. It does not indicate which features are certification-relevant and is not organized around the exam's objective domains.
  * *Why D is incorrect:* Provider documentation covers individual provider-specific resource arguments, which are useful for real-world usage and some exam scenarios. However, the Terraform Associate exam is provider-agnostic — it tests Terraform language, workflow, state, and Cloud concepts, not the specific arguments of AWS, Azure, or GCP resources.
