# Discussion: Module 13 — CI/CD with Cloud Build and Artifact Registry

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This discussion asks you to design a CI/CD pipeline for a realistic software deployment
scenario. You will apply Cloud Build, Artifact Registry, and Cloud Deploy concepts from
Module 13 and reflect on a deployment challenge from your own experience.

**Initial post due**: Thursday at 11:59 PM Central

**Peer responses due**: Sunday at 11:59 PM Central

---

### Scenario

A fintech company called PayStream is modernizing their payment processing application.
The application is a containerized microservice written in Java. The development team
pushes code to GitHub multiple times per day. Here are their requirements:

- Every push to a feature branch should trigger a build and run unit tests, but NOT
  deploy anywhere
- Every push to the `main` branch should build the image, run tests, push to Artifact
  Registry, and deploy to a development GKE cluster automatically
- Deployments to the staging environment should happen automatically after dev, but
  only if the health check passes post-deployment
- Deployments to the production GKE cluster must require a manual approval from the
  Release Manager role
- The production environment has a strict requirement: no image may be deployed unless
  it was built from a tagged release commit (e.g., `v1.2.3`)
- All build and deployment activity must be auditable with full history

---

### Response Requirements

#### Part 1: Cloud Build Pipeline Design

Describe the `cloudbuild.yaml` steps you would write for the `main` branch build. List
the steps in order, specify the builder image for each step, and explain what each step
does. Include the substitution variable you would use to tag the Docker image. You do not
need to write full YAML — describe the steps in plain text. (4–6 sentences)

#### Part 2: Trigger Configuration

Describe the trigger configuration for each of the two scenarios: feature branch pushes
and `main` branch pushes. What branch pattern would you use for each, and how would you
make the feature branch trigger run tests but NOT deploy? (3–4 sentences)

#### Part 3: Cloud Deploy Pipeline Design

Describe the Cloud Deploy pipeline structure for this application. How many targets are
in the pipeline, what is the order, and which targets have `requireApproval: true`?
How does Cloud Deploy's release model support the auditability requirement? (3–4 sentences)

#### Part 4: Tag-Based Production Gate

The production requirement states that only images built from a tagged release commit
may be deployed. Describe the Cloud Build trigger configuration that enforces this
constraint at the build level, and explain what additional GCP service you would use to
enforce it at the deploy level. (2–3 sentences)

#### Part 5: Reflection

Describe a deployment process you have experienced or observed that was manual, error-
prone, or slow. What problems did the manual process cause? How would an automated
CI/CD pipeline with the tools in Module 13 have improved the situation? (3–5 sentences;
hypothetical scenarios are acceptable.)

---

### Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Correct Cloud Build steps with builder images and substitution variable | 25 |
| Part 2: Correct trigger patterns distinguishing feature vs. main branch | 20 |
| Part 3: Correct Cloud Deploy pipeline with approval gate and auditability | 20 |
| Part 4: Tag trigger and deploy-time enforcement service identified | 15 |
| Part 5: Thoughtful reflection | 5 |
| Peer response 1: Substantive technical engagement | 7 |
| Peer response 2: Substantive technical engagement | 8 |
| **Total** | **100** |

---

### Peer Response Guidelines

A substantive peer response does at least one of the following:

- Proposes a different step order or an additional step (vulnerability scan, static
  analysis) with technical justification
- Challenges the trigger branch pattern with a more specific or general regex and
  explains why
- Points out a gap in the approval gate design (who can approve, what notification goes
  out)
- Identifies the GCP service for deploy-time image enforcement if the original poster
  did not

---

### Discussion Hints

For Part 2, a separate `cloudbuild.yaml` file for feature branches (without deploy
steps) is one valid approach. Another is using a single YAML with conditional logic via
custom substitution variables. Both are acceptable — explain your choice.

For Part 3, remember that Cloud Deploy maintains a full audit trail of every release,
rollout, approval action, and deployment result in Cloud Audit Logs. This directly
addresses the auditability requirement without any additional configuration.

For Part 4, the deploy-time enforcement service that verifies image provenance before
deployment to a GKE cluster is Binary Authorization. It works with attestations generated
during the build pipeline to verify that images meet defined policies before GKE admits
them as pods.
