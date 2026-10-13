# Quiz: Module 03 - Requirements Elicitation Techniques

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

A business analyst is working with a call center team whose members struggle to explain their daily tasks verbally but perform complex workarounds that are not documented anywhere. Which elicitation technique is most appropriate?

A) Survey / Questionnaire

B) Document Analysis

C) Observation (Job Shadowing)

D) Focus Group

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Surveys require stakeholders to articulate their knowledge in written form; they cannot capture tacit or undocumented knowledge.
- Why B is incorrect: Document analysis reviews existing artifacts; it cannot capture undocumented workarounds that exist only in practitioners' heads.
- Why D is incorrect: Focus groups elicit opinions and reactions from a group; they are not well-suited for capturing procedural tacit knowledge.
- Why C is correct: Observation allows the BA to directly witness and document tasks as they are actually performed, making it the ideal technique for capturing tacit knowledge and undocumented processes.

---

## Question 2

In the context of requirements elicitation, which of the following is the most accurate definition of a requirements workshop?

A) A formal written survey distributed to all stakeholders asking them to rank requirements by priority using a numbered scale

B) A one-on-one structured conversation between the BA and a single subject matter expert conducted over several sessions

C) A facilitated, time-boxed meeting that brings multiple stakeholders together to collaboratively elicit, discuss, and agree on requirements

D) An automated tool that scans existing system code to extract implied business rules and generate a draft requirements document

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: This describes a survey/questionnaire technique, not a workshop.
- Why B is incorrect: This describes a structured interview with a single stakeholder, which is a distinct elicitation technique.
- Why D is incorrect: Automated code scanning is a reverse-engineering tool, not an elicitation technique in the BABOK sense.
- Why C is correct: BABOK Guide v3 defines workshops (including JAD sessions) as collaborative, facilitated group sessions specifically designed to achieve stakeholder consensus on requirements efficiently.

---

## Question 3

After conducting twelve stakeholder interviews, a BA has compiled detailed notes from each session. According to BABOK Guide v3 KA 4, what must the BA do before treating these notes as confirmed elicitation results?

A) Convert the notes directly into a formal requirements specification document and submit it for project manager approval

B) Review the notes with the relevant stakeholders to verify accuracy and obtain their confirmation of what was captured

C) Archive the notes in the project repository and proceed immediately to requirements analysis

D) Distribute the notes to the development team so they can begin estimating implementation effort

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Converting unverified notes directly into a specification skips the critical confirmation step and risks embedding misunderstandings into the requirements baseline.
- Why C is incorrect: Archiving and proceeding without confirmation leaves errors and misinterpretations uncorrected.
- Why D is incorrect: Distributing unconfirmed notes to developers before stakeholder review risks development effort based on incorrect information.
- Why B is correct: BABOK task "Confirm Elicitation Results" specifically requires reviewing captured information with stakeholders to ensure accuracy before moving forward.

---

## Question 4

A BA needs to quickly gather input from 200 geographically dispersed stakeholders about which system features they use most frequently and which pain points are most critical. Which elicitation technique is most practical?

A) Individual structured interviews with each of the 200 stakeholders

B) Observation sessions scheduled across all 200 stakeholder locations

C) A facilitated in-person workshop requiring all 200 stakeholders to travel to headquarters

D) A structured survey or questionnaire distributed electronically to all 200 stakeholders

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: Interviewing 200 individuals is not practical due to the time and coordination cost; interviews are more effective for smaller, high-priority stakeholder groups.
- Why B is incorrect: Observation across 200 distributed locations is logistically infeasible for initial broad input gathering.
- Why C is incorrect: Requiring 200 stakeholders to travel is cost-prohibitive and creates scheduling conflicts that make the approach impractical.
- Why D is correct: Surveys are the most efficient technique for collecting structured input from a large, geographically dispersed audience and are explicitly identified in BABOK as appropriate for breadth-first information gathering.

---

## Question 5

During an elicitation workshop, several stakeholders from different departments provide conflicting requirements about how the system should handle customer refunds. The BA captures all positions but does not resolve the conflict during the session. Which BABOK task should the BA perform next?

A) Immediately escalate all conflicting requirements to the CIO for a final decision

