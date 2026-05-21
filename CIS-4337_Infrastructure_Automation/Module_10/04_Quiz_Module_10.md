# Quiz: Module 10 - Managing AWS Infrastructure with Terraform
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

**Question 1**
Which two arguments are always required when declaring an `aws_instance` resource in Terraform?
*   A) `instance_type` and `key_name`
*   B) `ami` and `instance_type`
*   C) `subnet_id` and `ami`
*   D) `region` and `instance_type`
*   **Correct Answer:** B) Both `ami` (the Amazon Machine Image ID) and `instance_type` (e.g., `"t3.micro"`) are required arguments for `aws_instance`. Without either, `terraform validate` will report an error.
*   **Distractor Analysis:**
    *   *Why B is correct:* The AWS provider enforces these two arguments as required because they are the minimum information needed for EC2 to launch an instance. All other arguments — `subnet_id`, `key_name`, `user_data`, `vpc_security_group_ids` — are optional and have provider-side defaults or are not needed in every use case.
    *   *Why A is incorrect:* `key_name` is optional. An instance can be launched without an SSH key pair if you plan to access it another way (e.g., AWS Systems Manager Session Manager) or if no interactive access is needed.
    *   *Why C is incorrect:* `subnet_id` is optional. If omitted, AWS places the instance in the default VPC's default subnet. Only `ami` is required from this pair.
    *   *Why D is incorrect:* `region` is not an argument inside the `aws_instance` resource block. Region is set in the `provider "aws"` block or via the `AWS_DEFAULT_REGION` environment variable. It cannot be set per resource.

---

**Question 2**
Which of the following most accurately describes the purpose of a **`data "aws_ami"` block** in an AWS Terraform configuration?
*   A) A resource block that creates a new custom AMI by snapshotting an existing EC2 instance and registering it with AWS
*   B) A read-only data source that queries the AWS API to find an existing AMI matching specified filters, making its ID available for use in `aws_instance` resources without creating any infrastructure
*   C) A variable block that stores a hardcoded AMI ID string so that multiple resources in the same configuration can reference the same value
*   D) A lifecycle block that instructs Terraform to ignore changes to the AMI ID on an existing EC2 instance, preventing replacement when a new AMI is published
*   **Correct Answer:** B) `data "aws_ami"` performs a read-only API query against AWS to find an AMI that matches the provided owner and filter criteria. The result — including the `id` attribute — is available to reference in `aws_instance.ami` without creating any new resource.
*   **Distractor Analysis:**
    *   *Why B is correct:* This is the canonical exam pattern for avoiding hardcoded, region-specific AMI IDs. Using `data "aws_ami"` with filters like `name = "amzn2-ami-hvm-*"` and `owners = ["amazon"]` ensures the configuration automatically resolves to the correct AMI in whatever region it is applied. Removing a `data` block never destroys infrastructure.
    *   *Why A is incorrect:* Creating a custom AMI is done with the `aws_ami` resource block (without the `data` keyword) or with `aws_ami_from_instance`. The `data` prefix always denotes a read-only query.
    *   *Why C is incorrect:* A variable block (`variable`) stores a user-supplied input value. A `data` block performs a live API query. These serve fundamentally different purposes.
    *   *Why D is incorrect:* Ignoring changes to resource arguments is configured with `lifecycle { ignore_changes = [ami] }` inside the resource block. This is unrelated to `data` blocks.

---

**Question 3**
A Terraform configuration stores its state in an S3 remote backend. A team member reports that two engineers ran `terraform apply` simultaneously and the state file is now corrupted. What backend configuration argument would have prevented this?
*   A) Adding `encrypt = true` to the `backend "s3"` block to enable server-side encryption of the state file
*   B) Adding `dynamodb_table = "<table-name>"` to the `backend "s3"` block to enable state locking via DynamoDB
*   C) Adding `versioning = true` to the S3 bucket to keep a backup of the previous state file
*   D) Adding `region = "us-east-1"` to the `backend "s3"` block to ensure all team members target the same region
*   **Correct Answer:** B) The `dynamodb_table` argument in the S3 backend configuration enables state locking. Before any operation that modifies state, Terraform writes a lock entry to the DynamoDB table. A second concurrent apply reads the lock and waits or fails, preventing the race condition that causes corruption.
*   **Distractor Analysis:**
    *   *Why B is correct:* State locking via DynamoDB is the AWS-native solution to concurrent-apply corruption. The exam tests this argument name and its purpose explicitly. The DynamoDB table must have a partition key named `LockID` of type String.
    *   *Why A is incorrect:* `encrypt = true` enables server-side encryption of the state file at rest in S3. This is a security best practice but has no effect on concurrency — it does not prevent simultaneous writes.
    *   *Why C is incorrect:* S3 bucket versioning allows recovery from accidental state deletion or corruption after the fact. It does not prevent simultaneous writes from occurring in the first place.
    *   *Why D is incorrect:* The `region` argument ensures Terraform targets the correct S3 bucket region but plays no role in preventing concurrent modifications to the state file.

---

**Question 4**
Which of the following is the recommended way to supply AWS credentials to Terraform running on an EC2 instance in a CI/CD pipeline, according to AWS and HashiCorp best practices?
*   A) Hardcode the `access_key` and `secret_key` arguments directly in the `provider "aws"` block so the credentials are always available
*   B) Store the access key and secret key in a `terraform.tfvars` file and commit it to the Git repository alongside the configuration
*   C) Attach an IAM instance profile with the necessary permissions to the EC2 instance running Terraform, allowing the AWS provider to retrieve temporary credentials automatically via the instance metadata service
*   D) Pass the credentials as command-line arguments using `terraform apply -var="access_key=..." -var="secret_key=..."`
*   **Correct Answer:** C) IAM instance profiles grant the EC2 instance a role with the required permissions. The AWS SDK (used by the Terraform AWS provider) automatically retrieves short-lived credentials from the EC2 instance metadata service (IMDS). No static credentials are needed anywhere in the configuration.
*   **Distractor Analysis:**
    *   *Why C is correct:* This is the AWS Well-Architected and HashiCorp-recommended pattern for automated environments. IAM roles provide temporary, automatically rotated credentials with no secret storage required. The exam tests that static credentials in configuration files are an anti-pattern.
    *   *Why A is incorrect:* Hardcoding credentials in `.tf` files is a serious security anti-pattern. The credentials are exposed to anyone with access to the code and will be committed to version control unless manually excluded. This is explicitly flagged on the exam as incorrect.
    *   *Why B is incorrect:* Committing credentials in `terraform.tfvars` to version control exposes them permanently in the repository history, even if the file is later deleted. This violates basic secrets management principles.
    *   *Why D is incorrect:* Passing credentials as `-var` arguments means they appear in shell history, CI/CD logs, and process lists. This is marginally better than hardcoding but still exposes credentials outside of a secure secrets store.

---

**Question 5**
A Terraform engineer wants to configure the S3 backend with different bucket names for the `dev` and `prod` environments without duplicating the backend block in two separate `.tf` files. Which approach does HashiCorp support for parameterizing backend configuration?
*   A) Use input variables (`var.bucket_name`) directly inside the `backend "s3"` block — Terraform resolves variables before initializing the backend
*   B) Use a `locals` block to define the bucket name and reference it in the backend block with `local.bucket_name`
*   C) Use partial backend configuration — leave the `bucket` argument out of the `backend "s3"` block and supply it at `terraform init` time with the `-backend-config="bucket=<name>"` flag
*   D) Use `terraform workspace` to switch environments — the S3 backend automatically uses a different bucket for each workspace name
*   **Correct Answer:** C) Terraform backend blocks do not support variable or local references. The supported pattern for parameterizing backend configuration is partial configuration: omit dynamic arguments from the block and supply them via `-backend-config` flags or a separate `.hcl` file at `terraform init` time.
*   **Distractor Analysis:**
    *   *Why C is correct:* This is a commonly tested exam trap. The constraint that backend configurations cannot use variables or locals is explicit in the Terraform documentation. Partial configuration with `-backend-config` is the only supported parameterization mechanism. Each environment runs `terraform init -backend-config=env/dev.hcl` or `env/prod.hcl`.
    *   *Why A is incorrect:* The Terraform backend is initialized before input variables are resolved, so `var.bucket_name` inside a backend block will cause a `terraform init` error. This is one of the most common exam traps.
    *   *Why B is incorrect:* The same constraint applies to `local` references — locals are not available during backend initialization. Using `local.bucket_name` in a backend block will also fail.
    *   *Why D is incorrect:* CLI workspaces do not change which S3 bucket is used. All workspaces using the same backend block write to the same bucket, differentiated by a key prefix (`env:/dev/terraform.tfstate`). Switching buckets requires separate backend configurations.
