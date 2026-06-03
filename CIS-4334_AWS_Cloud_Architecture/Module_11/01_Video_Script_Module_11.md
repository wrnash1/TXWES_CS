# Video Script: Module 11 — Containers: ECS, EKS, and Container Architecture

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20–24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 11: Containers: ECS, EKS, and Container Architecture.

Containers have changed how applications are packaged, deployed, and scaled on AWS. The SAA-C03 exam tests containers in the context of choosing the right compute model — when to use Lambda, when to use EC2, and when to use containers. You need to understand Amazon ECS, Amazon EKS, and AWS Fargate well enough to match each to a given architectural scenario.

By the end of this module you will be able to:

- Explain what a container is and how it differs from a virtual machine
- Describe the Amazon ECS architecture: clusters, task definitions, tasks, and services
- Distinguish between ECS on EC2 launch type and ECS on Fargate launch type
- Explain Amazon EKS and when Kubernetes is the right choice
- Describe AWS Fargate as a serverless container runtime
- Identify the appropriate container service for a given exam scenario
- Explain how containers integrate with IAM, VPC, load balancers, and ECR

---

## [01:30 - 06:00] Containers and Why They Matter

[SHOW DIAGRAM]

A container is a lightweight, portable execution environment that packages application code together with its dependencies, runtime, and configuration. Containers run on top of a container runtime (such as Docker) that shares the host operating system kernel. This makes containers much smaller and faster to start than virtual machines, which each run a full guest operating system.

The key properties of containers:

Portability: A container image built on a developer's laptop runs identically on a test server, a staging environment, and a production cluster — the environment is packaged inside the image.

Isolation: Each container has its own filesystem, network namespace, and process space, isolating applications from each other.

Density: Many containers can run on a single EC2 instance, making better use of compute resources than running one application per VM.

Fast startup: Containers start in seconds rather than the minutes it takes to boot a virtual machine.

[SHOW DIAGRAM]

Container images are stored in a container registry. AWS provides Amazon Elastic Container Registry (ECR) as a fully managed, private Docker-compatible container registry. ECR integrates with IAM for access control — no separate login credentials to manage. ECR images are pulled by ECS and EKS tasks at deployment time.

The container lifecycle:

1. Developer writes a Dockerfile and builds an image.
2. Image is pushed to ECR.
3. ECS or EKS pulls the image from ECR and runs it as a container.
4. Containers are registered with an Application Load Balancer for traffic distribution.
5. Auto Scaling adjusts the number of running containers based on CPU, memory, or custom metrics.

---

## [06:00 - 12:00] Amazon ECS

[SHOW DIAGRAM]

Amazon Elastic Container Service is AWS's fully managed container orchestration service. ECS manages the placement, scheduling, and lifecycle of containers on a cluster of compute resources.

ECS core components:

Cluster: The logical boundary for a group of compute resources that run containers. A cluster contains either EC2 instances (EC2 launch type) or is managed entirely by Fargate (Fargate launch type).

Task Definition: A blueprint that specifies how a container should run. The task definition contains: the container image URI (from ECR or any registry), CPU and memory allocation, port mappings, environment variables, IAM task role, logging configuration, and the number of containers that form the task.

Task: A running instance of a task definition. A task is one or more containers running together on the same host, sharing network and storage resources. Tasks are ephemeral — they start, run, and stop.

Service: An ECS service maintains a desired number of running tasks. If a task fails or the underlying instance is terminated, the ECS service scheduler launches a replacement task to maintain the desired count. Services integrate with Application Load Balancers for traffic routing.

[SHOW DIAGRAM]

ECS Launch Types:

EC2 launch type: You provision and manage a cluster of EC2 instances. The ECS agent runs on each instance and registers it with the cluster. You are responsible for the EC2 instances — choosing instance types, patching the OS, managing capacity. The advantage is full control over the host environment and cost optimization for sustained workloads.

Fargate launch type: AWS manages the underlying compute infrastructure. You define the task — the container image, CPU, memory, and networking — and Fargate runs it without you provisioning any EC2 instances. You pay per vCPU-second and GB-second of memory used by each task. Fargate eliminates the operational overhead of managing EC2 instances for containers.

Exam rule: "No infrastructure management" or "serverless containers" → Fargate. "Need full control of underlying host" or "cost-optimize sustained container workloads with reserved instances" → ECS on EC2.

[SHOW DIAGRAM]

ECS Task IAM Roles:

Each ECS task can be assigned an IAM task role. The task role grants the containers in the task permissions to call AWS services — S3, DynamoDB, SQS, Secrets Manager, and others. The task role credentials are provided via the EC2 instance metadata service endpoint inside the container. This follows the same principle as EC2 instance profiles: credentials are injected, not hardcoded.

Do not confuse the task role (permissions for the container application) with the task execution role (permissions for ECS itself to pull images from ECR and write logs to CloudWatch Logs).

---