B) Select the requirement version from the department with the highest organizational authority and discard the others

C) Manage stakeholder collaboration by facilitating a conflict-resolution discussion to reach a negotiated agreement or escalate to the appropriate governance authority

D) Document both conflicting requirements as separate requirements and let developers choose which one to implement

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Escalating immediately without attempting to resolve the conflict at the stakeholder level skips the BA's facilitation responsibility and burdens executives with operational decisions.
- Why B is incorrect: Unilaterally discarding requirements based on organizational hierarchy rather than merit and business value will cause dissatisfaction and likely missed requirements.
- Why D is incorrect: Leaving conflict resolution to developers is inappropriate; developers are not authorized to make business decisions about requirements scope.
- Why C is correct: BABOK KA 4 includes the task "Manage Stakeholder Collaboration," which explicitly covers facilitating conflict resolution, negotiating compromises, and escalating to governance bodies when consensus cannot be reached.

---

## Question 6

A BA is preparing to observe a warehouse receiving team to document their inventory intake process. Two hours into the observation, the BA notices the team is following documented procedures very carefully, even checking steps they would normally skip. What phenomenon is the BA encountering?

A) Analysis paralysis — the team is overthinking their decisions because of the documentation pressure

B) The Hawthorne Effect — workers change their behavior when they know they are being observed

C) Confirmation bias — the BA is unconsciously noticing only behaviors that match existing assumptions

D) Scope creep — the team is adding steps to the process that are outside the BA's elicitation scope

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Analysis paralysis refers to decision-making delays, not behavioral change during observation.
- Why C is incorrect: Confirmation bias is an error in the observer's perception, not a behavioral change by the observed workers.
- Why D is incorrect: Scope creep refers to expanding project scope, not behavioral change during an observation session.
- Why B is correct: The Hawthorne Effect is the well-documented tendency for people to modify their behavior when they know they are being watched. It is a named limitation of the observation elicitation technique; the BA should conduct multiple sessions over time until natural behavior resumes.

---

## Question 7

A BA is planning elicitation for a complex actuarial pricing model used by only two senior actuaries who can perform their calculations fluently but find it very difficult to explain the process in words. Which combination of techniques is most likely to produce complete, accurate elicitation results?

A) Survey followed by document analysis

B) Large group workshop with all actuarial department staff

C) Structured interview followed by prototyping

D) Focus group with actuaries and IT staff together

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Surveys require written articulation, which the actuaries cannot do well; document analysis alone will not capture the judgment and nuance in their calculations.
- Why B is incorrect: Only two actuaries are involved; a large group workshop is unnecessarily broad and introduces participants whose input would not clarify the specialized actuarial process.
- Why D is incorrect: Mixing technical staff with IT staff may produce requirements influenced by technical constraints rather than pure actuarial needs, and does not address the verbal articulation limitation.
- Why C is correct: A structured interview surfaces what the actuaries can articulate; prototyping then gives them something concrete to react to, surfacing tacit requirements they could not verbalize — a highly effective two-phase approach for specialist, hard-to-articulate processes.

---

## Question 8

After a requirements workshop, one participant emails the BA saying: "I reviewed my notes and I think I miscommunicated our inventory threshold rule — it should be 50 units, not 500 units." The BA has already shared the raw workshop notes with the team. What step in BABOK KA 4 does this situation illustrate the importance of?

A) Prepare for Elicitation — the BA should have prepared better questions to avoid miscommunication

B) Confirm Elicitation Results — the review process caught an error before it became a formal requirement

C) Manage Stakeholder Collaboration — the stakeholder's email is an example of ongoing collaboration

D) Communicate Business Analysis Information — the BA should have sent a formatted summary report instead of raw notes

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Better preparation could reduce miscommunication risk, but the scenario specifically illustrates the value of the confirmation step after elicitation is complete.
- Why C is incorrect: While this is technically collaboration, the scenario specifically illustrates the purpose and value of the "Confirm Elicitation Results" task.
- Why D is incorrect: Communication format is a secondary concern; the fundamental point is that stakeholder review caught an error before it propagated into requirements.
- Why B is correct: This is a textbook example of why "Confirm Elicitation Results" is a required BABOK task. The stakeholder's review caught a critical error (50 vs. 500 units) before it became a baselined requirement. Without this step, the wrong threshold would have driven design, development, and testing.

