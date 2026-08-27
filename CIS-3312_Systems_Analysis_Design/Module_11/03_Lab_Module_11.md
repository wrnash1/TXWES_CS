# Lab Activity: Module 11 — Entity-Relationship Diagrams and Data Modeling

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Lab Overview

In this lab you will build a complete data model for the Lakewood Community Library
Management System, progressing from a conceptual ERD to a logical ERD. You will identify
entities, define attributes, specify relationships with Crow's Foot cardinality notation,
resolve many-to-many relationships, and document primary and foreign key assignments. You
will also analyze a provided problem description to identify all entities and relationships
independently before modeling.

**Estimated time:** 2.5–3 hours

**Tools allowed:** draw.io (free at app.diagrams.net — use the Entity Relation shape
library), Lucidchart free tier, MySQL Workbench (EER diagram mode), or hand-drawn and
photographed. All notation must use Crow's Foot symbols — not Chen notation diamonds.

---

### Case Study: Lakewood LMS — Data Requirements

The following narrative describes the data the LMS must store. Read it carefully and
identify all entities before beginning Task 1.

#### Data Narrative

The library maintains records for all registered members. Each member has a unique member
ID, a first name, last name, email address, phone number, home address (street, city,
state, and ZIP code), membership status (Active, Suspended, or Expired), and a membership
expiry date. Members may borrow physical books and other materials from the library.

The library's collection consists of books, each of which has a unique ISBN, a title, one
or more authors, a publisher, a publication year, and a genre classification. The library
may own multiple physical copies of the same book. Each physical copy has a copy number
that distinguishes it from other copies of the same title. Each copy also has a condition
rating (New, Good, Fair, Poor) and a current availability status (Available, Checked Out,
On Hold, Lost).

When a member borrows a book copy, the system records a loan transaction. Each loan has
a system-generated loan ID, a check-out date, a due date, an actual return date (null
until returned), and a renewal count. A member can borrow many book copies over time, and
a single book copy can be borrowed by many members over its lifetime.

Members can reserve a book title when all copies are currently checked out. A reservation
has a system-generated reservation ID, the date the reservation was requested, the date a
hold notification was sent (if applicable), the hold expiry date (7 days from notification),
and a reservation status (Pending, Notified, Fulfilled, Cancelled, Expired). One member can
have multiple active reservations, and one book title can have multiple reservations from
different members.

The library organizes its collection into genres. Each genre has a genre ID and a genre
name. A book belongs to exactly one genre, and a genre can contain many books.

Librarians are staff members who process in-person check-out and return transactions. Each
librarian has a librarian ID, first name, last name, staff email, and a hire date. The
system records which librarian processed each in-person loan transaction to support
accountability reporting.

Late fees accrue when a book is returned after its due date. Each late fee record has a
fee ID, the calculated amount, the date the fee was assessed, and a paid status. A late
fee is associated with exactly one loan, and each loan may have at most one late fee.

---

### Task 1: Entity Identification (10 points)

Before drawing any diagrams, complete the entity identification worksheet below.

#### Step 1 — List All Entities

From the data narrative above, list every entity you can identify. For each entity, write
one sentence justifying its inclusion (why does it meet the criteria for an entity?).

Minimum required entities:

- Member
- Book
- BookCopy
- Genre
- Loan
- Reservation
- Librarian
- LateFee

For each entity, answer: Can it have multiple instances? Can it be uniquely identified?
Does it have attributes beyond just an identifier?

#### Step 2 — Identify Relationship Candidates

For each pair of entities that interact in the narrative, write a preliminary relationship
statement: "[Entity A] [verb] [Entity B]." Do not add cardinality yet — just name the
relationships you see.

Submit your entity list and relationship statements as a written document before beginning
the diagramming tasks.

---

### Task 2: Conceptual ERD (20 points)

Create a conceptual entity-relationship diagram for the LMS.

#### Requirements for the Conceptual ERD

- Show all eight entities as labeled rectangles
- Show all relationships as labeled lines between entities — use verb phrases
- Do not list attributes inside entity boxes (conceptual level only)
- Do not add cardinality symbols yet
- Use a layout that minimizes crossing lines

#### Suggested Layout

Place entities in a logical spatial arrangement. One approach: center Loan and Reservation
in the middle of the diagram because they are associative entities with connections to
multiple other entities. Place Member and Librarian on the left. Place Book, BookCopy, and
Genre on the right. Place LateFee below Loan.

#### Relationship Names to Include

Use these verb phrases to name each relationship line:

- Member — places — Loan
- Member — makes — Reservation
- Librarian — processes — Loan
- Book — has copies — BookCopy
- Book — belongs to — Genre
- Book — subject of — Reservation
- BookCopy — involved in — Loan
- Loan — incurs — LateFee

---

### Task 3: Logical ERD with Crow's Foot Notation (45 points)

Refine the conceptual ERD into a full logical ERD with attributes, primary keys, foreign
keys, and Crow's Foot cardinality notation.

