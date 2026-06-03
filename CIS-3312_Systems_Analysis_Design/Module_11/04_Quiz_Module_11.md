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
