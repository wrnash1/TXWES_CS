# Reading Guide: Module 06 - Data Flow Diagrams and Entity-Relationship Diagrams

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3312 &BULL; SYSTEMS ANALYSIS & DESIGN</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 06 covers two foundational visual modeling techniques in systems analysis and design: Data Flow Diagrams (DFDs) and Entity-Relationship Diagrams (ERDs). DFDs model how data moves through a system — the processes, stores, and flows that make up system behavior. ERDs model the structure of data the system stores — the entities, attributes, and relationships that will become the database schema. Both techniques appear on the IIBA ECBA exam and are used throughout professional BA practice.

---

## 1. Core Vocabulary

### 1.1 Data Flow Diagram (DFD)

A DFD is a graphical model showing how data enters, moves through, is transformed within, and exits a system. DFDs use four symbols: external entities (rectangles), processes (circles or rounded rectangles), data stores (open-ended rectangles), and data flows (labeled arrows). DFDs are leveled — the Context Diagram (Level 0) shows the whole system; Level 1 decomposes it into major sub-processes; Level 2 decomposes each Level 1 process.

### 1.2 Context Diagram

A Context Diagram (Level 0 DFD) shows the entire system as a single process bubble, all external entities, and all data flows between them. It establishes system scope without revealing internal detail. Context Diagrams are ideal for stakeholder scope alignment.

### 1.3 External Entity

An external entity is a person, organization, or system outside the system boundary that sends data to or receives data from the system. External entities are shown as rectangles. A source sends data into the system; a sink receives data from it. An entity can be both.

### 1.4 Process

A process represents a transformation — the system acts on data and produces output. Every process must have at least one input data flow and at least one output data flow. A process with input but no output is a "black hole"; a process with output but no input is a "miracle" — both are DFD rule violations.

### 1.5 Data Store

A data store is a repository where data is held at rest within the system boundary — a database table, file, or information repository. Data stores are shown as open-ended rectangles. Data cannot flow directly between two data stores without passing through a process.

### 1.6 Data Flow

A data flow is a labeled arrow showing data moving between DFD symbols. Every data flow must be named with a description of the data it carries ("Customer Order," "Validated Payment"). Data cannot flow directly between two external entities.

### 1.7 Level Balancing

Level balancing means the inputs and outputs of a Level 0 process must match exactly the inputs and outputs shown in the Level 1 diagram. Every data flow crossing the system boundary at Level 0 must appear at Level 1. Unbalanced DFDs are a common exam trap.

### 1.8 Entity-Relationship Diagram (ERD)

An ERD is a data modeling diagram showing the entities (things the system stores data about), their attributes (descriptive data elements), and the relationships between entities. ERDs are the conceptual blueprint from which relational database schemas are derived.

### 1.9 Entity

An entity is a distinct real-world person, place, object, event, or concept about which the system stores data. Entities become tables. A strong entity has its own primary key; a weak entity depends on a related strong entity for unique identification.

### 1.10 Cardinality

Cardinality describes the numerical relationship between instances of two related entities: how many of one can be associated with how many of another. The three cardinalities are one-to-one (1:1), one-to-many (1:N), and many-to-many (M:N). Cardinality drives database design decisions: which table holds the foreign key and when a junction table is needed.

### 1.11 Junction Table

A junction table (also called an associative entity or bridge table) resolves a many-to-many relationship in a relational database by creating a new table that holds the primary keys of both related entities as foreign keys. Example: OrderLine resolves the M:N relationship between Order and Product.

### 1.12 Data Dictionary

A data dictionary catalogs every data element referenced in a system — name, data type, format, acceptable values, and the processes or data stores that use it. It removes ambiguity about data definitions and complements both DFDs and ERDs.

---

## 2. DFD Symbol Reference

