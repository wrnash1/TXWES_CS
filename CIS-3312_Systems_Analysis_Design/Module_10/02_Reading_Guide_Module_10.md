# Reading Guide: Module 10 — Data Flow Diagrams and System Models

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Overview

This reading guide covers DFD notation, context diagrams, Level 0 and Level 1 DFDs, data
stores, external entities, leveling, balancing, and common DFD errors. DFDs are listed as
a business analysis technique in the BABOK Guide and appear on the ECBA exam.

---

### Section 1: DFD Notation — Yourdon-Coad Reference

Data Flow Diagrams use exactly four element types. Every DFD element has a specific shape
that must be used consistently within a single notation standard.

#### Four DFD Elements

| Element | Yourdon-Coad Shape | Gane-Sarson Shape | Represents |
|---|---|---|---|
| External Entity | Square or rectangle | Square or rectangle | Source or sink of data outside the system |
| Process | Circle (bubble) | Rounded rectangle | Data transformation — inputs become outputs |
| Data Store | Open rectangle (two parallel lines, open left end) | Open rectangle | Data at rest — storage and retrieval |
| Data Flow | Labeled directional arrow | Labeled directional arrow | Data moving between elements |

This course uses Yourdon-Coad notation. If you see a rounded rectangle for processes in
another textbook, that source is using Gane-Sarson. Both notations are valid; they differ
only in process shape.

#### Yourdon-Coad Visual Summary

```text
External Entity:   [  Label  ]      Square/rectangle

Process:            ( Label )       Circle or bubble

Data Store:        |= Label =|      Open parallel lines

Data Flow:          ------>         Arrow with noun-phrase label
```

---

### Section 2: Context Diagram Rules and Structure

The context diagram — also called the Level 0 DFD — is always the starting point for DFD
modeling. It provides the highest level of abstraction.

#### Context Diagram Rules

- Contains exactly ONE process bubble representing the entire system
- The process bubble is labeled with the system name and numbered 0 or 1.0
- All external entities that interact with the system appear around the bubble
- All data flows between external entities and the system are labeled
- No data stores appear at the context level — internal details are hidden
- No process-to-process flows appear — there is only one process

#### Context Diagram Purpose

- Defines system scope: data flows on the diagram are in scope; absent flows are out of scope
- Identifies all system stakeholders as external entities
- Provides a scope agreement document that stakeholders can review and sign off

#### LMS Context Diagram — Element Inventory

External entities:

- Library Patron
- Librarian
- System Administrator
- Email Notification Service

Data flows from external entities to system:

- Member Registration Request (from Patron)
- Catalog Search Query (from Patron)
- Book Reservation Request (from Patron)
- Check-Out Transaction (from Librarian)
- Return Transaction (from Librarian)
- Member Account Update (from Administrator)
- Loan Policy Configuration (from Administrator)

Data flows from system to external entities:

- Search Results (to Patron)
- Reservation Confirmation (to Patron)
- Overdue Notice (to Patron via Email Service)
- Loan Receipt (to Librarian)
- Return Confirmation (to Librarian)
- Account Confirmation (to Administrator)
- Hold Notification (to Patron via Email Service)

---

### Section 3: Level 1 DFD — Structure and Rules

The Level 1 DFD expands the single context diagram process into the major functional
subsystems of the system. Each major function becomes a numbered process bubble.

#### Level 1 Rules

- Every data flow from the context diagram must appear in the Level 1 DFD (leveling
  consistency)
- External entities from the context diagram appear again in the Level 1 DFD
- Data stores appear for the first time at Level 1
- Process bubbles are numbered with single integers: 1.0, 2.0, 3.0, etc.
- Data flows between processes are now visible — they were hidden in the context diagram

#### LMS Level 1 DFD — Process Inventory

| Process | Number | Purpose |
|---|---|---|
| Manage Member Accounts | 1.0 | Registration, updates, suspensions |
| Catalog Management | 2.0 | Book records, search, availability |
| Circulation Management | 3.0 | Check-out, return, renewals |
| Reservation Management | 4.0 | Hold requests, notifications, cancellations |
| Reporting | 5.0 | Overdue reports, activity summaries |

#### LMS Level 1 DFD — Data Store Inventory

