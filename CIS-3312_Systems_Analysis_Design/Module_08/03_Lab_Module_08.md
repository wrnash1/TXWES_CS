# Lab Activity: Module 08 — Use Case and User Story Development

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Lab Overview

In this lab you will apply use case modeling and user story techniques to the Lakewood
Community Library Management System (LMS). You will produce a use case diagram, two fully
dressed specifications, a user story backlog with acceptance criteria, and a story map. This
set of deliverables mirrors what a business analyst produces during the requirements analysis
phase of a real project.

**Estimated time:** 2.5–3 hours

**Tools allowed:** Draw.io (free), Lucidchart free tier, Microsoft Visio, or hand-drawn and
photographed. All story documents may be submitted as plain text or formatted Word/Google
Docs.

---

### Case Study: Lakewood Community Library Management System

The Lakewood Community Library serves approximately 4,200 active members. The library
director, Ms. Chen, has commissioned a new Library Management System to replace a legacy
desktop application that cannot support online catalog access or self-service renewal.

The following stakeholders have been interviewed:

- **Library Patrons** want to search the catalog online, place holds on checked-out items,
  renew loans without visiting the library, and receive reminders before due dates.
- **Librarians** want to manage check-out and return transactions efficiently, view a
  dashboard of overdue items, and process reservations with minimal manual steps.
- **The System Administrator** wants to add, update, and deactivate member accounts and
  configure loan period rules.
- **An Email Notification Service** (third-party integration) sends automated emails for
  confirmations, reminders, and overdue notices.

Business rules:

- Members may borrow up to 10 items at one time.
- Standard loan period is 21 days; reference materials are 7 days.
- Members with 3 or more overdue items are suspended and cannot borrow.
- Late fees accrue at $0.25 per day per item.
- Holds expire after 7 days if the member does not collect the reserved item.

---

### Task 1: Use Case Diagram (35 points)

Using the case study above, create a use case diagram for the Lakewood LMS.

#### Step 1 — Identify All Actors

List every actor before opening your drawing tool. For each actor, identify whether they are
primary or secondary and note at least one goal they bring to the system.

Minimum actors to include:

- Library Patron
- Librarian
- System Administrator
- Email Notification Service

#### Step 2 — Identify All Use Cases

List at least 10 use cases. Each use case name must be a verb-noun phrase. Do not use
generic names like "Process Transaction" — be specific to the LMS domain.

Required use cases (at minimum):

- Search Catalog
- Check Out Book
- Return Book
- Reserve Book
- Renew Loan
- View Member Account
- Manage Member Account
- Generate Overdue Report
- Authenticate Member
- Send Notification
- Apply Late Fee

#### Step 3 — Draw the Diagram

Draw the use case diagram following UML notation:

- System boundary rectangle labeled "Library Management System"
- Actors as stick figures outside the boundary
- Use cases as ellipses inside the boundary
- Association lines between actors and the use cases they participate in
- At least two include relationships (dashed arrows, labeled include)
- At least one extend relationship (dashed arrow, labeled extend, arrow points TO base)
- At least one generalization relationship if appropriate

#### Step 4 — Annotate Your Diagram

Add a legend identifying which relationships are include, extend, and generalization. Label
primary actors with a P and secondary actors with an S.

#### Diagram Deliverable

Submit your diagram as an exported PNG or PDF. Name the file: LastName_LMS_UseCaseDiagram.

---

### Task 2: Fully Dressed Use Case Specifications (30 points)

Write fully dressed use case specifications for two use cases from your diagram. You must
include one use case that uses the include relationship and one that uses the extend
relationship.

#### Suggested Pairs

Option A: Check Out Book (uses include) + Apply Late Fee (uses extend via Return Book)

Option B: Reserve Book (uses include) + Send Overdue Notice (uses extend via notification)

#### Required Fields for Each Specification

For each use case, complete all fields listed below:

- **Use Case ID**: Assign UC-01 through UC-11 based on your diagram
- **Use Case Name**: Verb-noun phrase matching your diagram ellipse
- **Goal in Context**: One complete sentence describing the actor's goal
- **Scope**: Library Management System
- **Level**: User Goal
- **Primary Actor**: Name the actor who initiates the use case
- **Stakeholders and Interests**: List at least two stakeholders and what each needs
- **Preconditions**: At least two conditions that must be true before the use case begins
- **Minimal Guarantees**: What the system ensures even if the use case fails
- **Success Guarantees**: What the system ensures when the use case completes
- **Main Success Scenario**: Numbered steps, minimum 6 steps, alternating actor/system
- **Extensions**: At least two extensions with step-letter reference and resolution steps
- **Technology Variations**: At least one technology-neutral alternative at a specific step

#### Specification Format Example

