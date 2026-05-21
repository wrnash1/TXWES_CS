# Quiz: Module 10 – Pub/Sub and Cloud Functions: Event-Driven Architecture
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your data pipeline receives order events from multiple upstream applications. Each event must be processed by both an inventory service and an analytics service independently. The two services should not be aware of each other and should be able to process at their own rates. Which Pub/Sub configuration implements this pattern?

A) Create one topic and one subscription shared between both services, so each message is delivered to whichever service polls first.
B) Create one topic with two separate subscriptions — one for the inventory service and one for the analytics service.
C) Create two topics — one for inventory and one for analytics — and publish each event to both topics using a custom fan-out function.
D) Create one subscription with a filter that routes messages with `type=inventory` to one service and `type=analytics` to the other.

*   **Correct Answer:** B) Create one topic with two separate subscriptions — one for the inventory service and one for the analytics service.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single subscription delivers each message to only one subscriber — whichever service acknowledges it first. The other service never receives the same message. Two separate subscriptions are required so each service gets its own independent copy of every message.
    *   *Why C is incorrect:* Publishing to two separate topics with a custom fan-out function adds unnecessary complexity and a single point of failure in the fan-out function. Pub/Sub's built-in multi-subscription model is purpose-built for this fan-out pattern.
    *   *Why D is incorrect:* Pub/Sub subscription filters route messages to a single subscriber based on message attributes — they do not duplicate a message to multiple services. A filter-based single subscription still delivers each matching message only once.

---

**Question 2**
A Cloud Function processes payment records published to a Pub/Sub topic. Occasionally the function fails midway through processing a record due to a transient database error, causing Pub/Sub to redeliver the message. You notice that some payments are being processed twice, resulting in duplicate charges. What is the root cause of this problem, and what is the correct fix?

A) The Cloud Function's maximum retry count is set too high; reduce it to 1 to prevent redelivery.
B) Pub/Sub delivers messages at least once and does not guarantee exactly-once delivery; the function must be made idempotent by checking whether the payment record already exists before processing it.
C) The function is using a pull subscription instead of a push subscription; switching to push delivery prevents duplicate messages.
D) The Pub/Sub acknowledgment deadline is too short; extend it to 600 seconds so the function always has time to acknowledge before redelivery occurs.

*   **Correct Answer:** B) Pub/Sub delivers messages at least once and does not guarantee exactly-once delivery; the function must be made idempotent by checking whether the payment record already exists before processing it.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Reducing the retry count limits how many times a failed message is retried, but it does not prevent the fundamental at-least-once delivery behavior of Pub/Sub. Reducing retries to 1 would cause messages to be dropped on the first failure rather than fixing the duplicate processing problem.
    *   *Why C is incorrect:* Push and pull delivery both provide at-least-once semantics — switching between them does not change the redelivery behavior. The delivery mode affects how messages are received, not whether duplicates can occur.
    *   *Why D is incorrect:* Extending the acknowledgment deadline reduces the likelihood of redelivery during normal processing, but it does not eliminate it — network timeouts, function crashes, and cold starts can still cause a message to be redelivered after the deadline. Idempotency is the only reliable solution.

---

**Question 3**
You want to automatically resize images uploaded to a Cloud Storage bucket. Every time a new image file is uploaded, a processing function should run, create a thumbnail, and save it to a separate output bucket. No HTTP endpoint is needed. Which Cloud Functions trigger type is correct for this use case?

A) HTTP trigger — configure an HTTPS endpoint and call it from the upload application after each upload completes.
B) Cloud Storage trigger with the `google.storage.object.finalize` event type on the input bucket.
C) Pub/Sub trigger — publish a message to a topic after each upload and have the function subscribe to that topic.
D) Firestore trigger — write a document to Firestore on each upload and trigger the function on document creation.

