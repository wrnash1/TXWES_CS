# Reading Guide: Module 07 – User Stories and Acceptance Criteria

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

User stories are the most common way of expressing Product Backlog items in Agile teams. They capture requirements from a user perspective, keep conversations focused on value, and — when combined with well-written acceptance criteria — create a testable, shared understanding of Done. This guide covers user story format, the Three Cs model, acceptance criteria in Given/When/Then format, the work item hierarchy (epics, stories, tasks), and the most common user story quality problems.

---

## 1. What a User Story Is

A user story is a short, simple description of a feature told from the perspective of the person who desires the new capability, usually a user or customer of the system. User stories emerged from the Extreme Programming (XP) community, popularized by Ron Jeffries' Three Cs model, and have become the standard way of describing Product Backlog items in Scrum teams worldwide.

User stories are deliberately not comprehensive specifications. They are promises for a conversation — lightweight records that prompt discussion between the Product Owner, Developers, and stakeholders during refinement and Sprint Planning.

### The Standard User Story Format

As a [user type], I can [action] so that [benefit].

- As a [user type]: identifies who needs the capability. Should be specific — not just "user," but "registered customer," "system administrator," "first-time visitor," or a named persona.
- I can [action]: describes what the user wants to do. Written from the user's perspective, not the system's. Focuses on behavior, not implementation.
- So that [benefit]: explains why the user needs this capability — the value it creates. This clause is critical for understanding priority and validating that the story is worth building.

### Full User Story Example

As a small business owner, I can generate a monthly expense summary report in PDF format so that I can share financial summaries with my accountant without manual data entry.

---

## 2. The Three Cs Model

Ron Jeffries described user stories using three components that together constitute what a story really is:

### Card

The Card is the written representation of the story — the brief text recorded on an index card, sticky note, or in a project management tool. The Card is not a specification; it is a reminder of what needs to be discussed. Its brevity is intentional: it invites conversation rather than substituting for it.

### Conversation

The Conversation is the real content of the user story. It is the dialogue between the Product Owner, Developers, and stakeholders that fills in the details, resolves ambiguities, and surfaces constraints. The Conversation happens during Product Backlog Refinement and Sprint Planning. The Card exists to prompt and guide this conversation.

A story that has never been discussed is a story that is not ready for development. Developers who start work on a story they have not discussed with the Product Owner frequently discover mid-Sprint that their assumptions were wrong.

### Confirmation

The Confirmation is the acceptance criteria — the written agreement about what Done means for this story. Acceptance criteria transform a vague story into a testable commitment. They are the record of the key points from the Conversation that the team wants to formalize as quality expectations.

---

## 3. Acceptance Criteria and Given/When/Then

### What Acceptance Criteria Are

Acceptance criteria are specific conditions that a user story must satisfy to be considered complete. They define the boundaries of the story — what is in scope and what is out — and provide the basis for testing.

Quality acceptance criteria are:

- Specific: they describe exact, observable behavior
- Testable: a test can be written that definitively passes or fails
- Unambiguous: both the Product Owner and Developers interpret them the same way
- Covering the happy path and key edge cases: the main scenario and important failure/edge scenarios

### Given/When/Then Format

The most common format for acceptance criteria in Agile teams is Given/When/Then, also known as Gherkin format or BDD (Behavior-Driven Development) format.

Structure:

- Given [initial context or precondition]: what state is the system in before the behavior occurs?
- When [action or trigger]: what does the user do, or what event occurs?
- Then [expected outcome]: what observable result does the user or system produce?

### Complete Example

User story: As a registered customer, I can reset my password so that I can regain access to my account when I forget my credentials.

Acceptance Criterion 1 — Happy path:

Given a registered customer is on the login page and clicks "Forgot Password,"
When they enter their registered email address and click Submit,
Then they receive an email with a secure password reset link within two minutes.

Acceptance Criterion 2 — Successful reset:

Given a customer has received a valid password reset link,
When they click the link within 24 hours and enter a new password meeting complexity requirements (minimum 8 characters, one uppercase, one number),
Then their password is updated and they are redirected to their dashboard with a success message.

Acceptance Criterion 3 — Expired link:

Given a customer has received a password reset link,
When they click the link after 24 hours have elapsed,
Then the link is expired, a clear error message is displayed, and they are prompted to request a new link.

Acceptance Criterion 4 — Unregistered email:

Given a visitor is on the Forgot Password page,
When they enter an email address that is not associated with any account and click Submit,
Then they see a generic confirmation message (to prevent email enumeration attacks) without revealing whether the address is registered.

---

## 4. User Stories vs. Acceptance Criteria vs. Definition of Done

This distinction is frequently tested on PSM I:

| Item | What It Defines | Scope | Owner |
|---|---|---|---|
| User Story | The feature need from the user's perspective | One backlog item | Product Owner (with team input) |
| Acceptance Criteria | The specific conditions for this story to be Done | One backlog item | Product Owner (confirmed with Developers) |
| Definition of Done | The quality standards every Increment must meet | All Increments | Scrum Team (Developers primarily) |

The Definition of Done applies universally — every Increment, regardless of which stories it contains, must meet the DoD. Acceptance criteria are item-specific — they apply only to the story they belong to. A story may meet all its acceptance criteria but still fail the Definition of Done if, for example, the DoD requires code review and code review was not performed.