```text
Use Case ID:       UC-03
Use Case Name:     Return Book
Goal in Context:   The Librarian processes the physical return of a borrowed item and
                   updates the loan record to release the member's borrowing quota.
Primary Actor:     Librarian
Preconditions:
  1. The book barcode is scannable.
  2. The member has an active loan record for this item.
Main Success Scenario:
  1. Librarian scans the book barcode.
  2. System retrieves the active loan record.
  3. System checks the return date against the due date.
  4. System marks the loan as returned and updates inventory.
  5. System checks for pending holds on this title.
  6. System confirms return and prints receipt.
Extensions:
  3a. Return date is after due date:
      3a.1 System calculates late fee.
      3a.2 Apply Late Fee extends: system posts fee to member account.
      3a.3 Use case continues at step 4.
  5a. Pending hold exists for this title:
      5a.1 System flags item as hold-reserved.
      5a.2 System notifies hold-requesting member via Email Service.
```

---

### Task 3: User Story Backlog with Acceptance Criteria (25 points)

Write a user story backlog for the LMS MVP release. Your backlog must contain at least eight
user stories covering at least three different actor types.

#### Step 1 — Write the User Stories

Use the standard format for all stories:

As a [actor], I want [capability], so that [business value].

Evaluate each story against INVEST. If a story fails any INVEST criterion, revise it until
it passes all six.

#### Step 2 — Add Acceptance Criteria

For each user story, write at least three acceptance criteria in Given-When-Then format.

Each criterion must follow this structure:

- Given [initial context or precondition]
- When [action or event]
- Then [observable, verifiable outcome]

#### Step 3 — Identify Epics

Mark any story in your backlog that is too large for a single sprint as an Epic. For each
Epic, write at least two child stories that decompose the Epic into implementable pieces.

#### Backlog Deliverable Format

Submit your backlog as a numbered list. For each item include: story number, story text,
INVEST pass/fail for each letter, and three or more acceptance criteria.

---

### Task 4: Story Map (10 points)

Create a story map for the LMS MVP release using the stories from Task 3.

#### Step 1 — Define the Backbone

List the major user activities in left-to-right sequence representing a typical patron
journey through a single library visit: Join, Browse, Borrow, Return, Manage Account.

#### Step 2 — Map Stories to Activities

Place each user story from your backlog in the column under the activity it supports. If a
story supports multiple activities, choose the primary one.

#### Step 3 — Define Release Slices

Draw two horizontal lines to define three releases:

- **MVP (Release 1)**: The minimum set of stories that supports end-to-end patron borrowing
- **Release 2**: Adds self-service features (online renewal, email reminders)
- **Release 3**: Adds advanced features (recommendations, mobile app)

#### Story Map Deliverable

Submit your story map as a table, spreadsheet, or drawn diagram. Clearly label rows as MVP,
Release 2, and Release 3.

---

### Submission Checklist

Before submitting, verify:

- [ ] Use case diagram includes all required actors, at least 10 use cases, 2 include
      relationships, and 1 extend relationship
- [ ] Both fully dressed specifications include all required fields
- [ ] Extensions in specifications use correct step-letter numbering
- [ ] Each user story uses As a / I want / so that format
- [ ] Each story includes at least 3 Given-When-Then acceptance criteria
- [ ] At least one Epic is identified and decomposed
- [ ] Story map has backbone across top and release slices as horizontal rows
- [ ] All files are named with LastName prefix

---

### Grading Rubric

| Task | Criteria | Points |
|---|---|---|
| Task 1 — Use Case Diagram | All actors correctly identified and placed (5) | 5 |
| | All use cases named with verb-noun phrases (5) | 5 |
| | Include relationships correct direction and label (8) | 8 |
| | Extend relationships correct direction and label (8) | 8 |
| | Diagram is legible and uses UML notation (5) | 5 |
| | Subtotal | **35** |
| Task 2 — Fully Dressed Specs | All required fields present in both specs (10) | 10 |
| | Main success scenario has 6+ numbered steps (8) | 8 |
| | Extensions use correct numbering convention (7) | 7 |
| | Stakeholders and interests clearly stated (5) | 5 |
| | Subtotal | **30** |
| Task 3 — User Stories | Stories use correct format; 8 or more stories (8) | 8 |
| | Each story passes INVEST evaluation (7) | 7 |
| | Acceptance criteria use Given-When-Then format (7) | 7 |
| | At least one Epic decomposed into child stories (3) | 3 |
| | Subtotal | **25** |
| Task 4 — Story Map | Backbone in correct activity sequence (3) | 3 |
| | Stories correctly placed under activities (4) | 4 |
| | Release slices clearly defined (3) | 3 |
| | Subtotal | **10** |
| **Total** | | **100** |

---

### Professor Nash Note

The most common mistake in this lab is drawing the extend arrow in the wrong direction.
Remember: the arrow points FROM the extending use case TO the base use case. If you drew it
the other way, fix it before submitting — it is an automatic 4-point deduction. The second
most common mistake is writing acceptance criteria that describe implementation details
instead of observable outcomes. Your Given-When-Then criteria should describe what a user
sees or experiences, not how the database updates internally.

---

*Lab Activity — Module 08 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