---

## Question 9

A marketing VP says to the BA: "We need a tier system with Gold, Platinum, and Diamond levels based on customer spending." The BA writes this down as a requirement. What error has the BA made?

A) The BA failed to use a structured interview format and should restart the elicitation

B) The BA documented a proposed solution as a requirement rather than uncovering the underlying business need

C) The BA should have used observation rather than an interview to capture the VP's preferences

D) The BA violated the BABOK governance process by accepting a requirement directly from the VP

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: The interview format is not the issue; the problem is how the BA interpreted and recorded what the VP said.
- Why C is incorrect: Observation is for capturing work tasks and processes; it is not appropriate for gathering executive strategic preferences.
- Why D is incorrect: Receiving input from stakeholders including VPs is entirely appropriate; the governance process governs requirement approval, not elicitation.
- Why B is correct: The VP stated a solution (tier structure with spending thresholds) rather than a business need (e.g., "retain high-value customers and incentivize increased spending"). The BA's job is to probe the underlying need. The tier structure is a design option, not the requirement itself.

---

## Question 10

A BA is planning elicitation for a new accounts payable system with 45 stakeholders across five departments and a six-week deadline for the requirements baseline. Which sequencing of techniques is most efficient and thorough?

A) Survey all 45 stakeholders first, then conduct workshops with high-priority groups to resolve conflicts, then use observation with key users for process verification

B) Begin with prototyping, show all stakeholders the prototype, then document whatever feedback they provide as requirements

C) Conduct one-on-one interviews with all 45 stakeholders sequentially, then compile notes into a single requirements document

D) Begin with brainstorming with IT staff, then conduct focus groups with users, then present findings to the sponsor for approval

Correct Answer: A

Distractor Analysis:

- Why B is incorrect: Starting with a prototype before any requirements have been gathered frames the design before the BA understands the actual business need; it causes anchoring bias and inverts the correct sequence.
- Why C is incorrect: Interviewing all 45 stakeholders individually is prohibitively time-intensive for a six-week timeline; surveys efficiently gather initial breadth before investing time in focused follow-up sessions.
- Why D is incorrect: Starting with IT staff brainstorming rather than business stakeholders inverts the analysis — requirements must drive technical design, not the reverse.
- Why A is correct: Survey for broad input, then workshops to resolve conflicts and reach consensus, then observation to verify that documented processes match reality. This sequence balances breadth, depth, and verification within the time constraint.

---

## Question 11

A BA is planning elicitation for a retail ordering system. The business users have strong opinions about the new system but work across three time zones and cannot attend synchronous sessions. Which technique allows the BA to gather their initial input efficiently without requiring real-time availability?

A) Facilitated workshop requiring video attendance at a scheduled time

B) Structured survey distributed asynchronously via email

C) Individual observation sessions scheduled at each location

D) JAD session conducted over two full days at corporate headquarters

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: A synchronous workshop negates the geographic and time-zone advantage; it is impractical when participants cannot attend at the same time.
- Why C is incorrect: Individual observation sessions across multiple locations are time-intensive and costly for initial broad-input gathering.
- Why D is incorrect: A JAD session requires all participants in one place or at least synchronous attendance, which the scenario explicitly rules out.
- Why B is correct: Surveys are asynchronous, scalable, and geographically neutral. They are the correct choice when stakeholders are dispersed and cannot attend real-time sessions. Results are then used to inform targeted follow-up interviews or workshops.

---

## Question 12

During document analysis of a legacy payroll system, a BA finds a 200-page policy manual, a 50-page system user guide from 2006, and 12 years of change request logs. Which aspect of document analysis does this scenario highlight as most critical?

A) The BA should read every document front-to-back before starting any other elicitation

B) The BA must evaluate the currency and accuracy of each document, as outdated materials may not reflect current business rules

C) Document analysis should only be used when other techniques have failed to gather requirements

