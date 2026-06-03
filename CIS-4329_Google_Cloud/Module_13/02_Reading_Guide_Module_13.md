# Reading Guide: Module 13 — CI/CD with Cloud Build and Artifact Registry

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This reading guide accompanies the Module 13 video lectures on CI/CD with Cloud Build
and Artifact Registry. It covers build configuration, triggers, artifact storage, Cloud
Deploy pipelines, and GKE integration.

**Estimated reading time**: 55–70 minutes

---

### Learning Objectives

After completing this module's readings you will be able to:

- Write a Cloud Build cloudbuild.yaml file with multiple steps and substitutions
- Create and configure Cloud Build triggers for branch, tag, and file patterns
- Create and manage Artifact Registry repositories for Docker and other formats
- Describe the Cloud Deploy pipeline model: pipelines, targets, releases, and rollouts
- Configure Cloud Deploy approval gates for production targets
- Explain the GKE rolling deployment model and kubectl integration in Cloud Build

---

### Required Reading 1: Cloud Build

**Source**: Google Cloud Documentation — Cloud Build Overview

**URL**: `https://cloud.google.com/build/docs/overview`

#### Cloud Build Key Terms

- **Build step**: A single operation in a build; runs a Docker container and executes
  specified arguments; steps run sequentially by default
- **Builder**: A Docker image used as the execution environment for a build step; Google
  provides builders at `gcr.io/cloud-builders/` for common tools
- **Build config file**: The `cloudbuild.yaml` or `cloudbuild.json` file defining all
  build steps; stored in the repository root by default
- **Substitution variable**: A placeholder in the build config resolved at build time;
  built-in variables include `$PROJECT_ID`, `$COMMIT_SHA`, `$BRANCH_NAME`
- **Trigger**: A configuration that starts a build automatically when repository events
  occur (push, tag, pull request)
- **Cloud Build service account**: The identity Cloud Build uses to access GCP resources
  during a build; by default `[PROJECT_NUMBER]@cloudbuild.gserviceaccount.com`

#### Build Config Field Reference

| Field | Purpose |
|---|---|
| `steps[].name` | Builder image (Docker image) to use for this step |
| `steps[].args` | List of arguments passed to the builder's entrypoint |
| `steps[].entrypoint` | Override the builder's default entrypoint |
| `steps[].id` | Unique name for this step (used in waitFor) |
| `steps[].waitFor` | List of step IDs this step waits for; enables parallel execution |
| `steps[].env` | Environment variables for the step |
| `substitutions` | Custom substitution variables defined in the config |
| `timeout` | Maximum build duration (default 10 minutes; max 24 hours) |
| `images` | Docker images to push to a registry after the build completes |
| `artifacts` | Non-Docker artifacts to store in Cloud Storage after the build |
| `options.machineType` | Build VM size (E2\_MEDIUM, E2\_HIGHCPU\_8, N1\_HIGHCPU\_32) |
| `options.logging` | Log destination (CLOUD\_LOGGING\_ONLY, GCS\_ONLY, NONE) |

#### Cloud Build Trigger Types

- **Branch trigger**: Fires when a push is made to a branch matching the pattern
- **Tag trigger**: Fires when a Git tag matching the pattern is pushed
- **Pull request trigger**: Fires when a pull request is opened or updated (GitHub only)
- **Manual trigger**: Started on demand via gcloud or the Cloud Console

#### Cloud Build ACE Exam Focus Points

- Cloud Build steps share a workspace at `/workspace`; files written by one step are
  readable by subsequent steps
- The `$COMMIT_SHA` substitution is available for branch triggers; `$TAG_NAME` is
  available for tag triggers
- Cloud Build service account must have appropriate IAM permissions to push to Artifact
  Registry, deploy to GKE, etc.
- The default timeout is 10 minutes; increase it for longer builds using the `timeout`
  field
- Build logs go to Cloud Logging by default; configure `options.logging` to control
  destination

#### Cloud Build Review Questions

1. What does the `waitFor` field in a build step accomplish?
2. Which substitution variable contains the Git commit hash that triggered the build?
3. What IAM role must be granted to the Cloud Build service account to push Docker images
   to Artifact Registry?

---

### Required Reading 2: Artifact Registry

**Source**: Google Cloud Documentation — Artifact Registry Overview

**URL**: `https://cloud.google.com/artifact-registry/docs/overview`

#### Artifact Registry Key Terms

- **Repository**: The storage container for a specific artifact format in a specific
  region; format and location cannot be changed after creation
- **Repository format**: Specifies the artifact type (DOCKER, MAVEN, NPM, PYTHON, APT,
  YUM, GENERIC)
- **Repository URL**: Format is `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME` for
  Docker; used as the image prefix
- **Cleanup policy**: Rules that automatically delete artifacts meeting specified criteria
  (age, tag, version count)
- **CMEK**: Customer-Managed Encryption Keys; optional alternative to Google-managed
  encryption for repositories

