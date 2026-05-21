# Quiz: Module 06 - Firestore and Datastore – Document Databases
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A startup is building a real-time collaborative document editing application. The backend must push data changes to thousands of simultaneously connected web clients within milliseconds and support offline editing on mobile devices. Which Google Cloud database service is most appropriate?
A) Cloud Bigtable
B) Cloud SQL for MySQL
C) Firestore in Native mode
D) Cloud Spanner
*   **Correct Answer:** C) Firestore in Native mode
*   **Distractor Analysis:**
    *   *Why C is correct:* Firestore in Native mode is purpose-built for exactly this use case. It provides real-time listeners that push document changes to connected clients instantly, and its client SDKs include built-in offline persistence for mobile and web apps.
    *   *Why A is incorrect:* Bigtable is optimized for high-throughput, low-latency reads and writes using a single row key; it has no real-time listener SDK or offline sync capability for client applications.
    *   *Why B is incorrect:* Cloud SQL is a relational database that requires clients to poll for changes; it has no native real-time push mechanism and no offline sync SDK.
    *   *Why D is incorrect:* Cloud Spanner is designed for globally distributed transactional workloads; it has no real-time listener SDK and is not designed for direct client-facing application backends.

---

---

**Question 2**
A Firestore application query returns an error: `"The query requires an index"`. The query filters documents on `status == 'active'` AND orders results by `created_at DESC`. What is the correct resolution?
A) Rewrite the query to filter on only one field; Firestore cannot filter and sort simultaneously.
B) Create a composite index on `(status ASC, created_at DESC)` in the Firestore index configuration.
C) Switch the database from Native mode to Datastore mode, which supports ad-hoc multi-field queries.
D) Add a `LIMIT 1000` clause to the query to reduce the result set size below the index threshold.
*   **Correct Answer:** B) Create a composite index on `(status ASC, created_at DESC)` in the Firestore index configuration.
*   **Distractor Analysis:**
    *   *Why B is correct:* Firestore requires a composite index for any query that filters or sorts on more than one field. The index must exactly match the fields and sort directions used in the query. You define it in `firestore.indexes.json` and deploy it with the Firebase CLI, or create it through the Firestore console.
    *   *Why A is incorrect:* Firestore supports compound queries that filter and sort on multiple fields — but only when the required composite index exists. The fix is to create the index, not to simplify the query.
    *   *Why C is incorrect:* Datastore mode does not eliminate the need for composite indexes; it still requires indexes for multi-field queries. Switching modes does not fix an index error.
    *   *Why D is incorrect:* The `LIMIT` clause restricts the number of results returned but does not change whether an index is required; the error will persist regardless of the limit value.

---

---

**Question 3**
A Firestore database administrator needs to **grant read-only access to a specific Firestore collection to a service account used by a reporting pipeline**. Which approach is most appropriate on Google Cloud?
A) Use IAM to grant the `roles/datastore.viewer` role to the service account at the project level.
B) Create a Firestore composite index that restricts which documents the service account can read.
C) Run `GRANT SELECT ON collection TO service_account` in the Firestore query console.
D) Add the service account email to the Firestore Security Rules `allow read` condition.
*   **Correct Answer:** A) Use IAM to grant the `roles/datastore.viewer` role to the service account at the project level.
*   **Distractor Analysis:**
    *   *Why A is correct:* Access to Firestore from server-side applications (like reporting pipelines using the Admin SDK) is controlled by GCP IAM roles. The `roles/datastore.viewer` role grants read-only access to all Firestore data for the assigned identity. For more granular collection-level control, VPC Service Controls or server-side filtering should be used alongside IAM.
    *   *Why B is incorrect:* Composite indexes are query optimization structures that define which multi-field queries Firestore can execute; they have no access control function.
    *   *Why C is incorrect:* Firestore does not support SQL syntax; there is no `GRANT SELECT` command. Firestore uses IAM and Security Rules for access control.
    *   *Why D is incorrect:* Firestore Security Rules control access from client SDKs (web and mobile); they do not apply to server-side Admin SDK access, which is governed exclusively by IAM.

---

**Question 4**
A Firestore-backed application is experiencing **slow query performance** when retrieving all orders for a specific customer, filtering by `customer_id == 'C001'` and ordering by `order_date DESC`. The query was working fine when the collection had 1,000 documents but is now slow with 5 million documents. What is the most likely cause and the correct fix?
A) Firestore is performing a full collection scan because no composite index exists for `(customer_id, order_date DESC)`. Create the required composite index.
B) Firestore document reads are throttled at 5 million documents per collection. Archive older orders to a separate collection.
C) The Firestore instance needs more nodes. Scale up the compute capacity in the Firestore console.
D) Switch the database to Datastore mode, which uses a B-tree index engine that scales better for large collections.
*   **Correct Answer:** A) Firestore is performing a full collection scan because no composite index exists for `(customer_id, order_date DESC)`. Create the required composite index.
*   **Distractor Analysis:**
    *   *Why A is correct:* Without a composite index on `(customer_id, order_date DESC)`, Firestore must scan the entire collection to evaluate the filter and sort, which degrades linearly with collection size. Creating the composite index reduces the query to an index range scan — constant time regardless of collection size.
    *   *Why B is incorrect:* Firestore has no inherent per-collection document count throttle; it is designed to scale to billions of documents. The performance problem is an index issue, not a capacity limit.
    *   *Why C is incorrect:* Firestore is fully serverless; there are no user-managed nodes or compute resources to scale. Performance is determined by schema and index design.
    *   *Why D is incorrect:* Datastore mode and Native mode use the same underlying index engine. Switching modes does not change indexing behavior and would lose real-time listener functionality.

---

**Question 5**
When securing a Firestore database backing a mobile application, you must mitigate the risk of **unauthenticated users reading all documents in a collection by directly calling the Firestore API**. Which control best addresses this vulnerability?
A) Write Firestore Security Rules that require `request.auth != null` before allowing any read operation.
B) Enable CMEK to encrypt Firestore documents at rest so unauthenticated reads return encrypted data.
C) Configure a VPC Service Controls perimeter around Firestore to block all external API calls.
D) Enable Cloud Audit Data Access Logs to detect and alert on unauthenticated read attempts.
*   **Correct Answer:** A) Write Firestore Security Rules that require `request.auth != null` before allowing any read operation.
*   **Distractor Analysis:**
    *   *Why A is correct:* Firestore Security Rules are evaluated server-side for every client SDK request. A rule requiring `request.auth != null` ensures that only authenticated users (those who have signed in with Firebase Authentication or a GCP identity) can read documents. Unauthenticated requests are rejected at the Firestore service layer.
    *   *Why B is incorrect:* CMEK encrypts data at rest on GCP's physical storage infrastructure; it does not affect API-level access control. Unauthenticated clients calling the Firestore API would still receive decrypted document data in the response if no access rules are in place.
    *   *Why C is incorrect:* VPC Service Controls restricts access from network perimeters and is designed for server-to-server Admin SDK access; it is not the correct tool for controlling unauthenticated end-user access from mobile/web clients.
    *   *Why D is incorrect:* Audit logs detect unauthorized access after it has occurred; they do not prevent unauthenticated users from reading documents. Detection is not a substitute for access control rules.
