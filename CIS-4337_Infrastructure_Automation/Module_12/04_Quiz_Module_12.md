# Quiz: Module 12 - Drift Management & Importing Existing Resources

## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which command reads real-world resource attributes and registers them inside your local state file without creating or modifying any infrastructure?

* A) `terraform apply`
* B) `terraform import`
* C) `terraform plan`
* D) `terraform state push`
* **Correct Answer:** B) `terraform import` reads the target resource by its provider-specific ID and populates the Terraform state file with its attributes. You must separately write the matching HCL `resource` block.
* **Distractor Analysis:**
  * *Why B is correct:* `terraform import` is the only command designed to bring an existing, unmanaged resource into Terraform state. It performs a read-only API call to fetch resource attributes and writes them to state — it does not create, update, or destroy infrastructure.
  * *Why A is incorrect:* `terraform apply` creates or modifies infrastructure to match desired state. It does not read an existing resource and register it; running apply on a new resource block would attempt to create a second copy of the resource.
  * *Why C is incorrect:* `terraform plan` computes a diff between desired configuration and current state but does not write anything to the state file. It would show a plan to create the resource if no state entry exists.
  * *Why D is incorrect:* `terraform state push` uploads a local state file to a remote backend, overwriting what is there. It is used for disaster recovery, not for importing individual resources.

---

**Question 2**
Which of the following most accurately describes **infrastructure drift** in the context of Terraform?

* A) The gradual increase in the size of the Terraform state file as more resources are added to a configuration over time
* B) The condition where real-world resource configuration has diverged from what Terraform's state file records, typically due to manual out-of-band changes made outside of Terraform
* C) A version mismatch between the Terraform CLI binary and the provider plugin installed in the `.terraform` directory
* D) The delay between when `terraform apply` is run and when cloud provider APIs complete resource provisioning
* **Correct Answer:** B) Drift occurs when someone modifies infrastructure directly — through the cloud console, CLI, or another tool — without going through Terraform, causing the actual resource state to differ from what Terraform expects.
* **Distractor Analysis:**
  * *Why B is correct:* This is the precise, exam-tested definition of infrastructure drift. Drift is detected when `terraform plan` shows changes that were not initiated by a configuration update — the diff reflects reality diverging from desired state recorded in the state file.
  * *Why A is incorrect:* State file growth is a normal consequence of managing more resources and is not called drift. Drift specifically refers to a divergence between actual and recorded resource attributes, not file size.
  * *Why C is incorrect:* A version mismatch between the CLI and provider plugin causes a compatibility error during `terraform init` or `terraform plan`, not drift. Drift is a runtime infrastructure condition, not a tooling version issue.
  * *Why D is incorrect:* API provisioning latency is an operational characteristic of cloud providers, not a Terraform-specific concept. It does not describe a relationship between desired state and actual state.

---

**Question 3**
After running `terraform import aws_instance.web i-0abc123`, a practitioner immediately runs `terraform plan`. What is the most likely outcome?

* A) Terraform reports no changes because the import synchronized the configuration with real infrastructure
* B) Terraform shows a plan to destroy `aws_instance.web` because no matching HCL `resource` block has been written yet
* C) Terraform generates the HCL `resource` block automatically from the imported state and writes it to `main.tf`
* D) Terraform reports an error stating the state file is locked and must be unlocked before planning
* **Correct Answer:** B) `terraform import` only writes to state. Without a corresponding `resource "aws_instance" "web"` block in the configuration, Terraform sees a state entry with no matching configuration and plans to destroy the orphaned resource.
* **Distractor Analysis:**
  * *Why B is correct:* This outcome is the most critical exam point about `terraform import`. State and configuration must both be present and aligned. Import populates only state; the practitioner must write the HCL and then iteratively run `terraform plan` until no diff remains.
  * *Why A is incorrect:* Import does not synchronize configuration — it only updates state. A clean plan requires both a matching resource block in HCL and state entries that reflect actual infrastructure attributes.
  * *Why C is incorrect:* `terraform import` has never automatically generated HCL in the classic CLI workflow. The newer config-driven `import` block (Terraform 1.5+) combined with `terraform plan -generate-config-out` can generate HCL, but this is a distinct, opt-in feature requiring explicit configuration.
  * *Why D is incorrect:* State locking is a concurrency control mechanism activated during write operations. Running `terraform plan` after an import does not encounter locking errors under normal circumstances.

---

**Question 4**
A cloud engineer manually deleted a security group rule directly in the AWS console without using Terraform. When the team next runs `terraform plan`, which behavior should they expect?

* A) Terraform detects no change because the state file was automatically updated when the console change was saved
* B) Terraform shows a plan to recreate the deleted security group rule in order to restore infrastructure to the desired state defined in the configuration
* C) Terraform permanently removes the security group rule from the configuration file to match the current real-world state
* D) Terraform locks the state file and requires an administrator to manually run `terraform refresh` before any further operations are possible
* **Correct Answer:** B) During `terraform plan`, Terraform refreshes state by querying the provider API. It detects the missing rule and computes a diff showing it will add the rule back to match the desired configuration.
* **Distractor Analysis:**
  * *Why B is correct:* Terraform's desired state is defined in HCL configuration. When real infrastructure diverges, `terraform plan` shows the changes needed to restore the desired state. The default behavior is always to reconcile infrastructure to match configuration, not the other way around.
  * *Why A is incorrect:* Terraform state is not automatically updated by cloud console actions. State is only updated when Terraform itself performs a refresh or apply operation. This is precisely why drift can accumulate undetected.
  * *Why C is incorrect:* Terraform never modifies `.tf` configuration files automatically. Configuration is always managed by the practitioner. Terraform only modifies state files and real infrastructure — never source files.
  * *Why D is incorrect:* `terraform plan` does not lock the state file in a way that requires administrator intervention. State locking is a short-lived concurrency control released automatically after each operation completes.

---

**Question 5**
Which `terraform state` subcommand would you use to remove a resource from Terraform state management without destroying the real infrastructure it represents?

* A) `terraform state delete`
* B) `terraform state rm`
* C) `terraform state detach`
* D) `terraform state purge`
* **Correct Answer:** B) `terraform state rm <resource_address>` removes the specified resource's entry from the state file. The real infrastructure is left untouched — Terraform simply stops tracking it.
* **Distractor Analysis:**
  * *Why B is correct:* `terraform state rm` is the correct and documented command for this operation. It is commonly used when a resource needs to be removed from Terraform management without destroying the underlying cloud resource — for example, when moving a resource to a different Terraform root module or simply abandoning IaC management of a resource.
  * *Why A is incorrect:* `terraform state delete` is not a valid Terraform CLI subcommand. The correct subcommand for removal is `terraform state rm`.
  * *Why C is incorrect:* `terraform state detach` does not exist as a Terraform CLI command. There is no `detach` subcommand in the `terraform state` family of commands.
  * *Why D is incorrect:* `terraform state purge` is not a valid Terraform CLI subcommand. Bulk state cleanup is done by running `terraform state rm` for each resource address or by directly editing the state file using `terraform state pull` and `terraform state push`.
