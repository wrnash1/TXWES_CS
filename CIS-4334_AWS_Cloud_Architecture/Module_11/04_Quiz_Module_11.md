# Quiz: Module 11 - ECS, EKS, and Container Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A startup with no Kubernetes expertise needs to run a set of containerized microservices on AWS. The team wants to avoid managing EC2 instances entirely and pay only for the compute consumed by running containers. Which combination of services best meets these requirements?
*   A) Amazon EKS with EC2 managed node groups — the team manages the Kubernetes worker nodes.
*   B) Amazon ECS with AWS Fargate — Fargate provisions and manages the underlying compute automatically; the team defines only CPU and memory per task.
*   C) Amazon EC2 with Docker Compose — install Docker on EC2 instances and manage containers manually.
*   D) Amazon EKS with AWS Fargate — EKS on Fargate eliminates node management while providing Kubernetes-native tooling.
*   **Correct Answer:** B) ECS with Fargate is the simplest path for teams without Kubernetes expertise — no EC2 instances to manage, no Kubernetes control plane to understand, and billing only for active container compute.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* EKS with EC2 managed node groups still requires Kubernetes knowledge for deployment configuration (pods, deployments, services). Managed node groups reduce but do not eliminate EC2 management. This contradicts the "no Kubernetes expertise" requirement.
    *   *Why B is correct:* ECS is simpler than EKS for teams without Kubernetes background — Task Definitions and Services are straightforward AWS constructs. Fargate eliminates EC2 provisioning and management. This combination precisely matches "no EC2 management + pay per consumed compute."
    *   *Why C is incorrect:* Self-managing Docker Compose on EC2 instances requires EC2 management (patching, sizing, availability), container orchestration (no auto-recovery, no load balancing), and significant operational overhead. This is the most complex and least scalable option.
    *   *Why D is incorrect:* EKS on Fargate is a valid option that eliminates node management, but it still requires Kubernetes expertise to configure deployments, services, ingress controllers, and RBAC. The "no Kubernetes expertise" requirement makes ECS a better fit.

---

**Question 2**
Which of the following is the most accurate description of **AWS Fargate** in the context of ECS and EKS?
*   A) A container image registry that stores and versions Docker images for use by ECS and EKS deployments.
*   B) A serverless container compute engine where AWS provisions and manages the underlying EC2 instances, and you specify only the CPU and memory requirements for each container task.
*   C) A Kubernetes-managed node group that automatically patches and updates EC2 worker node operating systems on behalf of the cluster administrator.
*   D) A monitoring service that tracks container resource usage and automatically right-sizes CPU and memory allocations for running ECS tasks.
*   **Correct Answer:** B) Fargate is a serverless compute engine for containers — you define resource requirements per task, and AWS handles all underlying infrastructure provisioning, scaling, and patching.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Amazon ECR (Elastic Container Registry), which is a separate service from Fargate. ECR stores images; Fargate runs them.
    *   *Why B is correct:* Fargate decouples container workload definition from infrastructure management. No EC2 instances appear in your account for Fargate tasks — AWS manages the compute fleet. You only configure `cpu` and `memory` in the ECS Task Definition (or Kubernetes pod spec for EKS Fargate profiles).
    *   *Why C is incorrect:* This partially describes EKS Managed Node Groups — a feature that automates EC2 node updates within an EKS cluster. It is not Fargate, and it still involves EC2 instances.
    *   *Why D is incorrect:* This describes container resource monitoring and optimization, which is not a Fargate feature. AWS Compute Optimizer can recommend right-sizing for ECS tasks, but Fargate itself is the compute layer, not a monitoring or optimization service.

---

**Question 3**
A company's ECS containerized application needs to read configuration secrets stored in AWS Secrets Manager and write processed data to an S3 bucket. The security team requires that no credentials are hardcoded in container images or environment variables. Which approach is most secure?
*   A) Store AWS access keys as ECS Task Definition environment variables and rotate them quarterly.
*   B) Assign an IAM Task Role to the ECS Task Definition; the container retrieves temporary credentials from the Task Metadata Endpoint automatically when making AWS API calls.
*   C) Bake the AWS credentials into the Docker image at build time using a build argument, ensuring they are not exposed at runtime.
*   D) Store credentials in an S3 bucket and configure the container to download them at startup using a `wget` command in the container entrypoint.
*   **Correct Answer:** B) IAM Task Roles inject temporary, automatically rotating credentials into the running container via the ECS Task Metadata Endpoint — no static credentials needed anywhere in the pipeline.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hardcoding access keys in Task Definition environment variables stores long-term credentials in ECS task definitions, which may be visible in CloudTrail, console access logs, and CI/CD pipelines. Keys require manual rotation. This is an IAM anti-pattern.
    *   *Why B is correct:* IAM Task Roles are the ECS equivalent of EC2 Instance Profiles. The AWS SDK inside the container automatically retrieves short-lived STS credentials from the Task Metadata Endpoint without any configuration. This is the zero-credential-exposure best practice for container-to-AWS service authentication.
    *   *Why C is incorrect:* Credentials embedded in a Docker image are visible to anyone with access to the image, including in the image layers. Docker image history commands can expose credentials even after layers are "removed." This is a critical security anti-pattern.
    *   *Why D is incorrect:* Storing credentials in S3 and downloading them at startup creates a chicken-and-egg problem (how does the container authenticate to S3 to get the credentials?) and still results in credentials written to container memory. IAM Task Roles eliminate this entirely.

