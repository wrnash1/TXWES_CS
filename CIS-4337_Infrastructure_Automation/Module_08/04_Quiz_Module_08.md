# Quiz: Module 08 - Provisioners and Null Resources
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which provisioner type executes a command on the machine running `terraform apply`, rather than on the newly created remote resource?
*   A) remote-exec
*   B) file
*   C) local-exec
*   D) inline
*   **Correct Answer:** C) `local-exec` runs a command on the machine where Terraform is executing (the local runner or CI agent). It does not connect to the provisioned resource over SSH or WinRM.
*   **Distractor Analysis:**
    *   *Why C is correct:* `local-exec` is the provisioner used when you need to trigger a side-effect on the Terraform runner itself — for example, calling an external API, writing a local inventory file, or invoking Ansible against the new resource. The command runs in a local shell context.
    *   *Why A is incorrect:* `remote-exec` connects to the provisioned resource over SSH or WinRM and runs commands on that machine, not on the local runner.
    *   *Why B is incorrect:* The `file` provisioner copies files or directories from the local machine to the remote resource over SSH or WinRM. It does not execute commands on either machine.
    *   *Why D is incorrect:* `inline` is an argument inside a `remote-exec` provisioner block that accepts a list of commands to run on the remote machine. It is not a provisioner type itself.

---

**Question 2**
Which of the following most accurately describes the **`null_resource`** in Terraform?
*   A) A resource that creates a null (empty) virtual machine with no operating system, used as a placeholder for future infrastructure
*   B) A special resource from the `hashicorp/null` provider that creates no real infrastructure but can have provisioners and lifecycle rules attached to it, re-running whenever its `triggers` map changes
*   C) A built-in Terraform block that marks another resource as optional, so Terraform skips it if the provider returns a null response
*   D) A resource that automatically destroys itself after the first successful `terraform apply`, leaving no trace in state
*   **Correct Answer:** B) `null_resource` is a resource that provisions nothing in any cloud or system, but serves as a vehicle for attaching provisioners to arbitrary trigger conditions. When any value in its `triggers` map changes, Terraform destroys and re-creates the `null_resource`, causing its provisioners to re-run.
*   **Distractor Analysis:**
    *   *Why B is correct:* The `null_resource` is the standard Terraform pattern for running scripts or side-effects in response to upstream changes without creating real infrastructure. The `triggers` argument is the key mechanism that controls when provisioners re-execute. The exam tests this pattern directly.
    *   *Why A is incorrect:* `null_resource` does not provision any virtual machine or cloud resource. The word "null" refers to the absence of managed infrastructure, not an empty VM.
    *   *Why C is incorrect:* There is no built-in Terraform block that marks a resource as optional. Conditional resource creation is handled with `count = 0` or `count = var.enabled ? 1 : 0`.
    *   *Why D is incorrect:* `null_resource` persists in state like any other resource. It is not self-destroying. Removing it from configuration causes Terraform to plan a destroy on the next apply.

---

**Question 3**
A Terraform configuration uses a `remote-exec` provisioner to run an installation script on a newly created EC2 instance. The provisioner command exits with a non-zero status code. What does Terraform do by default?
*   A) Terraform logs the error as a warning and continues with the rest of the apply without modifying the resource's state
*   B) Terraform marks the resource as tainted in state, halts the current apply, and plans to destroy and re-create the resource on the next apply
*   C) Terraform automatically retries the failed provisioner command up to three times before stopping
*   D) Terraform rolls back all changes made during the current apply and restores the previous state file
*   **Correct Answer:** B) The default `on_failure` behavior for a provisioner is `fail` — Terraform marks the resource as tainted and stops the apply. A tainted resource is destroyed and re-created on the next `terraform apply`.
*   **Distractor Analysis:**
    *   *Why B is correct:* This is the exact behavior the exam tests. The resource exists in the real world but its provisioner failed, so Terraform can't confirm it is correctly configured. Tainting signals that the resource must be replaced. You can override this with `on_failure = continue` if you want Terraform to proceed despite the failure.
    *   *Why A is incorrect:* Continuing silently after a provisioner failure is only the behavior when `on_failure = continue` is explicitly set. The default is to fail and taint.
    *   *Why C is incorrect:* Terraform does not have a built-in provisioner retry mechanism. There is no automatic retry count.
    *   *Why D is incorrect:* Terraform does not perform rollbacks. Resources already created during the apply remain in their created state. Terraform is not transactional in the way that database operations are.

