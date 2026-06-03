# Discussion Forum: Module 11 — Entity-Relationship Diagrams and Data Modeling

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Forum Instructions

Post an original response to ONE of the three scenarios below (A, B, or C). Your initial
post must be 175–225 words written in complete sentences. After posting, reply to at least
two classmates who responded to a different scenario. Each peer reply must be at least 60
words and must engage substantively with the classmate's reasoning — not simply agree or
restate their point.

**Due dates:** Initial post due by Thursday 11:59 PM. Peer replies due by Sunday 11:59 PM.

---

### Scenario A — Cardinality Dispute

A team of analysts is modeling a hospital scheduling system. Two analysts disagree on the
cardinality between Doctor and Appointment. Analyst 1 argues the relationship should be
one-to-many: one Doctor can have many Appointments, and each Appointment belongs to
exactly one Doctor. Analyst 2 argues the relationship should be many-to-many: one
Appointment can involve multiple doctors — for example, a surgical procedure where a
surgeon and an anesthesiologist are both required.

Respond to this scenario: Explain how a business analyst should resolve this disagreement.
Describe what questions you would ask stakeholders to determine the correct cardinality.
If Analyst 2 is correct and the relationship is many-to-many, describe the associative
entity you would create to resolve it, including what attributes that associative entity
would carry and why those attributes belong there rather than in Doctor or Appointment.

---

### Sample Response A

This disagreement is a requirements validation issue, not a technical debate. The business
analyst's role is not to pick a side based on intuition but to go back to the stakeholders
with specific, concrete questions that reveal the actual business rules. The questions I
would ask include: Can a single appointment ever require more than one physician to be
formally recorded as participating? Are both the surgeon and anesthesiologist tracked
separately for billing, liability, and outcome reporting purposes? Are there appointment
types that are always single-doctor and others that are always multi-doctor, or is the
rule universal? Does the scheduling system need to show each doctor's individual
appointment load on their calendar?

If stakeholder interviews confirm that multiple doctors can share a single appointment and
that the system must track each doctor's role in each appointment, then Analyst 2 is
correct and a many-to-many relationship exists. I would resolve it by creating an
associative entity called DoctorAppointment or AppointmentProvider with a composite
primary key of (DoctorID, AppointmentID). The associative entity would carry its own
attributes: ProviderRole (for example, Surgeon, Anesthesiologist, or Consulting) and
TimeContributed (if billing is tracked by time per provider). These attributes describe
the specific doctor-appointment relationship instance — they are not properties of the
Doctor alone or the Appointment alone, which is precisely the criterion for placing an
attribute in an associative entity rather than in either parent entity.

---

### Peer Reply Guidance for Scenario A

When replying to a classmate's Scenario A post, consider: Did they identify the right
stakeholder questions, or did they just pick one analyst's answer without eliciting
requirements? Are their proposed associative entity attributes genuinely relationship-level
attributes, or could any of them logically live in Doctor or Appointment? Can you propose
a different attribute that belongs in the associative entity?

---

### Scenario B — Natural Key vs. Surrogate Key

A retail company is building a new customer management system. The development team
debates whether to use CustomerEmail as the primary key for the Customer entity, since
email is unique per customer and has real business meaning. A database architect argues
for using a system-generated CustomerID instead. The business sponsor argues that
CustomerEmail is simpler and avoids adding an extra column.

Respond to this scenario: Explain the trade-offs between natural keys and surrogate keys
as primary keys. Take a position on which type of key is more appropriate for the Customer
entity in this scenario, and defend your position using at least two specific technical or
business risks associated with the alternative you are rejecting. Describe how the choice
of primary key affects the foreign key design in related entities such as Order and
SupportTicket.

---

### Sample Response B

The debate between natural keys and surrogate keys is one of the most important practical
decisions in data modeling, and the stakes extend far beyond the Customer table itself.

A natural key like CustomerEmail has intuitive appeal: it is already unique, it has
business meaning, and it is visible to users without requiring a join. However, natural
keys introduce two serious risks in a production customer management system. First,
natural keys are mutable — email addresses change. If a customer changes their email
address, every Order, SupportTicket, and other child record that uses CustomerEmail as a
foreign key must also be updated. In a large database with millions of records, this
cascading update creates significant performance risk and potential for inconsistency if
the update fails partway through. Second, natural keys assume uniqueness guarantees that
the business environment cannot always provide. Two different individuals may legitimately
share a household email, or a data entry error may create a duplicate that blocks
insertion of a valid customer record.

A surrogate key — CustomerID as a system-generated integer — eliminates both risks. It
never changes, so foreign keys in Order and SupportTicket remain stable for the lifetime
of the record regardless of how many times the customer updates their contact information.
It also decouples identity from business data, allowing the email field to have its own
uniqueness constraint without being burdened with referential integrity duties.

I recommend CustomerID as the primary key. CustomerEmail should carry a unique constraint
as a candidate key but should not be the primary key.