D) The BA should discard all documents older than five years as unreliable

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Reading all documents exhaustively before other elicitation is inefficient; document analysis is most valuable when combined with stakeholder interviews to confirm which documented rules are still in effect.
- Why C is incorrect: Document analysis is a primary, not last-resort, technique; it is especially valuable for legacy system replacement projects where undocumented behavior may exist only in old records.
- Why D is incorrect: Age alone does not make a document unreliable; a regulatory compliance rule from 15 years ago may still be fully in force.
- Why B is correct: The critical challenge in document analysis is verifying that the documents reflect current reality. Policies, procedures, and system guides frequently become outdated; the BA must cross-reference documents with stakeholder interviews to confirm which rules are still active.

---

## Question 13

A BA is facilitating a JAD session when two senior managers begin arguing over a business rule. The argument escalates and derails the session. Which BA action is most appropriate?

A) Let the managers continue until one concedes, since authority-based resolution is fastest

B) Adjourn the session immediately and report the conflict to the project manager

C) Acknowledge the disagreement, document both positions, table the item for offline resolution by the governance authority, and move the session forward to other agenda items

D) Remove the lower-ranking manager from the session to preserve senior management authority

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Allowing an unresolved argument to continue wastes the session time of all participants and may damage stakeholder relationships.
- Why B is incorrect: Adjourning immediately is a disproportionate response; other agenda items can still be addressed productively.
- Why D is incorrect: Removing participants based on rank is inappropriate and damages trust; it also risks losing domain knowledge the lower-ranking manager may hold.
- Why C is correct: The BA's facilitation role includes managing conflict without making business decisions. Documenting both positions, tabling the item, and forwarding to governance maintains session productivity and respects the established decision-making process.

---

## Question 14

A BA discovers during elicitation that users of the current system have developed an unofficial spreadsheet to track orders because the official system's reporting feature is broken. Which elicitation technique would have been most likely to uncover this workaround before it was mentioned?

A) Structured interview

B) Survey

C) Observation

D) Prototyping

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Structured interviews rely on stakeholders articulating their practices; users often do not mention workarounds because they consider them "just how things work."
- Why B is incorrect: Surveys are unlikely to surface undocumented workarounds because users answer questions about the official system, not their shadow processes.
- Why D is incorrect: Prototyping presents a proposed future-state design; it does not reveal current-state workarounds.
- Why C is correct: Observation captures what users actually do, not what they say they do. An analyst watching a user would immediately notice the unofficial spreadsheet being opened, prompting the investigation that uncovers the broken reporting feature.

---

## Question 15

Which of the following best describes the purpose of an elicitation "Prepare" activity in BABOK KA 4?

A) Scheduling all project meetings for the remainder of the analysis phase

B) Writing the requirements specification document outline before elicitation begins

C) Reviewing existing information, selecting the appropriate technique, and preparing materials and questions before conducting an elicitation event

D) Obtaining sign-off from the project sponsor on the elicitation plan

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Scheduling meetings is a logistics activity, not the BA preparation described in KA 4.
- Why B is incorrect: Writing a requirements specification outline is a premature design of the requirements document; it belongs after elicitation, not before.
- Why D is incorrect: Sponsor sign-off on an elicitation plan is a governance activity; while sometimes appropriate, it is not the definition of "Prepare for Elicitation."
- Why C is correct: BABOK KA 4 task "Prepare for Elicitation" covers reviewing existing documentation, understanding stakeholder context, selecting the appropriate elicitation technique, and creating supporting materials (question guides, prototypes, surveys) before the session begins.

---

## Question 16

A BA asks a stakeholder: "Walk me through a typical day handling customer complaints from start to finish." This is best classified as which type of interview question?

A) Closed-ended question

B) Leading question

C) Open-ended question

D) Hypothetical scenario question

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: A closed-ended question elicits a yes/no or short specific answer (e.g., "Do you handle more than 20 complaints per day?"). This question invites a narrative.
- Why B is incorrect: A leading question suggests the desired answer; this question is neutral and exploratory.
- Why D is incorrect: A hypothetical scenario question presents a future or imagined situation (e.g., "What would you do if...?"); this question asks about current practice.
- Why C is correct: "Walk me through..." is a classic open-ended question that invites the stakeholder to provide a detailed narrative response, surfacing process steps, decisions, and pain points the BA might not have thought to ask about directly.

---

## Question 17

