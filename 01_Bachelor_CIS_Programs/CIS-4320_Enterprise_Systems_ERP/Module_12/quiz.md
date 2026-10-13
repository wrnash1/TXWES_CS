# Quiz: Module 12 — ERP Integration and Middleware

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question to explain why incorrect answers are wrong — this section is for instructor and student review, not visible during the live quiz.

---

## Question 1

A sales order is created in Salesforce and must trigger an SAP sales order within 15 minutes. The integration team has MuleSoft available. Which Salesforce feature should publish the trigger event to MuleSoft?

A. Bulk API job

B. Platform Event

C. SOAP API callout from a scheduled Apex job

D. Data Loader CSV export

**Correct Answer: B**

**Distractor Analysis:**

- **A — Bulk API job:** Bulk API is designed for large-volume data operations, not for real-time event notification. It is asynchronous and batch-oriented, making it unsuitable for a 15-minute SLA trigger.
- **B — Platform Event (Correct):** Platform Events enable near-real-time publish-subscribe messaging. Salesforce publishes the event when the order is created; MuleSoft subscribes to the event channel and reacts immediately. This is the architecturally correct solution.
- **C — Scheduled Apex job:** A scheduled job runs on a schedule (e.g., every 15 minutes at best), introducing latency up to the schedule interval. It is not event-driven, meaning it does not react immediately to the triggering action.
- **D — Data Loader CSV export:** Data Loader is a manual or scripted administrative tool, not an integration mechanism. It cannot respond to record creation events.

---

## Question 2

An SAP integration developer needs to call a function module in a remote SAP system and guarantee that the function executes exactly once, even if the network fails mid-transmission. Which RFC type is required?

A. Synchronous RFC (sRFC)

B. Asynchronous RFC (aRFC)

C. Transactional RFC (tRFC)

D. Background RFC type aRFC with retry logic in the calling program

**Correct Answer: C**

**Distractor Analysis:**

- **A — sRFC:** Synchronous RFC waits for a response but does not provide duplicate-execution protection. If the network fails after the remote system starts executing but before the response is sent, the caller has no way to know whether execution succeeded, and a retry may cause a duplicate.
- **B — aRFC:** Asynchronous RFC fires and forgets — no response, no exactly-once guarantee. Suitable for parallel processing where duplicates are acceptable.
- **C — tRFC (Correct):** Transactional RFC assigns a unique Transaction ID (TID) to each call. The system tracks TIDs to ensure a function module is executed exactly once, even if the call is retried after a network failure. This is the standard mechanism for financial postings and other operations where duplicates are unacceptable.
- **D:** aRFC with custom retry logic still does not provide exactly-once semantics — the calling program cannot know whether the remote execution succeeded before the network failure. tRFC handles this at the protocol level.

---

## Question 3

A Salesforce Administrator needs to synchronize 80,000 Account records from an external ERP system into Salesforce overnight. Which API should the integration use?

A. REST API with individual PATCH requests per record

B. SOAP API with a loop calling update() for each record

C. Bulk API 2.0 with an Upsert job

D. Streaming API with Platform Events

**Correct Answer: C**

**Distractor Analysis:**

- **A — REST API with individual PATCH requests:** Making 80,000 individual REST calls would rapidly exhaust the daily API call limit and would run far too slowly for an overnight process. REST is optimized for individual record operations, not mass data operations.
- **B — SOAP API with a loop:** Similar problem as option A. The SOAP API's update() call can accept batches of up to 200 records, but 80,000 records would still require 400 separate calls and is not efficient for this volume.
- **C — Bulk API 2.0 with Upsert (Correct):** Bulk API 2.0 is specifically designed for high-volume operations. Upsert will create records that do not exist and update records that do, based on an external ID. This is the exact use case Bulk API was built for.
- **D — Streaming API with Platform Events:** Streaming API is for receiving real-time event notifications from Salesforce, not for loading data into Salesforce in bulk. This is the wrong tool for the scenario.

---

## Question 4

In SAP, an IDoc's Control Record primarily serves what purpose?

A. Storing the business data content of the document

B. Recording the processing history and error messages

C. Identifying the sender, receiver, message type, and transmission status