*   **Correct Answer:** B) Cloud Storage trigger with the `google.storage.object.finalize` event type on the input bucket.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An HTTP trigger requires the upload application to make an explicit HTTPS call to the function after each upload. This creates a tight coupling between the upload service and the processing function, and means the processing will fail silently if the call is missed. A Cloud Storage trigger fires automatically without any application-side changes.
    *   *Why C is incorrect:* While a Pub/Sub trigger is a valid indirect approach (GCS can publish notifications to a Pub/Sub topic), it adds an intermediate resource that must be configured and maintained. The direct Cloud Storage trigger is simpler and is specifically designed for this pattern.
    *   *Why D is incorrect:* Writing a Firestore document as an intermediary just to trigger the function on document creation is an unnecessary indirect pattern that adds complexity and latency. The Cloud Storage trigger fires directly on the upload event.

---

**Question 4**
Your Cloud Function processes messages from a Pub/Sub subscription. Some messages consistently fail processing due to malformed data that will never succeed regardless of how many times they are retried. These messages are blocking your queue and consuming processing resources. What configuration prevents these messages from retrying indefinitely while preserving them for investigation?

A) Set the subscription's acknowledgment deadline to 10 seconds so failed messages expire quickly and are dropped from the queue.
B) Delete and recreate the subscription each time a bad message is detected to flush the queue.
C) Configure a dead letter topic on the subscription with a maximum delivery attempt count, so messages that exceed the retry limit are forwarded to the dead letter topic for investigation.
D) Enable message ordering on the subscription so that malformed messages are processed sequentially and do not block other messages.

*   **Correct Answer:** C) Configure a dead letter topic on the subscription with a maximum delivery attempt count, so messages that exceed the retry limit are forwarded to the dead letter topic for investigation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A short acknowledgment deadline causes messages to be redelivered faster, not dropped. Pub/Sub does not automatically discard unacknowledged messages based on the deadline alone — they continue to be redelivered until they are acknowledged or the message retention period expires (up to 7 days).
    *   *Why B is incorrect:* Deleting and recreating the subscription discards all messages in the queue — including valid messages that have not yet been processed — and is a destructive operation that cannot be targeted at specific bad messages.
    *   *Why D is incorrect:* Message ordering ensures messages with the same ordering key are delivered sequentially within a partition. It does not skip or remove malformed messages — ordered delivery of a bad message still blocks all subsequent messages with the same ordering key.

---

**Question 5**
You are designing a system where a Cloud Function must write processed results to a Cloud SQL database. The function is deployed without a VPC connector and the Cloud SQL instance is configured with only a private IP address (no public IP). The function cannot connect to the database. What is the correct fix?

A) Assign a public IP address to the Cloud SQL instance and add the function's outbound IP range to the Cloud SQL authorized networks list.
B) Configure a Serverless VPC Access connector for the Cloud Function and connect the function to the VPC that contains the Cloud SQL private IP, then use the Cloud SQL Auth Proxy sidecar.
C) Deploy the Cloud Function in the same region as the Cloud SQL instance — same-region functions automatically have access to private IP resources.
D) Grant the Cloud Function's service account the `roles/cloudsql.client` role, which enables direct access to private IP Cloud SQL instances without VPC configuration.

*   **Correct Answer:** B) Configure a Serverless VPC Access connector for the Cloud Function and connect the function to the VPC that contains the Cloud SQL private IP, then use the Cloud SQL Auth Proxy sidecar.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Enabling a public IP on the Cloud SQL instance and adding the function's egress IP to authorized networks exposes the database to the public internet and requires managing IP allowlists. Using a private IP with a VPC connector is the recommended secure approach.
    *   *Why C is incorrect:* Cloud Functions run in Google's managed serverless infrastructure, not inside your VPC. Being in the same region as a Cloud SQL instance with a private IP does not automatically grant network access — a Serverless VPC Access connector is required to route traffic from the function into the VPC.
    *   *Why D is incorrect:* `roles/cloudsql.client` is an IAM role that grants permission to connect to Cloud SQL via the Cloud SQL Auth Proxy — it is an authorization credential, not a network path. Without a VPC connector providing network connectivity to the private IP, the IAM role alone cannot establish a TCP connection.
