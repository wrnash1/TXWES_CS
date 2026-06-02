# CIS-4337 Infrastructure Automation

## Module 08: Provisioners and Null Resources

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337. I am Professor Nash. In this module we cover provisioners and the `null_resource` type — powerful escape hatches that let Terraform execute arbitrary commands during resource lifecycle operations.

By the end of this video you will understand what provisioners are, when to use them, the three provisioner types (`local-exec`, `remote-exec`, and `file`), provisioner failure behavior and the `on_failure` argument, the `null_resource` and its `triggers` map, and HashiCorp's guidance on when provisioners should and should not be used.

Provisioners appear on the Terraform Associate 003 exam in Domain 8 (Read, generate, and modify configuration).

---

## Section 2: What Are Provisioners — 1:30–4:30

Provisioners are blocks inside resource blocks that execute scripts or commands at specific points in a resource's lifecycle: after creation or before destruction.

HashiCorp describes provisioners as a "last resort." Their guidance is clear: use cloud-native alternatives whenever they exist. For bootstrapping EC2 instances, use `user_data`. For Azure VMs, use `custom_data`. For Kubernetes pods, use init containers. Provisioners are appropriate only when no native provider argument exists for the task.

Why is this the recommendation? Two reasons.

First, provisioner execution is opaque to Terraform's plan. The `terraform plan` output does not show what a provisioner will do or verify it will succeed. The plan says the resource will be created — it says nothing about the script that runs afterward.

Second, provisioner execution is not retryable by design. If the script fails, the resource is tainted, not retried. This creates operational complexity in large deployments.

With that context, let me explain when provisioners are genuinely necessary and how to use them correctly.

---

## Section 3: local-exec Provisioner — 4:30–8:30

The `local-exec` provisioner runs a command on the machine where Terraform is executing — your laptop, a CI runner, or a Terraform Cloud worker. It does not connect to the provisioned resource.

**[SHOW CODE]**

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = "echo 'Instance ${self.id} created in ${self.availability_zone}' >> deployment.log"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Instance ${self.id} is being destroyed' >> deployment.log"
  }
}
```

Key arguments:

- `command` — the shell command to execute (required).
- `when = destroy` — runs the provisioner before destruction instead of after creation.
- `working_dir` — the directory in which to execute the command.
- `interpreter` — the interpreter to use (default: `["/bin/sh", "-c"]` on Linux/macOS, `["cmd", "/C"]` on Windows).
- `environment` — a map of environment variables to set for the command.

The `self` reference inside a provisioner refers to the containing resource's attributes.

A common use case for `local-exec` is triggering an Ansible playbook against a newly created instance:

**[SHOW CODE]**

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' ./playbooks/configure-app.yml"
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }
}
```

---

## Section 4: remote-exec Provisioner — 8:30–12:00

The `remote-exec` provisioner connects to a newly created resource over SSH or WinRM and runs commands on that machine. It requires a `connection` block to establish the connection.

**[SHOW CODE]**

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

The `inline` argument accepts a list of commands executed sequentially. Alternatively, use `script` (a path to a local script file to upload and execute) or `scripts` (a list of paths).

**[SHOW CODE]**

```hcl
provisioner "remote-exec" {
  script = "./bootstrap.sh"
}
```

---

## Section 5: file Provisioner — 12:00–13:30

The `file` provisioner copies a local file or directory to the remote resource over SSH or WinRM. It requires a `connection` block.

**[SHOW CODE]**

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
}
```

The `file` provisioner itself does not execute the copied file. It is typically combined with a `remote-exec` provisioner that runs the file after copying it.

---

## Section 6: Provisioner Failure Behavior — 13:30–16:00

When a provisioner command exits with a non-zero status code, Terraform's default behavior is:

1. The resource is marked as **tainted** in the state file.
2. The current apply halts.
3. On the next `terraform apply`, Terraform plans to destroy and recreate the tainted resource, then run the provisioner again.

You can change this behavior with the `on_failure` argument:

**[SHOW CODE]**

```hcl
provisioner "local-exec" {
  command    = "notify-external-system.sh ${self.id}"
  on_failure = continue
}
```

With `on_failure = continue`, Terraform logs the error but proceeds with the apply. Use this for non-critical side-effects where failure should not block the deployment.

The two valid values are `fail` (default) and `continue`.

---

## Section 7: The null_resource — 16:00–20:00

The `null_resource` is a resource from the `hashicorp/null` provider that creates no real infrastructure but can have provisioners and lifecycle rules attached to it.

The key feature is the `triggers` argument — a map of values that, when changed, cause Terraform to destroy and recreate the `null_resource`, thereby re-running its provisioners.

**[SHOW CODE]**

```hcl
resource "null_resource" "ansible_provisioner" {
  triggers = {
    instance_id   = aws_instance.web.id
    script_hash   = filemd5("./playbooks/configure.yml")
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i '${aws_instance.web.public_ip},' ./playbooks/configure.yml"
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }
}
```

This pattern re-runs the Ansible playbook whenever:

1. The EC2 instance is replaced (its ID changes).
2. The Ansible playbook file content changes (`filemd5` detects the change).

The `null_resource` pattern cleanly decouples provisioner execution from the resource's own lifecycle. The EC2 instance does not need to be tainted or recreated just to re-run configuration management.

Using `timestamp()` as a trigger forces the null_resource to re-run on every apply:

**[SHOW CODE]**

```hcl
resource "null_resource" "always_run" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "date >> always-runs.log"
  }
}
```

---

## Section 8: Closing — 20:00–21:00

Provisioners are a last resort. Prefer cloud-native alternatives: `user_data` for EC2 bootstrapping, `custom_data` for Azure, Kubernetes init containers for pods.

The three provisioner types: `local-exec` (runs on the Terraform runner), `remote-exec` (runs on the provisioned resource over SSH/WinRM), `file` (copies files to the provisioned resource).

Default failure behavior: taint the resource and halt apply. Override with `on_failure = continue`.

The `null_resource` creates no infrastructure but runs provisioners when its `triggers` map changes.

In Module 09 we cover Terraform Cloud and Terraform Enterprise. Complete the reading guide, lab, quiz, and discussion first.

See you in Module 09.

---

End of Script — Module 08
