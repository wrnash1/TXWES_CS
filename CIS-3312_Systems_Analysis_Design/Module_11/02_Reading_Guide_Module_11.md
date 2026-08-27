# Reading Guide: Module 11 — Entity-Relationship Diagrams and Data Modeling

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Overview

This reading guide covers entity-relationship modeling using Crow's Foot notation,
including entities, attributes, relationships, cardinality, primary and foreign keys,
associative entities, weak entities, and the distinction between conceptual and logical
data models. Data modeling is a BABOK-listed business analysis technique.

---

### Section 1: ERD Element Reference

An entity-relationship diagram has three building blocks: entities, attributes, and
relationships. Every ERD element has a specific visual representation in Crow's Foot
notation.

#### Entities

An entity represents a person, place, thing, event, or concept about which the system
must store information. Entities are drawn as rectangles.

Criteria for a well-defined entity:

- Has multiple instances (there is more than one)
- Each instance can be uniquely identified
- Has attributes worth storing beyond just an identifier
- Is relevant to the business domain being modeled

Examples from the LMS: Member, Book, BookCopy, Loan, Reservation, Genre, Librarian.

Non-examples: "Information," "Data," "Blue" — these fail the criteria above.

#### Attributes

Attributes are properties of an entity. They are listed inside the entity rectangle below
the entity name in Crow's Foot notation.

| Attribute Type | Definition | LMS Example |
|---|---|---|
| Simple | Single indivisible value | LastName, Email |
| Composite | Made up of component parts | Address (Street, City, State, ZIP) |
| Derived | Calculated from other attributes | MembershipDaysRemaining from ExpiryDate |
| Multi-valued | Multiple values per instance | PhoneNumbers (triggers separate entity) |
| Primary Key (PK) | Uniquely identifies each instance; never null | MemberID, LoanID |
| Foreign Key (FK) | References the PK of another entity | Loan.MemberID references Member.MemberID |

#### Relationships

A relationship is an association between two entities. It is drawn as a line connecting
the two entity rectangles. The line is labeled with a verb phrase describing the
association read from the perspective of the left or top entity.

---

### Section 2: Crow's Foot Notation — Complete Symbol Reference

Crow's Foot notation encodes cardinality using symbols placed at each end of the
relationship line. Two symbols appear at each end: an outer symbol (maximum) and an inner
symbol (minimum/optionality).

#### Cardinality Symbols

| Symbol | Position | Meaning |
|---|---|---|
| Single vertical line ( | ) | Outer (maximum) | One — at most one |
| Crow's foot (three-pronged mark) | Outer (maximum) | Many — more than one |
| Circle ( o ) | Inner (minimum) | Zero — optional; the relationship is not required |
| Single vertical line ( | ) | Inner (minimum) | One — mandatory; the relationship is required |

#### Reading the Symbols — Combined Notation

The combination of outer and inner symbols produces six possible endpoint notations.

| Outer + Inner | Reads As | Meaning |
|---|---|---|
| Line + Line | One and only one | Exactly one; mandatory |
| Line + Circle | Zero or one | Optional; at most one |
| Crow's foot + Line | One or more | Mandatory; at least one |
| Crow's foot + Circle | Zero or more | Optional; any number including none |
| (Line + Line both ends) | One-to-one | Each A has exactly one B; each B has exactly one A |

#### How to Read a Crow's Foot Relationship

To read a relationship, choose a starting entity and cross to the other entity. The
symbols at the far end (the end you are approaching) describe how many of that entity
are associated with one instance of your starting entity.

Example: Member — places — Loan

- Reading from Member to Loan: look at the symbols at the Loan end.
  If Loan end shows crow's foot (outer) and circle (inner) → "Each Member places
  zero-or-more Loans."
- Reading from Loan to Member: look at the symbols at the Member end.
  If Member end shows line (outer) and line (inner) → "Each Loan is placed by exactly
  one Member."