#### Step 1 — Add Attributes to All Entities

Add all attributes to each entity box. Mark primary keys with (PK) and foreign keys with
(FK). Use the following attribute specifications:

Member entity attributes:

- MemberID (PK) — INT, surrogate key
- FirstName — VARCHAR(50)
- LastName — VARCHAR(50)
- Email — VARCHAR(100), unique
- Phone — VARCHAR(15)
- Street — VARCHAR(100)
- City — VARCHAR(50)
- State — CHAR(2)
- ZIP — CHAR(10)
- MembershipStatus — VARCHAR(10) — Active, Suspended, Expired
- ExpiryDate — DATE

Book entity attributes:

- BookID (PK) — INT, surrogate key
- ISBN — VARCHAR(13), unique
- Title — VARCHAR(200)
- Author — VARCHAR(200)
- Publisher — VARCHAR(100)
- PublicationYear — YEAR
- GenreID (FK) — INT, references Genre.GenreID

BookCopy entity attributes:

- BookCopyID (PK) — INT, surrogate key
- BookID (FK) — INT, references Book.BookID
- CopyNumber — INT
- Condition — VARCHAR(10) — New, Good, Fair, Poor
- AvailabilityStatus — VARCHAR(15) — Available, CheckedOut, OnHold, Lost

Genre entity attributes:

- GenreID (PK) — INT, surrogate key
- GenreName — VARCHAR(50)
- Description — VARCHAR(200)

Loan entity attributes:

- LoanID (PK) — INT, surrogate key
- MemberID (FK) — INT, references Member.MemberID
- BookCopyID (FK) — INT, references BookCopy.BookCopyID
- LibrarianID (FK) — INT, references Librarian.LibrarianID, nullable
- CheckOutDate — DATE
- DueDate — DATE
- ReturnDate — DATE, nullable
- RenewalCount — INT, default 0

Reservation entity attributes:

- ReservationID (PK) — INT, surrogate key
- MemberID (FK) — INT, references Member.MemberID
- BookID (FK) — INT, references Book.BookID
- RequestDate — DATE
- NotificationDate — DATE, nullable
- HoldExpiryDate — DATE, nullable
- ReservationStatus — VARCHAR(15) — Pending, Notified, Fulfilled, Cancelled, Expired

Librarian entity attributes:

- LibrarianID (PK) — INT, surrogate key
- FirstName — VARCHAR(50)
- LastName — VARCHAR(50)
- StaffEmail — VARCHAR(100)
- HireDate — DATE

LateFee entity attributes:

- FeeID (PK) — INT, surrogate key
- LoanID (FK) — INT, references Loan.LoanID
- FeeAmount — DECIMAL(8,2)
- AssessmentDate — DATE
- PaidStatus — BOOLEAN, default false

#### Step 2 — Add Crow's Foot Cardinality Notation

Add Crow's Foot symbols to every relationship line. Use the following business rules to
determine the correct notation:

Business rules to encode:

1. A Member can place zero or more Loans over their membership. Each Loan belongs to
   exactly one Member.
2. A Member can make zero or more Reservations. Each Reservation is made by exactly one
   Member.
3. A Librarian can process zero or more Loans. Each in-person Loan may be processed by
   a Librarian or may have no Librarian (self-checkout) — the relationship is optional
   on the Loan side.
4. A Book has one or more BookCopies (at least one copy must exist). Each BookCopy belongs
   to exactly one Book.
5. A Genre contains zero or more Books. Each Book belongs to exactly one Genre.
6. A Book can be the subject of zero or more Reservations. Each Reservation is for exactly
   one Book.
7. A BookCopy can be involved in zero or more Loans over time. Each Loan involves exactly
   one BookCopy.
8. A Loan may incur zero or one LateFee. Each LateFee belongs to exactly one Loan.

#### Step 3 — Verify Referential Integrity

For each foreign key in your logical ERD, write one sentence confirming the referential
integrity constraint it enforces. Example: "Loan.MemberID must match an existing value in
Member.MemberID, ensuring a loan cannot be recorded for a non-existent member."

Submit eight referential integrity statements — one per foreign key relationship.

---

### Task 4: Cardinality Analysis — Business Rule Derivation (15 points)

The following business rules describe proposed changes to the LMS. For each rule, state how
it would change the cardinality notation in the logical ERD and draw the updated endpoint
symbols for the affected relationship.

#### Business Rule Change A

The library decides that a book copy can now be donated directly by patrons and may exist
in the catalog before it has been physically processed by a librarian. During the processing
period, a BookCopy may temporarily have no associated Book record if the ISBN is not yet
confirmed. How does this change the Book-to-BookCopy relationship on the BookCopy side?

#### Business Rule Change B

Library policy changes so that every loan transaction — including self-checkout — must be
associated with a Librarian account for accountability. Anonymous or kiosk-based loans
will use a special system Librarian account rather than having a null LibrarianID.
How does this change the Librarian-to-Loan relationship on the Loan side?

