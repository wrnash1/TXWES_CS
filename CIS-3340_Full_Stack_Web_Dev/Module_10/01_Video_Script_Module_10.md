# Video Script: Module 10 - NoSQL Databases with MongoDB

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 21 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code, MongoDB Compass, Postman/Thunder Client
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for MongoDB Compass; [SHOW TERMINAL] for mongosh
- Install MongoDB Community Edition locally before recording
- Have MongoDB Compass open showing the bookstore database

---

## Section 1: Introduction - Document Databases [00:00 - 04:00]

Welcome to Module 10. I am Professor Nash. Last module we built a PostgreSQL database — rows, columns, tables, foreign keys, JOINs. This module we explore a completely different data model: document databases, specifically MongoDB.

MongoDB stores data as documents — JSON-like objects with flexible fields. There are no tables, no columns, no predefined schema. A document in a "books" collection might have five fields. Another document in the same collection might have ten. This is called schema-flexibility.

[SHOW BROWSER]

Let me open MongoDB Compass — MongoDB's GUI — and show you what this looks like. I can see the `bookstore` database with a `books` collection. Each document has a unique `_id` field that MongoDB assigns automatically. The documents look like JavaScript objects.

When should you use MongoDB instead of PostgreSQL? The deciding factor is your data model and access pattern. MongoDB excels when:

- Documents in the same collection legitimately have different fields (a product catalog where laptops have `RAM` and `storage`, books have `author` and `ISBN`)
- You embed related data in a single document rather than joining multiple tables
- Your primary access pattern is "fetch one document by ID"

**AWS Exam Tip:** Amazon DocumentDB is the AWS managed service for MongoDB-compatible workloads. DVA-C02 questions about NoSQL databases on AWS test whether you know when to use DocumentDB (MongoDB workloads) versus DynamoDB (key-value with single access pattern at scale). This module's SQL vs. NoSQL decision framework will help you answer those questions correctly.

---

## Section 2: MongoDB Concepts and mongosh [04:00 - 08:30]

[SHOW TERMINAL]

Let me open `mongosh` — the MongoDB shell:

```bash
mongosh
```

Key vocabulary:

- Database: equivalent to a PostgreSQL database
- Collection: equivalent to a table, but without a fixed schema
- Document: a JSON-like record, equivalent to a row
- `_id`: automatically assigned unique identifier (ObjectId type)

```javascript
// Switch to a database (creates it if it doesn't exist)
use bookstore

// Create a collection and insert a document
db.books.insertOne({
  title: "Clean Code",
  author: "Robert C. Martin",
  year: 2008,
  genre: "Software Engineering",
  tags: ["refactoring", "best practices"]
})

// Find all documents
db.books.find()

// Find with a filter
db.books.find({ genre: "Software Engineering" })

// Find with projection (include only specified fields)
db.books.find({ genre: "JavaScript" }, { title: 1, year: 1, _id: 0 })
```

Unlike SQL, queries in MongoDB use a JavaScript-like syntax with query operators:

```javascript
// Greater than
db.books.find({ year: { $gt: 2000 } })

// In a list
db.books.find({ genre: { $in: ["JavaScript", "Python"] } })

// Text search (requires text index)
db.books.find({ $text: { $search: "refactoring" } })
```

---

## Section 3: Mongoose - Schema and Models [08:30 - 13:30]

[SHOW CODE]

Mongoose is an Object Document Mapper (ODM) for MongoDB in Node.js. It adds schema validation, type coercion, and a model-based CRUD API on top of the raw MongoDB driver.

Install it:

```bash
npm install mongoose dotenv
```

Connect to MongoDB in `db.js`:

```javascript
const mongoose = require('mongoose');
require('dotenv').config();

const connect = async () => {
  await mongoose.connect(process.env.MONGO_URI || 'mongodb://localhost:27017/bookstore');
  console.log('MongoDB connected');
};

module.exports = { connect };
```

In `.env`:

```text
MONGO_URI=mongodb://localhost:27017/bookstore
```

Define a schema in `models/Book.js`:

```javascript
const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: [true, 'Title is required'],
      trim: true,
      maxlength: 255
    },
    author: {
      type: String,
      required: [true, 'Author is required'],
      trim: true
    },
    year: {
      type: Number,
      min: 1000,
      max: 2100
    },
    genre: {
      type: String,
      enum: ['JavaScript', 'Software Engineering', 'Python', 'Other'],
      default: 'Other'
    },
    tags: [String]     // array of strings
  },
  { timestamps: true }  // adds createdAt and updatedAt automatically
);

const Book = mongoose.model('Book', bookSchema);

module.exports = Book;
```

