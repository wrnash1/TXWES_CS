# Video Script: Module 06 — Firestore and Datastore: Document Databases (Part 1)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 13–15 minutes

---

### Opening

**[SHOW SLIDE: Module 06 — Firestore and Datastore: Document Databases]**

Hello, and welcome back to CIS-4327. I am Professor Nash. This is Module 06: Firestore and Datastore.

In this module we cover Cloud Firestore — Google Cloud's fully managed, serverless document database — and Cloud Datastore, which is the predecessor that Firestore supersedes. These are the services you use when your data is semi-structured, your schema needs to evolve frequently, and your primary clients are mobile or web applications.

In Part 1 we cover Firestore's data model, modes, security rules, and how it compares to the relational databases we have studied. In Part 2 we cover querying, indexing, transactions, and exam scenarios.

---

### Section 1 — What Is Firestore?

**[SHOW SLIDE: Firestore positioning — document database between Bigtable and Cloud SQL]**

Cloud Firestore is a serverless document database. Serverless means there are no instances to create, no nodes to configure, and no clusters to size. You write data and it scales automatically.

The word document refers to the data model. In Firestore, data is stored as documents — JSON-like structures containing key-value pairs, nested objects, and arrays. Documents are grouped into collections, and collections can contain sub-collections, enabling a hierarchical data model.

Firestore is the recommended successor to Cloud Datastore. All new projects should use Firestore. Legacy Datastore applications can run in Datastore mode in Firestore — they use the Datastore API but benefit from Firestore's underlying infrastructure.

---

### Section 2 — Firestore Data Model

**[SHOW SLIDE: Firestore hierarchy — project, databases, collections, documents, sub-collections]**

The Firestore data model has four levels.

A database is the top-level resource. Each GCP project can have multiple Firestore databases.

A collection is a container for documents. Collections are analogous to tables in a relational database, but they are schema-less — different documents in the same collection can have different fields.

A document is the primary data unit. It is a JSON-like object with a unique ID within its collection. A document can contain:

- Scalar values: string, number, boolean, null, timestamp, geopoint
- Arrays of scalar values
- Maps (nested objects)
- References to other documents

A sub-collection is a collection nested within a document. This is how you model one-to-many relationships in Firestore — each parent document can have zero or more sub-collections containing child documents.

**[SHOW SLIDE: Document structure example — user document with nested address map and a reviews sub-collection]**

Example document structure:

```json
{
  "users/user-001": {
    "fullName": "Alice Johnson",
    "email": "alice@example.com",
    "createdAt": "2024-01-15T09:00:00Z",
    "address": {
      "street": "123 Main St",
      "city": "Fort Worth",
      "state": "TX"
    },
    "tags": ["premium", "verified"]
  }
}
```

The address is a nested map. The tags is an array. Sub-collections for reviews or orders would appear as separate collection paths under this document.

---

### Section 3 — Firestore Modes

**[SHOW SLIDE: Native Mode vs. Datastore Mode comparison table]**

Firestore has two modes.

Native mode is the current default and the recommended choice for all new applications. It supports real-time listeners (live updates pushed to clients when data changes), offline data persistence for mobile clients, a more expressive query model, and improved consistency guarantees.

Datastore mode is for applications migrating from Cloud Datastore. It supports the Datastore API and data model but runs on Firestore infrastructure. It does not support real-time listeners.

For the exam: always select Firestore Native mode for new mobile or web application backends. Datastore mode is only selected when the question specifically mentions a legacy Datastore migration.

---

### Section 4 — Firestore Security Rules

**[SHOW SLIDE: Firestore Security Rules — server-side access control]**

Firestore Security Rules are server-side access control policies written in a declarative language. They control which clients can read, write, create, update, or delete documents based on authentication state, user identity, or document field values.

Security rules are critical for mobile applications where clients connect directly to Firestore without a backend server intermediary.

**[SHOW CODE]**

```text
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Allow authenticated users to read their own profile
    match /users/{userId} {
      allow read: if request.auth != null
                  && request.auth.uid == userId;

      // Allow write only to the user's own document
      allow write: if request.auth != null
                   && request.auth.uid == userId;
    }

    // Allow any authenticated user to read products
    match /products/{productId} {
      allow read: if request.auth != null;
      // Only server-side writes allowed (no client write rule)
    }
  }
}
```

**[END CODE]**

`request.auth.uid` is the Firebase Authentication user ID of the requesting client. `resource.data` provides access to the current document's fields for field-level validation. Security rules are deployed separately from application code.

---

### Section 5 — Firestore vs. Cloud Datastore

**[SHOW SLIDE: Feature comparison — Firestore Native vs. Datastore Mode]**

| Feature | Firestore Native Mode | Datastore Mode |
|---|---|---|
| Real-time listeners | Yes | No |
| Offline persistence (mobile) | Yes | No |
| Transactions | Multi-document | Single entity group |
| Query expressiveness | Higher | Lower |
| API | Firestore SDK | Datastore API |
| Use case | New mobile/web apps | Legacy Datastore migration |

---

### Section 6 — Comparing Document Databases to Relational Databases

**[SHOW SLIDE: When to use Firestore vs. Cloud SQL]**

The decision between Firestore and Cloud SQL comes down to schema flexibility and client access patterns.

Use Firestore when:

- The schema changes frequently and different records may have different shapes
- Primary clients are mobile iOS, Android, or web browsers connecting directly to the database
- Real-time live updates need to be pushed to clients without polling
- Offline data access for mobile users is required

Use Cloud SQL when:

- The schema is stable and well-defined
- ACID transactions spanning multiple tables are required
- Complex SQL JOINs and aggregations are needed
- The application is a server-side service, not a mobile client

---

### Closing — Part 1 Summary

**[SHOW SLIDE: Module 06 Part 1 key concepts]**

In Part 1 we covered Firestore's data model — projects, databases, collections, documents, and sub-collections. We covered Firestore Native mode vs. Datastore mode and when to use each. We covered Security Rules as server-side access control for direct client connections.

We established the decision criteria: Firestore for mobile/web apps with flexible schema, Cloud SQL for stable relational schemas with ACID transactions.

In Part 2 we cover Firestore querying, composite indexes, transactions and batch writes, and exam scenarios.

See you in Part 2.

---

Reference: cloud.google.com/learn
