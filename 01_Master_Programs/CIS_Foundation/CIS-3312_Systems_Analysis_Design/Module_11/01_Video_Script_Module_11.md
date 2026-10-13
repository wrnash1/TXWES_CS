# Video Script: Module 11 — Entity-Relationship Diagrams and Data Modeling

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: IIBA ECBA — Business Analysis Core Concept Model

---

### SEGMENT 1: Introduction — Why Data Modeling Matters (0:00–2:00)

Welcome to Module 11. We have been building requirements models throughout this course:
use case diagrams show who interacts with the system, BPMN shows how work flows, and DFDs
show how data moves. Today we go deeper into the data itself.

[PAUSE]

Entity-Relationship Diagrams — ERDs — model the structure of data. They answer the
question: what things does the system need to remember, what do we know about each thing,
and how are those things related to each other? This is the foundation of database design,
but it is also a requirements analysis tool that business analysts use to validate that
stakeholders share a common understanding of the business domain.

[SHOW DIAGRAM: Simple ERD with Member, Book, and Loan entities and relationships between them]

Peter Chen introduced the entity-relationship model in a landmark 1976 paper that remains
one of the most cited works in computer science. Today we work with a refined version of
his ideas using Crow's Foot notation, which is the most common ERD notation in modern
business analysis and database design tools.

[PAUSE]

By the end of this module you will be able to identify entities, attributes, and
relationships in a business problem description, draw a conceptual ERD using Crow's Foot
notation, specify cardinality and optionality for every relationship, and distinguish
between conceptual and logical data models.

---

### SEGMENT 2: Entities and Attributes (2:00–5:30)

An entity is a thing about which the system needs to store information. Entities represent
real-world objects, concepts, events, or roles. In an ERD, an entity is drawn as a
rectangle with the entity name in all caps or title case at the top.

[PAUSE]

Good entities have these characteristics: they can have multiple instances — there can be
more than one; each instance can be uniquely identified; and each instance has attributes
worth storing. "Member" is a good entity — there are thousands of members, each uniquely
identified by a member ID, and we store their name, email, address, and status. "Blue" is
not an entity — it has no attributes and cannot be uniquely identified.

[SHOW DIAGRAM: Member entity box with attributes listed inside: MemberID (PK), LastName, FirstName, Email, Phone, MembershipStatus, ExpiryDate]

Attributes are the properties of an entity — the individual pieces of information we store
about each instance. In Crow's Foot notation, attributes are typically listed inside the
entity rectangle below the entity name.

[PAUSE]

Attribute types you need to know:

A simple attribute holds a single indivisible value — MemberID, LastName, Email.

A composite attribute is made up of multiple components — an Address attribute might
contain Street, City, State, and ZIP. In a logical model we usually split composites into
their components.

A derived attribute can be calculated from other attributes — Age can be derived from
DateOfBirth. We mark derived attributes with a dashed underline in Chen notation or with
a note in Crow's Foot.

A multi-valued attribute can hold multiple values for one entity instance — a Member might
have multiple phone numbers. Multi-valued attributes often indicate a need for a separate
entity and relationship.

The primary key attribute uniquely identifies each entity instance. It must be unique across
all instances and must never be null. We mark it with a bold or underlined font and often
add (PK) or a key icon depending on the tool.

---

### SEGMENT 3: Relationships and Crow's Foot Notation (5:30–9:00)

Relationships describe how entities are associated with each other. In an ERD, a
relationship is drawn as a line connecting two entities. The relationship has a name — a
verb phrase describing how one entity relates to the other.

[PAUSE]

In our LMS: a Member borrows Books. A Librarian processes Loans. A Book belongs to a
Genre. These are relationships — verbs that describe the association between two nouns.

Crow's Foot notation adds cardinality symbols at each end of the relationship line to
specify how many instances of one entity can be related to instances of the other entity.

[SHOW DIAGRAM: Crow's Foot symbol reference — one, many (crow's foot), zero-or-one, one-and-only-one, zero-or-many, one-or-many]

Let me walk through the Crow's Foot symbols. On the relationship line, at each end, we
draw two marks. The outer mark (furthest from the entity) shows the maximum cardinality:
either a straight line (meaning one) or a crow's foot (three prongs, meaning many).

The inner mark (closest to the entity) shows the minimum cardinality — the optionality:
either a circle (meaning zero — optional) or a straight line (meaning one — mandatory).

[PAUSE]