D. Defining the segment hierarchy and field lengths for the IDoc type

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Business data content is stored in Data Records, not the Control Record. The Control Record is the envelope.
- **B:** Processing history and error messages are captured in Status Records, not the Control Record.
- **C — Control Record (Correct):** The Control Record is the IDoc envelope. It identifies who sent the IDoc, who should receive it, what message type it is, when it was created, and its current processing status.
- **D:** Segment hierarchy and field definitions are part of the IDoc type definition in the data dictionary, not stored in the runtime Control Record of a specific IDoc instance.

---

## Question 5

A Salesforce Administrator is setting up an integration between Salesforce and a third-party HR system. The HR system's API URL and credentials must be stored securely so they do not appear in Apex code. What Salesforce feature is designed for this purpose?

A. Static Resources

B. Custom Metadata Types

C. Named Credentials

D. Remote Site Settings

**Correct Answer: C**

**Distractor Analysis:**

- **A — Static Resources:** Used to store static files (images, CSS, JavaScript) for Visualforce and Lightning pages. Not designed for storing API credentials.
- **B — Custom Metadata Types:** Used to store configuration data that can be deployed between orgs. While you could store a URL here, Custom Metadata does not handle authentication and does not protect credentials from appearing in code in the same way.
- **C — Named Credentials (Correct):** Named Credentials store endpoint URLs and authentication details (including OAuth tokens and passwords) securely in Salesforce. Apex code references the Named Credential by name rather than hardcoding URLs and secrets. Salesforce handles the authentication handshake automatically.
- **D — Remote Site Settings:** Remote Site Settings simply whitelist external URLs that Salesforce is allowed to call. They do not store credentials or handle authentication. You need both a Remote Site Setting (or Named Credential, which supersedes it) AND credentials management.

---

## Question 6

Which of the following best describes the "Extract" phase of an ETL process?

A. Applying business rules to convert source data into the format required by the target system

B. Writing transformed data records to the target system database

C. Pulling raw data from one or more source systems

D. Validating that loaded data matches expected record counts and checksums

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Applying business rules and converting formats describes the Transform phase, not Extract.
- **B:** Writing data to the target system is the Load phase.
- **C — Extract (Correct):** The Extract phase involves pulling raw data from source systems — whether by SQL query, API call, file read, or change data capture stream. No transformation is applied; data is pulled as-is from the source.
- **D:** Post-load validation (reconciliation) is a quality check that follows the ETL process. It is not one of the three ETL phases itself.

---

## Question 7

A development team is designing a Salesforce integration where an external application needs to call Salesforce APIs without any human logging in to authorize the connection. Which OAuth flow is most appropriate?

A. Web Server Flow (Authorization Code)

B. User-Agent Flow (Implicit)

C. JWT Bearer Flow

D. Resource Owner Password Credentials Flow

**Correct Answer: C**

**Distractor Analysis:**

- **A — Web Server Flow:** Requires a user to open a browser, log in to Salesforce, and click Allow. Not suitable for a server-to-server process with no human interaction.
- **B — User-Agent Flow:** Designed for client-side JavaScript applications where the user is present. Access tokens are returned to the browser URL, which is a security concern for server processes.
- **C — JWT Bearer Flow (Correct):** The JWT Bearer Flow uses a signed JSON Web Token (JWT) constructed with a private key. Salesforce validates the JWT signature using a previously uploaded certificate, grants an access token, and the external application can call the API — all without any human interaction. This is the standard pattern for automated server-to-server Salesforce integrations.
- **D — Resource Owner Password Credentials:** Requires passing a username and password directly in the API call. Salesforce is deprecating this flow for security reasons; it is not recommended for new integrations and is disabled for most orgs.

---

## Question 8

MuleSoft Anypoint Platform organizes APIs into three layers under the API-Led Connectivity model. Which layer is responsible for providing an API that a mobile app uses to display account information, combining data from both Salesforce and SAP?

A. System API

B. Process API

C. Experience API

D. Connector API

**Correct Answer: C**

**Distractor Analysis:**