> ECBA Exam Tip: The direction you read matters. Always start at one entity and read
> toward the other, using the symbols at the destination end. Never read both ends from
> the same starting point.

---

### Section 3: Cardinality Types

#### One-to-One (1:1)

Each instance of Entity A is associated with at most one instance of Entity B, and each
instance of Entity B is associated with at most one instance of Entity A.

LMS Example: Member — has — LibraryCard (each member has exactly one card; each card
belongs to exactly one member).

Design implication: Consider whether A and B should be the same entity. If the attributes
of A and B are always together and there is always exactly one of each, they can often be
merged.

#### One-to-Many (1:N)

Each instance of Entity A is associated with zero, one, or many instances of Entity B,
but each instance of Entity B is associated with exactly one instance of Entity A.

LMS Examples:

- Genre — contains — Book (one genre contains many books; each book belongs to one genre)
- Member — places — Loan (one member places many loans; each loan belongs to one member)
- Book — has copies — BookCopy (one book has many copies; each copy is of one book)

This is the most common relationship type in business data models.

#### Many-to-Many (M:N)

Each instance of Entity A can be associated with many instances of Entity B, and each
instance of Entity B can be associated with many instances of Entity A.

LMS Example: Member — reads — Book (one member reads many books; one book is read by
many members).

Design implication: Many-to-many relationships cannot be directly implemented in a
relational database. They must be resolved by creating an associative entity.

---

### Section 4: Associative Entities — Resolving Many-to-Many

An associative entity (also called a junction entity or bridge table) sits between two
entities that have a many-to-many relationship. It converts the M:N into two one-to-many
relationships.

#### Rules for Associative Entities

- The associative entity has a composite primary key made up of the foreign keys from both
  parent entities
- The associative entity may have additional attributes that belong to the relationship
  itself, not to either parent
- Both parent entities now have a one-to-many relationship with the associative entity

#### LMS Example — Resolving Member-Book Many-to-Many

Before resolution:

Member — reads — Book (M:N — cannot be implemented directly)

After resolution with Loan associative entity:

- Member — places — Loan (1:N)
- Loan — involves — BookCopy (N:1)
- Loan has its own attributes: LoanID (PK), CheckOutDate, DueDate, ReturnDate, RenewalCount

The Loan entity makes sense as a real business concept — not just a technical bridge. The
best associative entities represent genuine business objects, not just relationship records.

#### Second LMS Example — BookReservation

Before: Member — reserves — Book (M:N)

After resolution with Reservation associative entity:

- Member — places — Reservation (1:N)
- Reservation — holds — BookCopy (N:1 or N:N depending on whether holds are copy-specific)
- Reservation attributes: ReservationID, RequestDate, HoldNotificationDate, HoldExpiryDate,
  Status

---

### Section 5: Primary Keys and Foreign Keys

#### Primary Key Rules

- Uniquely identifies every instance of an entity
- Never null — every instance must have a value
- Never changes once assigned — stability requirement
- May be a single attribute (simple key) or multiple attributes (composite key)

#### Key Types

| Type | Description | LMS Example |
|---|---|---|
| Natural Key | A real-world value that is inherently unique | ISBN for Book, Email for Member |
| Surrogate Key | System-generated ID with no business meaning | MemberID, LoanID, BookCopyID |
| Composite Key | Two or more attributes combined to form the PK | BookCopy PK = (BookID, CopyNumber) |

Business analysts should be aware that natural keys can change — an email address can
be updated — while surrogate keys are stable. Most production systems use surrogate keys
for stability.

#### Foreign Key Rules

- A foreign key references the primary key of another entity
- The foreign key value must either be null (if the relationship is optional) or match an
  existing primary key value in the referenced entity
- This constraint is called referential integrity

#### LMS Foreign Key Examples

| Table | Foreign Key Column | References |
|---|---|---|
| Loan | MemberID | Member.MemberID |
| Loan | BookCopyID | BookCopy.BookCopyID |
| BookCopy | BookID | Book.BookID |
| Reservation | MemberID | Member.MemberID |
| Book | GenreID | Genre.GenreID |

