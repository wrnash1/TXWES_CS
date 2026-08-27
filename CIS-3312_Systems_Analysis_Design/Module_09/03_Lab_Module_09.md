# Lab Activity: Module 09 — Process Modeling with BPMN

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Business Process Modeling

---

### Lab Overview

In this lab you will create two BPMN 2.0 process models for the Lakewood Community Library
Management System: an As-Is model of the current manual book reservation process and a
To-Be model of the improved digital process. You will then annotate the differences and
write a brief process improvement summary.

**Estimated time:** 2.5–3 hours

**Tools allowed:** draw.io (free at app.diagrams.net), Lucidchart free tier, Microsoft
Visio, Bizagi Modeler (free), or hand-drawn and photographed. All BPMN shapes must follow
the standard notation described in the Reading Guide — not generic flowchart shapes.

---

### Case Study: LMS Book Reservation — Background

The Lakewood Community Library currently handles book reservations through a manual phone
and paper-based process. The library director wants to understand the current process before
approving the new LMS. You have conducted interviews with the Head Librarian (Ms. Rodriguez)
and three library patrons. The following narrative summarizes your findings.

#### As-Is Narrative

A patron who wants to reserve a book that is currently checked out calls the library during
business hours (9 AM–5 PM, Monday–Saturday). The Librarian who answers the call checks the
paper catalog binder to confirm the book exists and is checked out. If the book is not in
the catalog, the Librarian tells the patron and the call ends. If the book is in the catalog
and is available (not checked out), the Librarian tells the patron to come in and the call
ends. If the book is checked out, the Librarian records the reservation on a paper form
with the patron name, phone number, book title, and date of request. The form is placed in
a physical reservation folder organized alphabetically by book title.

When the book is returned by the borrower, the Librarian checks the reservation folder for
the book title. If no reservation exists, the book is placed back on the shelf. If a
reservation exists, the Librarian calls the patron. If the patron answers, they confirm a
pickup date within 5 days. If the patron does not answer, the Librarian leaves a voicemail
and marks the form "awaiting callback." The Librarian calls again the next business day if
no callback is received. If the patron does not respond within 3 business days, the
reservation is cancelled, the form is discarded, and the book is shelved.

Known pain points identified in interviews:

- Patrons cannot make reservations outside business hours
- Two rounds of phone tag delay notification by 1–3 business days on average
- Paper forms are occasionally lost or misfiled
- No systematic reminder if patron forgets pickup deadline
- Librarian time is consumed by repeated outbound calls

#### To-Be Narrative

With the new LMS, patrons search the online catalog at any time. If a book is checked out,
the patron clicks the Reserve button on the book detail page. The system checks whether the
patron account is active and in good standing. If the account is suspended, the system
displays an error and the process ends. If the account is active, the system records the
reservation, assigns a reservation ID, and sends a confirmation email immediately.

When the checked-out book is returned via the existing check-in process, the LMS
automatically checks for pending reservations. If a reservation exists, the system marks
the book as hold-reserved, sends a hold notification email to the patron with a 7-day
pickup deadline, and updates the patron's account to show the pending hold. The patron
receives the email and comes in to collect the book within 7 days. At day 4 after the hold
notification, the LMS automatically sends a reminder email if the book has not yet been
collected. If the patron collects the book, the hold is cleared and a standard checkout
transaction is processed. If 7 days pass without collection, the LMS automatically cancels
the reservation, sends a cancellation notification email, and makes the book available for
the next patron on the waitlist (if any).

---

### Task 1: As-Is BPMN Process Model (40 points)

Model the current manual book reservation process using BPMN 2.0 notation.

#### Step 1 — Identify Pools and Lanes

Before drawing, list your participants and decide on pool and lane structure.

Required pool: Library (single pool containing all internal participants)

Required lanes within the Library pool:

- Patron (telephone-based interactions)
- Librarian (all staff actions)

Optional second pool: if you model the patron as a separate pool, use message flow between
pools for all patron-Librarian communication. Both approaches are acceptable.

#### Step 2 — Identify All Activities

Map each step in the As-Is narrative to a named BPMN Task or Gateway. Name tasks with
verb-noun phrases: "Search Paper Catalog," "Record Reservation on Form," "Call Patron,"
"Leave Voicemail."

#### Step 3 — Identify All Decision Points

Identify every branch in the narrative and model each branch as the correct gateway type.
Justify your gateway choice in your submission notes.

