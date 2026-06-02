# CIS-4337 Infrastructure Automation

## Module 01: IaC Concepts and Benefits

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Hello and welcome to CIS-4337 Infrastructure Automation at Texas Wesleyan University. I am Professor Nash, and this first module lays the intellectual foundation for everything that follows: Infrastructure as Code, commonly abbreviated IaC.

By the end of this video you will be able to define Infrastructure as Code, explain the specific problems it solves, articulate its core benefits, distinguish between the declarative and imperative approaches, and place Terraform in the broader ecosystem of automation tools. You will also understand why the Terraform Associate 003 certification exam places IaC concepts in its very first domain.

Before we write a single line of configuration, we need to ask an honest question: what was wrong with the way organizations provisioned infrastructure before tools like Terraform existed? The answer to that question is the entire reason this course exists.

---

## Section 2: The Pre-IaC World — 1:30–5:30

Imagine it is 2010. Your organization needs a new web server. What happens?

Someone opens a ticket. A systems administrator logs into a hosting console, clicks through a series of menus, fills out forms, selects an operating system image, picks a disk size, and eventually a virtual machine appears. They SSH into it, run commands from memory or from a shared wiki page, install packages, edit configuration files by hand, and declare the server ready. They might document what they did. They might not.

This process is called **ClickOps**. It is manual, slow, and fragile. Let me be specific about the problems, because each one maps directly to a benefit that IaC provides.

**Inconsistency.** If you need ten servers that are supposed to be identical, you have ten opportunities for human error. Maybe one server gets a slightly different library version. Maybe one has a firewall rule that was added for a test and never removed. These small differences accumulate over time into what engineers call configuration drift — the gradual divergence of actual infrastructure from its intended state.

**No audit trail.** When infrastructure is provisioned manually, the only record of what was done lives in one person's memory or in a change log that nobody keeps current. When something breaks at 2 a.m., you cannot quickly answer: what changed, when did it change, and who changed it?

**Slow recovery.** If a server fails, recreating it from memory is slow and error-prone. If the person who built it is unavailable, recovery becomes even harder. There is no blueprint.

**Poor scalability.** Provisioning one server manually is tedious. Provisioning a hundred is nearly impossible without automation.

**Weak collaboration.** Infrastructure changes bypass the review processes that software teams apply to application code. Changes are not tested before reaching production. New engineers learn by watching a senior colleague, not by reading a specification.

These are not hypothetical problems. They affected every organization that ran servers before the IaC era. Each one is solved — directly — by Infrastructure as Code.

---

## Section 3: What Is Infrastructure as Code — 5:30–9:30

Infrastructure as Code is the practice of managing and provisioning infrastructure through machine-readable configuration files rather than through interactive consoles or manual processes. Instead of clicking through a web interface, you write a text file that describes the infrastructure you want, and an automation tool reads that file and makes it real.

The word "code" is deliberate and important. Because the infrastructure definition is code, it can be:

- Stored in version control, such as Git
- Reviewed by teammates before being applied
- Tested automatically in a pipeline
- Rolled back if a change causes problems
- Reused across projects and environments
- Audited to see what changed, when, and who approved it

The Terraform Associate 003 exam defines IaC as writing infrastructure definitions in a configuration language that a tool can interpret and execute. That is compact but accurate. Keep it in your mental model.

There are two primary paradigms in IaC, and the exam tests both.

**Declarative IaC** means you describe the desired end state of your infrastructure. The tool determines how to reach that state. You say "I want three EC2 instances of this type in this region," and the tool handles the API calls, dependency ordering, and error handling. Terraform is declarative. AWS CloudFormation is also declarative.

**Imperative IaC** means you write step-by-step instructions telling the tool exactly what actions to take. You say "call the EC2 API to create an instance, then call it again, then a third time." Bash scripts, Python scripts using Boto3, and Ansible playbooks written in a task-by-task style are imperative.

The declarative approach has a critical advantage: **idempotency**. If you run a declarative tool multiple times with the same configuration, the result is the same. If the infrastructure already matches your declaration, nothing changes. This property is not guaranteed with imperative scripts, which can fail in unexpected ways when run a second time.

Terraform uses a domain-specific language called **HashiCorp Configuration Language**, which we abbreviate HCL. You will write HCL in every lab from Module 02 onward. Let me show you the simplest possible HCL block to make the concept concrete.

**[SHOW CODE]**

```hcl
resource "null_resource" "example" {
  triggers = {
    always_run = timestamp()
  }
}
```

This block declares a resource of type `null_resource` named `example`. The `triggers` argument causes Terraform to consider this resource changed on every run. The block tells Terraform what to manage — not how to manage it. That is the declarative model in its purest form.

---

## Section 4: The Benefits of IaC — 9:30–14:00

Let us now examine the benefits of IaC systematically. These map directly to Terraform Associate 003 exam objectives.

**Speed.** Manual provisioning that takes hours can be automated to complete in minutes. You can provision an entire application environment — network, compute, database, load balancer, and DNS — with a single command.

**Consistency and reproducibility.** Because the same configuration file is applied every time, environments are identical. Development, staging, and production environments can be defined by the same configuration with only environment-specific values substituted through variables.

