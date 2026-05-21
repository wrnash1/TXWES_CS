# Reading Guide: Module 07 – User Stories and Acceptance Criteria

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Introduction

Welcome to **Module 07 – User Stories and Acceptance Criteria**! User stories are the most widely used format for expressing Product Backlog items in Agile teams. While the Scrum Guide does not mandate user stories specifically, the PSM I exam environment assumes familiarity with them as a common Scrum practice.

This module covers the anatomy of a well-formed user story, the role of acceptance criteria in defining "done" at the story level, and the INVEST criteria for evaluating story quality. These skills bridge the gap between Scrum theory and the practical day-to-day work of a Scrum team.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **User story:** A short, informal description of a software feature written from the perspective of an end user, following the format: "As a [type of user], I want [some goal] so that [some reason]." User stories encourage conversation between the Product Owner, stakeholders, and Developers rather than serving as a complete specification.

* **Acceptance criteria:** Specific, testable conditions that a user story must satisfy to be considered complete. Acceptance criteria define the boundary of a story's scope and are agreed upon between the Product Owner and Developers before work begins. They are distinct from the Definition of Done, which applies to all Increments.

* **INVEST criteria:** A checklist for evaluating user story quality, where each letter represents a quality attribute: Independent (can be developed without depending on other stories), Negotiable (details are open to discussion), Valuable (delivers value to the user or business), Estimable (the team can size it), Small (fits within a Sprint), Testable (acceptance criteria can be verified). Stories that fail INVEST criteria should be refined or split.

* **Story splitting:** The practice of decomposing a large user story (an "epic") into smaller, independently deliverable stories that each fit within a Sprint. Common splitting patterns include splitting by workflow steps, data variations, user roles, happy/unhappy paths, and operational boundaries.

* **Epic:** A large user story or feature too big to complete in a single Sprint that must be broken down into smaller stories before it can be selected for Sprint Planning. Epics are valid Product Backlog items but are not ready for a Sprint until split into appropriately sized stories.

---

### 2. Certification Exam Tips

* **PSM I Focus — User stories are not required by the Scrum Guide:** A common trap presents user stories as a Scrum requirement. They are not. The Scrum Guide says Product Backlog items should have a description, order, and estimate — but does not prescribe format. User stories are a widely adopted practice, not a Scrum rule.
* **Scenario Trap — Acceptance criteria vs. Definition of Done:** Acceptance criteria are story-specific conditions agreed between the Product Owner and Developers. The Definition of Done applies to all Increments as a quality floor. A story can meet its acceptance criteria but still not meet the DoD — in which case it is not done.
* **INVEST — Negotiable does not mean changeable at will:** The "N" in INVEST means the details of a story should be open for conversation before the Sprint begins — not that scope can be changed mid-Sprint. Once a story is in the Sprint Backlog, it is committed to the Sprint Goal.
* **"As a user" is not enough:** A vague actor in a user story (e.g., "as a user") produces vague acceptance criteria. Good stories name a specific role with specific needs, leading to more testable acceptance criteria.
* **Study Resource:** [The Scrum Guide (2020)](https://scrumguides.org/) does not cover user stories directly. Supplement with the [Agile Alliance user story guide](https://www.agilealliance.org/glossary/user-stories/) and Mike Cohn's *User Stories Applied* (available via library or OpenLibrary).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** [User Stories — Agile Alliance Glossary](https://www.agilealliance.org/glossary/user-stories/) — the Agile Alliance's free definition covering story format, INVEST criteria, and the relationship between stories and acceptance criteria.
* **Required Video:** [Writing Good User Stories and Acceptance Criteria – Agile for Humans](https://www.youtube.com/watch?v=tKSUokG3a0g) — practical examples of strong vs. weak user stories and how to write acceptance criteria using Given-When-Then format. (~14 min)

---

### Lab & Command Integration

In this week's hands-on lab, you will:

* **Write user stories from a product brief:** Given a one-paragraph product description, write five user stories in the standard "As a / I want / So that" format, each targeting a distinct user role and delivering specific value.
* **Add acceptance criteria using Given-When-Then:** For each of your five user stories, write at least two acceptance criteria using the Gherkin Given-When-Then format, ensuring each criterion is independently testable.
* **Apply INVEST to evaluate story quality:** Score each of your five stories against the INVEST criteria and identify any that need to be split, refined, or clarified before they would be ready for Sprint Planning.

---

### 3. Study Checklist

* [ ] Read the Agile Alliance user story glossary entry and memorize the INVEST criteria.
* [ ] Be able to write a user story in the standard format without referring to notes.
* [ ] Understand the difference between acceptance criteria (story-level) and the Definition of Done (increment-level).
* [ ] Watch the required video and practice writing at least two Given-When-Then acceptance criteria.
* [ ] Proceed to the weekly hands-on lab activity.