---

### Peer Reply Guidance for Scenario B

When replying to a classmate's Scenario B post, consider: Did they identify the mutability
risk as the core argument against natural keys? Did they address the cascading update
impact on child tables like Order? Do you agree with their final recommendation, or can
you construct a scenario where a natural key might be preferable?

---

### Scenario C — ERD Stakeholder Validation

A business analyst presents a conceptual ERD for a property management system to a group
of property managers and leasing agents. The ERD shows: Property, Unit, Tenant, Lease,
and MaintenanceRequest as entities. The Lease entity has a one-to-many relationship with
Tenant on one side and Unit on the other. A property manager immediately says: "We
sometimes have two tenants on the same lease — like roommates. And sometimes we let a
tenant hold two overlapping short-term leases for different units." The leasing agent adds:
"Also, a maintenance request can be for a whole building, not just one unit."

Respond to this scenario: Identify each business rule correction implied by the
stakeholders' feedback. For each correction, describe the specific change to the ERD —
including which relationships change, what the new cardinality would be, and whether any
new entities need to be added. Explain why this stakeholder validation step is more
valuable when done at the conceptual ERD stage rather than after the physical database
has been built.

---

### Sample Response C

The stakeholder feedback reveals three business rule corrections that must be reflected
in the ERD before design proceeds further.

The first correction addresses the roommate scenario. The original ERD models Lease with
a one-to-many relationship to Tenant — meaning one Lease belongs to one Tenant — but the
property manager confirms that multiple tenants can share one lease. Simultaneously, a
single tenant can hold multiple leases. This makes the Lease-Tenant relationship
many-to-many. To resolve it, I would create an associative entity called LeaseTenant or
TenantLease with a composite primary key of (LeaseID, TenantID). The associative entity
would carry attributes like TenantRole (Primary, Co-signer, Occupant) to distinguish
different types of tenants on the same lease.

The second correction addresses the overlapping leases. The property manager's statement
that a tenant can hold two overlapping leases for different units confirms that one Tenant
can have multiple Leases and one Lease can theoretically involve multiple Tenants as
established above. This is already resolved by the LeaseTenant associative entity.

The third correction addresses maintenance requests. The leasing agent notes that a
request can be for an entire building, not just a unit. The original ERD likely shows a
mandatory one-to-many from Unit to MaintenanceRequest, but this must change to optional —
a maintenance request may or may not be associated with a specific Unit. A new Property
entity relationship to MaintenanceRequest should be added with the appropriate cardinality.

Performing this validation at the conceptual ERD stage is exponentially less costly than
discovering the same errors after physical database construction. Changing a cardinality
in a conceptual diagram takes minutes. Migrating data, altering tables, and updating
application code in a deployed database can take days or weeks and may require a
maintenance window that disrupts users. The conceptual ERD is specifically designed to be
a cheap, high-communication tool for catching exactly these kinds of misunderstandings
before they become expensive structural defects.

---

### Peer Reply Guidance for Scenario C

When replying to a classmate's Scenario C post, consider: Did they correctly identify all
three corrections from the stakeholder feedback? Did they propose a specific associative
entity for the roommate scenario with named attributes? Is their argument for early
validation specific to ERD modeling, or is it a generic statement about early requirements
work? Can you add a concrete cost example to strengthen their argument?

---

### Discussion Rubric

| Criterion | Excellent (10) | Proficient (7) | Developing (4) | Beginning (1) |
|---|---|---|---|---|
| Accuracy of ERD concepts | All cardinality, key, and entity concepts correct | Minor error in one concept | One significant conceptual error | Multiple errors or core concept missing |
| Depth of analysis | Reasoning is specific, scenario-grounded, and anticipates consequences | Some scenario-specific reasoning | Mostly general statements | Restates scenario without analysis |
| Word count and completeness | 175–225 words; all required elements addressed | 150–175 words; most elements present | Under 150 words; one element missing | Under 100 words or major element absent |
| Peer reply quality | Engages with classmate's specific argument; adds new insight | Brief engagement with extension | Agreement without substantive engagement | One sentence or off-topic |
| Writing quality | Professional sentences; no errors | 1–2 minor errors | 3–4 errors affecting clarity | Frequent errors impeding understanding |

---

### Professor Nash Note

For Scenario A, the most important thing I am evaluating is whether you understand that
cardinality is determined by business rules, not by a modeler's preference. Many students
pick one answer and defend it without acknowledging that only stakeholder interviews can
settle the dispute. Show me that you understand the analyst's role: ask the right questions,
document the answers, and let the business rules drive the notation.

For Scenario C, I want to see you address all three pieces of feedback from the two
stakeholders — not just the most obvious one. Each piece of feedback maps to a specific
ERD change, and I expect you to name the change with precision: which relationship,
which cardinality update, and whether a new entity is required.

---

*Discussion Forum — Module 11 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
