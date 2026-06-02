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