---

**Question 4**
HashiCorp's official documentation describes provisioners as a "last resort." A team wants to bootstrap an AWS EC2 instance with a startup script. Which approach does HashiCorp recommend over using a `remote-exec` provisioner?
*   A) Use a `local-exec` provisioner instead, since it avoids the SSH connection requirement
*   B) Use the EC2 instance's `user_data` argument to pass the bootstrap script directly through the provider, keeping the configuration declarative and Terraform-managed
*   C) Use a `null_resource` with a `remote-exec` provisioner and a `depends_on` argument pointing to the EC2 instance
*   D) Split the bootstrap script into a separate Terraform configuration directory and apply it as a second pass after the first apply completes
*   **Correct Answer:** B) Cloud provider resources like `aws_instance` expose a `user_data` argument that passes the startup script to the instance through the provider API. This is fully declarative, requires no SSH connection, and is modeled in the plan — making it strongly preferred over a provisioner.
*   **Distractor Analysis:**
    *   *Why B is correct:* The official Terraform documentation explicitly recommends `user_data` (AWS), `custom_data` (Azure), and equivalent cloud-native mechanisms as alternatives to `remote-exec`. These attributes are tracked in state and shown in plan diffs, whereas provisioner execution is opaque to Terraform.
    *   *Why A is incorrect:* Replacing `remote-exec` with `local-exec` still uses a provisioner — it does not avoid the "last resort" problem. `local-exec` introduces the same state opacity and side-effect issues.
    *   *Why C is incorrect:* This approach still uses a provisioner; wrapping it in a `null_resource` does not resolve the underlying concern about external side-effects being invisible to Terraform's plan.
    *   *Why D is incorrect:* Splitting into a second configuration pass adds operational complexity and does not eliminate the need for a provisioner — it just defers it.

---

**Question 5**
A `null_resource` has the following configuration: `triggers = { instance_id = aws_instance.web.id }`. Under which condition will Terraform destroy and re-create the `null_resource`, causing its provisioners to re-run?
*   A) Every time `terraform plan` is run, regardless of whether the instance ID changes
*   B) Only when the `null_resource` block is removed from the configuration and then re-added
*   C) Whenever the value of `aws_instance.web.id` changes — for example, when the EC2 instance is replaced with a new one that has a different ID
*   D) Only on the first `terraform apply` after the `null_resource` is initially declared; it never re-runs after that
*   **Correct Answer:** C) The `triggers` map causes Terraform to detect a change in the `null_resource` whenever any trigger value changes. Since `aws_instance.web.id` changes when the instance is replaced, the `null_resource` is destroyed and re-created, running its provisioners against the new instance.
*   **Distractor Analysis:**
    *   *Why C is correct:* This is the core exam-tested behavior of `null_resource`. The `triggers` argument is specifically designed to re-run provisioners in response to upstream changes that would otherwise not affect the `null_resource` itself. It is the primary reason `null_resource` exists.
    *   *Why A is incorrect:* `terraform plan` does not cause resources to be re-created. Resources are re-created only when their configuration or trigger values change and `terraform apply` is run.
    *   *Why B is incorrect:* Removing and re-adding a resource from configuration would destroy and re-create it, but this describes manually editing code — not the purpose of the `triggers` mechanism. `triggers` automates re-creation in response to referenced value changes.
    *   *Why D is incorrect:* `null_resource` is not a one-time resource. It will re-run its provisioners whenever a trigger value changes, which can happen on any subsequent apply.
