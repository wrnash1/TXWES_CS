# Reading Guide: Module 12 - Elastic Beanstalk, CloudFormation, and IaC
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 12 - Elastic Beanstalk, CloudFormation, and Infrastructure as Code**! Infrastructure as Code (IaC) treats infrastructure provisioning the same way as application code — version-controlled, repeatable, and reviewable. This module covers AWS CloudFormation (AWS's native IaC service) and AWS Elastic Beanstalk (a platform-as-a-service that abstracts infrastructure for application developers). Understanding when to use each, and how CloudFormation templates are structured, is directly tested on the SAA-C03 exam in scenarios involving deployment automation, stack management, and environment consistency.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AWS CloudFormation**: A native AWS IaC service that provisions and manages AWS resources using declarative templates written in YAML or JSON. You define the desired state of your infrastructure in a template, and CloudFormation creates, updates, or deletes resources to match. Key template sections include: `AWSTemplateFormatVersion`, `Parameters` (user-provided inputs), `Resources` (the only required section — defines AWS resources to create), `Outputs` (exported values for cross-stack references), and `Mappings` (key-value lookup tables).

*   **CloudFormation Stacks**: A single unit of deployment for a CloudFormation template. When you create a stack, CloudFormation provisions all resources defined in the template together. Stacks are updated via change sets and deleted as a unit (deleting the stack deletes all resources unless a deletion policy is set). Nested Stacks allow large architectures to be broken into modular, reusable templates. Stack Sets extend a single template across multiple accounts and Regions.

*   **CloudFormation Change Sets**: A preview mechanism that shows exactly what CloudFormation will add, modify, or delete before applying an update. Change Sets allow architects to review the planned infrastructure changes (including replacement vs. update behavior for modified resources) before committing. Replacement of a resource (e.g., changing an RDS instance's engine) causes a new resource to be created and the old one deleted — important for understanding data loss risk.

*   **AWS Elastic Beanstalk**: A platform-as-a-service (PaaS) that abstracts the underlying infrastructure for deploying web applications and services. Developers upload application code (ZIP or WAR), and Beanstalk automatically provisions EC2 instances, Auto Scaling Groups, Elastic Load Balancers, and (optionally) RDS databases. Beanstalk supports multiple platforms: Java, .NET, Node.js, PHP, Python, Ruby, Go, and Docker. It is best for teams that want managed infrastructure without writing CloudFormation templates.

*   **CloudFormation Drift Detection**: A feature that compares the current live state of stack resources against the expected state defined in the CloudFormation template. Drift occurs when someone manually changes a resource outside of CloudFormation (e.g., modifying an EC2 security group directly in the console). Drift detection identifies these inconsistencies so they can be corrected to maintain infrastructure-as-code discipline.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** IaC appears primarily in Design High-Performing Architectures (24%) and Operational Excellence scenarios. The exam tests CloudFormation template structure, Change Sets, and when to use Beanstalk vs. raw CloudFormation.

*   **CloudFormation vs. Elastic Beanstalk Selection:** The exam distinguishes by audience. Developers who want to deploy code without learning AWS infrastructure → Elastic Beanstalk. DevOps engineers who need full control over every AWS resource, multi-service architectures, or compliance-required configurations → CloudFormation. CloudFormation is the answer for "infrastructure as code" scenarios; Beanstalk is the answer for "deploy application code quickly."

*   **CloudFormation Rollback:** If stack creation or update fails, CloudFormation automatically rolls back to the last known good state by default. This atomic transaction model prevents partial deployments. You can disable rollback during troubleshooting to inspect failed resources.

*   **Intrinsic Functions:** CloudFormation templates use intrinsic functions like `!Ref` (references a parameter or resource), `!Sub` (string substitution), `!GetAtt` (retrieves an attribute of a resource), `!Join`, and `!Select`. The exam may ask what a function like `!GetAtt MyEC2Instance.PublicIp` returns — the public IP address of the created EC2 instance.

*   **Stack Policies:** A JSON document that controls which stack resources can be updated or replaced during a stack update. Stack Policies protect critical resources (e.g., RDS production databases) from accidental modification during routine updates. This is an exam-tested governance control for production stacks.

*   **Study Resource:** The CloudFormation User Guide covers template anatomy, intrinsic functions, and Change Sets: [AWS CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/index.html). The "Template reference" section lists all resource types and their properties.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the CloudFormation and Elastic Beanstalk chapters in the AWS Solutions Architect study materials. Review the [AWS CloudFormation sample templates](https://aws.amazon.com/cloudformation/resources/templates/) for practical YAML template examples. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Infrastructure as Code" whitepaper covering CloudFormation best practices.

*   **Required Video:** Watch the CloudFormation and Elastic Beanstalk module in the official course playlist, focusing on the template structure, the Change Set workflow, and the Beanstalk environment tiers (web server vs. worker): [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Write and deploy a CloudFormation template:** Author a YAML CloudFormation template that creates an S3 bucket, an IAM Role, and an EC2 instance with the Role attached. Use `Parameters` for the EC2 instance type. Deploy using `aws cloudformation create-stack --stack-name my-lab-stack --template-body file://template.yaml --parameters ParameterKey=InstanceType,ParameterValue=t3.micro`.

*   **Create and execute a Change Set:** Modify the template to add an S3 bucket policy and create a Change Set: `aws cloudformation create-change-set --stack-name my-lab-stack --change-set-name add-bucket-policy --template-body file://template-v2.yaml`. Review the Change Set to confirm only the policy is added, then execute it.

*   **Enable Drift Detection:** After manually modifying the EC2 security group in the console, run `aws cloudformation detect-stack-drift --stack-name my-lab-stack` and review the drift report to identify the out-of-band change.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review CloudFormation template anatomy at [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html).
- [ ] Understand CloudFormation intrinsic functions at [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html).
- [ ] Watch the CloudFormation/Beanstalk video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab authoring, deploying, and updating a CloudFormation stack.
- [ ] Proceed to the weekly quiz.
