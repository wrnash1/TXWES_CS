# Quiz: Module 06 — Firestore and Datastore: Document Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A startup is building a social fitness app for iOS and Android. The app must display a live activity feed that updates in real time as friends complete workouts, support offline mode so users can log workouts without internet connectivity, and store flexible user profile data that varies per sport type. Which GCP database service is most appropriate?

- A) Cloud Firestore in Native mode
- B) Cloud SQL for PostgreSQL
- C) Cloud Bigtable
- D) Cloud Spanner

Correct Answer: A — Firestore Native mode provides real-time listeners for live feed updates, offline persistence for mobile clients, and a flexible document model that accommodates variable-structure profile data across different sport types. These three features together make Native mode the only appropriate choice.

Distractor analysis: B is incorrect because Cloud SQL does not provide real-time push updates to mobile clients or native offline persistence; it requires a server-side application layer and has a fixed schema. C is incorrect because Bigtable has no real-time listener capability, no mobile SDK, and no offline sync support; it is for high-throughput server-side analytical operations. D is incorrect because Cloud Spanner is a globally distributed relational database with no mobile SDK, no real-time listeners, and no offline mode.

---

### Question 2

An existing Cloud Datastore application needs to be migrated to Firestore to gain access to real-time listeners and improved offline support. What is the correct migration path?

- A) Create a new Firestore database in Native mode and rewrite the application to use the Firestore SDK.
- B) Upgrade the existing Datastore instance to Native mode via the Console settings page.
- C) Enable the Firestore API in the GCP project, which automatically upgrades Datastore to Native mode.
- D) Create a new Firestore database in Datastore mode, which provides real-time listeners automatically.

Correct Answer: A — Firestore mode selection is permanent at database creation and cannot be changed afterward. To use Native mode features, a new database must be created in Native mode and the application must be rewritten to use the Firestore SDK. There is no in-place upgrade path from Datastore mode to Native mode.

Distractor analysis: B is incorrect because the mode cannot be changed after creation; there is no upgrade button in the Console. C is incorrect because enabling the Firestore API does not change the mode of an existing Datastore database. D is incorrect because Datastore mode does not provide real-time listeners or the improved offline support; those features are exclusive to Native mode.

---

### Question 3

A developer runs a Firestore query: `WHERE category == "Electronics" AND price < 50 ORDER BY price ASC`. The query returns an error message about a missing index. What is the correct resolution?

- A) Create a composite index on the fields (category, price) in the Firestore Indexes Console.
- B) Create a single-field index on the category field; single-field indexes cover all query combinations.
- C) Restructure the data so that each category is a separate collection, eliminating the need for a multi-field query.
- D) Use a transaction instead of a query to filter documents by category and price.

Correct Answer: A — Firestore queries that filter or order on multiple fields simultaneously require a composite index. Firestore's error message for a missing composite index typically includes a direct link to create the required index in the Console. The composite index on (category, price) is required for this specific query pattern.

Distractor analysis: B is incorrect because single-field indexes only support queries filtering on one field; they do not cover multi-field combinations. C is incorrect because restructuring the entire data model to avoid a composite index is not a sound approach; composite indexes are a normal Firestore feature designed for this use case. D is incorrect because transactions are for atomic read-write operations; they do not change query execution semantics or index requirements.

---

### Question 4

A Firestore Security Rule is configured as follows: `allow read: if request.auth != null && request.auth.uid == userId;`. Which statement accurately describes what this rule does?

- A) It allows authenticated users to read only the document in the users collection whose ID matches their own authentication UID.
- B) It allows any user, whether authenticated or not, to read any document in the collection.
- C) It allows authenticated users to read all documents in the users collection regardless of document ID.
- D) It blocks all reads permanently because both conditions must be true simultaneously and cannot be.

Correct Answer: A — The rule has two conditions joined by `&&`. The first checks that the user is authenticated (`request.auth != null`). The second checks that the authenticated user's UID matches the `userId` wildcard in the document path (`match /users/{userId}`). Only the owner of the document can read it.

Distractor analysis: B is incorrect because `request.auth != null` specifically requires authentication; unauthenticated requests are denied. C is incorrect because the second condition `request.auth.uid == userId` restricts each authenticated user to only their own document, not all documents in the collection. D is incorrect because the two conditions are not logically contradictory; they are met simultaneously when an authenticated user accesses their own document.

---

### Question 5

Which of the following is a correct statement about Firestore sub-collections?

- A) A sub-collection is a collection nested within a document and is used to model one-to-many relationships hierarchically.
- B) Sub-collections are automatically created when a document contains more than 10 fields.
- C) Documents and their sub-collections must have the same schema and field structure.
- D) Sub-collections cannot be queried independently; they must always be accessed through the parent document.

Correct Answer: A — Sub-collections are nested within documents and represent the Firestore approach to one-to-many relationships. A user document can have an orders sub-collection, a posts sub-collection, and so on. Each sub-collection is independently queryable.

Distractor analysis: B is incorrect because sub-collections are explicitly defined by the application when writing documents; they are not automatically created based on field count. C is incorrect because Firestore is schema-less; documents in a sub-collection can have completely different fields from the parent document or from each other. D is incorrect because Firestore supports collection group queries that query all sub-collections with the same name across all parent documents simultaneously.

---

### Question 6

