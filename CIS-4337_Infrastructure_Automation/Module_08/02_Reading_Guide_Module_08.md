# CIS-4337 Infrastructure Automation

## Module 08: Provisioners and Null Resources

### Reading Guide

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This module covers Terraform provisioners — escape hatches that execute scripts during resource lifecycle operations — and the `null_resource` type, which decouples provisioner execution from specific infrastructure resources. Provisioner behavior, failure modes, and the `null_resource` triggers pattern are tested on the Terraform Associate 003 exam in Domain 8 (Read, generate, and modify configuration).

---

## 1. Core Vocabulary

### Provisioner

A block nested inside a resource block that executes a command or script at a specific point in the resource lifecycle: after creation or before destruction.

### local-exec Provisioner

A provisioner that runs a command on the machine where Terraform is executing. The command runs in a local shell and has no connection to the provisioned resource.

### remote-exec Provisioner

A provisioner that connects to a newly created resource over SSH or WinRM and runs commands on that machine. Requires a `connection` block.

### file Provisioner

A provisioner that copies a local file or directory to the remote resource over SSH or WinRM. Does not execute the copied file.

#### connection Block

A block nested inside a resource or provisioner that specifies how Terraform connects to a remote resource. Required by both `remote-exec` and `file` provisioners.

#### on_failure

A provisioner argument that controls behavior when the provisioner command exits with a non-zero status. Values: `fail` (default — taint and halt) or `continue` (log and proceed).

#### Tainted Resource

A resource marked in state as requiring replacement. On the next apply, Terraform plans to destroy and recreate it. Provisioner failures produce tainted resources by default.

#### null_resource

A resource from the `hashicorp/null` provider that creates no infrastructure. Used to attach provisioners and lifecycle rules to arbitrary trigger conditions.

#### triggers

An argument on `null_resource` that accepts a map of key-value pairs. When any value changes, Terraform destroys and recreates the `null_resource`, re-running its provisioners.

#### self

A reference available inside provisioner blocks that refers to the attributes of the containing resource. Example: `self.public_ip`.

---

## 2. When to Use Provisioners

HashiCorp describes provisioners as a "last resort." Use cloud-native alternatives whenever they exist.

| Task | Preferred Approach | When Provisioner Is Needed |
|---|---|---|
| Bootstrap an EC2 instance | `user_data` argument on `aws_instance` | No native attribute exists for the task |
| Bootstrap an Azure VM | `custom_data` argument on `azurerm_linux_virtual_machine` | No native attribute exists |
| Initialize a Kubernetes pod | Init containers | No native attribute exists |
| Register instance in external system | `local-exec` provisioner | External system has no Terraform provider |

Two reasons provisioners are problematic:

- Provisioner execution is opaque to `terraform plan`. The plan shows the resource will be created but says nothing about what the provisioner will do or whether it will succeed.
- Provisioner execution is not retryable. Failure taints the resource rather than retrying the command.

---

## 3. local-exec Provisioner

The `local-exec` provisioner runs a command on the Terraform runner.

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = "echo 'Instance ${self.id} created' >> deployment.log"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Instance ${self.id} destroyed' >> deployment.log"
  }
}
```

Key arguments:

- `command` — the shell command to execute. Required.
- `when = destroy` — runs before destruction instead of after creation.
- `working_dir` — directory in which to run the command.
- `interpreter` — shell interpreter. Default: `["/bin/sh", "-c"]` on Linux/macOS, `["cmd", "/C"]` on Windows.
- `environment` — map of environment variables for the command.

The `self` reference accesses the containing resource's computed attributes.

Common use case — triggering Ansible after EC2 creation:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' ./playbooks/configure.yml"
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }
}
```

---

## 4. remote-exec Provisioner

The `remote-exec` provisioner connects to the resource and runs commands on it. A `connection` block is required.

```hcl
resource "aws_instance" "web" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t3.micro"
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.ssh.id]

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd"
    ]
  }
}
```

Three argument forms for `remote-exec`:

- `inline` — list of commands executed sequentially on the remote host.
- `script` — path to a local script file that is uploaded and executed.
- `scripts` — list of local script paths uploaded and executed in order.

```hcl
provisioner "remote-exec" {
  script = "./bootstrap.sh"
}
```

The `connection` block arguments:

- `type` — `"ssh"` (default) or `"winrm"`.
- `host` — IP address or hostname of the resource.
- `user` — login user.
- `private_key` — SSH private key content.
- `password` — password for WinRM or SSH password authentication.
- `port` — connection port. Default: 22 for SSH, 5985 for WinRM.