#### Business Rule Change C

The library introduces a new Book Club feature. A Book Club is a named group of members
who share a reading list. One member can belong to many book clubs and one book club can
have many members. Identify the correct cardinality type for the Member-BookClub
relationship and describe the associative entity that would need to be created to resolve
it in the relational model.

---

### Submission Checklist

Before submitting, verify:

- [ ] Entity identification worksheet lists all eight required entities with justifications
- [ ] Conceptual ERD shows all entities and named relationships without attributes
- [ ] Logical ERD includes all entities with complete attribute lists
- [ ] All primary keys are marked (PK) and foreign keys are marked (FK)
- [ ] Crow's Foot symbols are drawn at both ends of every relationship line
- [ ] Eight referential integrity statements are present
- [ ] All three business rule change analyses are answered
- [ ] All files named with LastName prefix

---

### Grading Rubric

| Task | Criteria | Points |
|---|---|---|
| Task 1 — Entity Identification | All 8 entities identified with justification (5) | 5 |
| | Relationship candidates listed as verb phrases (5) | 5 |
| | Subtotal | **10** |
| Task 2 — Conceptual ERD | All 8 entities present as labeled rectangles (5) | 5 |
| | All 8 relationships named with verb phrases (10) | 10 |
| | Clean layout with minimal crossing lines (5) | 5 |
| | Subtotal | **20** |
| Task 3 — Logical ERD | All attributes present with correct PK/FK marking (15) | 15 |
| | Crow's Foot notation correct on all 8 relationships (20) | 20 |
| | 8 referential integrity statements correct (10) | 10 |
| | Subtotal | **45** |
| Task 4 — Cardinality Analysis | Rule A: correct notation change identified (5) | 5 |
| | Rule B: correct notation change identified (5) | 5 |
| | Rule C: M:N identified, associative entity described (5) | 5 |
| | Subtotal | **15** |
| **Total** | | **90** |

Note: Task 3 referential integrity statements are worth 10 points and are part of the
Task 3 subtotal. Total is 90 points; the remaining 10 points come from lab participation
credit awarded by the instructor for submitting all required components on time.

---

### Professor Nash Note

The most common error in this lab is forgetting to add the optionality (inner) symbol and
only drawing the maximum cardinality (outer) symbol. Both symbols are required at each
end of every relationship line. A relationship line showing only a crow's foot without the
accompanying circle or line for optionality is incomplete and will lose points. Review the
Crow's Foot symbol table in the Reading Guide and apply it systematically to each of the
eight business rules before finalizing your diagram.

---

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced data
modeling practice aligned with ECBA exam competencies.

### Challenge Step 1: Extended ERD with Author and Fine History Entities

The current LMS logical ERD models Author data as a single VARCHAR attribute on the Book
entity. Extend the model to treat Author as a full entity. Design an Author entity with
appropriate attributes (AuthorID, FirstName, LastName, Bio, Nationality). Then model the
relationship between Author and Book correctly, accounting for the fact that a book can
have multiple co-authors and an author can write multiple books. Identify the correct
cardinality, determine whether an associative entity is needed, and specify what attributes
(if any) belong in the associative entity rather than in Author or Book. Draw the updated
ERD fragment showing Author, BookAuthor (if needed), and Book with full Crow's Foot
notation. Write two sentences explaining how this change affects the existing Loan and
Reservation entities — do any foreign keys change?

### Challenge Step 2: Third Normal Form Analysis

Take the logical ERD you produced in Task 3 and perform a third normal form (3NF) analysis
on two of the entities. For each entity, list all non-key attributes and determine whether
any non-key attribute depends on another non-key attribute rather than on the primary key.
If a transitive dependency exists, describe the decomposition required to eliminate it and
show the resulting entities. Then explain in one paragraph why removing transitive
dependencies matters from a business analysis perspective — specifically, what data quality
problems can arise if a logical ERD is implemented with transitive dependencies left in
place. Use the Member entity (with its address fields) and the Book entity (with its
PublicationYear and Publisher fields) as your two analysis targets.

### Challenge Step 3: ERD to Data Dictionary Crosswalk

Select four entities from your completed logical ERD (Member, Loan, Book, and one of your
choice). For each entity, create a data dictionary entry that lists every attribute with:
the attribute name, data type, whether it is PK or FK, whether null is allowed, the
business meaning in one sentence, and any validation constraints (value ranges, allowed
values, format rules). Present the entries in a table. Then write a one-paragraph
explanation of how the data dictionary and the ERD work together as paired artifacts —
specifically, what information is conveyed by the ERD that is not in the data dictionary,
and what information is in the data dictionary that cannot be expressed in the ERD diagram
itself. This exercise develops the documentation skills that BAs use when handing off data
requirements to database designers.

---

*Lab Activity — Module 11 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
