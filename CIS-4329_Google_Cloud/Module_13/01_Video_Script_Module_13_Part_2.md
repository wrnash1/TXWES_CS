# Video Script: Module 13 — CI/CD with Cloud Build and Artifact Registry (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction to Part 2

Welcome back. In Part 1 we covered Cloud Build triggers and build config YAML. In Part 2
we cover Artifact Registry for storing Docker images and packages, Cloud Deploy for
managed delivery pipelines, and GKE integration patterns.

---

### Section 1: Artifact Registry

Artifact Registry is GCP's fully managed artifact storage service. It stores:

- Docker container images
- Maven (Java) packages
- npm (Node.js) packages
- Python packages (PyPI)
- Apt and Yum OS packages
- Generic binary artifacts

Artifact Registry replaces the older Container Registry (gcr.io) and is the recommended
storage for all build artifacts on GCP.

#### Creating a Repository

```bash
# Create a Docker repository in us-central1
gcloud artifacts repositories create my-docker-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Production Docker images"

# Create a Maven repository
gcloud artifacts repositories create my-maven-repo \
  --repository-format=maven \
  --location=us-central1

# List repositories
gcloud artifacts repositories list --location=us-central1

# Describe a repository
gcloud artifacts repositories describe my-docker-repo \
  --location=us-central1
```

#### Authenticating Docker to Artifact Registry

```bash
# Configure Docker credential helper for us-central1
gcloud auth configure-docker us-central1-docker.pkg.dev

# Build and tag an image for Artifact Registry
docker build -t us-central1-docker.pkg.dev/MY_PROJECT/my-docker-repo/my-app:v1.0 .

# Push the image
docker push us-central1-docker.pkg.dev/MY_PROJECT/my-docker-repo/my-app:v1.0

# Pull the image
docker pull us-central1-docker.pkg.dev/MY_PROJECT/my-docker-repo/my-app:v1.0

# List images in the repository
gcloud artifacts docker images list \
  us-central1-docker.pkg.dev/MY_PROJECT/my-docker-repo
```

#### Cleanup Policies

Artifact Registry supports cleanup policies to automatically delete old images:

```bash
# Delete images older than 30 days that are not tagged "latest" or "stable"
gcloud artifacts repositories set-cleanup-policies my-docker-repo \
  --location=us-central1 \
  --policy=cleanup-policy.json
```

Cleanup policies prevent storage from growing unbounded as CI/CD systems push new images
on every commit.

---

### Section 2: Cloud Deploy

Cloud Deploy is GCP's managed continuous delivery service. It models your delivery
pipeline as a series of **targets** (environments) with optional approval gates between
them.

Key concepts:

- **Delivery pipeline** — defines the sequence of targets and the configuration for
  deploying to each
- **Target** — a deployment destination (GKE cluster, Cloud Run service, or Anthos)
- **Release** — a snapshot of application artifacts and configuration; immutable after
  creation
- **Rollout** — a deployment of a specific release to a specific target
- **Approval** — a manual gate between targets; a designated approver must approve before
  the rollout proceeds to the next target

#### Delivery Pipeline Configuration

```yaml
# clouddeploy.yaml
apiVersion: deploy.cloud.google.com/v1
kind: DeliveryPipeline
metadata:
  name: my-app-pipeline
serialPipeline:
  stages:
    - targetId: dev
      profiles: [dev]
    - targetId: staging
      profiles: [staging]
    - targetId: production
      profiles: [production]

---
apiVersion: deploy.cloud.google.com/v1
kind: Target
metadata:
  name: dev
gke:
  cluster: projects/MY_PROJECT/locations/us-central1/clusters/dev-cluster

---
apiVersion: deploy.cloud.google.com/v1
kind: Target
metadata:
  name: staging
requireApproval: false
gke:
  cluster: projects/MY_PROJECT/locations/us-central1/clusters/staging-cluster

---
apiVersion: deploy.cloud.google.com/v1
kind: Target
metadata:
  name: production
requireApproval: true
gke:
  cluster: projects/MY_PROJECT/locations/us-central1/clusters/prod-cluster
```

#### Deploying with Cloud Deploy

```bash
# Apply the pipeline and target configuration
gcloud deploy apply \
  --file=clouddeploy.yaml \
  --region=us-central1

# Create a release (snapshot of the application at this point)
gcloud deploy releases create my-app-release-001 \
  --delivery-pipeline=my-app-pipeline \
  --region=us-central1 \
  --images=my-app=us-central1-docker.pkg.dev/MY_PROJECT/my-docker-repo/my-app:v1.0

# List rollouts for the release
gcloud deploy rollouts list \
  --delivery-pipeline=my-app-pipeline \
  --release=my-app-release-001 \
  --region=us-central1

# Approve a production rollout (if requireApproval=true)
gcloud deploy rollouts approve my-app-release-001-to-production-0001 \
  --delivery-pipeline=my-app-pipeline \
  --release=my-app-release-001 \
  --region=us-central1
```

---

### Section 3: GKE Integration with Cloud Build

For GKE deployments without Cloud Deploy, Cloud Build can apply Kubernetes manifests
directly:

```yaml
# cloudbuild.yaml for GKE deployment
steps:
  # Build and push the image
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '-t'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
      - '.'

  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'push'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'

  # Update the image in the Kubernetes deployment
  - name: 'gcr.io/cloud-builders/kubectl'
    args:
      - 'set'
      - 'image'
      - 'deployment/my-app'
      - 'my-app=us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
    env:
      - 'CLOUDSDK_COMPUTE_ZONE=us-central1-a'
      - 'CLOUDSDK_CONTAINER_CLUSTER=my-gke-cluster'
```

---

### Section 4: ACE Exam CI/CD Patterns

Key ACE exam scenarios for Module 13:

**Build configuration** — The exam may show a partial `cloudbuild.yaml` and ask which
step is missing or what a specific field does. Know the `name`, `args`, `id`, `waitFor`,
`entrypoint`, and substitution variable patterns.

**Artifact storage** — "Where should Docker images built by Cloud Build be stored?"
Answer: Artifact Registry. The old answer was Container Registry (gcr.io) but Artifact
Registry is now recommended and tested.

**Rolling deployments** — Cloud Deploy supports rolling deployments where a new release
gradually replaces the old version. For GKE, this is controlled by the Deployment
`strategy.rollingUpdate.maxSurge` and `maxUnavailable` settings in the Kubernetes
manifest.

**Approval gates** — `requireApproval: true` on a Cloud Deploy target requires a human
to approve before the rollout proceeds. This is the correct answer for questions about
controlling production deployments.

---

### Module 13 Summary

Module 13 covered CI/CD on GCP:

- **Cloud Build** — managed build service; cloudbuild.yaml with steps, substitutions,
  parallel execution; triggers for branch, tag, and file patterns
- **Artifact Registry** — stores Docker images, Maven, npm, Python, and other packages;
  replaces Container Registry; cleanup policies for storage management
- **Cloud Deploy** — managed delivery pipeline with targets, releases, rollouts, and
  approval gates; supports GKE, Cloud Run, and Anthos targets
- **GKE integration** — direct kubectl steps in Cloud Build or Cloud Deploy for
  Kubernetes manifest management

For the ACE exam: know cloudbuild.yaml step structure and substitution variables; know
that Artifact Registry replaces gcr.io; know that Cloud Deploy approval gates require
`requireApproval: true` on the target.

Complete the lab, take the quiz, and join the discussion. Module 14 covers GCP Security
and Compliance.