**Version control and change management.** Infrastructure configurations live in Git. Every change is a commit with an author, a timestamp, and a message. Code reviews catch mistakes before they reach production. Branches allow experimentation. Rollback is as simple as reverting a commit and re-applying.

**Self-documenting infrastructure.** The configuration file is the documentation. It is always accurate because it is the source of truth. There is no separate document that can fall out of sync with reality.

**Reusability.** Well-written IaC modules can be reused across projects and teams. A module for creating a VPC with standard security settings can be used by every team in an organization, enforcing consistent baseline practices.

**Cost management.** When you can destroy and recreate environments programmatically, you can spin up environments for testing and destroy them immediately when the test is complete. This eliminates the "zombie resource" problem where forgotten instances run indefinitely and accumulate cloud costs.

**Disaster recovery.** If infrastructure is fully defined in code, rebuilding after a failure requires running your automation against a clean account. Recovery time drops from days to hours or minutes.

**Collaboration.** Infrastructure changes go through the same review processes as application code. Team members learn from each other's configurations. New engineers understand the infrastructure by reading the code rather than reverse-engineering a running system.

---

## Section 5: Terraform in the IaC Ecosystem — 14:00–18:30

Now that we understand IaC in the abstract, let us place Terraform specifically in the ecosystem.

Terraform is an open-source tool created by HashiCorp and first released in 2014. It is written in Go. The community edition is available under the Business Source License. HashiCorp also offers Terraform Cloud and Terraform Enterprise as managed and self-hosted commercial products. We will cover those in Module 09.

What makes Terraform distinctive?

**Provider model.** Terraform uses a plugin-based provider system. A provider is a plugin that knows how to communicate with a specific API. AWS, Azure, Google Cloud, Kubernetes, GitHub, and hundreds of other platforms all have Terraform providers. One tool and one language can manage infrastructure across every major cloud simultaneously.

**State management.** Terraform maintains a state file that maps your configuration to real-world resources. State is what allows Terraform to know what already exists and what needs to change. We devote an entire module to state in Module 04.

**Execution plans.** Before making any changes, Terraform shows you an execution plan — a preview of exactly what will be created, modified, or destroyed. This plan-before-apply workflow is one of the most important safety features in Terraform.

**Module system.** Terraform's module system enables reusable, composable infrastructure components. The public Terraform Registry at registry.terraform.io hosts thousands of pre-built modules for common infrastructure patterns.

Let me briefly compare Terraform to the other tools you will encounter in industry.

**AWS CloudFormation** is also declarative and also manages state. However, it only manages AWS resources. Terraform is cloud-agnostic.

**Ansible** is primarily a configuration management tool. It can provision infrastructure imperatively, but its primary strength is configuring software on existing servers. Ansible and Terraform are complementary, not competing.

**Pulumi** is similar in concept to Terraform but allows you to write infrastructure definitions in general-purpose programming languages such as Python, TypeScript, or Go instead of a domain-specific language.

**Chef and Puppet** are configuration management tools focused on software configuration on existing servers. They solve a different problem than Terraform solves.

For the Terraform Associate 003 exam, remember three characteristics of Terraform: it is cloud-agnostic, declarative, and uses a state file. Those three points appear in exam questions repeatedly.

---

## Section 6: The IaC Workflow at a High Level — 18:30–21:30

Before closing, let me give you a mental model of how Terraform works at the highest level. We will go much deeper in Module 02, but I want you to leave this video with a complete picture.

The Terraform workflow has three core phases: **Write**, **Plan**, **Apply**.

**Write.** You author configuration files in HCL. These files describe the infrastructure you want to exist.

**Plan.** You run `terraform plan`. Terraform reads your configuration, compares it to the current state, and produces an execution plan showing exactly what changes will be made. No changes are applied yet.

**Apply.** You run `terraform apply`. Terraform executes the plan, making API calls to create, modify, or destroy resources as needed. The state file is updated to reflect the new reality.

There is a fourth operation to know: `terraform destroy`. This reads your configuration and state file, then deletes all managed resources. It is the reverse of apply.

This Write-Plan-Apply cycle is central to the Terraform Associate 003 exam. Every question about Terraform's process maps back to this cycle. Internalize it now, and every subsequent module will build naturally on it.

---

## Section 7: Closing — 21:30–22:30

Let me recap what we covered.

Infrastructure as Code is the practice of defining infrastructure in machine-readable files stored in version control. It solves the problems of manual provisioning: inconsistency, lack of audit trails, slow recovery, and poor collaboration.

The benefits of IaC include speed, consistency, version control, self-documentation, reusability, cost management, disaster recovery, and improved team collaboration.

There are two IaC paradigms: declarative, where you describe desired state, and imperative, where you describe steps. Terraform is declarative.

Terraform's distinctive features are its provider model, state management, execution plans, and module system. It is cloud-agnostic.

The core workflow is Write, Plan, Apply.

In Module 02 we go hands-on with the Terraform CLI, walk through the full workflow in detail, and interpret the output of `terraform plan`. Before then, complete the reading guide, the lab, the quiz, and the discussion post.

The official Terraform documentation lives at developer.hashicorp.com. That is the authoritative reference for this course and the only reference permitted during your certification exam. Get comfortable with it now.

See you in Module 02.

---

End of Script — Module 01
