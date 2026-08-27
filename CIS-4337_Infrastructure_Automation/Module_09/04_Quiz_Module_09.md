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

---

### Question 11 (5 points)

A team runs `terraform init` and then checks in `.terraform.lock.hcl` to version control. A second developer checks out the repository and runs `terraform init`. What is the effect of the committed lock file on the second developer's environment?

- A) Terraform ignores the lock file and downloads the latest matching module versions.
- B) Terraform uses the exact module and provider versions recorded in the lock file, ensuring consistency.
- C) Terraform deletes the lock file and regenerates it from scratch.
- D) Terraform requires the second developer to manually run `terraform get` before `terraform init` can succeed.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — the lock file is explicitly honored by Terraform; its purpose is to prevent version drift across developer environments.
  - C is incorrect — Terraform only regenerates the lock file when you pass `-upgrade` or when no lock file exists.
  - D is incorrect — `terraform get` is not a prerequisite for `terraform init`; `terraform init` handles both module and provider installation.

---

### Question 12 (5 points)

Which meta-argument allows a root module to pass a provider alias to a child module that requires it?

- A) `depends_on`
- B) `for_each`
- C) `providers`
- D) `aliases`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — `depends_on` declares explicit resource or module dependencies; it does not pass provider configurations.
  - B is incorrect — `for_each` creates multiple module instances from a map or set; it does not configure providers.
  - D is incorrect — `aliases` is not a valid meta-argument for module blocks; provider aliases are passed using the `providers` map.

---

### Question 13 (5 points)

A module block includes `count = 3`. How would Terraform address the second instance of a resource named `local_file.config` inside that module (module block name is `app`)?

- A) `module.app.local_file.config`
- B) `module.app[2].local_file.config`
- C) `module.app[1].local_file.config`
- D) `module.app.1.local_file.config`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A is incorrect — without an index, this address refers to a module called without `count`; with `count`, an index is always required.
  - B is incorrect — `[2]` would refer to the third instance (zero-indexed), not the second.
  - D is incorrect — `.1.` is not valid Terraform address syntax; bracket notation `[1]` is required for count-indexed modules.

---

### Question 14 (5 points)

What happens when you run `terraform get -update` in a directory that already has modules installed?

- A) Terraform removes all installed modules and forces a clean re-download.
- B) Terraform checks for newer versions that satisfy existing constraints and updates installed modules if a newer matching version is available.
- C) Terraform upgrades all modules to the absolute latest version regardless of version constraints.
- D) Terraform regenerates the `.terraform.lock.hcl` file with the latest provider versions.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — `terraform get -update` does not perform a clean wipe; it updates selectively where a newer constrained version exists.
  - C is incorrect — version constraints are always honored; `-update` still respects the constraint boundaries.
  - D is incorrect — `terraform get` manages modules only; provider lock file updates require `terraform init -upgrade`.

---

### Question 15 (5 points)

A child module declares `variable "db_password" { type = string; sensitive = true }`. The root module passes `db_password = var.root_db_password`. How does Terraform handle this sensitive value in plan output?

- A) Terraform displays the value in plan output because the root module's variable is not marked sensitive.
- B) Terraform redacts the value in plan output and marks any output derived from it as sensitive.
- C) Terraform stores the value in a separate encrypted secrets file.
- D) Terraform refuses to pass sensitive values between modules and returns an error.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — sensitivity propagates; if the receiving module variable is marked sensitive, the value is redacted regardless of the source.
  - C is incorrect — Terraform does not create a separate encrypted secrets file; sensitive values still appear in plaintext in state.
  - D is incorrect — Terraform fully supports passing sensitive values between modules; it only affects display behavior.

---

### Question 16 (5 points)

You want to test a module change without affecting real infrastructure. Which command lets you see what Terraform would do without making any changes?

- A) `terraform validate`
- B) `terraform plan`
- C) `terraform apply -dry-run`
- D) `terraform graph`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — `terraform validate` checks configuration syntax and type correctness but does not show resource-level add/change/destroy actions.
  - C is incorrect — `-dry-run` is not a valid Terraform flag; the equivalent functionality is provided by `terraform plan`.
  - D is incorrect — `terraform graph` outputs the dependency graph in DOT format; it does not show planned resource changes.

---

### Question 17 (5 points)

A module source is set to `"./modules/compute"`. After a developer moves the module directory to `"./modules/infra/compute"`, what is the minimum change required to make the configuration valid again?

- A) Run `terraform state mv` to update the state.
- B) Update the `source` argument in the module block to `"./modules/infra/compute"` and run `terraform init`.
- C) Delete the `.terraform` directory and run `terraform apply`.
- D) Add `depends_on = [module.compute]` to the calling resource.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — `terraform state mv` renames resources in state; it does not resolve a missing module source path.
  - C is incorrect — deleting `.terraform` and running `apply` without fixing the source path will fail at the module lookup step.
  - D is incorrect — `depends_on` adds explicit ordering dependencies; it has no effect on resolving module source paths.

---

### Question 18 (5 points)

Which of the following statements about the `terraform graph` command and modules is true?

- A) `terraform graph` only shows root module resources, not child module resources.
- B) `terraform graph` outputs a DOT-format graph that includes all resources and modules, showing dependency edges.
- C) `terraform graph` is only available after `terraform apply` has been run.
- D) `terraform graph` requires a `-module` flag to display module-level dependencies.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — `terraform graph` represents the full dependency graph including all module and resource nodes.
  - C is incorrect — `terraform graph` works at any stage of the workflow; it reads configuration and state, not apply history.
  - D is incorrect — no `-module` flag is required; module nodes are included automatically.

---

### Question 19 (5 points)

In the Terraform Registry source format `namespace/module/provider`, what does the `provider` component represent?

- A) The cloud provider you are authenticated to for this session.
- B) The primary provider that the module's resources use, used to disambiguate modules with the same name across providers.
- C) The Terraform provider plugin version that must be installed.
- D) The provider alias that the module expects to receive via the `providers` meta-argument.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — the `provider` field in the source address is a static identifier, not tied to authentication state.
  - C is incorrect — provider plugin versions are specified in `required_providers` blocks, not in the module source string.
  - D is incorrect — the `providers` meta-argument is separate from the source address; the source `provider` component is purely a naming disambiguator.

---

### Question 20 (5 points)

A team has a module that creates an S3 bucket. They want to reuse the module to create buckets in three different AWS regions simultaneously using a single module block. Which approach is correct?

- A) Set `count = 3` on the module block and use a list of region strings indexed by `count.index`.
- B) Use `for_each = toset(["us-east-1", "us-west-2", "eu-west-1"])` on the module block and pass a provider alias per region using `providers`.
- C) Call the module three times with different block labels and the same `source`.
- D) Add `regions = ["us-east-1", "us-west-2", "eu-west-1"]` as an input variable and handle multiple regions inside the module.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A is incorrect — `count` with an indexed region list works but produces numerically addressed instances (`module.bucket[0]`); `for_each` with named keys is the preferred approach and directly maps to meaningful instance addresses.
  - C is incorrect — calling the module three times with separate block labels is valid but is not "a single module block" as the question specifies.
  - D is incorrect — handling multiple regions inside a module requires provider configurations that cannot be dynamically created inside a module; provider aliasing must happen at the calling level.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