| Data Store | ID | Contains |
|---|---|---|
| Member Records | D1 | Member profiles, account status, contact info |
| Catalog | D2 | Book titles, authors, ISBNs, copy counts |
| Loan Records | D3 | Active loans, due dates, history |
| Reservation Queue | D4 | Pending holds, hold expiry dates |

#### Level 1 Inter-Process Data Flows

Some data flows connect processes to each other through shared data stores. Examples:

- Circulation Management (3.0) writes Loan Record to D3 Loan Records
- Reservation Management (4.0) reads from D3 Loan Records to check if a title is available
- Reporting (5.0) reads from D3 Loan Records to identify overdue items
- Reservation Management (4.0) writes to D4 Reservation Queue
- Circulation Management (3.0) reads from D4 Reservation Queue when processing returns

---

### Section 4: Level 2 DFD — Process Explosion

A Level 2 DFD expands a single Level 1 process bubble into its internal sub-processes.
The child diagram shows the internal data transformations hidden inside the parent bubble.

#### Level 2 Numbering Convention

Level 2 processes are numbered with the parent process number as a prefix, followed by a
decimal and a child number. Expansion of process 3.0 (Circulation Management) produces
child processes numbered 3.1, 3.2, 3.3, etc.

#### LMS Level 2 DFD Example — Expanding Process 3.0 Circulation Management

Sub-processes of Circulation Management:

- 3.1 Validate Member Status — reads from D1 Member Records; outputs validated status
- 3.2 Check Item Availability — reads from D2 Catalog and D3 Loan Records
- 3.3 Record Check-Out — writes to D3 Loan Records; outputs Loan Receipt
- 3.4 Process Return — reads from D3 Loan Records; writes return status; triggers 3.5
- 3.5 Check for Holds — reads from D4 Reservation Queue; outputs Hold Notification Flag

The boundary of the Level 2 diagram must show the same incoming and outgoing data flows
that were drawn on the parent Process 3.0 bubble in the Level 1 DFD.

---

### Section 5: Leveling and Balancing

Leveling and balancing are the quality assurance checks that confirm DFD decomposition is
correct across levels.

#### Leveling Definition

Leveling is the process of decomposing a higher-level DFD into a more detailed lower-level
DFD. Each level of decomposition must maintain consistency with the level above it.

#### Balancing Definition

Balancing is the verification check confirming that all data flows entering and leaving a
parent process bubble appear as boundary data flows in the child diagram.

#### Balancing Checklist

For any Level 2 DFD that expands Level 1 Process X.0:

- [ ] Every data flow INTO Process X.0 appears as an input at the boundary of the Level 2
      diagram
- [ ] Every data flow OUT OF Process X.0 appears as an output at the boundary of the
      Level 2 diagram
- [ ] No additional external entities appear in the Level 2 diagram that did not interact
      with Process X.0 in the Level 1 diagram
- [ ] New data stores may appear in the Level 2 diagram only if they represent internal
      detail that was hidden in the parent; they must not introduce new boundary flows

#### Balancing Table Template

| Data Flow in Level 1 | Direction | Appears in Level 2? | Level 2 Location |
|---|---|---|---|
| Check-Out Transaction | IN to 3.0 | Yes | Input to Process 3.1 |
| Loan Receipt | OUT from 3.0 | Yes | Output from Process 3.3 |
| Return Transaction | IN to 3.0 | Yes | Input to Process 3.4 |
| Hold Notification Flag | OUT from 3.0 | Yes | Output from Process 3.5 |

---

### Section 6: Common DFD Errors — Reference Table

| Error Name | Description | Visual Indicator | Correction |
|---|---|---|---|
| Black Hole | Process has inputs but no outputs | Arrow enters bubble; no arrows exit | Add output data flow or split into sub-processes |
| Miracle | Process has outputs but no inputs | Arrows exit bubble; none enter | Add input data flow or trace where data originates |
| Direct Entity-to-Store | External entity connects directly to a data store | Arrow from square to open-rectangle | Insert a process bubble between the entity and the store |
| Unnamed Data Flow | Arrow has no label | Unlabeled arrow | Add descriptive noun-phrase label |
| Process-to-Process Direct Flow | Two processes exchange data without a data store | Arrow between two circles | Either add an intermediate data store or verify this is correct |
| External Entity in Wrong Scope | Item that should be a process is drawn as an external entity | See entity criterion | Apply the control-and-own test: does the system own this logic? |
| Missing Leveling Consistency | Level 1 data flow absent from Level 2 diagram | Balance table shows gap | Add missing boundary flow to Level 2 diagram |