---

## 5. file Provisioner

The `file` provisioner copies a local file or directory to the remote resource. It does not execute the file.

```hcl
resource "aws_instance" "app" {
  # ... instance config ...

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
  }

  provisioner "file" {
    source      = "configs/app.conf"
    destination = "/etc/app/app.conf"
  }

  provisioner "remote-exec" {
    inline = ["sudo systemctl restart app"]
  }
}
```

Arguments:

- `source` — local path to the file or directory to copy.
- `destination` — path on the remote resource where the file is placed.
- `content` — inline string content to write to the destination file (alternative to `source`).

---

## 6. Provisioner Failure Behavior

Default behavior when a provisioner exits non-zero:

1. The resource is marked as **tainted** in state.
2. The current apply halts.
3. On the next `terraform apply`, Terraform plans to destroy and recreate the tainted resource, then re-run the provisioner.

Override with `on_failure`:

```hcl
provisioner "local-exec" {
  command    = "notify-external-system.sh ${self.id}"
  on_failure = continue
}
```

| Value | Behavior |
|---|---|
| `fail` | Default. Taint resource, halt apply. |
| `continue` | Log error, proceed with apply. Resource is not tainted. |

Use `on_failure = continue` for non-critical side-effects where failure must not block the deployment.

---

## 7. null_resource

The `null_resource` is a resource from the `hashicorp/null` provider that manages no real infrastructure.

```hcl
terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

resource "null_resource" "ansible_provisioner" {
  triggers = {
    instance_id = aws_instance.web.id
    script_hash = filemd5("./playbooks/configure.yml")
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i '${aws_instance.web.public_ip},' ./playbooks/configure.yml"
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }
}
```

The `triggers` map controls when the `null_resource` is recreated:

- Any value in the map changes → Terraform destroys and recreates the `null_resource` → provisioners re-run.
- `instance_id` trigger: re-runs when the EC2 instance is replaced.
- `script_hash` trigger: re-runs when the Ansible playbook file content changes.

Using `timestamp()` as a trigger forces the `null_resource` to re-run on every apply:

```hcl
resource "null_resource" "always_run" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "date >> run-log.txt"
  }
}
```

This pattern is useful for side-effects that must always execute, such as cache invalidation or external notification.

---

## 8. Required Reading

- Read the provisioners overview at developer.hashicorp.com/terraform/language/resources/provisioners/syntax
- Read the local-exec provisioner reference at developer.hashicorp.com/terraform/language/resources/provisioners/local-exec
- Read the remote-exec provisioner reference at developer.hashicorp.com/terraform/language/resources/provisioners/remote-exec
- Read the null provider documentation at registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource

---

## 9. Terraform Associate 003 Exam Tips

**Tip 1.** Provisioners are a last resort. The exam presents scenarios asking for the best way to bootstrap a VM. Always prefer `user_data` (AWS) or `custom_data` (Azure) over a provisioner.

**Tip 2.** `local-exec` runs on the Terraform runner. `remote-exec` runs on the provisioned resource. Know which is which.

**Tip 3.** Default `on_failure` behavior is `fail` — taints the resource and halts the apply. `on_failure = continue` logs the error and proceeds.

**Tip 4.** A tainted resource is destroyed and recreated on the next apply. Know what "tainted" means and how it is produced.

**Tip 5.** The `null_resource` creates no infrastructure. It exists to run provisioners when upstream values change.

**Tip 6.** The `triggers` map on `null_resource` causes destruction and recreation whenever any trigger value changes between applies.

**Tip 7.** `filemd5()` in a trigger detects script content changes. This is the standard pattern for re-running Ansible when a playbook file is modified.

**Tip 8.** `self` inside a provisioner block references the containing resource's attributes. You cannot use `self` outside of a provisioner.

---

## 10. Study Checklist

- [ ] Explain the difference between `local-exec` and `remote-exec` from memory.
- [ ] List the three provisioner types and one use case for each.
- [ ] Write a `connection` block with `type`, `host`, `user`, and `private_key` arguments.
- [ ] Explain what happens when a provisioner exits with a non-zero status code.
- [ ] Describe what `on_failure = continue` does and when to use it.
- [ ] Write a `null_resource` block with a `triggers` map referencing another resource's ID.
- [ ] Explain why `filemd5()` is used in a `null_resource` trigger.
- [ ] List two cloud-native alternatives to using provisioners for VM bootstrapping.
- [ ] Read all four required documentation pages.
- [ ] Complete the Module 08 lab, quiz, and discussion post.

---

Module 08 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
