# Lab Activity: Module 10 — Data Flow Diagrams and System Models

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Lab Overview

In this lab you will construct a complete leveled DFD set for the Lakewood Community
Library Management System using Yourdon-Coad notation. You will build a context diagram,
a Level 1 DFD, and a Level 2 DFD for one selected process. You will then perform a
balancing check and identify errors in a provided diagram fragment.

**Estimated time:** 2.5–3 hours

**Tools allowed:** draw.io (free at app.diagrams.net), Lucidchart free tier, Microsoft
Visio, or hand-drawn and photographed. All DFD shapes must follow Yourdon-Coad notation:
circles for processes, squares for external entities, open rectangles for data stores.
Do not use flowchart shapes.

---

### Case Study: Lakewood Community Library Management System

You have already been introduced to the LMS case study in previous modules. For this lab,
focus on the following system scope description and the data requirements it implies.

#### System Scope

The Lakewood LMS must support the following functions:

- Member registration and account management (new members, account updates, suspensions)
- Online catalog search (by title, author, ISBN, genre)
- Book check-out and return processing
- Loan renewal (online and at-desk)
- Book reservation (holds) with automated hold notifications
- Overdue management (identifying overdue loans, generating overdue notices)
- Reporting (overdue items list, circulation statistics, membership summary)

#### Data in the System

The LMS stores and manages the following types of data:

- Member profiles including name, email, address, membership status, and account standing
- Catalog records including title, author, ISBN, genre, copy count, and availability status
- Loan records including member ID, item ID, check-out date, due date, return date, and
  renewal count
- Reservation records including member ID, item ID, request date, hold notification date,
  hold expiry date, and status
- Overdue records derived from loan records where return date is null and due date is past

#### External Participants

The following participants interact with the LMS from outside the system boundary:

- Library Patron (human user — patron portal or in-person)
- Librarian (human user — staff workstation)
- System Administrator (human user — admin console)
- Email Notification Service (third-party system — sends automated emails)

---

### Task 1: Context Diagram (20 points)

Create a context diagram for the LMS using Yourdon-Coad notation.

#### Step 1 — Single Process

Draw one circle labeled "Library Management System" in the center of the diagram. Number
it 0.

#### Step 2 — External Entities

Draw all four external entities as squares around the central process. Place patrons and
the librarian on the left side; the administrator and Email Notification Service on the
right side.

#### Step 3 — Data Flows

Draw and label every data flow between each external entity and the central process. Use
noun-phrase labels only. Required data flows:

Flows FROM Patron TO System:

- Member Registration Request
- Catalog Search Query
- Book Reservation Request
- Loan Renewal Request
- Return Transaction (self-service kiosk)

Flows FROM System TO Patron:

- Search Results
- Reservation Confirmation
- Hold Notification
- Renewal Confirmation
- Overdue Notice

Flows FROM Librarian TO System:

- Check-Out Transaction
- Return Transaction (desk)
- Manual Renewal Request

Flows FROM System TO Librarian:

- Loan Receipt
- Return Confirmation
- Overdue Items Report

Flows FROM Administrator TO System:

- Member Account Update
- Loan Policy Configuration

Flows FROM System TO Administrator:

- Account Confirmation
- Policy Update Confirmation

Flows FROM System TO Email Notification Service:

- Outbound Email Request

Flows FROM Email Notification Service TO System:

- Email Delivery Status

#### Step 4 — Quality Check

Before submitting the context diagram, verify:

- Exactly one process bubble is present
- All four external entities appear
- Every arrow has a noun-phrase label
- No data stores appear in the context diagram
- No process-to-process arrows exist (only one process, so this check is trivially met)

---

### Task 2: Level 1 DFD (35 points)

Expand the context diagram into a Level 1 DFD showing the five major processes of the LMS.

#### Step 1 — Process Bubbles

Draw five numbered process bubbles:

- 1.0 Manage Member Accounts
- 2.0 Catalog Management
- 3.0 Circulation Management
- 4.0 Reservation Management
- 5.0 Reporting

#### Step 2 — Data Stores

Draw four data stores:

- D1 Member Records
- D2 Catalog
- D3 Loan Records
- D4 Reservation Queue

#### Step 3 — External Entities

Repeat the external entities from the context diagram. It is acceptable to repeat an
external entity symbol multiple times on the diagram if it interacts with multiple processes
— this avoids crossing arrows.

#### Step 4 — Data Flows

Connect processes, data stores, and external entities with labeled data flows. Required
flows include:

- Patron → 1.0: Member Registration Request
- 1.0 → D1: New Member Record
- 1.0 → Patron: Account Confirmation
- Administrator → 1.0: Member Account Update
- Patron → 2.0: Catalog Search Query
- 2.0 → D2: Catalog Update (from Administrator path)
- 2.0 → Patron: Search Results
- 2.0 → D2: Availability Status Update (triggered by circulation)
- Librarian → 3.0: Check-Out Transaction
- 3.0 → D1: Member Status Check (read)
- 3.0 → D2: Item Availability Check (read)
- 3.0 → D3: Loan Record (write)
- 3.0 → Librarian: Loan Receipt
- Librarian → 3.0: Return Transaction
- 3.0 → D4: Hold Queue Check (read)
- Patron → 4.0: Book Reservation Request
- 4.0 → D1: Member Status Check (read)
- 4.0 → D2: Availability Check (read)
- 4.0 → D4: Reservation Record (write)
- 4.0 → Email Notification Service: Hold Notification Request
- 4.0 → Patron: Reservation Confirmation
- 5.0 → D3: Overdue Query (read)
- 5.0 → D1: Membership Data Query (read)
- 5.0 → Librarian: Overdue Items Report

#### Step 5 — Leveling Consistency Check

Compare every data flow in your context diagram against your Level 1 DFD. Every context
diagram flow must appear in the Level 1 DFD. Complete the following table in your
submission:

| Context Diagram Flow | Direction | Present in Level 1? | Level 1 Process |
|---|---|---|---|
| Member Registration Request | Patron → System | Yes / No | Process # |
| Catalog Search Query | Patron → System | Yes / No | Process # |
| (continue for all flows) | | | |

---

### Task 3: Level 2 DFD — Expansion of Process 3.0 (30 points)

Expand Process 3.0 Circulation Management into a Level 2 DFD showing its internal
sub-processes.

#### Step 1 — Sub-Processes

Draw the following numbered sub-processes:

- 3.1 Validate Member Status
- 3.2 Check Item Availability
- 3.3 Record Check-Out
- 3.4 Process Return
- 3.5 Process Renewal
- 3.6 Check Hold Queue

#### Step 2 — Boundary Data Flows

The Level 2 diagram must show the same boundary flows that appeared on Process 3.0 in the
Level 1 DFD. Place these flows at the edges of the Level 2 diagram, with arrows entering
or leaving the diagram boundary.

Incoming boundary flows:

- Check-Out Transaction (from Librarian)
- Return Transaction (from Librarian)
- Loan Renewal Request (from Patron or Librarian)
- Member Status from D1 (read access)
- Item Availability from D2 (read access)

Outgoing boundary flows:

- Loan Receipt (to Librarian)
- Return Confirmation (to Librarian)
- Loan Record to D3 (write)
- Hold Queue Check from D4 (read)
- Hold Notification Request (to Email Notification Service)

#### Step 3 — Internal Data Flows

Add data flows connecting the Level 2 sub-processes to each other and to any Level 2-only
data stores. Example:

- 3.1 outputs "Validated Member Status" to 3.2 and 3.3
- 3.2 outputs "Item Availability Confirmed" to 3.3
- 3.3 writes "New Loan Record" to D3 Loan Records
- 3.4 reads "Existing Loan Record" from D3 Loan Records
- 3.4 passes "Returned Item ID" to 3.6
- 3.6 reads "Pending Hold" from D4 Reservation Queue
- 3.6 outputs "Hold Notification Request" to boundary

#### Step 4 — Balancing Table

Submit a completed balancing table confirming every Level 1 boundary flow is present in
the Level 2 diagram:

| Level 1 Flow on Process 3.0 | Direction | Present in Level 2? | Level 2 Location |
|---|---|---|---|
| Check-Out Transaction | IN | | |
| Return Transaction | IN | | |
| Loan Receipt | OUT | | |
| Return Confirmation | OUT | | |
| Loan Record (D3) | OUT | | |
| Hold Notification Request | OUT | | |

---

### Task 4: Error Identification (15 points)

The following diagram fragment descriptions contain DFD errors. For each item, identify
the error by name and describe the correction.

#### Fragment A

A DFD fragment shows an External Entity labeled "Insurance Company" with an arrow pointing
directly to a Data Store labeled "D5 Claims Records." There is no process bubble between
them.

Identify the error and describe the correction.

#### Fragment B

