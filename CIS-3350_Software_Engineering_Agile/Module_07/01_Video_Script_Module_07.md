# Video Script: Module 07 – User Stories and Acceptance Criteria

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Estimated Duration:** 20 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Show before/after examples of user story transformations prominently

---

## Section 1 — Welcome and Why User Stories Matter [00:00–03:00]

"Welcome to Module 7. We have covered the Product Backlog as a structure — what it is, who owns it, and how it is maintained. This module goes inside the Product Backlog and examines its most common content type: the user story.

User stories are not unique to Scrum — they come from the Extreme Programming (XP) community and were popularized by Ron Jeffries and Kent Beck in the late 1990s. They have become the dominant way of expressing Product Backlog items in Agile teams because they naturally keep the conversation focused on what users need rather than what systems must do.

By the end of this module you will be able to:

- Write user stories in the standard format with all three components
- Explain what acceptance criteria are and why they are necessary
- Write acceptance criteria in Given/When/Then format
- Apply the Three Cs — Card, Conversation, Confirmation — to understand what a user story really is
- Identify poorly written user stories and rewrite them
- Explain the difference between a user story, an epic, and a task

Let's begin."

---

## Section 2 — The User Story Format and the Three Cs [03:00–09:00]

"A user story is a lightweight way to express a requirement from the perspective of the person who will use the feature. The standard format is: As a [user type], I can [action] so that [benefit].

[SHOW DIAGRAM: User story template with three labeled parts — Who (As a...), What (I can...), Why (so that...)]

Let me break down each component.

As a [user type]: The user type should be a specific role or persona — not just 'user.' 'As a customer' is better than 'as a user.' 'As a returning customer who has saved payment methods' is even better when the distinction matters. Being specific about the user type forces the team to understand whose problem they are solving.

I can [action]: The action describes what the user can do. It should be expressed in terms of user behavior, not system implementation. 'I can filter search results by price range' focuses on what the user does. 'The system shall implement a filtering algorithm' focuses on the implementation — that is requirements specification language, not user story language.

So that [benefit]: This is the most important and most often omitted part. The 'so that' clause explains why this feature matters — what value it creates for the user. Without it, the team is building features without understanding their purpose. 'So that I can find products within my budget without scrolling through irrelevant results' is the reason this feature should exist.

PSM I Exam Tip: User stories with no 'so that' clause are a common indicator of a poorly refined backlog. The 'so that' clause is what makes the story valuable and testable.

Now, Ron Jeffries described user stories using the Three Cs model, which captures what a user story actually is.

[SHOW DIAGRAM: Three circles — Card, Conversation, Confirmation — overlapping, with a brief description in each]

Card: The written user story is a short record — just enough to remind the team what needs to be discussed. The Card is not a complete specification. 'As a customer, I can save my payment method for future purchases' is sufficient to start a conversation.

Conversation: The real content of a user story is the conversation it enables between the Product Owner, Developers, and stakeholders. The story is a placeholder for a richer discussion about what the feature should do, why it matters, and how it will be built.

Confirmation: Acceptance criteria are the written confirmation of what 'done' means for this story. They transform the vague story into a testable commitment."

---

## Section 3 — Acceptance Criteria and Given/When/Then [09:00–15:30]

"Acceptance criteria are the conditions that must be satisfied for a user story to be considered Done. They answer the question: how will we know this story is complete?

Well-written acceptance criteria are:

- Specific: they describe exact behaviors, not vague qualities
- Testable: you can write an automated or manual test that definitively passes or fails
- Complete: they cover the main scenario and important edge cases
- Understood: both the Product Owner and the Developers agree on what they mean

[SHOW DIAGRAM: User story with three acceptance criteria below it, formatted as Given/When/Then statements]

The most common format for acceptance criteria in Agile teams is Given/When/Then, also called BDD (Behavior-Driven Development) format. Let me explain each component.

Given: The initial context or precondition. What state is the system in before the behavior occurs? Who is the user and what have they already done?

