# Reading Guide: Module 10 – Pub/Sub and Cloud Functions: Event-Driven Architecture
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 10 – Pub/Sub and Cloud Functions: Event-Driven Architecture**! Event-driven architectures decouple services by passing messages through an intermediary rather than calling each other directly. This module covers Cloud Pub/Sub for reliable asynchronous messaging, Cloud Functions for serverless event handlers, and Eventarc for routing events from GCP services to Cloud Run or Cloud Functions. The ACE exam tests your ability to design event pipelines, configure subscriptions, and select the right trigger type for a given scenario.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Cloud Pub/Sub**: A fully managed, globally distributed message queue service. Publishers send messages to a **topic**; subscribers receive messages through **subscriptions**. Pub/Sub guarantees at-least-once delivery — a message may be delivered more than once, so consumers should be idempotent. Messages are retained for up to 7 days if unacknowledged.

*   **Topic**: The named resource in Pub/Sub to which publishers send messages. A single topic can have multiple subscriptions, allowing the same message to be delivered to multiple independent consumers (fan-out pattern).

*   **Subscription**: A named resource representing a stream of messages from a single topic. Pull subscriptions require the subscriber to call the Pub/Sub API to retrieve messages. Push subscriptions have Pub/Sub deliver messages to an HTTPS endpoint (such as a Cloud Run service or App Engine app) automatically.

*   **Cloud Functions (1st/2nd gen)**: A serverless, event-driven compute service. A function is triggered by an event (HTTP request, Pub/Sub message, Cloud Storage object finalization, Firestore document change) and executes in an isolated, ephemeral environment. 2nd generation Cloud Functions are built on Cloud Run and support longer timeouts (up to 60 minutes) and higher concurrency.

*   **Eventarc**: A GCP service that routes events from over 90 GCP event sources (including Audit Log events, Cloud Storage, Pub/Sub) to Cloud Run services or Cloud Functions 2nd gen targets using CloudEvents format. Eventarc simplifies connecting GCP service events to serverless handlers without writing custom Pub/Sub notification code.

*   **Dead Letter Topic**: A Pub/Sub topic configured on a subscription to receive messages that could not be successfully delivered after a maximum number of delivery attempts. Use a dead letter topic to capture and investigate failed messages without losing them.

---

### 2. Certification Exam Tips

*   **Pull vs. Push subscriptions — know when to use each**: Pull is appropriate when the subscriber controls its own consumption rate (e.g., a batch processing job). Push is appropriate when you want Pub/Sub to proactively deliver messages to an HTTP endpoint without the subscriber polling — use push for Cloud Run or App Engine backends that should react immediately to messages.

*   **At-least-once delivery requires idempotent consumers**: The ACE exam tests this. Pub/Sub can redeliver the same message if the acknowledgment deadline expires before the subscriber calls `acknowledge()`. Design your Cloud Functions and subscriber code to handle duplicate messages safely (e.g., check if the record already exists before inserting).

*   **Cloud Functions trigger types**: Know the three most common triggers tested on the ACE exam: HTTP trigger (HTTPS endpoint), Cloud Storage trigger (object finalize/delete/archive/metadataUpdate), and Pub/Sub trigger (message published to a topic). The exam may ask which trigger to use for a given event source.

*   **Pub/Sub message ordering**: By default, Pub/Sub does not guarantee message ordering across partitions. Enable **message ordering** on a subscription and publish with an ordering key if your use case requires messages from the same entity to be processed in sequence.

*   **Study Resource**: The freeCodeCamp ACE course covers Pub/Sub architecture and Cloud Functions deployment with hands-on examples: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Pub/Sub and Cloud Functions chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Pub/Sub overview including topics, subscriptions, pull vs. push delivery, and dead letter topics: [Cloud Pub/Sub Overview](https://cloud.google.com/pubsub/docs/overview). The delivery model and subscription types are directly exam-relevant.
*   **Required Reading**: Review how Cloud Functions are triggered, configured, and deployed, including the difference between 1st and 2nd generation: [Cloud Functions Overview](https://cloud.google.com/functions/docs/concepts/overview).
*   **Required Video**: Watch the Pub/Sub and Cloud Functions segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Event-Driven Architecture chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a Pub/Sub topic and subscription, publish messages, and deploy a Cloud Function triggered by the topic. Key commands to practice:

*   `gcloud pubsub topics create my-topic` — creates a Pub/Sub topic
*   `gcloud pubsub subscriptions create my-sub --topic=my-topic` — creates a pull subscription
*   `gcloud pubsub topics publish my-topic --message="hello"` — publishes a test message
*   `gcloud functions deploy my-function --runtime=python311 --trigger-topic=my-topic --entry-point=handle_message` — deploys a Cloud Function with a Pub/Sub trigger

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Pub/Sub Overview](https://cloud.google.com/pubsub/docs/overview) documentation page.
- [ ] Read the [Cloud Functions Overview](https://cloud.google.com/functions/docs/concepts/overview) documentation page.
- [ ] Watch the Event-Driven Architecture segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a Pub/Sub topic and deploy a Cloud Function with a Pub/Sub trigger.
- [ ] Proceed to the weekly quiz.