A fintech application stores account balance documents in Firestore. When a user initiates a transfer, the application must read the sender's balance, verify it is sufficient, subtract the transfer amount, and add it to the recipient's balance. Which Firestore mechanism is required?

- A) A Firestore transaction, which reads documents and then writes them atomically, retrying if concurrent modifications occur.
- B) A batch write with all four operations bundled together.
- C) Two separate UPDATE operations executed sequentially in the application.
- D) A Cloud SQL trigger that monitors the Firestore collection and applies the debit and credit.

Correct Answer: A — The transfer operation requires reading the sender's balance before deciding what to write (to check sufficiency). This read-then-conditional-write pattern requires a transaction. If another transaction modifies the sender's balance between the read and the write, Firestore automatically retries the transaction to prevent race conditions.

Distractor analysis: B is incorrect because a batch write performs writes-only without a prior read; it cannot read the current balance to check sufficiency before writing. C is incorrect because two sequential update statements are not atomic; if the application crashes between the debit and credit, money disappears from the sender without arriving at the recipient. D is incorrect because Cloud SQL cannot monitor Firestore collections; this describes a cross-service architecture that is not how Firestore operations work.

---

### Question 7

A Firestore query returns unexpected results for a query that filters on an array field using array-contains. The developer checks and confirms the index exists. What is the most likely cause of unexpected results?

- A) The query may have matched documents correctly; Firestore array-contains checks for exact element equality and the data may not match expectations.
- B) Array-contains queries are not supported by Firestore; arrays can only be read in full.
- C) Firestore requires a composite index for any array query; a single-field index is insufficient.
- D) Array-contains automatically converts values to lowercase before matching, causing case-sensitive mismatches.

Correct Answer: A — Firestore's array-contains operator performs exact element equality matching. If the query is `array-contains "wireless"` but the document contains `"Wireless"` (capitalized), they do not match. The most likely cause of unexpected results is a data mismatch rather than an index or API problem.

Distractor analysis: B is incorrect because array-contains is a fully supported Firestore query operator. C is incorrect because array-contains queries use a single-field index on the array field, which Firestore creates automatically; no composite index is required for a single array-contains filter. D is incorrect because Firestore does not normalize or transform stored values; it stores and queries exactly what is written.

---

### Question 8

You are comparing Cloud Firestore pricing to Cloud SQL pricing for a new mobile application. Which statement accurately describes the fundamental pricing model difference?

- A) Firestore charges per document read, write, and delete; Cloud SQL charges for provisioned instance hours regardless of query volume.
- B) Both Firestore and Cloud SQL charge per query executed, but Firestore has a higher per-query cost.
- C) Firestore charges for provisioned capacity in processing units; Cloud SQL charges per document operation.
- D) Both services are priced identically through the GCP pricing calculator.

Correct Answer: A — Firestore is serverless and charges based on actual usage: document reads, writes, and deletes. Cloud SQL is instance-based and charges for the provisioned machine type per hour, whether or not queries are running. This makes Firestore cost-effective for variable-traffic applications and Cloud SQL more predictable for steady-state workloads.

Distractor analysis: B is incorrect because Cloud SQL does not charge per query; it charges for the running instance. C is incorrect because processing units are a Cloud Spanner concept; Firestore uses document operation-based pricing. D is incorrect because the two services have fundamentally different pricing models.

---

### Question 9

What is the maximum number of documents that can be included in a single Firestore batch write or transaction?

- A) 500 documents
- B) 1,000 documents
- C) 10,000 documents
- D) There is no documented limit; it is bounded only by available memory

Correct Answer: A — Both Firestore transactions and batch writes are limited to 500 documents per operation. This limit applies to the total number of document reads and writes combined in a transaction, and the total number of write operations in a batch write.

Distractor analysis: B is incorrect because 1,000 is not the Firestore limit; the actual limit is 500. C is incorrect because 10,000 significantly overstates the limit. D is incorrect because there is a hard documented limit of 500 documents; exceeding it causes an error, not a performance degradation.

---

### Question 10

A legacy Cloud Datastore application is being evaluated for migration to Firestore Native mode. The application currently uses entity groups to ensure consistency within a set of related entities. What is the Native mode equivalent of Datastore entity groups?

- A) Firestore Native mode multi-document transactions provide consistent reads and writes across up to 500 related documents, replacing entity group consistency.
- B) Firestore Native mode uses collection groups to provide the same consistency guarantees as Datastore entity groups.
- C) Firestore Native mode does not support entity groups; you must migrate to Cloud Spanner to maintain consistent multi-entity operations.
- D) Firestore Native mode sub-collections provide exactly the same consistency semantics as Datastore entity groups.

Correct Answer: A — Firestore Native mode provides multi-document transactions that allow atomic reads and writes across multiple related documents, providing stronger consistency than Datastore entity groups in many cases. The 500-document limit per transaction replaces the entity group constraint with a more flexible and broadly scoped consistency mechanism.

Distractor analysis: B is incorrect because collection groups are a query feature that allows querying across multiple sub-collections with the same name; they are not a consistency mechanism equivalent to entity groups. C is incorrect because Firestore Native mode does support consistent multi-document operations through transactions; migration to Cloud Spanner is not required. D is incorrect because sub-collections are a hierarchical data modeling feature, not a consistency primitive; they do not provide the same semantics as entity groups.

---

Reference: cloud.google.com/learn
