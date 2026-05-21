# Reading Guide: Module 10 - NoSQL Databases with MongoDB
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 10 - NoSQL Databases with MongoDB**! This module covers document-oriented NoSQL databases with MongoDB as the primary example. Unlike relational databases with rigid schemas, MongoDB stores data as flexible JSON-like BSON documents in collections, allowing the document structure to evolve without schema migrations. You will learn how to connect to MongoDB using the Mongoose ODM (Object Document Mapper), define schemas and models, and perform CRUD operations. On AWS, Amazon DocumentDB provides MongoDB-compatible managed hosting, and DynamoDB provides a related key-value/document NoSQL model that is heavily tested on the DVA-C02 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Document database**: A type of NoSQL database that stores each record as a self-describing, semi-structured document — typically in JSON or BSON format — rather than as rows in a fixed-schema table. Document databases like MongoDB are well-suited for hierarchical, variable-structure data (e.g., user profiles with different optional fields) that would require many nullable columns or complex joins in a relational model.
*   **Collections**: The MongoDB equivalent of a relational database table — a grouping of related BSON documents. Unlike SQL tables, collections do not enforce a schema by default; documents in the same collection can have different fields and nested structures. Collections are created implicitly when the first document is inserted.
*   **BSON (Binary JSON)**: The binary-encoded serialization format MongoDB uses internally to store documents. BSON extends JSON with additional data types including `Date`, `ObjectId`, `Binary`, `Decimal128`, and `Int32`/`Int64` integers. When you work with Mongoose or the MongoDB driver, BSON is handled transparently — you write plain JavaScript objects, and the driver serializes them to BSON automatically.
*   **Schema design**: In MongoDB and Mongoose, the deliberate modeling of document structures including field names, data types, validation rules, and relationships (embedding vs. referencing). Mongoose schemas are defined with `new Schema({ field: type })` and enforce structure at the application layer. Good NoSQL schema design considers query patterns first — embed related data when it is always read together and use references when data is shared across many documents.
*   **Mongoose model operations**: The CRUD API provided by Mongoose models compiled from schemas. Key methods include `Model.create()` (insert), `Model.find()` (query all matching), `Model.findById()` (query by `_id`), `Model.findByIdAndUpdate()` (update by `_id`), and `Model.findByIdAndDelete()` (delete by `_id`). All Mongoose operations are asynchronous and return Promises, making them compatible with `async/await`.

---

### 2. Certification Exam Tips
*   **DynamoDB vs. MongoDB on DVA-C02:** The DVA-C02 exam focuses on Amazon DynamoDB — AWS's proprietary NoSQL key-value and document database — not MongoDB. However, the document model concepts you learn here (flexible schemas, document embedding, query patterns) apply directly to DynamoDB. Key DVA-C02 DynamoDB topics: partition keys, sort keys, Global Secondary Indexes (GSI), on-demand vs. provisioned capacity, and DynamoDB Streams.
*   **Amazon DocumentDB for MongoDB Workloads:** The exam may present scenarios asking which AWS service is most appropriate for a MongoDB application migrating to AWS. Amazon DocumentDB is the MongoDB-compatible managed service. Know that DocumentDB is API-compatible with MongoDB 3.6/4.0/5.0 but uses Aurora's storage engine internally.
*   **Study Resource:** The official Mongoose documentation is the most practical reference for MongoDB with Node.js. [Mongoose — Getting Started](https://mongoosejs.com/docs/index.html) covers schema definition, model creation, and CRUD operations with working code examples relevant to this module's lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 3 section covering **MongoDB and Mongoose** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3) — this section integrates MongoDB into the REST API built in earlier parts of the course.
*   **Required Video:** Watch the MongoDB and Mongoose section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering database connection, schema definition, and CRUD operations.

---

### Lab & Command Integration
In this week's hands-on lab, you will connect a Node.js application to MongoDB:
*   **Establish a Mongoose server connection profile**: Call `mongoose.connect(process.env.MONGODB_URI)` in your Express app's entry file and handle the resulting Promise to log a success message or throw an error on connection failure.
*   **Define user models with schema validation**: Create a `User` schema using `new mongoose.Schema({ name: { type: String, required: true }, email: { type: String, required: true, unique: true } })` and compile it with `mongoose.model('User', userSchema)`.
*   **Write CRUD queries to write records**: Use `User.create({ name, email })` to insert a document and `User.find()` to retrieve all users — test both operations with Postman and verify the data appears in MongoDB Atlas (free tier cloud database).

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 3 covering **MongoDB and Mongoose** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3).
- [ ] Watch the MongoDB and Mongoose section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Create a free [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) cluster and obtain a connection string before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