#### Artifact Registry vs. Container Registry

| Feature | Artifact Registry | Container Registry |
|---|---|---|
| Supported formats | Docker, Maven, npm, Python, Apt, Yum, Generic | Docker only |
| Repository URL format | REGION-docker.pkg.dev/PROJECT/REPO | gcr.io/PROJECT |
| Cleanup policies | Yes | No |
| VPC Service Controls | Yes | Limited |
| Recommended | Yes | Deprecated (use AR instead) |

#### Artifact Registry ACE Exam Focus Points

- Artifact Registry is the recommended replacement for Container Registry; new projects
  should use Artifact Registry
- Docker image URLs use the format:
  `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:TAG`
- Run `gcloud auth configure-docker REGION-docker.pkg.dev` before pushing with docker CLI
- Artifact Registry is regional; create repositories in the same region as your Cloud
  Build workers and GKE clusters to avoid egress charges
- The Cloud Build service account needs `roles/artifactregistry.writer` to push images

#### Artifact Registry Review Questions

1. What is the Docker image URL format for Artifact Registry?
2. What command configures Docker to authenticate to Artifact Registry?
3. What role is required for the Cloud Build service account to push to Artifact Registry?

---

### Required Reading 3: Cloud Deploy

**Source**: Google Cloud Documentation — Cloud Deploy Overview

**URL**: `https://cloud.google.com/deploy/docs/overview`

#### Cloud Deploy Key Terms

- **Delivery pipeline**: Defines the ordered sequence of targets and deployment
  configuration for an application; specified in a YAML file
- **Target**: A deployment destination (GKE cluster, Cloud Run service, or Anthos);
  can require approval before a rollout proceeds
- **Release**: An immutable snapshot of the application artifacts and Kubernetes manifests
  at the time of release creation
- **Rollout**: The deployment of a specific release to a specific target in the pipeline;
  tracks deployment status and history
- **Approval**: A gate between pipeline stages requiring a designated user to approve
  before the rollout advances to the next target
- **Skaffold**: The underlying tool Cloud Deploy uses to render and apply Kubernetes
  manifests; a `skaffold.yaml` file is required in the repository

#### Cloud Deploy Pipeline Model

A release flows through targets in order:

```text
Release Created → Dev Rollout (auto) → Staging Rollout (auto) → Production Rollout (requires approval)
```

Each rollout is tracked independently. If a rollout fails, Cloud Deploy does not
automatically promote to the next target.

#### Cloud Deploy ACE Exam Focus Points

- Cloud Deploy manages the delivery (CD) portion; Cloud Build handles the build (CI)
  portion; they are complementary services
- `requireApproval: true` on a target adds a human gate before that environment is
  updated; this is the standard pattern for production gating
- Cloud Deploy creates a release, not directly a deployment; the release is then
  rolled out to each target
- Cloud Deploy integrates with Cloud Audit Logs for a full trail of every deployment
  action and approval
- Rolling deployments on GKE are controlled by the Kubernetes Deployment strategy
  settings, not Cloud Deploy itself

---

### Required Reading 4: GKE Integration

**Source**: Google Cloud Documentation — Deploying to GKE using Cloud Build

**URL**: `https://cloud.google.com/build/docs/deploying-builds/deploy-gke`

#### GKE Integration Key Terms

- **kubectl builder**: `gcr.io/cloud-builders/kubectl` — Cloud Build builder that applies
  Kubernetes manifests or runs kubectl commands
- **`gke-deploy` builder**: A GCP-provided builder that packages kubectl deployment
  with rollout status checking and rollback support
- **Rolling update**: Kubernetes Deployment strategy that gradually replaces old pods
  with new ones; controlled by `maxSurge` and `maxUnavailable` settings
- **Image tag immutability**: Best practice of tagging images with `$COMMIT_SHA` rather
  than `latest` so every deployment is traceable to a specific commit

#### GKE Rolling Deployment Settings

```yaml
strategy:
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
  type: RollingUpdate
```

- `maxSurge`: Number of extra pods that can exist above the desired count during update
- `maxUnavailable`: Number of pods that can be unavailable during update; 0 ensures
  no downtime

---

### Pre-Lab Checklist

Before starting Lab 13, confirm you can answer yes to each item:

- I can write a cloudbuild.yaml with at least 2 steps and a substitution variable
- I know how to create an Artifact Registry Docker repository with gcloud
- I understand the Cloud Build service account and what permissions it needs
- I can describe the Cloud Deploy pipeline: pipeline, target, release, rollout
- I know what `requireApproval: true` does in a Cloud Deploy target

---

### Additional Resources

- Cloud Build documentation:
  `https://cloud.google.com/build/docs`
- Artifact Registry documentation:
  `https://cloud.google.com/artifact-registry/docs`
- Cloud Deploy documentation:
  `https://cloud.google.com/deploy/docs`
- ACE exam guide:
  `https://cloud.google.com/certification/guides/cloud-engineer`
