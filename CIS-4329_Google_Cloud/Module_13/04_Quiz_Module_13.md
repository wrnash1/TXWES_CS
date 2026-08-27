# Quiz: Module 13 — CI/CD with Cloud Build and Artifact Registry

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A development team wants every push to the `main` branch to automatically build a Docker
image and push it to Artifact Registry. Which Cloud Build feature enables this automation?

- A) Cloud Build worker pools
- B) Cloud Build triggers with a branch pattern
- C) Cloud Build substitution variables
- D) Cloud Build private pools

Correct answer: B — Cloud Build triggers watch a repository and automatically start a
build when specified events occur. A trigger with branch pattern `^main$` fires on every
push to the `main` branch. Worker pools and private pools are compute configurations,
not automation mechanisms. Substitution variables are used within a build config, not
to start builds automatically.

---

### Question 2

In a `cloudbuild.yaml` file, two steps both have `waitFor: ['build-image']`. What is
the effect?

- A) Both steps run sequentially after the build-image step
- B) Both steps run in parallel after the build-image step completes
- C) The second step waits for both the first step and build-image to complete
- D) The build fails because two steps cannot share the same waitFor value

Correct answer: B — When multiple steps reference the same `waitFor` step ID, they all
become eligible to run as soon as that step completes. Cloud Build executes eligible
steps in parallel. This is the standard pattern for parallelizing push operations for
multiple image tags after a single build step.

---

### Question 3

A team wants to deploy container images from Cloud Build to an Artifact Registry
repository. The build fails with a permission denied error on the push step. What is
the most likely cause?

- A) The Docker image tag format is incorrect
- B) The Cloud Build service account has not been granted the Artifact Registry Writer role
- C) Artifact Registry does not accept pushes from Cloud Build
- D) The repository format is set to Maven instead of Docker

Correct answer: B — Cloud Build executes with the permissions of the Cloud Build service
account. By default this account does not have write access to Artifact Registry
repositories. You must grant `roles/artifactregistry.writer` (or the equivalent
predefined role) to the Cloud Build service account
(`[PROJECT_NUMBER]@cloudbuild.gserviceaccount.com`).

---

### Question 4

Which substitution variable in Cloud Build contains the first 7 characters of the Git
commit hash that triggered the build?

- A) `$COMMIT_SHA`
- B) `$SHORT_SHA`
- C) `$BUILD_ID`
- D) `$REVISION_ID`

Correct answer: B — `$SHORT_SHA` is the abbreviated 7-character commit hash.
`$COMMIT_SHA` contains the full 40-character commit hash. `$BUILD_ID` is the Cloud Build
build identifier (not a Git hash). `$REVISION_ID` is not a standard Cloud Build
substitution variable.

---

### Question 5

A team uses Artifact Registry to store Docker images. They want images older than 30 days
that are not tagged with `stable` or `production` to be automatically deleted. Which
Artifact Registry feature handles this?

- A) Container Analysis vulnerability scanning
- B) VPC Service Controls for the repository
- C) Cleanup policies on the repository
- D) Object lifecycle rules on the underlying Cloud Storage bucket

Correct answer: C — Artifact Registry cleanup policies allow you to define rules that
automatically delete images based on age, tags, or version count. Container Analysis is
for vulnerability scanning. VPC Service Controls restrict network access. Artifact
Registry does not use Cloud Storage bucket lifecycle rules — it manages storage
internally.

---

### Question 6

Which statement correctly describes the relationship between Cloud Build and Cloud Deploy?

- A) Cloud Deploy replaces Cloud Build; you only need one service
- B) Cloud Build handles building and testing (CI); Cloud Deploy handles delivery
   pipeline management (CD)
- C) Cloud Build is only for non-containerized applications; Cloud Deploy is for
   containers
- D) Cloud Deploy must be used; Cloud Build cannot deploy to GKE directly

Correct answer: B — Cloud Build is the CI (Continuous Integration) service that builds,
tests, and packages applications. Cloud Deploy is the CD (Continuous Delivery) service
that manages delivery pipelines with targets, releases, rollouts, and approval gates.
They are complementary. Cloud Build can also deploy directly to GKE via kubectl steps
without Cloud Deploy, though Cloud Deploy provides more structured pipeline management.