A DFD fragment shows a process bubble labeled "3.3 Record Check-Out." Two arrows enter the
bubble: "Check-Out Transaction" from the Librarian and "Member Status" from D1. No arrows
exit the bubble.

Identify the error and describe the correction.

#### Fragment C

A DFD fragment shows a process bubble labeled "2.1 Search Catalog." One arrow exits the
bubble labeled "Search Results" going to the Patron external entity. No arrows enter the
bubble.

Identify the error and describe the correction.

#### Fragment D

A DFD fragment shows an arrow connecting Process 1.0 to Process 4.0. The arrow has no
label.

Identify BOTH errors present and describe both corrections.

---

### Submission Checklist

Before submitting, verify:

- [ ] Context diagram has exactly one process, all four external entities, and all flows
      labeled with noun phrases
- [ ] Level 1 DFD has five process bubbles with correct numbering
- [ ] Level 1 DFD has all four data stores
- [ ] Leveling consistency table is complete
- [ ] Level 2 DFD has correct decimal numbering (3.1 through 3.6)
- [ ] Balancing table is complete and shows all Level 1 flows present in Level 2
- [ ] All four error identification fragments are answered with error name and correction
- [ ] All files named with LastName prefix

---

### Grading Rubric

| Task | Criteria | Points |
|---|---|---|
| Task 1 — Context Diagram | Correct single process, all entities, all flows labeled (20) | 20 |
| Task 2 — Level 1 DFD | All five processes correctly numbered (10) | 10 |
| | All four data stores present with data flows (10) | 10 |
| | Leveling consistency table complete (8) | 8 |
| | All data flows labeled with noun phrases (7) | 7 |
| | Subtotal | **35** |
| Task 3 — Level 2 DFD | All six sub-processes with correct decimal numbering (8) | 8 |
| | Boundary flows match Level 1 Process 3.0 (12) | 12 |
| | Internal data flows complete (5) | 5 |
| | Balancing table complete (5) | 5 |
| | Subtotal | **30** |
| Task 4 — Error ID | Each error correctly named and corrected (4 × 3.75) | 15 |
| | Subtotal | **15** |
| **Total** | | **100** |

---

### Professor Nash Note

The most common lab error I see is using flowchart diamonds to show decisions inside a DFD.
DFDs do not have decision logic — that belongs in BPMN or in a process specification. If
you want to show that "if account is suspended then deny check-out," that logic lives in the
process specification for Process 3.1 Validate Member Status, not in the DFD itself. The
DFD simply shows the data flows. Keep those two modeling techniques separate.

---

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced DFD and data dictionary practice aligned with ECBA exam competencies.

### Challenge Step 1: Level 2 DFD with Process Specifications

Select the most complex process from your Level 1 DFD. Decompose it into a Level 2 DFD showing its internal sub-processes. Then, for each Level 2 process that has no further decomposition (a primitive process), write a short process specification (minispec) describing the transformation logic in structured English. A minispec should: identify the inputs, describe the processing rules in IF/THEN/ELSE or sequential steps, and identify the outputs. Verify that your Level 2 diagram is balanced with Level 1 — every boundary flow at Level 1 for the decomposed process must appear as a boundary flow at Level 2.

### Challenge Step 2: Data Dictionary Expansion

Review the data flows and data stores in your Level 1 DFD. Create a complete data dictionary with entries for: all five most significant data flows (with composition using +, [], {}, and () notation), all data stores (listing the data elements they contain), and three process specifications for primitive processes. Use the standard data dictionary notation: + means AND, [] means OR (selection), {} means iteration (one or more), () means optional. Your data dictionary should serve as a standalone reference that a developer could use to understand every data element in the system without referring to the DFD diagram.

### Challenge Step 3: DFD Quality Audit Checklist

After completing all lab tasks, perform a systematic quality audit of your own DFD set (context diagram and Level 1) using the following checklist. For each item, mark Pass or Fail and, for any Fail, describe the specific violation found:

- All process names use verb-noun format
- All data flows are labeled with noun-phrase names
- No direct external entity to data store connections exist
- No direct data store to data store connections exist
- No black hole processes (input with no output)
- No miracle processes (output with no input)
- Level 1 boundary flows exactly match context diagram boundary flows
- All data store names are nouns describing stored content (not process or function names)

Submit the completed audit checklist as an appendix to your lab submission. This exercise develops the self-review habits that professional BAs apply before presenting diagrams to stakeholders.

*Lab Activity — Module 10 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
