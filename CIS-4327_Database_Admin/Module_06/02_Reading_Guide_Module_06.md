# Reading Guide: Module 06 — Firestore and Datastore: Document Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Introduction

Cloud Firestore is Google Cloud's serverless document database, designed for mobile and web application backends where flexible schema, real-time updates, and offline data access are required. The GCP Database Engineer exam tests Firestore in service selection scenarios, security configuration, and the Datastore vs. Firestore Native mode distinction. This reading guide provides the reference depth you need for both the lab and the exam.

---

### 1. High-Yield Glossary

**Cloud Firestore**: Google Cloud's fully managed, serverless document database. Designed for mobile and web app backends. Scales automatically with no instance provisioning.

**Serverless**: No instances, nodes, or clusters to configure. Firestore scales automatically based on traffic. Billing is based on document reads, writes, and deletes rather than provisioned capacity.

**Document**: The primary data unit in Firestore. A JSON-like object with a unique ID within a collection. Can contain scalar values, arrays, maps, and references to other documents.

**Collection**: A container for documents in Firestore. Schema-less — different documents in the same collection can have different fields. Analogous to a table in a relational database, but without a fixed schema.

**Sub-Collection**: A collection nested within a document. Used to model one-to-many hierarchical relationships (e.g., a user document with a reviews sub-collection).

**Document ID**: The unique identifier for a document within its parent collection. Can be auto-generated or set by the application.

**Document Path**: The full hierarchical path to a document. Format: `collection/documentId/sub-collection/documentId`.

**Field**: A key-value pair within a document. Fields can hold strings, numbers, booleans, timestamps, geopoints, arrays, maps, or null.

**Map**: A nested object within a Firestore document. Allows structured nested data without creating a sub-collection.

**Array**: An ordered list of values within a Firestore field. Supports array-contains queries.

**Firestore Native Mode**: The current default mode. Supports real-time listeners, offline persistence, improved queries, and Firestore SDK. Recommended for all new applications.

**Datastore Mode**: A backward-compatible mode for legacy Cloud Datastore applications. Uses the Datastore API. Does not support real-time listeners or offline persistence.

**Real-Time Listener**: A Firestore Native mode feature that pushes document changes to subscribed clients automatically, without polling. Ideal for live dashboards, collaborative apps, and chat systems.

**Offline Persistence**: A Firestore Native mode feature that caches data locally on mobile clients. The app remains functional when network connectivity is lost and synchronizes when connectivity is restored.

**Security Rules**: Server-side declarative access control policies for Firestore. Control which authenticated clients can read or write which documents. Evaluated before data is returned to any client.

**`request.auth`**: The Security Rules variable containing the authenticated user's identity. `request.auth.uid` is the user's unique ID from Firebase Authentication.

**`resource.data`**: The Security Rules variable providing access to the current document's field values. Used for field-level validation rules.

**Single-Field Index**: An index automatically created by Firestore for every field in every document. Supports simple equality and range queries on individual fields.

**Composite Index**: An index on two or more fields required for queries that filter or order on multiple fields simultaneously. Must be created explicitly.

**Transaction**: An atomic multi-document operation that reads and then writes. Firestore automatically retries if conflicting changes occur during execution.

**Batch Write**: An atomic set of write operations (create, update, delete) on multiple documents without a prior read. Does not retry on conflict. Succeeds entirely or fails entirely.

**Cloud Datastore**: The predecessor to Cloud Firestore. Still available as Datastore mode within Firestore. Legacy service; new projects should use Firestore.

**Entity (Datastore)**: The Datastore term for a document. Stored in a Kind (equivalent to a collection).

**Kind (Datastore)**: The Datastore term for a collection. A named group of entities.

---

### 2. Firestore Data Types Reference

| Firestore Type | Description | Example |
|---|---|---|
| String | UTF-8 encoded text | `"Fort Worth"` |
| Number | 64-bit floating point | `49.99` |
| Boolean | true or false | `true` |
| Timestamp | Date and time with microsecond precision | `2024-01-15T09:00:00Z` |
| Geopoint | Latitude/longitude coordinate | `(32.725, -97.321)` |
| Null | Absent value | `null` |
| Array | Ordered list of values | `["premium", "verified"]` |
| Map | Nested key-value object | `{"street": "123 Main", "city": "Fort Worth"}` |
| Reference | Pointer to another Firestore document | `/users/user-001` |
| Bytes | Binary data (max 1 MB) | Raw binary payload |

---

### 3. Firestore Modes Comparison

| Feature | Native Mode | Datastore Mode |
|---|---|---|
| Real-time listeners | Yes | No |
| Offline persistence | Yes | No |
| Multi-document transactions | Yes (up to 500 docs) | Single entity group only |
| Composite query support | Yes | Limited |
| API | Firestore SDK | Datastore API |
| Recommended for | All new applications | Legacy Datastore migrations |
| Can be changed after creation | No — permanent | No — permanent |