The `{ timestamps: true }` option adds `createdAt` and `updatedAt` fields managed by Mongoose.

---

## Section 4: CRUD Operations with Mongoose [13:30 - 17:30]

[SHOW CODE]

Mongoose model methods are asynchronous and return Promises. Use `async/await` in route handlers.

```javascript
const Book = require('../models/Book');

// GET all books
router.get('/', async (req, res, next) => {
  try {
    const books = await Book.find().sort({ title: 1 });
    res.status(200).json(books);
  } catch (err) {
    next(err);
  }
});

// GET one book by _id
router.get('/:id', async (req, res, next) => {
  try {
    const book = await Book.findById(req.params.id);
    if (!book) return res.status(404).json({ error: 'Book not found', code: 'BOOK_NOT_FOUND' });
    res.status(200).json(book);
  } catch (err) {
    next(err); // CastError if :id is not a valid ObjectId
  }
});

// POST create a book
router.post('/', async (req, res, next) => {
  try {
    const book = await Book.create(req.body);
    res.status(201)
      .set('Location', `/api/books/${book._id}`)
      .json(book);
  } catch (err) {
    if (err.name === 'ValidationError') {
      return res.status(400).json({
        error: 'Validation failed',
        code: 'VALIDATION_ERROR',
        details: Object.values(err.errors).map(e => ({
          field: e.path,
          message: e.message
        }))
      });
    }
    next(err);
  }
});

// PUT replace a book
router.put('/:id', async (req, res, next) => {
  try {
    const book = await Book.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true, overwrite: true }
    );
    if (!book) return res.status(404).json({ error: 'Book not found' });
    res.status(200).json(book);
  } catch (err) {
    next(err);
  }
});

// DELETE a book
router.delete('/:id', async (req, res, next) => {
  try {
    const book = await Book.findByIdAndDelete(req.params.id);
    if (!book) return res.status(404).json({ error: 'Book not found' });
    res.status(204).send();
  } catch (err) {
    next(err);
  }
});
```

The `{ new: true }` option on `findByIdAndUpdate` returns the updated document rather than the original. The `runValidators: true` option applies schema validation to the update.

**AWS Exam Tip:** When connecting a Lambda function to MongoDB Atlas or DocumentDB, manage the connection outside the handler function — reuse it across warm invocations. Calling `mongoose.connect()` inside the handler creates a new connection on every invocation, which is slow and can exhaust connection limits. This is the same connection pool principle as RDS with node-postgres.

---

## Section 5: Embedded Documents and Lab Preview [17:30 - 21:00]

[SHOW CODE]

MongoDB's most distinctive feature is embedding related data in a single document, rather than joining two tables. Compare the two approaches:

PostgreSQL (join required):

```sql
SELECT b.title, a.name, a.country
FROM books b
INNER JOIN authors a ON a.id = b.author_id
WHERE b.id = 42;
```

MongoDB (embedded, single query):

```javascript
// Document structure
{
  _id: ObjectId("..."),
  title: "Clean Code",
  year: 2008,
  author: {           // embedded sub-document
    name: "Robert C. Martin",
    country: "USA"
  },
  reviews: [          // embedded array of sub-documents
    { user: "alice", rating: 5, comment: "Essential reading" },
    { user: "bob", rating: 4, comment: "Very practical" }
  ]
}

// Single query retrieves all related data
const book = await Book.findById(id);
// book.author.name, book.reviews[0].rating — all in one document
```

When to embed vs. when to reference:

- Embed when the child data is always accessed with the parent (reviews, addresses, metadata)
- Reference (store an `_id`) when the child data is large, changes frequently, or is shared across many parents

In the lab this week you will set up MongoDB locally, create a Mongoose schema for books with embedded author information, implement all five CRUD routes, and test with Thunder Client. You will also create a text index on the title field and test the search capability.

Thank you for watching. See you in Module 11 where we move to the front end and learn React.

---

## Additional Resources

- developer.mozilla.org — search "Mongoose documentation" for complete schema and query reference
- aws.amazon.com/certification — review Amazon DocumentDB documentation for DVA-C02 exam preparation