Reading a Crow's Foot relationship: you read it from each entity's perspective, going
across to the other entity. Start at one entity, cross to the other, and read the symbols
nearest that entity as the minimum and maximum for how many of the other entity are
associated with this one.

Let me make this concrete. Member BORROWS Book. From Member's side reading toward Book:
the symbols at the Book end show crow's foot (many) and circle (zero). So: one Member
can borrow zero-or-many Books.

From Book's side reading toward Member: the symbols at the Member end show one-line
(one) and one-line (one). So: each Book loan is associated with exactly one Member.

---

### SEGMENT 4: Cardinality Types — One-to-One, One-to-Many, Many-to-Many (9:00–12:00)

There are three fundamental cardinality types you must master: one-to-one, one-to-many,
and many-to-many.

[PAUSE]

A one-to-one relationship means each instance of Entity A is associated with at most one
instance of Entity B, and vice versa. Example: each Member has exactly one LibraryCard,
and each LibraryCard is issued to exactly one Member. One-to-one relationships are
relatively rare in data models — if every A has exactly one B, you should ask whether A
and B should be the same entity.

[SHOW DIAGRAM: Member — has — LibraryCard with one-to-one Crow's Foot notation]

A one-to-many relationship means each instance of Entity A is associated with zero or more
instances of Entity B, but each instance of Entity B is associated with exactly one instance
of Entity A. This is the most common relationship type in business data models.

Example: one Genre contains many Books, but each Book belongs to exactly one Genre. One
Member can have many Loans, but each Loan belongs to exactly one Member.

[PAUSE]

A many-to-many relationship means each instance of Entity A can be associated with many
instances of Entity B, and each instance of Entity B can be associated with many instances
of Entity A.

Example: one Book can appear on many Members' reading lists, and one Member can have many
books on their reading list. But here is the critical concept: many-to-many relationships
cannot be directly implemented in a relational database. They must be resolved by creating
an associative entity — also called a junction or bridge entity — that sits between the two
original entities and holds the relationship as two one-to-many relationships.

[SHOW DIAGRAM: Member — many-to-many — Book resolved with Loan associative entity; Loan has LoanID, CheckOutDate, DueDate, ReturnDate]

The Loan entity resolves the many-to-many between Member and Book. Each Loan belongs to
one Member and involves one Book. Each Member can have many Loans. Each Book can have many
Loans. The Loan entity also has its own attributes — CheckOutDate, DueDate, ReturnDate —
that belong to the relationship, not to either original entity.

---

### SEGMENT 5: Primary Keys, Foreign Keys, and Referential Integrity (12:00–14:30)

Now let's connect ERD concepts to relational database concepts that the ERD drives.

[PAUSE]

A primary key uniquely identifies each row in a database table. It corresponds to the
primary key attribute of an entity. Every entity must have a primary key. Common choices:
natural keys — values that already exist in the domain like ISBN for books or Email for
members — or surrogate keys — system-generated IDs like MemberID or LoanID.

A foreign key is an attribute in one table that references the primary key of another
table. Foreign keys implement relationships. In the Loan table, MemberID is a foreign key
referencing the Member table, and BookCopyID is a foreign key referencing the BookCopy
table.

[SHOW DIAGRAM: Three-table ERD with PK/FK annotations showing Member.MemberID ← Loan.MemberID → BookCopy.BookCopyID]

Referential integrity is the database rule that a foreign key value must either be null
(if the relationship is optional) or match an existing primary key value in the referenced
table. If a Loan record has a MemberID of 9999 and no Member with ID 9999 exists, that is
a referential integrity violation.

[PAUSE]

For ECBA alignment: understanding primary and foreign keys is part of understanding data
modeling as a requirements technique. The BABOK lists data modeling as a business analysis
tool, and business analysts must be able to read and evaluate ERDs even if they do not
personally design databases.

---

### SEGMENT 6: Conceptual vs. Logical Data Models (14:30–17:00)

In practice, data modeling happens in stages. The two stages most relevant to business
analysis are the conceptual model and the logical model.

[PAUSE]

A conceptual data model is technology-independent and audience-focused. It shows entities
and relationships — the business view of data — without data types, primary keys, or
implementation details. It is designed to be understood by business stakeholders who do not
know SQL. A conceptual model for the LMS might show: Member, Book, Loan, Reservation,
Librarian, Genre. The relationships are named but not yet fully specified with keys.

[SHOW DIAGRAM: Conceptual LMS ERD — five entity boxes with named relationships but no attribute lists]

A logical data model refines the conceptual model into a more precise technical
specification. It adds: all attributes with their data types, primary key identification,
foreign key assignments that implement relationships, normalization to reduce redundancy,
and full cardinality notation. The logical model is the input to physical database design.

[PAUSE]

A physical data model adds implementation specifics: actual table names, column names in
the target database's naming conventions, index definitions, storage parameters, and
database-specific data type choices. Physical models are produced by database architects,
not typically by business analysts.

The business analyst's work lives primarily in the conceptual and logical models. You
capture what the business needs to remember; the database team translates that into a
physical schema.

---

### SEGMENT 7: Relationship Naming and Reading ERDs (17:00–19:00)

One of the most practical skills in ERD work is the ability to read an ERD fluently — to
look at a diagram and describe the business rules it encodes in plain English.

[PAUSE]

Every relationship should have a name that can be read as a sentence. The convention is to
read from left to right and then right to left. For each direction, you say: "Each [Entity
A] [relationship name] [zero/one/one-or-more] [Entity B]."

Using our LMS: the relationship between Member and Loan is "places." Reading left to right:
"Each Member places zero-or-more Loans." Reading right to left: "Each Loan is placed by
exactly one Member." Those two sentences completely describe the business rules about
member borrowing.

[SHOW DIAGRAM: Member — places — Loan with bidirectional reading arrows and sentence annotations]

[PAUSE]

Reading ERDs fluently is a stakeholder validation skill. When you present an ERD in a
requirements review, walk stakeholders through each relationship by reading it as a
sentence. Ask: "Does this match your understanding of the business rule?" If a Librarian
says "actually, a book can belong to multiple genres," that tells you the Genre-Book
relationship should be many-to-many, not one-to-many. The ERD catches that misunderstanding
before database design begins.

---

### SEGMENT 8: Weak Entities and Identifying Relationships (19:00–21:00)

A weak entity is an entity whose instances cannot be uniquely identified by their own
attributes alone — they need to be identified in the context of a related entity.

[PAUSE]

Example: a BookCopy entity represents a specific physical copy of a book. A BookCopy is
identified by its CopyNumber — but CopyNumber 1 exists for thousands of different books.
BookCopy cannot be uniquely identified without also knowing which Book it belongs to. So
BookCopy is a weak entity. Its full identifier is the combination of BookID (from its parent
entity Book) plus CopyNumber.

The relationship between a weak entity and its parent is called an identifying relationship.
In Crow's Foot notation, weak entities are sometimes drawn with a double border, and the
identifying relationship has a diamond with a double line in Chen notation.

[SHOW DIAGRAM: Book — has copies — BookCopy with weak entity notation; BookCopy identifier is (BookID, CopyNumber)]

[PAUSE]

Weak entities are common in library, order, and invoicing data models: OrderLineItem is
weak relative to Order. InvoiceLine is weak relative to Invoice. BookCopy is weak relative
to Book. Recognizing weak entities ensures that the primary key design correctly captures
the identifying context.

---

### SEGMENT 9: Summary and ECBA Connections (21:00–23:00)

Let's close by connecting what we have covered to the ECBA exam and to the broader project
in this course.

[PAUSE]

Entity-Relationship Diagrams model data structure. The four core concepts are entities —
things to store data about; attributes — properties of entities; relationships — associations
between entities; and cardinality — the numeric constraints on those associations.

Crow's Foot notation uses an outer symbol for maximum cardinality — line for one, crow's
foot for many — and an inner symbol for minimum cardinality — circle for zero, line for one.
Many-to-many relationships are resolved with associative entities. Conceptual models are
business-facing; logical models are database-facing.

[SHOW DIAGRAM: Complete LMS logical ERD with Member, Book, BookCopy, Loan, Reservation, Genre, and Librarian entities with all attributes and relationships]

For the ECBA exam: data modeling is a listed technique in the BABOK. Expect questions about
cardinality identification, relationship types, and the purpose of associative entities.
Know that a primary key uniquely identifies an entity instance and that a foreign key
implements a relationship between tables.

[PAUSE]

Your lab this week takes you through the full LMS data model from conceptual to logical.
Your quiz tests cardinality reading, entity identification, and key concepts. In Module 12
we move to interface and interaction design — shifting from what data the system stores to
how users experience the system. See you there.

---

*[END OF VIDEO SCRIPT — Module 11]*