| Symbol | Shape | Represents | Rules |
|---|---|---|---|
| External Entity | Rectangle | Source or sink outside system boundary | Cannot connect directly to another external entity |
| Process | Circle or rounded rectangle | Data transformation inside system | Must have at least one input and one output |
| Data Store | Open-ended rectangle | Data at rest inside system | Cannot connect directly to another data store |
| Data Flow | Labeled arrow | Data moving between symbols | Must be named; cannot skip symbols |

---

## 3. DFD Leveling Structure

| Level | Name | Content |
|---|---|---|
| Level 0 | Context Diagram | One process bubble (entire system), all external entities, all system boundary data flows |
| Level 1 | System DFD | Major sub-processes, data stores, internal data flows; must balance with Level 0 |
| Level 2 | Process DFD | Decomposition of one Level 1 process; must balance with parent Level 1 process |

---

## 4. DFD Rule Violations (Commonly Tested)

| Violation Name | Description | Fix |
|---|---|---|
| Data store to data store | Arrow goes directly between two data stores | Add a process in between |
| External entity to external entity | Arrow goes directly between two external entities | Route through system processes |
| Black hole | Process has input but no output | Add output data flow or data store |
| Miracle | Process has output but no input | Add input data flow |
| Unnamed data flow | Arrow carries no label | Name the data being carried |
| Unbalanced diagram | Level 1 inputs/outputs do not match Level 0 | Add or remove flows to restore balance |

---

## 5. ERD Crow's Foot Notation Reference

| Symbol | Meaning | Example |
|---|---|---|
| Single vertical line (\|) | Exactly one (mandatory) | Each Order belongs to exactly one Customer |
| Circle (O) | Zero (optional) | A Customer may have zero or more Orders |
| Crow's foot (three-pronged) | Many | One Customer places many Orders |
| Crow's foot + circle | Zero or many (optional many) | Order may contain zero or many OrderLines |
| Crow's foot + line | One or many (mandatory many) | Invoice must have one or many LineItems |
| Single line + line | Exactly one (mandatory one) | OrderLine belongs to exactly one Order |

---

## 6. Cardinality Comparison and Database Design Impact

| Cardinality | Definition | Database Implementation |
|---|---|---|
| 1:1 | One instance of A associates with exactly one instance of B | Foreign key in either table; often merged into one table |
| 1:N | One instance of A associates with many instances of B; each B associates with exactly one A | Foreign key on the "many" (N) side |
| M:N | Many instances of A associate with many instances of B | Requires a junction table with foreign keys from both A and B |

---

## 7. DFD vs. ERD Comparison

| Dimension | DFD | ERD |
|---|---|---|
| Models | Data in motion — how data moves and transforms | Data at rest — what data is stored and how it is related |
| Primary symbols | External entity, process, data store, data flow | Entity, attribute, relationship, cardinality notation |
| Levels | Leveled hierarchy (0, 1, 2) | Conceptual, logical, physical stages |
| Primary audience | Business analysts, process stakeholders | Database designers, developers |
| BABOK technique | Data Flow Diagrams (KA 5) | Data Modeling (KA 5) |
| Output feeds into | System design, process specifications | Database schema design |

---

## 8. Certification Exam Tips

1. The three DFD symbols that cannot connect directly to each other are: data store to data store, external entity to external entity. Any direct connection between these must pass through a process. This rule is tested by showing a diagram with a direct connection and asking you to identify the violation.

2. Level balancing is tested by showing a Level 0 and Level 1 DFD pair and asking whether they are balanced. Check: every data flow crossing the system boundary at Level 0 must appear at Level 1. Count inputs and outputs on both sides.

3. Cardinality identification is tested with scenario descriptions. Practice mapping relationship descriptions to 1:1, 1:N, or M:N immediately upon reading. "One X can have many Y; each Y belongs to exactly one X" = 1:N every time.

4. The M:N resolution pattern is tested. Whenever you see an M:N relationship, know that it requires a junction table. Know that the junction table holds the primary keys of both entities as foreign keys. Know common examples: Student-Course resolved by Enrollment; Order-Product resolved by OrderLine.