A BA is using prototyping as an elicitation technique. A stakeholder reviews the prototype and immediately says: "That's not what I meant at all — the report needs to show weekly totals, not daily." What value does this response demonstrate about prototyping?

A) Prototyping is too expensive because it requires building a working system before requirements are confirmed

B) Prototyping surfaces requirements that stakeholders could not articulate verbally but can recognize when they see a concrete representation

C) Prototyping replaces the need for interviews and workshops on projects with visually complex requirements

D) Prototyping eliminates the need for the "Confirm Elicitation Results" step because stakeholders react in real time

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Prototypes are typically low-fidelity (wireframes, mockups) and do not require a working system; the cost concern misrepresents the technique.
- Why C is incorrect: Prototyping supplements other techniques; it does not replace interviews or workshops.
- Why D is incorrect: A prototype review is itself a form of confirmation; BABOK still requires confirming that the feedback captured from the prototype review is accurate before it drives requirements.
- Why B is correct: Prototyping's primary value is making abstract requirements concrete so stakeholders can react to them. The stakeholder's immediate correction illustrates that they could not have articulated the weekly-vs-daily distinction in a verbal interview but recognized it instantly when shown the wrong version.

---

## Question 18

Which of the following describes the key difference between "Elicit Requirements" and "Confirm Elicitation Results" in BABOK KA 4?

A) Eliciting is performed by the BA; confirming is performed by the project manager

B) Eliciting gathers raw information from stakeholders; confirming verifies with stakeholders that the captured information accurately reflects what they communicated

C) Eliciting is a one-time activity; confirming is a recurring activity performed at each sprint review

D) Eliciting is optional when documentation already exists; confirming is always mandatory

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Both activities are BA responsibilities; the project manager does not perform either.
- Why C is incorrect: BABOK does not characterize eliciting as a one-time activity; both tasks recur as needed throughout the project.
- Why D is incorrect: Eliciting is never optional simply because documentation exists; existing documents must be verified through stakeholder engagement to confirm they reflect current reality.
- Why B is correct: The distinction is straightforward: Elicit gathers the raw information; Confirm verifies accuracy. Confirmation is the step that converts raw elicitation notes into trusted information that can drive requirements analysis.

---

## Question 19

A BA is eliciting requirements for a new expense reimbursement system. During an interview, a finance manager says: "Every expense report needs manager approval before payment." The BA documents this as a requirement. What type of requirement is this?

A) Non-functional requirement — it describes a performance characteristic

B) Business rule — it defines an organizational policy that governs a business decision

C) System constraint — it limits the technical architecture options

D) Assumption — it has not been confirmed by the project sponsor

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Non-functional requirements describe quality attributes such as performance, security, and availability; an approval workflow is a business behavior, not a quality characteristic.
- Why C is incorrect: A system constraint limits design choices (e.g., "the system must run on the existing Oracle database"); a manager-approval rule is an organizational policy, not a technical constraint.
- Why D is incorrect: A confirmed statement from a finance manager is not an assumption; it is a stakeholder-provided requirement that must be documented and validated.
- Why B is correct: A business rule is an organizational policy that governs how decisions are made or actions are taken. "All expense reports require manager approval before payment" is a textbook business rule — it defines a condition that the system must enforce.

---

## Question 20

According to BABOK KA 4, which of the following is the most important factor a BA should consider when selecting an elicitation technique for a specific situation?

A) The technique the BA is most personally comfortable using

B) The technique that requires the least preparation time before the session

C) The type of information needed, the characteristics of the available stakeholders, and the constraints of the project context

D) The technique most commonly listed in the organization's software development methodology documentation

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Personal comfort is not a criterion for technique selection; the BA's role is to serve stakeholder and project needs, not personal preferences.
- Why B is incorrect: Minimizing preparation time is a cost consideration, not a selection criterion for technique appropriateness; poor preparation leads to poor elicitation quality.
- Why D is incorrect: Organizational methodology documentation may recommend common techniques, but the BA must exercise judgment about fitness for each specific situation.
- Why C is correct: BABOK explicitly states that technique selection should be based on: the type of information being sought, the characteristics of stakeholders (availability, location, number, communication style), and project constraints (budget, timeline, regulatory requirements). No single technique is universally best.
