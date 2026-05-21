# Quiz: Module 12 - Elastic Beanstalk, CloudFormation, and IaC
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
What is the purpose of AWS CloudFormation?
*   A) A monitoring service that collects CloudWatch metrics and automatically remediates configuration drift.
*   B) An Infrastructure as Code service that provisions and manages AWS resources from declarative YAML or JSON templates, enabling repeatable, version-controlled infrastructure deployments.
*   C) A code deployment service that automates rolling application updates to EC2 instances and Lambda functions.
*   D) A database migration service that converts on-premises schema definitions into AWS RDS configurations.
*   **Correct Answer:** B) AWS CloudFormation is an IaC service that provisions all resources in a template as a managed stack, enabling consistent, repeatable, version-controlled infrastructure.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CloudFormation does have Drift Detection, but its primary purpose is infrastructure provisioning and lifecycle management — not monitoring or auto-remediation. CloudWatch + AWS Config handle monitoring and remediation.
    *   *Why B is correct:* CloudFormation is AWS's native IaC service. Templates declare the desired state; CloudFormation determines the actions needed (create, update, delete) to reach that state. Stacks ensure all resources are managed as a unit with automatic rollback on failure.
    *   *Why C is incorrect:* This describes AWS CodeDeploy, a deployment automation service for application code. CloudFormation manages infrastructure resources, not application code deployment lifecycle.
    *   *Why D is incorrect:* This describes AWS Database Migration Service (DMS) or Schema Conversion Tool (SCT). CloudFormation can create RDS instances but does not migrate schemas or convert database structures.

---

**Question 2**
Which of the following is the most accurate description of a **CloudFormation Change Set**?
*   A) A CloudFormation stack copy that maintains the last 10 successful stack configurations for rollback purposes.
*   B) A preview of the proposed changes CloudFormation will make to a stack — showing which resources will be added, modified, or replaced — before the changes are executed.
*   C) A CloudFormation policy document that restricts which resources in a stack can be modified during updates.
*   D) An automated test suite that validates CloudFormation template syntax and logical dependencies before deployment.
*   **Correct Answer:** B) A Change Set shows the specific AWS resources that will be created, modified, or deleted when a stack update is applied, allowing review before execution.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CloudFormation does not maintain a history of stack copies. It maintains deployment history (previous template versions and events), but a Change Set is a forward-looking preview of pending changes, not a historical record.
    *   *Why B is correct:* Change Sets are essential for production stack governance. They show not just what will change but the nature of the change (e.g., whether a resource will be updated in-place vs. replaced, which would cause downtime or data loss). Change Sets are the answer when the exam asks "how do you safely review infrastructure changes before applying them?"
    *   *Why C is incorrect:* This describes a Stack Policy — a JSON document that protects specific resources from update or replacement during stack operations. Stack Policies and Change Sets are different features with different purposes.
    *   *Why D is incorrect:* CloudFormation linting and template validation is handled by `aws cloudformation validate-template` (syntax only) or cfn-lint (third-party). A Change Set is not a test suite — it is a preview of live changes against an existing deployed stack.

---

**Question 3**
A developer team deploys a Python Flask web application on AWS. They want the infrastructure (EC2, ALB, ASG, RDS) to be automatically provisioned without writing CloudFormation templates or learning AWS infrastructure details. The application code deployment and environment configuration should be manageable through a simple CLI command. Which AWS service best meets this requirement?
*   A) AWS CloudFormation with nested stacks — organize the infrastructure into modular templates that developers can deploy with a single `cloudformation deploy` command.
*   B) AWS Elastic Beanstalk — upload the application code, and Beanstalk automatically provisions and manages the underlying EC2, ALB, and ASG infrastructure for the chosen platform.
*   C) AWS CodePipeline with CodeBuild — set up a CI/CD pipeline that builds and deploys application artifacts to pre-provisioned EC2 instances.
*   D) Amazon EKS with Fargate — containerize the Flask application and deploy it to a managed Kubernetes cluster.
*   **Correct Answer:** B) Elastic Beanstalk is designed for developers who want to deploy application code without managing infrastructure. It automatically provisions and configures all required AWS resources for the chosen platform (Python in this case).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Writing CloudFormation templates — even with nested stacks — requires significant AWS infrastructure knowledge. This contradicts the requirement of not learning AWS infrastructure details. CloudFormation is for infrastructure engineers, not application developers who want abstraction.
    *   *Why B is correct:* Elastic Beanstalk is the AWS PaaS offering. Developers run `eb deploy` or upload a ZIP file, and Beanstalk handles EC2 provisioning, load balancer creation, Auto Scaling configuration, and health monitoring. The team focuses on Python code, not infrastructure YAML.
    *   *Why C is incorrect:* CodePipeline + CodeBuild is a CI/CD pipeline service for build and deployment automation. It does not provision infrastructure — it requires infrastructure (EC2 instances, ECS, Lambda) to already exist as deployment targets. This does not eliminate the need for infrastructure knowledge.
    *   *Why D is incorrect:* Containerizing the application with EKS adds significant operational complexity (Kubernetes expertise, Dockerfile, Helm charts, RBAC configuration). This is the opposite of "without learning AWS infrastructure details."