---

### Question 7

A team has a Cloud Deploy delivery pipeline with three targets: dev, staging, and
production. The production target has `requireApproval: true`. A release is deployed
to dev and staging successfully. What happens next?

- A) The release automatically deploys to production after staging succeeds
- B) The production rollout is created but waits for a designated approver to approve
   before applying
- C) The build fails because production approval is not configured in Cloud Build
- D) Cloud Deploy sends an email to all project owners requesting approval

Correct answer: B — When a Cloud Deploy target has `requireApproval: true`, the rollout
to that target is created in a PENDING\_APPROVAL state. It does not proceed until a
user with the `clouddeploy.approver` role approves the rollout via the Console or
`gcloud deploy rollouts approve`. Cloud Deploy sends notifications via Pub/Sub or Cloud
Monitoring alerts, not direct emails to project owners.

---

### Question 8

What is the correct Docker image URL format for an image stored in Artifact Registry in
the `us-central1` region?

- A) `gcr.io/PROJECT_ID/REPOSITORY/IMAGE:TAG`
- B) `docker.io/PROJECT_ID/REPOSITORY/IMAGE:TAG`
- C) `us-central1-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:TAG`
- D) `us-central1.artifacts.googleapis.com/PROJECT_ID/REPOSITORY/IMAGE:TAG`

Correct answer: C — Artifact Registry Docker repositories use the URL format
`REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/IMAGE:TAG`. The old Container Registry
format was `gcr.io/PROJECT_ID/IMAGE:TAG`. Artifact Registry is the replacement and uses
the `pkg.dev` domain.

---

### Question 9

A `cloudbuild.yaml` does not include a `timeout` field. What is the default maximum
build duration?

- A) 2 minutes
- B) 10 minutes
- C) 60 minutes
- D) 24 hours

Correct answer: B — The default Cloud Build timeout is 10 minutes. If a build exceeds
10 minutes without an explicit `timeout` field, it is automatically cancelled. You can
increase the timeout up to 24 hours by setting `timeout: '86400s'` in the build config.
Complex builds (large Docker images, extensive test suites) often require a longer
timeout.

---

### Question 10

A team stores Docker images in Artifact Registry and wants to scan them for known
vulnerabilities before deploying. Which GCP service integrates with Artifact Registry
for this purpose?

- A) Cloud Armor
- B) Security Command Center
- C) Container Analysis (Artifact Analysis)
- D) Binary Authorization

Correct answer: C — Container Analysis (also called Artifact Analysis) automatically
scans Docker images pushed to Artifact Registry for known OS and package vulnerabilities.
It integrates natively with Artifact Registry and publishes vulnerability findings to
the Cloud Console. Binary Authorization enforces deploy-time policies based on image
attestations. Cloud Armor protects HTTP endpoints. Security Command Center aggregates
security findings but does not perform image scanning itself.

---

### Question 11 (5 points)

A Cloud Build step needs to access a secret API key stored in Secret Manager
without embedding it in the `cloudbuild.yaml` file. Which Cloud Build feature
enables this?

- A) Cloud Build substitution variables prefixed with `_SECRET_`
- B) `availableSecrets` block in `cloudbuild.yaml` referencing the secret by
   resource name; the secret value is injected as an environment variable
- C) Store the secret in a Cloud Storage bucket and download it in the first step
- D) Use `gcloud secrets versions access` inline in the step's shell command

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Substitution variables (prefixed with `_`) are user-defined values passed at build invocation time; they are stored in the build config or trigger, not in Secret Manager, and would expose the secret in the config file.
  - C) Storing secrets in Cloud Storage provides no encryption-at-rest advantage over embedding them in the config; Secret Manager is the purpose-built service for secret storage with IAM-controlled access.
  - D) `gcloud secrets versions access` can retrieve a secret value at runtime, but embedding it in a shell command exposes the value in build logs; the `availableSecrets` approach keeps the value out of logs.

---

### Question 12 (5 points)

