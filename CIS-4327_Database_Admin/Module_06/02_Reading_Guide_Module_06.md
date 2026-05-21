# Reading Guide: Module 06 - Firestore and Datastore – Document Databases
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 06 - Firestore and Datastore – Document Databases**! This week you will study Google Cloud Firestore, GCP's fully managed, serverless document database. Firestore stores data as collections of JSON-like documents and is optimized for mobile and web application backends that require real-time data synchronization and offline support. Understanding the Firestore data model and its distinction from relational databases and Bigtable is essential for the GCP Professional Cloud Database Engineer exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Firestore**: A fully managed, serverless, document-oriented NoSQL database service on GCP. Firestore organizes data into collections of documents (analogous to JSON objects), supports real-time listeners for live data updates, and provides offline synchronization for mobile and web clients through its native SDKs. It guarantees strong consistency for all reads.
*   **Document**: The fundamental storage unit in Firestore. A document is a set of key-value pairs stored as a JSON-like object with a unique ID within a collection. Documents can contain nested sub-collections, enabling hierarchical data modeling. A single document is limited to 1 MB in size.
*   **Collection**: A container for documents in Firestore. Collections are analogous to database tables but are schemaless — different documents within the same collection can have different fields. Collections can contain sub-collections nested within documents.
*   **Firestore vs. Datastore (Legacy)**: Cloud Datastore is the legacy version of Firestore (now called Firestore in Datastore mode). Firestore in Native mode is the current, recommended version that adds real-time listeners and offline sync. The exam tests whether you know that Datastore mode is for server-side workloads and Native mode is for mobile/web apps with real-time requirements.
*   **Composite Index**: Firestore requires a composite index for any query that filters or orders on more than one field simultaneously. Unlike Cloud SQL, which can perform ad-hoc multi-column queries without pre-declared indexes, Firestore rejects queries against non-indexed field combinations at query time. Managing composite indexes is an important DBA task.

---

### 2. Certification Exam Tips
*   **Firestore vs. Bigtable vs. Cloud SQL**: The exam presents a workload and asks you to pick the correct service. Use Firestore for: mobile/web backends, real-time sync, offline support, and hierarchical document data. Use Bigtable for: high-throughput time-series and IoT with single-key access. Use Cloud SQL for: ACID transactional relational data with SQL queries.
*   **Firestore Modes**: Know the two modes. Native mode supports real-time listeners and is for client-facing applications. Datastore mode is for server-to-server backend workloads that do not need real-time sync. You cannot change modes after a database is created.
*   **Composite Index Requirement**: Expect a scenario question where a Firestore query fails at runtime. The cause is almost always a missing composite index. The fix is to deploy the index definition using the Firebase CLI or the Firestore console.
*   **Document Size and Subcollection Limits**: Know that a single document is limited to 1 MB and 20,000 fields, and that subcollections do not count against the parent document's size limit. Storing large arrays inside a document that grows over time will eventually hit the 1 MB limit.
*   **Study Resource:** The official Google Cloud Firestore documentation is the primary study source: [Cloud Firestore Documentation – Google Cloud](https://cloud.google.com/firestore/docs). The freeCodeCamp database course reinforces NoSQL concepts: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to understand the relational model that Firestore's document model is designed to contrast with: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free comprehensive lecture provides the database fundamentals context needed before studying Firestore's document model: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will create a Firestore database in Native mode, write and read documents using the Firebase Admin SDK, create a composite index for a multi-field query, and observe the real-time listener behavior using the Firestore emulator.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the relevant NoSQL and data modeling chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the NoSQL and database design segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the Firestore index and data model steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