## [12:00 - 16:00] Amazon EKS

[SHOW DIAGRAM]

Amazon Elastic Kubernetes Service is a fully managed Kubernetes control plane on AWS. Kubernetes is an open-source container orchestration system that has become the industry standard for deploying, scaling, and managing containerized applications at scale.

If your organization already runs Kubernetes on-premises or in another cloud, EKS provides a managed Kubernetes environment on AWS without the operational burden of running your own Kubernetes control plane (API server, etcd, controller manager, scheduler).

EKS core concepts for the exam:

Managed control plane: AWS runs and manages the Kubernetes API server and etcd cluster across multiple AZs. You do not patch or manage the control plane — AWS handles upgrades and availability.

Worker nodes: The compute that runs your pods. Worker nodes can be:

- Self-managed EC2 nodes: You provision and manage EC2 instances that join the EKS cluster.
- EKS managed node groups: AWS automates the provisioning and lifecycle of EC2 worker nodes — OS patching, node draining, rolling updates — while you retain control over instance type and scaling configuration.
- AWS Fargate for EKS: Run Kubernetes pods without managing any EC2 nodes. Define Fargate profiles to specify which pods run on Fargate.

EKS vs. ECS for the exam:

ECS is simpler to learn and is a good choice when you are starting with containers on AWS and do not need Kubernetes compatibility. EKS is the right choice when your organization has existing Kubernetes expertise, runs Kubernetes workloads on-premises, needs Kubernetes-native tooling (Helm, operators, service mesh), or requires portability across cloud providers.

Exam rule: "Kubernetes" → EKS. "Managed containers without Kubernetes" → ECS. "Serverless containers, no cluster management" → Fargate (works with both ECS and EKS).

---

## [16:00 - 19:30] AWS Fargate

[SHOW DIAGRAM]

AWS Fargate is the serverless compute engine for containers. Fargate runs containers without requiring you to provision, configure, or manage any EC2 instances. It works with both ECS and EKS.

With Fargate:

- You specify the container image, CPU, memory, networking, and IAM role.
- Fargate allocates isolated compute for each task — no noisy neighbor, no shared host.
- You are billed per vCPU-second and GB-second of memory allocated to the task.
- Tasks run in their own ENI in your VPC, receiving their own security group and private IP address.

Fargate is ideal for:

- Workloads where infrastructure management is a burden (small teams, startup environments)
- Batch processing jobs that run intermittently — pay only when the task is running
- Microservices with variable traffic — scale from zero with no idle EC2 instances consuming cost
- Security-sensitive workloads requiring strong task isolation

Fargate is less cost-effective for sustained high-throughput workloads compared to reserved EC2 instances. If containers run at near-100% utilization 24/7, EC2 reserved instances will be cheaper than Fargate per-second billing.

---

## [19:30 - 22:00] Container Architecture Integration

[SHOW DIAGRAM]

A production container architecture on AWS typically includes:

VPC with private subnets: Container tasks run in private subnets — they are not directly internet-accessible. Inbound traffic flows through an Application Load Balancer in a public subnet, which routes to containers in the private subnet.

Application Load Balancer: Routes HTTP/HTTPS traffic to ECS services. The ALB performs health checks on individual tasks. When a task fails, it is removed from the target group and a replacement is launched by the ECS service.

ECR: Stores the container images. Tasks pull images at launch. ECR image scanning detects known CVEs in container images.

CloudWatch Logs: ECS and EKS containers send logs to CloudWatch Logs via the awslogs log driver. Centralized logging enables troubleshooting without accessing individual container hosts.

AWS Secrets Manager: Container tasks retrieve database credentials, API keys, and configuration values from Secrets Manager at runtime via the task IAM role. Secrets are never baked into container images.

Auto Scaling: ECS service auto scaling adjusts the desired task count based on CPU utilization, memory utilization, or custom CloudWatch metrics. Fargate scales instantly without waiting for EC2 instance warm-up.

---

## [22:00 - 24:00] Module Summary

Containers package application code and dependencies into portable, isolated units. Amazon ECR stores container images.

Amazon ECS is the AWS-native container orchestration service. EC2 launch type gives you control of the underlying hosts. Fargate launch type is serverless — no EC2 management. ECS services maintain desired task count and integrate with ALBs.

Amazon EKS is managed Kubernetes on AWS. Use EKS when your organization requires Kubernetes compatibility, portability, or ecosystem tooling. EKS supports EC2 managed node groups and Fargate for worker nodes.

AWS Fargate is the serverless compute engine for both ECS and EKS. Pay per task execution time. Ideal for variable workloads and batch jobs.

Exam decision rule: containers on AWS with no existing Kubernetes investment → ECS. Kubernetes required → EKS. No infrastructure management for either → Fargate. Sustained high-utilization containers with cost sensitivity → ECS on EC2 with reserved instances.

For your certification study: <aws.amazon.com/certification>

---

End of Module 11 Video Script