---

### Section 6: Conceptual vs. Logical Data Models

Business analysts work primarily at the conceptual and logical levels. Physical model
design is typically handled by database architects.

#### Conceptual Data Model

Purpose: Capture the business view of data for stakeholder validation.

Characteristics:

- Shows entities and relationships
- Relationship names are included
- Attributes may be listed but data types are omitted
- Primary keys may be noted but foreign keys are not yet shown
- Technology-independent — no database platform assumptions
- Audience: business stakeholders, project sponsors, domain experts

LMS conceptual model entities: Member, Book, BookCopy, Loan, Reservation, Genre, Librarian.

#### Logical Data Model

Purpose: Precise data specification for database design input.

Characteristics:

- All entities from conceptual model are present
- All attributes listed with data types (VARCHAR, INT, DATE, BOOLEAN)
- All primary keys identified and marked (PK)
- All foreign keys identified and marked (FK)
- Many-to-many relationships resolved with associative entities
- Normalization applied to remove redundancy
- Audience: database designers, developers, data architects

#### Physical Data Model

Purpose: Actual database implementation specification.

Characteristics:

- Table names in target platform conventions
- Column names with platform-specific data types
- Index definitions
- Storage parameters
- Not typically produced by business analysts

---

### Section 7: Weak Entities and Identifying Relationships

A weak entity cannot be uniquely identified by its own attributes alone. Its identity
depends on its relationship to a parent (strong) entity.

#### Identifying a Weak Entity

Test: Can you uniquely identify an instance of this entity without knowing its parent?
If no, it is a weak entity.

LMS Example: BookCopy. CopyNumber 1 exists for thousands of books. A specific copy is
only uniquely identified as "Copy 1 of BookID 4521." So BookCopy is weak relative to Book.

#### Weak Entity Notation

In Crow's Foot notation, weak entities are sometimes drawn with a double-border rectangle.
The identifying relationship is drawn with a double diamond in Chen notation. In practical
Crow's Foot tools, the composite PK annotation (BookID, CopyNumber) communicates the
dependency without special symbols.

Common weak entities in business domains:

- OrderLineItem (weak relative to Order)
- InvoiceLine (weak relative to Invoice)
- BookCopy (weak relative to Book)
- AppointmentSlot (weak relative to ProviderSchedule)

---

### Section 8: Complete LMS Logical ERD — Element Inventory

The following table documents all entities, their primary keys, and their relationships
in the LMS logical data model.

| Entity | PK | Key Attributes | Relationships |
|---|---|---|---|
| Member | MemberID | LastName, Email, Status, ExpiryDate | Places Loans, Places Reservations |
| Book | BookID | ISBN, Title, Author, GenreID (FK) | Has BookCopies, Belongs to Genre |
| BookCopy | BookCopyID | BookID (FK), CopyNumber, Condition | Involved in Loans, Holds |
| Genre | GenreID | GenreName, Description | Contains Books |
| Loan | LoanID | MemberID (FK), BookCopyID (FK), CheckOutDate, DueDate, ReturnDate | Placed by Member, Involves BookCopy |
| Reservation | ReservationID | MemberID (FK), BookID (FK), RequestDate, Status, ExpiryDate | Placed by Member, Holds Book |
| Librarian | LibrarianID | LastName, Email, StaffID | Processes Loans |

---

### Section 9: ECBA Exam Preparation

#### BABOK Alignment

Data modeling is listed in the BABOK Guide v3 under Requirements Analysis and Design
Definition as a technique for specifying data requirements. The ECBA exam tests recognition
of ERD notation, cardinality identification, and understanding of entity vs. attribute
distinctions.

#### Likely ECBA Question Patterns

- Given a business rule, identify the correct cardinality notation
- Identify whether an M:N relationship requires an associative entity
- Identify the primary key type (natural vs. surrogate) for a given entity
- Distinguish between a conceptual and a logical data model
- Identify which element in a diagram is incorrectly modeled

