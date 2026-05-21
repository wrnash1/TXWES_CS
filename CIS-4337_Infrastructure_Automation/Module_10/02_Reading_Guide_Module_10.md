# Reading Guide: Module 10 - Managing AWS Infrastructure with Terraform
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 10 - Managing AWS Infrastructure with Terraform**! This week's study material applies all core Terraform concepts to the **Amazon Web Services (AWS)** provider — the most widely used provider in Terraform's ecosystem and the one most heavily represented in Terraform Associate exam scenarios. You will learn how to configure the AWS provider, provision key AWS resources (`aws_instance`, `aws_vpc`, `aws_s3_bucket`, `aws_iam_role`), manage credentials securely, and use the S3 remote backend with DynamoDB state locking.

As a student, you will connect the HCL fundamentals from earlier modules to real AWS resource arguments, understand how Terraform interacts with AWS APIs, and practice reading plan output for common AWS change scenarios. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AWS provider configuration**: The `provider "aws"` block that tells Terraform which AWS region to target and how to authenticate. The `region` argument is required; credentials are typically supplied via environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) or an IAM instance profile — never hardcoded in `.tf` files. The `required_providers` block in the `terraform {}` block pins the AWS provider version.
*   **`aws_instance` resource**: The Terraform resource for provisioning an EC2 virtual machine. Key arguments include `ami` (Amazon Machine Image ID), `instance_type` (e.g., `"t3.micro"`), `subnet_id`, `vpc_security_group_ids`, `key_name`, and `user_data`. The AMI ID is region-specific; a data source (`data "aws_ami"`) is the recommended way to look up the latest AMI dynamically rather than hardcoding an ID.
*   **`aws_vpc` and `aws_subnet`**: Resources for creating a Virtual Private Cloud and its subnets. The `aws_vpc` block requires a `cidr_block` argument (e.g., `"10.0.0.0/16"`). Subnets require `vpc_id` (referencing the VPC resource), `cidr_block`, and `availability_zone`. These are foundational resources that most other AWS resources depend on, making them important for understanding Terraform dependency graphs.
*   **S3 remote backend with DynamoDB locking**: The standard AWS-native pattern for team state management. The `backend "s3"` block stores `terraform.tfstate` in an S3 bucket. The `dynamodb_table` argument enables state locking — Terraform writes a lock record to DynamoDB before modifying state and deletes it when done, preventing simultaneous applies from corrupting state.
*   **IAM roles and instance profiles**: AWS IAM resources managed by Terraform (`aws_iam_role`, `aws_iam_role_policy`, `aws_iam_instance_profile`) that grant EC2 instances permissions to interact with other AWS services without storing access keys. This is the recommended credential pattern for EC2-based Terraform runners and the exam tests the difference between IAM user credentials and instance profile credentials.

---

### 2. Certification Exam Tips
*   **Exam Domain — Interact with Terraform Modules and Providers (Domain 3 & 4):** AWS provider scenarios are the most common exam context. Know how to read a resource block for `aws_instance` and identify missing required arguments. Know that `ami` and `instance_type` are always required for `aws_instance`.
*   **Never hardcode AWS credentials:** The exam tests best practices for credential management. Hardcoding `access_key` and `secret_key` in the `provider "aws"` block is explicitly flagged as an anti-pattern. The correct approaches are environment variables, shared credentials files, or IAM instance profiles. Credentials should also never be committed to version control.
*   **AMI IDs are region-specific:** A question may present an `aws_instance` with a hardcoded `ami` value and ask what is wrong with the configuration — the answer is that AMI IDs are not portable across regions. The correct fix is to use a `data "aws_ami"` block with filters to look up the appropriate AMI dynamically.
*   **S3 backend configuration does not support variables:** Backend configurations cannot reference Terraform input variables or locals. All backend arguments must be literal values. If you need to parameterize the backend (e.g., different S3 buckets per environment), you must use partial configuration with `-backend-config` flags passed to `terraform init`.
*   **Study Resource:** The AWS provider documentation lists every resource argument and attribute: [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs). Review the `aws_instance`, `aws_vpc`, and `aws_s3_bucket` resource pages to understand the most commonly tested arguments and their types.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the AWS provider overview and key resource pages at [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs). Focus on the `aws_instance`, `aws_vpc`, `aws_subnet`, and `aws_s3_bucket` resource pages. Review the provider authentication section to understand the credential resolution order.
*   **Required Video:** Watch the video lecture on **Managing AWS Infrastructure with Terraform** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the sections demonstrating the full workflow: provider configuration, VPC and EC2 resource blocks, `terraform plan` output interpretation, and the S3 remote backend setup.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure the AWS provider and authenticate via environment variables**: Set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in your shell environment. Add the `provider "aws"` block with a `region` argument and run `terraform init` to download the AWS provider plugin.
*   **Provision a VPC and EC2 instance**: Write `aws_vpc`, `aws_subnet`, `aws_security_group`, and `aws_instance` resource blocks with correct dependencies. Use `data "aws_ami"` to look up the latest Amazon Linux 2 AMI. Run `terraform plan` and review the dependency order in the output.
*   **Configure the S3 remote backend**: Add a `backend "s3"` block referencing an existing S3 bucket and DynamoDB table. Run `terraform init -migrate-state` to move local state to the remote backend. Verify the state file appears in the S3 bucket.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the AWS provider documentation at [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).
*   [ ] Watch the video lecture on **Managing AWS Infrastructure with Terraform** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