When: The action or trigger. What does the user do, or what event occurs?

Then: The expected outcome. What observable result does the user or system produce?

Let me give you an example with a complete user story.

User story: As a registered customer, I can reset my password so that I can regain access to my account when I forget my credentials.

Acceptance Criterion 1:
Given a customer is on the login page and clicks 'Forgot Password,'
When they enter their registered email address and click Submit,
Then they receive an email with a secure password reset link within two minutes.

Acceptance Criterion 2:
Given a customer has received a password reset link,
When they click the link within 24 hours and enter a new password meeting the complexity requirements,
Then their password is updated and they are redirected to the dashboard.

Acceptance Criterion 3:
Given a customer has received a password reset link,
When they try to use the link after 24 hours have passed,
Then the link is expired and they see an error message prompting them to request a new one.

Notice that the third criterion covers an edge case — the expired link scenario. Good acceptance criteria always think through the 'what could go wrong' scenarios, not just the happy path.

PSM I Exam Tip: Acceptance criteria are item-specific — they define Done for a particular user story. They are distinct from the Definition of Done, which applies to every Increment regardless of which stories it contains. Both can appear in the same context; knowing the difference is a PSM I exam point."

---

## Section 4 — Epics, Stories, and Tasks [15:30–18:30]

"Before we close, let me explain the hierarchy of work items that teams commonly use, because PSM I questions sometimes test this hierarchy.

[SHOW DIAGRAM: Three-tier pyramid — Epic at top, Stories in the middle, Tasks at the bottom — with size arrows on the side]

An Epic is a large, coarse-grained user story that is too big to complete in one Sprint. Epics are common at the top of a new Product Backlog, when requirements are understood at a high level but not yet decomposed. Epics must be broken down into smaller stories through Product Backlog Refinement before they can be selected for a Sprint.

Example Epic: 'As a user, I can manage my account.' This is far too large for a Sprint — it contains password management, profile editing, notification preferences, billing information, and much more.

A User Story is a story that is small enough to be completed within one Sprint. When refined properly, it meets the INVEST criteria from Module 6. User stories are the primary unit of work in a Scrum Sprint.

A Task is a specific technical activity that a Developer performs to implement a user story. Tasks are created during Sprint Planning and live in the Sprint Backlog. They are not Product Backlog items — they are the implementation details of the plan.

Example: For the user story 'As a customer, I can filter products by price range,' the tasks might include: design the filter UI component, implement the filter API endpoint, write unit tests for the filter logic, test filter integration with the product catalog.

PSM I Exam Tip: Product Backlog items (user stories) are managed by the Product Owner. Tasks are created by the Developers during Sprint Planning and managed by the Developers in the Sprint Backlog. These are different levels of the work hierarchy."

---

## Section 5 — Common User Story Mistakes [18:30–20:00]

"Let me close with the most common user story mistakes I see in practice.

Mistake 1: No 'so that' clause. Writing 'As a user, I can view my order history' without explaining why misses half the story. The purpose of the feature determines how it should be designed.

Mistake 2: Technical stories without a user perspective. 'The system shall use Redis for caching' is a technical decision, not a user story. If it needs to be in the backlog, write it as: 'As a user, I experience page loads under one second so that I can navigate the app without frustration' — and the team's technical approach (Redis caching) emerges from the conversation.

Mistake 3: Acceptance criteria written as UI specifications. 'The button is blue with a 16px font' is a design spec, not an acceptance criterion. A better AC: 'When the user submits the form, the confirmation button is clearly visible and does not require scrolling on standard mobile screen sizes.'

Mistake 4: One giant story for a whole feature. If your story takes three Sprints, it is an epic. Break it down.

In Module 8 we cover estimation — how teams assign story points to user stories and how Planning Poker works as an estimation technique. See you there."

---

## End Card

- Next module: Module 08 – Estimation: Story Points and Planning Poker
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
