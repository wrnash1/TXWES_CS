# Video Script: Module 13 — CI/CD with Cloud Build and Artifact Registry (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 13. I am Professor Nash. Today we cover CI/CD — Continuous Integration
and Continuous Delivery — on Google Cloud Platform, using Cloud Build and Artifact
Registry.

CI/CD automates the process of building, testing, and deploying your application code.
Every time a developer pushes code, a pipeline runs automatically — compiling, testing,
packaging, and deploying to the target environment. This eliminates manual deployment
steps and reduces the time between writing code and running it in production.

By the end of this two-part video you will be able to configure Cloud Build triggers,
write build config YAML files, store artifacts in Artifact Registry, and deploy to GKE
using Cloud Deploy.

---

### Section 1: CI/CD Concepts

A CI/CD pipeline has two phases:

- **Continuous Integration (CI)** — automatically build and test code on every push;
  catch bugs early before they reach production
- **Continuous Delivery (CD)** — automatically deploy tested builds to target
  environments; production deployments may require a manual approval gate

On GCP, the primary CI/CD tools are:

- **Cloud Build** — managed build service; executes build steps in containers
- **Artifact Registry** — stores Docker images, Maven/Gradle packages, npm modules, and
  other artifacts
- **Cloud Deploy** — managed continuous delivery service for GKE and Cloud Run
- **Cloud Source Repositories** — managed Git hosting on GCP (also integrates with
  GitHub and Bitbucket)

---

### Section 2: Cloud Build Overview

Cloud Build executes builds as a series of **build steps**. Each step runs a Docker
container. Google provides pre-built builder images for common tasks (Docker, gcloud,
npm, Maven, Gradle, etc.) and you can bring your own.

A build is defined in a **cloudbuild.yaml** file (or cloudbuild.json) stored in your
repository root.

#### Basic Build Config Structure

```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA']

  - name: 'gcr.io/cloud-builders/gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'my-service'
      - '--image=us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'

images:
  - 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
```

#### Substitution Variables

Cloud Build provides built-in substitution variables:

- `$PROJECT_ID` — the GCP project ID
- `$BUILD_ID` — the unique build ID
- `$COMMIT_SHA` — the Git commit SHA that triggered the build
- `$BRANCH_NAME` — the Git branch name
- `$TAG_NAME` — the Git tag name (for tag-triggered builds)
- `$REPO_NAME` — the repository name
- `$SHORT_SHA` — first 7 characters of the commit SHA

You can also define custom substitution variables in the trigger configuration.

---

### Section 3: Cloud Build Triggers

A trigger automatically starts a build when specified conditions are met in a connected
repository.

#### Creating a Trigger

```bash
# Connect to GitHub repository first via Cloud Console
# Then create a trigger via gcloud

# Create a trigger that fires on push to the main branch
gcloud builds triggers create github \
  --repo-name=my-app-repo \
  --repo-owner=my-github-org \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml \
  --description="Build and deploy on push to main"

# Create a trigger that fires on any push to a release/* branch
gcloud builds triggers create github \
  --repo-name=my-app-repo \
  --repo-owner=my-github-org \
  --branch-pattern="^release/.*$" \
  --build-config=cloudbuild.yaml \
  --description="Build on release branch push"

# Create a tag trigger (fires when a Git tag matching v*.*.* is pushed)
gcloud builds triggers create github \
  --repo-name=my-app-repo \
  --repo-owner=my-github-org \
  --tag-pattern="^v[0-9]+\.[0-9]+\.[0-9]+$" \
  --build-config=cloudbuild.yaml

# List all triggers
gcloud builds triggers list

# Manually run a trigger
gcloud builds triggers run TRIGGER_ID \
  --branch=main
```

#### Trigger Filter Options

- **Branch pattern** — regex matching branch names; `^main$` matches only `main`
- **Tag pattern** — regex matching Git tags; useful for production releases
- **File include/exclude** — trigger only when specific files are modified;
  useful for monorepos

---

### Section 4: Advanced Build Config Features

#### Multi-Step Build with Testing

```yaml
# cloudbuild.yaml with test step
steps:
  # Step 1: Install dependencies
  - name: 'node:18'
    entrypoint: 'npm'
    args: ['install']

  # Step 2: Run unit tests
  - name: 'node:18'
    entrypoint: 'npm'
    args: ['test']

  # Step 3: Build Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '-t'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
      - '.'

  # Step 4: Push to Artifact Registry
  - name: 'gcr.io/cloud-builders/docker'
    args:
      - 'push'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'

timeout: '600s'

options:
  machineType: 'E2_HIGHCPU_8'
  logging: CLOUD_LOGGING_ONLY
```

#### Step Dependencies (Parallel Steps)

```yaml
steps:
  # These two steps run in parallel because they have no dependency
  - name: 'node:18'
    id: 'test-unit'
    entrypoint: 'npm'
    args: ['run', 'test:unit']

  - name: 'node:18'
    id: 'test-lint'
    entrypoint: 'npm'
    args: ['run', 'lint']

  # This step waits for both test steps to complete
  - name: 'gcr.io/cloud-builders/docker'
    id: 'build-image'
    waitFor: ['test-unit', 'test-lint']
    args: ['build', '-t', 'IMAGE_URL', '.']
```

Using `id` and `waitFor` enables parallel execution of independent steps, reducing
overall build time.

---

### Closing — Part 1

In Part 1 we covered:

- CI/CD concepts and the GCP CI/CD tool family
- Cloud Build: build steps, cloudbuild.yaml, substitution variables
- Cloud Build triggers: branch triggers, tag triggers, file filters
- Advanced build config: multi-step builds, testing, parallel steps

In Part 2 we cover Artifact Registry, Cloud Deploy for rolling deployments, GKE
integration, and the ACE exam patterns for CI/CD.

See you in Part 2.