> ECBA Exam Tip: The four most-tested DFD errors are Black Hole, Miracle, Direct
> Entity-to-Store, and Unnamed Data Flow. Given a diagram fragment, you should be able to
> identify which error is present without hesitation.

---

### Section 7: Data Flow Labeling Standards

Data flow labels are the most information-dense part of a DFD. Poor labels make a DFD
unreadable and unusable as a requirements document.

#### Labeling Rules

- Use noun phrases, not verbs: "Member Record" not "Retrieve Member"
- Be specific: "Book Availability Status" not "Book Data"
- Reflect actual data content, not system actions
- Use consistent naming across all DFD levels — a flow named "Loan Record" at Level 1
  should not become "Borrowing Data" at Level 2
- Bidirectional arrows must be labeled in both directions if the data differs

#### Good vs. Poor Label Examples

| Poor Label | Problem | Better Label |
|---|---|---|
| Data | Too generic | Member Registration Request |
| Info | Too generic | Catalog Search Results |
| Doing search | Verb phrase — describes action | Catalog Search Query |
| SQL response | Implementation detail | Search Results |
| Stuff | Meaningless | Reservation Confirmation |

---

### Section 8: DFD vs. BPMN — When to Use Each

Students often ask: if I already have a BPMN process model, do I also need a DFD? The
answer depends on what you need to communicate.

| Dimension | DFD | BPMN |
|---|---|---|
| Focus | Data transformation and flow | Process sequence and control flow |
| Decision logic | Not shown | Shown via gateways |
| Sequence | Not shown (logical only) | Explicitly shown |
| Data stores | Explicitly shown | Rarely shown |
| Roles and swimlanes | Not shown | Explicitly shown via pools/lanes |
| System scope | Context diagram defines scope | Pool boundaries define scope |
| Best for | Data requirements, data architecture | Process improvement, workflow automation |

Use both when you need a complete requirements picture. DFDs answer "what data does the
system need and how does it transform it." BPMN answers "how does work flow through the
organization and what are the decision rules."

---

### Section 9: ECBA Exam Preparation

#### BABOK Alignment

DFDs are listed in the BABOK Guide v3 as a technique under Requirements Analysis and Design
Definition. The ECBA exam tests identification of DFD elements and error recognition.

#### Likely ECBA Question Patterns

- Identify the correct DFD element for a described scenario
- Identify which error is present in a given diagram fragment
- Determine whether an item should be an external entity or a process
- Identify which data flows must appear in a Level 2 diagram based on the Level 1 parent
- Explain the purpose of the context diagram vs. the Level 1 DFD

---

### Study Checklist

Work through each item before attempting the quiz.

- [ ] Can you draw all four Yourdon-Coad DFD elements from memory?
- [ ] Can you state the three rules of a context diagram?
- [ ] Can you describe the difference between a context diagram and a Level 1 DFD?
- [ ] Can you identify a Black Hole and a Miracle error in a diagram?
- [ ] Can you explain why an external entity cannot connect directly to a data store?
- [ ] Can you perform a balancing check using a balancing table?
- [ ] Can you correctly number Level 1 and Level 2 processes?
- [ ] Can you distinguish when a DFD is more appropriate than a BPMN diagram?

---

### Key Terms Glossary

| Term | Definition |
|---|---|
| Balancing | Verification that parent process data flows match Level 2 boundary flows |
| Black Hole | DFD error: process has inputs but no outputs |
| Context Diagram | Level 0 DFD — entire system as one process with all external interactions |
| Data Flow | Labeled arrow showing data movement between DFD elements |
| Data Store | Open rectangle representing stored data at rest |
| External Entity | Square representing a source or sink of data outside the system |
| Gane-Sarson | DFD notation using rounded rectangles for processes |
| Level 1 DFD | Expansion of context diagram showing major system processes |
| Level 2 DFD | Expansion of a single Level 1 process into sub-processes |
| Leveling | Decomposition of a higher-level DFD into a more detailed lower-level DFD |
| Leveled Set | The complete collection of context, Level 1, and Level 2 DFDs for a system |
| Miracle | DFD error: process has outputs but no inputs |
| Process | Circle representing a data transformation |
| Yourdon-Coad | DFD notation using circles for processes and squares for external entities |

---

*Reading Guide — Module 10 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