5. The Context Diagram shows only one process bubble. If a Level 0 diagram shows more than one process, it is actually a Level 1 diagram. This distinction is directly tested.

6. Crow's Foot notation uses specific line endings. The crow's foot (three prongs) means "many." A single vertical tick means "exactly one." A circle means "zero (optional)." These are combined: a crow's foot with a circle = "zero or many"; a crow's foot with a tick = "one or many."

7. A data dictionary is a complement to DFDs and ERDs — it formally defines every data element referenced in the diagrams. When a question asks how to remove ambiguity about a named data flow or attribute, the answer is the data dictionary.

8. Both DFD and ERD techniques appear in BABOK Guide v3 KA 5 (Requirements Analysis and Design Definition) under the Techniques section. When the exam references a "data modeling technique," it includes both. Know that the ERD is a data modeling technique and the DFD is a process/data flow modeling technique.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, Chapter 10 (Techniques) — Data Flow Diagrams; Data Modeling
- BABOK Guide v3, KA 5: Requirements Analysis and Design Definition — Model Requirements task

Supplemental reading:

- Crow's Foot ERD notation reference at any major diagramming tool documentation (draw.io, Lucidchart)
- Yourdon-DeMarco DFD notation reference (the standard used in most systems analysis textbooks)

---

## 10. Study Checklist

- [ ] Draw a Context Diagram from memory for a simple scenario (3 external entities, 5 data flows).
- [ ] Draw a Level 1 DFD from the same scenario with at least 3 processes and 2 data stores, balanced with the Level 0.
- [ ] Identify all four DFD symbols by shape and explain the rule associated with each.
- [ ] List the three DFD rule violations that appear most on the ECBA exam.
- [ ] Draw an ERD using Crow's Foot notation with at least 4 entities including one M:N relationship resolved with a junction table.
- [ ] Explain the difference between 1:N and M:N cardinality and describe the database implementation of each.
- [ ] Define data dictionary and explain its relationship to DFDs and ERDs.
- [ ] Watch the Module 06 video lecture.
- [ ] Complete the Module 06 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 11. Supplemental Resources

The following open educational resources extend module content on DFDs and ERDs. All are freely accessible without login or purchase.

1. **Data Flow Diagrams — Visual Paradigm Guide**
   <https://www.visual-paradigm.com/guide/data-flow-diagram/what-is-data-flow-diagram/>
   Focus: Comprehensive illustrated guide covering all DFD symbols, leveling rules, and notation conventions. Includes worked examples of Context Diagrams and Level 1 DFDs that directly support the lab exercises.

2. **Entity-Relationship Diagram Tutorial — Lucidchart**
   <https://www.lucidchart.com/pages/er-diagrams>
   Focus: Clear explanation of ERD notation including Crow's Foot symbols, cardinality types, and junction table design. The worked examples reinforce Sections 5 and 6 of this guide.

3. **Data Flow Diagram Rules and Best Practices — Sparxsystems**
   <https://sparxsystems.com/resources/tutorials/uml/dataflow-diagram.html>
   Focus: Reference guide covering DFD rule violations (black holes, miracles, level balancing) with diagrams. Directly reinforces Section 4 of this guide and the most common ECBA exam traps on DFDs.

4. **Normalization and ERD Design — Database Design Course (freeCodeCamp YouTube)**
   <https://www.youtube.com/watch?v=ztHopE5Wnpc>
   Focus: Free university-level video covering entity-relationship modeling, normalization, and junction table design. Supplements the ERD sections of this module for visual learners.

5. **Data Dictionary Best Practices — TechTarget**
   <https://www.techtarget.com/searchdatamanagement/definition/data-dictionary>
   Focus: Plain-language explanation of data dictionary structure, purpose, and content standards. Reinforces Section 1.12 and the data dictionary entries required in the lab.
