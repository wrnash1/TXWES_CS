# Quiz: Module 10 - NoSQL Databases with MongoDB
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which data format does MongoDB use natively to store documents in collections?
*   A) XML
*   B) CSV
*   C) BSON (Binary JSON)
*   D) SQL Table Structure
*   **Correct Answer:** C) MongoDB stores documents internally as BSON (Binary JSON) — a binary-encoded extension of JSON that supports additional data types including `Date`, `ObjectId`, and 64-bit integers not available in plain JSON.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* XML is a markup language used for document exchange and configuration files — MongoDB does not use XML for document storage.
    *   *Why B is incorrect:* CSV is a flat text format for tabular data — it has no concept of nested documents or arrays and is incompatible with MongoDB's document model.
    *   *Why C is correct:* BSON (Binary JSON) is MongoDB's native storage format — it is optimized for efficient encoding, decoding, and traversal of documents.
    *   *Why D is incorrect:* SQL table structures are rows and columns in a relational schema — MongoDB explicitly avoids this fixed-schema tabular model.

---

**Question 2**
Which of the following is the most accurate definition of **Mongoose model operations**?
*   A) Low-level TCP socket operations used by the MongoDB driver to open, authenticate, and close connections to the database server.
*   B) The CRUD API methods provided by a Mongoose model — such as `Model.create()`, `Model.find()`, `Model.findByIdAndUpdate()`, and `Model.findByIdAndDelete()` — that perform database operations asynchronously and return Promises.
*   C) The configuration options passed to `mongoose.connect()` that control connection pool size, timeout duration, and SSL certificate validation.
*   D) The Express route handlers that proxy HTTP requests from the API layer to the MongoDB database without any intermediate application logic.
*   **Correct Answer:** B) The CRUD API methods provided by a Mongoose model — such as `Model.create()`, `Model.find()`, `Model.findByIdAndUpdate()`, and `Model.findByIdAndDelete()` — that perform database operations asynchronously and return Promises.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes the MongoDB driver's connection layer — not Mongoose model operations.
    *   *Why B is correct:* Mongoose model operations are the query and mutation methods on compiled Mongoose models — they provide a higher-level abstraction over the raw MongoDB driver.
    *   *Why C is incorrect:* These are connection configuration options — separate from model operation methods.
    *   *Why D is incorrect:* Mongoose models are application-layer abstractions — they are not Express middleware or HTTP proxy handlers.

---

**Question 3**
A Mongoose schema is defined as `{ title: { type: String, required: true }, published: Boolean }`. A developer tries to save a document with `{ published: true }` — omitting `title`. What happens?
*   A) MongoDB silently inserts the document without `title` because collections have no schema enforcement by default.
*   B) Mongoose throws a `ValidationError` before sending the insert to MongoDB, because the `required: true` constraint on `title` is violated.
*   C) The document is saved with `title: null` automatically since MongoDB defaults missing required fields to null.
*   D) The operation succeeds but returns a warning — Mongoose `required` constraints are advisory only and do not block saves.
*   **Correct Answer:** B) Mongoose throws a `ValidationError` before sending the insert to MongoDB, because the `required: true` constraint on `title` is violated.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is true for raw MongoDB without Mongoose, but Mongoose adds schema-level validation that runs before the database operation.
    *   *Why B is correct:* Mongoose validates documents against the schema before executing the database write. `required: true` causes validation to fail and throws a `ValidationError`.
    *   *Why C is incorrect:* Mongoose does not default missing required fields to `null` — it throws a validation error.
    *   *Why D is incorrect:* `required` in a Mongoose schema is a hard constraint that blocks saves, not an advisory warning.

---

**Question 4**
When should a developer choose MongoDB over PostgreSQL for an AWS application?
*   A) When the data has a fixed, well-defined schema with strong referential integrity requirements between multiple related entities.
*   B) When the application needs complex multi-table JOIN queries with ACID transaction guarantees across multiple related records.
*   C) When the data structure varies between records (e.g., product catalogs with different attributes per category) or when horizontal scalability at the document level is a primary requirement.
*   D) When the application needs to store and query data using SQL syntax, because MongoDB supports standard SQL via the aggregation pipeline.
*   **Correct Answer:** C) When the data structure varies between records (e.g., product catalogs with different attributes per category) or when horizontal scalability at the document level is a primary requirement.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Fixed schemas with strong referential integrity are a strength of relational databases like PostgreSQL — not a MongoDB use case.
    *   *Why B is incorrect:* Complex multi-table JOINs and multi-record ACID transactions are where relational databases excel — MongoDB's aggregation pipeline is more complex for relational patterns.
    *   *Why C is correct:* MongoDB's schema-flexible document model is best suited for heterogeneous data where documents in the same collection legitimately have different fields.
    *   *Why D is incorrect:* MongoDB does not support SQL syntax — it uses its own query language and aggregation framework.

---

**Question 5**
On AWS, which service is the managed option for running MongoDB-compatible workloads without managing the underlying infrastructure?
*   A) Amazon RDS for MySQL
*   B) Amazon DynamoDB
*   C) Amazon DocumentDB (with MongoDB compatibility)
*   D) Amazon Redshift
*   **Correct Answer:** C) Amazon DocumentDB (with MongoDB compatibility) is AWS's managed document database service that implements MongoDB's API, allowing applications written for MongoDB to run without code changes while AWS handles patching, backups, and storage scaling.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Amazon RDS for MySQL is a relational database service — it uses SQL and a table-based schema, not MongoDB's document model.
    *   *Why B is incorrect:* Amazon DynamoDB is a key-value and document NoSQL database but is not MongoDB-compatible — it uses a different API and data model.
    *   *Why C is correct:* DocumentDB was designed to be API-compatible with MongoDB, making it the AWS migration target for MongoDB workloads.
    *   *Why D is incorrect:* Amazon Redshift is a cloud data warehouse optimized for analytical SQL queries against large datasets — not a document or operational database.