---

## 5. Work Item Hierarchy: Epics, Stories, and Tasks

### Epics

An Epic is a large user story that is too big to complete in one Sprint. Epics represent high-level features or capabilities that will require multiple stories to implement fully. They sit at the top of the Product Backlog when a product is new or a major capability is first being described.

Epics must be decomposed into user stories through Product Backlog Refinement before they are ready for Sprint Planning. A story that takes more than one Sprint to complete is too large and should be treated as an epic until it is split.

Example Epic: "As a customer, I can manage my subscription." This encompasses billing management, plan changes, cancellation, payment method updates, and invoice history — multiple Sprints of work.

### User Stories (Sprint-ready)

User stories are refined, Sprint-sized items that meet the INVEST criteria. They are the unit of work the team commits to during Sprint Planning and the items that are demonstrated at Sprint Review.

### Tasks

Tasks are the technical activities Developers create during Sprint Planning to plan how they will implement a user story. Tasks live in the Sprint Backlog, not the Product Backlog. They are created by the Developers and are at a finer grain than stories — typically one to eight hours of work each.

Tasks are not user-facing; they are implementation activities. "Write unit tests for the password reset endpoint" is a task, not a user story.

---

## 6. Common User Story Mistakes

Mistake 1 — Missing "so that" clause: "As a user, I can search for products" omits the benefit. Why do they want to search? The benefit clause is what enables the team to evaluate priority and test whether the feature actually delivers value.

Mistake 2 — System-centric stories: "The system shall implement Redis caching for product pages" is a technical decision written in system-specification language. Rewrite as a user story with a user benefit, then let the implementation approach emerge from the team's conversation.

Mistake 3 — Acceptance criteria as UI specifications: "The submit button will be blue with a 16px Helvetica font" is a design spec. Acceptance criteria should describe behavior and outcome, not visual design details.

Mistake 4 — Stories too large for one Sprint: Stories that cannot be completed in one Sprint must be split. Common splitting patterns include splitting by user type, by workflow step, by data type, or by happy path vs. edge cases.

Mistake 5 — No acceptance criteria: Stories without acceptance criteria have no confirmation — the "C" in the Three Cs is missing. The team does not know when they are done, leading to ambiguous Sprint Reviews and Definition of Done disputes.

---

## 7. PSM I Exam Tips

Tip 1: User stories are not mandated by the Scrum Guide. The Scrum Guide does not prescribe how Product Backlog items are written. User stories are a common practice, not a Scrum rule. PSM I questions that ask about mandatory formats for PBIs are testing this knowledge.

Tip 2: Acceptance criteria are item-specific; the Definition of Done applies to all Increments. Both must be satisfied for a story to be truly Done.

Tip 3: The "so that" clause is the most important part of a user story from a value perspective. Stories without it cannot be prioritized by value because value is unstated.

Tip 4: The Three Cs — Card, Conversation, Confirmation — describe what a user story actually is. Know these terms and what each represents.

Tip 5: An epic is a large user story, not a Scrum framework element. The Scrum Guide does not use the word "epic." It is a common practice term, not an official Scrum term.

Tip 6: Tasks are created by Developers during Sprint Planning and live in the Sprint Backlog. They are not Product Backlog items.

Tip 7: Given/When/Then acceptance criteria format is a BDD (Behavior-Driven Development) practice. It is widely used with Scrum but is not mandated by the Scrum Guide.

Tip 8: PSM I questions about user stories often present poorly written stories and ask what is wrong with them. Apply the INVEST criteria and look for missing "so that" clauses, overly large stories, and non-testable acceptance criteria.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 07 topics:

**1. "User Stories" — Agile Alliance Glossary**
<https://www.agilealliance.org/glossary/user-stories/>
The Agile Alliance's canonical glossary entry on user stories. Covers the Three Cs model, the standard format, common variations, and the distinction between user stories and traditional requirements. Includes references to further reading.

**2. "Introduction to Given When Then" — Martin Fowler**
<https://martinfowler.com/bliki/GivenWhenThen.html>
A concise explanation of the Given/When/Then (Gherkin) acceptance criteria format by a Manifesto signatory. Explains the relationship between BDD (Behavior-Driven Development) and Agile acceptance testing. Free access on martinfowler.com.

**3. "Story Splitting Flowchart" — Richard Lawrence**
<https://www.agileforall.com/splitting-user-stories/>
A free, practical guide to splitting user stories with a flowchart decision tree. Covers ten splitting patterns with worked examples. Highly useful for the epic decomposition exercises in this module's lab. Free access on agileforall.com.

---

## 8. Study Checklist

- [ ] Write five user stories in the standard format for an app of your choice
- [ ] For each story, write 2–3 acceptance criteria in Given/When/Then format
- [ ] Explain the Three Cs model: what is the Card, what is the Conversation, and what is the Confirmation?
- [ ] Explain the difference between acceptance criteria and the Definition of Done
- [ ] Define Epic, User Story, and Task and explain how they differ in scope and ownership
- [ ] Identify five common user story mistakes and rewrite one poorly written story to fix all five
- [ ] State whether user stories are required by the Scrum Guide (they are not)
- [ ] Complete this module's Lab and Quiz

---
