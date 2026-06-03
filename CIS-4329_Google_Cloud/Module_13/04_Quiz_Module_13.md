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
