# Quiz: Module 09 — Terraform Modules

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

**Instructions**: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A team is calling a module from the Terraform Registry with `source = "terraform-aws-modules/vpc/aws"`. They want to allow patch-level updates but prevent minor or major version changes from being applied automatically. Which version constraint achieves this?

A. `version = ">= 5.0.0"`
B. `version = "~> 5.0"`
C. `version = "~> 5.1.2"`
D. `version = "= 5.1.2"`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — `>= 5.0.0` allows any version from 5.0.0 upward, including major version 6 and beyond — far too permissive.
- B is incorrect — `~> 5.0` allows any 5.x version (patch and minor updates), not just patch updates.
- D is incorrect — `= 5.1.2` pins to exactly one version, preventing even patch updates from being applied. While safe, it does not "allow" patch updates.

---

### Question 2

You have a module sourced from a Git repository: `source = "git::https://github.com/acme/infra.git//modules/vpc?ref=v2.0.0"`. What is the purpose of the `//` characters in this URL?

A. They indicate that the repository is private and requires authentication.
B. They separate the repository root URL from the subdirectory within the repository containing the module.
C. They specify that Terraform should use HTTPS rather than SSH for the Git connection.
D. They are a Terraform comment syntax embedded in the source string.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — authentication for Git modules is handled by SSH keys or credential helpers, not by `//`.
- C is incorrect — the `https://` in the URL already specifies the protocol; `//` is a Terraform-specific path separator.
- D is incorrect — Terraform comments use `#` or `//` inside HCL, but within a string value `//` is a literal path separator recognized by Terraform's module loader.

---

### Question 3

A child module declares an output named `subnet_id`. Which expression correctly references this output in the calling root module, assuming the module block is named `network`?

A. `var.network.subnet_id`
B. `output.network.subnet_id`
C. `module.network.outputs.subnet_id`
D. `module.network.subnet_id`

**Correct Answer**: D

**Distractor Analysis**:

- A is incorrect — `var.` is the prefix for input variables, not module outputs.
- B is incorrect — `output.` is not a valid reference namespace; outputs inside a module are accessed through the module namespace.
- C is incorrect — `.outputs.` is not part of the reference path; the correct form goes directly from the module name to the output name.

---

### Question 4

You add a new module block to your root configuration and run `terraform plan` without running `terraform init` first. What happens?

A. Terraform downloads the module automatically and proceeds with the plan.
B. Terraform errors with a message indicating the module has not been installed.
C. Terraform ignores the new module block and plans the rest of the configuration.
D. Terraform prompts you to run `terraform init` and then continues automatically.

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — `terraform plan` does not download modules; that is the responsibility of `terraform init`.
- C is incorrect — Terraform does not silently ignore uninstalled modules; the missing module causes a hard error.
- D is incorrect — Terraform errors and exits; it does not auto-run `terraform init`.

---

### Question 5

Which of the following is a valid Terraform Registry source address format?

A. `registry.terraform.io/hashicorp/consul`
B. `hashicorp/consul/aws`
C. `aws/consul/hashicorp`
D. `https://registry.terraform.io/hashicorp/consul/aws`

**Correct Answer**: B

**Distractor Analysis**:

- A is incorrect — the full registry hostname prefix is not used in the `source` argument; Terraform infers it from the format.
- C is incorrect — the format is `<namespace>/<module>/<provider>`, not `<provider>/<module>/<namespace>`.
- D is incorrect — using a full HTTPS URL would make Terraform treat this as an HTTP archive source, not a Registry source.

---

### Question 6

A root module calls two child modules: `module.network` and `module.compute`. The `module.compute` block uses `module.network.vpc_id` as an input. How does Terraform handle the execution order?

A. Terraform creates both modules simultaneously and retries any failures.
B. Terraform creates `module.compute` first because it is declared later in the file.
C. Terraform creates `module.network` first because `module.compute` has an implicit dependency on it through the reference.
D. The order depends on the `depends_on` argument; without it, order is undefined.

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — Terraform respects dependencies; it does not run dependent modules simultaneously and retry.
- B is incorrect — Terraform does not use file declaration order to determine execution order; it uses the dependency graph.
- D is incorrect — `depends_on` is for explicit dependencies when implicit ones cannot be detected (e.g., when dependencies exist through external systems). Reference-based dependencies are detected automatically.

---

### Question 7

What is the correct naming convention for a Terraform module repository intended for publication on the public Terraform Registry?

A. `terraform_<module>_<provider>`
B. `<provider>-<module>-terraform`
C. `terraform-<provider>-<module_name>`
D. `<namespace>_terraform_<module>`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — underscores are not used in the naming convention; hyphens are required.
- B is incorrect — the order is wrong; `terraform` must be the prefix, not the suffix.
- D is incorrect — this format is not recognized by the Registry; the required format is `terraform-<provider>-<module_name>`.

---

### Question 8

A developer wants to create three identical network module instances for three different regions using a single module block. Which meta-argument enables this?

A. `count = 3`
B. `source = "3"`
C. `instances = 3`
D. `version = "3.0"`

**Correct Answer**: A

**Distractor Analysis**:

- B is incorrect — `source` specifies where the module code lives; it is not used to set the instance count.
- C is incorrect — `instances` is not a valid Terraform meta-argument for modules or resources.
- D is incorrect — `version` is a constraint on which published version of the module to use, not a count.

---

### Question 9

A module is stored in `./modules/database`. Which of the following `source` values is valid for calling this module from the root configuration?

A. `source = "modules/database"`
B. `source = "/modules/database"`
C. `source = "./modules/database"`
D. `source = "local::./modules/database"`

**Correct Answer**: C

**Distractor Analysis**:

- A is incorrect — local paths without `./` or `../` are ambiguous and would cause Terraform to interpret the string as a Registry module address.
- B is incorrect — absolute paths starting with `/` are not a supported local module source format in Terraform.
- D is incorrect — `local::` is not a valid Terraform source prefix; local paths simply use `./` or `../`.

---

### Question 10

What is the key architectural difference between an input variable (`variable`) and a module output (`output`) in the context of module interfaces?

A. Input variables flow data into a module; outputs flow data out of a module to the caller.
B. Input variables are read-only; outputs are read-write.
C. Input variables are defined in `variables.tf`; outputs must be in `main.tf`.
D. Input variables accept any type; outputs only support string values.

**Correct Answer**: A

**Distractor Analysis**:

- B is incorrect — neither variables nor outputs are "read-write" in Terraform's immutable evaluation model; both are evaluated once per plan cycle.
- C is incorrect — while convention places outputs in `outputs.tf`, Terraform loads all `.tf` files in a directory regardless of name; file names do not determine functionality.
- D is incorrect — outputs support all Terraform types including complex types like `list`, `map`, and `object`.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