Required gateways:

- Is the book in the catalog? (exclusive — yes/no)
- Is the book currently checked out? (exclusive — yes/no)
- Is a reservation on file for this book? (exclusive — yes/no)
- Did patron answer the call? (exclusive — yes/no)
- Did patron respond within 3 business days? (exclusive — yes/no)

#### Step 4 — Add Events

Required events:

- Start Event: "Patron Calls Library" (Message Start)
- End Event 1: "Call Ends — Book Not Found" (None End)
- End Event 2: "Call Ends — Book Available" (None End)
- End Event 3: "Reservation Confirmed" (None End)
- End Event 4: "Book Shelved — No Reservation" (None End)
- End Event 5: "Patron Confirms Pickup Date" (None End)
- End Event 6: "Reservation Cancelled" (None End)
- Timer Intermediate Event: "Wait 1 Business Day" before second call attempt

#### Step 5 — Apply BPMN Quality Checks

Before submitting, verify:

- Every path reaches an End Event
- All Exclusive Gateway splits have a default path
- Sequence flow does not cross pool boundaries
- Every activity is labeled with a verb-noun phrase
- Every gateway condition is labeled on the outgoing arrows

---

### Task 2: To-Be BPMN Process Model (40 points)

Model the improved future-state book reservation process using BPMN 2.0 notation.

#### Step 1 — Identify Pools and Lanes

Required pools:

- Patron (single lane — web portal interactions)
- Library System (lanes: Patron Portal, Circulation System, Email Service)

Use message flow for all communication between the Patron pool and the Library System pool.

#### Step 2 — Identify All Activities

Required tasks:

- Search Online Catalog (User Task — Patron Portal lane)
- Click Reserve Button (User Task — Patron Portal lane)
- Validate Patron Account Status (Service Task — Circulation System lane)
- Record Reservation and Assign ID (Service Task — Circulation System lane)
- Send Confirmation Email (Send Task — Email Service lane)
- Receive Confirmation Email (Receive Task — Patron pool)
- Process Book Check-In (Service Task — Circulation System lane)
- Check for Pending Reservations (Service Task — Circulation System lane)
- Mark Book as Hold-Reserved (Service Task — Circulation System lane)
- Send Hold Notification Email (Send Task — Email Service lane)
- Receive Hold Notification (Receive Task — Patron pool)
- Collect Book at Desk (User Task — Patron pool)
- Process Checkout Transaction (Service Task — Circulation System lane)
- Send Day-4 Reminder Email (Send Task — Email Service lane)
- Cancel Reservation (Service Task — Circulation System lane)
- Send Cancellation Email (Send Task — Email Service lane)
- Notify Next Waitlist Patron (Send Task — Email Service lane)

#### Step 3 — Model the Timer Logic

Use a Timer Intermediate Boundary Event attached to a Wait subprocess to model the 7-day
hold window. At day 4, a Timer Intermediate Event triggers the reminder email. At day 7, a
Timer Intermediate Event triggers the auto-cancellation.

Alternative approach: model the 7-day window as a collapsed subprocess labeled "Manage
Hold Period" with an attached boundary Timer Event for the 7-day expiry.

#### Step 4 — Add Events

Required events:

- Start Event: "Patron Initiates Reservation" (None Start — triggered by catalog search)
- End Event 1: "Account Suspended — Process Ends" (Error End)
- End Event 2: "Reservation Recorded — Awaiting Return" (None End)
- End Event 3: "Checkout Complete" (None End)
- End Event 4: "Reservation Cancelled — Book Available" (None End)

#### Step 5 — Apply BPMN Quality Checks

Use the same quality checklist from Task 1. Additionally verify:

- Message flows cross pool boundaries correctly
- Sequence flows stay within pools
- Timer events are drawn as double-circle with clock icon
- Service tasks are labeled to indicate automation

---

### Task 3: Process Improvement Annotation (10 points)

Prepare a brief written annotation document (one page maximum) that includes:

- A table comparing As-Is vs. To-Be on these dimensions: total number of tasks, number of
  decision gateways, number of end events, number of potential phone-tag loops, availability
  hours (business hours only vs. 24/7).
- Three specific process improvements enabled by the new LMS, stated as: "Pain point X in
  the As-Is is resolved in the To-Be by Y."
- One process risk introduced by the To-Be model that did not exist in the As-Is model and
  a proposed mitigation.

---