You need to build a Docker image in Cloud Build that requires access to a private
NPM registry inside your VPC. The default Cloud Build workers cannot reach your
VPC. Which Cloud Build feature resolves this?

- A) Cloud Build triggers with a VPC annotation
- B) Cloud Build private pools connected to your VPC
- C) A Serverless VPC Access connector attached to Cloud Build
- D) VPC peering between the Cloud Build project and the VPC project

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Build triggers do not have a VPC annotation; they define when builds start, not where the build workers run.
  - C) Serverless VPC Access connectors are used by Cloud Run, Cloud Functions, and App Engine to reach VPC resources; they are not a feature of Cloud Build worker infrastructure.
  - D) VPC peering connects two VPC networks but does not route Cloud Build's default worker traffic (which runs in Google's managed project) into your VPC; private pools are the mechanism for this.

---

### Question 13 (5 points)

A team has a Cloud Deploy pipeline: `dev → staging → production`. After a successful
release to staging, a team member runs:

```text
gcloud deploy releases promote --release=my-release-001 \
  --delivery-pipeline=my-pipeline --region=us-central1 --to-target=production
```

The production target has `requireApproval: true`. What is the state of the
production rollout immediately after this command?

- A) `SUCCEEDED` — the promote command bypasses approval for manual promotions
- B) `PENDING_APPROVAL` — the rollout is created but waits for an approver
- C) `IN_PROGRESS` — deployment to production has started
- D) `FAILED` — you cannot manually promote when approval is required

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Manual promotions via `gcloud deploy releases promote` do not bypass the `requireApproval` setting; the approval gate applies regardless of whether the promotion is automated or manual.
  - C) The rollout does not begin applying changes until an authorized user approves it; `IN_PROGRESS` state is only reached after approval.
  - D) The command succeeds — it creates the rollout in `PENDING_APPROVAL` state; it does not fail.

---

### Question 14 (5 points)

A Cloud Build build fails intermittently with `exit status 137` on the Docker build
step. What does exit status 137 typically indicate?

- A) The Docker daemon was not found in the build worker
- B) The build step exceeded its memory limit and was killed by the OS (OOM kill)
- C) The Dockerfile contains a syntax error at line 137
- D) The build exceeded the 10-minute default timeout

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Exit status 137 is a Linux signal code (SIGKILL = 9; 128 + 9 = 137); it indicates the process was forcibly terminated, not that Docker was missing.
  - C) Exit status 137 is a process termination signal, not a file line reference; Dockerfile syntax errors produce different exit codes with parser error messages.
  - D) A build timeout results in a timeout-specific error message and a different exit code; exit status 137 specifically indicates SIGKILL, most commonly caused by OOM conditions.

---

### Question 15 (5 points)

Binary Authorization is configured on a GKE cluster with a policy that requires
all deployed images to have an attestation from the `production-approver` attestor.
A Cloud Build pipeline builds a new image but does not create the attestation.
What happens when Kubernetes tries to deploy the image?

- A) Kubernetes deploys the image and logs a warning to Cloud Logging
- B) The deployment is blocked by Binary Authorization and the pod is not created
- C) Binary Authorization scans the image and creates the attestation automatically
- D) The deployment proceeds but the pod is immediately terminated after 60 seconds

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Binary Authorization is an admission controller that enforces policy at admission time; a missing attestation causes an admission denial, not a warning.
  - C) Binary Authorization enforces attestation policies; it does not create attestations — attestations are created by authorized parties (e.g., Cloud Build steps using KMS to sign images).
  - D) Once a pod is admitted and running, Binary Authorization does not retroactively terminate it; enforcement happens at admission time only.

---

### Question 16 (5 points)

A team's `cloudbuild.yaml` includes a step that runs unit tests. If the tests fail,
they want the build to be marked as failed and subsequent steps to not run. What
Cloud Build behavior ensures this?

- A) Add `failFast: true` to the step definition
- B) This is the default behavior — if any step exits with a non-zero code, the
   build fails and remaining steps do not execute
