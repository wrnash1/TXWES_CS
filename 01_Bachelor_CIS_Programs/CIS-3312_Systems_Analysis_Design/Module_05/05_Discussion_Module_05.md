# Discussion Forum: Module 05 - Use Case Modeling and User Stories

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Your initial post must address all three sub-questions for your chosen scenario.

Initial Post: Due Wednesday at 11:59 PM (175–225 words)

Peer Responses: Due Sunday at 11:59 PM (reply to at least two classmates who chose different scenarios; minimum 75 words each)

---

## Scenario A: The Missing Extend

A BA has delivered a use case diagram for a new airline check-in system. The diagram shows actors (Passenger, Gate Agent, Frequent Flyer System) and use cases (Check In, Select Seat, Add Baggage, View Boarding Pass, Upgrade Seat). A senior BA reviewer looks at the diagram and says: "Your model assumes everything goes right. What happens if a passenger tries to check in but their flight has been cancelled? What about seat upgrades for passengers who are not Frequent Flyers?" The reviewer also notes that two use cases share an identical sub-flow — both "Check In" and "Add Baggage" require the system to verify the passenger's identity — but the BA has duplicated this behavior rather than using an include relationship.

Sub-questions:

1. Explain what the reviewer means about the model only showing what goes right, and describe at least two extend relationships the BA should add to address the reviewer's concerns. Include the condition note for each.
2. The duplicated identity verification sub-flow is a modeling error. Explain which use case relationship should be used to fix it and how it would be represented in the diagram.
3. Use case diagrams show scope but not sequence. How should the BA communicate the step-by-step interaction for the "Check In" use case — including the exception path for a cancelled flight — to the development team?

---

## Scenario B: User Stories Without a "Why"

A product owner hands the BA a backlog of 12 user stories for a new expense reporting system. The BA reviews them and notices that 7 of the 12 stories follow the format "As a finance employee, I want [feature]" — they are missing the "so that [value]" component. The product owner says: "The 'so that' part is obvious — we all know why we need expense reporting. Do we really need to write it down?" The BA also flags three stories as epics that need to be broken down before sprint planning.

Sub-questions:

1. Explain why the "so that [value]" component of a user story is not just a formatting requirement but a functional necessity for the development team. Give a specific example of how omitting the value statement could lead to building the wrong feature.
2. Choose one of the two epic scenarios below and demonstrate how you would split it into at least two sprint-sized stories. Explain why each resulting story satisfies the Small and Independent INVEST criteria. Epic options: (a) "As a manager, I want to approve, reject, and audit all expense reports for my team so that I can control costs and ensure policy compliance." (b) "As an employee, I want to submit, track, and receive reimbursement for my business expenses so that I am paid back promptly."
3. The product owner has stated that the "so that" documentation is unnecessary overhead. Describe how you would respond to this professionally, referencing the BA's responsibility to ensure requirements quality.

---

## Scenario C: Use Case vs. User Story Debate

A development team is transitioning from Waterfall to Agile Scrum. The senior systems analyst on the team (12 years of experience with use cases) argues that use cases are more rigorous and complete than user stories, and that switching to user stories will sacrifice requirement quality. The new Agile coach argues that user stories are more collaborative and that use cases are over-documentation that slows the team down. The BA is asked to help the team reach a practical working agreement.

Sub-questions:

1. Evaluate the senior analyst's concern about rigor. Identify at least one legitimate advantage of use case specifications over user stories for capturing complex interactions, and one situation where user stories are clearly superior.
2. Evaluate the Agile coach's concern about over-documentation. Identify one specific type of system requirement or interaction that actually benefits from the formal structure of a use case specification, even in an Agile context.
3. As the BA, propose a practical hybrid approach that respects both perspectives. Your proposal should specify when use cases would be used and when user stories would be used on the same project, with a clear rule for deciding which format applies in each situation.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5–6 pts | Addresses all three sub-questions with specific evidence from the scenario. Uses correct use case and user story terminology. Meets the 175–225 word count. |
| 3–4 pts | Addresses most sub-questions but lacks specificity or misuses terminology. Slightly outside the word count. |
| 1–2 pts | Addresses only one sub-question or provides only vague, generic responses. |
| 0 pts | No initial post submitted by the deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Responds to at least two classmates who chose different scenarios. Each reply is at least 75 words and adds substantive analysis. |
| 2 pts | Responds to only one classmate, or both responses are fewer than 75 words or superficial. |
| 0 pts | No peer responses submitted. |

---

## A Note from Professor Nash

Use cases and user stories are both right. The question is always: what does your audience need to understand, and what level of detail helps them build the correct thing? A use case specification for a complex multi-party workflow gives developers a roadmap they could not extract from a three-line user story card. A user story for a simple notification feature gives the team what they need without burying it in 12 pages of alternate flows for scenarios that will never happen. Professional judgment means knowing the difference.
