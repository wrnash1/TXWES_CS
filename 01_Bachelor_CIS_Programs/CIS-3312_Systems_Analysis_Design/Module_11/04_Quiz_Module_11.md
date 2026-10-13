# Quiz: Module 11 — Entity-Relationship Diagrams and Data Modeling

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

In Crow's Foot notation, a relationship line has a crow's foot (three-pronged mark) as
the outer symbol and a circle as the inner symbol at one end. What does this combination
of symbols mean when reading from the opposite entity toward this end?

A. Exactly one — the relationship is mandatory and limited to one instance

B. One or more — at least one instance is required

C. Zero or one — the relationship is optional and at most one instance exists

D. Zero or more — the relationship is optional and any number of instances is allowed

Correct Answer: D

Distractor Analysis:

- A describes the combination of a single vertical line (outer) and a single vertical line
  (inner), which reads as one-and-only-one — mandatory and exactly one.
- B describes a crow's foot (outer) plus a vertical line (inner) — one-or-more, which is
  mandatory many.
- C describes a single vertical line (outer) plus a circle (inner) — zero-or-one, which is
  optional but limited to one.

---

### Question 2

A database analyst proposes modeling "Student" and "Course" as two entities in a university
enrollment system. A student can enroll in many courses, and a course can have many students
enrolled. Which relationship type exists between Student and Course, and what must be done
to implement this in a relational database?

A. One-to-many — add a foreign key in the Course entity referencing the Student primary key

B. One-to-one — merge Student and Course into a single entity since they are so closely
   related

C. Many-to-many — create an associative entity (such as Enrollment) to resolve the
   relationship into two one-to-many relationships

D. Many-to-many — implement it directly in the database using a multi-valued column in the
   Student entity

Correct Answer: C

Distractor Analysis:

- A is incorrect because one-to-many would mean each course belongs to exactly one student,
  which is not the case. Many students can enroll in one course.
- B is incorrect because one-to-one would mean each student is paired with exactly one
  course, which contradicts the requirement.
- D is incorrect because relational databases do not support multi-valued columns as a
  direct implementation of many-to-many relationships. Multi-valued columns violate first
  normal form and create query and maintenance problems.

---

### Question 3

A business analyst is reading an ERD for a hospital system. The relationship between
Doctor and Patient shows: at the Doctor end — a single vertical line (outer) and a single
vertical line (inner); at the Patient end — a crow's foot (outer) and a circle (inner).
Which of the following correctly reads this relationship from the Doctor's perspective?

A. Each Doctor is associated with zero or more Patients

B. Each Doctor is associated with exactly one Patient

C. Each Patient is associated with zero or more Doctors

D. Each Doctor is associated with one or more Patients

Correct Answer: A

Distractor Analysis:

- B incorrectly reads the symbols at the Patient end as if they applied to Doctor. The
  Patient-end symbols (crow's foot + circle = zero-or-more) describe how many Patients
  one Doctor can have.
- C describes the reading from the Patient's perspective, not the Doctor's — "each Patient
  is associated with zero or more Doctors" would require different symbols.
- D would require a crow's foot plus a vertical line (one-or-more) at the Patient end, not
  a crow's foot plus a circle.

---

### Question 4

An analyst is designing a data model for a shipping company. A Shipment contains multiple
ShipmentItems, and each ShipmentItem exists only as part of its parent Shipment.
ShipmentItem has a LineNumber attribute, but LineNumber 1 exists in every shipment — it
is not unique across all shipments. What type of entity is ShipmentItem, and what should
its primary key be?

A. A strong entity; its primary key should be a surrogate ShipmentItemID

B. A weak entity; its composite primary key should be (ShipmentID, LineNumber) because
   its identity depends on the parent Shipment

C. An associative entity; it resolves a many-to-many relationship between Shipment and
   Item

D. A derived entity; its attributes can be calculated from the Shipment entity

Correct Answer: B

Distractor Analysis:

- A is incorrect because while adding a surrogate key would work technically, it misses the
  analytical point: ShipmentItem cannot be identified without Shipment context, making it a
  weak entity. The question tests concept recognition, not just implementation options.
- C is incorrect because ShipmentItem is not resolving a many-to-many between two other
  entities. It is a dependent child entity with a direct parent-child relationship.
- D is incorrect because derived entities are not a standard ERD entity type. Derived
  attributes can be calculated, but entities are not derived.

---

### Question 5

A conceptual ERD for a retail system shows Product and Order as entities with a
relationship named "includes." A junior analyst wants to add UnitPrice as an attribute
of the Product entity. A senior analyst argues that UnitPrice should be an attribute of
an associative entity called OrderLine, not of Product. Who is correct and why?

A. The junior analyst is correct because UnitPrice describes the Product and belongs with
   its other product attributes like name and description.

B. The senior analyst is correct because UnitPrice at the time of purchase may differ from
   the current Product price, and it belongs to the relationship instance — the specific
   OrderLine — not to the Product itself.

C. Both are correct because UnitPrice can be stored in both places without causing data
   problems.

D. Neither is correct because price data belongs in a separate Pricing entity unrelated to
   either Order or Product.

Correct Answer: B

Distractor Analysis:

- A is incorrect because Product.UnitPrice reflects the current listed price, which may
  change over time. An order placed six months ago was charged at the price valid then,
  not the current price. Storing price only in Product loses historical accuracy.
- C is incorrect because storing UnitPrice in both places creates a data redundancy and
  update anomaly — if the Product price changes, does the OrderLine price also change?
  The two values would become inconsistent.
- D is incorrect because while a Pricing history entity is a reasonable advanced design
  choice, the core analytical answer is that UnitPrice belongs in the relationship instance
  (OrderLine), not in the Product entity.

---

### Question 6

Which of the following best describes the difference between a conceptual data model and a
logical data model?

A. A conceptual model is drawn by hand while a logical model uses software tools.

B. A conceptual model shows entities and relationships without attributes or keys,
   targeting business stakeholder review; a logical model adds attributes, data types,
   primary keys, and foreign keys for use by database designers.

C. A conceptual model includes normalization while a logical model uses denormalization
   for performance.

D. A conceptual model is for current-state documentation while a logical model represents
   the future-state design.

Correct Answer: B

Distractor Analysis:

- A is incorrect because the distinction between conceptual and logical models is based on
  content and audience, not on how the diagram is drawn or what tool is used.
- C reverses the actual relationship. Normalization is applied during logical modeling;
  denormalization is sometimes applied at the physical level for performance, not at the
  conceptual level.
- D is incorrect because both conceptual and logical models can represent either current-
  state or future-state data structures. The levels of abstraction are independent of the
  As-Is/To-Be dimension.

---

### Question 7

A library data model has a Member entity with a primary key of MemberID. The Loan entity
has a foreign key column also named MemberID. A new loan record is inserted with
MemberID = 7749, but no member with MemberID = 7749 exists in the Member table. What
database constraint does this violate?

A. Entity integrity — primary keys may not contain null values

B. Domain integrity — the data type of MemberID in Loan does not match the Member table

C. Referential integrity — a foreign key value must match an existing primary key value in
   the referenced table

D. Uniqueness constraint — MemberID values must be unique across both the Member and Loan
   tables

Correct Answer: C

Distractor Analysis:

- A is incorrect because entity integrity prohibits null primary key values; this scenario
  involves a non-null foreign key value that has no matching parent record — a different
  type of violation.
- B is incorrect because the scenario does not describe a data type mismatch; domain
  integrity violations involve wrong data types or values outside a defined range.
- D is incorrect because foreign key values are not required to be unique — a member can
  have many loans, all with the same MemberID value. Only primary keys have uniqueness
  constraints.

---

### Question 8

An analyst draws an ERD for an airline reservation system. The relationship between
Flight and Passenger shows a many-to-many cardinality. The analyst proposes resolving
this with an associative entity called Booking. Which attributes would most logically
belong in the Booking entity rather than in Flight or Passenger?

A. FlightNumber and DepartureCity — because these describe the flight

B. PassengerName and PassportNumber — because these describe the passenger

C. SeatNumber, BookingDate, and TicketPrice — because these describe the specific
   booking instance, not the flight or passenger independently

D. AircraftType and TotalSeats — because these are needed to process the booking

Correct Answer: C

Distractor Analysis:

- A is incorrect because FlightNumber and DepartureCity are attributes of the Flight
  entity. They describe the flight as a whole, not any specific booking.
- B is incorrect because PassengerName and PassportNumber are attributes of the Passenger
  entity. They identify the traveler, not their booking.
- D is incorrect because AircraftType and TotalSeats are attributes of the Flight or
  Aircraft entity. They describe the aircraft capacity, not the passenger-flight
  relationship.

---

### Question 9

An ERD for a school system shows a Student entity and a Parent entity. The business rule
states: every student must have at least one parent on record, and a parent may have one
or more students in the school. Which Crow's Foot notation correctly represents the
relationship at the Student end of the Student-Parent relationship line, when reading
from Parent toward Student?

A. Circle (inner) and single line (outer) — zero-or-one

B. Single line (inner) and crow's foot (outer) — one-or-more

C. Circle (inner) and crow's foot (outer) — zero-or-more

D. Single line (inner) and single line (outer) — one-and-only-one

Correct Answer: B

Distractor Analysis:

- A would mean each parent has at most one student, which contradicts the rule allowing
  one or more students per parent.
- C would mean a parent can have zero students, but the rule states a parent in this
  system has one or more students enrolled (they are on record because they have a
  student in the school).
- D would mean each parent has exactly one student, which contradicts the one-or-more
  rule.

---

### Question 10

A business analyst is presenting an ERD to a group of stakeholders who have no database
background. The analyst reads the relationship between Member and Loan as: "Each Member
places zero-or-more Loans" and "Each Loan is placed by exactly one Member." A stakeholder
responds: "Actually, we allow joint accounts where two family members share one loan
record." How should the analyst respond?

A. Ignore the feedback because ERDs are technical documents not subject to stakeholder
   revision.

B. Update the ERD to change the relationship cardinality at the Member end of Loan from
   one-and-only-one to many, and discuss whether a new associative entity is needed to
   model the joint account relationship.

C. Accept the feedback but do not change the ERD — note it in the meeting minutes instead.

D. Replace the Loan entity with a JointLoan entity to accommodate the new requirement.

Correct Answer: B

Distractor Analysis:

- A is incorrect because stakeholder validation of ERDs is one of the primary purposes of
  presenting conceptual and logical models to business stakeholders. Feedback that reveals
  a modeling gap must be addressed.
- C is incorrect because meeting notes do not update requirements documentation. The ERD
  must be revised to reflect confirmed business rules.
- D is incorrect because creating a separate JointLoan entity would complicate the model
  unnecessarily. The correct approach is to revise the cardinality of the existing
  relationship and assess whether an associative entity (such as LoanMember) is the right
  resolution for the many-to-many that now exists between Member and Loan.

---

*Quiz — Module 11 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

---

### Question 11

A business analyst is reviewing a proposed ERD and notices that the Author entity has
attributes AuthorID (PK), FirstName, LastName, and Bio. The Book entity has a separate
AuthorID (FK) column. The relationship line shows each Book associated with exactly one
Author, and each Author associated with one-or-more Books. A stakeholder points out that
some books have two or three co-authors. What change is required to the data model?

A. Add a CoAuthor1 and CoAuthor2 column to the Book entity to store additional authors

B. Remove the Author entity and store author names as a comma-separated list in the
   Book.Author column

C. Change the Book-Author relationship to many-to-many and introduce an associative
   entity (such as BookAuthor) to store the authorship role and sequence order

D. Create separate entity types PrimaryAuthor and SecondaryAuthor, each with a one-to-
   many relationship to Book

Correct Answer: C

Distractor Analysis:

- A is incorrect because adding fixed-count columns (CoAuthor1, CoAuthor2) fails when a
  book has more co-authors than the columns accommodate. This is a repeating group that
  violates first normal form.
- B is incorrect because storing multiple values in a single column (comma-separated list)
  violates first normal form and makes individual author queries, sorts, and joins
  impossible without string parsing.
- D is incorrect because separating authors into PrimaryAuthor and SecondaryAuthor entities
  creates maintenance complexity and still fails for books with three or more authors. It
  also forces a business distinction that may not always apply.

---

### Question 12

In a Crow's Foot ERD, what does a circle symbol at the inner position of a relationship
endpoint signify?

A. The relationship is mandatory — at least one instance must exist

B. The relationship is optional — zero instances are allowed

C. The relationship is many — multiple instances are expected

D. The relationship is a primary key reference

Correct Answer: B

Distractor Analysis:

- A describes the single vertical line at the inner position, which signals that the
  relationship is mandatory and at least one instance must participate.
- C describes the outer crow's foot symbol, which signals multiplicity (many). The inner
  symbol governs minimum participation (optionality), not maximum.
- D is incorrect because primary key references are communicated through (PK) attribute
  annotations and foreign key columns, not through relationship endpoint symbols.

---

### Question 13

A university data model includes a Course entity and a Section entity. The narrative
states: "Each Course may be offered as one or more Sections per semester; a Section cannot
exist without being associated with a Course." What type of entity is Section relative to
Course, and what is the correct cardinality at the Section end of the Course-Section
relationship line?

A. Section is a strong entity; the Section end shows zero-or-more (crow's foot + circle)

B. Section is a weak entity; the Section end shows one-or-more (crow's foot + line)
   because a Section must belong to exactly one Course and at least one Section is required

C. Section is an associative entity; the Section end shows many-to-many cardinality

D. Section is a weak entity; the Course end shows one-or-more (crow's foot + line)

Correct Answer: B

Distractor Analysis:

- A is incorrect because Section cannot be identified without its parent Course (a section
  number like "001" exists across many courses), making it a weak entity, not a strong one.
  The crow's foot + circle would mean zero or more sections, but the narrative says one or
  more sections per course.
- C is incorrect because Section is not an associative entity resolving a many-to-many. It
  is a dependent child entity of Course.
- D misreads the direction. The symbols at an endpoint describe how many of that entity are
  associated with one instance of the opposite entity. The crow's foot belongs at the
  Section end (one Course has many Sections), not at the Course end.

---

### Question 14

An analyst proposes using a natural key — specifically, the ISBN — as the primary key for
the Book entity in the LMS data model. A colleague argues for a surrogate key (BookID).
Which statement best supports the surrogate key argument?

A. ISBNs are too long to display in a user interface, making them impractical as keys

B. ISBN values can theoretically be reassigned by publishers when a book is reissued with
   significant revisions, and the system would need to update all foreign key references
   if the ISBN changes — surrogate keys avoid this cascade problem

C. Surrogate keys are required by BABOK Guide standards for all entity primary keys

D. ISBNs are not unique — two different books can share the same ISBN

Correct Answer: B

Distractor Analysis:

- A is incorrect because primary keys do not need to be displayed in the user interface.
  The display identifier (ISBN or title) can differ from the internal primary key.
- C is incorrect because BABOK does not prescribe surrogate versus natural key choices.
  This is a data modeling design decision, not a BABOK mandate.
- D is incorrect because ISBNs are designed to be globally unique identifiers. Duplicate
  ISBNs represent data entry errors, not a structural problem with the ISBN standard.

---

### Question 15

A logical ERD for a hospital system shows a Patient entity and a Physician entity. A
business rule states: "Each patient is assigned to exactly one primary care physician.
A physician may have zero patients in the system initially." A second business rule adds:
"A patient may also have referrals to zero or more specialist physicians." How many
separate relationships are needed, and what cardinality does each require?

A. One relationship — Patient-Physician — with many-to-many cardinality resolved by a
   single associative entity

B. Two relationships: Patient-PrimaryPhysician (each Patient has exactly one, each
   Physician has zero-or-more) and Patient-Specialist modeled through a separate
   Referral associative entity

C. One relationship — Patient-Physician — with one-to-one cardinality because each
   patient has only one physician

D. Two relationships both using one-to-many cardinality, with no associative entity needed

Correct Answer: B

Distractor Analysis:

- A is incorrect because collapsing primary care and specialist referrals into one
  many-to-many relationship loses the business distinction between the two physician roles
  and the different business rules that govern each.
- C is incorrect because the one-to-one reading ignores the second business rule about
  specialist referrals entirely, and it also misrepresents the primary care rule (each
  physician has many patients, not one).
- D is incorrect because the specialist referral relationship is many-to-many (a patient
  can have multiple specialist referrals, and one specialist can receive referrals from
  many patients), which requires an associative entity, not a direct one-to-many line.

---

### Question 16

A business analyst is building a logical ERD and notices that the Customer entity contains
a PhoneNumbers attribute that can hold multiple values — a customer may have a home phone,
a mobile phone, and a work phone. What is the correct way to handle this in a relational
data model?

A. Store all phone numbers in a single VARCHAR column separated by semicolons

B. Add three columns to Customer: HomePhone, MobilePhone, WorkPhone

C. Create a separate CustomerPhone entity with a composite or surrogate key, a PhoneType
   attribute, and a foreign key referencing Customer.CustomerID

D. Make PhoneNumbers a derived attribute calculated from a separate lookup table

Correct Answer: C

Distractor Analysis:

- A violates first normal form by storing multiple values in a single column. This makes
  it impossible to query or validate individual phone numbers without string manipulation.
- B uses a fixed set of columns for a variable set of values. If a customer has four phone
  numbers, or if phone type categories change, the structure fails without schema changes.
- D is incorrect because phone numbers are not derived — they are stored facts about a
  customer, not calculated values. Derived attributes are computed from other attributes
  already in the model (such as Age derived from BirthDate).

---

### Question 17

An analyst reviews an ERD for a project management system. The relationship between Project
and Employee shows the business rule: "A project must have at least one employee assigned,
and an employee may be assigned to zero or more projects." An intern has drawn both
endpoints with crow's foot symbols. What error has the intern made, and what is the correct
fix?

A. The intern is correct — both entities participate in the many side, so both get crow's
   foot symbols

B. The Project end should show one-or-more (crow's foot + line), but the Employee end
   should show a line (outer) and circle (inner) — zero-or-one — because employees have
   limited assignments

C. The Project end should show a line (outer) and line (inner) — one-and-only-one —
   because the project is mandatory; the Employee end should show crow's foot + circle
   for zero-or-more

D. The cardinality is many-to-many, which cannot be shown directly; an associative entity
   called ProjectAssignment is needed, with the Project side one-or-more and the Employee
   side zero-or-more

Correct Answer: D

Distractor Analysis:

- A is incorrect because crow's foot symbols at both ends of a direct relationship line
  represent a many-to-many, which cannot be directly implemented in a relational database.
  The intern's error is not in the symbol choice but in leaving the M:N unresolved.
- B is incorrect because the business rule states employees can be assigned to zero or more
  projects — not zero or one. The zero-or-one notation would mean each employee has at
  most one project assignment.
- C describes the cardinality in the wrong direction. The rule says a project needs at
  least one employee (one-or-more employees per project), not that the project relates to
  exactly one employee.

---

### Question 18

Which of the following scenarios describes a violation of referential integrity?

A. A Member row has a null value in the Phone column

B. A Loan row has a MemberID value of 5001, but no row with MemberID = 5001 exists in
   the Member table

C. Two Loan rows have the same MemberID value of 3312

D. A Book row has a Title column that contains a numeric value

Correct Answer: B

Distractor Analysis:

- A describes a null value in a non-key column. Null in optional attributes (Phone may not
  be known) is permitted and does not violate referential integrity. Entity integrity
  would be violated only if a primary key were null.
- C is not a violation — multiple loans belonging to the same member is the expected and
  correct behavior in a one-to-many relationship. Referential integrity requires FK values
  to match a PK, not to be unique.
- D describes a domain integrity issue (wrong data type in a column), not a referential
  integrity violation. Referential integrity specifically governs foreign key to primary
  key relationships across tables.

---

### Question 19

An analyst is presented with the following entity description: "An invoice line item
represents one product on one invoice. Its line number (1, 2, 3…) is unique within the
invoice but not globally. It cannot exist without its parent invoice." What are the
correct primary key and entity classification for InvoiceLine?

A. Strong entity; primary key = LineNumber alone, since it is unique within the invoice

B. Weak entity; composite primary key = (InvoiceID, LineNumber) because the entity's
   identity depends on the parent Invoice

C. Associative entity; it resolves a many-to-many between Invoice and Product

D. Strong entity; primary key = a system-generated InvoiceLineID surrogate key, making
   it independent of Invoice

Correct Answer: B

Distractor Analysis:

- A is incorrect because LineNumber is not globally unique — the same LineNumber value
  exists in every invoice. A primary key must uniquely identify each row across the entire
  table, not just within a subset.
- C is incorrect because InvoiceLine is not an associative entity resolving an M:N. It
  is a dependent child of Invoice. An associative entity would bridge two independent
  parent entities in a many-to-many relationship.
- D is technically implementable in a database, but it misidentifies the entity
  classification. Using a surrogate key does not change the fact that InvoiceLine is
  conceptually a weak entity whose identity is derived from Invoice.

---

### Question 20

A conceptual ERD for the LMS shows a Genre entity and a Book entity connected by a
relationship line. The analyst needs to select the correct cardinality. The library
requires that every book be classified into exactly one genre, and that a genre may
exist in the catalog even if no books have been assigned to it yet. Which Crow's Foot
notation correctly represents the Genre end of the Genre-Book relationship line when
reading from Book toward Genre?

A. Crow's foot (outer) and circle (inner) — zero-or-more

B. Single line (outer) and single line (inner) — one-and-only-one

C. Crow's foot (outer) and line (inner) — one-or-more

D. Single line (outer) and circle (inner) — zero-or-one

Correct Answer: B

Distractor Analysis:

- A would mean each book belongs to zero or more genres, contradicting the rule that every
  book must belong to exactly one genre.
- C would mean each book belongs to one or more genres, again allowing multiple genre
  memberships per book, which contradicts the single-genre rule.
- D would mean each book belongs to zero or one genre, allowing a book to have no genre
  classification. The business rule states every book must be classified into exactly one
  genre, so zero is not permitted — making the relationship mandatory.

---

*Quiz — Module 11 (extended) | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