---

**Question 4**
An organization runs containerized workloads using Amazon EKS. They have microservices written in Go, Python, and Java that require different base images and must be independently deployable without redeploying the entire cluster. Which Kubernetes concept supports this independent deployment model?
*   A) Kubernetes DaemonSets — run one pod of each service per cluster node, ensuring each node runs all services simultaneously.
*   B) Kubernetes Deployments — define the desired state (number of replicas, container image) for each microservice independently; rolling updates replace containers one at a time without downtime.
*   C) Kubernetes StatefulSets — deploy each microservice with a stable network identifier and persistent volume per pod.
*   D) Kubernetes CronJobs — schedule each microservice to run on a fixed schedule and exit after completion.
*   **Correct Answer:** B) Kubernetes Deployments allow each microservice to be defined, versioned, and updated independently using rolling update strategies — the standard pattern for independent microservice deployments.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DaemonSets run one pod per node across the entire cluster — used for node-level agents like log collectors or monitoring daemons. DaemonSets are not appropriate for general application microservices.
    *   *Why B is correct:* Kubernetes Deployments are the standard workload resource for stateless microservices. Each service has its own Deployment YAML specifying its container image, replicas, and update strategy. A rolling update (`strategy: RollingUpdate`) replaces old pods with new ones incrementally, enabling zero-downtime deployments of individual services without touching others.
    *   *Why C is incorrect:* StatefulSets are designed for stateful applications that require stable network identities and persistent storage (e.g., databases, Kafka). Stateless microservices (web services, APIs) should use Deployments, not StatefulSets.
    *   *Why D is incorrect:* Kubernetes CronJobs run pods on a scheduled basis and terminate after completion — appropriate for batch jobs, report generation, or cleanup tasks. They are not appropriate for long-running microservices that need to continuously serve traffic.

---

**Question 5**
A company runs ECS Fargate tasks that process uploaded images. The workload is light during weekdays (10 tasks) and peaks on weekends (up to 200 tasks). The team wants automatic scaling without manual intervention. Which ECS configuration achieves this?
*   A) Set the ECS Service desired count to 200 permanently to ensure capacity is always available for peak weekend loads.
*   B) Configure ECS Service Auto Scaling with a Target Tracking policy on a CloudWatch metric such as CPU utilization or ALB requests per target; ECS automatically adjusts the desired task count within configured min/max bounds.
*   C) Create two separate ECS Services — one with 10 tasks for weekdays and one with 200 tasks for weekends — and manually switch between them each week.
*   D) Enable Fargate Spot instances and rely on Spot capacity to automatically provide additional tasks during peak periods.
*   **Correct Answer:** B) ECS Service Auto Scaling with Target Tracking dynamically adjusts the desired task count in response to demand, scaling up for weekend peaks and scaling back down during weekday lows.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running 200 tasks at all times when only 10 are needed on weekdays wastes 190 tasks' worth of Fargate compute costs. For a 5-day weekday + 2-day weekend cycle, this represents roughly 71% cost waste. This contradicts cost optimization principles.
    *   *Why B is correct:* ECS Service Auto Scaling uses Application Auto Scaling to adjust the ECS Service's desired count between minimum and maximum bounds based on CloudWatch metrics. Target Tracking policies (e.g., maintain 50% average CPU) scale out proactively as load increases and scale in when load decreases — achieving the automated scaling requirement.
    *   *Why C is incorrect:* Manually switching between two services every week is operationally untenable, error-prone, and does not handle gradual traffic increases or unexpected mid-week spikes. Auto Scaling exists precisely to eliminate manual capacity management.
    *   *Why D is incorrect:* Fargate Spot provides discounted compute for interruption-tolerant workloads but does not automatically provide more tasks — Spot only affects the pricing and interruption model for the tasks the ECS Service requests. Service Auto Scaling controls how many tasks are requested; Fargate Spot controls whether those tasks run on Spot capacity.

