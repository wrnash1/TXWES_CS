# Lab Activity: Module 09 - System Design: Logical vs. Physical Design

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab gives you practice applying the logical-physical design distinction, producing a logical design artifact, evaluating design options, and writing a formal solution recommendation. No software installation or terminal commands are required. All work is document-based.

---

## Case Study: Cedarbrook Public Library — Digital Membership and Catalog System

Cedarbrook Public Library currently manages patron memberships and catalog borrowing through a combination of a spreadsheet-based catalog (maintained by staff), paper membership forms filed in binders, and a manual checkout log kept at the circulation desk. The system has no online presence — patrons must visit the library in person to check availability, borrow items, and renew memberships.

The Library Board has approved a project to replace this system with a digital solution. The following requirements have been elicited and approved:

Functional Requirements:

- Patrons shall be able to search the catalog online by title, author, subject, and keyword.
- Patrons shall be able to create and manage their own membership accounts online.
- Patrons shall be able to place holds on items and receive email notifications when holds are available.
- Staff shall be able to check items in and out, renew memberships, and add new catalog items through a staff portal.
- The system shall send automated overdue notices to patrons by email when items are past their due date.

Non-Functional Requirements:

- The system shall support at least 500 concurrent users during peak hours.
- The system shall be available 99.5% of the time.
- All patron data shall be stored within the United States in compliance with applicable state library privacy laws.
- Staff response time for catalog searches shall not exceed 2 seconds.

The Library Director has asked the BA to evaluate three design options before selecting an approach.

---

## Part 1: Logical Design Artifact — 30 Points

### Part 1 Instructions

Produce a logical Entity-Relationship Diagram (ERD) for the Cedarbrook Library system. Your diagram must be technology-independent — it must not include any database product names, data types, SQL syntax, or technology-specific naming conventions.

Your ERD must include:

- At least five entities derived from the requirements (e.g., Patron, Item, Hold, Checkout, Staff)
- Primary key attribute for each entity (underlined)
- At least three additional attributes per entity
- All relationships between entities labeled with verb phrases
- Crow's Foot cardinality notation on all relationship lines (both ends)
- At least one M:N relationship resolved with a junction entity

After drawing the ERD, answer the following in 2–3 sentences: How does your ERD qualify as a logical (rather than physical) design artifact? What would need to change to make it a physical design artifact?

### Grading Rubric — Part 1

| Criterion | Points |
|---|---|
| At least 5 entities with primary keys and additional attributes (3 pts each) | 15 |
| All relationships labeled with verb phrases and cardinality on both ends | 7 |
| M:N relationship resolved with junction entity | 4 |
| Written reflection on logical vs. physical distinction (2–3 sentences) | 4 |

Part 1 Total: 30 points

---

## Part 2: Design Options Analysis — 40 Points

### Part 2 Instructions

The Library Director has identified three candidate design options for the Cedarbrook system:

Option A — Build Custom: Contract a local software development firm to build a custom library management web application from scratch, tailored exactly to Cedarbrook's requirements.

Option B — Buy COTS: Purchase a commercially available library management system (a packaged software product installed on the library's server) that includes catalog, membership, checkout, and notification features.

Option C — Subscribe SaaS: Subscribe to a cloud-based library management platform that provides all required functionality through a monthly subscription, hosted and maintained by the vendor.

Complete the following analysis:

Analysis Step 1: Requirements Coverage Matrix

Create a table with the five functional requirements as rows and the three options as columns (A, B, C). For each cell, mark whether the option satisfies the requirement (Full, Partial, or Not Met) and add a brief note explaining your assessment. Use reasonable professional judgment based on what you know about custom, COTS, and SaaS solutions.

Analysis Step 2: Tradeoff Summary

For each option (A, B, C), write a 3–5 sentence paragraph covering: estimated relative cost (not exact dollar amounts — high/medium/low), implementation timeline (fast/medium/long), primary risks, and primary advantages for this specific scenario.

Analysis Step 3: Non-Functional Requirements Evaluation

Review the four non-functional requirements. For each NF requirement, identify which option (A, B, or C) presents the greatest risk of not satisfying it, and briefly explain why (one sentence per NF requirement).

### Grading Rubric — Part 2

| Criterion | Points |
|---|---|
| Requirements coverage matrix: all 5 requirements x 3 options with assessment notes | 12 |
| Tradeoff summary: cost, timeline, risks, and advantages described for each option | 12 |
| NF requirements evaluation: risk option identified with brief justification (4 pts for each NF requirement) | 16 |

Part 2 Total: 40 points

---

## Part 3: Solution Recommendation Memo — 30 Points

### Part 3 Instructions

Write a professional solution recommendation memo (250–350 words) to the Cedarbrook Library Director recommending one of the three design options.

Your memo must include:

- A brief statement of the recommendation (which option you recommend and why in one sentence)
- Summary of the key findings from your options analysis that support the recommendation
- At least one tradeoff or limitation of your recommended option that the Library Director should be aware of
- At least one condition or next step you would recommend before implementation begins (such as a pilot evaluation, reference check, vendor assessment, or requirements confirmation)
- Professional memo format (To:, From:, Subject:, Date: header; paragraphs with clear transitions)

### Grading Rubric — Part 3

| Criterion | Points |
|---|---|
| Clear recommendation stated with specific supporting rationale | 8 |
| Key findings from options analysis accurately summarized | 8 |
| At least one acknowledged tradeoff or limitation of the recommended option | 7 |
| At least one condition or next step recommended before implementation | 7 |

Part 3 Total: 30 points

---

## Submission Instructions

Combine all three parts into one document with clearly labeled sections. For the ERD in Part 1, embed the diagram image or include a link to the shared diagram file. For written parts, type your responses directly in the document. Submit to the Canvas Module 09 Lab assignment by the due date shown in the course calendar.