- C) Add `onFailure: FAIL` to each step
- D) Use a `finally` block to catch test failures and mark the build failed

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `failFast` is not a Cloud Build step field; Cloud Build's default behavior is already to fail the build on any non-zero exit code.
  - C) `onFailure` is not a valid Cloud Build step field; build step failure behavior is controlled by exit codes and the default fail-fast build semantics.
  - D) Cloud Build does not have a `finally` block concept in `cloudbuild.yaml`; shell-level `finally`/`trap` constructs can be used inside a step's shell command but are separate from build configuration.

---

### Question 17 (5 points)

You want to use Cloud Build to automatically deploy to Cloud Run after each
successful build. The `gcloud run deploy` step in `cloudbuild.yaml` fails with
permission denied. What IAM role must be granted to the Cloud Build service account?

- A) `roles/run.admin`
- B) `roles/run.invoker`
- C) `roles/run.developer`
- D) `roles/compute.admin`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `roles/run.invoker` grants the ability to invoke (send HTTP requests to) a Cloud Run service; it does not grant the ability to deploy or update services.
  - C) `roles/run.developer` grants the ability to deploy and manage Cloud Run services but does not include the permission to set IAM policies on services; `roles/run.admin` includes both deployment and IAM management permissions needed for a typical CI/CD deployment step.
  - D) `roles/compute.admin` manages Compute Engine resources; it has no effect on Cloud Run deployments.

---

### Question 18 (5 points)

A team wants to store both Docker images and Maven JAR artifacts in the same GCP
project using Artifact Registry. What is the correct approach?

- A) Create one Artifact Registry repository with format `DOCKER` and store all
   artifacts there
- B) Create two separate Artifact Registry repositories — one with format `DOCKER`
   and one with format `MAVEN`
- C) Artifact Registry only supports Docker images; Maven artifacts must use
   Nexus or JFrog Artifactory
- D) Create one Artifact Registry repository with format `UNIVERSAL` that supports
   all artifact types

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Artifact Registry repositories are format-specific; a Docker repository cannot store Maven JARs and vice versa.
  - C) Artifact Registry supports Docker, Maven, npm, Python (PyPI), APT, YUM, and other formats natively; it does not require external repository managers.
  - D) There is no `UNIVERSAL` format in Artifact Registry; each repository has a specific format that determines what artifact types it stores.

---

### Question 19 (5 points)

What is the purpose of the `_DEFAULT_REGION` prefix convention for user-defined
substitutions in Cloud Build?

- A) Substitutions starting with `_DEFAULT_` are automatically populated from the
   GCP project's default configuration
- B) User-defined substitutions must start with `_` (underscore) to distinguish
   them from built-in Cloud Build substitutions; `_DEFAULT_REGION` is simply a
   variable named according to team convention
- C) Substitutions prefixed with `_DEFAULT_` are shared across all triggers in
   the project
- D) The `_DEFAULT_` prefix enables the substitution to be used in the build's
   trigger filter expressions

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Build does not automatically populate user-defined substitutions from project defaults; built-in substitutions like `$PROJECT_ID` are auto-populated, but user-defined `_` variables must be explicitly provided.
  - C) User-defined substitutions are scoped to the trigger or build invocation that defines them; they are not shared across all triggers in the project.
  - D) Trigger filter expressions use branch patterns and tag patterns, not substitution variables; substitutions are used within the build steps themselves.

---

### Question 20 (5 points)

A Cloud Build trigger is connected to a GitHub repository. A developer pushes to
the `feature/login` branch. The trigger has the branch pattern `^main$`. What happens?

- A) The build is triggered because the pattern matches any branch containing `main`
- B) No build is triggered because `feature/login` does not match the `^main$`
   pattern
- C) The build is triggered but only runs linting steps, not the full pipeline
- D) Cloud Build queues the build and runs it when the branch is merged to main

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `^main$` is a regular expression anchored with `^` (start) and `$` (end); it matches only the string `main` exactly, not branches that contain the word `main` as a substring.
  - C) Cloud Build triggers do not have branch-conditional step filtering; the trigger either fires the full `cloudbuild.yaml` or does not fire at all.
  - D) Cloud Build does not queue builds for future branch events; each trigger evaluates the push event at the moment it occurs and either fires or does not.
