# Discussion — Module 08

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Run, App Engine, and Cloud Functions — Serverless Compute

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. In your peer responses, you may respond to classmates who chose any scenario.

Initial Post due: Wednesday at 11:59 PM Central

Peer Responses due: Sunday at 11:59 PM Central

---

## Scenario A — The Platform Selection Decision

A software engineering team is building a new backend for a mobile app. The backend consists of three components:

Component 1 is a REST API that handles user authentication and data queries. It receives traffic proportional to app usage — almost zero overnight and several hundred requests per second during peak hours. The API is built in Go and is already containerized.

Component 2 is an image resize pipeline. Whenever a user uploads a profile photo to Cloud Storage, the image must be automatically resized to three sizes (thumbnail, medium, full) and the results written back to Cloud Storage. Each resize operation takes less than 5 seconds.

Component 3 is a scheduled report generator that runs every day at 3 AM, queries Firestore for the previous day's user activity, and generates a PDF report stored in Cloud Storage. The report generation takes approximately 8 minutes.

In 175–225 words, address the following:

- For each component, recommend a specific GCP serverless compute service and explain why it is the most appropriate choice.
- Component 1 receives near-zero traffic overnight. Explain what "scale to zero" means in the context of your recommended platform and whether the team should set `--min-instances=1`. What is the tradeoff?
- Component 3 runs for 8 minutes. Identify any execution time limits that apply to your recommended platform and state whether the 8-minute runtime fits within those limits.

---

## Scenario B — The App Engine Migration

A SaaS company is running a customer portal on App Engine Standard using Python 3.9. They are preparing to release a major new version with a redesigned UI and new API endpoints. The previous version must remain available as a rollback option for at least 72 hours after the new version is released. Some enterprise customers require the ability to opt out of the new UI and stay on the old version for 30 additional days.

In 175–225 words, address the following:

- Describe the App Engine deployment strategy that allows the new version to receive the majority of traffic while preserving the old version as a rollback option. What gcloud command performs the initial traffic migration, and what command reverts it if a critical bug is found?
- App Engine versions accumulate over time and incur storage costs. After the 72-hour rollback window has passed and all customers have migrated, which gcloud command removes the old version? What happens to traffic if you delete the currently serving version by accident?
- Enterprise customers who need to remain on the old version for 30 additional days will connect to a version-specific URL. How does App Engine expose individual version URLs, and what does that URL format look like for a version named `v3` in the `default` service of project `my-project`?

---

## Scenario C — The Serverless Architecture Trade-offs

An engineering team is debating the architecture for a new event processing pipeline. They receive 50,000 events per hour from IoT sensors via Pub/Sub. Each event requires a lookup in Cloud Firestore, a transformation, and a write to BigQuery. The team is considering three architectures:

Architecture 1: Cloud Functions triggered directly by Pub/Sub, one function invocation per message.

Architecture 2: Cloud Run service with a Pub/Sub push subscription that delivers batches of messages to an HTTP endpoint.

Architecture 3: GKE Autopilot with a consumer application that pulls messages from Pub/Sub using the Pull model.

In 175–225 words, address the following:

- Compare the three architectures for this workload. For each, describe the operational overhead, cost model, and any important constraints (message ordering, at-least-once delivery, batching behavior).
- At 50,000 events per hour (approximately 14 per second), which architecture provides the best balance of cost, simplicity, and reliability? Justify your answer.
- The team later learns that 0.5% of events require special handling that takes 90 seconds per event. How does this requirement affect your recommendation? Which architectures can accommodate 90-second processing per message, and which cannot?

---

## Peer Response Guidelines

Your peer responses must be at least 50 words each. A strong peer response does at least one of the following:

- Challenges the platform selection for one of the components in Scenario A with a specific technical reason
- Identifies a missing step or incorrect gcloud command syntax in the App Engine deployment described in Scenario B
- Questions the 90-second processing constraint analysis from Scenario C and proposes a different architecture that addresses it
- References a specific lab step or gcloud command from this module's lab that implements part of the classmate's design

Responses that consist only of agreement without substantive technical additions receive no credit.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all sub-questions accurately. Uses correct serverless terminology (revision, scale-to-zero, traffic split, concurrency, trigger, execution timeout). Justifies design choices with reference to specific platform features, execution limits, or configuration parameters. 175–225 words.
- 3–4 pts: Addresses most sub-questions but uses vague terminology or lacks specific technical justification.
- 1–2 pts: Only addresses one sub-question or contains significant factual errors about serverless platforms.
- 0 pts: Initial post not submitted by the Wednesday deadline.

Peer Responses — 4 Points:

- 4 pts: Two responses submitted by Sunday, each at least 50 words, each contributing specific technical additions or corrections.
- 2 pts: Only one qualifying response, or both are superficial.
- 0 pts: No peer responses submitted.

---

Professor Nash note: The most common mistake in serverless platform selection is treating all three options as interchangeable because they all say "no servers." They are not. Cloud Functions is specifically optimized for event-driven, short-lived, lightweight handlers — it shines when the trigger is a GCP event. Cloud Run is the right choice when you have a container and want HTTP-driven, zero-infrastructure scaling. App Engine Standard is best when you have source code in a supported framework and want the absolute minimum deployment complexity. Mixing these up on the ACE exam costs points. In Scenario A, every component points clearly to a different service for a different reason. If your answer assigns the same service to all three, re-read the platform selection rules in the reading guide.

---

End of Discussion — Module 08

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer
