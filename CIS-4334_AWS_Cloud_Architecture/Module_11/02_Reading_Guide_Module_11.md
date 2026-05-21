# Reading Guide: Module 11 - ECS, EKS, and Container Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 11 - ECS, EKS, and Container Architecture**! Containers have become the standard packaging and deployment unit for cloud-native applications. This module covers Amazon ECS (Elastic Container Service), Amazon EKS (Elastic Kubernetes Service), and AWS Fargate — the serverless container compute engine. You will learn how containers differ from virtual machines, how ECS and EKS orchestrate containerized workloads, and when to choose each service. Container architecture questions appear regularly on the SAA-C03 exam in scenarios involving microservices, portability, and cost-optimized compute.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Docker Containers**: Lightweight, portable units of software that package application code, runtime, system libraries, and dependencies into a single image. Containers share the host OS kernel (unlike VMs which include a full OS) — making them faster to start and more resource-efficient. Docker images are stored in container registries (Amazon ECR, Docker Hub). Each container instance runs from an image and provides process isolation.

*   **Amazon ECS (Elastic Container Service)**: AWS's proprietary container orchestration service that manages running, scaling, and scheduling Docker containers. ECS uses Task Definitions (JSON documents that specify container images, CPU/memory, networking, IAM roles, environment variables) and Services (which maintain a desired number of running tasks and integrate with load balancers). ECS can run containers on EC2 instances (you manage the fleet) or on AWS Fargate (serverless — AWS manages the underlying infrastructure).

*   **Amazon EKS (Elastic Kubernetes Service)**: A fully managed Kubernetes service. AWS manages the Kubernetes control plane (API server, etcd, scheduler), while you manage the worker nodes (on EC2 or Fargate). EKS is the correct choice when the organization has existing Kubernetes expertise, needs Kubernetes-native tooling (Helm charts, kubectl), or requires portability across cloud providers and on-premises environments.

*   **AWS Fargate**: A serverless compute engine for containers that works with both ECS and EKS. With Fargate, you do not provision, scale, or manage EC2 instances — you define the task's CPU and memory requirements and Fargate allocates the underlying compute. Billing is per vCPU-second and GB-second consumed by running tasks. Fargate eliminates EC2 management overhead at the cost of slightly higher per-unit pricing vs. EC2.

*   **Amazon ECR (Elastic Container Registry)**: A fully managed Docker container image registry integrated with ECS, EKS, and Fargate. ECR stores, versions, and scans container images for vulnerabilities. ECR is private by default, and access is controlled via IAM policies. ECR eliminates the need to self-host a container registry and provides image replication across Regions for multi-Region deployments.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** Container services appear in Design High-Performing Architectures (24%) and Design Cost-Optimized Architectures (20%). The most common exam scenario asks whether to use ECS vs. EKS, and EC2 launch type vs. Fargate.

*   **ECS vs. EKS Selection:** The exam asks you to choose between ECS and EKS based on organizational context. ECS = simpler AWS-native orchestration, no Kubernetes knowledge needed, tighter AWS integration. EKS = required when the company already uses Kubernetes, needs Kubernetes-specific tooling (Helm, service mesh), or has a multi-cloud portability requirement.

*   **Fargate vs. EC2 Launch Type:** Fargate = no infrastructure management, ideal for teams without EC2 expertise, variable workloads, or compliance requirements restricting OS access. EC2 launch type = more control over instance type/placement, better for workloads needing GPU instances, consistent high-density container packing, or cost-optimized spot instance use.

*   **ECS Task Roles:** Just like EC2 instance profiles, ECS Tasks should use IAM Task Roles (not embedded credentials) to grant containers access to AWS services like S3, DynamoDB, and Secrets Manager. The exam tests this as the "most secure" pattern for container-to-AWS service authentication.

*   **Containers vs. Lambda:** Lambda = event-driven, stateless, short-duration (max 15 minutes), no container management. Fargate/ECS = containerized long-running services, services requiring more memory/CPU than Lambda allows, or workloads with consistent traffic that make always-on containers more cost-effective than per-invocation Lambda billing.

*   **Study Resource:** The ECS and EKS documentation provides comprehensive configuration and best practices: [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) and [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/). Review the "Choosing between Amazon ECS and Amazon EKS" guidance.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the ECS, EKS, and Fargate chapters in the AWS Solutions Architect study materials. Review the [AWS Fargate product page](https://aws.amazon.com/fargate/) for the serverless container model. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Containers on AWS" whitepaper with detailed architecture patterns.

*   **Required Video:** Watch the ECS, EKS, and Fargate module in the official course playlist, focusing on the Task Definition schema, the EC2 vs. Fargate launch type trade-offs, and the ECS Service Autoscaling configuration: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Build and push a Docker image to Amazon ECR:** Build a simple Node.js web application container, authenticate the Docker CLI to ECR (`aws ecr get-login-password | docker login`), and push the image to a private ECR repository.

*   **Deploy the container as an ECS Fargate Service:** Create an ECS Task Definition referencing the ECR image with 0.5 vCPU and 1 GB memory. Create an ECS Service on Fargate with desired count = 2, attach an Application Load Balancer, and verify both tasks are reachable via the ALB DNS name.

*   **Test ECS Service Auto Scaling:** Configure target tracking auto scaling on the ECS Service based on ALB request count per target. Simulate load and observe the ECS Service scaling out the desired task count automatically.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Understand ECS Task Definitions and Services at [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html).
- [ ] Review Fargate pricing model at [https://aws.amazon.com/fargate/pricing/](https://aws.amazon.com/fargate/pricing/).
- [ ] Watch the ECS/EKS/Fargate video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab building, pushing, and deploying a containerized application on ECS Fargate.
- [ ] Proceed to the weekly quiz.
