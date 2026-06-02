# Lab Activity: Module 07 – User Stories and Acceptance Criteria

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University
**Points:** 100

---

## Overview

This lab is a user story writing and acceptance criteria exercise. You will convert traditional requirements into user stories, write Given/When/Then acceptance criteria, and practice splitting epics into Sprint-sized stories. No programming is required.

The ability to write, evaluate, and refine user stories is a core Agile skill tested directly on the PSM I exam.

Estimated time: 90–120 minutes

---

## Part 1 — Requirement Conversion (30 points)

### Part 1 Instructions

The following list contains six traditional requirements written in system-specification style. Convert each one into a well-formed user story in the standard "As a / I can / so that" format.

For each conversion, also write 2–3 acceptance criteria in Given/When/Then format.

### Traditional Requirements to Convert

Requirement 1: The system shall allow users to upload a profile photo in JPEG or PNG format, not to exceed 5 MB.

Requirement 2: The application must send an email notification when an order is shipped.

Requirement 3: Administrators shall be able to deactivate user accounts.

Requirement 4: The search feature shall return results within 500 milliseconds for queries up to 50 characters.

Requirement 5: The system shall generate a PDF invoice for each completed transaction.

Requirement 6: Users must be able to select their preferred language from a list of supported languages before logging in.

### Part 1 Grading (30 points)

Each conversion (6 × 5 pts):

- Correct user story format with all three components (who/what/why): 2 pts
- 2–3 acceptance criteria in Given/When/Then format: 3 pts

---

## Part 2 — Epic Decomposition (35 points)

### Part 2 Instructions

The following two epics are too large to complete in a single Sprint. For each epic, decompose it into 3–4 Sprint-sized user stories using one or more story-splitting patterns from the list below.

Story-splitting patterns:

- Split by user type or persona (different users need different capabilities)
- Split by workflow step (break a multi-step process into individual steps)
- Split by data type or variation (handle different data formats or categories separately)
- Split by happy path vs. edge cases (implement the main scenario first, then add error handling)
- Split by CRUD operations (Create, Read, Update, Delete as separate stories)

### Epic A: Account Management

As a registered user, I can fully manage my account including my profile information, security settings, notification preferences, saved payment methods, and account deactivation.

For each sub-story you write, include:

- User story in standard format
- The splitting pattern you used (label it)
- Story Point estimate (Fibonacci scale)
- 2 acceptance criteria in Given/When/Then format

### Epic B: Product Review System

As a customer, I can read, write, and manage product reviews including star ratings, text reviews, photos, and the ability to mark reviews as helpful or report inappropriate content.

For each sub-story you write, include the same four items as Epic A.

### Part 2 Grading (35 points)

- Epic A decomposition (3–4 stories): 17 points (correct splitting pattern 3, story format 2, estimate 2, 2 ACs 10 — scoring per story)
- Epic B decomposition (3–4 stories): 18 points (same breakdown)

---

## Part 3 — User Story Quality Review (35 points)

### Part 3 Instructions

The following six user stories are poorly written. For each story:

1. Identify every problem with the story (using the INVEST criteria and common mistake categories from the Reading Guide)
2. Rewrite the story to fix all identified problems
3. Write 2 acceptance criteria in Given/When/Then format for the rewritten story

### Stories to Evaluate and Rewrite

Story A: As a user, I want the app to work fast.

Story B: As a user, I want to be able to search, filter, sort, bookmark, compare, share, and purchase products.

Story C: The database will be indexed on the user_id and session_token columns to improve query performance.

Story D: As an admin, I can do everything related to user management.

Story E: As a customer, I can check out.

Story F: As a member, I can view my activity history so that I can see my activity history.

### Part 3 Grading (35 points)

Each story review (6 stories):

- Problem identification (all issues named): 2 pts
- Rewritten story (correct format, all problems fixed): 2 pts
- 2 acceptance criteria in Given/When/Then: 2 pts

Note: Two stories score 6 pts each (Stories A and B are worth more due to complexity); four stories score 5 pts each — totaling 35 points.

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Six requirement-to-user-story conversions with acceptance criteria
2. Part 2: Epic A and Epic B decompositions with all required fields
3. Part 3: Six story quality reviews with problem identification, rewrites, and acceptance criteria

Submit to the Canvas assignment portal by the module due date.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Requirement Conversion (6 × 5 pts) | 30 |
| Part 2 — Epic Decomposition (A and B) | 35 |
| Part 3 — User Story Quality Review (6 stories) | 35 |
| Total | 100 |

---
