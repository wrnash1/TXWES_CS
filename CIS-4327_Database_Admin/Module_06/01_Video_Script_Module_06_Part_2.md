# Video Script: Module 06 — Firestore and Datastore: Document Databases (Part 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 11–13 minutes

---

### Opening

**[SHOW SLIDE: Module 06 Part 2 — Querying, Indexes, Transactions, and Exam Tips]**

Welcome back. I am Professor Nash, and this is Part 2 of Module 06.

In Part 1 we covered Firestore's document data model, modes, and security rules. Now we cover how to query documents, how indexes work in Firestore, transactions and batch writes, and the exam scenarios that test Firestore knowledge.

---

### Section 1 — Querying Firestore

**[SHOW SLIDE: Firestore query operations — collection queries, document reads, sub-collection queries]**

Firestore supports two types of reads.

A document read retrieves a single document by its full path. This is always efficient — it is a direct key lookup.

A collection query retrieves multiple documents from a collection based on filter conditions. Firestore supports filtering by field value equality, comparison operators (less than, greater than, less than or equal to, greater than or equal to), array-contains, and in operators.

**[SHOW CODE]**

```bash
# Read a single document by path (using gcloud firestore CLI)
gcloud firestore documents get \
    "projects/PROJECT_ID/databases/(default)/documents/users/user-001"

# Create a document
gcloud firestore documents create \
    "projects/PROJECT_ID/databases/(default)/documents/products/prod-001" \
    --fields='productName="Wireless Keyboard",price=49.99,category="Electronics",inStock=true'
```

**[END CODE]**

In application code using the Firestore SDK, queries look like this conceptually:

```text
Collection: products
Filter: category == "Electronics" AND price < 50.00
Order: price ASC
Limit: 10
```

Firestore queries are always indexed. There are no full-collection scans — every query uses an index. This is what gives Firestore predictable query performance regardless of collection size.

---

### Section 2 — Indexes in Firestore

**[SHOW SLIDE: Single-field indexes vs. composite indexes]**

Firestore automatically creates single-field indexes for every field in every document. This means simple equality and range queries on a single field work out of the box.

Composite indexes are required for queries that filter or order on multiple fields simultaneously. If you run a query like `category == "Electronics" AND price < 50 ORDER BY price`, Firestore needs a composite index on (category, price). Firestore will return an error if the required composite index does not exist, along with a link to create it in the Console.

**[SHOW CONSOLE: Firestore Console — Indexes tab showing composite indexes]**

Composite indexes must be created explicitly. You define them in the `firestore.indexes.json` file and deploy them with the Firebase CLI, or create them manually in the Console.

Index Exemptions: for fields that are never queried individually or in combinations, you can disable automatic single-field indexing to reduce index storage costs. This is particularly useful for large text fields or blob-like fields that are written but not filtered.

---

### Section 3 — Transactions and Batch Writes

**[SHOW SLIDE: Firestore transactions — atomic multi-document reads and writes]**

Firestore supports two mechanisms for multi-document atomic operations.

Transactions allow you to read and then write multiple documents atomically. If any document changes between the read and the write, Firestore automatically retries the transaction. Firestore transactions provide Serializable isolation for the documents involved.

Batch writes allow you to write multiple documents atomically — create, update, or delete — without reading first. A batch write either succeeds entirely or fails entirely. Batch writes do not retry automatically on conflict.

Both transactions and batch writes are limited to 500 documents per operation.

The key distinction for the exam: use a transaction when you need to read a value before deciding what to write. Use a batch write when you know what you want to write without reading first.

---

### Section 4 — Firestore vs. Bigtable vs. Cloud SQL — Exam Comparison

**[SHOW SLIDE: Three-service comparison matrix]**

| Criterion | Firestore | Bigtable | Cloud SQL |
|---|---|---|---|
| Data model | Document (JSON-like) | Wide-column key-value | Relational tables |
| Schema | Flexible, schema-less | Column families defined | Fixed columns |
| JOINs | None | None | Full SQL JOINs |
| ACID transactions | Single-document or multi-document (limited) | None | Full ACID |
| Real-time updates | Yes (Native mode) | No | No |
| Offline mobile sync | Yes (Native mode) | No | No |
| Query model | Field equality and ranges; no full-text search | Key-based range scan | Full SQL |
| Scale | Automatic, serverless | Manual cluster sizing | Vertical scaling |
| Best for | Mobile/web app backends | Time-series, IoT, petabyte-scale | Enterprise OLTP |

---

### Section 5 — Datastore Mode and Legacy Applications

**[SHOW SLIDE: Cloud Datastore to Firestore migration path]**

Cloud Datastore was the original document-style database on Google Cloud, introduced before Firestore existed. New projects should always use Firestore. Existing Datastore applications have two options.

Run in Datastore mode: the application continues using the Datastore API. Data is stored on Firestore infrastructure but accessed through the Datastore-compatible interface. No code changes are needed, and the application gains Firestore's improved reliability.

Migrate to Native mode: the application code is rewritten to use the Firestore SDK. This enables real-time listeners, better offline support, and improved query capabilities. This is the recommended long-term path.

For the exam: if a question describes a Cloud Datastore application that needs real-time listeners or offline sync, the answer is migrating to Firestore Native mode.

---

### Section 6 — Exam Tips for Module 06

**[SHOW SLIDE: Firestore exam tips]**

Tip one: Firestore is the answer for mobile and web app backends where clients connect directly to the database, especially when offline sync or real-time updates are mentioned.

Tip two: Firestore Native mode vs. Datastore mode. Native mode is for new applications. Datastore mode is for legacy Datastore migrations. If the question describes real-time listeners, the answer requires Native mode.

Tip three: every Firestore query uses an index. Simple single-field queries use automatically created indexes. Multi-field queries require composite indexes. If a composite index is missing, Firestore returns an error.

Tip four: Firestore does not support full-text search. If a scenario requires searching document content by keyword, Firestore alone is insufficient — a search service would be needed alongside it.

Tip five: Security Rules are the access control mechanism for direct client connections to Firestore. They run on the server side and are evaluated before any data is returned to a client.

Tip six: the difference between transactions and batch writes. Transactions read then write; they retry on conflict. Batch writes just write; they do not retry. Both are limited to 500 documents.

Tip seven: Firestore is serverless. You do not provision instances or configure node counts. This is a key differentiator from Cloud SQL, Cloud Spanner, and Bigtable, all of which require explicit capacity configuration.

Tip eight: Firestore pricing is based on document reads, writes, and deletes — not on provisioned capacity. This aligns cost with actual usage for variable-traffic applications.

---

### Closing — Module 06 Wrap-Up

**[SHOW SLIDE: Module 06 complete]**

That completes Module 06. You now understand Firestore's document model, security rules, querying, indexing, and transactions.

Your lab walks you through creating a Firestore database, writing and reading documents, creating a composite index, and writing security rules.

In Module 07 we move to BigQuery — Google Cloud's serverless data warehouse for large-scale analytics. This is the final major GCP database service on the exam and covers an entirely different workload class: analytical SQL queries over billions of rows.

See you in Module 07.

---

Reference: cloud.google.com/learn