---

### Study Checklist

Work through each item before attempting the quiz.

- [ ] Can you draw all six Crow's Foot endpoint symbols from memory?
- [ ] Can you read a relationship in both directions and produce two complete sentences?
- [ ] Can you identify the correct cardinality type for a given business rule?
- [ ] Can you recognize a many-to-many relationship and create the associative entity?
- [ ] Can you distinguish primary key from foreign key with an LMS example?
- [ ] Can you list three differences between a conceptual and a logical data model?
- [ ] Can you identify a weak entity and explain why it requires a composite key?

---

### Key Terms Glossary

| Term | Definition |
|---|---|
| Associative Entity | Junction entity that resolves a many-to-many relationship |
| Attribute | A property stored about an entity |
| Cardinality | The numeric constraint on instances in a relationship |
| Composite Key | A primary key made of two or more attributes combined |
| Conceptual Model | Technology-independent ERD showing entities and relationships for stakeholder review |
| Crow's Foot | ERD notation using line and three-pronged symbols for cardinality |
| Entity | A thing about which the system stores information |
| Foreign Key | An attribute that references the primary key of another entity |
| Identifying Relationship | Relationship between a weak entity and its parent strong entity |
| Logical Model | Precise ERD with attributes, data types, PKs, FKs, and normalized structure |
| Many-to-Many | Relationship where each A can relate to many B and each B can relate to many A |
| Natural Key | A real-world business value used as the primary key |
| One-to-Many | Relationship where each A relates to many B but each B relates to only one A |
| One-to-One | Relationship where each A relates to at most one B and vice versa |
| Optionality | Whether a relationship is required (mandatory) or not required (optional) |
| Primary Key | Attribute or attributes that uniquely identify each entity instance |
| Referential Integrity | Database rule requiring FK values to match existing PK values |
| Surrogate Key | System-generated identifier with no business meaning |
| Weak Entity | Entity that cannot be uniquely identified without its parent entity |

---

## 10. Supplemental Resources

The following open educational resources extend module content on entity-relationship
modeling and data modeling. All are freely accessible without login or purchase.

1. **Crow's Foot Notation ERD Guide — Lucidchart**
   <https://www.lucidchart.com/pages/er-diagrams>
   Focus: Illustrated walkthrough of Crow's Foot notation symbols, cardinality combinations,
   and step-by-step ERD construction. Directly supports lab Tasks 2 and 3 and reinforces the
   symbol reference tables in this reading guide.

2. **Database Design — Normalization and ERDs — Khan Academy Computing**
   <https://www.khanacademy.org/computing/computer-programming/sql>
   Focus: Free SQL and relational database fundamentals course covering tables, primary keys,
   foreign keys, joins, and referential integrity. Supports understanding of how logical ERD
   decisions translate into relational database structures.

3. **Entity-Relationship Modeling Technique — BABOK Guide Techniques Summary**
   <https://www.iiba.org/standards-and-resources/babok/>
   Focus: Official IIBA BABOK Guide listing of data modeling as a Requirements Analysis and
   Design Definition technique. Reviewing the technique summary reinforces ECBA exam alignment
   and the analyst's role in data modeling versus the database designer's role.

4. **ERD Tutorial with Crow's Foot Notation — Visual Paradigm**
   <https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/>
   Focus: Comprehensive guide to ERD concepts including entities, attributes, relationships,
   associative entities, weak entities, and Crow's Foot vs. Chen notation comparisons.
   Supplements all sections of this reading guide with additional worked examples.

5. **Introduction to Databases — Stanford Online (free audit)**
   <https://online.stanford.edu/courses/soe-ydatabases0005-databases-relational-databases-and-sql>
   Focus: University-level introduction to relational database theory including the relational
   model, entity integrity, referential integrity, and normal forms. Provides the conceptual
   foundation for understanding why ERD design decisions matter at implementation time.

---

*Reading Guide — Module 11 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