### Task 4: Gateway Justification Notes (10 points)

For each gateway in your To-Be model, write one sentence explaining why you chose that
gateway type. Submit these as a numbered list matching your gateway labels.

Example format:

1. "Is patron account active?" — Exclusive Gateway — because exactly one of two mutually
   exclusive outcomes applies: the account is active or it is not.

---

### Submission Checklist

Before submitting, verify:

- [ ] As-Is diagram uses BPMN notation (not generic flowchart shapes)
- [ ] As-Is diagram has all required events, tasks, and gateways from Task 1
- [ ] To-Be diagram has separate Patron and Library System pools
- [ ] To-Be diagram uses message flow between pools and sequence flow within pools
- [ ] Timer events are correctly drawn and labeled
- [ ] Process improvement annotation table is complete
- [ ] Gateway justification notes are submitted as a numbered list
- [ ] All files named with LastName prefix

---

### Grading Rubric

| Task | Criteria | Points |
|---|---|---|
| Task 1 — As-Is Model | Correct BPMN notation (not flowchart shapes) (5) | 5 |
| | All required tasks identified and labeled (10) | 10 |
| | Gateways correctly typed and labeled with conditions (10) | 10 |
| | All paths reach an End Event (8) | 8 |
| | Timer intermediate event present (7) | 7 |
| | Subtotal | **40** |
| Task 2 — To-Be Model | Correct pool/lane structure with message flows (8) | 8 |
| | All required tasks present and correctly typed (10) | 10 |
| | Timer boundary events model hold window correctly (10) | 10 |
| | Quality checks pass — no broken paths or wrong flows (7) | 7 |
| | Send/Receive task pairs on message flows (5) | 5 |
| | Subtotal | **40** |
| Task 3 — Annotation | As-Is vs. To-Be comparison table complete (4) | 4 |
| | Three specific improvement statements (4) | 4 |
| | Risk + mitigation identified (2) | 2 |
| | Subtotal | **10** |
| Task 4 — Justification | One justification per gateway, correct reasoning (10) | 10 |
| | Subtotal | **10** |
| **Total** | | **100** |

---

### Professor Nash Note

The most common error I see in BPMN labs is using generic diamond flowchart shapes instead
of BPMN gateway diamonds with the correct interior icons. A plain diamond with no icon is
not a valid BPMN gateway — it is ambiguous. Use your drawing tool's BPMN shape library, not
the basic flowchart library. In draw.io, the BPMN shapes are in the Extras menu under Edit
Diagram or in the shape search. If you cannot find BPMN shapes, post in the discussion
board before the deadline.

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced BPMN modeling and process improvement practice aligned with ECBA exam competencies.

### Challenge Step 1: Subprocess Expansion

Select one task from your To-Be BPMN diagram that involves multiple internal steps (for example, "Process Hold Request" or "Notify Member"). Expand it into a fully detailed collapsed subprocess by creating a separate sub-process diagram. Your sub-process diagram must include: a None Start Event, at least three tasks, at least one gateway, and an End Event. Ensure the sub-process is balanced — every data input needed from the parent process is represented as a data input to the sub-process, and every output produced is returned to the parent. Add a plus-sign marker to the task in the parent diagram to indicate the collapsed subprocess. This exercise practices the BPMN subprocess concept and the scope boundaries that separate parent and child process flows.

### Challenge Step 2: Performance Measurement Framework

Using the improvement annotations you created in Task 3, design a formal performance measurement framework for the To-Be library book return process. For each improvement identified, define: the metric name, how it will be measured (data source and collection method), the As-Is baseline value, the To-Be target value, and the measurement frequency. Present your framework as a table. Then write a one-paragraph explanation of how this framework connects BABOK Solution Evaluation (KA 7) to the BPMN process model — specifically, how process models enable measurement of solution value after deployment.

### Challenge Step 3: Error Handling Extension

Review your To-Be BPMN diagram and identify at least two failure scenarios that are not currently modeled (for example: the book barcode does not scan, the patron's card is expired, or the system is offline during check-in). For each failure scenario, add the appropriate BPMN error handling element to your diagram — either an interrupting boundary event on the relevant task, an error end event, or an exception flow using an Exclusive Gateway. Document each addition with a note explaining: what triggers the exception, which BPMN element type handles it, and what the expected outcome is. This exercise practices complete process modeling that accounts for real-world failure conditions, not just the happy path.

---

*Lab Activity — Module 09 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
