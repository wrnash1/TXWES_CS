# Reading Guide: Module 08 - Provisioners and Null Resources
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 08 - Provisioners and Null Resources**! This week's study material covers **Terraform provisioners**, which allow you to execute scripts or commands on local or remote machines as part of resource creation and destruction, and the **null_resource**, which lets you attach provisioners to an arbitrary trigger without creating real infrastructure. Both topics are tested on the **HashiCorp Certified: Terraform Associate** exam as part of understanding the full Terraform resource lifecycle.

As a student, you will learn when provisioners are appropriate, how `local-exec` and `remote-exec` differ, why HashiCorp considers provisioners a last resort, and how `null_resource` combined with `triggers` provides a flexible mechanism for running arbitrary side-effects. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Terraform provisioner**: A special block that runs scripts or commands on a local machine (`local-exec`) or on a remote resource (`remote-exec`) during resource creation or destruction. Provisioners are attached inside a `resource` block and run after the resource is created. HashiCorp recommends treating provisioners as a last resort because they introduce external side-effects that Terraform cannot model in its plan or track in state.
*   **`local-exec` provisioner**: Executes a command on the machine running `terraform apply`, not on the provisioned resource. It is used for tasks such as calling an external API, writing a local file, or triggering a configuration management tool like Ansible from the Terraform runner. Example: `command = "echo ${self.public_ip} >> inventory.txt"`.
*   **`remote-exec` provisioner**: Connects to the newly created resource over SSH or WinRM and runs a list of commands or a script on that machine. It requires a `connection` block specifying the protocol, host, user, and authentication method. It is commonly used for bootstrapping software before a configuration management tool takes over.
*   **`null_resource`**: A special resource from the `hashicorp/null` provider that does not create any real infrastructure. It exists solely to attach provisioners to arbitrary triggers. The `triggers` argument accepts a map of values — whenever any trigger value changes, the `null_resource` is re-created, causing its provisioners to re-run. This is the primary use case for `null_resource` on the exam.
*   **`on_failure` provisioner setting**: Controls what Terraform does when a provisioner command exits with a non-zero status. The two values are `continue` (log the error and proceed) and `fail` (the default — mark the resource as tainted and halt the apply). A tainted resource will be destroyed and re-created on the next `terraform apply`.

---

### 2. Certification Exam Tips
*   **Exam Domain — Use Terraform Outside the Core Workflow (Domain 6):** Provisioners and the null provider appear in exam questions focused on resource lifecycle and side-effects. Know the difference between `local-exec` and `remote-exec`, and know when each is used.
*   **Provisioners are a last resort:** The exam may present a scenario asking the best practice for bootstrapping a VM. The correct answer will favor cloud-native mechanisms like `user_data` (AWS) or `custom_data` (Azure) over provisioners wherever possible. Only choose a provisioner when no provider attribute accomplishes the same task.
*   **`null_resource` + `triggers` pattern:** The exam tests that `triggers` is a map of arbitrary key-value pairs. When any value in the map changes between applies, Terraform destroys and re-creates the `null_resource`, causing its provisioners to re-run. This is the standard pattern for re-running a `local-exec` script when an upstream resource changes.
*   **Tainted resources:** When a `remote-exec` provisioner fails with the default `on_failure = fail`, Terraform marks the resource as tainted in state. A tainted resource is destroyed and re-created on the next apply. The exam tests what "tainted" means and how to manually taint or untaint a resource using `terraform taint` and `terraform untaint` (or `terraform apply -replace`).
*   **Study Resource:** The official provisioner documentation explains all provisioner types, the `connection` block syntax, and the recommended alternatives: [HashiCorp Terraform Documentation — Provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax). Pay particular attention to the "Provisioners are a Last Resort" section, which the exam directly references.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the provisioners documentation at [HashiCorp Terraform Documentation — Provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax). This page covers `local-exec`, `remote-exec`, the `connection` block, `on_failure` behavior, and the null provider. The "Last Resort" guidance is exam-critical.
*   **Required Video:** Watch the video lecture on **Provisioners and Null Resources** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the sections demonstrating `local-exec` vs. `remote-exec`, the `connection` block configuration, and the `null_resource` with `triggers` pattern.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Attach a `local-exec` provisioner to a resource**: Add a `provisioner "local-exec"` block inside a resource and use `self.id` to reference the created resource's attribute. Run `terraform apply` and confirm the command executes on the local machine after resource creation.
*   **Use `null_resource` with `triggers`**: Declare a `null_resource` with a `triggers` map referencing another resource's attribute. Apply, then change the upstream resource and re-apply to observe the `null_resource` being re-created and its provisioner re-running.
*   **Observe tainted resource behavior**: Intentionally fail a provisioner command and observe Terraform marking the resource as tainted in state output. Run `terraform apply` again to see Terraform destroy and re-create the tainted resource.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the provisioners documentation at [HashiCorp Terraform Documentation — Provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax).
*   [ ] Watch the video lecture on **Provisioners and Null Resources** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