Mode selection is permanent at database creation. You cannot switch from Datastore mode to Native mode after the database is created.

---

### 4. Firestore vs. Cloud SQL vs. Cloud Bigtable

| Dimension | Firestore | Cloud SQL | Cloud Bigtable |
|---|---|---|---|
| Data model | Document | Relational tables | Wide-column key-value |
| Schema | Flexible | Fixed | Column families fixed, qualifiers dynamic |
| SQL JOINs | None | Full SQL | None |
| ACID transactions | Multi-document (limited) | Full ACID | None |
| Real-time updates to clients | Yes (Native) | No | No |
| Offline mobile sync | Yes (Native) | No | No |
| Full-text search | No | Limited (PostgreSQL tsvector) | No |
| Scaling | Serverless, automatic | Vertical (larger machine) | Horizontal (add nodes) |
| Primary use case | Mobile/web app backends | Enterprise OLTP | Time-series, IoT |

---

### 5. Security Rules Reference

| Rule Component | Description |
|---|---|
| `match /databases/{database}/documents` | Root match for all document paths |
| `match /collection/{docId}` | Matches a specific collection path |
| `allow read` | Grants read access (get and list) |
| `allow write` | Grants write access (create, update, delete) |
| `allow create` | Grants create-only access |
| `allow update` | Grants update-only access |
| `allow delete` | Grants delete-only access |
| `request.auth != null` | Condition: user is authenticated |
| `request.auth.uid == userId` | Condition: user is accessing their own document |
| `resource.data.field == value` | Condition: current document field has specific value |
| `request.resource.data.field` | Condition: incoming write data has specific field |

---

### 6. Index Requirements Reference

| Query Type | Index Required |
|---|---|
| Single field equality | Automatic single-field index (no action needed) |
| Single field range (< > <= >=) | Automatic single-field index (no action needed) |
| Multiple field filter (AND) | Composite index required |
| Filter + order on different fields | Composite index required |
| Array-contains query | Automatic single-field index |
| Array-contains-any query | Automatic single-field index |
| Collection group query | Collection group index required |

---

### 7. Transaction vs. Batch Write Decision Guide

| Scenario | Use Transaction | Use Batch Write |
|---|---|---|
| Read document A, then update document B based on A's value | Yes | No |
| Update 10 documents simultaneously without reading first | No | Yes |
| Decrement a counter only if current value > 0 | Yes | No |
| Create 5 new documents atomically | No | Yes |
| Transfer a value from one document to another | Yes | No |

---

### 8. Required Readings and Resources

**GCP Documentation — Cloud Firestore Overview**: Data model, Native vs. Datastore mode, and getting started guide. Available at cloud.google.com/learn.

**GCP Documentation — Firestore Security Rules**: Full reference for security rules syntax, authentication checks, and field validation. Available at cloud.google.com/learn.

**GCP Documentation — Firestore Indexes**: Single-field and composite index explanation, how to create composite indexes, and index exemptions. Available at cloud.google.com/learn.

---

### 9. Exam Tips

Tip 1: Firestore is the answer for mobile/web app backends, especially when real-time listeners or offline sync are mentioned. Cloud SQL is the answer when stable schema and ACID transactions are the priority.

Tip 2: Native mode vs. Datastore mode. Native mode is for new applications. Datastore mode is for legacy migrations. The mode is permanent — it cannot be changed after database creation.

Tip 3: Firestore queries always use an index. Multi-field queries require a composite index. If the exam scenario describes a Firestore query failing with an error about a missing index, the answer is creating a composite index.

Tip 4: Security Rules are required for any application where clients connect directly to Firestore (mobile/web). Without rules, Firestore defaults to deny-all in production.

Tip 5: Firestore does not support full-text search or SQL JOINs. Any scenario requiring these capabilities needs a different service (BigQuery for analytics, Cloud SQL for JOINs, a search service for full-text).

Tip 6: transactions read-then-write and retry on conflict; batch writes write-only and do not retry. Both are limited to 500 documents per operation.

Tip 7: Firestore is serverless — no instance provisioning. This is the primary cost model difference from Cloud SQL (instance-based) and Bigtable (node-based).

Tip 8: sub-collections are the Firestore pattern for one-to-many relationships. A user document can have an orders sub-collection. This is different from a relational foreign key but achieves the same hierarchical structure.

---

### 10. Study Checklist

- Describe the five-level Firestore data hierarchy (project, database, collection, document, sub-collection)
- State the two Firestore modes and identify when each is appropriate
- Explain what a Security Rule does and write a simple rule that allows only authenticated users to read their own document
- Explain why multi-field Firestore queries require composite indexes
- Distinguish between a Firestore transaction and a batch write
- List three features that Firestore Native mode provides that Datastore mode does not
- Explain why Firestore is serverless and what that means for capacity planning
- Identify three workload characteristics that point to Firestore over Cloud SQL
- Complete the Module 06 lab activity
- Pass the Module 06 quiz with at least 80 percent

---

Reference: cloud.google.com/learn