- **A — System API:** System APIs abstract individual backend systems. A Salesforce System API would wrap Salesforce, and a separate SAP System API would wrap SAP. They do not combine data from multiple systems.
- **B — Process API:** Process APIs implement business logic and can call multiple System APIs. They orchestrate data flow between systems. However, they are not the final consumer-facing API; they serve the Experience layer.
- **C — Experience API (Correct):** Experience APIs are tailored to specific consumers — mobile, web, partner portal. They combine data from multiple Process or System APIs and present it in the format the consumer needs. In this scenario, the mobile app consumes the Experience API, which internally calls both Salesforce and SAP Process/System APIs.
- **D — Connector API:** Not a layer in the API-Led Connectivity model. Connectors are components within MuleSoft that wrap individual protocols and systems; they are not a separate layer in the architectural model.

---

## Question 9

A nightly SAP-to-Salesforce account sync is failing intermittently. The middleware team finds messages accumulating in an unexpected queue that were not processed. What is this queue called, and what does it indicate?

A. Priority Queue — indicates high-volume messages are being delayed

B. Dead Letter Queue — indicates messages that have exhausted retry attempts

C. FIFO Queue — indicates messages are being processed out of sequence

D. Poison Queue — indicates the queue configuration is incorrect

**Correct Answer: B**

**Distractor Analysis:**

- **A — Priority Queue:** A priority queue routes high-priority messages before lower-priority ones. It is a design pattern, not an error condition. Messages do not "accumulate" in a priority queue due to failures.
- **B — Dead Letter Queue (Correct):** The Dead Letter Queue (DLQ) holds messages that have failed processing after the maximum number of configured retry attempts. Messages in the DLQ require manual investigation — they represent data that has not been loaded into the target system. Monitoring the DLQ is a key operational practice for any message-based integration.
- **C — FIFO Queue:** FIFO (First In, First Out) guarantees message ordering. It is a queue type, not an error state. Messages do not accumulate in a FIFO queue due to failures.
- **D — Poison Queue:** "Poison queue" and "dead letter queue" are sometimes used interchangeably in different platforms. In the context of most middleware documentation (and the certification exam), "Dead Letter Queue" is the standard term. "Poison" message is sometimes used to describe a message that causes repeated processing failures, but the standard term for the accumulation queue is DLQ.

---

## Question 10

Salesforce Change Data Capture (CDC) differs from Platform Events primarily because:

A. Platform Events require Apex code to consume; CDC does not

B. CDC events are automatically generated by Salesforce when records change; Platform Events must be explicitly published

C. CDC supports only external objects; Platform Events support standard and custom objects

D. Platform Events are stored for 72 hours; CDC events are discarded after 24 hours

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Both Platform Events and CDC can be consumed by Apex, Flows, external systems via CometD, and other subscribers. The consumption mechanism is not the differentiating factor.
- **B — Automatic generation (Correct):** This is the key distinction. Change Data Capture automatically publishes events when records are created, updated, deleted, or undeleted for the object types you configure in Setup. You do not add any code or configuration to your business logic to emit these events. Platform Events, by contrast, must be explicitly published — someone must call `EventBus.publish()` in Apex or invoke a Publish action in a Flow.
- **C:** CDC supports standard and custom Salesforce objects, not just external objects. External Objects relate to Salesforce Connect, which is a different feature.
- **D:** Salesforce retains CDC event messages for up to 3 days (72 hours), and Platform Event messages are retained for the event's configured retention period (also up to 3 days). Retention behavior is similar; it is not the primary differentiator.

---

## Quiz Summary

| Question | Topic | Correct Answer |
|----------|-------|----------------|
| 1 | Platform Events for real-time trigger | B |
| 2 | tRFC for exactly-once execution | C |
| 3 | Bulk API 2.0 for high-volume sync | C |
| 4 | IDoc Control Record purpose | C |
| 5 | Named Credentials for secure endpoint storage | C |
| 6 | ETL Extract phase definition | C |
| 7 | JWT Bearer Flow for server-to-server OAuth | C |
| 8 | Experience API in API-Led Connectivity | C |
| 9 | Dead Letter Queue identification | B |
| 10 | CDC vs. Platform Events distinction | B |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