---

**Question 4**
A DevOps team uses CloudFormation to manage a production VPC stack. A junior engineer manually changes a security group rule directly in the AWS Console without updating the CloudFormation template. The team discovers the discrepancy during a security audit. Which CloudFormation feature identifies this inconsistency?
*   A) CloudFormation Stack Policies — configure a policy to alert when resources are modified outside of CloudFormation.
*   B) CloudFormation Drift Detection — detects differences between the expected resource configuration (template) and the actual live resource configuration.
*   C) AWS Config — enable the `cloudformation-stack-drift-detection-check` managed rule to monitor for manual changes.
*   D) CloudFormation Change Sets — run a Change Set with the original template to identify which resources differ from the deployed state.
*   **Correct Answer:** B) CloudFormation Drift Detection compares each resource's actual configuration in AWS against the configuration defined in the deployed CloudFormation template, identifying manually made changes.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Stack Policies restrict which resources can be updated or replaced during a CloudFormation stack update — they are a preventive control, not a detective control. Stack Policies do not detect changes made directly in the console.
    *   *Why B is correct:* Drift Detection is the purpose-built feature for identifying when a deployed stack's resources have been modified outside of CloudFormation. You initiate drift detection (`detect-stack-drift`), and CloudFormation compares each resource's live state against the template-defined state, marking modified resources as DRIFTED.
    *   *Why C is incorrect:* AWS Config continuously records resource configuration changes and can detect drift-like scenarios, but the `cloudformation-stack-drift-detection-check` rule is not a standard AWS managed Config rule. CloudFormation's native Drift Detection is the more direct and accurate answer for this specific use case.
    *   *Why D is incorrect:* A Change Set previews proposed template changes against the deployed stack. It does not detect out-of-band manual changes to the deployed resources. Change Sets compare the template you submit against the last-deployed template, not against the actual live resource configuration.

---

**Question 5**
A solutions architect designs a multi-environment deployment system. The same CloudFormation template must deploy a development environment (t3.micro EC2, no Multi-AZ RDS) and a production environment (m5.xlarge EC2, Multi-AZ RDS, deletion protection). How should the architect parameterize this to avoid maintaining two separate templates?
*   A) Create two separate CloudFormation templates — one for dev and one for prod — and deploy each independently.
*   B) Use CloudFormation `Parameters` and `Conditions` in a single template. Parameters accept user input (e.g., `Environment: dev|prod`); Conditions evaluate the parameter and conditionally configure resources (e.g., `EnableMultiAZ: !Equals [!Ref Environment, prod]`).
*   C) Deploy the dev stack first, then manually modify the stack in the console to change resource types for production.
*   D) Use CloudFormation Stack Sets to deploy the same identical template to both environments simultaneously in different accounts.
*   **Correct Answer:** B) CloudFormation Parameters accept environment-specific input values; Conditions evaluate those inputs to conditionally set resource properties or enable/disable resources — enabling a single template to serve multiple environments.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Two separate templates create a maintenance burden — every change must be made in both templates. They also risk divergence over time. Single-template parameterization is the IaC best practice.
    *   *Why B is correct:* Parameters + Conditions is the standard CloudFormation pattern for multi-environment templates. The `Conditions` section defines logical tests (e.g., `IsProduction: !Equals [!Ref Environment, prod]`), and resource properties reference those conditions with `!If [IsProduction, m5.xlarge, t3.micro]`. This is a high-frequency SAA-C03 exam pattern.
    *   *Why C is incorrect:* Manually modifying a CloudFormation-managed stack in the console introduces drift and breaks the IaC paradigm. This is exactly the anti-pattern CloudFormation Drift Detection is designed to catch.
    *   *Why D is incorrect:* CloudFormation Stack Sets deploy the same template to multiple accounts/Regions — used for multi-account governance policies, not for deploying different environment configurations from the same template. Stack Sets do not provide the conditional logic needed to change instance types between dev and prod.

